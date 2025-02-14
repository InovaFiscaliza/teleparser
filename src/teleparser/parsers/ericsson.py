import binascii
from contextlib import contextmanager
import gzip
from dataclasses import dataclass
from enum import Enum
from typing import BinaryIO, Dict, Iterator, Optional

CSV_HEADER = (
    "Tipo_de_chamada",
    "Bilhetador",
    "Referencia",
    "Data",
    "Hora",
    "IMSI",
    "1stCelA",
    "Outgoing_route",
    "Origem",
    "Destino",
    "Type_of_calling_subscriber",
    "TTC",
    "Call_position",
    "Fault_code",
    "EOS_info",
    "Internal_cause_and_location",
    "Disconnecting_party",
    "BSSMAP_cause_code",
    "Time_for_calling_party_traffic_channel_seizure",
    "Time_for_called_party_traffic_channel_seizure",
    "Call_identification_number",
    "Translated_number",
    "IMEI",
    "TimefromRregistertoStartofCharging",
    "InterruptionTime",
)


class EricssonRecordType(str, Enum):
    TRANSIT = "a0"  # TRA
    ORIGINATING = "a1"  # ORI
    FORWARDING = "a3"  # FOR
    TERMINATING = "a4"  # TER
    SMS_ORIGIN = "a5"  # SMSo
    SMS_TERM = "a7"  # SMSt


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
        return ";".join(
            [
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
                self.interruption_time,
            ]
        )

    def format_date(self) -> str:
        """Format date as DD/MM/YY"""
        date_parts = self.date.split("/")
        return f"{date_parts[2].zfill(2)}/{date_parts[1].zfill(2)}/{date_parts[0].zfill(2)}"

    def format_time(self) -> str:
        """Format time as HH:MM:SS"""
        time_parts = self.time.split(":")
        return f"{time_parts[0].zfill(2)}:{time_parts[1].zfill(2)}:{time_parts[2].zfill(2)}"



class BufferManager:
    """Manages CDR file reading and hex conversion"""

    def __init__(self, buffer_size: int):
        self.buffer_size = buffer_size
        self.file_handle: Optional[BinaryIO] = None
        self.current_buffer: str = ""

    @contextmanager
    def open(self, file_path: str):
        with gzip.open(file_path, "rb") as self.file_handle:
            yield self

    def has_data(self) -> bool:
        return bool(self.file_handle and not self.file_handle.closed)

    def read_buffer(self) -> str:
        raw_data = self.file_handle.read(self.buffer_size)
        if not raw_data:
            return ""
        return str(binascii.b2a_hex(raw_data))


class RecordValidator:
    """Validates CDR record structure and content"""

    TIMESTAMP_THRESHOLD = 10000  # Threshold for timestamp validation

    def is_valid_timestamp(self, hex_data: str, position: int) -> bool:
        """Validate timestamp in current buffer position"""
        if 2 * BufferManager.BUFFER_SIZE - position < self.TIMESTAMP_THRESHOLD:
            return len(hex_data[position:].replace("'", "")) >= self.TIMESTAMP_THRESHOLD
        return True

    def is_valid_record_type(self, record_type: str) -> bool:
        """Verify if record type is supported"""
        return record_type in EricssonRecordType.__members__.values()

    def validate_field_length(self, length: int) -> bool:
        """Validate field length indicators"""
        return length != 128

    def validate_record_structure(self, record_data: str) -> bool:
        """Validate overall record structure"""
        return (
            record_data
            and len(record_data) >= 4  # Minimum record size
            and record_data[-1] == "."  # Record terminator
        )


class RecordReader:
    """Handles reading and validation of individual CDR records"""

    def __init__(self):
        self.current_position: int = 2
        self.validator = RecordValidator()

    def read_records(self, buffer: BufferManager) -> Iterator[str]:
        hex_data = buffer.read_buffer()
        while self.current_position < len(hex_data):
            if not self.validator.is_valid_timestamp(hex_data, self.current_position):
                remaining_data = self._handle_buffer_boundary(hex_data)
                if remaining_data:
                    hex_data = remaining_data
                    self.current_position = 0
                    continue
                break

            record = self._read_single_record(hex_data)
            if record:
                yield record

    def _read_single_record(self, hex_data: str) -> Optional[str]:
        record_type = hex_data[self.current_position : self.current_position + 2]
        if record_type == "00":
            self.current_position += 2
            return None

        record_block = self._read_record_block(hex_data)
        return record_block if record_block else None

    def _read_record_block(self, hex_data: str) -> Optional[str]:
        tag_length = self._calculate_tag_length(hex_data)
        field_length = self._calculate_field_length(hex_data)

        if field_length is None:
            return None

        record_data = hex_data[
            self.current_position : self.current_position + field_length * 2
        ]
        self.current_position += field_length * 2

        return record_data


