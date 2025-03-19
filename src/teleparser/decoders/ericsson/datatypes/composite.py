"""This module implement simple datatypes inherited from the primitives
It's organized here because it's just the boilerplate of the type name and its description
"""

from collections import namedtuple
from functools import cached_property
from . import primitives

Carrier = namedtuple("Carrier", ["name", "mcc", "mnc"])

CARRIERS = (
    Carrier("ALGAR_TELECOM", 724, 33),
    Carrier("ALGAR_TELECOM", 724, 34),
    Carrier("ALGAR_TELECOM", 724, 32),
    Carrier("AMERICANET", 724, 26),
    Carrier("ARQIA", 724, 299),
    Carrier("BBS_OPTIONS", 724, 299),
    Carrier("CINCO", 724, 299),
    Carrier("CLARO", 724, 38),
    Carrier("CLARO", 724, 5),
    Carrier("FAILED_CALLS", 724, 299),
    Carrier("FIX_LINE", 724, 999),
    Carrier("LIGUE", 724, 21),
    Carrier("CLARO_NXT_NEXTEL", 724, 0),
    Carrier("CLARO_NXT_NEXTEL", 724, 39),
    Carrier("NLT", 724, 299),
    Carrier("OI_MOVEL", 724, 31),
    Carrier("OI_MOVEL", 724, 16),
    Carrier("SERCOMTEL", 724, 15),
    Carrier("SURF", 724, 17),
    Carrier("TELECALL", 724, 299),
    Carrier("TIM", 724, 4),
    Carrier("TIM", 724, 3),
    Carrier("TIM", 724, 54),
    Carrier("TIM", 724, 2),
    Carrier("VECTO_MOBILE", 724, 299),
    Carrier("VIVO", 724, 23),
    Carrier("VIVO", 724, 6),
    Carrier("VIVO", 724, 10),
    Carrier("VIVO", 724, 11),
)


class CalledPartyNumber(primitives.AddressString):
    """Called Party Number

    This parameter contains Type of Number (TON), Numbering
    Plan Indicator (NPI), and the number, to identify
    the called party.

    In case of mobile originating Call Component, this
    parameter contains the number received from the UE,
    excluding prefixes. Overdecadic digits received from
    a user equipment can be mapped to other values using
    Exchange Parameters.

    In case of mobile terminating Call Component, mobile
    terminated short message service in MSC/VLR, and
    mobile terminated short message service in SMS-GMSC, the
    called party number is the called MSISDN number.

    In case of call forwarding component, the parameter
    contains the number of the party to whom the call is
    forwarded.

    In case of transit Call Component and roaming call
    forwarding component, this parameter contains the
    number received from the incoming network. See also
    the clarification for transit component in case of
    IN calls in the next paragraph.

    In all IN-traffic cases, the parameter has the possible
    IN-prefix. When a call is routed to an SSF/gsmSSF because
    of terminating IN service or terminating IN category key
    service, the parameter is the possible IN-prefix and
    MSISDN in case of transit component. In case of CAMEL
    service, the prefix mechanism is not used. When a call
    is routed from the SSF/gsmSSF, the parameter may be
    modified by SCF/gsmSCF.

    If an additional MSISDN is used as the called-subscriber
    number, either the 'main' MSISDN or the additional MSISDN
    is registered in the terminating Call Component, according
    to an Exchange Parameter.

    If the subscriber uses the 'international prefix button'
    ('+'-button), then Type of Number (TON) for the
    called-party number in the mobile-originating record
    contains TON=1(international format). No prefix is
    stored in the digit information.

    If the subscriber selects the international prefix by
    himself, then TON=2 (unknown), and the prefix is included
    in the beginning of digit information.

    No Called Party Number is available when a call is
    originated using emergency call set-up. Emergency calls are
    indicated in the Teleservice Code field."""


class CalledPartyMNPInfo(primitives.AddressString):
    """Called Party MNP Info

    This parameter contains information about the ported
    called party number, that is, TON, NPI, and the
    number.

    This parameter may contain routing information from
    Mobile Number Portability database.
    """


@primitives.fixed_size_unsigned_int(3)
class CallIDNumber(primitives.UnsignedInt):
    """Call Identification Number  (M)

    This parameter is a unique number within the own exchange
    that identifies the Call Component.

    All Call Modules produced in the same Call Component
    have the same call identification number; that is,
    if partial output records are produced for the same
    Call Component, the same call identification number
    is used
    """


class CallingPartyNumber(primitives.AddressString):
    """Calling Party Number

    This parameter contains the Type of Number (TON),
    Numbering Plan Indicator (NPI), and the calling
    party number.

    The calling party number is the calling MSISDN number
    in case of originating Call Component, mobile originated
    Short Message Service in MSC/VLR, mobile originated
    Short Message Service in SMS-IWMSC, or call independent
    supplementary service procedure.

    In case of Roaming Call Forwarding, Call Forwarding, and
    UE Terminating component, the calling party number is
    received from the incoming network.

    In the case of network-initiated USSD service request,
    this parameter contains the number for the served
    subscriber in the Subscriber Service Procedure service.

    When a call is routed from the SSF/gsmSSF, the parameter
    may be modified by the SCF/gsmSCF."""


