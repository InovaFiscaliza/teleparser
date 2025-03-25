from teleparser.ericsson import datatypes as dt

CAMELTDPData = {
    0: {"name": "serviceKey", "type": dt.ServiceKey},
    1: {"name": "gsmSCFAddress", "type": dt.GsmSCFAddress},
}

MultimediaInformation = {
    0: {"name": "userRate", "type": dt.UserRate},
    1: {"name": "asyncSyncIndicator", "type": dt.AsyncSyncIndicator},
    2: {"name": "uILayer1Protocol", "type": dt.UILayer1Protocol},
}

Transit = {
    0: {"name": "tAC", "type": dt.TAC},
    1: {"name": "callIdentificationNumber", "type": dt.CallIDNumber},
    2: {"name": "recordSequenceNumber", "type": dt.RecordSequenceNumber},
    3: {"name": "typeOfCallingSubscriber", "type": dt.TypeOfCallingSubscriber},
    4: {"name": "callingPartyNumber", "type": dt.AddressString},
    5: {"name": "calledPartyNumber", "type": dt.AddressString},
    6: {"name": "calledSubscriberIMSI", "type": dt.IMSI},
    7: {"name": "disconnectingParty", "type": dt.DisconnectingParty},
    8: {"name": "dateForStartOfCharge", "type": dt.Date},
    9: {"name": "timeForStartOfCharge", "type": dt.Time},
    10: {"name": "timeForStopOfCharge", "type": dt.Time},
    11: {"name": "chargeableDuration", "type": dt.Time},
    12: {"name": "interruptionTime", "type": dt.Time},
    13: {"name": "timeFromRegisterSeizureToStartOfCharging", "type": dt.Time},
    14: {"name": "chargedParty", "type": dt.ChargedParty},
    15: {"name": "originForCharging", "type": dt.ChargingOrigin},
    16: {"name": "tariffClass", "type": dt.TariffClass},
    17: {"name": "tariffSwitchInd", "type": dt.TariffSwitchInd},
    18: {"name": "numberOfMeterPulses", "type": dt.NumberOfMeterPulses},
    19: {"name": "exchangeIdentity", "type": dt.ExchangeIdentity},
    20: {"name": "mSCIdentification", "type": dt.AddressString},
    21: {"name": "outgoingRoute", "type": dt.Route},
    22: {"name": "incomingRoute", "type": dt.Route},
    23: {"name": "miscellaneousInformation", "type": dt.MiscellaneousInformation},
    25: {"name": "iNMarkingOfMS", "type": dt.INMarkingOfMS},
    26: {"name": "callPosition", "type": dt.CallPosition},
    27: {"name": "eosInfo", "type": dt.EosInfo},
    28: {"name": "internalCauseAndLoc", "type": dt.InternalCauseAndLoc},
    29: {"name": "originalCalledNumber", "type": dt.AddressString},
    30: {"name": "redirectingNumber", "type": dt.AddressString},
    31: {"name": "redirectionCounter", "type": dt.RedirectionCounter},
    32: {"name": "redirectingDropBackNumber", "type": dt.AddressString},
    33: {"name": "redirectingDropBack", "type": dt.Bool},  # NULL type
    34: {"name": "restartDuringCall", "type": dt.Bool},  # NULL type
    35: {"name": "restartDuringOutputIndicator", "type": dt.Bool},  # NULL type
    36: {"name": "iCIOrdered", "type": dt.Bool},  # NULL type
    37: {"name": "outputForSubscriber", "type": dt.OutputForSubscriber},
    38: {"name": "lastPartialOutput", "type": dt.Bool},  # NULL type
    39: {"name": "partialOutputRecNum", "type": dt.PartialOutputRecNum},
    40: {"name": "relatedCallNumber", "type": dt.CallIDNumber},
    41: {"name": "faultCode", "type": dt.FaultCode},
    42: {"name": "subscriptionType", "type": dt.SubscriptionType},
    43: {"name": "incompleteCallDataIndicator", "type": dt.Bool},  # NULL type
    44: {"name": "incompleteCompositeCDRIndicator", "type": dt.Bool},  # NULL type
    45: {"name": "switchIdentity", "type": dt.SwitchIdentity},
    46: {"name": "networkCallReference", "type": dt.NetworkCallReference},
    47: {"name": "disconnectionDueToSystemRecovery", "type": dt.Bool},  # NULL type
    48: {"name": "forloppDuringOutputIndicator", "type": dt.Bool},  # NULL type
    49: {"name": "forloppReleaseDuringCall", "type": dt.Bool},  # NULL type
    50: {"name": "translatedNumber", "type": dt.AddressString},
    51: {
        "name": "bCSMTDPData1",
        "tag": "camelTDPData",
        "type": CAMELTDPData,
    },
    52: {"name": "bCSMTDPData2", "tag": "camelTDPData", "type": CAMELTDPData},
    53: {"name": "bCSMTDPData3", "tag": "camelTDPData", "type": CAMELTDPData},
    54: {"name": "bCSMTDPData4", "tag": "camelTDPData", "type": CAMELTDPData},
    55: {"name": "bCSMTDPData5", "tag": "camelTDPData", "type": CAMELTDPData},
    56: {"name": "bCSMTDPData6", "tag": "camelTDPData", "type": CAMELTDPData},
    57: {"name": "bCSMTDPData7", "tag": "camelTDPData", "type": CAMELTDPData},
    58: {"name": "bCSMTDPData8", "tag": "camelTDPData", "type": CAMELTDPData},
    59: {"name": "bCSMTDPData9", "tag": "camelTDPData", "type": CAMELTDPData},
    60: {"name": "bCSMTDPData10", "tag": "camelTDPData", "type": CAMELTDPData},
    61: {"name": "gSMCallReferenceNumber", "type": dt.GSMCallReferenceNumber},
    # 62: {"name": "c7ChargingMessage", "type": C7ChargingMessage}, # WCDMA Japan
    # 63: {"name": "c7FirstCHTMessage", "type": dt.C7CHTMessage}, # WCDMA Japan
    # 64: {"name": "c7SecondCHTMessage", "type": dt.C7CHTMessage}, # WCDMA Japan
    65: {"name": "aCMChargingIndicator", "type": dt.ChargingIndicator},
    66: {"name": "aNMChargingIndicator", "type": dt.ChargingIndicator},
    67: {"name": "mSCAddress", "type": dt.AddressString},
    # 68: {"name": "carrierInformationBackward", "type": TransitCarrierInfo}, # WCDMA Japan
    # 69: {"name": "carrierInformationForward", "type": TransitCarrierInfo}, # WCDMA Japan
    # 70: {"name": "chargeInformation", "type": ChargeInformation},  # WCDMA Japan
    71: {"name": "disconnectionDate", "type": dt.Date},
    72: {"name": "disconnectionTime", "type": dt.Time},
    73: {"name": "entryPOICA", "type": dt.ChargeAreaCode},
    74: {"name": "exitPOICA", "type": dt.ChargeAreaCode},
    75: {"name": "internationalCallIndicator", "type": dt.Bool},  # NULL type
    76: {"name": "mobileUserClass1", "type": dt.MobileUserClass1},
    # 77: {"name": "mobileUserClass2", "type": MobileUserClass2}, # WCDMA Japan
    78: {"name": "originatingAccessISDN", "type": dt.Bool},  # NULL type
    79: {"name": "originatingCarrier", "type": dt.CarrierInfo},
    80: {"name": "originatingChargeArea", "type": dt.ChargeAreaCode},
    # 81: {"name": "tDSCounter", "type": Counter}, #WCDMA Japan
    82: {"name": "terminatingAccessISDN", "type": dt.Bool},  # NULL type
    83: {"name": "terminatingCarrier", "type": dt.CarrierInfo},
    84: {"name": "terminatingChargeArea", "type": dt.ChargeAreaCode},
    85: {"name": "terminatingMobileUserClass1", "type": dt.MobileUserClass1},
    # 86: {"name": "terminatingMobileUserClass2", "type": MobileUserClass2}, # WCDMA Japan
    87: {"name": "contractorNumber", "type": dt.AddressString},
    88: {"name": "terminatingUserClass", "type": dt.UserClass},
    89: {"name": "userClass", "type": dt.UserClass},
    90: {"name": "calledPartyMNPInfo", "type": dt.AddressString},
    91: {"name": "chargeNumber", "type": dt.AddressString},
    92: {"name": "originatingLineInformation", "type": dt.OriginatingLineInformation},
    93: {
        "name": "multimediaInformation",
        "tag": "multimediaInformation",
        "type": MultimediaInformation,
    },
    102: {"name": "outputType", "type": dt.OutputType},
    24: {"name": "originatedCode", "type": dt.OriginatedCode},
    121: {"name": "reroutingIndicator", "type": dt.RerountingIndicator},
}

