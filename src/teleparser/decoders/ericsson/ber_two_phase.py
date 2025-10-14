"""Two-Phase BER Decoder - Prototype Implementation

This module implements a two-phase approach to BER decoding:
1. Phase 1: Extract TLV structure without interpretation (fast)
2. Phase 2: Interpret values (parallelizable)
"""

from dataclasses import dataclass
from collections import namedtuple
from typing import Optional, Tuple, Callable, List
from concurrent.futures import ThreadPoolExecutor
from functools import partial
import time

from tqdm.auto import tqdm
from teleparser.buffer import MemoryBufferManager
from teleparser.decoders.ericsson.fieldnames import ERICSSON_VOZ_FIELDS
from teleparser.decoders.ericsson.ber_optimized import (
    BerDecoderOptimized, BerTag, EOC,
    CLASS_SHIFT, TWO_BIT_MASK, ENCODE_SHIFT, MODULO_2, CLASSNUM_MASK,
    MASK_BIT7, SHIFT_7, HIGH_CLASS_NUM, MASK_BIT8, SHIFT_8
)


@dataclass
class TLVTriple:
    """Lightweight TLV representation for phase 1"""
    __slots__ = ['tag_class', 'constructed', 'tag_number', 'value_start', 
                 'value_length', 'depth', 'parent_idx', 'tlv_start']
    
    tag_class: int
    constructed: bool
    tag_number: int
    value_start: int    # Position of value in memoryview
    value_length: int
    depth: int
    parent_idx: int     # Index of parent TLV (-1 for root)
    tlv_start: int     # Position where TLV starts (for debugging)


