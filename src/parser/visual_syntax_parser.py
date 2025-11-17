#!/usr/bin/env python3
"""
🎨 Visual Syntax Parser for HyperCode V3
The first "click moment" for neurodivergent developers

This parser transforms emoji-based semantic markers into executable code
while maintaining the visual clarity that makes neurodivergent developers
think "Finally, a language that gets me!"
"""

import re
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Any, Dict, List


class SemanticMarker(Enum):
    """🎨 Semantic marker types with emoji representations"""

    VERIFIABLE = "🔍"  # Formal verification
    ENSURES = "📐"  # Postconditions
    REQUIRES = "📋"  # Preconditions
    INTENT = "🧠"  # Function intent
    ACCESSIBILITY = "🎯"  # Accessibility features
    COMPUTATION = "🎨"  # Computation operations
    OPERATION = "⚡"  # Fast operations
    RETURN = "🔄"  # Return values
    DISTRIBUTED = "🖥️"  # Hardware placement
    PROBABILISTIC = "📊"  # Uncertainty/Probability
    DIFFERENTIABLE = "🎲"  # Gradients/Differentiable
    EVOLVABLE = "🧬"  # Code evolution
    UNIVERSAL = "♿"  # Universal accessibility


@dataclass
class SemanticAnnotation:
    """📋 A single semantic annotation with its metadata"""

    marker: SemanticMarker
    params: Dict[str, Any]
    line_number: int
    column_number: int
    raw_text: str

    def __str__(self) -> str:
        return f"{self.marker.value} {self.raw_text}"


@dataclass
class ParsedFunction:
    """🔍 A fully parsed HyperCode function"""

    name: str
    annotations: List[SemanticAnnotation]
    parameters: List[str]
    return_type: str
    body_lines: List[str]
    line_start: int
    line_end: int

    def get_annotations_by_type(
        self, marker_type: SemanticMarker
    ) -> List[SemanticAnnotation]:
        """Get all annotations of a specific type"""
        return [ann for ann in self.annotations if ann.marker == marker_type]


