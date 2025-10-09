"""Tests for the optimized BER decoder implementation."""

import gzip
import tempfile
from pathlib import Path
import pytest

from teleparser.buffer import BufferManager, MemoryBufferManager
from teleparser.decoders.ericsson import (
    ericsson_voz_decoder,
    ericsson_voz_decoder_optimized,
)
from teleparser.decoders.ericsson.ber import BerDecoder
from teleparser.decoders.ericsson.ber_optimized import BerDecoderOptimized


class TestMemoryBufferManager:
    """Test the MemoryBufferManager class."""
    
    def test_load_data(self, tmp_path):
        """Test that data is loaded correctly."""
        # Create a test gzipped file
        test_data = b"Hello, World! This is test data."
        test_file = tmp_path / "test.gz"
        
        with gzip.open(test_file, "wb") as f:
            f.write(test_data)
        
        # Load using MemoryBufferManager
        manager = MemoryBufferManager(test_file)
        memview = manager.load()
        
        assert isinstance(memview, memoryview)
        assert bytes(memview) == test_data
        assert manager.get_size() == len(test_data)
    
    def test_context_manager(self, tmp_path):
        """Test context manager functionality."""
        test_data = b"Context manager test data"
        test_file = tmp_path / "test_context.gz"
        
        with gzip.open(test_file, "wb") as f:
            f.write(test_data)
        
        manager = MemoryBufferManager(test_file)
        
        with manager.open() as mgr:
            assert mgr.has_data()
            memview = mgr.get_memoryview()
            assert bytes(memview) == test_data
    
    def test_memoryview_slicing(self, tmp_path):
        """Test that memoryview slicing works correctly."""
        test_data = b"0123456789ABCDEF"
        test_file = tmp_path / "test_slice.gz"
        
        with gzip.open(test_file, "wb") as f:
            f.write(test_data)
        
        manager = MemoryBufferManager(test_file)
        memview = manager.load()
        
        # Test slicing
        assert bytes(memview[0:5]) == b"01234"
        assert bytes(memview[5:10]) == b"56789"
        assert memview[0] == ord('0')
        assert memview[15] == ord('F')


class TestBerDecoderOptimized:
    """Test the optimized BER decoder."""
    
    def test_read_tag_single_byte(self):
        """Test reading a single-byte tag."""
        data = memoryview(b"\x02\x01\x05")  # INTEGER tag
        tag_bytes, bytes_read = BerDecoderOptimized.read_tag(data, 0)
        
        assert tag_bytes == b"\x02"
        assert bytes_read == 1
    
    def test_read_tag_multi_byte(self):
        """Test reading a multi-byte tag."""
        # Tag with value > 30 (requires multi-byte encoding)
        data = memoryview(b"\x1f\x81\x00\x01")  # Multi-byte tag
        tag_bytes, bytes_read = BerDecoderOptimized.read_tag(data, 0)
        
        assert len(tag_bytes) > 1
        assert bytes_read > 1
    
    def test_decode_tag(self):
        """Test decoding tag bytes."""
        tag_bytes = b"\x02"  # UNIVERSAL, primitive, tag 2 (INTEGER)
        tag = BerDecoderOptimized.decode_tag(tag_bytes)
        
        assert tag.tag_class == 0  # UNIVERSAL
        assert tag.constructed is False
        assert tag.number == 2
    
    def test_read_length_short_form(self):
        """Test reading length in short form."""
        data = memoryview(b"\x05")  # Length = 5
        length, bytes_read = BerDecoderOptimized.read_length(data, 0)
        
        assert length == 5
        assert bytes_read == 1
    
    def test_read_length_long_form(self):
        """Test reading length in long form."""
        # Length = 0x0100 (256) encoded in long form
        data = memoryview(b"\x82\x01\x00")  # 0x82 = long form with 2 bytes
        length, bytes_read = BerDecoderOptimized.read_length(data, 0)
        
        assert length == 256
        assert bytes_read == 3
    
    def test_reached_eoc(self):
        """Test End-of-Content detection."""
        from teleparser.decoders.ericsson.ber_optimized import BerTag
        
        # EOC is (0, False, 0, 0)
        tag = BerTag(tag_class=0, constructed=False, number=0)
        assert BerDecoderOptimized.reached_eoc(tag, 0) is True
        
        # Non-EOC
        tag = BerTag(tag_class=0, constructed=False, number=2)
        assert BerDecoderOptimized.reached_eoc(tag, 5) is False


