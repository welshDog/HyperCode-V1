"""
Enhanced DuelCode Documentation Validator

This script provides comprehensive validation for DuelCode documentation format,
ensuring consistency and quality across all DuelCode tutorials.
"""

import re
import sys
from dataclasses import dataclass
from enum import Enum, auto
from pathlib import Path
from typing import Dict, List, Optional, Tuple


class Severity(Enum):
    ERROR = auto()
    WARNING = auto()
    INFO = auto()


@dataclass
class ValidationResult:
    message: str
    severity: Severity
    line: Optional[int] = None
    col: Optional[int] = None


class DuelCodeValidator:
    """Validates DuelCode documentation files against the required format."""

    # Supported programming languages for code blocks
    SUPPORTED_LANGUAGES = {
        "python",
        "javascript",
        "typescript",
        "java",
        "c",
        "cpp",
        "csharp",
        "go",
        "rust",
        "ruby",
        "php",
        "swift",
        "kotlin",
        "dart",
    }

    def __init__(self, file_path: str):
        self.file_path = Path(file_path)
        self.content = self.file_path.read_text(encoding="utf-8")
        self.lines = self.content.split("\n")
        self.results: List[ValidationResult] = []
        self._line_cache: Dict[str, List[Tuple[int, str]]] = {}

    def _add_result(
        self, message: str, severity: Severity, line: Optional[int] = None
    ) -> None:
        """Add a validation result with proper line number."""
        col = None
        if line is not None and 0 <= line < len(self.lines):
            col = (
                len(self.lines[line]) - len(self.lines[line].lstrip()) + 1
                if self.lines[line].strip()
                else 1
            )
        self.results.append(ValidationResult(message, severity, line, col))

    def _find_lines(self, pattern: str) -> List[Tuple[int, str]]:
        """Find all lines matching the pattern with their line numbers."""
        if pattern not in self._line_cache:
            self._line_cache[pattern] = [
                (i, line)
                for i, line in enumerate(self.lines)
                if re.search(pattern, line)
            ]
        return self._line_cache[pattern]

    def validate(self) -> bool:
        """Run all validation checks."""
        self.validate_structure()
        self.validate_headings()
        self.validate_code_blocks()
        self.validate_checklists()
        self.validate_visual_elements()
        self.validate_links()

        # Return True if there are no errors (warnings are allowed)
        return not any(r.severity == Severity.ERROR for r in self.results)

    def validate_structure(self) -> None:
        """Validate the overall document structure."""
        # Check for required top-level sections
        required_sections = [
            (r"^# .+", "Document title (H1)"),
            (r"^## 🎯 Learning Objective", "Learning Objectives section"),
            (r"^## 📋 Before You Start", "Before You Start checklist"),
            (r"^## Part \d+:", "At least one Part section"),
        ]

        for pattern, name in required_sections:
            if not self._find_lines(pattern):
                self._add_result(f"Missing required section: {name}", Severity.ERROR)

        # Check for proper section order
        section_order = [
            (r"^# ", "Document title"),
            (r"^## 🎯", "Learning Objectives"),
            (r"^## 📋", "Before You Start"),
            (r"^## Part 1:", "First Part section"),
        ]

        last_index = -1
        for pattern, name in section_order:
            matches = self._find_lines(pattern)
            if not matches:
                continue
            current_index = matches[0][0]
            if current_index <= last_index:
                self._add_result(
                    f"Section out of order: {name} appears after a section that should come later",
                    Severity.ERROR,
                    current_index,
                )
            last_index = current_index

    def validate_headings(self) -> None:
        """Validate heading hierarchy and formatting."""
        headings = []
        for i, line in enumerate(self.lines):
            if match := re.match(r"^(#{1,6})\s+(.+)$", line):
                level = len(match.group(1))
                text = match.group(2).strip()
                headings.append((i, level, text))

                # Check for proper heading capitalization (first word and proper nouns)
                if not text[0].isupper():
                    self._add_result(
                        "Headings should start with a capital letter",
                        Severity.WARNING,
                        i,
                    )

                # Check for proper heading formatting (no trailing punctuation)
                if text.endswith((".", ":", ";", ",")):
                    self._add_result(
                        "Headings should not end with punctuation", Severity.WARNING, i
                    )

        # Check heading hierarchy
        prev_level = 0
        for i, (line_num, level, text) in enumerate(headings):
            if i == 0 and level != 1:
                self._add_result(
                    "First heading should be a level 1 heading (#)",
                    Severity.ERROR,
                    line_num,
                )

            if level > prev_level + 1:
                self._add_result(
                    f"Heading level jumps from {prev_level} to {level}",
                    Severity.ERROR,
                    line_num,
                )

            prev_level = level

    def validate_code_blocks(self) -> None:
        """Validate code blocks for proper formatting and language specification."""
        in_code_block = False
        current_lang = None
        code_block_start = 0

        for i, line in enumerate(self.lines):
            # Check for code block start
            if line.startswith("```"):
                if not in_code_block:
                    in_code_block = True
                    code_block_start = i
                    # Get language if specified
                    lang = line[3:].strip()
                    if lang and not any(
                        lang.lower() == l.lower() for l in self.SUPPORTED_LANGUAGES
                    ):
                        self._add_result(
                            f"Unsupported code language: {lang}", Severity.WARNING, i
                        )
                    current_lang = lang.lower() if lang else None
                else:
                    # Check for empty code blocks
                    if i - code_block_start <= 1:  # Only the opening line
                        self._add_result(
                            "Empty code block", Severity.WARNING, code_block_start
                        )
                    in_code_block = False

            # Inside code block checks
            elif in_code_block and current_lang == "python":
                # Example: Check for Python-specific issues
                if "    " in line and "\t" in line:
                    self._add_result(
                        "Inconsistent indentation (mixing tabs and spaces)",
                        Severity.ERROR,
                        i,
                    )

    def validate_checklists(self) -> None:
        """Validate checklist items in the document."""
        in_checklist = False
        checklist_items = []

        for i, line in enumerate(self.lines):
            # Detect checklist section
            if line.strip() == "## 📋 Before You Start":
                in_checklist = True
                continue
            if in_checklist and line.startswith("## "):
                in_checklist = False
                break

            if in_checklist and line.strip().startswith("- [ ]"):
                item = line.strip()[5:].strip()
                if not item.endswith("."):
                    self._add_result(
                        "Checklist items should end with a period", Severity.WARNING, i
                    )
                if not item[0].isupper():
                    self._add_result(
                        "Checklist items should start with a capital letter",
                        Severity.WARNING,
                        i,
                    )
                checklist_items.append((i, item))

        if len(checklist_items) < 3:
            self._add_result(
                "Checklist should have at least 3 items",
                Severity.WARNING,
                0,  # Will be adjusted to the checklist section
            )

    def validate_visual_elements(self) -> None:
        """Validate visual elements like diagrams, images, etc."""
        # Check for visual representation sections
        visual_sections = self._find_lines(r"^### 📊 Visual Representation")

        for line_num, _ in visual_sections:
            # Check if there's content after the visual representation heading
            has_content = False
            for i in range(line_num + 1, min(line_num + 5, len(self.lines))):
                if self.lines[i].strip() and not self.lines[i].startswith("```"):
                    has_content = True
                    break

            if not has_content:
                self._add_result(
                    "Visual Representation section is empty", Severity.WARNING, line_num
                )

    def validate_links(self) -> None:
        """Validate internal and external links."""
        # Check for broken markdown links
        for i, line in enumerate(self.lines):
            # Check for markdown links [text](url)
            for match in re.finditer(r"\[(?P<text>[^\]]+)\]\((?P<url>[^)]+)\)", line):
                url = match.group("url")
                # Skip anchor links for now
                if url.startswith("#"):
                    continue

                # Check for empty link text
                if not match.group("text").strip():
                    self._add_result("Link text cannot be empty", Severity.ERROR, i)

                # Check for URLs with spaces
                if " " in url:
                    self._add_result(f"URL contains spaces: {url}", Severity.ERROR, i)


