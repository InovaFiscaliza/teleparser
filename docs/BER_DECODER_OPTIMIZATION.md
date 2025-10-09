# BER Decoder Optimization

## Overview

The BER (Basic Encoding Rules) decoder has been optimized to eliminate repetitive disk I/O operations by reading the entire file into memory once and using Python's `memoryview` for efficient byte-level access.

## Problem

The original `BerDecoder` class made multiple calls to `stream.read()` throughout the decoding process:
- Reading tags (1+ bytes per tag)
- Reading lengths (1+ bytes per length field)
- Reading values (variable bytes per value)
- Recursive calls for constructed types

For a typical CDR file with thousands of records, this resulted in tens of thousands of small disk reads, creating significant I/O overhead.

## Solution

### Architecture

The optimization introduces two new components:

#### 1. **MemoryBufferManager** (`buffer.py`)
A new buffer manager that:
- Reads the entire gzipped file into memory in one operation
- Provides a `memoryview` object for zero-copy byte access
- Maintains backward compatibility with the existing `BufferManager` interface

#### 2. **BerDecoderOptimized** (`ber_optimized.py`)
An optimized decoder that:
- Operates on `memoryview` objects instead of streams
- Uses integer indexing instead of `read()` calls
- Tracks position explicitly through the decode process
- Eliminates intermediate `BytesIO` object creation for constructed types

### Key Optimizations

1. **Single File Read**: The entire decompressed file is loaded into memory once
2. **Memoryview Access**: Direct byte access without copying using `memoryview`
3. **Position Tracking**: Explicit position management instead of stream seeking
4. **Reduced Allocations**: Fewer temporary object creations during parsing

### Performance Benefits

- **Eliminated I/O Overhead**: No repetitive disk reads
- **Better CPU Cache Utilization**: Sequential memory access patterns
- **Reduced System Calls**: Single `read()` vs. thousands
- **Memory Efficiency**: `memoryview` provides zero-copy slicing

## Usage

### Basic Usage

```python
from pathlib import Path
from teleparser.buffer import MemoryBufferManager
from teleparser.decoders.ericsson import ericsson_voz_decoder_optimized

# Create memory buffer manager
buffer = MemoryBufferManager(Path("path/to/file.gz"))

# Create optimized decoder
decoder = ericsson_voz_decoder_optimized(buffer)

# Process file
results = decoder.process()
```

### Using with CLI

The optimized decoder is available through the CLI with the type `ericsson_voz_optimized`:

```bash
# Using optimized decoder
teleparser entrada.gz --saida ./output --tipo ericsson_voz_optimized

# Using original decoder (for comparison or troubleshooting)
teleparser entrada.gz --saida ./output --tipo ericsson_voz
```

### Using Programmatically

```python
from pathlib import Path
from teleparser.main import main

# Use optimized decoder
results = main(
    input_path=Path("data/input"),
    output_path=Path("data/output"),
    cdr_type="ericsson_voz_optimized",  # Use optimized version
    workers=4,
    reprocess=False
)
```

## Implementation Details

### Memory Layout

```
Original Approach:
┌─────────────┐
│  File.gz    │  ──read()──> ┌──────────┐
└─────────────┘              │ GzipFile │ ──read(n)──> [Multiple small reads]
                              └──────────┘

Optimized Approach:
┌─────────────┐
│  File.gz    │  ──read()──> ┌──────────┐  ──read()──>  ┌─────────────────┐
└─────────────┘              │ GzipFile │               │  bytes (memory) │
                              └──────────┘               └─────────────────┘
                                                                  │
                                                                  v
                                                          ┌─────────────────┐
                                                          │   memoryview    │ ──[pos:pos+n]──> [Zero-copy access]
                                                          └─────────────────┘
```

### Method Signatures

#### Original BerDecoder
```python
def decode(self, stream: BerStream, offset: int = 0, depth: int = 0, schema: dict | None = None)
    # stream.read() calls throughout
```

#### Optimized BerDecoderOptimized
```python
def decode(self, data: memoryview, position: int, depth: int = 0, schema: dict | None = None) -> Tuple[Optional[dict], int]
    # data[position:position+n] access patterns
    # Returns (decoded_data, bytes_consumed)
```

### Error Handling

The optimized decoder includes bounds checking to prevent buffer overruns:

```python
# Check if we have enough data
if position + length > len(data):
    raise ValueError(f"Unexpected end of data: need {length} bytes at position {position}")
```

## Trade-offs

### Advantages
✅ Significantly faster for files that fit in memory  
✅ Simpler state management with explicit positioning  
✅ Better performance for sequential processing  
✅ Reduced system call overhead  

### Considerations
⚠️ Requires sufficient RAM for the entire decompressed file  
⚠️ Not suitable for extremely large files (>available RAM)  
⚠️ Initial load time includes full decompression  

## Backward Compatibility

The original `BerDecoder` remains available and unchanged:
- Use `ericsson_voz` for the original stream-based decoder
- Use `ericsson_voz_optimized` for the new memory-based decoder

Both decoders produce identical output.

## Benchmarking

To compare performance:

```bash
# Test with original decoder
time teleparser data/test.gz --saida /tmp/out1 --tipo ericsson_voz

# Test with optimized decoder
time teleparser data/test.gz --saida /tmp/out2 --tipo ericsson_voz_optimized

# Verify outputs are identical
diff -r /tmp/out1 /tmp/out2
```

## Future Enhancements

Potential improvements:
1. **Lazy loading**: Load file chunks on-demand for large files
2. **Memory mapping**: Use `mmap` for OS-level memory management
3. **Parallel decoding**: Process multiple records simultaneously
4. **Adaptive strategy**: Automatically choose decoder based on file size

## Technical Notes

### Why memoryview?

`memoryview` provides:
- Zero-copy slicing: `data[start:end]` doesn't copy bytes
- Efficient indexing: `data[i]` returns integer directly
- Memory efficiency: No duplicate buffers created
- Compatible with bytes: Can convert to bytes when needed

Example:
```python
# With bytes - creates copies
data = b"hello world"
slice1 = data[0:5]  # Copies 5 bytes
slice2 = data[6:11]  # Copies 5 bytes

# With memoryview - no copies
mv = memoryview(data)
slice1 = mv[0:5]  # No copy, just offset tracking
slice2 = mv[6:11]  # No copy, just offset tracking
```

### Position Tracking

The optimized decoder explicitly tracks position:

```python
def parse_blocks(self):
    data = self.buffer_manager.get_memoryview()
    position = 0
    
    while position < len(data):
        result = self.decode(data, position)
        if result[0] is not None:
            record, bytes_read = result
            position += bytes_read  # Explicit position update
            yield record
```

## References

- [ASN.1 BER Encoding](https://luca.ntop.org/Teaching/Appunti/asn1.html)
- [Python memoryview](https://docs.python.org/3/library/stdtypes.html#memoryview)
- [Zero-copy techniques](https://en.wikipedia.org/wiki/Zero-copy)
