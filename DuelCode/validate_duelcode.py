"""
DuelCode Documentation Validator

This script validates that Markdown files follow the DuelCode documentation standards.
It checks for required sections, formatting, and structure.
"""

import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple, Optional

# Required sections and their validation patterns
REQUIRED_SECTIONS = {
    "Learning Objectives": r"## 🎯 Learning Objective[s]?\n\n(?:- \[ \].+\n)+",
    "Before You Start": r"## 📋 Before You Start \(Checklist\)\n\n(?:- \[ \].+\n)+",
    "Concept Explanation": r"## Part \d+: .+\n\n### 🧠 Concept:",
    "Visual Representation": r"### 📊 Visual Representation\n\n```",
    "Code Example": r"### 💻 Code Example\n\n```"
}

class DuelCodeValidator:
    def __init__(self, file_path: str):
        self.file_path = Path(file_path)
        self.content = self.file_path.read_text(encoding='utf-8')
        self.errors: List[str] = []
        self.warnings: List[str] = []

    def validate_sections(self) -> bool:
        """Check if all required sections are present."""
        all_valid = True
        for section, pattern in REQUIRED_SECTIONS.items():
            if not re.search(pattern, self.content, re.MULTILINE | re.DOTALL):
                self.errors.append(f"Missing or malformed section: {section}")
                all_valid = False
        return all_valid

    def check_formatting(self) -> None:
        """Check for common formatting issues."""
        # Check for proper heading levels
        headings = re.findall(r'^(#{1,6})\s+(.+)$', self.content, re.MULTILINE)
        for i, (hashes, text) in enumerate(headings):
            if i > 0 and len(hashes) > len(headings[i-1][0]) + 1:
                self.warnings.append(
                    f"Heading level jump: '{text}' (skipped a level)"
                )

        # Check for long paragraphs
        paragraphs = re.split(r'\n{2,}', self.content)
        for para in paragraphs:
            if len(para) > 500 and not para.startswith('```') and 'http' not in para:
                self.warnings.append(
                    f"Long paragraph detected (>{len(para)} chars). Consider breaking it down."
                )

    def check_visual_aids(self) -> None:
        """Check for presence of visual aids."""
        if self.content.count('```') < 3:  # At least one code block and one diagram
            self.warnings.append("Consider adding more visual aids or code examples")

    def validate(self) -> Tuple[bool, List[str], List[str]]:
        """Run all validations and return results."""
        self.validate_sections()
        self.check_formatting()
        self.check_visual_aids()
        return (not bool(self.errors), self.errors, self.warnings)

def main():
    if len(sys.argv) != 2:
        print("Usage: python validate_duelcode.py <markdown_file.md>")
        sys.exit(1)

    validator = DuelCodeValidator(sys.argv[1])
    is_valid, errors, warnings = validator.validate()

    if warnings:
        print("\n⚠️  Warnings:")
        for warning in warnings:
            print(f"  - {warning}")

    if errors:
        print("\n❌ Errors:")
        for error in errors:
            print(f"  - {error}")
        print("\nDocumentation does not meet DuelCode standards!")
        sys.exit(1)
    
    print("\n✅ Documentation meets DuelCode standards!")
    sys.exit(0)

if __name__ == "__main__":
    main()
