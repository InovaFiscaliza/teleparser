import struct
from datetime import datetime, timedelta
from dataclasses import dataclass
from typing import Generator, Tuple
import socket
from tqdm.auto import tqdm
from .transform import transform_ericsson_volte

# Vendor IDs
VENDOR_3GPP = 10415
VENDOR_ERICSSON = 193
VENDOR_HUAWEI = 2011
# Type constants (as provided)
TYPE_OCTET_STRING = 0
TYPE_INTEGER_32 = 1
TYPE_UNSIGNED_32 = 2
TYPE_UNSIGNED_64 = 3
TYPE_UTF8_STRING = 4
TYPE_GROUPED = 8
TYPE_TIME = 9
TYPE_ENUMERATED = 10
TYPE_DIAMETER_IDENTITY = 11
TYPE_ADDRESS = 12

STRUCT_UNSIGNED_32 = struct.Struct(">I")
STRUCT_SIGNED_32 = struct.Struct(">i")
STRUCT_UNSIGNED_64 = struct.Struct(">Q")

KNOWN_SIZES = {
    TYPE_UNSIGNED_32: 4,
    TYPE_UNSIGNED_64: 8,
    TYPE_INTEGER_32: 4,
}


@dataclass
class VendorID:
    """Data class to represent a Diameter AVP with vendor information"""

    avp: str
    type: int
    acr_flag: str | None = None
    vendor_id: int | None = None


