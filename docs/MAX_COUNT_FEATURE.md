# Max Count Feature

## Overview

The `max_count` parameter allows you to limit the number of files processed in a single run. This is particularly useful for:

- **Testing**: Validate your processing pipeline with a small subset of files
- **Batch Processing**: Process files in controlled batches to manage memory usage
- **Development**: Quick iterations during development without processing all files
- **Resource Management**: Control processing load on the system

## Usage

### CLI Usage

```bash
# Process only 10 files
teleparser input_dir --max-arquivos 10
teleparser input_dir -m 10

# Combined with other options
teleparser input_dir -s output_dir -m 5 --log DEBUG
teleparser input_dir -m 20 -t ericsson_volte -n 4

# Process all files (default behavior)
teleparser input_dir
```

### Python API Usage

```python
from pathlib import Path
from teleparser.main import CDRFileManager, main

# Using CDRFileManager directly
manager = CDRFileManager(
    input_path=Path("data/cdrs/"),
    output_path=Path("output/"),
    cdr_type="ericsson_voz",
    reprocess=False,
    max_count=10  # Process only 10 files
)

results = manager.decode_files_sequential()
print(f"Processed {len(results)} files")

# Using main function
main(
    input_path=Path("data/cdrs/"),
    output_path=Path("output/"),
    cdr_type="ericsson_voz",
    workers=4,
    reprocess=False,
    log_level=logging.INFO,
    max_count=5  # Process only 5 files
)
```

## Implementation Details

### How It Works

1. **File Discovery**: All matching `.gz` and `.zip` files are discovered first
2. **Filtering**: If `reprocess=False` and `output_path` is set, already-processed files are filtered out
3. **Sorting**: Files are sorted by size (smallest first) for better load balancing
4. **Limiting**: If `max_count` is specified, only the first `max_count` files are selected
5. **Processing**: The limited set of files is then processed

### Order of Files

Files are processed in order of **file size** (smallest to largest). This ensures:
- Better load balancing in parallel processing
- Smaller files complete first, providing faster initial feedback
- More consistent progress bar behavior

If you need different ordering, you can modify the sorting logic in the `gz_files` property.

### Logging

When `max_count` is specified, you'll see a log entry like:

```
Limited to 10 files (max_count=10, found 150)
Found 10 GZ files to process
```

This shows:
- How many files will be processed (10)
- The `max_count` value set (10)
- How many files were originally found (150)

## Use Cases

### 1. Quick Testing

Before processing a large batch of files, test with a small subset:

```bash
# Test with 3 files first
teleparser test_data/ -m 3 --log DEBUG

# If successful, process more
teleparser test_data/ -m 50

# Finally process all
teleparser test_data/
```

### 2. Batch Processing for Memory Management

Process large datasets in controlled batches:

```python
from pathlib import Path
from teleparser.main import CDRFileManager
import logging

batch_size = 100
input_path = Path("data/large_dataset/")
output_path = Path("output/")

# First batch
manager = CDRFileManager(
    input_path=input_path,
    output_path=output_path,
    cdr_type="ericsson_voz",
    reprocess=False,
    max_count=batch_size
)
results = manager.decode_files_parallel(workers=4)
print(f"Batch 1: {len(results)} files processed")

# Second batch - files already processed are automatically skipped
manager2 = CDRFileManager(
    input_path=input_path,
    output_path=output_path,
    cdr_type="ericsson_voz",
    reprocess=False,
    max_count=batch_size
)
results2 = manager2.decode_files_parallel(workers=4)
print(f"Batch 2: {len(results2)} files processed")

# Continue until no more files...
```

### 3. Development Iterations

During development, iterate quickly with a small sample:

```bash
# Develop with just 5 files
teleparser dev_data/ -m 5 --log DEBUG

# Make code changes...

# Test again
teleparser dev_data/ -m 5 --log DEBUG
```

### 4. Database Testing

Test your database integration with limited files:

```python
from pathlib import Path
from teleparser.main import CDRFileManager
from sqlalchemy import create_engine

# Test with 5 files first
manager = CDRFileManager(
    input_path=Path("data/"),
    output_path=None,  # No disk output
    cdr_type="ericsson_voz",
    reprocess=False,
    max_count=5  # Just 5 files for testing
)

results = manager.decode_files_sequential()
engine = create_engine("postgresql://user:pass@localhost/testdb")

for result in results:
    if result["status"] == "success":
        df = result["dataframe"]
        df.to_sql("cdr_records", engine, if_exists="append")
        print(f"Inserted {len(df)} records")

# If successful, increase max_count or remove it
```

## Important Notes

### Default Behavior

- **Default**: `max_count=None` (process all files)
- **Minimum**: No minimum - you can set `max_count=1` to process just one file
- **Type**: Must be a positive integer or `None`

### Interaction with Reprocessing

The order of operations is:

1. Find all `.gz` and `.zip` files
2. Extract ZIP files (if any)
3. Filter already-processed files (if `reprocess=False` and `output_path` is set)
4. Sort by file size
5. **Apply `max_count` limit** (if specified)

This means:
- If you have 100 total files
- 30 are already processed (and `reprocess=False`)
- 70 remain to be processed
- With `max_count=10`, you'll process 10 of the remaining 70 files

### No File Found Warning

If `max_count` is set but no files match the criteria, you'll see:

```
Found 0 GZ files to process
```

And the program will complete without processing anything (this is not an error).

## Examples Summary

```bash
# Basic usage
teleparser data/ -m 10                          # Process 10 files
teleparser data/ -s output/ -m 5                # Process 5 files, save output
teleparser data/ -m 100 -n 8                    # Process 100 files with 8 workers

# Testing
teleparser test/ -m 1 --log DEBUG               # Process 1 file with debug logging
teleparser test/ -m 3 -t ericsson_volte         # Process 3 VoLTE files

# No output directory (memory only)
teleparser data/ -m 20                          # Process 20 files, no disk output
teleparser data/ -m 10 --log INFO               # Process 10, logs to ~/.local/share/teleparser/logs/

# Reprocessing with limit
teleparser data/ -s output/ -m 50 -r            # Reprocess 50 files (even if already done)
```

## Performance Considerations

### Memory Usage

When using `max_count` without `output_path`, all DataFrames are kept in memory:

```python
# This keeps all 100 DataFrames in memory
manager = CDRFileManager(
    input_path=Path("data/"),
    output_path=None,
    cdr_type="ericsson_voz",
    reprocess=False,
    max_count=100
)
```

Monitor memory usage and adjust `max_count` accordingly.

### Optimal Batch Sizes

For different scenarios:

- **Testing**: 1-10 files
- **Development**: 5-50 files
- **Small batches**: 50-100 files
- **Medium batches**: 100-500 files
- **Large batches**: 500-1000 files
- **Full processing**: No limit (default)

The optimal size depends on:
- Available RAM
- File sizes
- Number of CPU cores
- Whether you're saving to disk or keeping in memory
