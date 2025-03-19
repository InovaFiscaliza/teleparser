from teleparser.decoders.ericsson.datatypes import primitives


class AccountCode:
    """ASN.1 Formal Description
    AccountCode ::= TBCDString (SIZE(1..5))
    Note: Only decimal digits are used.
    """


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


class ApplicationIdentifier(primitives.AddressString):
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


class AsyncSyncIndicator(primitives.ByteEnum):
    """ASN.1 Formal Description
    AsyncSyncIndicator ::= ENUMERATED
    (syncData        (0),
    asyncData       (1))
    """

    VALUES = {
        0: "syncData",
        1: "asyncData",
    }


class BearerServiceCode(primitives.AddressString):
    """ASN.1 Formal Description
    BearerServiceCode ::= OCTET STRING (SIZE(1))
    |    |    |    |    |    |    |    |    |
    |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
    |    |    |    |    |    |    |    |    |
    /---------------------------------------/
    |                                       |
    /---------------------------------------/
    -  PLMN-specific bearer services:
    Bits 87654321 are defined by the Home Public Land
    Mobile Network (HPLMN) operator.
    -  Rest of  bearer services:
    bit 8: 0 (unused)
    BearerService                 Bits  8 7 6 5 4 3 2 1
    All data Circuit Data
    Asynchronous (CDA) Services         0 0 0 1 0 0 0 0
    Data CDA - 300bps                   0 0 0 1 0 0 0 1
    Data CDA - 1200bps                  0 0 0 1 0 0 1 0
    Data CDA - 1200-75bps               0 0 0 1 0 0 1 1
    Data CDA - 2400bps                  0 0 0 1 0 1 0 0
    Data CDA - 4800bps                  0 0 0 1 0 1 0 1
    Data CDA - 9600bps                  0 0 0 1 0 1 1 0
    General - data CDA                  0 0 0 1 0 1 1 1
    All data Circuit Data
    Synchronous (CDS) Services          0 0 0 1 1 0 0 0
    Data CDS - 1200bps                  0 0 0 1 1 0 1 0
    Data CDS - 2400bps                  0 0 0 1 1 1 0 0
    Data CDS - 4800bps                  0 0 0 1 1 1 0 1
    Data CDS - 9600bps                  0 0 0 1 1 1 1 0
    General - data CDS                  0 0 0 1 1 1 1 1
    Note: Only the values for 'General - data CDA'
    and  'General - data CDS' are output in
    case of an WCDMA call
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


class BSSMAPCauseCode(primitives.AddressString):
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


class CallAttemptState(primitives.ByteEnum):
    """ASN.1 Formal Description
    CallAttemptState ::= ENUMERATED
    (initialState           (0),
    callSentState          (1),
    callRejectedState      (2),
    callOfferedState       (3),
    noResponseState        (4),
    alertingState          (5),
    unknownCallState       (6),
    callActiveState        (7))
    """

    VALUES = {
        0: "initialState",
        1: "callSentState",
        2: "callRejectedState",
        3: "callOfferedState",
        4: "noResponseState",
        5: "alertingState",
        6: "unknownCallState",
        7: "callActiveState",
    }


class CAMELTDPData:
    """ASN.1 Formal Description
    CAMELTDPData ::= SEQUENCE(
    serviceKey     (0) IMPLICIT  ServiceKey,
    gsmSCFAddress  (1) IMPLICIT  AddressString (SIZE (1..9)))
    """


class CarrierIdentificationCode:
    """ASN.1 Formal Description
    CarrierIdentificationCode ::= TBCDString (SIZE(1..3))
    """


class CarrierInfo(primitives.AddressString):
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


class ChangeInitiatingParty(primitives.ByteEnum):
    """ASN.1 Formal Description
    ChangeInitiatingParty ::= ENUMERATED
    (userInitiated                  (0),
    networkInitiated               (1))
    """

    VALUES = {
        0: "userInitiated",
        1: "networkInitiated",
    }


class ChannelAllocationPriorityLevel(primitives.AddressString):
    """ASN.1 Formal Description
    ChannelAllocationPriorityLevel ::= OCTET STRING (SIZE(1))
    |   |   |   |   |   |   |   |   |
    | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 |
    |   |   |   |   |   |   |   |   |
    /-------------------------------/
    |MSB                         LSB| Octet 1
    /-------------------------------/
    - Bits 8-7:  Spare
    - Bits 6-3:  Priority Level
    0000  Spare
    0001  Priority level 1 = highest priority
    0010  Priority level 2 = second-highest priority
    0011  Priority level 3 = third-highest priority
    .
    .
    .
    1110  Priority level 14 = lowest priority
    1111  Priority level not used
    - Bits 2-1:  Spare
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
    """ASN.1 Formal Description
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


class ChargingCase(primitives.AddressString):
    """ASN.1 Formal Description
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


class ChargingIndicator(primitives.AddressString):
    """ASN.1 Formal Description
    ChargingIndicator ::= OCTET STRING (SIZE(1))
    |    |    |    |    |    |    |    |    |
    |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
    |    |    |    |    |    |    |    |    |
    /---------------------------------------/
    | MSB                               LSB |
    /---------------------------------------/
    - Bit 8-3: Unused, set always to 00000
    - Bit 2-1: Charging indicator
    00   No Indication
    01   No Charge
    10   Charge
    11   Spare
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
    """ASN.1 Formal Description
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


