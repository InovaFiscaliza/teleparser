"""This module implement simple datatypes inherited from the primitives
It's organized here because it's just the boilerplate of the type name and its description
"""

from functools import cached_property
from . import primitives


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
        month = int.from_bytes(self.octets[i], "big")
        assert 1 <= month <= 12, f"Month should be in range 1-12: {month}"
        day = int.from_bytes(self.octets[i + 1], "big")
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


class LCSClientIdentity(primitives.AddressString):
    """LCS Client Identity
    This parameter contains the identity of external client
    interacting with an LCS Server for the purpose of obtaining
    location information for one or more mobile stations.
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


class TargetMSISDN(primitives.AddressString):
    """Target MSISDN

    This LCS parameter contains the MSISDN number for which
    positioning is performed."""


class TerminatingLocationNumber(primitives.AddressString):
    """Terminating Location Number

    This parameter contains information, that is, the TON,
    the NPI, and the number, to identify the location of
    the called subscriber.

    This parameter contains the location number assigned
    to the called-subscriber's cell, location area or MSC/VLR
    cell.
    """


class Time(primitives.AddressString):
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
