import os
from datetime import datetime, timezone
from contextlib import contextmanager
import gzip
from functools import cached_property
from pathlib import Path
import zipfile
import shutil
from typing import List, Set, Optional, BinaryIO

from fastcore.parallel import parallel_async, parallel

from teleparser.decoders.ber import BerDecoder


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
        self.input_path = input_path
        self.output_path = output_path
        self.cdr_type = cdr_type
        self.processed_files: Set[Path] = set()
        self.failed_files: Set[Path] = set()
        self.temp_dir: Path | None = None

    def setup_directories(self) -> Path:
        """Create necessary output directories and return working path"""
        timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
        output_dir = self.output_path / f"{self.cdr_type}_{timestamp}"
        output_dir.mkdir(parents=True, exist_ok=True)
        return output_dir

    @cached_property
    def gz_files(self) -> List[Path]:
        """It traverses the tree to get the list of .gz files, decompressing ZIP archives if needed"""
        files = list(self.input_path.rglob("*[.gz|.zip]"))
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
        return gz_files

    def cleanup(self):
        """Clean up temporary files and directories"""
        if self.temp_dir is not None and self.temp_dir.exists():
            shutil.rmtree(self.temp_dir)

    @staticmethod
    def decode_file(file_path: Path) -> list:
        blocks = []
        buffer_manager = BufferManager(file_path)
        ber = BerDecoder()
        with buffer_manager.open() as file_buffer:
            while (tlv := ber.decode_tlv(file_buffer)) is not None:
                blocks.append(tlv)
        print(f"{file_path.name} done!")
        return blocks

    async def decode_async(self):
        return await parallel_async(
            CDRFileManager.decode_file,
            self.gz_files,
            n_workers=min(16, len(self.gz_files)),
        )

    def decode(self):
        return parallel(
            CDRFileManager.decode_file,
            self.gz_files,
            n_workers=min(16, len(self.gz_files)),
            progress=True,
        )


if __name__ == "__main__":
    import asyncio
    from collections import Counter
    from time import perf_counter

    blocks = Counter()
    types = Counter()

    async def process_cdr_files():
        input_folder = Path(r"D:\code\cdr\data\input\ClaroVozEricssonMenu1")
        # input_folder = Path(__file__).parent.parent.parent / "data"
        output_path = Path(__file__).parent.parent.parent / "data"
        start = perf_counter()

        file_manager = CDRFileManager(input_folder, output_path, "VozEricsson")
        decoded_files = await file_manager.decode_async()

        for cdr in decoded_files:
            for tlv in cdr:
                if tlv.children is not None:
                    for child in tlv.children:
                        blocks[child.tag.number] += 1
                        for c in child.children:
                            types[(child.tag.number, c.tag.number)] += 1
            # Clean up temporary files when done
        file_manager.cleanup()
        print(f"Count of CDR blocks: {blocks}")
        print(f"Count of Parameter Types: {types}")
        print(f"Total time: {perf_counter() - start}")

    # asyncio.run(process_cdr_files())
    # from contextlib import suppress

    # folder = Path(__file__).parent.parent.parent / "data"
    # file = folder / "timvoz.gz"
    # buffer_manager = BufferManager(file)
    # ber = BerDecoder()
    # file_buffer = buffer_manager.open_file()
    # while file_buffer.has_data():
    #     with suppress(KeyError):
    #         while (tlv := ber.decode_tlv(file_buffer)) is not None:
    #             print("Varredura: (Call Data Record)")
    #             print(tlv)
    #             if tlv.children is not None:
    #                 for child in tlv.children:
    #                     print(80 * "=")
    #                     print("Call Module")
    #                     print(child)
    #                     # print(f"string={child.tag.string}, tipo={child.tag.number}, comprimento={child.length}, bytes={child.value}")
    #                     print(80 * "=")
    #                     print(
    #                         f"Quantidade de parâmetros dentro do Call Module: {len(child.children)}"
    #                     )
    #                     print("Parâmetros:")
    #                     for c in child.children:
    #                         print(c)
