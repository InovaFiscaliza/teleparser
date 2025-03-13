class OctetString:
    def __init__(self, octets, size: int = None):
        if size and size > len(octets):
            raise ValueError("size parameter is bigger than octets length")
        self.string = octets.hex().upper()


class UnsignedInt:
    """OCTET STRING is coded as an unsigned integer."""

    def __init__(self, octets: bytes, size: int):
        assert len(octets) == size, f"Parameter should have size {size}, {len(octets)=}"
        self.octets = octets

    @property
    def value(self) -> int:
        """Call ID Number - 3 byte unsigned integer"""

        # Convert 3 bytes to integer (big endian)
        return int.from_bytes(self.octets, byteorder="big")
        # # Format as hex with 0x prefix
        # return f"0x{value:06X}"
