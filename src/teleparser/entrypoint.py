import asyncio
import gc
import gzip
import os
import shutil
import zipfile
import concurrent.futures
from concurrent.futures import ProcessPoolExecutor
from contextlib import contextmanager
from datetime import datetime, timezone
from functools import cached_property
from pathlib import Path
from typing import BinaryIO, List, Optional, Set
from time import perf_counter


import pandas as pd
from rich.progress import (
    Progress,
    BarColumn,
    SpinnerColumn,
    TaskProgressColumn,
    TextColumn,
    TimeRemainingColumn,
)
from rich import print

from teleparser.decoders.ericsson import ericsson_voz_decoder

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
            raise NotImplementedError(
                f"Decoder invalid or not implemented for {self.cdr_type}"
            )
        self.decoder = DECODERS[self.cdr_type]
        timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
        output_dir = self.output_path / f"{self.cdr_type}_{timestamp}"
        output_dir.mkdir(parents=True, exist_ok=True)
        self.output_path = output_dir

    @cached_property
    def gz_files(self) -> List[Path]:
        """It traverses the tree to get the list of .gz files, decompressing ZIP archives if needed"""
        if self.input_path.is_file():
            files = [self.input_path]
        elif self.input_path.is_dir():
            files = list(self.input_path.rglob("*[.gz|.zip]"))
        else:
            raise ValueError(f"Invalid input path: {self.input_path}")
        zip_files = [f for f in files if f.suffix == ".zip"]
        gz_files = [f for f in files if f.suffix == ".gz"]
        if zip_files:
            gz_files.extend(self.decompress_zips(zip_files))
        return gz_files

    def decompress_zips(self, zip_files: List[Path]) -> List[Path]:
        """Extract ZIP files and return paths to extracted files"""
        self.temp_dir = self.output_path / "temp_extracted"
        self.temp_dir.mkdir(parents=True, exist_ok=True)

        gz_files: List[Path] = []
        with self.create_progress_bar() as progress:
            task = progress.add_task(
                "[cyan]Extracting ZIP files...", total=len(zip_files)
            )
            for zip_file in zip_files:
                try:
                    with zipfile.ZipFile(zip_file) as zf:
                        zf.extractall(self.temp_dir)
                        gz_files.extend(
                            self.temp_dir / file
                            for file in zf.namelist()
                            if file.endswith(".gz")
                        )
                except zipfile.BadZipFile:
                    self.failed_files.add(Path(zip_file))
                progress.update(task, advance=1)
        return gz_files

    def cleanup(self):
        """Clean up temporary files and directories"""
        if self.temp_dir is not None and self.temp_dir.exists():
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

    def decode_files_sequential(self):
        """Decode all files sequentially with a progress bar and return results"""
        results = []

        with self.create_progress_bar() as progress:
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
                    progress.update(file_tasks[file_path], visible=True)
                    progress.update(
                        file_tasks[file_path],
                        description=f"[green]Processing: {file_path.name}",
                    )

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

                except Exception as e:
                    # Handle errors
                    progress.update(
                        file_tasks[file_path],
                        description=f"[red]Failed: {file_path.name} [red]({str(e)})",
                    )
                    self.failed_files.add(file_path)
                    results.append(
                        {"file": file_path, "error": str(e), "status": "failed"}
                    )

                finally:
                    # Hide the completed file task to reduce clutter
                    progress.update(file_tasks[file_path], visible=False)
                    # Update main progress when a file is complete
                    progress.update(main_task, advance=1)

        return results

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
            # Update task description to show it's being processed
            progress.update(
                task,
                description=f"[green]Processing: [green]{file_path.name} [cyan](0 records)",
            )

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
            df = pd.DataFrame(
                blocks,
                copy=False,
                dtype="string",
            )
            df.astype("category").to_parquet(
                output_file,
                index=False,
                compression="gzip",
            )
            del blocks, df
            gc.collect()

            # Final progress update
            progress.update(
                task,
                description=f"[green]Completed: [green]{file_path.name} [cyan]({counter} records)",
            )

            return {"file": file_path, "records": counter, "status": "success"}

        except Exception as e:
            progress.update(
                task, description=f"[red]Failed: [red]{file_path.name} [red]({str(e)})"
            )
            return {"file": file_path, "error": str(e), "status": "failed"}

        finally:
            # Only close the progress if we created it locally
            if local_progress:
                local_progress.stop()

    async def decode_files_async(self):
        # Create a single shared progress context for all tasks
        with CDRFileManager.create_progress_bar(False) as progress:
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

                # Process the file
                result = await asyncio.to_thread(
                    CDRFileManager.decode_file,
                    file_path=file_path,
                    decoder=self.decoder,
                    output_path=self.output_path,
                    progress=progress,
                    task=file_tasks[file_path],
                )

                # Update main progress when a file is complete
                progress.update(main_task, advance=1)

                # Hide the completed file task to reduce clutter
                progress.update(file_tasks[file_path], visible=False)

                return result

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
    def process_single_file(file_path, decoder, output_path):
        """Process a single file in a worker process"""
        try:
            result = CDRFileManager.decode_file(
                file_path=file_path,
                decoder=decoder,
                output_path=output_path,
                # Can't pass progress objects to subprocesses
                progress=None,
                task=None,
            )
            return {"file_path": file_path, "result": result}
        except Exception as e:
            return {"file_path": file_path, "error": str(e)}

    def decode_files_parallel(self):
        """Decode files using parallel processing with multiple CPU cores"""

        # Determine the number of workers (use fewer than available cores to avoid overloading)
        max_workers = min(os.cpu_count() - 2, ASYNC_CONCURRENCY, len(self.gz_files))

        # Create a progress bar for tracking overall progress
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
            results = []
            # Use ProcessPoolExecutor for true parallel processing
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
                # Process results as they complete
                for future in concurrent.futures.as_completed(future_to_file):
                    file_path = future_to_file[future]
                    try:
                        # Make this file's task visible
                        progress.update(file_tasks[file_path], visible=True)
                        progress.update(
                            file_tasks[file_path],
                            description=f"[green]Processing: {file_path.name}",
                        )

                        # Get the result
                        data = future.result()
                        result = data.get("result", {})

                        # Update progress
                        if "records" in result:
                            progress.update(
                                file_tasks[file_path],
                                description=f"[green]Completed: {file_path.name} [cyan]({result['records']} records)",
                            )
                        else:
                            progress.update(
                                file_tasks[file_path],
                                description=f"[red]Failed: {file_path.name}",
                            )

                        # Hide the completed file task to reduce clutter
                        progress.update(file_tasks[file_path], visible=False)

                        # Update main progress
                        progress.update(main_task, advance=1)

                        results.append(result)
                    except Exception as exc:
                        print(exc)
                        progress.update(
                            file_tasks[file_path],
                            description=f"[red]Error: {file_path.name} - {exc}",
                        )
                        progress.update(file_tasks[file_path], visible=False)
                        progress.update(main_task, advance=1)
                        results.append(
                            {"file": file_path, "error": str(exc), "status": "failed"}
                        )

            return results


