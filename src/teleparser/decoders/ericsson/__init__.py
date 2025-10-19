from .voz import EricssonVoz
from .ber import BerDecoder
from .ber_optimized import BerDecoderOptimized

# from .ber_two_phase import BerDecoderTwoPhase
from .volte import EricssonVolte
from .volte_final import EricssonVolteFinal
from teleparser.buffer import BufferManager, MemoryBufferManager


def ericsson_voz_decoder(buffer_manager):
    """Original stream-based decoder (legacy)."""
    return BerDecoder(EricssonVoz, buffer_manager)


def ericsson_voz_decoder_optimized(buffer_manager):
    """Optimized memory-based decoder using memoryview.

    This decoder reads the entire file into memory once and uses memoryview
    for efficient byte access, eliminating repetitive disk I/O operations.
    Significantly faster for files that fit in memory.
    """
    # Convert BufferManager to MemoryBufferManager if needed
    if isinstance(buffer_manager, BufferManager):
        memory_buffer = MemoryBufferManager(buffer_manager.file_path)
    else:
        memory_buffer = buffer_manager
    return BerDecoderOptimized(EricssonVoz, memory_buffer)


# def ericsson_voz_decoder_two_phase(buffer_manager):
#     """Two-phase decoder for Ericsson VOZ."""
#     # Convert BufferManager to MemoryBufferManager if needed
#     if isinstance(buffer_manager, BufferManager):
#         memory_buffer = MemoryBufferManager(buffer_manager.file_path)
#     else:
#         memory_buffer = buffer_manager
#     return BerDecoderTwoPhase(EricssonVoz, memory_buffer)


def ericsson_volte_decoder(buffer_manager):
    return EricssonVolte(buffer_manager)


def ericsson_volte_decoder_optimized(buffer_manager):
    return EricssonVolteFinal(buffer_manager)