class CAMELCallingPartyNumber(primitives.AddressString):
    """CAMEL Calling Party Number

    This parameter contains the calling party number which is
    used when a call is routed from CAMEL Service Environment
    back to PLMN.
    """


class CAMELSMSAddress(primitives.AddressString):
    """CAMEL SMS Address

    The CAMEL SMS Address is CAMEL specific parameter. It is
    used to address the CAMEL Service Environment instance to
    which successful Short Message Service invocation
    notification(s) are sent during the handling of short
    message.
    """


class ChargeAreaCode(primitives.DigitString):
    r"""ChargeAreaCode ::= OCTET STRING (SIZE(3))
 
    The digits for ID Code are encoded as a TBCD-STRING.
    
    |    |    |    |    |    |    |    |    | 
    |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 | 
    |    |    |    |    |    |    |    |    | 
    /---------------------------------------\ 
    | 2nd CA Code digit | 1st CA Code digit | octet 1 of TBCD 
    +-------------------+-------------------+ 
    | 4th CA Code digit | 3rd CA Code digit | octet 2 of TBCD 
    +-------------------+-------------------+ 
    | Filler            | 5th CA Code digit | octet 3 of TBCD 
    \---------------------------------------/ 
    
    Acceptable digits are between 0 and 9.
    
    Note1: CA Code consists currently of max 5 digits and
        the 6th digit is filler (H'F).
    Note2: In case of POICA the 6th digit is filler (H'0)."""

    @cached_property
    def digits(self):
        digits = [int.from_bytes(byte, byteorder="big") for byte in self.octets]
        assert all(0 <= digit <= 9 for digit in digits), (
            " Acceptable digits are between 0 and 9."
        )
        return digits


class ChargeNumber(primitives.AddressString):
    """Charge Number  (M)

    This parameter contains the TON, the NPI, and one of

    following numbers: calling party number, called party

    number, or switch identity, depending on chargeable

    traffic activity. The Charge Number parameter is not

    included in the CDR for Japan. The parameter Contractor

    Number is used instead.

    """


class ChargedCallingPartyNumber(primitives.AddressString):
    """Charged Calling Party Number

    The subscriber number that is charged for the call. The
    Charged Calling Party number is either the Default Calling
    Number (DCN) for the access or a validated calling party
    number received from the user.  The subscriber property of
    the calling party number determines if the DCN or the
    validated calling party number is charged. When a calling
    party number is not received from the user or the received
    calling party number is not successfully validated, the
    DCN is charged.  When a call is forwarded, the subscriber
    number forwarding the call is assumed to be a validated
    calling party number received from the user.

    The parameter is not applicable for WCDMA Japan."""


class ChargingIndicator(primitives.OctetString):
    r"""Charging Indicator
    
    |    |    |    |    |    |    |    |    |
    |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
    |    |    |    |    |    |    |    |    |
    /---------------------------------------\
    | MSB                               LSB |
    \---------------------------------------/
    
    - Bit 8-3: Unused, set always to 00000
    - Bit 2-1: Charging indicator
    
        00   No Indication
        01   No Charge
        10   Charge
        11   Spare
    """

    # Constants for charging indicator values
    NO_INDICATION = 0
    NO_CHARGE = 1
    CHARGE = 2
    SPARE = 3

    def __init__(self, octets: bytes):
        super().__init__(octets, size=1)
        self._parse_indicator()

    def _parse_indicator(self):
        value = int.from_bytes(self.octets, byteorder="big")
        # Extract bits 2-1 (the last 2 bits)
        self.indicator = value & 0x03
        # Validate that bits 8-3 are all zeros
        unused_bits = (value >> 2) & 0x3F
        assert unused_bits == 0, (
            f"Bits 8-3 should be all zeros, got: {bin(unused_bits)}"
        )

    @property
    def value(self):
        """Return the charging indicator as a string"""
        match self.indicator:
            case self.NO_INDICATION:
                return "No Indication"
            case self.NO_CHARGE:
                return "No Charge"
            case self.CHARGE:
                return "Charge"
            case self.SPARE:
                return "Spare"
            case _:
                return f"Unknown ({self.indicator})"


@primitives.fixed_size_unsigned_int(1)
class ChargingOrigin(primitives.UnsignedInt):
    """ASN.1 Formal Description
    ChargingOrigin ::= OCTET STRING (SIZE(1))
    |    |    |    |    |    |    |    |    |
    |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
    |    |    |    |    |    |    |    |    |
    /---------------------------------------/
    | MSB                               LSB |
    /---------------------------------------/
    Note: The OCTET STRING is coded as an unsigned integer.
    Values vary according to operator's definition.
    Value range: H'1 - H'7F
    """


class ContractorNumber(primitives.AddressString):
    """Contractor Number

    This parameter indicates the contractor number, that is,
    the TON, the NPI, and the number, for identifying the
    contractor who provides the service.

    The parameter is only applicable for WCDMA Japan.
    """


