class AcceptableChannelCodings:
	"""Acceptable Channel Codings
	This parameter contains the acceptable traffic
	channel codings received from the user equipment at
	call set-up. Channel Codings which are received from
	the user equipment but which are not supported by the
	MSC/VLR are not included in the Acceptable Channel Codings.
	The parameter is only applicable for GSM.
	"""

class AcceptanceOfCallWaiting:
	"""Acceptance Of Call Waiting
	This parameter indicates that a subscriber
	accepted a waiting call.
	"""

class AccountCode:
	"""ASN.1 Formal Description
	AccountCode ::= TBCDString (SIZE(1..5))
	Note: Only decimal digits are used.
	"""

class ACMChargingIndicator:
	"""ACM Charging Indicator (M)
	This parameter contains the Charging Indicator as sent in
	the Address Complete Message (ACM). It is output even if
	the signalling protocol does not support the ACM with
	charging indicator.
	The parameter is only applicable for WCDMA Japan.
	"""

class AgeOfLocationEstimate:
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

class AIURRequested:
	"""Air Interface User Rate Requested
	This parameter contains the Radio Access Network Interface
	user rate requested by the user equipment at call setup
	time, or changed later during the call.
	This parameter is available for non-transparent services,
	in case of multi-slot configurations or 14.4 kbit/s
	channel coding when the call is a GSM call.
	"""

class ANMChargingIndicator:
	"""ANM Charging Indicator
	This parameter contains the Charging Indicator as sent
	in  the Answer Message (ANM). It is output even if the
	signalling protocol does not support the ANM with charging
	indicator.
	The parameter is only applicable for WCDMA Japan.
	"""

class AoCCurrencyAmountSent:
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

class BCSMTDPData110:
	"""Basic Call State Model (BCSM) Trigger Detection Point (TDP)
	Data
	These elements identify the service key and the gsmSCF
	address to be used when invoking either terminating or
	originating CAMEL services. The element is taken
	from Originating or Terminating CAMEL Subscription
	Information (O/T-CSI).
	This parameter is also used when invoking CAMEL services
	related to SMS. The element is then taken from SMS-CSI.
	The fields bCSMTDPData1..10 are output in MS Originating
	and Call Forwarding CDRs in case of CAMEL Ph1 and
	CAMEL Ph2 calls. They are NOT output in case of a
	CAMEL Ph3 call (but output in SSFAM IN Incoming Call CDR).
	In case of MO-SMS CAMEL Ph3 call case, the field
	bCSMTDPData1 will be output in MS Originating SMS CDR.
	"""

class BearerServiceCode:
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

class BSSMAPCauseCode:
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

class CallAttemptIndicator:
	"""Call Attempt Indicator
	This parameter indicates that the call attempt has been
	charged.
	"""

class CallAttemptState:
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

class CalledSubscriberIMEI:
	"""Called Subscriber IMEI
	This parameter contains the called-subscriber
	International Mobile Station Equipment Identity (IMEI).
	The parameter is output, if the exchange data is set
	so that IMEI is fetched from user equipment at call setup.
	"""

class CalledSubscriberIMSI:
	"""Called Subscriber IMSI
	This parameter contains the called-subscriber
	International Mobile Subscriber Identity (IMSI).
	The parameter is applicable in a transit record when
	the called party has an active terminating IN service,
	terminating IN category key service or terminating CAMEL
	service.
	"""

class CallIdentificationNumber:
	"""Call Identification Number  (M)
	This parameter is a unique number within the own exchange
	that identifies the Call Component.
	All Call Modules produced in the same Call Component
	have the same call identification number; that is,
	if partial output records are produced for the same
	Call Component, the same call identification number
	is used.
	"""

class CallingPartyNumberSpecialArrangementInd:
	"""Calling Party Number Special Arrangement Indicator
	This parameter indicates that a special arrangement has
	applied to the calling number.
	"""

class CallingSubscriberIMEI:
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
	"""

class CallingSubscriberIMSI:
	"""Calling Subscriber IMSI
	This parameter contains the calling subscriber
	International Mobile Subscriber Identity (IMSI).
	Unavailable in mobile originating Call Component for
	emergency calls without IMSI (without SIM card).
	In case of network initiated USSD service request, this
	parameter contains the IMSI for the served subscriber
	in SSProcedure Call Module.
	In case of ineffective call the parameter is not
	available for mobile originating Call Component.
	"""

class CAMELDestinationAddress:
	"""CAMEL Destination Address
	Contains the address to identify destination of
	the MO SMS modified by gsmSCF.
	"""

class CAMELInitiatedCallForwarding:
	"""CAMEL Initiated Call Forwarding
	This parameter indicates that call forwarding is initiated
	by a terminating CAMEL service.
	"""

class CAMELSMSCAddress:
	"""CAMEL SMSC Address
	This parameter indicates the Short Message Service Centre
	address modified by gsmSCF.
	"""

class CarrierIdentificationCode:
	"""ASN.1 Formal Description
	CarrierIdentificationCode ::= TBCDString (SIZE(1..3))
	"""

class CarrierInformation:
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

class CarrierInformationBackward:
	"""Carrier Information Backward
	This is received in the Carrier Information (CARI)
	parameter in eACM/ACM or CPG message from the B-side.
	This information can be used for accounting purposes.
	It contains the received Transit Carrier Information
	in the order they are received from the superior
	exchange (IEC, CIEC or SCPC).
	IEC and CIEC contain the Carrier Identification Code
	and possibly the POICA or POI-hierarchy, or both
	information. SCPC contains only the Carrier
	Identification Code and can be set by a service provider.
	At maximum 6 carriers (CIEC, IEC or SCPC) will be output
	per call. The rest will be discarded.
	Note: The last received Carrier Information Backward
	will be stored in the CDR.
	The parameter is only applicable for WCDMA Japan.
	"""

class CarrierInformationForward:
	"""Carrier Information Forward
	This parameter is received in the Carrier Information
	(CARI) parameter in IAM message sent in the forward
	direction. This information can be used for accounting
	purposes.
	CarrierInformationForward contains the Transit Carrier
	Information (IEC, CIEC or SCPC) of all transit carriers
	involved in the call. IEC and CIEC contain the Carrier
	Identification Code and possibly POICA or POI-hierarchy,
	or information from both. SCPC contains only the Carrier
	Identification Code and can be set by a service provider.
	At maximum six carriers (CIEC, IEC or SCPC) will be
	output per call. The rest will be discarded.
	The parameter is only applicable for WCDMA Japan.
	"""

class CarrierSelectionSubstitutionInformation:
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

class CauseCode:
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

class ChangeInitiatingParty:
	"""ASN.1 Formal Description
	ChangeInitiatingParty ::= ENUMERATED
	(userInitiated                  (0),
	networkInitiated               (1))
	"""

class ChannelAllocationPriorityLevel:
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

class ChannelCodingUsed:
	"""Channel Coding Used
	This parameter indicates the assigned channel coding.
	The contents of the field is based on the information
	received from the mobile station at call setup phase.
	At first assignment, the selection of the channel coding
	to be used by the BSC is based on the preference of
	the mobile subscriber, the preference for each basic
	service or the operator and the capability of the BSC.
	If the channel coding changes during the call, Channel
	Coding Used is output in Charge Rate Change Call Module
	and it indicates the new channel coding.
	In case of handover Channel Coding Used in target MSC
	is output in Handover event module.
	The parameter is not applicable for WCDMA Japan.
	"""

class ChargeableDuration:
	"""Chargeable Duration (P)
	This parameter registers chargeable duration of a call.
	Chargeable duration is registered as the time
	from 'start of charging' to 'stop of charging',
	minus the interruption time. It is always truncated
	to seconds for WCDMA ETSI and GSM and always truncated
	to deciseconds for WCDMA Japan.
	Whether the B-subscriber on-hook time is registered as
	interruption time or as chargeable duration can be
	defined by AXE parameter.
	If originating or terminating Call Components, or both,
	are not charged, but there exists chargeable
	Supplementary Service invocations, the parameter contains
	the value zero.
	"""

class ChargedParty:
	"""ASN.1 Formal Description
	ChargedParty ::= ENUMERATED
	(chargingOfCallingSubscriber  (0),
	chargingOfCalledSubscriber   (1),
	noCharging                   (2))
	"""

class ChargeInformation:
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

class ChargePartyDistributed:
	"""Charge Party Distributed
	This parameter indicates the percentage of the total
	charge to be given to each party. It originates from
	INAP operation FurnishChargingInformation.
	The distribution among all parties is given as follows:
	- Percentage for A-party
	- Percentage for B-party
	- Percentage for C-party
	- Percentage for Other Party
	"""

class ChargePartySingle:
	"""Charge Party Single
	This parameter indicates which party is to be charged
	for the IN-part of the call. It originates from
	INAP operation FurnishChargingInformation.
	"""

class ChargingCase:
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

class ChargingUnitsAddition:
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

class CRIIndicator:
	"""ASN.1 Formal Description
	CRIIndicator ::= ENUMERATED
	(chargeRateInformationAcknowledged       (1),
	chargeRateInformationNotAcknowledged    (2))
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

