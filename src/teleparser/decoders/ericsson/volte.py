import struct
from collections import namedtuple
from datetime import datetime, timedelta
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

VendorID = namedtuple(
    "VendorID",
    ["avp", "avp_code", "type", "acr_flag", "vendor_id"],
    defaults=(None, None),
)

AVP_DB = {
    1: VendorID("User-Name", 1, TYPE_UTF8_STRING),
    23: VendorID("3GPP-MS-TimeZone", 23, TYPE_OCTET_STRING, "V", VENDOR_3GPP),
    55: VendorID("Event-Timestamp", 55, TYPE_TIME, "M"),
    85: VendorID("Acct-Interim-Interval", 85, TYPE_UNSIGNED_32, "M"),
    259: VendorID("Acct-Application-Id", 259, TYPE_UNSIGNED_32, "M"),
    263: VendorID("Session-Id", 263, TYPE_UTF8_STRING, "M"),
    264: VendorID("Origin-Host", 264, TYPE_DIAMETER_IDENTITY),
    266: VendorID("Vendor-Id", 266, TYPE_UNSIGNED_32),
    268: VendorID("Result-Code", 268, TYPE_UNSIGNED_32, "M"),
    283: VendorID("Destination-Realm", 283, TYPE_DIAMETER_IDENTITY),
    293: VendorID("Destination-Host", 293, TYPE_DIAMETER_IDENTITY, "M"),
    296: VendorID("Origin-Realm", 296, TYPE_DIAMETER_IDENTITY),
    297: VendorID("Experimental-Result", 297, TYPE_GROUPED),
    298: VendorID("Experimental-Result-Code", 298, TYPE_UNSIGNED_32),
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
    285: VendorID(
        "Ericsson-Service-Information", 285, TYPE_GROUPED, "V", VENDOR_ERICSSON
    ),
    284: VendorID(
        "IMS-Service-Identification", 284, TYPE_UTF8_STRING, "V", VENDOR_ERICSSON
    ),
    338: VendorID("SIP-Ringing-Timestamp", 338, TYPE_TIME, "V", VENDOR_ERICSSON),
    3401: VendorID("Reason-Header", 3401, TYPE_UTF8_STRING, "VM", VENDOR_3GPP),
    3402: VendorID("Instance-id", 3402, TYPE_UTF8_STRING, "VM", VENDOR_3GPP),
    873: VendorID("Service-Information", 873, TYPE_GROUPED, "VM", VENDOR_3GPP),
    874: VendorID("PS-Information", 874, TYPE_GROUPED, "VM", VENDOR_3GPP),
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


class EricssonAVPDatabase:
    def __init__(self):
        self.avp_db = {}
        self._build_avp_database()

    def _build_avp_database(self):
        def add_avp(code, vendor, name, avp_type, flags=None, variant=None):
            """Helper function to add AVP definitions
            Flags are only applicable to ACR messages, None indicates ACA messages
            """
            key = (code, vendor)
            self.avp_db[key] = {
                "name": name,
                "type": avp_type,
                "flags": flags,
                "variant": variant,
            }

        # Common AVPs (both variants)
        add_avp(1, self.VENDOR_DIAMETER, "User-Name", self.TYPE_UTF8_STRING)
        add_avp(263, self.VENDOR_DIAMETER, "Session-Id", self.TYPE_UTF8_STRING, "M")
        add_avp(264, self.VENDOR_DIAMETER, "Origin-Host", self.TYPE_DIAMETER_IDENTITY)
        add_avp(296, self.VENDOR_DIAMETER, "Origin-Realm", self.TYPE_DIAMETER_IDENTITY)
        # ... (add all common AVPs from Tables 3/4)

        # Variant-1 specific AVPs (Table 3)
        add_avp(
            285,
            self.VENDOR_ERICSSON,
            "Ericsson-Service-Information",
            self.TYPE_GROUPED,
            1,
        )
        add_avp(1264, self.VENDOR_ERICSSON, "Transaction-Info", self.TYPE_GROUPED, 1)
        # ... (add all Variant-1 specific AVPs)

        # Variant-2 specific AVPs (Table 4)
        add_avp(876, self.VENDOR_3GPP, "IMS-Information", self.TYPE_GROUPED, 2)
        add_avp(873, self.VENDOR_3GPP, "Service-Information", self.TYPE_GROUPED, 2)
        # ... (add all Variant-2 specific AVPs)

    def get_avp_definition(self, code, vendor_id):
        return self.avp_db.get((code, vendor_id))


class EricssonCDRParser:
    DIAMETER_HEADER_FORMAT = ">B3sB3sIII"  # Big-endian format
    HEADER_SIZE = 20  # Fixed 20-byte header
    NTP_EPOCH = datetime(1900, 1, 1)  # For timestamp conversion
    PREFIX_HEADER_LENGTH = 2

    def __init__(self, binary_data: bytes):
        self.avp_db = EricssonAVPDatabase()
        self.binary_data = binary_data
        self.index = 0

    def parse_header(self, index: int) -> dict | None:
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
        self.index = index + 2  # Skip first 2 bytes
        i = self.index
        j = i + self.HEADER_SIZE
        if not (header := self.binary_data[i:j]):
            return None

        # Validate minimum length
        if len(header) < self.HEADER_SIZE:
            raise ValueError(
                f"Header requires {self.HEADER_SIZE} bytes, got {len(header)}"
            )

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

        # end_idx = self.index + msg_length  # msg_length includes the header
        # self.index += self.HEADER_SIZE
        # code, vendor_id, name, value = [], [], [], []
        # while self.index < end_idx:
        #     if (avp := self.parse_avp(self.binary_data[self.index : end_idx])) is None:
        #         self.index = end_idx  # Reject message
        #         return None
        #     code.append(avp[0])
        #     vendor_id.append(avp[1])
        #     name.append(avp[2])
        #     value.append(avp[3])

        # Build header dictionary
        return {
            "length": msg_length,
            "flags": "".join(k for k, v in flag_bits.items() if v),
            "application_id": app_id,
            "hop_by_hop_id": hbh_id,
            "end_to_end_id": e2e_id,
            "message_type": "ACR" if flag_bits["R"] else "ACA",
            # "code": code,
            # "vendor_id": vendor_id,
            # "name": name,
            # "value": value,
        }

    def parse_avp(self, binary_data) -> Tuple | None:
        """Parse a single AVP from binary data"""
        if len(binary_data) < 8:
            raise ValueError("Insufficient data for AVP header")

        i = 0
        while (avp_code := int.from_bytes(binary_data[i : i + 4])) == 0:
            i += 1

        # Parse the rest of AVP header (8 bytes)
        flags = binary_data[i + 4]
        avp_length = int.from_bytes(binary_data[i + 5 : i + 8])

        # Check if we have enough data
        if len(binary_data) < avp_length:
            print(
                f"AVP length {avp_length} differs from available data {len(binary_data)}"
            )  # TODO: log this
            return None

        self.index += i + avp_length

        # Extract vendor ID if present
        vendor_id = EricssonAVPDatabase.VENDOR_DIAMETER
        header_size = 8
        if flags & 0x80:  # Vendor flag set
            if avp_length < 12:
                raise ValueError("AVP with vendor flag requires at least 12 bytes")
            vendor_id = struct.unpack(">I", binary_data[i + 8 : i + 12])[0]
            header_size = 12

        # Get AVP definition
        avp_def = self.avp_db.get_avp_definition(avp_code, vendor_id)

        # Handle unknown AVP
        if not avp_def:
            return (
                avp_code,
                vendor_id,
                f"Unknown_{avp_code}",
                binary_data[i + header_size : i + avp_length],
            )

        assert is_avp_flag_valid(flags, avp_def["flags"]), (
            f"Invalid AVP flags: {bin(flags)}"
        )

        # Parse value based on type
        value_data = binary_data[i + header_size : i + avp_length]
        avp_type = avp_def["type"]

        if avp_type == EricssonAVPDatabase.TYPE_GROUPED:
            value = self.parse_grouped_avp(value_data, avp_def["name"])
        else:
            value = self.parse_simple_value(value_data, avp_type)

        return (
            avp_code,
            vendor_id,
            avp_def["name"],
            value,
        )

    def parse_grouped_avp(self, binary_data, grouped_name):
        """Parse a grouped AVP (recursive)"""
        avps = []
        data = binary_data

        # Handle variant-specific grouping rules
        if grouped_name == "Ericsson-Service-Information":
            # Variant-1 specific structure
            while data:
                avp, data = self.parse_avp(data)
                avps.append(avp)

        elif grouped_name == "IMS-Information":
            # Variant-2 specific structure
            while data:
                avp, data = self.parse_avp(data)
                # Special handling for Event-Type subgroup
                if avp["name"] == "Event-Type":
                    avp["value"] = self.parse_grouped_avp(avp["value"], "Event-Type")
                avps.append(avp)

        else:
            # Default grouping behavior
            while data:
                avp, data = self.parse_avp(data, variant)
                avps.append(avp)

        return avps

    def parse_simple_value(self, binary_data, avp_type):
        """Parse simple AVP types"""
        match avp_type:
            case EricssonAVPDatabase.TYPE_INTEGER_32:
                return struct.unpack(">i", binary_data)[0]

            case EricssonAVPDatabase.TYPE_UNSIGNED_32:
                return struct.unpack(">I", binary_data)[0]

            case EricssonAVPDatabase.TYPE_UTF8_STRING:
                return binary_data.decode("utf-8")

            case EricssonAVPDatabase.TYPE_OCTET_STRING:
                return binary_data

            case EricssonAVPDatabase.TYPE_TIME:
                seconds = struct.unpack(">I", binary_data)[0]
                return self.NTP_EPOCH + timedelta(seconds=seconds)

            case EricssonAVPDatabase.TYPE_ENUMERATED:
                return struct.unpack(">i", binary_data)[0]

            case EricssonAVPDatabase.TYPE_DIAMETER_IDENTITY:
                return binary_data.decode("utf-8")

            case EricssonAVPDatabase.TYPE_ADDRESS:
                # Address format: 1 byte family + address bytes
                family = binary_data[0]
                address_bytes = binary_data[1:]
                if family == 1:  # IPv4
                    return socket.inet_ntoa(address_bytes)
                elif family == 2:  # IPv6
                    return socket.inet_ntop(socket.AF_INET6, address_bytes)
                else:
                    return address_bytes  # Unknown format

            case _:
                return binary_data  # Fallback for unknown types

    def parse_message(self, binary_data):
        """Parse complete Diameter message"""
        # Parse header
        header, data = self.parse_header(binary_data)
        print(header)

        # Detect variant based on first AVP
        variant = self.detect_variant(data)

        # Parse all AVPs
        avps = []
        while data:
            avp, data = self.parse_avp(data, variant)
            avps.append(avp)

        return {"header": header, "variant": variant, "avps": avps}

    def detect_variant(self, avp_data):
        """Detect charging variant from AVP structure"""
        # Try to parse the first AVP without knowing variant
        first_avp, _ = self.parse_avp(avp_data, None)

        # Variant-1 uses Ericsson-specific grouped AVPs
        if first_avp["name"] == "Ericsson-Service-Information":
            return 1

        # Variant-2 uses standard 3GPP grouped AVPs
        if first_avp["name"] in ["Service-Information", "IMS-Information"]:
            return 2

        # Default to Variant-2 (more recent standard)
        return 2


def run():
    import gzip
    from rich.progress import Progress

    file = Path("/home/rsilva/volte_claro/").ls().shuffle()[0]
    # Read CDR file
    with gzip.open(file, "rb") as f:
        binary_data = f.read()

    # Parse CDR
    parser = EricssonCDRParser(binary_data)
    with Progress(transient=True) as progress:
        total = len(binary_data)
        task = progress.add_task("[red]Reading Headers...", total=total)
        i = 0

        while parser.index < total:
            if (header := parser.parse_header(i)) is not None:
                i = parser.index + header["length"]
                progress.update(
                    task,
                    description=f"[green]Position: {i}, Header: {header}",
                    completed=i,
                )


if __name__ == "__main__":
    import typer

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
