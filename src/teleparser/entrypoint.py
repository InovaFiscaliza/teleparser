import asyncio
import gc
import gzip
import os
import shutil
import zipfile
import concurrent.futures
import logging
import traceback
from concurrent.futures import ProcessPoolExecutor
from contextlib import contextmanager
from datetime import datetime, timezone
from functools import cached_property
from pathlib import Path
from typing import BinaryIO, List, Optional, Set
from time import perf_counter


import pandas as pd
from contextlib import suppress
from rich.progress import (
    Progress,
    BarColumn,
    TaskProgressColumn,
    TextColumn,
    TimeRemainingColumn,
)
from rich import print
from teleparser.decoders.ericsson import ericsson_voz_decoder


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

ASYNC_CONCURRENCY = 8

DECODERS = {
    "ericsson_voz": ericsson_voz_decoder,
}


class BufferManager:
    """Manages CDR file reading and hex conversion"""

    def __init__(self, file_path: Path):
        self.file_path = file_path
        self.file_handle: Optional[BinaryIO] = None

    @contextmanager
    def open(self):
        with gzip.open(self.file_path, "rb") as self.file_handle:
            yield self

    def open_file(self):
        """Opens the gzip file directly"""
        self.file_handle = gzip.open(self.file_path, "rb")
        return self

    def close(self):
        """Closes the file handle if open"""
        if self.has_data():
            self.file_handle.close()

    def has_data(self) -> bool:
        return bool(self.file_handle and not self.file_handle.closed)

    def read(self, size) -> str:
        return self.file_handle.read(size)


