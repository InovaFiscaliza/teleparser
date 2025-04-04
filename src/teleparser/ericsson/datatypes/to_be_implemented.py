from teleparser.ericsson.datatypes import primitives


class AddressStringExtended(primitives.AddressString):
    """ASN.1 Formal Description
    AddressStringExtended ::= OCTET STRING (SIZE(1..20))
    TBCD representation
    |    |    |    |    |    |    |    |    |
    |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
    |    |    |    |    |    |    |    |    |
    /---------------------------------------/
    |        TON        |        NPI        |
    +-------------------+-------------------+
    |     2nd digit     |     1st digit     | octet 1 of TBCD
    +-------------------+-------------------+
    |     4th digit     |     3rd digit     | octet 2 of TBCD
    +-------------------+-------------------+
    |     6th digit     |     5th digit     | octet 3 of TBCD
    /---------------------------------------/
    .
    .
    .
    /---------------------------------------/
    |    (2n)th digit   | (2n - 1)th digit  | octet n of TBCD
    /---------------------------------------/
    Character representation
    |    |    |    |    |    |    |    |    |
    |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
    |    |    |    |    |    |    |    |    |
    /---------------------------------------/
    |       TON         |        NPI        |
    +---------------------------------------+
    |               1st character           | octet 1 of char
    +---------------------------------------+
    |               2nd character           | octet 2 of char
    +---------------------------------------+
    |               3rd character           | octet 3 of char
    /---------------------------------------/
    .
    .
    .
    /---------------------------------------/
    |               Nth character           | octet N of char
    /---------------------------------------/
    Note: The OCTET STRING is coded as an unsigned INTEGER.
    The first octet uses 4 bits for Type Of Number (TON)
    and 4 bits for Numbering Plan Indicator (NPI):
    - Bit 8-5: Type of number
    - Bit 4-1: Numbering plan indicator
    Note: The values and their meanings for TON and NPI are
    described in the Application Information "Type Of
    Number and Numbering Plan Indicator".
    Subsequent octets representing address digits or characters
    are encoded as TBCD string or as GSM 7-bit default alphabet
    character depending on the NPI value.
    """


class AgeOfLocationEstimate(primitives.AddressString):
    """ASN.1 Formal Description
    AgeOfLocationEstimate ::= OCTET STRING (SIZE(2))
    |    |    |    |    |    |    |    |    |
    |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
    |    |    |    |    |    |    |    |    |
    /---------------------------------------/
    | MSB                                   |  octet 1
    +---------------------------------------+
    |                                    LSB|  octet 2
    /---------------------------------------/
    Value range: H'0 - H'7FFF (0-32767)
    The value represents the elapsed time in minutes since
    the last network contact of the mobile station (i.e.
    the actuality of the location information).
    value 0       UE is currently in contact with the
    network
    value 32767   Location information is at least
    32767 minutes (~22 days) old
    """


class AoCCurrencyAmountSent(primitives.AddressString):
    """ASN.1 Formal Description
    AoCCurrencyAmountSent ::= OCTET STRING (SIZE(4))
    |    |    |    |    |    |    |    |    |
    |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
    |    |    |    |    |    |    |    |    |
    /---------------------------------------/
    |         AoC Information Sent          |  octet 1
    +---------------------------------------+
    |MSB      Currency Amount               |  octet 2
    +---------------------------------------+
    |         Currency Amount               |  octet 3
    +---------------------------------------+
    |         Currency Amount            LSB|  octet 4
    /---------------------------------------/
    Note: OCTET STRING is coded as an unsigned integer.
    Value range of AoC Information Sent: H'0 - H'FF
    AoC Information Sent.
    Value      Meaning
    -----      -------
    00         Amount of Currency was sent to User
    01         Amount of Currency was not available
    02-FF      Spare
    Value range of Currency Amount: H'0 - H'FFFFFF
    """


class BitRate(primitives.AddressString):
    """ASN.1 Formal Description
    BitRate ::= OCTET STRING (SIZE(1))
    |    |    |    |    |    |    |    |    |
    |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
    |    |    |    |    |    |    |    |    |
    /---------------------------------------/
    | MSB                                LSB|  octet 1
    /---------------------------------------/
    BitRate                      Bits 8 7 6 5 4 3 2 1
    4.75 kbps                        0 0 0 0 0 0 0 1
    5.15 kbps                        0 0 0 0 0 0 1 0
    5.9  kbps                        0 0 0 0 0 0 1 1
    6.7  kbps                        0 0 0 0 0 1 0 0
    7.4  kbps                        0 0 0 0 0 1 0 1
    7.95 kbps                        0 0 0 0 0 1 1 0
    10.2  kbps                        0 0 0 0 0 1 1 1
    12.2  kbps                        0 0 0 0 1 0 0 0
    14.4  kbps                        0 0 0 0 1 0 0 1
    64.0  kbps                        0 0 0 0 1 0 1 0
    28.8  kbps                        0 0 0 0 1 0 1 1
    57.6  kbps                        0 0 0 0 1 1 0 0
    """


class CAMELTDPData:
    """ASN.1 Formal Description
    CAMELTDPData ::= SEQUENCE(
    serviceKey     (0) IMPLICIT  ServiceKey,
    gsmSCFAddress  (1) IMPLICIT  AddressString (SIZE (1..9)))
    """


class CarrierInformation(primitives.AddressString):
    """ASN.1 Formal Description
    CarrierInformation ::= OCTET STRING (SIZE(1))
    |   |   |   |   |   |   |   |   |
    | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 |
    |   |   |   |   |   |   |   |   |
    /-------------------------------/
    |   |   TNI     |     NIP       |  Octet 1
    /-------------------------------/
    Note: The OCTET STRING is coded as an unsigned INTEGER.
    - Bit 8: Spare
    - Bit 7-5: Type Of Network Identification (TNI)
    where
    010  national network
    - Bit 4-1: Network Identification Plan (NIP)
    where
    0000  unknown
    0001  3-digit carrier
    0010  4-digit carrier
    """


class CarrierSelectionSubstitutionInformation(primitives.AddressString):
    """ASN.1 Formal Description
    CarrierSelectionSubstitutionInformation ::= OCTET STRING
    (SIZE(1))
    |   |   |   |   |   |   |   |   |
    | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 |
    |   |   |   |   |   |   |   |   |
    /-------------------------------/
    |MSB                         LSB|  Octet 1
    /-------------------------------/
    Note: The OCTET STRING is coded as an unsigned INTEGER.
    CarrierSelectionSubstitionInformation
    Bits  8 7 6 5 4 3 2 1
    Presubscribed carrier exists,       0 0 0 0 0 0 0 1
    and carrier is not input by
    calling party. Presubscribed
    carrier is used.
    Presubscribed carrier is same as    0 0 0 0 0 0 1 0
    carrier input by calling party.
    Input carrier is used.
    Presubscribed carrier exists,       0 0 0 0 0 0 1 1
    and input by calling party is
    undetermined. Presubscribed
    carrier is used.
    Carrier is input by calling party,  0 0 0 0 0 1 0 0
    and it is not the presubscribed
    carrier for the calling party.
    Input carrier is used.
    Carrier given by Carrier Analysis   0 0 0 0 0 1 0 1
    is used instead of presubscribed
    carrier.
    Carrier given by Carrier Analysis   0 0 0 0 0 1 1 0
    is used instead of carrier input
    by calling party.
    Default carrier is used.            0 0 0 0 0 1 1 1
    """


class CauseCode(primitives.AddressString):
    """ASN.1 Formal Description
    CauseCode ::= OCTET STRING (SIZE(1))
    |    |    |    |    |    |    |    |    |
    |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
    |    |    |    |    |    |    |    |    |
    /---------------------------------------/
    | MSB                               LSB |
    /---------------------------------------/
    Note: The OCTET STRING is coded as an unsigned integer.
    Value range: H'0 - H'FF
    Value and Meaning information for Cause Code is available
    in the Application Information "Mapping of Cause Codes
    and Location Information".
    """