class CUGIncomingAccessUsed:
	"""Closed User Group Incoming Access Used
	This parameter indicates the subscriber has a subscription
	to Closed User Group (CUG) supplementary service and has
	received a call from outside the subscriber's group.
	.
	"""

class CUGIndex:
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

class CUGInterlockCode:
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

class CUGOutgoingAccessIndicator:
	"""Closed User Group Outgoing Access Indicator
	This parameter indicates that the calling subscriber has
	made a Closed User Group (CUG) call with Outgoing Access.
	That information will be carried in an Initial Address
	Message (IAM) toward the destination.
	"""

class CUGOutgoingAccessUsed:
	"""Closed User Group Outgoing Access Used
	This parameter indicates that Closed User Group (CUG)
	Outgoing Access has been used. The subscriber has
	a subscription to CUG supplementary service and has
	made a call that is able to terminate outside the
	subscriber's CUG, that is, a call without CUG properties
	or a CUG call with Outgoing Access.
	In the case of a call-forwarding component, the forwarding
	subscriber has CUG Outgoing Access, and the call is
	forwarded as a received being CUG call with Outgoing
	Access.
	"""

class C7ChargingMessage:
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

class C7FirstCHTMessage:
	"""CCITT No.7 First Charging Change Message  (P)
	This parameter contains the time of the reception of the
	message and the data of the first CHT message. The first
	CHT message is received only if more than one tariff change
	is to be applied to the call.
	This parameter is available if received and the national
	signalling system supports the function.
	The parameter is not applicable for WCDMA Japan.
	"""

class C7SecondCHTMessage:
	"""CCITT No.7 Second Charging Change Message  (P)
	This parameter contains the time of the reception of
	the message and the data of the second CHT message. The
	second CHT message is received only if more tariff changes
	than specified in the first CHT message are to be applied
	to the call.
	This parameter is available if received and the national
	signalling system supports the function.
	The parameter is not applicable for WCDMA Japan.
	"""

class Date:
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

class DateForStartOfCharge:
	"""Date for Start of Charging (M)(P)
	Date For Start Of Charge registers the date when charging
	was started. For details when charging is considered
	started, refer to timeForStartofCharge.
	"""

class DecipheringKeys:
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

class DefaultCallHandling:
	"""ASN.1 Formal Description
	DefaultCallHandling ::= ENUMERATED
	(continueCall                    (0),
	releaseCall                     (1))
	"""

class DefaultSMSHandling:
	"""ASN.1 Formal Description
	DefaultSMS-Handling ::= ENUMERATED
	(continueTransaction             (0),
	releaseTransaction              (1))
	"""

class DeliveryOfErroneousSDU13:
	"""Delivery Of Erroneous SDU
	These parameters are reliability attributes, which
	indicates whether Service Data Unit (SDU) with detected
	errors must be delivered or not. In case of unequal
	error protection, these attributes are set per subflow.
	These parameters are only applicable for WCDMA.
	"""

class DestinationAddress:
	"""Destination Address
	This parameter indicates the destination address to which
	the transfer protocol message refers when a UE sends a
	short message to the service centre or when a UE invokes
	an operation at the service centre.
	"""

class DisconnectingParty:
	"""ASN.1 Formal Description
	DisconnectingParty ::= ENUMERATED
	(callingPartyRelease          (0),
	calledPartyRelease           (1),
	networkRelease               (2))
	"""

class DisconnectionDate:
	"""Disconnection Date
	Indicates the date, according to the system clock, when
	the call was disconnected. Disconnection Date is output
	only if a small system restart occurred during the call.
	Disconnection Date and Disconnection Time together contain
	the exact release time for a call according to the system
	clock in case a small restart has occurred during the call.
	The exact release time may  be used for calculating the
	restart time.
	In case of partial output during the call the Disconnection
	Date is included only in the last partial output record
	only if the small system restart has occurred during
	the last partial output period.
	The parameter is only applicable for WCDMA Japan.
	"""

class DisconnectionDueToSystemRecovery:
	"""Disconnection due to System Recovery
	This parameter indicates that the call has been
	disconnected because of a small or large restart.
	"""

class DisconnectionTime:
	"""Disconnection Time
	Indicates the time, according to the system clock, when
	the call was disconnected. Disconnection Time is output
	only if a small system restart has occurred during
	the call.
	Disconnection Time and Disconnection Date together contain
	the exact release time for a call according to the system
	clock in case a small restart has occurred during the call.
	The exact release time may be used for calculating the
	restart time.
	In case of partial output during the call the
	Disconnection Time is included only in the last partial
	output record only if the small system restart has
	occurred during the last partial output period.
	The parameter is only applicable for WCDMA Japan.
	"""

class DTMFUsed:
	"""DTMF Sender Used
	This parameter indicates that a Dual Tone Multi-Frequency
	(DTMF) sender has been used during the call.
	"""

class EMLPPPriorityLevel:
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

class EndToEndAccessDataMap:
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

class EntryPOICA:
	"""Entry POICA
	Entry POICA information is sent in forward direction
	in the intra-network ISUP Initial Address Message (IAM)
	if external POI-CA has been defined in the entry
	POI-GMSC.
	POICA information can be used to calculate the
	distance between the Entry POICA and Exit POICA. Transit
	operators may set the network fee depending on this
	distance.
	Entry POICA is output only in the Call Data Record
	generated by the node that has POICA defined.
	The parameter is only applicable for WCDMA Japan.
	"""

