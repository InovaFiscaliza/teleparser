import argparse
import concurrent.futures
import csv
import gc
import gzip as gzip_module
import logging
import os
import shutil
import sys
import traceback
import zipfile
from concurrent.futures import ProcessPoolExecutor
from contextlib import suppress
from datetime import datetime, timezone
from functools import cached_property
from pathlib import Path
from time import perf_counter
from typing import Any, Dict, List, Set

from tqdm.auto import tqdm
from teleparser.buffer import BufferManager
from teleparser.decoders.ericsson import (
    ericsson_volte_decoder,
    ericsson_volte_decoder_optimized,
    ericsson_voz_decoder,
    ericsson_voz_decoder_optimized,
    ericsson_voz_decoder_two_phase,
)

# Initialize a placeholder logger - will be properly configured later
logger = logging.getLogger("teleparser")


# Configure logging
def setup_logging(output_path: Path | None, log_level: int = logging.INFO):
    """Set up logging to both file and console

    If output_path is None, logs are saved to ~/.local/share/teleparser/logs/
    following XDG Base Directory specification.
    """
    # Determine logs directory
    if output_path is None:
        # Use XDG Base Directory for application logs
        xdg_data_home = Path.home() / ".local" / "share"
        logs_dir = xdg_data_home / "teleparser" / "logs"
    else:
        logs_dir = output_path / "logs"

    logs_dir.mkdir(parents=True, exist_ok=True)

    # Create a timestamped log file name
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    log_file = logs_dir / f"teleparser_{timestamp}.log"

    # Configure root logger
    logger = logging.getLogger("teleparser")
    logger.setLevel(log_level)

    # Clear any existing handlers
    if logger.handlers:
        logger.handlers.clear()

    # File handler - detailed format with timestamps
    file_handler = logging.FileHandler(log_file)
    file_format = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    file_handler.setFormatter(file_format)
    file_handler.setLevel(log_level)

    # Add handlers to logger
    logger.addHandler(file_handler)

    return logger


DECODERS = {
    "ericsson_voz": ericsson_voz_decoder,
    "ericsson_voz_optimized": ericsson_voz_decoder_optimized,
    "ericsson_voz_two_phase": ericsson_voz_decoder_two_phase,
    "ericsson_volte": ericsson_volte_decoder,
    "ericsson_volte_optimized": ericsson_volte_decoder_optimized,
}