class FieldParserFactory:
    """Factory for creating and managing field parsers"""

    def __init__(self):
        self.parsers = {
            "number": self._parse_phone_number,
            "datetime": self._parse_time_field,
            "ascii": self._parse_ascii_field,
            "hex": self._parse_hex_integer,
            "location": self._parse_location_info,
        }

        self.field_types = {
            "84": "number",  # Phone numbers
            "85": "number",
            "88": "datetime",  # Date/time fields
            "89": "datetime",
            "8b": "datetime",
            "8d": "datetime",
            "96": "ascii",  # ASCII fields
            "93": "ascii",
            "95": "ascii",
            "9f29": "hex",  # Hex integers
            "9b": "hex",
            "9c": "hex",
            "83": "hex",
            "9a": "hex",
            "87": "hex",
        }

    def get_parser(self, field_tag: str):
        """Get appropriate parser for field type"""
        field_type = self.field_types.get(field_tag)
        return self.parsers.get(field_type, lambda x: x)

    @staticmethod
    def _parse_phone_number(field_data: str) -> str:
        number = ""
        for i in range(2, len(field_data), 2):
            number += field_data[i + 1] + field_data[i]
        return number

    @staticmethod
    def _parse_time_field(field_data: str) -> str:
        return f"{int(field_data[0:2], 16)}:{int(field_data[2:4], 16)}:{int(field_data[4:6], 16)}"

    @staticmethod
    def _parse_ascii_field(field_data: str) -> str:
        ascii_bytes = str.encode(field_data)
        return str(binascii.a2b_hex(ascii_bytes))[2:].replace("'", "")

    @staticmethod
    def _parse_hex_integer(field_data: str) -> str:
        return str(int(field_data, 16))

    @staticmethod
    def _parse_location_info(field_data: str) -> str:
        if not field_data:
            return ""
        parts = [
            f"{int(field_data[1], 16)}{int(field_data[0], 16)}{int(field_data[3], 16)}",
            f"{int(field_data[5], 16)}{int(field_data[4], 16)}{int(field_data[2], 16)}",
            str(int(field_data[6:10], 16)),
            str(int(field_data[10:14], 16)),
        ]
        return "-".join(parts)