MSOriginating = {
    0: {"name": "tAC", "type": dt.TAC},
    1: {"name": "callIdentificationNumber", "type": dt.CallIDNumber},
    2: {"name": "recordSequenceNumber", "type": dt.RecordSequenceNumber},
    3: {"name": "typeOfCallingSubscriber", "type": dt.TypeOfCallingSubscriber},
    4: {"name": "callingPartyNumber", "type": dt.AddressString},
    5: {"name": "callingSubscriberIMSI", "type": dt.IMSI},
    6: {"name": "callingSubscriberIMEI", "type": dt.IMEI},
    7: {"name": "calledPartyNumber", "type": dt.AddressString},
    8: {"name": "disconnectingParty", "type": dt.DisconnectingParty},
    9: {"name": "dateForStartOfCharge", "type": dt.Date},
    10: {"name": "timeForStartOfCharge", "type": dt.Time},
    11: {"name": "timeForStopOfCharge", "type": dt.Time},
    12: {"name": "chargeableDuration", "type": dt.Time},
    13: {"name": "interruptionTime", "type": dt.Time},
    14: {"name": "timeFromRegisterSeizureToStartOfCharging", "type": dt.Time},
    15: {"name": "chargedParty", "type": dt.ChargedParty},
    16: {"name": "originForCharging", "type": dt.ChargingOrigin},
    17: {"name": "chargingCase", "type": dt.ChargingCase},
    18: {"name": "tariffClass", "type": dt.TariffClass},
    19: {"name": "tariffSwitchInd", "type": dt.TariffSwitchInd},
    20: {"name": "exchangeIdentity", "type": dt.ExchangeIdentity},
    21: {"name": "mSCIdentification", "type": dt.AddressString},
    22: {"name": "outgoingRoute", "type": dt.Route},
    23: {"name": "incomingRoute", "type": dt.Route},
    24: {"name": "miscellaneousInformation", "type": dt.MiscellaneousInformation},
    25: {"name": "originatingLocationNumber", "type": dt.AddressString},
    26: {"name": "timeForTCSeizureCalling", "type": dt.Time},
    27: {"name": "firstCallingLocationInformation", "type": dt.LocationInformation},
    28: {"name": "lastCallingLocationInformation", "type": dt.LocationInformation},
    29: {"name": "teleServiceCode", "type": dt.TeleServiceCode},
    30: {"name": "bearerServiceCode", "type": dt.BearerServiceCode},
    31: {"name": "transparencyIndicator", "type": dt.TransparencyIndicator},
    32: {"name": "firstRadioChannelUsed", "type": dt.FirstRadioChannelUsed},
    33: {"name": "callPosition", "type": dt.CallPosition},
    34: {"name": "eosInfo", "type": dt.EosInfo},
    35: {"name": "internalCauseAndLoc", "type": dt.InternalCauseAndLoc},
    36: {"name": "restartDuringCall", "type": dt.Bool},  # NULL type
    37: {"name": "restartDuringOutputIndicator", "type": dt.Bool},  # NULL type
    38: {"name": "numberOfMeterPulses", "type": dt.NumberOfMeterPulses},
    # 39: {"name": "c7ChargingMessage", "type": dt.C7ChargingMessage}, # WCDMA Japan
    # 40: {"name": "c7FirstCHTMessage", "type": dt.C7CHTMessage}, # WCDMA Japan
    # 41: {"name": "c7SecondCHTMessage", "type": dt.C7CHTMessage}, # WCDMA Japan
    42: {"name": "calledPartyMNPInfo", "type": dt.AddressString},
    43: {"name": "carrierIdentificationCode", "type": dt.CarrierIdentificationCode},
    44: {"name": "dTMFUsed", "type": dt.Bool},  # NULL type
    45: {"name": "iCIOrdered", "type": dt.Bool},  # NULL type
    46: {"name": "outputForSubscriber", "type": dt.OutputForSubscriber},
    47: {"name": "iNMarkingOfMS", "type": dt.INMarkingOfMS},
    48: {"name": "lastPartialOutput", "type": dt.Bool},  # NULL type
    49: {"name": "partialOutputRecNum", "type": dt.PartialOutputRecNum},
    50: {"name": "cUGInterlockCode", "type": dt.CUGInterlockCode},
    51: {"name": "cUGIndex", "type": dt.CUGIndex},
    52: {"name": "cUGOutgoingAccessUsed", "type": dt.Bool},  # NULL type
    53: {"name": "cUGOutgoingAccessIndicator", "type": dt.Bool},  # NULL type
    54: {"name": "regionalServiceUsed", "type": dt.RegionalServiceUsed},
    55: {"name": "regionDependentChargingOrigin", "type": dt.ChargingOrigin},
    56: {"name": "sSCode", "type": dt.SSCode},
    57: {
        "name": "channelAllocationPriorityLevel",
        "type": dt.ChannelAllocationPriorityLevel,
    },
    58: {"name": "radioChannelProperty", "type": dt.RadioChannelProperty},
    59: {"name": "faultCode", "type": dt.FaultCode},
    60: {"name": "intermediateRate", "type": dt.IntermediateRate},
    61: {"name": "firstAssignedSpeechCoderVersion", "type": dt.SpeechCoderVersion},
    62: {"name": "speechCoderPreferenceList", "type": dt.SpeechCoderPreferenceList},
    63: {"name": "subscriptionType", "type": dt.SubscriptionType},
    64: {"name": "incompleteCallDataIndicator", "type": dt.Bool},  # NULL type
    65: {"name": "incompleteCompositeCDRIndicator", "type": dt.Bool},  # NULL type
    66: {"name": "originatedCode", "type": dt.OriginatedCode},
    67: {"name": "switchIdentity", "type": dt.SwitchIdentity},
    68: {"name": "networkCallReference", "type": dt.NetworkCallReference},
    69: {"name": "frequencyBandSupported", "type": dt.FrequencyBandSupported},
    70: {"name": "disconnectionDueToSystemRecovery", "type": dt.Bool},  # NULL type
    71: {"name": "forloppDuringOutputIndicator", "type": dt.Bool},  # NULL type
    72: {"name": "forloppReleaseDuringCall", "type": dt.Bool},  # NULL type
    73: {"name": "accountCode", "type": dt.AccountCode},
    74: {"name": "translatedNumber", "type": dt.AddressString},
    75: {"name": "bCSMTDPData1", "tag": "camelTDPData", "type": CAMELTDPData},
    76: {"name": "bCSMTDPData2", "tag": "camelTDPData", "type": CAMELTDPData},
    77: {"name": "bCSMTDPData3", "tag": "camelTDPData", "type": CAMELTDPData},
    78: {"name": "bCSMTDPData4", "tag": "camelTDPData", "type": CAMELTDPData},
    79: {"name": "bCSMTDPData5", "tag": "camelTDPData", "type": CAMELTDPData},
    80: {"name": "bCSMTDPData6", "tag": "camelTDPData", "type": CAMELTDPData},
    81: {"name": "bCSMTDPData7", "tag": "camelTDPData", "type": CAMELTDPData},
    82: {"name": "bCSMTDPData8", "tag": "camelTDPData", "type": CAMELTDPData},
    83: {"name": "bCSMTDPData9", "tag": "camelTDPData", "type": CAMELTDPData},
    84: {"name": "bCSMTDPData10", "tag": "camelTDPData", "type": CAMELTDPData},
    85: {"name": "gSMCallReferenceNumber", "type": dt.GSMCallReferenceNumber},
    86: {"name": "mSCAddress", "type": dt.AddressString},
    87: {"name": "eMLPPPriorityLevel", "type": dt.EMLPPPriorityLevel},  #
    88: {"name": "positionAccuracy", "type": dt.PositionAccuracy},
    # 89: {"name": "userTerminalPosition", "type": dt.UserTerminalPosition},
    # 90: {"name": "acceptableChannelCodings", "type": dt.ChannelCodings},
    91: {"name": "incomingAssignedRoute", "type": dt.Route},
    # 92: {"name": "channelCodingUsed", "type": dt.ChannelCodings},
    # 93: {"name": "rANAPCauseCode", "type": dt.RANAPCauseCode},
    94: {"name": "gsmSCFAddress", "type": dt.AddressString},
    95: {"name": "fNURRequested", "type": dt.FixedNetworkUserRate},
    96: {"name": "aIURRequested", "type": dt.AirInterfaceUserRate},
    97: {"name": "numberOfChannelsRequested", "type": dt.NumberOfChannels},
    98: {"name": "bSSMAPCauseCode", "type": dt.BSSMAPCauseCode},
    99: {"name": "multimediaCall", "type": dt.Bool},  # NULL type
    # 100: {"name": "guaranteedBitRate", "type": dt.BitRate},
    101: {"name": "trafficClass", "type": dt.TrafficClass},
    102: {"name": "outputType", "type": dt.OutputType},
    # 103: {"name": "rNCidOfFirstRNC", "type": dt.TargetRNCid},
    # 104: {"name": "maxBitRateDownlink", "type": dt.BitRate},
    # 105: {"name": "maxBitRateUplink", "type": dt.BitRate},
    # 106: {"name": "transferDelay", "type": dt.TransferDelay},
    107: {"name": "deliveryOfErroneousSDU1", "type": dt.DeliveryOfErroneousSDU},
    108: {"name": "deliveryOfErroneousSDU2", "type": dt.DeliveryOfErroneousSDU},
    109: {"name": "deliveryOfErroneousSDU3", "type": dt.DeliveryOfErroneousSDU},
    # 110: {"name": "residualBitErrorRatio1", "type": dt.ErrorRatio},
    # 111: {"name": "residualBitErrorRatio2", "type": dt.ErrorRatio},
    # 112: {"name": "residualBitErrorRatio3", "type": dt.ErrorRatio},
    # 113: {"name": "sDUErrorRatio1", "type": dt.ErrorRatio},
    # 114: {"name": "sDUErrorRatio2", "type": dt.ErrorRatio},
    # 115: {"name": "sDUErrorRatio3", "type": dt.ErrorRatio},
    116: {"name": "aCMChargingIndicator", "type": dt.ChargingIndicator},
    117: {"name": "aNMChargingIndicator", "type": dt.ChargingIndicator},
    # 118: {"name": "carrierInformationBackward", "type": dt.TransitCarrierInfo}, # WCDMA Japan
    # 119: {"name": "chargeInformation", "type": dt.ChargeInformation}, # WCDMA Japan
    120: {"name": "disconnectionDate", "type": dt.Date},
    124: {"name": "disconnectionTime", "type": dt.Time},
    125: {"name": "originatingCarrier", "type": dt.CarrierInfo},
    126: {"name": "originatingChargeArea", "type": dt.ChargeAreaCode},
    # 127: {"name": "tDSCounter", "type": dt.Counter}, # WCDMA Japan
    128: {"name": "terminatingAccessISDN", "type": dt.Bool},  # NULL type
    129: {"name": "terminatingCarrier", "type": dt.CarrierInfo},
    130: {"name": "terminatingChargeArea", "type": dt.ChargeAreaCode},
    131: {"name": "terminatingMobileUserClass1", "type": dt.MobileUserClass1},
    # 132: {
    #     "name": "terminatingMobileUserClass2",
    #     "type": dt.MobileUserClass2,
    # },  # WCDMA Japan
    133: {"name": "terminatingUserClass", "type": dt.UserClass},
    134: {"name": "contractorNumber", "type": dt.AddressString},
    # 135: {"name": "carrierInformation", "type": dt.CarrierInformation},
    # 136: {
    #     "name": "carrierSelectionSubstitutionInformation",
    #     "type": dt.CarrierSelectionSubstitutionInformation,
    # },
    137: {"name": "chargeNumber", "type": dt.AddressString},
    138: {"name": "interExchangeCarrierIndicator", "type": dt.Bool},  # NULL type
    139: {"name": "originatingLineInformation", "type": dt.OriginatingLineInformation},
    140: {"name": "selectedCodec", "type": dt.SelectedCodec},
    141: {"name": "wPSCallIndicator", "type": dt.Bool},  # NULL type
}
RoamingCallForwarding = {
    0: {"name": "tAC", "type": dt.TAC},
    1: {"name": "callIdentificationNumber", "type": dt.CallIDNumber},
    2: {"name": "recordSequenceNumber", "type": dt.RecordSequenceNumber},
    3: {"name": "typeOfCallingSubscriber", "type": dt.TypeOfCallingSubscriber},
    4: {"name": "callingPartyNumber", "type": dt.AddressString},
    5: {"name": "calledPartyNumber", "type": dt.AddressString},
    6: {"name": "calledSubscriberIMSI", "type": dt.IMSI},
    7: {"name": "mobileStationRoamingNumber", "type": dt.AddressString},
    8: {"name": "disconnectingParty", "type": dt.DisconnectingParty},
    9: {"name": "dateForStartOfCharge", "type": dt.Date},
    10: {"name": "timeForStartOfCharge", "type": dt.Time},
    11: {"name": "timeForStopOfCharge", "type": dt.Time},
    12: {"name": "chargeableDuration", "type": dt.Time},
    13: {"name": "interruptionTime", "type": dt.Time},
    14: {"name": "timeFromRegisterSeizureToStartOfCharging", "type": dt.Time},
    15: {"name": "chargedParty", "type": dt.ChargedParty},
    16: {"name": "originForCharging", "type": dt.ChargingOrigin},
    17: {"name": "tariffClass", "type": dt.TariffClass},
    18: {"name": "tariffSwitchInd", "type": dt.TariffSwitchInd},
    19: {"name": "exchangeIdentity", "type": dt.ExchangeIdentity},
    20: {"name": "mSCIdentification", "type": dt.AddressString},
    21: {"name": "outgoingRoute", "type": dt.Route},
    22: {"name": "incomingRoute", "type": dt.Route},
    23: {"name": "miscellaneousInformation", "type": dt.MiscellaneousInformation},
    24: {"name": "subscriptionType", "type": dt.SubscriptionType},
    25: {"name": "callPosition", "type": dt.CallPosition},
    26: {"name": "eosInfo", "type": dt.EosInfo},
    27: {"name": "internalCauseAndLoc", "type": dt.InternalCauseAndLoc},
    28: {"name": "originalCalledNumber", "type": dt.AddressString},
    29: {"name": "redirectingNumber", "type": dt.AddressString},
    30: {"name": "redirectionCounter", "type": dt.RedirectionCounter},
    31: {"name": "restartDuringCall", "type": dt.Bool},  # NULL type
    32: {"name": "restartDuringOutputIndicator", "type": dt.Bool},  # NULL type
    33: {"name": "numberOfMeterPulses", "type": dt.NumberOfMeterPulses},
    # 34: {"name": "c7ChargingMessage", "type": dt.C7ChargingMessage},
    35: {"name": "c7FirstCHTMessage", "type": dt.C7CHTMessage},
    36: {"name": "c7SecondCHTMessage", "type": dt.C7CHTMessage},
    37: {"name": "iCIOrdered", "type": dt.Bool},  # NULL type
    38: {"name": "outputForSubscriber", "type": dt.OutputForSubscriber},
    39: {"name": "lastPartialOutput", "type": dt.Bool},  # NULL type
    40: {"name": "partialOutputRecNum", "type": dt.PartialOutputRecNum},
    41: {"name": "relatedCallNumber", "type": dt.CallIDNumber},
    # 42: {"name": "cUGInterlockCode", "type": dt.CUGInterlockCode},
    43: {"name": "cUGOutgoingAccessIndicator", "type": dt.Bool},  # NULL type
    44: {
        "name": "presentationAndScreeningIndicator",
        "type": dt.PresentationAndScreeningIndicator,
    },
    45: {"name": "faultCode", "type": dt.FaultCode},
    46: {"name": "incompleteCallDataIndicator", "type": dt.Bool},  # NULL type
    48: {"name": "switchIdentity", "type": dt.SwitchIdentity},
    49: {"name": "networkCallReference", "type": dt.NetworkCallReference},
    50: {"name": "disconnectionDueToSystemRecovery", "type": dt.Bool},  # NULL type
    51: {"name": "forloppDuringOutputIndicator", "type": dt.Bool},  # NULL type
    52: {"name": "forloppReleaseDuringCall", "type": dt.Bool},  # NULL type
    53: {"name": "gSMCallReferenceNumber", "type": dt.GSMCallReferenceNumber},
    54: {"name": "mSCAddress", "type": dt.AddressString},
    # 55: {"name": "carrierInformationBackward", "type": dt.TransitCarrierInfo}, # WCDMA Japan
    57: {"name": "originatingCarrier", "type": dt.CarrierInfo},
    58: {"name": "originatingChargeArea", "type": dt.ChargeAreaCode},
    59: {"name": "terminatingAccessISDN", "type": dt.Bool},  # NULL type
    60: {"name": "terminatingCarrier", "type": dt.CarrierInfo},
    61: {"name": "terminatingChargeArea", "type": dt.ChargeAreaCode},
    62: {"name": "contractorNumber", "type": dt.AddressString},
    # 63: {"name": "carrierIdentificationCode", "type": dt.CarrierIdentificationCode},
    # 64: {"name": "carrierInformation", "type": dt.CarrierInformation},
    # 65: {
    #     "name": "carrierSelectionSubstitutionInformation",
    #     "type": dt.CarrierSelectionSubstitutionInformation,
    # },
    66: {"name": "chargeNumber", "type": dt.AddressString},
    67: {"name": "interExchangeCarrierIndicator", "type": dt.Bool},  # NULL type
    68: {"name": "originatingLineInformation", "type": dt.OriginatingLineInformation},
    102: {"name": "outputType", "type": dt.OutputType},
    121: {"name": "reroutingIndicator", "type": dt.Bool},  # NULL type
}

