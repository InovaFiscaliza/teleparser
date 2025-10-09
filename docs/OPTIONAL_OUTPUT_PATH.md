# Optional Output Path Feature

## Overview

The `teleparser` application now supports optional output paths. When no output directory is specified, the application processes CDR files and returns results in memory without saving to disk, while still maintaining comprehensive logging.

## Key Changes

### 1. Logging Strategy

**When `output_path` is specified:**
- Logs are saved to: `{output_path}/logs/teleparser_YYYYMMDD_HHMMSS.log`

**When `output_path` is `None`:**
- Logs are saved to: `~/.local/share/teleparser/logs/teleparser_YYYYMMDD_HHMMSS.log`
- This follows the XDG Base Directory specification for Linux/Ubuntu
- Your logs location: `/home/ronaldo/.local/share/teleparser/logs/`

### 2. Modified Function Signatures

All functions now have `output_path` defaulting to `None` and support `max_count`:

```python
# main.py
def setup_logging(output_path: Path | None, log_level: int = logging.INFO)

class CDRFileManager:
    def __init__(
        self, 
        input_path: Path, 
        output_path: Path | None, 
        cdr_type: str, 
        reprocess: bool,
        max_count: int | None = None
    )

def decode_file(file_path: Path, decoder, output_path: Path | None = None)

def process_single_file(file_path, decoder, output_path=None)

def main(
    input_path: Path, 
    output_path: Path | None = None, 
    ...,
    max_count: int | None = None
)
```

### 3. Behavior Changes

#### File Processing
- **With output_path**: Parquet files are saved to disk
- **Without output_path**: DataFrames are returned in the results dict (key: `"dataframe"`)

#### Reprocessing Logic
- **With output_path**: Skips files that already have `.parquet` output (unless `--reprocessar` flag)
- **Without output_path**: Processes all files (no skip logic)

#### ZIP Extraction
- **With output_path**: Temporary extraction to `{output_path}/temp_extracted/`
- **Without output_path**: Temporary extraction to `/tmp/teleparser_temp_extracted/`

### 4. CLI Usage

The `saída` parameter is now an **optional flag** instead of a positional argument:

```bash
# Process and save to disk
teleparser input_dir --saida output_dir

# Process in memory only (no disk output)
teleparser input_dir

# Short form
teleparser input_dir -s output_dir

# Limit number of files to process (useful for testing)
teleparser input_dir --max-arquivos 10
teleparser input_dir -m 5

# Combined options
teleparser input_dir -s output_dir -t ericsson_volte -n 4 --log DEBUG -m 100
```

### 5. Return Values

When `output_path=None`, the `decode_file` method returns:

```python
{
    "file": Path("..."),
    "records": 1234,
    "status": "success",
    "dataframe": pd.DataFrame(...)  # Only present when output_path=None
}
```

When `output_path` is specified, `"dataframe"` is `None` (to save memory).

## Use Cases

### 0. Testing & Quick Validation
Process only a few files for testing:

```bash
# Test with just 5 files
teleparser input_dir -m 5 --log DEBUG

# Test 10 files and save output
teleparser input_dir -s output_dir -m 10
```

### 1. Database Integration
Process CDR files and insert directly into a database without intermediate file storage:

```python
from pathlib import Path
from teleparser.main import CDRFileManager

manager = CDRFileManager(
    input_path=Path("data/cdrs/"),
    output_path=None,  # No disk output
    cdr_type="ericsson_voz",
    reprocess=False
)

results = manager.decode_files_sequential()

for result in results:
    if result["status"] == "success":
        df = result["dataframe"]
        # Insert df into database
        df.to_sql("cdr_records", engine, if_exists="append")
```

### 2. Data Pipeline Integration
Stream processing for ETL pipelines:

```python
from teleparser.main import main

# Process without saving
main(
    input_path=Path("input/"),
    output_path=None,
    cdr_type="ericsson_volte",
    workers=4
)
```

### 3. Testing & Development
Quick data exploration without cluttering filesystem:

```bash
teleparser test_data/ --log DEBUG
# Results processed, logs in ~/.local/share/teleparser/logs/
```

## Log File Management

Logs accumulate in the logs directory. Consider implementing log rotation:

```bash
# View recent logs
ls -lht ~/.local/share/teleparser/logs/

# Clean old logs (older than 30 days)
find ~/.local/share/teleparser/logs/ -name "*.log" -mtime +30 -delete

# Check log size
du -sh ~/.local/share/teleparser/logs/
```

## Migration Notes

### Breaking Changes
- CLI: `saída` changed from positional argument to optional flag (`--saida` or `-s`)
- Old: `teleparser input_dir output_dir`
- New: `teleparser input_dir --saida output_dir` or `teleparser input_dir -s output_dir`

### Backward Compatibility
All existing code using `output_path` explicitly will continue to work unchanged.

## Technical Details

### XDG Base Directory Specification
The XDG Base Directory spec defines standard locations for user-specific data:
- **Data**: `~/.local/share/` - User-specific data files
- **Cache**: `~/.cache/` - User-specific non-essential data
- **Config**: `~/.config/` - User-specific configuration files

We use `~/.local/share/teleparser/logs/` for persistent application logs.

### Memory Considerations
When processing without output_path:
- DataFrames are kept in memory in the results list
- For large batch processing, consider processing in smaller chunks
- Monitor memory usage with large files

### Temporary Files
ZIP extraction temporary directories are automatically cleaned up via `manager.cleanup()`.
