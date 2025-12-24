#!/usr/bin/env python3
"""
Debug the Visual Syntax Parser - Find what's wrong with annotation detection
"""

import os
import sys

sys.path.append(os.path.dirname(__file__))

from visual_syntax_parser import VisualSyntaxParser


def debug_annotation_detection():
    """Debug why annotations aren't being detected"""

    # Test simple annotation
    test_line = '🔍 @verifiable("formal_proof")'

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

    # Test with the full example
    print("\n" + "=" * 50)
    print("Testing full example:")

    example_code = """🔍 @verifiable("formal_proof")
📐 @ensures("output.shape == (batch, classes)")
📋 @requires("input.shape[1] == features")
🧠 @intent("Classify input features")
🎯 @accessibility("high_contrast", "dyslexia_font")
function classifier(input: Tensor[batch, features]) -> Tensor[batch, classes] {
    🎨 weights = initialize(features, classes)
    ⚡ logits = matmul(input, weights)
    🔄 return softmax(logits)
}"""

    lines = example_code.split("\n")
    for i, line in enumerate(lines, 1):
        annotations = parser._parse_line_annotations(line, i)
        if annotations:
            print(f"Line {i}: {line}")
            for ann in annotations:
                print(f"  -> {ann}")


if __name__ == "__main__":
    debug_annotation_detection()
