"""EricssonVolte decoder with two-phase AVP processing optimization.

This module implements a two-phase approach to AVP processing:
1. Phase 1: Extract AVP structure without interpretation (fast, non-recursive)
2. Phase 2: Interpret values (parallelizable)

This approach eliminates recursion and enables parallel processing of AVPs.
"""

import struct
from datetime import datetime, timedelta
from typing import Generator, Tuple, List
from dataclasses import dataclass
import socket
from concurrent.futures import ThreadPoolExecutor
from functools import partial
from tqdm.auto import tqdm

from teleparser.decoders.ericsson.volte import (
    VendorID, AVP_DB, is_avp_flag_valid,
    # Constants
    VENDOR_3GPP, VENDOR_ERICSSON, VENDOR_HUAWEI,
    TYPE_OCTET_STRING, TYPE_INTEGER_32, TYPE_UNSIGNED_32, TYPE_UNSIGNED_64,
    TYPE_UTF8_STRING, TYPE_GROUPED, TYPE_TIME, TYPE_ENUMERATED,
    TYPE_DIAMETER_IDENTITY, TYPE_ADDRESS,
    STRUCT_UNSIGNED_32, STRUCT_SIGNED_32, STRUCT_UNSIGNED_64, KNOWN_SIZES
)


@dataclass
class AVPTriple:
    """Lightweight AVP representation for phase 1 processing."""
    __slots__ = ['code', 'flags', 'length', 'value_start', 'value_end', 
                 'vendor_id', 'parent_idx', 'depth', 'block_offset']
    
    code: int
    flags: int
    length: int
    value_start: int     # Position of value in block data
    value_end: int       # End position of value
    vendor_id: int | None
    parent_idx: int      # Index of parent AVP (-1 for root)
    depth: int          # Nesting depth
    block_offset: int   # Offset within the block for debugging


