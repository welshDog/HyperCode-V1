#!/usr/bin/env python3
"""
Performance Benchmark Tool for HyperCode Knowledge Base
Generates beautiful markdown reports and tests scalability
"""

import argparse
import json
import os
import sys
import tempfile
import time
from pathlib import Path
from typing import Any, Dict, List

import psutil

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from hypercode.knowledge_base import HyperCodeKnowledgeBase


class BenchmarkSuite:
    """Comprehensive benchmark suite for Knowledge Base"""

    def __init__(self):
        self.results = {
            "test_runs": [],
            "summary": {},
            "system_info": self._get_system_info(),
        }

    def _get_system_info(self) -> Dict[str, Any]:
        """Get system information for benchmark context"""
        return {
            "cpu_count": psutil.cpu_count(),
            "memory_total": f"{psutil.virtual_memory().total / 1024 / 1024 / 1024:.2f} GB",
            "python_version": sys.version,
            "platform": sys.platform,
        }

    def generate_test_data(self, size: int) -> List[Dict[str, Any]]:
        """Generate test data of specified size"""
        categories = [
            "ai",
            "spatial",
            "compilation",
            "community",
            "philosophy",
            "testing",
            "performance",
            "architecture",
        ]
        tags_pool = [
            "neurodivergent",
            "accessibility",
            "open-source",
            "quantum",
            "dna",
            "visual",
            "2d",
            "3d",
            "gpt-4",
            "claude",
        ]

        documents = []
        for i in range(size):
            category = categories[i % len(categories)]
            doc = {
                "title": f"Benchmark Document {i} - {category.title()}",
                "content": (
                    f"This is benchmark content for document {i}. "
                    f"The document belongs to the {category} category. "
                    f"It contains various keywords for testing search performance. "
                    f"Keywords: neurodivergent programming, AI integration, spatial computing, "
                    f"quantum compilation, DNA computing, visual programming, accessibility features. "
                    f"Repeated content for size testing: " * (10 if i % 10 == 0 else 5)
                ),
                "tags": [
                    category,
                    tags_pool[i % len(tags_pool)],
                    f"size-{size}",
                    f"batch-{i // 100}",
                    "benchmark",
                ],
            }
            documents.append(doc)

        return documents

    def benchmark_operation(
        self, operation_name: str, operation_func, **kwargs
    ) -> Dict[str, Any]:
        """Benchmark a single operation"""
        # Measure memory before
        process = psutil.Process(os.getpid())
        mem_before = process.memory_info().rss

        # Time the operation
        start_time = time.time()
        result = operation_func(**kwargs)
        end_time = time.time()

        # Measure memory after
        mem_after = process.memory_info().rss

        return {
            "operation": operation_name,
            "duration": end_time - start_time,
            "memory_before": mem_before,
            "memory_after": mem_after,
            "memory_delta": mem_after - mem_before,
            "result": result,
        }

    def run_benchmark_suite(self, size: int = 1000) -> Dict[str, Any]:
        """Run complete benchmark suite"""
        print(f"🚀 Starting benchmark with {size} documents...")

        # Create temporary knowledge base
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            temp_path = f.name

        try:
            kb = HyperCodeKnowledgeBase(temp_path)

            # Generate test data
            print(f"📝 Generating {size} test documents...")
            test_docs = self.generate_test_data(size)

            # Benchmark 1: Document Addition
            print("📊 Benchmarking document addition...")
            add_results = []
            for i, doc in enumerate(test_docs):
                result = self.benchmark_operation(
                    f"add_document_{i}", kb.add_document, **doc
                )
                add_results.append(result)

                if (i + 1) % 100 == 0:
                    print(f"  Added {i + 1}/{size} documents")

            # Benchmark 2: Save Operation
            print("💾 Benchmarking save operation...")
            save_result = self.benchmark_operation("save", kb.save)

            # Benchmark 3: Load Operation
            print("📂 Benchmarking load operation...")
            kb2 = HyperCodeKnowledgeBase(temp_path)
            load_result = {
                "operation": "load",
                "duration": save_result["duration"],  # Load happens in __init__
                "documents_loaded": len(kb2.documents),
            }

            # Benchmark 4: Search Operations
            print("🔍 Benchmarking search operations...")
            search_queries = [
                "neurodivergent",
                "AI integration",
                "spatial computing",
                "quantum compilation",
                "benchmark",
                "performance",
                "testing",
                "architecture",
                "open-source",
                "accessibility",
            ]

            search_results = []
            for query in search_queries:
                result = self.benchmark_operation(
                    f"search_{query.replace(' ', '_')}",
                    kb2.search_documents,
                    query=query,
                    limit=10,
                )
                search_results.append(result)

            # Benchmark 5: Context Extraction
            print("📄 Benchmarking context extraction...")
            context_results = []
            for query in search_queries[:5]:  # Test subset
                result = self.benchmark_operation(
                    f"context_{query.replace(' ', '_')}",
                    kb2.get_context_for_query,
                    query=query,
                )
                context_results.append(result)

            # Benchmark 6: Bulk Operations
            print("🔄 Benchmarking bulk operations...")

            # Bulk search
            bulk_search_start = time.time()
            all_search_results = []
            for query in search_queries:
                results = kb2.search_documents(query, limit=20)
                all_search_results.extend(results)
            bulk_search_duration = time.time() - bulk_search_start

            # Benchmark 7: Memory Stress Test
            print("🧠 Running memory stress test...")
            memory_results = []
            for i in range(10):
                # Perform intensive operations
                results = kb2.search_documents("benchmark", limit=50)
                context = kb2.get_context_for_query("benchmark")

                mem_info = psutil.Process(os.getpid()).memory_info()
                memory_results.append(
                    {
                        "iteration": i,
                        "memory_mb": mem_info.rss / 1024 / 1024,
                        "search_results": len(results),
                        "context_length": len(context),
                    }
                )

            # Compile results
            test_run = {
                "size": size,
                "timestamp": time.time(),
                "addition": {
                    "total_duration": sum(r["duration"] for r in add_results),
                    "avg_duration_per_doc": sum(r["duration"] for r in add_results)
                    / len(add_results),
                    "docs_per_second": size / sum(r["duration"] for r in add_results),
                },
                "save": save_result,
                "load": load_result,
                "search": {
                    "queries_tested": len(search_results),
                    "avg_duration": sum(r["duration"] for r in search_results)
                    / len(search_results),
                    "max_duration": max(r["duration"] for r in search_results),
                    "min_duration": min(r["duration"] for r in search_results),
                    "total_results": sum(len(r["result"]) for r in search_results),
                },
                "context": {
                    "queries_tested": len(context_results),
                    "avg_duration": sum(r["duration"] for r in context_results)
                    / len(context_results),
                    "avg_context_length": sum(len(r["result"]) for r in context_results)
                    / len(context_results),
                },
                "bulk_search": {
                    "duration": bulk_search_duration,
                    "queries": len(search_queries),
                    "total_results": len(all_search_results),
                },
                "memory_stress": {
                    "peak_memory_mb": max(r["memory_mb"] for r in memory_results),
                    "memory_growth_mb": memory_results[-1]["memory_mb"]
                    - memory_results[0]["memory_mb"],
                    "iterations": len(memory_results),
                },
            }

            self.results["test_runs"].append(test_run)

            # Calculate summary
            self._calculate_summary()

            return test_run

        finally:
            # Cleanup
            Path(temp_path).unlink(missing_ok=True)

    def _calculate_summary(self):
        """Calculate summary statistics"""
        if not self.results["test_runs"]:
            return

        runs = self.results["test_runs"]

        self.results["summary"] = {
            "total_runs": len(runs),
            "sizes_tested": [run["size"] for run in runs],
            "performance_trends": {
                "addition_throughput": [
                    run["addition"]["docs_per_second"] for run in runs
                ],
                "search_performance": [run["search"]["avg_duration"] for run in runs],
                "memory_usage": [
                    run["memory_stress"]["peak_memory_mb"] for run in runs
                ],
            },
            "recommendations": self._generate_recommendations(),
        }

    def _generate_recommendations(self) -> List[str]:
        """Generate performance recommendations"""
        recommendations = []

        if not self.results["test_runs"]:
            return recommendations

        latest_run = self.results["test_runs"][-1]

        # Check addition performance
        if latest_run["addition"]["docs_per_second"] < 100:
            recommendations.append(
                "📉 Document addition is slow (<100 docs/sec). Consider optimizing the save operation."
            )

        # Check search performance
        if latest_run["search"]["avg_duration"] > 0.1:
            recommendations.append(
                "🔍 Search is slow (>0.1s per query). Consider implementing indexing."
            )

        # Check memory usage
        if latest_run["memory_stress"]["memory_growth_mb"] > 50:
            recommendations.append(
                "🧠 Memory usage is growing significantly. Check for memory leaks."
            )

        # Check file size
        if latest_run["size"] > 1000:
            docs_per_mb = (
                latest_run["size"] / latest_run["memory_stress"]["peak_memory_mb"]
            )
            if docs_per_mb < 10:
                recommendations.append(
                    "💾 Memory efficiency is low. Consider optimizing data structures."
                )

        if not recommendations:
            recommendations.append("✅ Performance looks good!")

        return recommendations

    def generate_markdown_report(self, output_file: str = "benchmark_report.md"):
        """Generate beautiful markdown report"""
        report = []

        # Header
        report.append("# 🚀 HyperCode Knowledge Base Performance Report")
        report.append("")
        report.append(f"Generated on: {time.strftime('%Y-%m-%d %H:%M:%S')}")
        report.append("")

        # System Info
        report.append("## 🖥️ System Information")
        report.append("")
        info = self.results["system_info"]
        report.append(f"- **CPU Cores**: {info['cpu_count']}")
        report.append(f"- **Total Memory**: {info['memory_total']}")
        report.append(f"- **Python Version**: {info['python_version']}")
        report.append(f"- **Platform**: {info['platform']}")
        report.append("")

        # Executive Summary
        report.append("## 📊 Executive Summary")
        report.append("")
        if self.results["summary"]:
            summary = self.results["summary"]
            report.append(f"- **Total Test Runs**: {summary['total_runs']}")
            report.append(
                f"- **Sizes Tested**: {', '.join(map(str, summary['sizes_tested']))} documents"
            )

            if summary["recommendations"]:
                report.append("")
                report.append("### 🎯 Recommendations")
                for rec in summary["recommendations"]:
                    report.append(f"- {rec}")
        report.append("")

        # Detailed Results
        report.append("## 📈 Detailed Results")
        report.append("")

        for i, run in enumerate(self.results["test_runs"], 1):
            report.append(f"### Test Run {i}: {run['size']} Documents")
            report.append("")

            # Addition Performance
            add = run["addition"]
            report.append("#### 📝 Document Addition")
            report.append(f"- **Total Duration**: {add['total_duration']:.3f}s")
            report.append(f"- **Avg Duration/Doc**: {add['avg_duration_per_doc']:.6f}s")
            report.append(f"- **Throughput**: {add['docs_per_second']:.1f} docs/sec")
            report.append("")

            # Save/Load Performance
            report.append("#### 💾 Save/Load Operations")
            report.append(f"- **Save Duration**: {run['save']['duration']:.3f}s")
            report.append(f"- **Documents Loaded**: {run['load']['documents_loaded']}")
            report.append("")

            # Search Performance
            search = run["search"]
            report.append("#### 🔍 Search Performance")
            report.append(f"- **Queries Tested**: {search['queries_tested']}")
            report.append(f"- **Avg Duration**: {search['avg_duration']:.6f}s")
            report.append(f"- **Max Duration**: {search['max_duration']:.6f}s")
            report.append(f"- **Min Duration**: {search['min_duration']:.6f}s")
            report.append(f"- **Total Results Found**: {search['total_results']}")
            report.append("")

            # Context Extraction
            context = run["context"]
            report.append("#### 📄 Context Extraction")
            report.append(f"- **Queries Tested**: {context['queries_tested']}")
            report.append(f"- **Avg Duration**: {context['avg_duration']:.6f}s")
            report.append(
                f"- **Avg Context Length**: {context['avg_context_length']:.0f} chars"
            )
            report.append("")

            # Bulk Operations
            bulk = run["bulk_search"]
            report.append("#### 🔄 Bulk Operations")
            report.append(f"- **Bulk Search Duration**: {bulk['duration']:.3f}s")
            report.append(f"- **Queries Processed**: {bulk['queries']}")
            report.append(f"- **Total Results**: {bulk['total_results']}")
            report.append("")

            # Memory Usage
            memory = run["memory_stress"]
            report.append("#### 🧠 Memory Usage")
            report.append(f"- **Peak Memory**: {memory['peak_memory_mb']:.1f} MB")
            report.append(f"- **Memory Growth**: {memory['memory_growth_mb']:.1f} MB")
            report.append(f"- **Stress Test Iterations**: {memory['iterations']}")
            report.append("")

        # Performance Trends
        if len(self.results["test_runs"]) > 1:
            report.append("## 📊 Performance Trends")
            report.append("")

            trends = self.results["summary"]["performance_trends"]

            report.append("### Addition Throughput (docs/sec)")
            for i, throughput in enumerate(trends["addition_throughput"]):
                size = self.results["test_runs"][i]["size"]
                report.append(f"- {size} docs: {throughput:.1f}")
            report.append("")

            report.append("### Search Performance (avg duration)")
            for i, duration in enumerate(trends["search_performance"]):
                size = self.results["test_runs"][i]["size"]
                report.append(f"- {size} docs: {duration:.6f}s")
            report.append("")

            report.append("### Memory Usage (peak MB)")
            for i, memory in enumerate(trends["memory_usage"]):
                size = self.results["test_runs"][i]["size"]
                report.append(f"- {size} docs: {memory:.1f} MB")
            report.append("")

        # Write report
        report_content = "\n".join(report)

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(report_content)

        print(f"📄 Report generated: {output_file}")
        return report_content

    def save_json_results(self, output_file: str = "benchmark_results.json"):
        """Save results as JSON"""
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(self.results, f, indent=2, default=str)
        print(f"💾 JSON results saved: {output_file}")