class CRIIndicator(primitives.ByteEnum):
    """ASN.1 Formal Description
    CRIIndicator ::= ENUMERATED
    (chargeRateInformationAcknowledged       (1),
    chargeRateInformationNotAcknowledged    (2))
    """

    VALUES = {
        1: "chargeRateInformationAcknowledged",
        2: "chargeRateInformationNotAcknowledged",
    }


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


class CUGIndex(primitives.AddressString):
    """ASN.1 Formal Description
    CUGIndex ::= OCTET STRING (SIZE(2))
    |    |    |    |    |    |    |    |    |
    |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
    |    |    |    |    |    |    |    |    |
    /---------------------------------------/
    | MSB                                   |  octet 1
    +---------------------------------------+
    |                                    LSB|  octet 2
    /---------------------------------------/
    Note: The OCTET STRING is coded as an unsigned integer.
    Value range:  H'0 - H'7FFF
    """


class CUGInterlockCode(primitives.AddressString):
    """ASN.1 Formal Description
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


class C7ChargingMessage(primitives.AddressString):
    """ASN.1 Formal Description
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


class C7CHTMessage(primitives.AddressString):
    """ASN.1 Formal Description
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


class DefaultCallHandling(primitives.ByteEnum):
    """ASN.1 Formal Description
    DefaultCallHandling ::= ENUMERATED
    (continueCall                    (0),
    releaseCall                     (1))
    """

    VALUES = {
        0: "continueCall",
        1: "releaseCall",
    }


class DefaultSMSHandling(primitives.ByteEnum):
    """ASN.1 Formal Description
    DefaultSMS-Handling ::= ENUMERATED
    (continueTransaction             (0),
    releaseTransaction              (1))
    """

    VALUES = {
        0: "continueTransaction",
        1: "releaseTransaction",
    }


class DeliveryOfErroneousSDU(primitives.ByteEnum):
    """ASN.1 Formal Description
    DeliveryOfErroneousSDU ::= ENUMERATED
    (yes                              (0),
    no                               (1),
    noErrorDetectionConsideration    (2))
    """

    VALUES = {
        0: "yes",
        1: "no",
        2: "noErrorDetectionConsideration",
    }


class DisconnectingParty(primitives.ByteEnum):
    """ASN.1 Formal Description
    DisconnectingParty ::= ENUMERATED
    (callingPartyRelease          (0),
    calledPartyRelease           (1),
    networkRelease               (2))
    """

    VALUES = {
        0: "callingPartyRelease",
        1: "calledPartyRelease",
        2: "networkRelease",
    }


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


class EMLPPPriorityLevel(primitives.AddressString):
    """ASN.1 Formal Description
    EMLPPPriorityLevel ::= OCTET STRING (SIZE(1))
    |    |    |    |    |    |    |    |    |
    |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
    |    |    |    |    |    |    |    |    |
    /---------------------------------------/
    |MSB                                 LSB|  Octet 1
    /---------------------------------------/
    Bits 8-4:   Not used
    Bits 3-1:   Priority Level
    000  Spare
    001  Priority level 4 = lowest priority for
    subscription
    010  Priority level 3 = sixth highest priority
    011  Priority level 2 = fifth highest priority
    100  Priority level 1 = fourth highest priority
    101  Priority level 0 = third highest priority
    110  Priority level B = second highest priority
    111  Priority level A = highest priority for
    subscription
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


class ExchangeIdentity:
    """ASN.1 Formal Description
    ExchangeIdentity ::= IA5STRING (SIZE(1..15))
    |    |    |    |    |    |    |    |    |
    |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
    |    |    |    |    |    |    |    |    |
    /---------------------------------------/
    |  1st character                        | octet 1
    /---------------------------------------/
    .
    .
    .
    /---------------------------------------/
    |  14th character                       | octet 14
    +---------------------------------------+
    |  15th character                       | octet 15
    /---------------------------------------/
    """


class FirstRadioChannelUsed(primitives.ByteEnum):
    """ASN.1 Formal Description
    FirstRadioChannelUsed ::= ENUMERATED
    (fullRateChannel               (0),
    halfRateChannel               (1))
    """

    VALUES = {
        0: "fullRateChannel",
        1: "halfRateChannel",
    }


class FixedNetworkUserRate(primitives.ByteEnum):
    """ASN.1 Formal Description
    FixedNetworkUserRate ::= ENUMERATED
    (fNUR9600bps                  (1),
    fNUR14400bps                 (2),
    fNUR19200bps                 (3),
    fNUR28800bps                 (4),
    fNUR38400bps                 (5),
    fNUR48000bps                 (6),
    fNUR56000bps                 (7),
    fNUR64000bps                 (8),
    fNURautobauding              (9))
    Note: Value (6) is only valid for GSM.
    """

    VALUES = {
        1: "fNUR9600bps",
        2: "fNUR14400bps",
        3: "fNUR19200bps",
        4: "fNUR28800bps",
        5: "fNUR38400bps",
        6: "fNUR48000bps",
        7: "fNUR56000bps",
        8: "fNUR64000bps",
        9: "fNURautobauding",
        9: "fNURautobauding",
    }


