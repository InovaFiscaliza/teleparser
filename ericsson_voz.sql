-- ================================================================
-- Ericsson Voice CDR Database Schema
-- ================================================================
-- This file contains:
-- 1. ENUM type definitions (53 types)
-- 2. Main table definition with 371 columns
-- 
-- Generated from teleparser datatypes and modules
-- ================================================================

-- ENUM Type Definitions for Ericsson Voice CDR
-- Generated from enums.py VALUES dictionaries

-- AirInterfaceUserRate (11 values)
CREATE TYPE AirInterfaceUserRateEnum AS ENUM (
  'aIUR9600bps',
  'aIUR14400bps',
  'aIUR19200bps',
  'aIUR28800bps',
  'aIUR38400bps',
  'aIUR43200bps',
  'aIUR57600bps',
  'aIUR38400bps1',
  'aIUR38400bps2',
  'aIUR38400bps3',
  'aIUR38400bps4'
);

-- AsyncSyncIndicator (2 values)
CREATE TYPE AsyncSyncIndicatorEnum AS ENUM (
  'syncData',
  'asyncData'
);

-- BearerServiceCode (14 values)
CREATE TYPE BearerServiceCodeEnum AS ENUM (
  'All data Circuit Data Asynchronous (CDA) Services',
  'Data CDA - 300bps',
  'Data CDA - 1200bps',
  'Data CDA - 1200-75bps',
  'Data CDA - 2400bps',
  'Data CDA - 4800bps',
  'Data CDA - 9600bps',
  'General - data CDA',
  'All data Circuit Data Synchronous (CDS) Services',
  'Data CDS - 1200bps',
  'Data CDS - 2400bps',
  'Data CDS - 4800bps',
  'Data CDS - 9600bps',
  'General - data CDS'
);

-- BitRate (12 values)
CREATE TYPE BitRateEnum AS ENUM (
  '4.75 kbps',
  '5.15 kbps',
  '5.9 kbps',
  '6.7 kbps',
  '7.4 kbps',
  '7.95 kbps',
  '10.2 kbps',
  '12.2 kbps',
  '14.4 kbps',
  '64.0 kbps',
  '28.8 kbps',
  '57.6 kbps'
);

-- CRIIndicator (2 values)
CREATE TYPE CRIIndicatorEnum AS ENUM (
  'chargeRateInformationAcknowledged',
  'chargeRateInformationNotAcknowledged'
);

-- CallAttemptState (8 values)
CREATE TYPE CallAttemptStateEnum AS ENUM (
  'initialState',
  'callSentState',
  'callRejectedState',
  'callOfferedState',
  'noResponseState',
  'alertingState',
  'unknownCallState',
  'callActiveState'
);

-- CallPosition (4 values)
CREATE TYPE CallPositionEnum AS ENUM (
  'valueUsedForAllCallsToDetermineIfOutputToTakePlace',
  'callHasReachedCongestionOrBusyState',
  'callHasOnlyReachedThroughConnection',
  'answerHasBeenReceived'
);

-- CarrierSelectionSubstitutionInformation (7 values)
CREATE TYPE CarrierSelectionSubstitutionInformationEnum AS ENUM (
  'Presubscribed carrier exists, and carrier is not input by calling party. Presubscribed carrier is used.',
  'Presubscribed carrier is same as carrier input by calling party. Input carrier is used.',
  'Presubscribed carrier exists, and input by calling party is undetermined. Presubscribed carrier is used.',
  'Carrier is input by calling party, and it is not the presubscribed carrier for the calling party. Input carrier is used.',
  'Carrier given by Carrier Analysis is used instead of presubscribed carrier.',
  'Carrier given by Carrier Analysis is used instead of carrier input by calling party.',
  'Default carrier is used.'
);

-- ChangeInitiatingParty (2 values)
CREATE TYPE ChangeInitiatingPartyEnum AS ENUM (
  'userInitiated',
  'networkInitiated'
);

-- ChannelAllocationPriorityLevel (15 values)
CREATE TYPE ChannelAllocationPriorityLevelEnum AS ENUM (
  'Priority level 1',
  'Priority level 2',
  'Priority level 3',
  'Priority level 4',
  'Priority level 5',
  'Priority level 6',
  'Priority level 7',
  'Priority level 8',
  'Priority level 9',
  'Priority level 10',
  'Priority level 11',
  'Priority level 12',
  'Priority level 13',
  'Priority level 14',
  'Priority level not used'
);

-- ChargedParty (3 values)
CREATE TYPE ChargedPartyEnum AS ENUM (
  'chargingOfCallingSubscriber',
  'chargingOfCalledSubscriber',
  'noCharging'
);

-- DefaultCallHandling (2 values)
CREATE TYPE DefaultCallHandlingEnum AS ENUM (
  'continueCall',
  'releaseCall'
);

-- DefaultSMSHandling (2 values)
CREATE TYPE DefaultSMSHandlingEnum AS ENUM (
  'continueTransaction',
  'releaseTransaction'
);

-- DeliveryOfErroneousSDU (3 values)
CREATE TYPE DeliveryOfErroneousSDUEnum AS ENUM (
  'yes',
  'no',
  'noErrorDetectionConsideration'
);

-- DisconnectingParty (3 values)
CREATE TYPE DisconnectingPartyEnum AS ENUM (
  'callingPartyRelease',
  'calledPartyRelease',
  'networkRelease'
);

