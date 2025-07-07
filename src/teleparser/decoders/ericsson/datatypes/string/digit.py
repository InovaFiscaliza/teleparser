from ..primitives import DigitString, fixed_size_digit_string


@fixed_size_digit_string(2)
class ApplicationIdentifier(DigitString):
    """ASN.1 Formal Description
    ApplicationIdentifier ::= OCTET STRING (SIZE(2))
    |    |    |    |    |    |    |    |    |
    |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
    |    |    |    |    |    |    |    |    |
    /---------------------------------------/
    | MSB                                   |  octet 1
    +---------------------------------------+
    |                                    LSB|  octet 2
    /---------------------------------------/
    Note: OCTET STRING is coded as an unsigned integer.
    Value range: H'0 - H'1FF
    The meaning of each value is specified in Application
    Information document "Mobile Telephony Data".
    """


@fixed_size_digit_string(3)
class ChargeAreaCode(DigitString):
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.digits = self._digits()

    def _digits(self):
        digits = [int.from_bytes(byte, byteorder="big") for byte in self.octets]
        assert all(0 <= digit <= 9 for digit in digits), (
            " Acceptable digits are between 0 and 9."
        )
        return digits


@fixed_size_digit_string(2)
class ChargingCase(DigitString):
    """Charging Case  (M)

      This parameter contains the charging case which is
      defined for the call and is used in charging analysis
      for this call.

    ASN.1 Formal Description
        ChargingCase ::= OCTET STRING (SIZE(2))
        |    |    |    |    |    |    |    |    |
        |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
        |    |    |    |    |    |    |    |    |
        /---------------------------------------/
        | MSB                                   |  octet 1
        +---------------------------------------+
        |                                    LSB|  octet 2
        /---------------------------------------/
        Note: The OCTET STRING is coded as an unsigned integer.
        Values vary according to operator's definition.
        Value range: H'0 - H'0FFF or value H'FFFF
    """


class FreeFormatData(DigitString):
    """Free Format Data

    This parameter is CAMEL specific information parameter. It
    indicates free-format billing or charging, or both
    characteristics.

    Free Format Data originates from gsmSCF in
    FurnishChargingInformation (FCI) or
    FurnishChargingInformationShortMessageService (FCI-SMS)
    operation. In the case of subsequent FCI operations for
    the same call party, the total or last data is output
    according to operations parameters.

    ASN.1 Formal Description
      FreeFormatData ::= OCTET STRING (SIZE(1..160))
      |    |    |    |    |    |    |    |    |
      |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
      |    |    |    |    |    |    |    |    |
      /---------------------------------------/
      |MSB                                    |  octet 1
      +---------------------------------------+
      |                                       |  octet 2
      /---------------------------------------/
      .
      .
      .
      /---------------------------------------/
      |                                    LSB|  octet 160
      /---------------------------------------/
    """

    def __init__(self, octets: bytes):
        super().__init__(octets, upper=160)


class GSMCallReferenceNumber(DigitString):
    """GSM Call Reference Number

    This parameter is CAMEL specific information parameter.
    It applies to CAMEL calls and extended CAMEL calls with
    IN Capability. It correlates Call Data Records output
    from the GMSC/gsmSSF and the terminating MSC, or call
    data records from the originating MSC/gsmSSF and a network
    optional Call Data Record from the gsmSCF."""

    def __init__(self, octets: bytes):
        super().__init__(octets, lower=1, upper=8)


@fixed_size_digit_string(2)
class INServiceTrigger(DigitString):
    """ASN.1 Formal Description
    INServiceTrigger ::= OCTET STRING (SIZE (2))
    |    |    |    |    |    |    |    |    |
    |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
    |    |    |    |    |    |    |    |    |
    /---------------------------------------/
    | MSB                                   | octet 1
    +---------------------------------------+
    |                                   LSB | octet 2
    /---------------------------------------/
    The meaning of the value can be specified by the operator.
    Note: OCTET STRING is coded as an unsigned integer.
    Value range: H'0 - H'FFFF
    """