class FreeFormatData(primitives.AddressString):
    """ASN.1 Formal Description
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


class FrequencyBandSupported(primitives.AddressString):
    """ASN.1 Formal Description
    FrequencyBandSupported ::= OCTET STRING (SIZE(1))
    |    |    |    |    |    |    |    |    |
    |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
    |    |    |    |    |    |    |    |    |
    /---------------------------------------/
    |                                       |
    /---------------------------------------/
    Value range: H'0 - H'07
    Bit assignment:
    Bit 1: Frequency Band 1 (P-GSM)
    Bit 2: Frequency Band 2 (E-GSM)
    Bit 3: Frequency Band 3 (GSM 1800)
    Bits 4-8: Spare
    Bit values:
    0: Frequency Band not supported
    1: Frequency Band supported
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


class GlobalTitle(primitives.AddressString):
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


class GlobalTitleAndSubSystemNumber(primitives.AddressString):
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


class IMEI:
    """ASN.1 Formal Description
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


class INServiceTrigger(primitives.AddressString):
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


class IntermediateRate(primitives.ByteEnum):
    """ASN.1 Formal Description
    IntermediateRate ::= ENUMERATED
    (rate8KbitPerSecondUsed           (2),
    rate16KbitPerSecondUsed          (3))
    """

    VALUES = {
        2: "rate8KbitPerSecondUsed",
        3: "rate16KbitPerSecondUsed",
    }


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


class LCSClientType(primitives.ByteEnum):
    """ASN.1 Formal Description
    LCSClientType ::= ENUMERATED
    (emergencyServices                  (0),
    valueAddedServices                 (1),
    plmnOperatorServices               (2),
    lawfulInterceptServices            (3))
    """

    VALUES = {
        0: "emergencyServices",
        1: "valueAddedServices",
        2: "plmnOperatorServices",
        3: "lawfulInterceptServices",
    }


class LegID(primitives.AddressString):
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


class LocationInformation(primitives.AddressString):
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


class MessageTypeIndicator(primitives.ByteEnum):
    """ASN.1 Formal Description
    MessageTypeIndicator ::= ENUMERATED
    (sMSdeliverSCtoMS         (0),
    sMSdeliveReportMStoSC    (1),
    sMSstatusReportSCtoMS    (2),
    sMScommanMStoSC          (3),
    sMSsubmitMStoSC          (4),
    sMSsubmitReportSCtoMS    (5))
    """

    VALUES = {
        0: "sMSdeliverSCtoMS",
        1: "sMSdeliveReportMStoSC",
        2: "sMSstatusReportSCtoMS",
        3: "sMScommanMStoSC",
        4: "sMSsubmitMStoSC",
        5: "sMSsubmitReportSCtoMS",
    }


class MobileUserClass1(primitives.AddressString):
    """ASN.1 Formal Description
    MobileUserClass1 ::= OCTET STRING (SIZE(1))
    |    |    |    |    |    |    |    |    |
    |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
    |    |    |    |    |    |    |    |    |
    /---------------------------------------/
    | MSB                               LSB |
    /---------------------------------------/
    Additional Mobile Service Information Type 1,
    service related information
    00000000 Spare
    00000001 Cellular Telephone Service
    00000010 Maritime Telephone Service
    00000011 Airplane Telephone Service
    00000100 Paging Service
    00000101 PHS service
    00000110
    to       Spare
    11111111
    """


class MobileUserClass2(primitives.AddressString):
    """ASN.1 Formal Description
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


class MultimediaInformation:
    """ASN.1 Formal Description
    MultimediaInformation ::= SEQUENCE(
    userRate                  (0) IMPLICIT UserRate
    OPTIONAL,
    asyncSyncIndicator        (1) IMPLICIT AsyncSyncIndicator
    OPTIONAL,
    uILayer1Protocol          (2) IMPLICIT UILayer1Protocol)
    """


class MSNB:
    """ASN.1 Formal Description
    MSNB ::= TBCDString (SIZE(3..8))
    """


class NumberOfChannels(primitives.ByteEnum):
    """ASN.1 Formal Description
    NumberOfChannels ::= ENUMERATED
    (oneTrafficChannel         (0),
    twoTrafficChannels        (1),
    threeTrafficChannels      (2),
    fourTrafficChannels       (3),
    fiveTrafficChannels       (4),
    sixTrafficChannels        (5),
    sevenTrafficChannels      (6),
    eightTrafficChannels      (7))
    """

    VALUES = {
        0: "oneTrafficChannel",
        1: "twoTrafficChannels",
        2: "threeTrafficChannels",
        3: "fourTrafficChannels",
        4: "fiveTrafficChannels",
        5: "sixTrafficChannels",
        6: "sevenTrafficChannels",
        7: "eightTrafficChannels",
    }


class NumberOfOperations(primitives.AddressString):
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


class NumberOfShortMessage(primitives.AddressString):
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


