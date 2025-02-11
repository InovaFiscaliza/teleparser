from dataclasses import dataclass
from typing import Dict, List, Optional, Iterator, BinaryIO
import binascii
import gzip
from enum import Enum

class EricssonRecordType(str, Enum):
    TRANSIT = "a0"  # TRA
    ORIGINATING = "a1"  # ORI 
    FORWARDING = "a3"  # FOR
    TERMINATING = "a4"  # TER
    SMS_ORIGIN = "a5"  # SMSo
    SMS_TERM = "a7"  # SMSt

class EricssonFieldParser:
    @staticmethod
    def parse_number_field(field_data: str) -> str:
        """Parse number fields like origin/destination"""
        number = ""
        for i in range(2, len(field_data), 2):
            number += field_data[i + 1] + field_data[i]
        return number

    @staticmethod
    def parse_datetime(field_data: str) -> str:
        """Parse date/time fields"""
        return f"{int(field_data[0:2], 16):02d}:{int(field_data[2:4], 16):02d}:{int(field_data[4:6], 16):02d}"

@dataclass
class EricssonRecord:
    """Represents a parsed Ericsson CDR record"""
    record_type: str
    billing_id: str 
    reference_id: str
    date: str
    time: str
    imsi: str
    location_info: str
    route: str
    origin_number: str
    destination_number: str
    call_type: str
    duration: str
    call_position: str
    fault_code: str
    eos_info: str
    internal_cause: str
    disconnecting_party: str
    bssmap_cause_code: str
    channel_seizure_time: str
    called_party_seizure_time: str
    carrier_code: str
    translated_number: str
    imei: str
    time_register_to_charging: str  # trssc
    interruption_time: str  # intt

    def to_csv_row(self) -> str:
        """Convert record to CSV row format matching original output"""
        return ";".join([
            self.record_type,
            self.billing_id.replace("'", "")[2:],
            self.reference_id,
            self.format_date(),
            self.format_time(),
            self.imsi.replace("f", ""),
            self.location_info,
            self.route.replace("'", "")[2:],
            self.origin_number,
            self.destination_number.replace("f", ""),
            self.call_type,
            self.duration,
            self.call_position,
            self.fault_code,
            self.eos_info,
            self.internal_cause,
            self.disconnecting_party,
            self.bssmap_cause_code,
            self.channel_seizure_time,
            self.called_party_seizure_time,
            self.carrier_code,
            self.translated_number,
            self.imei.replace("f", ""),
            self.time_register_to_charging,
            self.interruption_time
        ])

    def format_date(self) -> str:
        """Format date as DD/MM/YY"""
        date_parts = self.date.split("/")
        return f"{date_parts[2].zfill(2)}/{date_parts[1].zfill(2)}/{date_parts[0].zfill(2)}"

    def format_time(self) -> str:
        """Format time as HH:MM:SS"""
        time_parts = self.time.split(":")
        return f"{time_parts[0].zfill(2)}:{time_parts[1].zfill(2)}:{time_parts[2].zfill(2)}"

FIELD_PARSERS = {
    "84": EricssonFieldParser.parse_number_field,
    "89": EricssonFieldParser.parse_datetime,
    # Add other field parsers...
}

