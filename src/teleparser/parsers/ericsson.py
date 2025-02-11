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
