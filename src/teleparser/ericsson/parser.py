from collections import UserDict
from typing import Mapping
from . import modules

UNKNOWNS_TAGS = {47: modules.RoamingCallForwarding}


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
        elif self._is_tag_unknown(tag_number, schema):
            self.name = None
            self.value = None
            self.schema = {}
            return
        else:
            tag_mapping = schema[tag_number]

        if isinstance(tag_mapping["type"], dict):
            self.name = tag_mapping["tag"]
            self.value = tag_mapping["name"]
            self.schema = tag_mapping["type"]
        else:
            self.name = tag_mapping["name"]
            self.value = getattr(tag_mapping["type"](value), "value")
            self.schema = {}

    def _is_tag_unknown(self, tag_number: int, schema: Mapping) -> bool:
        return tag_number not in schema and UNKNOWNS_TAGS.get(tag_number) == schema