class ChannelCodings(primitives.AddressString):
    """ASN.1 Formal Description
    ChannelCodings ::= OCTET STRING (SIZE(1))
    |    |    |    |    |    |    |    |    |
    |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
    |    |    |    |    |    |    |    |    |
    /---------------------------------------/
    |                                       |
    /---------------------------------------/
    Bit assignment:
    Bit 1:         4.8 kbps channel coding
    Bit 2:         9.6 kbps channel coding
    Bit 4:         14.4 kbps channel coding
    Bits 3, 5 - 8: Spare
    Bit values:
    0: Channel Coding not Acceptable/Used
    1: Channel Coding Acceptable/Used
    """


class ChargeAreaCode(primitives.AddressString):
    """ASN.1 Formal Description
    ChargeAreaCode ::= OCTET STRING (SIZE(3))
    The digits for ID Code are encoded as a TBCD-STRING.
    |    |    |    |    |    |    |    |    |
    |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
    |    |    |    |    |    |    |    |    |
    /---------------------------------------/
    | 2nd CA Code digit | 1st CA Code digit | octet 1 of TBCD
    +-------------------+-------------------+
    | 4th CA Code digit | 3rd CA Code digit | octet 2 of TBCD
    +-------------------+-------------------+
    | Filler            | 5th CA Code digit | octet 3 of TBCD
    /---------------------------------------/
    Acceptable digits are between 0 and 9.
    Note1: CA Code consists currently of max 5 digits and
    the 6th digit is filler (H'F).
    Note2: In case of POICA the 6th digit is filler (H'0).
    """


class ChargeInformation(primitives.AddressString):
    """Charge Information

    This parameter Contains flexible charging tariff
    information that is received or generated by
    the mobile network. It is transmitted in eACM/ACM,
    CHG or CPG message.

    Charge Information consists of a unit rate indicator
    (10 or 100 Yen), a charge rate information category
    and the charge rate information (i.e. tariffs) itself.
    Charge rate information is made up of initial units
    and one to four (day, evening, night and spare) charge
    rates.

    Unit rate indicator can also be specified as 'No
    indication' and in that case no charge rate information
    is included.

    Note: The last received Charge Information will be
          stored in the CDR.

    The parameter is only applicable for WCDMA Japan.

      ASN.1 Formal Description
      ChargeInformation ::= OCTET STRING (SIZE(2..33))
      |     |     |     |     |     |     |     |     |
      |  8  |  7  |  6  |  5  |  4  |  3  |  2  |  1  |
      |     |     |     |     |     |     |     |     |
      /-----------------------------------------------/
      |       Units per time period (UTP)             |  octet 1
      +-----------------------------------------------+
      | ext | Charge rate information category (CRIC) |  octet 2
      +-----------------------------------------------+
      |       Length of charge rate information       |  octet 3
      +-----------------------------------------------+
      |       Initial units (IU)            (octet M) |  octet 4
      +-----------------------------------------------+
      |       Initial units (IU)            (octet N) |  octet 5
      +-----------------------------------------------+
      |       Daytime charge rate (DCR)     (octet A) |  octet 6
      +-----------------------------------------------+
      |       Daytime charge rate (DCR)     (octet B) |  octet 7
      +-----------------------------------------------+
      |       Daytime charge rate (DCR)     (octet C) |  octet 8
      +-----------------------------------------------+
      |       Evening time charge rate (ECR)(octet D) |  octet 9
      +-----------------------------------------------+
      |       Evening time charge rate (ECR)(octet E) |  octet 10
      +-----------------------------------------------+
      |       Evening time charge rate (ECR)(octet F) |  octet 11
      +-----------------------------------------------+
      |       Nighttime charge rate (NCR)   (octet G) |  octet 12
      +-----------------------------------------------+
      |       Nighttime charge rate (NCR)   (octet H) |  octet 13
      +-----------------------------------------------+
      |       Nighttime charge rate (NCR)   (octet I) |  octet 14
      +-----------------------------------------------+
      |       Spare charge rate (SCR)       (octet J) |  octet 15
      +-----------------------------------------------+
      |       Spare charge rate (SCR)       (octet K) |  octet 16
      +-----------------------------------------------+
      |       Spare charge rate (SCR)       (octet L) |  octet 17
      +-----------------------------------------------+
      | ext | Charge rate information category (CRIC) |  octet 18
      +-----------------------------------------------+
      |       Length of charge rate information       |  octet 19
      +-----------------------------------------------+
      |       Initial units (IU)            (octet M) |  octet 20
      +-----------------------------------------------+
      |       Initial units (IU)            (octet N) |  octet 21
      +-----------------------------------------------+
      |       Daytime charge rate (DCR)     (octet A) |  octet 22
      +-----------------------------------------------+
      |       Daytime charge rate (DCR)     (octet B) |  octet 23
      +-----------------------------------------------+
      |       Daytime charge rate (DCR)     (octet C) |  octet 24
      +-----------------------------------------------+
      |       Evening time charge rate (ECR)(octet D) |  octet 25
      +-----------------------------------------------+
      |       Evening time charge rate (ECR)(octet E) |  octet 26
      +-----------------------------------------------+
      |       Evening time charge rate (ECR)(octet F) |  octet 27
      +-----------------------------------------------+
      |       Nighttime charge rate (NCR)   (octet G) |  octet 28
      +-----------------------------------------------+
      |       Nighttime charge rate (NCR)   (octet H) |  octet 29
      +-----------------------------------------------+
      |       Nighttime charge rate (NCR)   (octet I) |  octet 30
      +-----------------------------------------------+
      |       Spare charge rate (SCR)       (octet J) |  octet 31
      +-----------------------------------------------+
      |       Spare charge rate (SCR)       (octet K) |  octet 32
      +-----------------------------------------------+
      |       Spare charge rate (SCR)       (octet L) |  octet 33
      /-----------------------------------------------/
      UNITS PER TIME PERIOD (UTP)
      00000000  Spare
      00000001
      to        Reserved for network specific use
      10000000
      10000001
      to        Spare
      11111011
      11111100  100 yen
      11111101  10 yen
      11111110  No indication
      11111111  Spare
      CHARGE RATE INFORMATION CATEGORY (CRIC)
      0000000  Spare
      0000001
      to       Reserved for network specific use
      1000000
      1000001
      to       Spare
      1111011
      1111100  Public (payphone)
      1111101  Ordinary
      1111110  No flexible charge rate information
      1111111  Spare
      EXTENSION INDICATOR (ext)
      0   Octet continues through the next octets.
      1   Last octet
      LENGTH OF CHARGE RATE INFORMATION
      Can assume only the value 14 if generated in WCDMA, but can
      assume also other values (e.g. 5, 8, 11) when received
      from other networks.
      INITIAL UNITS (IU)
      Value range '0 - 15' as IA5 coded in two octets (10M + N),
      e.g. for IU value '1' octet M = '30H' and octet N = '31H'.
      DAYTIME CHARGE RATE (DCR)
      Consists of the Time Period (TP) field with the value
      range '1 - 999' as IA5 coded in three octets
      ((100A + 10B + C))/2) seconds/ unit charge, e.g. for
      TP value '120' octet A = '31H', B = '32H' and C = '30H'.
      The unit of the TP field is 0.5 s, and thus e.g. the value
      '120' stands for 60 s meaning, that the call charge will be
      incremented every minute with e.g. 10 yen.
      EVENING TIME CHARGE RATE (ECR),
      Same coding as for Daytime Charge Rate (DCR) with octets
      D, E and F, ie. ((100D+10E+F)/2) seconds/unit charge
      NIGHTTIME CHARGE RATE (NCR),
      Same coding as for Daytime Charge Rate (DCR) with octets
      G, H and I, ie. ((100G+10H+I)/2) seconds/unit charge
      SPARE CHARGE RATE (SCR)
      Same coding as for Daytime Charge Rate (DCR) with octets
      J, K and L, ie. ((100J+10K+L)/2) seconds/unit charge
      Note 1:  A certain Charge Rate Information Category
      (CRIC) value can occur only once in the CI
      parameter.
      Note 2:  The maximum length (33 octets) of the CI
      parameter occurs, when the charge rate
      information is given for both the 'ordinary'
      and 'public' category at the same time (for
      two CRIC values).
      Note 3:  The minimum length (2 octets) of the CI
      parameter occurs, when the CRIC field holds
      the value 'No flexible charge rate information'.
      In this case the UTP field holds the value
      'No Indication' and the Extension indicator is
      coded '1'. This means in fact that the call is
      free of charge (from flexible charging point of
      view).
    """


