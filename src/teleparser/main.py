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
from fastcore.basics import partialler

from tqdm.auto import tqdm
from rich import print
from teleparser.decoders.ericsson import (
    ericsson_voz_decoder,
    ericsson_voz_decoder_optimized,
    ericsson_volte_decoder,
)
from teleparser.buffer import BufferManager


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
    "ericsson_volte": ericsson_volte_decoder,
}


MAPPING_TYPES = {
    "chargeableDuration": partialler(lambda x: pd.to_timedelta(x)),
    "dateForStartOfCharge": partialler(lambda x: pd.to_datetime(x, format="%d-%m-%y")),
    "interruptionTime": partialler(lambda x: pd.to_timedelta(x)),
    "timeForStartOfCharge": partialler(lambda x: pd.to_datetime(x, format="%H:%M:%S")),
    "timeForStopOfCharge": partialler(lambda x: pd.to_datetime(x, format="%H:%M:%S")),
    "timeForTCSeizureCalled": partialler(
        lambda x: pd.to_datetime(x, format="%H:%M:%S")
    ),
    "timeForTCSeizureCalling": partialler(
        lambda x: pd.to_datetime(x, format="%H:%M:%S")
    ),
    "timeForEvent": partialler(lambda x: pd.to_datetime(x, format="%H:%M:%S")),
    "recordSequenceNumber": partialler(pd.to_numeric, downcast="unsigned"),
    "calledSubscriberIMSI.msin": partialler(pd.to_numeric, downcast="unsigned"),
    "firstCalledLocationInformation.lac": partialler(
        pd.to_numeric, downcast="unsigned"
    ),
    "firstCalledLocationInformation.ci_sac": partialler(
        pd.to_numeric, downcast="unsigned"
    ),
    "calledSubscriberIMEI.TAC": partialler(pd.to_numeric, downcast="unsigned"),
    "internalCauseAndLoc.location": partialler(pd.to_numeric, downcast="unsigned"),
    "internalCauseAndLoc.cause": partialler(pd.to_numeric, downcast="unsigned"),
    "faultCode": partialler(pd.to_numeric, downcast="unsigned"),
    "lastCalledLocationInformation.lac": partialler(pd.to_numeric, downcast="unsigned"),
    "lastCalledLocationInformation.ci_sac": partialler(
        pd.to_numeric, downcast="unsigned"
    ),
    "callingPartyNumber.digits": partialler(pd.to_numeric, downcast="integer"),
    "relatedCallNumber": partialler(pd.to_numeric, downcast="unsigned"),
    "callIdentificationNumber": partialler(pd.to_numeric, downcast="unsigned"),
    "originalCalledNumber.digits": partialler(pd.to_numeric, downcast="integer"),
    "redirectingNumber.digits": partialler(pd.to_numeric, downcast="integer"),
    "firstCallingLocationInformation.lac": partialler(
        pd.to_numeric, downcast="unsigned"
    ),
    "firstCallingLocationInformation.ci_sac": partialler(
        pd.to_numeric, downcast="unsigned"
    ),
    "callingSubscriberIMEI.TAC": partialler(pd.to_numeric, downcast="unsigned"),
    "serviceKey": partialler(pd.to_numeric, downcast="integer"),
    "translatedNumber.digits": partialler(pd.to_numeric, downcast="integer"),
    "chargeNumber.digits": partialler(pd.to_numeric, downcast="integer"),
    "lastCallingLocationInformation.lac": partialler(
        pd.to_numeric, downcast="unsigned"
    ),
    "lastCallingLocationInformation.ci_sac": partialler(
        pd.to_numeric, downcast="unsigned"
    ),
    "sCPAddress.globalTitleAndSubSystemNumber.digits": partialler(
        pd.to_numeric, downcast="integer"
    ),
    "speechCoderPreferenceList": partialler(pd.to_numeric, downcast="unsigned"),
    "originatingLocationNumber.digits": partialler(pd.to_numeric, downcast="integer"),
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
                if not (self.output_path / f"{f.stem}.parquet").is_file()
            ]

        # Sort by size for better load balancing in parallel processing
        gz_files.sort(key=lambda x: x.stat().st_size)

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
    def _save_parquet(df: pd.DataFrame, output_file: Path):
        try:
            df.to_parquet(output_file, index=False, compression="snappy")
            logger.info(f"Data saved to {output_file} successfully")
        except Exception as e:
            logger.error(f"Failed to save data to {output_file}: {e}", exc_info=True)
            raise

    @staticmethod
    def format_df(
        blocks: list, transform_func: Callable | None = None, format_types: bool = False
    ):
        df = pd.DataFrame(blocks, copy=False, dtype="object")
        if transform_func is not None:
            df = transform_func(df)
        # Use a try-finally block to ensure resources are released
        try:
            if format_types:
                for col, func in MAPPING_TYPES.items():
                    if col in df.columns:
                        try:
                            df[col] = func(df[col])
                        except Exception as e:
                            logger.warning(
                                f"Failed to convert column {col} with custom function: {e}. Setting to category",
                                exc_info=False,
                            )

            return df.astype("string", copy=False).astype("category", copy=False)
        finally:
            # Explicitly clean up resources
            del blocks
            gc.collect()

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
        decoder = decoder(buffer_manager)

        try:
            blocks = decoder.process(pbar_position=pbar_position, show_progress=show_progress)
            if (counter := len(blocks)) == 0:
                logger.warning(f"No records found in {file_path}")
                return {
                    "file": file_path,
                    "records": 0,
                    "status": "success",
                    "dataframe": None,
                }
            df = CDRFileManager.format_df(blocks, transform_func=decoder.transform_func)

            # Only save to disk if output_path is provided
            if output_path is not None:
                output_file = output_path / f"{file_path.stem}.parquet"
                CDRFileManager._save_parquet(df, output_file)

            return {
                "file": file_path,
                "records": counter,
                "status": "success",
                "dataframe": df,
            }

        except Exception as e:
            error_details = traceback.format_exc()
            logger.error(f"Failed to process {file_path}: {e}\n{error_details}")

            return {
                "file": file_path,
                "error": str(e),
                "traceback": error_details,
                "status": "failed",
                "dataframe": None,
            }

        finally:
            buffer_manager.close()

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
            colour="green"
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
                            "dataframe": None,
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

    # Also print for user-friendly output
    print("\n[bold cyan]Processing Summary:[/bold cyan]")
    print(f"[green]Files processed successfully: {success_count}[/green]")
    print(f"[red]Files failed: {failed_count}[/red]")
    print(f"[yellow]Total records processed: {total_records}[/yellow]")

    if output_path is not None:
        print(f"[magenta]Output directory: {output_path}[/magenta]")
    else:
        print(
            "[magenta]No output directory - results returned in memory only[/magenta]"
        )

    print(f"[green]Total Time: {total_time:.2f} seconds[/green]")
    print("[blue]Cleaning up temporary files now, if present...[/blue]")


def main(
    input_path: Path,
    output_path: Path | None = None,
    cdr_type: str = "ericsson_voz",
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
