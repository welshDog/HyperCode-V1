#!/usr/bin/env python3
"""
Debug the full parsing flow
"""

import os
import sys

sys.path.append(os.path.dirname(__file__))

from visual_syntax_parser import VisualSyntaxParser


def debug_full_parsing():
    """Debug the full parsing flow"""

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

    parser = VisualSyntaxParser()

    print("=== DEBUGGING FULL PARSING FLOW ===")

    # Test line by line
    lines = example_code.split("\n")
    for i, line in enumerate(lines, 1):
        print(f"Line {i}: {repr(line)}")
        annotations = parser._parse_line_annotations(line, i)
        print(f"  Annotations found: {len(annotations)}")
        for ann in annotations:
            print(f"    {ann}")
        print()

    print("=== TESTING FULL PARSE ===")
    functions = parser.parse_content(example_code)
    print(f"Functions found: {len(functions)}")

    for func in functions:
        print(f"Function: {func.name}")
        print(f"Annotations: {len(func.annotations)}")
        for ann in func.annotations:
            print(f"  {ann}")


if __name__ == "__main__":
    debug_full_parsing()
