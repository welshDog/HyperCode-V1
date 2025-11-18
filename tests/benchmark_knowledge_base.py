#!/usr/bin/env python3
"""Performance benchmark script for knowledge base search.

Run this to measure search performance with different dataset sizes
and generate a performance report.

Usage:
    python benchmark_knowledge_base.py
    python benchmark_knowledge_base.py --size 1000
    python benchmark_knowledge_base.py --report performance_report.md
"""

import argparse
import time
import statistics
from typing import List, Dict, Any
import json


class KnowledgeBaseBenchmark:
    """Benchmark suite for knowledge base performance testing."""

    def __init__(self, document_count: int = 100):
        self.document_count = document_count
        self.results: Dict[str, Any] = {}

    def generate_test_documents(self) -> List[Dict[str, Any]]:
        """Generate test documents for benchmarking."""
        print(f"Generating {self.document_count} test documents...")
        documents = []

        # Sample topics based on HyperCode themes
        topics = [
            "neurodivergent programming",
            "AI integration",
            "accessibility features",
            "historical languages",
            "quantum computing",
            "DNA computing",
            "visual programming",
            "spatial logic",
        ]

        for i in range(self.document_count):
            topic = topics[i % len(topics)]
            doc = {
                "id": f"doc_{i}",
                "title": f"{topic.title()} - Document {i}",
                "content": f"This is document {i} about {topic}. "
                f"It contains information relevant to HyperCode development. "
                f"Additional content to simulate realistic document size. "
                * 3,
                "tags": topic.split(),
                "created_at": f"2025-11-{(i % 30) + 1:02d}",
            }
            documents.append(doc)

        return documents

    def benchmark_search_speed(self, knowledge_base, queries: List[str]) -> Dict[str, float]:
        """Benchmark search speed with multiple queries."""
        print(f"\nBenchmarking search speed with {len(queries)} queries...")
        times = []

        for query in queries:
            start_time = time.perf_counter()
            results = knowledge_base.search(query)
            elapsed = time.perf_counter() - start_time
            times.append(elapsed)

        return {
            "mean_ms": statistics.mean(times) * 1000,
            "median_ms": statistics.median(times) * 1000,
            "min_ms": min(times) * 1000,
            "max_ms": max(times) * 1000,
            "stdev_ms": statistics.stdev(times) * 1000 if len(times) > 1 else 0,
        }

    def benchmark_concurrent_searches(self, knowledge_base, query: str, count: int = 10) -> Dict[str, float]:
        """Benchmark concurrent search operations."""
        print(f"\nBenchmarking {count} concurrent searches...")

        start_time = time.perf_counter()
        results = [knowledge_base.search(query) for _ in range(count)]
        total_time = time.perf_counter() - start_time

        return {
            "total_time_s": total_time,
            "queries_per_second": count / total_time,
            "avg_time_per_query_ms": (total_time / count) * 1000,
        }

    def benchmark_memory_usage(self, knowledge_base) -> Dict[str, Any]:
        """Benchmark memory usage (simplified version)."""
        print("\nMeasuring approximate memory usage...")

        # This is a simplified measurement
        # For production, use memory_profiler or tracemalloc
        import sys

        doc_size = sys.getsizeof(knowledge_base.documents) if hasattr(knowledge_base, "documents") else 0

        return {
            "documents_size_bytes": doc_size,
            "documents_size_mb": doc_size / (1024 * 1024),
            "note": "Simplified measurement. Use memory_profiler for accurate profiling.",
        }

    def run_full_benchmark(self, knowledge_base) -> Dict[str, Any]:
        """Run complete benchmark suite."""
        print(f"\n{'=' * 60}")
        print(f"  HyperCode Knowledge Base Performance Benchmark")
        print(f"{'=' * 60}")
        print(f"Document count: {self.document_count}")

        # Test queries
        test_queries = [
            "neurodivergent programming",
            "AI integration",
            "accessibility",
            "quantum computing",
            "visual programming",
            "HyperCode features",
            "ADHD friendly code",
            "spatial logic",
        ]

        # Run benchmarks
        results = {
            "document_count": self.document_count,
            "search_speed": self.benchmark_search_speed(knowledge_base, test_queries),
            "concurrent_searches": self.benchmark_concurrent_searches(knowledge_base, "neurodivergent programming"),
            "memory_usage": self.benchmark_memory_usage(knowledge_base),
        }

        self.results = results
        return results

    def generate_report(self, output_file: str = None):
        """Generate a markdown performance report."""
        if not self.results:
            print("No benchmark results available. Run benchmark first.")
            return

        report = f"""# Knowledge Base Performance Report

**Generated:** {time.strftime('%Y-%m-%d %H:%M:%S')}
**Document Count:** {self.results['document_count']}

## Search Speed Performance

| Metric | Value |
|--------|-------|
| Mean | {self.results['search_speed']['mean_ms']:.2f} ms |
| Median | {self.results['search_speed']['median_ms']:.2f} ms |
| Min | {self.results['search_speed']['min_ms']:.2f} ms |
| Max | {self.results['search_speed']['max_ms']:.2f} ms |
| Std Dev | {self.results['search_speed']['stdev_ms']:.2f} ms |

## Concurrent Search Performance

| Metric | Value |
|--------|-------|
| Total Time | {self.results['concurrent_searches']['total_time_s']:.3f} s |
| Queries/Second | {self.results['concurrent_searches']['queries_per_second']:.1f} |
| Avg Time/Query | {self.results['concurrent_searches']['avg_time_per_query_ms']:.2f} ms |

## Memory Usage

| Metric | Value |
|--------|-------|
| Documents Size | {self.results['memory_usage']['documents_size_mb']:.2f} MB |

## Performance Assessment

"""

        # Add performance assessment
        mean_time = self.results["search_speed"]["mean_ms"]
        if mean_time < 100:
            report += "✅ **EXCELLENT** - Search is blazing fast!\n"
        elif mean_time < 500:
            report += "✔️ **GOOD** - Search performance is acceptable.\n"
        elif mean_time < 1000:
            report += "⚠️ **FAIR** - Search could be optimized.\n"
        else:
            report += "❌ **NEEDS IMPROVEMENT** - Search is too slow.\n"

        report += f"\n## Recommendations\n\n"

        if mean_time > 500:
            report += "- Consider implementing caching for frequent queries\n"
            report += "- Optimize search algorithm (use TF-IDF or BM25)\n"
            report += "- Add indexing for faster lookups\n"
        else:
            report += "- Performance is good! Consider load testing for production scale.\n"

        if self.document_count < 1000:
            report += f"- Test with larger dataset (current: {self.document_count}, target: 1000+)\n"

        report += "\n---\n\n*Generated by HyperCode Knowledge Base Benchmark Suite* 🧠🚀\n"

        # Output report
        if output_file:
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(report)
            print(f"\nReport saved to: {output_file}")
        else:
            print("\n" + report)

        return report


