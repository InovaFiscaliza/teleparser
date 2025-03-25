from ..primitives import OctetString, TBCDString
from ..exceptions import OctetStringError
from teleparser.config import PRESTADORAS, Prestadora


class BSSMAPCauseCode(OctetString):
    """ASN.1 Formal Description
    BSSMAPCauseCode ::= OCTET STRING (SIZE(1..2))
    |    |    |    |    |    |    |    |    |
    | 8  | 7  | 6  | 5  | 4  | 3  | 2  | 1  |
    |    |    |    |    |    |    |    |    |
    /---------------------------------------/
    |ext |         cause value              | octet 1
    +---------------------------------------+
    |          extended cause value         | octet 2
    /---------------------------------------/
    The second octet is used only if the ext bit is
    set to one.
    The cause value is specified in the Function
    Specification "A-Interface, Section H:
    Base Station System Management Application Part,
    BSSMAP, Message Formats And Coding" in chapter
    "Information Elements".
    """

    def __init__(self, octets):
        super().__init__(octets, upper=2)
        self._parse_cause_value()

    def _parse_cause_value(self):
        """Parse cause value from octets 1 and 2"""
        self.cause_value = self.octets[0] & 0x7F
        if self.octets[0] >> 7 == 1:
            self.extended_cause_value = self.octets[1]

    @property
    def value(self):
        if self.size == 2:
            return {
                "cause_value": self.cause_value,
                "extended_cause_value": self.extended_cause_value,
            }
        return {"cause_value": self.cause_value}


class CarrierInfo(OctetString):
    """ASN.1 Formal Description
    CarrierInfo ::= OCTET STRING (SIZE(2..3))
    The digits for ID Code are encoded as a TBCD-STRING.
    |    |    |    |    |    |    |    |    |
    |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
    |    |    |    |    |    |    |    |    |
    /---------------------------------------/
    | 2nd ID Code digit | 1st ID Code digit | octet 1 of TBCD
    +-------------------+-------------------+
    | 4th ID Code digit | 3rd ID Code digit | octet 2 of TBCD
    +-------------------+-------------------+
    |Entry POI-Hierarchy| Exit POI-Hierarchy| octet 3 (Note 2)
    /---------------------------------------/
    Acceptable digits are between 0 and 9.
    Note 1: OLEC and TLEC information contains always Carrier
    identification code.
    Note 2: POI-Hierarchy information is optional.
    Exit/Entry POI Hierarchy
    0000  No Indication
    0001  Hierarchy level 1
    0010  Hierarchy level 2
    0011
    to    Spare
    1111
    """

    def __init__(self, octets):
        super().__init__(octets, lower=2, upper=3)
        self._parse_carrier_identification_code()
        self._parse_entry_poi_hierarchy()
        self._parse_exit_poi_hierarchy()

    VALUES = {
        0: "No Indication",
        1: "Hierarchy level 1",
        2: "Hierarchy level 2",
    }

    def _parse_carrier_identification_code(self):
        """Parse Carrier Identification Code from octets 2 and 3"""
        self.carrier_identification_code = TBCDString(self.digits[:2]).value

    def _parse_entry_poi_hierarchy(self):
        """Parse Entry POI Hierarchy from option octet 3"""
        entry_poi_hierarchy = None
        if self.size == 3:
            digit = self.digits[2] >> 4
            entry_poi_hierarchy = "Spare" if digit > 2 else self.VALUES[digit]
        self.entry_poi_hierarchy = entry_poi_hierarchy

    def _parse_exit_poi_hierarchy(self):
        """Parse Exit POI Hierarchy from optional octets 3"""
        exit_poi_hierarchy = None
        if self.size == 3:
            digit = self.digits[2] & 0x0F
            exit_poi_hierarchy = "Spare" if digit > 2 else self.VALUES[digit]
        self.exit_poi_hierarchy = exit_poi_hierarchy


class ChargingIndicator(OctetString):
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


