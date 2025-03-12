from dataclasses import dataclass
from enum import Enum
from typing import Optional, Tuple
from io import BufferedReader, BytesIO
from binascii import hexlify

# Basic ASN.1 Reference
# https://luca.ntop.org/Teaching/Appunti/asn1.html


CLASS_SHIFT = 6
ENCODE_SHIFT = 5
CLASSNUM_MASK = 0x1F

BITS7_MASK = 0x7F
BIT8_SHIFT = 7

HIGH_CLASS_NUM = 0x1F


class BerClass(Enum):
    UNIVERSAL = 0
    APPLICATION = 1
    CONTEXT = 2
    PRIVATE = 3


class BerTag:
    def __init__(self, tag_bytes: bytes):
        first_byte = tag_bytes[0]
        self.tag_string = hexlify(
            tag_bytes[:1]
        ).decode(
            "utf-8"
        )  # This doesn't belong to the original ber encoding, it's specific to this implementation
        self.tag_class = BerClass((first_byte >> 6) & 0x03)
        self.constructed = bool((first_byte >> 5) & 0x01)
        self.tag_number = first_byte & 0x1F

        if self.tag_number == 0x1F:
            # Handle multi-byte tag
            self.tag_number = 0
            for b in tag_bytes[1:]:
                self.tag_number = (self.tag_number << 7) | (b & 0x7F)


@dataclass
class TlvObject:
    """Tag-Length-Value object for BER encoding"""

    tag: BerTag
    length: int
    value: bytes
    offset: int
    children: list["TlvObject"] = None


class BerDecoder:
    """Basic Encoding Rules decoder"""

    def __init__(self):
        self.max_depth = None  # Prevent stack overflow

    def decode_tlv(
        self, stream: BufferedReader, offset: int = 0, depth: int = 0
    ) -> Optional[TlvObject]:
        if self.max_depth is not None and depth > self.max_depth:
            raise ValueError("Maximum decoding depth exceeded")

        start_offset = offset
        if not (tag_bytes := self._read_tag(stream)):
            return None

        length, length_size = self._read_length(stream)
        if length == 0:
            return None

        # Read value
        value = stream.read(length)
        if len(value) != length:
            raise ValueError("Unexpected end of data")

        # Update offset after tag and length
        offset += len(tag_bytes) + length_size
        tag = BerTag(tag_bytes)
        tlv = TlvObject(tag, length, value, start_offset)

        # Parse constructed types recursively
        if tag.constructed:
            tlv.children = []
            value_stream = BufferedReader(BytesIO(value))
            while value_stream.tell() < length:
                if child := self.decode_tlv(value_stream, offset, depth + 1):
                    tlv.children.append(child)
                    offset += child.length

        return tlv

    def _read_tag(self, stream: BufferedReader) -> Optional[bytes]:
        first_byte = stream.read(1)
        if not first_byte:
            return None

        tag_bytes = bytearray(first_byte)
        if (first_byte[0] & 0x1F) == 0x1F:
            # Multi-byte tag
            while True:
                b = stream.read(1)
                if not b:
                    raise ValueError("Unexpected end of tag")
                tag_bytes.append(b[0])
                if not (b[0] & 0x80):
                    break

        return bytes(tag_bytes)

    def _read_length(self, stream: BufferedReader) -> Tuple[int, int]:
        first_byte = stream.read(1)[0]
        if not (first_byte & 0x80):
            return first_byte, 1

        length_size = first_byte & 0x7F
        length_bytes = stream.read(length_size)
        if len(length_bytes) != length_size:
            raise ValueError("Unexpected end of length")

        length = 0
        for b in length_bytes:
            length = (length << 8) | b

        return length, length_size + 1
