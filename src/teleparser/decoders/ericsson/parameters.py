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


if __name__ == "__main__":
    print(f"{TAC(b'\x00\x02\x01').value=}")

    print(f"{CallIDNumber(b'|;\xac').value=}")