class C7CHTMessage(primitives.OctetString):
    """CCITT No.7 First Charging Change Message  (P)

      This parameter contains the time of the reception of the
      message and the data of the first CHT message. The first
      CHT message is received only if more than one tariff change
      is to be applied to the call.

      This parameter is available if received and the national
      signalling system supports the function.

      The parameter is not applicable for WCDMA Japan.

    ASN.1 Formal Description
        C7CHTMessage ::= OCTET STRING (SIZE (5))
        |    |    |    |    |    |    |    |    |
        |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
        |    |    |    |    |    |    |    |    |
        /---------------------------------------/
        |                  Hours                | octet 1
        +---------------------------------------+
        |                 Minutes               | octet 2
        +---------------------------------------+
        |  Message Ind.     |  Tariff Ind.      | octet 3
        +---------------------------------------+
        |            Traffic Factor             | octet 4
        +---------------------------------------+
        |            Time Indicator             | octet 5
        /---------------------------------------/
        TIME OF RECEPTION OF THE MESSAGE (octets 1 and 2)
        Octet 1 contains hours, value range 00-23
        Octet 2 contains minutes, value range 00-59
        MESSAGE INDICATOR (octet 3 bits 8-5)
        Indicator of the next tariff
        B8-B6 are reserved.
        B5:  0=  Tariff indicator is not present.
        1=  Tariff indicator is present.
        TARIFF INDICATOR (octet 3 bits 4-1)
        Value                Meaning
        _____                _______
        0                 Tariff scale 0
        (no time-dependent Tariff)
        1                 Tariff scale I (reserved)
        2                 Tariff scale II (0.1 second)
        3                 Tariff scale III (0.2 second)
        4                 Tariff scale IV (0.5 second)
        5                 Tariff scale V (1 second)
        6                 Tariff scale VI (2 second)
        7                 Tariff scale VII(4 second)
        8-15              Tariff scale VIII to XV (reserved)
        TARIFF FACTOR (octet 4)
        Number from H'1 to H'FF (coded in hexadecimal).
        TIME INDICATOR (octet 5)
        Bit 1 is coded as zero (reserved).
        Bits 8 7 6 5 4 3 2 1      Meaning:
        -------------
        0 0 0 0 0 0 0 0      Immediate Change
        0 0 0 0 0 0 1 0      00 Hours 15 Minutes
        0 0 0 0 0 1 0 0      00 Hours 30 Minutes
        0 0 0 0 0 1 1 0      00 Hours 45 Minutes
        .
        .
        1 1 0 0 0 0 0 0      24 Hours 00 Minutes
        1 1 0 0 0 0 1 0      Reserved
        .
        .
        1 1 1 1 1 1 1 0
    """

    TARIFF_INDICATOR = {
        0: "Tariff scale 0",
        1: "Tariff scale I (reserved)",
        2: "Tariff scale II (0.1 second)",
        3: "Tariff scale III (0.2 second)",
        4: "Tariff scale IV (0.5 second)",
        5: "Tariff scale V (1 second)",
        6: "Tariff scale VI (2 second)",
        7: "Tariff scale VII(4 second)",
    }

    def __init__(self, octets, **kwargs):
        super().__init__(octets, size=5, **kwargs)
        self._parse_hours_indicator()
        self._parse_minutes_indicator()
        self._parse_message_indicator()
        self._parse_tariff_indicator()
        self._parse_tariff_factor()
        self._parse_time_indicator()

    def _parse_hours_indicator(self):
        """Parse hours Indicator from first octet"""
        hours_indicator = self.octets[0]
        assert 0 <= hours_indicator <= 23, (
            f"Hours should be in range 0-23: {hours_indicator}"
        )
        self.hours_indicator = hours_indicator

    def _parse_minutes_indicator(self):
        """Parse minutes Indicator from second octet"""
        minutes_indicator = self.octets[1]
        assert 0 <= minutes_indicator <= 59, (
            f"Minutes should be in range 0-59: {minutes_indicator}"
        )

    def _parse_message_indicator(self):
        """Parse Message Indicator from third octet"""
        self.tarif_indicator_is_present = (self.octets[2] & 0xF0) == 0xF0

    def _parse_tariff_indicator(self):
        """Parse Tariff Indicator from third octet"""
        tariff_indicator = self.octets[2] & 0x0F
        if 8 <= tariff_indicator <= 15:
            self.tariff_indicator = "Tariff scale VIII to XV (reserved)"
            return
        self.tariff_indicator = self.TARIFF_INDICATOR[tariff_indicator]

    def _parse_tariff_factor(self):
        """Parse Tariff Factor from fourth octet"""
        tariff_factor = self.octets[3]
        assert 1 <= tariff_factor <= 255, (
            f"Tariff Factor should be in range 1-255: {tariff_factor}"
        )

    def _parse_time_indicator(self):
        """Parse Time Indicator from fifth octet in blocks of 15 minutes"""
        time_indicator = self.octets[4]
        assert 0 <= time_indicator <= 192, (
            f"Time Indicator should be in range 0-192: {time_indicator}"
        )
        self.time_indicator = time_indicator * 15

    @property
    def value(self):
        return (
            f"{self.hours_indicator:02d}:{self.minutes_indicator:02d}",
            self.message_indicator,
            self.tariff_indicator,
            self.tariff_factor,
            self.time_indicator,
        )