class ChargingUnitsAddition(primitives.AddressString):
    """ASN.1 Formal Description
    ChargingUnitsAddition ::= OCTET STRING (SIZE(2))
    |    |    |    |    |    |    |    |    |
    |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
    |    |    |    |    |    |    |    |    |
    /---------------------------------------/
    | MSB                                   |  octet 1
    +---------------------------------------+
    |                                    LSB|  octet 2
    /---------------------------------------/
    Value range: H'0 - H'7FFF
    """


class Counter(primitives.AddressString):
    """TDS Counter

      The TDS Counter contains the number of received TDS
      related CHG messages, i.e. it reflects the number of
      telephone numbers supplied by the service provider
      when a mobile subscriber is using the telephone
      directory service.

      The parameter is only applicable for WCDMA Japan.

    ASN.1 Formal Description
        Counter ::= OCTET STRING (SIZE(1..4))
        |    |    |    |    |    |    |    |    |
        |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
        |    |    |    |    |    |    |    |    |
        /---------------------------------------/
        | MSB                                   | octet 1
        +---------------------------------------+
        |                                       | octet 2
        +---------------------------------------+
        |                                       | octet 3
        +---------------------------------------+
        |                                    LSB| octet 4
        /---------------------------------------/
        Value range 0 - H'FFFFFFFF (4 Octets)
        1 - H'F        (1 Octet )
        Note : The OCTET STRING is internally coded as
        an unsigned INTEGER.
        For WCDMA ETSI and GSM the number of octets is
        always 4 and for WCDMA Japan the number of octets
        is always 1.
    """


class CRIToMS:
    """ASN.1 Formal Description
    CRIToMS ::= TBCDString (SIZE(14))
    |    |    |    |    |    |    |    |    |
    |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
    |    |    |    |    |    |    |    |    |
    /---------------------------------------/
    |   e1 2nd digit    |  e1 1st digit     | octet 1
    +-------------------+-------------------+
    |   e1 4th digit    |  e1 3rd digit     | octet 2
    +-------------------+-------------------+
    |   e2 2nd digit    |  e2 1st digit     | octet 3
    +-------------------+-------------------+
    |   e2 4th digit    |  e2 3rd digit     | octet 4
    +-------------------+-------------------+
    |   e3 2nd digit    |  e3 1st digit     | octet 5
    +-------------------+-------------------+
    |   e3 4th digit    |  e3 3rd digit     | octet 6
    +-------------------+-------------------+
    |   e4 2nd digit    |  e4 1st digit     | octet 7
    +-------------------+-------------------+
    |   e4 4th digit    |  e4 3rd digit     | octet 8
    +-------------------+-------------------+
    |   e5 2nd digit    |  e5 1st digit     | octet 9
    +-------------------+-------------------+
    |   e5 4th digit    |  e5 3rd digit     | octet 10
    +-------------------+-------------------+
    |   e6 2nd digit    |  e6 1st digit     | octet 11
    +-------------------+-------------------+
    |   e6 4th digit    |  e6 3rd digit     | octet 12
    +-------------------+-------------------+
    |   e7 2nd digit    |  e7 1st digit     | octet 13
    +-------------------+-------------------+
    |   e7 4th digit    |  e7 3rd digit     | octet 14
    /---------------------------------------/
    Value range for all e-elements: 0 - 8191
    Note: Further details of e-elements can be found in the
    Technical Specification '3GPP 22.024, Description of
    Charge Advice Information (CAI)'.
    Values are represented as binary coded decimal digits
    in TBCDString.
    """


class C7ChargingMessage(primitives.AddressString):
    """CCITT No.7 Charging Message

      This parameter contains the time of the reception of the
      message and the data of the charging message.

      This parameter is available if received and the national
      signalling system supports the function.

      The parameter is not applicable for WCDMA Japan.
    ASN.1 Formal Description
        C7ChargingMessage ::= OCTET STRING (SIZE(8))
        |    |    |    |    |    |    |    |    |
        |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
        |    |    |    |    |    |    |    |    |
        /---------------------------------------/
        |                  Hours                | octet 1
        +---------------------------------------+
        |                 Minutes               | octet 2
        +---------------------------------------+
        |                MessageInd.            | octet 3
        +---------------------------------------+
        | Tax quantum  (A)  | Tariff Ind. (A)   | octet 4
        +---------------------------------------+
        |       Tariff factor (A)               | octet 5
        +---------------------------------------+
        |            Time Indicator  (B)        | octet 6
        +---------------------------------------+
        | Tax quantum  (B)  | Tariff Ind. (B)   | octet 7
        +---------------------------------------+
        |       Tariff factor (B)               | octet 8
        /---------------------------------------/
        The C7 Charging Message contains the
        following information:
        TIME OF RECEPTION OF THE MESSAGE (octets 1 and 2)
        Octet 1 contains hours, value range 00-23
        Octet 2 contains minutes, value range 00-59
        MESSAGE INDICATORS (octet 3)
        Bits 8-5  are always set to zero
        Bits 4-1
        B1 : Indicator of the current tariff
        0= Tax quantum (A) and tariff
        indicator (A) are not present.
        1= Tax quantum (A) and tariff
        indicator (A) are present.
        B2 : Indicator of the current tariff
        0= Tariff factor (A) is not present.
        1= Tariff factor (A) is present.
        B3 : Indicator of the next tariff
        0= Tax quantum (B) and tariff
        indicator (B) are not present.
        1= Tax quantum (B) and tariff
        indicator (B) are present.
        B4 : Indicator of the next tariff
        0= Tariff factor (B) is not present.
        1= Tariff factor (B) is present.
        TAX QUANTUM (A) (octet 4, bits 8-5)
        Number of Charging Units 0-15 can be registered.
        TARIFF INDICATOR (A) (octet 4, bits 4-1)
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
        TARIFF FACTOR (A) (octet 5)
        Number from 1 to 255.
        TIME INDICATOR (B) (octet 6)
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
        TAX QUANTUM (B) (octet 7, bits 8-5)
        Number of Charging Units 0-15 can be registered.
        TARIFF INDICATOR (B) (octet 7, bits 4-1)
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
        TARIFF FACTOR (B) (octet 8)
        Number from 1 to 255.
    """


class Date(primitives.AddressString):
    """ASN.1 Formal Description
    Date ::= OCTET STRING (SIZE(3..4))
    Note: The OCTET STRING is coded as an unsigned
    integer.
    The number of year digits is determined by exchange
    parameter.
    Two digit (Year) format:
    |    |    |    |    |    |    |    |    |
    |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
    |    |    |    |    |    |    |    |    |
    /---------------------------------------/
    |                                       | octet 1 (Year)
    +---------------------------------------+
    |                                       | octet 2 (Month)
    +---------------------------------------+
    |                                       | octet 3 (Day)
    /---------------------------------------/
    Year  (octet 1): Value range 0-99 (H'0 - H'63)
    Month (octet 2): Value range 1-12 (H'1 - H'C)
    Day   (octet 3): Value range 1-31 (H'1 - H'1F)
    Four digit (Year) format:
    |    |    |    |    |    |    |    |    |
    |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
    |    |    |    |    |    |    |    |    |
    /---------------------------------------/
    |                                       | octet 1 (Year)
    +---------------------------------------+
    |                                       | octet 2 (Year)
    +---------------------------------------+
    |                                       | octet 3 (Month)
    +---------------------------------------+
    |                                       | octet 4 (Day)
    /---------------------------------------/
    Year  (octet 1): Value range 19 or 20 (H'13 or H'14)
    Year  (octet 2): Value range 0 - 99 (H'0 - H'63)
    Month (octet 3): Value range 1 - 12 (H'1 - H'C)
    Day   (octet 4): Value range 1 - 31 (H'1 - H'1F)
    """


