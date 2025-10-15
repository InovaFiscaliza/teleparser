#!/usr/bin/env python3
"""Comprehensive benchmarking script for EricssonVolte decoder optimizations.

This script compares the performance of different EricssonVolte decoder implementations:
1. Original decoder
2. Pre-compiled AVP tables
3. Memory pooled decoder
4. Parallel block processing
5. Two-phase processing
6. Vectorized block detection
7. Full optimized decoder
"""

import sys
import time
import gc
import tracemalloc
from pathlib import Path
from statistics import mean, median, stdev
from dataclasses import dataclass, asdict
from typing import List, Dict, Any, Callable
import tempfile
import gzip
import json

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from teleparser.buffer import MemoryBufferManager
from teleparser.decoders.ericsson.volte import EricssonVolte

# Import optimized decoders
try:
    from teleparser.decoders.ericsson.volte_optimized import EricssonVolteOptimized
    HAS_OPTIMIZED = True
except ImportError as e:
    print(f"Warning: Optimized decoder not available: {e}")
    HAS_OPTIMIZED = False
    
try:
    from teleparser.decoders.ericsson.volte_pooled import EricssonVoltePooled
    HAS_POOLED = True
except ImportError as e:
    print(f"Warning: Pooled decoder not available: {e}")
    HAS_POOLED = False
    
try:
    from teleparser.decoders.ericsson.volte_parallel import EricssonVolteParallel
    HAS_PARALLEL = True
except ImportError as e:
    print(f"Warning: Parallel decoder not available: {e}")
    HAS_PARALLEL = False
    
try:
    from teleparser.decoders.ericsson.volte_two_phase import EricssonVolteTwoPhase
    HAS_TWO_PHASE = True
except ImportError as e:
    print(f"Warning: Two-phase decoder not available: {e}")
    HAS_TWO_PHASE = False
    
try:
    from teleparser.decoders.ericsson.volte_final import EricssonVolteFinal
    HAS_FINAL = True
except ImportError as e:
    print(f"Warning: Final optimized decoder not available: {e}")
    HAS_FINAL = False


@dataclass
class BenchmarkResult:
    """Results from a single benchmark run."""
    decoder_name: str
    file_size: int
    records_parsed: int
    parse_time: float
    memory_peak: int
    memory_current: int
    records_per_second: float
    mb_per_second: float
    
    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