class VisualSyntaxParser:
    """🎨 Main parser for HyperCode's visual semantic syntax"""

    def __init__(self) -> None:
        self.semantic_patterns = self._build_semantic_patterns()
        self.color_scheme = self._build_color_scheme()

    def _build_semantic_patterns(self) -> Dict[str, Dict[str, Any]]:
        """🔍 Build regex patterns for all semantic markers"""
        patterns = {}

        # Map semantic markers to their annotation keywords
        annotation_map = {
            "🔍": "verifiable",
            "📐": "ensures",
            "📋": "requires",
            "🧠": "intent",
            "🎯": "accessibility",
            "🎨": "computation",
            "⚡": "operation",
            "🔄": "return",
            "🖥️": "distributed",
            "📊": "probabilistic",
            "🎲": "differentiable",
            "🧬": "evolvable",
            "♿": "universal",
        }

        for emoji, keyword in annotation_map.items():
            # Match: emoji @keyword("param") - the emoji is the marker,
            # @keyword is the syntax
            pattern = rf"{emoji}\s*@{keyword}\s*\((.*?)\)"
            marker = next(m for m in SemanticMarker if m.value == emoji)
            patterns[emoji] = {"regex": re.compile(pattern), "marker": marker}
        return patterns

    def _build_color_scheme(self) -> Dict[str, str]:
        """🎨 Build semantic color mapping for IDE highlighting"""
        return {
            "🔍": "#FF6B6B",  # Verification - Red (attention)
            "📐": "#4ECDC4",  # Ensures - Teal (calm, trustworthy)
            "📋": "#45B7D1",  # Requires - Blue (informational)
            "🧠": "#96CEB4",  # Intent - Green (growth, ideas)
            "🎯": "#FFEAA7",  # Accessibility - Yellow (warm, inclusive)
            "🎨": "#DDA0DD",  # Computation - Purple (creative)
            "⚡": "#FFA500",  # Operation - Orange (energy)
            "🔄": "#98D8C8",  # Return - Mint (completion)
            "🖥️": "#74B9FF",  # Hardware - Sky blue (tech)
            "📊": "#A29BFE",  # Probabilistic - Lavender (uncertainty)
            "🎲": "#FD79A8",  # Differentiable - Pink (gradients)
            "🧬": "#6C5CE7",  # Evolvable - Violet (growth)
            "♿": "#00B894",  # Universal - Emerald (accessibility)
        }

    def parse_file(self, file_path: str) -> List[ParsedFunction]:
        """📄 Parse an entire HyperCode file"""
        with Path(file_path).open("r", encoding="utf-8") as f:
            content = f.read()

        return self.parse_content(content)

    def parse_content(self, content: str) -> List[ParsedFunction]:
        """📝 Parse HyperCode content string"""
        lines = content.split("\n")
        functions = []
        current_function = None
        pending_annotations: List[SemanticAnnotation] = []  # Store annotations

        for line_num, line in enumerate(lines, 1):
            line = line.strip()

            # Parse semantic annotations on any line
            annotations = self._parse_line_annotations(line, line_num)

            # Check for function definition
            if self._is_function_definition(line):
                if current_function:
                    functions.append(current_function)
                current_function = self._start_new_function(line, line_num)
                # Add pending annotations (found before function definition)
                current_function.annotations.extend(pending_annotations)
                # Add annotations found on the same line as function definition
                current_function.annotations.extend(annotations)
                pending_annotations = []  # Clear pending annotations
            elif annotations and not current_function:
                # Store annotations found before function definition
                pending_annotations.extend(annotations)
            elif annotations and current_function:
                # Add annotations found after function definition
                # (shouldn't happen in normal syntax)
                current_function.annotations.extend(annotations)

            # Add function body lines
            if current_function and not self._is_function_definition(line):
                current_function.body_lines.append(line)

        if current_function:
            functions.append(current_function)

        return functions

    def _is_function_definition(self, line: str) -> bool:
        """🔍 Check if line is a function definition"""
        stripped = line.strip()
        return (
            stripped.startswith("function ")
            or stripped.startswith("def ")
            or "function " in stripped
        )

    def _start_new_function(self, line: str, line_num: int) -> ParsedFunction:
        """🆕 Create new ParsedFunction from definition line"""
        # Extract function name
        name_match = re.search(r"(?:function|def)\s+(\w+)", line)
        name = name_match.group(1) if name_match else "unnamed"

        # Extract parameters and return type
        params_match = re.search(r"\((.*?)\)", line)
        params = params_match.group(1).split(",") if params_match else []
        params = [p.strip() for p in params if p.strip()]

        return_type = "void"  # Default, can be enhanced later

        return ParsedFunction(
            name=name,
            annotations=[],
            parameters=params,
            return_type=return_type,
            body_lines=[line],
            line_start=line_num,
            line_end=line_num,
        )

    def _parse_line_annotations(
        self, line: str, line_num: int
    ) -> List[SemanticAnnotation]:
        """� Parse semantic annotations from a line"""
        annotations = []

        for _emoji, pattern_info in self.semantic_patterns.items():
            matches = pattern_info["regex"].findall(line)
            for params_str in matches:
                params = self._parse_annotation_params(params_str)
                annotation = SemanticAnnotation(
                    marker=pattern_info["marker"],
                    params=params,
                    line_number=line_num,
                    column_number=0,
                    raw_text=line,
                )
                annotations.append(annotation)

        return annotations

    def _parse_annotation_params(self, params_str: str) -> Dict[str, Any]:
        """🔧 Parse annotation parameters from string"""
        params = {}
        params_str = params_str.strip()

        # Handle empty parameters
        if not params_str:
            return {}

        # Handle simple string parameters: @emoji("text")
        if params_str.startswith('"') and params_str.endswith('"'):
            return {"text": params_str[1:-1]}

        # Handle single word without quotes: @emoji(formal_proof)
        if (
            not params_str.startswith('"')
            and not params_str.endswith('"')
            and "=" not in params_str
            and "," not in params_str
        ):
            return {"text": params_str}

        # Handle key=value parameters: @emoji(key=value, other="text")
        parts = [part.strip() for part in params_str.split(",")]
        for part in parts:
            if "=" in part:
                key, value = part.split("=", 1)
                key = key.strip()
                value = value.strip()
                # Remove quotes if present
                if value.startswith('"') and value.endswith('"'):
                    value = value[1:-1]
                params[key] = value
            else:
                # Positional parameter
                if part.startswith('"') and part.endswith('"'):
                    params[f"param_{len(params)}"] = part[1:-1]
                else:
                    params[f"param_{len(params)}"] = part

        return params

    def generate_syntax_highlighting(self, content: str) -> str:
        """🎨 Generate HTML with syntax highlighting for visual markers"""
        highlighted = content

        # Apply semantic coloring
        for emoji, color in self.color_scheme.items():
            pattern = rf"(@{emoji}\([^)]*\))"
            replacement = f'<span style="color: {color}; font-weight: bold;">\\1</span>'
            highlighted = re.sub(pattern, replacement, highlighted)

        return highlighted

    def extract_semantic_summary(
        self, functions: List[ParsedFunction]
    ) -> Dict[str, Any]:
        """📊 Extract semantic summary for analysis"""
        summary: Dict[str, Any] = {
            "total_functions": len(functions),
            "marker_counts": {},
            "accessibility_features": [],
            "verification_level": "none",
            "cognitive_load_score": 0,
        }

        # Count markers
        for marker in SemanticMarker:
            summary["marker_counts"][marker.value] = 0

        for func in functions:
            for annotation in func.annotations:
                summary["marker_counts"][annotation.marker.value] += 1

                # Track accessibility features
                if annotation.marker == SemanticMarker.ACCESSIBILITY:
                    summary["accessibility_features"].append(annotation.params)

                # Check verification level
                if annotation.marker == SemanticMarker.VERIFIABLE:
                    summary["verification_level"] = "formal"

        # Calculate cognitive load score (lower is better)
        total_annotations = sum(summary["marker_counts"].values())
        summary["cognitive_load_score"] = total_annotations / max(len(functions), 1)

        return summary

    def validate_neurodiversity_compliance(
        self, functions: List[ParsedFunction]
    ) -> Dict[str, Any]:
        """🧠 Validate neurodiversity-first design principles"""
        compliance: Dict[str, Any] = {
            "score": 0,
            "issues": [],
            "recommendations": [],
            "accessibility_coverage": 0,
        }

        total_checks = 0
        passed_checks = 0

        for func in functions:
            # Check 1: Has accessibility annotations
            total_checks += 1
            accessibility_annotations = func.get_annotations_by_type(
                SemanticMarker.ACCESSIBILITY
            )
            if accessibility_annotations:
                passed_checks += 1
            else:
                compliance["issues"].append(
                    f"Function '{func.name}' lacks accessibility annotations"
                )
                compliance["recommendations"].append(
                    f"Add @🎯 annotations to '{func.name}'"
                )

            # Check 2: Has intent annotations (reduces cognitive load)
            total_checks += 1
            intent_annotations = func.get_annotations_by_type(SemanticMarker.INTENT)
            if intent_annotations:
                passed_checks += 1
            else:
                compliance["issues"].append(
                    f"Function '{func.name}' lacks intent annotations"
                )
                compliance["recommendations"].append(
                    f"Add @🧠 intent annotation to '{func.name}'"
                )

            # Check 3: Not too many annotations (cognitive overload)
            total_checks += 1
            if len(func.annotations) <= 5:  # Reasonable limit
                passed_checks += 1
            else:
                compliance["issues"].append(
                    f"Function '{func.name}' has too many annotations "
                    f"({len(func.annotations)})"
                )
                compliance["recommendations"].append(
                    f"Consider reducing annotations in '{func.name}'"
                )

        compliance["score"] = (
            (passed_checks / total_checks) * 100 if total_checks > 0 else 0
        )
        compliance["accessibility_coverage"] = (
            passed_checks / total_checks if total_checks > 0 else 0
        )

        return compliance