-- EMLPPPriorityLevel (8 values)
CREATE TYPE EMLPPPriorityLevelEnum AS ENUM (
  'Spare',
  'Priority level 4 = lowest priority for subscription',
  'Priority level 3 = sixth highest priority',
  'Priority level 2 = fifth highest priority',
  'Priority level 1 = fourth highest priority',
  'Priority level 0 = third highest priority',
  'Priority level B = second highest priority',
  'Priority level A = highest priority for subscription'
);

-- EosInfo (39 values)
CREATE TYPE EosInfoEnum AS ENUM (
  'Free subscriber.',
  'Free subscriber. No time supervision.',
  'Free subscriber. No charging.',
  'Free subscriber. No time supervision. No charging.',
  'Free subscriber. Last party release.',
  'Free subscriber. No time supervision. Last party release.',
  'Free subscriber. No charging. Last party release.',
  'Free subscriber. No time supervision. No charging. Last party release.',
  'Set up speech condition.',
  'Set up speech condition. No time supervision.',
  'Set up speech condition. No charging.',
  'Access barred',
  'Transferred subscriber.',
  'Busy subscriber.',
  'Busy subscriber with callback protection.',
  'Unallocated number.',
  'Address incomplete.',
  'Call transfer protection, that is "follow me" not allowed to this subscriber.',
  'Subscriber line out of order.',
  'Intercepted subscriber.',
  'Supervised by an operator. Trunk offering marked.',
  'Rerouting to service centre.',
  'Line lock out.',
  'Send acceptance tone.',
  'No answer/incompatible destination (used for ISDN).',
  'Send refusal tone. Only used at subscriber services.',
  'Digital path not provided.',
  'Congestion without differentiation.',
  'Time release.',
  'Technical fault.',
  'Congestion in group selection network.',
  'Lack of devices.',
  'Congestion in subscriber selection network.',
  'Congestion in international network.',
  'Congestion in national network.',
  'Conditional congestion (Region option).',
  'Route congestion.',
  'Unpermitted traffic case.',
  'No acknowledgement from mobile subscriber.'
);

-- FirstRadioChannelUsed (2 values)
CREATE TYPE FirstRadioChannelUsedEnum AS ENUM (
  'fullRateChannel',
  'halfRateChannel'
);

-- FixedNetworkUserRate (9 values)
CREATE TYPE FixedNetworkUserRateEnum AS ENUM (
  'fNUR9600bps',
  'fNUR14400bps',
  'fNUR19200bps',
  'fNUR28800bps',
  'fNUR38400bps',
  'fNUR48000bps',
  'fNUR56000bps',
  'fNUR64000bps',
  'fNURautobauding'
);

-- INMarkingOfMS (13 values)
CREATE TYPE INMarkingOfMSEnum AS ENUM (
  'originatingINService',
  'terminatingINService',
  'originatingINCategoryKeyService',
  'terminatingINCategoryKeyService',
  'originatingCAMELService',
  'terminatingCAMELService',
  'originatingExtendedCAMELServiceWithINCapabilityIndicator ',
  'terminatingExtendedCAMELServiceWithINCapabilityIndicator',
  'originatingExtendedCAMELServiceWithOriginatingINCategoryKey',
  'terminatingExtendedCAMELServiceWithTerminatingINCategoryKey',
  'subscriberDialledCAMELService',
  'subscriberDialledCAMELServiceAndOriginatingCAMELService',
  'visitedTerminatingCAMELService'
);

-- IntermediateRate (2 values)
CREATE TYPE IntermediateRateEnum AS ENUM (
  'rate8KbitPerSecondUsed',
  'rate16KbitPerSecondUsed'
);

-- LCSClientType (4 values)
CREATE TYPE LCSClientTypeEnum AS ENUM (
  'emergencyServices',
  'valueAddedServices',
  'plmnOperatorServices',
  'lawfulInterceptServices'
);

-- MessageTypeIndicator (6 values)
CREATE TYPE MessageTypeIndicatorEnum AS ENUM (
  'sMSdeliverSCtoMS',
  'sMSdeliveReportMStoSC',
  'sMSstatusReportSCtoMS',
  'sMScommanMStoSC',
  'sMSsubmitMStoSC',
  'sMSsubmitReportSCtoMS'
);

-- MobileUserClass1 (6 values)
CREATE TYPE MobileUserClass1Enum AS ENUM (
  'Spare',
  'Cellular Telephone Service',
  'Maritime Telephone Service',
  'Airplane Telephone Service',
  'Paging Service',
  'PHS service'
);

-- NumberOfChannels (8 values)
CREATE TYPE NumberOfChannelsEnum AS ENUM (
  'oneTrafficChannel',
  'twoTrafficChannels',
  'threeTrafficChannels',
  'fourTrafficChannels',
  'fiveTrafficChannels',
  'sixTrafficChannels',
  'sevenTrafficChannels',
  'eightTrafficChannels'
);

-- OptimalRoutingType (1 values)
CREATE TYPE OptimalRoutingTypeEnum AS ENUM (
  'optimalRoutingAtLateCallForwarding'
);

-- OriginatedCode (10 values)
CREATE TYPE OriginatedCodeEnum AS ENUM (
  'callOriginatingFromOwnSubscriberInSSN',
  'callOriginatingFromOwnSubscriberInGSN',
  'callOriginatingFromIncomingTrunk',
  'callOriginatingFromSUSblock',
  'callOriginatingFromOMSblock',
  'testCallTowardsIL-OL-BL',
  'testCallWithIndividualSelectionOfB-Subscriber',
  'testCallWithIndividualSelectionExceptB-Subscriber',
  'testCallWithSelectionInSpecifiedRoute',
  'operator'
);

