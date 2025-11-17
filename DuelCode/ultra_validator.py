"""
Ultra-Enhanced DuelCode Validator with advanced validation rules.
"""

import re
from dataclasses import dataclass
from enum import Enum, auto
from pathlib import Path
from typing import Dict, List, Optional, Tuple
import json


class Severity(Enum):
    ERROR = auto()
    WARNING = auto()
    INFO = auto()
    SUGGESTION = auto()


@dataclass
class ValidationResult:
    message: str
    severity: Severity
    line: Optional[int] = None
    col: Optional[int] = None
    suggestion: Optional[str] = None


class DuelCodeUltraValidator:
    """Ultra-enhanced validator with comprehensive rules for DuelCode documentation."""
    
    SUPPORTED_LANGUAGES = {
        "python", "javascript", "typescript", "java", "c", "cpp", 
        "csharp", "go", "rust", "ruby", "php", "swift", "kotlin",
        "dart", "html", "css", "sql", "json", "yaml", "markdown",
        "mermaid", "hypercode", "bash", "text", "ascii", "shell",
        "dockerfile", "makefile", "ini", "toml", "xml"
    }

    # Required sections for complete tutorials
    REQUIRED_SECTIONS = {
        "objective", "checklist", "learning objectives", 
        "visual representation", "code examples", "exercises",
        "conclusion", "what's next"
    }
    
    # Recommended sections
    RECOMMENDED_SECTIONS = {
        "faq", "see also", "glossary", "acknowledgments",
        "troubleshooting", "resources", "prerequisites"
    }

    def __init__(self, file_path: str):
        self.file_path = Path(file_path)
        self.content = self.file_path.read_text(encoding="utf-8")
        self.lines = self.content.split("\n")
        self.results: List[ValidationResult] = []
        self._line_cache: Dict[str, List[Tuple[int, str]]] = {}

    def _add_result(
        self, 
        message: str, 
        severity: Severity, 
        line: Optional[int] = None,
        suggestion: Optional[str] = None
    ) -> None:
        self.results.append(ValidationResult(message, severity, line, suggestion=suggestion))

    def _find_lines(self, pattern: str) -> List[Tuple[int, str]]:
        if pattern in self._line_cache:
            return self._line_cache[pattern]
        
        matches = []
        for i, line in enumerate(self.lines, 1):
            if re.search(pattern, line, re.IGNORECASE):
                matches.append((i, line))
        
        self._line_cache[pattern] = matches
        return matches

    def validate_code_blocks_have_language(self) -> None:
        """Validate all code blocks have language specifications."""
        code_block_pattern = r"^```(\w+)?$"
        in_code_block = False
        block_start_line = None
        
        for i, line in enumerate(self.lines, 1):
            if line.strip().startswith("```"):
                if not in_code_block:
                    # Start of code block
                    lang_match = re.match(r"^```(\w+)$", line.strip())
                    if not lang_match or not lang_match.group(1):
                        self._add_result(
                            "Code block is missing a language specification",
                            Severity.ERROR,
                            i,
                            suggestion="Add a language identifier after the opening ``` (e.g., ```python)"
                        )
                    elif lang_match.group(1).lower() not in self.SUPPORTED_LANGUAGES:
                        self._add_result(
                            f"Unsupported language '{lang_match.group(1)}'",
                            Severity.WARNING,
                            i,
                            suggestion=f"Use one of: {', '.join(sorted(self.SUPPORTED_LANGUAGES))}"
                        )
                    block_start_line = i
                    in_code_block = True
                else:
                    # End of code block
                    in_code_block = False

    def validate_has_visual_representation(self) -> None:
        """Check for visual elements like diagrams, charts, or ASCII art."""
        visual_patterns = [
            r"```mermaid",
            r"```ascii",
            r"┌|└|┐|┘|─|│",  # Box drawing characters
            r"▄|█|▀|░",      # Block characters
            r"→|←|↑|↓",      # Arrows
        ]
        
        has_visual = any(self._find_lines(pattern) for pattern in visual_patterns)
        
        if not has_visual:
            self._add_result(
                "Consider adding visual representations (diagrams, charts, ASCII art)",
                Severity.INFO,
                suggestion="Add visual elements to improve understanding"
            )

    def validate_has_practical_exercise(self) -> None:
        """Check for practical exercises or challenges."""
        exercise_patterns = [
            r"###\s+challenge",
            r"###\s+exercise",
            r"###\s+try\s+it\s+yourself",
            r"##\s+exercise",
            r"##\s+practice",
            r"\*\*challenge\*\*",
            r"\*\*exercise\*\*",
        ]
        
        has_exercise = any(self._find_lines(pattern) for pattern in exercise_patterns)
        
        if not has_exercise:
            self._add_result(
                "Consider adding practical exercises for better engagement",
                Severity.INFO,
                suggestion="Add hands-on exercises or challenges"
            )

    def validate_has_learning_objectives(self) -> None:
        """Check for learning objectives section."""
        objective_patterns = [
            r"##\s+🎯\s+learning\s+objectives",
            r"##\s+learning\s+objectives",
            r"##\s+objectives",
            r"##\s+what\s+you'll\s+learn",
            r"###\s+🎯\s+learning\s+objectives",
            r"###\s+learning\s+objectives",
            r"###\s+objectives",
        ]
        
        has_objectives = any(self._find_lines(pattern) for pattern in objective_patterns)
        
        if not has_objectives:
            self._add_result(
                "Consider adding learning objectives",
                Severity.INFO,
                suggestion="Add a section outlining what readers will learn"
            )

    def validate_has_checklist(self) -> None:
        """Check for checklist elements."""
        checklist_patterns = [
            r"-\s*\[.*?\]",  # Markdown checkbox
            r"☐|☑|☒",       # Unicode checkboxes
            r"✓|✗",         # Check marks
            r"checklist",
            r"prerequisites",
        ]
        
        has_checklist = any(self._find_lines(pattern) for pattern in checklist_patterns)
        
        if not has_checklist:
            self._add_result(
                "Consider adding a checklist for prerequisites or objectives",
                Severity.INFO,
                suggestion="Add checkboxes or checklist elements"
            )

    def validate_has_conclusion(self) -> None:
        """Check for conclusion section."""
        conclusion_patterns = [
            r"##\s+🎉\s+conclusion",
            r"##\s+conclusion",
            r"##\s+summary",
            r"##\s+wrap\s+up",
            r"###\s+🎉\s+conclusion",
            r"###\s+conclusion",
            r"###\s+summary",
        ]
        
        has_conclusion = any(self._find_lines(pattern) for pattern in conclusion_patterns)
        
        if not has_conclusion:
            self._add_result(
                "Consider adding a 'Conclusion' section to summarize key points",
                Severity.INFO,
                suggestion="Add a conclusion to reinforce learning"
            )

    def validate_has_whats_next(self) -> None:
        """Check for 'What's Next' section."""
        next_patterns = [
            r"##\s+🚀\s+what's\s+next",
            r"##\s+what's\s+next",
            r"##\s+next\s+steps",
            r"##\s+continue\s+learning",
            r"###\s+🚀\s+what's\s+next",
            r"###\s+what's\s+next",
            r"###\s+next\s+steps",
        ]
        
        has_next = any(self._find_lines(pattern) for pattern in next_patterns)
        
        if not has_next:
            self._add_result(
                "Consider adding a 'What's Next' section to guide readers",
                Severity.INFO,
                suggestion="Add next steps for continued learning"
            )

    def validate_code_quality(self) -> None:
        """Validate code block quality and best practices."""
        in_code_block = False
        current_lang = None
        block_start_line = None
        block_lines = []
        
        for i, line in enumerate(self.lines, 1):
            if line.strip().startswith("```"):
                if not in_code_block:
                    # Start of code block
                    lang_match = re.match(r"^```(\w+)$", line.strip())
                    current_lang = lang_match.group(1).lower() if lang_match else None
                    block_start_line = i
                    in_code_block = True
                    block_lines = []
                else:
                    # End of code block - validate
                    if current_lang and block_lines:
                        self._validate_code_block_content(
                            block_lines, current_lang, block_start_line
                        )
                    in_code_block = False
                    current_lang = None
            elif in_code_block:
                block_lines.append((i, line))

    def _validate_code_block_content(self, block_lines: List[Tuple[int, str]], lang: str, start_line: int) -> None:
        """Validate specific code block content based on language."""
        content = "\n".join(line for _, line in block_lines)
        
        # Language-specific validations
        if lang == "python":
            # Check for common Python patterns
            if "print(" in content and not re.search(r'print\s*\(\s*["\']', content):
                self._add_result(
                    "Consider using f-strings or formatted output",
                    Severity.SUGGESTION,
                    start_line,
                    suggestion="Use f-strings for better readability: print(f'Value: {variable}')"
                )
        
        elif lang == "hypercode":
            # Check for Brainfuck/HyperCode best practices
            if content.count(".") > content.count("+"):
                self._add_result(
                    "More output commands than increments - possible logic error",
                    Severity.WARNING,
                    start_line,
                    suggestion="Ensure memory cells are properly initialized before output"
                )
        
        # General code quality checks
        if len(content.split("\n")) > 20:
            self._add_result(
                "Large code block - consider breaking into smaller examples",
                Severity.SUGGESTION,
                start_line,
                suggestion="Split complex code into multiple smaller examples"
            )

    def validate_has_glossary(self) -> None:
        """Check for glossary section."""
        glossary_patterns = [
            r"##\s+🎓\s+glossary",
            r"##\s+glossary",
            r"##\s+terminology",
            r"###\s+🎓\s+glossary",
            r"###\s+glossary",
            r"###\s+terminology",
        ]
        
        has_glossary = any(self._find_lines(pattern) for pattern in glossary_patterns)
        
        if not has_glossary:
            self._add_result(
                "Consider adding a glossary for technical terms",
                Severity.INFO,
                suggestion="Define key terms in a glossary section"
            )

    def validate_has_see_also(self) -> None:
        """Check for 'See Also' section."""
        see_also_patterns = [
            r"##\s+📚\s+see\s+also",
            r"##\s+see\s+also",
            r"##\s+related\s+resources",
            r"##\s+further\s+reading",
            r"###\s+📚\s+see\s+also",
            r"###\s+see\s+also",
        ]
        
        has_see_also = any(self._find_lines(pattern) for pattern in see_also_patterns)
        
        if not has_see_also:
            self._add_result(
                "Consider adding a 'See Also' section with links to related resources",
                Severity.INFO,
                suggestion="Add references to related tutorials or documentation"
            )

    def validate_has_faq(self) -> None:
        """Check for FAQ section."""
        faq_patterns = [
            r"##\s+❓\s+faq",
            r"##\s+faq",
            r"##\s+frequently\s+asked\s+questions",
            r"###\s+❓\s+faq",
            r"###\s+faq",
            r"\?\s+",  # Question patterns
        ]
        
        has_faq = any(self._find_lines(pattern) for pattern in faq_patterns)
        
        # Also check for question marks in headings
        question_headings = self._find_lines(r"\?\s*$")
        if not has_faq and not question_headings:
            self._add_result(
                "Document contains questions. Consider adding an FAQ section",
                Severity.INFO,
                suggestion="Add FAQ for common questions"
            )

    def validate_has_acknowledgments(self) -> None:
        """Check for acknowledgments section."""
        ack_patterns = [
            r"##\s+🙏\s+acknowledgments?",
            r"##\s+acknowledgments?",
            r"##\s+credits?",
            r"##\s+thanks?",
            r"###\s+🙏\s+acknowledgments?",
            r"###\s+acknowledgments?",
        ]
        
        has_ack = any(self._find_lines(pattern) for pattern in ack_patterns)
        
        if not has_ack:
            self._add_result(
                "Consider adding an Acknowledgments section to credit contributors",
                Severity.INFO,
                suggestion="Acknowledge contributors and references"
            )

    def validate_accessibility(self) -> None:
        """Check for accessibility features."""
        # Check for alt text in images
        img_patterns = self._find_lines(r"!\[.*?\]\(.*?\)")
        for line_no, line in img_patterns:
            if not re.match(r"!\[.*?\].*?\(.*?\)", line) or line.startswith("![]("):
                self._add_result(
                    "Image missing alt text",
                    Severity.WARNING,
                    line_no,
                    suggestion="Add descriptive alt text for accessibility"
                )
        
        # Check for color-blind friendly indicators
        if "red" in self.content.lower() or "green" in self.content.lower():
            self._add_result(
                "Consider using patterns/shapes instead of just colors for indicators",
                Severity.SUGGESTION,
                suggestion="Use icons or patterns in addition to colors"
            )

    def validate_interactive_elements(self) -> None:
        """Check for interactive elements."""
        interactive_patterns = [
            r"<details>",
            r"<summary>",
            r"```{.*,.*}",  # Jupyter notebook cells
            r"\[.*\]\(#.*\)",  # Internal links
        ]
        
        has_interactive = any(self._find_lines(pattern) for pattern in interactive_patterns)
        
        if not has_interactive:
            self._add_result(
                "Consider adding interactive elements (collapsible sections, links)",
                Severity.SUGGESTION,
                suggestion="Add interactive elements to improve engagement"
            )

    def validate_all(self) -> List[ValidationResult]:
        """Run all validations and return results."""
        self.results = []
        
        # Core validations
        self.validate_code_blocks_have_language()
        self.validate_has_visual_representation()
        self.validate_has_practical_exercise()
        self.validate_has_learning_objectives()
        self.validate_has_checklist()
        self.validate_has_conclusion()
        self.validate_has_whats_next()
        self.validate_code_quality()
        
        # Enhanced validations
        self.validate_has_glossary()
        self.validate_has_see_also()
        self.validate_has_faq()
        self.validate_has_acknowledgments()
        self.validate_accessibility()
        self.validate_interactive_elements()
        
        return self.results

    def print_results(self) -> None:
        """Print validation results in a formatted way."""
        if not self.results:
            print("✅ All validations passed!")
            return
        
        # Group by severity
        by_severity = {}
        for result in self.results:
            if result.severity not in by_severity:
                by_severity[result.severity] = []
            by_severity[result.severity].append(result)
        
        # Print in order of severity
        severity_order = [Severity.ERROR, Severity.WARNING, Severity.INFO, Severity.SUGGESTION]
        severity_names = {
            Severity.ERROR: "ERRORS",
            Severity.WARNING: "WARNINGS", 
            Severity.INFO: "INFOS",
            Severity.SUGGESTION: "SUGGESTIONS"
        }
        
        for severity in severity_order:
            if severity in by_severity:
                print(f"\n{severity_names[severity]} ({len(by_severity[severity])}):")
                print("=" * (len(severity_names[severity]) + 5))
                for result in by_severity[severity]:
                    location = f" (at line {result.line})" if result.line else ""
                    print(f"• {result.message}{location}")
                    if result.suggestion:
                        print(f"  💡 {result.suggestion}")
        
        # Summary
        total_issues = len(self.results)
        errors = len(by_severity.get(Severity.ERROR, []))
        warnings = len(by_severity.get(Severity.WARNING, []))
        
        if errors > 0:
            print(f"\n❌ Validation failed with {errors} error(s)")
        elif warnings > 0:
            print(f"\n⚠️  Validation passed with {warnings} warning(s)")
        else:
            print(f"\n✅ Validation passed with {total_issues} info/suggestion(s)")


def main():
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python ultra_validator.py <markdown_file>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    validator = DuelCodeUltraValidator(file_path)
    results = validator.validate_all()
    validator.print_results()
    
    # Exit with error code if there are errors
    errors = sum(1 for r in results if r.severity == Severity.ERROR)
    sys.exit(1 if errors > 0 else 0)


if __name__ == "__main__":
    main()
