"""EricssonVolte decoder with pre-compiled AVP lookup optimization.

This module implements optimizations for the EricssonVolte decoder:
1. Pre-compiled AVP lookup tables
2. Optimized parser functions
3. Flag validation patterns
"""

import struct
from datetime import datetime, timedelta
from dataclasses import dataclass
from typing import Generator, Tuple, NamedTuple, Callable, Dict, Any
import socket
import logging
from tqdm.auto import tqdm

from teleparser.decoders.ericsson.volte import (
    VendorID,
    AVP_DB,
    is_avp_flag_valid,
    # Constants
    VENDOR_3GPP,
    VENDOR_ERICSSON,
    VENDOR_HUAWEI,
    TYPE_OCTET_STRING,
    TYPE_INTEGER_32,
    TYPE_UNSIGNED_32,
    TYPE_UNSIGNED_64,
    TYPE_UTF8_STRING,
    TYPE_GROUPED,
    TYPE_TIME,
    TYPE_ENUMERATED,
    TYPE_DIAMETER_IDENTITY,
    TYPE_ADDRESS,
    STRUCT_UNSIGNED_32,
    STRUCT_SIGNED_32,
    STRUCT_UNSIGNED_64,
    KNOWN_SIZES,
)


class CompiledAVP(NamedTuple):
    """Pre-compiled AVP definition for O(1) lookups."""

    name: str
    type: int
    flags_pattern: bytes | None
    vendor_id: int | None
    parser_func: Callable[[bytes], Any]


# Global compiled lookup tables
COMPILED_AVP_DB: Dict[int, CompiledAVP] = {}
GROUPED_AVP_CODES: set = set()


def create_value_parser(avp_type: int) -> Callable[[bytes], Any]:
    """Create optimized parser function for specific AVP type."""

    def parse_unsigned_32(data: bytes) -> int:
        return STRUCT_UNSIGNED_32.unpack(data)[0]

    def parse_unsigned_64(data: bytes) -> int:
        return STRUCT_UNSIGNED_64.unpack(data)[0]

    def parse_signed_32(data: bytes) -> int:
        return STRUCT_SIGNED_32.unpack(data)[0]

    def parse_utf8_string(data: bytes) -> str:
        try:
            return data.decode("utf-8").rstrip("\x00")
        except UnicodeDecodeError:
            return data.hex()

    def parse_octet_string(data: bytes) -> str:
        # If data is small and looks like binary, return hex
        if len(data) <= 16:
            return data.hex()
        # Otherwise try to decode as UTF-8
        try:
            return data.decode("utf-8", errors="replace").rstrip("\x00")
        except UnicodeDecodeError:
            return data.hex()

    def parse_time(data: bytes) -> str:
        seconds = STRUCT_UNSIGNED_32.unpack(data)[0]
        ntp_epoch = datetime(1900, 1, 1)
        return (ntp_epoch + timedelta(seconds=seconds)).strftime("%Y-%m-%d %H:%M:%S")

    def parse_address(data: bytes) -> str:
        if len(data) < 2:
            return data.hex()

        family = int.from_bytes(data[:2], "big")
        address_bytes = data[2:]

        try:
            if family == 1:  # IPv4
                return socket.inet_ntoa(address_bytes)
            elif family == 2:  # IPv6
                return socket.inet_ntop(socket.AF_INET6, address_bytes)
            else:
                return data.decode("utf-8", errors="replace")
        except (socket.error, UnicodeDecodeError):
            return data.hex()

    def parse_fallback(data: bytes) -> str:
        return data.hex()

    # Return appropriate parser function
    parser_map = {
        TYPE_UNSIGNED_32: parse_unsigned_32,
        TYPE_UNSIGNED_64: parse_unsigned_64,
        TYPE_INTEGER_32: parse_signed_32,
        TYPE_ENUMERATED: parse_signed_32,
        TYPE_UTF8_STRING: parse_utf8_string,
        TYPE_DIAMETER_IDENTITY: parse_utf8_string,
        TYPE_OCTET_STRING: parse_octet_string,
        TYPE_TIME: parse_time,
        TYPE_ADDRESS: parse_address,
    }

    return parser_map.get(avp_type, parse_fallback)


def compile_flags_pattern(acr_flag: str | None) -> bytes | None:
    """Pre-compile flags validation pattern."""
    if not acr_flag:
        return None

    # Convert flag string to expected byte value
    expected_flags = 0
    if "V" in acr_flag:
        expected_flags |= 0x80
    if "M" in acr_flag:
        expected_flags |= 0x40
    if "P" in acr_flag:
        expected_flags |= 0x20

    return expected_flags.to_bytes(1, "big")


import logging


def compile_avp_database():
    """Compile AVP database for optimal O(1) lookups."""
    global COMPILED_AVP_DB, GROUPED_AVP_CODES

    logging.debug("Compiling AVP database...")
    COMPILED_AVP_DB.clear()
    GROUPED_AVP_CODES.clear()

    for code, avp_def in AVP_DB.items():
        # Identify grouped AVPs
        if avp_def.type == TYPE_GROUPED:
            GROUPED_AVP_CODES.add(code)
            parser_func = lambda data: data  # Grouped AVPs handled separately
        else:
            parser_func = create_value_parser(avp_def.type)

        # Pre-compile flags validation pattern
        flags_pattern = compile_flags_pattern(avp_def.acr_flag)

        COMPILED_AVP_DB[code] = CompiledAVP(
            name=avp_def.avp,
            type=avp_def.type,
            flags_pattern=flags_pattern,
            vendor_id=avp_def.vendor_id,
            parser_func=parser_func,
        )

    logging.debug(f"Compiled {len(COMPILED_AVP_DB)} AVP definitions")
    logging.debug(f"Compiled {len(COMPILED_AVP_DB)} AVP definitions")


