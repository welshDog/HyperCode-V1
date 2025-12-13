#!/usr/bin/env python3
"""
ASCII-only debug
"""

import os
import sys

sys.path.append(os.path.dirname(__file__))

import re


def test_regex_patterns():
    """Test regex patterns directly"""

    # Test pattern
    pattern = re.compile(r"@🔍\s*\((.*?)\)")

    test_lines = [
        '@verifiable("formal_proof")',
        "@verifiable(formal_proof)",
        '@🔍("formal_proof")',
        "@🔍(formal_proof)",
        '🔍 @🔍("formal_proof")',
    ]

    print("Testing regex patterns:")
    for line in test_lines:
        matches = pattern.findall(line)
        print(f"Line: {line}")
        print(f"Matches: {matches}")
        print()


if __name__ == "__main__":
    test_regex_patterns()