class DecipheringKeys(primitives.AddressString):
    """ASN.1 Formal Description
    DecipheringKeys ::= OCTET STRING (SIZE (8..15))
    |    |    |    |    |    |    |    |    |
    |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
    |    |    |    |    |    |    |    |    |
    /---------------------------------------/
    |MSB              Spare            |CKF |  octet 1
    +---------------------------------------+
    |     Current Deciphering Key Value     |  octet 2
    /---------------------------------------/
    .
    .
    .
    /---------------------------------------/
    |     Current Deciphering Key Value     |  octet 8
    +---------------------------------------+
    |       Next Deciphering Key Value      |  octet 9
    /---------------------------------------/
    .
    .
    .
    /---------------------------------------/
    |       Next Deciphering Key Value   LSB|  octet 15
    /---------------------------------------/
    Octet 1:
    Bit 1     Ciphering Key Flag (CKF)
    Bit 2 - 7 Spare
    This flag indicates the current Ciphering Key Flag used
    in the LCS assistance data broadcast messages in the
    location area.
    Octet 2 - 8:
    Current Deciphering Key contains the 56 bit
    deciphering key that is currently in use in location
    area for deciphering the LCS assistance data broadcast
    messages.
    Octet 9 - 15:
    Next Deciphering Key contains the 56 bit deciphering
    key that will be used next in location area for deciphering
    the LCS assistance data broadcast messages.
    For further information see GSM 09.31.
    """


class Distributed(primitives.AddressString):
    """ASN.1 Formal Description
    Distributed ::=  OCTET STRING (SIZE(4))
    |    |    |    |    |    |    |    |    |
    |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
    |    |    |    |    |    |    |    |    |
    /----------------------------------------/
    |     Percentage for A-party             |  octet 1
    +----------------------------------------+
    |     Percentage for B-party             |  octet 2
    +----------------------------------------+
    |     Percentage for C-party             |  octet 3
    +----------------------------------------+
    |     Percentage for Other Party         |  octet 4
    /----------------------------------------/
    Octet 1: Value range 0 - 99  (H'0 - H'63)
    Octet 2: Value range 0 - 99  (H'0 - H'63)
    Octet 3: Value range 0 - 99  (H'0 - H'63)
    Octet 4: Value range 0 - 99  (H'0 - H'63)
    """


class EndToEndAccessDataMap(primitives.AddressString):
    """ASN.1 Formal Description
    EndToEndAccessDataMap ::= OCTET STRING (SIZE(1))
    |    |    |    |    |    |    |    |    |
    |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
    |    |    |    |    |    |    |    |    |
    /---------------------------------------/
    |                                       |
    /---------------------------------------/
    Bit 1:
    Calling party number indicator
    0 = Calling party number not sent
    1 = Calling party number sent(SETUP)
    Bit 2:
    Calling party subaddress indicator
    0 = Calling party subaddress not sent
    1 = Calling party subaddress sent (SETUP)
    Bit 3:
    Called party subadresss indicator
    0 = Called party subaddress not sent
    1 = Called party subaddress sent (SETUP)
    Bit 4:
    High layer compatibility indicator
    0 = High layer compatibility not sent
    1 = High layer compatibility sent (SETUP)
    Bit 5:
    Low layer compatibility indicator
    0 = Low layer compatibility not sent
    1 = low layer compatibility sent (SETUP)
    Bit 6:
    Low layer compatibility indicator
    0 = Low layer compatibility not sent
    1 = low layer compatibility sent (CONNECT)
    Bit 7:
    Connected party subaddress indicator
    0 = Connected party subaddress not sent
    1 = Connected party subaddress sent (CONNECT)
    Bit 8:
    Reserved
    Note that "SETUP" and "CONNECT" are functional messages.
    """


class ErrorRatio(primitives.AddressString):
    """ASN.1 Formal Description
    ErrorRatio ::= OCTET STRING (SIZE(2))
    |    |    |    |    |    |    |    |    |
    |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
    |    |    |    |    |    |    |    |    |
    /---------------------------------------/
    |               Mantissa                |  octet 1
    +---------------------------------------+
    |               Exponent                |  octet 2
    /---------------------------------------/
    Note: The OCTET STRING is coded as an unsigned INTEGER.
    Value range:  0 - 9 for both octets.
    """


class EventCRIToMS:
    """ASN.1 Formal Description
    EventCRIToMS ::= TBCDString (SIZE(4))
    |   |   |   |   |   |   |   |   |
    | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 |
    |   |   |   |   |   |   |   |   |
    /-------------------------------/
    | e3 2nd digit  | e3 1st digit  |  octet 1
    +---------------+---------------+
    | e3 4th digit  | e3 3rd digit  |  octet 2
    +---------------+---------------+
    | e4 2nd digit  | e4 1st digit  |  octet 3
    +---------------+---------------+
    | e4 4th digit  | e4 3rd digit  |  octet 4
    /-------------------------------/
    Value range for all e-elements : 0 - 8191
    Note: Further details of e-elements can be found in
    Technical Specification '3GPP 22.024.
    Values are represented as binary coded decimal
    digits in TBCDString.
    """


class GenericDigitsSet(primitives.AddressString):
    """ASN.1 Formal Description
    GenericDigitsSet ::= SET SIZE (1..20) OF GenericDigits
    GenericDigits ::= OCTET STRING (SIZE(2..15))
    |    |    |    |    |    |    |    |    |
    |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
    |    |    |    |    |    |    |    |    |
    /---------------------------------------/
    |              contents                 |  octet 1
    +---------------------------------------+
    |              contents                 |  octet 2
    /---------------------------------------/
    .
    .
    .
    /---------------------------------------/
    |              contents                 |  octet n (<16)
    /---------------------------------------/
    The contents of each octet are specified in the Function
    Specification (FS) for a particular Ericsson provided IN
    service, and in INAP protocol specifications.
    """


class GenericNumbersSet(primitives.AddressString):
    """ASN.1 Formal Description
    GenericNumbersSet ::= SET SIZE (1..20) OF GenericNumber
    GenericNumber ::= OCTET STRING (SIZE(3..17))
    |    |    |    |    |    |    |    |    |
    |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
    |    |    |    |    |    |    |    |    |
    /---------------------------------------/
    |              contents                 |  octet 1
    +---------------------------------------+
    |              contents                 |  octet 2
    /---------------------------------------/
    .
    .
    .
    /---------------------------------------/
    |              contents                 |  octet n (<18)
    /---------------------------------------/
    The contents of each octet are specified in the
    Function Specification (FS) for a particular Ericsson
    provided IN service, and in INAP protocol specifications.
    """


class GSMCallReferenceNumber(primitives.AddressString):
    """ASN.1 Formal Description
    GSMCallReferenceNumber ::= OCTET STRING (SIZE(1..8))
    |    |    |    |    |    |    |    |    |
    |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
    |    |    |    |    |    |    |    |    |
    /---------------------------------------/
    | MSB                                   |  octet 1
    +---------------------------------------+
    |                                       |  octet 2
    /---------------------------------------/
    .
    .
    .
    /---------------------------------------/
    |                                    LSB|  octet n
    /---------------------------------------/
    """


class LCSAccuracy(primitives.AddressString):
    """ASN.1 Formal Description
    LCSAccuracy ::= OCTET STRING (SIZE(1))
    |    |    |    |    |    |    |    |    |
    |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
    |    |    |    |    |    |    |    |    |
    /---------------------------------------/
    | MSB                               LSB |
    /---------------------------------------/
    Bits 7 - 1 = Uncertainty Code
    Bit  8 = 0
    Value range: H'0 - H'7F (0 - 127)
    The uncertainty is coded on 7 bits, as the binary
    encoding of K. The uncertainty r, expressed in metres,
    is mapped to a number K, with the following formula:
    K
    r = C ((1 + x)   - 1)
    With C = 10 and x = 0,1. With 0 <= K <= 127,
    a range between 0 and 1800 kilometres is achieved for the
    uncertainty, still being able to code down to values as
    small as 1 metre.
    For further details for Uncertainty Code see 3G TS 23.032.
    """


class LocationCode(primitives.AddressString):
    """ASN.1 Formal Description
    LocationCode ::= OCTET STRING (SIZE(1))
    |    |    |    |    |    |    |    |    |
    |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
    |    |    |    |    |    |    |    |    |
    /---------------------------------------/
    | MSB                               LSB |
    /---------------------------------------/
    Note: OCTET STRING is coded as an unsigned integer.
    Value range: H'0 - H'F
    Value and Meaning information for Location Code is available
    in the Application Information "Mapping of Cause Codes
    and Location Information".
    """