# Compile database at module load
compile_avp_database()


class EricssonVolteOptimized:
    """EricssonVolte decoder with pre-compiled lookup optimizations."""

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
        """Parse a block using optimized lookups."""
        parsed_blocks = []
        while block:
            avp, offset = EricssonVolteOptimized.parse_avp_optimized(block)
            block = block[offset:]
            parsed_blocks.append(avp)
        return {k: v for block in parsed_blocks for k, v in block.items()}

    @staticmethod
    def parse_avp_optimized(current_block: memoryview | bytes) -> Tuple:
        """Parse a single AVP using optimized pre-compiled lookups."""
        i = 0
        header_size = 8

        while True:
            # Parse AVP header (8 bytes)
            if (offset := len(current_block[i:])) < 8:
                return {}, offset  # Not enough data for AVP header

            avp_code = int.from_bytes(current_block[i : i + 4], byteorder="big")

            # Fast lookup in compiled database
            compiled_avp = COMPILED_AVP_DB.get(avp_code)
            if not compiled_avp:
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

            # Fast size validation using compiled sizes
            if (known_size := KNOWN_SIZES.get(compiled_avp.type)) is not None:
                if avp_length - header_size != known_size:
                    i += 1
                    continue  # Slide window if AVP length does not match known size
            break

        offset: int = i + avp_length

        # Fast flags validation using pre-compiled pattern
        if compiled_avp.flags_pattern is not None:
            if not EricssonVolteOptimized.validate_flags_fast(
                flags, compiled_avp.flags_pattern
            ):
                return {}, offset  # Invalid AVP flags, skip this AVP

        value_data: bytes = bytes(current_block[i + header_size : i + avp_length])

        # Handle grouped AVPs
        if compiled_avp.type == TYPE_GROUPED:
            avps, offset = EricssonVolteOptimized.parse_grouped_avp(value_data)
            if not avps:
                return {}, offset
            return EricssonVolteOptimized.flatten_avp(compiled_avp.name, avps), offset
        else:
            # Use pre-compiled parser function
            try:
                parsed_value = compiled_avp.parser_func(value_data)
                return {compiled_avp.name: parsed_value}, offset
            except (struct.error, ValueError, UnicodeDecodeError):
                # Fallback to hex representation
                return {compiled_avp.name: value_data.hex()}, offset

    @staticmethod
    def validate_flags_fast(flags: int, expected_pattern: bytes) -> bool:
        """Fast flags validation using pre-compiled pattern."""
        expected = expected_pattern[0]

        # Check reserved bits (bits 4-0 should be zero for reserved)
        if (flags & 0x1F) != 0:
            return False

        # Check that all expected flags are present
        return (flags & expected) == expected

    @staticmethod
    def flatten_avp(prefix: str, avp: dict | list) -> dict:
        """Flatten nested AVP dictionaries."""
        flattened_avp = {}
        if isinstance(avp, dict):
            for key, value in avp.items():
                if not isinstance(value, (dict, list)):
                    if previous_value := flattened_avp.get(key):
                        value = f"{previous_value};{value}"  # Concatenate values
                    flattened_avp[key] = value
                if isinstance(value, dict):
                    flattened_avp.update(EricssonVolteOptimized.flatten_avp(key, value))
                elif isinstance(value, list):
                    for item in value:
                        flattened_avp.update(
                            EricssonVolteOptimized.flatten_avp(key, item)
                        )
        elif isinstance(avp, list):
            for item in avp:
                flattened_avp.update(EricssonVolteOptimized.flatten_avp(prefix, item))
        return flattened_avp

    @staticmethod
    def parse_grouped_avp(binary_data: bytes | bytes) -> Tuple[list, int]:
        """Parse a grouped AVP (recursive)"""
        avps = []
        current_block = binary_data
        total_offset = 0
        while current_block:
            avp, offset = EricssonVolteOptimized.parse_avp_optimized(current_block)
            current_block = current_block[offset:]  # Move to next AVP
            if avp:
                avps.append(avp)
            total_offset += offset
        if len(avps) == 1:
            avps = avps[0]  # If only one AVP, return it directly
        return avps, total_offset

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
        end_idx = index + EricssonVolteOptimized.HEADER_SIZE
        header = self.binary_data[index:end_idx]

        # Validate minimum length
        if len(header) < EricssonVolteOptimized.HEADER_SIZE:
            index += len(header)  # Skip this block
            return index, index, True

        # Unpack all header fields
        (version, msg_len_bytes, flag_int, cmd_bytes, app_id, hbh_id, e2e_id) = (
            EricssonVolteOptimized.DIAMETER_HEADER_FORMAT.unpack(header)
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

        start_idx = index + EricssonVolteOptimized.HEADER_SIZE
        index = index + msg_length  # msg_length includes the header
        return start_idx, index, False

    def process(self, pbar_position=None, show_progress=True):
        """Process the VoLTE data and return a list of parsed AVPs."""
        if show_progress:
            return list(
                tqdm(
                    self.avps(),
                    desc="  ↳ Parsing AVPs (optimized)",
                    unit=" block",
                    leave=False,
                    position=pbar_position,
                    colour="blue",
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
        return EricssonVolteOptimized.insert_vendor_info(blocks)
