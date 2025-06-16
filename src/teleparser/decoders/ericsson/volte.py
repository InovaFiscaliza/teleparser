import struct
from datetime import datetime, timedelta
from dataclasses import dataclass
from typing import Tuple
import socket
from fastcore.xtras import Path

# Vendor IDs
VENDOR_3GPP = 10415
VENDOR_ERICSSON = 193
# Type constants (as provided)
TYPE_OCTET_STRING = 0
TYPE_INTEGER_32 = 1
TYPE_UNSIGNED_32 = 2
TYPE_UTF8_STRING = 4
TYPE_GROUPED = 8
TYPE_TIME = 9
TYPE_ENUMERATED = 10
TYPE_DIAMETER_IDENTITY = 11
TYPE_ADDRESS = 12

counter = 0


@dataclass
class VendorID:
    """Data class to represent a Diameter AVP with vendor information"""

    avp: str
    avp_code: int
    type: int
    acr_flag: str | None = None
    vendor_id: int | None = None


MTAS = {
    1,
    23,
    55,
    85,
    259,
    263,
    264,
    268,
    283,
    284,
    293,
    296,
    338,
    420,
    443,
    444,
    450,
    459,
    460,
    461,
    480,
    485,
    650,
    701,
    701,
    824,
    826,
    827,
    828,
    829,
    830,
    831,
    832,
    834,
    835,
    839,
    840,
    841,
    842,
    844,
    845,
    861,
    862,
    863,
    864,
    874,
    876,
    878,
    882,
    1061,
    1127,
    1128,
    1129,
    1130,
    1131,
    1133,
    1141,
    1142,
    1153,
    1160,
    1206,
    1207,
    1250,
    1251,
    1256,
    1257,
    1262,
    1263,
    1264,
    1265,
    1266,
    1267,
    1302,
    1303,
    1307,
    1308,
    1314,
    1315,
    1330,
    1346,
    1357,
    1371,
    1372,
    1373,
    1380,
    1384,
    1388,
    1389,
    1390,
    1393,
    1394,
    1395,
    1395,
    1396,
    1396,
    1397,
    1397,
    1398,
    1406,
    1407,
    1433,
    1460,
    1463,
    1464,
    1465,
    1477,
    1478,
    1527,
    1531,
    1532,
    1533,
    1536,
    2023,
    2023,
    2024,
    2035,
    2036,
    2301,
    2302,
    2304,
    2320,
    2713,
    3401,
    3402,
}

SBG = {
    1,
    2,
    55,
    259,
    263,
    264,
    283,
    293,
    296,
    336,
    337,
    363,
    364,
    365,
    366,
    444,
    450,
    480,
    485,
    518,
    650,
    824,
    826,
    827,
    828,
    829,
    830,
    831,
    832,
    834,
    835,
    839,
    840,
    841,
    842,
    844,
    845,
    847,
    848,
    861,
    862,
    864,
    882,
    1087,
    1088,
    1089,
    1090,
    1091,
    1092,
    1093,
    1094,
    1095,
    1096,
    1178,
    1182,
    1252,
    1253,
    1263,
    1265,
    1266,
    1267,
    1298,
    1305,
    1436,
    2301,
    2302,
    2713,
    2819,
    3402,
}

