"""
Test script for the DuelCode validator.
"""

import sys
from pathlib import Path

from duelcode_validator import DuelCodeValidator, print_validation_results


def test_valid_file() -> bool:
    """Test with a valid DuelCode file."""
    test_file = Path("test_valid.md")
    test_file.write_text("""# Sample DuelCode Tutorial

## 🎯 Learning Objectives

- [ ] Understand the basics of DuelCode
- [ ] Learn how to validate DuelCode files
- [ ] Create your own DuelCode tutorials

## 📋 Before You Start (Checklist)

- [ ] Install Python 3.8+
- [ ] Install required packages
- [ ] Read the documentation

## Part 1: Introduction

### 🧠 Concept: What is DuelCode?

DuelCode is a documentation format that combines explanations with code.

### 📊 Visual Representation

```mermaid
graph TD
    A[Start] --> B{Is it?}
    B -->|Yes| C[OK]
    B -->|No| D[Rethink]
```

### 💻 Code Example

```python
def hello():
    print("Hello, DuelCode!")
```
""", encoding="utf-8")

    validator = DuelCodeValidator(str(test_file))
    is_valid = validator.validate()

    print(f"Testing valid file: {test_file}")
    print("-" * 50)
    print_validation_results(validator)

    test_file.unlink()
    return is_valid

def test_invalid_file() -> bool:
    """Test with an invalid DuelCode file."""
    test_file = Path("test_invalid.md")
    test_file.write_text("""# Missing Sections

This file is missing required sections.

```python
def bad():
    pass  # No language specified
""")

    validator = DuelCodeValidator(str(test_file))
    is_valid = validator.validate()

    print(f"\nTesting invalid file: {test_file}")
    print("-" * 50)
    print_validation_results(validator)

    test_file.unlink()
    return is_valid

def main() -> int:
    """Run the test suite."""
    print("Running DuelCode Validator Tests")
    print("=" * 50)

    valid_passed = test_valid_file()
    invalid_failed = not test_invalid_file()

    print("\nTest Summary:")
    print(f"✅ Valid file test: {'PASSED' if valid_passed else 'FAILED'}")
    print(f"❌ Invalid file test: {'PASSED' if invalid_failed else 'FAILED'}")

    return 0 if (valid_passed and invalid_failed) else 1

if __name__ == "__main__":
    sys.exit(main())