AVP_DB = {
    1: VendorID("User-Name", TYPE_UTF8_STRING),
    2: VendorID("3GPP-Charging-Id", TYPE_OCTET_STRING, "V"),
    18: VendorID("3GPP-SGSN-MCC-MNC", TYPE_UTF8_STRING, "VM", VENDOR_3GPP),
    23: VendorID("3GPP-MS-TimeZone", TYPE_OCTET_STRING, "V", VENDOR_3GPP),
    55: VendorID("Event-Timestamp", TYPE_TIME, "M"),
    85: VendorID("Acct-Interim-Interval", TYPE_UNSIGNED_32, "M"),
    259: VendorID("Acct-Application-Id", TYPE_UNSIGNED_32, "M"),
    263: VendorID("Session-Id", TYPE_UTF8_STRING, "M"),
    264: VendorID("Origin-Host", TYPE_DIAMETER_IDENTITY),
    266: VendorID("Vendor-Id", TYPE_UNSIGNED_32),
    268: VendorID("Result-Code", TYPE_UNSIGNED_32, "M"),
    283: VendorID("Destination-Realm", TYPE_DIAMETER_IDENTITY),
    284: VendorID("IMS-Service-Identification", TYPE_UTF8_STRING, "V", VENDOR_ERICSSON),
    285: VendorID("Ericsson-Service-Information", TYPE_GROUPED, "V", VENDOR_ERICSSON),
    286: VendorID(
        "Called-Party-Original-Address", TYPE_UTF8_STRING, "VM", VENDOR_ERICSSON
    ),
    293: VendorID("Destination-Host", TYPE_DIAMETER_IDENTITY, "M"),
    296: VendorID("Origin-Realm", TYPE_DIAMETER_IDENTITY),
    297: VendorID("Experimental-Result", TYPE_GROUPED),
    298: VendorID("Experimental-Result-Code", TYPE_UNSIGNED_32),
    333: VendorID("GPRS-Roaming-Status ", TYPE_ENUMERATED, "VM", VENDOR_ERICSSON),
    336: VendorID("SIP-Reason-Cause", TYPE_UNSIGNED_32, "VM", VENDOR_ERICSSON),
    337: VendorID("SIP-Reason-Text", TYPE_UTF8_STRING, "VM", VENDOR_ERICSSON),
    338: VendorID("SIP-Ringing-Timestamp", TYPE_TIME, "V", VENDOR_ERICSSON),
    340: VendorID("Event-NTP-Timestamp", TYPE_OCTET_STRING, "VM", VENDOR_ERICSSON),
    # SBG
    363: VendorID("Accounting-Input-Octets", TYPE_UNSIGNED_64, "M"),
    364: VendorID("Accounting-Output-Octets", TYPE_UNSIGNED_64, "M"),
    365: VendorID("Accounting-Input-Packets", TYPE_UNSIGNED_64, "M"),
    366: VendorID("Accounting-Output-Packets", TYPE_UNSIGNED_64, "M"),
    420: VendorID("CC-Time", TYPE_UNSIGNED_32, "M"),
    443: VendorID("Subscription-Id", TYPE_GROUPED, "M"),
    444: VendorID("Subscription-Id-Data", TYPE_UTF8_STRING, "M"),
    450: VendorID("Subscription-Id-Type", TYPE_ENUMERATED, "M"),
    458: VendorID("User-Equipment-Info", TYPE_GROUPED, "M"),
    459: VendorID("User-Equipment-Info-Type", TYPE_ENUMERATED, "M"),
    460: VendorID("User-Equipment-Info-Value", TYPE_OCTET_STRING, "M"),
    461: VendorID("Service-Context-Id", TYPE_UTF8_STRING, "M"),
    480: VendorID("Accounting-Record-Type", TYPE_ENUMERATED, "M"),
    485: VendorID("Accounting-Record-Number", TYPE_UNSIGNED_32, "M"),
    518: VendorID("Media-Component-Number", TYPE_UNSIGNED_32, "VM", VENDOR_3GPP),
    650: VendorID("Session-Priority", TYPE_ENUMERATED, "V", VENDOR_3GPP),
    701: VendorID("MSISDN", TYPE_OCTET_STRING, "VM", VENDOR_3GPP),
    823: VendorID("Event-Type", TYPE_GROUPED, "VM", VENDOR_3GPP),
    824: VendorID("SIP-Method", TYPE_UTF8_STRING, "VM", VENDOR_3GPP),
    826: VendorID("Content-Type", TYPE_UTF8_STRING, "VM", VENDOR_3GPP),
    827: VendorID("Content-Length", TYPE_UNSIGNED_32, "VM", VENDOR_3GPP),
    828: VendorID("Content-Disposition", TYPE_UTF8_STRING, "VM", VENDOR_3GPP),
    829: VendorID("Role-of-Node", TYPE_ENUMERATED, "VM", VENDOR_3GPP),
    830: VendorID("User-Session-Id", TYPE_UTF8_STRING, "VM", VENDOR_3GPP),
    831: VendorID("Calling-Party-Address", TYPE_UTF8_STRING, "VM", VENDOR_3GPP),
    832: VendorID("Called-Party-Address", TYPE_UTF8_STRING, "VM", VENDOR_3GPP),
    833: VendorID("Time-Stamps", TYPE_GROUPED, "VM", VENDOR_3GPP),
    834: VendorID("SIP-Request-Timestamp", TYPE_TIME, "VM", VENDOR_3GPP),
    835: VendorID("SIP-Response-Timestamp", TYPE_TIME, "VM", VENDOR_3GPP),
    838: VendorID("Inter-Operator-Identifier", TYPE_GROUPED, "VM", VENDOR_3GPP),
    839: VendorID("Originating-IOI", TYPE_UTF8_STRING, "VM", VENDOR_3GPP),
    840: VendorID("Terminating-IOI", TYPE_UTF8_STRING, "VM", VENDOR_3GPP),
    841: VendorID("IMS-Charging-Identifier", TYPE_UTF8_STRING, "VM", VENDOR_3GPP),
    842: VendorID("SDP-Session-Description", TYPE_UTF8_STRING, "VM", VENDOR_3GPP),
    843: VendorID("SDP-Media-Component", TYPE_GROUPED, "VM", VENDOR_3GPP),
    844: VendorID("SDP-Media-Name", TYPE_UTF8_STRING, "VM", VENDOR_3GPP),
    845: VendorID("SDP-Media-Description", TYPE_UTF8_STRING, "VM", VENDOR_3GPP),
    847: VendorID("GGSN-Address", TYPE_ADDRESS, "VM", VENDOR_3GPP),
    848: VendorID("Served-Party-IP-Address", TYPE_ADDRESS, "VM", VENDOR_3GPP),
    861: VendorID("Cause-Code", TYPE_INTEGER_32, "VM", VENDOR_3GPP),
    862: VendorID("Node-Functionality", TYPE_ENUMERATED, "VM", VENDOR_3GPP),
    863: VendorID("Service-Specific-Data", TYPE_UTF8_STRING, "VM", VENDOR_3GPP),
    864: VendorID("Originator", TYPE_ENUMERATED, "VM", VENDOR_3GPP),
    873: VendorID("Service-Information", TYPE_GROUPED, "VM", VENDOR_3GPP),
    874: VendorID("PS-Information", TYPE_GROUPED, "VM", VENDOR_3GPP),
    876: VendorID("IMS-Information", TYPE_GROUPED, "VM", VENDOR_3GPP),
    878: VendorID("LCS-Information", TYPE_GROUPED, "VM", VENDOR_3GPP),
    882: VendorID("Media-Initiator-Flag", TYPE_ENUMERATED, "VM", VENDOR_3GPP),
    889: VendorID("Message-Body", TYPE_GROUPED, "VM", VENDOR_3GPP),
    1061: VendorID(
        "MMT-Information", TYPE_GROUPED, "V", 193
    ),  # Ericsson vendor ID is 193
    # Ericsson Statistics AVPs
    1087: VendorID(
        "Pockets-Discarded-Filtering", TYPE_UNSIGNED_64, "V", VENDOR_ERICSSON
    ),
    1088: VendorID(
        "Octets-Discarded-Filtering", TYPE_UNSIGNED_64, "V", VENDOR_ERICSSON
    ),
    1089: VendorID(
        "Pockets-Discarded-Policing", TYPE_UNSIGNED_64, "V", VENDOR_ERICSSON
    ),
    1090: VendorID("Octets-Discarded-Policing", TYPE_UNSIGNED_64, "V", VENDOR_ERICSSON),
    1091: VendorID("Pockets-Out-Of-Sequence", TYPE_UNSIGNED_64, "V", VENDOR_ERICSSON),
    1092: VendorID("Pockets-Lost", TYPE_UNSIGNED_64, "V", VENDOR_ERICSSON),
    1093: VendorID(
        "RTCP-Reported-Average-Jitter", TYPE_UNSIGNED_32, "V", VENDOR_ERICSSON
    ),
    1094: VendorID(
        "RTCP-Reported-Packets-Lost", TYPE_UNSIGNED_64, "V", VENDOR_ERICSSON
    ),
    1095: VendorID("Accepted-MSRP-Chunks", TYPE_UNSIGNED_64, "V", VENDOR_ERICSSON),
    1096: VendorID("Discarded-MSRP-Chunks", TYPE_UNSIGNED_64, "V", VENDOR_ERICSSON),
    # Ericsson Timestamp and Session AVPs
    1127: VendorID("Conference-Id", TYPE_UTF8_STRING, "V", VENDOR_ERICSSON),
    1128: VendorID("Related-ICID", TYPE_UTF8_STRING, "V", VENDOR_ERICSSON),
    1129: VendorID(
        "Supplementary-Service-Information", TYPE_GROUPED, "V", VENDOR_ERICSSON
    ),
    1130: VendorID(
        "Supplementary-Service-Identity", TYPE_ENUMERATED, "V", VENDOR_ERICSSON
    ),
    1131: VendorID(
        "Supplementary-Service-Action", TYPE_ENUMERATED, "V", VENDOR_ERICSSON
    ),
    1133: VendorID("Redirecting-Party-Address", TYPE_UTF8_STRING, "V", VENDOR_ERICSSON),
    1141: VendorID(
        "Calling-Party-Address-Presentation-Status", TYPE_ENUMERATED, "V", 193
    ),
    1142: VendorID(
        "Called-Asserted-Identity-Presentation-Status", TYPE_ENUMERATED, "V", 193
    ),
    1153: VendorID("From-Header", TYPE_UTF8_STRING, "V", VENDOR_ERICSSON),
    1160: VendorID("Dial-Around-Indicator", TYPE_UTF8_STRING, "V", VENDOR_ERICSSON),
    1178: VendorID("Occurrence-Timestamp", TYPE_TIME, "V", VENDOR_ERICSSON),
    1182: VendorID("Session-Priority", TYPE_ENUMERATED, "V", VENDOR_ERICSSON),
    # Ericsson User Agent AVPs
    # Ericsson Charging AVPs
    1206: VendorID("GSM-Call-Reference-Number", TYPE_UTF8_STRING, "V", VENDOR_ERICSSON),
    1207: VendorID("MSC-Address", TYPE_UTF8_STRING, "V", VENDOR_ERICSSON),
    1249: VendorID("Service-Specific-Info", TYPE_GROUPED, "VM", VENDOR_3GPP),
    1250: VendorID("Called-Asserted-Identity", TYPE_UTF8_STRING, "VM", VENDOR_3GPP),
    1251: VendorID("Requested-Party-Address", TYPE_UTF8_STRING, "VM", VENDOR_3GPP),
    1252: VendorID("Originating-User-Agent", TYPE_UTF8_STRING, "V", VENDOR_ERICSSON),
    1253: VendorID("Terminating-User-Agent", TYPE_UTF8_STRING, "V", VENDOR_ERICSSON),
    1256: VendorID(
        "SIP-Ringing-Timestamp-Fraction", TYPE_UNSIGNED_32, "V", VENDOR_ERICSSON
    ),
    1257: VendorID("Service-Specific-Type", TYPE_UNSIGNED_32, "VM", VENDOR_3GPP),
    1261: VendorID("Authentication-Method", TYPE_ENUMERATED, "VM", VENDOR_ERICSSON),
    1262: VendorID(
        "From-Header-Presentation-Status", TYPE_ENUMERATED, "V", VENDOR_ERICSSON
    ),
    1263: VendorID("Access-Network-Information", TYPE_OCTET_STRING, "VM", VENDOR_3GPP),
    1264: VendorID("Transaction-Info", TYPE_GROUPED, "V", VENDOR_ERICSSON),
    1265: VendorID("Transaction-Type", TYPE_ENUMERATED, "V", VENDOR_ERICSSON),
    1266: VendorID("Transaction-Data-Name", TYPE_UTF8_STRING, "V", VENDOR_ERICSSON),
    1267: VendorID("Transaction-Data-Value", TYPE_UTF8_STRING, "V", VENDOR_ERICSSON),
    1298: VendorID(
        "Additional-Charging-Information", TYPE_UTF8_STRING, "V", VENDOR_ERICSSON
    ),
    1302: VendorID("Routing-Call-Type", TYPE_UTF8_STRING, "V", VENDOR_ERICSSON),
    1303: VendorID("Analyzed-Call-Type", TYPE_UTF8_STRING, "V", VENDOR_ERICSSON),
    1305: VendorID("Disconnect-Direction", TYPE_ENUMERATED, "VM", VENDOR_ERICSSON),
    1307: VendorID("Service-Number-Type", TYPE_ENUMERATED, "V", VENDOR_ERICSSON),
    1308: VendorID(
        "Common-Policy-Rule-Identity", TYPE_UTF8_STRING, "V", VENDOR_ERICSSON
    ),
    1314: VendorID("SCC-Service-Identity", TYPE_ENUMERATED, "V", VENDOR_ERICSSON),
    1315: VendorID("SCC-TADS-Decision", TYPE_ENUMERATED, "V", VENDOR_ERICSSON),
    1330: VendorID("Served-User", TYPE_UTF8_STRING, "V", VENDOR_ERICSSON),
    1346: VendorID("XCON-Id", TYPE_UTF8_STRING, "V", VENDOR_ERICSSON),
    1357: VendorID("Party-To-Charge", TYPE_UNSIGNED_32, "V", VENDOR_ERICSSON),
    1371: VendorID("Service-Suppression-Info", TYPE_GROUPED, "V", VENDOR_ERICSSON),
    1372: VendorID(
        "Matched-Regular-Expression", TYPE_UTF8_STRING, "V", VENDOR_ERICSSON
    ),
    1373: VendorID("Services-To-Suppress", TYPE_UTF8_STRING, "V", VENDOR_ERICSSON),
    1380: VendorID("Tenant", TYPE_UTF8_STRING, "V", VENDOR_ERICSSON),
    1384: VendorID("CCMP-User-Info", TYPE_UTF8_STRING, "V", VENDOR_ERICSSON),
    1388: VendorID("UHTZ-Offset", TYPE_UTF8_STRING, "V", VENDOR_ERICSSON),
    1389: VendorID("Participants-Involved", TYPE_UTF8_STRING, "V", VENDOR_ERICSSON),
    1390: VendorID("Participants-List", TYPE_UTF8_STRING, "V", VENDOR_ERICSSON),
    1393: VendorID("Forward-TTC-Charging-Headers", TYPE_GROUPED, "V", VENDOR_ERICSSON),
    1394: VendorID("Backward-TTC-Charging-Headers", TYPE_GROUPED, "V", VENDOR_ERICSSON),
    1395: VendorID("Charging-Area", TYPE_UTF8_STRING, "V", VENDOR_ERICSSON),
    1396: VendorID("Carrier-Information", TYPE_OCTET_STRING, "V", VENDOR_ERICSSON),
    1397: VendorID("Additional-User-Category", TYPE_OCTET_STRING, "V", VENDOR_ERICSSON),
    1398: VendorID("Flexible-Charging-Info", TYPE_OCTET_STRING, "V", VENDOR_ERICSSON),
    1406: VendorID(
        "Forward-TTC-Charging-Parameters", TYPE_UTF8_STRING, "V", VENDOR_ERICSSON
    ),
    1407: VendorID("Backward-TTC-Charging-Parameters", TYPE_UTF8_STRING, "V", 193),
    1433: VendorID("AS-Type", TYPE_ENUMERATED, "V", VENDOR_ERICSSON),
    1436: VendorID(
        "Last-Access-Network-Information", TYPE_UTF8_STRING, "V", VENDOR_ERICSSON
    ),
    1460: VendorID("Transaction-SIP-Message", TYPE_UTF8_STRING, "V", VENDOR_ERICSSON),
    1463: VendorID("Subscriber-Type", TYPE_ENUMERATED, "V", VENDOR_ERICSSON),
    1464: VendorID("UC-Mobility-Call-Leg", TYPE_ENUMERATED, "V", VENDOR_ERICSSON),
    1465: VendorID("Interim-Reason", TYPE_ENUMERATED, "V", VENDOR_ERICSSON),
    1477: VendorID("Ro-Status", TYPE_ENUMERATED, "V", VENDOR_ERICSSON),
    1478: VendorID("Ro-Information", TYPE_GROUPED, "V", VENDOR_ERICSSON),
    1527: VendorID("Analyzed-B-Number-Type", TYPE_UTF8_STRING, "V", VENDOR_ERICSSON),
    1531: VendorID("Caller-Category", TYPE_UNSIGNED_32, "V", VENDOR_ERICSSON),
    1532: VendorID("Caller-Sub-Category", TYPE_UNSIGNED_32, "V", VENDOR_ERICSSON),
    1533: VendorID("Caller-Treatment", TYPE_ENUMERATED, "V", VENDOR_ERICSSON),
    1536: VendorID(
        "Caller-Category-Presentation", TYPE_UTF8_STRING, "V", VENDOR_ERICSSON
    ),
    2023: VendorID("Carrier-Select-Routing-Information", TYPE_UTF8_STRING, "VM", 10415),
    2024: VendorID(
        "Number-Portability-Routing-Information", TYPE_UTF8_STRING, "VM", 10415
    ),
    2030: VendorID("MMTel-Information", TYPE_GROUPED, "VM", VENDOR_3GPP),
    2035: VendorID("Associated-Party-Address", TYPE_UTF8_STRING, "VM", VENDOR_3GPP),
    2036: VendorID("SDP-Type", TYPE_ENUMERATED, "VM", VENDOR_3GPP),
    2048: VendorID("Supplementary-Service", TYPE_GROUPED, "VM", VENDOR_3GPP),
    2301: VendorID("SIP-Request-Timestamp-Fraction", TYPE_UNSIGNED_32, "VM", 10415),
    2302: VendorID("SIP-Response-Timestamp-Fraction", TYPE_UNSIGNED_32, "VM", 10415),
    2304: VendorID("CUG-Information", TYPE_OCTET_STRING, "VM", VENDOR_3GPP),
    2320: VendorID("Outgoing-Session-Id", TYPE_UTF8_STRING, "VM", VENDOR_3GPP),
    2711: VendorID(
        "Related-IMS-Charging-Identifier", TYPE_UTF8_STRING, "VM", VENDOR_3GPP
    ),
    2712: VendorID(
        "Related-IMS-Charging-Identifier-Node", TYPE_ADDRESS, "VM", VENDOR_3GPP
    ),
    2713: VendorID("IMS-Visited-Network-Identifier", TYPE_UTF8_STRING, "VM", 10415),
    2819: VendorID("RAN-NAS-Relapse-Cause", TYPE_OCTET_STRING, "V", VENDOR_3GPP),
    3401: VendorID("Reason-Header", TYPE_UTF8_STRING, "VM", VENDOR_3GPP),
    3402: VendorID("Instance-id", TYPE_UTF8_STRING, "VM", VENDOR_3GPP),
    # Huawei vendor-specific AVPs
    6103: VendorID("User-Agent-Value", TYPE_UTF8_STRING, "VMP", VENDOR_HUAWEI),
    6104: VendorID("IN-Information", TYPE_GROUPED, "VMP", VENDOR_HUAWEI),
    6105: VendorID("Service-Key", TYPE_UNSIGNED_32, "VMP", VENDOR_HUAWEI),
    6106: VendorID("IN-Service-Number", TYPE_UTF8_STRING, "VMP", VENDOR_HUAWEI),
    6107: VendorID("Session-Release-Mode", TYPE_UNSIGNED_32, "VMP", VENDOR_HUAWEI),
    6109: VendorID("Fci-Free-Format-Data", TYPE_OCTET_STRING, "VMP", VENDOR_HUAWEI),
    6110: VendorID(
        "Fci-Free-Format-Data-Manner", TYPE_ENUMERATED, "VMP", VENDOR_HUAWEI
    ),
    6111: VendorID("Default-Call-Handling", TYPE_ENUMERATED, "VMP", VENDOR_HUAWEI),
    6114: VendorID("Initial-Location", TYPE_UTF8_STRING, "VMP", VENDOR_HUAWEI),
    6115: VendorID("Change-of-Location", TYPE_GROUPED, "VMP", VENDOR_HUAWEI),
    6116: VendorID("Location-Info", TYPE_UTF8_STRING, "VMP", VENDOR_HUAWEI),
    6117: VendorID("Scf-Address", TYPE_OCTET_STRING, "VMP", VENDOR_HUAWEI),
    6118: VendorID("Level-Of-Camel-Service", TYPE_OCTET_STRING, "VMP", VENDOR_HUAWEI),
    6119: VendorID("Charge-Class", TYPE_UNSIGNED_32, "VMP", VENDOR_HUAWEI),
    6120: VendorID("Substituted-Location-Info", TYPE_UTF8_STRING, "VMP", VENDOR_HUAWEI),
    6121: VendorID("Message-Reference", TYPE_OCTET_STRING, "VMP", VENDOR_HUAWEI),
    6122: VendorID("Call-Reference-Number", TYPE_UTF8_STRING, "VMP", VENDOR_HUAWEI),
    6123: VendorID("VMSC-Address", TYPE_UTF8_STRING, "VMP", VENDOR_HUAWEI),
    6124: VendorID("SMS-Result", TYPE_ENUMERATED, "VMP", VENDOR_HUAWEI),
    6125: VendorID("Map-Fail-Cause", TYPE_UNSIGNED_32, "VMP", VENDOR_HUAWEI),
    6126: VendorID(
        "Maximum-Of-Concatenated-SMS", TYPE_UNSIGNED_32, "VMP", VENDOR_HUAWEI
    ),
    6127: VendorID(
        "Concatenated-SMS-Reference-Number", TYPE_UNSIGNED_32, "VMP", VENDOR_HUAWEI
    ),
    6128: VendorID(
        "Sequence-Number-Of-Current-SMS", TYPE_UNSIGNED_32, "VMP", VENDOR_HUAWEI
    ),
    6129: VendorID("IN-Generic-Number", TYPE_UTF8_STRING, "VMP", VENDOR_HUAWEI),
    6130: VendorID("End-Of-In", TYPE_UTF8_STRING, "VMP", VENDOR_HUAWEI),
    6131: VendorID("Triggered_IN_Flag", TYPE_UNSIGNED_32, "VMP", VENDOR_HUAWEI),
    6132: VendorID("Routing-Category", TYPE_UNSIGNED_32, "VMP", VENDOR_HUAWEI),
    6133: VendorID("Routing-Category-Ext", TYPE_UNSIGNED_32, "VMP", VENDOR_HUAWEI),
    6134: VendorID("IN-Bypass", TYPE_UNSIGNED_32, "VMP", VENDOR_HUAWEI),
    6135: VendorID("Network-Call-Reference", TYPE_UTF8_STRING, "VMP", VENDOR_HUAWEI),
    6136: VendorID("Ut-Operate-Result", TYPE_UNSIGNED_32, "VMP", VENDOR_HUAWEI),
    6137: VendorID("SCI-Charge-Number", TYPE_OCTET_STRING, "VMP", VENDOR_HUAWEI),
    6138: VendorID("FCI-Charge-Number", TYPE_OCTET_STRING, "VMP", VENDOR_HUAWEI),
    6139: VendorID("FCI-Charged-Party-ID", TYPE_OCTET_STRING, "VMP", VENDOR_HUAWEI),
    6140: VendorID("Camel-Destination-Number", TYPE_UTF8_STRING, "VMP", VENDOR_HUAWEI),
    6141: VendorID(
        "Camel-Destination-Number-Type", TYPE_ENUMERATED, "VMP", VENDOR_HUAWEI
    ),
    6142: VendorID("Sip-From-Uri", TYPE_UTF8_STRING, "VMP", VENDOR_HUAWEI),
    6143: VendorID("User-Time-Zone", TYPE_UTF8_STRING, "VMP", VENDOR_HUAWEI),
    6144: VendorID("Call-Transfer-Info", TYPE_GROUPED, "VMP", VENDOR_HUAWEI),
    6145: VendorID("Call-Transfer-Type", TYPE_ENUMERATED, "VMP", VENDOR_HUAWEI),
    6146: VendorID("Call-Transfer-Data", TYPE_UTF8_STRING, "VMP", VENDOR_HUAWEI),
    6147: VendorID("Recording-Entity-ID", TYPE_UTF8_STRING, "VMP", VENDOR_HUAWEI),
    6148: VendorID("Service-Operate-Result", TYPE_UNSIGNED_32, "VMP", VENDOR_HUAWEI),
    6149: VendorID(
        "Number-Of-Video-Participants", TYPE_UNSIGNED_32, "VMP", VENDOR_HUAWEI
    ),
    6150: VendorID("aOCParameters", TYPE_OCTET_STRING, "VMP", VENDOR_HUAWEI),
    6151: VendorID("Account-Code", TYPE_OCTET_STRING, "VMP", VENDOR_HUAWEI),
    20820: VendorID("SDP-Media-Identifier", TYPE_ENUMERATED, "VMP", VENDOR_HUAWEI),
    22661: VendorID("Group-ID", TYPE_UNSIGNED_32, "VMP", VENDOR_HUAWEI),
    22662: VendorID("Private-Number", TYPE_UTF8_STRING, "VMP", VENDOR_HUAWEI),
    22663: VendorID("VPN-Call-Property", TYPE_ENUMERATED, "VMP", VENDOR_HUAWEI),
    22664: VendorID("MscNumer", TYPE_UTF8_STRING, "VMP", VENDOR_HUAWEI),
    22681: VendorID("Drvcc-Info", TYPE_GROUPED, "VMP", VENDOR_HUAWEI),
    22682: VendorID("Drvcc-Type", TYPE_ENUMERATED, "VMP", VENDOR_HUAWEI),
    22683: VendorID("Drvcc-Request-Time", TYPE_UTF8_STRING, "VMP", VENDOR_HUAWEI),
    22684: VendorID("Drvcc-Transfer-Number", TYPE_UTF8_STRING, "VMP", VENDOR_HUAWEI),
    22685: VendorID("Drvcc-Transfer-Identity", TYPE_UTF8_STRING, "VMP", VENDOR_HUAWEI),
    22686: VendorID("Peer-Subgroup-ID", TYPE_UNSIGNED_32, "VMP", VENDOR_HUAWEI),
    22700: VendorID("Interim-Time-Stamps", TYPE_GROUPED, "VMP", VENDOR_HUAWEI),
    22701: VendorID("Interim-Start-Time-Stamps", TYPE_TIME, "VMP", VENDOR_HUAWEI),
    22702: VendorID("Interim-End-Time-Stamps", TYPE_TIME, "VMP", VENDOR_HUAWEI),
    22703: VendorID("Special-CDR-flag", TYPE_UNSIGNED_32, "VMP", VENDOR_HUAWEI),
    22704: VendorID("UserDataLength-SMS", TYPE_UNSIGNED_32, "VMP", VENDOR_HUAWEI),
    22705: VendorID(
        "Call-Identification-Number", TYPE_UTF8_STRING, "VMP", VENDOR_HUAWEI
    ),
    22706: VendorID("Interruption-Time", TYPE_UNSIGNED_32, "VMP", VENDOR_HUAWEI),
    22707: VendorID("Origin-For-Charging", TYPE_UTF8_STRING, "VMP", VENDOR_HUAWEI),
    22708: VendorID("Outgoing-Route", TYPE_UTF8_STRING, "VMP", VENDOR_HUAWEI),
    22709: VendorID("Incoming-Route", TYPE_UTF8_STRING, "VMP", VENDOR_HUAWEI),
    22710: VendorID("Initial-Visit-CGI", TYPE_UTF8_STRING, "VMP", VENDOR_HUAWEI),
    22711: VendorID("Called-MNP-Info", TYPE_UTF8_STRING, "VMP", VENDOR_HUAWEI),
    22712: VendorID("Subscription-Type", TYPE_UTF8_STRING, "VMP", VENDOR_HUAWEI),
    22713: VendorID("Translated-Number", TYPE_UTF8_STRING, "VMP", VENDOR_HUAWEI),
    22714: VendorID("MTC-Roaming-Number", TYPE_UTF8_STRING, "VMP", VENDOR_HUAWEI),
    22715: VendorID("Redirecting-Number", TYPE_UTF8_STRING, "VMP", VENDOR_HUAWEI),
    22716: VendorID("RCF-Roaming-Number", TYPE_UTF8_STRING, "VMP", VENDOR_HUAWEI),
    22717: VendorID("RCF-Indication", TYPE_UNSIGNED_32, "VMP", VENDOR_HUAWEI),
    22718: VendorID(
        "Finish-P-Access-Network-Information", TYPE_UTF8_STRING, "VMP", VENDOR_HUAWEI
    ),
    22720: VendorID("Fail-AS-Addr", TYPE_GROUPED, "VMP", VENDOR_HUAWEI),
    22721: VendorID("iFCSeq", TYPE_UNSIGNED_32, "VMP", VENDOR_HUAWEI),
    22722: VendorID("ASPriority", TYPE_UNSIGNED_32, "VMP", VENDOR_HUAWEI),
    22723: VendorID("iFCAddr", TYPE_UTF8_STRING, "VMP", VENDOR_HUAWEI),
    22724: VendorID("Acct-Interaction-With-IP", TYPE_UNSIGNED_32, "VMP", VENDOR_HUAWEI),
    22735: VendorID(
        "Acct-Resource-Charge-IP-number", TYPE_OCTET_STRING, "VMP", VENDOR_HUAWEI
    ),
    22736: VendorID("Trigger-Detection-Point", TYPE_UNSIGNED_32, "VMP", VENDOR_HUAWEI),
    22737: VendorID("Time-For-TH-EOS", TYPE_TIME, "VMP", VENDOR_HUAWEI),
    22738: VendorID("IN-Service-Trigger", TYPE_UTF8_STRING, "VMP", VENDOR_HUAWEI),
    22739: VendorID("SSF-Charging-Case", TYPE_UNSIGNED_32, "VMP", VENDOR_HUAWEI),
    22740: VendorID("Global-Title-Subsystem", TYPE_OCTET_STRING, "VMP", VENDOR_HUAWEI),
    22741: VendorID("IN-Composite-CDR", TYPE_UNSIGNED_32, "VMP", VENDOR_HUAWEI),
    22743: VendorID("P-Cellular-Network-Info", TYPE_UTF8_STRING, "VMP", VENDOR_HUAWEI),
    22745: VendorID("SCP-Connection", TYPE_ENUMERATED, "VMP", VENDOR_HUAWEI),
    22752: VendorID("Secondary-Party-Address", TYPE_UTF8_STRING, "VMP", VENDOR_HUAWEI),
    22753: VendorID("Group-Id-Of-Other-Party", TYPE_UNSIGNED_32, "VMP", VENDOR_HUAWEI),
    22754: VendorID(
        "Private-Number-Of-Other-Party", TYPE_UTF8_STRING, "VMP", VENDOR_HUAWEI
    ),
}