class EricssonParser:
    """Base parser for Ericsson CDR binary format"""
    
    BUFFER_SIZE = 1024 * 1024  # 1MB buffer
    
    def __init__(self):
        self.current_position: int = 2
        self.hex_data: str = ""
        
    def parse_file(self, file_path: str) -> Iterator[EricssonRecord]:
        """Main entry point for parsing a CDR file"""
        with gzip.open(file_path, "rb") as file_content:
            while True:
                records = self._process_buffer(file_content)
                if not records:
                    break
                yield from records

    def _process_buffer(self, file_content: BinaryIO) -> List[EricssonRecord]:
        """Process a buffer of binary data"""
        raw_binary_data = file_content.read(self.BUFFER_SIZE)
        if not raw_binary_data:
            return []
            
        self.hex_data = str(binascii.b2a_hex(raw_binary_data))
        return self._parse_records()

    def _parse_records(self) -> List[EricssonRecord]:
        """Parse individual records from hex data"""
        records = []
        
        while self.current_position < len(self.hex_data) and self.hex_data[self.current_position] != "'":
            record = self._parse_single_record()
            if record:
                records.append(record)
                
        return records

    def _parse_single_record(self) -> Optional[EricssonRecord]:
        """Parse a single CDR record"""
        current_tag = self.hex_data[self.current_position:self.current_position + 2]
        
        if current_tag == "00":
            self.current_position += 2
            return None
            
        record_block = self._read_record_block()
        if not record_block:
            return None
            
        return self._create_record(record_block)

    def _read_record_block(self) -> Optional[str]:
        """Read a record block and handle length indicators"""
        tag_length = self._get_tag_length()
        field_length = self._get_field_length()
        
        if field_length is None:
            return None
            
        record_data = self.hex_data[self.current_position:self.current_position + field_length * 2]
        self.current_position += field_length * 2
        
        return record_data

    def _get_tag_length(self) -> int:
        """Calculate tag length based on format indicators"""
        tag_length = 1
        if (int(self.hex_data[self.current_position + 1], 16) == 15 and 
            int(self.hex_data[self.current_position], 16) % 2 != 0):
            self.current_position += 2
            while int(self.hex_data[self.current_position:self.current_position + 2], 16) > 127:
                self.current_position += 2
                tag_length += 1
        return tag_length

    def _get_field_length(self) -> Optional[int]:
        """Get field length accounting for extended length format"""
        self.current_position += 2
        length = int(self.hex_data[self.current_position:self.current_position + 2], 16)
        
        if length > 127:
            length_indicator = length - 128
            if length_indicator == 0:
                return 0
            
            self.current_position += 2
            actual_length = self.hex_data[self.current_position:self.current_position + length_indicator * 2]
            return int(actual_length, 16)
            
        return length

    def _create_record(self, record_block: str) -> Optional[EricssonRecord]:
        """Create EricssonRecord instance based on record type"""
        record_type = record_block[0:2]
        if record_type not in EricssonRecordType.__members__.values():
            return None
            
        # Record type specific parsing will be implemented in derived classes
        raise NotImplementedError("Record parsing must be implemented by specific parser classes")

class TransitRecordParser(EricssonParser):
    """Parser for Transit (TRA) records - record type a0"""
    
    FIELD_TAGS = {
        "84": "origin_number",
        "96": "carrier_code",
        "86": "imsi",
        "9f2e": "reference_id",
        "85": "destination_number",
        "88": "date",
        "89": "time",
        "93": "billing_id",
        "8b": "duration",
        "9f29": "fault_code",
        "9b": "eos_info",
        "9c": "internal_cause",
        "83": "call_type",
        "9a": "call_position",
        "95": "route",
        "87": "disconnecting_party",
        "8d": "time_register_to_charging"
    }

    def _parse_tra_record(self, record_data: str) -> EricssonRecord:
        """Parse Transit record fields"""
        field_values = {}
        field_position = 0

        while record_data[field_position] != ".":
            tag = self._get_field_tag(record_data, field_position)
            field_position += len(tag) + 2  # Skip tag and length indicator
            
            field_length = self._get_field_length_from_data(record_data[field_position:])
            field_data = record_data[field_position + 2:field_position + field_length * 2 + 2]
            
            if tag in self.FIELD_TAGS:
                field_name = self.FIELD_TAGS[tag]
                field_values[field_name] = self._parse_field_value(tag, field_data)
            
            field_position += 2 + field_length * 2

        return EricssonRecord(
            record_type="TRA",
            billing_id=field_values.get("billing_id", ""),
            reference_id=field_values.get("reference_id", ""),
            date=self._format_date(field_values.get("date", "")),
            time=self._format_time(field_values.get("time", "")),
            imsi=field_values.get("imsi", ""),
            location_info="",  # Not present in TRA records
            route=field_values.get("route", ""),
            origin_number=field_values.get("origin_number", ""),
            destination_number=field_values.get("destination_number", ""),
            call_type=field_values.get("call_type", ""),
            duration=field_values.get("duration", ""),
            call_position=field_values.get("call_position", ""),
            fault_code=field_values.get("fault_code", ""),
            eos_info=field_values.get("eos_info", ""),
            internal_cause=field_values.get("internal_cause", ""),
            disconnecting_party=field_values.get("disconnecting_party", ""),
            bssmap_cause_code="",  # Not present in TRA records
            channel_seizure_time="",  # Not present in TRA records
            called_party_seizure_time="",  # Not present in TRA records
            carrier_code=field_values.get("carrier_code", ""),
            translated_number="",  # Not present in TRA records
            imei="",  # Not present in TRA records
            time_register_to_charging=field_values.get("time_register_to_charging", ""),
            interruption_time=""  # Not present in TRA records
        )

    def _parse_field_value(self, tag: str, field_data: str) -> str:
        """Parse field value based on tag type"""
        if tag in ("84", "85"):  # Phone numbers
            return self._parse_phone_number(field_data)
        elif tag in ("88", "89", "8b", "8d"):  # Time fields
            return self._parse_time_field(field_data)
        elif tag in ("96", "93", "95"):  # ASCII fields
            return self._parse_ascii_field(field_data)
        elif tag in ("9f29", "9b", "9c", "83", "9a", "87"):  # Hex integers
            return str(int(field_data, 16))
        return field_data

    def _parse_phone_number(self, field_data: str) -> str:
        number = ""
        for i in range(2, len(field_data), 2):
            number += field_data[i + 1] + field_data[i]
        return number

    def _parse_time_field(self, field_data: str) -> str:
        return f"{int(field_data[0:2], 16)}:{int(field_data[2:4], 16)}:{int(field_data[4:6], 16)}"

    def _parse_ascii_field(self, field_data: str) -> str:
        ascii_bytes = str.encode(field_data)
        return str(binascii.a2b_hex(ascii_bytes))[2:].replace("'", "")

