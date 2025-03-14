from contextlib import contextmanager
import gzip
from functools import cached_property
from pathlib import Path
import zipfile
import shutil
from typing import List, Set, Optional, BinaryIO


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
    def input_gz_files(self) -> List[Path]:
        """It traverses the tree to get the list of .gz files, decompressing ZIP archives if needed"""
        files = list(self.setup.input_path.rglob("*[.gz|.zip]"))
        zip_files = [f for f in files if f.suffix == ".zip"]
        gz_files = [f for f in files if f.suffix == ".gz"]
        if zip_files:
            gz_files.extend(self.decompress_zips(zip_files))
        return gz_files

    def decompress_zips(self, zip_files: List[Path]) -> List[Path]:
        """Extract ZIP files and return paths to extracted files"""
        self.temp_dir = self.setup.output_path / "temp_extracted"
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


if __name__ == "__main__":
    from teleparser.decoders.ber import BerDecoder
    from collections import Counter

    blocks = Counter()
    types = Counter()
    folder = Path(__file__).parent.parent.parent / "data"
    # folder = Path(r"D:\code\cdr\data\input\ClaroVozEricssonMenu1")
    for file in folder.iterdir():
        if file.suffix == ".gz":
            buffer_manager = BufferManager(file)
            ber = BerDecoder()
            with buffer_manager.open() as file_buffer:
                while (tlv := ber.decode_tlv(file_buffer)) is not None:
                    if tlv.children is not None:
                        for child in tlv.children:
                            blocks[child.tag.number] += 1
                            for c in child.children:
                                types[(child.tag.number, c.tag.number)] += 1

    print(f"Count of CDR blocks: {blocks}")
    print(f"Count of Parameter Types: {types}")
