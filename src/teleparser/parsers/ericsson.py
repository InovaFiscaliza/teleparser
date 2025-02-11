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