class EosInfo:
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

class ExitPOICA:
	"""Exit POICA
	Exit POICA information is always sent in the
	backward direction in the intra-network ISUP eACM/ACM
	message if external POICA has been defined in exit
	POI-GMSC. It is also sent in the CPG message if CARI
	(Carrier Information) parameter is received in CPG
	message and if external POICA has been defined in
	exit POI-GMSC.
	POICA information can be used to calculate
	the distance between the entry-POI and exit-POI.
	Transit operators may set the network fee depending
	on this distance.
	Exit POICA is output only in the Call Data Record
	generated by the node that has POICA defined. In transit
	call case Exit POICA is added to the IEC information.
	Exit POICA is output only in the Call Data Record
	generated by the node that has POICA defined.
	Note: The last received Exit POICA is stored in
	the CDR.
	The parameter is only applicable for WCDMA Japan.
	"""

class FaultCode:
	"""ASN.1 Formal Description
	FaultCode ::= OCTET STRING (SIZE(2))
	|    |    |    |    |    |    |    |    |
	|  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
	|    |    |    |    |    |    |    |    |
	/---------------------------------------/
	|MSB                                    |  octet 1
	+---------------------------------------+
	|                                    LSB|  octet 2
	/---------------------------------------/
	Note: OCTET STRING is coded as an unsigned integer.
	Note: Detailed information on fault code values is
	available in the Application Information "List
	Of End-Of-Selection Codes".
	"""

class FirstAssignedSpeechCoderVersion:
	"""First Assigned Speech Coder Version
	This parameter indicates the speech coder version that was
	originally assigned for the call.
	The parameter is only applicable for GSM.
	"""

class FirstCalledLocationInformation:
	"""First Called Location Information
	This parameter contains information about the initial
	service area when the location information is
	provided by RANAP in case of an WCDMA call. It is coded
	in similar way as CGI (CellGlobalIdentity) in GSM.
	In case this information is received from GSM, it contains
	the identity of the first cell where traffic channel or
	dedicated control channel was allocated.
	In the case of call related supplementary services
	(invocations) the parameter contains the current cell.
	"""

class FirstCallingLocationInformation:
	"""First Calling Location Information
	This parameter contains information about the initial service
	area when the location information is provided by RANAP in case
	of an WCDMA call. It is coded in similar way as CGI
	(CellGlobalIdentity) in GSM.
	In case this information is received from GSM, it contains
	the identity of the first cell where traffic channel or
	dedicated control channel was allocated.
	In case of parallel transaction, the parameter contains
	the current cell or service area.
	In case of a network-initiated USSD service request, this
	parameter contains the identity for the served subscriber
	in the Subscriber Service Procedure Call Module.
	In case of call related supplementary services
	(invocations) the parameter contains the current cell or service
	area.
	"""

class FirstRadioChannelUsed:
	"""ASN.1 Formal Description
	FirstRadioChannelUsed ::= ENUMERATED
	(fullRateChannel               (0),
	halfRateChannel               (1))
	"""

class FirstTargetLocationInformation:
	"""First Target Location Information
	This LCS parameter contains information about the
	identity of the first cell/service area where traffic channel
	or dedicated control channel was allocated when a positioning
	was performed for a mobile station.
	"""

class FlexibleCounter18:
	"""Flexible Counter 1..8
	The flexible counters are used to store both end-to-end
	charging information elements and the information sent in
	User Information elements within the call control message.
	One out of eight flexible counters is used for call
	attempt.
	The parameter is not applicable for WCDMA Japan.
	"""

class FNURRequested:
	"""Fixed Network User Rate Requested
	This parameter contains the fixed network user rate for
	transparent and non-transparent bearer services in case
	of an WCDMA call.
	For GSM calls the parameter contains the fixed network
	user rate for a High Speed Circuit Switched Data (HSCSD)
	connection and is available for transparent and
	non-transparent services, in case of multi-slot
	configurations or 14.4 kbit/s channel coding.
	"""

class ForloppDuringOutputIndicator:
	"""Forlopp During Output Indicator
	This parameter indicates that forlopp release during
	output has occurred, resulting in an incomplete
	Call Module or Event Module and possibly missing event
	modules.
	"""

class ForloppReleaseDuringCall:
	"""Forlopp Release During Call
	This parameter indicates a forlopp release has occurred
	during the call.
	"""

class FreeFormatData:
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

class FreeFormatDataAppendIndicator:
	"""Free Format Data Append Indicator
	This parameter is needed in CDR postprocessing to indicate
	whether the free format data is to be appended to the free
	format data in the previous partial CDR, i.e. if the free
	format data in the previous partial CDR is valid. The
	indicator must not be output to the first partial record.
	"""

class FrequencyBandSupported:
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

class GenericChargingDigits:
	"""Generic Charging Digits
	This parameter indicates a set of generic digits
	to be included in the Call Data Record. It originates
	from INAP operation FurnishChargingInformation.
	This parameter makes it possible to provide generic
	charging information as a digit string for off-line
	billing purposes. The information can be Binary Coded
	Decimal (BCD),binary, or International Alphabetical
	number 5 (IA5) coded. Use of this parameter is operator
	specific and is intended for flexible introduction of
	service- or operator-specific charging information without
	impact on the on-line charging process.
	.
	"""

class GenericChargingNumbers:
	"""Generic Charging Numbers
	This parameter indicates a set of generic numbers
	to be included in the Call Data Record. It originates
	from INAP operation FurnishChargingInformation.
	This parameter makes it possible to provide generic
	charging information in number format for off-line
	billing purposes. Use of this parameter is operator
	specific and is intended for flexible introduction of
	service- or operator-specific charging information without
	impact on the on-line charging process.
	"""

class GSMCallReferenceNumber:
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

class GsmSCFControlOfAoC:
	"""gsmSCF Control of Advice of Charge
	The gsmSCF Control of AoC is CAMEL specific parameter.
	It is used to indicate that the associated Charge Rate
	Info data is received from gsmSCF.
	"""

class GuaranteedBitRate:
	"""Guaranteed Bit Rate
	This parameter indicates the minimum bit rate
	required on the Iu interface to handle the wanted
	quality of service.
	The parameter is used at Radio Access Bearer (RAB)
	assignment during call setup.
	The parameter is only applicable for WCDMA.
	"""

class HorizontalAccuracy:
	"""Horizontal Accuracy
	This LCS parameter expresses the requested horizontal
	accuracy of the UE being positioned. The parameter is
	a part of LCS Quality of Service (QoS) received.
	"""

class ICIOrdered:
	"""Immediate Call Itemization Ordered
	This parameter indicates that ICI has been ordered for
	the call. It is included both in TT and ICI records when
	ICI is ordered.
	"""

class IncomingAssignedRoute:
	"""Incoming Assigned Route
	This parameter registers the assigned incoming route.
	The route identification of the radio access network
	interface (the interface between the MSC and BSC/RNC) is
	registered.
	The assigned route is taken into consideration after
	successful initial traffic assignment.
	This parameter is unavailable if the route has no name.
	"""

