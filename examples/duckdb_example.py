#!/usr/bin/env python3
"""
Example: Using teleparser with DuckDB without pandas dependency

This example demonstrates how to process CDR files and query them
directly with DuckDB using Python dictionaries, without needing
pandas as a dependency.
"""

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
    Process a single CDR file and return the blocks (list of dictionaries).
    
    Args:
        file_path: Path to the CDR .gz file
        
    Returns:
        list: List of dictionaries containing CDR records
    """
    result = CDRFileManager.decode_file(
        file_path=file_path,
        decoder=ericsson_voz_decoder,
        output_path=None,  # Don't save to disk
        show_progress=True,
    )
    
    if result["status"] == "failed":
        raise RuntimeError(f"Failed to process file: {result.get('error')}")
    
    return result["blocks"]


def query_cdr_with_duckdb(blocks: list):
    """
    Query the blocks using DuckDB without loading into pandas.
    
    Args:
        blocks: List of dictionaries containing CDR records
        
    Returns:
        DuckDB result set
    """
    # Create an in-memory DuckDB connection
    conn = duckdb.connect(":memory:")
    
    # DuckDB can directly query Python lists of dictionaries
    result = conn.execute(
        """
        SELECT 
            CallModule,
            COUNT(*) as call_count,
            COUNT(DISTINCT "callingSubscriberIMSI.msin") as unique_callers
        FROM blocks
        WHERE CallModule IS NOT NULL
        GROUP BY CallModule
        ORDER BY call_count DESC
    """
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
    blocks = process_cdr_to_memory(cdr_file)
    
    print(f"Records loaded: {len(blocks):,}\n")
    
    # Query the data
    print("Querying call statistics by module...\n")
    results = query_cdr_with_duckdb(blocks)
    
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
    blocks = process_cdr_to_memory(cdr_file)
    
    # Create DuckDB connection
    conn = duckdb.connect(":memory:")
    
    # More complex query with multiple aggregations
    # DuckDB can directly query the blocks variable
    query = """
    SELECT 
        "callingSubscriberIMSI.pais" as country,
        COUNT(*) as total_calls,
        COUNT(DISTINCT "callingSubscriberIMSI.msin") as unique_subscribers,
        AVG(CAST(chargeableDuration AS INTEGER)) as avg_duration_seconds,
        SUM(CASE WHEN disconnectingParty = 'callingPartyRelease' THEN 1 ELSE 0 END) as caller_initiated,
        SUM(CASE WHEN disconnectingParty = 'networkRelease' THEN 1 ELSE 0 END) as network_released
    FROM blocks
    WHERE "callingSubscriberIMSI.pais" IS NOT NULL
    GROUP BY "callingSubscriberIMSI.pais"
    ORDER BY total_calls DESC
    LIMIT 10
    """
    
    results = conn.execute(query).fetchall()
    conn.close()
    
    print("Top Countries by Call Volume:")
    print("\nCountry | Calls | Subscribers | Avg Duration | Caller End | Network End")
    print("-" * 80)
    for row in results:
        print(
            f"{row[0]:<8} | {row[1]:>5} | {row[2]:>11} | {row[3]:>12.1f}s | {row[4]:>10} | {row[5]:>11}"
        )


def example_query_sample_data():
    """Example 3: Querying sample data directly"""
    print("\n=== Example 3: Query Sample Data ===\n")
    
    # Simulate processing blocks
    sample_blocks = [
        {"CallModule": "transit", "records": 100, "country": "BR"},
        {"CallModule": "mobile", "records": 200, "country": "BR"},
        {"CallModule": "transit", "records": 150, "country": "US"},
    ]
    
    print(f"Created {len(sample_blocks)} sample records\n")
    
    # Query it directly with DuckDB
    conn = duckdb.connect(":memory:")
    
    results = conn.execute(
        """
        SELECT CallModule, SUM(records) as total_records
        FROM sample_blocks
        GROUP BY CallModule
    """
    ).fetchall()
    
    conn.close()
    
    print("Aggregated Results:")
    for row in results:
        print(f"  {row[0]}: {row[1]} records")


def example_export_to_parquet():
    """Example 4: Export query results to Parquet"""
    print("\n=== Example 4: Export to Parquet ===\n")
    
    sample_blocks = [
        {"id": 1, "value": "test1", "score": 100},
        {"id": 2, "value": "test2", "score": 200},
        {"id": 3, "value": "test3", "score": 150},
    ]
    
    print("Processing sample data in memory")
    
    # Do some processing/validation
    conn = duckdb.connect(":memory:")
    count = conn.execute(
        "SELECT COUNT(*) FROM sample_blocks"
    ).fetchone()[0]
    
    print(f"Validated: {count} records\n")
    
    # Export aggregated results to Parquet
    output_path = Path("/tmp/teleparser_example.parquet")
    conn.execute(
        f"""
        COPY (
            SELECT value, SUM(score) as total_score
            FROM sample_blocks
            GROUP BY value
        ) TO '{output_path}' (FORMAT PARQUET)
        """
    )
    conn.close()
    
    print(f"Exported results to: {output_path}")
    print(f"File size: {output_path.stat().st_size} bytes")
    
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

    example_query_sample_data()
    example_export_to_parquet()

    print("\n" + "=" * 60)
    print("Examples complete!")
    print("\nKey Benefits:")
    print("  ✓ No pandas dependency required")
    print("  ✓ Process CDR files entirely in memory")
    print("  ✓ Query Python dictionaries directly with SQL using DuckDB")
    print("  ✓ Save to disk only when needed")
    print("  ✓ Export to Parquet, CSV, or other formats")
    print("  ✓ Efficient for streaming/pipeline architectures")
