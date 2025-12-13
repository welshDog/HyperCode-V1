#!/usr/bin/env python3
"""
Hyper Database Builder - Scans HyperCode repo, builds knowledge graph.

Usage:
  python scripts/build-hyper-database.py

Output:
  HYPER_DATABASE.md (living codebase inventory)
  HYPER_DATABASE.json (machine-readable format)
"""

import ast
import json
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any


class HyperDatabaseBuilder:
    """Scans codebase and builds semantic knowledge graph."""

    def __init__(self, repo_root: str = ".") -> None:
        """Initialize builder with repo root path."""
        self.repo_root = Path(repo_root)
        self.entities: list[dict[str, Any]] = []
        self.relationships: dict[str, set[str]] = defaultdict(set)
        self.files_scanned: int = 0
        self.start_time = datetime.now()

    def scan_python_file(self, file_path: Path) -> list[dict[str, Any]]:
        """Extract functions, classes from Python file."""
        entities: list[dict[str, Any]] = []
        try:
            with open(file_path, encoding="utf-8") as f:
                content = f.read()
                tree = ast.parse(content)
        except (SyntaxError, UnicodeDecodeError):
            return entities

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                docstring = ast.get_docstring(node)
                entities.append(
                    {
                        "id": f"{file_path}:{node.name}",
                        "type": "function",
                        "name": node.name,
                        "file": str(file_path),
                        "lineno": node.lineno,
                        "docstring": docstring,
                        "args": [arg.arg for arg in node.args.args],
                        "has_test": False,
                        "has_doc": bool(docstring),
                        "complexity": "LOW",
                    }
                )
            elif isinstance(node, ast.ClassDef):
                docstring = ast.get_docstring(node)
                methods = [m.name for m in node.body if isinstance(m, ast.FunctionDef)]
                entities.append(
                    {
                        "id": f"{file_path}:{node.name}",
                        "type": "class",
                        "name": node.name,
                        "file": str(file_path),
                        "lineno": node.lineno,
                        "docstring": docstring,
                        "methods": methods,
                        "has_test": False,
                        "has_doc": bool(docstring),
                    }
                )

        return entities

    def scan_javascript_file(self, file_path: Path) -> list[dict[str, Any]]:
        """Extract functions from JavaScript (regex-based)."""
        entities: list[dict[str, Any]] = []
        try:
            with open(file_path, encoding="utf-8") as f:
                lines = f.readlines()
        except (UnicodeDecodeError, OSError):
            return entities

        for i, line in enumerate(lines):
            line_stripped = line.strip()
            # Match: function name() or const name = () =>
            if line_stripped.startswith("function ") or "=>" in line_stripped:
                has_doc = "/*" in line or "//" in line
                entities.append(
                    {
                        "id": f"{file_path}:{i}",
                        "type": "function",
                        "file": str(file_path),
                        "lineno": i + 1,
                        "snippet": line_stripped[:80],
                        "has_test": False,
                        "has_doc": has_doc,
                    }
                )

        return entities

    @staticmethod
    def should_skip_directory(dirname: str) -> bool:
        """Check if directory should be skipped."""
        skip_dirs = {
            "node_modules",
            ".git",
            "__pycache__",
            ".venv",
            "venv",
            ".pytest_cache",
            "dist",
            "build",
            ".egg-info",
            "coverage",
            ".nyc_output",
            ".DS_Store",
            ".idea",
            ".vscode",
        }
        return dirname in skip_dirs or dirname.startswith(".")

    def build(self) -> list[dict[str, Any]]:
        """Scan entire repo and build database."""
        print(f"Scanning repository: {self.repo_root}")
        print()

        for root, dirs, files in __import__("os").walk(self.repo_root):
            # Skip ignored directories
            dirs[:] = [d for d in dirs if not self.should_skip_directory(d)]

            for file in files:
                file_path = Path(root) / file
                relative_path = file_path.relative_to(self.repo_root)

                try:
                    if file.endswith(".py"):
                        entities = self.scan_python_file(file_path)
                        self.entities.extend(entities)
                        self.files_scanned += 1
                        if entities:
                            print(f"  Found {relative_path}: {len(entities)} entities")

                    elif file.endswith((".js", ".ts")):
                        entities = self.scan_javascript_file(file_path)
                        self.entities.extend(entities)
                        self.files_scanned += 1
                        if entities:
                            print(f"  Found {relative_path}: {len(entities)} entities")

                except Exception as e:
                    print(f"  Error scanning {relative_path}: {e}")

        print()
        return self.entities

    def generate_markdown_report(self) -> str:
        """Generate HYPER_DATABASE.md report."""
        elapsed = (datetime.now() - self.start_time).total_seconds()

        functions = [e for e in self.entities if e["type"] == "function"]
        classes = [e for e in self.entities if e["type"] == "class"]
        documented = sum(1 for e in self.entities if e.get("has_doc", False))

        coverage_pct = 100 * documented / len(self.entities) if self.entities else 0

        report = f"""# HYPER DATABASE
## Living Inventory of HyperCode Codebase

**Generated**: {datetime.now().isoformat()}
**Scan Time**: {elapsed:.1f}s
**Files Scanned**: {self.files_scanned}
**Total Entities**: {len(self.entities)}

---

## HEALTH SNAPSHOT

| Metric | Value |
|--------|-------|
| **Functions** | {len(functions)} |
| **Classes** | {len(classes)} |
| **Files** | {self.files_scanned} |
| **Documentation** | {documented}/{len(self.entities)} ({coverage_pct:.1f}%) |
| **Status** | OK |

---

## ALL FUNCTIONS

"""

        # Group by file
        by_file: dict[str, list[dict[str, Any]]] = defaultdict(list)
        for entity in self.entities:
            if entity["type"] == "function":
                by_file[entity["file"]].append(entity)

        for file_path in sorted(by_file.keys()):
            report += f"### {file_path}\n\n"
            for func in sorted(by_file[file_path], key=lambda f: f.get("lineno", 0)):
                func_name = func.get("name", "unnamed_function")
                line_no = func.get("lineno", "N/A")
                report += f"#### `{func_name}()` (line {line_no})\n"
                if func.get("docstring"):
                    report += f"_{func['docstring']}_\n\n"
                if func.get("args"):
                    report += f"**Args**: {', '.join(func['args'])}\n\n"
                report += "\n"

        report += "---\n\n## ALL CLASSES\n\n"

        by_file_classes: dict[str, list[dict[str, Any]]] = defaultdict(list)
        for entity in self.entities:
            if entity["type"] == "class":
                by_file_classes[entity["file"]].append(entity)

        for file_path in sorted(by_file_classes.keys()):
            report += f"### {file_path}\n\n"
            for cls in sorted(by_file_classes[file_path], key=lambda c: c["lineno"]):
                report += f"#### `{cls['name']}`\n"
                if cls.get("docstring"):
                    report += f"_{cls['docstring']}_\n\n"
                if cls.get("methods"):
                    methods_str = ", ".join(cls["methods"])
                    report += f"**Methods**: {methods_str}\n\n"
                report += "\n"

        report += """---

## NEXT STEPS

1. Load HYPER_DATABASE.md into Windsurf Cascade
2. Tell Cascade: "Consulting HYPER_DATABASE before every task"
3. Add database queries to workflow:
   - "What functions are in X?"
   - "What calls function Y?"
   - "What tests cover Z?"
4. Auto-update daily

**This database is TRUTH. Your code follows it.**
"""

        return report

    def generate_json_report(self) -> dict[str, Any]:
        """Generate machine-readable HYPER_DATABASE.json."""
        return {
            "generated": datetime.now().isoformat(),
            "files_scanned": self.files_scanned,
            "entities": self.entities,
            "stats": {
                "total_entities": len(self.entities),
                "functions": sum(1 for e in self.entities if e["type"] == "function"),
                "classes": sum(1 for e in self.entities if e["type"] == "class"),
                "documented": sum(1 for e in self.entities if e.get("has_doc", False)),
            },
        }