@dataclass
class BerDecoderTwoPhase:
    """Two-phase BER decoder for optimal performance.
    
    Phase 1: Extract all TLV structures in one pass (no recursion)
    Phase 2: Interpret values in parallel
    """

    parser: Callable
    buffer_manager: MemoryBufferManager
    FIELDNAMES: set = None
    n_workers: int = 4
    
    def __post_init__(self):
        """Initialize the decoder."""
        if self.FIELDNAMES is None:
            self.FIELDNAMES = ERICSSON_VOZ_FIELDS
    
    def extract_tlv_structure(self, data: memoryview) -> List[TLVTriple]:
        """Phase 1: Extract ALL TLVs in a single pass without interpretation.
        
        Returns:
            List of TLVTriple objects representing the complete TLV structure
        """
        tlvs = []
        # Stack entries: (start_pos, end_pos, depth, parent_idx)
        stack = [(0, len(data), 0, -1)]
        
        while stack:
            pos, end_pos, depth, parent_idx = stack.pop()
            
            while pos < end_pos:
                tlv_start = pos
                
                # Read tag
                tag_bytes, tag_len = BerDecoderOptimized.read_tag(data, pos)
                if tag_bytes is None:
                    break
                pos += tag_len
                
                # Decode tag
                tag = BerDecoderOptimized.decode_tag(tag_bytes)
                
                # Read length
                try:
                    length, len_bytes = BerDecoderOptimized.read_length(data, pos)
                except ValueError:
                    # Malformed length, skip this TLV
                    break
                pos += len_bytes
                
                # Handle EOC or zero-length
                if BerDecoderOptimized.reached_eoc(tag, length):
                    if length == 0:
                        continue  # Skip EOC markers
                    # For indefinite length, we'd need special handling
                    # For now, treat as regular TLV
                
                # Check if we have enough data for the value
                if pos + length > len(data):
                    # Not enough data, possibly truncated file
                    break
                
                # Store TLV triple
                current_idx = len(tlvs)
                tlvs.append(TLVTriple(
                    tag_class=tag.tag_class,
                    constructed=tag.constructed,
                    tag_number=tag.number,
                    value_start=pos,
                    value_length=length,
                    depth=depth,
                    parent_idx=parent_idx,
                    tlv_start=tlv_start
                ))
                
                # Schedule children for constructed types
                if tag.constructed and length > 0:
                    stack.append((pos, pos + length, depth + 1, current_idx))
                
                pos += length
        
        return tlvs
    
    def get_schema_for_tlv(self, tlvs: List[TLVTriple], tlv_idx: int) -> dict:
        """Get the appropriate schema for a TLV based on its parent hierarchy."""
        tlv = tlvs[tlv_idx]
        
        if tlv.parent_idx == -1:
            # Root level - use main schema
            return None
        
        # Walk up the parent chain to find the right schema context
        # This is a simplified version - in practice, you'd need to
        # implement the full schema resolution logic
        parent_tlv = tlvs[tlv.parent_idx]
        
        # For now, return None (will use root schema in parser)
        # TODO: Implement full schema traversal
        return None
    
    def interpret_tlv_batch(
        self, 
        tlvs: List[TLVTriple], 
        data: memoryview, 
        start_idx: int, 
        end_idx: int
    ) -> dict:
        """Interpret a batch of TLVs in parallel.
        
        Args:
            tlvs: List of all TLVs
            data: Raw data memoryview
            start_idx: Start index in tlvs list
            end_idx: End index in tlvs list
            
        Returns:
            Dictionary of parsed field names and values
        """
        results = {}
        
        for i in range(start_idx, end_idx):
            if i >= len(tlvs):
                break
                
            tlv = tlvs[i]
            
            # Skip constructed types - their values come from children
            if tlv.constructed:
                continue
            
            # Extract value from memoryview (zero-copy)
            if tlv.value_length == 0:
                continue
                
            try:
                value = bytes(data[tlv.value_start:tlv.value_start + tlv.value_length])
                
                # Get appropriate schema based on parent
                schema = self.get_schema_for_tlv(tlvs, i)
                
                # Parse the value
                parsed = self.parser(tlv.tag_number, value, schema)
                
                if parsed.value is not None:
                    if isinstance(parsed.value, dict):
                        # Flatten nested dictionaries
                        for k, v in parsed.value.items():
                            results[f"{parsed.name}.{k}"] = v
                    else:
                        results[parsed.name] = parsed.value
                        
            except (KeyError, ValueError, AttributeError) as e:
                # Unknown tag or parsing error - skip silently
                # In production, you might want to log this
                continue
        
        return results
    
    def parallel_interpret(
        self, 
        tlvs: List[TLVTriple], 
        data: memoryview
    ) -> List[dict]:
        """Phase 2: Interpret TLV values in parallel.
        
        Args:
            tlvs: List of TLV structures from phase 1
            data: Raw data memoryview
            
        Returns:
            List of parsed records
        """
        if not tlvs:
            return []
        
        # Find leaf (non-constructed) TLVs for parallel processing
        leaf_indices = [i for i, tlv in enumerate(tlvs) if not tlv.constructed]
        
        if not leaf_indices:
            return []
        
        # Create batches for parallel processing
        if len(leaf_indices) < self.n_workers:
            # Not enough work for parallelization
            batch_size = len(leaf_indices)
            n_workers = 1
        else:
            batch_size = max(1, len(leaf_indices) // self.n_workers)
            n_workers = self.n_workers
        
        batches = []
        for i in range(0, len(leaf_indices), batch_size):
            batch_indices = leaf_indices[i:i + batch_size]
            if batch_indices:
                batches.append((min(batch_indices), max(batch_indices) + 1))
        
        # Process batches in parallel
        if n_workers > 1:
            with ThreadPoolExecutor(max_workers=n_workers) as executor:
                batch_results = list(executor.map(
                    lambda batch: self.interpret_tlv_batch(tlvs, data, batch[0], batch[1]),
                    batches
                ))
        else:
            # Sequential processing for small datasets
            batch_results = [
                self.interpret_tlv_batch(tlvs, data, batch[0], batch[1])
                for batch in batches
            ]
        
        # Group results by record (top-level TLVs)
        records = []
        
        # Find root-level TLVs (depth 0)
        root_tlvs = [i for i, tlv in enumerate(tlvs) if tlv.depth == 0]
        
        for root_idx in root_tlvs:
            record = {}
            
            # Collect all parsed fields for this record
            # In a more sophisticated implementation, you'd need to
            # properly associate child TLVs with their parent records
            for batch_result in batch_results:
                record.update(batch_result)
            
            if record:
                records.append(record)
        
        return records
    
    def parse_blocks(self):
        """Parse all blocks using two-phase approach."""
        with self.buffer_manager.open():
            data = self.buffer_manager.get_memoryview()
            
            if len(data) == 0:
                return
            
            # Phase 1: Extract TLV structure (fast, single-threaded)
            start_time = time.perf_counter()
            tlvs = self.extract_tlv_structure(data)
            phase1_time = time.perf_counter() - start_time
            
            # Phase 2: Parallel interpretation
            start_time = time.perf_counter()
            records = self.parallel_interpret(tlvs, data)
            phase2_time = time.perf_counter() - start_time
            
            # Optional: Print timing info for benchmarking
            # print(f"Phase 1 (structure): {phase1_time:.4f}s, Phase 2 (interpret): {phase2_time:.4f}s")
            
            for record in records:
                yield record
    
    def process(self, pbar_position=None, show_progress=True):
        """Process the BER data and return a list of parsed blocks.
        
        Args:
            pbar_position: Position for nested progress bar
            show_progress: Whether to show progress bar
        """
        if show_progress:
            return list(
                tqdm(
                    self.parse_blocks(),
                    desc="  ↳ Parsing TLVs (2-phase)",
                    unit=" block",
                    leave=False,
                    position=pbar_position,
                    colour="green",
                )
            )
        else:
            return list(self.parse_blocks())
    
    @property
    def transform_func(self):
        """Placeholder for compatibility."""
        return None


def ericsson_voz_decoder_two_phase(buffer_manager: MemoryBufferManager, n_workers: int = 4):
    """Create a two-phase BER decoder for Ericsson VOZ records.
    
    Args:
        buffer_manager: Memory buffer manager for the input file
        n_workers: Number of worker threads for parallel interpretation
        
    Returns:
        Configured two-phase BER decoder
    """
    from teleparser.decoders.ericsson.voz import EricssonVoz
    
    return BerDecoderTwoPhase(
        parser=EricssonVoz,
        buffer_manager=buffer_manager,
        FIELDNAMES=ERICSSON_VOZ_FIELDS,
        n_workers=n_workers
    )