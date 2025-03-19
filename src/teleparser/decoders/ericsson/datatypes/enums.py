from . import primitives


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
