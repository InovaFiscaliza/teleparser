from dataclasses import dataclass
from collections import namedtuple
from typing import Optional, Tuple, Callable
from tqdm.auto import tqdm
from teleparser.buffer import MemoryBufferManager

# Basic ASN.1 Reference
# https://luca.ntop.org/Teaching/Appunti/asn1.html


CLASS_SHIFT = 6
TWO_BIT_MASK = 3
ENCODE_SHIFT = 5
MODULO_2 = 1
CLASSNUM_MASK = 31
MASK_BIT7 = 127
SHIFT_7 = 7
HIGH_CLASS_NUM = 31
MASK_BIT8 = 128
SHIFT_8 = 8


# BerClass
UNIVERSAL = 0
APPLICATION = 1
CONTEXT = 2
PRIVATE = 3


EOC = {(0, False, 0, 0), (2, True, 1, 0)}


BerTag = namedtuple("BerTag", ["tag_class", "constructed", "number"])


@dataclass
class BerDecoderOptimized:
    """Optimized Basic Encoding Rules decoder using memory-mapped data.
    
    This decoder reads the entire file into memory once and uses memoryview
    for efficient byte access, eliminating repetitive disk I/O operations.
    """

    parser: Callable
    buffer_manager: MemoryBufferManager

    def __post_init__(self):
        """Initialize the memory buffer after dataclass initialization."""
        self._data: Optional[memoryview] = None
        self._size: int = 0

    @staticmethod
    def read_tag(data: memoryview, position: int) -> Tuple[Optional[bytes], int]:
        """Read a BER tag from memoryview starting at position.
        
        Returns:
            Tuple of (tag_bytes, bytes_read) or (None, 0) if EOF
        """
        if position >= len(data):
            return None, 0
        
        first_byte = data[position]
        tag_bytes = bytes([first_byte])
        bytes_read = 1
        
        if first_byte & HIGH_CLASS_NUM == HIGH_CLASS_NUM:
            # Multi-byte tag
            while position + bytes_read < len(data):
                b = data[position + bytes_read]
                tag_bytes += bytes([b])
                bytes_read += 1
                if b & MASK_BIT8 == 0:
                    break
            else:
                raise ValueError("Unexpected end of tag")
        
        return tag_bytes, bytes_read

    @staticmethod
    def decode_tag(tag_bytes: bytes) -> BerTag:
        """Decode tag bytes into a BerTag namedtuple."""
        first_byte = tag_bytes[0]
        tag_class = (first_byte >> CLASS_SHIFT) & TWO_BIT_MASK
        constructed = ((first_byte >> ENCODE_SHIFT) & MODULO_2) == 1
        number = first_byte & CLASSNUM_MASK

        if number == CLASSNUM_MASK:
            # Handle multi-byte tag
            number = 0
            for b in tag_bytes[1:]:
                number = (number << SHIFT_7) | (b & MASK_BIT7)
                if b >> SHIFT_7 == 0:
                    break

        return BerTag(tag_class, constructed, number)

    @staticmethod
    def read_length(data: memoryview, position: int) -> Tuple[int, int]:
        """Read BER length from memoryview starting at position.
        
        Returns:
            Tuple of (length_value, bytes_read)
        """
        if position >= len(data):
            raise ValueError("Unexpected end of data while reading length")
        
        first_byte = data[position]
        
        # Definite short form
        if first_byte >> SHIFT_7 == 0:
            return first_byte, 1
        
        length = 0
        length_size = first_byte & MASK_BIT7
        
        # Indefinite form
        if length_size == 0:
            return 0, 1
        
        # Check if we have enough data
        if position + 1 + length_size > len(data):
            raise ValueError("Unexpected end of length")
        
        # Definite long form
        for i in range(length_size):
            length = (length << SHIFT_8) | data[position + 1 + i]
        
        return length, length_size + 1

    @staticmethod
    def reached_eoc(tag: BerTag, length: int) -> bool:
        """Check if we've reached an End-of-Content marker."""
        return (tag.tag_class, tag.constructed, tag.number, length) in EOC

    def decode(
        self,
        data: memoryview,
        position: int,
        depth: int = 0,
        schema: dict | None = None,
    ) -> Tuple[Optional[dict], int]:
        """Decode BER data from memoryview starting at position.
        
        Returns:
            Tuple of (decoded_data, bytes_consumed) or (None, 0) if EOF
        """
        # Read tag
        tag_bytes, tag_bytes_read = BerDecoderOptimized.read_tag(data, position)
        if tag_bytes is None:
            return None, 0
        
        position += tag_bytes_read
        tag: BerTag = BerDecoderOptimized.decode_tag(tag_bytes)
        
        # Read length
        length, length_bytes_read = BerDecoderOptimized.read_length(data, position)
        position += length_bytes_read
        
        total_bytes_read = tag_bytes_read + length_bytes_read
        
        # Handle EOC or zero-length
        if BerDecoderOptimized.reached_eoc(tag, length) or length == 0:
            result = self.decode(data, position, depth, schema)
            if result[0] is not None:
                return result[0], total_bytes_read + result[1]
            return None, total_bytes_read
        
        # Check if we have enough data for the value
        if position + length > len(data):
            raise ValueError(f"Unexpected end of data: need {length} bytes at position {position}, but only {len(data) - position} available")
        
        # Read value
        value = bytes(data[position:position + length])
        total_bytes_read += length
        
        # Unravel the TLV
        decoded_tlv = self.unravel_decoded_tlv(tag.number, value, schema)
        if decoded_tlv is None:
            return None, total_bytes_read
        
        decoded_data, schema = decoded_tlv
        
        # Parse constructed types recursively
        if tag.constructed:
            child_position = position
            end_position = position + length
            
            while child_position < end_position:
                child_result = self.decode(data, child_position, depth + 1, schema)
                if child_result[0] is not None:
                    child_data, child_bytes = child_result
                    child_position += child_bytes
                    decoded_data.update(child_data)
                else:
                    break
        
        return decoded_data, total_bytes_read

    def unravel_decoded_tlv(
        self, tag_number: int, value: bytes, schema: dict | None
    ) -> Tuple[dict, dict] | None:
        """Unravel TLV tree to a flat dictionary."""
        try:
            tlv = self.parser(tag_number, value, schema)
        except KeyError:
            # Unknown tag in schema
            return None
        
        if tlv.value is None:
            return None
        
        if isinstance(tlv.value, dict):
            output = {f"{tlv.name}.{k}": v for k, v in tlv.value.items()}
        else:
            output = {tlv.name: tlv.value}
        
        return output, tlv.schema

    def parse_blocks(self):
        """Parse all blocks from the memory-mapped data."""
        # Load data into memory once
        with self.buffer_manager.open():
            data = self.buffer_manager.get_memoryview()
            data_size = len(data)
            position = 0
            
            while position < data_size:
                result = self.decode(data, position)
                if result[0] is not None:
                    record, bytes_read = result
                    position += bytes_read
                    yield record
                else:
                    # No more valid data
                    break

    def process(self, pbar_position=None, show_progress=True):
        """Process the BER data and return a list of parsed blocks.
        
        Args:
            pbar_position: Position for nested progress bar (for hierarchical display)
            show_progress: Whether to show progress bar
        """
        if show_progress:
            return list(
                tqdm(
                    self.parse_blocks(),
                    desc="  ↳ Parsing TLVs",
                    unit=" block",
                    leave=False,
                    position=pbar_position,
                    colour="blue"
                )
            )
        else:
            return list(self.parse_blocks())

    @property
    def transform_func(self):
        """Placeholder for compatibility."""
        return None