class OptimalRoutingType(primitives.ByteEnum):
    """ASN.1 Formal Description
    OptimalRoutingType ::= ENUMERATED
    (optimalRoutingAtLateCallForwarding    (0))
    """

    VALUES = {
        0: "optimalRoutingAtLateCallForwarding",
    }


class OriginatingLineInformation(primitives.AddressString):
    """ASN.1 Formal Description
    OriginatingLineInformation ::= OCTET STRING (SIZE(1))
    |   |   |   |   |   |   |   |   |
    | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 |
    |   |   |   |   |   |   |   |   |
    /-------------------------------/
    |MSB                         LSB|
    /-------------------------------/
    Note: The OCTET STRING is coded as an unsigned INTEGER.
    Value        Meaning
    _____        _______
    H'00         Identified Line - no special treatment
    H'02         Automatic Number Identification (ANI) failure
    H'3D         Traffic originating from cellular
    carrier over Type 1 connection to
    Inter-exchange Carrier (IXC) or
    International Exchange Carrier (INC).
    Charge Number is the switch identity.
    H'3E         Traffic originating from cellular
    carrier over Type 2 connection to
    IXC or INC.
    Charge Number is the subscriber number
    (callingPartyNumber or last
    redirectingNumber).
    H'3F         Traffic originating from cellular
    carrier over Type 2 connection to
    IXC or INC, roaming forwarding call.
    Charge Number is the subscriber number
    of called mobile subscriber.
    """


class OutputType(primitives.ByteEnum):
    """ASN.1 Formal Description
    OutputType ::= ENUMERATED
    (noOutput                                (0),
    iCIoutputForCallingSubscriber           (1),
    iCIOutputForCalledSubscriber            (2),
    iCIOutputForCallingAndCalledSubscribers (3),
    tTOutputOnly                            (4),
    tTAndICIForCallingSubscriber            (5),
    tTAndICIForCalledSubscriber             (6),
    tTAndICIForCallingAndCalledSubscribers  (7))
    """

    VALUES = {
        0: "noOutput",
        1: "iCIoutputForCallingSubscriber",
        2: "iCIOutputForCalledSubscriber",
        3: "iCIOutputForCallingAndCalledSubscribers",
        4: "tTOutputOnly",
        5: "tTAndICIForCallingSubscriber",
        6: "tTAndICIForCalledSubscriber",
        7: "tTAndICIForCallingAndCalledSubscribers",
    }


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


class PointCodeAndSubSystemNumber(primitives.AddressString):
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


class PositionAccuracy(primitives.AddressString):
    """ASN.1 Formal Description
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


class PresentationAndScreeningIndicator(primitives.AddressString):
    """ASN.1 Formal Description
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


class ProcedureCode:
    """ASN.1 Formal Description
    ProcedureCode ::= TBCDString (SIZE(1))
    """


class RadioChannelProperty(primitives.ByteEnum):
    """ASN.1 Formal Description
    RadioChannelProperty ::= ENUMERATED
    (halfRateChannel                            (0),
    fullRateChannel                            (1),
    dualRateHalfRatePreferred                  (2),
    dualRateFullRatePreferred                  (3),
    twoFullRateChannels                        (4),
    threeFullRateChannels                      (5),
    fourFullRateChannels                       (6),
    twoAssignedAirTimeSlots                    (7),
    fourAssignedAirTimeSlots                   (8),
    sixAssignedAirTimeSlots                    (9),
    eightAssignedAirTimeSlots                 (10),
    twelveAssignedAirTimeSlots                (11),
    sixteenAssignedAirtimeSlots               (12),
    twoDownlinkOneUplinkAssignedAirTimeSlots  (13),
    fourDownlinkOneUplinkAssignedAirTimeSlots (14))
    Note: Values 7-14 are specified only for global satellite
    system and used only by GSM.
    """

    VALUES = {
        0: "halfRateChannel",
        1: "fullRateChannel",
        2: "dualRateHalfRatePreferred",
        3: "dualRateFullRatePreferred",
        4: "twoFullRateChannels",
        5: "threeFullRateChannels",
        6: "fourFullRateChannels",
        7: "twoAssignedAirTimeSlots",
        8: "fourAssignedAirTimeSlots",
        9: "sixAssignedAirTimeSlots",
        10: "eightAssignedAirTimeSlots",
        11: "twelveAssignedAirTimeSlots",
        12: "sixteenAssignedAirtimeSlots",
        13: "twoDownlinkOneUplinkAssignedAirTimeSlots",
        14: "fourDownlinkOneUplinkAssignedAirTimeSlots",
    }


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


class RegionalServiceUsed(primitives.ByteEnum):
    """ASN.1 Formal Description
    RegionalServiceUsed ::= ENUMERATED
    (localSubscription                                  (0),
    regionalSubcription                                (1),
    subscriptionWithTariffAreas                        (2),
    regionalSubcriptionAndSubscriptionWithTariffAreas  (3))
    """

    VALUES = {
        0: "localSubscription",
        1: "regionalSubcription",
        2: "subscriptionWithTariffAreas",
        3: "regionalSubcriptionAndSubscriptionWithTariffAreas",
    }


