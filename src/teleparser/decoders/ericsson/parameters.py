from .decorators import fixed_size_unsigned_int, UnsignedInt
from . import primitives


@fixed_size_unsigned_int(3)
class CallIDNumber(UnsignedInt):
    """Call Identification Number  (M)

    This parameter is a unique number within the own exchange
    that identifies the Call Component.

    All Call Modules produced in the same Call Component
    have the same call identification number; that is,
    if partial output records are produced for the same
    Call Component, the same call identification number
    is used
    """

    pass  # No need to override __init__ anymore


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


class ChargeNumber(primitives.AddressString):
    """Charge Number  (M)

    This parameter contains the TON, the NPI, and one of

    following numbers: calling party number, called party

    number, or switch identity, depending on chargeable

    traffic activity. The Charge Number parameter is not

    included in the CDR for Japan. The parameter Contractor

    Number is used instead.

    """


class ContractorNumber(primitives.AddressString):
    """Contractor Number

    This parameter indicates the contractor number, that is,
    the TON, the NPI, and the number, for identifying the
    contractor who provides the service.

    The parameter is only applicable for WCDMA Japan.
    """


class GsmSCFAddress(primitives.AddressString):
    """gsmSCF Address

    The gsmSCF Address is CAMEL specific parameter. It is
    used to address the CAMEL Service Environment instance
    to which successful Supplementary Service Invocation
    notification(s) are sent during the call.
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


@fixed_size_unsigned_int(3)
class RecordSequenceNumber(UnsignedInt):
    """Record Sequence Number  (M)

    This parameter contains a consecutive number for each
    Call Data Record generated and output.
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


class TerminatingLocationNumber(primitives.AddressString):
    """Terminating Location Number

    This parameter contains information, that is, the TON,
    the NPI, and the number, to identify the location of
    the called subscriber.

    This parameter contains the location number assigned
    to the called-subscriber's cell, location area or MSC/VLR
    cell.
    """


class TranslatedNumber(primitives.AddressString):
    """Translated Number

    The Translated Number is obtained from the B-number
    analysis which may modify the received called party number.
    The purpose of this number is to determine the
    routing before being sent towards the outgoing side.

    In case called party number is not modified in B-number
    analysis the translated number contains the same number
    as the called party number."""


@fixed_size_unsigned_int(1)
class TypeOfCallingSubscriber(UnsignedInt):
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


class UserProvidedCallingPartyNumber(primitives.AddressString):
    """User Provided Calling Party Number
    
    This parameter contains the calling party number provided by 
    the user that can be used in GSM/ISDN service interworking 
    cases.
    """


if __name__ == "__main__":
    print(f"{TAC(b'\x00\x02\x01').value=}")

    print(f"{CallIDNumber(b'|;\xac').value=}")
``` 
