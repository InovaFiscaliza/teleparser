from .voz import EricssonVoz
from .ber import BerDecoder
from .volte import EricssonVolte


def ericsson_voz_decoder(buffer_manager):
    return BerDecoder(EricssonVoz, buffer_manager)


def ericsson_volte_decoder(buffer_manager):
    return EricssonVolte(buffer_manager)
