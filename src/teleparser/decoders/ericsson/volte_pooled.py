"""EricssonVolte decoder with memory pooling optimization.

This module implements memory pooling to reduce dictionary allocation overhead
and garbage collection pressure.
"""

import struct
from datetime import datetime, timedelta
from typing import Generator, Tuple
import socket
from collections import deque
import threading
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


class AVPObjectPool:
    """Thread-safe object pool for AVP dictionaries to reduce allocation overhead."""
    
    def __init__(self, max_size=10000):
        self._pool = deque(maxlen=max_size)
        self._lock = threading.Lock()
        self._stats = {"acquired": 0, "created": 0, "released": 0}
    
    def acquire(self) -> dict:
        """Get a dictionary from pool or create a new one."""
        with self._lock:
            try:
                obj = self._pool.pop()
                obj.clear()
                self._stats["acquired"] += 1
                return obj
            except IndexError:
                self._stats["created"] += 1
                return {}
    
    def release(self, obj: dict):
        """Return dictionary to pool for reuse."""
        if obj:
            with self._lock:
                self._pool.append(obj)
                self._stats["released"] += 1
    
    def get_stats(self) -> dict:
        """Get pool statistics."""
        with self._lock:
            stats = self._stats.copy()
            stats["pool_size"] = len(self._pool)
            stats["hit_rate"] = (stats["acquired"] / max(1, stats["acquired"] + stats["created"]))
            return stats


# Global object pools
_avp_pool = AVPObjectPool(max_size=5000)
_nested_pool = AVPObjectPool(max_size=2000)


class EricssonVoltePooled:
    """EricssonVolte decoder with memory pooling optimizations."""
    
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
        """Parse a block using memory pooling."""
        # Use main pool for the result dictionary
        result = _avp_pool.acquire()
        
        try:
            while block:
                avp, offset = EricssonVoltePooled.parse_avp_pooled(block)
                block = block[offset:]
                if avp:
                    result.update(avp)
            
            # Return a copy and release the pooled object
            final_result = result.copy()
            return final_result
        finally:
            _avp_pool.release(result)

    @staticmethod
    def parse_avp_pooled(current_block: memoryview | bytes) -> Tuple:
        """Parse a single AVP using memory pooling."""
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
            avps, offset = EricssonVoltePooled.parse_grouped_avp_pooled(value_data)
            if not avps:
                return {}, offset
            return EricssonVoltePooled.flatten_avp_pooled(avp_def.avp, avps), offset
        else:
            return {
                avp_def.avp: EricssonVoltePooled.parse_simple_value(value_data, avp_type),
            }, offset

    @staticmethod
    def parse_grouped_avp_pooled(binary_data: bytes | bytes) -> Tuple[list, int]:
        """Parse a grouped AVP using memory pooling."""
        avps = []
        current_block = binary_data
        total_offset = 0
        
        while current_block:
            avp, offset = EricssonVoltePooled.parse_avp_pooled(current_block)
            current_block = current_block[offset:]  # Move to next AVP
            if avp:
                avps.append(avp)
            total_offset += offset
            
        if len(avps) == 1:
            avps = avps[0]  # If only one AVP, return it directly
        return avps, total_offset

    @staticmethod
    def flatten_avp_pooled(prefix: str, avp: dict | list) -> dict:
        """Flatten AVP using pooled dictionaries."""
        flattened_avp = _nested_pool.acquire()
        
        try:
            if isinstance(avp, dict):
                for key, value in avp.items():
                    if not isinstance(value, (dict, list)):
                        if previous_value := flattened_avp.get(key):
                            value = f"{previous_value};{value}"  # Concatenate values
                        flattened_avp[key] = value
                    if isinstance(value, dict):
                        nested_result = EricssonVoltePooled.flatten_avp_pooled(key, value)
                        flattened_avp.update(nested_result)
                        _nested_pool.release(nested_result)
                    elif isinstance(value, list):
                        for item in value:
                            nested_result = EricssonVoltePooled.flatten_avp_pooled(key, item)
                            flattened_avp.update(nested_result)
                            _nested_pool.release(nested_result)
            elif isinstance(avp, list):
                for item in avp:
                    nested_result = EricssonVoltePooled.flatten_avp_pooled(prefix, item)
                    flattened_avp.update(nested_result)
                    _nested_pool.release(nested_result)
            
            # Return a copy
            result = flattened_avp.copy()
            return result
        finally:
            _nested_pool.release(flattened_avp)

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
            return (EricssonVoltePooled.NTP_EPOCH + timedelta(seconds=seconds)).strftime(
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
        end_idx = index + EricssonVoltePooled.HEADER_SIZE
        header = self.binary_data[index:end_idx]

        # Validate minimum length
        if len(header) < EricssonVoltePooled.HEADER_SIZE:
            index += len(header)  # Skip this block
            return index, index, True

        # Unpack all header fields
        (version, msg_len_bytes, flag_int, cmd_bytes, app_id, hbh_id, e2e_id) = (
            EricssonVoltePooled.DIAMETER_HEADER_FORMAT.unpack(header)
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
        
        start_idx = index + EricssonVoltePooled.HEADER_SIZE
        index = index + msg_length  # msg_length includes the header
        return start_idx, index, False

    def process(self, pbar_position=None, show_progress=True):
        """Process the VoLTE data and return a list of parsed AVPs."""
        if show_progress:
            return list(
                tqdm(
                    self.avps(),
                    desc="  ↳ Parsing AVPs (pooled)",
                    unit=" block",
                    leave=False,
                    position=pbar_position,
                    colour="green",
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
        return EricssonVoltePooled.insert_vendor_info(blocks)

    @classmethod
    def get_pool_stats(cls):
        """Get memory pool statistics."""
        return {
            "main_pool": _avp_pool.get_stats(),
            "nested_pool": _nested_pool.get_stats()
        }