CallForwarding = {
    0: {"name": "tAC", "type": dt.TAC},
    1: {"name": "callIdentificationNumber", "type": dt.CallIDNumber},
    2: {"name": "recordSequenceNumber", "type": dt.RecordSequenceNumber},
    3: {"name": "typeOfCallingSubscriber", "type": dt.TypeOfCallingSubscriber},
    4: {"name": "callingPartyNumber", "type": dt.AddressString},
    5: {"name": "calledPartyNumber", "type": dt.AddressString},
    6: {"name": "originalCalledNumber", "type": dt.AddressString},
    7: {"name": "redirectingNumber", "type": dt.AddressString},
    8: {"name": "redirectionCounter", "type": dt.RedirectionCounter},
    9: {"name": "redirectingSPN", "type": dt.AddressString},
    10: {"name": "redirectingIMSI", "type": dt.IMSI},
    11: {"name": "mobileStationRoamingNumber", "type": dt.AddressString},
    12: {"name": "disconnectingParty", "type": dt.DisconnectingParty},
    13: {"name": "dateForStartOfCharge", "type": dt.Date},
    14: {"name": "timeForStartOfCharge", "type": dt.Time},
    15: {"name": "timeForStopOfCharge", "type": dt.Time},
    16: {"name": "chargeableDuration", "type": dt.Time},
    17: {"name": "interruptionTime", "type": dt.Time},
    18: {"name": "timeFromRegisterSeizureToStartOfCharging", "type": dt.Time},
    19: {"name": "chargedParty", "type": dt.ChargedParty},
    20: {"name": "originForCharging", "type": dt.ChargingOrigin},
    21: {"name": "tariffClass", "type": dt.TariffClass},
    22: {"name": "tariffSwitchInd", "type": dt.TariffSwitchInd},
    23: {"name": "exchangeIdentity", "type": dt.ExchangeIdentity},
    24: {"name": "mSCIdentification", "type": dt.AddressString},
    25: {"name": "outgoingRoute", "type": dt.Route},
    26: {"name": "incomingRoute", "type": dt.Route},
    27: {"name": "miscellaneousInformation", "type": dt.MiscellaneousInformation},
    28: {"name": "originatingLocationNumber", "type": dt.AddressString},
    29: {"name": "callPosition", "type": dt.CallPosition},
    30: {"name": "eosInfo", "type": dt.EosInfo},
    31: {"name": "internalCauseAndLoc", "type": dt.InternalCauseAndLoc},
    32: {"name": "restartDuringCall", "type": dt.Bool},  # NULL type
    33: {"name": "restartDuringOutputIndicator", "type": dt.Bool},  # NULL type
    34: {"name": "numberOfMeterPulses", "type": dt.NumberOfMeterPulses},
    # 35: {"name": "c7ChargingMessage", "type": dt.C7ChargingMessage},
    # 36: {"name": "c7FirstCHTMessage", "type": dt.C7CHTMessage}, # WCDMA Japan
    # 37: {"name": "c7SecondCHTMessage", "type": dt.C7CHTMessage}, # WCDMA Japan
    38: {"name": "iCIOrdered", "type": dt.Bool},  # NULL type
    39: {"name": "outputForSubscriber", "type": dt.OutputForSubscriber},
    40: {"name": "iNMarkingOfMS", "type": dt.INMarkingOfMS},
    41: {"name": "lastPartialOutput", "type": dt.Bool},  # NULL type
    42: {"name": "partialOutputRecNum", "type": dt.PartialOutputRecNum},
    43: {"name": "relatedCallNumber", "type": dt.CallIDNumber},
    44: {"name": "cUGInterlockCode", "type": dt.CUGInterlockCode},
    45: {"name": "cUGIndex", "type": dt.CUGIndex},
    46: {"name": "cUGOutgoingAccessUsed", "type": dt.Bool},  # NULL type
    47: {"name": "cUGOutgoingAccessIndicator", "type": dt.Bool},  # NULL type
    48: {"name": "regionalServiceUsed", "type": dt.RegionalServiceUsed},
    49: {"name": "regionDependentChargingOrigin", "type": dt.ChargingOrigin},
    50: {
        "name": "presentationAndScreeningIndicator",
        "type": dt.PresentationAndScreeningIndicator,
    },
    51: {"name": "faultCode", "type": dt.FaultCode},
    52: {"name": "subscriptionType", "type": dt.SubscriptionType},
    53: {"name": "incompleteCallDataIndicator", "type": dt.Bool},  # NULL type
    54: {"name": "incompleteCompositeCDRIndicator", "type": dt.Bool},  # NULL type
    55: {"name": "originatedCode", "type": dt.OriginatedCode},
    56: {"name": "switchIdentity", "type": dt.SwitchIdentity},
    57: {"name": "networkCallReference", "type": dt.NetworkCallReference},
    58: {"name": "disconnectionDueToSystemRecovery", "type": dt.Bool},  # NULL type
    59: {"name": "forloppDuringOutputIndicator", "type": dt.Bool},  # NULL type
    60: {"name": "forloppReleaseDuringCall", "type": dt.Bool},  # NULL type
    61: {"name": "translatedNumber", "type": dt.AddressString},
    62: {"name": "cAMELInitiatedCallForwarding", "type": dt.Bool},  # NULL type
    63: {"name": "bCSMTDPData1", "tag": "camelTDPData", "type": CAMELTDPData},
    64: {"name": "bCSMTDPData2", "tag": "camelTDPData", "type": CAMELTDPData},
    65: {"name": "bCSMTDPData3", "tag": "camelTDPData", "type": CAMELTDPData},
    66: {"name": "bCSMTDPData4", "tag": "camelTDPData", "type": CAMELTDPData},
    67: {"name": "bCSMTDPData5", "tag": "camelTDPData", "type": CAMELTDPData},
    68: {"name": "bCSMTDPData6", "tag": "camelTDPData", "type": CAMELTDPData},
    69: {"name": "bCSMTDPData7", "tag": "camelTDPData", "type": CAMELTDPData},
    70: {"name": "bCSMTDPData8", "tag": "camelTDPData", "type": CAMELTDPData},
    71: {"name": "bCSMTDPData9", "tag": "camelTDPData", "type": CAMELTDPData},
    72: {"name": "bCSMTDPData10", "tag": "camelTDPData", "type": CAMELTDPData},
    73: {"name": "gSMCallReferenceNumber", "type": dt.GSMCallReferenceNumber},
    74: {"name": "mSCAddress", "type": dt.AddressString},
    75: {"name": "aCMChargingIndicator", "type": dt.ChargingIndicator},
    76: {"name": "aNMChargingIndicator", "type": dt.ChargingIndicator},
    # 77: {"name": "carrierInformationBackward", "type": dt.TransitCarrierInfo}, # WCDMA Japan
    # 78: {"name": "chargeInformation", "type": dt.ChargeInformation}, # WCDMA Japan
    79: {"name": "disconnectionDate", "type": dt.Date},
    80: {"name": "disconnectionTime", "type": dt.Time},
    81: {"name": "exitPOICA", "type": dt.ChargeAreaCode},
    82: {"name": "originatingCarrier", "type": dt.CarrierInfo},
    83: {"name": "originatingChargeArea", "type": dt.ChargeAreaCode},
    84: {"name": "terminatingAccessISDN", "type": dt.Bool},  # NULL type
    85: {"name": "terminatingCarrier", "type": dt.CarrierInfo},
    86: {"name": "terminatingChargeArea", "type": dt.ChargeAreaCode},
    87: {"name": "terminatingMobileUserClass1", "type": dt.MobileUserClass1},
    # 88: {"name": "terminatingMobileUserClass2", "type": dt.MobileUserClass2}, # WCDMA Japan
    89: {"name": "terminatingUserClass", "type": dt.UserClass},
    90: {"name": "originatingAccessISDN", "type": dt.Bool},  # NULL type
    91: {"name": "contractorNumber", "type": dt.AddressString},
    92: {"name": "calledPartyMNPInfo", "type": dt.AddressString},
    93: {"name": "carrierIdentificationCode", "type": dt.CarrierIdentificationCode},
    # 94: {"name": "carrierInformation", "type": dt.CarrierInformation},
    # 95: {
    #     "name": "carrierSelectionSubstitutionInformation",
    #     "type": dt.CarrierSelectionSubstitutionInformation,
    # },
    96: {"name": "chargeNumber", "type": dt.AddressString},
    97: {"name": "interExchangeCarrierIndicator", "type": dt.Bool},  # NULL type
    98: {"name": "originatingLineInformation", "type": dt.OriginatingLineInformation},
    99: {"name": "optimalRoutingType", "type": dt.OptimalRoutingType},
    100: {"name": "optimalRoutingInvocationFailed", "type": dt.Bool},  # NULL type
    102: {"name": "outputType", "type": dt.OutputType},
}