class CUGInterlockCode(OctetString):
    """Closed User Group Interlock Code

      The Closed User Group (CUG) Interlock Code identifies
      a Closed User Group within the networks.

      In the originating Call Component, the CUG Interlock Code
      indicates that the subscriber has made a CUG call.

      In the terminating Call Component, the CUG Interlock Code
      indicates that the subscriber has received a CUG call from
      another member of the subscriber's closed user group.

      In the call-forwarding component, the CUG Interlock Code
      indicates that the subscriber has forwarded a CUG call.

      In the roaming call forwarding component, the CUG
      Interlock Code indicates that the calling subscriber has
      made a CUG call.

    ASN.1 Formal Description
        CUGInterlockCode ::= OCTET STRING (SIZE (4))
        |   |   |   |   |   |   |   |   |
        | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 |
        |   |   |   |   |   |   |   |   |
        /-------------------------------/
        |  2nd NI digit | 1st NI digit  |  octet 1
        +---------------+---------------+
        |  4th NI digit | 3rd NI digit  |  octet 2
        +-------------------------------+
        | MSB       binary code         |  octet 3
        +-------------------------------+
        |                            LSB|  octet 4
        /-------------------------------/
        The first digit of Network Indicator (NI) is 0 or 9,
        which means that the telephony Country Code follows in
        the 2nd to 4th NI digits.
    """

    def __init__(self, octets: bytes):
        super().__init__(octets, size=4)
        self._parse_network_indicator()

    def _parse_network_indicator(self):
        """Parse Network Indicator from octets 1 and 2"""
        self.network_indicator = TBCDString(self.octets[:2]).value
        self.code = int.from_bytes(self.octets[2:], byteorder="big")

    @property
    def value(self):
        return self.network_indicator, self.code

    def __str__(self):
        return f"NI: {self.network_indicator}, CODE:{self.code}"


class C7CHTMessage(OctetString):
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


class Date(OctetString):
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


class GlobalTitle(OctetString):
    """ASN.1 Formal Description
    GlobalTitle ::= OCTET STRING (SIZE(4..12))
    |    |    |    |    |    |    |    |    |
    | 8  | 7  | 6  | 5  | 4  | 3  | 2  | 1  |
    |    |    |    |    |    |    |    |    |
    /---------------------------------------/
    |  Translation Type                     | octet 1
    +---------------------------------------+
    | Numbering Plan    | ODD/EVEN Indicator| octet 2
    +---------------------------------------+
    | Nature of Address Indicator           | octet 3
    +---------------------------------------+
    |    2nd digit      |     1st digit     | octet 4
    /---------------------------------------/
    .
    .
    .
    /---------------------------------------/
    |    18th digit     |     17th digit    | octet 12
    /---------------------------------------/
    Octet 2:  Bits 4-1 Odd/Even Indicator:
    0 0 0 1  BCD, odd number of digits
    0 0 1 0  BCD, even number of digits
    Bits 8-5 Numbering plan:
    0 0 0 1  ISDN numbering plan (E.164)
    0 0 1 1  Data numbering plan (X.121)
    0 1 0 0  Telex numbering plan (F.69)
    0 1 0 1  Maritime mobile numbering plan
    0 1 1 0  Land mobile numbering plan
    0 1 1 1  ISDN mobile numbering plan
    Octet 3:  Bits 7-1 Nature of address indicator:
    0 0 0 0 0 0 1  Subscriber number
    0 0 0 0 0 1 0  Unknown
    0 0 0 0 0 1 1  National significant number
    0 0 0 0 1 0 0  International number
    Bit 8  Spare
    Octets 4..12: Address signals, BCD coded
    Digits value range: H'0-H'9,
    H'B (code 11)
    and H'C (code 12)
    Note: Filler H'0 (last digit) is used in case
    of odd number of digits.
    """

    NUMBERING_PLAN = {
        1: "ISDN numbering plan (E.164)",
        3: "Data numbering plan (X.121)",
        4: "Telex numbering plan (F.69)",
        5: "Maritime mobile numbering plan",
        6: "Land mobile numbering plan",
        7: "ISDN mobile numbering plan",
    }
    NATURE_OF_ADDRESS = {
        1: "Subscriber number",
        2: "Unknown",
        3: "National significant number",
        4: "International number",
    }

    def __init__(self, octets):
        super().__init__(octets, lower=4, upper=12)
        self._parse_translation_type()
        self._parse_numbering_plan()
        self._parse_numbering_indicator()
        self._parse_nature_of_address_indicator()
        self._parse_digits()

    def _parse_translation_type(self):
        """Parse Translation Type from octets 1"""
        self.translation_type = self.octets[0]

    def _parse_numbering_plan(self):
        """Parse Numbering Plan from octets 1 bits 5-5"""
        self.numbering_plan = self.NUMBERING_PLAN[self.octets[1] >> 4]

    def _parse_numbering_indicator(self):
        """Parse Nature of Address Indicator from octets 1 bits 4-1"""
        if self.octets[1] & 1 == 1:
            self.odd = True
        elif self.octets[1] & 2 == 2:
            self.odd = False
        else:
            raise ValueError("Invalid value for ODD/EVEN Indicator")

    def _parse_nature_of_address_indicator(self):
        """Parse Nature of Address Indicator from octets 2 bits 7-1"""
        self.nature_of_address = self.NATURE_OF_ADDRESS[self.octets[2] & 7]

    def _parse_digits(self):
        """Parse digits from octets 4..12"""
        digits = []
        for octet in self.octets[3:]:
            # Extract two digits from each octet
            digit1 = octet & 0x0F
            digit2 = (octet >> 4) & 0x0F
            digits.extend([digit1, digit2])
        if digits and self.odd:  # Discard Filler
            digits.pop()
        self.digits = digits

    @property
    def value(self):
        return {
            "translation_type": self.translation_type,
            "numbering_plan": self.numbering_plan,
            "nature_of_address": self.nature_of_address,
            "digits": "".join(str(d) for d in self.digits),
        }


