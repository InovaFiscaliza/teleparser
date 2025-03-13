from teleparser.decoders.ericsson import primitives
import pytest


class TestOctet:

    def test_octet_none(self):
        error_msg = "parsing octeto string 'NoneType' object has no attribute 'hex"
        with pytest.raises(primitives.OctetStringError) as e_info:
            assert primitives.OctetString(None) == error_msg

    def test_octet_len_diff_size(self):
        error_msg = "Size parameter is bigger than octets length"
        with pytest.raises(primitives.OctetStringError) as e_info:
            assert primitives.OctetString(octets=b"\x0a", size=3) == error_msg

    def test_octet_no_size(self):
        octet = primitives.OctetString(octets=b"\x0a", size=None)
        octet.string == "0A"

    
  


