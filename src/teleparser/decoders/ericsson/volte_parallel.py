"""EricssonVolte decoder with parallel block processing optimization.

This module implements parallel processing of Diameter blocks to utilize
multiple CPU cores for improved performance on files with multiple messages.
"""

import struct
from datetime import datetime, timedelta
from typing import Generator, Tuple, List
import socket
from concurrent.futures import ThreadPoolExecutor, as_completed
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


class EricssonVolteParallel:
    """EricssonVolte decoder with parallel block processing optimizations."""
    
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

    @staticmethod
    def parse_block(block: bytes) -> dict[str, int | str | bool]:
        """Parse a single block (same logic as original)."""
        parsed_blocks = []
        while block:
            avp, offset = EricssonVolteParallel.parse_avp(block)
            block = block[offset:]
            parsed_blocks.append(avp)
        return {k: v for block in parsed_blocks for k, v in block.items()}

    @staticmethod
    def parse_avp(current_block: memoryview | bytes) -> Tuple:
        """Parse a single AVP (same logic as original)."""
        i = 0
        header_size = 8
        
        while True:
            # Parse AVP header (8 bytes)
            if (offset := len(current_block[i:])) < 8:
                return {}, offset  # Not enough data for AVP header

            avp_code = int.from_bytes(current_block[i : i + 4], byteorder="big")
            if not (avp_def := AVP_DB.get(avp_code)):
                i += 1
                continue  # Slide window if AVP code is unknown
                
            flags = current_block[i + 4]
            avp_length = int.from_bytes(current_block[i + 5 : i + 8], byteorder="big")
            
            if len(current_block[i:]) < avp_length or avp_length < 8:
                i += 1
                continue  # Slide window if AVP length is invalid
            
            # Handle vendor flag
            if flags & 0x80:  # Vendor flag set
                if avp_length < 12:
                    i += 1
                    continue  # Slide window if AVP length is less than 12 bytes
                header_size = 12

            # Fast size validation
            if (known_size := KNOWN_SIZES.get(avp_def.type)) is not None:
                if avp_length - header_size != known_size:
                    i += 1
                    continue  # Slide window if AVP length does not match known size
            break

        offset: int = i + avp_length

        # Fast flags validation
        if not is_avp_flag_valid(flags, avp_def.acr_flag):
            return {}, offset  # Invalid AVP flags, skip this AVP

        value_data: bytes = bytes(current_block[i + header_size : i + avp_length])

        if (avp_type := avp_def.type) == TYPE_GROUPED:
            avps, offset = EricssonVolteParallel.parse_grouped_avp(value_data)
            if not avps:
                return {}, offset
            return EricssonVolteParallel.flatten_avp(avp_def.avp, avps), offset
        else:
            return {
                avp_def.avp: EricssonVolteParallel.parse_simple_value(value_data, avp_type),
            }, offset

    @staticmethod
    def parse_grouped_avp(binary_data: bytes | bytes) -> Tuple[list, int]:
        """Parse a grouped AVP (same logic as original)."""
        avps = []
        current_block = binary_data
        total_offset = 0
        
        while current_block:
            avp, offset = EricssonVolteParallel.parse_avp(current_block)
            current_block = current_block[offset:]  # Move to next AVP
            if avp:
                avps.append(avp)
            total_offset += offset
            
        if len(avps) == 1:
            avps = avps[0]  # If only one AVP, return it directly
        return avps, total_offset

    @staticmethod
    def flatten_avp(prefix: str, avp: dict | list) -> dict:
        """Flatten AVP (same logic as original)."""
        flattened_avp = {}
        if isinstance(avp, dict):
            for key, value in avp.items():
                if not isinstance(value, (dict, list)):
                    if previous_value := flattened_avp.get(key):
                        value = f"{previous_value};{value}"  # Concatenate values
                    flattened_avp[key] = value
                if isinstance(value, dict):
                    flattened_avp.update(EricssonVolteParallel.flatten_avp(key, value))
                elif isinstance(value, list):
                    for item in value:
                        flattened_avp.update(EricssonVolteParallel.flatten_avp(key, item))
        elif isinstance(avp, list):
            for item in avp:
                flattened_avp.update(EricssonVolteParallel.flatten_avp(prefix, item))
        return flattened_avp

    @staticmethod
    def parse_simple_value(binary_view: bytes, avp_type: int) -> str | int:
        """Parse a simple AVP value (same logic as original)."""
        if avp_type in (TYPE_OCTET_STRING, TYPE_UTF8_STRING, TYPE_DIAMETER_IDENTITY):
            try:
                return binary_view.decode("utf-8").rstrip('\x00')
            except UnicodeDecodeError:
                # If decoding fails, return string representation of raw bytes
                return binary_view.hex()
        elif avp_type == TYPE_TIME:
            seconds = STRUCT_UNSIGNED_32.unpack(binary_view)[0]
            return (EricssonVolteParallel.NTP_EPOCH + timedelta(seconds=seconds)).strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        elif avp_type in (TYPE_ENUMERATED, TYPE_INTEGER_32):
            # Enumerated and Integer 32 are both 4-byte signed integers
            return STRUCT_SIGNED_32.unpack(binary_view)[0]
        elif avp_type == TYPE_ADDRESS:
            # Address format: 2 byte family + address bytes
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
            return STRUCT_UNSIGNED_32.unpack(binary_view)[0]
        elif avp_type == TYPE_UNSIGNED_64:
            return STRUCT_UNSIGNED_64.unpack(binary_view)[0]
        else:
            return binary_view.hex()  # Fallback for unknown types

    def extract_all_blocks(self) -> List[bytes]:
        """Extract all blocks from the binary data for parallel processing."""
        blocks = []
        idx = 0
        length = self.length
        
        while idx < length:
            start_idx, stop_idx, error = self.slice_next_block(idx)
            if not error:
                blocks.append(bytes(self.binary_data[start_idx:stop_idx]))
            idx = stop_idx
        
        return blocks

    def avps_parallel(self) -> Generator[dict[str, int | str | bool], None, None]:
        """Parse all blocks using parallel processing."""
        blocks = self.extract_all_blocks()
        
        if len(blocks) == 0:
            return
        
        # If only one block or few blocks, use sequential processing
        if len(blocks) < self.n_workers or len(blocks) < 2:
            for block in blocks:
                yield self.parse_block(block)
            return
        
        # Parallel processing for multiple blocks
        with ThreadPoolExecutor(max_workers=self.n_workers) as executor:
            # Submit all block parsing tasks
            future_to_block = {
                executor.submit(self.parse_block, block): i 
                for i, block in enumerate(blocks)
            }
            
            # Collect results in order
            results = [None] * len(blocks)
            for future in as_completed(future_to_block):
                block_index = future_to_block[future]
                try:
                    results[block_index] = future.result()
                except Exception as e:
                    print(f"Error processing block {block_index}: {e}")
                    results[block_index] = {}
            
            # Yield results in original order
            for result in results:
                if result:
                    yield result

    def avps(self) -> Generator[dict[str, int | str | bool], None, None]:
        """Parse all blocks (choose between parallel and sequential based on block count)."""
        return self.avps_parallel()

    def blocks(self) -> Generator[bytes, None, None]:
        """Generator to yield sliced blocks from binary data (for compatibility)."""
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
        end_idx = index + EricssonVolteParallel.HEADER_SIZE
        header = self.binary_data[index:end_idx]

        # Validate minimum length
        if len(header) < EricssonVolteParallel.HEADER_SIZE:
            index += len(header)  # Skip this block
            return index, index, True

        # Unpack all header fields
        (version, msg_len_bytes, flag_int, cmd_bytes, app_id, hbh_id, e2e_id) = (
            EricssonVolteParallel.DIAMETER_HEADER_FORMAT.unpack(header)
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
        
        start_idx = index + EricssonVolteParallel.HEADER_SIZE
        index = index + msg_length  # msg_length includes the header
        return start_idx, index, False

    def process(self, pbar_position=None, show_progress=True):
        """Process the VoLTE data and return a list of parsed AVPs."""
        if show_progress:
            return list(
                tqdm(
                    self.avps(),
                    desc=f"  ↳ Parsing AVPs (parallel {self.n_workers}w)",
                    unit=" block",
                    leave=False,
                    position=pbar_position,
                    colour="yellow",
                )
            )
        else:
            return list(self.avps())

    @staticmethod
    def insert_vendor_info(blocks):
        """Insert vendor information into blocks (same as original)."""
        # Import the original function to maintain compatibility
        from teleparser.decoders.ericsson.volte import EricssonVolte
        return EricssonVolte.insert_vendor_info(blocks)

    @staticmethod
    def transform_func(blocks):
        """Transform function that applies vendor information enrichment."""
        return EricssonVolteParallel.insert_vendor_info(blocks)

    def get_stats(self):
        """Get parallel processing statistics."""
        blocks = self.extract_all_blocks()
        return {
            "total_blocks": len(blocks),
            "n_workers": self.n_workers,
            "parallel_enabled": len(blocks) >= self.n_workers and len(blocks) >= 2,
            "avg_block_size": sum(len(block) for block in blocks) / len(blocks) if blocks else 0
        }