def display_summary(results, total_time, output_path):
    success_count = sum(r.get("status") == "success" for r in results)
    failed_count = sum(r.get("status") == "failed" for r in results)
    total_records = sum(r.get("records", 0) for r in results)
    print("\n[bold cyan]Processing Summary:[/bold cyan]")
    print(f"[green]Files processed successfully: {success_count}[/green]")
    print(f"[red]Files failed: {failed_count}[/red]")
    print(f"[yellow]Total records processed: {total_records}[/yellow]")
    print(f"[magenta]Output directory: {output_path}[/magenta]")
    print(f"[green]Time taken: {total_time:.2f} seconds[/green]")
    print("[blue]Cleaning up temporary files now, if present...[/blue]")


async def main(
    input_path: Path, output_path: Path, cdr_type: str, parallel: bool, async_: bool
):
    manager = CDRFileManager(input_path, output_path, cdr_type)
    print(f"[blue]Starting processing of {len(manager.gz_files)} files...[/blue]")
    start = perf_counter()
    if parallel:
        if async_:
            results = await manager.decode_files_async()
        else:
            results = manager.decode_files_parallel()
    else:
        results = manager.decode_files_sequential()
    total_time = perf_counter() - start
    display_summary(results, total_time, manager.output_path)
    manager.cleanup()


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
        parallel: bool = typer.Option(
            False,
            "--parallel",
            help="Process files in parallel. If True and async is False, uses multiple CPU cores",
        ),
        async_: bool = typer.Option(
            False,
            "--async",
            help="Process files asynchronously. If True and parallel is False, it's ignored and the files will be processed sequentially",
        ),
    ):
        """Process CDR files from input_path (file/folder) and save results to output path.\n
        The expected format is a file or folder with one or more gzipped files.\n
        If the gzipped files are in a ZIP archive, they will be extracted first.
        """
        asyncio.run(
            main(Path(input_path), Path(output_path), cdr_type, parallel, async_)
        )

    app()


if __name__ == "__main__":
    process_cdrs()
