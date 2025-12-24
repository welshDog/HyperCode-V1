"""
Database Analysis and Improvement Tool

This script provides tools to analyze and improve the Hypercode database,
focusing on documentation, testing, code structure, and maintenance.
"""

import json
import statistics
from collections import defaultdict
from pathlib import Path
from typing import Any, DefaultDict, Dict, List, TypedDict


class EntityMetrics(TypedDict):
    doc_count: int
    total_entities: int
    tested_entities: int


class DocstringStats(TypedDict):
    total_with_docs: int
    avg_length: float
    min_length: int
    max_length: int


class DatabaseAnalyzer:
    def __init__(self, db_path: str) -> None:
        self.db_path = Path(db_path)
        self.entities: List[Dict[str, Any]] = []
        self.stats: Dict[str, Any] = {
            "total_entities": 0,
            "entity_types": defaultdict(int),
            "files": defaultdict(int),
            "doc_coverage": 0.0,
            "test_coverage": 0.0,
            "avg_methods_per_class": 0.0,
            "docstring_stats": DocstringStats(
                total_with_docs=0, avg_length=0.0, min_length=0, max_length=0
            ),
            "file_metrics": defaultdict(
                lambda: EntityMetrics(doc_count=0, total_entities=0, tested_entities=0)
            ),
            "files_with_most_entities": [],
        }

    def load_database(self) -> bool:
        """Load and validate the database."""
        try:
            with open(self.db_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            if not isinstance(data, dict) or "entities" not in data:
                raise ValueError("Invalid database format: missing 'entities' key")

            self.entities = data["entities"]
            self.stats["total_entities"] = len(self.entities)
            return True
        except Exception as e:
            print(f"Error loading database: {e}")
            return False

    def analyze_documentation(self) -> None:
        """Analyze documentation coverage and quality."""
        doc_lengths: List[int] = []
        has_doc = 0

        for entity in self.entities:
            # Handle case where docstring is None
            docstring = str(entity.get("docstring") or "").strip()

            if docstring:
                has_doc += 1
                doc_lengths.append(len(docstring))

            # Track documentation by file
            file = str(entity.get("file", "unknown"))
            metrics = self.stats["file_metrics"][file]
            metrics["total_entities"] = metrics.get("total_entities", 0) + 1
            if docstring:
                metrics["doc_count"] = metrics.get("doc_count", 0) + 1

        # Calculate documentation statistics
        total_entities = self.stats["total_entities"]
        self.stats["doc_coverage"] = (
            (has_doc / total_entities) * 100 if total_entities else 0.0
        )
        self.stats["docstring_stats"] = DocstringStats(
            total_with_docs=has_doc,
            avg_length=float(statistics.mean(doc_lengths)) if doc_lengths else 0.0,
            min_length=min(doc_lengths) if doc_lengths else 0,
            max_length=max(doc_lengths) if doc_lengths else 0,
        )

    def analyze_test_coverage(self) -> None:
        """Analyze test coverage across the codebase."""
        has_test = sum(1 for e in self.entities if e.get("has_test", False))
        total_entities = self.stats["total_entities"]
        self.stats["test_coverage"] = (
            (has_test / total_entities) * 100 if total_entities else 0.0
        )

        # Track test coverage by file
        for entity in self.entities:
            file = str(entity.get("file", "unknown"))
            metrics = self.stats["file_metrics"][file]
            metrics["total_entities"] = metrics.get("total_entities", 0) + 1
            if entity.get("has_test", False):
                metrics["tested_entities"] = metrics.get("tested_entities", 0) + 1

    def analyze_code_structure(self) -> None:
        """Analyze code structure metrics."""
        methods_per_class: List[int] = []
        entities_per_file: DefaultDict[str, int] = defaultdict(int)

        for entity in self.entities:
            # Count entities per file
            file = str(entity.get("file", "unknown"))
            entities_per_file[file] += 1

            # Count methods per class
            if entity.get("type") == "class":
                methods = entity.get("methods", [])
                if isinstance(methods, list):
                    methods_per_class.append(len(methods))

        self.stats["avg_methods_per_class"] = (
            statistics.mean(methods_per_class) if methods_per_class else 0.0
        )
        self.stats["files_with_most_entities"] = sorted(
            entities_per_file.items(), key=lambda x: x[1], reverse=True
        )[:10]

    def generate_report(self) -> str:
        """Generate a comprehensive report of findings."""
        doc_stats = self.stats["docstring_stats"]
        report = [
            "=" * 80,
            "DATABASE ANALYSIS REPORT",
            "=" * 80,
            f"Database: {self.db_path}",
            f"Total entities: {self.stats['total_entities']}",
            "\nDOCUMENTATION:",
            "-" * 40,
            f"Documentation coverage: {self.stats['doc_coverage']:.1f}%",
            f"Documents with docstrings: {doc_stats['total_with_docs']}",
            f"Average docstring length: {doc_stats['avg_length']:.1f} chars",
            f"Min/Max docstring length: {doc_stats['min_length']}/"
            f"{doc_stats['max_length']}",
            "\nTEST COVERAGE:",
            "-" * 40,
            f"Test coverage: {self.stats['test_coverage']:.1f}%",
            "\nCODE STRUCTURE:",
            "-" * 40,
            f"Average methods per class: {self.stats['avg_methods_per_class']:.1f}",
            "\nFILES NEEDING ATTENTION:",
            "-" * 40,
        ]

        # Add files with most entities but low documentation
        report.append("\nFiles with most entities (potential refactoring candidates):")
        for file, count in self.stats.get("files_with_most_entities", [])[:10]:
            metrics = self.stats["file_metrics"].get(file, {})
            total = metrics.get("total_entities", 1)
            doc_count = metrics.get("doc_count", 0)
            doc_coverage = (doc_count / total) * 100
            report.append(f"- {file}: {count} entities, {doc_coverage:.1f}% documented")

        # Add files with lowest test coverage
        report.append("\nFiles with lowest test coverage:")
        test_coverage = []
        for file, metrics in self.stats["file_metrics"].items():
            total = metrics.get("total_entities", 0)
            if total > 0:
                tested = metrics.get("tested_entities", 0)
                coverage = (tested / total) * 100
                test_coverage.append((file, coverage, total))

        for file, coverage, count in sorted(test_coverage, key=lambda x: x[1])[:10]:
            report.append(f"- {file}: {coverage:.1f}% coverage ({count} entities)")

        return "\n".join(report)

    def get_entities_needing_docs(self, limit: int = 10) -> List[Dict[str, Any]]:
        """Get entities that need documentation."""
        return [e for e in self.entities if not str(e.get("docstring", "")).strip()][
            :limit
        ]

    def get_untested_entities(self, limit: int = 10) -> List[Dict[str, Any]]:
        """Get entities that need tests."""
        return [e for e in self.entities if not e.get("has_test", False)][:limit]


def main() -> None:
    """Main function to run the database analyzer."""
    try:
        analyzer = DatabaseAnalyzer("HYPER_DATABASE.json")

        if not analyzer.load_database():
            print("Failed to load database")
            return

        print("Analyzing documentation...")
        analyzer.analyze_documentation()

        print("Analyzing test coverage...")
        analyzer.analyze_test_coverage()

        print("Analyzing code structure...")
        analyzer.analyze_code_structure()

        # Generate and print report
        report = analyzer.generate_report()
        print("\n" + report)

        # Save report to file
        with open("database_analysis_report.txt", "w", encoding="utf-8") as f:
            f.write(report)

        print("\nAnalysis complete. Report saved to 'database_analysis_report.txt'")

    except Exception as e:
        print(f"An error occurred: {e}")
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    main()