class EricssonVolteTwoPhase:
    """EricssonVolte decoder with two-phase AVP processing optimizations."""
    
    DIAMETER_HEADER_FORMAT = struct.Struct(">B3sB3sIII")  # Big-endian format
    HEADER_SIZE = 20  # Fixed 20-byte header
    NTP_EPOCH = datetime(1900, 1, 1)  # For timestamp conversion
    PREFIX_HEADER_LENGTH = 2

    def __init__(self, buffer_manager, n_workers=None):
        self.buffer_manager = buffer_manager
        # Default to CPU count - 1, or at least 1 worker
        if n_workers is None:
            import os
            self.n_workers = max(1, os.cpu_count() - 1)
        else:
            self.n_workers = max(1, n_workers)
        self._init_handler()
        self.index = 0

    def _init_handler(self) -> None:
        """Initialize the handler for parsing AVPs"""
        with self.buffer_manager.open() as file_buffer:
            self.binary_data = memoryview(file_buffer.read())
        self.length = len(self.binary_data)

    def extract_avp_structure(self, block: bytes) -> List[AVPTriple]:
        """Phase 1: Extract all AVP structures in a single pass without interpretation."""
        avps = []
        # Stack entries: (start, end, parent_idx, depth)
        stack = [(0, len(block), -1, 0)]
        
        while stack:
            pos, end_pos, parent_idx, depth = stack.pop()
            
            while pos < end_pos:
                block_offset = pos
                
                # Need at least 8 bytes for AVP header
                if pos + 8 > end_pos:
                    break
                
                # Parse AVP header
                code = int.from_bytes(block[pos:pos+4], byteorder="big")
                flags = block[pos+4]
                length = int.from_bytes(block[pos+5:pos+8], byteorder="big")
                
                # Handle vendor ID
                vendor_id = None
                header_size = 8
                if flags & 0x80:  # Vendor flag set
                    if pos + 12 <= end_pos and length >= 12:
                        vendor_id = int.from_bytes(block[pos+8:pos+12], byteorder="big")
                        header_size = 12
                    else:
                        pos += 1  # Skip malformed AVP
                        continue
                
                # Validate AVP
                if length < header_size or pos + length > end_pos:
                    pos += 1  # Skip malformed AVP
                    continue
                
                # Store AVP info
                current_idx = len(avps)
                avps.append(AVPTriple(
                    code=code,
                    flags=flags,
                    length=length,
                    value_start=pos + header_size,
                    value_end=pos + length,
                    vendor_id=vendor_id,
                    parent_idx=parent_idx,
                    depth=depth,
                    block_offset=block_offset
                ))
                
                # Schedule grouped AVP processing
                if code in self.get_grouped_avp_codes():
                    stack.append((pos + header_size, pos + length, current_idx, depth + 1))
                
                pos += length
        
        return avps

    def get_grouped_avp_codes(self) -> set:
        """Get set of grouped AVP codes for efficient lookup."""
        # Cache this to avoid repeated computation
        if not hasattr(self, '_grouped_avp_codes'):
            self._grouped_avp_codes = {
                code for code, avp_def in AVP_DB.items() 
                if avp_def.type == TYPE_GROUPED
            }
        return self._grouped_avp_codes

    def interpret_avp_batch(
        self, 
        avps: List[AVPTriple], 
        block: bytes, 
        start_idx: int, 
        end_idx: int
    ) -> dict:
        """Phase 2: Interpret a batch of AVPs in parallel."""
        results = {}
        
        for i in range(start_idx, min(end_idx, len(avps))):
            avp = avps[i]
            
            # Skip grouped AVPs (processed by structure)
            if avp.code in self.get_grouped_avp_codes():
                continue
                
            # Get AVP definition
            avp_def = AVP_DB.get(avp.code)
            if not avp_def:
                continue
            
            # Validate flags
            if not is_avp_flag_valid(avp.flags, avp_def.acr_flag):
                continue
                
            # Parse value
            value_data = bytes(block[avp.value_start:avp.value_end])
            parsed_value = self.parse_simple_value(value_data, avp_def.type)
            
            if parsed_value is not None:
                results[avp_def.avp] = parsed_value
        
        return results

    def parallel_interpret(self, avps: List[AVPTriple], block: bytes) -> dict:
        """Phase 2: Interpret AVP values using parallel processing."""
        if not avps:
            return {}
        
        # Find leaf (non-grouped) AVPs for parallel processing
        leaf_indices = [
            i for i, avp in enumerate(avps) 
            if avp.code not in self.get_grouped_avp_codes()
        ]
        
        if not leaf_indices:
            return {}
        
        # Create batches for parallel processing
        if len(leaf_indices) < self.n_workers:
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
                    lambda batch: self.interpret_avp_batch(avps, block, batch[0], batch[1]),
                    batches
                ))
        else:
            # Sequential processing for small datasets
            batch_results = [
                self.interpret_avp_batch(avps, block, batch[0], batch[1])
                for batch in batches
            ]
        
        # Merge results
        merged_results = {}
        for batch_result in batch_results:
            merged_results.update(batch_result)
        
        return merged_results

    def parse_block(self, block: bytes) -> dict[str, int | str | bool]:
        """Parse a block using two-phase approach."""
        # Phase 1: Extract AVP structure (fast, non-recursive)
        avps = self.extract_avp_structure(block)
        
        # Phase 2: Parallel interpretation
        results = self.parallel_interpret(avps, block)
        
        return results

    def parse_simple_value(self, binary_view: bytes, avp_type: int) -> str | int:
        """Parse a simple AVP value (same logic as original)."""
        if avp_type in (TYPE_OCTET_STRING, TYPE_UTF8_STRING, TYPE_DIAMETER_IDENTITY):
            try:
                return binary_view.decode("utf-8").rstrip('\x00')
            except UnicodeDecodeError:
                return binary_view.hex()
        elif avp_type == TYPE_TIME:
            if len(binary_view) >= 4:
                seconds = STRUCT_UNSIGNED_32.unpack(binary_view[:4])[0]
                return (EricssonVolteTwoPhase.NTP_EPOCH + timedelta(seconds=seconds)).strftime(
                    "%Y-%m-%d %H:%M:%S"
                )
            return binary_view.hex()
        elif avp_type in (TYPE_ENUMERATED, TYPE_INTEGER_32):
            if len(binary_view) >= 4:
                return STRUCT_SIGNED_32.unpack(binary_view[:4])[0]
            return binary_view.hex()
        elif avp_type == TYPE_ADDRESS:
            if len(binary_view) < 2:
                return binary_view.hex()
            family = int.from_bytes(binary_view[:2], 'big')
            address_bytes = binary_view[2:]
            try:
                if family == 1:  # IPv4
                    return socket.inet_ntoa(address_bytes)
                elif family == 2:  # IPv6
                    return socket.inet_ntop(socket.AF_INET6, address_bytes)
                else:
                    return binary_view.decode("utf-8", errors='replace')
            except (socket.error, UnicodeDecodeError):
                return binary_view.hex()
        elif avp_type == TYPE_UNSIGNED_32:
            if len(binary_view) >= 4:
                return STRUCT_UNSIGNED_32.unpack(binary_view[:4])[0]
            return binary_view.hex()
        elif avp_type == TYPE_UNSIGNED_64:
            if len(binary_view) >= 8:
                return STRUCT_UNSIGNED_64.unpack(binary_view[:8])[0]
            return binary_view.hex()
        else:
            return binary_view.hex()

    def avps(self) -> Generator[dict[str, int | str | bool], None, None]:
        """Parse all blocks in the binary data"""
        return (self.parse_block(block) for block in self.blocks())

    def blocks(self) -> Generator[bytes, None, None]:
        """Generator to yield sliced blocks from binary data"""
        idx = 0
        length = self.length
        while idx < length:
            start_idx, stop_idx, error = self.slice_next_block(idx)
            if not error:
                yield self.binary_data[start_idx:stop_idx]
            idx = stop_idx

    def slice_next_block(self, index: int) -> Tuple[int, int, bool]:
        """Parse Diameter header using the same logic as original"""
        index += 2  # Skip first 2 bytes
        end_idx = index + EricssonVolteTwoPhase.HEADER_SIZE
        header = self.binary_data[index:end_idx]

        # Validate minimum length
        if len(header) < EricssonVolteTwoPhase.HEADER_SIZE:
            index += len(header)  # Skip this block
            return index, index, True

        # Unpack all header fields
        (version, msg_len_bytes, flag_int, cmd_bytes, app_id, hbh_id, e2e_id) = (
            EricssonVolteTwoPhase.DIAMETER_HEADER_FORMAT.unpack(header)
        )

        # Convert 24-bit fields
        msg_length = int.from_bytes(msg_len_bytes)

        # Validate version (MUST be 1)
        if version != 1:
            raise ValueError(f"Invalid Diameter version: {version} (must be 1)")

        # Validate message type
        if cmd_bytes != b"\x00\x01\x0f":
            raise ValueError(
                f"Invalid Command-Code: {int.from_bytes(cmd_bytes)} (expected 271 for accounting)"
            )
        
        start_idx = index + EricssonVolteTwoPhase.HEADER_SIZE
        index = index + msg_length  # msg_length includes the header
        return start_idx, index, False

    def process(self, pbar_position=None, show_progress=True):
        """Process the VoLTE data and return a list of parsed AVPs."""
        if show_progress:
            return list(
                tqdm(
                    self.avps(),
                    desc=f"  ↳ Parsing AVPs (two-phase {self.n_workers}w)",
                    unit=" block",
                    leave=False,
                    position=pbar_position,
                    colour="magenta",
                )
            )
        else:
            return list(self.avps())

    @staticmethod
    def insert_vendor_info(blocks):
        """Insert vendor information into blocks (same as original)."""
        from teleparser.decoders.ericsson.volte import EricssonVolte
        return EricssonVolte.insert_vendor_info(blocks)

    @staticmethod
    def transform_func(blocks):
        """Transform function that applies vendor information enrichment."""
        return EricssonVolteTwoPhase.insert_vendor_info(blocks)

    def get_stats(self):
        """Get two-phase processing statistics."""
        # Extract first block for analysis
        first_block = next(self.blocks(), b'')
        if not first_block:
            return {"avps_extracted": 0, "grouped_avps": 0, "leaf_avps": 0}
        
        avps = self.extract_avp_structure(first_block)
        grouped_codes = self.get_grouped_avp_codes()
        grouped_avps = sum(1 for avp in avps if avp.code in grouped_codes)
        leaf_avps = len(avps) - grouped_avps
        
        return {
            "avps_extracted": len(avps),
            "grouped_avps": grouped_avps, 
            "leaf_avps": leaf_avps,
            "n_workers": self.n_workers,
            "grouped_avp_codes": len(grouped_codes)
        }