class CDRFileManager:
    def __init__(self, input_path: Path, output_path: Path, cdr_type: str):
        self.input_path = Path(input_path)
        self.output_path = Path(output_path)
        self.cdr_type = cdr_type
        self.processed_files: Set[Path] = set()
        self.failed_files: Set[Path] = set()
        self.temp_dir: Path | None = None
        self.setup()

    def setup(self) -> Path:
        """Create necessary output directories and validate input parameters"""
        if self.cdr_type not in DECODERS:
            logger.error(f"Decoder invalid or not implemented for {self.cdr_type}")
            raise NotImplementedError(
                f"Decoder invalid or not implemented for {self.cdr_type}"
            )
        self.decoder = DECODERS[self.cdr_type]
        timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
        output_dir = self.output_path / f"{timestamp}"
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
        logger.info(f"Found {len(gz_files)} GZ files to process")
        return gz_files

    def decompress_zips(self, zip_files: List[Path]) -> List[Path]:
        """Extract ZIP files and return paths to extracted files"""
        self.temp_dir = self.output_path / "temp_extracted"
        self.temp_dir.mkdir(parents=True, exist_ok=True)
        logger.info(f"Created temporary directory for ZIP extraction: {self.temp_dir}")

        gz_files: List[Path] = []
        with self.create_progress_bar() as progress:
            task = progress.add_task(
                "[cyan]Extracting ZIP files...", total=len(zip_files)
            )
            for zip_file in zip_files:
                try:
                    with zipfile.ZipFile(zip_file) as zf:
                        zf.extractall(self.temp_dir)
                        extracted = [
                            self.temp_dir / file
                            for file in zf.namelist()
                            if file.endswith(".gz")
                        ]
                        gz_files.extend(extracted)
                        logger.info(
                            f"Extracted {len(extracted)} GZ files from {zip_file}"
                        )
                except zipfile.BadZipFile:
                    logger.error(
                        f"Failed to extract {zip_file}: Bad ZIP file", exc_info=True
                    )
                    self.failed_files.add(Path(zip_file))
                progress.update(task, advance=1)
        return gz_files

    def cleanup(self):
        """Clean up temporary files and directories"""
        if self.temp_dir is not None and self.temp_dir.exists():
            logger.info(f"Cleaning up temporary directory: {self.temp_dir}")
            shutil.rmtree(self.temp_dir)

    @staticmethod
    def create_progress_bar():
        """Create a progress bar for decoding files"""
        return Progress(
            TextColumn("[bold blue]{task.description}"),
            BarColumn(),
            TaskProgressColumn(),
            TimeRemainingColumn(),
            expand=False,
            transient=False,  # Keep completed tasks visible
        )

    @staticmethod
    def _save_data(blocks: list, output_file: Path):
        # Use a try-finally block to ensure resources are released
        try:
            pd.DataFrame(
                blocks,
                copy=False,
                dtype="string",  # Convert to string first to avoid casting issues with pyarrow
            ).astype("category").to_parquet(
                output_file,
                index=False,
                compression="gzip",
            )
        finally:
            # Explicitly clean up resources
            del blocks
            gc.collect()

    @staticmethod
    def decode_file(
        file_path: Path,
        decoder,
        output_path: Path,
        progress: Progress = None,
        task=None,
    ):
        blocks = []
        buffer_manager = BufferManager(file_path)
        decoder = decoder()
        counter = 0

        # Create a local progress bar only if not provided
        local_progress = None
        if progress is None:
            local_progress = CDRFileManager.create_progress_bar()
            progress = local_progress
            task = progress.add_task(f"[green]Processing: {file_path.name}", total=None)

        try:
            logger.info(f"Started processing file: {file_path}")
            with buffer_manager.open() as file_buffer:
                while (tlv := decoder.decode(file_buffer)) is not None:
                    record, _ = tlv
                    blocks.append(record)
                    counter += 1
                    if counter % 250 == 0:
                        progress.update(
                            task,
                            description=f"[green]Processing: [green]{file_path.name} [cyan]({counter} records)",
                        )
            # Save the processed data
            output_file = output_path / f"{file_path.stem}.parquet.gzip"
            logger.info(
                f"Completed processing {counter} records from , saving to {output_file}"
            )
            CDRFileManager._save_data(blocks, output_file)

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
            # Only close the progress if we created it locally
            if local_progress:
                local_progress.stop()
            # Ensure buffer is closed
            buffer_manager.close()

    def decode_files_sequential(self):
        """Decode all files sequentially with a progress bar and return results"""
        results = []
        logger.info(f"Starting sequential processing of {len(self.gz_files)} files")
        with CDRFileManager.create_progress_bar() as progress:
            # Main task for overall progress
            main_task = progress.add_task(
                "[cyan]Decoding CDR files...", total=len(self.gz_files)
            )

            file_tasks = {
                file_path: progress.add_task(
                    f"[green]Waiting: {file_path.name}", total=None, visible=False
                )
                for file_path in self.gz_files
            }
            for file_path in self.gz_files:
                try:
                    # Make this file's task visible when processing starts
                    progress.update(
                        file_tasks[file_path],
                        description=f"[green]Processing: {file_path.name}",
                        visible=True,
                    )
                    logger.info(f"Processing file: {file_path}")

                    # Process the file
                    result = self.decode_file(
                        file_path=file_path,
                        decoder=self.decoder,
                        output_path=self.output_path,
                        progress=progress,
                        task=file_tasks[file_path],
                    )

                    # Add to processed files
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
                    # Handle errors
                    error_details = traceback.format_exc()
                    logger.error(
                        f"Exception while processing {file_path}: {str(e)}\n{error_details}"
                    )
                    progress.update(
                        file_tasks[file_path],
                        description=f"[red]Failed: {file_path.name} [red]({str(e)})",
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
                    # Hide the completed file task to reduce clutter
                    progress.update(file_tasks[file_path], visible=False)
                    # Update main progress when a file is complete
                    progress.update(main_task, advance=1)

        return results

    async def decode_files_async(self):
        logger.info(f"Starting async processing of {len(self.gz_files)} files")
        # Create a single shared progress context for all tasks
        with CDRFileManager.create_progress_bar() as progress:
            # Main task for overall progress
            main_task = progress.add_task(
                "[cyan]Decoding CDR files...", total=len(self.gz_files)
            )

            # Create a dictionary to track individual file tasks
            file_tasks = {
                # Create a task for each file but don't show it yet (set visible=False)
                file_path: progress.add_task(
                    f"[green]Waiting: {file_path.name}", total=None, visible=False
                )
                for file_path in self.gz_files
            }

            # Define a wrapper function to handle progress updates
            async def process_file(file_path):
                # Make this file's task visible when processing starts
                progress.update(file_tasks[file_path], visible=True)
                logger.info(f"Starting async processing of file: {file_path}")

                try:
                    # Process the file
                    result = await asyncio.to_thread(
                        CDRFileManager.process_single_file,
                        file_path=file_path,
                        decoder=self.decoder,
                        output_path=self.output_path,
                        progress=progress,
                        task=file_tasks[file_path],
                    )

                    if result.get("result", {}).get("status") == "success":
                        logger.info(
                            f"Successfully processed {file_path} asynchronously"
                        )
                    else:
                        logger.error(
                            f"Failed to process {file_path} asynchronously: {result.get('error', 'Unknown error')}"
                        )

                    # Update main progress when a file is complete
                    progress.update(main_task, advance=1)

                    # Hide the completed file task to reduce clutter
                    progress.update(file_tasks[file_path], visible=False)

                    return result
                except Exception as e:
                    error_details = traceback.format_exc()
                    logger.error(
                        f"Exception in async processing of {file_path}: {str(e)}\n{error_details}"
                    )
                    progress.update(main_task, advance=1)
                    progress.update(file_tasks[file_path], visible=False)
                    return {
                        "file_path": file_path,
                        "error": str(e),
                        "traceback": error_details,
                        "status": "failed",
                    }

            # Process files with controlled concurrency
            results = []
            # Use a semaphore to limit concurrent tasks
            semaphore = asyncio.Semaphore(min(ASYNC_CONCURRENCY, len(self.gz_files)))

            async def bounded_process_file(file_path):
                async with semaphore:
                    return await process_file(file_path)

            # Execute all tasks and gather results
            results = await asyncio.gather(
                *[bounded_process_file(file_path) for file_path in self.gz_files]
            )

            return results

    @staticmethod
    def process_single_file(file_path, decoder, output_path, progress=None, task=None):
        """Process a single file in a worker process"""
        try:
            logger.info(f"Processing file in worker: {file_path}")
            result = CDRFileManager.decode_file(
                file_path=file_path,
                decoder=decoder,
                output_path=output_path,
                progress=progress,
                task=task,
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

    def decode_files_parallel(self):
        """Decode files using parallel processing with multiple CPU cores"""

        # Determine the number of workers (use fewer than available cores to avoid overloading)
        max_workers = min(
            max(os.cpu_count() - 2, 1), ASYNC_CONCURRENCY, len(self.gz_files)
        )
        logger.info(
            f"Starting parallel processing with {max_workers} workers for {len(self.gz_files)} files"
        )

        # Create a progress bar for tracking overall progress
        with CDRFileManager.create_progress_bar() as progress:
            # Main task for overall progress
            main_task = progress.add_task(
                "[cyan]Decoding CDR files...", total=len(self.gz_files)
            )
            results = []
            # Use ProcessPoolExecutor for true parallel processing
            logger.info(f"Creating process pool with {max_workers} workers")
            with ProcessPoolExecutor(max_workers=max_workers) as executor:
                # Submit all tasks
                future_to_file = {
                    executor.submit(
                        CDRFileManager.process_single_file,
                        file_path,
                        self.decoder,
                        self.output_path,
                    ): file_path
                    for file_path in self.gz_files
                }
                logger.info(
                    f"Submitted {len(future_to_file)} tasks to the process pool"
                )

                # Process results as they complete
                for future in concurrent.futures.as_completed(future_to_file):
                    file_path = future_to_file[future]
                    try:
                        logger.info(f"Processing result for file: {file_path}")

                        # Get the result
                        data = future.result()
                        result = data.get("result", {})
                        # Update progress
                        if "records" in result:
                            logger.info(
                                f"Successfully processed {file_path}: {result['records']} records"
                            )
                        else:
                            logger.error(
                                f"Failed to process {file_path}: {data.get('error', 'Unknown error')}"
                            )
                        if "traceback" in data:
                            logger.debug(
                                f"Traceback for {file_path}:\n{data['traceback']}"
                            )

                        # Update main progress
                        progress.update(
                            main_task,
                            description=f"[green]Processed: {file_path.name} [cyan]({result['records']} records)",
                            advance=1,
                        )

                        results.append(result)
                    except Exception as exc:
                        error_details = traceback.format_exc()
                        logger.error(
                            f"Exception processing result for {file_path}: {str(exc)}\n{error_details}"
                        )
                        progress.update(main_task, advance=1)
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
    logger.info(f"Time taken: {total_time:.2f} seconds")
    logger.info("Cleaning up temporary files now, if present...")

    # Also print for user-friendly output
    print("\n[bold cyan]Processing Summary:[/bold cyan]")
    print(f"[green]Files processed successfully: {success_count}[/green]")
    print(f"[red]Files failed: {failed_count}[/red]")
    print(f"[yellow]Total records processed: {total_records}[/yellow]")
    print(f"[magenta]Output directory: {output_path}[/magenta]")
    print(f"[green]Time taken: {total_time:.2f} seconds[/green]")
    print("[blue]Cleaning up temporary files now, if present...[/blue]")


async def main(
    input_path: Path,
    output_path: Path,
    cdr_type: str,
    mode: str,
    log_level: int = logging.INFO,
):
    # Set up logging to file and console
    global logger
    logger = setup_logging(output_path, log_level)

    logger.info(
        f"Starting teleparser with input: {input_path}, output: {output_path}, type: {cdr_type}, mode: {mode}"
    )
    try:
        manager = CDRFileManager(input_path, output_path, cdr_type)
        file_count = len(manager.gz_files)
        print(f"[blue]Started processing of {file_count} files...[/blue]")

        start = perf_counter()
        match mode:
            case "multi_core":
                logger.info("Using multi-core processing mode")
                results = manager.decode_files_parallel()
            case "single_core":
                logger.info("Using single-core processing mode")
                results = manager.decode_files_sequential()
            case "async":
                logger.info("Using async processing mode")
                if asyncio.get_event_loop().is_running():
                    results = await manager.decode_files_async()
                else:
                    logger.info(
                        "No event loop running, falling back to multi-core mode"
                    )
                    results = manager.decode_files_parallel()
            case _:
                logger.error(f"Invalid processing mode: {mode}")
                raise ValueError(f"Invalid mode: {mode}")

        total_time = perf_counter() - start
        logger.info(f"Processing completed in {total_time:.2f} seconds")

        display_summary(results, total_time, manager.output_path)
        manager.cleanup()

        if failed_files := [r for r in results if r.get("status") == "failed"]:
            logger.warning(
                f"Detailed information for {len(failed_files)} failed files:"
            )
            for failed in failed_files:
                logger.error(f"Failed file: {failed.get('file')}")
                logger.error(f"Error: {failed.get('error')}")
                if "traceback" in failed:
                    logger.debug(f"Traceback:\n{failed['traceback']}")

    except Exception as e:
        error_details = traceback.format_exc()
        logger.critical(f"Critical error in main process: {str(e)}\n{error_details}")
        print(f"[bold red]Critical error: {str(e)}[/bold red]")
        raise


def process_cdrs():
    import typer

    app = typer.Typer()

    @app.command()
    def cli(
        input_path: str = typer.Argument(
            ..., help="Path to input CDR files or directory"
        ),
        output_path: str = typer.Argument(..., help="Path to output directory"),
        cdr_type: str = typer.Argument(
            "ericsson_voz",
            help=f"CDR type to process. Options: {', '.join(DECODERS.keys())}",
        ),
        mode: str = typer.Option(
            "multi_core",
            "--mode",
            help="Processing mode. Options: multi-core, single-core, async",
        ),
        log_level: str = typer.Option(
            "INFO",
            "--log-level",
            help="Logging level. Options: DEBUG, INFO, WARNING, ERROR, CRITICAL",
        ),
    ):
        """Process CDR files from input_path (file/folder) and save results to output path.\n
        The expected format is a file or folder with one or more gzipped files.\n
        If the gzipped files are in a ZIP archive, they will be extracted first.
        Default mode is multi-core CPU processing.
        """
        # Create output directory if it doesn't exist
        output_dir = Path(output_path)
        output_dir.mkdir(parents=True, exist_ok=True)

        # Set log level based on command line argument
        numeric_level = getattr(logging, log_level.upper(), None)
        if not isinstance(numeric_level, int):
            print(f"[bold red]Invalid log level: {log_level}[/bold red]")
            numeric_level = logging.INFO

        try:
            asyncio.run(
                main(Path(input_path), output_dir, cdr_type, mode, numeric_level)
            )
        except Exception as e:
            # At this point, logger might not be initialized yet, so we print to console
            error_details = traceback.format_exc()
            print(f"[bold red]Fatal error: {str(e)}[/bold red]")

            # Try to log to file if possible
            with suppress(Exception):
                temp_logger = setup_logging(output_dir, logging.ERROR)
                temp_logger.critical(
                    f"Unhandled exception in main process: {str(e)}\n{error_details}"
                )
            raise

    app()


if __name__ == "__main__":
    process_cdrs()
