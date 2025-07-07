import gc
import os
import shutil
import zipfile
import concurrent.futures
import logging
import traceback
from concurrent.futures import ProcessPoolExecutor
from datetime import datetime, timezone
from functools import cached_property
from pathlib import Path
from typing import Callable, List, Set
from time import perf_counter
import pandas as pd

from tqdm.auto import tqdm
from rich import print
from teleparser.decoders.ericsson import ericsson_voz_decoder, ericsson_volte_decoder
from teleparser.buffer import BufferManager


# Configure logging
def setup_logging(output_path: Path, log_level: int = logging.INFO):
    """Set up logging to both file and console"""
    # Create logs directory if it doesn't exist
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

    # # Console handler - using Rich for better formatting
    # console_handler = RichHandler(rich_tracebacks=True)
    # console_handler.setLevel(log_level)

    # Add handlers to logger
    logger.addHandler(file_handler)
    # logger.addHandler(console_handler)

    # logger.info(f"Logging initialized. Log file: {log_file}")
    return logger


# Initialize a placeholder logger - will be properly configured later
logger = logging.getLogger("teleparser")

DECODERS = {
    "ericsson_voz": ericsson_voz_decoder,
    "ericsson_volte": ericsson_volte_decoder,
}


class CDRFileManager:
    def __init__(self, input_path: Path, output_path: Path, cdr_type: str):
        self.input_path = Path(input_path)
        self.output_path = Path(output_path)
        self.cdr_type = cdr_type
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
        output_dir = self.output_path
        output_dir.mkdir(parents=True, exist_ok=True)
        self.output_path = output_dir
        logger.info(f"Output directory created: {output_dir}")

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
        gz_files = [
            f
            for f in gz_files
            if not (self.output_path / f"{f.stem}.parquet").is_file()
        ]
        logger.info(f"Found {len(gz_files)} GZ files to process")
        gz_files.sort(key=lambda x: x.stat().st_size)
        return gz_files

    def decompress_zips(self, zip_files: List[Path]) -> List[Path]:
        """Extract ZIP files and return paths to extracted files"""
        self.temp_dir = self.output_path / "temp_extracted"
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
    def _save_data(
        blocks: list, output_file: Path, transform_func: Callable | None = None
    ):
        df = pd.DataFrame(blocks, copy=False)
        if transform_func is not None:
            df = transform_func(df)
        # Use a try-finally block to ensure resources are released
        try:
            df.astype("string", copy=False).astype("category", copy=False).to_parquet(
                output_file, index=False, compression="snappy"
            )
            logger.info(f"Data saved to {output_file} successfully")
        except Exception as e:
            logger.error(f"Failed to save data to {output_file}: {e}", exc_info=True)
            raise
        finally:
            # Explicitly clean up resources
            del blocks
            gc.collect()

    @staticmethod
    def decode_file(
        file_path: Path,
        decoder,
        output_path: Path,
    ):
        blocks = []
        buffer_manager = BufferManager(file_path)
        decoder = decoder(buffer_manager)

        try:
            blocks = decoder.process()
            counter = len(blocks)
            # Save the processed data
            output_file = output_path / f"{file_path.stem}.parquet"
            CDRFileManager._save_data(
                blocks, output_file, transform_func=decoder.transform_func
            )

            return {"file": file_path, "records": counter, "status": "success"}

        except Exception as e:
            error_details = traceback.format_exc()
            logger.error(f"Failed to process {file_path}: {e}\n{error_details}")

            return {
                "file": file_path,
                "error": str(e),
                "traceback": error_details,
                "status": "failed",
            }

        finally:
            buffer_manager.close()

    def decode_files_sequential(self):
        """Decode all files sequentially with a progress bar and return results"""
        results = []
        logger.info(f"Starting sequential processing of {len(self.gz_files)} files")
        for file_path in tqdm(self.gz_files, desc="Decoding CDR files", unit="file"):
            try:
                logger.info(f"Processing file: {file_path}")
                result = self.decode_file(
                    file_path=file_path,
                    decoder=self.decoder,
                    output_path=self.output_path,
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
        return results

    @staticmethod
    def process_single_file(file_path, decoder, output_path):
        """Process a single file in a worker process"""
        try:
            logger.info(f"Processing file in worker: {file_path}")
            result = CDRFileManager.decode_file(
                file_path=file_path,
                decoder=decoder,
                output_path=output_path,
            )
            return {"file_path": file_path, "result": result}

        except Exception as e:
            error_details = traceback.format_exc()
            logger.error(
                f"Exception in worker processing {file_path}: {str(e)}\n{error_details}"
            )
            return {
                "file_path": file_path,
                "error": str(e),
                "traceback": error_details,
                "status": "failed",
            }

    def decode_files_parallel(self, workers: int):
        """Decode files using parallel processing with multiple CPU cores"""
        cpu_count = os.cpu_count() or 1
        max_workers = min(workers, cpu_count, len(self.gz_files))
        logger.info(
            f"Starting parallel processing with {max_workers} workers for {len(self.gz_files)} files"
        )
        results = []
        with ProcessPoolExecutor(max_workers=max_workers) as executor:
            future_to_file = {
                executor.submit(
                    CDRFileManager.process_single_file,
                    file_path,
                    self.decoder,
                    self.output_path,
                ): file_path
                for file_path in self.gz_files
            }
            for future in tqdm(
                concurrent.futures.as_completed(future_to_file),
                total=len(future_to_file),
                desc="Decoding CDR files (parallel)",
                unit="file",
            ):
                file_path = future_to_file[future]
                try:
                    logger.info(f"Processing result for file: {file_path}")
                    data = future.result()
                    result = data.get("result", {})
                    if "records" in result:
                        logger.info(
                            f"Successfully processed {file_path}: {result['records']} records"
                        )
                    else:
                        logger.error(
                            f"Failed to process {file_path}: {data.get('error', 'Unknown error')}"
                        )
                    if "traceback" in data:
                        logger.debug(f"Traceback for {file_path}:\n{data['traceback']}")
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
    logger.info(f"Output directory: {output_path}")
    logger.info(f"Total Time: {total_time:.2f} seconds")
    logger.info("Cleaning up temporary files now, if present...")

    # Also print for user-friendly output
    print("\n[bold cyan]Processing Summary:[/bold cyan]")
    print(f"[green]Files processed successfully: {success_count}[/green]")
    print(f"[red]Files failed: {failed_count}[/red]")
    print(f"[yellow]Total records processed: {total_records}[/yellow]")
    print(f"[magenta]Output directory: {output_path}[/magenta]")
    print(f"[green]Total Time: {total_time:.2f} seconds[/green]")
    print("[blue]Cleaning up temporary files now, if present...[/blue]")


def main(
    input_path: Path,
    output_path: Path,
    cdr_type: str,
    workers: int,
    log_level: int = logging.INFO,
):
    # Set up logging to file and console
    global logger
    logger = setup_logging(output_path, log_level)

    logger.info(
        f"Starting teleparser with input: {input_path}, output: {output_path}, type: {cdr_type}, workers: {workers}"
    )
    try:
        manager = CDRFileManager(input_path, output_path, cdr_type)
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

    except Exception as e:
        error_details = traceback.format_exc()
        logger.critical(f"Critical error in main process: {str(e)}\n{error_details}")
        print(f"[bold red]Critical error: {str(e)}[/bold red]")
        raise