class IncomingRoute:
	"""Incoming Route
	This parameter registers the incoming route name.
	In case of the mobile originating Call Component, the
	route identification of the radio access network
	interface (the interface between the MSC and BSC/RNC)
	is registered.
	This is the initial route taken into consideration
	at reception of the SETUP message from the UE.
	This parameter is unavailable if the route has no name.
	"""

class IncompleteCallDataIndicator:
	"""Incomplete Call Data Indicator
	This parameter indicates that some data in the call
	or Event Module are missing because of congestion
	in recording resources, forlopp release during output,
	or a small/large restart during the call.
	"""

class IncompleteCompositeCDRIndicator:
	"""Incomplete Composite Call Data Record Indicator
	This parameter indicates that the Composite Call
	Data Record is incomplete because the data
	buffer is too small to handle the whole
	Composite Call Data Record or forlopp during output has
	occurred and one or more of the last records is
	missing (discarded). This parameter is included only in
	the first record in the Composite Call Data Record.
	"""

class INMarkingOfMS:
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

class INServiceTrigger:
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

class InterExchangeCarrierIndicator:
	"""InterExchange Carrier Indicator
	This parameter indicates that a Call Component
	involved an inter-exchange carrier.
	"""

class IntermediateRate:
	"""ASN.1 Formal Description
	IntermediateRate ::= ENUMERATED
	(rate8KbitPerSecondUsed           (2),
	rate16KbitPerSecondUsed          (3))
	"""

class InternalCauseAndLoc:
	"""ASN.1 Formal Description
	InternalCauseAndLoc ::= OCTET STRING (SIZE(2))
	|    |    |    |    |    |    |    |    |
	|  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
	|    |    |    |    |    |    |    |    |
	/---------------------------------------/
	|         LOCATION                      |  octet 1
	+---------------------------------------+
	|         CAUSE                         |  octet 2
	/---------------------------------------/
	Note: OCTET STRING is coded as an unsigned integer.
	For values, see the Application Information for function
	block RA.
	Also see the Application Information "Mapping of Cause
	Codes and Location Information".
	"""

class InternationalCallIndicator:
	"""International Call Indicator
	Contains an indication obtained from Forward Call Indicators
	in Initial Address Message (IAM) in ISUP. The indication is
	needed to distinguish between national transit call and
	international call. This parameter is output on the Call
	Data Record only in case of international call.
	The parameter is only applicable for WCDMA Japan.
	"""

class InterruptionTime:
	"""Interruption Time  (P)
	This parameter indicates the time during the call when
	the call has not been charged. The call is not charged
	when the calling subscriber is on-hook.
	Whether the B-subscriber on-hook time is registered
	as interruption time or as chargeable duration can be
	defined by AXE parameter.
	If originating or terminating Call Components, or both,
	are not charged but chargeable Supplementary Service
	invocations exist, the parameter contains a value of zero.
	"""

class InvocationOfCallHold:
	"""Invocation of Call Hold
	This parameter indicates that supplementary service
	call hold has been used during the call. This field
	is output only for ISOCODE or PACKED postprocessing
	purposes.
	The parameter is not applicable for WCDMA Japan.
	"""

class LastCalledLocationInformation:
	"""Last Called Location Information
	This parameter contains the cell (GSM) or service
	area (WCDMA) identity of the last cell (GSM) or service
	area (WCDMA) used by the called subscriber at
	disconnection.
	In case of delivery of multiple short messages, this
	parameter contains the location where the last successful
	short message transaction was made.
	"""

class LastCallingLocationInformation:
	"""Last Calling Location Information
	This parameter contains the cell (GSM) or service area
	(WCDMA) identity of the last cell or service area used
	by the calling subscriber at disconnection.
	"""

class LastPartialOutput:
	"""Last Partial Output
	This parameter indicates that this output is the last
	partial output. It appears only when partial output
	has previously taken place.
	"""

class LCSClientType:
	"""ASN.1 Formal Description
	LCSClientType ::= ENUMERATED
	(emergencyServices                  (0),
	valueAddedServices                 (1),
	plmnOperatorServices               (2),
	lawfulInterceptServices            (3))
	"""

class LocationCode:
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

class LocationEstimate:
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

class MaxBitRateDownlink:
	"""Max Bit Rate Downlink
	This parameter indicates the maximum number of bits
	delivered by UMTS Terrestrial Radio Access Network (UTRAN)
	at a Service Action Point (SAP) within a period of time.
	The parameter is only applicable for WCDMA.
	"""

class MaxBitRateUplink:
	"""Max Bit Rate Uplink
	This parameter indicates the maximum number of bits
	delivered to UMTS Terrestrial Radio Access Network (UTRAN)
	at a Service Action Point (SAP) within a period of time.
	The parameter is only applicable for WCDMA.
	"""

class MessageReference:
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

class MessageTypeIndicator:
	"""ASN.1 Formal Description
	MessageTypeIndicator ::= ENUMERATED
	(sMSdeliverSCtoMS         (0),
	sMSdeliveReportMStoSC    (1),
	sMSstatusReportSCtoMS    (2),
	sMScommanMStoSC          (3),
	sMSsubmitMStoSC          (4),
	sMSsubmitReportSCtoMS    (5))
	"""

class MiscellaneousInformation:
	"""ASN.1 Formal Description
	MiscellaneousInformation ::= OCTET STRING (SIZE(1))
	|    |    |    |    |    |    |    |    |
	|  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
	|    |    |    |    |    |    |    |    |
	/---------------------------------------/
	| MSB                               LSB |
	/---------------------------------------/
	Note: OCTET STRING is coded as an unsigned integer.
	Value range: H'0 - H'FE, value H'FF is reserved.
	"""

class MLCAddress:
	"""MLC Address
	This parameter includes the Gateway Mobile Location Center
	(GMLC) through which the LCS Client is accessed, when
	requesting location information for a specific target UE.
	"""

class MobileUserClass1:
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

class MobileUserClass2:
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