class Date(primitives.OctetString):
    r"""Date ::= OCTET STRING (SIZE(3..4))

    Note: The OCTET STRING is coded as an unsigned
        integer.

        The number of year digits is determined by exchange
        parameter.

    Two digit (Year) format:


    |    |    |    |    |    |    |    |    | 
    |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 | 
    |    |    |    |    |    |    |    |    | 
    /---------------------------------------\ 
    |                                       | octet 1 (Year) 
    +---------------------------------------+ 
    |                                       | octet 2 (Month) 
    +---------------------------------------+ 
    |                                       | octet 3 (Day) 
    \---------------------------------------/ 

    Year  (octet 1): Value range 0-99 (H'0 - H'63)
    Month (octet 2): Value range 1-12 (H'1 - H'C)
    Day   (octet 3): Value range 1-31 (H'1 - H'1F)


    Four digit (Year) format:


    |    |    |    |    |    |    |    |    | 
    |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 | 
    |    |    |    |    |    |    |    |    | 
    /---------------------------------------\ 
    |                                       | octet 1 (Year) 
    +---------------------------------------+ 
    |                                       | octet 2 (Year) 
    +---------------------------------------+ 
    |                                       | octet 3 (Month)
    +---------------------------------------+ 
    |                                       | octet 4 (Day) 
    \---------------------------------------/ 


    Year  (octet 1): Value range 19 or 20 (H'13 or H'14)
    Year  (octet 2): Value range 0 - 99 (H'0 - H'63)
    Month (octet 3): Value range 1 - 12 (H'1 - H'C)
    Day   (octet 4): Value range 1 - 31 (H'1 - H'1F)"""

    def __init__(self, octets: bytes):
        super().__init__(octets, lower=3, upper=4)
        self._parse_digits()

    def _parse_digits(self):
        if self.size == 4:
            self._extract_4digits_year()
            i = 2
        else:
            year = int.from_bytes(self.octets[:1], "big")
            assert 0 <= year <= 99, f"Year should be in range 0-99: {year}"
            self.year = year
            i = 1
        month = int.from_bytes(self.octets[i : i + 1], "big")
        assert 1 <= month <= 12, f"Month should be in range 1-12: {month}"
        day = int.from_bytes(self.octets[i + 1 :], "big")
        assert 1 <= day <= 31, f"Day should be in range 1-31: {day}"
        self.month = month
        self.day = day

    def _extract_4digits_year(self):
        year1 = int.from_bytes(self.octets[:1], "big")
        year2 = int.from_bytes(self.octets[1:2], "big")
        assert 19 <= year1 <= 20, f"Year should be in range 19-20: {year1}"
        assert 0 <= year2 <= 99, f"Year should be in range 0-99: {year2}"
        self.year = year1 * 100 + year2

    @property
    def value(self):
        """Return date string"""
        if self.size == 4:
            return f"{self.year:04d}-{self.month:02d}-{self.day:02d}"
        else:
            return f"{self.year:02d}-{self.month:02d}-{self.day:02d}"


@primitives.fixed_size_ia5_string(15)
class ExchangeIdentity(primitives.Ia5String):
    """Exchange Identity

      This parameter contains the identity (name) of the
      exchange where the output is initiated.

    ASN.1 Formal Description
        ExchangeIdentity ::= IA5STRING (SIZE(1..15))
        |    |    |    |    |    |    |    |    |
        |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
        |    |    |    |    |    |    |    |    |
        /---------------------------------------/
        |  1st character                        | octet 1
        /---------------------------------------/
        .
        .
        .
        /---------------------------------------/
        |  14th character                       | octet 14
        +---------------------------------------+
        |  15th character                       | octet 15
        /---------------------------------------/
    """


@primitives.fixed_size_unsigned_int(2)
class FaultCode(primitives.UnsignedInt):
    """Fault Code

      This parameter contains the internal End-of-Selection
      code (EOS), which defines the event that lead to
      disconnection of the call component.

      Fault codes are also present for successful calls. It
      can be determined from the EOS code if a fault occurred
      or not.

    ASN.1 Formal Description
        FaultCode ::= OCTET STRING (SIZE(2))
        |    |    |    |    |    |    |    |    |
        |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
        |    |    |    |    |    |    |    |    |
        /---------------------------------------/
        |MSB                                    |  octet 1
        +---------------------------------------+
        |                                    LSB|  octet 2
        /---------------------------------------/
        Note: OCTET STRING is coded as an unsigned integer.
        Note: Detailed information on fault code values is
        available in the Application Information "List
        Of End-Of-Selection Codes".
    """


class GSMCallReferenceNumber(primitives.DigitString):
    """GSM Call Reference Number

    This parameter is CAMEL specific information parameter.
    It applies to CAMEL calls and extended CAMEL calls with
    IN Capability. It correlates Call Data Records output
    from the GMSC/gsmSSF and the terminating MSC, or call
    data records from the originating MSC/gsmSSF and a network
    optional Call Data Record from the gsmSCF."""

    def __init__(self, octets: bytes):
        super().__init__(octets, lower=1, upper=8)


class GsmSCFAddress(primitives.AddressString):
    """gsmSCF Address

    The gsmSCF Address is CAMEL specific parameter. It is
    used to address the CAMEL Service Environment instance
    to which successful Supplementary Service Invocation
    notification(s) are sent during the call.
    """

    def __init__(self, octets):
        super().__init__(octets, lower=1, upper=9)


