from dataclasses import dataclass
from enum import Enum
from typing import Optional, Tuple
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


class BerTag:
    def __init__(self, tag_bytes: bytes):
        first_byte = tag_bytes[0]
        self.string = hexlify(
            tag_bytes[:1]
        ).decode(
            "utf-8"
        )  # This doesn't belong to the original ber encoding, it's specific to this implementation
        self.tag_class = BerClass((first_byte >> CLASS_SHIFT) & TWO_BIT_MASK)
        self.constructed = bool((first_byte >> ENCODE_SHIFT) & MODULO_2)
        self.number = first_byte & CLASSNUM_MASK

        if self.number == CLASSNUM_MASK:
            # Handle multi-byte tag
            self.number = 0
            for b in tag_bytes[1:]:
                self.number = (self.number << SHIFT_7) | (b & MASK_BIT7)


@dataclass
class TlvObject:
    """Tag-Length-Value object for BER encoding"""

    tag: BerTag
    length: int
    value: bytes
    offset: int
    children: list["TlvObject"] = None


@dataclass
class BerDecoder:
    """Basic Encoding Rules decoder"""

    @staticmethod
    def _reached_eoc(tag: BerTag, length: int):
        return (tag.tag_class, tag.constructed, tag.number, length) in EOC

    def decode_tlv(
        self, stream: BufferedReader | BytesIO, offset: int = 0, depth: int = 0
    ) -> Optional[TlvObject]:
        start_offset = offset
        if (tag_bytes := self._read_tag(stream)) is None:
            return None

        tag = BerTag(tag_bytes)
        length, length_size = self._read_length(stream)
        offset += len(tag_bytes) + length_size

        if self._reached_eoc(tag, length):
            return self.decode_tlv(stream, offset, depth)

        # Read value
        value = stream.read(length)
        if len(value) != length:
            raise ValueError("Unexpected end of data")

        # Update offset after tag and length
        tlv = TlvObject(tag, length, value, start_offset)

        # Parse constructed types recursively
        if tag.constructed:
            tlv.children = []
            value_stream = BytesIO(value)
            while value_stream.tell() < length:
                if child := self.decode_tlv(value_stream, offset, depth + 1):
                    tlv.children.append(child)
                    offset += child.length

        return tlv

    def _read_tag(self, stream: BufferedReader) -> Optional[bytes]:
        first_byte = stream.read(1)
        if not first_byte:
            return None

        tag_bytes = first_byte
        if int.from_bytes(tag_bytes, "big") & HIGH_CLASS_NUM == HIGH_CLASS_NUM:
            # Multi-byte tag
            while True:
                b = stream.read(1)
                if not b:
                    raise ValueError("Unexpected end of tag")
                tag_bytes += b
                if int.from_bytes(b, "big") & MASK_BIT8 == 0:
                    break

        return tag_bytes

    def _read_length(self, stream: BufferedReader) -> Tuple[int, int]:
        first_byte = stream.read(1)[0]
        if first_byte & MASK_BIT8 == 0:  # first_byte = 128
            return first_byte, 1

        length_size = first_byte & MASK_BIT7
        length_bytes = stream.read(length_size)
        if len(length_bytes) != length_size:
            raise ValueError("Unexpected end of length")

        length = 0
        # When iterating on bytes it's already converted to int
        for b in length_bytes:
            length = (length << SHIFT_8) | b

        return length, length_size + 1