class OriginatingRecordParser(EricssonParser):
    """Parser for Originating (ORI) records - record type a1"""
    
    FIELD_TAGS = {
        "84": "origin_number",
        "97": "carrier_code",
        "86": "imsi",
        "9f44": "reference_id",
        "87": "destination_number",
        "89": "date",
        "8a": "time",
        "94": "billing_id",
        "8c": "duration",
        "9f3b": "fault_code",
        "9f22": "eos_info",
        "9f23": "internal_cause",
        "83": "call_type",
        "9f21": "call_position",
        "96": "route",
        "88": "disconnecting_party",
        "9a": "channel_seizure_time",
        "9f62": "bssmap_cause_code",
        "9b": "location_info",
        "8e": "time_register_to_charging",
        "9f4a": "translated_number",
        "85": "imei"
    }

    def _parse_ori_record(self, record_data: str) -> EricssonRecord:
        """Parse Originating record fields"""
        field_values = {}
        field_position = 0

        while record_data[field_position] != ".":
            tag = self._get_field_tag(record_data, field_position)
            field_position += len(tag) + 2
            
            field_length = self._get_field_length_from_data(record_data[field_position:])
            field_data = record_data[field_position + 2:field_position + field_length * 2 + 2]
            
            if tag in self.FIELD_TAGS:
                field_name = self.FIELD_TAGS[tag]
                field_values[field_name] = self._parse_field_value(tag, field_data)
            
            field_position += 2 + field_length * 2

        return EricssonRecord(
            record_type="ORI",
            billing_id=field_values.get("billing_id", ""),
            reference_id=field_values.get("reference_id", ""),
            date=self._format_date(field_values.get("date", "")),
            time=self._format_time(field_values.get("time", "")),
            imsi=field_values.get("imsi", ""),
            location_info=self._format_location_info(field_values.get("location_info", "")),
            route=field_values.get("route", ""),
            origin_number=field_values.get("origin_number", ""),
            destination_number=field_values.get("destination_number", ""),
            call_type=field_values.get("call_type", ""),
            duration=field_values.get("duration", ""),
            call_position=field_values.get("call_position", ""),
            fault_code=field_values.get("fault_code", ""),
            eos_info=field_values.get("eos_info", ""),
            internal_cause=field_values.get("internal_cause", ""),
            disconnecting_party=field_values.get("disconnecting_party", ""),
            bssmap_cause_code=field_values.get("bssmap_cause_code", ""),
            channel_seizure_time=field_values.get("channel_seizure_time", ""),
            called_party_seizure_time="",  # Not present in ORI records
            carrier_code=field_values.get("carrier_code", ""),
            translated_number=field_values.get("translated_number", ""),
            imei=field_values.get("imei", ""),
            time_register_to_charging=field_values.get("time_register_to_charging", ""),
            interruption_time=""  # Not present in ORI records
        )

    def _format_location_info(self, location_data: str) -> str:
        """Format location information specific to ORI records"""
        if not location_data:
            return ""
            
        parts = [
            f"{int(location_data[1], 16)}{int(location_data[0], 16)}{int(location_data[3], 16)}",
            f"{int(location_data[5], 16)}{int(location_data[4], 16)}{int(location_data[2], 16)}",
            str(int(location_data[6:10], 16)),
            str(int(location_data[10:14], 16))
        ]
        return "-".join(parts)