class MultimediaCall:
	"""Multimedia Call
	This parameter is output when the call is of a 3G.324M
	standard type, that is, low bit rate multimedia
	communication call using either a real-time video, audio,
	data or any combination between two multimedia terminals
	over a PSTN or ISDN network.
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

class NetworkCallReference:
	"""ASN.1 Formal Description
	NetworkCallReference ::= OCTET STRING (SIZE(5))
	|    |    |    |    |    |    |    |    |
	|  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
	|    |    |    |    |    |    |    |    |
	/---------------------------------------/
	| MSB       SEQUENCE NUMBER             |  octet 1
	+---------------------------------------+
	|           SEQUENCE NUMBER             |  octet 2
	+---------------------------------------+
	|           SEQUENCE NUMBER         LSB |  octet 3
	+---------------------------------------+
	| MSB       SWITCH IDENTITY             |  octet 4
	+---------------------------------------+
	|           SWITCH IDENTITY         LSB |  octet 5
	/---------------------------------------/
	Note: OCTET STRING is coded internally as an
	unsigned integer.
	-   Octet 1-3 Sequence number
	-   Octet 4-5 Switch identity
	Value range of Sequence number: H'0 - H'FFFFFF
	Value range of Switch identity: H'1 - H'FFFF
	"""

class NetworkInitiatedUSSDOperations:
	"""Network Initiated Unstructured Supplementary Service
	Data Operations
	This parameter indicates the number of successful
	network initiated USSD operations.
	"""

class NumberOfChannelsRequested:
	"""Number of Channels Requested
	This parameter contains the maximum number of full-rate
	traffic channels requested by the UE for a connection.
	The parameter is available in case of multi-slot
	configurations or 14.4 kbit/s channel coding.
	The parameter is only applicable for GSM.
	"""

class NumberOfMeterPulses:
	"""ASN.1 Formal Description
	NumberOfMeterPulses ::=  OCTET STRING (SIZE(3))
	|    |    |    |    |    |    |    |    |
	|  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
	|    |    |    |    |    |    |    |    |
	/---------------------------------------/
	| MSB                                   | octet 1
	+---------------------------------------+
	|                                       | octet 2
	+---------------------------------------+
	|                                  LSB  | octet 3
	/---------------------------------------/
	Note: OCTET STRING is coded as an unsigned integer.
	Value range: H'1 - H'FFFFFF
	"""

class NumberOfShortMessages:
	"""Number of Short Messages (M)
	This parameter indicates the number of successfully
	delivered SMS in case of Multiple Short Message
	Mobile Terminated transfers.
	"""

class OptimalRoutingInvocationFailed:
	"""Optimal Routing Invocation Failed
	This parameter indicates that Optimal Routing (OR) was
	not successfully invoked.
	"""

class OptimalRoutingType:
	"""ASN.1 Formal Description
	OptimalRoutingType ::= ENUMERATED
	(optimalRoutingAtLateCallForwarding    (0))
	"""

class OriginatedCode:
	"""ASN.1 Formal Description
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

class OriginatingAccessISDN:
	"""Originating Access ISDN
	This parameter indicates that the originating access
	has ISDN capabilities.
	The parameter is only applicable for WCDMA Japan.
	"""

class OriginatingAddress:
	"""Originating Address
	This parameter contains the address for the user of a
	service, when a service center replies by sending user
	data to the UE, or when the service center informs the
	UE of the status of a previously submitted short message.
	"""

class OriginatingCarrier:
	"""Originating Carrier
	Contains the Carrier Identification Code of the network
	from which the call originates, that is, the Originating
	Local Exchange Carrier (OLEC). Originating carrier received
	from another network may also contain POI-hierarchy
	information.
	Originating carrier is not output for calls within one
	carrier network.
	Note: For an enquiry call after an Inter MSC Handover
	Originating Carrier will contain the carrier
	identification code of the Anchor MSC.
	The parameter is only applicable for WCDMA Japan.
	"""

class OriginatingChargeArea:
	"""Originating Charge Area (OCA)
	This parameter contains the location, specified with
	a Charge Area code, from which the call originates.
	Note: For an enquiry call after an Inter MSC Handover
	this parameter will contain the Charge Area Code
	of the drift MSC.
	If a call originates from international carrier OCA
	might not be received and a default value is output.
	If no default value is defined OCA is not output.
	The parameter is only applicable for WCDMA Japan.
	"""

class OriginatingLineInformation:
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

class OriginForCharging:
	"""Origin for Charging
	The value of the parameter is specified by the operator.
	The value of this parameter reflects the origin for the
	call and is received from, for example, the incoming route
	or originating cell.
	When a call is routed from the SSF, the parameter may be
	modified by SCF.
	"""

class OutgoingAssignedRoute:
	"""Outgoing Assigned Route
	This parameter registers the assigned outgoing route name.
	The route identification of the radio access network
	interface (the interface between the MSC and RNC) is
	registered.
	This assigned route is taken into consideration after
	successful initial traffic channel assignment.
	This parameter is unavailable if the route has no name.
	"""

class OutgoingRoute:
	"""Outgoing Route
	This parameter registers the outgoing route name.
	In case of mobile terminating Call Component, the route
	identification of the initial radio access network
	interface (the interface  between the MSC and RNC) is
	registered.
	This is the initial route taken into consideration at
	sending of the SETUP message to the UE.
	This information is unavailable if the route has no name.
	"""

class OutputForSubscriber:
	"""ASN.1 Formal Description
	OutputForSubscriber ::= ENUMERATED
	(callingParty           (0),
	calledParty            (1),
	callingAndCalledParty  (2))
	"""

class OutputType:
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

class PartialOutputRecNum:
	"""ASN.1 Formal Description
	PartialOutputRecNum ::= OCTET STRING (SIZE(1))
	|    |    |    |    |    |    |    |    |
	|  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
	|    |    |    |    |    |    |    |    |
	/---------------------------------------/
	| MSB                              LSB  |
	/---------------------------------------/
	Note: OCTET STRING is coded as an unsigned integer.
	Value range: H'1 - H'FF
	"""

class PositionAccuracy:
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

class PositioningDelivery:
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

class PresentationAndScreeningIndicator:
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

class RadioChannelProperty:
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

class RANAPCauseCode:
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

class RedirectingDropBack:
	"""Redirecting Drop Back
	The presence of this parameter indicates that Call
	Drop Back function is used.
	The parameter is not applicable for WCDMA Japan.
	"""

class RedirectingIMSI:
	"""Redirecting IMSI
	This parameter contains the IMSI of the subscriber who
	forwarded the call, when the call is redirected.
	"""

class RedirectionCounter:
	"""ASN.1 Formal Description
	RedirectionCounter ::= OCTET STRING (SIZE(1))
	|    |    |    |    |    |    |    |    |
	|  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
	|    |    |    |    |    |    |    |    |
	/---------------------------------------/
	| MSB                              LSB  |
	/---------------------------------------/
	Note: OCTET STRING is coded as an unsigned integer.
	Values     Meaning
	0 - 10     Number of redirections
	Note: The maximum value is set by an
	Exchange Parameter.
	"""

class RegionalServiceUsed:
	"""ASN.1 Formal Description
	RegionalServiceUsed ::= ENUMERATED
	(localSubscription                                  (0),
	regionalSubcription                                (1),
	subscriptionWithTariffAreas                        (2),
	regionalSubcriptionAndSubscriptionWithTariffAreas  (3))
	"""

class RegionDependentChargingOrigin:
	"""Region Dependent Charging Origin
	The value of the parameter reflects the used region
	dependent service and region. The meaning of the
	value is specified by the operator.
	"""

class RelatedCallNumber:
	"""Related Call Number
	This parameter contains the call identification number of
	a previous Call Data Record, which belongs to the same
	call in the same node.
	In the Subscriber Service Procedure module, in the case
	of call-related USSD transaction, the parameter indicates
	the call identification number of the related call.
	If the Call Data Record for the previous Call Component
	is not produced, this parameter is irrelevant.
	"""

class ReroutingIndicator:
	"""Rerouting Indicator
	This parameter indicates if the call has been rerouted
	(for example a new B-number analysis has been performed)
	by the exchange where the charging data is output. This
	field is output only for ISOCODE or PACKED postprocessing
	purposes.
	"""

