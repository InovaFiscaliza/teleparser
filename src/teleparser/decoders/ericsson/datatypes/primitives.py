"""This module implements primitive datatypes as described in the ASN.1 Especification"""

from functools import wraps
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

    __slots__ = ("octets", "size", "value")

    def __init__(
        self,
        octets,
        size: int | None = None,
        lower: int | None = None,
        upper: int | None = None,
    ):
        self.octets = octets

        if size is None:
            size = len(octets)
        elif size and size > len(octets):
            raise exceptions.OctetStringError(
                f"{size=} parameter is bigger than octets' length: {len(octets)}"
            )
        if lower and lower > size:
            raise exceptions.OctetStringError(f"{size=} is smaller than {lower=} limit")
        if upper and size > upper:
            raise exceptions.OctetStringError(f"{size=} is bigger than {upper=} limit")
        self.octets = octets
        self.size = size


class DigitString(OctetString):
    """ASN.1 DigitString implementation for OCTET STRING (SIZE(1..n))"""

    __slots__ = ("octets", "size", "digits", "value")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.digits = list(self.octets)
        self.value = "".join(str(d) for d in self.digits)


class Bool:
    """Flag type for presence of optional NULL values"""

    __slots__ = ("value",)

    def __init__(self, byte: bytes):
        assert not byte, "byte should be empty"
        self.value = True


@fixed_size_digit_string(1)
class ByteEnum(DigitString):

    # VALUES dict will be defined in runtime for inherited classes
    VALUES = {}     
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.value = self._value()

    def _value(self):
        return self.VALUES.get(int.from_bytes(self.octets, "big"), "Unknown")


class AddressString(OctetString):
    """ASN.1 AddressString implementation for OCTET STRING (SIZE(1..20))

    Format:
    - First octet: TON (4 bits) + NPI (4 bits)
    - Subsequent octets: TBCD encoded digits (2 digits per octet)
    """

    __slots__ = ("octets", "size", "ton", "npi", "digits", "value")

    # https://www.infobip.com/glossary/ton-npi-settings
    TON_LABELS: dict[int, str] = {
    0: "Unknown",
    1: "International",
    2: "National",
    3: "Network-Specific",
    4: "Subscriber Number",
    5: "Alphanumeric",
    6: "Abbreviated",
    7: "Reserved",
}

    NPI_LABELS: dict[int, str] = {
    0: "Unknown",
    1: "ISDN/telephone numbering plan (E163/E164)",
    3: "Data numbering plan (X.121)",
    4: "Telex numbering plan (F.69)",
    6: "Land Mobile (E.212)",
    8: "National numbering plan",
    9: "Private numbering plan",
    10: "ERMES numbering plan (ETSI DE/PS 3 01-3)",
    13: "Internet (IP)",
    18: "WAP Client Id (to be defined by WAP Forum)",
}

    def __init__(self, octets: bytes, **kwargs):
        super().__init__(octets, **kwargs)
        self._parse_ton_npi()
        self._parse_digits()
        self.value = self._value()

    def _parse_ton_npi(self):
        """Parse Type of Number and Numbering Plan Indicator from first octet"""
        first_octet = self.octets[0]
        self.ton = AddressString.TON_LABELS.get((first_octet >> 4) & 0x0F, "Unknown")  # Extract bits 8-5
        self.npi = AddressString.NPI_LABELS.get(first_octet & 0x0F, "Unknown")  # Extract bits 4-1

    def _parse_digits(self):
        """Parse TBCD-encoded digits from remaining octets"""
        self.digits = TBCDString(self.octets[1:]).digits

    def _value(self):
        """Return a dictionary representation of the address"""
        return {
            "ton": self.ton,
            "npi": self.npi,
            "digits": "".join(self.digits),
        }

    def __str__(self) -> str:
        """String representation including TON/NPI and number"""
        return f"TON={self.ton}, NPI={self.npi}, Number={self.digits}"


class Ia5String(OctetString):
    """ASN.1 IA5String implementation for OCTET STRING (SIZE(1..n))"""

    __slots__ = ("octets", "size", "value")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.value = "".join(chr(byte) for byte in self.octets)


class TBCDString(OctetString):
    r"""TBCDString ::= OCTET STRING (SIZE(1..n))

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

    __slots__ = ("octets", "size", "digits", "value")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._parse_digits()
        self.value = "".join(self.digits)

    @staticmethod
    def _digit_to_str(d):
        if 0 <= d <= 9:
            return str(d)
        elif 10 <= d <= 15:
            return chr(ord('A') + d - 10)
        else:
            return str(d)

    def _parse_digits(self):
        digits = []
        for octet in self.octets:
            # Extract two digits from each octet
            digit1 = octet & 0x0F
            digit2 = (octet >> 4) & 0x0F
            digits.extend([digit1, digit2])
        self.digits = [self._digit_to_str(d) for d in digits]


class UnsignedInt:
    """OCTET STRING is coded as an unsigned integer."""

    __slots__ = ("octets", "size", "value")

    def __init__(self, octets: bytes, size: int):
        if not isinstance(octets, bytes):
            raise TypeError(f"Octet parameter is not a byte object: {type(octets)}")
        if not isinstance(size, int):
            raise TypeError(f"size parameter is not an int: {type(octets)}")
        # assert len(octets) == size, f"Parameter should have size {size}, {len(octets)=}"
        self.octets = octets
        self.value = int.from_bytes(octets, byteorder="big")