class ForwardingRecordParser(EricssonParser):
    """Parser for Forwarding (FOR) records - record type a3"""
    
    FIELD_TAGS = {
        "84": "origin_number",
        "9a": "carrier_code",
        "8a": "imsi",
        "9f39": "reference_id",
        "85": "destination_number",
        "8d": "date",
        "8e": "time",
        "97": "billing_id",
        "90": "duration",
        "9f33": "fault_code",
        "9e": "eos_info",
        "9f1f": "internal_cause",
        "83": "call_type",
        "9d": "call_position",
        "99": "route",
        "8c": "disconnecting_party",
        "92": "time_register_to_charging",
        "86": "imei"
    }

    def _parse_for_record(self, record_data: str) -> EricssonRecord:
        """Parse Forwarding record fields"""
        field_values = {}
        field_position = 0

        while record_data[field_position] != ".":
            tag = self._get_field_tag(record_data, field_position)
            field_position += len(tag) + 2
            
            field_length = self._get_field_length_from_data(record_data[field_position:])
            field_data = record_data[field_position + 2:field_position + field_length * 2 + 2]
            
            if tag in self.FIELD_TAGS:
                field_name = self.FIELD_TAGS[tag]
                field_values[field_name] = self._parse_field_value(tag, field_data)
            
            field_position += 2 + field_length * 2

        return EricssonRecord(
            record_type="FOR",
            billing_id=field_values.get("billing_id", ""),
            reference_id=field_values.get("reference_id", ""),
            date=self._format_date(field_values.get("date", "")),
            time=self._format_time(field_values.get("time", "")),
            imsi=field_values.get("imsi", ""),
            location_info="",  # Not present in FOR records
            route=field_values.get("route", ""),
            origin_number=field_values.get("origin_number", ""),
            destination_number=field_values.get("destination_number", ""),
            call_type=field_values.get("call_type", ""),
            duration=field_values.get("duration", ""),
            call_position=field_values.get("call_position", ""),
            fault_code=field_values.get("fault_code", ""),
            eos_info=field_values.get("eos_info", ""),
            internal_cause=field_values.get("internal_cause", ""),
            disconnecting_party=field_values.get("disconnecting_party", ""),
            bssmap_cause_code="",  # Not present in FOR records
            channel_seizure_time="",  # Not present in FOR records
            called_party_seizure_time="",  # Not present in FOR records
            carrier_code=field_values.get("carrier_code", ""),
            translated_number="",  # Not present in FOR records
            imei=field_values.get("imei", ""),
            time_register_to_charging=field_values.get("time_register_to_charging", ""),
            interruption_time=""  # Not present in FOR records
        )

