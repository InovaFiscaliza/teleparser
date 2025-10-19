from dataclasses import dataclass
from collections import namedtuple
from typing import Optional, Tuple, Callable
from io import BufferedReader, BytesIO
from tqdm.auto import tqdm  # Use standard tqdm for compatibility with nesting
from teleparser.buffer import BufferManager
from teleparser.decoders.ericsson.fieldnames import ERICSSON_VOZ_FIELDS

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

BerStream = BufferedReader | BytesIO | BufferManager


@dataclass
class BerDecoder:
    """Basic Encoding Rules decoder"""

    parser: Callable
    buffer_manager: BufferManager
    FIELDNAMES: set = None  # Default field names - set in __post_init__

    def __post_init__(self):
        """Initialize the memory buffer after dataclass initialization."""
        self._data: Optional[memoryview] = None
        self._size: int = 0
        if self.FIELDNAMES is None:
            self.FIELDNAMES = ERICSSON_VOZ_FIELDS

    @staticmethod
    def read_tag(stream: BerStream) -> Optional[bytes]:
        first_byte = stream.read(1)  # index makes a converted to int
        if not first_byte:
            return None

        tag_byte = first_byte
        if int.from_bytes(tag_byte, "big") & HIGH_CLASS_NUM == HIGH_CLASS_NUM:
            # Multi-byte tag
            while True:
                b = stream.read(1)
                if not b:
                    raise ValueError("Unexpected end of tag")
                tag_byte += b
                if int.from_bytes(b, "big") & MASK_BIT8 == 0:
                    break

        return tag_byte

    @staticmethod
    def decode_tag(tag_bytes: bytes) -> BerTag:
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
    def read_length(stream: BerStream) -> Tuple[int, int]:
        first_byte = stream.read(1)[0]
        # definite short form
        if first_byte >> SHIFT_7 == 0:
            return first_byte, 1

        length = 0
        length_size = first_byte & MASK_BIT7
        # indefinite form
        if length_size == 0:
            return 0, 1

        length_bytes = stream.read(length_size)
        if length_bytes is not None:
            if len(length_bytes) != length_size:
                raise ValueError("Unexpected end of length")

            #  definite long form
            #  When iterating on bytes it's already converted to int
            for b in length_bytes:
                length = (length << SHIFT_8) | b

        return length, length_size + 1

    @staticmethod
    def reached_eoc(tag: BerTag, length: int) -> bool:
        return (tag.tag_class, tag.constructed, tag.number, length) in EOC

    def decode(
        self,
        stream: BerStream,
        offset: int = 0,
        depth: int = 0,
        schema: dict | None = None,
    ):
        if (tag_bytes := BerDecoder.read_tag(stream)) is None:
            return None

        tag: BerTag = BerDecoder.decode_tag(tag_bytes)
        length, length_size = BerDecoder.read_length(stream)
        offset += len(tag_bytes) + length_size

        if BerDecoder.reached_eoc(tag, length) or length == 0:
            return self.decode(stream, offset, depth, schema)
        # Read value
        value: bytes = stream.read(length)
        if len(value) != length:
            raise ValueError("Unexpected end of data")

        # Update offset after tag and length
        if (decoded_tlv := self.unravel_decoded_tlv(tag.number, value, schema)) is None:
            return None
        decoded_data, schema = decoded_tlv

        # Parse constructed types recursively
        if tag.constructed:
            value_stream = BytesIO(value)
            while value_stream.tell() < length:
                if child := self.decode(value_stream, offset, depth + 1, schema):
                    child_data, child_length = child
                    offset += child_length
                    decoded_data.update(child_data)
        return decoded_data, length

    def unravel_decoded_tlv(
        self, tag_number: int, value: bytes, schema: dict | None
    ) -> Tuple[dict, dict] | None:
        """Unravel TLV tree to a flat dictionary"""
        try:
            tlv = self.parser(tag_number, value, schema)
        except KeyError:
            # print(f"{e}: Unknown tag {tag_number} in {schema}")
            return None
        if tlv.value is None:
            return None
        if isinstance(tlv.value, dict):
            output = {f"{tlv.name}.{k}": v for k, v in tlv.value.items()}
        else:
            output = {tlv.name: tlv.value}
        return output, tlv.schema

    def parse_blocks(self):
        with self.buffer_manager.open() as file_buffer:
            while (tlv := self.decode(file_buffer)) is not None:
                record, _ = tlv
                yield record

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
                    colour="blue",
                )
            )
        else:
            return list(self.parse_blocks())

    @property
    def transform_func(self):  # Just a placeholder for compatibility
        return None
