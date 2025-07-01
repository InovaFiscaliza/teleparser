from .voz import EricssonVoz
from .ber import BerDecoder


def ericsson_voz_decoder():
    return BerDecoder(EricssonVoz)