class IMSI(primitives.TBCDString):
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._parse_mcc_mnc_msin()

    def _parse_mcc_mnc_msin(self):
        mcc = self.digits[0]
        mnc = self.digits[1]
        msin = self.digits[2:]
        self.carrier = CARRIERS[(mcc, mnc)]
        self.msin = msin

    @property
    def value(self):
        return self.carrier.name, self.carrier.mcc, self.carrier.mnc, self.msin

    def __str__(self) -> str:
        return f"{self.carrier.name} (MCC: {self.carrier.mcc}, MNC: {self.carrier.mnc}) MSIN: {self.msin}"


@primitives.fixed_size_digit_string(2)
class InternalCauseAndLoc(primitives.DigitString):
    """Internal Cause and Location

    This parameter contains the reason why the call was
    disconnected, as well as where the disconnection decision
    was made.

    MAP, BSSAP, ISUP (or other National User Part) cause codes
    are converted to the Internal Cause and Location. The
    translation is market dependent and is defined by exchange
    parameters.

    This parameter is available if the cause has a
    relevant value.

    Values for Internal Cause and Location are described in
    Application Information for Application Information for
    block RA.

    ASN.1 Formal Description
    InternalCauseAndLoc ::= OCTET STRING (SIZE(2))
    |    |    |    |    |    |    |    |    |
    |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
    |    |    |    |    |    |    |    |    |
    /---------------------------------------/
    |         LOCATION                      |  octet 1
    +---------------------------------------+
    |         CAUSE                         |  octet 2
    /---------------------------------------/
    Note: OCTET STRING is coded as an unsigned integer.
    For values, see the Application Information for function
    block RA.
    Also see the Application Information "Mapping of Cause
    Codes and Location Information".
    """

    @property
    def value(self):
        self.location = self.digits[0]
        self.cause = self.digits[1]
        return self.location, self.cause

    def __str__(self):
        return f"Location: {self.location}, Cause: {self.cause}"


class LCSClientIdentity(primitives.AddressString):
    """LCS Client Identity
    This parameter contains the identity of external client
    interacting with an LCS Server for the purpose of obtaining
    location information for one or more mobile stations.
    """


@primitives.fixed_size_digit_string(1)
class MiscellaneousInformation(primitives.DigitString):
    """ASN.1 Formal Description
    MiscellaneousInformation ::= OCTET STRING (SIZE(1))
    |    |    |    |    |    |    |    |    |
    |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
    |    |    |    |    |    |    |    |    |
    /---------------------------------------/
    | MSB                               LSB |
    /---------------------------------------/
    Note: OCTET STRING is coded as an unsigned integer.
    Value range: H'0 - H'FE, value H'FF is reserved.
    """


class MobileStationRoamingNumber(primitives.AddressString):
    """Mobile Station Roaming Number

    This parameter contains the MSRN, that is, the TON,
    the NPI, and the number.

    In the case of CallForwarding component in GMSC, this
    parameter is not output.

    In the case of an UE Terminating SMS in an SMS-GMSC
    component, this parameter can be received from HLR
    instead of the MSC Number.
    """


class MSCAddress(primitives.AddressString):
    """MSC Address

    This parameter identifies the address of a mobile
    switching center when it functions as an MSC/VLR
    or as an SMS gateway MSC (SMS-GMSC), or when it
    acts as a visited MSC/VLR.

    For a mobile-originated call forwarding case, this
    parameter identifies the MSC/VLR address of the
    calling subscriber.

    For a mobile-terminated call forwarding case, this
    parameter identifies the MSC/VLR address of a called
    subscriber.

    For a roaming call forwarding case, this parameter
    identifies the MSC/VLR address of a called subscriber.

    For a mobile-originated Short Message Service, this
    parameter identifies the MSC/VLR address of a calling
    subscriber.

    For a mobile-terminated Short Message Service in the
    SMS-GMSC, this parameter identifies the MSC/VLR address
    of a called subscriber.

    For a mobile-terminated Short Message Service in the
    MSC/VLR, this parameter identifies the address of the
    SMS-GMSC.
    """


class MSCIdentification(primitives.AddressString):
    """MSC Identification

    This parameter indicates the identification of the (G)MSC
    where the output is initiated.

    MSC Identification is used as the own calling address when
    a MAP message is sent from the GMSC or MSC/VLR to other
    WCDMA network entities, for instance, HLR.

    The parameter is output in the transit component only
    in case the called party is a mobile subscriber with
    terminating IN service or terminating IN category key
    service or terminating CAMEL service."""


class MSCNumber(primitives.AddressString):
    """MSC Number

    This parameter indicates the MSC address, that is, the TON,
    the NPI, and the number. The MSC Number parameter is used
    to identify a mobile switching center. For mobile
    originated SMS, the MSC Number represents the actual
    MSC/VLR address. For mobile terminated SMS, it represents
    the SMS Gateway MSC (SMS-GMSC) address and is used by the
    HLR to route the short message towards the SMS-GMSC.
    """


