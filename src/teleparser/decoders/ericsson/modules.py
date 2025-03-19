from teleparser.decoders.ericsson import datatypes as dt

CAMELTDPData = {
    0: {"name": "serviceKey", "type": dt.ServiceKey},
    1: {"name": "gsmSCFAddress", "type": dt.GsmSCFAddress},
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
    51: {"name": "bCSMTDPData1", "type": CAMELTDPData},
    52: {"name": "bCSMTDPData2", "type": CAMELTDPData},
    53: {"name": "bCSMTDPData3", "type": CAMELTDPData},
    54: {"name": "bCSMTDPData4", "type": CAMELTDPData},
    55: {"name": "bCSMTDPData5", "type": CAMELTDPData},
    56: {"name": "bCSMTDPData6", "type": CAMELTDPData},
    57: {"name": "bCSMTDPData7", "type": CAMELTDPData},
    58: {"name": "bCSMTDPData8", "type": CAMELTDPData},
    59: {"name": "bCSMTDPData9", "type": CAMELTDPData},
    60: {"name": "bCSMTDPData10", "type": CAMELTDPData},
    61: {"name": "gSMCallReferenceNumber", "type": dt.GSMCallReferenceNumber},
    # 62: {"name": "c7ChargingMessage", "type": C7ChargingMessage},
    63: {"name": "c7FirstCHTMessage", "type": dt.C7CHTMessage},
    64: {"name": "c7SecondCHTMessage", "type": dt.C7CHTMessage},
    65: {"name": "aCMChargingIndicator", "type": dt.ChargingIndicator},
    66: {"name": "aNMChargingIndicator", "type": dt.ChargingIndicator},
    67: {"name": "mSCAddress", "type": dt.AddressString},
    # 68: {"name": "carrierInformationBackward", "type": TransitCarrierInfo},
    # 69: {"name": "carrierInformationForward", "type": TransitCarrierInfo},
    # 70: {"name": "chargeInformation", "type": ChargeInformation},
    71: {"name": "disconnectionDate", "type": dt.Date},
    72: {"name": "disconnectionTime", "type": dt.Time},
    73: {"name": "entryPOICA", "type": dt.ChargeAreaCode},
    74: {"name": "exitPOICA", "type": dt.ChargeAreaCode},
    75: {"name": "internationalCallIndicator", "type": dt.Bool},  # NULL type
    76: {"name": "mobileUserClass1", "type": dt.MobileUserClass1},
    # 77: {"name": "mobileUserClass2", "type": MobileUserClass2},
    78: {"name": "originatingAccessISDN", "type": dt.Bool},  # NULL type
    79: {"name": "originatingCarrier", "type": dt.CarrierInfo},
    80: {"name": "originatingChargeArea", "type": dt.ChargeAreaCode},
    # 81: {"name": "tDSCounter", "type": Counter},
    82: {"name": "terminatingAccessISDN", "type": dt.Bool},  # NULL type
    83: {"name": "terminatingCarrier", "type": dt.CarrierInfo},
    84: {"name": "terminatingChargeArea", "type": dt.ChargeAreaCode},
    85: {"name": "terminatingMobileUserClass1", "type": dt.MobileUserClass1},
    # 86: {"name": "terminatingMobileUserClass2", "type": MobileUserClass2},
    87: {"name": "contractorNumber", "type": dt.AddressString},
    88: {"name": "terminatingUserClass", "type": dt.UserClass},
    89: {"name": "userClass", "type": dt.UserClass},
    90: {"name": "calledPartyMNPInfo", "type": dt.AddressString},
    91: {"name": "chargeNumber", "type": dt.AddressString},
    92: {"name": "originatingLineInformation", "type": dt.OriginatingLineInformation},
    # 93: {"name": "multimediaInformation", "type": MultimediaInformation},
    102: {"name": "outputType", "type": dt.OutputType},
    24: {"name": "originatedCode", "type": dt.OriginatedCode},
    121: {"name": "reroutingIndicator", "type": dt.RerountingIndicator},
}

MSOriginating = {}

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
    # 44: {
    #     "name": "presentationAndScreeningIndicator",
    #     "type": dt.PresentationAndScreeningIndicator,
    # },
    45: {"name": "faultCode", "type": dt.FaultCode},
    46: {"name": "incompleteCallDataIndicator", "type": dt.Bool},  # NULL type
    48: {"name": "switchIdentity", "type": dt.SwitchIdentity},
    49: {"name": "networkCallReference", "type": dt.NetworkCallReference},
    50: {"name": "disconnectionDueToSystemRecovery", "type": dt.Bool},  # NULL type
    51: {"name": "forloppDuringOutputIndicator", "type": dt.Bool},  # NULL type
    52: {"name": "forloppReleaseDuringCall", "type": dt.Bool},  # NULL type
    53: {"name": "gSMCallReferenceNumber", "type": dt.GSMCallReferenceNumber},
    54: {"name": "mSCAddress", "type": dt.AddressString},
    # 55: {"name": "carrierInformationBackward", "type": dt.TransitCarrierInfo},
    56: {"name": "originatingAccessISDN", "type": dt.Bool},  # NULL type
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


UMTSGSMPLMNCallDataRecord = {
    0: {"name": "transit", "tag": "CallModule", "type": Transit},
    2: {
        "name": "roamingCallForwarding",
        "tag": "CallModule",
        "type": RoamingCallForwarding,
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
