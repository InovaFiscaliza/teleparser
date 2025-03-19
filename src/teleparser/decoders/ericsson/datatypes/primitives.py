"""This module implements primitive datatypes as described in the ASN.1 Especification"""

from functools import cached_property, wraps
from . import exceptions


def fixed_size_unsigned_int(size):
    """Factory function to create UnsignedInt classes with fixed size"""

    def decorator(cls):
        original_init = cls.__init__

        @wraps(original_init)
        def new_init(self, octets, *args, **kwargs):
            UnsignedInt.__init__(self, octets, size)
            if (
                hasattr(original_init, "__code__")
                and original_init.__code__ != UnsignedInt.__init__.__code__
            ):
                original_init(self, octets, *args, **kwargs)

        cls.__init__ = new_init
        return cls

    return decorator


def fixed_size_digit_string(size):
    """Factory function to create DigitString classes with fixed size"""

    def decorator(cls):
        original_init = cls.__init__

        @wraps(original_init)
        def new_init(self, octets, *args, **kwargs):
            DigitString.__init__(self, octets, size)
            if (
                hasattr(original_init, "__code__")
                and original_init.__code__ != DigitString.__init__.__code__
            ):
                original_init(self, octets, *args, **kwargs)

        cls.__init__ = new_init
        return cls

    return decorator


def fixed_size_ia5_string(size):
    """Factory function to create DigitString classes with fixed size"""

    def decorator(cls):
        original_init = cls.__init__

        @wraps(original_init)
        def new_init(self, octets, *args, **kwargs):
            Ia5String.__init__(self, octets, size)
            if (
                hasattr(original_init, "__code__")
                and original_init.__code__ != Ia5String.__init__.__code__
            ):
                original_init(self, octets, *args, **kwargs)

        cls.__init__ = new_init
        return cls

    return decorator


class OctetString:
    """Implement ASN.1 Octet String type with optional size and boundaries constraints"""

    def __init__(self, octets, size: int = None, lower: int = None, upper: int = None):
        if size is None:
            size = len(octets)
        elif size and size != len(octets):
            raise exceptions.OctetStringError(
                f"{size:=} parameter is different from octets' length: {len(octets)}"
            )
        if lower and lower > size:
            raise exceptions.OctetStringError(
                f"{size:=} is smaller than {lower:=} limit"
            )
        if upper and size > upper:
            raise exceptions.OctetStringError(
                f"{size:=} is bigger than {upper:=} limit"
            )
        self.octets = octets
        self.size = size


class DigitString(OctetString):
    """ASN.1 DigitString implementation for OCTET STRING (SIZE(1..n))"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @cached_property
    def digits(self):  # sourcery skip: identity-comprehension
        # When you iterate over a bytes object, it returns the bytes as integers
        return [byte for byte in self.octets]

    @property
    def value(self) -> str:
        """Returns the n digits as a string"""
        return "".join(str(d) for d in self.digits)


class Bool:
    """Flag type for presence of optional NULL values"""

    @property
    def value(self):
        return True


@fixed_size_digit_string(1)
class ByteEnum(DigitString):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def value(self):
        return self.VALUES[int.from_bytes(self.octets, "big")]


class AddressString(OctetString):
    """ASN.1 AddressString implementation for OCTET STRING (SIZE(1..20))

    Format:
    - First octet: TON (4 bits) + NPI (4 bits)
    - Subsequent octets: TBCD encoded digits (2 digits per octet)
    """

    # Type of Number (TON) values
    TON_UNKNOWN = 0
    TON_INTERNATIONAL = 1
    TON_NATIONAL = 2
    TON_NETWORK_SPECIFIC = 3
    TON_SUBSCRIBER = 4
    TON_ALPHANUMERIC = 5
    TON_ABBREVIATED = 6
    TON_RESERVED = 7

    # Numbering Plan Indicator (NPI) values
    NPI_UNKNOWN = 0
    NPI_ISDN = 1
    NPI_DATA = 3
    NPI_TELEX = 4
    NPI_PRIVATE = 9
    NPI_RESERVED = 15

    def __init__(self, octets: bytes):
        super().__init__(octets, lower=1, upper=20)
        self._parse_ton_npi()
        self._parse_digits()

    def _parse_ton_npi(self):
        """Parse Type of Number and Numbering Plan Indicator from first octet"""
        first_octet = self.octets[0]
        self.ton = (first_octet >> 4) & 0x0F  # Extract bits 8-5
        self.npi = first_octet & 0x0F  # Extract bits 4-1

    def _parse_digits(self):
        """Parse TBCD-encoded digits from remaining octets"""
        self.digits = TBCDString(self.octets[1:], size=19).value

    @property
    def value(self):
        return self.digits

    def __str__(self) -> str:
        """String representation including TON/NPI and number"""
        return f"TON={self.ton}, NPI={self.npi}, Number={self.digits}"


class Ia5String(OctetString):
    """ASN.1 IA5String implementation for OCTET STRING (SIZE(1..n))"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def value(self):
        return "".join(chr(byte) for byte in self.octets)


class TBCDString(OctetString):
    """TBCDString ::= OCTET STRING (SIZE(1..n))

    |    |    |    |    |    |    |    |    |
    |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
    |    |    |    |    |    |    |    |    |
    /---------------------------------------|
    |     2nd digit     |     1st digit     | octet 1
    +-------------------+-------------------+
    |     4th digit     |     3rd digit     | octet 2
    +-------------------+-------------------+
    |     6th digit     |     5th digit     | octet 3
    \---------------------------------------/
                        .
                        .
                        .
    /---------------------------------------|
    |   (2n)th digit    | (2n - 1)th digit  | octet n
    \---------------------------------------/

    - Digits 0 to 9, two digits per octet,
    each digit encoded 0000 to 1001,
    - Overdecadic digits H'A to H'E, two digits
    per octet, each digit encoded as 1010 to 1110
    - Number 1111 used as filler when an odd
    number of digits occurs

    Bits 4 to 1 of octet n, encoding digit 2n-1.

    Bits 8 to 5 of octet n, encoding digit 2n.

    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._parse_digits()

    def _parse_digits(self):
        digits = []
        for octet in self.octets:
            # Extract two digits from each octet
            digit1 = octet & 0x0F
            digit2 = (octet >> 4) & 0x0F
            digits.extend([digit1, digit2])
        if self.size % 2 != 0:
            digits.append(15)  # Filler
        self.digits = digits

    @property
    def value(self):
        "Returns the 2n digits as a string"
        return "".join(self.digits)


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