@primitives.fixed_size_digit_string(5)
class NetworkCallReference(primitives.DigitString):
    """Network Call Reference  (M)

      This parameter provides a mechanism for the post-
      processing system to link together different call
      data records produced for a call or, when Multi Party
      Supplementary Service is invoked, several related calls
      within a node. As an option, Call Data Records produced
      in different nodes for the same call can contain the same
      Network Call Reference (NCR), if the signalling transfers
      the values between different nodes.

    ASN.1 Formal Description
        NetworkCallReference ::= OCTET STRING (SIZE(5))
        |    |    |    |    |    |    |    |    |
        |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
        |    |    |    |    |    |    |    |    |
        /---------------------------------------/
        | MSB       SEQUENCE NUMBER             |  octet 1
        +---------------------------------------+
        |           SEQUENCE NUMBER             |  octet 2
        +---------------------------------------+
        |           SEQUENCE NUMBER         LSB |  octet 3
        +---------------------------------------+
        | MSB       SWITCH IDENTITY             |  octet 4
        +---------------------------------------+
        |           SWITCH IDENTITY         LSB |  octet 5
        /---------------------------------------/
        Note: OCTET STRING is coded internally as an
        unsigned integer.
        -   Octet 1-3 Sequence number
        -   Octet 4-5 Switch identity
        Value range of Sequence number: H'0 - H'FFFFFF
        Value range of Switch identity: H'1 - H'FFFF
    """

    @property
    def value(self):
        self.sequence_number = int.from_bytes(self.octets[:3], "big")
        self.switch_identity = int.from_bytes(self.octets[3:], "big")
        return self.sequence_number, self.switch_identity

    def __str__(self):
        return f"{self.sequence_number:06d}-{self.switch_identity:04d}"


class NetworkProvidedCallingPartyNumber(primitives.AddressString):
    """Network Provided Calling Party Number

    This parameter contains the calling party number provided
    by the network that can be used in GSM/ISDN service
    interworking cases.
    """


@primitives.fixed_size_digit_string(3)
class NumberOfMeterPulses(primitives.DigitString):
    """ASN.1 Formal Description
    NumberOfMeterPulses ::=  OCTET STRING (SIZE(3))
    |    |    |    |    |    |    |    |    |
    |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
    |    |    |    |    |    |    |    |    |
    /---------------------------------------/
    | MSB                                   | octet 1
    +---------------------------------------+
    |                                       | octet 2
    +---------------------------------------+
    |                                  LSB  | octet 3
    /---------------------------------------/
    Note: OCTET STRING is coded as an unsigned integer.
    Value range: H'1 - H'FFFFFF
    """


class OriginalCalledNumber(primitives.AddressString):
    """Original Called Number

    This parameter identifies the original called party,
    including Type of Number (TON) and Numbering Plan
    Indicator (NPI), when the call is redirected.

    In the call forwarding component, the parameter contains
    the MSISDN number of the subscriber who forwarded the
    call, when the call is redirected once. In other cases,
    the parameter is received from the incoming network.

    When a call is routed from the SSF/gsmSSF, the parameter
    may be modified by the SCF/gsmSCF."""


class OriginatingLocationNumber(primitives.AddressString):
    """Originating Location Number

    This parameter contains information, that is,
    Type of Number(TON) and Numbering Plan Indicator(NPI)
    and the number to identify the location of the calling
    subscriber.

    In the case of an originating-Call Component, the
    parameter contains the location number assigned to
    the calling subscriber's cell, location area or
    MSC/VLR service area.

    In the case of a call-forwarding component, the
    parameter contains the location number assigned to
    the cell, location area or the MSC/VLR service area
    of the forwarding subscriber or the location number
    assigned for the GMSC service area."""


@primitives.fixed_size_unsigned_int(1)
class PartialOutputRecNum(primitives.UnsignedInt):
    """Partial Output Record Number

      This parameter contains a consecutive number which is
      incremented at every partial output for a call.

      It appears only if partial output has taken place.
    ASN.1 Formal Description
        PartialOutputRecNum ::= OCTET STRING (SIZE(1))
        |    |    |    |    |    |    |    |    |
        |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
        |    |    |    |    |    |    |    |    |
        /---------------------------------------/
        | MSB                              LSB  |
        /---------------------------------------/
        Note: OCTET STRING is coded as an unsigned integer.
        Value range: H'1 - H'FF
    """


@primitives.fixed_size_unsigned_int(3)
class RecordSequenceNumber(primitives.UnsignedInt):
    r"""Record Sequence Number  (M)

    This parameter contains a consecutive number for each
    Call Data Record generated and output.
    ASN.1 Formal Description

    RecordSequenceNumber ::= OCTET STRING (SIZE(3))

    |    |    |    |    |    |    |    |    |
    |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
    |    |    |    |    |    |    |    |    |
    /---------------------------------------\
    | MSB                                   | octet 1
    +---------------------------------------+
    |                                       | octet 2
    +---------------------------------------+
    |                                  LSB  | octet 3
    \---------------------------------------/

    Note: OCTET STRING is coded as an unsigned integer.

    Value range: H'0 - H'FFFFFF"""


@primitives.fixed_size_unsigned_int(1)
class RedirectionCounter(primitives.UnsignedInt):
    """ASN.1 Formal Description
    RedirectionCounter ::= OCTET STRING (SIZE(1))
    |    |    |    |    |    |    |    |    |
    |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
    |    |    |    |    |    |    |    |    |
    /---------------------------------------/
    | MSB                              LSB  |
    /---------------------------------------/
    Note: OCTET STRING is coded as an unsigned integer.
    Values     Meaning
    0 - 10     Number of redirections
    Note: The maximum value is set by an
    Exchange Parameter.
    """


