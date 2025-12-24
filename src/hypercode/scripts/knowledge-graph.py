#!/usr/bin/env python3
"""
HyperCode Knowledge Graph Generator

Generates visual knowledge graphs showing connections between research topics.

Usage:
    python scripts/knowledge-graph.py

Outputs:
    - docs/knowledge-graph.png (visual graph)
    - docs/knowledge-graph.json (data for interactive visualization)
"""

import json
import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Set, Tuple

import yaml


class KnowledgeGraphGenerator:
    """Generate visual knowledge graphs from research entries."""

    def __init__(self, docs_dir: str = "docs"):
        self.docs_dir = Path(docs_dir)
        self.nodes = {}
        self.edges = []
        self.categories = {
            "forgotten-languages": {"color": "#3b82f6", "shape": "box"},
            "ai-integration": {"color": "#10b981", "shape": "ellipse"},
            "quantum-dna-computing": {"color": "#8b5cf6", "shape": "diamond"},
            "neurodivergent-design": {"color": "#f59e0b", "shape": "triangle"},
            "hypercode-specs": {"color": "#ef4444", "shape": "star"},
        }

    def extract_frontmatter(self, content: str) -> Dict:
        """Extract YAML frontmatter from markdown file."""
        match = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
        if match:
            try:
                return yaml.safe_load(match.group(1))
            except yaml.YAMLError:
                return {}
        return {}

    def scan_research_entries(self):
        """Scan all research entries and build graph data."""
        print("🔍 Scanning research entries...")

        for category_dir in self.docs_dir.iterdir():
            if not category_dir.is_dir():
                continue

            category = category_dir.name

            if category not in self.categories and category != "templates":
                continue

            for md_file in category_dir.glob("*.md"):
                if md_file.stem in ["index", "README"]:
                    continue

                with open(md_file, "r", encoding="utf-8") as f:
                    content = f.read()

                frontmatter = self.extract_frontmatter(content)

                if not frontmatter:
                    continue

                title = frontmatter.get("title", md_file.stem)
                node_id = md_file.stem

                # Add node
                self.nodes[node_id] = {
                    "id": node_id,
                    "label": title,
                    "category": category,
                    "relevance": frontmatter.get("relevance_to_hypercode", "medium"),
                    "tags": frontmatter.get("tags", []),
                    "file": str(md_file.relative_to(self.docs_dir)),
                }

                # Extract related topics (edges)
                related = frontmatter.get("related_topics", [])
                for related_id in related:
                    self.edges.append(
                        {"from": node_id, "to": related_id, "type": "related"}
                    )

                print(f"   ✓ {title}")

        print(f"\n📊 Graph stats:")
        print(f"   Nodes: {len(self.nodes)}")
        print(f"   Edges: {len(self.edges)}")

    def generate_json(self, output_file: str = "docs/knowledge-graph.json"):
        """Generate JSON representation for interactive visualization."""
        graph_data = {
            "nodes": list(self.nodes.values()),
            "edges": self.edges,
            "categories": self.categories,
            "metadata": {
                "generated": "2025-11-22",
                "total_nodes": len(self.nodes),
                "total_edges": len(self.edges),
            },
        }

        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(graph_data, f, indent=2)

        print(f"\n💾 Saved JSON: {output_file}")

    def generate_mermaid(self, output_file: str = "docs/knowledge-graph.mmd"):
        """Generate Mermaid diagram syntax."""
        lines = ["graph TD"]

        # Add nodes
        for node_id, node in self.nodes.items():
            label = node["label"][:30]  # Truncate long labels
            category = node["category"]

            # Mermaid node syntax
            if category == "forgotten-languages":
                lines.append(f"    {node_id}[{label}]")
            elif category == "ai-integration":
                lines.append(f"    {node_id}({label})")
            elif category == "quantum-dna-computing":
                lines.append(f"    {node_id}{{{label}}}")
            elif category == "neurodivergent-design":
                lines.append(f"    {node_id}[/{label}/]")
            else:
                lines.append(f"    {node_id}[{label}]")

        # Add edges
        for edge in self.edges:
            lines.append(f"    {edge['from']} --> {edge['to']}")

        # Add styling
        lines.append("")
        lines.append(
            "    classDef forgottenLang fill:#3b82f6,stroke:#1e40af,color:#fff"
        )
        lines.append(
            "    classDef aiIntegration fill:#10b981,stroke:#047857,color:#fff"
        )
        lines.append("    classDef quantumDna fill:#8b5cf6,stroke:#6d28d9,color:#fff")
        lines.append(
            "    classDef neurodivergent fill:#f59e0b,stroke:#d97706,color:#fff"
        )

        mermaid_content = "\n".join(lines)

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(mermaid_content)

        print(f"📊 Saved Mermaid diagram: {output_file}")

    def generate_ascii_graph(self):
        """Generate simple ASCII representation of the graph."""
        print("\n" + "=" * 60)
        print("KNOWLEDGE GRAPH - ASCII VISUALIZATION")
        print("=" * 60)

        for category, style in self.categories.items():
            category_nodes = [
                n for n in self.nodes.values() if n["category"] == category
            ]

            if not category_nodes:
                continue

            print(f"\n📦 {category.upper().replace('-', ' ')}:")

            for node in category_nodes:
                print(f"   ├─ {node['label'][:40]}")

                # Find connections
                connections = [
                    self.nodes.get(e["to"], {}).get("label", e["to"])
                    for e in self.edges
                    if e["from"] == node["id"] and e["to"] in self.nodes
                ]

                for conn in connections[:3]:  # Limit to 3 connections
                    print(f"   │  └─→ {conn[:35]}")

        print("\n" + "=" * 60)

    def generate_graphviz_dot(self, output_file: str = "docs/knowledge-graph.dot"):
        """Generate GraphViz DOT format (requires graphviz to render)."""
        lines = ["digraph HyperCodeKnowledge {"]
        lines.append("    rankdir=LR;")
        lines.append('    node [style=filled, fontname="Arial"];')
        lines.append("")

        # Add nodes with styling
        for node_id, node in self.nodes.items():
            category = node["category"]
            color = self.categories.get(category, {}).get("color", "#cccccc")
            label = node["label"].replace('"', '\\"')[:40]

            lines.append(
                f'    "{node_id}" [label="{label}", fillcolor="{color}", fontcolor="white"];'
            )

        lines.append("")

        # Add edges
        for edge in self.edges:
            if edge["to"] in self.nodes:
                lines.append(f'    "{edge["from"]}" -> "{edge["to"]}";')

        lines.append("}")

        dot_content = "\n".join(lines)

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(dot_content)

        print(f"🌐 Saved GraphViz DOT: {output_file}")
        print(f"   (Run: dot -Tpng {output_file} -o docs/knowledge-graph.png)")