class ResidualBitErrorRatio13:
	"""Residual Bit Error Ratio
	These parameters are a reliability attribute, which
	indicates the undetected bit error ratio for each
	subflow in the delivered Service Data Unit (SDU).
	These parameters are only applicable for WCDMA.
	"""

class ResponseTimeCategory:
	"""ASN.1 Formal Description
	ResponseTimeCategory ::= ENUMERATED
	(lowdelay       (0),
	delaytolerant  (1))
	"""

class RestartDuringCall:
	"""Restart During the Call  (P)
	This parameter indicates that a restart has taken place
	during the call.
	"""

class RestartDuringOutputIndicator:
	"""Restart During Output Indicator
	This parameter indicates that a restart has occurred
	after an output has been initiated but before the output
	procedure was completed.
	"""

class RetrievalOfHeldCall:
	"""Retrieval of Held Call
	This parameter indicates retrieval of the held call
	has been used during the call. This field is output
	only for ISOCODE or PACKED postprocessing purposes.
	The parameter is not applicable for WCDMA Japan.
	"""

class RNCidOfFirstRNC:
	"""RNC id of First RNC
	The RNC id Of First RNC identifies the original RNC
	for WCDMA originated/terminating call or transaction.
	The parameter is only applicable for WCDMA.
	"""

class RNCidOfTargetRNC:
	"""RNC id of Target RNC
	The RNC id Of Target RNC identifies the target for the
	handover of a call from GSM to WCDMA.
	The parameter is applicable for GSM900/1800.
	"""

class SDUErrorRatio13:
	"""SDU Error Ratio
	These parameters are reliability attributes which indicates
	the fraction of Service Data Unit (SDU) lost or detected
	as erroneous when transferring data in a Radio Access
	Bearer (RAB).
	These parameters are only applicable for WCDMA.
	"""

class SelectedCodec:
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

class ServiceFeatureCode:
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

class ServiceSwitchingType:
	"""ASN.1 Formal Description
	ServiceSwitchingType ::= ENUMERATED
	(speechToFax       (0),
	faxToSpeech       (1))
	"""

class SMSReferenceNumber:
	"""SMS Reference Number
	The SMS Reference Number can be used for correlation
	of CDRs produced in the MSC/VLR Server with CDRs produced
	in the gsmSCF.
	"""

class SMSResult:
	"""ASN.1 Formal Description
	SMSResult ::= ENUMERATED
	(unsuccessfulMOSMSDeliverytoSMSCDuetoCAMELReason  (0),
	unsuccessfulMOSMSDeliverytoSMSCDuetoOtherReason  (1))
	"""

class SpeechCoderPreferenceList:
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

class SSCode:
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

class SSFLegID:
	"""SSF Leg Identity
	This parameter indicates the call leg identity.
	It originates from gsmSCF in FurnishChargingInformation
	operation.
	"""

class SSFChargingCase:
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

class SSInvocationNotification:
	"""Supplementary Service Invocation Notification
	This parameter is a CAMEL specific parameter.
	It indicates successful SS invocation notification
	to gsmSCF.
	"""

class SSRequest:
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

class SubscriberState:
	"""ASN.1 Formal Description
	SubscriberState ::= ENUMERATED
	(detached                   (0),
	attached                   (1),
	implicitDetached           (2))
	"""

class SubscriptionType:
	"""ASN.1 Formal Description
	SubscriptionType ::= OCTET STRING (SIZE(1))
	|    |    |    |    |    |    |    |    |
	|  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
	|    |    |    |    |    |    |    |    |
	/---------------------------------------/
	|                                       |
	/---------------------------------------/
	Value range: H'0 - H'7F
	Value H'0 : No subscription type
	Value H'1 - H'7F : Subscription type 1 - 127
	"""

class SwitchIdentity:
	"""ASN.1 Formal Description
	SwitchIdentity ::= OCTET STRING (SIZE(2))
	|    |    |    |    |    |    |    |    |
	|  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
	|    |    |    |    |    |    |    |    |
	/---------------------------------------/
	| MSB                                   |   octet 1
	+---------------------------------------|
	|                                   LSB |   octet 2
	/---------------------------------------/
	Note: OCTET STRING is coded internally as
	an unsigned integer.
	Value range: H'1 - H'FFFF
	"""

class TargetIMEI:
	"""Target IMEI
	This LCS parameter includes the IMEI number for the UE
	being positioned.
	"""

class TargetIMSI:
	"""Target IMSI
	This LCS parameter includes the IMSI number for the UE
	being positioned.
	"""

class TargetLocationInformation:
	"""Target Location Information
	The Target Location Information contains the Cell Global
	Identity (CGI) if the target of the handover is GSM. The
	Target Location Information contains the Service Area
	Identity (SAI) if the target of the handover is WCDMA.
	"""

class TariffClass:
	"""ASN.1 Formal Description
	TariffClass ::= OCTET STRING (SIZE(2))
	|    |    |    |    |    |    |    |    |
	|  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
	|    |    |    |    |    |    |    |    |
	/---------------------------------------/
	| MSB                                   |  octet 1
	+---------------------------------------+
	|                                   LSB |  octet 2
	/---------------------------------------/
	Note: OCTET STRING is coded as an unsigned integer.
	Value varies according to operator's definition.
	Value range: H'0 - H'FFFF
	Value H'0: No tariff class is defined.
	"""

class TariffSwitchInd:
	"""ASN.1 Formal Description
	TariffSwitchInd ::= ENUMERATED
	(noTariffSwitch                    (0),
	tariffSwitchAfterStartOfCharging  (2))
	"""

class TDSCounter:
	"""TDS Counter
	The TDS Counter contains the number of received TDS
	related CHG messages, i.e. it reflects the number of
	telephone numbers supplied by the service provider
	when a mobile subscriber is using the telephone
	directory service.
	The parameter is only applicable for WCDMA Japan.
	"""

class TeleServiceCode:
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

class TerminatingAccessISDN:
	"""Terminating Access ISDN
	This parameter indicates that the terminating access has
	ISDN capabilities.
	It is received in the ACM message, and is output only in
	the case of an ISDN-ISDN call.
	The parameter is only applicable for WCDMA Japan.
	"""

class TerminatingCarrier:
	"""Terminating Carrier
	This parameter contains the Carrier Identification Code
	of the network in which the call terminates, that is,
	Terminating Local Exchange Carrier (TLEC). Terminating
	carrier received from another network may also contain
	POI-hierarchy information.
	Terminating carrier is not output for calls within one
	carrier network.
	Note: The last received Terminating Carrier will be stored
	in the CDR.
	The parameter is only applicable for WCDMA Japan.
	"""

class TerminatingChargeArea:
	"""Terminating Charge Area
	This parameter contains the location, specified with
	a Charge Area code, in which the call terminates. If
	a call terminates at an international carrier Terminating
	Charge Area may not be output.
	Note: The last received Terminating Charge Area will be
	stored in the CDR.
	The parameter is only applicable for WCDMA Japan.
	"""

class TerminatingMobileUserClass1:
	"""Terminating Mobile User Class 1
	This parameter contains Additional Mobile Service
	Information Type 1, obtained from Additional User Category
	(AUC) parameter transmitted in ISUP messages eACM/ACM, CHG,
	CPG and ANM.
	It is used to indicate service related information in
	the terminating side of the call, for example 'cellular
	telephone service'. It is received only from a mobile
	carrier.
	Note: The last received Terminating Mobile User Class
	1 is stored in the CDR.
	The parameter is only applicable for WCDMA Japan.
	"""