class RedirectingDropBackNumber(primitives.AddressString):
    """Redirecting Drop Back Number

    This parameter contains the called-party number which
    caused the initiation of Call Drop Back.

    This parameter is available if Call Drop Back is used.

    The parameter is not applicable for WCDMA Japan."""


class RedirectingNumber(primitives.AddressString):
    """Redirecting Number

    This parameter contains Type of Number (TON), Numbering
    Plan Indicator (NPI), and the number, when the call is
    redirected, indicating the number from which the call
    was last redirected.

    The call forwarding component contains the MSISDN
    number of the mobile subscriber who forwarded the call
    when the call is redirected.

    The ISDN call forwarding component contains the subscriber
    number which has a call forwarding service active and
    therefore forwards the incoming call.

    When a call is routed from the SSF/gsmSSF, the parameter
    may be modified by SCF/gsmSCF.

    In other cases, the parameter is received from the
    incoming network."""


class RedirectingSPN(primitives.AddressString):
    """Redirecting Single Personal Number

    This parameter contains the called-party number which
    """


class RerountingIndicator(primitives.Bool):
    """Rerouting Indicator

    This parameter indicates if the call has been rerouted
    (for example a new B-number analysis has been performed)
    by the exchange where the charging data is output. This
    field is output only for ISOCODE or PACKED postprocessing
    purposes.
    """


@primitives.fixed_size_ia5_string(7)
class Route(primitives.Ia5String):
    """ASN.1 Formal Description
    Route ::= IA5STRING (SIZE(1..7))
    |    |    |    |    |    |    |    |    |
    |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
    |    |    |    |    |    |    |    |    |
    /---------------------------------------/
    |            1st character              | octet 1
    /---------------------------------------/
    .
    .
    .
    /---------------------------------------/
    |            6th character              | octet 6
    +---------------------------------------+
    |            7th character              | octet 7
    /---------------------------------------/
    """


class ServiceCentreAddress(primitives.AddressString):
    """Service Centre Address  (M)

    This parameter indicates the Service Centre address, that
    is, the TON, the NPI, and the number.
    """


class ServedSubscriberNumber(primitives.AddressString):
    """Served Subscriber Number  (M)

    This parameter contains the Type of Number (TON), Numbering
    Plan Indicator (NPI), and the number of served subscriber.

    The parameter is not applicable for WCDMA Japan."""


class ServiceKey(primitives.DigitString):
    def __init__(self, octets: bytes):
        super().__init__(octets, size=4)


class SubscriptionType(primitives.UnsignedInt):
    """Subscription Type

      This parameter indicates the subscription type used for
      mobile subscriber. This parameter enables grouping
      of mobile subscribers independent of their numbers.

      The parameter values are defined by operator. The value
      '0' is output if the feature 'Support for Subscription
      Type Dependent Analysis' is not active in the (G)MSC.

    ASN.1 Formal Description
        SubscriptionType ::= OCTET STRING (SIZE(1))
        |    |    |    |    |    |    |    |    |
        |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
        |    |    |    |    |    |    |    |    |
        /---------------------------------------/
        |                                       |
        /---------------------------------------/
        Value range: H'0 - H'7F
        Value H'0 : No subscription type
        Value H'1 - H'7F : Subscription type 1 - 127
    """


@primitives.fixed_size_unsigned_int(2)
class SwitchIdentity(primitives.UnsignedInt):
    """Switch Identity

      This parameter contains the identification
      number of the exchange where the output originated.

      This parameter is part of the Network Call Reference
      (NCR). Switch Identity in NCR identifies the exchange
      where the NCR has been generated. Thus, this parameter
      can be used to determine whether the own exchange
      generated the NCR or the NCR was received from the
      incoming network.

    ASN.1 Formal Description
        SwitchIdentity ::= OCTET STRING (SIZE(2))
        |    |    |    |    |    |    |    |    |
        |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
        |    |    |    |    |    |    |    |    |
        /---------------------------------------/
        | MSB                                   |   octet 1
        +---------------------------------------|
        |                                   LSB |   octet 2
        /---------------------------------------/
        Note: OCTET STRING is coded internally as
        an unsigned integer.
        Value range: H'1 - H'FFFF
    """


