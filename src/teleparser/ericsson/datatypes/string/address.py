from ..primitives import AddressString


class CallingPartyNumber(AddressString):
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


class CAMELCallingPartyNumber(AddressString):
    """CAMEL Calling Party Number

    This parameter contains the calling party number which is
    used when a call is routed from CAMEL Service Environment
    back to PLMN.
    """


class CAMELSMSAddress(AddressString):
    """CAMEL SMS Address

    The CAMEL SMS Address is CAMEL specific parameter. It is
    used to address the CAMEL Service Environment instance to
    which successful Short Message Service invocation
    notification(s) are sent during the handling of short
    message.
    """


class ChargeNumber(AddressString):
    """Charge Number  (M)

    This parameter contains the TON, the NPI, and one of

    following numbers: calling party number, called party

    number, or switch identity, depending on chargeable

    traffic activity. The Charge Number parameter is not

    included in the CDR for Japan. The parameter Contractor

    Number is used instead.

    """


class ChargedCallingPartyNumber(AddressString):
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


class ContractorNumber(AddressString):
    """Contractor Number

    This parameter indicates the contractor number, that is,
    the TON, the NPI, and the number, for identifying the
    contractor who provides the service.

    The parameter is only applicable for WCDMA Japan.
    """


class GsmSCFAddress(AddressString):
    """gsmSCF Address

    The gsmSCF Address is CAMEL specific parameter. It is
    used to address the CAMEL Service Environment instance
    to which successful Supplementary Service Invocation
    notification(s) are sent during the call.
    """

    def __init__(self, octets):
        super().__init__(octets, lower=1, upper=9)


class LCSClientIdentity(AddressString):
    """LCS Client Identity
    This parameter contains the identity of external client
    interacting with an LCS Server for the purpose of obtaining
    location information for one or more mobile stations.
    """


class MobileStationRoamingNumber(AddressString):
    """Mobile Station Roaming Number

    This parameter contains the MSRN, that is, the TON,
    the NPI, and the number.

    In the case of CallForwarding component in GMSC, this
    parameter is not output.

    In the case of an UE Terminating SMS in an SMS-GMSC
    component, this parameter can be received from HLR
    instead of the MSC Number.
    """


class MSCAddress(AddressString):
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


class MSCIdentification(AddressString):
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


class MSCNumber(AddressString):
    """MSC Number

    This parameter indicates the MSC address, that is, the TON,
    the NPI, and the number. The MSC Number parameter is used
    to identify a mobile switching center. For mobile
    originated SMS, the MSC Number represents the actual
    MSC/VLR address. For mobile terminated SMS, it represents
    the SMS Gateway MSC (SMS-GMSC) address and is used by the
    HLR to route the short message towards the SMS-GMSC.
    """


class NetworkProvidedCallingPartyNumber(AddressString):
    """Network Provided Calling Party Number

    This parameter contains the calling party number provided
    by the network that can be used in GSM/ISDN service
    interworking cases.
    """


class OriginalCalledNumber(AddressString):
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


class OriginatingLocationNumber(AddressString):
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


class RedirectingDropBackNumber(AddressString):
    """Redirecting Drop Back Number

    This parameter contains the called-party number which
    caused the initiation of Call Drop Back.

    This parameter is available if Call Drop Back is used.

    The parameter is not applicable for WCDMA Japan."""


class RedirectingNumber(AddressString):
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


class RedirectingSPN(AddressString):
    """Redirecting Single Personal Number

    This parameter contains the called-party number which
    """


class ServiceCentreAddress(AddressString):
    """Service Centre Address  (M)

    This parameter indicates the Service Centre address, that
    is, the TON, the NPI, and the number.
    """


class ServedSubscriberNumber(AddressString):
    """Served Subscriber Number  (M)

    This parameter contains the Type of Number (TON), Numbering
    Plan Indicator (NPI), and the number of served subscriber.

    The parameter is not applicable for WCDMA Japan."""


class TargetMSISDN(AddressString):
    """Target MSISDN

    This LCS parameter contains the MSISDN number for which
    positioning is performed."""


class TerminatingLocationNumber(AddressString):
    """Terminating Location Number

    This parameter contains information, that is, the TON,
    the NPI, and the number, to identify the location of
    the called subscriber.

    This parameter contains the location number assigned
    to the called-subscriber's cell, location area or MSC/VLR
    cell.
    """


class TranslatedNumber(AddressString):
    """Translated Number

    The Translated Number is obtained from the B-number
    analysis which may modify the received called party number.
    The purpose of this number is to determine the
    routing before being sent towards the outgoing side.

    In case called party number is not modified in B-number
    analysis the translated number contains the same number
    as the called party number."""


class UserProvidedCallingPartyNumber(AddressString):
    """User Provided Calling Party Number

    This parameter contains the calling party number provided by
    the user that can be used in GSM/ISDN service interworking
    cases.
    """
