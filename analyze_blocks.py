#!/usr/bin/env python3
"""Analyze the block structure of synthetic VoLTE data."""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from teleparser.buffer import MemoryBufferManager
from teleparser.decoders.ericsson.volte_parallel import EricssonVolteParallel

# Import the benchmark data generator
sys.path.insert(0, str(Path(__file__).parent / "benchmarks"))
from volte_optimization_benchmark import VoLTEBenchmarkRunner

def analyze_synthetic_data(size_kb=500):
    """Analyze the block structure of synthetic data."""
    
    print(f"Analyzing {size_kb}KB synthetic VoLTE data...")
    
    # Create synthetic data
    runner = VoLTEBenchmarkRunner()
    test_file = runner.create_synthetic_volte_data(size_kb)
    
    try:
        # Analyze with parallel decoder
        buffer = MemoryBufferManager(test_file)
        decoder = EricssonVolteParallel(buffer, n_workers=4)
        
        # Get stats
        stats = decoder.get_stats()
        print(f"Total blocks: {stats['total_blocks']}")
        print(f"Workers: {stats['n_workers']}")
        print(f"Parallel enabled: {stats['parallel_enabled']}")
        print(f"Average block size: {stats['avg_block_size']:.1f} bytes")
        
        # Extract blocks to analyze sizes
        blocks = decoder.extract_all_blocks()
        print(f"\nBlock sizes:")
        for i, block in enumerate(blocks[:10]):  # Show first 10
            print(f"  Block {i}: {len(block)} bytes")
        if len(blocks) > 10:
            print(f"  ... and {len(blocks) - 10} more blocks")
            
        # Calculate optimal threshold for parallel processing
        total_work = sum(len(block) for block in blocks)
        print(f"\nTotal work: {total_work} bytes")
        print(f"Work per worker (4 workers): {total_work / 4:.1f} bytes")
        print(f"Parallel overhead threshold: {len(blocks) >= 8}")  # 2x workers
        
    finally:
        # Clean up
        test_file.unlink(missing_ok=True)

if __name__ == "__main__":
    analyze_synthetic_data(500)