MSTerminating = {
    0: {"name": "tAC", "type": dt.TAC},
    1: {"name": "callIdentificationNumber", "type": dt.CallIDNumber},
    2: {"name": "recordSequenceNumber", "type": dt.RecordSequenceNumber},
    3: {"name": "typeOfCallingSubscriber", "type": dt.TypeOfCallingSubscriber},
    4: {"name": "callingPartyNumber", "type": dt.AddressString},
    5: {"name": "calledPartyNumber", "type": dt.AddressString},
    6: {"name": "calledSubscriberIMSI", "type": dt.IMSI},
    7: {"name": "calledSubscriberIMEI", "type": dt.IMEI},
    8: {"name": "mobileStationRoamingNumber", "type": dt.AddressString},
    9: {"name": "disconnectingParty", "type": dt.DisconnectingParty},
    10: {"name": "dateForStartOfCharge", "type": dt.Date},
    11: {"name": "timeForStartOfCharge", "type": dt.Time},
    12: {"name": "timeForStopOfCharge", "type": dt.Time},
    13: {"name": "chargeableDuration", "type": dt.Time},
    14: {"name": "interruptionTime", "type": dt.Time},
    15: {"name": "timeFromRegisterSeizureToStartOfCharging", "type": dt.Time},
    16: {"name": "chargedParty", "type": dt.ChargedParty},
    17: {"name": "originForCharging", "type": dt.ChargingOrigin},
    18: {"name": "tariffClass", "type": dt.TariffClass},
    19: {"name": "tariffSwitchInd", "type": dt.TariffSwitchInd},
    20: {"name": "exchangeIdentity", "type": dt.ExchangeIdentity},
    21: {"name": "mSCIdentification", "type": dt.AddressString},
    22: {"name": "outgoingRoute", "type": dt.Route},
    23: {"name": "incomingRoute", "type": dt.Route},
    24: {
        "name": "channelAllocationPriorityLevel",
        "type": dt.ChannelAllocationPriorityLevel,
    },
    25: {"name": "terminatingLocationNumber", "type": dt.AddressString},
    26: {"name": "timeForTCSeizureCalled", "type": dt.Time},
    27: {"name": "firstCalledLocationInformation", "type": dt.LocationInformation},
    28: {"name": "lastCalledLocationInformation", "type": dt.LocationInformation},
    29: {"name": "teleServiceCode", "type": dt.TeleServiceCode},
    30: {"name": "bearerServiceCode", "type": dt.BearerServiceCode},
    31: {"name": "transparencyIndicator", "type": dt.TransparencyIndicator},
    32: {"name": "firstRadioChannelUsed", "type": dt.FirstRadioChannelUsed},
    33: {"name": "callPosition", "type": dt.CallPosition},
    34: {"name": "eosInfo", "type": dt.EosInfo},
    35: {"name": "internalCauseAndLoc", "type": dt.InternalCauseAndLoc},
    36: {"name": "originalCalledNumber", "type": dt.AddressString},
    37: {"name": "redirectingNumber", "type": dt.AddressString},
    38: {"name": "redirectionCounter", "type": dt.RedirectionCounter},
    39: {"name": "selectedCodec", "type": dt.SelectedCodec},
    41: {"name": "restartDuringCall", "type": dt.Bool},  # NULL type
    42: {"name": "restartDuringOutputIndicator", "type": dt.Bool},  # NULL type
    43: {"name": "dTMFUsed", "type": dt.Bool},  # NULL type
    44: {"name": "iCIOrdered", "type": dt.Bool},  # NULL type
    45: {"name": "outputForSubscriber", "type": dt.OutputForSubscriber},
    46: {"name": "lastPartialOutput", "type": dt.Bool},  # NULL type
    47: {"name": "partialOutputRecNum", "type": dt.PartialOutputRecNum},
    48: {"name": "relatedCallNumber", "type": dt.CallIDNumber},
    49: {"name": "acceptanceOfCallWaiting", "type": dt.Bool},  # NULL type
    50: {"name": "miscellaneousInformation", "type": dt.MiscellaneousInformation},
    51: {"name": "cUGInterlockCode", "type": dt.CUGInterlockCode},
    52: {"name": "cUGIndex", "type": dt.CUGIndex},
    53: {"name": "cUGIncomingAccessUsed", "type": dt.Bool},  # NULL type
    54: {"name": "regionalServiceUsed", "type": dt.RegionalServiceUsed},
    55: {"name": "regionDependentChargingOrigin", "type": dt.ChargingOrigin},
    56: {"name": "sSCode", "type": dt.SSCode},
    57: {
        "name": "presentationAndScreeningIndicator",
        "type": dt.PresentationAndScreeningIndicator,
    },
    58: {"name": "radioChannelProperty", "type": dt.RadioChannelProperty},
    59: {"name": "faultCode", "type": dt.FaultCode},
    60: {"name": "intermediateRate", "type": dt.IntermediateRate},
    61: {"name": "firstAssignedSpeechCoderVersion", "type": dt.SpeechCoderVersion},
    62: {"name": "speechCoderPreferenceList", "type": dt.SpeechCoderPreferenceList},
    63: {"name": "subscriptionType", "type": dt.SubscriptionType},
    64: {"name": "incompleteCallDataIndicator", "type": dt.Bool},  # NULL type
    65: {"name": "mSCAddress", "type": dt.AddressString},
    66: {"name": "switchIdentity", "type": dt.SwitchIdentity},
    67: {"name": "networkCallReference", "type": dt.NetworkCallReference},
    68: {"name": "frequencyBandSupported", "type": dt.FrequencyBandSupported},
    69: {"name": "disconnectionDueToSystemRecovery", "type": dt.Bool},  # NULL type
    70: {"name": "forloppDuringOutputIndicator", "type": dt.Bool},  # NULL type
    71: {"name": "forloppReleaseDuringCall", "type": dt.Bool},  # NULL type
    72: {"name": "accountCode", "type": dt.AccountCode},
    73: {"name": "gSMCallReferenceNumber", "type": dt.GSMCallReferenceNumber},
    74: {"name": "eMLPPPriorityLevel", "type": dt.EMLPPPriorityLevel},
    75: {"name": "positionAccuracy", "type": dt.PositionAccuracy},
    # 76: {"name": "userTerminalPosition", "type": dt.UserTerminalPosition},
    # 77: {"name": "acceptableChannelCodings", "type": dt.ChannelCodings},
    78: {"name": "outgoingAssignedRoute", "type": dt.Route},
    # 79: {"name": "channelCodingUsed", "type": dt.ChannelCodings},
    80: {"name": "multimediaCall", "type": dt.Bool},  # NULL type
    81: {"name": "gsmSCFAddress", "type": dt.AddressString},
    82: {"name": "fNURRequested", "type": dt.FixedNetworkUserRate},
    83: {"name": "aIURRequested", "type": dt.AirInterfaceUserRate},
    84: {"name": "numberOfChannelsRequested", "type": dt.NumberOfChannels},
    85: {"name": "bSSMAPCauseCode", "type": dt.BSSMAPCauseCode},
    # 86: {"name": "guaranteedBitRate", "type": dt.BitRate},
    87: {"name": "trafficClass", "type": dt.TrafficClass},
    # 88: {"name": "rANAPCauseCode", "type": dt.RANAPCauseCode},
    # 89: {"name": "rNCidOfFirstRNC", "type": dt.TargetRNCid},
    # 90: {"name": "maxBitRateDownlink", "type": dt.BitRate},
    # 91: {"name": "maxBitRateUplink", "type": dt.BitRate},
    # 92: {"name": "transferDelay", "type": dt.TransferDelay},
    93: {"name": "deliveryOfErroneousSDU1", "type": dt.DeliveryOfErroneousSDU},
    94: {"name": "deliveryOfErroneousSDU2", "type": dt.DeliveryOfErroneousSDU},
    95: {"name": "deliveryOfErroneousSDU3", "type": dt.DeliveryOfErroneousSDU},
    # 96: {"name": "residualBitErrorRatio1", "type": dt.ErrorRatio},
    # 97: {"name": "residualBitErrorRatio2", "type": dt.ErrorRatio},
    # 98: {"name": "residualBitErrorRatio3", "type": dt.ErrorRatio},
    # 99: {"name": "sDUErrorRatio1", "type": dt.ErrorRatio},
    # 100: {"name": "sDUErrorRatio2", "type": dt.ErrorRatio},
    # 101: {"name": "sDUErrorRatio3", "type": dt.ErrorRatio},
    102: {"name": "outputType", "type": dt.OutputType},
    103: {"name": "aCMChargingIndicator", "type": dt.ChargingIndicator},
    104: {"name": "aNMChargingIndicator", "type": dt.ChargingIndicator},
    # 105: {"name": "chargeInformation", "type": dt.ChargeInformation}, # WCDMA Japan
    106: {"name": "disconnectionDate", "type": dt.Date},
    107: {"name": "disconnectionTime", "type": dt.Time},
    108: {"name": "internationalCallIndicator", "type": dt.Bool},  # NULL type
    109: {"name": "mobileUserClass1", "type": dt.MobileUserClass1},
    # 110: {"name": "mobileUserClass2", "type": dt.MobileUserClass2}, # WCDMA Japan
    111: {"name": "originatingCarrier", "type": dt.CarrierInfo},
    112: {"name": "originatingChargeArea", "type": dt.ChargeAreaCode},
    113: {"name": "terminatingCarrier", "type": dt.CarrierInfo},
    114: {"name": "terminatingChargeArea", "type": dt.ChargeAreaCode},
    115: {"name": "userClass", "type": dt.UserClass},
}