def print_validation_results(validator: DuelCodeValidator) -> None:
    """Print validation results in a user-friendly format."""
    if not validator.results:
        print("✅ No issues found!")
        return

    # Group results by severity
    by_severity: Dict[Severity, List[ValidationResult]] = {
        Severity.ERROR: [],
        Severity.WARNING: [],
        Severity.INFO: [],
    }

    for result in validator.results:
        by_severity[result.severity].append(result)

    # Print errors first, then warnings, then info
    for severity, results in by_severity.items():
        if not results:
            continue

        print(f"\n{severity.name}S ({(len(results))}):")
        print("=" * (len(severity.name) + 10))

        for result in results:
            location = (
                f"line {result.line}" if result.line is not None else "unknown location"
            )
            if result.col is not None:
                location += f":{result.col}"
            print(f"• {result.message} (at {location})")


def main() -> None:
    """Main entry point for the validator."""
    if len(sys.argv) != 2:
        print("Usage: python duelcode_validator.py <markdown_file>")
        sys.exit(1)

    file_path = sys.argv[1]
    if not Path(file_path).exists():
        print(f"Error: File '{file_path}' not found")
        sys.exit(1)

    validator = DuelCodeValidator(file_path)
    is_valid = validator.validate()

    print(f"Validating: {file_path}")
    print("-" * 50)

    print_validation_results(validator)

    if not is_valid:
        print("\n❌ Validation failed with errors")
        sys.exit(1)
    elif any(r.severity == Severity.WARNING for r in validator.results):
        print("\n⚠️  Validation passed with warnings")
    else:
        print("\n✅ Validation passed successfully!")


if __name__ == "__main__":
    main()
