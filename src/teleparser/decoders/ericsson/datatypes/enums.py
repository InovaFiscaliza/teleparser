from . import primitives


class AirInterfaceUserRate(primitives.ByteEnum):
    """ASN.1 Formal Description
    AirInterfaceUserRate ::= ENUMERATED
    (aIUR9600bps                  (1),
    aIUR14400bps                 (2),
    aIUR19200bps                 (3),
    aIUR28800bps                 (5),
    aIUR38400bps                 (6),
    aIUR43200bps                 (7),
    aIUR57600bps                 (8),
    aIUR38400bps1                (9),
    aIUR38400bps2                (10),
    aIUR38400bps3                (11),
    aIUR38400bps4                (12))
    Note: Values 9 - 12 mean that the network has interpreted
    AirInterfaceUserRate as 38400 bits/s.
    """

    VALUES = {
        1: "aIUR9600bps",
        2: "aIUR14400bps",
        3: "aIUR19200bps",
        5: "aIUR28800bps",
        6: "aIUR38400bps",
        7: "aIUR43200bps",
        8: "aIUR57600bps",
        9: "aIUR38400bps1",
        10: "aIUR38400bps2",
        11: "aIUR38400bps3",
        12: "aIUR38400bps4",
    }


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


class BearerServiceCode(primitives.ByteEnum):
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

    VALUES = {
        16: "All data Circuit Data Asynchronous (CDA) Services",
        17: "Data CDA - 300bps",
        18: "Data CDA - 1200bps",
        19: "Data CDA - 1200-75bps",
        20: "Data CDA - 2400bps",
        21: "Data CDA - 4800bps",
        22: "Data CDA - 9600bps",
        23: "General - data CDA",
        24: "All data Circuit Data Synchronous (CDS) Services",
        26: "Data CDS - 1200bps",
        28: "Data CDS - 2400bps",
        29: "Data CDS - 4800bps",
        30: "Data CDS - 9600bps",
        31: "General - data CDS",
    }


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


class CallPosition(primitives.ByteEnum):
    octets: bytes
    VALUES = {
        0: "valueUsedForAllCallsToDetermineIfOutputToTakePlace",
        1: "callHasReachedCongestionOrBusyState",
        2: "callHasOnlyReachedThroughConnection",
        3: "answerHasBeenReceived",
    }


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