CSCF = {
    1,
    18,
    55,
    259,
    263,
    264,
    283,
    286,
    293,
    296,
    333,
    336,
    337,
    338,
    340,
    444,
    450,
    461,
    480,
    485,
    824,
    827,
    828,
    829,
    830,
    831,
    832,
    834,
    835,
    839,
    840,
    841,
    842,
    844,
    845,
    848,
    861,
    862,
    864,
    1160,
    1250,
    1261,
    1263,
    1265,
    1266,
    1267,
    1305,
    2023,
    2024,
    2301,
    2302,
    2711,
    2712,
    2713,
    3402,
}
AVP_DB = {
    1: VendorID("User-Name", 1, TYPE_UTF8_STRING),
    2: VendorID("3GPP-Charging-Id", 2, TYPE_OCTET_STRING, "V"),
    18: VendorID("3GPP-SGSN-MCC-MNC", 18, TYPE_UTF8_STRING, "VM", VENDOR_3GPP),
    23: VendorID("3GPP-MS-TimeZone", 23, TYPE_OCTET_STRING, "V", VENDOR_3GPP),
    55: VendorID("Event-Timestamp", 55, TYPE_TIME, "M"),
    85: VendorID("Acct-Interim-Interval", 85, TYPE_UNSIGNED_32, "M"),
    259: VendorID("Acct-Application-Id", 259, TYPE_UNSIGNED_32, "M"),
    263: VendorID("Session-Id", 263, TYPE_UTF8_STRING, "M"),
    264: VendorID("Origin-Host", 264, TYPE_DIAMETER_IDENTITY),
    266: VendorID("Vendor-Id", 266, TYPE_UNSIGNED_32),
    268: VendorID("Result-Code", 268, TYPE_UNSIGNED_32, "M"),
    283: VendorID("Destination-Realm", 283, TYPE_DIAMETER_IDENTITY),
    284: VendorID(
        "IMS-Service-Identification", 284, TYPE_UTF8_STRING, "V", VENDOR_ERICSSON
    ),
    285: VendorID(
        "Ericsson-Service-Information", 285, TYPE_GROUPED, "V", VENDOR_ERICSSON
    ),
    286: VendorID(
        "Called-Party-Original-Address", 286, TYPE_UTF8_STRING, "VM", VENDOR_ERICSSON
    ),
    293: VendorID("Destination-Host", 293, TYPE_DIAMETER_IDENTITY, "M"),
    296: VendorID("Origin-Realm", 296, TYPE_DIAMETER_IDENTITY),
    297: VendorID("Experimental-Result", 297, TYPE_GROUPED),
    298: VendorID("Experimental-Result-Code", 298, TYPE_UNSIGNED_32),
    338: VendorID("SIP-Ringing-Timestamp", 338, TYPE_TIME, "V", VENDOR_ERICSSON),
    420: VendorID("CC-Time", 420, TYPE_UNSIGNED_32, "M"),
    443: VendorID("Subscription-Id", 443, TYPE_GROUPED, "M"),
    444: VendorID("Subscription-Id-Data", 444, TYPE_UTF8_STRING, "M"),
    450: VendorID("Subscription-Id-Type", 450, TYPE_ENUMERATED, "M"),
    458: VendorID("User-Equipment-Info", 458, TYPE_GROUPED, "M"),
    459: VendorID("User-Equipment-Info-Type", 459, TYPE_ENUMERATED, "M"),
    460: VendorID("User-Equipment-Info-Value", 460, TYPE_OCTET_STRING, "M"),
    461: VendorID("Service-Context-Id", 461, TYPE_UTF8_STRING, "M"),
    480: VendorID("Accounting-Record-Type", 480, TYPE_ENUMERATED, "M"),
    485: VendorID("Accounting-Record-Number", 485, TYPE_UNSIGNED_32, "M"),
    650: VendorID("Session-Priority", 650, TYPE_ENUMERATED, "V", VENDOR_3GPP),
    701: VendorID("MSISDN", 701, TYPE_OCTET_STRING, "VM", VENDOR_3GPP),
    823: VendorID("Event-Type", 823, TYPE_GROUPED, "VM", VENDOR_3GPP),
    824: VendorID("SIP-Method", 824, TYPE_UTF8_STRING, "VM", VENDOR_3GPP),
    826: VendorID("Content-Type", 826, TYPE_UTF8_STRING, "VM", VENDOR_3GPP),
    827: VendorID("Content-Length", 827, TYPE_UNSIGNED_32, "VM", VENDOR_3GPP),
    828: VendorID("Content-Disposition", 828, TYPE_UTF8_STRING, "VM", VENDOR_3GPP),
    829: VendorID("Role-of-Node", 829, TYPE_ENUMERATED, "VM", VENDOR_3GPP),
    830: VendorID("User-Session-Id", 830, TYPE_UTF8_STRING, "VM", VENDOR_3GPP),
    831: VendorID("Calling-Party-Address", 831, TYPE_UTF8_STRING, "VM", VENDOR_3GPP),
    832: VendorID("Called-Party-Address", 832, TYPE_UTF8_STRING, "VM", VENDOR_3GPP),
    833: VendorID("Time-Stamps", 833, TYPE_GROUPED, "VM", VENDOR_3GPP),
    834: VendorID("SIP-Request-Timestamp", 834, TYPE_TIME, "VM", VENDOR_3GPP),
    835: VendorID("SIP-Response-Timestamp", 835, TYPE_TIME, "VM", VENDOR_3GPP),
    838: VendorID("Inter-Operator-Identifier", 838, TYPE_GROUPED, "VM", VENDOR_3GPP),
    839: VendorID("Originating-IOI", 839, TYPE_UTF8_STRING, "VM", VENDOR_3GPP),
    840: VendorID("Terminating-IOI", 840, TYPE_UTF8_STRING, "VM", VENDOR_3GPP),
    841: VendorID("IMS-Charging-Identifier", 841, TYPE_UTF8_STRING, "VM", VENDOR_3GPP),
    842: VendorID("SDP-Session-Description", 842, TYPE_UTF8_STRING, "VM", VENDOR_3GPP),
    843: VendorID("SDP-Media-Component", 843, TYPE_GROUPED, "VM", VENDOR_3GPP),
    844: VendorID("SDP-Media-Name", 844, TYPE_UTF8_STRING, "VM", VENDOR_3GPP),
    845: VendorID("SDP-Media-Description", 845, TYPE_UTF8_STRING, "VM", VENDOR_3GPP),
    861: VendorID("Cause-Code", 861, TYPE_INTEGER_32, "VM", VENDOR_3GPP),
    862: VendorID("Node-Functionality", 862, TYPE_ENUMERATED, "VM", VENDOR_3GPP),
    863: VendorID("Service-Specific-Data", 863, TYPE_UTF8_STRING, "VM", VENDOR_3GPP),
    864: VendorID("Originator", 864, TYPE_ENUMERATED, "VM", VENDOR_3GPP),
    873: VendorID("Service-Information", 873, TYPE_GROUPED, "VM", VENDOR_3GPP),
    874: VendorID("PS-Information", 874, TYPE_GROUPED, "VM", VENDOR_3GPP),
    876: VendorID("IMS-Information", 876, TYPE_GROUPED, "VM", VENDOR_3GPP),
    878: VendorID("LCS-Information", 878, TYPE_GROUPED, "VM", VENDOR_3GPP),
    882: VendorID("Media-Initiator-Flag", 882, TYPE_ENUMERATED, "VM", VENDOR_3GPP),
    889: VendorID("Message-Body", 889, TYPE_GROUPED, "VM", VENDOR_3GPP),
    1061: VendorID(
        "MMT-Information", 1061, TYPE_GROUPED, "V", 193
    ),  # Ericsson vendor ID is 193
    1127: VendorID("Conference-Id", 1127, TYPE_UTF8_STRING, "V", VENDOR_ERICSSON),
    1128: VendorID("Related-ICID", 1128, TYPE_UTF8_STRING, "V", VENDOR_ERICSSON),
    1129: VendorID(
        "Supplementary-Service-Information", 1129, TYPE_GROUPED, "V", VENDOR_ERICSSON
    ),
    1130: VendorID(
        "Supplementary-Service-Identity", 1130, TYPE_ENUMERATED, "V", VENDOR_ERICSSON
    ),
    1131: VendorID(
        "Supplementary-Service-Action", 1131, TYPE_ENUMERATED, "V", VENDOR_ERICSSON
    ),
    1133: VendorID(
        "Redirecting-Party-Address", 1133, TYPE_UTF8_STRING, "V", VENDOR_ERICSSON
    ),
    1141: VendorID(
        "Calling-Party-Address-Presentation-Status", 1141, TYPE_ENUMERATED, "V", 193
    ),
    1142: VendorID(
        "Called-Asserted-Identity-Presentation-Status", 1142, TYPE_ENUMERATED, "V", 193
    ),
    1153: VendorID("From-Header", 1153, TYPE_UTF8_STRING, "V", VENDOR_ERICSSON),
    1160: VendorID(
        "Dial-Around-Indicator", 1160, TYPE_UTF8_STRING, "V", VENDOR_ERICSSON
    ),
    1206: VendorID(
        "GSM-Call-Reference-Number", 1206, TYPE_UTF8_STRING, "V", VENDOR_ERICSSON
    ),
    1207: VendorID("MSC-Address", 1207, TYPE_UTF8_STRING, "V", VENDOR_ERICSSON),
    1249: VendorID("Service-Specific-Info", 1249, TYPE_GROUPED, "VM", VENDOR_3GPP),
    1250: VendorID(
        "Called-Asserted-Identity", 1250, TYPE_UTF8_STRING, "VM", VENDOR_3GPP
    ),
    1251: VendorID(
        "Requested-Party-Address", 1251, TYPE_UTF8_STRING, "VM", VENDOR_3GPP
    ),
    1256: VendorID(
        "SIP-Ringing-Timestamp-Fraction", 1256, TYPE_UNSIGNED_32, "V", VENDOR_ERICSSON
    ),
    1257: VendorID("Service-Specific-Type", 1257, TYPE_UNSIGNED_32, "VM", VENDOR_3GPP),
    1262: VendorID(
        "From-Header-Presentation-Status", 1262, TYPE_ENUMERATED, "V", VENDOR_ERICSSON
    ),
    1263: VendorID(
        "Access-Network-Information", 1263, TYPE_OCTET_STRING, "VM", VENDOR_3GPP
    ),
    1264: VendorID("Transaction-Info", 1264, TYPE_GROUPED, "V", VENDOR_ERICSSON),
    1265: VendorID("Transaction-Type", 1265, TYPE_ENUMERATED, "V", VENDOR_ERICSSON),
    1266: VendorID(
        "Transaction-Data-Name", 1266, TYPE_UTF8_STRING, "V", VENDOR_ERICSSON
    ),
    1267: VendorID(
        "Transaction-Data-Value", 1267, TYPE_UTF8_STRING, "V", VENDOR_ERICSSON
    ),
    1302: VendorID("Routing-Call-Type", 1302, TYPE_UTF8_STRING, "V", VENDOR_ERICSSON),
    1303: VendorID("Analyzed-Call-Type", 1303, TYPE_UTF8_STRING, "V", VENDOR_ERICSSON),
    1307: VendorID("Service-Number-Type", 1307, TYPE_ENUMERATED, "V", VENDOR_ERICSSON),
    1308: VendorID(
        "Common-Policy-Rule-Identity", 1308, TYPE_UTF8_STRING, "V", VENDOR_ERICSSON
    ),
    1314: VendorID("SCC-Service-Identity", 1314, TYPE_ENUMERATED, "V", VENDOR_ERICSSON),
    1315: VendorID("SCC-TADS-Decision", 1315, TYPE_ENUMERATED, "V", VENDOR_ERICSSON),
    1330: VendorID("Served-User", 1330, TYPE_UTF8_STRING, "V", VENDOR_ERICSSON),
    1346: VendorID("XCON-Id", 1346, TYPE_UTF8_STRING, "V", VENDOR_ERICSSON),
    1357: VendorID("Party-To-Charge", 1357, TYPE_UNSIGNED_32, "V", VENDOR_ERICSSON),
    1371: VendorID(
        "Service-Suppression-Info", 1371, TYPE_GROUPED, "V", VENDOR_ERICSSON
    ),
    1372: VendorID(
        "Matched-Regular-Expression", 1372, TYPE_UTF8_STRING, "V", VENDOR_ERICSSON
    ),
    1373: VendorID(
        "Services-To-Suppress", 1373, TYPE_UTF8_STRING, "V", VENDOR_ERICSSON
    ),
    1380: VendorID("Tenant", 1380, TYPE_UTF8_STRING, "V", VENDOR_ERICSSON),
    1384: VendorID("CCMP-User-Info", 1384, TYPE_UTF8_STRING, "V", VENDOR_ERICSSON),
    1388: VendorID("UHTZ-Offset", 1388, TYPE_UTF8_STRING, "V", VENDOR_ERICSSON),
    1389: VendorID(
        "Participants-Involved", 1389, TYPE_UTF8_STRING, "V", VENDOR_ERICSSON
    ),
    1390: VendorID("Participants-List", 1390, TYPE_UTF8_STRING, "V", VENDOR_ERICSSON),
    1393: VendorID(
        "Forward-TTC-Charging-Headers", 1393, TYPE_GROUPED, "V", VENDOR_ERICSSON
    ),
    1394: VendorID(
        "Backward-TTC-Charging-Headers", 1394, TYPE_GROUPED, "V", VENDOR_ERICSSON
    ),
    1395: VendorID("Charging-Area", 1395, TYPE_UTF8_STRING, "V", VENDOR_ERICSSON),
    1396: VendorID(
        "Carrier-Information", 1396, TYPE_OCTET_STRING, "V", VENDOR_ERICSSON
    ),
    1397: VendorID(
        "Additional-User-Category", 1397, TYPE_OCTET_STRING, "V", VENDOR_ERICSSON
    ),
    1398: VendorID(
        "Flexible-Charging-Info", 1398, TYPE_OCTET_STRING, "V", VENDOR_ERICSSON
    ),
    1406: VendorID(
        "Forward-TTC-Charging-Parameters", 1406, TYPE_UTF8_STRING, "V", VENDOR_ERICSSON
    ),
    1407: VendorID(
        "Backward-TTC-Charging-Parameters", 1407, TYPE_UTF8_STRING, "V", 193
    ),
    1433: VendorID("AS-Type", 1433, TYPE_ENUMERATED, "V", VENDOR_ERICSSON),
    1460: VendorID(
        "Transaction-SIP-Message", 1460, TYPE_UTF8_STRING, "V", VENDOR_ERICSSON
    ),
    1463: VendorID("Subscriber-Type", 1463, TYPE_ENUMERATED, "V", VENDOR_ERICSSON),
    1464: VendorID("UC-Mobility-Call-Leg", 1464, TYPE_ENUMERATED, "V", VENDOR_ERICSSON),
    1465: VendorID("Interim-Reason", 1465, TYPE_ENUMERATED, "V", VENDOR_ERICSSON),
    1477: VendorID("Ro-Status", 1477, TYPE_ENUMERATED, "V", VENDOR_ERICSSON),
    1478: VendorID("Ro-Information", 1478, TYPE_GROUPED, "V", VENDOR_ERICSSON),
    1527: VendorID(
        "Analyzed-B-Number-Type", 1527, TYPE_UTF8_STRING, "V", VENDOR_ERICSSON
    ),
    1531: VendorID("Caller-Category", 1531, TYPE_UNSIGNED_32, "V", VENDOR_ERICSSON),
    1532: VendorID("Caller-Sub-Category", 1532, TYPE_UNSIGNED_32, "V", VENDOR_ERICSSON),
    1533: VendorID("Caller-Treatment", 1533, TYPE_ENUMERATED, "V", VENDOR_ERICSSON),
    1536: VendorID(
        "Caller-Category-Presentation", 1536, TYPE_UTF8_STRING, "V", VENDOR_ERICSSON
    ),
    2023: VendorID(
        "Carrier-Select-Routing-Information", 2023, TYPE_UTF8_STRING, "VM", 10415
    ),
    2024: VendorID(
        "Number-Portability-Routing-Information", 2024, TYPE_UTF8_STRING, "VM", 10415
    ),
    2030: VendorID("MMTel-Information", 2030, TYPE_GROUPED, "VM", VENDOR_3GPP),
    2035: VendorID(
        "Associated-Party-Address", 2035, TYPE_UTF8_STRING, "VM", VENDOR_3GPP
    ),
    2036: VendorID("SDP-Type", 2036, TYPE_ENUMERATED, "VM", VENDOR_3GPP),
    2048: VendorID("Supplementary-Service", 2048, TYPE_GROUPED, "VM", VENDOR_3GPP),
    2301: VendorID(
        "SIP-Request-Timestamp-Fraction", 2301, TYPE_UNSIGNED_32, "VM", 10415
    ),
    2302: VendorID(
        "SIP-Response-Timestamp-Fraction", 2302, TYPE_UNSIGNED_32, "VM", 10415
    ),
    2304: VendorID("CUG-Information", 2304, TYPE_OCTET_STRING, "VM", VENDOR_3GPP),
    2320: VendorID("Outgoing-Session-Id", 2320, TYPE_UTF8_STRING, "VM", VENDOR_3GPP),
    2713: VendorID(
        "IMS-Visited-Network-Identifier", 2713, TYPE_UTF8_STRING, "VM", 10415
    ),
    3401: VendorID("Reason-Header", 3401, TYPE_UTF8_STRING, "VM", VENDOR_3GPP),
    3402: VendorID("Instance-id", 3402, TYPE_UTF8_STRING, "VM", VENDOR_3GPP),
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

    # Extract flag bits
    v_flag = bool(flags_byte & 0x80)  # Vendor flag
    m_flag = bool(flags_byte & 0x40)  # Mandatory flag
    p_flag = bool(flags_byte & 0x20)  # Protected flag

    # Check reserved bits (bits 7-3 should be zero)
    if not (flags_byte & 0x1F) == 0:
        raise ValueError("Reserved bits 7-3 must be 0, got: {bin(flags_byte)[3:]}")
    flags_string = "".join(
        ["V" if v_flag else "", "M" if m_flag else "", "P" if p_flag else ""]
    )
    return flags_string == parameter_flag


class EricssonCDRParser:
    DIAMETER_HEADER_FORMAT = ">B3sB3sIII"  # Big-endian format
    HEADER_SIZE = 20  # Fixed 20-byte header
    NTP_EPOCH = datetime(1900, 1, 1)  # For timestamp conversion
    PREFIX_HEADER_LENGTH = 2

    def __init__(self, binary_data: bytes):
        self.binary_data = binary_data
        self.index = 0
        self.avp_map = {k: v for k, v in AVP_DB.items() if k in MTAS.union(SBG)}
        self.valid_avps = 0
        self.invalid_flags = 0  # Track invalid AVP flags
        self.invalid_size = 0  # Track invalid AVPs

    def parse_next_block(self) -> dict | None:
        """Parse Diameter header (version 1 only)
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
        self.index += 2  # Skip first 2 bytes
        i = self.index
        j = i + self.HEADER_SIZE
        header = self.binary_data[i:j]

        # Validate minimum length
        if len(header) < self.HEADER_SIZE:
            self.index += len(header)  # Skip this block
            return None

        # Unpack all header fields
        (version, msg_len_bytes, flags, cmd_bytes, app_id, hbh_id, e2e_id) = (
            struct.unpack(
                self.DIAMETER_HEADER_FORMAT,
                header,
            )
        )

        # Convert 24-bit fields
        msg_length = int.from_bytes(msg_len_bytes)

        # Validate version (MUST be 1)
        if version != 1:
            raise ValueError(f"Invalid Diameter version: {version} (must be 1)")

        # Parse command flags
        flag_bits = {
            "R": bool(flags & 0x80),  # Request flag
            "P": bool(flags & 0x40),  # Proxiable flag
            "E": bool(flags & 0x20),  # Error flag
            "T": bool(flags & 0x10),  # Re-transmitted flag
        }

        # Validate message type
        if cmd_bytes != b"\x00\x01\x0f":
            raise ValueError(
                f"Invalid Command-Code: {int.from_bytes(cmd_bytes)} (expected 271 for accounting)"
            )

        end_idx = self.index + msg_length  # msg_length includes the header
        self.index += self.HEADER_SIZE
        avps: dict[str, int | str] = {}
        current_block = self.binary_data[self.index : end_idx]
        while current_block:
            avp, offset = self.parse_avp(current_block)
            current_block = current_block[offset:]  # Move to next AVP
            if avp is not None:
                avps.update(avp)
            self.index += offset  # Move index forward by the size of the parsed AVP
        # Build header dictionary
        return {
            "flags": "".join(k for k, v in flag_bits.items() if v),
            "hop_by_hop_id": hbh_id,
            "end_to_end_id": e2e_id,
            **avps,
        }

    def parse_avp(self, current_block) -> Tuple:
        """Parse a single AVP from binary data"""

        i = 0

        while True:
            # Parse AVP header (8 bytes)
            if (offset := len(current_block[i:])) < 8:
                self.invalid_size += 1
                return None, offset  # Not enough data for AVP header

            avp_code = int.from_bytes(current_block[i : i + 4], byteorder="big")
            if not (avp_def := self.avp_map.get(avp_code)):
                if avp_code != 0:
                    breakpoint()
                i += 1
                continue  # Skip unknown AVPs
            flags = current_block[i + 4]
            avp_length = int.from_bytes(current_block[i + 5 : i + 8], byteorder="big")
            if len(current_block[i:]) < avp_length or avp_length < 8:
                i += 1
                continue  # Skip unknown AVPs
            break

        # Extract vendor ID if present
        header_size = 8
        if flags & 0x80:  # Vendor flag set
            if avp_length < 12:
                raise ValueError("AVP with vendor flag requires at least 12 bytes")
            # vendor_id = struct.unpack(">I", binary_data[i + 8 : i + 12])[0] #just for debug
            header_size = 12

        offset: int = i + avp_length

        if not is_avp_flag_valid(flags, avp_def.acr_flag):
            self.invalid_flags += 1
            return None, offset  # Invalid AVP flags, skip this AVP

        value_data = current_block[i + header_size : i + avp_length]

        if (avp_type := avp_def.type) == TYPE_GROUPED:
            return self.parse_grouped_avp(value_data)
        self.valid_avps += 1
        return {
            avp_def.avp: self.parse_simple_value(value_data, avp_type),
            "start_idx": i,
        }, offset

    def parse_grouped_avp(self, binary_data):
        """Parse a grouped AVP (recursive)"""
        avps = {}
        current_block = binary_data
        total_offset = 0
        while current_block:
            avp, offset = self.parse_avp(current_block)
            current_block = current_block[offset:]  # Move to next AVP
            if avp is not None:
                avps.update(avp)
            total_offset += offset
        return avps, total_offset

    def parse_simple_value(self, binary_view, avp_type):
        """Parse simple AVP types"""
        binary_data = binary_view.tobytes()
        if avp_type in (TYPE_OCTET_STRING, TYPE_UTF8_STRING, TYPE_DIAMETER_IDENTITY):
            try:
                return binary_data.decode("utf-8")
            except UnicodeDecodeError:
                # If decoding fails, return string representation of raw bytes
                return binary_data.hex()
        elif avp_type == TYPE_TIME:
            seconds = struct.unpack(">I", binary_data)[0]
            return (self.NTP_EPOCH + timedelta(seconds=seconds)).strftime(
                "%Y-%m-%d %H:%M:%S"
            )  # Convert to human-readable format
        elif avp_type in (TYPE_ENUMERATED, TYPE_INTEGER_32):
            # Enumerated and Integer 32 are both 4-byte signed integers
            return struct.unpack(">i", binary_data)[0]
        elif avp_type == TYPE_ADDRESS:
            # Address format: 1 byte family + address bytes
            family = binary_data[0]
            address_bytes = binary_data[1:]
            if family == 1:  # IPv4
                return socket.inet_ntoa(address_bytes)
            elif family == 2:  # IPv6
                return socket.inet_ntop(socket.AF_INET6, address_bytes)
            else:
                return address_bytes
        elif avp_type == TYPE_UNSIGNED_32:
            return struct.unpack(">I", binary_data)[0]

        else:
            return binary_data.hex()  # Fallback for unknown types


def run():
    import gzip
    import pandas as pd
    from rich.progress import Progress

    files = Path("/home/rsilva/volte_claro/").ls().filter(lambda f: f.suffix == ".gz")
    file = sorted(files, key=lambda f: f.stat().st_size)[0]

    # Read CDR file
    with gzip.open(file, "rb") as f:
        binary_data = memoryview(f.read())
    blocks = []
    # Parse CDR
    parser = EricssonCDRParser(binary_data)
    with Progress(transient=True) as progress:
        total = len(binary_data)
        task = progress.add_task("[red]Reading Headers...", total=total)
        while parser.index < total:
            if (block := parser.parse_next_block()) is not None:
                blocks.append(block)
            progress.update(
                task,
                completed=parser.index,
                total=total,
            )

    # json.dump(blocks, (Path(__file__).parent / f'{file.stem}.json').open("w"), ensure_ascii=False, indent=4)
    # pd.DataFrame(blocks, dtype="category").set_index(["hop_by_hop_id", "end_to_end_id"]).to_parquet(
    #     file.with_suffix(".parquet.gzip"),
    #     compression="gzip",
    # )
    pd.DataFrame(blocks, dtype="category").set_index(
        ["hop_by_hop_id", "end_to_end_id"]
    ).to_csv(
        Path(__file__).parent / file.with_suffix(".csv").name,
    )

    print(f"Blocos com sucesso: {parser.valid_avps}")
    print(f"Blocos com flag inválido: {parser.invalid_flags}")
    print(f"Blocos com tamanho inválido: {parser.invalid_size}")


if __name__ == "__main__":
    import os
    import typer

    # from fastcore.parallel import parallel
    # files = Path("/home/rsilva/volte_claro/").ls().filter(lambda f: f.suffix == ".gz")
    # file = sorted(
    #     files, key=lambda f: f.stat().st_size
    # )[1]
    # parallel(run, files, n_workers=os.cpu_count()//2, progress=True)
    typer.run(run)

    # parsed_cdr = parser.parse_message(binary_data)

    # # Print results
    # print(f"Session ID: {parsed_cdr['header']['session_id']}")
    # print(f"Record Type: {parsed_cdr['header']['record_type']}")
    # print(f"Variant: {parsed_cdr['variant']}")

    # for avp in parsed_cdr["avps"]:
    #     if avp["name"] == "IMS-Charging-Identifier":
    #         print(f"ICID: {avp['value']}")
    #     elif avp["name"] == "Calling-Party-Address":
    #         print(f"Caller: {avp['value']}")