class ResponseTimeCategory(primitives.ByteEnum):
    """ASN.1 Formal Description
    ResponseTimeCategory ::= ENUMERATED
    (lowdelay       (0),
    delaytolerant  (1))
    """

    VALUES = {
        0: "lowdelay",
        1: "delaytolerant",
    }


class Route:
    """ASN.1 Formal Description
    Route ::= IA5STRING (SIZE(1..7))
    |    |    |    |    |    |    |    |    |
    |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
    |    |    |    |    |    |    |    |    |
    /---------------------------------------/
    |            1st character              | octet 1
    /---------------------------------------/
    .
    .
    .
    /---------------------------------------/
    |            6th character              | octet 6
    +---------------------------------------+
    |            7th character              | octet 7
    /---------------------------------------/
    """


class SelectedCodec(primitives.ByteEnum):
    """ASN.1 Formal Description
    SelectedCodec ::= ENUMERATED
    (gSMFullRate                (0),
    gSMHalfRate                (1),
    gSMEnhancedFullRate        (2),
    fullRateAdaptiveMultiRate  (3),
    halfRateAdaptiveMultiRate  (4),
    uMTSAdaptiveMultiRate      (5),
    uMTSAdaptiveMultiRate2     (6),
    tDMAEnhancedFullRate       (7),
    pDCEnhancedFullRate        (8),
    inmarsatCoding            (15))
    Note: Only value 15 is used.
    """

    VALUES = {
        0: "gSMFullRate",
        1: "gSMHalfRate",
        2: "gSMEnhancedFullRate",
        3: "fullRateAdaptiveMultiRate",
        4: "halfRateAdaptiveMultiRate",
        5: "uMTSAdaptiveMultiRate",
        6: "uMTSAdaptiveMultiRate2",
        7: "tDMAEnhancedFullRate",
        8: "pDCEnhancedFullRate",
        15: "inmarsatCoding",
    }


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


class ServiceSwitchingType(primitives.ByteEnum):
    """ASN.1 Formal Description
    ServiceSwitchingType ::= ENUMERATED
    (speechToFax       (0),
    faxToSpeech       (1))
    """

    VALUES = {
        0: "speechToFax",
        1: "faxToSpeech",
    }


class Single(primitives.ByteEnum):
    """ASN.1 Formal Description
    Single ::=  ENUMERATED
    (aPartyToBeCharged      (0),
    bPartyToBeCharged      (1),
    cPartyToBeCharged      (2),
    otherPartyToBeCharged  (3))
    """

    VALUES = {
        0: "aPartyToBeCharged",
        1: "bPartyToBeCharged",
        2: "cPartyToBeCharged",
        3: "otherPartyToBeCharged",
    }


class SMSResult(primitives.ByteEnum):
    """ASN.1 Formal Description
    SMSResult ::= ENUMERATED
    (unsuccessfulMOSMSDeliverytoSMSCDuetoCAMELReason  (0),
    unsuccessfulMOSMSDeliverytoSMSCDuetoOtherReason  (1))
    """

    VALUES = {
        0: "unsuccessfulMOSMSDeliverytoSMSCDuetoCAMELReason",
        1: "unsuccessfulMOSMSDeliverytoSMSCDuetoOtherReason",
    }


