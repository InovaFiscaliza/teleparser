from enum import Enum
from dataclasses import dataclass
from functools import cached_property
from pathlib import Path
import zipfile
import shutil
from typing import List, Set


@dataclass
class CDRFileSetup:
    input_path: Path
    output_path: Path
    carrier: str
    cdr_type: str
    timestamp: str


class OutputFormat(str, Enum):
    SINGLE = "single"  # Single output file
    INDIVIDUAL = "individual"  # One file per input
    NUMBER_RANGE = "number_range"  # Split by number ranges
    DATETIME = "datetime"  # Split by date/time


class CDRFileManager:
    def __init__(self, file_setup: CDRFileSetup):
        self.setup = file_setup
        self.processed_files: Set[Path] = set()
        self.failed_files: Set[Path] = set()

    def setup_directories(self) -> Path:
        """Create necessary output directories and return working path"""
        output_dir = (
            self.setup.output_path / f"{self.setup.carrier}_{self.setup.timestamp}"
        )
        output_dir.mkdir(parents=True, exist_ok=True)
        return output_dir

    @cached_property
    def input_gz_files(self) -> List[Path]:
        """It traverses the tree to get the list of .gz files, decompressing ZIP archives if needed"""
        files = list(self.setup.input_path.rglob("*[.gz|.zip]"))
        zip_files = [f for f in files if f.suffix == ".zip"]
        gz_files = [f for f in files if f.suffix == ".gz"]
        gz_files.extend(self.decompress_zips(zip_files))
        return gz_files

    def decompress_zips(self, zip_files: List[Path]) -> List[Path]:
        """Extract ZIP files and return paths to extracted files"""
        extract_dir = self.setup.output_path / "temp_extracted"
        extract_dir.mkdir(parents=True, exist_ok=True)

        gz_files: List[Path] = []
        for zip_file in zip_files:
            try:
                with zipfile.ZipFile(zip_file) as zf:
                    zf.extractall(extract_dir)
                    for file in zf.namelist():
                        if file.endswith(".gz"):
                            gz_files.append(extract_dir / file)
            except zipfile.BadZipFile:
                self.failed_files.add(Path(zip_file))

        return gz_files

    def cleanup(self):
        """Clean up temporary files and directories"""
        temp_dir = self.setup.output_path / "temp_extracted"
        if temp_dir.exists():
            shutil.rmtree(temp_dir)


if __name__ == "__main__":
    from datetime import datetime, timezone

    file_setup = CDRFileSetup(
        input_path=Path(__file__).parent / "data/input",
        output_path=Path(__file__).parent / "data/output",
        carrier="carrier",
        cdr_type="cdr_type",
        timestamp=datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S"),
    )
    manager = CDRFileManager(file_setup)
    manager.setup_directories()
    print(f".gz files in folders and subfolders: {len(manager.input_gz_files)}")
    manager.cleanup()