class GlobalTitleAndSubSystemNumber(GlobalTitle):
    """ASN.1 Formal Description
    GlobalTitleAndSubSystemNumber ::=
    OCTET STRING (SIZE(5..13))
    |    |    |    |    |    |    |    |    |
    |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
    |    |    |    |    |    |    |    |    |
    /---------------------------------------/
    |  SubSystemNumber                      | octet 1
    +---------------------------------------+
    |  Translation Type                     | octet 2
    +---------------------------------------+
    | Numbering Plan    | ODD/EVEN Indicator| octet 3
    +---------------------------------------+
    | Nature of Address Indicator           | octet 4
    +---------------------------------------+
    |    2nd digit      |     1st digit     | octet 5
    /---------------------------------------/
    .
    .
    .
    /---------------------------------------/
    |    18th digit     |     17th digit    | octet 13
    /---------------------------------------/
    Octet 3:  Bits 4-1 Odd/Even Indicator:
    0 0 0 1  BCD, odd number of digits
    0 0 1 0  BCD, even number of digits
    Bits 8-5 Numbering plan:
    0 0 0 1  ISDN numbering plan (E.164)
    0 0 1 1  Data numbering plan (X.121)
    0 1 0 0  Telex numbering plan (F.69)
    0 1 0 1  Maritime mobile numbering plan
    0 1 1 0  Land mobile numbering plan
    0 1 1 1  ISDN mobile numbering plan
    Octet 4:  Bits 7-1 Nature of address indicator:
    0 0 0 0 0 0 1  Subscriber number
    0 0 0 0 0 1 0  Unknown
    0 0 0 0 0 1 1  National significant number
    0 0 0 0 1 0 0  International number
    Bit 8  Spare
    Octets 5..13: Address signals, BCD coded
    Digits value range: H'0-H'9,
    H'B (code 11)
    and H'C (code 12)
    Note: Filler H'0 (last digit) is used in case
    of odd number of digits.
    """

    def __init__(self, octets: bytes):
        super().__init__(octets[1:])
        self.subsystem_number = octets[0]

    @property
    def value(self):
        return {
            "subsystem_number": self.subsystem_number,
            "translation_type": self.translation_type,
            "numbering_plan": self.numbering_plan,
            "nature_of_address": self.nature_of_address,
            "digits": "".join(str(d) for d in self.digits),
        }