class TerminatingRecordParser(EricssonParser):
    """Parser for Terminating (TER) records - record type a4"""
    
    FIELD_TAGS = {
        "84": "origin_number",
        "97": "carrier_code",
        "87": "imei",
        "86": "imsi",
        "9f43": "reference_id",
        "85": "destination_number",
        "8a": "date",
        "8b": "time",
        "94": "billing_id",
        "8d": "duration",
        "9f3b": "fault_code",
        "9f22": "eos_info",
        "9f23": "internal_cause",
        "83": "call_type",
        "9f21": "call_position",
        "96": "route",
        "89": "disconnecting_party",
        "9a": "called_party_seizure_time",
        "9f55": "bssmap_cause_code",
        "9b": "location_info",
        "8f": "time_register_to_charging"
    }

    def _parse_ter_record(self, record_data: str) -> EricssonRecord:
        """Parse Terminating record fields"""
        field_values = {}
        field_position = 0

        while record_data[field_position] != ".":
            tag = self._get_field_tag(record_data, field_position)
            field_position += len(tag) + 2
            
            field_length = self._get_field_length_from_data(record_data[field_position:])
            field_data = record_data[field_position + 2:field_position + field_length * 2 + 2]
            
            if tag in self.FIELD_TAGS:
                field_name = self.FIELD_TAGS[tag]
                field_values[field_name] = self._parse_field_value(tag, field_data)
            
            field_position += 2 + field_length * 2

        return EricssonRecord(
            record_type="TER",
            billing_id=field_values.get("billing_id", ""),
            reference_id=field_values.get("reference_id", ""),
            date=self._format_date(field_values.get("date", "")),
            time=self._format_time(field_values.get("time", "")),
            imsi=field_values.get("imsi", ""),
            location_info=self._format_location_info(field_values.get("location_info", "")),
            route=field_values.get("route", ""),
            origin_number=field_values.get("origin_number", ""),
            destination_number=field_values.get("destination_number", ""),
            call_type=field_values.get("call_type", ""),
            duration=field_values.get("duration", ""),
            call_position=field_values.get("call_position", ""),
            fault_code=field_values.get("fault_code", ""),
            eos_info=field_values.get("eos_info", ""),
            internal_cause=field_values.get("internal_cause", ""),
            disconnecting_party=field_values.get("disconnecting_party", ""),
            bssmap_cause_code=field_values.get("bssmap_cause_code", ""),
            channel_seizure_time="",  # Not present in TER records
            called_party_seizure_time=field_values.get("called_party_seizure_time", ""),
            carrier_code=field_values.get("carrier_code", ""),
            translated_number="",  # Not present in TER records
            imei=field_values.get("imei", ""),
            time_register_to_charging=field_values.get("time_register_to_charging", ""),
            interruption_time=""  # Not present in TER records
        )

    def _format_location_info(self, location_data: str) -> str:
        """Format location information specific to TER records"""
        if not location_data:
            return ""
            
        parts = [
            f"{int(location_data[1], 16)}{int(location_data[0], 16)}{int(location_data[3], 16)}",
            f"{int(location_data[5], 16)}{int(location_data[4], 16)}{int(location_data[2], 16)}",
            str(int(location_data[6:10], 16)),
            str(int(location_data[10:14], 16))
        ]
        return "-".join(parts)
