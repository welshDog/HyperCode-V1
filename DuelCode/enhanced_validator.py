"""
Enhanced DuelCode Validator with additional validation rules.
"""

import re
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


class DuelCodeEnhancedValidator:
    """Enhanced validator with additional rules for DuelCode documentation."""

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
        "html",
        "css",
        "sql",
        "json",
        "yaml",
        "markdown",
        "mermaid",
    }

    # Common programming language file extensions
    CODE_EXTENSIONS = {
        ".py",
        ".js",
        ".ts",
        ".jsx",
        ".tsx",
        ".java",
        ".c",
        ".cpp",
        ".h",
        ".hpp",
        ".cs",
        ".go",
        ".rs",
        ".rb",
        ".php",
        ".swift",
        ".kt",
        ".dart",
        ".html",
        ".css",
        ".scss",
        ".sql",
        ".json",
        ".yaml",
        ".yml",
        ".md",
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
                if re.search(pattern, line, re.IGNORECASE)
            ]
        return self._line_cache[pattern]

    # === New Validation Rules ===

    def validate_code_blocks_have_language(self) -> None:
        """Ensure all code blocks have a specified language."""
        in_code_block = False
        for i, line in enumerate(self.lines):
            if line.startswith("```"):
                if not in_code_block and not line[3:].strip():
                    self._add_result(
                        "Code block is missing a language specification",
                        Severity.ERROR,
                        i,
                    )
                in_code_block = not in_code_block

    def validate_has_visual_representation(self) -> None:
        """Ensure each part has a visual representation."""
        parts = self._find_lines(r"^## Part \d+:")
        visual_reps = self._find_lines(r"^### 📊 Visual Representation")

        if parts and not visual_reps:
            self._add_result(
                "Document contains parts but no visual representations",
                Severity.WARNING,
                0,
            )

    def validate_has_practical_exercise(self) -> None:
        """Ensure each part has a practical exercise."""
        parts = self._find_lines(r"^## Part \d+:")
        exercises = self._find_lines(r"### 🛠️ Exercise")

        if parts and not exercises:
            self._add_result(
                "Consider adding practical exercises for better engagement",
                Severity.INFO,
                0,
            )

    def validate_has_learning_objectives(self) -> None:
        """Ensure learning objectives are present and well-formed."""
        objectives = self._find_lines(r"^## 🎯 Learning Objective")
        if not objectives:
            self._add_result("Missing Learning Objectives section", Severity.ERROR, 0)
            return

        # Check for at least 3 learning objectives
        start_line = objectives[0][0]
        objectives_count = 0
        for i in range(start_line, min(start_line + 20, len(self.lines))):
            if re.match(r"^- \[ \]", self.lines[i]):
                objectives_count += 1

        if objectives_count < 3:
            self._add_result(
                f"Learning Objectives should have at least 3 items (found {objectives_count})",
                Severity.WARNING,
                start_line,
            )

    def validate_has_checklist(self) -> None:
        """Ensure a checklist is present and has items."""
        checklist = self._find_lines(r"^## 📋 Before You Start")
        if not checklist:
            self._add_result("Missing 'Before You Start' checklist", Severity.ERROR, 0)
            return

        # Check for checklist items
        start_line = checklist[0][0]
        checklist_items = 0
        for i in range(start_line, min(start_line + 20, len(self.lines))):
            if re.match(r"^- \[ \]", self.lines[i]):
                checklist_items += 1

        if checklist_items < 3:
            self._add_result(
                f"Checklist should have at least 3 items (found {checklist_items})",
                Severity.WARNING,
                start_line,
            )

    def validate_has_conclusion(self) -> None:
        """Ensure the document has a conclusion section."""
        if not self._find_lines(r"^## 🏁 Conclusion"):
            self._add_result(
                "Consider adding a 'Conclusion' section to summarize key points",
                Severity.INFO,
                len(self.lines) - 1,
            )

    def validate_has_whats_next(self) -> None:
        """Suggest adding a 'What's Next' section."""
        if not self._find_lines(r"^## ➡️ What\'?s Next"):
            self._add_result(
                "Consider adding a 'What's Next' section to guide readers",
                Severity.INFO,
                len(self.lines) - 1,
            )

    def validate_code_quality(self) -> None:
        """Check code quality in code blocks."""
        in_code_block = False
        current_lang = None
        code_block_lines = []

        for i, line in enumerate(self.lines):
            if line.startswith("```"):
                if in_code_block and code_block_lines:
                    self._analyze_code_block(
                        code_block_lines, current_lang, i - len(code_block_lines) - 1
                    )
                    code_block_lines = []
                else:
                    current_lang = line[3:].strip().lower()
                in_code_block = not in_code_block
            elif in_code_block:
                code_block_lines.append((i, line))

    def _analyze_code_block(
        self, lines: List[Tuple[int, str]], lang: str, start_line: int
    ) -> None:
        """Analyze a code block for quality issues."""
        if not lines or not lang:
            return

        # Check for long lines
        for line_num, line in lines:
            if len(line) > 100:  # 100 character line length limit
                self._add_result(
                    "Line exceeds 100 characters (consider breaking it up)",
                    Severity.WARNING,
                    line_num,
                )

        # Language-specific checks
        if lang == "python":
            self._analyze_python_code(lines, start_line)
        elif lang in ("javascript", "typescript"):
            self._analyze_javascript_code(lines, start_line)

    def _analyze_python_code(
        self, lines: List[Tuple[int, str]], start_line: int
    ) -> None:
        """Python-specific code analysis."""
        for i, (line_num, line) in enumerate(lines):
            # Check for print statements (suggest using logging in production code)
            if re.match(r"^\s*print\(", line):
                self._add_result(
                    "Consider using logging instead of print() for production code",
                    Severity.INFO,
                    line_num,
                )

            # Check for TODO comments
            if "TODO" in line.upper() and not line.strip().startswith("#"):
                self._add_result(
                    "TODO comment found - make sure to address it",
                    Severity.INFO,
                    line_num,
                )

    def _analyze_javascript_code(
        self, lines: List[Tuple[int, str]], start_line: int
    ) -> None:
        """JavaScript/TypeScript-specific code analysis."""
        for i, (line_num, line) in enumerate(lines):
            # Check for console.log
            if "console.log(" in line and not line.strip().startswith("//"):
                self._add_result(
                    "Consider removing or commenting out console.log statements in production code",
                    Severity.INFO,
                    line_num,
                )

    def validate_has_glossary(self) -> None:
        """Suggest adding a glossary for technical terms."""
        technical_terms = [
            "API",
            "REST",
            "GraphQL",
            "OAuth",
            "JWT",
            "Docker",
            "Kubernetes",
            "Microservices",
            "CI/CD",
            "TDD",
            "BDD",
            "MVC",
            "ORM",
            "SQL",
            "NoSQL",
        ]

        found_terms = []
        for term in technical_terms:
            if self._find_lines(r"\b" + re.escape(term) + r"\b"):
                found_terms.append(term)

        if found_terms and not self._find_lines(r"^## 📚 Glossary"):
            self._add_result(
                f"Document contains technical terms ({', '.join(found_terms[:3])}...). "
                "Consider adding a Glossary section.",
                Severity.INFO,
                0,
            )

    def validate_has_see_also(self) -> None:
        """Suggest adding a 'See Also' section with related resources."""
        if not self._find_lines(r"^## 🔗 See Also"):
            self._add_result(
                "Consider adding a 'See Also' section with links to related resources",
                Severity.INFO,
                len(self.lines) - 1,
            )

    def validate_has_faq(self) -> None:
        """Suggest adding an FAQ section."""
        question_marks = self._find_lines(r"\?")
        if question_marks and not self._find_lines(r"^## ❓ FAQ"):
            self._add_result(
                "Document contains questions. Consider adding an FAQ section",
                Severity.INFO,
                len(self.lines) - 1,
            )

    def validate_has_acknowledgments(self) -> None:
        """Suggest adding an acknowledgments section."""
        if not self._find_lines(r"^## 🙏 Acknowledgments"):
            self._add_result(
                "Consider adding an Acknowledgments section to credit contributors",
                Severity.INFO,
                len(self.lines) - 1,
            )

    def validate_all(self) -> List[ValidationResult]:
        """Run all validations."""
        # Structure validations
        self.validate_has_learning_objectives()
        self.validate_has_checklist()
        self.validate_has_visual_representation()
        self.validate_has_practical_exercise()
        self.validate_has_conclusion()
        self.validate_has_whats_next()

        # Code quality validations
        self.validate_code_blocks_have_language()
        self.validate_code_quality()

        # Content suggestions
        self.validate_has_glossary()
        self.validate_has_see_also()
        self.validate_has_faq()
        self.validate_has_acknowledgments()

        return self.results