class ChargedParty(primitives.ByteEnum):
    """ASN.1 Formal Description
    ChargedParty ::= ENUMERATED
    (chargingOfCallingSubscriber  (0),
    chargingOfCalledSubscriber   (1),
    noCharging                   (2))
    """

    VALUES = {
        0: "chargingOfCallingSubscriber",
        1: "chargingOfCalledSubscriber",
        2: "noCharging",
    }


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
    """Disconnecting Party

      This parameter indicates whether the call was disconnected
      due to calling party termination, called party termination
      or 'Network termination'. 'Network termination' covers
      everything that is not covered by calling party termination
      or called party termination.

      This parameter is not output in case of partial output.

    ASN.1 Formal Description
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


class EosInfo(primitives.ByteEnum):
    """ASN.1 Formal Description
    EosInfo ::= OCTET STRING (SIZE(1))
    |    |    |    |    |    |    |    |    |
    |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
    |    |    |    |    |    |    |    |    |
    /---------------------------------------/
    | MSB                               LSB |
    /---------------------------------------/
    Note: OCTET STRING is coded as an unsigned integer.
    Value range:  H'0 - H'3F
    End-of-Selection Information
    Value        Meaning
    _____        _______
    00         Free subscriber.
    01         Free subscriber. No time supervision.
    02         Free subscriber. No charging.
    03         Free subscriber. No time supervision.
    No charging.
    04         Free subscriber. Last party release.
    05         Free subscriber. No time supervision.
    Last party release.
    06         Free subscriber. No charging. Last
    party release.
    07         Free subscriber. No time supervision.
    No charging. Last party release.
    10         Set up speech condition.
    11         Set up speech condition.
    No time supervision.
    12         Set up speech condition.
    No charging.
    21         Access barred
    22         Transferred subscriber.
    23         Busy subscriber.
    24         Busy subscriber with callback protection.
    25         Unallocated number.
    26         Address incomplete.
    27         Call transfer protection, that is
    "follow me" not allowed to this subscriber.
    28         Subscriber line out of order.
    29         Intercepted subscriber.
    2A         Supervised by an operator.
    Trunk offering marked.
    2B         Rerouting to service centre.
    2C         Line lock out.
    2D         Send acceptance tone.
    2E         No answer/incompatible destination
    (used for ISDN).
    2F         Send refusal tone. Only used
    at subscriber services.
    33         Digital path not provided.
    34         Congestion without differentiation.
    35         Time release.
    36         Technical fault.
    37         Congestion in group selection
    network.
    38         Lack of devices.
    39         Congestion in subscriber
    selection network.
    3A         Congestion in international
    network.
    3B         Congestion in national network.
    3C         Conditional congestion (Region option).
    3D         Route congestion.
    3E         Unpermitted traffic case.
    3F         No acknowledgement from mobile subscriber.
    """

    VALUES = {
        0: "Free subscriber.",
        1: "Free subscriber. No time supervision.",
        2: "Free subscriber. No charging.",
        3: "Free subscriber. No time supervision. No charging.",
        4: "Free subscriber. Last party release.",
        5: "Free subscriber. No time supervision. Last party release.",
        6: "Free subscriber. No charging. Last party release.",
        7: "Free subscriber. No time supervision. No charging. Last party release.",
        16: "Set up speech condition.",
        17: "Set up speech condition. No time supervision.",
        18: "Set up speech condition. No charging.",
        33: "Access barred",
        34: "Transferred subscriber.",
        35: "Busy subscriber.",
        36: "Busy subscriber with callback protection.",
        37: "Unallocated number.",
        38: "Address incomplete.",
        39: 'Call transfer protection, that is "follow me" not allowed to this subscriber.',
        40: "Subscriber line out of order.",
        41: "Intercepted subscriber.",
        42: "Supervised by an operator. Trunk offering marked.",
        43: "Rerouting to service centre.",
        44: "Line lock out.",
        45: "Send acceptance tone.",
        46: "No answer/incompatible destination (used for ISDN).",
        47: "Send refusal tone. Only used at subscriber services.",
        51: "Digital path not provided.",
        52: "Congestion without differentiation.",
        53: "Time release.",
        54: "Technical fault.",
        55: "Congestion in group selection network.",
        56: "Lack of devices.",
        57: "Congestion in subscriber selection network.",
        58: "Congestion in international network.",
        59: "Congestion in national network.",
        60: "Conditional congestion (Region option).",
        61: "Route congestion.",
        62: "Unpermitted traffic case.",
        63: "No acknowledgement from mobile subscriber.",
    }


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
    }


class INMarkingOfMS(primitives.ByteEnum):
    """ASN.1 Formal Description
    INMarkingOfMS ::= ENUMERATED
    (originatingINService                                 (1),
    terminatingINService                                 (2),
    originatingINCategoryKeyService                      (3),
    terminatingINCategoryKeyService                      (4),
    originatingCAMELService                              (5),
    terminatingCAMELService                              (6),
    originatingExtendedCAMELServiceWithINCapabilityIndicator
    (7),
    terminatingExtendedCAMELServiceWithINCapabilityIndicator
    (8),
    originatingExtendedCAMELServiceWithOriginatingINCategoryKey
    (9),
    terminatingExtendedCAMELServiceWithTerminatingINCategoryKey
    (10),
    subscriberDialledCAMELService                       (11),
    subscriberDialledCAMELServiceAndOriginatingCAMELService
    (12),
    visitedTerminatingCAMELService                      (13))
    """

    VALUES = {
        1: "originatingINService",
        2: "terminatingINService",
        3: "originatingINCategoryKeyService",
        4: "terminatingINCategoryKeyService",
        5: "originatingCAMELService",
        6: "terminatingCAMELService",
        7: "originatingExtendedCAMELServiceWithINCapabilityIndicator ",
        8: "terminatingExtendedCAMELServiceWithINCapabilityIndicator",
        9: "originatingExtendedCAMELServiceWithOriginatingINCategoryKey",
        10: "terminatingExtendedCAMELServiceWithTerminatingINCategoryKey",
        11: "subscriberDialledCAMELService",
        12: "subscriberDialledCAMELServiceAndOriginatingCAMELService",
        13: "visitedTerminatingCAMELService",
    }


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


class MobileUserClass1(primitives.ByteEnum):
    """Mobile User Class 1

      This parameter contains Mobile system supplementary
      user type 1, obtained from Additional User Category
      (AUC) parameter in ISUP.

      It is used to indicate service related information
      in the originating side of the call, for example
      cellular telephone service.

      The parameter is only applicable for WCDMA Japan.

    ASN.1 Formal Description
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

    VALUES = {
        0: "Spare",
        1: "Cellular Telephone Service",
        2: "Maritime Telephone Service",
        3: "Airplane Telephone Service",
        4: "Paging Service",
        5: "PHS service",
    }

    @property
    def value(self):
        number = self.octets[0]
        return "Spare" if 6 <= number <= 255 else self.VALUES[number]


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


