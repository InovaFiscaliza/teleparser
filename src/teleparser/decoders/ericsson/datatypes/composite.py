"""This module implement simple datatypes inherited from the primitives
It's organized here because it's just the boilerplate of the type name and its description
"""

from collections import namedtuple
from functools import cached_property
from . import primitives
from .decorators import fixed_size_unsigned_int, fixed_size_digit_string


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


class AirInterfaceUserRate(primitives.ByteEnum):
    """ASN.1 Formal Description
    AirInterfaceUserRate ::= ENUMERATED
    (aIUR9600bps                  (1),
    aIUR14400bps                 (2),
    aIUR19200bps                 (3),
    aIUR28800bps                 (5),
    aIUR38400bps                 (6),
    aIUR43200bps                 (7),
    aIUR57600bps                 (8),
    aIUR38400bps1                (9),
    aIUR38400bps2                (10),
    aIUR38400bps3                (11),
    aIUR38400bps4                (12))
    Note: Values 9 - 12 mean that the network has interpreted
    AirInterfaceUserRate as 38400 bits/s.
    """

    VALUES = {
        1: "aIUR9600bps",
        2: "aIUR14400bps",
        3: "aIUR19200bps",
        5: "aIUR28800bps",
        6: "aIUR38400bps",
        7: "aIUR43200bps",
        8: "aIUR57600bps",
        9: "aIUR38400bps1",
        10: "aIUR38400bps2",
        11: "aIUR38400bps3",
        12: "aIUR38400bps4",
    }


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


@fixed_size_unsigned_int(3)
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


class ChargedParty(primitives.ByteEnum):
    """ASN.1 Formal Description
    ChargedParty ::= ENUMERATED
    (chargingOfCallingSubscriber  (0),
    chargingOfCalledSubscriber   (1),
    noCharging                   (2))
    """

    VALUES = {
        0: "chargingOfCallingSubscriber",
        1: "chargingOfCalledSubscriber",
        2: "noCharging",
    }


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


@fixed_size_unsigned_int(1)
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


class EosInfo(primitives.ByteEnum):
    """ASN.1 Formal Description
    EosInfo ::= OCTET STRING (SIZE(1))
    |    |    |    |    |    |    |    |    |
    |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
    |    |    |    |    |    |    |    |    |
    /---------------------------------------/
    | MSB                               LSB |
    /---------------------------------------/
    Note: OCTET STRING is coded as an unsigned integer.
    Value range:  H'0 - H'3F
    End-of-Selection Information
    Value        Meaning
    _____        _______
    00         Free subscriber.
    01         Free subscriber. No time supervision.
    02         Free subscriber. No charging.
    03         Free subscriber. No time supervision.
    No charging.
    04         Free subscriber. Last party release.
    05         Free subscriber. No time supervision.
    Last party release.
    06         Free subscriber. No charging. Last
    party release.
    07         Free subscriber. No time supervision.
    No charging. Last party release.
    10         Set up speech condition.
    11         Set up speech condition.
    No time supervision.
    12         Set up speech condition.
    No charging.
    21         Access barred
    22         Transferred subscriber.
    23         Busy subscriber.
    24         Busy subscriber with callback protection.
    25         Unallocated number.
    26         Address incomplete.
    27         Call transfer protection, that is
    "follow me" not allowed to this subscriber.
    28         Subscriber line out of order.
    29         Intercepted subscriber.
    2A         Supervised by an operator.
    Trunk offering marked.
    2B         Rerouting to service centre.
    2C         Line lock out.
    2D         Send acceptance tone.
    2E         No answer/incompatible destination
    (used for ISDN).
    2F         Send refusal tone. Only used
    at subscriber services.
    33         Digital path not provided.
    34         Congestion without differentiation.
    35         Time release.
    36         Technical fault.
    37         Congestion in group selection
    network.
    38         Lack of devices.
    39         Congestion in subscriber
    selection network.
    3A         Congestion in international
    network.
    3B         Congestion in national network.
    3C         Conditional congestion (Region option).
    3D         Route congestion.
    3E         Unpermitted traffic case.
    3F         No acknowledgement from mobile subscriber.
    """

    VALUES = {
        0: "Free subscriber.",
        1: "Free subscriber. No time supervision.",
        2: "Free subscriber. No charging.",
        3: "Free subscriber. No time supervision. No charging.",
        4: "Free subscriber. Last party release.",
        5: "Free subscriber. No time supervision. Last party release.",
        6: "Free subscriber. No charging. Last party release.",
        7: "Free subscriber. No time supervision. No charging. Last party release.",
        16: "Set up speech condition.",
        17: "Set up speech condition. No time supervision.",
        18: "Set up speech condition. No charging.",
        33: "Access barred",
        34: "Transferred subscriber.",
        35: "Busy subscriber.",
        36: "Busy subscriber with callback protection.",
        37: "Unallocated number.",
        38: "Address incomplete.",
        39: 'Call transfer protection, that is "follow me" not allowed to this subscriber.',
        40: "Subscriber line out of order.",
        41: "Intercepted subscriber.",
        42: "Supervised by an operator. Trunk offering marked.",
        43: "Rerouting to service centre.",
        44: "Line lock out.",
        45: "Send acceptance tone.",
        46: "No answer/incompatible destination (used for ISDN).",
        47: "Send refusal tone. Only used at subscriber services.",
        51: "Digital path not provided.",
        52: "Congestion without differentiation.",
        53: "Time release.",
        54: "Technical fault.",
        55: "Congestion in group selection network.",
        56: "Lack of devices.",
        57: "Congestion in subscriber selection network.",
        58: "Congestion in international network.",
        59: "Congestion in national network.",
        60: "Conditional congestion (Region option).",
        61: "Route congestion.",
        62: "Unpermitted traffic case.",
        63: "No acknowledgement from mobile subscriber.",
    }


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


