from teleparser.decoders.ericsson import primitives
import pytest


class TestOctetString:
    def test_octet_none(self):
        error_msg = "parsing octeto string 'NoneType' object has no attribute 'hex"
        with pytest.raises(primitives.OctetStringError):
            assert primitives.OctetString(None) == error_msg

    def test_octet_len_diff_size(self):
        error_msg = "Size parameter is bigger than octets length"
        with pytest.raises(primitives.OctetStringError):
            assert primitives.OctetString(octets=b"\x0a", size=3) == error_msg

    def test_octet_no_size(self):
        octet = primitives.OctetString(octets=b"\x0a", size=None)
        octet.string == "0A"

    @pytest.mark.parametrize(
        "test_id, octets, size, expected_error",
        [
            (
                "error_case_none_octets",
                None,
                None,
                primitives.OctetStringError,
            ),
            (
                "error_case_size_mismatch",
                b"\x0a",
                3,
                primitives.OctetStringError,
            ),
        ],
    )
    def test_octet_error_cases(self, test_id, octets, size, expected_error):
        with pytest.raises(expected_error):
            primitives.OctetString(octets, size)

    @pytest.mark.parametrize(
        "test_id, octets, size, expected_string",
        [
            (
                "happy_path_no_size",
                b"\x0a",
                None,
                "0A",
            ),
        ],
    )
    def test_octet_happy_path(self, test_id, octets, size, expected_string):
        octet = primitives.OctetString(octets, size)
        assert octet.string == expected_string


class TestUnsignedInt:
    @pytest.mark.parametrize(
        "test_id, octets, size, expected_value",
        [
            (
                "happy_path_single_octet",
                b"\x01",
                1,
                1,
            ),
            (
                "happy_path_multiple_octets",
                b"\x01\x02\x03",
                3,
                66051,
            ),
            (
                "edge_case_empty_octets",
                b"",
                0,
                0,
            ),
            ("happy_path_max_value_single_byte", b"\xff", 1, 255),
            ("happy_path_max_value_two_bytes", b"\xff\xff", 2, 65535),
        ],
    )
    def test_unsigned_int_happy_path(self, test_id, octets, size, expected_value):
        unsigned_int = primitives.UnsignedInt(octets, size)
        assert unsigned_int.octets == octets
        assert unsigned_int.value == expected_value

    @pytest.mark.parametrize(
        "test_id, octets, size, expected_error",
        [
            (
                "error_case_invalid_octets_type",
                "invalid",
                1,
                TypeError,
            ),
            (
                "error_case_invalid_size_type",
                b"\x01",
                "invalid",
                TypeError,
            ),
            (
                "error_case_size_mismatch",
                b"\x01",
                2,
                AssertionError,
            ),
        ],
    )
    def test_unsigned_int_error_cases(self, test_id, octets, size, expected_error):
        with pytest.raises(expected_error):
            primitives.UnsignedInt(octets, size)