def is_avp_flag_valid(flags_byte: int, parameter_flag: str | None = None) -> bool:
    """Validate AVP flags byte according to Diameter protocol specification

    Bit layout (8 bits):
    V M P 0 0 0 0 0
    | | | | | | | |
    0 1 2 3 4 5 6 7  (bit positions)

    Args:
        flags_byte: Single byte (0-255) containing the flags
        parameter_flag: String containing expected flags ('V', 'M', 'P')

    Returns:
        bool: True if flags match expected pattern, False otherwise

    Raises:
        ValueError: If flags_byte is not a valid byte value or reserved bits are not 0
    """
    if parameter_flag is None:  # No parameter flag means ACA message
        return True

    if not (0 <= flags_byte <= 255):
        raise ValueError(f"Flags byte must be 0-255, got: {flags_byte}")

    # Check reserved bits (bits 7-3 should be zero)
    if not (flags_byte & 0x1F) == 0:
        raise ValueError("Reserved bits 7-3 must be 0, got: {bin(flags_byte)[3:]}")

    flags_string = ""
    # Vendor flag
    if bool(flags_byte & 0x80):
        flags_string += "V"
    # Mandatory flag
    if bool(flags_byte & 0x40):
        flags_string += "M"
    # Protected flag
    if bool(flags_byte & 0x20):
        flags_string += "P"

    return flags_string == parameter_flag