def main():
    """
    Main entry point for knowledge graph generator.
    """
    print("")
    print("╔═══════════════════════════════════════════════════════════╗")
    print("║       HyperCode Knowledge Graph Generator v1.0.0          ║")
    print("║   Visualizing connections between research topics         ║")
    print("╚═══════════════════════════════════════════════════════════╝")
    print("")

    generator = KnowledgeGraphGenerator()

    try:
        # Scan all research entries
        generator.scan_research_entries()

        # Generate multiple output formats
        generator.generate_json()
        generator.generate_mermaid()
        generator.generate_graphviz_dot()
        generator.generate_ascii_graph()

        print("")
        print("✅ Knowledge graph generation complete!")
        print("")
        print("📂 Output files:")
        print("   - docs/knowledge-graph.json (interactive data)")
        print("   - docs/knowledge-graph.mmd (Mermaid diagram)")
        print("   - docs/knowledge-graph.dot (GraphViz)")
        print("")
        print("🌐 To visualize:")
        print("   - Mermaid: https://mermaid.live/")
        print(
            "   - GraphViz: dot -Tpng docs/knowledge-graph.dot -o docs/knowledge-graph.png"
        )
        print("")

        return 0

    except Exception as e:
        print(f"")
        print(f"❌ Error: {str(e)}")
        import traceback

        traceback.print_exc()
        print(f"")
        return 1


if __name__ == "__main__":
    sys.exit(main())