class TerminatingMobileUserClass2:
	"""Terminating Mobile User Class 2
	This parameter contains Additional Mobile Service
	Information Type 2, obtained from Additional User
	Category (AUC) parameter transmitted in ISUP messages
	eACM/ACM, CHG, CPG and ANM.
	It is used to indicate telecommunication method related
	information in the terminating side of the call,
	for example 'PDC 1500 MHz'. It is received only from
	a mobile carrier.
	Note: The last received Terminating Mobile User Class 2
	is stored in the CDR.
	The parameter is only applicable for WCDMA Japan.
	"""

class TerminatingUserClass:
	"""Terminating User Class
	This parameter is derived from the Additional User
	Category (AUC) parameter transmitted in ISUP messages
	eACM/ACM, CHG, CPG and ANM.
	Terminating user class specifies the type of phone
	used on the terminating side of the call in the fixed
	network.
	Values can be set to Pink or Train Payphone in the fixed
	system. This is possibly received from fixed network.
	Note: The last received Terminating User Class is stored
	in the CDR.
	The parameter is only applicable for WCDMA Japan.
	"""

class TimeForEvent:
	"""Time for Event  (M)
	This parameter is a time stamp for events.
	In case of AoC Charging service, the time of the
	reception of the acknowledgement from the mobile
	subscriber is recorded, both at call set-up and
	tariff switching.
	In case of AoC Information service, the time of
	sending the AoC data to the user equipment at
	tariff switching is recorded. At call set-up,
	no timestamp is recorded for the AoC information.
	In case of SCF charging output call record, the time
	for event of the first SCF transaction that generates
	charging data is registered in the IN service data
	Event Module. The corresponding date for event of the
	first SCF transaction that generates charging data is
	contained in parameter date in SCF Charging Output
	Call Module.
	"""

class TimeForStartOfCharge:
	"""Time for Start of Charging  (M)(P)
	Start of charging begins at B-answer. The time being
	registered is recorded using a 24-hour clock system.
	In mobile originating, roaming call forwarding, call
	forwarding, and transit Call Components, this parameter
	contains the time when the ISUP "ANSWER" message is
	received. In the mobile terminating Call Component,
	this parameter contains the time when the BSSAP/RANAP
	"CONNECT" message is received from the user equipment.
	For calls released before start of charging, the time
	for the release is registered. For long calls with partial
	outputs, the time for start of charging is the time
	when the previous output was made.
	For SMS and Subscriber Service Procedure, the
	time when charging is reserved is registered.
	If originating or terminating Call Components, or both,
	are not charged but Supplementary Service invocations made
	by the originating or terminating leg are charged, the
	Time for Start of Charge parameter is registered when the
	first chargeable Supplementary Service invocation is made
	from the beginning of the call or during the partial output
	period.
	"""

class TimeForStopOfCharge:
	"""Time for Stop of Charging  (P)
	The time for stop of charging is registered in
	this parameter. The time being registered
	is recorded using a 24-hour clock system.
	For mobile-originating and mobile-terminating call
	components, the reception of the BSSAP/RANAP message
	"DISCONNECT" or the ISUP message "RELEASE" marks the
	point where timing ends.
	If originating or terminating Call Components, or
	both, are not charged but Supplementary Service
	invocations made by the originating or terminating
	leg are charged, the Time for Stop of Charge parameter
	has the same value as the Time for Start of Charge
	parameter.
	"""

class TimeForTCSeizureCalled:
	"""Time for Called Party Traffic Channel Seizure
	This parameter contains the time of called party
	traffic channel seizure. The timestamp is registered
	after reception of the BSSAP message "ASSIGNMENT COMPLETE"
	or the RANAP message "ASSIGNMENT RESPONSE".
	In the case of a waiting call, this parameter is not output
	in the UE terminating Call Module.
	"""

class TimeForTCSeizureCalling:
	"""Time for Calling Party Traffic Channel Seizure
	This parameter contains the time of calling party
	traffic channel seizure. The timestamp is registered
	after reception of the BSSAP message "ASSIGNMENT COMPLETE"
	or the RANAP message "ASSIGNMENT RESPONSE".
	In the case of an enquiry call, this parameter is not
	output in the UE originating Call Module.
	"""

class TimeFromRegisterSeizureToStartOfCharging:
	"""Time from Register Seizure to Start of Charging  (M)
	This parameter registers the time from register seizure
	to start of charging.
	In case of calls for which charging is started (see
	the Time for Start of Charging parameter), this parameter
	contains the length of time from when the Register was
	seized until charging was started. The Register is seized
	for mobile-originating record when the BSSAP/RANAP message
	"SETUP" is received from the user equipment. For roaming
	call forwarding, call forwarding, transit, and mobile
	terminating records, the Register is seized when the
	ISUP "INITIAL ADDRESS MESSAGE" (IAM) message is received.
	In the case of call release before start of charging, the
	time from register seizure to call release is registered.
	"""

class TrafficActivityCode:
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

class TrafficClass:
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

class TransferDelay:
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

class TransparencyIndicator:
	"""ASN.1 Formal Description
	TransparencyIndicator ::= ENUMERATED
	(transparent                              (0),
	nonTransparent                           (1))
	"""

class TriggerData07:
	"""Trigger Data
	The Trigger data parameter stores data for each SCF
	invocation.
	The trigger data is sent to Charging Data Output when
	a dialogue towards an SCF has been opened as a result
	of processing an armed Trigger Detection Point (TDP).
	The first data will be stored in TriggerData 0. In the
	case of several dialogues resulting from processing of
	armed TDPs in the same call then each will produce
	trigger data to Call Data Output by using the first
	free number of Trigger Data.
	Note that if criteria for invoking a dialogue towards
	the SCF is not met during the call then no Trigger Data
	will be sent to Call Data Output. Trigger Data applies
	to CAMEL calls, extended CAMEL calls and to IN calls.
	The Trigger data are built up of the following:
	- Trigger Detection Point
	This parameter indicates at what point in the
	call the SCF invocation took place.
	- Service Key
	The Service key is sent to the SCF in the Initial
	Detection Point Operation. It is used as a
	reference by the SCF.
	- SCP Address
	The SCP address includes the full network address of
	the SCF/gsmSCF used for sending the Initial Detection
	Point operation.
	"""

class TypeOfCalledSubscriber:
	"""ASN.1 Formal Description
	TypeOfCalledSubscriber ::= ENUMERATED
	(pSTNSubscriber       (0),
	iSDNSubscriber       (1),
	unknownSubscriber    (2))
	"""

class TypeOfLocationRequest:
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

class TypeOfSignalling:
	"""ASN.1 Formal Description
	TypeOfSignalling ::= ENUMERATED
	(iSUPIsNotAppliedAllTheWay       (0),
	iSUPIsAppliedAllTheWay          (1),
	unknownSignalling               (2))
	"""