-- OriginatingLineInformation (5 values)
CREATE TYPE OriginatingLineInformationEnum AS ENUM (
  'Identified Line - no special treatment',
  'Automatic Number Identification (ANI) failure',
  'Traffic originating from cellular carrier over Type 1 connection to Inter-exchange Carrier (IXC) or International Exchange Carrier (INC).',
  'Traffic originating from cellular carrier over Type 2 connection to IXC or INC. Charge Number is the subscriber number (callingPartyNumber or last redirectingNumber).',
  'Traffic originating from cellular carrier over Type 2 connection to IXC or INC, roaming forwarding call. Charge Number is the subscriber number of called mobile subscriber.'
);

-- OutputForSubscriber (3 values)
CREATE TYPE OutputForSubscriberEnum AS ENUM (
  'callingParty',
  'calledParty',
  'callingAndCalledParty'
);

-- OutputType (8 values)
CREATE TYPE OutputTypeEnum AS ENUM (
  'noOutput',
  'iCIoutputForCallingSubscriber',
  'iCIOutputForCalledSubscriber',
  'iCIOutputForCallingAndCalledSubscribers',
  'tTOutputOnly',
  'tTAndICIForCallingSubscriber',
  'tTAndICIForCalledSubscriber',
  'tTAndICIForCallingAndCalledSubscribers'
);

-- RadioChannelProperty (15 values)
CREATE TYPE RadioChannelPropertyEnum AS ENUM (
  'halfRateChannel',
  'fullRateChannel',
  'dualRateHalfRatePreferred',
  'dualRateFullRatePreferred',
  'twoFullRateChannels',
  'threeFullRateChannels',
  'fourFullRateChannels',
  'twoAssignedAirTimeSlots',
  'fourAssignedAirTimeSlots',
  'sixAssignedAirTimeSlots',
  'eightAssignedAirTimeSlots',
  'twelveAssignedAirTimeSlots',
  'sixteenAssignedAirtimeSlots',
  'twoDownlinkOneUplinkAssignedAirTimeSlots',
  'fourDownlinkOneUplinkAssignedAirTimeSlots'
);

-- RegionalServiceUsed (4 values)
CREATE TYPE RegionalServiceUsedEnum AS ENUM (
  'localSubscription',
  'regionalSubcription',
  'subscriptionWithTariffAreas',
  'regionalSubcriptionAndSubscriptionWithTariffAreas'
);

-- ResponseTimeCategory (2 values)
CREATE TYPE ResponseTimeCategoryEnum AS ENUM (
  'lowdelay',
  'delaytolerant'
);

-- SMSResult (2 values)
CREATE TYPE SMSResultEnum AS ENUM (
  'unsuccessfulMOSMSDeliverytoSMSCDuetoCAMELReason',
  'unsuccessfulMOSMSDeliverytoSMSCDuetoOtherReason'
);

-- SSCode (54 values)
CREATE TYPE SSCodeEnum AS ENUM (
  'All Supplementary Services (SS)',
  'All line identification SS',
  'Calling line identification presentation',
  'Calling line identification restriction',
  'Connected line identification presentation',
  'Connected line identification restriction',
  'Malicious call identification',
  'All forwarding SS',
  'Call forwarding unconditional',
  'All conditional forward. serv.',
  'Call forwarding on mobile subscriber busy',
  'Call forwarding on no reply',
  'Call forwarding on subscriber not reachable',
  'All call offering SS',
  'Call transfer',
  'Mobile access hunting',
  'All call completion SS',
  'Call waiting',
  'Call hold',
  'Completion of call to busy subscribers',
  'All Multi-Party Services',
  'Multi-Party Services',
  'All community of interest SS',
  'All charging SS',
  'Advice of charge information',
  'Advice of charge charging',
  'All additional info transfer SS',
  'User to user signalling',
  'All call restriction SS',
  'Barring of outgoing calls',
  'Barring of all outgoing calls',
  'Barring of outgoing international calls',
  'Barring of OG inter. calls except those directed to the home PLMN country',
  'Barring of incoming calls',
  'Barring of all inc. calls',
  'Barring of inc. calls when roaming outside the home PLMN country',
  'All call priority SS',
  'Enhanced multi-level precedence and preemption',
  'All PLMN specific SS',
  'PLMN specific SS - 1',
  'PLMN specific SS - 2',
  'PLMN specific SS - 3',
  'PLMN specific SS - 4',
  'PLMN specific SS - 5',
  'PLMN specific SS - 6',
  'PLMN specific SS - 7',
  'PLMN specific SS - 8',
  'PLMN specific SS - 9',
  'PLMN specific SS - A',
  'PLMN specific SS - B',
  'PLMN specific SS - C',
  'PLMN specific SS - D',
  'PLMN specific SS - E',
  'PLMN specific SS - F'
);

-- SSRequest (8 values)
CREATE TYPE SSRequestEnum AS ENUM (
  'registration',
  'erasure',
  'activation',
  'deactivation',
  'interrogation',
  'invoke',
  'registerPassword',
  'processUSSD'
);

-- SelectedCodec (10 values)
CREATE TYPE SelectedCodecEnum AS ENUM (
  'gSMFullRate',
  'gSMHalfRate',
  'gSMEnhancedFullRate',
  'fullRateAdaptiveMultiRate',
  'halfRateAdaptiveMultiRate',
  'uMTSAdaptiveMultiRate',
  'uMTSAdaptiveMultiRate2',
  'tDMAEnhancedFullRate',
  'pDCEnhancedFullRate',
  'inmarsatCoding'
);

