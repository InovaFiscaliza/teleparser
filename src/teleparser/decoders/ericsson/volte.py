import struct
from datetime import datetime, timedelta
from typing import Tuple
import socket
from fastcore.xtras import Path


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
    # Vendor IDs
    VENDOR_DIAMETER = 0
    VENDOR_3GPP = 10415
    VENDOR_ERICSSON = 193

    # AVP Type Codes
    TYPE_OCTET_STRING = 0
    TYPE_INTEGER_32 = 1
    TYPE_UNSIGNED_32 = 2
    TYPE_UTF8_STRING = 4
    TYPE_GROUPED = 8
    TYPE_TIME = 9
    TYPE_ENUMERATED = 10
    TYPE_DIAMETER_IDENTITY = 11
    TYPE_ADDRESS = 12

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


# class CommandFlags:
#     """Command Flags parser for Diameter protocol messages

#     Parses an 8-bit byte according to the following rules:
#     Bit 0: R - Set to 1 if ACR message, 0 if ACA message
#     Bit 1: P - Set to 1 if message is proxiable (always 1 for ACR/ACA)
#     Bit 2: E - Set to 1 if ACA contains Protocol Error 3xxx, 0 otherwise
#     Bit 3: T - Set to 1 if retransmitted message, 0 otherwise
#     Bits 4-7: Reserved (must be 0)
#     """

#     def __init__(self, flags_byte: int):
#         """Initialize with a single byte (0-255) or hex value"""
#         if not (0 <= flags_byte <= 255):
#             raise ValueError(
#                 f"Command flags must be a single byte (0-255), got: {flags_byte}"
#             )

#         self.flags_byte = flags_byte
#         self._parse_flags()

#     def _parse_flags(self):
#         """Parse individual flag bits from the byte"""
#         # Extract individual bits (bit 0 is MSB, bit 7 is LSB)
#         self.R = bool(self.flags_byte & 0x80)  # Bit 0 (MSB)
#         self.P = bool(self.flags_byte & 0x40)  # Bit 1
#         self.E = bool(self.flags_byte & 0x20)  # Bit 2
#         self.T = bool(self.flags_byte & 0x10)  # Bit 3

#         if self.E and self.R:
#             raise ValueError(
#                 "Protocol Error 3xxx flag (E=1) is only valid for ACA messages, got R=1 which marks an ACR message"
#             )

#         # Check reserved bits (bits 4-7) should be 0
#         reserved_bits = self.flags_byte & 0x0F
#         if reserved_bits != 0:
#             raise ValueError(f"Reserved bits 4-7 must be 0, got: {bin(reserved_bits)}")

#     @property
#     def is_acr_message(self) -> bool:
#         """Returns True if this is an ACR message (R=1), False if ACA (R=0)"""
#         return self.R

#     @property
#     def is_aca_message(self) -> bool:
#         """Returns True if this is an ACA message (R=0, P=1), False if ACR (R=1)"""
#         return not self.R and self.P

#     @property
#     def is_proxiable(self) -> bool:
#         """Returns True if message is proxiable (should always be True for ACR/ACA)"""
#         return self.P

#     @property
#     def has_protocol_error(self) -> bool:
#         """Returns True if ACA contains Protocol Error 3xxx"""
#         return self.E

#     @property
#     def is_retransmitted(self) -> bool:
#         """Returns True if this is a retransmitted message"""
#         return self.T

#     @property
#     def value(self) -> dict:
#         """Returns a dictionary with all flag values"""
#         return {
#             "R": self.R,
#             "P": self.P,
#             "E": self.E,
#             "T": self.T,
#             "isACR": self.is_acr_message,
#             "isACA": self.is_aca_message,
#         }

#     def __str__(self) -> str:
#         """String representation showing flag states"""
#         msg_type = "ACR" if self.is_acr_message else "ACA"
#         flags = []
#         if self.P:
#             flags.append("Proxiable")
#         if self.E:
#             flags.append("Protocol Error")
#         if self.T:
#             flags.append("Retransmitted")

