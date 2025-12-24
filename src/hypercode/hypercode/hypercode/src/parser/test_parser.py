#!/usr/bin/env python3
"""
Test the Visual Syntax Parser - First Click Moment Demo
"""

import os
import sys

sys.path.append(os.path.dirname(__file__))

from visual_syntax_parser import VisualSyntaxParser


def test_first_click_moment():
    """Test the parser with the first click moment example"""

    # Example HyperCode code
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
    functions = parser.parse_content(example_code)

    print("Visual Syntax Parser Results:")
    print(f"Found {len(functions)} functions")

    for func in functions:
        print(f"\nFunction: {func.name}")
        print(f"Annotations: {len(func.annotations)}")
        for annotation in func.annotations:
            print(f"  {annotation}")

    # Generate summary
    summary = parser.extract_semantic_summary(functions)
    print("\nSemantic Summary:")
    print(f"Total functions: {summary['total_functions']}")
    print(f"Cognitive load score: {summary['cognitive_load_score']:.2f}")

    # Validate neurodiversity compliance
    compliance = parser.validate_neurodiversity_compliance(functions)
    print(f"\nNeurodiversity Compliance: {compliance['score']:.1f}%")
    if compliance["issues"]:
        print("Issues:")
        for issue in compliance["issues"]:
            print(f"  - {issue}")

    print("\nFirst 'click moment' ready!")


if __name__ == "__main__":
    test_first_click_moment()