class IMEI(OctetString):
    """Calling Subscriber IMEI

      This parameter contains the calling-subscriber
      International Mobile Station Equipment Identity (IMEI).

      The parameter is output, if the exchange data is
      set so that IMEI is fetched from user equipment at call
      setup.

      In case of a network-initiated USSD service, this
      parameter contains the IMEI for the served subscriber
      in Subscriber Service Procedure Call Module.

      In case of ineffective call the parameter is not
      available for mobile originating Call Component.

    ASN.1 Formal Description
        IMEI ::= TBCDString (SIZE(8))
        |    |    |    |    |    |    |    |    |
        |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
        |    |    |    |    |    |    |    |    |
        /---------------------------------------/
        |  TAC digit 2      |  TAC digit 1      | octet 1
        +-------------------+-------------------+
        |  TAC digit 4      |  TAC digit 3      | octet 2
        +-------------------+-------------------+
        |  TAC digit 6      |  TAC digit 5      | octet 3
        +-------------------+-------------------+
        |  TAC digit 8      |  TAC digit 7      | octet 4
        +-------------------+-------------------+
        |  SNR digit 2      |  SNR digit 1      | octet 5
        +-------------------+-------------------+
        |  SNR digit 4      |  SNR digit 3      | octet 6
        +-------------------+-------------------+
        |  SNR digit 6      |  SNR digit 5      | octet 7
        +-------------------+-------------------+
        |  See note         |  See note         | octet 8
        /---------------------------------------/
        TAC Type Allocation Code (octet 1, 2, 3 and 4).
        SNR Serial Number (octet 5, 6 and 7).
        Digits 0 to 9, two digits per octet,
        each digit encoded 0000 to 1001
        Note:
        Bits 1-4 of octet 8: Spare
        Bits 5-8 of octet 8: 1111 used as a filler.
    """

    def __init__(self, octets):
        super().__init__(octets, size=8)
        self._parse_tac_snr()

    def _parse_tac_snr(self):
        self.tac = TBCDString(self.octets[:4]).value
        self.snr = TBCDString(self.octets[4:]).value
        self.spare = self.octets[7] & 0x0F

    @property
    def value(self):
        return self.tac, self.snr, self.spare

    def __str__(self):
        return f"TAC: {self.tac}, SNR: {self.snr}, Spare: {self.spare}"


class LocationInformation(OctetString):
    """ASN.1 Formal Description
    LocationInformation ::= OCTET STRING (SIZE(7))
    |   |   |   |   |   |   |   |   |
    | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 |
    |   |   |   |   |   |   |   |   |
    /-------------------------------/
    |  MCC digit 2  |  MCC digit 1  | octet 1
    +---------------+---------------+
    |  MNC digit 3  |  MCC digit 3  | octet 2
    +---------------+---------------+
    |  MNC digit 2  |  MNC digit 1  | octet 3
    +-------------------------------+
    | MSB          LAC              | octet 4
    +-------------------------------+
    |              LAC, cont.   LSB | octet 5
    +-------------------------------+
    | MSB   CI/SAC value            | octet 6
    +-------------------------------+
    |       CI/SAC value, cont. LSB | octet 7
    /-------------------------------/
    MCC, Mobile country code (octet 1 and octet 2)
    MNC, Mobile network code (octet 2 and octet 3).
    Note: If MNC uses only 2 digits, then 3rd
    is coded with filler H'F.
    LAC Location area code (octet 4 and 5)
    CI  Cell Identity, value (octets 6 and 7) (GSM)
    SAC Service Area Code, value (octets 6 and 7) (WCDMA)
    In the CI/SAC value field bit 8 of octet 6 is the most
    significant bit.  Bit 1 of octet 7 is the least
    significant bit.  Coding using full hexadecimal
    representation is used.
    In the LAC field, bit 8 of octet 4 is the most
    significant bit.Bit 1 of octet 5 is the least
    significant bit.Coding using full hexadecimal
    representation is used.
    In the case of a deleted or non-existent Location
    Area Identity (LAI), both octets of the location
    area code are coded with zeros.
    """

    def __init__(self, octets: bytes):
        super().__init__(octets, size=7)
        self._parse_mcc_mnc()
        self._parse_lac()
        self._parse_ci_sac()

    def _parse_mcc_mnc(self):
        mcc1 = self.octets[0] & 0x0F  # MCC digit 1
        mcc2 = self.octets[0] >> 4  # MCC digit 2
        mcc3 = self.octets[1] & 0x0F  # MCC digit 3
        self.mcc = mcc1 * 100 + mcc2 * 10 + mcc3
        mnc1 = self.octets[2] & 0x0F  # MNC digit 1
        mnc2 = self.octets[2] >> 4  # MNC digit 2
        if (mnc3 := self.octets[1] >> 4) == 15:  # MNC digit 3
            mnc = mnc1 * 10 + mnc2
        else:
            mnc = mnc1 * 100 + mnc2 * 10 + mnc3
        self.carrier = PRESTADORAS.get(mnc, Prestadora(mnc=mnc, mcc=self.mcc))

    def _parse_lac(self):
        self.lac = int.from_bytes(self.octets[3:5], "big")

    def _parse_ci_sac(self):
        ci_sac = int.from_bytes(self.octets[5:], "big")
        self.ci_sac = ci_sac

    @property
    def value(self):
        return self.carrier._asdict() | {"lac": self.lac, "ci_sac": self.ci_sac}

    def __str__(self):
        return f"{self.carrier.name} (MCC: {self.carrier.mcc}, MNC: {self.carrier.mnc}) LAC: {self.lac}, CI/SAC: {self.ci_sac}"