def print_validation_results(results: List[ValidationResult]) -> None:
    """Print validation results in a user-friendly format."""
    if not results:
        print("✅ No issues found!")
        return

    # Group by severity
    by_severity = {Severity.ERROR: [], Severity.WARNING: [], Severity.INFO: []}

    for result in results:
        by_severity[result.severity].append(result)

    # Print by severity
    for severity, results in by_severity.items():
        if not results:
            continue

        print(f"\n{severity.name}S ({len(results)}):")
        print("=" * (len(severity.name) + 10))

        for result in results:
            location = f"line {result.line}" if result.line is not None else "document"
            if result.col is not None:
                location += f":{result.col}"
            print(f"• {result.message} (at {location})")


def main() -> None:
    """Main entry point for the enhanced validator."""
    import sys

    if len(sys.argv) != 2:
        print("Usage: python enhanced_validator.py <markdown_file>")
        sys.exit(1)

    file_path = sys.argv[1]
    if not Path(file_path).exists():
        print(f"Error: File '{file_path}' not found")
        sys.exit(1)

    validator = DuelCodeEnhancedValidator(file_path)
    results = validator.validate_all()

    print(f"Validating: {file_path}")
    print("-" * 50)

    print_validation_results(results)

    has_errors = any(r.severity == Severity.ERROR for r in results)
    has_warnings = any(r.severity == Severity.WARNING for r in results)

    if has_errors:
        print("\n❌ Validation failed with errors")
        sys.exit(1)
    elif has_warnings:
        print("\n⚠️  Validation passed with warnings")
    else:
        print("\n✅ Validation passed successfully!")


if __name__ == "__main__":
    main()
