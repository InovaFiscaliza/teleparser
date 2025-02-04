from enum import Enum
from dataclasses import dataclass


@dataclass
class ProcessConfig:
    parallel_processes: int = 5  # Number of parallel processes
    chunk_size: int = 1000  # Records per chunk
    max_files_per_batch: int = 8000  # Maximum files in memory


class CDRType(str, Enum):
    VOICE_VIVO_TIM_CLARO = "voice_vivo_tim_claro"
    VOICE_CLARO_NOKIA = "voice_claro_nokia"
    VOICE_OI = "voice_oi"
    VOICE_NEXTEL_HUAWEI = "voice_nextel_huawei"
    VOICE_ALGAR = "voice_algar"
    DATA_ALL = "data_all"
    VOLTE_3GPP = "volte_3gpp"
    VOLTE_NON_3GPP_TIM = "volte_non_3gpp_tim"
    VOLTE_NON_3GPP_CLARO = "volte_non_3gpp_claro"
    STIR_TIM = "stir_tim"


@dataclass
class CDRHeaders(Enum):
    VOICE = [
        "Reference",
        "Origin",
        "Date",
        "Time",
        "Call_Type",
        "Biller",
        "IMSI",
        "1stCelA",
        "Outgoing_route",
        "Destination",
    ]
    DATA = [
        "CDR_Type",
        "listOfTrafficVolumes",
        "Location",
        "servedMSISDN",
        "listOfServiceData",
        "recordSequenceNumber",
        "CauseforRecClosing",
        "chargingID",
        "duration",
        "ggsnAddress",
        "OpeningTime",
        "StartTime",
        "Diagnostics",
        "Radio",
        "ServedIMSI",
        "Empty_Column",
        "IMEI",
        "File",
    ]

    VOLTE_3GPP = [
        "list-Of-Calling-Party-Address",
        "recordOpeningTime",
        "Time",
        "role-of-Node",
        "called - Party - Address",
        "dialled-Party-Address",
        "List-Of-Called-Asserted-Identity",
        "Duration",
        "accessNetworkInformation",
        "List-of-Subscription-ID",
        "private-User-Equipment-Info",
        "MSC-Number",
        "network-Call-Reference",
        "causeForRecordClosing",
        "interOperatorIdentifiers",
        "sIP-Method",
    ]