#         flag_str = ", ".join(flags) if flags else "None"
#         return f"{msg_type} message - Flags: {flag_str}"

#     def __repr__(self) -> str:
#         return f"CommandFlags(0x{self.flags_byte:02X}) - R:{int(self.R)} P:{int(self.P)} E:{int(self.E)} T:{int(self.T)}"


# def parse_command_flags(flags_byte: int) -> CommandFlags:
#     """Parse command flags from a single byte

#     Args:
#         flags_byte: Integer value (0-255) representing the 8-bit command flags

#     Returns:
#         CommandFlags object with parsed flag values

#     Example:
#         >>> flags = parse_command_flags(0xC0)  # R=1, P=1, E=0, T=0
#         >>> print(flags.is_acr_message)  # True
#         >>> print(flags.is_proxiable)    # True
#         >>> print(flags)                 # ACR message - Flags: Proxiable
#     """
#     return CommandFlags(flags_byte)


class EricssonCDRParser:
    DIAMETER_HEADER_FORMAT = ">B3sB3sIII"  # Big-endian format
    HEADER_SIZE = 20  # Fixed 20-byte header
    NTP_EPOCH = datetime(1900, 1, 1)  # For timestamp conversion
    PREFIX_HEADER_LENGTH = 2

    def __init__(self, binary_data: bytes):
        self.avp_db = EricssonAVPDatabase()
        self.binary_data = binary_data
        self.index = 0

    def parse_header(self, index: int) -> dict:
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

        block_data = self.binary_data[self.index :]

        # Validate minimum length
        if len(block_data) < self.HEADER_SIZE:
            raise ValueError(
                f"Header requires {self.HEADER_SIZE} bytes, got {len(block_data)}"
            )

        # Unpack all header fields
        (version, msg_len_bytes, flags, cmd_bytes, app_id, hbh_id, e2e_id) = (
            struct.unpack(self.DIAMETER_HEADER_FORMAT, block_data[: self.HEADER_SIZE])
        )

        # Convert 24-bit fields
        msg_length = int.from_bytes(msg_len_bytes)
        command_code = int.from_bytes(cmd_bytes)

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
        if command_code != 271:
            raise ValueError(
                f"Invalid Command-Code: {command_code} (expected 271 for accounting)"
            )

        # Build header dictionary
        return {
            "version": version,
            "length": msg_length,
            "flags": flag_bits,
            "command_code": command_code,
            "application_id": app_id,
            "hop_by_hop_id": hbh_id,
            "end_to_end_id": e2e_id,
            "message_type": "ACR" if flag_bits["R"] else "ACA",
        }

    def parse_avp(self, binary_data, variant):
        """Parse a single AVP from binary data"""
        if len(binary_data) < 8:
            raise ValueError("Insufficient data for AVP header")

        # Parse AVP header (8 bytes)
        avp_code, flags, avp_length = struct.unpack(">IBB", binary_data[0:6])
        avp_length = (avp_length << 16) | struct.unpack(">H", binary_data[6:8])[0]

        # Check if we have enough data
        if len(binary_data) < avp_length:
            raise ValueError(
                f"AVP length {avp_length} exceeds available data {len(binary_data)}"
            )

        # Extract vendor ID if present
        vendor_id = EricssonAVPDatabase.VENDOR_DIAMETER
        header_size = 8
        if flags & 0x80:  # Vendor flag set
            if avp_length < 12:
                raise ValueError("AVP with vendor flag requires at least 12 bytes")
            vendor_id = struct.unpack(">I", binary_data[8:12])[0]
            header_size = 12

        # Get AVP definition
        avp_def = self.avp_db.get_avp_definition(avp_code, vendor_id)

        # Handle unknown AVP
        if not avp_def:
            return {
                "code": avp_code,
                "vendor_id": vendor_id,
                "name": f"Unknown_{avp_code}",
                "type": "OctetString",
                "value": binary_data[header_size:avp_length],
            }, binary_data[avp_length:]

        assert is_avp_flag_valid(flags, avp_def["flags"]), (
            f"Invalid AVP flags: {bin(flags)}"
        )

        # Parse value based on type
        value_data = binary_data[header_size:avp_length]
        avp_type = avp_def["type"]

        if avp_type == EricssonAVPDatabase.TYPE_GROUPED:
            value = self.parse_grouped_avp(value_data, variant, avp_def["name"])
        else:
            value = self.parse_simple_value(value_data, avp_type)

        return {
            "code": avp_code,
            "vendor_id": vendor_id,
            "name": avp_def["name"],
            "type": avp_type,
            "value": value,
        }, binary_data[avp_length:]

    def parse_grouped_avp(self, binary_data, variant, grouped_name):
        """Parse a grouped AVP (recursive)"""
        avps = []
        data = binary_data

        # Handle variant-specific grouping rules
        if grouped_name == "Ericsson-Service-Information" and variant == 1:
            # Variant-1 specific structure
            while data:
                avp, data = self.parse_avp(data, variant)
                avps.append(avp)

        elif grouped_name == "IMS-Information" and variant == 2:
            # Variant-2 specific structure
            while data:
                avp, data = self.parse_avp(data, variant)
                # Special handling for Event-Type subgroup
                if avp["name"] == "Event-Type":
                    avp["value"] = self.parse_grouped_avp(
                        avp["value"], variant, "Event-Type"
                    )
                avps.append(avp)

        else:
            # Default grouping behavior
            while data:
                avp, data = self.parse_avp(data, variant)
                avps.append(avp)

        return avps

    def parse_simple_value(self, binary_data, avp_type):
        """Parse simple AVP types"""
        if avp_type == EricssonAVPDatabase.TYPE_INTEGER_32:
            return struct.unpack(">i", binary_data)[0]

        elif avp_type == EricssonAVPDatabase.TYPE_UNSIGNED_32:
            return struct.unpack(">I", binary_data)[0]

        elif avp_type == EricssonAVPDatabase.TYPE_UTF8_STRING:
            return binary_data.decode("utf-8")

        elif avp_type == EricssonAVPDatabase.TYPE_OCTET_STRING:
            return binary_data

        elif avp_type == EricssonAVPDatabase.TYPE_TIME:
            seconds = struct.unpack(">I", binary_data)[0]
            return self.NTP_EPOCH + timedelta(seconds=seconds)

        elif avp_type == EricssonAVPDatabase.TYPE_ENUMERATED:
            return struct.unpack(">i", binary_data)[0]

        elif avp_type == EricssonAVPDatabase.TYPE_DIAMETER_IDENTITY:
            return binary_data.decode("utf-8")

        elif avp_type == EricssonAVPDatabase.TYPE_ADDRESS:
            # Address format: 1 byte family + address bytes
            family = binary_data[0]
            address_bytes = binary_data[1:]
            if family == 1:  # IPv4
                return socket.inet_ntoa(address_bytes)
            elif family == 2:  # IPv6
                return socket.inet_ntop(socket.AF_INET6, address_bytes)
            else:
                return address_bytes  # Unknown format

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


if __name__ == "__main__":
    import gzip
    from rich.progress import Progress

    file = Path("/home/rsilva/volte_claro/").ls().shuffle()[0]
    # Read CDR file
    with gzip.open(file, "rb") as f:
        binary_data = f.read()

    # Parse CDR
    parser = EricssonCDRParser(binary_data)
    with Progress(transient=True) as progress:
        task = progress.add_task("[red]Reading Headers...", total=len(binary_data))
        i = 0
        header = parser.parse_header(i)

        while i < len(parser.binary_data):
            i = parser.index + header["length"]
            parser.binary_data[i : i + 22]
            header = parser.parse_header(i)
            progress.update(task, description=f"[green]Position: {i}", advance=i)

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
