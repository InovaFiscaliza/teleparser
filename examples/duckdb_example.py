#!/usr/bin/env python3
"""
Example: Using teleparser with DuckDB without pandas dependency

This example demonstrates how to process CDR files and query them
directly with DuckDB using the in-memory CSV buffer, without needing
pandas as a dependency.
"""

import io
from pathlib import Path
from teleparser.main import CDRFileManager
from teleparser.decoders.ericsson import ericsson_voz_decoder

try:
    import duckdb
except ImportError:
    print("This example requires duckdb. Install it with: uv add duckdb")
    print("Or run: pip install duckdb")
    exit(1)


def process_cdr_to_memory(file_path: Path):
    """
    Process a single CDR file and return the in-memory CSV buffer.

    Args:
        file_path: Path to the CDR .gz file

    Returns:
        io.BytesIO: In-memory gzipped CSV buffer ready for reading
    """
    result = CDRFileManager.decode_file(
        file_path=file_path,
        decoder=ericsson_voz_decoder,
        output_path=None,  # Don't save to disk
        show_progress=True,
    )

    if result["status"] == "failed":
        raise RuntimeError(f"Failed to process file: {result.get('error')}")

    return result["buffer"]


def query_cdr_with_duckdb(csv_buffer: io.BytesIO):
    """
    Query the CSV buffer using DuckDB without loading into pandas.

    Args:
        csv_buffer: In-memory gzipped CSV buffer

    Returns:
        DuckDB result set
    """
    # Create an in-memory DuckDB connection
    conn = duckdb.connect(":memory:")

    # Reset buffer to start
    csv_buffer.seek(0)

    # Read directly from gzipped buffer
    # DuckDB can read gzipped CSV files directly from memory
    result = conn.execute(
        """
        SELECT 
            CallModule,
            COUNT(*) as call_count,
            COUNT(DISTINCT "callingSubscriberIMSI.msin") as unique_callers
        FROM read_blob(?, union_by_name=true, filename=true)
        WHERE CallModule IS NOT NULL
        GROUP BY CallModule
        ORDER BY call_count DESC
    """,
        [csv_buffer],
    ).fetchall()

    conn.close()
    return result


def example_basic_query():
    """Example 1: Basic query on a single file"""
    print("=== Example 1: Basic Query ===\n")

    # Process a single CDR file
    cdr_file = Path(
        "data/input/ericsson_voz/MSSSID.TTFILE00.202503211906578503.BACKUP.gz"
    )

    if not cdr_file.exists():
        print(f"File not found: {cdr_file}")
        print("Please update the path to point to an existing CDR file.")
        return

    print(f"Processing: {cdr_file.name}")
    buffer = process_cdr_to_memory(cdr_file)

    print(f"Buffer size: {buffer.getbuffer().nbytes:,} bytes\n")

    # Query the data
    print("Querying call statistics by module...\n")
    results = query_cdr_with_duckdb(buffer)

    print("Call Module | Count | Unique Callers")
    print("-" * 50)
    for row in results:
        print(f"{row[0]:<12} | {row[1]:>5} | {row[2]:>14}")


