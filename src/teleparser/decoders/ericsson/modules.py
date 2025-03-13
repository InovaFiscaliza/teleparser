from parameters import *

Transit = {
    0: {"name": "tAC", "type": TAC},
    1: {"name": "callIdentificationNumber", "type": CallIDNumber},
    2: {"name": "recordSequenceNumber", "type": RecordSequenceNumber},
    3: {"name": "typeOfCallingSubscriber", "type": TypeOfCallingSubscriber},
    4: {"name": "callingPartyNumber", "type": AddressString},
    5: {"name": "calledPartyNumber", "type": AddressString},
    6: {"name": "calledSubscriberIMSI", "type": IMSI},
    7: {"name": "disconnectingParty", "type": DisconnectingParty},
    8: {"name": "dateForStartOfCharge", "type": Date},
    9: {"name": "timeForStartOfCharge", "type": Time},
    10: {"name": "timeForStopOfCharge", "type": Time},
    11: {"name": "chargeableDuration", "type": Time},
    12: {"name": "interruptionTime", "type": Time},
    13: {"name": "timeFromRegisterSeizureToStartOfCharging", "type": Time},
    14: {"name": "chargedParty", "type": ChargedParty},
    15: {"name": "originForCharging", "type": ChargingOrigin},
    16: {"name": "tariffClass", "type": TariffClass},
    17: {"name": "tariffSwitchInd", "type": TariffSwitchInd},
    18: {"name": "numberOfMeterPulses", "type": NumberOfMeterPulses},
    19: {"name": "exchangeIdentity", "type": ExchangeIdentity},
    20: {"name": "mSCIdentification", "type": AddressString},
    21: {"name": "outgoingRoute", "type": Route},
    22: {"name": "incomingRoute", "type": Route},
    23: {"name": "miscellaneousInformation", "type": MiscellaneousInformation},
    25: {"name": "iNMarkingOfMS", "type": INMarkingOfMS},
    26: {"name": "callPosition", "type": CallPosition},
    27: {"name": "eosInfo", "type": EosInfo},
    28: {"name": "internalCauseAndLoc", "type": InternalCauseAndLoc},
    29: {"name": "originalCalledNumber", "type": AddressString},
    30: {"name": "redirectingNumber", "type": AddressString},
    31: {"name": "redirectionCounter", "type": RedirectionCounter},
    32: {"name": "redirectingDropBackNumber", "type": AddressString},
    33: {"name": "redirectingDropBack", "type": None},  # NULL type
    34: {"name": "restartDuringCall", "type": None},  # NULL type
    35: {"name": "restartDuringOutputIndicator", "type": None},  # NULL type
    36: {"name": "iCIOrdered", "type": None},  # NULL type
    37: {"name": "outputForSubscriber", "type": OutputForSubscriber},
    38: {"name": "lastPartialOutput", "type": None},  # NULL type
    39: {"name": "partialOutputRecNum", "type": PartialOutputRecNum},
    40: {"name": "relatedCallNumber", "type": CallIDNumber},
    41: {"name": "faultCode", "type": FaultCode},
    42: {"name": "subscriptionType", "type": SubscriptionType},
    43: {"name": "incompleteCallDataIndicator", "type": None},  # NULL type
    44: {"name": "incompleteCompositeCDRIndicator", "type": None},  # NULL type
    45: {"name": "switchIdentity", "type": SwitchIdentity},
    46: {"name": "networkCallReference", "type": NetworkCallReference},
    47: {"name": "disconnectionDueToSystemRecovery", "type": None},  # NULL type
    48: {"name": "forloppDuringOutputIndicator", "type": None},  # NULL type
    49: {"name": "forloppReleaseDuringCall", "type": None},  # NULL type
    50: {"name": "translatedNumber", "type": AddressString},
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
    61: {"name": "gSMCallReferenceNumber", "type": GSMCallReferenceNumber},
    62: {"name": "c7ChargingMessage", "type": C7ChargingMessage},
    63: {"name": "c7FirstCHTMessage", "type": C7CHTMessage},
    64: {"name": "c7SecondCHTMessage", "type": C7CHTMessage},
    65: {"name": "aCMChargingIndicator", "type": ChargingIndicator},
    66: {"name": "aNMChargingIndicator", "type": ChargingIndicator},
    67: {"name": "mSCAddress", "type": AddressString},
    68: {"name": "carrierInformationBackward", "type": TransitCarrierInfo},
    69: {"name": "carrierInformationForward", "type": TransitCarrierInfo},
    70: {"name": "chargeInformation", "type": ChargeInformation},
    71: {"name": "disconnectionDate", "type": Date},
    72: {"name": "disconnectionTime", "type": Time},
    73: {"name": "entryPOICA", "type": ChargeAreaCode},
    74: {"name": "exitPOICA", "type": ChargeAreaCode},
    75: {"name": "internationalCallIndicator", "type": None},  # NULL type
    76: {"name": "mobileUserClass1", "type": MobileUserClass1},
    77: {"name": "mobileUserClass2", "type": MobileUserClass2},
    78: {"name": "originatingAccessISDN", "type": None},  # NULL type
    79: {"name": "originatingCarrier", "type": CarrierInfo},
    80: {"name": "originatingChargeArea", "type": ChargeAreaCode},
    81: {"name": "tDSCounter", "type": Counter},
    82: {"name": "terminatingAccessISDN", "type": None},  # NULL type
    83: {"name": "terminatingCarrier", "type": CarrierInfo},
    84: {"name": "terminatingChargeArea", "type": ChargeAreaCode},
    85: {"name": "terminatingMobileUserClass1", "type": MobileUserClass1},
    86: {"name": "terminatingMobileUserClass2", "type": MobileUserClass2},
    87: {"name": "contractorNumber", "type": AddressString},
    88: {"name": "terminatingUserClass", "type": UserClass},
    89: {"name": "userClass", "type": UserClass},
    90: {"name": "calledPartyMNPInfo", "type": AddressString},
    91: {"name": "chargeNumber", "type": AddressString},
    92: {"name": "originatingLineInformation", "type": OriginatingLineInformation},
    93: {"name": "multimediaInformation", "type": MultimediaInformation},
    102: {"name": "outputType", "type": OutputType},
    24: {"name": "originatedCode", "type": OriginatedCode},
    121: {"name": "reroutingIndicator", "type": ReroutingIndicator},
}

MSOriginating = {}
