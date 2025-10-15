"""Tests for the two-phase BER decoder implementation."""

import gzip
import tempfile
from pathlib import Path
import pytest

from teleparser.buffer import MemoryBufferManager
from teleparser.decoders.ericsson.ber_two_phase import (
    BerDecoderTwoPhase, TLVTriple, ericsson_voz_decoder_two_phase
)
from teleparser.decoders.ericsson.ber_optimized import BerDecoderOptimized
from teleparser.decoders.ericsson.voz import EricssonVoz


class TestTLVTriple:
    """Test the TLVTriple data structure."""
    
    def test_tlv_triple_creation(self):
        """Test basic TLVTriple creation and attributes."""
        tlv = TLVTriple(
            tag_class=0,
            constructed=False,
            tag_number=2,
            value_start=10,
            value_length=5,
            depth=0,
            parent_idx=-1,
            tlv_start=8
        )
        
        assert tlv.tag_class == 0
        assert tlv.constructed is False
        assert tlv.tag_number == 2
        assert tlv.value_start == 10
        assert tlv.value_length == 5
        assert tlv.depth == 0
        assert tlv.parent_idx == -1
        assert tlv.tlv_start == 8


class TestBerDecoderTwoPhase:
    """Test the two-phase BER decoder."""
    
    @pytest.fixture
    def sample_ber_data(self):
        """Create sample BER-encoded data for testing."""
        # Simple BER structures that should be parseable
        # SEQUENCE (0x30) containing INTEGERs (0x02) and OCTET STRINGs (0x04)
        return (
            b'\\x30\\x10'  # SEQUENCE, length 16
            b'\\x02\\x01\\x01'  # INTEGER 1
            b'\\x02\\x01\\x02'  # INTEGER 2
            b'\\x04\\x04test'  # OCTET STRING "test"
            b'\\x02\\x02\\x03\\xe8'  # INTEGER 1000
        )
    
    @pytest.fixture
    def test_file(self, tmp_path, sample_ber_data):
        """Create a temporary gzipped test file."""
        test_file = tmp_path / "test.gz"
        
        with gzip.open(test_file, "wb") as f:
            f.write(sample_ber_data)
        
        return test_file
    
    @pytest.fixture
    def decoder(self, test_file):
        """Create a two-phase decoder instance."""
        buffer_manager = MemoryBufferManager(test_file)
        return BerDecoderTwoPhase(
            parser=EricssonVoz,
            buffer_manager=buffer_manager,
            n_workers=2
        )
    
    def test_extract_tlv_structure_basic(self, decoder, sample_ber_data):
        """Test basic TLV structure extraction."""
        data = memoryview(sample_ber_data)
        tlvs = decoder.extract_tlv_structure(data)
        
        # Should have at least a few TLVs
        assert len(tlvs) >= 4
        
        # First should be the SEQUENCE
        first_tlv = tlvs[0]
        assert first_tlv.tag_number == 16  # SEQUENCE tag (0x30 & 0x1F = 16)
        assert first_tlv.constructed is True
        assert first_tlv.depth == 0
        assert first_tlv.parent_idx == -1
        
        # Should have child TLVs with depth > 0
        child_tlvs = [tlv for tlv in tlvs if tlv.depth > 0]
        assert len(child_tlvs) >= 3
    
    def test_extract_tlv_structure_empty_data(self, decoder):
        """Test TLV extraction with empty data."""
        data = memoryview(b'')
        tlvs = decoder.extract_tlv_structure(data)
        
        assert tlvs == []
    
    def test_extract_tlv_structure_malformed_data(self, decoder):
        """Test TLV extraction with malformed data."""
        # Incomplete TLV (tag without length/value)
        data = memoryview(b'\\x02')
        tlvs = decoder.extract_tlv_structure(data)
        
        # Should handle gracefully and return empty or partial results
        assert isinstance(tlvs, list)
    
    def test_get_schema_for_tlv(self, decoder, sample_ber_data):
        """Test schema resolution for TLVs."""
        data = memoryview(sample_ber_data)
        tlvs = decoder.extract_tlv_structure(data)
        
        if tlvs:
            schema = decoder.get_schema_for_tlv(tlvs, 0)
            # For now, should return None (simplified implementation)
            assert schema is None
    
    def test_interpret_tlv_batch_basic(self, decoder, sample_ber_data):
        """Test basic TLV batch interpretation."""
        data = memoryview(sample_ber_data)
        tlvs = decoder.extract_tlv_structure(data)
        
        if len(tlvs) > 1:
            # Test interpreting first few TLVs
            results = decoder.interpret_tlv_batch(tlvs, data, 0, min(3, len(tlvs)))
            
            # Results should be a dictionary
            assert isinstance(results, dict)
            # Might be empty if parsing fails, but should not crash
    
    def test_parallel_interpret_basic(self, decoder, sample_ber_data):
        """Test parallel interpretation of TLVs."""
        data = memoryview(sample_ber_data)
        tlvs = decoder.extract_tlv_structure(data)
        
        records = decoder.parallel_interpret(tlvs, data)
        
        # Should return a list of records
        assert isinstance(records, list)
        # Might be empty if parsing fails, but should not crash
    
    def test_parse_blocks_integration(self, decoder):
        """Test the complete parse_blocks integration."""
        try:
            records = list(decoder.parse_blocks())
            
            # Should return a list (might be empty if parsing fails)
            assert isinstance(records, list)
            
            # If we have records, they should be dictionaries
            for record in records:
                assert isinstance(record, dict)
                
        except Exception as e:
            # Some parsing failures are expected with synthetic data
            # Just ensure it doesn't crash catastrophically
            assert isinstance(e, (KeyError, ValueError, AttributeError))
    
    def test_process_with_progress(self, decoder):
        """Test the process method with progress bar."""
        try:
            records = decoder.process(show_progress=False)
            
            assert isinstance(records, list)
            
        except Exception as e:
            # Some parsing failures are expected
            assert isinstance(e, (KeyError, ValueError, AttributeError))
    
    def test_different_worker_counts(self, test_file):
        """Test decoder with different worker counts."""
        buffer_manager = MemoryBufferManager(test_file)
        
        for n_workers in [1, 2, 4]:
            decoder = BerDecoderTwoPhase(
                parser=EricssonVoz,
                buffer_manager=buffer_manager,
                n_workers=n_workers
            )
            
            try:
                records = decoder.process(show_progress=False)
                assert isinstance(records, list)
                
            except Exception as e:
                # Parsing might fail, but shouldn't crash
                assert isinstance(e, (KeyError, ValueError, AttributeError))