class SpeechCoderPreferenceList(primitives.AddressString):
    """ASN.1 Formal Description
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


class SpeechCoderVersion(primitives.ByteEnum):
    """ASN.1 Formal Description
    SpeechCoderVersion ::= ENUMERATED
    (fullRateVersion1         (0),
    fullRateVersion2         (1),
    fullRateVersion3         (2),
    halfRateVersion1         (3),
    halfRateVersion2         (4),
    halfRateVersion3         (5))
    """

    VALUES = {
        0: "fullRateVersion1",
        1: "fullRateVersion2",
        2: "fullRateVersion3",
        3: "halfRateVersion1",
        4: "halfRateVersion2",
        5: "halfRateVersion3",
    }


class SSCode(primitives.AddressString):
    """ASN.1 Formal Description
    SSCode ::= OCTET STRING (SIZE(1))
    |    |    |    |    |    |    |    |    |
    |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
    |    |    |    |    |    |    |    |    |
    /---------------------------------------/
    |                                       |
    /---------------------------------------/
    SSCode                                Bits  8 7 6 5 4 3 2 1
    All Supplementary Services (SS)             0 0 0 0 0 0 0 0
    All line identification SS                  0 0 0 1 0 0 0 0
    Calling line identification presentation    0 0 0 1 0 0 0 1
    Calling line identification restriction     0 0 0 1 0 0 1 0
    Connected line identification presentation  0 0 0 1 0 0 1 1
    Connected line identification restriction   0 0 0 1 0 1 0 0
    Malicious call identification               0 0 0 1 0 1 0 1
    All forwarding SS                           0 0 1 0 0 0 0 0
    Call forwarding unconditional               0 0 1 0 0 0 0 1
    All conditional forward. serv.              0 0 1 0 1 0 0 0
    Call forwarding on mobile subscriber busy   0 0 1 0 1 0 0 1
    Call forwarding on no reply                 0 0 1 0 1 0 1 0
    Call forwarding on subscriber not reachable 0 0 1 0 1 0 1 1
    All call offering SS                        0 0 1 1 0 0 0 0
    Call transfer                               0 0 1 1 0 0 0 1
    Mobile access hunting                       0 0 1 1 0 0 1 0
    All call completion SS                      0 1 0 0 0 0 0 0
    Call waiting                                0 1 0 0 0 0 0 1
    Call hold                                   0 1 0 0 0 0 1 0
    Completion of call to busy subscribers      0 1 0 0 0 0 1 1
    All Multi-Party Services                    0 1 0 1 0 0 0 0
    Multi-Party Services                        0 1 0 1 0 0 0 1
    All community of interest SS                0 1 1 0 0 0 0 0
    All charging SS                             0 1 1 1 0 0 0 0
    Advice of charge information                0 1 1 1 0 0 0 1
    Advice of charge charging                   0 1 1 1 0 0 1 0
    All additional info transfer SS             1 0 0 0 0 0 0 0
    User to user signalling                     1 0 0 0 0 0 0 1
    All call restriction SS                     1 0 0 1 0 0 0 0
    Barring of outgoing calls                   1 0 0 1 0 0 0 1
    Barring of all outgoing calls               1 0 0 1 0 0 1 0
    Barring of outgoing international calls     1 0 0 1 0 0 1 1
    Barring of OG inter. calls except those
    directed to the home PLMN country        1 0 0 1 0 1 0 0
    Barring of incoming calls                   1 0 0 1 1 0 0 1
    Barring of all inc. calls                   1 0 0 1 1 0 1 0
    Barring of inc. calls when roaming outside
    the home PLMN country                     1 0 0 1 1 0 1 1
    All call priority SS                        1 0 1 0 0 0 0 0
    Enhanced multi-level precedence and
    pre-emption                                 1 0 1 0 0 0 0 1
    All PLMN specific SS                        1 1 1 1 0 0 0 0
    PLMN specific SS - 1                        1 1 1 1 0 0 0 1
    PLMN specific SS - 2                        1 1 1 1 0 0 1 0
    PLMN specific SS - 3                        1 1 1 1 0 0 1 1
    PLMN specific SS - 4                        1 1 1 1 0 1 0 0
    PLMN specific SS - 5                        1 1 1 1 0 1 0 1
    PLMN specific SS - 6                        1 1 1 1 0 1 1 0
    PLMN specific SS - 7                        1 1 1 1 0 1 1 1
    PLMN specific SS - 8                        1 1 1 1 1 0 0 0
    PLMN specific SS - 9                        1 1 1 1 1 0 0 1
    PLMN specific SS - A                        1 1 1 1 1 0 1 0
    PLMN specific SS - B                        1 1 1 1 1 0 1 1
    PLMN specific SS - C                        1 1 1 1 1 1 0 0
    PLMN specific SS - D                        1 1 1 1 1 1 0 1
    PLMN specific SS - E                        1 1 1 1 1 1 1 0
    PLMN specific SS - F                        1 1 1 1 1 1 1 1
    """


class SSFChargingCase(primitives.AddressString):
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


class SSRequest(primitives.ByteEnum):
    """ASN.1 Formal Description
    SSRequest ::= ENUMERATED
    (registration               (0),
    erasure                    (1),
    activation                 (2),
    deactivation               (3),
    interrogation              (4),
    invoke                     (5),
    registerPassword           (6),
    processUSSD                (7))
    """

    VALUES = {
        0: "registration",
        1: "erasure",
        2: "activation",
        3: "deactivation",
        4: "interrogation",
        5: "invoke",
        6: "registerPassword",
        7: "processUSSD",
    }


class SubscriberState(primitives.ByteEnum):
    """ASN.1 Formal Description
    SubscriberState ::= ENUMERATED
    (detached                   (0),
    attached                   (1),
    implicitDetached           (2))
    """

    VALUES = {
        0: "detached",
        1: "attached",
        2: "implicitDetached",
    }


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


class TeleServiceCode(primitives.AddressString):
    """ASN.1 Formal Description
    TeleServiceCode ::= OCTET STRING (SIZE (1))
    |    |    |    |    |    |    |    |    |
    |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
    |    |    |    |    |    |    |    |    |
    /---------------------------------------/
    |                                       |
    /---------------------------------------/
    Tele Service (TS)                Bits  8 7 6 5 4 3 2 1
    Telephony                              0 0 0 1 0 0 0 1
    Emergency calls                        0 0 0 1 0 0 1 0
    Short Message MT-PP                    0 0 1 0 0 0 0 1
    Short Message MO-PP                    0 0 1 0 0 0 1 0
    Facsimile group3 and alter speech      0 1 1 0 0 0 0 1
    Automatic facsimile group3             0 1 1 0 0 0 1 0
    All PLMN specific TS                   1 1 0 1 0 0 0 0
    PLMN specific TS - 1                   1 1 0 1 0 0 0 1
    PLMN specific TS - 2                   1 1 0 1 0 0 1 0
    PLMN specific TS - 3                   1 1 0 1 0 0 1 1
    PLMN specific TS - 4                   1 1 0 1 0 1 0 0
    PLMN specific TS - 5                   1 1 0 1 0 1 0 1
    PLMN specific TS - 6                   1 1 0 1 0 1 1 0
    PLMN specific TS - 7                   1 1 0 1 0 1 1 1
    PLMN specific TS - 8                   1 1 0 1 1 0 0 0
    PLMN specific TS - 9                   1 1 0 1 1 0 0 1
    PLMN specific TS - A                   1 1 0 1 1 0 1 0
    PLMN specific TS - B                   1 1 0 1 1 0 1 1
    PLMN specific TS - C                   1 1 0 1 1 1 0 0
    PLMN specific TS - D                   1 1 0 1 1 1 0 1
    PLMN specific TS - E                   1 1 0 1 1 1 1 0
    PLMN specific TS - F                   1 1 0 1 1 1 1 1
    Note: Short Message MT-PP is Short Message Mobile-Terminated
    Point-to-Point.
    Short Message MO-PP is Short Message Mobile-Originated
    Point-to-Point.
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


