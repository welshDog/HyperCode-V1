#!/usr/bin/env python3
"""
Simple debug without emoji characters
"""

import os
import sys

sys.path.append(os.path.dirname(__file__))

from visual_syntax_parser import VisualSyntaxParser


def debug_simple():
    """Debug without emoji characters"""

    # Test simple annotation
    test_line = '@verifiable("formal_proof")'

    parser = VisualSyntaxParser()

    print("Debug: Testing annotation detection")
    print(f"Test line: {test_line}")

    # Test each pattern
    for emoji, pattern_data in parser.semantic_patterns.items():
        pattern = pattern_data["regex"]
        matches = pattern.findall(test_line)
        print(f"Pattern {emoji}: {matches}")

    # Test the full line parsing
    annotations = parser._parse_line_annotations(test_line, 1)
    print(f"\nParsed annotations: {len(annotations)}")
    for ann in annotations:
        print(f"  {ann}")

    # Test with emoji line
    print("\n" + "=" * 50)
    test_emoji_line = '🔍 @verifiable("formal_proof")'
    print(f"Testing emoji line: {test_emoji_line}")

    annotations = parser._parse_line_annotations(test_emoji_line, 1)
    print(f"Parsed annotations: {len(annotations)}")
    for ann in annotations:
        print(f"  {ann}")


if __name__ == "__main__":
    debug_simple()