def main():
    """Main entry point for benchmark script."""
    parser = argparse.ArgumentParser(description="Benchmark knowledge base performance")
    parser.add_argument(
        "--size",
        type=int,
        default=100,
        help="Number of test documents to generate (default: 100)",
    )
    parser.add_argument(
        "--report",
        type=str,
        default=None,
        help="Output file for performance report (default: print to console)",
    )
    args = parser.parse_args()

    # Create benchmark instance
    benchmark = KnowledgeBaseBenchmark(document_count=args.size)

    # Generate test data
    documents = benchmark.generate_test_documents()

    # TODO: Replace with actual KnowledgeBase implementation
    print("\n⚠️  NOTE: Using mock knowledge base. Replace with actual implementation.")

    # Mock knowledge base for demonstration
    class MockKnowledgeBase:
        def __init__(self, documents):
            self.documents = documents

        def search(self, query):
            # Simple mock search - just return first 5 docs
            time.sleep(0.01)  # Simulate search time
            return self.documents[:5]

    knowledge_base = MockKnowledgeBase(documents)

    # Run benchmarks
    results = benchmark.run_full_benchmark(knowledge_base)

    # Generate report
    benchmark.generate_report(output_file=args.report)

    print("\n" + "=" * 60)
    print("  Benchmark Complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()
