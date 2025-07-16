from ..primitives import TBCDString
from teleparser.prestadoras import PRESTADORAS


class AccountCode(TBCDString):
    """Account Code

    This parameter indicates which account is to be charged
    for the call.

    The Account Code contains the account code entered by
    the calling or called subscriber.

      ASN.1 Formal Description
      AccountCode ::= TBCDString (SIZE(1..5))
      Note: Only decimal digits are used.
    """

    def __init__(self, octets):
        super().__init__(octets, lower=1, upper=5)


class CarrierIdentificationCode(TBCDString):
    """Carrier Identification Code

    This parameter identifies which interexchange carrier
    was used for the Call Component.

    This parameter is present only when an interexchange
    carrier was used.

      ASN.1 Formal Description
      CarrierIdentificationCode ::= TBCDString (SIZE(1..3))
    """

    def __init__(self, octets):
        super().__init__(octets, lower=1, upper=3)


class IMSI(TBCDString):
    """ASN.1 Formal Description
    IMSI ::= TBCDString (SIZE(3..8))
    |    |    |    |    |    |    |    |    |
    |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
    |    |    |    |    |    |    |    |    |
    /---------------------------------------/
    |  MCC digit 2      |  MCC digit 1      | octet 1
    +-------------------+-------------------+
    |  MNC digit 1      |  MCC digit 3      | octet 2
    +-------------------+-------------------+
    |  MSIN digit 1     |  MNC digit 2      | octet 3
    +-------------------+-------------------+
    |  MSIN digit 3     |  MSIN digit 2     | octet 4
    /---------------------------------------/
    .
    .
    .
    /---------------------------------------/
    |  MSIN digit 2n-7  |  MSIN digit 2n-8  | octet n-1
    +-------------------+-------------------+
    |  See note         |  MSIN digit 2n-6  | octet n
    /---------------------------------------/
    Note: bits 5-8 of octet n contain
    - last MSIN digit, or
    - 1111 used as a filler when there is an odd
    total number of digits.
    MCC Mobile Country Code (octet 1 and bits 1-4 of octet 2)
    MNC Mobile Network Code (bits 5-8 of octet 2 and bits 1-4
    of octet 3).
    MSIN Mobile Subscriber Identification Number
    The total number of digits should not exceed 15.
    Digits 0 to 9, two digits per octet,
    each digit encoded 0000 to 1001
    """

    __slots__ = ("octets", "size", "digits", "mcc", "mnc", "msin", "carrier", "value")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._parse_mcc_mnc_msin()
        self.value = self._value()

    def _parse_mcc_mnc_msin(self):
        # According to ASN.1 specification:
        # MCC: digit 1, digit 2, digit 3 (positions 0, 1, 2 in digits array)
        # MNC: digit 1, digit 2 (positions 3, 4 in digits array)
        # MSIN: remaining digits (from position 5 onwards)

        if len(self.digits) < 5:
            raise ValueError(
                f"IMSI must have at least 5 digits, got {len(self.digits)}"
            )

        # Extract MCC (Mobile Country Code) - first 3 digits
        mcc_digits = self.digits[0:3]
        self.mcc = "".join(str(d) for d in mcc_digits)

        # Extract MNC (Mobile Network Code) - next 2 digits
        mnc_digits = self.digits[3:5]
        mnc = "".join(str(d) for d in mnc_digits)

        # Extract MSIN (Mobile Subscriber Identification Number) - remaining digits
        msin_digits = self.digits[5:]

        # Validate MSIN length constraint
        assert len(msin_digits) <= 10, (
            f"MSIN digits should not exceed 10, got {len(msin_digits)}"
        )

        # Total digits should not exceed 15 (MCC=3 + MNC=2 + MSIN≤10)
        total_digits = len(self.digits)
        assert total_digits <= 15, (
            f"Total IMSI digits should not exceed 15, got {total_digits}"
        )

        # Set instance variables
        self.carrier = PRESTADORAS[mnc]
        self.msin = "".join(str(d) for d in msin_digits)

    def _value(self):
        return self.carrier._asdict() | {"msin": self.msin}

    def __str__(self) -> str:
        return f"{self.carrier.nome} (MCC: {self.carrier.mcc}, MNC: {self.carrier.mnc}) MSIN: {self.msin}"


class ProcedureCode(TBCDString):
    """ASN.1 Formal Description
    ProcedureCode ::= TBCDString (SIZE(1))
    """

    def __init__(self, octets: bytes):
        super().__init__(octets, size=1)


class ServiceCode(TBCDString):
    """Unstructured Supplementary Service Data Service Code

    This parameter identifies the call-independent
    USSD service in the case of a mobile-initiated
    service request.

    The parameter values are defined by the operator and
    are administered with General Purpose Digit Analysis.

    The operator can associate a USSD Service Code with
    a USSD Application Identifier. The service code is
    part of the MSC/VLR-supported formats for USSD strings
    of UE-initiated USSD operations. For further details,
    see the Application Information for function
    block MUSSAN.

    This parameter is unavailable for a network-initiated
    service request.

      ASN.1 Formal Description
      ServiceCode ::= TBCDString (SIZE(1..2))
    """

    def __init__(self, octets):
        super().__init__(octets, lower=1, upper=2)
