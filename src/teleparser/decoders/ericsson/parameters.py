from dataclasses import dataclass
from primitives import OctetString, UnsignedInt


class TAC(OctetString):
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
        super().__init__(octets)
        size = len(octets)
        assert size in {3, 4}, f"Size should be 3 or 4 for TAC, {size:=}"

    @property
    def value(self) -> str:
        # Convert bytes to hex string
        hex_str = self.string

        # Extract individual octets
        tsc = hex_str[:2]  # Telecom Service Code
        tos = hex_str[2:4]  # Type of Seizure
        toi = hex_str[4:6]  # Type of Indicator

        # Handle optional TOP octet
        top = hex_str[6:8] if len(hex_str) == 8 else ""

        # Build result string
        result = f"TSC={tsc} TOS={tos} TOI={toi}"
        if top:
            result += f" TOP={top}"

        return result


class CallIDNumber(UnsignedInt):
    """Call Identification Number  (M)

    This parameter is a unique number within the own exchange
    that identifies the Call Component.

    All Call Modules produced in the same Call Component
    have the same call identification number; that is,
    if partial output records are produced for the same
    Call Component, the same call identification number
    is used.
    """

    def __init__(self, octets: bytes):
        super().__init__(octets, 3)


class AddressString:
    def __call__(self, octets) -> str:
        pass


class RecordSequenceNumber(UnsignedInt):
    """Record Sequence Number  (M)

    This parameter contains a consecutive number for each
    Call Data Record generated and output.
    """

    def __init__(self, octets: bytes):
        super().__init__(octets, 3)


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

    def __init__(self, octets: bytes):
        super().__init__(octets, 1)


class IMSI:
    def __call__(self, octets) -> str:
        pass


class DisconnectingParty:
    def __call__(self, octets) -> str:
        pass


class Date:
    def __call__(self, octets) -> str:
        pass


class Time:
    def __call__(self, octets) -> str:
        pass


class ChargedParty:
    def __call__(self, octets) -> str:
        pass


class ChargingOrigin:
    def __call__(self, octets) -> str:
        pass


class TariffClass:
    def __call__(self, octets) -> str:
        pass


class TariffSwitchInd:
    def __call__(self, octets) -> str:
        pass


class NumberOfMeterPulses:
    def __call__(self, octets) -> str:
        pass


class ExchangeIdentity:
    def __call__(self, octets) -> str:
        pass


class Route:
    def __call__(self, octets) -> str:
        pass


class MiscellaneousInformation:
    def __call__(self, octets) -> str:
        pass


class INMarkingOfMS:
    def __call__(self, octets) -> str:
        pass


class CallPosition:
    def __call__(self, octets) -> str:
        pass


class EosInfo:
    def __call__(self, octets) -> str:
        pass


class InternalCauseAndLoc:
    def __call__(self, octets) -> str:
        pass


class RedirectionCounter:
    def __call__(self, octets) -> str:
        pass


class OutputForSubscriber:
    def __call__(self, octets) -> str:
        pass


class PartialOutputRecNum:
    def __call__(self, octets) -> str:
        pass


class FaultCode:
    def __call__(self, octets) -> str:
        pass


class SubscriptionType:
    def __call__(self, octets) -> str:
        pass


class SwitchIdentity:
    def __call__(self, octets) -> str:
        pass


class NetworkCallReference:
    def __call__(self, octets) -> str:
        pass


class CAMELTDPData:
    def __call__(self, octets) -> str:
        pass


class GSMCallReferenceNumber:
    def __call__(self, octets) -> str:
        pass


class C7ChargingMessage:
    def __call__(self, octets) -> str:
        pass


class C7CHTMessage:
    def __call__(self, octets) -> str:
        pass


class ChargingIndicator:
    def __call__(self, octets) -> str:
        pass


class TransitCarrierInfo:
    def __call__(self, octets) -> str:
        pass


class ChargeInformation:
    def __call__(self, octets) -> str:
        pass


class ChargeAreaCode:
    def __call__(self, octets) -> str:
        pass


class MobileUserClass1:
    def __call__(self, octets) -> str:
        pass


class MobileUserClass2:
    def __call__(self, octets) -> str:
        pass


class CarrierInfo:
    def __call__(self, octets) -> str:
        pass


class Counter:
    def __call__(self, octets) -> str:
        pass


class UserClass:
    def __call__(self, octets) -> str:
        pass


class OriginatingLineInformation:
    def __call__(self, octets) -> str:
        pass


class MultimediaInformation:
    def __call__(self, octets) -> str:
        pass


class OutputType:
    def __call__(self, octets) -> str:
        pass


class OriginatedCode:
    def __call__(self, octets) -> str:
        pass


class ReroutingIndicator:
    def __call__(self, octets) -> str:
        pass


if __name__ == "__main__":
    print(f"{TAC(b'\x00\x02\x01').value=}")

    print(f"{CallIDNumber(b'|;\xac').value=}")
