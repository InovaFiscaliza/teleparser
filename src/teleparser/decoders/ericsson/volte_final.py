"""Final optimized EricssonVolte decoder.

This implementation combines the most effective optimizations while avoiding 
overhead-heavy approaches like excessive parallelization for small AVPs.

Optimizations included:
1. Streamlined AVP parsing with reduced function call overhead
2. Improved flag validation
3. Better memory usage patterns
4. Optimized string handling
"""

import struct
from datetime import datetime, timedelta
from typing import Generator, Tuple
import socket
from tqdm.auto import tqdm

from teleparser.decoders.ericsson.volte import (
    AVP_DB, 
    # Constants
    TYPE_OCTET_STRING, TYPE_INTEGER_32, TYPE_UNSIGNED_32, TYPE_UNSIGNED_64,
    TYPE_UTF8_STRING, TYPE_GROUPED, TYPE_TIME, TYPE_ENUMERATED,
    TYPE_DIAMETER_IDENTITY, TYPE_ADDRESS,
    STRUCT_UNSIGNED_32, STRUCT_SIGNED_32, STRUCT_UNSIGNED_64, KNOWN_SIZES
)


class EricssonVolteFinal:
    """Final optimized EricssonVolte decoder with selected optimizations."""
    
    DIAMETER_HEADER_FORMAT = struct.Struct(">B3sB3sIII")  # Big-endian format
    HEADER_SIZE = 20  # Fixed 20-byte header
    NTP_EPOCH = datetime(1900, 1, 1)  # For timestamp conversion
    PREFIX_HEADER_LENGTH = 2

    def __init__(self, buffer_manager):
        self.buffer_manager = buffer_manager
        self._init_handler()
        self.index = 0

    def _init_handler(self) -> None:
        """Initialize the handler for parsing AVPs"""
        with self.buffer_manager.open() as file_buffer:
            self.binary_data = memoryview(file_buffer.read())
        self.length = len(self.binary_data)

    @staticmethod
    def parse_block(block: bytes) -> dict[str, int | str | bool]:
        """Parse a block using optimized approach."""
        result = {}
        pos = 0
        block_len = len(block)
        
        while pos < block_len:
            avp_data, offset = EricssonVolteFinal.parse_avp_optimized(block, pos)
            if avp_data:
                result.update(avp_data)
            pos += offset
            if offset == 0:  # Prevent infinite loop
                break
        
        return result

    @staticmethod 
    def parse_avp_optimized(block: bytes, start_pos: int) -> Tuple[dict, int]:
        """Optimized AVP parsing with reduced overhead."""
        pos = start_pos
        block_len = len(block)
        
        # Sliding window search with optimizations
        for attempt in range(min(100, block_len - pos)):  # Limit search attempts
            i = pos + attempt
            
            # Check if we have enough data for AVP header
            if i + 8 > block_len:
                return {}, block_len - pos
                
            # Parse AVP header
            avp_code = int.from_bytes(block[i:i+4], byteorder="big")
            
            # Fast lookup - exit early if unknown
            avp_def = AVP_DB.get(avp_code)
            if not avp_def:
                continue
                
            flags = block[i + 4]
            avp_length = int.from_bytes(block[i + 5:i + 8], byteorder="big")
            
            # Validate basic constraints
            if avp_length < 8 or i + avp_length > block_len:
                continue
            
            # Handle vendor flag
            header_size = 8
            if flags & 0x80:  # Vendor flag set
                if avp_length < 12:
                    continue
                header_size = 12

            # Fast size validation for known types
            known_size = KNOWN_SIZES.get(avp_def.type)
            if known_size is not None and avp_length - header_size != known_size:
                continue
            
            # Fast flags validation
            if not EricssonVolteFinal.validate_flags_fast(flags, avp_def.acr_flag):
                continue
                
            # Parse value
            value_start = i + header_size
            value_end = i + avp_length
            value_data = block[value_start:value_end]
            
            # Handle different AVP types
            if avp_def.type == TYPE_GROUPED:
                # Recursive parsing for grouped AVPs
                nested_avp = EricssonVolteFinal.parse_grouped_avp_optimized(value_data)
                flattened = EricssonVolteFinal.flatten_avp_fast(avp_def.avp, nested_avp)
                return flattened, avp_length + attempt
            else:
                # Parse simple value
                parsed_value = EricssonVolteFinal.parse_simple_value_fast(value_data, avp_def.type)
                return {avp_def.avp: parsed_value}, avp_length + attempt
        
        # No valid AVP found
        return {}, block_len - pos

    @staticmethod
    def validate_flags_fast(flags: int, expected_flags: str | None) -> bool:
        """Fast flags validation."""
        if expected_flags is None:
            return True
            
        # Check reserved bits
        if flags & 0x1F != 0:
            return False
            
        # Simple flag checking
        expected_v = 'V' in expected_flags if expected_flags else False
        expected_m = 'M' in expected_flags if expected_flags else False 
        expected_p = 'P' in expected_flags if expected_flags else False
        
        actual_v = bool(flags & 0x80)
        actual_m = bool(flags & 0x40)
        actual_p = bool(flags & 0x20)
        
        # Allow more flags than expected, but require expected ones
        if expected_v and not actual_v:
            return False
        if expected_m and not actual_m:
            return False
        if expected_p and not actual_p:
            return False
            
        return True

    @staticmethod
    def parse_grouped_avp_optimized(binary_data: bytes) -> dict:
        """Parse grouped AVP with reduced overhead."""
        result = {}
        pos = 0
        
        while pos < len(binary_data):
            avp_data, offset = EricssonVolteFinal.parse_avp_optimized(binary_data, pos)
            if avp_data:
                result.update(avp_data)
            pos += offset
            if offset == 0:
                break
                
        return result

    @staticmethod
    def flatten_avp_fast(prefix: str, avp: dict | list) -> dict:
        """Fast AVP flattening with minimal allocations."""
        if isinstance(avp, dict):
            result = {}
            for key, value in avp.items():
                if isinstance(value, (dict, list)):
                    nested = EricssonVolteFinal.flatten_avp_fast(key, value)
                    result.update(nested)
                else:
                    # Handle duplicate keys by concatenation
                    if key in result:
                        result[key] = f"{result[key]};{value}"
                    else:
                        result[key] = value
            return result
        elif isinstance(avp, list):
            result = {}
            for item in avp:
                nested = EricssonVolteFinal.flatten_avp_fast(prefix, item)
                result.update(nested)
            return result
        else:
            return {prefix: avp}

    @staticmethod
    def parse_simple_value_fast(binary_view: bytes, avp_type: int) -> str | int:
        """Fast simple value parsing with optimizations."""
        
        # String types - optimized path
        if avp_type in (TYPE_OCTET_STRING, TYPE_UTF8_STRING, TYPE_DIAMETER_IDENTITY):
            try:
                # Strip null bytes directly 
                result = binary_view.decode("utf-8")
                return result.rstrip('\x00') if '\x00' in result else result
            except UnicodeDecodeError:
                return binary_view.hex()
                
        # Time type - optimized path
        elif avp_type == TYPE_TIME:
            if len(binary_view) >= 4:
                seconds = STRUCT_UNSIGNED_32.unpack(binary_view[:4])[0]
                # Cache the epoch calculation would be even better, but this is still fast
                return (EricssonVolteFinal.NTP_EPOCH + timedelta(seconds=seconds)).strftime(
                    "%Y-%m-%d %H:%M:%S"
                )
            return binary_view.hex()
            
        # Integer types - direct struct unpack
        elif avp_type in (TYPE_ENUMERATED, TYPE_INTEGER_32):
            if len(binary_view) >= 4:
                return STRUCT_SIGNED_32.unpack(binary_view[:4])[0]
            return binary_view.hex()
            
        elif avp_type == TYPE_UNSIGNED_32:
            if len(binary_view) >= 4:
                return STRUCT_UNSIGNED_32.unpack(binary_view[:4])[0]
            return binary_view.hex()
            
        elif avp_type == TYPE_UNSIGNED_64:
            if len(binary_view) >= 8:
                return STRUCT_UNSIGNED_64.unpack(binary_view[:8])[0]
            return binary_view.hex()
            
        # Address type - optimized path
        elif avp_type == TYPE_ADDRESS:
            if len(binary_view) < 2:
                return binary_view.hex()
            family = int.from_bytes(binary_view[:2], 'big')
            address_bytes = binary_view[2:]
            try:
                if family == 1 and len(address_bytes) == 4:  # IPv4
                    return socket.inet_ntoa(address_bytes)
                elif family == 2 and len(address_bytes) == 16:  # IPv6
                    return socket.inet_ntop(socket.AF_INET6, address_bytes)
                else:
                    return binary_view.decode("utf-8", errors='replace')
            except (socket.error, UnicodeDecodeError):
                return binary_view.hex()
                
        # Fallback
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
                yield bytes(self.binary_data[start_idx:stop_idx])
            idx = stop_idx

    def slice_next_block(self, index: int) -> Tuple[int, int, bool]:
        """Parse Diameter header using the same logic as original"""
        index += 2  # Skip first 2 bytes
        end_idx = index + EricssonVolteFinal.HEADER_SIZE
        header = self.binary_data[index:end_idx]

        # Validate minimum length
        if len(header) < EricssonVolteFinal.HEADER_SIZE:
            index += len(header)  # Skip this block
            return index, index, True

        # Unpack all header fields
        try:
            (version, msg_len_bytes, flag_int, cmd_bytes, app_id, hbh_id, e2e_id) = (
                EricssonVolteFinal.DIAMETER_HEADER_FORMAT.unpack(header)
            )
        except struct.error:
            return index + len(header), index + len(header), True

        # Convert 24-bit fields
        msg_length = int.from_bytes(msg_len_bytes)

        # Validate version (MUST be 1)
        if version != 1:
            return index + len(header), index + len(header), True

        # Validate message type
        if cmd_bytes != b"\x00\x01\x0f":
            return index + len(header), index + len(header), True
        
        start_idx = index + EricssonVolteFinal.HEADER_SIZE
        index = index + msg_length  # msg_length includes the header
        return start_idx, index, False

    def process(self, pbar_position=None, show_progress=True):
        """Process the VoLTE data and return a list of parsed AVPs."""
        if show_progress:
            return list(
                tqdm(
                    self.avps(),
                    desc="  ↳ Parsing AVPs (final optimized)",
                    unit=" block",
                    leave=False,
                    position=pbar_position,
                    colour="cyan",
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
        return EricssonVolteFinal.insert_vendor_info(blocks)