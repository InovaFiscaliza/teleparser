"""Simple tests for the optimized BER decoder (no pytest required)."""

import gzip
import tempfile
from pathlib import Path

from teleparser.buffer import BufferManager, MemoryBufferManager
from teleparser.decoders.ericsson import (
    ericsson_voz_decoder,
    ericsson_voz_decoder_optimized,
)
from teleparser.decoders.ericsson.ber_optimized import BerDecoderOptimized


def test_memory_buffer_manager():
    """Test MemoryBufferManager basic functionality."""
    print("Testing MemoryBufferManager...")
    
    with tempfile.TemporaryDirectory() as tmpdir:
        test_data = b"Hello, World! This is test data for memory buffer."
        test_file = Path(tmpdir) / "test.gz"
        
        # Create test file
        with gzip.open(test_file, "wb") as f:
            f.write(test_data)
        
        # Test loading
        manager = MemoryBufferManager(test_file)
        memview = manager.load()
        
        assert isinstance(memview, memoryview), "Should return memoryview"
        assert bytes(memview) == test_data, "Data should match"
        assert manager.get_size() == len(test_data), "Size should match"
        
        print("  ✓ Basic loading works")
        
        # Test context manager
        with manager.open() as mgr:
            assert mgr.has_data(), "Should have data"
            memview2 = mgr.get_memoryview()
            assert bytes(memview2) == test_data, "Data should match in context"
        
        print("  ✓ Context manager works")
        
        # Test slicing
        assert bytes(memview[0:5]) == test_data[0:5], "Slicing should work"
        assert memview[0] == test_data[0], "Indexing should work"
        
        print("  ✓ Memoryview slicing works")
    
    print("✅ MemoryBufferManager tests passed!\n")


def test_ber_decoder_optimized_primitives():
    """Test BER decoder primitive operations."""
    print("Testing BerDecoderOptimized primitives...")
    
    # Test read_tag (single byte)
    data = memoryview(b"\x02\x01\x05")
    tag_bytes, bytes_read = BerDecoderOptimized.read_tag(data, 0)
    assert tag_bytes == b"\x02", "Should read correct tag"
    assert bytes_read == 1, "Should read 1 byte"
    print("  ✓ Single-byte tag reading works")
    
    # Test decode_tag
    tag = BerDecoderOptimized.decode_tag(b"\x02")
    assert tag.tag_class == 0, "Should be UNIVERSAL class"
    assert tag.constructed is False, "Should be primitive"
    assert tag.number == 2, "Should be tag number 2 (INTEGER)"
    print("  ✓ Tag decoding works")
    
    # Test read_length (short form)
    data = memoryview(b"\x05")
    length, bytes_read = BerDecoderOptimized.read_length(data, 0)
    assert length == 5, "Should read length 5"
    assert bytes_read == 1, "Should consume 1 byte"
    print("  ✓ Short length form works")
    
    # Test read_length (long form)
    data = memoryview(b"\x82\x01\x00")  # Long form: 256 bytes
    length, bytes_read = BerDecoderOptimized.read_length(data, 0)
    assert length == 256, "Should read length 256"
    assert bytes_read == 3, "Should consume 3 bytes"
    print("  ✓ Long length form works")
    
    # Test EOC detection
    from teleparser.decoders.ericsson.ber_optimized import BerTag
    eoc_tag = BerTag(tag_class=0, constructed=False, number=0)
    assert BerDecoderOptimized.reached_eoc(eoc_tag, 0), "Should detect EOC"
    
    non_eoc_tag = BerTag(tag_class=0, constructed=False, number=2)
    assert not BerDecoderOptimized.reached_eoc(non_eoc_tag, 5), "Should not be EOC"
    print("  ✓ EOC detection works")
    
    print("✅ BerDecoderOptimized primitive tests passed!\n")