-- ServiceSwitchingType (2 values)
CREATE TYPE ServiceSwitchingTypeEnum AS ENUM (
  'speechToFax',
  'faxToSpeech'
);

-- Single (4 values)
CREATE TYPE SingleEnum AS ENUM (
  'aPartyToBeCharged',
  'bPartyToBeCharged',
  'cPartyToBeCharged',
  'otherPartyToBeCharged'
);

-- SpeechCoderVersion (6 values)
CREATE TYPE SpeechCoderVersionEnum AS ENUM (
  'fullRateVersion1',
  'fullRateVersion2',
  'fullRateVersion3',
  'halfRateVersion1',
  'halfRateVersion2',
  'halfRateVersion3'
);

-- SubscriberState (3 values)
CREATE TYPE SubscriberStateEnum AS ENUM (
  'detached',
  'attached',
  'implicitDetached'
);

-- TariffSwitchInd (2 values)
CREATE TYPE TariffSwitchIndEnum AS ENUM (
  'noTariffSwitch',
  'tariffSwitchAfterStartOfCharging'
);

-- TeleServiceCode (22 values)
CREATE TYPE TeleServiceCodeEnum AS ENUM (
  'Telephony',
  'Emergency calls',
  'Short Message MT-PP',
  'Short Message MO-PP',
  'Facsimile group3 and alter speech',
  'Automatic facsimile group3',
  'All PLMN specific TS',
  'PLMN specific TS - 1',
  'PLMN specific TS - 2',
  'PLMN specific TS - 3',
  'PLMN specific TS - 4',
  'PLMN specific TS - 5',
  'PLMN specific TS - 6',
  'PLMN specific TS - 7',
  'PLMN specific TS - 8',
  'PLMN specific TS - 9',
  'PLMN specific TS - A',
  'PLMN specific TS - B',
  'PLMN specific TS - C',
  'PLMN specific TS - D',
  'PLMN specific TS - E',
  'PLMN specific TS - F'
);

-- TrafficClass (4 values)
CREATE TYPE TrafficClassEnum AS ENUM (
  'Conversational Class',
  'Streaming Class',
  'Interactive Class',
  'Background Class'
);

-- TransparencyIndicator (2 values)
CREATE TYPE TransparencyIndicatorEnum AS ENUM (
  'transparent',
  'nonTransparent'
);

-- TriggerDetectionPoint (26 values)
CREATE TYPE TriggerDetectionPointEnum AS ENUM (
  'originatingCallAttemptAuthorized',
  'collectedInformation',
  'analyzedInformation',
  'originatingCallAttemptRouteSelectFailure',
  'originatingCallAttemptCalledPartyBusy',
  'originatingCallAttemptCalledPartyNotAnswer',
  'originatingCallAttemptCalledPartyAnswer',
  'originatingCallAttemptMid-CallEventDetected',
  'originatingCallAttemptCallDisconnecting',
  'originatingCallAttemptCallAbandon',
  'terminatingCallAttemptAuthorized',
  'terminatingCallAttemptCalledPartyBusy',
  'terminatingCallAttemptNoAnswer',
  'terminatingCallAttemptAnswer',
  'terminatingCallAttemptMid-CallEventDetected',
  'terminatingCallAttemptCallDisconnect',
  'terminatingCallAttemptCallAbandon',
  'terminatingCallAttemptCallReAnswer',
  'terminatingCallAttemptCallSuspended',
  'terminatingCallAttemptCalledPartyNotReachable',
  'terminatingCallAttemptAlerting',
  'terminatingCallAttemptRouteSelectFailure',
  'originatingCallAttemptCalledPartyReAnswer',
  'originatingCallAttemptCallSuspended',
  'originatingCallAttemptCalledPartyNotReachable',
  'originatingCallAttemptAlerting'
);

-- TypeOfCalledSubscriber (3 values)
CREATE TYPE TypeOfCalledSubscriberEnum AS ENUM (
  'pSTNSubscriber',
  'iSDNSubscriber',
  'unknownSubscriber'
);

-- TypeOfLocationRequest (7 values)
CREATE TYPE TypeOfLocationRequestEnum AS ENUM (
  'mT_LocationRequestCurrentLocation',
  'mT_LocationRequestCurrentOrLastKnownLocation',
  'mO_LocationRequestLocEstimateToMS',
  'mO_LocationRequestLocEstimateToThirdParty',
  'mO_LocationRequestAssistData',
  'mO_LocationRequestDeciphKeys',
  'nI_LocationRequest'
);

-- TypeOfSignalling (3 values)
CREATE TYPE TypeOfSignallingEnum AS ENUM (
  'iSUPIsNotAppliedAllTheWay',
  'iSUPIsAppliedAllTheWay',
  'unknownSignalling'
);

-- UILayer1Protocol (10 values)
CREATE TYPE UILayer1ProtocolEnum AS ENUM (
  'V110_X30',
  'G711mulaw',
  'G711Alaw',
  'G721_32000bps_I460',
  'H221_H242',
  'H223_H245',
  'nonITU_T',
  'V120',
  'X31',
  'vSELP_Speech'
);

-- UnsuccessfulPositioningDataReason (2 values)
CREATE TYPE UnsuccessfulPositioningDataReasonEnum AS ENUM (
  'systemError',
  'userDeniedDueToPrivacyVerification'
);

