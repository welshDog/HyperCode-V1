#!/usr/bin/env python3
"""
Codebase Analysis Report

This script analyzes the codebase and generates a report on code quality metrics.
"""

import ast
import datetime
import os
from pathlib import Path


def analyze_codebase():
    """Analyze the codebase and generate statistics."""
    stats = {"files": 0, "functions": 0, "classes": 0, "documented": 0, "errors": []}

    for root, _, files in os.walk("."):
        # Skip certain directories
        if any(
            d in root for d in ["venv", ".git", "__pycache__", "node_modules", ".venv"]
        ):
            continue

        for file in files:
            if file.endswith(".py"):
                try:
                    stats["files"] += 1
                    with open(Path(root) / file, "r", encoding="utf-8") as f:
                        tree = ast.parse(f.read())
                        for node in ast.walk(tree):
                            if isinstance(
                                node, (ast.FunctionDef, ast.AsyncFunctionDef)
                            ):
                                stats["functions"] += 1
                                if ast.get_docstring(node):
                                    stats["documented"] += 1
                            elif isinstance(node, ast.ClassDef):
                                stats["classes"] += 1
                                if ast.get_docstring(node):
                                    stats["documented"] += 1
                except Exception as e:
                    stats["errors"].append(f"Error in {Path(root) / file}: {str(e)}")

    return stats


def generate_report(stats):
    """Generate markdown report from stats."""
    total = stats["functions"] + stats["classes"]
    coverage = (stats["documented"] / total * 100) if total > 0 else 0

    report = [
        "# Codebase Analysis Report",
        f"Generated: {datetime.datetime.now().isoformat()}",
        "",
        "## Statistics",
        f"- Files: {stats['files']}",
        f"- Functions: {stats['functions']}",
        f"- Classes: {stats['classes']}",
        f"- Documented: {stats['documented']}/{total} ({coverage:.1f}%)",
        "",
        "## Documentation Coverage",
        f"Overall documentation coverage: **{coverage:.1f}%**",
        "",
        "## Recommendations",
        "1. Add docstrings to all public functions and classes",
        "2. Include type hints for better code clarity",
        "3. Document complex algorithms and business logic",
        "4. Add examples in docstrings where applicable",
    ]

    if stats["errors"]:
        report.extend(
            ["", "## Errors Encountered"] + [f"- {error}" for error in stats["errors"]]
        )

    return "\n".join(report)


def main():
    """Main function to analyze codebase and generate report."""
    print("🔍 Analyzing codebase...")
    stats = analyze_codebase()
    report = generate_report(stats)

    # Ensure docs directory exists
    docs_dir = Path("docs")
    docs_dir.mkdir(exist_ok=True)

    # Write report
    report_path = docs_dir / "CODEBASE_REPORT.md"
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(report)

    print(f"✅ Codebase report generated at {report_path}")
    print(
        f"📊 Documentation coverage: {(stats['documented'] / (stats['functions'] + stats['classes']) * 100):.1f}%"
    )


if __name__ == "__main__":
    main()