MSOriginatingSMSinMSC = {
    0: {"name": "tAC", "type": dt.TAC},
    1: {"name": "callIdentificationNumber", "type": dt.CallIDNumber},
    2: {"name": "recordSequenceNumber", "type": dt.RecordSequenceNumber},
    3: {"name": "typeOfCallingSubscriber", "type": dt.TypeOfCallingSubscriber},
    4: {"name": "callingPartyNumber", "type": dt.AddressString},
    5: {"name": "callingSubscriberIMSI", "type": dt.IMSI},
    6: {"name": "callingSubscriberIMEI", "type": dt.IMEI},
    7: {"name": "dateForStartOfCharge", "type": dt.Date},
    8: {"name": "timeForStartOfCharge", "type": dt.Time},
    9: {"name": "chargedParty", "type": dt.ChargedParty},
    10: {"name": "originForCharging", "type": dt.ChargingOrigin},
    11: {"name": "exchangeIdentity", "type": dt.ExchangeIdentity},
    12: {"name": "mSCIdentification", "type": dt.AddressString},
    13: {"name": "incomingRoute", "type": dt.Route},
    14: {"name": "firstCallingLocationInformation", "type": dt.LocationInformation},
    15: {"name": "teleServiceCode", "type": dt.TeleServiceCode},
    16: {"name": "serviceCentreAddress", "type": dt.AddressString},
    19: {"name": "iCIOrdered", "type": dt.Bool},  # NULL type
    20: {"name": "outputForSubscriber", "type": dt.OutputForSubscriber},
    21: {"name": "miscellaneousInformation", "type": dt.MiscellaneousInformation},
    22: {"name": "regionalServiceUsed", "type": dt.RegionalServiceUsed},
    23: {"name": "regionDependentChargingOrigin", "type": dt.ChargingOrigin},
    24: {
        "name": "channelAllocationPriorityLevel",
        "type": dt.ChannelAllocationPriorityLevel,
    },
    25: {"name": "frequencyBandSupported", "type": dt.FrequencyBandSupported},
    26: {"name": "incompleteCallDataIndicator", "type": dt.Bool},  # NULL type
    27: {"name": "restartDuringOutputIndicator", "type": dt.Bool},  # NULL type
    28: {"name": "forloppDuringOutputIndicator", "type": dt.Bool},  # NULL type
    29: {"name": "positionAccuracy", "type": dt.PositionAccuracy},
    # 30: {"name": "userTerminalPosition", "type": dt.UserTerminalPosition},
    31: {"name": "switchIdentity", "type": dt.SwitchIdentity},
    # 32: {"name": "destinationAddress", "type": dt.AddressStringExtended},
    # 33: {"name": "messageReference", "type": dt.MessageReference},
    34: {"name": "messageTypeIndicator", "type": dt.MessageTypeIndicator},
    # 35: {"name": "rNCidOfFirstRNC", "type": dt.TargetRNCid},
    36: {"name": "bCSMTDPData1", "tag": "camelTDPData", "type": CAMELTDPData},
    37: {"name": "cAMELCallingPartyNumber", "type": dt.AddressString},
    # 38: {"name": "cAMELDestinationAddress", "type": dt.AddressStringExtended},
    39: {"name": "cAMELSMSCAddress", "type": dt.AddressString},
    40: {"name": "defaultSMSHandling", "type": dt.DefaultSMSHandling},
    41: {"name": "freeFormatData", "type": dt.FreeFormatData},
    42: {"name": "sMSResult", "type": dt.SMSResult},
    43: {"name": "sMSReferenceNumber", "type": dt.NetworkCallReference},
    44: {"name": "mSCAddress", "type": dt.AddressString},
    102: {"name": "outputType", "type": dt.OutputType},
}

MSOriginatingSMSinSMSIWMSC = {
    0: {"name": "tAC", "type": dt.TAC},
    1: {"name": "callIdentificationNumber", "type": dt.CallIDNumber},
    2: {"name": "recordSequenceNumber", "type": dt.RecordSequenceNumber},
    3: {"name": "callingPartyNumber", "type": dt.AddressString},
    4: {"name": "dateForStartOfCharge", "type": dt.Date},
    5: {"name": "timeForStartOfCharge", "type": dt.Time},
    6: {"name": "chargedParty", "type": dt.ChargedParty},
    7: {"name": "exchangeIdentity", "type": dt.ExchangeIdentity},
    8: {"name": "mSCIdentification", "type": dt.AddressString},
    9: {"name": "teleServiceCode", "type": dt.TeleServiceCode},
    10: {"name": "serviceCentreAddress", "type": dt.AddressString},
    11: {"name": "miscellaneousInformation", "type": dt.MiscellaneousInformation},
    12: {"name": "incompleteCallDataIndicator", "type": dt.Bool},  # NULL type
    13: {"name": "restartDuringOutputIndicator", "type": dt.Bool},  # NULL type
    14: {"name": "forloppDuringOutputIndicator", "type": dt.Bool},  # NULL type
    15: {"name": "switchIdentity", "type": dt.SwitchIdentity},
    102: {"name": "outputType", "type": dt.OutputType},
}

MSTerminatingSMSinMSC = {
    0: {"name": "tAC", "type": dt.TAC},
    1: {"name": "callIdentificationNumber", "type": dt.CallIDNumber},
    2: {"name": "recordSequenceNumber", "type": dt.RecordSequenceNumber},
    3: {"name": "calledPartyNumber", "type": dt.AddressString},
    4: {"name": "calledSubscriberIMSI", "type": dt.IMSI},
    5: {"name": "calledSubscriberIMEI", "type": dt.IMEI},
    6: {"name": "dateForStartOfCharge", "type": dt.Date},
    7: {"name": "timeForStartOfCharge", "type": dt.Time},
    8: {"name": "originForCharging", "type": dt.ChargingOrigin},
    9: {"name": "chargedParty", "type": dt.ChargedParty},
    10: {"name": "exchangeIdentity", "type": dt.ExchangeIdentity},
    11: {"name": "mSCIdentification", "type": dt.AddressString},
    12: {"name": "outgoingRoute", "type": dt.Route},
    13: {"name": "firstCalledLocationInformation", "type": dt.LocationInformation},
    14: {"name": "teleServiceCode", "type": dt.TeleServiceCode},
    15: {"name": "serviceCentreAddress", "type": dt.AddressString},
    18: {"name": "iCIOrdered", "type": dt.Bool},  # NULL type
    19: {"name": "outputForSubscriber", "type": dt.OutputForSubscriber},
    20: {"name": "miscellaneousInformation", "type": dt.MiscellaneousInformation},
    21: {"name": "regionalServiceUsed", "type": dt.RegionalServiceUsed},
    22: {"name": "regionDependentChargingOrigin", "type": dt.ChargingOrigin},
    23: {
        "name": "channelAllocationPriorityLevel",
        "type": dt.ChannelAllocationPriorityLevel,
    },
    24: {"name": "incompleteCallDataIndicator", "type": dt.Bool},  # NULL type
    25: {"name": "restartDuringOutputIndicator", "type": dt.Bool},  # NULL type
    26: {"name": "frequencyBandSupported", "type": dt.FrequencyBandSupported},
    27: {"name": "forloppDuringOutputIndicator", "type": dt.Bool},  # NULL type
    28: {"name": "numberOfShortMessages", "type": dt.NumberOfShortMessage},
    29: {"name": "lastCalledLocationInformation", "type": dt.LocationInformation},
    30: {"name": "positionAccuracy", "type": dt.PositionAccuracy},
    # 31: {"name": "userTerminalPosition", "type": dt.UserTerminalPosition},
    32: {"name": "switchIdentity", "type": dt.SwitchIdentity},
    # 33: {"name": "originatingAddress", "type": dt.AddressStringExtended},
    34: {"name": "messageTypeIndicator", "type": dt.MessageTypeIndicator},
    # 35: {"name": "rNCidOfFirstRNC", "type": dt.TargetRNCid},
    102: {"name": "outputType", "type": dt.OutputType},
}

MSTerminatingSMSinSMSGMSC = {
    0: {"name": "tAC", "type": dt.TAC},
    1: {"name": "callIdentificationNumber", "type": dt.CallIDNumber},
    2: {"name": "recordSequenceNumber", "type": dt.RecordSequenceNumber},
    3: {"name": "calledPartyNumber", "type": dt.AddressString},
    4: {"name": "calledSubscriberIMSI", "type": dt.IMSI},
    5: {"name": "mobileStationRoamingNumber", "type": dt.AddressString},
    6: {"name": "dateForStartOfCharge", "type": dt.Date},
    7: {"name": "timeForStartOfCharge", "type": dt.Time},
    8: {"name": "chargedParty", "type": dt.ChargedParty},
    9: {"name": "exchangeIdentity", "type": dt.ExchangeIdentity},
    10: {"name": "mSCIdentification", "type": dt.AddressString},
    11: {"name": "teleServiceCode", "type": dt.TeleServiceCode},
    12: {"name": "serviceCentreAddress", "type": dt.AddressString},
    13: {"name": "mSCNumber", "type": dt.AddressString},
    14: {"name": "miscellaneousInformation", "type": dt.MiscellaneousInformation},
    15: {"name": "incompleteCallDataIndicator", "type": dt.Bool},  # NULL type
    16: {"name": "restartDuringOutputIndicator", "type": dt.Bool},  # NULL type
    17: {"name": "forloppDuringOutputIndicator", "type": dt.Bool},  # NULL type
    # 18: {"name": "numberOfShortMessages", "type": dt.NumberOfShortMessage},
    19: {"name": "switchIdentity", "type": dt.SwitchIdentity},
    102: {"name": "outputType", "type": dt.OutputType},
}

