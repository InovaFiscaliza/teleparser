from .decorators import fixed_size_unsigned_int, UnsignedInt
from .datatypes import primitives


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


@fixed_size_unsigned_int(3)
class RecordSequenceNumber(UnsignedInt):
    """Record Sequence Number  (M)

    This parameter contains a consecutive number for each
    Call Data Record generated and output.
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


if __name__ == "__main__":
    print(f"{TAC(b'\x00\x02\x01').value=}")

    print(f"{CallIDNumber(b'|;\xac').value=}")