class LocationEstimate(primitives.AddressString):
    """ASN.1 Formal Description
    LocationEstimate ::= OCTET STRING (SIZE(1..91))
    When shape is 'Ellipsoid point':
    |    |    |    |    |    |    |    |    |
    |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
    |    |    |    |    |    |    |    |    |
    /---------------------------------------/
    |   Type of Shape   |       Spare       |  octet 1
    +---------------------------------------+
    | S  | MSB   Degrees of Latitude        |  octet 2
    +---------------------------------------+
    |            Degrees of Latitude        |  octet 3
    +---------------------------------------+
    |            Degrees of Latitude    LSB |  octet 4
    +---------------------------------------+
    | MSB      Degrees of Longitude         |  octet 5
    +---------------------------------------+
    |          Degrees of Longitude         |  octet 6
    +---------------------------------------+
    |          Degrees of Longitude     LSB |  octet 7
    /---------------------------------------/
    When shape is 'Ellipsoid point with uncertainty Circle':
    |    |    |    |    |    |    |    |    |
    |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
    |    |    |    |    |    |    |    |    |
    /---------------------------------------/
    |   Type of Shape   |       Spare       |  octet 1
    +---------------------------------------+
    | S  | MSB   Degrees of Latitude        |  octet 2
    +---------------------------------------+
    |            Degrees of Latitude        |  octet 3
    +---------------------------------------+
    |            Degrees of Latitude    LSB |  octet 4
    +---------------------------------------+
    | MSB      Degrees of Longitude         |  octet 5
    +---------------------------------------+
    |          Degrees of Longitude         |  octet 6
    +---------------------------------------+
    |          Degrees of Longitude     LSB |  octet 7
    +---------------------------------------+
    |Spare       Uncertainty code           |  octet 8
    /---------------------------------------/
    When shape is 'Ellipsoid point with uncertainty Ellipse':
    |    |    |    |    |    |    |    |    |
    |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
    |    |    |    |    |    |    |    |    |
    /---------------------------------------/
    |   Type of Shape   |       Spare       |  octet 1
    +---------------------------------------+
    | S  | MSB   Degrees of Latitude        |  octet 2
    +---------------------------------------+
    |            Degrees of Latitude        |  octet 3
    +---------------------------------------+
    |            Degrees of Latitude    LSB |  octet 4
    +---------------------------------------+
    | MSB      Degrees of Longitude         |  octet 5
    +---------------------------------------+
    |          Degrees of Longitude         |  octet 6
    +---------------------------------------+
    |          Degrees of Longitude     LSB |  octet 7
    +---------------------------------------+
    |Spare    Uncertainty semi-major        |  octet 8
    +---------------------------------------+
    |Spare    Uncertainty semi-minor        |  octet 9
    +---------------------------------------+
    |       Orientation of major axis       |  octet 10
    +---------------------------------------+
    |Spare        Confidence                |  octet 11
    /---------------------------------------/
    When shape is 'Polygon':
    |    |    |    |    |    |    |    |    |
    |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
    |    |    |    |    |    |    |    |    |
    /---------------------------------------/
    |   Type of Shape   |       Spare       |  octet 1
    +---------------------------------------+
    | S1 | MSB   Degrees of Latitude        |  octet 2
    +---------------------------------------+
    |            Degrees of Latitude        |  octet 3
    +---------------------------------------+
    |            Degrees of Latitude    LSB |  octet 4
    +---------------------------------------+
    | MSB      Degrees of Longitude         |  octet 5
    +---------------------------------------+
    |          Degrees of Longitude         |  octet 6
    +---------------------------------------+
    |          Degrees of Longitude     LSB |  octet 7
    /---------------------------------------/
    .
    .
    .
    /---------------------------------------/
    | Sn | MSB   Degrees of Latitude        |  octet 6n-4
    +---------------------------------------+
    |            Degrees of Latitude        |  octet 6n-3
    +---------------------------------------+
    |            Degrees of Latitude    LSB |  octet 6n-2
    +---------------------------------------+
    | MSB      Degrees of Longitude         |  octet 6n-1
    +---------------------------------------+
    |          Degrees of Longitude         |  octet 6n
    +---------------------------------------+
    |          Degrees of Longitude     LSB |  octet 6n+1
    /---------------------------------------/
    When shape is 'Ellipsoid point with altitude':
    |    |    |    |    |    |    |    |    |
    |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
    |    |    |    |    |    |    |    |    |
    /---------------------------------------/
    |   Type of Shape   |       Spare       |  octet 1
    +---------------------------------------+
    | S  | MSB   Degrees of Latitude        |  octet 2
    +---------------------------------------+
    |            Degrees of Latitude        |  octet 3
    +---------------------------------------+
    |            Degrees of Latitude    LSB |  octet 4
    +---------------------------------------+
    | MSB      Degrees of Longitude         |  octet 5
    +---------------------------------------+
    |          Degrees of Longitude         |  octet 6
    +---------------------------------------+
    |          Degrees of Longitude     LSB |  octet 7
    +---------------------------------------+
    | D  | MSB      Altitude                |  octet 8
    +---------------------------------------+
    |               Altitude            LSB |  octet 9
    /---------------------------------------/
    When shape is 'Ellipsoid point with altitude and
    uncertainty ellipsoid':
    |    |    |    |    |    |    |    |    |
    |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
    |    |    |    |    |    |    |    |    |
    /---------------------------------------/
    |   Type of Shape   |       Spare       |  octet 1
    +---------------------------------------+
    | S  | MSB   Degrees of Latitude        |  octet 2
    +---------------------------------------+
    |            Degrees of Latitude        |  octet 3
    +---------------------------------------+
    |            Degrees of Latitude    LSB |  octet 4
    +---------------------------------------+
    | MSB      Degrees of Longitude         |  octet 5
    +---------------------------------------+
    |          Degrees of Longitude         |  octet 6
    +---------------------------------------+
    |          Degrees of Longitude     LSB |  octet 7
    +---------------------------------------+
    | D  | MSB      Altitude                |  octet 8
    +---------------------------------------+
    |               Altitude            LSB |  octet 9
    +---------------------------------------+
    |Spare    Uncertainty semi-major        |  octet 10
    +---------------------------------------+
    |Spare    Uncertainty semi-minor        |  octet 11
    +---------------------------------------+
    |       Orientation of major axis       |  octet 12
    +---------------------------------------+
    |Spare    Uncertainty altidude          |  octet 13
    +---------------------------------------+
    |Spare        Confidence                |  octet 14
    /---------------------------------------/
    When shape is ' Ellipsoid Arc':
    |    |    |    |    |    |    |    |    |
    |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
    |    |    |    |    |    |    |    |    |
    /---------------------------------------/
    |   Type of Shape   |       Spare       |  octet 1
    +---------------------------------------+
    | S  | MSB   Degrees of Latitude        |  octet 2
    +---------------------------------------+
    |            Degrees of Latitude        |  octet 3
    +---------------------------------------+
    |            Degrees of Latitude    LSB |  octet 4
    +---------------------------------------+
    | MSB      Degrees of Longitude         |  octet 5
    +---------------------------------------+
    |          Degrees of Longitude         |  octet 6
    +---------------------------------------+
    |          Degrees of Longitude     LSB |  octet 7
    +---------------------------------------+
    | MSB         Inner radius              |  octet 8
    +---------------------------------------+
    |             Inner radius          LSB |  octet 9
    +---------------------------------------+
    |           Uncertainty radius          |  octet 10
    +---------------------------------------+
    |              Offset angle             |  octet 11
    +---------------------------------------+
    |            Included angle             |  octet 12
    +---------------------------------------+
    |Spare         Confidence               |  octet 13
    /---------------------------------------/
    Descriptions and Value Ranges:
    Type of Shape
    =============
    Bits
    8 7 6 5
    0 0 0 0  Ellipsoid point
    0 0 0 1  Ellipsoid point with uncertainty Circle
    0 0 1 1  Ellipsoid point with uncertainty Ellipse
    0 1 0 1  Polygon
    1 0 0 0  Ellipsoid point with altitude
    1 0 0 1  Ellipsoid point with altitude and
    uncertainty Ellipsoid
    1 0 1 0  Ellipsoid Arc
    other values   reserved for future use
    Number of points (n)
    ====================
    Then number of points (n) in Polygon shape is coded
    with 4 bits.
    Value range: 3 - 15
    S - Sign of Latitude
    ==================
    Bit 8 S: Sign of latitude
    Value 0  North
    Value 1  South
    Degrees of Latitude
    ===================
    The latitude is coded with 24 bits: 1 bit of sign and a
    number between
    23
    0 and 2  - 1 coded in binary on 23 bits.
    The relation between the coded number N and the range of
    (absolute) latitudes X it encodes is the following
    (X in degrees):
    23
    2
    N <= ---  X < N + 1
    90
    23
    except for N = 2  - 1, for which the range is extended to
    include N + 1.
    Value range: H'0 - H'7FFFFF (0 - 8388607)
    Degrees of Longitude
    ====================
    The longitude, expressed in the range -180 degrees,
    +180 degrees, is coded as a number between
    23      23
    - 2   and 2  - 1, coded in 2's complement binary on 24 bits.
    The relation between the coded number N and the range of
    longitude X it encodes is the following (X in degrees):
    24
    2
    N <= ---  X < N + 1
    360
    Value range: H'0 - H'FFFFFF (0 - 16777215)
    Uncertainty Code
    ================
    The uncertainty is coded on 7 bits, as the binary
    encoding of K. The uncertainty r, expressed in metres,
    is mapped to a number K, with the following formula:
    K
    r = C ((1 + x) - 1)
    With C = 10 and x = 0,1. With 0 <= K <= 127,
    a range between 0 and 1800 kilometres is achieved for the
    uncertainty, still being able to code down to values as
    small as 1 metre.
    -- Bits 7 - 1 = Uncertainty code
    -- Bit  8     = 0 (spare)
    Value range: H'0 - H'7F (0 - 127)
    Uncertainty of semi-major axis
    ==============================
    Semi-major axis length is defined as the maximum
    radius of the ellipse.
    -- Bits 7 - 1 = Uncertainty code of semi-major axis
    -- Bit  8     = 0 (spare)
    Value range: H'0 - H'7F (0 - 127)
    Uncertainty of semi-minor axis
    ==============================
    Semi-minor axis length is defined as the minimum
    radius of the ellipse.
    -- Bits 7 - 1 = Uncertainty code of semi-minor axis
    -- Bit  8     = 0 (spare)
    Value range: H'0 - H'7F (0 - 127)
    Orientation of major axis
    =========================
    8 bit 2's complement, allowing for necessary range
    from -90 to +90 degrees.
    North = 0 degree, West = 90 degrees, East = -90 degrees.
    Value range: H'0 - H'FF (0 - 255)
    Confidence
    ==========
    The confidence by which the position of a target entity
    is known to be within the shape description, (expressed
    as a percentage) is directly mapped from the 7 bit binary
    number K, except for K = 0 which is used to indicate 'no
    information', and 100 < K <= 128 which should not be used
    but may be interpreted as "no information" if received.
    -- Bits 7 - 1 = Uncertainty code of semi-major axis
    -- Bit  8     = 0 (spare)
    Value range: H'0 - H'7F (0 - 127)
    Altitude
    ========
    Altitude is encoded in increments of 1 meter using a 15 bit
    binary coded number N. The relation between the number N
    and the range of altitudes alpha (in metres) it encodes is
    described by the following equation:
    N <= alpha < N + 1
    15
    except for N = 2  - 1 for which the range is extended to
    include all greater values of alpha.
    The direction of altitude is encoded by a single bit with
    bit value 0 representing height above the WGS84 (Military
    Standard Department of Defence World Geodetic System)
    ellipsoid  surface and bit value 1 representing depth
    below the WGS84 ellipsoid surface.
    -- Bits 15 - 1 = Altitude
    -- Bit  16     = D
    D:  Direction of Altitude
    Bit value 0 Altitude expresses height
    Bit value 1 Altitude expresses depth
    Value range: H'0 - H'7FFFF ( 0 - 32767)
    Uncertainty altitude
    ====================
    The uncertainty in altitude, h, expressed in metres is
    mapped from the binary number K, with the following
    formula:
    K
    h = C((1 + x)  - 1)
    with C = 45 and x = 0.025. With 0 <= K <= 127, a suitably
    useful range between 0 and 990 meters is achieved for the
    uncertainty altitude. The uncertainty can then be coded
    on 7 bits, as the binary encoding of K.
    For values of K and geometrical definition uncertainty
    altitude of an ellipsoid point with altitude, see
    3G TS 23.032.
    -- Bits 7 - 1 = Uncertainty altitude
    -- Bit  8     = 0 (spare)
    Value range: H'0 - H'7F (0 - 127)
    Inner radius
    ============
    Inner radius is encoded in increments of 5 meters using a
    16 bit binary coded number N. The relation between the
    number N and the range of radius r (in metres) it encodes
    is described by the following equation:
    5N <= r < 5(N + 1)
    16
    Except for N = 2  - 1 for which the range is extended to
    include all greater values of r. This provides a true
    maximum radius of 327,675 meters.
    The uncertainty radius is encoded as for the uncertainty
    latitude and longitude.
    Value range: H'0 - H'FFFF (0 - 65535)
    Uncertainty radius
    ==================
    The uncertainty radius is encoded as for the uncertainty
    latitude and longitude.
    -- Bits 7 - 1 = Uncertainty radius
    -- Bit  8     = 0 (spare)
    Value range: H'0 - H'7F (0 - 127)
    Offset Angle
    ============
    Offset and Included angle are encoded in increments of
    2 degrees using an 8 bit binary coded number N in the
    range 0 to 179.
    The relation between the number N and the range of angle
    alpha (in degrees) it encodes is described by the
    following equation:
    2N <= alpha < 2(N + 1)
    Accepted values for alpha are within the range
    from 0 to 359 degrees.
    Value range: H'0 - H'B3 (0 - 179)
    Values H'B4 - H'FF (180 - 255) are spare.
    Included Angle
    ==============
    Same as for Offset Angle except that accepted values for
    alpha are within the range from 1 to 360 degrees.
    For further details and geometrical definitions see
    3G TS 23.032.
    """