SSProcedure = {
    0: {"name": "tAC", "type": dt.TAC},
    1: {"name": "callIdentificationNumber", "type": dt.CallIDNumber},
    2: {"name": "recordSequenceNumber", "type": dt.RecordSequenceNumber},
    3: {"name": "typeOfCallingSubscriber", "type": dt.TypeOfCallingSubscriber},
    4: {"name": "callingPartyNumber", "type": dt.AddressString},
    5: {"name": "callingSubscriberIMSI", "type": dt.IMSI},
    6: {"name": "callingSubscriberIMEI", "type": dt.IMEI},
    7: {"name": "dateForStartOfCharge", "type": dt.Date},
    8: {"name": "timeForStartOfCharge", "type": dt.Time},
    9: {"name": "originForCharging", "type": dt.ChargingOrigin},
    10: {"name": "exchangeIdentity", "type": dt.ExchangeIdentity},
    11: {"name": "mSCIdentification", "type": dt.AddressString},
    12: {"name": "firstCallingLocationInformation", "type": dt.LocationInformation},
    15: {"name": "iCIOrdered", "type": dt.Bool},  # NULL type
    16: {"name": "outputForSubscriber", "type": dt.OutputForSubscriber},
    17: {"name": "sSCode", "type": dt.SSCode},
    18: {"name": "sSRequest", "type": dt.SSRequest},
    19: {"name": "miscellaneousInformation", "type": dt.MiscellaneousInformation},
    20: {"name": "regionalServiceUsed", "type": dt.RegionalServiceUsed},
    21: {"name": "regionDependentChargingOrigin", "type": dt.ChargingOrigin},
    22: {"name": "relatedCallNumber", "type": dt.CallIDNumber},
    23: {"name": "uSSDApplicationIdentifier", "type": dt.ApplicationIdentifier},
    24: {"name": "uSSDServiceCode", "type": dt.ServiceCode},
    # 25: {"name": "uSSDProcedureCode", "type": dt.ProcedureCode},
    26: {"name": "networkInitiatedUSSDOperations", "type": dt.NumberOfOperations},
    # 27: {"name": "uSSDOperationIdentifier", "type": dt.OperationIdentifier},
    28: {"name": "incompleteCallDataIndicator", "type": dt.Bool},  # NULL type
    29: {"name": "restartDuringOutputIndicator", "type": dt.Bool},  # NULL type
    30: {"name": "frequencyBandSupported", "type": dt.FrequencyBandSupported},
    31: {"name": "forloppDuringOutputIndicator", "type": dt.Bool},  # NULL type
    32: {"name": "switchIdentity", "type": dt.SwitchIdentity},
    33: {"name": "networkCallReference", "type": dt.NetworkCallReference},
    34: {"name": "positionAccuracy", "type": dt.PositionAccuracy},
    # 35: {"name": "userTerminalPosition", "type": dt.UserTerminalPosition},
    # 36: {"name": "rNCidOfFirstRNC", "type": dt.TargetRNCid},
    102: {"name": "outputType", "type": dt.OutputType},
}

TransitINOutgoingCall = {
    0: {"name": "tAC", "type": dt.TAC},
    1: {"name": "callIdentificationNumber", "type": dt.CallIDNumber},
    2: {"name": "recordSequenceNumber", "type": dt.RecordSequenceNumber},
    3: {"name": "outgoingRoute", "type": dt.Route},
    4: {"name": "subscriptionType", "type": dt.SubscriptionType},
    5: {"name": "incompleteCallDataIndicator", "type": dt.Bool},  # NULL type
    6: {"name": "incompleteCompositeCDRIndicator", "type": dt.Bool},  # NULL type
    7: {"name": "lastPartialOutput", "type": dt.Bool},  # NULL type
    8: {"name": "partialOutputRecNum", "type": dt.PartialOutputRecNum},
    9: {"name": "restartDuringOutputIndicator", "type": dt.Bool},  # NULL type
    10: {"name": "exchangeIdentity", "type": dt.ExchangeIdentity},
    11: {"name": "restartDuringCall", "type": dt.Bool},  # NULL type
    12: {"name": "networkCallReference", "type": dt.NetworkCallReference},
    13: {"name": "iCIOrdered", "type": dt.Bool},  # NULL type
    14: {"name": "outputForSubscriber", "type": dt.OutputForSubscriber},
    15: {"name": "switchIdentity", "type": dt.SwitchIdentity},
    16: {"name": "disconnectionDueToSystemRecovery", "type": dt.Bool},  # NULL type
    17: {"name": "forloppDuringOutputIndicator", "type": dt.Bool},  # NULL type
    18: {"name": "tariffClass", "type": dt.TariffClass},
    19: {"name": "forloppReleaseDuringCall", "type": dt.Bool},  # NULL type
    # 20: {"name": "c7ChargingMessage", "type": dt.C7ChargingMessage}, # WCDMA Japan
    # 21: {"name": "c7FirstCHTMessage", "type": dt.C7CHTMessage}, # WCDMA Japan
    # 22: {"name": "c7SecondCHTMessage", "type": dt.C7CHTMessage}, # WCDMA Japan
    23: {"name": "contractorNumber", "type": dt.AddressString},
    24: {"name": "calledPartyMNPInfo", "type": dt.AddressString},
    102: {"name": "outputType", "type": dt.OutputType},
}

INIncomingCall = {
    0: {"name": "callIdentificationNumber", "type": dt.CallIDNumber},
    1: {"name": "switchIdentity", "type": dt.SwitchIdentity},
    2: {"name": "networkCallReference", "type": dt.NetworkCallReference},
    3: {"name": "iNServiceTrigger", "type": dt.INServiceTrigger},
    4: {"name": "sSFChargingCase", "type": dt.SSFChargingCase},
    5: {"name": "triggerData0", "tag": "triggerData", "type": dt.TriggerData},
    6: {"name": "triggerData1", "tag": "triggerData", "type": dt.TriggerData},
    7: {"name": "triggerData2", "tag": "triggerData", "type": dt.TriggerData},
    8: {"name": "triggerData3", "tag": "triggerData", "type": dt.TriggerData},
    9: {"name": "triggerData4", "tag": "triggerData", "type": dt.TriggerData},
    10: {"name": "triggerData5", "tag": "triggerData", "type": dt.TriggerData},
    11: {"name": "triggerData6", "tag": "triggerData", "type": dt.TriggerData},
    12: {"name": "triggerData7", "tag": "triggerData", "type": dt.TriggerData},
    13: {"name": "recordSequenceNumber", "type": dt.RecordSequenceNumber},
    14: {"name": "disconnectionDueToSystemRecovery", "type": dt.Bool},  # NULL type
    15: {"name": "incompleteCallDataIndicator", "type": dt.Bool},  # NULL type
    16: {"name": "incompleteCompositeCDRIndicator", "type": dt.Bool},  # NULL type
    17: {"name": "lastPartialOutput", "type": dt.Bool},  # NULL type
    18: {"name": "partialOutputRecNum", "type": dt.PartialOutputRecNum},
    19: {"name": "restartDuringOutputIndicator", "type": dt.Bool},  # NULL type
    20: {"name": "restartDuringCall", "type": dt.Bool},  # NULL type
    21: {"name": "exchangeIdentity", "type": dt.ExchangeIdentity},
    22: {"name": "forloppDuringOutputIndicator", "type": dt.Bool},  # NULL type
    23: {"name": "forloppReleaseDuringCall", "type": dt.Bool},  # NULL type
    24: {"name": "gSMCallReferenceNumber", "type": dt.GSMCallReferenceNumber},
    25: {"name": "mSCAddress", "type": dt.AddressString},
    26: {"name": "defaultCallHandling", "type": dt.DefaultCallHandling},
    27: {"name": "defaultCallHandling2", "type": dt.DefaultCallHandling},
    102: {"name": "outputType", "type": dt.OutputType},
}

INOutgoingCall = {
    0: {"name": "callIdentificationNumber", "type": dt.CallIDNumber},
    1: {"name": "switchIdentity", "type": dt.SwitchIdentity},
    2: {"name": "networkCallReference", "type": dt.NetworkCallReference},
    3: {"name": "iNServiceTrigger", "type": dt.INServiceTrigger},
    4: {"name": "sSFChargingCase", "type": dt.SSFChargingCase},
    5: {"name": "triggerData0", "type": dt.TriggerData},
    6: {"name": "triggerData1", "type": dt.TriggerData},
    7: {"name": "triggerData2", "type": dt.TriggerData},
    8: {"name": "triggerData3", "type": dt.TriggerData},
    9: {"name": "triggerData4", "type": dt.TriggerData},
    10: {"name": "triggerData5", "type": dt.TriggerData},
    11: {"name": "triggerData6", "type": dt.TriggerData},
    12: {"name": "triggerData7", "type": dt.TriggerData},
    13: {"name": "recordSequenceNumber", "type": dt.RecordSequenceNumber},
    14: {"name": "disconnectionDueToSystemRecovery", "type": dt.Bool},  # NULL type
    15: {"name": "incompleteCallDataIndicator", "type": dt.Bool},  # NULL type
    16: {"name": "incompleteCompositeCDRIndicator", "type": dt.Bool},  # NULL type
    17: {"name": "lastPartialOutput", "type": dt.Bool},  # NULL type
    18: {"name": "partialOutputRecNum", "type": dt.PartialOutputRecNum},
    19: {"name": "restartDuringOutputIndicator", "type": dt.Bool},  # NULL type
    20: {"name": "restartDuringCall", "type": dt.Bool},  # NULL type
    21: {"name": "exchangeIdentity", "type": dt.ExchangeIdentity},
    22: {"name": "forloppDuringOutputIndicator", "type": dt.Bool},  # NULL type
    23: {"name": "forloppReleaseDuringCall", "type": dt.Bool},  # NULL type
    24: {"name": "gSMCallReferenceNumber", "type": dt.GSMCallReferenceNumber},
    25: {"name": "mSCAddress", "type": dt.AddressString},
    26: {"name": "defaultCallHandling", "type": dt.DefaultCallHandling},
    27: {"name": "defaultCallHandling2", "type": dt.DefaultCallHandling},
    102: {"name": "outputType", "type": dt.OutputType},
}

