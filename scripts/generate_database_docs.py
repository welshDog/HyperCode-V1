#!/usr/bin/env python3
"""
HyperCode Database Documentation Generator

This script generates and updates the database documentation for the HyperCode project.
"""

import ast
import datetime
import os
import subprocess
from pathlib import Path
from typing import Dict, List, Tuple

# Configuration
PROJECT_ROOT = Path(__file__).parent.parent
DOCS_DIR = PROJECT_ROOT / "docs"
DATABASE_DOCS_DIR = DOCS_DIR / "database"
REPORT_FILE = DATABASE_DOCS_DIR / "HYPER_DATABASE.md"

# Ensure directories exist
DATABASE_DOCS_DIR.mkdir(parents=True, exist_ok=True)


def get_git_info() -> Dict[str, str]:
    """Get Git repository information."""
    try:
        return {
            "branch": subprocess.check_output(
                ["git", "rev-parse", "--abbrev-ref", "HEAD"],
                cwd=PROJECT_ROOT,
                text=True,
            ).strip(),
            "commit": subprocess.check_output(
                ["git", "rev-parse", "HEAD"], cwd=PROJECT_ROOT, text=True
            ).strip(),
            "last_commit_date": subprocess.check_output(
                ["git", "log", "-1", "--format=%cd"], cwd=PROJECT_ROOT, text=True
            ).strip(),
        }
    except Exception as e:
        print(f"Warning: Could not get Git info: {e}")
        return {}


def analyze_codebase() -> Dict:
    """Analyze the codebase and return statistics."""
    stats = {
        "files": 0,
        "functions": 0,
        "classes": 0,
        "documented": 0,
        "start_time": datetime.datetime.now(),
        "entities": [],
    }

    # Walk through the project directory
    for root, _, files in os.walk(PROJECT_ROOT):
        # Skip virtual environments and other non-source directories
        if any(
            d in root for d in ["venv", ".venv", "__pycache__", ".git", "node_modules"]
        ):
            continue

        for file in files:
            if file.endswith(".py"):
                stats["files"] += 1
                filepath = Path(root) / file
                try:
                    with open(filepath, "r", encoding="utf-8") as f:
                        tree = ast.parse(f.read(), filename=filepath)

                    # Analyze the AST
                    for node in ast.walk(tree):
                        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                            stats["functions"] += 1
                            docstring = ast.get_docstring(node)
                            if docstring and docstring.strip():
                                stats["documented"] += 1

                        elif isinstance(node, ast.ClassDef):
                            stats["classes"] += 1
                            docstring = ast.get_docstring(node)
                            if docstring and docstring.strip():
                                stats["documented"] += 1

                except Exception as e:
                    print(f"Error analyzing {filepath}: {e}")

    stats["end_time"] = datetime.datetime.now()
    stats["duration"] = (stats["end_time"] - stats["start_time"]).total_seconds()
    return stats


def generate_markdown_report(stats: Dict, git_info: Dict) -> str:
    """Generate the markdown report."""
    total_entities = stats["functions"] + stats["classes"]
    doc_coverage = (
        (stats["documented"] / total_entities * 100) if total_entities > 0 else 0
    )

    report = [
        "# 🧠 HYPER DATABASE",
        "## Living Inventory of HyperCode Codebase\n",
        f"**Generated**: {datetime.datetime.now().isoformat()}",
        f"**Scan Time**: {stats['duration']:.1f}s",
        f"**Files Scanned**: {stats['files']}",
        f"**Total Entities**: {total_entities}\n",
        "---\n",
        "## 📊 HEALTH SNAPSHOT\n",
        "| Metric | Value |",
        "|--------|-------|",
        f"| **Functions** | {stats['functions']} |",
        f"| **Classes** | {stats['classes']} |",
        f"| **Files** | {stats['files']} |",
        f"| **Documentation** | {stats['documented']}/{total_entities} ({doc_coverage:.1f}%) |",
        f"| **Status** | {'✅ HEALTHY' if doc_coverage > 70 else '⚠️ NEEDS IMPROVEMENT' if doc_coverage > 40 else '❌ POOR'} |\n",
        "---\n",
        "## 📋 GIT INFORMATION\n",
    ]

    if git_info:
        report.extend(
            [
                f"- **Branch**: {git_info.get('branch', 'N/A')}",
                f"- **Commit**: `{git_info.get('commit', 'N/A')}`",
                f"- **Last Commit**: {git_info.get('last_commit_date', 'N/A')}\n",
                "---\n",
            ]
        )

    report.extend(
        [
            "## 📁 DIRECTORY STRUCTURE\n",
            "```",
            subprocess.check_output(
                ["tree", "-L", "3", "-I", "venv|.venv|__pycache__|.git|node_modules"],
                cwd=PROJECT_ROOT,
                text=True,
            ),
            "```\n",
            "---\n",
            "## 📝 DOCUMENTATION COVERAGE\n",
            f"Overall documentation coverage: **{doc_coverage:.1f}%**\n",
            "### Recommendations:\n",
            "1. Add docstrings to all public functions and classes\n",
            "2. Include type hints for better code clarity\n",
            "3. Document complex algorithms and business logic\n",
            "4. Add examples in docstrings where applicable\n",
            "---\n",
            "*This document was automatically generated by the HyperCode documentation system.*",
        ]
    )

    return "\n".join(str(line) for line in report)


def update_database_documentation():
    """Update the database documentation."""
    print("🔍 Analyzing codebase...")
    git_info = get_git_info()
    stats = analyze_codebase()

    print("📝 Generating report...")
    report = generate_markdown_report(stats, git_info)

    print(f"💾 Saving report to {REPORT_FILE}...")
    with open(REPORT_FILE, "w", encoding="utf-8") as f:
        f.write(report)

    print("✅ Database documentation updated successfully!")


if __name__ == "__main__":
    update_database_documentation()
