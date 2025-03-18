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
    15: {"name": "originForCharging", "type": ChargingOrigin},
    16: {"name": "tariffClass", "type": TariffClass},
    17: {"name": "tariffSwitchInd", "type": TariffSwitchInd},
    18: {"name": "numberOfMeterPulses", "type": NumberOfMeterPulses},
    19: {"name": "exchangeIdentity", "type": ExchangeIdentity},
    20: {"name": "mSCIdentification", "type": dt.AddressString},
    21: {"name": "outgoingRoute", "type": Route},
    22: {"name": "incomingRoute", "type": Route},
    23: {"name": "miscellaneousInformation", "type": MiscellaneousInformation},
    25: {"name": "iNMarkingOfMS", "type": INMarkingOfMS},
    26: {"name": "callPosition", "type": dt.CallPosition},
    27: {"name": "eosInfo", "type": EosInfo},
    28: {"name": "internalCauseAndLoc", "type": InternalCauseAndLoc},
    29: {"name": "originalCalledNumber", "type": dt.AddressString},
    30: {"name": "redirectingNumber", "type": dt.AddressString},
    31: {"name": "redirectionCounter", "type": RedirectionCounter},
    32: {"name": "redirectingDropBackNumber", "type": dt.AddressString},
    33: {"name": "redirectingDropBack", "type": dt.Bool},  # NULL type
    34: {"name": "restartDuringCall", "type": dt.Bool},  # NULL type
    35: {"name": "restartDuringOutputIndicator", "type": dt.Bool},  # NULL type
    36: {"name": "iCIOrdered", "type": dt.Bool},  # NULL type
    37: {"name": "outputForSubscriber", "type": OutputForSubscriber},
    38: {"name": "lastPartialOutput", "type": dt.Bool},  # NULL type
    39: {"name": "partialOutputRecNum", "type": PartialOutputRecNum},
    40: {"name": "relatedCallNumber", "type": CallIDNumber},
    41: {"name": "faultCode", "type": FaultCode},
    42: {"name": "subscriptionType", "type": SubscriptionType},
    43: {"name": "incompleteCallDataIndicator", "type": dt.Bool},  # NULL type
    44: {"name": "incompleteCompositeCDRIndicator", "type": dt.Bool},  # NULL type
    45: {"name": "switchIdentity", "type": SwitchIdentity},
    46: {"name": "networkCallReference", "type": NetworkCallReference},
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
    62: {"name": "c7ChargingMessage", "type": C7ChargingMessage},
    63: {"name": "c7FirstCHTMessage", "type": C7CHTMessage},
    64: {"name": "c7SecondCHTMessage", "type": C7CHTMessage},
    65: {"name": "aCMChargingIndicator", "type": dt.ChargingIndicator},
    66: {"name": "aNMChargingIndicator", "type": dt.ChargingIndicator},
    67: {"name": "mSCAddress", "type": dt.AddressString},
    68: {"name": "carrierInformationBackward", "type": TransitCarrierInfo},
    69: {"name": "carrierInformationForward", "type": TransitCarrierInfo},
    70: {"name": "chargeInformation", "type": ChargeInformation},
    71: {"name": "disconnectionDate", "type": dt.Date},
    72: {"name": "disconnectionTime", "type": dt.Time},
    73: {"name": "entryPOICA", "type": dt.ChargeAreaCode},
    74: {"name": "exitPOICA", "type": dt.ChargeAreaCode},
    75: {"name": "internationalCallIndicator", "type": dt.Bool},  # NULL type
    76: {"name": "mobileUserClass1", "type": MobileUserClass1},
    77: {"name": "mobileUserClass2", "type": MobileUserClass2},
    78: {"name": "originatingAccessISDN", "type": dt.Bool},  # NULL type
    79: {"name": "originatingCarrier", "type": CarrierInfo},
    80: {"name": "originatingChargeArea", "type": dt.ChargeAreaCode},
    81: {"name": "tDSCounter", "type": Counter},
    82: {"name": "terminatingAccessISDN", "type": dt.Bool},  # NULL type
    83: {"name": "terminatingCarrier", "type": CarrierInfo},
    84: {"name": "terminatingChargeArea", "type": dt.ChargeAreaCode},
    85: {"name": "terminatingMobileUserClass1", "type": MobileUserClass1},
    86: {"name": "terminatingMobileUserClass2", "type": MobileUserClass2},
    87: {"name": "contractorNumber", "type": dt.AddressString},
    88: {"name": "terminatingUserClass", "type": UserClass},
    89: {"name": "userClass", "type": UserClass},
    90: {"name": "calledPartyMNPInfo", "type": dt.AddressString},
    91: {"name": "chargeNumber", "type": dt.AddressString},
    92: {"name": "originatingLineInformation", "type": OriginatingLineInformation},
    93: {"name": "multimediaInformation", "type": MultimediaInformation},
    102: {"name": "outputType", "type": OutputType},
    24: {"name": "originatedCode", "type": OriginatedCode},
    121: {"name": "reroutingIndicator", "type": ReroutingIndicator},
}

MSOriginating = {}

UMTSGSMPLMNCallDataRecord = {
    0: {"name": "transit", "tag": "CallModule", "type": Transit}
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