def example_advanced_query():
    """Example 2: More complex aggregations"""
    print("\n=== Example 2: Advanced Query ===\n")

    cdr_file = Path(
        "data/input/ericsson_voz/MSSSID.TTFILE00.202503211906578503.BACKUP.gz"
    )

    if not cdr_file.exists():
        print(f"File not found: {cdr_file}")
        return

    print(f"Processing: {cdr_file.name}")
    buffer = process_cdr_to_memory(cdr_file)

    # Create DuckDB connection
    conn = duckdb.connect(":memory:")
    buffer.seek(0)

    # More complex query with multiple aggregations
    query = """
    SELECT 
        "callingSubscriberIMSI.pais" as country,
        COUNT(*) as total_calls,
        COUNT(DISTINCT "callingSubscriberIMSI.msin") as unique_subscribers,
        AVG(CAST(chargeableDuration AS INTEGER)) as avg_duration_seconds,
        SUM(CASE WHEN disconnectingParty = 'callingPartyRelease' THEN 1 ELSE 0 END) as caller_initiated,
        SUM(CASE WHEN disconnectingParty = 'networkRelease' THEN 1 ELSE 0 END) as network_released
    FROM read_csv_auto(?, compression='gzip', header=true)
    WHERE "callingSubscriberIMSI.pais" IS NOT NULL
    GROUP BY "callingSubscriberIMSI.pais"
    ORDER BY total_calls DESC
    LIMIT 10
    """

    results = conn.execute(query, [buffer.getvalue()]).fetchall()
    conn.close()

    print("Top Countries by Call Volume:")
    print("\nCountry | Calls | Subscribers | Avg Duration | Caller End | Network End")
    print("-" * 80)
    for row in results:
        print(
            f"{row[0]:<8} | {row[1]:>5} | {row[2]:>11} | {row[3]:>12.1f}s | {row[4]:>10} | {row[5]:>11}"
        )


def example_create_buffer_manually():
    """Example 3: Creating a CSV buffer manually from blocks"""
    print("\n=== Example 3: Manual Buffer Creation ===\n")

    # Simulate processing blocks
    sample_blocks = [
        {"CallModule": "transit", "records": 100, "country": "BR"},
        {"CallModule": "mobile", "records": 200, "country": "BR"},
        {"CallModule": "transit", "records": 150, "country": "US"},
    ]

    # Create buffer manually
    buffer = CDRFileManager._create_csv_buffer(sample_blocks, fieldnames_set=None)

    print(f"Created buffer with {len(sample_blocks)} sample records")
    print(f"Buffer size: {buffer.getbuffer().nbytes} bytes\n")

    # Query it
    conn = duckdb.connect(":memory:")
    buffer.seek(0)

    results = conn.execute(
        """
        SELECT CallModule, SUM(records) as total_records
        FROM read_csv_auto(?, compression='gzip', header=true)
        GROUP BY CallModule
    """,
        [buffer.getvalue()],
    ).fetchall()

    conn.close()

    print("Aggregated Results:")
    for row in results:
        print(f"  {row[0]}: {row[1]} records")


def example_save_buffer_later():
    """Example 4: Process in memory, save to disk later if needed"""
    print("\n=== Example 4: Save Buffer Later ===\n")

    sample_blocks = [
        {"id": 1, "value": "test1"},
        {"id": 2, "value": "test2"},
    ]

    # Create buffer
    buffer = CDRFileManager._create_csv_buffer(sample_blocks)
    print("Created buffer in memory")

    # Do some processing/validation
    conn = duckdb.connect(":memory:")
    buffer.seek(0)
    count = conn.execute(
        "SELECT COUNT(*) FROM read_csv_auto(?, compression='gzip', header=true)",
        [buffer.getvalue()],
    ).fetchone()[0]
    conn.close()

    print(f"Validated: {count} records in buffer")

    # Decide to save to disk
    output_path = Path("/tmp/teleparser_example.csv.gz")
    CDRFileManager._save_buffer_to_disk(buffer, output_path)
    print(f"Saved buffer to: {output_path}")

    # Clean up
    if output_path.exists():
        output_path.unlink()
        print("Cleaned up example file")


if __name__ == "__main__":
    print("Teleparser + DuckDB Integration Examples")
    print("=" * 60)
    print()

    # Run examples
    try:
        example_basic_query()
    except Exception as e:
        print(f"Example 1 error: {e}")

    try:
        example_advanced_query()
    except Exception as e:
        print(f"Example 2 error: {e}")

    example_create_buffer_manually()
    example_save_buffer_later()

    print("\n" + "=" * 60)
    print("Examples complete!")
    print("\nKey Benefits:")
    print("  ✓ No pandas dependency required")
    print("  ✓ Process CDR files entirely in memory")
    print("  ✓ Query with SQL using DuckDB")
    print("  ✓ Save to disk only when needed")
    print("  ✓ Efficient for streaming/pipeline architectures")
