#!/usr/bin/env python3
"""Comprehensive benchmarking script for BER decoder optimizations.

This script compares the performance of different BER decoder implementations:
1. Original recursive decoder
2. Current optimized decoder  
3. Two-phase decoder (sequential)
4. Two-phase decoder (parallel)
"""

import sys
import time
import gc
import tracemalloc
from pathlib import Path
from statistics import mean, median, stdev
from dataclasses import dataclass, asdict
from typing import List, Dict, Any
import tempfile
import gzip

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from teleparser.buffer import BufferManager, MemoryBufferManager
from teleparser.decoders.ericsson import ericsson_voz_decoder, ericsson_voz_decoder_optimized

# Import our new two-phase decoder
try:
    from teleparser.decoders.ericsson.ber_two_phase import ericsson_voz_decoder_two_phase
    HAS_TWO_PHASE = True
except ImportError as e:
    print(f"Warning: Two-phase decoder not available: {e}")
    HAS_TWO_PHASE = False


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


class BenchmarkRunner:
    """Runs performance benchmarks on BER decoders."""
    
    def __init__(self, n_runs: int = 5, warmup_runs: int = 1):
        self.n_runs = n_runs
        self.warmup_runs = warmup_runs
    
    def benchmark_decoder(
        self, 
        decoder_factory, 
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
                decoder = decoder_factory(test_file)
                list(decoder.parse_blocks())
                del decoder
                gc.collect()
            except Exception as e:
                print(f"Warmup failed for {decoder_name}: {e}")
        
        # Actual benchmark runs
        for run_idx in range(self.n_runs):
            # Start memory tracking
            tracemalloc.start()
            
            try:
                start_time = time.perf_counter()
                
                decoder = decoder_factory(test_file)
                if show_progress and run_idx == 0:
                    records = decoder.process(show_progress=True)
                else:
                    records = list(decoder.parse_blocks())
                
                end_time = time.perf_counter()
                
                # Get memory usage
                current, peak = tracemalloc.get_traced_memory()
                tracemalloc.stop()
                
                parse_time = end_time - start_time
                times.append(parse_time)
                memory_peaks.append(peak)
                record_counts.append(len(records))
                
                del decoder, records
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
    
    def create_synthetic_test_data(self, size_kb: int) -> Path:
        """Create synthetic BER test data for benchmarking."""
        
        # Simple BER structure: SEQUENCE containing INTEGERs and OCTET STRINGs
        # This creates a repeating pattern that should be parseable
        
        basic_record = (
            b'\x30\x20'  # SEQUENCE, length 32
            b'\x02\x01\x01'  # INTEGER 1
            b'\x02\x01\x02'  # INTEGER 2  
            b'\x04\x04test'  # OCTET STRING "test"
            b'\x02\x02\x03\xe8'  # INTEGER 1000
            b'\x04\x08\x31\x32\x33\x34\x35\x36\x37\x38'  # OCTET STRING "12345678"
            b'\x02\x01\x0a'  # INTEGER 10
            b'\x04\x02\xff\x00'  # OCTET STRING with binary data
        )
        
        target_size = size_kb * 1024
        records_needed = target_size // len(basic_record) + 1
        
        test_data = basic_record * records_needed
        test_data = test_data[:target_size]  # Truncate to exact size
        
        # Create temporary compressed file
        temp_file = tempfile.NamedTemporaryFile(suffix='.gz', delete=False)
        temp_path = Path(temp_file.name)
        
        with gzip.open(temp_path, 'wb') as f:
            f.write(test_data)
        
        return temp_path
    
    def run_comprehensive_benchmark(
        self, 
        test_files: List[Path] = None,
        synthetic_sizes: List[int] = None
    ) -> List[BenchmarkResult]:
        """Run comprehensive benchmark across all decoders and test cases."""
        
        if test_files is None:
            test_files = []
        
        if synthetic_sizes is None:
            synthetic_sizes = [100, 500, 1000, 5000]  # KB
        
        all_results = []
        
        # Create decoder factories
        decoder_configs = [
            ("Original", lambda f: ericsson_voz_decoder(BufferManager(f))),
            ("Optimized", lambda f: ericsson_voz_decoder_optimized(MemoryBufferManager(f))),
        ]
        
        if HAS_TWO_PHASE:
            decoder_configs.extend([
                ("Two-Phase (1 worker)", lambda f: ericsson_voz_decoder_two_phase(MemoryBufferManager(f), n_workers=1)),
                ("Two-Phase (2 workers)", lambda f: ericsson_voz_decoder_two_phase(MemoryBufferManager(f), n_workers=2)),
                ("Two-Phase (4 workers)", lambda f: ericsson_voz_decoder_two_phase(MemoryBufferManager(f), n_workers=4)),
            ])
        
        # Test with synthetic data
        print("\\n" + "="*80)
        print("SYNTHETIC DATA BENCHMARKS")
        print("="*80)
        
        synthetic_files = []
        try:
            for size_kb in synthetic_sizes:
                print(f"\\nCreating synthetic test file ({size_kb} KB)...")
                test_file = self.create_synthetic_test_data(size_kb)
                synthetic_files.append(test_file)
                
                print(f"Benchmarking {size_kb} KB file ({test_file})...")
                
                for decoder_name, decoder_factory in decoder_configs:
                    try:
                        print(f"  Running {decoder_name}...")
                        result = self.benchmark_decoder(
                            decoder_factory, 
                            f"{decoder_name} ({size_kb}KB)", 
                            test_file,
                            show_progress=(decoder_name == "Optimized")  # Show progress for one decoder
                        )
                        all_results.append(result)
                        print(f"    {result.records_per_second:.0f} records/sec, "
                              f"{result.mb_per_second:.2f} MB/sec, "
                              f"{result.memory_peak/1024/1024:.1f} MB peak")
                        
                    except Exception as e:
                        print(f"    FAILED: {e}")
                        continue
        
        finally:
            # Clean up synthetic files
            for temp_file in synthetic_files:
                try:
                    temp_file.unlink()
                except:
                    pass
        
        # Test with real files if provided
        if test_files:
            print("\\n" + "="*80)
            print("REAL FILE BENCHMARKS")
            print("="*80)
            
            for test_file in test_files:
                if not test_file.exists():
                    print(f"Skipping missing file: {test_file}")
                    continue
                
                file_size_mb = test_file.stat().st_size / 1024 / 1024
                print(f"\\nBenchmarking real file: {test_file} ({file_size_mb:.1f} MB)")
                
                for decoder_name, decoder_factory in decoder_configs:
                    try:
                        print(f"  Running {decoder_name}...")
                        result = self.benchmark_decoder(
                            decoder_factory, 
                            f"{decoder_name} (real)", 
                            test_file
                        )
                        all_results.append(result)
                        print(f"    {result.records_per_second:.0f} records/sec, "
                              f"{result.mb_per_second:.2f} MB/sec, "
                              f"{result.memory_peak/1024/1024:.1f} MB peak")
                        
                    except Exception as e:
                        print(f"    FAILED: {e}")
                        continue
        
        return all_results
    
    def print_summary_report(self, results: List[BenchmarkResult]):
        """Print a comprehensive summary report."""
        
        if not results:
            print("No benchmark results to report.")
            return
        
        print("\\n" + "="*120)
        print("BENCHMARK SUMMARY REPORT")
        print("="*120)
        
        # Group results by test case (file size)
        by_test_case = {}
        for result in results:
            # Extract test case info from decoder name
            parts = result.decoder_name.split('(')
            decoder_name = parts[0].strip()
            test_case = parts[1].rstrip(')') if len(parts) > 1 else "unknown"
            
            if test_case not in by_test_case:
                by_test_case[test_case] = []
            by_test_case[test_case].append((decoder_name, result))
        
        for test_case, test_results in by_test_case.items():
            print(f"\\n--- {test_case} ---")
            print(f"{'Decoder':<25} {'Records/sec':<12} {'MB/sec':<10} {'Memory(MB)':<12} {'Speedup':<10}")
            print("-" * 75)
            
            # Sort by records per second (descending)
            test_results.sort(key=lambda x: x[1].records_per_second, reverse=True)
            
            baseline_rps = test_results[-1][1].records_per_second  # Slowest as baseline
            if baseline_rps == 0:
                baseline_rps = 1  # Avoid division by zero
            
            for decoder_name, result in test_results:
                speedup = result.records_per_second / baseline_rps
                memory_mb = result.memory_peak / 1024 / 1024
                
                print(f"{decoder_name:<25} {result.records_per_second:<12.0f} "
                      f"{result.mb_per_second:<10.2f} {memory_mb:<12.1f} "
                      f"{speedup:<10.2f}x")
        
        # Overall statistics
        print("\\n" + "="*80)
        print("OVERALL STATISTICS")
        print("="*80)
        
        by_decoder = {}
        for result in results:
            decoder_name = result.decoder_name.split('(')[0].strip()
            if decoder_name not in by_decoder:
                by_decoder[decoder_name] = []
            by_decoder[decoder_name].append(result)
        
        for decoder_name, decoder_results in by_decoder.items():
            if not decoder_results:
                continue
            
            avg_rps = mean([r.records_per_second for r in decoder_results])
            avg_mbs = mean([r.mb_per_second for r in decoder_results])
            avg_mem = mean([r.memory_peak for r in decoder_results]) / 1024 / 1024
            
            print(f"{decoder_name}:")
            print(f"  Average: {avg_rps:.0f} records/sec, {avg_mbs:.2f} MB/sec, {avg_mem:.1f} MB memory")
            
            if len(decoder_results) > 1:
                rps_stdev = stdev([r.records_per_second for r in decoder_results])
                print(f"  Std Dev: {rps_stdev:.0f} records/sec")


def main():
    """Main benchmark execution."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Benchmark BER decoder optimizations')
    parser.add_argument('--files', nargs='*', help='Real BER files to test')
    parser.add_argument('--sizes', nargs='*', type=int, default=[100, 500, 1000], 
                       help='Synthetic file sizes in KB')
    parser.add_argument('--runs', type=int, default=5, help='Number of benchmark runs')
    parser.add_argument('--warmup', type=int, default=1, help='Number of warmup runs')
    parser.add_argument('--output', help='Save detailed results to JSON file')
    
    args = parser.parse_args()
    
    # Convert file paths
    test_files = [Path(f) for f in (args.files or [])]
    
    print("BER Decoder Optimization Benchmark")
    print("=" * 50)
    print(f"Test runs: {args.runs}")
    print(f"Warmup runs: {args.warmup}")
    print(f"Synthetic sizes: {args.sizes} KB")
    print(f"Real files: {len(test_files)}")
    print(f"Two-phase decoder available: {HAS_TWO_PHASE}")
    
    # Run benchmarks
    runner = BenchmarkRunner(n_runs=args.runs, warmup_runs=args.warmup)
    results = runner.run_comprehensive_benchmark(
        test_files=test_files,
        synthetic_sizes=args.sizes
    )
    
    # Print summary
    runner.print_summary_report(results)
    
    # Save detailed results if requested
    if args.output:
        import json
        output_path = Path(args.output)
        output_data = {
            'config': {
                'runs': args.runs,
                'warmup': args.warmup,
                'sizes': args.sizes,
                'files': [str(f) for f in test_files]
            },
            'results': [r.to_dict() for r in results]
        }
        
        with open(output_path, 'w') as f:
            json.dump(output_data, f, indent=2)
        
        print(f"\\nDetailed results saved to: {output_path}")


if __name__ == "__main__":
    main()