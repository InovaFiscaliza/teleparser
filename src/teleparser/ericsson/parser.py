from collections import UserDict
from typing import Mapping
from . import modules

MAPPING_TYPES = (dict, UserDict)


class TlvVozEricsson:
    """Tag-Length-Value object for BER encoding for Ericsson Common Charging Output"""

    def __init__(
        self,
        tag_number: int,
        value: bytes,
        schema: Mapping = None,
    ):
        self.length = len(value)
        if schema is None:  # root
            tag_mapping = modules.CallDataRecord[tag_number]
        else:
            tag_mapping = schema[tag_number]
        if isinstance(tag_mapping["type"], MAPPING_TYPES):
            self.name = tag_mapping["tag"]
            self.value = tag_mapping["name"]
            self.schema = tag_mapping["type"]
        else:
            self.name = tag_mapping["name"]
            self.value = getattr(tag_mapping["type"](value), "value")
            self.schema = {}