class CDRFileManager:
    def __init__(
        self,
        input_path: Path,
        output_path: Path | None,
        cdr_type: str,
        reprocess: bool,
        max_count: int | None = None,
    ):
        self.input_path = Path(input_path)
        self.output_path = Path(output_path) if output_path is not None else None
        self.cdr_type = cdr_type
        self.reprocess = reprocess
        self.max_count = max_count
        self.processed_files: Set[Path] = set()
        self.failed_files: Set[Path] = set()
        self.temp_dir: Path | None = None
        self.setup()

    def setup(self):
        """Create necessary output directories and validate input parameters"""
        if self.cdr_type not in DECODERS:
            logger.error(f"Decoder invalid or not implemented for {self.cdr_type}")
            raise NotImplementedError(
                f"Decoder invalid or not implemented for {self.cdr_type}"
            )
        self.decoder = DECODERS[self.cdr_type]

        if self.output_path is not None:
            output_dir = self.output_path
            output_dir.mkdir(parents=True, exist_ok=True)
            self.output_path = output_dir
            logger.info(f"Output directory created: {output_dir}")
        else:
            logger.info(
                "No output directory specified - results will not be saved to disk"
            )

    @cached_property
    def gz_files(self) -> List[Path]:
        """It traverses the tree to get the list of .gz files, decompressing ZIP archives if needed"""
        if self.input_path.is_file():
            files = [self.input_path]
        elif self.input_path.is_dir():
            files = list(self.input_path.rglob("*[.gz|.zip]"))
        else:
            logger.error(f"Invalid input path: {self.input_path}")
            raise ValueError(f"Invalid input path: {self.input_path}")
        zip_files = [f for f in files if f.suffix == ".zip"]
        gz_files = [f for f in files if f.suffix == ".gz"]
        if zip_files:
            logger.info(f"Found {len(zip_files)} ZIP files to extract")
            gz_files.extend(self.decompress_zips(zip_files))

        # Only skip already processed files if output_path is set and reprocess is False
        if not self.reprocess and self.output_path is not None:
            gz_files = [
                f
                for f in gz_files
                if not (
                    (self.output_path / f"{f.stem}.csv.gz").is_file()
                    or (self.output_path / f"{f.stem}.parquet").is_file()
                )
            ]

        # Warn if .parquet files exist in output directory (migration notice)
        if self.output_path is not None:
            parquet_files = list(self.output_path.glob("*.parquet"))
            if parquet_files:
                logger.warning(
                    f"Found {len(parquet_files)} .parquet files in output directory. "
                    "These will not be processed. Consider migrating or cleaning up old .parquet files."
                )

        # Sort by size for better load balancing in parallel processing
        gz_files.sort(key=lambda x: x.stat().st_size, reverse=True)

        # Limit to max_count files if specified
        if self.max_count is not None and self.max_count > 0:
            original_count = len(gz_files)
            gz_files = gz_files[: self.max_count]
            logger.info(
                f"Limited to {len(gz_files)} files (max_count={self.max_count}, found {original_count})"
            )

        logger.info(f"Found {len(gz_files)} GZ files to process")
        return gz_files

    def decompress_zips(self, zip_files: List[Path]) -> List[Path]:
        """Extract ZIP files and return paths to extracted files"""
        # Use output_path if available, otherwise use system temp directory
        if self.output_path is not None:
            self.temp_dir = self.output_path / "temp_extracted"
        else:
            import tempfile

            self.temp_dir = Path(tempfile.gettempdir()) / "teleparser_temp_extracted"

        self.temp_dir.mkdir(parents=True, exist_ok=True)
        logger.info(f"Created temporary directory for ZIP extraction: {self.temp_dir}")

        gz_files: List[Path] = []
        for zip_file in tqdm(zip_files, desc="Extracting ZIP files", unit="zip"):
            try:
                with zipfile.ZipFile(zip_file) as zf:
                    zf.extractall(self.temp_dir)
                    extracted = [
                        self.temp_dir / file
                        for file in zf.namelist()
                        if file.endswith(".gz")
                    ]
                    gz_files.extend(extracted)
                    logger.info(f"Extracted {len(extracted)} GZ files from {zip_file}")
            except zipfile.BadZipFile:
                logger.error(
                    f"Failed to extract {zip_file}: Bad ZIP file", exc_info=True
                )
                self.failed_files.add(Path(zip_file))
        return gz_files

    def cleanup(self):
        """Clean up temporary files and directories"""
        if self.temp_dir is not None and self.temp_dir.exists():
            logger.info(f"Cleaning up temporary directory: {self.temp_dir}")
            shutil.rmtree(self.temp_dir)

    @staticmethod
    def _save(
        blocks: List[Dict[str, Any]],
        output_file: Path,
        fieldnames_set: Set[str] | None = None,
    ):
        """Save blocks to a gzipped CSV file.

        Args:
            blocks: List of dictionaries containing CDR data
            output_file: Path to the output CSV.GZ file
        """
        try:
            if not blocks:
                logger.warning(f"No data to save for {output_file}")
                return

            # Collect fieldnames if not provided or empty
            if fieldnames_set is None:
                fieldnames_set = set()

            # Collect fieldnames during initial processing to avoid double iteration
            if not fieldnames_set:
                fieldnames_set = set()
                for block in blocks:
                    fieldnames_set.update(block.keys())
            else:
                for block in blocks:
                    fieldnames_set.update(block.keys())

            # Sort fieldnames for consistent output
            fieldnames = sorted(fieldnames_set)

            # Write to gzipped CSV
            with gzip_module.open(output_file, "wt", encoding="utf-8", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(blocks)

            logger.info(f"Data saved to {output_file} successfully")
        except Exception as e:
            logger.error(f"Failed to save data to {output_file}: {e}", exc_info=True)
            raise

    @staticmethod
    def decode_file(
        file_path: Path,
        decoder,
        output_path: Path | None = None,
        pbar_position: int | None = None,
        show_progress: bool = True,
    ):
        blocks = []
        buffer_manager = BufferManager(file_path)
        decoder_instance = decoder(buffer_manager)

        try:
            blocks = decoder_instance.process(
                pbar_position=pbar_position, show_progress=show_progress
            )
            if (counter := len(blocks)) == 0:
                logger.warning(f"No records found in {file_path}")
                return {
                    "file": file_path,
                    "records": 0,
                    "status": "success",
                    "blocks": None,
                }

            # Apply transform function if provided
            if (
                hasattr(decoder_instance, "transform_func")
                and decoder_instance.transform_func is not None
            ):
                try:
                    blocks = decoder_instance.transform_func(blocks)
                    logger.debug(f"Applied transform function for {file_path}")
                except Exception as e:
                    logger.warning(
                        f"Failed to apply transform function for {file_path}: {e}"
                    )
                    # Continue without transformation

            # Get fieldnames from decoder if available
            fieldnames_set = None
            if hasattr(decoder_instance, "FIELDNAMES"):
                fieldnames_set = decoder_instance.FIELDNAMES
            elif hasattr(decoder_instance, "fieldnames"):
                fieldnames_set = decoder_instance.fieldnames

            # Save to disk if output_path is provided
            if output_path is not None:
                output_file = output_path / f"{file_path.stem}.csv.gz"
                CDRFileManager._save(blocks, output_file, fieldnames_set)

            return {
                "file": file_path,
                "records": counter,
                "status": "success",
                "fieldnames": fieldnames_set,
                "blocks": blocks
                if output_path is None
                else None,  # Return blocks for in-memory processing
            }

        except Exception as e:
            error_details = traceback.format_exc()
            logger.error(f"Failed to process {file_path}: {e}\n{error_details}")

            return {
                "file": file_path,
                "error": str(e),
                "traceback": error_details,
                "status": "failed",
                "blocks": None,
            }

        finally:
            buffer_manager.close()
            # Clean up blocks to free memory
            if blocks:
                del blocks
            gc.collect()

    def decode_files_sequential(self):
        """Decode all files sequentially with hierarchical progress bars and return results"""
        results = []
        logger.info(f"Starting sequential processing of {len(self.gz_files)} files")

        # Master progress bar for files (position 0)
        with tqdm(
            total=len(self.gz_files),
            desc="📂 Processing files",
            unit="file",
            position=0,
            leave=True,
            colour="green",
        ) as pbar_files:
            for file_path in self.gz_files:
                # Update master bar with current file name
                pbar_files.set_postfix_str(f"{file_path.name}", refresh=True)

                try:
                    result = self.decode_file(
                        file_path=file_path,
                        decoder=self.decoder,
                        output_path=self.output_path,
                        pbar_position=1,  # Nested progress bar at position 1
                        show_progress=True,
                    )
                    self.processed_files.add(file_path)
                    results.append(result)

                    if result["status"] == "success":
                        logger.info(
                            f"Successfully processed {file_path}: {result.get('records', 0)} records"
                        )
                    else:
                        logger.error(
                            f"Failed to process {file_path}: {result.get('error', 'Unknown error')}"
                        )
                except Exception as e:
                    error_details = traceback.format_exc()
                    logger.error(
                        f"Exception while processing {file_path}: {str(e)}\n{error_details}"
                    )
                    self.failed_files.add(file_path)
                    results.append(
                        {
                            "file": file_path,
                            "error": str(e),
                            "traceback": error_details,
                            "status": "failed",
                        }
                    )
                finally:
                    # Update master progress bar
                    pbar_files.update(1)

        return results

    def decode_files_parallel(self, workers: int):
        """Decode files using parallel processing with multiple CPU cores"""
        cpu_count = os.cpu_count() or 1
        max_workers = max(1, min(workers, cpu_count, len(self.gz_files)))
        logger.info(
            f"Starting parallel processing with {max_workers} workers for {len(self.gz_files)} files"
        )
        results = []
        with ProcessPoolExecutor(max_workers=max_workers) as executor:
            future_to_file = {
                executor.submit(
                    CDRFileManager.decode_file,
                    file_path,
                    self.decoder,
                    self.output_path,
                    None,  # pbar_position: not used in parallel mode
                    False,  # show_progress: disabled in parallel to avoid overlap
                ): file_path
                for file_path in self.gz_files
            }
            for future in tqdm(
                concurrent.futures.as_completed(future_to_file),
                total=len(future_to_file),
                desc="🔄 Processing files (parallel)",
                unit="file",
                colour="green",
            ):
                file_path = future_to_file[future]
                try:
                    result = future.result()
                    if "records" in result:
                        logger.info(
                            f"Successfully processed {file_path}: {result['records']} records"
                        )
                    else:
                        logger.error(
                            f"Failed to process {file_path}: {result.get('error', 'Unknown error')}"
                        )
                    if "traceback" in result:
                        logger.debug(
                            f"Traceback for {file_path}:\n{result['traceback']}"
                        )
                    results.append(result)
                except Exception as exc:
                    error_details = traceback.format_exc()
                    logger.error(
                        f"Exception processing result for {file_path}: {str(exc)}\n{error_details}"
                    )
                    results.append(
                        {
                            "file": file_path,
                            "error": str(exc),
                            "traceback": error_details,
                            "status": "failed",
                            "blocks": None,
                        }
                    )
                gc.collect()
        return results


def display_summary(results, total_time, output_path):
    success_count = sum(r.get("status") == "success" for r in results)
    failed_count = sum(r.get("status") == "failed" for r in results)
    total_records = sum(r.get("records", 0) for r in results)

    # Log summary information
    logger.info("Processing Summary:")
    logger.info(f"Files processed successfully: {success_count}")
    logger.info(f"Files failed: {failed_count}")
    logger.info(f"Total records processed: {total_records}")

    if output_path is not None:
        logger.info(f"Output directory: {output_path}")
    else:
        logger.info("No output directory - results returned in memory only")

    logger.info(f"Total Time: {total_time:.2f} seconds")
    logger.info("Cleaning up temporary files now, if present...")

    # Also print for user-friendly output (no color formatting)
    print("\n==================== 📊 Processing Summary ====================")
    print(f"✅ Files processed successfully: {success_count}")
    print(f"❌ Files failed: {failed_count}")
    print(f"📄 Total records processed: {total_records}")

    if output_path is not None:
    cdr_type: str = "ericsson_voz",
    else:
        print("📦 No output directory - results returned in memory only")

    print(f"⏱️ Total Time: {total_time:.2f} seconds")
    print("🧹 Cleaning up temporary files now, if present...")
    print("===============================================================")


def main(
    input_path: Path,
    output_path: Path | None = None,
    cdr_type: str = "ericsson_voz_optimized",
    workers: int = os.cpu_count() // 2,
    reprocess: bool = True,
    log_level: int = logging.INFO,
    max_count: int | None = None,
):
    # Set up logging to file and console
    global logger
    logger = setup_logging(output_path, log_level)

    logger.info(
        f"Starting teleparser with input: {input_path}, output: {output_path}, type: {cdr_type}, workers: {workers}, reprocess: {reprocess}, max_count: {max_count}"
    )
    try:
        manager = CDRFileManager(
            input_path, output_path, cdr_type, reprocess, max_count
        )
        file_count = len(manager.gz_files)
        logger.info(f"[blue]Started processing of {file_count} files...[/blue]")

        start = perf_counter()
        if workers <= 1 or file_count == 1:
            logger.info("Using single-core processing mode")
            results = manager.decode_files_sequential()
        else:
            logger.info("Using multi-core processing mode")
            results = manager.decode_files_parallel(workers)

        total_time = perf_counter() - start
        logger.info(f"Processing completed in {total_time:.2f} seconds")

        display_summary(results, total_time, manager.output_path)
        manager.cleanup()

        if failed_files := [r for r in results if r.get("status") == "failed"]:
            logger.warning(
                f"Detailed information for {len(failed_files)} failed files:"
            )
            for failed in failed_files:
                logger.error(
                    f"Failed file: {failed.get('file')}, Error: {failed.get('error')}"
                )
                if "traceback" in failed:
                    logger.debug(f"Traceback:\n{failed['traceback']}")

        return results

    except Exception as e:
        error_details = traceback.format_exc()
        logger.critical(f"Critical error in main process: {str(e)}\n{error_details}")
        print(f"[bold red]Critical error: {str(e)}[/bold red]")
        raise


def cli():
    """Command-line interface entry point using argparse."""
    parser = argparse.ArgumentParser(
        prog="teleparser",
        description="Processa arquivos CDR da ENTRADA (arquivo/pasta) e opcionalmente salva resultados na pasta SAIDA em formato CSV.GZ.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
O formato esperado é um arquivo ou pasta com um ou mais arquivos gzip.
Se os arquivos gzip estiverem em um arquivo ZIP, eles serão extraídos primeiro.
O modo padrão é processamento paralelo utilizando múltiplos núcleos da CPU.
Se --saida não for especificado, os resultados são processados em memória e não salvos em disco.
        """,
    )

    parser.add_argument(
        "entrada",
        type=str,
        "-t",
        "--tipo",
        type=str,
        default="ericsson_voz",
        choices=list(DECODERS.keys()),
        help=f"Tipo de CDR para processar. Opções: {', '.join(DECODERS.keys())} (padrão: ericsson_voz)\nNota: O valor padrão foi restaurado para manter compatibilidade com versões anteriores.",
    )
        default=None,
        help="Caminho para o diretório de saída. Somente a tabela resultado é retornada caso None",
    )

    parser.add_argument(
        "-t",
        "--tipo",
        type=str,
        default="ericsson_voz_optimized",
        choices=list(DECODERS.keys()),
        help=f"Tipo de CDR para processar. Opções: {', '.join(DECODERS.keys())} (padrão: ericsson_voz_optimized)",
    )

    parser.add_argument(
        "-n",
        "--nucleos",
        type=int,
        default=os.cpu_count() // 2 if os.cpu_count() else 1,
        help=f"Número de núcleos para processamento paralelo, máximo é o número de núcleos da CPU - 1 (padrão: {os.cpu_count() // 2 if os.cpu_count() else 1})",
    )

    parser.add_argument(
        "-r",
        "--reprocessar",
        action="store_true",
        default=True,
        help="Reprocessar arquivos existentes (padrão: True)",
    )

    parser.add_argument(
        "--log",
        type=str,
        default="INFO",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        help="Nível de log (padrão: INFO)",
    )

    parser.add_argument(
        "-m",
        "--max-arquivos",
        type=int,
        default=None,
        help="Número máximo de arquivos para processar. Padrão: None (processar todos)",
    )

    args = parser.parse_args()

    # Convert entrada to Path
    entrada_path = Path(args.entrada)

    # Convert saída to Path if provided
    output_dir = Path(args.saida) if args.saida is not None else None

    # Set log level based on command line argument
    numeric_level = getattr(logging, args.log.upper(), None)
    if not isinstance(numeric_level, int):
        print(f"Nível de log inválido: {args.log}")
        numeric_level = logging.INFO

    try:
        _ = main(
            entrada_path,
            output_dir,
            args.tipo,
            args.nucleos,
            args.reprocessar,
            numeric_level,
            args.max_arquivos,
        )
    except Exception as e:
        # At this point, logger might not be initialized yet, so we print to console
        error_details = traceback.format_exc()
        print(f"Fatal Error: {str(e)}")

        # Try to log to file if possible
        with suppress(Exception):
            temp_logger = setup_logging(output_dir, logging.ERROR)
            temp_logger.critical(
                f"Exception untreated in main process: {str(e)}\n{error_details}"
            )
        sys.exit(1)


if __name__ == "__main__":
    import multiprocessing

    multiprocessing.freeze_support()
    cli()