class TAC(primitives.OctetString):
    """Traffic Activity Code (TAC)  (M)

      This parameter contains information about traffic
      activity and consists of the following four parts:

    - Telecommunication Service Code (TSC)

      The Telecommunication Service Code parameter contains
      information about the telecommunication service used,
      for example, telephony, telefax, specific basic services,
      or Short Message Service. The Telecommunication Service
      Code is obtained from the telecommunication service
      analysis or from transmission medium requirement analysis.

    - Type of Seizure (TOS)

      This parameter points out a function family group,
      that is, subscriber service or "call/Short Message
      Service".

    - Type of Indicator (TOI)

      If the Type of Seizure indicates "Call/Short Message
      Service", this parameter contains information about
      which type of "call/Short Message Service", for example,
      call from UE, call to UE, roaming call forwarding, or
      mobile-originated short message in the MSC/VLR was set up.

      If the Type of Seizure indicates "Subscriber Service",
      this parameter indicates the Supplementary Service,
      for example, Call Forwarding, that was used.

    - Type of Procedure (TOP)

      This parameter indicates the procedure performed in the
      case of Supplementary Service, for example, activation
      or deactivation of the service is registered.
    """

    def __init__(self, octets):
        super().__init__(octets, lower=3, upper=4)
        try:
            self.string = octets.hex().upper()
        except AttributeError as e:
            raise primitives.OctetStringError("Error parsing octet") from e

    @property
    def value(self) -> str:
        # Extract individual octets
        tsc = self.string[:2]  # Telecom Service Code
        tos = self.string[2:4]  # Type of Seizure
        toi = self.string[4:6]  # Type of Indicator

        # Handle optional TOP octet
        top = self.string[6:8] if len(self.string) == 8 else ""

        # Build result string
        result = f"TSC={tsc} TOS={tos} TOI={toi}"
        if top:
            result += f" TOP={top}"

        return result


@primitives.fixed_size_unsigned_int(1)
class TypeOfCallingSubscriber(primitives.UnsignedInt):
    """Type of Calling Subscriber

    This parameter indicates that the type of subscriber is
    registered, for example, normal subscriber, subscriber
    with priority, or coin box.

    In case of a network-initiated USSD service request,
    this parameter contains the type of served subscriber in
    the Subscriber Service Procedure Call Module.

    When a call is routed from the SSF/gsmSSF, the parameter
    may be modified by SCF/gsmSCF.
    """


class TargetMSISDN(primitives.AddressString):
    """Target MSISDN

    This LCS parameter contains the MSISDN number for which
    positioning is performed."""


@primitives.fixed_size_digit_string(2)
class TariffClass(primitives.DigitString):
    """ASN.1 Formal Description
    TariffClass ::= OCTET STRING (SIZE(2))
    |    |    |    |    |    |    |    |    |
    |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
    |    |    |    |    |    |    |    |    |
    /---------------------------------------/
    | MSB                                   |  octet 1
    +---------------------------------------+
    |                                   LSB |  octet 2
    /---------------------------------------/
    Note: OCTET STRING is coded as an unsigned integer.
    Value varies according to operator's definition.
    Value range: H'0 - H'FFFF
    Value H'0: No tariff class is defined.
    """


class TerminatingLocationNumber(primitives.AddressString):
    """Terminating Location Number

    This parameter contains information, that is, the TON,
    the NPI, and the number, to identify the location of
    the called subscriber.

    This parameter contains the location number assigned
    to the called-subscriber's cell, location area or MSC/VLR
    cell.
    """


class Time(primitives.DigitString):
    r"""Time ::= OCTET STRING (SIZE(3..4))

    |    |    |    |    |    |    |    |    | 
    |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 | 
    |    |    |    |    |    |    |    |    | 
    /---------------------------------------\ 
    |                                       | octet 1 (Hour)
    +---------------------------------------+ 
    |                                       | octet 2 (Minute)
    +---------------------------------------+ 
    |                                       | octet 3 (Second)
    +---------------------------------------+ 
    |                                       | octet 4 (10th of
    \---------------------------------------/          a second)

    Note: OCTET STRING is coded as an unsigned integer.

    Hour             (octet 1): value range  0-23 (H'0 - H'17)
    Minute           (octet 2): value range  0-59 (H'0 - H'3B)
    Second           (octet 3): value range  0-59 (H'0 - H'3B)
    10th of a second (octet 4): value range  0-9  (H'0 - H'9)

    Note: 10th of a second is only included for the parameter
        chargeableDuration and only used for WCDMA Japan."""

    def __init__(self, octets: bytes):
        super().__init__(octets, lower=3, upper=4)
        self._parse_digits()

    def _parse_digits(self):
        hour = int.from_bytes(self.octets[:1], "big")
        minute = int.from_bytes(self.octets[1:2], "big")
        second = int.from_bytes(self.octets[2:3], "big")
        assert 0 <= hour <= 23, f"Hour should be in range 0-23: {hour}"
        assert 0 <= minute <= 59, f"Minute should be in range 0-59: {minute}"
        assert 0 <= second <= 59, f"Second should be in range 0-59: {second}"
        self.hour = hour
        self.minute = minute
        self.second = second
        if self.size == 4:
            tenth_of_a_second = int.from_bytes(self.octets[3:4], "big")
            assert 0 <= tenth_of_a_second <= 9, (
                f"10th of a second should be in range 0-9: {tenth_of_a_second}"
            )
            self.tenth_of_a_second = tenth_of_a_second

    @property
    def value(self):
        """Return datetime string"""
        value = f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}"
        if self.size == 4:
            value += f".{self.tenth_of_a_second:01d}"
        return value


class TranslatedNumber(primitives.AddressString):
    """Translated Number

    The Translated Number is obtained from the B-number
    analysis which may modify the received called party number.
    The purpose of this number is to determine the
    routing before being sent towards the outgoing side.

    In case called party number is not modified in B-number
    analysis the translated number contains the same number
    as the called party number."""


class UserProvidedCallingPartyNumber(primitives.AddressString):
    """User Provided Calling Party Number

    This parameter contains the calling party number provided by
    the user that can be used in GSM/ISDN service interworking
    cases.
    """