class OptimalRoutingType(primitives.ByteEnum):
    """ASN.1 Formal Description
    OptimalRoutingType ::= ENUMERATED
    (optimalRoutingAtLateCallForwarding    (0))
    """

    VALUES = {
        0: "optimalRoutingAtLateCallForwarding",
    }


class OriginatedCode(primitives.ByteEnum):
    """Originated Code

      This parameter indicates from where the call is originated.
      This field is output only for ISOCODE or PACKED
      postprocessing purposes.

      The parameter is not applicable for WCDMA Japan.

    ASN.1 Formal Description
        OriginatedCode ::= ENUMERATED
        (callOriginatingFromOwnSubscriberInSSN             (0),
        callOriginatingFromOwnSubscriberInGSN             (1),
        callOriginatingFromIncomingTrunk                  (2),
        callOriginatingFromSUSblock                       (3),
        callOriginatingFromOMSblock                       (4),
        testCallTowardsIL-OL-BL                           (5),
        testCallWithIndividualSelectionOfB-Subscriber     (6),
        testCallWithIndividualSelectionExceptB-Subscriber (7),
        testCallWithSelectionInSpecifiedRoute             (8),
        operator                                          (9))
    """

    VALUES = {
        0: "callOriginatingFromOwnSubscriberInSSN",
        1: "callOriginatingFromOwnSubscriberInGSN",
        2: "callOriginatingFromIncomingTrunk",
        3: "callOriginatingFromSUSblock",
        4: "callOriginatingFromOMSblock",
        5: "testCallTowardsIL-OL-BL",
        6: "testCallWithIndividualSelectionOfB-Subscriber",
        7: "testCallWithIndividualSelectionExceptB-Subscriber",
        8: "testCallWithSelectionInSpecifiedRoute",
        9: "operator",
    }


class OriginatingLineInformation(primitives.ByteEnum):
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
      assigned for the GMSC service area.

    ASN.1 Formal Description
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

    VALUES = {
        0: "Identified Line - no special treatment",
        2: "Automatic Number Identification (ANI) failure",
        61: "Traffic originating from cellular carrier over Type 1 connection to Inter-exchange Carrier (IXC) or International Exchange Carrier (INC).",
        62: """Traffic originating from cellular
                    carrier over Type 2 connection to
                    IXC or INC.
                    Charge Number is the subscriber number
                    (callingPartyNumber or last
                    redirectingNumber).""",
        63: """Traffic originating from cellular
                    carrier over Type 2 connection to
                    IXC or INC, roaming forwarding call.
                    Charge Number is the subscriber number
                    of called mobile subscriber.""",
    }