class EricssonParser:
    """Base parser for Ericsson CDR binary format"""

    BUFFER_SIZE = 1024 * 1024  # 1MB buffer

    def __init__(self):
        self.buffer_manager = BufferManager(self.BUFFER_SIZE)
        self.record_reader = RecordReader()
        self.field_parser = FieldParserFactory()
        self.validator = RecordValidator()

    def parse_file(self, file_path: str) -> Iterator[EricssonRecord]:
        """Main entry point for parsing a CDR file"""
        with self.buffer_manager.open(file_path) as buffer:
            while buffer.has_data():
                for record_data in self.record_reader.read_records(buffer):
                    if not self.validator.validate_record_structure(record_data):
                        continue

                    if record := self._create_record(record_data):
                        yield record

    def _create_record(self, record_data: str) -> Optional[EricssonRecord]:
        """Create record instance - to be implemented by specific parsers"""
        record_type = record_data[0:2]
        if not self.validator.is_valid_record_type(record_type):
            return None

        raise NotImplementedError(
            "Record parsing must be implemented by specific parser classes"
        )

    def parse_field(self, field_tag: str, field_data: str) -> str:
        """Parse field using appropriate parser"""
        parser = self.field_parser.get_parser(field_tag)
        return parser(field_data)



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
        "8d": "time_register_to_charging",
    }

    def _create_record(self, record_data: str) -> Optional[EricssonRecord]:
        """Create Transit record from record block"""
        record_type = record_data[0:2]
        if record_type != EricssonRecordType.TRANSIT:
            return None

        field_values = self._parse_fields(record_data)
        return self._create_transit_record(field_values)

    def _parse_fields(self, record_data: str) -> Dict[str, str]:
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
                field_values[field_name] = self.parse_field(tag, field_data)

            field_position += 2 + field_length * 2

        return field_values

    def _create_transit_record(self, field_values: Dict[str, str]) -> EricssonRecord:
        return EricssonRecord(
            record_type="TRA",
            billing_id=field_values.get("billing_id", ""),
            reference_id=field_values.get("reference_id", ""),
            date=field_values.get("date", ""),
            time=field_values.get("time", ""),
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
            bssmap_cause_code="",
            channel_seizure_time="",
            called_party_seizure_time="",
            carrier_code=field_values.get("carrier_code", ""),
            translated_number="",
            imei="",
            time_register_to_charging=field_values.get("time_register_to_charging", ""),
            interruption_time="",
        )


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
        "85": "imei",
    }

    def _create_record(self, record_data: str) -> Optional[EricssonRecord]:
        """Create Originating record from record block"""
        record_type = record_data[0:2]
        if record_type != EricssonRecordType.ORIGINATING:
            return None

        field_values = self._parse_fields(record_data)
        return self._create_originating_record(field_values)

    def _parse_fields(self, record_data: str) -> Dict[str, str]:
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
                field_values[field_name] = self.parse_field(tag, field_data)

            field_position += 2 + field_length * 2

        return field_values

    def _create_originating_record(
        self, field_values: Dict[str, str]
    ) -> EricssonRecord:
        return EricssonRecord(
            record_type="ORI",
            billing_id=field_values.get("billing_id", ""),
            reference_id=field_values.get("reference_id", ""),
            date=field_values.get("date", ""),
            time=field_values.get("time", ""),
            imsi=field_values.get("imsi", ""),
            location_info=self.field_parser._parse_location_info(
                field_values.get("location_info", "")
            ),
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
            called_party_seizure_time="",
            carrier_code=field_values.get("carrier_code", ""),
            translated_number=field_values.get("translated_number", ""),
            imei=field_values.get("imei", ""),
            time_register_to_charging=field_values.get("time_register_to_charging", ""),
            interruption_time="",
        )


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
        "86": "imei",
    }

    def _create_record(self, record_data: str) -> Optional[EricssonRecord]:
        """Create Forwarding record from record block"""
        record_type = record_data[0:2]
        if record_type != EricssonRecordType.FORWARDING:
            return None

        field_values = self._parse_fields(record_data)
        return self._create_forwarding_record(field_values)

    def _parse_fields(self, record_data: str) -> Dict[str, str]:
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
                field_values[field_name] = self.parse_field(tag, field_data)

            field_position += 2 + field_length * 2

        return field_values

    def _create_forwarding_record(self, field_values: Dict[str, str]) -> EricssonRecord:
        return EricssonRecord(
            record_type="FOR",
            billing_id=field_values.get("billing_id", ""),
            reference_id=field_values.get("reference_id", ""),
            date=field_values.get("date", ""),
            time=field_values.get("time", ""),
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
            bssmap_cause_code="",
            channel_seizure_time="",
            called_party_seizure_time="",
            carrier_code=field_values.get("carrier_code", ""),
            translated_number="",
            imei=field_values.get("imei", ""),
            time_register_to_charging=field_values.get("time_register_to_charging", ""),
            interruption_time="",
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
        "8f": "time_register_to_charging",
    }

    def _create_record(self, record_data: str) -> Optional[EricssonRecord]:
        """Create Terminating record from record block"""
        record_type = record_data[0:2]
        if record_type != EricssonRecordType.TERMINATING:
            return None

        field_values = self._parse_fields(record_data)
        return self._create_terminating_record(field_values)

    def _parse_fields(self, record_data: str) -> Dict[str, str]:
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
                field_values[field_name] = self.parse_field(tag, field_data)

            field_position += 2 + field_length * 2

        return field_values

    def _create_terminating_record(
        self, field_values: Dict[str, str]
    ) -> EricssonRecord:
        return EricssonRecord(
            record_type="TER",
            billing_id=field_values.get("billing_id", ""),
            reference_id=field_values.get("reference_id", ""),
            date=field_values.get("date", ""),
            time=field_values.get("time", ""),
            imsi=field_values.get("imsi", ""),
            location_info=self.field_parser._parse_location_info(
                field_values.get("location_info", "")
            ),
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
            channel_seizure_time="",
            called_party_seizure_time=field_values.get("called_party_seizure_time", ""),
            carrier_code=field_values.get("carrier_code", ""),
            translated_number="",
            imei=field_values.get("imei", ""),
            time_register_to_charging=field_values.get("time_register_to_charging", ""),
            interruption_time="",
        )


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
        "9f2a": "call_position",
    }

    def _create_record(self, record_data: str) -> Optional[EricssonRecord]:
        """Create SMS Origin record from record block"""
        record_type = record_data[0:2]
        if record_type != EricssonRecordType.SMS_ORIGIN:
            return None

        field_values = self._parse_fields(record_data)
        return self._create_sms_origin_record(field_values)

    def _parse_fields(self, record_data: str) -> Dict[str, str]:
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
                field_values[field_name] = self.parse_field(tag, field_data)

            field_position += 2 + field_length * 2

        return field_values

    def _create_sms_origin_record(self, field_values: Dict[str, str]) -> EricssonRecord:
        return EricssonRecord(
            record_type="SMSo",
            billing_id=field_values.get("billing_id", ""),
            reference_id=field_values.get("reference_id", ""),
            date=field_values.get("date", ""),
            time=field_values.get("time", ""),
            imsi="",
            location_info=self.field_parser._parse_location_info(
                field_values.get("location_info", "")
            ),
            route="",
            origin_number=field_values.get("origin_number", ""),
            destination_number="",
            call_type=field_values.get("call_type", ""),
            duration="",
            call_position=field_values.get("call_position", ""),
            fault_code="",
            eos_info="",
            internal_cause="",
            disconnecting_party="",
            bssmap_cause_code="",
            channel_seizure_time="",
            called_party_seizure_time="",
            carrier_code=field_values.get("carrier_code", ""),
            translated_number="",
            imei=field_values.get("imei", ""),
            time_register_to_charging="",
            interruption_time="",
        )