class EricssonVolte:
    DIAMETER_HEADER_FORMAT = struct.Struct(">B3sB3sIII")  # Big-endian format
    HEADER_SIZE = 20  # Fixed 20-byte header
    NTP_EPOCH = datetime(1900, 1, 1)  # For timestamp conversion
    PREFIX_HEADER_LENGTH = 2

    def __init__(self, buffer_manager):
        self.buffer_manager = buffer_manager
        self._init_handler()
        self.index = 0

    def _init_handler(self) -> None:
        """Initialize the handler for parsing AVPs"""
        with self.buffer_manager.open() as file_buffer:
            self.binary_data = memoryview(file_buffer.read())
        self.length = len(self.binary_data)

    @staticmethod
    def parse_block(block: bytes) -> dict[str, int | str | bool]:
        parsed_blocks = []
        while block:
            avp, offset = EricssonVolte.parse_avp(block)
            block = block[offset:]
            parsed_blocks.append(avp)
        return {k: v for block in parsed_blocks for k, v in block.items()}

    def avps(self) -> Generator[dict[str, int | str | bool]]:
        """Parse all blocks in the binary data"""
        return (self.parse_block(block) for block in self.blocks())

    def blocks(self) -> Generator[bytes]:
        """Generator to yield sliced blocks from binary data to"""
        idx = 0
        length = self.length
        while idx < length:
            start_idx, stop_idx, error = self.slice_next_block(idx)
            if not error:
                yield self.binary_data[start_idx:stop_idx]
            idx = stop_idx

    def slice_next_block(self, index: int) -> Tuple[int, int, bool]:
        """Parse Diameter header
        The format string ">B3sB3sIII" defines how to interpret the 20-byte Diameter protocol header:
        Format Components:
        > - Big-endian byte order (network byte order)
        B - Unsigned char (1 byte) → Version
        3s - 3-byte string → Message Length
        B - Unsigned char (1 byte) → Command Flags
        3s - 3-byte string → Command Code
        I - Unsigned int (4 bytes) → Application-ID
        I - Unsigned int (4 bytes) → Hop-by-Hop Identifier
        I - Unsigned int (4 bytes) → End-to-End Identifier
        Total: 1 + 3 + 1 + 3 + 4 + 4 + 4 = 20 bytes
        """
        index += 2  # Skip first 2 bytes
        end_idx = index + EricssonVolte.HEADER_SIZE
        header = self.binary_data[index:end_idx]

        # Validate minimum length
        if len(header) < EricssonVolte.HEADER_SIZE:
            index += len(header)  # Skip this block
            return index, index, True

        # Unpack all header fields
        (version, msg_len_bytes, flag_int, cmd_bytes, app_id, hbh_id, e2e_id) = (
            EricssonVolte.DIAMETER_HEADER_FORMAT.unpack(
                header,
            )
        )

        # Convert 24-bit fields
        msg_length = int.from_bytes(msg_len_bytes)

        # Validate version (MUST be 1)
        if version != 1:
            raise ValueError(f"Invalid Diameter version: {version} (must be 1)")

        # flags = ""
        # if bool(flag_int & 0x80):
        #     flags += "R"  # Request flag
        # if bool(flag_int & 0x40):
        #     flags += "P"  # Proxiable flag
        # if bool(flag_int & 0x20):
        #     flags += "E"  # Error flag
        # if bool(flag_int & 0x10):
        #     flags += "T"  # Re-transmitted flag

        # Validate message type
        if cmd_bytes != b"\x00\x01\x0f":
            raise ValueError(
                f"Invalid Command-Code: {int.from_bytes(cmd_bytes)} (expected 271 for accounting)"
            )
        start_idx = index + EricssonVolte.HEADER_SIZE
        index = index + msg_length  # msg_length includes the header
        # Build header dictionary
        return start_idx, index, False

    @staticmethod
    def validate_block_structure(block: bytes) -> bool:
        """Pre-validate that block contains valid Diameter structure"""
        if len(block) < 8:
            return False

        # Quick sanity checks before expensive parsing
        potential_length = int.from_bytes(block[5:8], byteorder="big")
        return 8 <= potential_length <= len(block)

    @staticmethod
    def parse_avp(current_block: memoryview | bytes) -> Tuple:
        """Parse a single AVP from binary data"""
        i = 0
        header_size = 8
        while True:
            # Parse AVP header (8 bytes)
            if (offset := len(current_block[i:])) < 8:
                return {}, offset  # Not enough data for AVP header

            avp_code = int.from_bytes(current_block[i : i + 4], byteorder="big")
            if not (avp_def := AVP_DB.get(avp_code)):
                i += 1
                continue  # Slide window if AVP code is unknown
            flags = current_block[i + 4]
            avp_length = int.from_bytes(current_block[i + 5 : i + 8], byteorder="big")
            if len(current_block[i:]) < avp_length or avp_length < 8:
                i += 1
                continue  # Slide window if AVP length is invalid
            # vendor_id = None
            if flags & 0x80:  # Vendor flag set
                if avp_length < 12:
                    i += 1
                    continue  # Slide window if AVP length is less than 12 bytes
                # vendor_id = STRUCT_UNSIGNED_32.unpack(current_block[i + 8 : i + 12])[
                #     0
                # ]  # just for debug
                header_size = 12

            if (known_size := KNOWN_SIZES.get(avp_def.type)) is not None:
                if avp_length - header_size != known_size:
                    i += 1
                    continue  # Slide window if AVP length does not match known size
            break

        offset: int = i + avp_length

        if not is_avp_flag_valid(flags, avp_def.acr_flag):
            return {}, offset  # Invalid AVP flags, skip this AVP

        value_data: bytes = current_block[i + header_size : i + avp_length]  # type: ignore

        if (avp_type := avp_def.type) == TYPE_GROUPED:
            avps, offset = EricssonVolte.parse_grouped_avp(value_data)
            if not avps:
                return {}, offset
            # return EricssonCDRParser.flatten_avp(avp_def.avp, avps), offset
            return {avp_def.avp: avps}, offset
        else:
            return {
                avp_def.avp: EricssonVolte.parse_simple_value(value_data, avp_type),
            }, offset

    @staticmethod
    def flatten_avp(prefix: str, avp: dict | list) -> dict:
        flattened_avp = {}
        if isinstance(avp, dict):
            for key, value in avp.items():
                if not isinstance(value, (dict, list)):
                    if previous_value := flattened_avp.get(key):
                        value = f"{previous_value};{value}"  # Concatenate values
                    flattened_avp[key] = value
                if isinstance(value, dict):
                    flattened_avp.update(EricssonVolte.flatten_avp(key, value))
                elif isinstance(value, list):
                    for item in value:
                        flattened_avp.update(EricssonVolte.flatten_avp(key, item))
        elif isinstance(avp, list):
            for item in avp:
                flattened_avp.update(EricssonVolte.flatten_avp(prefix, item))
        return flattened_avp

    @staticmethod
    def parse_grouped_avp(binary_data: bytes | bytes) -> Tuple[list, int]:
        """Parse a grouped AVP (recursive)"""
        avps = []
        current_block = binary_data
        total_offset = 0
        while current_block:
            avp, offset = EricssonVolte.parse_avp(current_block)
            current_block = current_block[offset:]  # Move to next AVP
            if avp:
                avps.append(avp)
            total_offset += offset
        if len(avps) == 1:
            avps = avps[0]  # If only one AVP, return it directly
        return avps, total_offset

    @staticmethod
    def parse_simple_value(binary_view: bytes, avp_type: int) -> str | int:
        """
        Parse a simple AVP (Attribute-Value Pair) based on its specified type.

        This method handles decoding of various AVP data types, including:
            - Strings (UTF-8, Octet, Diameter Identity)
            - Timestamps
            - Integers and Enumerations
            - Network Addresses (IPv4/IPv6)
            - Unsigned 32/64-bit integers

        Args:
            binary_view (memoryview): Raw binary data to be parsed
            avp_type (int): The type of AVP to decode

        Returns:
                Decoded value in an appropriate Python type (str, int, etc.)
        """
        if avp_type in (TYPE_OCTET_STRING, TYPE_UTF8_STRING, TYPE_DIAMETER_IDENTITY):
            try:
                return binary_view.tobytes().decode("utf-8")  # type: ignore
            except UnicodeDecodeError:
                # If decoding fails, return string representation of raw bytes
                return binary_view.tobytes().hex()  # type: ignore
        elif avp_type == TYPE_TIME:
            seconds = STRUCT_UNSIGNED_32.unpack(binary_view)[0]
            return (EricssonVolte.NTP_EPOCH + timedelta(seconds=seconds)).strftime(
                "%Y-%m-%d %H:%M:%S"
            )  # Convert to human-readable format
        elif avp_type in (TYPE_ENUMERATED, TYPE_INTEGER_32):
            # Enumerated and Integer 32 are both 4-byte signed integers
            return STRUCT_SIGNED_32.unpack(binary_view)[0]
        elif avp_type == TYPE_ADDRESS:
            # Address format: 1 byte family + address bytes
            binary_data = binary_view.tobytes()  # type: ignore
            family = int.from_bytes(binary_data[:2])
            address_bytes = binary_data[2:]
            if family == 1:  # IPv4
                return socket.inet_ntoa(address_bytes)
            elif family == 2:  # IPv6
                return socket.inet_ntop(socket.AF_INET6, address_bytes)
            else:
                return address_bytes.decode("utf-8")  # Unknown family, return raw bytes
        elif avp_type == TYPE_UNSIGNED_32:
            return STRUCT_UNSIGNED_32.unpack(binary_view)[0]
        elif avp_type == TYPE_UNSIGNED_64:
            return STRUCT_UNSIGNED_64.unpack(binary_view)[0]
        else:
            return binary_view.tobytes().hex()  # type: ignore # Fallback for unknown types

    def process(self):
        return list(
            tqdm(self.avps(), desc="Parsing AVPs", unit=" block", leave=False)
        )  # Process all AVPs and return as a list

    @staticmethod
    def transform_func(df):
        return transform_ericsson_volte(df)