class SMSOriginRecordParser(EricssonParser):
    """Parser for SMS Origin (SMSo) records - record type a5"""
    
    FIELD_TAGS = {
        "8e": "location_info",
        "84": "origin_number",
        "81": "carrier_code",
        "9f2a": "imei",
        "9f2b": "reference_id",
        "87": "date",
        "88": "time",
        "8b": "billing_id",
        "83": "call_type",
        "9f2a": "call_position"
    }

    def _parse_smso_record(self, record_data: str) -> EricssonRecord:
        """Parse SMS Origin record fields"""
        field_values = {}
        field_position = 0

        while record_data[field_position] != ".":
            tag = self._get_field_tag(record_data, field_position)
            field_position += len(tag) + 2
            
            field_length = self._get_field_length_from_data(record_data[field_position:])
            field_data = record_data[field_position + 2:field_position + field_length * 2 + 2]
            
            if tag in self.FIELD_TAGS:
                field_name = self.FIELD_TAGS[tag]
                field_values[field_name] = self._parse_field_value(tag, field_data)
            
            field_position += 2 + field_length * 2

        return EricssonRecord(
            record_type="SMSo",
            billing_id=field_values.get("billing_id", ""),
            reference_id=field_values.get("reference_id", ""),
            date=self._format_date(field_values.get("date", "")),
            time=self._format_time(field_values.get("time", "")),
            imsi="",  # Not present in SMSo records
            location_info=self._format_location_info(field_values.get("location_info", "")),
            route="",  # Not present in SMSo records
            origin_number=field_values.get("origin_number", ""),
            destination_number="",  # Not present in SMSo records
            call_type=field_values.get("call_type", ""),
            duration="",  # Not present in SMSo records
            call_position=field_values.get("call_position", ""),
            fault_code="",  # Not present in SMSo records
            eos_info="",  # Not present in SMSo records
            internal_cause="",  # Not present in SMSo records
            disconnecting_party="",  # Not present in SMSo records
            bssmap_cause_code="",  # Not present in SMSo records
            channel_seizure_time="",  # Not present in SMSo records
            called_party_seizure_time="",  # Not present in SMSo records
            carrier_code=field_values.get("carrier_code", ""),
            translated_number="",  # Not present in SMSo records
            imei=field_values.get("imei", ""),
            time_register_to_charging="",  # Not present in SMSo records
            interruption_time=""  # Not present in SMSo records
        )

    def _format_location_info(self, location_data: str) -> str:
        """Format location information specific to SMSo records"""
        if not location_data:
            return ""
            
        parts = [
            f"{int(location_data[1], 16)}{int(location_data[0], 16)}{int(location_data[3], 16)}",
            f"{int(location_data[5], 16)}{int(location_data[4], 16)}{int(location_data[2], 16)}",
            str(int(location_data[6:10], 16)),
            str(int(location_data[10:14], 16))
        ]
        return "-".join(parts)

class SMSTerminatingRecordParser(EricssonParser):
    """Parser for SMS Terminating (SMSt) records - record type a7"""

    FIELD_TAGS = {
        "81": "carrier_code",
        "83": "destination_number",
        "86": "date",
        "87": "time",
        "8a": "billing_id",
    }

    def _parse_smst_record(self, record_data: str) -> EricssonRecord:
        """Parse SMS Terminating record fields"""
        field_values = {}
        field_position = 0

        while record_data[field_position] != ".":
            tag = self._get_field_tag(record_data, field_position)
            field_position += len(tag) + 2

            field_length = self._get_field_length_from_data(
                record_data[field_position:]
            )
            field_data = record_data[
                field_position + 2 : field_position + field_length * 2 + 2
            ]

            if tag in self.FIELD_TAGS:
                field_name = self.FIELD_TAGS[tag]
                field_values[field_name] = self._parse_field_value(tag, field_data)

            field_position += 2 + field_length * 2

        return EricssonRecord(
            record_type="SMSt",
            billing_id=field_values.get("billing_id", ""),
            reference_id="",  # Not present in SMSt records
            date=self._format_date(field_values.get("date", "")),
            time=self._format_time(field_values.get("time", "")),
            imsi="",  # Not present in SMSt records
            location_info="",  # Not present in SMSt records
            route="",  # Not present in SMSt records
            origin_number="",  # Not present in SMSt records
            destination_number=field_values.get("destination_number", ""),
            call_type="",  # Not present in SMSt records
            duration="",  # Not present in SMSt records
            call_position="",  # Not present in SMSt records
            fault_code="",  # Not present in SMSt records
            eos_info="",  # Not present in SMSt records
            internal_cause="",  # Not present in SMSt records
            disconnecting_party="",  # Not present in SMSt records
            bssmap_cause_code="",  # Not present in SMSt records
            channel_seizure_time="",  # Not present in SMSt records
            called_party_seizure_time="",  # Not present in SMSt records
            carrier_code=field_values.get("carrier_code", ""),
            translated_number="",  # Not present in SMSt records
            imei="",  # Not present in SMSt records
            time_register_to_charging="",  # Not present in SMSt records
            interruption_time="",  # Not present in SMSt records
        )

    def _parse_field_value(self, tag: str, field_data: str) -> str:
        """Parse field value based on tag type"""
        if tag == "83":  # Destination number
            return self._parse_phone_number(field_data)
        elif tag in ("86", "87"):  # Date and time fields
            return self._parse_time_field(field_data)
        elif tag == "81":  # Carrier code
            return str(int(field_data, 16))
        elif tag == "8a":  # Billing ID
            return self._parse_ascii_field(field_data)
        return field_data