class MessageReference(primitives.AddressString):
    """ASN.1 Formal Description
    MessageReference ::= OCTET STRING (SIZE(1))
    |    |    |    |    |    |    |    |    |
    |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
    |    |    |    |    |    |    |    |    |
    /---------------------------------------/
    | MSB                               LSB |
    /---------------------------------------/
    Note: OCTET STRING is coded as an unsigned integer.
    Value range: H'0 - H'FF
    """


class MobileUserClass2(primitives.AddressString):
    """Mobile User Class 2

    This parameter contains Mobile system supplementary
    user type 2, obtained from Additional User Category
    (AUC) parameter in ISUP.

    It is used to indicate telecommunication method
    related information in the originating side of the call.

    The parameter is only applicable for WCDMA Japan.

      ASN.1 Formal Description
      MobileUserClass2 ::= OCTET STRING (SIZE(1))
      |    |    |    |    |    |    |    |    |
      |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
      |    |    |    |    |    |    |    |    |
      /---------------------------------------/
      | MSB                               LSB |
      /---------------------------------------/
      Additional Mobile Service Information Type 2,
      telecommunication method related information
      00000000 Spare
      00000001 HiCap method (analog)
      00000010 N/J-TACS
      00000011 PDC 800 MHz
      00000100 PDC 1.5 GHz
      00000101 N-STAR Satellite
      00000110 cdmaOne 800MHz
      00000111 Iridium Satellite
      00001000 IMT-2000
      00001001 PHS (fixed network dependent)
      00001010
      to       Spare
      11111111
    """


class MSNB:
    """ASN.1 Formal Description
    MSNB ::= TBCDString (SIZE(3..8))
    """


class OperationIdentifier(primitives.AddressString):
    """ASN.1 Formal Description
    OperationIdentifier ::= OCTET STRING (SIZE(1))
    |    |    |    |    |    |    |    |    |
    |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
    |    |    |    |    |    |    |    |    |
    /---------------------------------------/
    | MSB                               LSB |
    /---------------------------------------/
    Note: OCTET STRING is coded as an unsigned integer.
    Value range: H'0 - H'FF
    The meaning of each value is specified in the Application
    Information documents of the application owner blocks.
    The application owner blocks are listed in Application
    Information document "Mobile Telephony Data" in the "USSD
    Application Identifiers" chapter.
    """