class PointCodeAndSubSystemNumber(OctetString):
    """ASN.1 Formal Description
    PointCodeAndSubSystemNumber ::= OCTET STRING (SIZE (4))
    |    |    |    |    |    |    |    |    |
    |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
    |    |    |    |    |    |    |    |    |
    /---------------------------------------/
    |  1st SPC                              | octet 1
    +---------------------------------------+
    |  2nd SPC                              | octet 2
    +---------------------------------------+
    |  3rd SPC                              | octet 3
    +---------------------------------------+
    |  SubSystemNumber                      | octet 4
    /---------------------------------------/
    - octets 1..3: SPC
    -              CCITT TCAP:
    The 2 most significant bits
    of the 2nd octet, and the 3rd octet
    are coded 0.
    -              ANSI TCAP
    All three octets used for SPC
    -              JAPANESE BLUE TCAP
    First two octets used for SPC. 3rd octet
    coded 0.
    - octet 4    : SubSystemNumber
    """

    def __init__(self, octets: bytes):
        super().__init__(octets, size=4)
        self._parse_spc()

    def _parse_spc(self):
        """Parse SPC from octets 1 and 2"""
        if self.octets[1] >> 6 == 0 and self.octets[2] == 0:
            self.spc_type = "CCITT TCAP"
        elif self.octets[2] == 0:
            self.spc_type = "JAPANESE BLUE TCAP"
        else:
            self.spc_type = "ANSI TCAP"
        self.spc = int.from_bytes(self.octets[:3], "big")
        self.subsystem_number = self.octets[3]

    @property
    def value(self):
        return {
            "spc_type": self.spc_type,
            "spc": self.spc,
            "subsystem_number": self.subsystem_number,
        }