class INMarkingOfMS(primitives.ByteEnum):
    """ASN.1 Formal Description
    INMarkingOfMS ::= ENUMERATED
    (originatingINService                                 (1),
    terminatingINService                                 (2),
    originatingINCategoryKeyService                      (3),
    terminatingINCategoryKeyService                      (4),
    originatingCAMELService                              (5),
    terminatingCAMELService                              (6),
    originatingExtendedCAMELServiceWithINCapabilityIndicator
    (7),
    terminatingExtendedCAMELServiceWithINCapabilityIndicator
    (8),
    originatingExtendedCAMELServiceWithOriginatingINCategoryKey
    (9),
    terminatingExtendedCAMELServiceWithTerminatingINCategoryKey
    (10),
    subscriberDialledCAMELService                       (11),
    subscriberDialledCAMELServiceAndOriginatingCAMELService
    (12),
    visitedTerminatingCAMELService                      (13))
    """

    VALUES = {
        1: "originatingINService",
        2: "terminatingINService",
        3: "originatingINCategoryKeyService",
        4: "terminatingINCategoryKeyService",
        5: "originatingCAMELService",
        6: "terminatingCAMELService",
        7: "originatingExtendedCAMELServiceWithINCapabilityIndicator ",
        8: "terminatingExtendedCAMELServiceWithINCapabilityIndicator",
        9: "originatingExtendedCAMELServiceWithOriginatingINCategoryKey",
        10: "terminatingExtendedCAMELServiceWithTerminatingINCategoryKey",
        11: "subscriberDialledCAMELService",
        12: "subscriberDialledCAMELServiceAndOriginatingCAMELService",
        13: "visitedTerminatingCAMELService",
    }


@fixed_size_digit_string(2)
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


@fixed_size_digit_string(1)
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


class NetworkProvidedCallingPartyNumber(primitives.AddressString):
    """Network Provided Calling Party Number

    This parameter contains the calling party number provided
    by the network that can be used in GSM/ISDN service
    interworking cases.
    """


@fixed_size_digit_string(3)
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


class OutputForSubscriber(primitives.ByteEnum):
    """Output for Subscriber

      This parameter indicates if the ICI output was made
      for the calling subscriber or called subscriber.

      This parameter is available only in ICI records.
    ASN.1 Formal Description
        OutputForSubscriber ::= ENUMERATED
        (callingParty           (0),
        calledParty            (1),
        callingAndCalledParty  (2))
    """

    VALUES = {
        0: "callingParty",
        1: "calledParty",
        2: "callingAndCalledParty",
    }


@fixed_size_unsigned_int(3)
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


@fixed_size_unsigned_int(1)
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


@fixed_size_unsigned_int(1)
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


@fixed_size_digit_string(2)
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


class TariffSwitchInd(primitives.ByteEnum):
    """ASN.1 Formal Description
    TariffSwitchInd ::= ENUMERATED
    (noTariffSwitch                    (0),
    tariffSwitchAfterStartOfCharging  (2))
    """

    VALUES = {
        0: "noTariffSwitch",
        2: "tariffSwitchAfterStartOfCharging",
    }


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


class TrafficClass(primitives.ByteEnum):
    """ASN.1 Formal Description
    TrafficClass ::= OCTET STRING (SIZE(1))
    |    |    |    |    |    |    |    |    |
    |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
    |    |    |    |    |    |    |    |    |
    /---------------------------------------/
    |                                       | octet 1
    /---------------------------------------/
    TrafficClass             Bits 8 7 6 5 4 3 2 1
    Conversational Class          0 0 0 0 0 0 0 0
    Streaming Class               0 0 0 0 0 0 0 1
    Interactive Class             0 0 0 0 0 0 1 0
    Background Class              0 0 0 0 0 0 1 1
    """

    VALUES = {
        0: "Conversational Class",
        1: "Streaming Class",
        2: "Interactive Class",
        3: "Background Class",
    }


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