# 🚀 Example usage and testing
if __name__ == "__main__":
    # Example HyperCode code
    example_code = """
🔍 @verifiable("formal_proof")
📐 @ensures("output.shape == (batch, classes)")
📋 @requires("input.shape[1] == features")
🧠 @intent("Classify input features")
🎯 @accessibility("high_contrast", "dyslexia_font")
function classifier(input: Tensor[batch, features]) -> Tensor[batch, classes] {
    🎨 weights = initialize(features, classes)
    ⚡ logits = matmul(input, weights)
    🔄 return softmax(logits)
}
"""

    parser = VisualSyntaxParser()
    functions = parser.parse_content(example_code)

    print("🎨 Visual Syntax Parser Results:")
    print(f"Found {len(functions)} functions")

    for func in functions:
        print(f"\n🔍 Function: {func.name}")
        print(f"📋 Annotations: {len(func.annotations)}")
        for annotation in func.annotations:
            print(f"  {annotation}")

    # Generate summary
    summary = parser.extract_semantic_summary(functions)
    print("\n📊 Semantic Summary:")
    print(f"Total functions: {summary['total_functions']}")
    print(f"Cognitive load score: {summary['cognitive_load_score']:.2f}")

    # Validate neurodiversity compliance
    compliance = parser.validate_neurodiversity_compliance(functions)
    print(f"\n🧠 Neurodiversity Compliance: {compliance['score']:.1f}%")
    if compliance["issues"]:
        print("⚠️  Issues:")
        for issue in compliance["issues"]:
            print(f"  - {issue}")

    print("\n✨ First 'click moment' ready! 🎯")