class TransparencyIndicator(primitives.ByteEnum):
    """ASN.1 Formal Description
    TransparencyIndicator ::= ENUMERATED
    (transparent                              (0),
    nonTransparent                           (1))
    """

    VALUES = {
        0: "transparent",
        1: "nonTransparent",
    }


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


class TriggerDetectionPoint(primitives.ByteEnum):
    """ASN.1 Formal Description
    TriggerDetectionPoint ::= ENUMERATED
    (originatingCallAttemptAuthorized                     (1),
    collectedInformation                                 (2),
    analyzedInformation                                  (3),
    originatingCallAttemptRouteSelectFailure             (4),
    originatingCallAttemptCalledPartyBusy                (5),
    originatingCallAttemptCalledPartyNotAnswer           (6),
    originatingCallAttemptCalledPartyAnswer              (7),
    originatingCallAttemptMid-CallEventDetected          (8),
    originatingCallAttemptCallDisconnecting              (9),
    originatingCallAttemptCallAbandon                   (10),
    terminatingCallAttemptAuthorized                    (12),
    terminatingCallAttemptCalledPartyBusy               (13),
    terminatingCallAttemptNoAnswer                      (14),
    terminatingCallAttemptAnswer                        (15),
    terminatingCallAttemptMid-CallEventDetected         (16),
    terminatingCallAttemptCallDisconnect                (17),
    terminatingCallAttemptCallAbandon                   (18),
    terminatingCallAttemptCallReAnswer                 (247),
    terminatingCallAttemptCallSuspended                (248),
    terminatingCallAttemptCalledPartyNotReachable      (249),
    terminatingCallAttemptAlerting                     (250),
    terminatingCallAttemptRouteSelectFailure           (251),
    originatingCallAttemptCalledPartyReAnswer          (252),
    originatingCallAttemptCallSuspended                (253),
    originatingCallAttemptCalledPartyNotReachable      (254),
    originatingCallAttemptAlerting                     (255))
    """

    VALUES = {
        1: "originatingCallAttemptAuthorized",
        2: "collectedInformation",
        3: "analyzedInformation",
        4: "originatingCallAttemptRouteSelectFailure",
        5: "originatingCallAttemptCalledPartyBusy",
        6: "originatingCallAttemptCalledPartyNotAnswer",
        7: "originatingCallAttemptCalledPartyAnswer",
        8: "originatingCallAttemptMid-CallEventDetected",
        9: "originatingCallAttemptCallDisconnecting",
        10: "originatingCallAttemptCallAbandon",
        12: "terminatingCallAttemptAuthorized",
        13: "terminatingCallAttemptCalledPartyBusy",
        14: "terminatingCallAttemptNoAnswer",
        15: "terminatingCallAttemptAnswer",
        16: "terminatingCallAttemptMid-CallEventDetected",
        17: "terminatingCallAttemptCallDisconnect",
        18: "terminatingCallAttemptCallAbandon",
        247: "terminatingCallAttemptCallReAnswer",
        248: "terminatingCallAttemptCallSuspended",
        249: "terminatingCallAttemptCalledPartyNotReachable",
        250: "terminatingCallAttemptAlerting",
        251: "terminatingCallAttemptRouteSelectFailure",
        252: "originatingCallAttemptCalledPartyReAnswer",
        253: "originatingCallAttemptCallSuspended",
        254: "originatingCallAttemptCalledPartyNotReachable",
        255: "originatingCallAttemptAlerting",
    }


class TypeOfCalledSubscriber(primitives.ByteEnum):
    """ASN.1 Formal Description
    TypeOfCalledSubscriber ::= ENUMERATED
    (pSTNSubscriber       (0),
    iSDNSubscriber       (1),
    unknownSubscriber    (2))
    """

    VALUES = {
        0: "pSTNSubscriber",
        1: "iSDNSubscriber",
        2: "unknownSubscriber",
    }