class OutputForSubscriber(primitives.ByteEnum):
    """Output for Subscriber

      This parameter indicates if the ICI output was made
      for the calling subscriber or called subscriber.

      This parameter is available only in ICI records.
    ASN.1 Formal Description
        OutputForSubscriber ::= ENUMERATED
        (callingParty           (0),
        calledParty            (1),
        callingAndCalledParty  (2))
    """

    VALUES = {
        0: "callingParty",
        1: "calledParty",
        2: "callingAndCalledParty",
    }


class OutputType(primitives.ByteEnum):
    """Output Type

      This field is used internally for Adjunc Processor(AP)
      output.

    ASN.1 Formal Description
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


class TariffSwitchInd(primitives.ByteEnum):
    """ASN.1 Formal Description
    TariffSwitchInd ::= ENUMERATED
    (noTariffSwitch                    (0),
    tariffSwitchAfterStartOfCharging  (2))
    """

    VALUES = {
        0: "noTariffSwitch",
        2: "tariffSwitchAfterStartOfCharging",
    }


class TeleServiceCode(primitives.ByteEnum):
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

    VALUES = {
        17: "Telephony",
        18: "Emergency calls",
        33: "Short Message MT-PP",
        34: "Short Message MO-PP",
        97: "Facsimile group3 and alter speech",
        98: "Automatic facsimile group3",
        208: "All PLMN specific TS",
        209: "PLMN specific TS - 1",
        210: "PLMN specific TS - 2",
        211: "PLMN specific TS - 3",
        212: "PLMN specific TS - 4",
        213: "PLMN specific TS - 5",
        214: "PLMN specific TS - 6",
        215: "PLMN specific TS - 7",
        216: "PLMN specific TS - 8",
        217: "PLMN specific TS - 9",
        218: "PLMN specific TS - A",
        219: "PLMN specific TS - B",
        220: "PLMN specific TS - C",
        221: "PLMN specific TS - D",
        222: "PLMN specific TS - E",
        223: "PLMN specific TS - F",
    }


class TrafficClass(primitives.ByteEnum):
    """ASN.1 Formal Description
    TrafficClass ::= OCTET STRING (SIZE(1))
    |    |    |    |    |    |    |    |    |
    |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
    |    |    |    |    |    |    |    |    |
    /---------------------------------------/
    |                                       | octet 1
    /---------------------------------------/
    TrafficClass             Bits 8 7 6 5 4 3 2 1
    Conversational Class          0 0 0 0 0 0 0 0
    Streaming Class               0 0 0 0 0 0 0 1
    Interactive Class             0 0 0 0 0 0 1 0
    Background Class              0 0 0 0 0 0 1 1
    """

    VALUES = {
        0: "Conversational Class",
        1: "Streaming Class",
        2: "Interactive Class",
        3: "Background Class",
    }


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


class UserClass(primitives.ByteEnum):
    """User Class

      This parameter is mapped from the Additional Fixed
      User Information in Additional User Category (AUC)
      parameter in ISUP message IAM received from
      the originating network.

      User class specifies the type of phone used on
      the originating side of the call from the fixed
      network. Values can be set to for example
      'train pay phone' or 'pink' (non-NTT payphone).

      This parameter is used in connection with Type of
      Calling Subscriber for the Flexible Charging function.

      The parameter is only applicable for WCDMA Japan.

    ASN.1 Formal Description
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

    VALUES = {
        0: "Spare",
        1: "Train Payphone",
        2: "Pink (non-NTT Payphone)",
        3: "Spare",
    }

    @property
    def value(self):
        self.additional_info = self.VALUES[self.octets[0] & 3]
        self.spare = self.octets[0] >> 2
        return self.spare, self.additional_info

    def __str__(self):
        return f"Spare: {self.spare}, Additional Info: {self.additional_info}"


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
