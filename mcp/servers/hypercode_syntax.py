#!/usr/bin/env python3
"""
HyperCode Syntax MCP Server
Provides real-time syntax highlighting, parsing, and neurodiversity features for IDEs
"""

import asyncio
import json
import sys
from pathlib import Path
from typing import Any, Dict, List

# Add src to path for importing parser
sys.path.append(str(Path(__file__).parent.parent.parent / "src" / "parser"))

from visual_syntax_parser import ParsedFunction, SemanticAnnotation, VisualSyntaxParser


class HyperCodeSyntaxServer:
    """🎨 MCP Server for HyperCode Visual Syntax Integration"""

    def __init__(self):
        self.parser = VisualSyntaxParser()
        self.cache = {}

    async def handle_request(self, request: Dict[str, Any]) -> Dict[str, Any]:
        """Handle MCP requests from IDE"""

        method = request.get("method")
        params = request.get("params", {})

        if method == "initialize":
            return await self._initialize(params)
        elif method == "textDocument/didChange":
            return await self._document_changed(params)
        elif method == "textDocument/hover":
            return await self._text_hover(params)
        elif method == "textDocument/completion":
            return await self._completion(params)
        elif method == "hypercode/parse":
            return await self._parse_document(params)
        elif method == "hypercode/validate":
            return await self._validate_neurodiversity(params)
        else:
            return {"error": f"Unknown method: {method}"}

    async def _initialize(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Initialize the MCP server"""
        return {
            "capabilities": {
                "textDocumentSync": 1,
                "hoverProvider": True,
                "completionProvider": {"resolveProvider": False},
                "semanticTokensProvider": {
                    "legend": {
                        "tokenTypes": [
                            "annotation",
                            "function",
                            "parameter",
                            "neurodiverse",
                            "semantic",
                            "accessibility",
                        ],
                        "tokenModifiers": ["bold", "italic", "underline"],
                    }
                },
            }
        }

    async def _document_changed(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Handle document changes for real-time parsing"""
        doc = params.get("textDocument", {})
        uri = doc.get("uri")
        content = params.get("content", [])

        # Update content
        full_content = "\n".join(change.get("text", "") for change in content)
        self.cache[uri] = full_content

        # Parse and provide diagnostics
        functions = self.parser.parse_content(full_content)
        diagnostics = self._generate_diagnostics(functions)

        return {
            "method": "textDocument/publishDiagnostics",
            "params": {"uri": uri, "diagnostics": diagnostics},
        }

    async def _text_hover(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Provide hover information for semantic annotations"""
        position = params.get("position", {})
        uri = params.get("textDocument", {}).get("uri")

        content = self.cache.get(uri, "")
        lines = content.split("\n")

        if position["line"] < len(lines):
            line = lines[position["line"]]

            # Check if line contains semantic annotation
            annotations = self.parser._parse_line_annotations(
                line, position["line"] + 1
            )
            if annotations:
                annotation = annotations[0]
                hover_info = self._get_annotation_hover_info(annotation)

                return {"contents": {"kind": "markdown", "value": hover_info}}

        return {"contents": None}

    async def _completion(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Provide completion for semantic annotations"""
        completions = []

        # Emoji-based completions
        annotations = [
            "🔍 @verifiable(...)",
            "📐 @ensures(...)",
            "📋 @requires(...)",
            "🧠 @intent(...)",
            "🎯 @accessibility(...)",
            "🎨 @computation(...)",
            "⚡ @operation(...)",
            "🔄 @return(...)",
        ]

        for annotation in annotations:
            completions.append(
                {
                    "label": annotation,
                    "kind": 15,  # Snippet
                    "insertText": annotation,
                    "detail": "HyperCode semantic annotation",
                    "documentation": f"Add {annotation} semantic marker",
                }
            )

        return {"items": completions}

    async def _parse_document(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Parse entire document and return semantic structure"""
        uri = params.get("uri")
        content = self.cache.get(uri, "")

        functions = self.parser.parse_content(content)

        return {
            "functions": [
                {
                    "name": func.name,
                    "line": func.line_start,
                    "annotations": [
                        {
                            "marker": ann.marker.value,
                            "params": ann.params,
                            "line": ann.line_number,
                        }
                        for ann in func.annotations
                    ],
                    "cognitive_load": len(func.annotations),
                }
                for func in functions
            ],
            "neurodiversity_compliance": self.parser.calculate_neurodiversity_compliance(
                functions
            ),
        }

    async def _validate_neurodiversity(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Validate neurodiversity compliance and provide suggestions"""
        uri = params.get("uri")
        content = self.cache.get(uri, "")

        functions = self.parser.parse_content(content)
        compliance = self.parser.calculate_neurodiversity_compliance(functions)

        suggestions = []

        # Check for missing accessibility annotations
        for func in functions:
            has_accessibility = any(ann.marker.value == "🎯" for ann in func.annotations)
            if not has_accessibility:
                suggestions.append(
                    {
                        "line": func.line_start,
                        "message": "Consider adding 🎯 @accessibility annotation for neurodiversity compliance",
                        "severity": "info",
                        "suggestion": '🎯 @accessibility("high_contrast", "screen_reader")',
                    }
                )

        return {
            "compliance_score": compliance,
            "suggestions": suggestions,
            "status": "compliant" if compliance >= 80.0 else "needs_improvement",
        }

    def _generate_diagnostics(
        self, functions: List[ParsedFunction]
    ) -> List[Dict[str, Any]]:
        """Generate IDE diagnostics from parsed functions"""
        diagnostics = []

        # Calculate cognitive load for each function
        for func in functions:
            cognitive_load = len(func.annotations)

            # Check cognitive load
            if cognitive_load > 7:
                diagnostics.append(
                    {
                        "range": {
                            "start": {"line": func.line_start - 1, "character": 0},
                            "end": {
                                "line": func.line_start - 1,
                                "character": len(func.name),
                            },
                        },
                        "severity": 2,  # Warning
                        "message": f"High cognitive load ({cognitive_load:.1f}) - consider simplifying",
                        "source": "HyperCode Neurodiversity",
                    }
                )

            # Check for missing intent annotations
            has_intent = any(ann.marker.value == "🧠" for ann in func.annotations)
            if not has_intent:
                diagnostics.append(
                    {
                        "range": {
                            "start": {"line": func.line_start - 1, "character": 0},
                            "end": {
                                "line": func.line_start - 1,
                                "character": len(func.name),
                            },
                        },
                        "severity": 1,  # Info
                        "message": "Consider adding 🧠 @intent annotation for clarity",
                        "source": "HyperCode Neurodiversity",
                    }
                )

        return diagnostics

    def _get_annotation_hover_info(self, annotation: SemanticAnnotation) -> str:
        """Generate hover information for semantic annotations"""
        marker_info = {
            "🔍": "Verifiable - Formal verification and proof annotations",
            "📐": "Ensures - Postconditions and guarantees",
            "📋": "Requires - Preconditions and dependencies",
            "🧠": "Intent - Purpose and cognitive context",
            "🎯": "Accessibility - Neurodiversity and inclusive design",
            "🎨": "Computation - Computational complexity and behavior",
            "⚡": "Operation - Runtime operations and side effects",
            "🔄": "Return - Return value specifications",
        }

        info = marker_info.get(annotation.marker.value, "Unknown semantic marker")

        hover = f"## {annotation.marker.value} {annotation.marker.name}\n\n"
        hover += f"{info}\n\n"

        if annotation.params:
            hover += "**Parameters:**\n"
            for key, value in annotation.params.items():
                hover += f"- `{key}`: {value}\n"

        hover += f"\n*Line {annotation.line_number}*"

        return hover


async def main():
    """Main MCP server loop"""
    server = HyperCodeSyntaxServer()

    try:
        while True:
            line = await asyncio.get_event_loop().run_in_executor(
                None, sys.stdin.readline
            )

            if not line:
                break

            try:
                request = json.loads(line.strip())
                response = await server.handle_request(request)

                if response:
                    print(json.dumps(response), flush=True)

            except json.JSONDecodeError:
                print(json.dumps({"error": "Invalid JSON"}), flush=True)
            except Exception as e:
                print(json.dumps({"error": str(e)}), flush=True)

    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    asyncio.run(main())
