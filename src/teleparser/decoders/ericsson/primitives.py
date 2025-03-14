class OctetStringError(Exception):
    pass


class UnsignedIntError(Exception):
    pass


class OctetString:
    """Implement ASN.1 Octet String type with optional size and boundaries constraints"""
    def __init__(self, octets, size: int = None, lower: int = None, upper: int = None):
        if size is None:
            size = len(octets)
        elif size and size > len(octets):
            raise OctetStringError("Size parameter is bigger than octets length")
        if lower and lower > size:
            raise OctetStringError(f"{size:=} is small er than {lower:=} limit")
        if upper and size > upper:
            raise OctetStringError(f"{size:=} is bigger than {upper:=} limit")    
        try:
            self.string = octets.hex().upper()
        except AttributeError as e:
            raise OctetStringError("Error parsing octet") from e
        

class UnsignedInt:
    """OCTET STRING is coded as an unsigned integer."""

    def __init__(self, octets: bytes, size: int):
        if not isinstance(octets, bytes):
            raise TypeError(f"Octet parameter is not a byte object: {type(octets)}")
        if not isinstance(size, int):
            raise TypeError(f"size parameter is not an int: {type(octets)}")
        assert len(octets) == size, f"Parameter should have size {size}, {len(octets)=}"
        self.octets = octets

    @property
    def value(self) -> int:
        """Call ID Number - 3 byte unsigned integer
        it convert 3 bytes to integer (big endian)"
        """
        return int.from_bytes(self.octets, byteorder="big")
