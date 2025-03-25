import gzip
from pathlib import Path
from dataclasses import dataclass
from enum import Enum
from typing import Optional, Tuple, Callable
from io import BufferedReader, BytesIO
from binascii import hexlify

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


class BerClass(Enum):
    UNIVERSAL = 0
    APPLICATION = 1
    CONTEXT = 2
    PRIVATE = 3


EOC = {(BerClass.UNIVERSAL, False, 0, 0), (BerClass.CONTEXT, True, 1, 0)}


@dataclass
class BerTag:
    """BER Encoded Class"""

    string: str
    tag_class: BerClass
    constructed: bool
    number: int


class BerDecoder:
    """Basic Encoding Rules decoder"""

    def __init__(self, parser: Callable, file_path_or_bytes: Path | bytes):
        self.parser = parser
        self.load_buffer(file_path_or_bytes)

    def load_buffer(self, file_path_or_bytes):
        """Load the entire file or bytes object into memory"""
        if isinstance(file_path_or_bytes, bytes):
            self.buffer = file_path_or_bytes
        elif isinstance(file_path_or_bytes, (str, Path)):
            file_path_or_bytes = Path(file_path_or_bytes)
            open_func = gzip.open if file_path_or_bytes.suffix == ".gz" else open
            with open_func(file_path_or_bytes, "rb") as f:
                self.buffer = f.read()
        else:
            raise ValueError("Invalid file path or bytes object")

    def decode_from_stream(self, stream: BufferedReader | BytesIO, schema: dict = None):
        """Backward compatible method that reads the stream and uses index-based decoding"""
        # Read the entire stream into memory
        if isinstance(stream, BytesIO):
            stream.seek(0)
            self.buffer = stream.read()
        else:
            self.buffer = stream.read()

        # Use the index-based approach
        return self.decode_tlv(0, 0, schema)

    @staticmethod
    def decode_tag(tag_bytes: bytes):
        first_byte = tag_bytes[0]
        string = hexlify(
            tag_bytes[:1]
        ).decode(
            "utf-8"
        )  # This doesn't belong to the original ber encoding, it's specific to this implementation
        tag_class = BerClass((first_byte >> CLASS_SHIFT) & TWO_BIT_MASK)
        constructed = bool((first_byte >> ENCODE_SHIFT) & MODULO_2)
        number = first_byte & CLASSNUM_MASK

        if number == CLASSNUM_MASK:
            # Handle multi-byte tag
            number = 0
            for b in tag_bytes[1:]:
                number = (number << SHIFT_7) | (b & MASK_BIT7)

        return BerTag(string, tag_class, constructed, number)

    @staticmethod
    def _reached_eoc(tag: BerTag, length: int):
        return (tag.tag_class, tag.constructed, tag.number, length) in EOC

    def decode_tlv(self, index: int = 0, depth: int = 0, schema: dict = None):
        """Decode TLV structure using index-based approach"""
        if index >= len(self.buffer):
            return None

        tag_data = self._read_tag_indexed(index)
        if tag_data is None:
            return None

        tag, tag_size = tag_data
        index += tag_size

        length_data = self._read_length_indexed(index)
        length, length_size = length_data
        index += length_size

        if self._reached_eoc(tag, length) or length == 0:
            return self.decode_tlv(index, depth, schema)

        # Extract value directly from buffer
        value = self.buffer[index : index + length]
        if len(value) != length:
            raise ValueError("Unexpected end of data")

        # Update index after value
        index += length

        decoded_data, schema = self.unravel_decoded_tlv(tag.number, value, schema)

        # Parse constructed types recursively
        if tag.constructed:
            value_index = index - length  # Start of value
            end_index = index  # End of value

            while value_index < end_index and (
                child := self.decode_tlv(value_index, depth + 1, schema)
            ):
                child_data, child_index = child
                value_index = child_index  # Move to next child
                decoded_data.update(child_data)

        return decoded_data, index

    def unravel_decoded_tlv(
        self, tag_number: int, value: bytes, schema: dict
    ) -> Tuple[dict, dict]:
        """Unravel TLV tree to a flat dictionary"""
        tlv = self.parser(tag_number, value, schema)
        if isinstance(tlv.value, dict):
            output = {f"{tlv.name}.{k}": v for k, v in tlv.value.items()}
        else:
            output = {tlv.name: tlv.value}
        return output, tlv.schema

    def _read_tag_indexed(self, index: int):
        """Read tag using index-based approach"""
        if index >= len(self.buffer):
            return None

        first_byte = self.buffer[index]
        tag_size = 1

        if first_byte & HIGH_CLASS_NUM == HIGH_CLASS_NUM:
            # Multi-byte tag
            while True:
                if index + tag_size >= len(self.buffer):
                    raise ValueError("Unexpected end of tag")

                b = self.buffer[index + tag_size]
                tag_size += 1

                if b & MASK_BIT8 == 0:
                    break

        tag_bytes = self.buffer[index : index + tag_size]
        tag = self.decode_tag(tag_bytes)

        return tag, tag_size

    def _read_length_indexed(self, index: int):
        """Read length using index-based approach"""
        first_byte = self.buffer[index]

        # definite short form
        if first_byte >> SHIFT_7 == 0:
            return first_byte, 1

        length = 0
        length_size = first_byte & MASK_BIT7

        # indefinite form
        if length_size == 0:
            return length, length_size + 1

        if index + 1 + length_size > len(self.buffer):
            raise ValueError("Unexpected end of length")

        # definite long form
        for i in range(length_size):
            b = self.buffer[index + 1 + i]
            length = (length << SHIFT_8) | b

        return length, length_size + 1
