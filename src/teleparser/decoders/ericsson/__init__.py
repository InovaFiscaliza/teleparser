from .voz import TlvVozEricsson
from .ber import BerDecoder


def ericsson_voz_decoder():
    return BerDecoder(TlvVozEricsson)