class SMSTerminatingRecordParser(EricssonParser):
    """Parser for SMS Terminating (SMSt) records - record type a7"""

    FIELD_TAGS = {
        "81": "carrier_code",
        "83": "destination_number",
        "86": "date",
        "87": "time",
        "8a": "billing_id",
    }

    def _create_record(self, record_data: str) -> Optional[EricssonRecord]:
        """Create SMS Terminating record from record block"""
        record_type = record_data[0:2]
        if record_type != EricssonRecordType.SMS_TERM:
            return None

        field_values = self._parse_fields(record_data)
        return self._create_sms_terminating_record(field_values)

    def _parse_fields(self, record_data: str) -> Dict[str, str]:
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
                field_values[field_name] = self.parse_field(tag, field_data)

            field_position += 2 + field_length * 2

        return field_values

    def _create_sms_terminating_record(
        self, field_values: Dict[str, str]
    ) -> EricssonRecord:
        return EricssonRecord(
            record_type="SMSt",
            billing_id=field_values.get("billing_id", ""),
            reference_id="",
            date=field_values.get("date", ""),
            time=field_values.get("time", ""),
            imsi="",
            location_info="",
            route="",
            origin_number="",
            destination_number=field_values.get("destination_number", ""),
            call_type="",
            duration="",
            call_position="",
            fault_code="",
            eos_info="",
            internal_cause="",
            disconnecting_party="",
            bssmap_cause_code="",
            channel_seizure_time="",
            called_party_seizure_time="",
            carrier_code=field_values.get("carrier_code", ""),
            translated_number="",
            imei="",
            time_register_to_charging="",
            interruption_time="",
        )


class EricssonUnifiedParser:
    """Unified parser system for all Ericsson CDR record types"""

    def __init__(self):
        self.parsers = {
            EricssonRecordType.TRANSIT: TransitRecordParser(),
            EricssonRecordType.ORIGINATING: OriginatingRecordParser(),
            EricssonRecordType.FORWARDING: ForwardingRecordParser(),
            EricssonRecordType.TERMINATING: TerminatingRecordParser(),
            EricssonRecordType.SMS_ORIGIN: SMSOriginRecordParser(),
            EricssonRecordType.SMS_TERM: SMSTerminatingRecordParser(),
        }
        self.buffer_manager = BufferManager(EricssonParser.BUFFER_SIZE)
        self.validator = RecordValidator()

    def parse_file(self, file_path: str) -> Iterator[EricssonRecord]:
        """Parse CDR file using appropriate parser based on record type"""
        for parser in self.parsers.values():
            yield from parser.parse_file(file_path)
    def parse_records_to_csv(self, input_path: str, output_path: str):
        """Parse CDR file and write records to CSV"""
        with open(output_path, "w") as out_file:
            out_file.write(self._get_csv_header())
            for record in self.parse_file(input_path):
                out_file.write(record.to_csv_row() + "\n")

    @staticmethod
    def _get_csv_header() -> str:
        """Return CSV header matching the original format"""
        return ";".join(CSV_HEADER) + "\n"
