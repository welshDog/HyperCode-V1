#!/usr/bin/env python3
"""
Local Project Health Scanner for HyperCode
Analyzes project structure, code quality, and documentation
"""

import ast
import os
import re
from pathlib import Path
from typing import Dict, List, Tuple

# Project configuration
PROJECT_ROOT = Path(__file__).parent
SRC_DIR = PROJECT_ROOT / "src"
DOCS_DIR = PROJECT_ROOT / "docs"
TEST_DIR = PROJECT_ROOT / "tests"


class ProjectScanner:
    """Scans the project for health metrics without external dependencies"""

    def __init__(self):
        self.metrics = {
            "files_scanned": 0,
            "total_lines": 0,
            "docstring_coverage": 0,
            "function_count": 0,
            "class_count": 0,
            "todo_count": 0,
            "test_coverage": 0,
            "errors": [],
        }

    def scan_project(self) -> Dict:
        """Scan the entire project and return health metrics"""
        self._scan_directory(SRC_DIR)
        self._check_documentation()
        self._check_tests()
        self._calculate_metrics()
        return self.metrics

    def _scan_directory(self, directory: Path) -> None:
        """Recursively scan a directory for Python files"""
        for item in directory.rglob("*.py"):
            if "__pycache__" in str(item) or ".venv" in str(item):
                continue

            self.metrics["files_scanned"] += 1
            self._analyze_file(item)

    def _analyze_file(self, file_path: Path) -> None:
        """Analyze a single Python file"""
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            # Count TODOs
            self.metrics["todo_count"] += len(
                re.findall(r"#\s*TODO", content, re.IGNORECASE)
            )

            # Basic line count
            lines = content.splitlines()
            self.metrics["total_lines"] += len(lines)

            # Parse AST for more complex analysis
            try:
                tree = ast.parse(content)
                self._analyze_ast(tree)
            except SyntaxError as e:
                self.metrics["errors"].append(f"Syntax error in {file_path}: {e}")

        except Exception as e:
            self.metrics["errors"].append(f"Error processing {file_path}: {e}")

    def _analyze_ast(self, node) -> None:
        """Analyze Python AST for code quality metrics"""
        if isinstance(node, ast.FunctionDef):
            self.metrics["function_count"] += 1
            if not ast.get_docstring(node):
                self.metrics["docstring_coverage"] -= 1
            else:
                self.metrics["docstring_coverage"] += 1

        elif isinstance(node, ast.ClassDef):
            self.metrics["class_count"] += 1
            if not ast.get_docstring(node):
                self.metrics["docstring_coverage"] -= 1
            else:
                self.metrics["docstring_coverage"] += 1

        # Recurse into child nodes
        for child in ast.iter_child_nodes(node):
            self._analyze_ast(child)

    def _check_documentation(self) -> None:
        """Check documentation coverage"""
        if not DOCS_DIR.exists():
            self.metrics["errors"].append("No docs/ directory found")
            return

        # Simple check for README and other key docs
        required_docs = ["README.md", "CONTRIBUTING.md", "LICENSE"]
        for doc in required_docs:
            if not (PROJECT_ROOT / doc).exists():
                self.metrics["errors"].append(f"Missing documentation: {doc}")

    def _check_tests(self) -> None:
        """Check test coverage"""
        if not TEST_DIR.exists():
            self.metrics["errors"].append("No tests/ directory found")
            return

        # Simple test file check
        test_files = list(TEST_DIR.rglob("test_*.py"))
        if not test_files:
            self.metrics["errors"].append("No test files found (test_*.py)")

    def _calculate_metrics(self) -> None:
        """Calculate final metrics"""
        # Calculate docstring coverage percentage
        total_items = self.metrics["function_count"] + self.metrics["class_count"]
        if total_items > 0:
            self.metrics["docstring_coverage"] = max(
                0, (self.metrics["docstring_coverage"] / total_items) * 100
            )
        else:
            self.metrics["docstring_coverage"] = 0


def print_health_report(metrics: Dict) -> None:
    """Print a formatted health report"""
    print("\n" + "=" * 50)
    print("  HYPERCODE PROJECT HEALTH REPORT")
    print("=" * 50)

    print("\n📊 CODE METRICS")
    print(f"  • Files Scanned: {metrics['files_scanned']}")
    print(f"  • Total Lines: {metrics['total_lines']}")
    print(f"  • Functions: {metrics['function_count']}")
    print(f"  • Classes: {metrics['class_count']}")
    print(f"  • Docstring Coverage: {metrics['docstring_coverage']:.1f}%")

    print("\n⚠️  ISSUES FOUND")
    if metrics["errors"]:
        for error in metrics["errors"]:
            print(f"  • {error}")
    else:
        print("  No critical issues found!")

    print("\n🔍 RECOMMENDATIONS")
    if metrics["todo_count"] > 0:
        print(f"  • Address {metrics['todo_count']} TODO comments")
    if metrics["docstring_coverage"] < 80:
        print("  • Improve documentation coverage (aim for >80%)")
    if not TEST_DIR.exists():
        print("  • Add unit tests in the tests/ directory")

    print("\n" + "=" * 50 + "\n")


def main():
    """Main function to run the health scanner"""
    print("🔍 Scanning HyperCode project...")
    scanner = ProjectScanner()
    metrics = scanner.scan_project()
    print_health_report(metrics)


if __name__ == "__main__":
    main()
