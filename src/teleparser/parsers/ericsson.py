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