class VoLTEBenchmarkRunner:
    """Runs performance benchmarks on EricssonVolte decoders."""
    
    def __init__(self, n_runs: int = 5, warmup_runs: int = 1):
        self.n_runs = n_runs
        self.warmup_runs = warmup_runs
    
    def create_synthetic_volte_data(self, size_kb: int) -> Path:
        """Create synthetic VoLTE Diameter data for benchmarking."""
        
        # Build AVPs first to calculate correct total length
        avps = (
            # Session-Id AVP (263)
            b'\x00\x00\x01\x07'      # AVP Code: Session-Id (263)
            b'\x40\x00\x00\x28'      # Flags (M) + Length (40)
            b'test-session-id-123456789012345678\x00\x00'  # Value (32 bytes + padding)
            
            # Origin-Host AVP (264)
            b'\x00\x00\x01\x08'      # AVP Code: Origin-Host (264)
            b'\x40\x00\x00\x18'      # Flags (M) + Length (24)
            b'scscf.ims.example.com\x00'  # Value (20 bytes + padding)
            
            # Accounting-Record-Type AVP (480) - START
            b'\x00\x00\x01\xe0'      # AVP Code: Accounting-Record-Type (480)
            b'\x40\x00\x00\x0c'      # Flags (M) + Length (12)
            b'\x00\x00\x00\x02'      # Value: START (2)
            
            # Accounting-Record-Number AVP (485)
            b'\x00\x00\x01\xe5'      # AVP Code: Accounting-Record-Number (485)
            b'\x40\x00\x00\x0c'      # Flags (M) + Length (12)
            b'\x00\x00\x00\x01'      # Value: 1
            
            # Service-Context-Id AVP (461)
            b'\x00\x00\x01\xcd'      # AVP Code: Service-Context-Id (461)
            b'\x40\x00\x00\x14'      # Flags (M) + Length (20)
            b'ims-charging\x00\x00\x00'  # Value (12 bytes + padding)
        )
        
        # Calculate total message length (header + AVPs)
        total_length = 20 + len(avps)  # 20-byte header + AVPs
        length_bytes = total_length.to_bytes(3, 'big')
        
        # Create complete Diameter message
        # 2-byte prefix + 20-byte Diameter Header + AVPs
        basic_diameter_message = (
            # 2-byte prefix (expected by slice_next_block)
            b'\x00\x00'
            
            # Diameter Header: Version=1, Length=calculated, Command=271 (ACR), App-ID=4
            b'\x01' + length_bytes +      # Version (1) + Length (3 bytes)
            b'\x80\x00\x01\x0f'           # Flags + Command Code (271 = ACR)
            b'\x00\x00\x00\x04'           # Application-ID (4 = Diameter Credit Control)
            b'\x12\x34\x56\x78'           # Hop-by-Hop ID
            b'\x87\x65\x43\x21'           # End-to-End ID
        ) + avps
        
        target_size = size_kb * 1024
        messages_needed = target_size // len(basic_diameter_message) + 1
        
        # Create multiple separate messages (not just repeated data)
        # This ensures we have multiple blocks for parallel processing
        test_data = b''
        for i in range(messages_needed):
            if len(test_data) >= target_size:
                break
            # Vary the hop-by-hop ID for each message to make them distinct
            message = basic_diameter_message[:-8] + (0x12345678 + i).to_bytes(4, 'big') + b'\x87\x65\x43\x21'
            test_data += message
        
        test_data = test_data[:target_size]  # Truncate to exact size
        
        # Create temporary compressed file
        temp_file = tempfile.NamedTemporaryFile(suffix='.gz', delete=False)
        temp_path = Path(temp_file.name)
        
        with gzip.open(temp_path, 'wb') as f:
            f.write(test_data)
        
        return temp_path
    
    def benchmark_decoder(
        self, 
        decoder_factory: Callable,
        decoder_name: str, 
        test_file: Path,
        show_progress: bool = False
    ) -> BenchmarkResult:
        """Benchmark a single decoder implementation."""
        
        file_size = test_file.stat().st_size
        times = []
        memory_peaks = []
        record_counts = []
        
        # Warmup runs
        for _ in range(self.warmup_runs):
            try:
                buffer = MemoryBufferManager(test_file)
                decoder = decoder_factory(buffer)
                list(decoder.process(show_progress=False))
                del decoder, buffer
                gc.collect()
            except Exception as e:
                print(f"Warmup failed for {decoder_name}: {e}")
        
        # Actual benchmark runs
        for run_idx in range(self.n_runs):
            # Start memory tracking
            tracemalloc.start()
            
            try:
                start_time = time.perf_counter()
                
                buffer = MemoryBufferManager(test_file)
                decoder = decoder_factory(buffer)
                
                if show_progress and run_idx == 0:
                    records = decoder.process(show_progress=True)
                else:
                    records = decoder.process(show_progress=False)
                
                end_time = time.perf_counter()
                
                # Get memory usage
                current, peak = tracemalloc.get_traced_memory()
                tracemalloc.stop()
                
                parse_time = end_time - start_time
                times.append(parse_time)
                memory_peaks.append(peak)
                record_counts.append(len(records))
                
                del decoder, buffer, records
                gc.collect()
                
            except Exception as e:
                tracemalloc.stop()
                print(f"Benchmark failed for {decoder_name} run {run_idx}: {e}")
                continue
        
        if not times:
            raise RuntimeError(f"All benchmark runs failed for {decoder_name}")
        
        # Calculate statistics
        avg_time = mean(times)
        avg_peak_memory = mean(memory_peaks)
        avg_records = mean(record_counts)
        
        records_per_sec = avg_records / avg_time if avg_time > 0 else 0
        mb_per_sec = (file_size / 1024 / 1024) / avg_time if avg_time > 0 else 0
        
        return BenchmarkResult(
            decoder_name=decoder_name,
            file_size=file_size,
            records_parsed=int(avg_records),
            parse_time=avg_time,
            memory_peak=int(avg_peak_memory),
            memory_current=0,  # Not available with tracemalloc
            records_per_second=records_per_sec,
            mb_per_second=mb_per_sec
        )
    
    def run_comprehensive_benchmark(
        self, 
        decoder_configs: List[tuple],
        test_files: List[Path] = None,
        synthetic_sizes: List[int] = None
    ) -> List[BenchmarkResult]:
        """Run comprehensive benchmark across all decoders and test cases."""
        
        if test_files is None:
            test_files = []
        
        if synthetic_sizes is None:
            synthetic_sizes = [100, 500, 1000]  # KB
        
        all_results = []
        
        # Test with synthetic data
        print("\n" + "="*80)
        print("VOLTE DECODER OPTIMIZATION BENCHMARK")
        print("="*80)
        
        for size_kb in synthetic_sizes:
            print(f"\n--- Testing with {size_kb}KB synthetic data ---")
            
            # Create synthetic test file
            test_file = self.create_synthetic_volte_data(size_kb)
            
            try:
                for decoder_name, decoder_factory in decoder_configs:
                    print(f"Benchmarking {decoder_name}...")
                    try:
                        result = self.benchmark_decoder(
                            decoder_factory, decoder_name, test_file, show_progress=(size_kb == synthetic_sizes[0])
                        )
                        all_results.append(result)
                        
                        print(f"  {result.records_per_second:.0f} rec/s | "
                              f"{result.mb_per_second:.2f} MB/s | "
                              f"{result.memory_peak/1024/1024:.1f} MB peak")
                              
                    except Exception as e:
                        print(f"  ERROR: {e}")
                
            finally:
                # Clean up synthetic file
                test_file.unlink(missing_ok=True)
        
        # Test with real files if provided
        for test_file in test_files:
            print(f"\n--- Testing with real file: {test_file.name} ---")
            
            for decoder_name, decoder_factory in decoder_configs:
                print(f"Benchmarking {decoder_name}...")
                try:
                    result = self.benchmark_decoder(decoder_factory, decoder_name, test_file)
                    all_results.append(result)
                    
                    print(f"  {result.records_per_second:.0f} rec/s | "
                          f"{result.mb_per_second:.2f} MB/s | "
                          f"{result.memory_peak/1024/1024:.1f} MB peak")
                          
                except Exception as e:
                    print(f"  ERROR: {e}")
        
        return all_results
    
    def print_comparison_table(self, results: List[BenchmarkResult]):
        """Print a comparison table of all benchmark results."""
        print("\n" + "="*80)
        print("PERFORMANCE COMPARISON SUMMARY")
        print("="*80)
        
        # Group results by file size
        grouped = {}
        for result in results:
            size_key = f"{result.file_size // 1024}KB"
            if size_key not in grouped:
                grouped[size_key] = []
            grouped[size_key].append(result)
        
        for size_key, size_results in grouped.items():
            print(f"\n--- {size_key} Files ---")
            print(f"{'Decoder':<25} {'Rec/s':<10} {'MB/s':<8} {'Mem(MB)':<10} {'Speedup':<10}")
            print("-" * 70)
            
            # Calculate speedup relative to original
            original_rps = next((r.records_per_second for r in size_results if 'Original' in r.decoder_name), 1)
            
            for result in size_results:
                speedup = result.records_per_second / original_rps if original_rps > 0 else 0
                print(f"{result.decoder_name:<25} {result.records_per_second:<10.0f} "
                      f"{result.mb_per_second:<8.2f} {result.memory_peak/1024/1024:<10.1f} "
                      f"{speedup:<10.2f}x")
    
    def save_results(self, results: List[BenchmarkResult], output_file: str):
        """Save benchmark results to JSON file."""
        results_dict = [result.to_dict() for result in results]
        
        with open(output_file, 'w') as f:
            json.dump({
                'timestamp': time.time(),
                'results': results_dict
            }, f, indent=2)
        
        print(f"\nResults saved to: {output_file}")