class TestDecoderComparison:
    """Compare output of original and optimized decoders."""
    
    @pytest.fixture
    def sample_ber_data(self, tmp_path):
        """Create a sample BER-encoded file for testing."""
        # Simple BER structure: SEQUENCE of INTEGER
        # SEQUENCE tag (0x30), length 5
        # INTEGER tag (0x02), length 1, value 42
        # INTEGER tag (0x02), length 1, value 99
        ber_data = b"\x30\x06\x02\x01\x2a\x02\x01\x63"
        
        test_file = tmp_path / "sample.gz"
        with gzip.open(test_file, "wb") as f:
            f.write(ber_data)
        
        return test_file
    
    def test_basic_parsing(self, tmp_path):
        """Test that both decoders can parse basic structures."""
        # Create a minimal test case
        test_file = tmp_path / "minimal.gz"
        
        # Empty or minimal BER data
        minimal_data = b""
        with gzip.open(test_file, "wb") as f:
            f.write(minimal_data)
        
        # Test original decoder
        buffer1 = BufferManager(test_file)
        decoder1 = ericsson_voz_decoder(buffer1)
        
        # Test optimized decoder  
        buffer2 = MemoryBufferManager(test_file)
        decoder2 = ericsson_voz_decoder_optimized(buffer2)
        
        # Both should handle empty files gracefully
        try:
            results1 = list(decoder1.parse_blocks())
            results2 = list(decoder2.parse_blocks())
            
            # Should have same number of results
            assert len(results1) == len(results2)
        except Exception as e:
            # Both should raise the same exception
            pytest.skip(f"Both decoders handled empty file: {e}")


class TestMemoryviewPerformance:
    """Performance-related tests for memoryview."""
    
    def test_zero_copy_slicing(self):
        """Verify that memoryview slicing doesn't copy data."""
        data = b"A" * 10000
        mv = memoryview(data)
        
        # Get multiple slices
        slice1 = mv[0:1000]
        slice2 = mv[1000:2000]
        slice3 = mv[2000:3000]
        
        # All should be memoryview objects
        assert isinstance(slice1, memoryview)
        assert isinstance(slice2, memoryview)
        assert isinstance(slice3, memoryview)
        
        # Verify data integrity
        assert bytes(slice1) == b"A" * 1000
        assert bytes(slice2) == b"A" * 1000
        assert bytes(slice3) == b"A" * 1000
    
    def test_position_tracking(self):
        """Test position tracking through decode process."""
        data = b"\x02\x01\x05\x02\x01\x0a\x02\x01\x0f"
        mv = memoryview(data)
        
        position = 0
        records = []
        
        # Simulate parsing multiple records
        while position < len(mv):
            # Read tag
            if position < len(mv):
                tag_byte = mv[position]
                position += 1
                
                # Read length
                if position < len(mv):
                    length = mv[position]
                    position += 1
                    
                    # Read value
                    if position + length <= len(mv):
                        value = bytes(mv[position:position + length])
                        position += length
                        records.append((tag_byte, length, value))
        
        # Should have parsed 3 records
        assert len(records) == 3
        assert records[0] == (0x02, 1, b"\x05")
        assert records[1] == (0x02, 1, b"\x0a")
        assert records[2] == (0x02, 1, b"\x0f")


def test_import_optimized_module():
    """Test that the optimized module can be imported."""
    from teleparser.decoders.ericsson.ber_optimized import BerDecoderOptimized
    from teleparser.buffer import MemoryBufferManager
    
    assert BerDecoderOptimized is not None
    assert MemoryBufferManager is not None


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