-- UserClass (4 values)
CREATE TYPE UserClassEnum AS ENUM (
  'Spare',
  'Train Payphone',
  'Pink (non-NTT Payphone)',
  'Spare'
);

-- UserRate (31 values)
CREATE TYPE UserRateEnum AS ENUM (
  'uRIndNeg',
  'uR600bps',
  'uR1200bps',
  'uR2400bps',
  'uR3600bps',
  'uR4800bps',
  'uR7200bps',
  'uR8000bps',
  'uR9600bps',
  'uR14400bps',
  'uR16000bps',
  'uR19200bps',
  'uR32000bps',
  'uR38400bps',
  'uR48000bps',
  'uR56000bps',
  'uR64000bps',
  'uR38400bps1',
  'uR57600bps',
  'uR28800bps',
  'uR134-5bps',
  'uR100bps',
  'uR75bps_1200bps',
  'uR1200bps_75bps',
  'uR50bps',
  'uR75bps',
  'uR110bps',
  'uR150bps',
  'uR200bps',
  'uR300bps',
  'uR12000bps'
);


-- ================================================================
-- Main Table Definition
-- ================================================================

CREATE OR REPLACE TABLE ericsson_voz(
  "acceptanceOfCallWaiting" VARCHAR,
  "accountCode" VARCHAR,
  "aCMChargingIndicator" VARCHAR,
  "aIURRequested" VARCHAR,
  "angle" VARCHAR,
  "aNMChargingIndicator" VARCHAR,
  "aoCEventModule" VARCHAR,
  "area" VARCHAR,
  "asyncSyncIndicator" AsyncSyncIndicatorEnum,
  "bCSMTDPData1" VARCHAR,
  "bCSMTDPData10" VARCHAR,
  "bCSMTDPData2" VARCHAR,
  "bCSMTDPData3" VARCHAR,
  "bCSMTDPData4" VARCHAR,
  "bCSMTDPData5" VARCHAR,
  "bCSMTDPData6" VARCHAR,
  "bCSMTDPData7" VARCHAR,
  "bCSMTDPData8" VARCHAR,
  "bCSMTDPData9" VARCHAR,
  "bearerServiceCode" BearerServiceCodeEnum,
  "bSSMAPCauseCode.cause_value" VARCHAR,
  "bSSMAPCauseCode.extended_cause_value" VARCHAR,
  "c7FirstCHTMessage" VARCHAR,
  "c7SecondCHTMessage" VARCHAR,
  "callAttemptIndicator" VARCHAR,
  "callAttemptState" CallAttemptStateEnum,
  "CallDataRecord" VARCHAR,
  "calledPartyMNPInfo" VARCHAR,
  "calledPartyNumber.digits" VARCHAR,
  "calledPartyNumber.npi" VARCHAR,
  "calledPartyNumber.ton" VARCHAR,
  "calledSubscriberIMEI.SNR" VARCHAR,
  "calledSubscriberIMEI.Spare" VARCHAR,
  "calledSubscriberIMEI.TAC" VARCHAR,
  "calledSubscriberIMSI.cnpj" VARCHAR,
  "calledSubscriberIMSI.mcc" VARCHAR,
  "calledSubscriberIMSI.mnc" VARCHAR,
  "calledSubscriberIMSI.msin" VARCHAR,
  "calledSubscriberIMSI.nome" VARCHAR,
  "calledSubscriberIMSI.pais" VARCHAR,
  "callForwarding" VARCHAR,
  "callIdentificationNumber" VARCHAR,
  "callingPartyNumber.digits" VARCHAR,
  "callingPartyNumber.npi" VARCHAR,
  "callingPartyNumberSpecialArrangementInd" VARCHAR,
  "callingPartyNumber.ton" VARCHAR,
  "callingSubscriberIMEI.SNR" VARCHAR,
  "callingSubscriberIMEI.Spare" VARCHAR,
  "callingSubscriberIMEI.TAC" VARCHAR,
  "callingSubscriberIMSI.cnpj" VARCHAR,
  "callingSubscriberIMSI.mcc" VARCHAR,
  "callingSubscriberIMSI.mnc" VARCHAR,
  "callingSubscriberIMSI.msin" VARCHAR,
  "callingSubscriberIMSI.nome" VARCHAR,
  "callingSubscriberIMSI.pais" VARCHAR,
  "CallModule" VARCHAR,
  "callPosition" CallPositionEnum,
  "cAMELCallingPartyNumber" VARCHAR,
  "cAMELDestinationAddress" VARCHAR,
  "cAMELInitiatedCallForwarding" VARCHAR,
  "cAMELSMSCAddress" VARCHAR,
  "camelTDPData" VARCHAR,
  "carrierIdentificationCode" VARCHAR,
  "carrierInformation" VARCHAR,
  "carrierSelectionSubstitutionInformation" CarrierSelectionSubstitutionInformationEnum,
  "changeInitiatingParty" ChangeInitiatingPartyEnum,
  "channelAllocationPriorityLevel" ChannelAllocationPriorityLevelEnum,
  "chargeableDuration" VARCHAR,
  "chargedCallingPartyNumber.digits" VARCHAR,
  "chargedCallingPartyNumber.npi" VARCHAR,
  "chargedCallingPartyNumber.ton" VARCHAR,
  "chargedParty" ChargedPartyEnum,
  "chargeNumber.digits" VARCHAR,
  "chargeNumber.npi" VARCHAR,
  "chargeNumber.ton" VARCHAR,
  "chargePartySingle" SingleEnum,
  "chargeRateChangeEventModule" VARCHAR,
  "chargingCase" VARCHAR,
  "compositeCallDataRecord" VARCHAR,
  "contractorNumber" VARCHAR,
  "cRIIndicator" CRIIndicatorEnum,
  "cUGIncomingAccessUsed" VARCHAR,
  "cUGIndex" VARCHAR,
  "cUGInterlockCode" VARCHAR,
  "cUGOutgoingAccessIndicator" VARCHAR,
  "cUGOutgoingAccessUsed" VARCHAR,
  "dateForStartOfCharge" VARCHAR,
  "defaultCallHandling" DefaultCallHandlingEnum,
  "defaultSMSHandling" DefaultSMSHandlingEnum,
  "deliveryOfErroneousSDU1" VARCHAR,
  "deliveryOfErroneousSDU2" VARCHAR,
  "deliveryOfErroneousSDU3" VARCHAR,
  "destinationAddress" VARCHAR,
  "disconnectingParty" DisconnectingPartyEnum,
  "disconnectionDate" VARCHAR,
  "disconnectionDueToSystemRecovery" VARCHAR,
  "disconnectionTime" VARCHAR,
  "dTMFUsed" VARCHAR,
  "eMLPPPriorityLevel" EMLPPPriorityLevelEnum,
  "entryPOICA" VARCHAR,
  "eosInfo" EosInfoEnum,
  "error_shape" VARCHAR,
  "exchangeIdentity" VARCHAR,
  "exitPOICA" VARCHAR,
  "faultCode" VARCHAR,
  "firstAssignedSpeechCoderVersion" VARCHAR,
  "firstCalledLocationInformation.ci_sac" VARCHAR,
  "firstCalledLocationInformation.cnpj" VARCHAR,
  "firstCalledLocationInformation.lac" VARCHAR,
  "firstCalledLocationInformation.mcc" VARCHAR,
  "firstCalledLocationInformation.mnc" VARCHAR,
  "firstCalledLocationInformation.nome" VARCHAR,
  "firstCalledLocationInformation.pais" VARCHAR,
  "firstCallingLocationInformation.ci_sac" VARCHAR,
  "firstCallingLocationInformation.cnpj" VARCHAR,
  "firstCallingLocationInformation.lac" VARCHAR,
  "firstCallingLocationInformation.mcc" VARCHAR,
  "firstCallingLocationInformation.mnc" VARCHAR,
  "firstCallingLocationInformation.nome" VARCHAR,
  "firstCallingLocationInformation.pais" VARCHAR,
  "firstRadioChannelUsed" FirstRadioChannelUsedEnum,
  "firstTargetLocationInformation" VARCHAR,
  "fNURRequested" VARCHAR,
  "forloppDuringOutputIndicator" VARCHAR,
  "forloppReleaseDuringCall" VARCHAR,
  "freeFormatData" VARCHAR,
  "freeFormatData2" VARCHAR,
  "freeFormatDataAppendIndicator" VARCHAR,
  "freeFormatDataAppendIndicator2" VARCHAR,
  "frequencyBandSupported.egsm" VARCHAR,
  "frequencyBandSupported.gsm1800" VARCHAR,
  "frequencyBandSupported.pgsm" VARCHAR,
  "gsm1800" VARCHAR,
  "gSMCallReferenceNumber" VARCHAR,
  "gsmSCFAddress.digits" VARCHAR,
  "gsmSCFAddress.npi" VARCHAR,
  "gsmSCFAddress.ton" VARCHAR,
  "gsmSCFControlOfAoC" VARCHAR,
  "guaranteedBitRate" VARCHAR,
  "handOverEventModule" VARCHAR,
  "iCIOrdered" VARCHAR,
  "incomingAssignedRoute" VARCHAR,
  "incomingRoute" VARCHAR,
  "incompleteCallDataIndicator" VARCHAR,
  "incompleteCompositeCDRIndicator" VARCHAR,
  "iNIncomingCall" VARCHAR,
  "iNMarkingOfMS" INMarkingOfMSEnum,
  "iNOutgoingCall" VARCHAR,
  "iNServiceDataEventModule" VARCHAR,
  "iNServiceTrigger" VARCHAR,
  "interExchangeCarrierIndicator" VARCHAR,
  "intermediateRate" IntermediateRateEnum,
  "internalCauseAndLoc.cause" VARCHAR,
  "internalCauseAndLoc.location" VARCHAR,
  "internationalCallIndicator" VARCHAR,
  "interruptionTime" VARCHAR,
  "iSDNCallForwarding" VARCHAR,
  "iSDNOriginating" VARCHAR,
  "iSDNSSInvocationEventModule" VARCHAR,
  "iSDNSSProcedure" VARCHAR,
  "lastCalledLocationInformation.ci_sac" VARCHAR,
  "lastCalledLocationInformation.cnpj" VARCHAR,
  "lastCalledLocationInformation.lac" VARCHAR,
  "lastCalledLocationInformation.mcc" VARCHAR,
  "lastCalledLocationInformation.mnc" VARCHAR,
  "lastCalledLocationInformation.nome" VARCHAR,
  "lastCalledLocationInformation.pais" VARCHAR,
  "lastCalledLocationInformation.rnc_id" VARCHAR,
  "lastCallingLocationInformation.ci_sac" VARCHAR,
  "lastCallingLocationInformation.cnpj" VARCHAR,
  "lastCallingLocationInformation.lac" VARCHAR,
  "lastCallingLocationInformation.mcc" VARCHAR,
  "lastCallingLocationInformation.mnc" VARCHAR,
  "lastCallingLocationInformation.nome" VARCHAR,
  "lastCallingLocationInformation.pais" VARCHAR,
  "lastCallingLocationInformation.rnc_id" VARCHAR,
  "lastPartialOutput" VARCHAR,
  "lCSClientIdentity" VARCHAR,
  "lCSClientType" LCSClientTypeEnum,
  "locationServices" VARCHAR,
  "maxBitRateDownlink" VARCHAR,
  "maxBitRateUplink" VARCHAR,
  "messageTypeIndicator" MessageTypeIndicatorEnum,
  "miscellaneousInformation" VARCHAR,
  "mLCAddress" VARCHAR,
  "mobileStationRoamingNumber.digits" VARCHAR,
  "mobileStationRoamingNumber.npi" VARCHAR,
  "mobileStationRoamingNumber.ton" VARCHAR,
  "mobileUserClass1" MobileUserClass1Enum,
  "mSCAddress.digits" VARCHAR,
  "mSCAddress.npi" VARCHAR,
  "mSCAddress.ton" VARCHAR,
  "mSCIdentification.digits" VARCHAR,
  "mSCIdentification.npi" VARCHAR,
  "mSCIdentification.ton" VARCHAR,
  "mSCNumber" VARCHAR,
  "msOriginating" VARCHAR,
  "msOriginatingSMSinMSC" VARCHAR,
  "msOriginatingSMSinSMSIWMSC" VARCHAR,
  "msTerminating" VARCHAR,
  "msTerminatingSMSinMSC" VARCHAR,
  "msTerminatingSMSinSMSGMSC" VARCHAR,
  "multimediaCall" VARCHAR,
  "multimediaInformation" VARCHAR,
  "networkCallReference" VARCHAR,
  "network_identification_plan" VARCHAR,
  "networkInitiatedUSSDOperations" VARCHAR,
  "networkProvidedCallingPartyNumber.digits" VARCHAR,
  "networkProvidedCallingPartyNumber.npi" VARCHAR,
  "networkProvidedCallingPartyNumber.ton" VARCHAR,
  "numberOfChannelsRequested" VARCHAR,
  "numberOfMeterPulses" VARCHAR,
  "numberOfShortMessages" VARCHAR,
  "optimalRoutingInvocationFailed" VARCHAR,
  "optimalRoutingType" OptimalRoutingTypeEnum,
  "originalCalledNumber.digits" VARCHAR,
  "originalCalledNumber.npi" VARCHAR,
  "originalCalledNumber.ton" VARCHAR,
  "originatedCode" OriginatedCodeEnum,
  "originatingAccessISDN" VARCHAR,
  "originatingAddress" VARCHAR,
  "originatingCarrier" VARCHAR,
  "originatingChargeArea" VARCHAR,
  "originatingLineInformation" OriginatingLineInformationEnum,
  "originatingLocationNumber.digits" VARCHAR,
  "originatingLocationNumber.npi" VARCHAR,
  "originatingLocationNumber.ton" VARCHAR,
  "originForCharging" VARCHAR,
  "outgoingAssignedRoute" VARCHAR,
  "outgoingRoute" VARCHAR,
  "outputForSubscriber" OutputForSubscriberEnum,
  "outputType" OutputTypeEnum,
  "partialOutputRecNum" VARCHAR,
  "positionAccuracy" VARCHAR,
  "presentationAndScreeningIndicator.presentation" VARCHAR,
  "presentationAndScreeningIndicator.screening" VARCHAR,
  "radioChannelProperty" RadioChannelPropertyEnum,
  "rANAPCauseCode" VARCHAR,
  "recordSequenceNumber" VARCHAR,
  "redirectingDropBack" VARCHAR,
  "redirectingDropBackNumber" VARCHAR,
  "redirectingIMSI.cnpj" VARCHAR,
  "redirectingIMSI.mcc" VARCHAR,
  "redirectingIMSI.mnc" VARCHAR,
  "redirectingIMSI.msin" VARCHAR,
  "redirectingIMSI.nome" VARCHAR,
  "redirectingIMSI.pais" VARCHAR,
  "redirectingNumber.digits" VARCHAR,
  "redirectingNumber.npi" VARCHAR,
  "redirectingNumber.ton" VARCHAR,
  "redirectingSPN" VARCHAR,
  "redirectionCounter" VARCHAR,
  "regionalServiceUsed" RegionalServiceUsedEnum,
  "regionDependentChargingOrigin" VARCHAR,
  "relatedCallNumber" VARCHAR,
  "reroutingIndicator" VARCHAR,
  "residualBitErrorRatio1" VARCHAR,
  "residualBitErrorRatio2" VARCHAR,
  "residualBitErrorRatio3" VARCHAR,
  "responseTimeCategory" ResponseTimeCategoryEnum,
  "restartDuringCall" VARCHAR,
  "restartDuringOutputIndicator" VARCHAR,
  "rNCidOfFirstRNC" VARCHAR,
  "rNCidOfTargetRNC.cnpj" VARCHAR,
  "rNCidOfTargetRNC.lac" VARCHAR,
  "rNCidOfTargetRNC.mcc" VARCHAR,
  "rNCidOfTargetRNC.mnc" VARCHAR,
  "rNCidOfTargetRNC.msin" VARCHAR,
  "rNCidOfTargetRNC.nome" VARCHAR,
  "rNCidOfTargetRNC.pais" VARCHAR,
  "rNCidOfTargetRNC.rnc_id" VARCHAR,
  "roamingCallForwarding" VARCHAR,
  "sCFChargingOutput" VARCHAR,
  "sCPAddress.co-located" VARCHAR,
  "sCPAddress.globalTitleAndSubSystemNumber.digits" VARCHAR,
  "sCPAddress.globalTitleAndSubSystemNumber.nature_of_address" VARCHAR,
  "sCPAddress.globalTitleAndSubSystemNumber.numbering_plan" VARCHAR,
  "sCPAddress.globalTitleAndSubSystemNumber.odd" VARCHAR,
  "sCPAddress.globalTitleAndSubSystemNumber.subsystem_number" VARCHAR,
  "sCPAddress.globalTitleAndSubSystemNumber.translation_type" VARCHAR,
  "sCPAddress.pointCodeAndSubSystemNumber" VARCHAR,
  "sDFLChargingCase" VARCHAR,
  "sDUErrorRatio1" VARCHAR,
  "sDUErrorRatio2" VARCHAR,
  "sDUErrorRatio3" VARCHAR,
  "selectedCodec" SelectedCodecEnum,
  "servedSubscriberNumber" VARCHAR,
  "serviceCentreAddress.digits" VARCHAR,
  "serviceCentreAddress.npi" VARCHAR,
  "serviceCentreAddress.ton" VARCHAR,
  "serviceKey" VARCHAR,
  "serviceSwitchEventModule" VARCHAR,
  "serviceSwitchingType" ServiceSwitchingTypeEnum,
  "singleDataRecord" VARCHAR,
  "sMSReferenceNumber" VARCHAR,
  "sMSResult" SMSResultEnum,
  "spc" VARCHAR,
  "spc_type" VARCHAR,
  "speechCoderPreferenceList" VARCHAR,
  "sSCode" SSCodeEnum,
  "sSFChargingCase" VARCHAR,
  "sSFLegID" VARCHAR,
  "sSIEventModule" VARCHAR,
  "sSInvocationEventModule" VARCHAR,
  "sSInvocationNotification" VARCHAR,
  "sSProcedure" VARCHAR,
  "sSRequest" SSRequestEnum,
  "subscriberState" SubscriberStateEnum,
  "subscriptionType" VARCHAR,
  "switchIdentity" VARCHAR,
  "tAC" VARCHAR,
  "targetIMEI" VARCHAR,
  "targetIMSI" VARCHAR,
  "targetLocationInformation.ci_sac" VARCHAR,
  "targetLocationInformation.cnpj" VARCHAR,
  "targetLocationInformation.lac" VARCHAR,
  "targetLocationInformation.mcc" VARCHAR,
  "targetLocationInformation.mnc" VARCHAR,
  "targetLocationInformation.nome" VARCHAR,
  "targetLocationInformation.pais" VARCHAR,
  "targetMSISDN" VARCHAR,
  "tariffClass" VARCHAR,
  "tariffSwitchInd" TariffSwitchIndEnum,
  "teleServiceCode" TeleServiceCodeEnum,
  "terminatingAccessISDN" VARCHAR,
  "terminatingCarrier" VARCHAR,
  "terminatingChargeArea" VARCHAR,
  "terminatingLocationNumber" VARCHAR,
  "terminatingMobileUserClass1" VARCHAR,
  "terminatingUserClass" VARCHAR,
  "timeForEvent" VARCHAR,
  "timeForStartOfCharge" VARCHAR,
  "timeForStopOfCharge" VARCHAR,
  "timeForTCSeizureCalled" VARCHAR,
  "timeForTCSeizureCalling" VARCHAR,
  "timeFromRegisterSeizureToStartOfCharging" VARCHAR,
  "trafficClass" TrafficClassEnum,
  "transferDelay" VARCHAR,
  "transit" VARCHAR,
  "transitINOutgoingCall" VARCHAR,
  "translatedNumber.digits" VARCHAR,
  "translatedNumber.npi" VARCHAR,
  "translatedNumber.ton" VARCHAR,
  "transparencyIndicator" TransparencyIndicatorEnum,
  "triggerData" VARCHAR,
  "triggerData0" VARCHAR,
  "triggerData1" VARCHAR,
  "triggerData2" VARCHAR,
  "triggerData3" VARCHAR,
  "triggerData4" VARCHAR,
  "triggerData5" VARCHAR,
  "triggerData6" VARCHAR,
  "triggerData7" VARCHAR,
  "triggerDetectionPoint" TriggerDetectionPointEnum,
  "typeOfCalledSubscriber" TypeOfCalledSubscriberEnum,
  "typeOfCallingSubscriber" VARCHAR,
  "typeOfLocationRequest" TypeOfLocationRequestEnum,
  "type_of_network_identification" VARCHAR,
  "typeOfSignalling" TypeOfSignallingEnum,
  "uILayer1Protocol" UILayer1ProtocolEnum,
  "unsuccessfulPositioningDataReason" UnsuccessfulPositioningDataReasonEnum,
  "userClass" UserClassEnum,
  "userProvidedCallingPartyNumber.digits" VARCHAR,
  "userProvidedCallingPartyNumber.npi" VARCHAR,
  "userProvidedCallingPartyNumber.ton" VARCHAR,
  "userRate" UserRateEnum,
  "uSSDApplicationIdentifier" VARCHAR,
  "uSSDProcedureCode" VARCHAR,
  "uSSDServiceCode" VARCHAR,
  "verticalCoordinateRequest" VARCHAR,
  "wPSCallIndicator" VARCHAR

);