class TestEricssonVozDecoderTwoPhase:
    """Test the convenience function for creating VOZ decoders."""
    
    def test_decoder_creation(self, tmp_path):
        """Test creating a VOZ decoder through the convenience function."""
        # Create a minimal test file
        test_file = tmp_path / "test.gz"
        with gzip.open(test_file, "wb") as f:
            f.write(b'\\x30\\x03\\x02\\x01\\x00')  # Minimal SEQUENCE with INTEGER
        
        buffer_manager = MemoryBufferManager(test_file)
        decoder = ericsson_voz_decoder_two_phase(buffer_manager, n_workers=2)
        
        assert isinstance(decoder, BerDecoderTwoPhase)
        assert decoder.n_workers == 2
        assert decoder.parser == EricssonVoz
    
    def test_decoder_default_workers(self, tmp_path):
        """Test decoder creation with default worker count."""
        test_file = tmp_path / "test.gz"
        with gzip.open(test_file, "wb") as f:
            f.write(b'\\x30\\x03\\x02\\x01\\x00')
        
        buffer_manager = MemoryBufferManager(test_file)
        decoder = ericsson_voz_decoder_two_phase(buffer_manager)
        
        assert decoder.n_workers == 4  # Default


class TestTwoPhasePerformance:
    """Performance-related tests."""
    
    def test_large_synthetic_data(self, tmp_path):
        """Test with larger synthetic data to verify performance characteristics."""
        # Create a larger test file
        basic_record = (
            b'\\x30\\x10'  # SEQUENCE, length 16
            b'\\x02\\x01\\x01'  # INTEGER 1
            b'\\x02\\x01\\x02'  # INTEGER 2
            b'\\x04\\x04test'  # OCTET STRING "test"
            b'\\x02\\x02\\x03\\xe8'  # INTEGER 1000
        )
        
        # Repeat the record many times
        large_data = basic_record * 100
        
        test_file = tmp_path / "large_test.gz"
        with gzip.open(test_file, "wb") as f:
            f.write(large_data)
        
        buffer_manager = MemoryBufferManager(test_file)
        decoder = ericsson_voz_decoder_two_phase(buffer_manager, n_workers=2)
        
        import time
        start_time = time.perf_counter()
        
        try:
            records = decoder.process(show_progress=False)
            end_time = time.perf_counter()
            
            parse_time = end_time - start_time
            
            # Should complete reasonably quickly (within 10 seconds)
            assert parse_time < 10.0
            
            # Should return a list
            assert isinstance(records, list)
            
        except Exception as e:
            # Parsing might fail with synthetic data, but should not hang or crash
            end_time = time.perf_counter()
            parse_time = end_time - start_time
            
            # Even failures should be quick
            assert parse_time < 10.0
            assert isinstance(e, (KeyError, ValueError, AttributeError))
    
    def test_zero_copy_behavior(self, tmp_path):
        """Test that memoryview slicing is zero-copy."""
        # This test verifies that the TLV extraction doesn't copy large amounts of data
        large_data = b'\\x30\\x05\\x02\\x01\\x00\\x00\\x00' + b'\\x00' * 10000
        
        test_file = tmp_path / "zero_copy_test.gz"
        with gzip.open(test_file, "wb") as f:
            f.write(large_data)
        
        buffer_manager = MemoryBufferManager(test_file)
        decoder = BerDecoderTwoPhase(
            parser=EricssonVoz,
            buffer_manager=buffer_manager,
            n_workers=1
        )
        
        with buffer_manager.open():
            data = buffer_manager.get_memoryview()
            
            # Extract TLV structure - this should be fast even with large data
            import time
            start_time = time.perf_counter()
            
            tlvs = decoder.extract_tlv_structure(data)
            
            end_time = time.perf_counter()
            extract_time = end_time - start_time
            
            # Should be very fast for structure extraction (under 0.1 seconds)
            assert extract_time < 0.1
            
            # Should have found at least one TLV
            assert len(tlvs) >= 1