class PositioningDelivery(primitives.AddressString):
    """ASN.1 Formal Description
    PositioningDelivery ::= OCTET STRING (SIZE(1))
    |    |    |    |    |    |    |    |    |
    |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
    |    |    |    |    |    |    |    |    |
    /---------------------------------------/
    | MSB                              LSB  |
    /---------------------------------------/
    Bits 1-2: Positioning Data Delivery to UE
    Bits 3-4: Positioning Data Delivery to GMLC
    Bits 5-6: Positioning Data Delivery to Emergency Center
    Bits 7-8: Validity indicator
    Bits 1-2, 3-4, 5-6
    Values: 0 = Successful positioning data
    Result successfully delivered
    1 = Successful positioning data
    Result unsuccessfully delivered
    2 = Unsuccessful positioning data
    Result successfully delivered
    3 = Unsuccessful positioning data
    Result unsuccessfully delivered
    Bits 7-8
    Values: 0 = Delivering required to UE
    (Bits 1-2 valid)
    1 = Delivering required to GMLC
    (Bits 3-4 valid)
    2 = Delivering required to Emergency Center
    (Bits 5-6 valid)
    3 = Delivering required to Emergency Center
    and to GMLC (Bits 3-4 and 5-6 valid)
    Note: Positioning Delivery to Emergency Center is not
    valid for WCDMA.
    """


class ProcedureCode:
    """ASN.1 Formal Description
    ProcedureCode ::= TBCDString (SIZE(1))
    """


class RANAPCauseCode(primitives.AddressString):
    """ASN.1 Formal Description
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


class ServiceCode:
    """ASN.1 Formal Description
    ServiceCode ::= TBCDString (SIZE(1..2))
    """


class ServiceFeatureCode(primitives.AddressString):
    """ASN.1 Formal Description
    ServiceFeatureCode ::= OCTET STRING (SIZE(2))
    |    |    |    |    |    |    |    |    |
    | 8  | 7  | 6  | 5  | 4  | 3  | 2  | 1  |
    |    |    |    |    |    |    |    |    |
    /---------------------------------------/
    |              contents                 | octet 1
    |---------------------------------------+
    |              contents                 | octet 2
    /---------------------------------------/
    The contents are specified in the Function Specification
    (FS) for a particular Ericsson provided IN service, and in
    INAP protocol specifications.
    """


class ServiceKey(primitives.AddressString):
    """ASN.1 Formal Description
    ServiceKey ::=  OCTET STRING (SIZE(4))
    |    |    |    |    |    |    |    |    |
    |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
    |    |    |    |    |    |    |    |    |
    /---------------------------------------/
    | MSB                                   | octet 1
    +---------------------------------------+
    |                                       | octet 2
    +---------------------------------------+
    |                                       | octet 3
    +---------------------------------------+
    |                                 LSB   | octet 4
    /---------------------------------------/
    Value Range H'0 - H'7FFFFFFF
    """


class TargetRNCid(primitives.AddressString):
    """ASN.1 Formal Description
    TargetRNCid ::= OCTET STRING (SIZE(7))
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
    | MSB   RNC-id                  | octet 6
    +-------------------------------+
    |       RNC-id,     cont.   LSB | octet 7
    /-------------------------------/
    Note: The OCTET STRING is coded as an unsigned INTEGER.
    MCC, Mobile country code (octet 1 and 2).
    MNC, Mobile network code (octet 2 and 3).
    Note: If MNC uses only 2 digits, 3rd is coded with
    filler H'F.
    LAC, Location area code (octet 4 and 5).
    RNC-id, Radio Network Control id (octet 6 and 7),
    value range: H'0 - H'FFF.
    """


class Time(primitives.AddressString):
    """ASN.1 Formal Description
    Time ::= OCTET STRING (SIZE(3..4))
    |    |    |    |    |    |    |    |    |
    |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
    |    |    |    |    |    |    |    |    |
    /---------------------------------------/
    |                                       | octet 1 (Hour)
    +---------------------------------------+
    |                                       | octet 2 (Minute)
    +---------------------------------------+
    |                                       | octet 3 (Second)
    +---------------------------------------+
    |                                       | octet 4 (10th of
    /---------------------------------------/          a second)
    Note: OCTET STRING is coded as an unsigned integer.
    Hour             (octet 1): value range  0-23 (H'0 - H'17)
    Minute           (octet 2): value range  0-59 (H'0 - H'3B)
    Second           (octet 3): value range  0-59 (H'0 - H'3B)
    10th of a second (octet 4): value range  0-9  (H'0 - H'9)
    Note: 10th of a second is only included for the parameter
    chargeableDuration and only used for WCDMA Japan.
    """


class TrafficActivityCode(primitives.AddressString):
    """ASN.1 Formal Description
    TrafficActivityCode ::= OCTET STRING (SIZE(5))
    |    |    |    |    |    |    |    |    |
    |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
    |    |    |    |    |    |    |    |    |
    /---------------------------------------/
    |                                       | octet 1 (TOS)
    +---------------------------------------+
    |                                       | octet 2 (TOI)
    +---------------------------------------+
    |                                       | octet 3 (TOP)
    +---------------------------------------+
    |                                       | octet 4 (TSC)
    +---------------------------------------+
    |                                       | octet 5 (ROP)
    /---------------------------------------/
    See the Application Information "Traffic Activity Code,
    ISDN-E Subscribers" for TOS, TOI, TOP and ROP values.
    The TSC is obtained from the Basic Service Charging Code
    (BSCC) and its value varies according to the operator's
    definition.
    """


class TransferDelay(primitives.AddressString):
    """ASN.1 Formal Description
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