ISDNOriginating = {
    # 0: {"name": "trafficActivityCode", "type": dt.TrafficActivityCode},
    1: {"name": "callIdentificationNumber", "type": dt.CallIDNumber},
    2: {"name": "recordSequenceNumber", "type": dt.RecordSequenceNumber},
    3: {"name": "typeOfCallingSubscriber", "type": dt.TypeOfCallingSubscriber},
    4: {"name": "chargedCallingPartyNumber", "type": dt.AddressString},
    5: {"name": "calledPartyNumber", "type": dt.AddressString},
    6: {"name": "disconnectingParty", "type": dt.DisconnectingParty},
    7: {"name": "dateForStartOfCharge", "type": dt.Date},
    8: {"name": "timeForStartOfCharge", "type": dt.Time},
    9: {"name": "timeForStopOfCharge", "type": dt.Time},
    10: {"name": "chargeableDuration", "type": dt.Time},
    11: {"name": "interruptionTime", "type": dt.Time},
    12: {"name": "tariffClass", "type": dt.TariffClass},
    13: {"name": "tariffSwitchInd", "type": dt.TariffSwitchInd},
    14: {"name": "exchangeIdentity", "type": dt.ExchangeIdentity},
    15: {"name": "outgoingRoute", "type": dt.Route},
    16: {"name": "callPosition", "type": dt.CallPosition},
    17: {"name": "restartDuringCall", "type": dt.Bool},  # NULL type
    18: {"name": "restartDuringOutputIndicator", "type": dt.Bool},  # NULL type
    19: {"name": "lastPartialOutput", "type": dt.Bool},  # NULL type
    20: {"name": "partialOutputRecNum", "type": dt.PartialOutputRecNum},
    21: {"name": "cUGInterlockCode", "type": dt.CUGInterlockCode},
    22: {"name": "cUGIndex", "type": dt.CUGIndex},
    23: {
        "name": "presentationAndScreeningIndicator",
        "type": dt.PresentationAndScreeningIndicator,
    },
    24: {"name": "incompleteCallDataIndicator", "type": dt.Bool},  # NULL type
    25: {"name": "networkCallReference", "type": dt.NetworkCallReference},
    26: {"name": "disconnectionDueToSystemRecovery", "type": dt.Bool},  # NULL type
    27: {"name": "forloppDuringOutputIndicator", "type": dt.Bool},  # NULL type
    # 28: {"name": "causeCode", "type": dt.CauseCode},
    # 29: {"name": "locationCode", "type": dt.LocationCode},
    30: {"name": "networkProvidedCallingPartyNumber", "type": dt.AddressString},
    32: {
        "name": "callingPartyNumberSpecialArrangementInd",
        "type": dt.Bool,
    },  # NULL type
    33: {"name": "userProvidedCallingPartyNumber", "type": dt.AddressString},
    34: {"name": "forloppReleaseDuringCall", "type": dt.Bool},  # NULL type
    35: {"name": "chargedParty", "type": dt.ChargedParty},
    36: {"name": "callAttemptIndicator", "type": dt.Bool},  # NULL type
    # 37: {"name": "flexibleCounter1", "type": dt.Counter}, # WCDMA Japan
    # 38: {"name": "flexibleCounter2", "type": dt.Counter}, # WCDMA Japan
    # 39: {"name": "flexibleCounter3", "type": dt.Counter}, # WCDMA Japan
    # 40: {"name": "flexibleCounter4", "type": dt.Counter}, # WCDMA Japan
    # 41: {"name": "flexibleCounter5", "type": dt.Counter}, # WCDMA Japan
    # 42: {"name": "flexibleCounter6", "type": dt.Counter}, # WCDMA Japan
    # 43: {"name": "flexibleCounter7", "type": dt.Counter}, # WCDMA Japan
    # 44: {"name": "flexibleCounter8", "type": dt.Counter}, # WCDMA Japan
    45: {"name": "callAttemptState", "type": dt.CallAttemptState},
    46: {"name": "typeOfSignalling", "type": dt.TypeOfSignalling},
    47: {"name": "typeOfCalledSubscriber", "type": dt.TypeOfCalledSubscriber},
    # 48: {"name": "endToEndAccessDataMap", "type": dt.EndToEndAccessDataMap},
    # 49: {
    #     "name": "userToUserService1Information",
    #     "type": dt.UserToUserService1Information,
    # },
    50: {"name": "switchIdentity", "type": dt.SwitchIdentity},
    # 51: {"name": "aoCCurrencyAmountSentToUser", "type": dt.AoCCurrencyAmountSent},
    102: {"name": "outputType", "type": dt.OutputType},
}

ISDNCallForwarding = {
    # 0: {"name": "trafficActivityCode", "type": dt.TrafficActivityCode},
    1: {"name": "callIdentificationNumber", "type": dt.CallIDNumber},
    2: {"name": "recordSequenceNumber", "type": dt.RecordSequenceNumber},
    3: {"name": "typeOfCallingSubscriber", "type": dt.TypeOfCallingSubscriber},
    4: {"name": "chargedCallingPartyNumber", "type": dt.AddressString},
    5: {"name": "calledPartyNumber", "type": dt.AddressString},
    6: {"name": "disconnectingParty", "type": dt.DisconnectingParty},
    7: {"name": "dateForStartOfCharge", "type": dt.Date},
    8: {"name": "timeForStartOfCharge", "type": dt.Time},
    9: {"name": "timeForStopOfCharge", "type": dt.Time},
    10: {"name": "chargeableDuration", "type": dt.Time},
    11: {"name": "interruptionTime", "type": dt.Time},
    12: {"name": "tariffClass", "type": dt.TariffClass},
    13: {"name": "tariffSwitchInd", "type": dt.TariffSwitchInd},
    14: {"name": "exchangeIdentity", "type": dt.ExchangeIdentity},
    15: {"name": "outgoingRoute", "type": dt.Route},
    16: {"name": "callPosition", "type": dt.CallPosition},
    17: {"name": "originalCalledNumber", "type": dt.AddressString},
    18: {"name": "redirectingNumber", "type": dt.AddressString},
    19: {"name": "restartDuringCall", "type": dt.Bool},  # NULL type
    20: {"name": "restartDuringOutputIndicator", "type": dt.Bool},  # NULL type
    21: {"name": "lastPartialOutput", "type": dt.Bool},  # NULL type
    22: {"name": "partialOutputRecNum", "type": dt.PartialOutputRecNum},
    23: {"name": "cUGInterlockCode", "type": dt.CUGInterlockCode},
    24: {"name": "cUGIndex", "type": dt.CUGIndex},
    25: {
        "name": "presentationAndScreeningIndicator",
        "type": dt.PresentationAndScreeningIndicator,
    },
    26: {"name": "incompleteCallDataIndicator", "type": dt.Bool},  # NULL type
    27: {"name": "networkCallReference", "type": dt.NetworkCallReference},
    28: {"name": "disconnectionDueToSystemRecovery", "type": dt.Bool},  # NULL type
    29: {"name": "forloppDuringOutputIndicator", "type": dt.Bool},  # NULL type
    # 30: {"name": "causeCode", "type": dt.CauseCode},
    # 31: {"name": "locationCode", "type": dt.LocationCode},
    32: {"name": "networkProvidedCallingPartyNumber", "type": dt.AddressString},
    33: {"name": "callingPartyNumber", "type": dt.AddressString},
    35: {"name": "forloppReleaseDuringCall", "type": dt.Bool},  # NULL type
    36: {"name": "chargedParty", "type": dt.ChargedParty},
    37: {"name": "callAttemptIndicator", "type": dt.Bool},  # NULL type
    # 38: {"name": "flexibleCounter1", "type": dt.Counter}, # WCDMA Japan
    # 39: {"name": "flexibleCounter2", "type": dt.Counter}, # WCDMA Japan
    # 40: {"name": "flexibleCounter3", "type": dt.Counter}, # WCDMA Japan
    # 41: {"name": "flexibleCounter4", "type": dt.Counter}, # WCDMA Japan
    # 42: {"name": "flexibleCounter5", "type": dt.Counter}, # WCDMA Japan
    # 43: {"name": "flexibleCounter6", "type": dt.Counter}, # WCDMA Japan
    # 44: {"name": "flexibleCounter7", "type": dt.Counter}, # WCDMA Japan
    # 45: {"name": "flexibleCounter8", "type": dt.Counter}, # WCDMA Japan
    46: {"name": "callAttemptState", "type": dt.CallAttemptState},
    47: {"name": "typeOfSignalling", "type": dt.TypeOfSignalling},
    48: {"name": "typeOfCalledSubscriber", "type": dt.TypeOfCalledSubscriber},
    # 49: {"name": "endToEndAccessDataMap", "type": dt.EndToEndAccessDataMap},
    # 50: {
    #     "name": "userToUserService1Information",
    #     "type": dt.UserToUserService1Information,
    # },
    51: {"name": "switchIdentity", "type": dt.SwitchIdentity},
    # 52: {"name": "aoCCurrencyAmountSentToUser", "type": dt.AoCCurrencyAmountSent},
    102: {"name": "outputType", "type": dt.OutputType},
}

ISDNSSProcedure = {
    # 0: {"name": "trafficActivityCode", "type": dt.TrafficActivityCode},
    1: {"name": "callIdentificationNumber", "type": dt.CallIDNumber},
    2: {"name": "recordSequenceNumber", "type": dt.RecordSequenceNumber},
    3: {"name": "typeOfCallingSubscriber", "type": dt.TypeOfCallingSubscriber},
    4: {"name": "dateForStartOfCharge", "type": dt.Date},
    5: {"name": "timeForStartOfCharge", "type": dt.Time},
    6: {"name": "tariffClass", "type": dt.TariffClass},
    7: {"name": "exchangeIdentity", "type": dt.ExchangeIdentity},
    8: {"name": "restartDuringOutputIndicator", "type": dt.Bool},  # NULL type
    9: {"name": "incompleteCallDataIndicator", "type": dt.Bool},  # NULL type
    10: {"name": "forloppDuringOutputIndicator", "type": dt.Bool},  # NULL type
    11: {"name": "servedSubscriberNumber", "type": dt.AddressString},
    12: {"name": "chargedParty", "type": dt.ChargedParty},
    13: {"name": "switchIdentity", "type": dt.SwitchIdentity},
    102: {"name": "outputType", "type": dt.OutputType},
}

SCFChargingOutput = {
    0: {"name": "callIdentificationNumber", "type": dt.CallIDNumber},
    1: {"name": "exchangeIdentity", "type": dt.ExchangeIdentity},
    2: {"name": "gSMCallReferenceNumber", "type": dt.GSMCallReferenceNumber},
    3: {"name": "restartDuringCall", "type": dt.Bool},  # NULL type
    4: {"name": "restartDuringOutputIndicator", "type": dt.Bool},  # NULL type
    5: {"name": "lastPartialOutput", "type": dt.Bool},  # NULL type
    6: {"name": "partialOutputRecNum", "type": dt.PartialOutputRecNum},
    7: {"name": "switchIdentity", "type": dt.SwitchIdentity},
    8: {"name": "disconnectionDueToSystemRecovery", "type": dt.Bool},  # NULL type
    9: {"name": "forloppDuringOutputIndicator", "type": dt.Bool},  # NULL type
    10: {"name": "forloppReleaseDuringCall", "type": dt.Bool},  # NULL type
    11: {"name": "recordSequenceNumber", "type": dt.RecordSequenceNumber},
    12: {"name": "incompleteCallDataIndicator", "type": dt.Bool},  # NULL type
    13: {"name": "mSCAddress", "type": dt.AddressString},
    14: {"name": "date", "type": dt.Date},
    102: {"name": "outputType", "type": dt.OutputType},
}