class PositionAccuracy(OctetString):
    """Position Accuracy

      This parameter contains data related to global
      satellite systems call. When user terminal is providing
      user terminal position it also includes the position
      accuracy.

      The parameter is not applicable for WCDMA Japan.

    ASN.1 Formal Description
        PositionAccuracy ::= OCTET STRING (SIZE(2))
        |    |    |    |    |    |    |    |    |
        |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
        |    |    |    |    |    |    |    |    |
        /---------------------------------------/
        | Es |    Error area definition         | octet 1
        +---------------------------------------+
        |     Error area definition, continued  | octet 2
        /---------------------------------------/
        Es (octet 1 bit 8):
        Value    Meaning
        -----    -------
        0        Shape of defined error area, rectangular
        1        Shape of defined error area, circular
        When Es=0
        Error area definition (octet 1, bits 7-1):
        Angle: Value range 0-127
        The angle defines the orientation of
        the error region with respect to User
        Terminal's (UT's) longitude. The range
        is 0-180 degrees with a 1.4 degree
        resolution.
        For example, value 2 = 2.8 degrees.
        Error area definition, continued (octet 2):
        Bits 8-6: Error region half width
        Bits 5-1: Error region half length
        Error region half width:  Value range 0-7
        Error region half length: Value range 0-31
        The error region length and error region width
        are presented in kilometers.
        When Es=1
        Octets 1 bits 7-1 are coded as zero.
        Error area definition, continued (octet 2):
        Error region radius: Value range 0-255
        The error region radius is presented in
        kilometers.
    """

    def __init__(self, octets):
        super().__init__(octets, size=2)
        self._parse_error_area_definition()

    def _parse_error_shape(self):
        """Parse Error Area Definition from octets 1, bit 8"""
        if self.octets[0] >> 7 == 1:
            self.error_shape == "circular"
            self._parse_area_circular()
        else:
            self.error_shape == "rectangular"
            self._parse_angle_rectangular()

    def _parse_area_rectangular(self):
        """Parse Angle from octets 1, bits 7-1"""
        self.angle = (self.octets[0] & 0x7F) * 1.4
        self.half_width = self.octets[1] >> 6
        self.half_length = self.octets[1] & 0x3F
        self.area = (self.half_width * self.half_length) * 2

    def _parse_area_circular(self):
        """Parse Radius from octets 1, bits 7-1"""
        from math import pi

        self.angle = (self.octets[0] & 0x7F) * 1.4
        self.radius = self.octets[1]
        self.area = self.radius * self.radius * pi

    @property
    def value(self):
        return {"error_shape": self.error_shape, "angle": self.angle, "area": self.area}

    def __str__(self):
        return (
            f"Error Shape: {self.error_shape}, Angle: {self.angle}, Area: {self.area}"
        )


class PresentationAndScreeningIndicator(OctetString):
    """Presentation and Screening Indicator

      This parameter indicates if the calling line identity
      can be shown to the called subscriber and whether the
      calling line identity was provided by the subscriber or
      by the network.

      The field is not output when the Calling Party Number
      is unavailable.
    ASN.1 Formal Description
        PresentationAndScreeningIndicator ::= OCTET STRING (SIZE(1))
        |    |    |    |    |    |    |    |    |
        |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
        |    |    |    |    |    |    |    |    |
        /---------------------------------------/
        | MSB                              LSB  |
        /---------------------------------------/
        - Bits 8-5:   Screening indicator
        0000   Screen indicator not valid
        0001   User provided, verified, and passed
        0011   Network provided
        - Bits 4-1:   Presentation indicator
        0000   Presentation allowed
        0001   Presentation restricted
    """

    def __init__(self, octets: bytes):
        super().__init__(octets, size=1)
        self.screening = {
            0: "Screen indicator not valid",
            1: "User provided, verified, and passed",
            3: "Network provided",
        }
        self.presentation = {0: "Presentation allowed", 1: "Presentation restricted"}
        self._parse_screening_indicator()
        self._parse_presentation_indicator()

    def _parse_presentation_indicator(self):
        """Parse Presentation Indicator from octets 1 bits 4-1"""
        self.presentation_indicator = self.presentation[self.octets[0] & 1]

    def _parse_screening_indicator(self):
        """Parse Screening Indicator from octets 1 bits 8-5"""
        self.screening_indicator = self.screening[(self.octets[0] >> 4) & 3]

    @property
    def value(self):
        return {
            "screening": self.screening_indicator,
            "presentation": self.presentation_indicator,
        }


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
        super().__init__(octets, lower=3, upper=4)
        try:
            self.string = octets.hex().upper()
        except AttributeError as e:
            raise OctetStringError("Error parsing octet") from e

    @property
    def value(self) -> str:
        # Extract individual octets
        tsc = self.string[:2]  # Telecom Service Code
        tos = self.string[2:4]  # Type of Seizure
        toi = self.string[4:6]  # Type of Indicator

        # Handle optional TOP octet
        top = self.string[6:8] if len(self.string) == 8 else ""

        return {"tsc": tsc, "tos": tos, "toi": toi, "top": top}

    def __str__(self):
        # Build result string
        return f"{self.value}"