class TransitCarrierInfo(primitives.AddressString):
    """ASN.1 Formal Description
    TransitCarrierInfo ::= OCTET STRING (SIZE(7..96))
    The digits in the Carrier ID Code and POICA are encoded
    as TBCD-STRING.
    |     |     |     |     |     |     |     |     |
    |  8  |  7  |  6  |  5  |  4  |  3  |  2  |  1  |
    |     |     |     |     |     |     |     |     |
    /-----------------------------------------------/
    |         Category of carrier 1                 |  octet 1
    |                                               |
    +-----------------------------------------------+
    |         Length of carrier 1                   |  octet 2
    |                                               |
    +-----------------------------------------------+
    |         Type of information                   |  octet 3
    |                                               |
    +-----------------------------------------------+
    |         Length of information                 |  octet 4
    |                                               |
    +-----------------------------------------------+
    |Odd/ |              Spare                      |  octet 5
    |even |                                         |
    +-----------------------------------------------+
    | 2nd Carrier ID Code   | 1st Carrier ID Code   |  octet 6
    | digit                 | digit                 |
    +-----------------------+-----------------------+
    | 4th Carrier ID Code   | 3rd Carrier ID Code   |  octet 7
    | digit                 | digit                 |
    +-----------------------------------------------+
    |         Type of information                   |  octet 8
    |                                               |
    +-----------------------------------------------+
    |         Length of information                 |  octet 9
    |                                               |
    +-----------------------------------------------+
    |Odd/ |              Spare                      |  octet 10
    |even |                                         |
    +-----------------------------------------------+
    | 2nd POICA digit       | 1st POICA digit       |  octet 11
    |                       |                       |
    +-----------------------+-----------------------+
    | 4th POICA digit       | 3rd POICA digit       |  octet 12
    |                       |                       |
    +-----------------------+-----------------------+
    | Filler (0 0 0 0)      | 5th POICA digit       |  octet 13
    |                       |                       |
    +-----------------------------------------------+
    |         Type of information                   |  octet 14
    |                                               |
    +-----------------------------------------------+
    |         Length of information                 |  octet 15
    |                                               |
    +-----------------------------------------------+
    | Entry POI-Hierarchy   | Exit POI-Hierarchy    |  octet 16
    |                       |                       |
    /-----------------------------------------------/
    .
    .
    .
    /-----------------------------------------------/
    |         Category of carrier 6                 |  octet 81
    |                                               |
    +-----------------------------------------------+
    |         Length of carrier 6                   |  octet 82
    |                                               |
    +-----------------------------------------------+
    |         Type of information                   |  octet 83
    |                                               |
    +-----------------------------------------------+
    |         Length of information                 |  octet 84
    |                                               |
    +-----------------------------------------------+
    |Odd/ |              Spare                      |  octet 85
    |even |                                         |
    +-----------------------------------------------+
    | 2nd Carrier ID Code   | 1st Carrier ID Code   |  octet 86
    | digit                 | digit                 |
    +-----------------------+-----------------------+
    | 4th Carrier ID Code   | 3rd Carrier ID Code   |  octet 87
    | digit                 | digit                 |
    +-----------------------------------------------+
    |         Type of information                   |  octet 88
    |                                               |
    +-----------------------------------------------+
    |         Length of information                 |  octet 89
    |                                               |
    +-----------------------------------------------+
    |Odd/ |              Spare                      |  octet 90
    |even |                                         |
    +-----------------------------------------------+
    | 2nd POICA digit       | 1st POICA digit       |  octet 91
    |                       |                       |
    +-----------------------+-----------------------+
    | 4th POICA digit       | 3rd POICA digit       |  octet 92
    |                       |                       |
    +-----------------------+-----------------------+
    | Filler (0 0 0 0)      | 5th POICA digit       |  octet 93
    |                       |                       |
    +-----------------------------------------------+
    |         Type of information                   |  octet 94
    |                                               |
    +-----------------------------------------------+
    |         Length of information                 |  octet 95
    |                                               |
    +-----------------------------------------------+
    | Entry POI-Hierarchy   | Exit POI-Hierarchy    |  octet 96
    |                       |                       |
    /-----------------------------------------------/
    Acceptable digits for Carrier ID Code and POICA are between
    0 and 9.
    Note 1: The possible length of the carrier x is
    5  octets : Carrier ID Code
    8  octets : Carrier ID Code and POI-Hierarchy
    11 octets : Carrier ID Code and POICA
    14 octets : Carrier ID Code, POI-Hierarchy and
    POICA information.
    Note 2: At maximum six carriers (CIEC, IEC or SCPC) will be
    output per call. The rest will be discarded.
    Note 3: CIEC and IEC information contain always Carrier
    identification code. Optionally they may contain
    POICA or POI-Hierarchy, or both.
    Note 4: SCPC contains only the Carrier identification code.
    Note 5: POI-Hierarchy information is not provided by
    carriers, which have only one POI-Hierarchy level
    in use.
    Note 6: The order of the Carrier identification code,
    POICA and POI-Hierarchy is not set.
    Note 7: POICA consists currently of max 5 digits and
    the 6th digit is filler (H'0). The 6th digit is
    spare for future use.
    CATEGORY OF CARRIER (x)
    00000000  Spare
    00000001
    to        Reserved for network specific use
    10000000
    10000001
    to        Spare
    11111001
    11111010  SCPC (Service Control Point Carrier)
    11111011  Reserved
    11111100  Reserved
    11111101  CIEC (Chosen Inter-Exchange Carrier)
    11111110  IEC  (Inter-Exchange Carrier)
    11111111  Spare
    TYPE OF INFORMATION
    00000000  Spare
    00000001
    to        Reserved for network specific use
    10000000
    10000001
    to        Spare
    11111011
    11111100  POI-Hierarchy
    11111101  POICA
    11111110  Carrier identification (ID) code
    11111111  Spare
    EXIT/ENTRY POI HIERARCHY
    0000  No indication
    0001  Hierarchy level 1
    0010  Hierarchy level 2
    0011
    to    Spare
    1111
    """


class TriggerData:
    """ASN.1 Formal Description
    TriggerData ::= SEQUENCE(
    triggerDetectionPoint (0) IMPLICIT TriggerDetectionPoint,
    serviceKey            (1) IMPLICIT ServiceKey,
    sCPAddress            CHOICE(
    co-located         (2) IMPLICIT NULL,
    pointCodeAndSubSystemNumber
    (3) IMPLICIT
    PointCodeAndSubSystemNumber,
    globalTitle        (4) IMPLICIT GlobalTitle,
    globalTitleAndSubSystemNumber
    (5) IMPLICIT
    GlobalTitleAndSubSystemNumber))
    """


class UserTerminalPosition(primitives.AddressString):
    """User Terminal Position

      This parameter contains data related to global satellite
      systems call. This parameter gives the user terminal
      position in longitude and latitude at call set up.

      The parameter is not applicable for WCDMA Japan.

    ASN.1 Formal Description
        UserTerminalPosition ::= OCTET STRING (SIZE(7))
        |    |    |    |    |    |    |    |    |
        |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
        |    |    |    |    |    |    |    |    |
        /---------------------------------------/
        |                   |F/S |N/S |E/W | D  |  Octet 1
        +-------------------+-------------------+
        |Longitude degrees  |Longitude degrees  |  Octet 2
        +-------------------+-------------------+
        |Longitude minutes  |Longitude minutes  |  Octet 3
        +-------------------+-------------------+
        |Longitude seconds  |Longitude seconds  |  Octet 4
        +-------------------+-------------------+
        |Latitude degrees   |Latitude degrees   |  Octet 5
        +-------------------+-------------------+
        |Latitude minutes   |Latitude minutes   |  Octet 6
        +-------------------+-------------------+
        |Latitude seconds   |Latitude seconds   |  Octet 7
        /---------------------------------------/
        Octet 1 bits 8-5 are coded as zero.
        F/S (octet 1 bit 4):
        0: Full representation
        (latitude/longitude down to seconds)
        1: Short representation
        (latitude/longitude down to minutes)
        N/S (octet 1 bit 3):
        0: Latitude value is to the SOUTH of the equator
        1: Latitude value is to the NORTH of the equator
        E/W (octet 1 bit 2):
        0: Longitude value is to the EAST of
        the prime meridian
        1: Longitude value is to the WEST of
        the prime meridian
        D (octet 1 bit 1):
        0: Longitude value less than 100 degrees
        (Actual Longitude value is the value in
        Octets 2-4)
        1: Longitude value is greater than or equal to
        100 degrees
        (Actual Longitude value is 100 added to
        the value in Octet 2-4)
        Octet 2:  Bits 8-5 Longitude degrees
        (most significant digit),
        BCD coded
        Value range: H'0-H'9
        Bits 4-1 Longitude degrees
        (least significant digit),
        BCD coded
        Value range: H'0-H'9
        Octet 3:  Bits 8-5 Longitude minutes
        (most significant digit),
        BCD coded
        Value range: H'0-H'5
        Bits 4-1 Longitude minutes
        (least significant digit),
        BCD coded
        Value range: H'0-H'9
        Octet 4:  Bits 8-5 Longitude seconds
        (most significant digit),
        BCD coded
        Value range: H'0-H'5
        Bits 4-1 Longitude seconds
        (least significant digit),
        BCD coded
        Value range: H'0-H'9
        Octet 5:  Bits 8-5 Latitude degrees
        (most significant digit),
        BCD coded
        Value range: H'0-H'9
        Bits 4-1 Latitude degrees
        (least significant digit),
        BCD coded
        Value range: H'0-H'9
        Octet 6:  Bits 8-5 Latitude minutes
        (most significant digit),
        BCD coded
        Value range: H'0-H'5
        Bits 4-1 Latitude minutes
        (least significant digit),
        BCD coded
        Value range: H'0-H'9
        Octet 7:  Bits 8-5 Latitude seconds
        (most significant digit),
        BCD coded
        Value range: H'0-H'5
        Bits 4-1 Latitude seconds
        (least significant digit),
        BCD coded
        Value range: H'0-H'9
    """


class UserToUserService1Information(primitives.AddressString):
    """ASN.1 Formal Description
    UserToUserService1Information ::= OCTET STRING (SIZE(1))
    |    |    |    |    |    |    |    |    |
    |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
    |    |    |    |    |    |    |    |    |
    /---------------------------------------/
    |                                       |  Octet 1
    /---------------------------------------/
    Bit 1:
    Attempt to use User to User Service 1 at call set up
    0 = was not made
    1 = was made
    Bit 2:
    Request to use User to User Service 1 at call set up
    0 = was implicit
    1 = was explicit
    Bit 3:
    Attempt to use User to User Service 1 at call set up
    0 = was successful
    1 = was not successful
    Bit 4:
    Attempt to use User to User Service 1 at call clear
    0 = was not made
    1 = was made
    Bit 5:
    Request to use User to User Service 1 at call clear
    0 = was implicit
    1 = was explicit
    Bit 6:
    Attempt to use User to User Service 1 at call clear
    0 = was not successful
    1 = was successful
    Bit 7 - 8 Spare (set to 0)
    """