LocationServices = {
    0: {"name": "tAC", "type": dt.TAC},
    1: {"name": "callIdentificationNumber", "type": dt.CallIDNumber},
    2: {"name": "recordSequenceNumber", "type": dt.RecordSequenceNumber},
    3: {"name": "typeOfCallingSubscriber", "type": dt.TypeOfCallingSubscriber},
    4: {"name": "targetMSISDN", "type": dt.AddressString},
    5: {"name": "targetIMSI", "type": dt.IMSI},
    6: {"name": "targetIMEI", "type": dt.IMEI},
    7: {"name": "dateForStartOfCharge", "type": dt.Date},
    8: {"name": "timeForStartOfCharge", "type": dt.Time},
    9: {"name": "exchangeIdentity", "type": dt.ExchangeIdentity},
    10: {"name": "mSCIdentification", "type": dt.AddressString},
    11: {"name": "miscellaneousInformation", "type": dt.MiscellaneousInformation},
    12: {"name": "restartDuringOutputIndicator", "type": dt.Bool},  # NULL type
    13: {"name": "iCIOrdered", "type": dt.Bool},  # NULL type
    14: {"name": "outputForSubscriber", "type": dt.OutputForSubscriber},
    15: {"name": "incompleteCallDataIndicator", "type": dt.Bool},  # NULL type
    16: {"name": "switchIdentity", "type": dt.SwitchIdentity},
    17: {"name": "networkCallReference", "type": dt.NetworkCallReference},
    18: {"name": "forloppDuringOutputIndicator", "type": dt.Bool},  # NULL type
    # 19: {"name": "positioningDelivery", "type": dt.PositioningDelivery},
    20: {"name": "lCSClientIdentity", "type": dt.AddressString},
    21: {"name": "lCSClientType", "type": dt.LCSClientType},
    # 22: {"name": "locationEstimate", "type": dt.LocationEstimate},
    # 23: {"name": "ageOfLocationEstimate", "type": dt.AgeOfLocationEstimate},
    24: {"name": "subscriberState", "type": dt.SubscriberState},
    25: {"name": "mLCAddress", "type": dt.AddressString},
    # 26: {"name": "decipheringKeys", "type": dt.DecipheringKeys},
    27: {"name": "typeOfLocationRequest", "type": dt.TypeOfLocationRequest},
    28: {"name": "firstTargetLocationInformation", "type": dt.LocationInformation},
    # 29: {"name": "horizontalAccuracy", "type": dt.LCSAccuracy},
    30: {"name": "responseTimeCategory", "type": dt.ResponseTimeCategory},
    # 31: {"name": "verticalAccuracy", "type": dt.LCSAccuracy},
    32: {"name": "verticalCoordinateRequest", "type": dt.Bool},  # NULL type
    33: {
        "name": "unsuccessfulPositioningDataReason",
        "type": dt.UnsuccessfulPositioningDataReason,
    },
    102: {"name": "outputType", "type": dt.OutputType},
}

# Event Modules

AoCEventModule = {
    0: {"name": "tAC", "type": dt.TAC},
    # 1: {"name": "cRIToMS", "type": dt.CRIToMS},
    2: {"name": "cRIIndicator", "type": dt.CRIIndicator},
    3: {"name": "sSCode", "type": dt.SSCode},
    4: {"name": "timeForEvent", "type": dt.Time},
    5: {"name": "incompleteCallDataIndicator", "type": dt.Bool},  # NULL type
    6: {"name": "gsmSCFControlOfAoC", "type": dt.Bool},  # NULL type
}

SSIEventModule = {
    0: {"name": "tAC", "type": dt.TAC},
    1: {"name": "sSCode", "type": dt.SSCode},
    2: {"name": "sSRequest", "type": dt.SSRequest},
    3: {"name": "timeForEvent", "type": dt.Time},
    4: {"name": "firstCallingLocationInformation", "type": dt.LocationInformation},
    5: {"name": "cRIIndicator", "type": dt.CRIIndicator},
    # 6: {"name": "eventCRIToMS", "type": dt.EventCRIToMS},
    7: {"name": "incompleteCallDataIndicator", "type": dt.Bool},  # NULL type
    9: {"name": "networkCallReference", "type": dt.NetworkCallReference},
    10: {"name": "sSInvocationNotification", "type": dt.Bool},  # NULL type
}

ServiceSwitchEventModule = {
    0: {"name": "tAC", "type": dt.TAC},
    1: {"name": "timeForEvent", "type": dt.Time},
    2: {"name": "serviceSwitchingType", "type": dt.ServiceSwitchingType},
    3: {"name": "incompleteCallDataIndicator", "type": dt.Bool},  # NULL type
}

INServiceDataEventModule = {
    # 0: {"name": "chargePartyDistributed", "type": dt.Distributed},
    1: {"name": "chargePartySingle", "type": dt.Single},
    # 2: {"name": "chargingUnitsAddition", "type": dt.ChargingUnitsAddition},
    # 3: {"name": "genericChargingDigits", "type": dt.GenericDigitsSet},
    # 4: {"name": "genericChargingNumbers", "type": dt.GenericNumbersSet},
    # 5: {"name": "serviceFeatureCode", "type": dt.ServiceFeatureCode},
    6: {"name": "timeForEvent", "type": dt.Time},
    7: {"name": "incompleteCallDataIndicator", "type": dt.Bool},  # NULL type
    8: {"name": "freeFormatData", "type": dt.FreeFormatData},
    9: {"name": "sSFLegID", "type": dt.LegID},
    10: {"name": "freeFormatData2", "type": dt.FreeFormatData},
    11: {"name": "freeFormatDataAppendIndicator", "type": dt.Bool},  # NULL type
    12: {"name": "freeFormatDataAppendIndicator2", "type": dt.Bool},  # NULL type
}

ChargeRateChangeEventModule = {
    0: {"name": "tAC", "type": dt.TAC},
    1: {"name": "timeForEvent", "type": dt.Time},
    2: {"name": "radioChannelProperty", "type": dt.RadioChannelProperty},
    3: {"name": "changeInitiatingParty", "type": dt.ChangeInitiatingParty},
    4: {"name": "tariffClass", "type": dt.TariffClass},
    7: {"name": "aIURRequested", "type": dt.AirInterfaceUserRate},
    8: {"name": "numberOfChannelsRequested", "type": dt.NumberOfChannels},
    # 9: {"name": "channelCodingUsed", "type": dt.ChannelCodings},
}

ISDNSSInvocationEventModule = {
    # 0: {"name": "trafficActivityCode", "type": dt.TrafficActivityCode},
    1: {"name": "incompleteCallDataIndicator", "type": dt.Bool},  # NULL type
}

handOverEventModule = {
    0: {"name": "tAC", "type": dt.TAC},
    1: {"name": "timeForEvent", "type": dt.Time},
    # 2: {"name": "rNCidOfTargetRNC", "type": dt.TargetRNCid},
    3: {"name": "incompleteCallDataIndicator", "type": dt.Bool},  # NULL type
    4: {"name": "targetLocationInformation", "type": dt.LocationInformation},
    5: {"name": "radioChannelProperty", "type": dt.RadioChannelProperty},
    # 6: {"name": "channelCodingUsed", "type": dt.ChannelCodings},
}

EventModule = {
    10: {"name": "aoCEventModule", "type": AoCEventModule},
    11: {"name": "sSInvocationEventModule", "type": SSIEventModule},
    12: {"name": "serviceSwitchEventModule", "type": ServiceSwitchEventModule},
    16: {"name": "iNServiceDataEventModule", "type": INServiceDataEventModule},
    20: {"name": "chargeRateChangeEventModule", "type": ChargeRateChangeEventModule},
    23: {"name": "iSDNSSInvocationEventModule", "type": ISDNSSInvocationEventModule},
    25: {"name": "handOverEventModule", "type": handOverEventModule},
}
UMTSGSMPLMNCallDataRecord = {
    0: {"name": "transit", "tag": "CallModule", "type": Transit},
    1: {"name": "msOriginating", "tag": "CallModule", "type": MSOriginating},
    2: {
        "name": "roamingCallForwarding",
        "tag": "CallModule",
        "type": RoamingCallForwarding,
    },
    3: {"name": "callForwarding", "tag": "CallModule", "type": CallForwarding},
    4: {"name": "msTerminating", "tag": "CallModule", "type": MSTerminating},
    5: {
        "name": "msOriginatingSMSinMSC",
        "tag": "CallModule",
        "type": MSOriginatingSMSinMSC,
    },
    6: {
        "name": "msOriginatingSMSinSMSIWMSC",
        "tag": "CallModule",
        "type": MSOriginatingSMSinSMSIWMSC,
    },
    7: {
        "name": "msTerminatingSMSinMSC",
        "tag": "CallModule",
        "type": MSTerminatingSMSinMSC,
    },
    8: {
        "name": "msTerminatingSMSinSMSGMSC",
        "tag": "CallModule",
        "type": MSTerminatingSMSinSMSGMSC,
    },
    9: {"name": "sSProcedure", "tag": "CallModule", "type": SSProcedure},
    13: {
        "name": "transitINOutgoingCall",
        "tag": "CallModule",
        "type": TransitINOutgoingCall,
    },
    14: {"name": "iNIncomingCall", "tag": "CallModule", "type": INIncomingCall},
    15: {"name": "iNOutgoingCall", "tag": "CallModule", "type": INOutgoingCall},
    17: {"name": "iSDNOriginating", "tag": "CallModule", "type": ISDNOriginating},
    18: {
        "name": "iSDNCallForwarding",
        "tag": "CallModule",
        "type": ISDNCallForwarding,
    },
    19: {"name": "iSDNSSProcedure", "tag": "CallModule", "type": ISDNSSProcedure},
    21: {"name": "sCFChargingOutput", "tag": "CallModule", "type": SCFChargingOutput},
    24: {
        "name": "locationServices",
        "tag": "CallModule",
        "type": LocationServices,
    },
    10: {"name": "aoCEventModule", "tag": "CallModule", "type": AoCEventModule},
    11: {"name": "sSIEventModule", "tag": "CallModule", "type": SSIEventModule},
    12: {
        "name": "serviceSwitchEventModule",
        "tag": "CallModule",
        "type": ServiceSwitchEventModule,
    },
    16: {
        "name": "iNServiceDataEventModule",
        "tag": "CallModule",
        "type": INServiceDataEventModule,
    },
    20: {
        "name": "chargeRateChangeEventModule",
        "tag": "CallModule",
        "type": ChargeRateChangeEventModule,
    },
    23: {
        "name": "iSDNSSInvocationEventModule",
        "tag": "CallModule",
        "type": ISDNSSInvocationEventModule,
    },
    25: {
        "name": "handOverEventModule",
        "tag": "CallModule",
        "type": handOverEventModule,
    },
}

CompositeDataRecord = {
    0: {
        "name": "singleDataRecord",
        "tag": "CallDataRecord",
        "type": UMTSGSMPLMNCallDataRecord,
    },
}

CallDataRecord = {
    0: {
        "name": "singleDataRecord",
        "tag": "CallDataRecord",
        "type": UMTSGSMPLMNCallDataRecord,
    },
    1: {
        "name": "compositeCallDataRecord",
        "tag": "CallDataRecord",
        "type": CompositeDataRecord,
    },
}