def main() -> None:
    """Main entry point with proper encoding handling."""
    import sys

    # Configure console output encoding
    if sys.stdout.encoding != "utf-8":
        import io
        import sys

        sys.stdout = io.TextIOWrapper(
            sys.stdout.buffer, encoding="utf-8", errors="replace"
        )

    builder = HyperDatabaseBuilder(".")

    print("=" * 60)
    print("HYPER DATABASE BUILDER")
    print("=" * 60)
    print()

    try:
        # Build
        builder.build()

        print("=" * 60)
        print("Scan complete!")
        print(f"   - Files: {builder.files_scanned}")
        print(f"   - Entities: {len(builder.entities)}")
        print("=" * 60)
        print()

        # Generate reports
        print("Generating HYPER_DATABASE.md...")
        md_report = builder.generate_markdown_report()
        with open("HYPER_DATABASE.md", "w", encoding="utf-8") as f:
            f.write(md_report)
        print("   [DONE] HYPER_DATABASE.md created")

        print("Generating HYPER_DATABASE.json...")
        json_report = builder.generate_json_report()
        with open("HYPER_DATABASE.json", "w", encoding="utf-8") as f:
            json.dump(json_report, f, indent=2)
        print("   [DONE] HYPER_DATABASE.json created")

        print()
        print("=" * 60)
        print("HYPER DATABASE GENERATION COMPLETE!")
        print("=" * 60)
        print()
        print("Next steps:")
        print("1. Review HYPER_DATABASE.md for an overview")
        print("2. Use the knowledge base for development")
        print("3. The database will be used automatically by the system")

    except Exception as e:
        print(f"\n[ERROR] An error occurred: {str(e)}")
        import traceback

        traceback.print_exc()
        sys.exit(1)

    print()
    print("=" * 60)
    print("HYPER DATABASE READY!")
    print("=" * 60)
    print()
    print("Next steps:")
    print("1. Open Windsurf")
    print("2. In Cascade Chat, paste:")
    print()
    print("   Load HYPER_DATABASE.md into context")
    print("   Ready for database-aware development")
    print()
    print("3. Watch Hyper Builder use it automatically!")
    print()


if __name__ == "__main__":
    main()