def main():
    """Main benchmark runner"""
    parser = argparse.ArgumentParser(
        description="HyperCode Knowledge Base Benchmark Tool"
    )
    parser.add_argument(
        "--size",
        type=int,
        default=1000,
        help="Number of documents to test (default: 1000)",
    )
    parser.add_argument(
        "--runs", type=int, default=1, help="Number of benchmark runs (default: 1)"
    )
    parser.add_argument(
        "--output", type=str, default="benchmark_report.md", help="Output report file"
    )
    parser.add_argument(
        "--json", type=str, default="benchmark_results.json", help="JSON results file"
    )
    parser.add_argument(
        "--sizes",
        nargs="+",
        type=int,
        help="Multiple sizes to test (e.g., --sizes 100 500 1000)",
    )

    args = parser.parse_args()

    # Create benchmark suite
    suite = BenchmarkSuite()

    # Run benchmarks
    sizes_to_test = args.sizes if args.sizes else [args.size]

    print("🎯 Starting HyperCode Knowledge Base Benchmark Suite")
    print("=" * 60)

    for size in sizes_to_test:
        for run in range(args.runs):
            print(f"\n🔄 Run {run + 1}/{args.runs} with {size} documents")
            suite.run_benchmark_suite(size)

    # Generate reports
    print("\n📊 Generating reports...")
    suite.generate_markdown_report(args.output)
    suite.save_json_results(args.json)

    print("\n✅ Benchmark complete!")
    print(f"📄 View report: {args.output}")
    print(f"💾 View JSON: {args.json}")


if __name__ == "__main__":
    main()