def main():
    """Main benchmark execution function."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Benchmark EricssonVolte decoder optimizations")
    parser.add_argument('--sizes', nargs='+', type=int, default=[100, 500, 1000],
                       help="Synthetic data sizes in KB")
    parser.add_argument('--files', nargs='*', type=Path, default=[],
                       help="Real test files to benchmark")
    parser.add_argument('--runs', type=int, default=5,
                       help="Number of benchmark runs per configuration")
    parser.add_argument('--output', type=str, default='volte_benchmark_results.json',
                       help="Output file for results")
    
    args = parser.parse_args()
    
    # Initialize benchmark runner
    runner = VoLTEBenchmarkRunner(n_runs=args.runs)
    
    # Define decoder configurations
    decoder_configs = [
        ("Original", lambda buffer: EricssonVolte(buffer)),
    ]
    
    if HAS_OPTIMIZED:
        decoder_configs.append(
            ("Pre-compiled AVP", lambda buffer: EricssonVolteOptimized(buffer))
        )
        
    if HAS_POOLED:
        decoder_configs.append(
            ("Memory Pooled", lambda buffer: EricssonVoltePooled(buffer))
        )
        
    if HAS_PARALLEL:
        decoder_configs.extend([
            ("Parallel (2 workers)", lambda buffer: EricssonVolteParallel(buffer, n_workers=2)),
            ("Parallel (4 workers)", lambda buffer: EricssonVolteParallel(buffer, n_workers=4)),
        ])
        
    if HAS_TWO_PHASE:
        decoder_configs.extend([
            ("Two-Phase (1 worker)", lambda buffer: EricssonVolteTwoPhase(buffer, n_workers=1)),
            ("Two-Phase (2 workers)", lambda buffer: EricssonVolteTwoPhase(buffer, n_workers=2)),
            ("Two-Phase (4 workers)", lambda buffer: EricssonVolteTwoPhase(buffer, n_workers=4)),
        ])
        
    if HAS_FINAL:
        decoder_configs.append(
            ("Final Optimized", lambda buffer: EricssonVolteFinal(buffer))
        )
    
    # Run benchmarks
    results = runner.run_comprehensive_benchmark(
        decoder_configs=decoder_configs,
        test_files=args.files,
        synthetic_sizes=args.sizes
    )
    
    # Print results
    runner.print_comparison_table(results)
    
    # Save results
    runner.save_results(results, args.output)


if __name__ == "__main__":
    main()