class UnsuccessfulPositioningDataReason:
	"""ASN.1 Formal Description
	UnsuccessfulPositioningDataReason ::= ENUMERATED
	(systemError                           (0),
	userDeniedDueToPrivacyVerification    (1))
	"""

class UserClass:
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

class UserTerminalPosition:
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

class UserToUserService1Information:
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

class USSDApplicationIdentifier:
	"""Unstructured Supplementary Service Data
	Application Identifier
	This parameter identifies the invoked or invoking
	USSD application.
	Each USSD application in an MSC/VLR is uniquely defined
	by an application identifier. This application identifier
	is a fixed value.
	The operator may associate service or procedure codes
	to these application identifiers.
	"""

class USSDOperationIdentifier:
	"""Unstructured Supplementary Service Data Operation
	Identifier
	This parameter contains detailed information about the
	invoked service within a USSD application.
	The USSD operation identifier allows identification
	of different operations which may exist and can be
	invoked within the same USSD application.
	This identifier is optional, that is, USSD
	applications may exist which do not need the use
	of the USSD operation identifier at all.
	"""

class USSDProcedureCode:
	"""Unstructured Supplementary Service Data Procedure Code
	This parameter identifies the call-related USSD service
	for a mobile-initiated service request.
	The parameter values are defined by operator and are
	administered with General Purpose Digit Analysis.
	The operator can associate a USSD procedure code with a
	USSD application identifier. The USSD procedure code is
	part of the MSC/VLR-supported format for the USSD strings
	of the user equipment which initiated USSD operations. For
	further details, see the Application Information for
	function block MUSSAN.
	This parameter is unavailable for a network-initiated
	service request.
	"""

class USSDServiceCode:
	"""Unstructured Supplementary Service Data Service Code
	This parameter identifies the call-independent
	USSD service in the case of a mobile-initiated
	service request.
	The parameter values are defined by the operator and
	are administered with General Purpose Digit Analysis.
	The operator can associate a USSD Service Code with
	a USSD Application Identifier. The service code is
	part of the MSC/VLR-supported formats for USSD strings
	of UE-initiated USSD operations. For further details,
	see the Application Information for function
	block MUSSAN.
	This parameter is unavailable for a network-initiated
	service request.
	"""

class VerticalAccuracy:
	"""Vertical Accuracy
	This LCS parameter expresses the requested vertical
	accuracy of the UE being positioned. The parameter is
	a part of LCS Quality of Service (QoS) received.
	"""

class VerticalCoordinateRequest:
	"""Vertical Coordinate Request
	This LCS parameter indicates in case vertical coordinates
	are requested for positioning the UE. The parameter is part
	of LCS Quality of Service (QoS) received.
	"""

class WPSCallIndicator:
	"""WPS Usage CDR Indicator
	This parameter indicates a Wireless Priority Service (WPS)
	call.
	The parameter is only applicable for GSM.
	1.5   Call Data Parameter Data Types
	"""

class AddressStringExtended:
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

class AirInterfaceUserRate:
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

class ApplicationIdentifier:
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

class AsyncSyncIndicator:
	"""ASN.1 Formal Description
	AsyncSyncIndicator ::= ENUMERATED
	(syncData        (0),
	asyncData       (1))
	"""

class BitRate:
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

class CarrierInfo:
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

class ChannelCodings:
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

class ChargeAreaCode:
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

class ChargingIndicator:
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

class ChargingOrigin:
	"""ASN.1 Formal Description
	ChargingOrigin ::= OCTET STRING (SIZE(1))
	|    |    |    |    |    |    |    |    |
	|  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
	|    |    |    |    |    |    |    |    |
	/---------------------------------------/
	| MSB                               LSB |
	/---------------------------------------/
	Note: The OCTET STRING is coded as an unsigned integer.
	Values vary according to operator's definition.
	Value range: H'1 - H'7F
	"""

class Counter:
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

class C7CHTMessage:
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

class DeliveryOfErroneousSDU:
	"""ASN.1 Formal Description
	DeliveryOfErroneousSDU ::= ENUMERATED
	(yes                              (0),
	no                               (1),
	noErrorDetectionConsideration    (2))
	"""

class Distributed:
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

class ErrorRatio:
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

class FixedNetworkUserRate:
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

class GenericDigitsSet:
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

class GenericNumbersSet:
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

class GlobalTitle:
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

class GlobalTitleAndSubSystemNumber:
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

class IMSI:
	"""ASN.1 Formal Description
	IMSI ::= TBCDString (SIZE(3..8))
	|    |    |    |    |    |    |    |    |
	|  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |
	|    |    |    |    |    |    |    |    |
	/---------------------------------------/
	|  MCC digit 2      |  MCC digit 1      | octet 1
	+-------------------+-------------------+
	|  MNC digit 1      |  MCC digit 3      | octet 2
	+-------------------+-------------------+
	|  MSIN digit 1     |  MNC digit 2      | octet 3
	+-------------------+-------------------+
	|  MSIN digit 3     |  MSIN digit 2     | octet 4
	/---------------------------------------/
	.
	.
	.
	/---------------------------------------/
	|  MSIN digit 2n-7  |  MSIN digit 2n-8  | octet n-1
	+-------------------+-------------------+
	|  See note         |  MSIN digit 2n-6  | octet n
	/---------------------------------------/
	Note: bits 5-8 of octet n contain
	- last MSIN digit, or
	- 1111 used as a filler when there is an odd
	total number of digits.
	MCC Mobile Country Code (octet 1 and bits 1-4 of octet 2)
	MNC Mobile Network Code (bits 5-8 of octet 2 and bits 1-4
	of octet 3).
	MSIN Mobile Subscriber Identification Number
	The total number of digits should not exceed 15.
	Digits 0 to 9, two digits per octet,
	each digit encoded 0000 to 1001
	"""

class LCSAccuracy:
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

class LegID:
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

class LocationInformation:
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

class MSNB:
	"""ASN.1 Formal Description
	MSNB ::= TBCDString (SIZE(3..8))
	"""

class NumberOfChannels:
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

class NumberOfOperations:
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

class NumberOfShortMessage:
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

class OperationIdentifier:
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

class PointCodeAndSubSystemNumber:
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

class ProcedureCode:
	"""ASN.1 Formal Description
	ProcedureCode ::= TBCDString (SIZE(1))
	"""

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

class ServiceCode:
	"""ASN.1 Formal Description
	ServiceCode ::= TBCDString (SIZE(1..2))
	"""

class ServiceKey:
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

class Single:
	"""ASN.1 Formal Description
	Single ::=  ENUMERATED
	(aPartyToBeCharged      (0),
	bPartyToBeCharged      (1),
	cPartyToBeCharged      (2),
	otherPartyToBeCharged  (3))
	"""

class SpeechCoderVersion:
	"""ASN.1 Formal Description
	SpeechCoderVersion ::= ENUMERATED
	(fullRateVersion1         (0),
	fullRateVersion2         (1),
	fullRateVersion3         (2),
	halfRateVersion1         (3),
	halfRateVersion2         (4),
	halfRateVersion3         (5))
	"""

class TargetRNCid:
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

class Time:
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

class TransitCarrierInfo:
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

class TriggerDetectionPoint:
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

class UILayer1Protocol:
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

class UserRate:
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