def test_memoryview_performance():
    """Test memoryview zero-copy behavior."""
    print("Testing memoryview performance characteristics...")
    
    # Create large data
    data = b"X" * 100000
    mv = memoryview(data)
    
    # Test slicing
    slice1 = mv[0:10000]
    slice2 = mv[10000:20000]
    slice3 = mv[20000:30000]
    
    assert isinstance(slice1, memoryview), "Slice should be memoryview"
    assert isinstance(slice2, memoryview), "Slice should be memoryview"
    assert isinstance(slice3, memoryview), "Slice should be memoryview"
    
    assert bytes(slice1) == b"X" * 10000, "Slice data should be correct"
    assert bytes(slice2) == b"X" * 10000, "Slice data should be correct"
    
    print("  ✓ Zero-copy slicing works")
    
    # Test position tracking
    test_data = b"\x02\x01\x05\x02\x01\x0a\x02\x01\x0f"
    mv = memoryview(test_data)
    
    position = 0
    records = []
    
    while position < len(mv):
        if position < len(mv):
            tag = mv[position]
            position += 1
            
            if position < len(mv):
                length = mv[position]
                position += 1
                
                if position + length <= len(mv):
                    value = bytes(mv[position:position + length])
                    position += length
                    records.append((tag, length, value))
    
    assert len(records) == 3, "Should parse 3 records"
    assert records[0] == (0x02, 1, b"\x05"), "First record should be correct"
    assert records[1] == (0x02, 1, b"\x0a"), "Second record should be correct"
    assert records[2] == (0x02, 1, b"\x0f"), "Third record should be correct"
    
    print("  ✓ Position tracking works")
    print("✅ Memoryview performance tests passed!\n")


def test_decoder_integration():
    """Test that decoders can be instantiated."""
    print("Testing decoder integration...")
    
    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = Path(tmpdir) / "empty.gz"
        
        # Create empty gzipped file
        with gzip.open(test_file, "wb") as f:
            f.write(b"")
        
        # Test original decoder
        buffer1 = BufferManager(test_file)
        decoder1 = ericsson_voz_decoder(buffer1)
        assert decoder1 is not None, "Original decoder should be created"
        print("  ✓ Original decoder instantiation works")
        
        # Test optimized decoder
        buffer2 = MemoryBufferManager(test_file)
        decoder2 = ericsson_voz_decoder_optimized(buffer2)
        assert decoder2 is not None, "Optimized decoder should be created"
        print("  ✓ Optimized decoder instantiation works")
        
        # Test conversion from BufferManager to MemoryBufferManager
        buffer3 = BufferManager(test_file)
        decoder3 = ericsson_voz_decoder_optimized(buffer3)
        assert decoder3 is not None, "Should auto-convert BufferManager"
        print("  ✓ Auto-conversion from BufferManager works")
    
    print("✅ Decoder integration tests passed!\n")


def test_imports():
    """Test that all required modules can be imported."""
    print("Testing imports...")
    
    try:
        from teleparser.buffer import BufferManager, MemoryBufferManager
        from teleparser.decoders.ericsson import (
            ericsson_voz_decoder,
            ericsson_voz_decoder_optimized,
        )
        from teleparser.decoders.ericsson.ber import BerDecoder
        from teleparser.decoders.ericsson.ber_optimized import BerDecoderOptimized
        
        print("  ✓ All imports successful")
        print("✅ Import tests passed!\n")
        return True
    except ImportError as e:
        print(f"  ✗ Import failed: {e}")
        return False


def main():
    """Run all tests."""
    print("=" * 60)
    print("Running BER Decoder Optimization Tests")
    print("=" * 60 + "\n")
    
    try:
        # Run all tests
        if not test_imports():
            print("\n❌ Import tests failed. Cannot continue.")
            return False
        
        test_memory_buffer_manager()
        test_ber_decoder_optimized_primitives()
        test_memoryview_performance()
        test_decoder_integration()
        
        print("=" * 60)
        print("🎉 All tests passed successfully!")
        print("=" * 60)
        return True
        
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
        return False
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    import sys
    success = main()
    sys.exit(0 if success else 1)
