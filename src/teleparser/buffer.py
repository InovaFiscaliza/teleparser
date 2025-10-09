import gzip
from pathlib import Path
from contextlib import contextmanager
from typing import Optional


class BufferManager:
    """Manages CDR file buffer reading and file conversion"""

    def __init__(self, file_path: Path):
        self.file_path = file_path
        self.file_handle: Optional[gzip.GzipFile] = None

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

    def read(self, size: int | None = -1):
        return self.file_handle.read(size) if self.file_handle else None


class MemoryBufferManager:
    """Manages CDR file buffer by reading entire file into memory for fast access.
    
    This class reads the entire decompressed file into memory and provides
    efficient access through memoryview objects, eliminating repetitive disk I/O.
    """

    def __init__(self, file_path: Path):
        self.file_path = file_path
        self._data: Optional[bytes] = None
        self._memoryview: Optional[memoryview] = None
        self._position: int = 0

    def load(self) -> memoryview:
        """Load the entire file into memory and return a memoryview."""
        if self._data is None:
            with gzip.open(self.file_path, "rb") as f:
                self._data = f.read()
            self._memoryview = memoryview(self._data)
            self._position = 0
        return self._memoryview

    def get_memoryview(self) -> memoryview:
        """Get the memoryview of the loaded data."""
        if self._memoryview is None:
            return self.load()
        return self._memoryview

    def get_size(self) -> int:
        """Get the total size of the decompressed data."""
        if self._data is None:
            self.load()
        return len(self._data)

    @contextmanager
    def open(self):
        """Context manager that loads data and yields self."""
        self.load()
        try:
            yield self
        finally:
            # Keep data in memory for potential reuse
            pass

    def close(self):
        """Release memory resources."""
        if self._memoryview is not None:
            self._memoryview.release()
            self._memoryview = None
        self._data = None
        self._position = 0

    def has_data(self) -> bool:
        """Check if data is loaded in memory."""
        return self._data is not None