@fixed_size_digit_string(2)
class InternalCauseAndLoc(DigitString):
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

    __slots__ = ("octets", "size", "digits", "value", "location", "cause")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.value = self._value()

    def _value(self):
        self.location = self.digits[0]
        self.cause = self.digits[1]
        return {"location": self.location, "cause": self.cause}

    def __str__(self):
        return f"Location: {self.location}, Cause: {self.cause}"


@fixed_size_digit_string(1)
class LegID(DigitString):
    """ASN.1 Formal Description
    LegID ::= OCTET STRING (SIZE(1))
    |    |    |    |    |    |    |    |    |
    |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
    |    |    |    |    |    |    |    |    |
    /---------------------------------------/
    | MSB                               LSB |
    /---------------------------------------/
    Note: OCTET STRING is coded as an unsigned integer.
    """


@fixed_size_digit_string(1)
class MiscellaneousInformation(DigitString):
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


@fixed_size_digit_string(5)
class NetworkCallReference(DigitString):
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

    __slots__ = (
        "octets",
        "size",
        "digits",
        "value",
        "sequence_number",
        "switch_identity",
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.value = self._value()

    def _value(self):
        self.sequence_number = int.from_bytes(self.octets[:3], "big")
        self.switch_identity = int.from_bytes(self.octets[3:], "big")
        return {
            "sequenceNumber": self.sequence_number,
            "switchIdentity": self.switch_identity,
        }

    def __str__(self):
        return f"{self.sequence_number:06d}-{self.switch_identity:04d}"


@fixed_size_digit_string(3)
class NumberOfMeterPulses(DigitString):
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


@fixed_size_digit_string(1)
class NumberOfOperations(DigitString):
    """ASN.1 Formal Description
    NumberOfOperations ::= OCTET STRING (SIZE(1))
    |    |    |    |    |    |    |    |    |
    |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
    |    |    |    |    |    |    |    |    |
    /---------------------------------------/
    | MSB                               LSB |
    /---------------------------------------/
    Note: OCTET STRING is coded as an unsigned integer.
    Value range: H'0 - H'FF
    """


@fixed_size_digit_string(2)
class NumberOfShortMessage(DigitString):
    """ASN.1 Formal Description
    NumberOfShortMessage ::= OCTET STRING (SIZE(2))
    |    |    |    |    |    |    |    |    |
    |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
    |    |    |    |    |    |    |    |    |
    /---------------------------------------/
    | MSB                                   | octet 1
    +---------------------------------------+
    |                                   LSB | octet 2
    /---------------------------------------/
    Note: OCTET STRING is coded as an unsigned integer.
    Value range: H'0 - H'FFFF
    """


@fixed_size_digit_string(1)
class RANAPCauseCode(DigitString):
    """Radio Access Network Application Part Cause Code

      This parameter is used to indicate the reason why
      a particular Radio Access Network Application Part event
      occured.

      This parameter is available if a call disconnection is
      initiated by the RANAP.

      The parameter is only applicable for WCDMA.
    ASN.1 Formal Description
        RANAPCauseCode ::= OCTET STRING (SIZE(1))
        |    |    |    |    |    |    |    |    |
        |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
        |    |    |    |    |    |    |    |    |
        /---------------------------------------/
        | MSB                              LSB  | octet 1
        /---------------------------------------/
        The cause value is specified in the Function
        Specification (FS) "IU-Interface, Section H:
        Radio Access Network Application Part,
        RANAP, Message Formats And Coding" in chapter
        "Information Elements".
    """


@fixed_size_digit_string(4)
class ServiceKey(DigitString):
    r"""ASN.1 Formal Description

    ServiceKey ::=  OCTET STRING (SIZE(4))

    |    |    |    |    |    |    |    |    | 
    |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 | 
    |    |    |    |    |    |    |    |    | 
    /---------------------------------------\ 
    | MSB                                   | octet 1 
    +---------------------------------------+ 
    |                                       | octet 2 
    +---------------------------------------+ 
    |                                       | octet 3 
    +---------------------------------------+ 
    |                                 LSB   | octet 4 
    \---------------------------------------/ 
    """


class SpeechCoderPreferenceList(DigitString):
    """Speech Coder Preference List

    This parameter contains speech coder versions received
    from the UE, listed from most to least preferred.

    The SpeechCoderPreferenceList that is sent to charging is
    actually the selected Speech Coder Preference list which
    is the result from the Telecommunication Service Analysis.
    With this it is possible to charge for what the subscriber
    will get after the operator's preferences have been taken
    into account. This gives the operator full control of the
    use of certain speech coders for certain call cases.

    The parameter is only applicable for GSM.

    ASN.1 Formal Description
      SpeechCoderPreferenceList ::= OCTET STRING (SIZE (1..6))
      |    |    |    |    |    |    |    |    |
      |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
      |    |    |    |    |    |    |    |    |
      /---------------------------------------/
      |  1st preference                       | octet 1
      +---------------------------------------+
      |  2nd preference                       | octet 2
      /---------------------------------------/
      .
      .
      .
      /---------------------------------------/
      |  6th preference                       | octet 6
      /---------------------------------------/
      Value range for all octets: 0 - 5, encoded as
      enumerated SpeechCoderVersion value.
    """

    def __init__(self, octets: bytes):
        super().__init__(octets, upper=6)
        self.digits = self._parse_digits()

    def _parse_digits(self):
        """Returns the n digits as a string"""
        digits = list(self.octets)
        assert all(0 <= digit <= 6 for digit in digits), (
            f"Speech Coder Preference List should be in range 0-6: {digits}"
        )
        return digits


@fixed_size_digit_string(2)
class SSFChargingCase(DigitString):
    """ASN.1 Formal Description
    SSFChargingCase ::= OCTET STRING (SIZE(2))
    |    |    |    |    |    |    |    |    |
    |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
    |    |    |    |    |    |    |    |    |
    /---------------------------------------/
    | MSB                                   | octet 1
    +---------------------------------------+
    |                                  LSB  | octet 2
    /---------------------------------------/
    The meaning of the value can be specified by the operator.
    Note: OCTET STRING is coded as an unsigned integer.
    Value range: H'0 - H'FFFF
    """


@fixed_size_digit_string(2)
class TariffClass(DigitString):
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


class Time(DigitString):
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

    __slots__ = (
        "octets",
        "size",
        "digits",
        "value",
        "hour",
        "minute",
        "second",
        "tenth_of_a_second",
    )

    def __init__(self, octets: bytes):
        super().__init__(octets, lower=3, upper=4)
        self._parse_digits()
        self.value = self._value()

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

    def _value(self):
        """Return datetime string"""
        value = f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}"
        if self.size == 4:
            value += f".{self.tenth_of_a_second:01d}"
        return value


@fixed_size_digit_string(2)
class TransferDelay(DigitString):
    """Transfer Delay

    This parameter indicates the maximum delay for 95 percent
    of the distribution of delay for all delivered Service Data
    Units (SDUs) during the lifetime of a Radio Access Bearer
    (RAB), where delay for an SDU is defined as the time from a
    request to transfer an SDU from a Service Access Point
    (SAP) to another. The unit is millisecond.

     The parameter is only applicable for WCDMA.

    ASN.1 Formal Description
       TransferDelay ::= OCTET STRING (SIZE(2))
       |    |    |    |    |    |    |    |    |
       |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
       |    |    |    |    |    |    |    |    |
       /---------------------------------------/
       | MSB                                   |  octet 1
       +---------------------------------------+
       |                                   LSB |  octet 2
       /---------------------------------------/
       Note : The OCTET STRING is coded as an unsigned INTEGER.
       Value range: H'0 - H'FFFF
    """