class TypeOfLocationRequest(primitives.ByteEnum):
    """ASN.1 Formal Description
    TypeOfLocationRequest ::= ENUMERATED
    (mT_LocationRequestCurrentLocation              (0),
    mT_LocationRequestCurrentOrLastKnownLocation   (1),
    mO_LocationRequestLocEstimateToMS              (2),
    mO_LocationRequestLocEstimateToThirdParty      (3),
    mO_LocationRequestAssistData                   (4),
    mO_LocationRequestDeciphKeys                   (5),
    nI_LocationRequest                             (6))
    Note: nI_LocationRequest is not valid for WCDMA.
    """

    VALUES = {
        0: "mT_LocationRequestCurrentLocation",
        1: "mT_LocationRequestCurrentOrLastKnownLocation",
        2: "mO_LocationRequestLocEstimateToMS",
        3: "mO_LocationRequestLocEstimateToThirdParty",
        4: "mO_LocationRequestAssistData",
        5: "mO_LocationRequestDeciphKeys",
        6: "nI_LocationRequest",
    }


class TypeOfSignalling(primitives.ByteEnum):
    """ASN.1 Formal Description
    TypeOfSignalling ::= ENUMERATED
    (iSUPIsNotAppliedAllTheWay       (0),
    iSUPIsAppliedAllTheWay          (1),
    unknownSignalling               (2))
    """

    VALUES = {
        0: "iSUPIsNotAppliedAllTheWay",
        1: "iSUPIsAppliedAllTheWay",
        2: "unknownSignalling",
    }


class UILayer1Protocol(primitives.ByteEnum):
    """ASN.1 Formal Description
    UILayer1Protocol ::= ENUMERATED
    (V110_X30                     (1),
    G711mulaw                    (2),
    G711Alaw                     (3),
    G721_32000bps_I460           (4),
    H221_H242                    (5),
    H223_H245                    (6),
    nonITU_T                     (7),
    V120                         (8),
    X31                          (9),
    vSELP_Speech                (10))
    """

    VALUES = {
        1: "V110_X30",
        2: "G711mulaw",
        3: "G711Alaw",
        4: "G721_32000bps_I460",
        5: "H221_H242",
        6: "H223_H245",
        7: "nonITU_T",
        8: "V120",
        9: "X31",
        10: "vSELP_Speech",
    }


class UnsuccessfulPositioningDataReason(primitives.ByteEnum):
    """ASN.1 Formal Description
    UnsuccessfulPositioningDataReason ::= ENUMERATED
    (systemError                           (0),
    userDeniedDueToPrivacyVerification    (1))
    """

    VALUES = {
        0: "systemError",
        1: "userDeniedDueToPrivacyVerification",
    }


class UserClass(primitives.AddressString):
    """ASN.1 Formal Description
    UserClass ::= OCTET STRING (SIZE(1))
    |    |    |    |    |    |    |    |    |
    |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
    |    |    |    |    |    |    |    |    |
    /---------------------------------------/
    | MSB                         |     LSB |
    /---------------------------------------/
    -- Bit 8-3 Spare
    -- Bit 2-1 Additional Fixed User Information,
    --         supplementary user type information
    00 Spare
    01 Train Payphone
    10 Pink (non-NTT Payphone)
    11 Spare
    """


class UserRate(primitives.ByteEnum):
    """ASN.1 Formal Description
    UserRate ::= ENUMERATED
    (uRIndNeg          (0),
    uR600bps          (1),
    uR1200bps         (2),
    uR2400bps         (3),
    uR3600bps         (4),
    uR4800bps         (5),
    uR7200bps         (6),
    uR8000bps         (7),
    uR9600bps         (8),
    uR14400bps        (9),
    uR16000bps       (10),
    uR19200bps       (11),
    uR32000bps       (12),
    uR38400bps       (13),
    uR48000bps       (14),
    uR56000bps       (15),
    uR64000bps       (16),
    uR38400bps1      (17),
    uR57600bps       (18),
    uR28800bps       (19),
    uR134-5bps       (21),
    uR100bps         (22),
    uR75bps_1200bps  (23),
    uR1200bps_75bps  (24),
    uR50bps          (25),
    uR75bps          (26),
    uR110bps         (27),
    uR150bps         (28),
    uR200bps         (29),
    uR300bps         (30),
    uR12000bps       (31))
    Note:
    The first rate of the values 23 and 24 is the transmit
    rate in the forward direction of the call. The second
    rate is the transmit rate in the backward direction of
    the call.
    Value 17 is an additional user rate for the French network.
    """

    VALUES = {
        0: "uRIndNeg",
        1: "uR600bps",
        2: "uR1200bps",
        3: "uR2400bps",
        4: "uR3600bps",
        5: "uR4800bps",
        6: "uR7200bps",
        7: "uR8000bps",
        8: "uR9600bps",
        9: "uR14400bps",
        10: "uR16000bps",
        11: "uR19200bps",
        12: "uR32000bps",
        13: "uR38400bps",
        14: "uR48000bps",
        15: "uR56000bps",
        16: "uR64000bps",
        17: "uR38400bps1",
        18: "uR57600bps",
        19: "uR28800bps",
        21: "uR134-5bps",
        22: "uR100bps",
        23: "uR75bps_1200bps",
        24: "uR1200bps_75bps",
        25: "uR50bps",
        26: "uR75bps",
        27: "uR110bps",
        28: "uR150bps",
        29: "uR200bps",
        30: "uR300bps",
        31: "uR12000bps",
    }


class UserTerminalPosition(primitives.AddressString):
    """ASN.1 Formal Description
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
