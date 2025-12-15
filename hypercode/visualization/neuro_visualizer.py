# hypercode/research/visualization/neuro_visualizer.py
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
from typing import Dict, List, Optional
import networkx as nx


class NeuroVisualizer:
    def __init__(self, theme: str = "high_contrast"):
        self.theme = config.VISUALIZATION_THEMES.get(
            theme, config.VISUALIZATION_THEMES["high_contrast"]
        )
        self._setup_theme()

    def _setup_theme(self):
        """Configure visualization theme based on neurodivergent needs"""
        plt.style.use(
            "seaborn"
            if self.theme.get("background", "#ffffff") == "#ffffff"
            else "dark_background"
        )
        plt.rcParams.update(
            {
                "figure.facecolor": self.theme["background"],
                "axes.facecolor": self.theme["background"],
                "text.color": self.theme["text"],
                "axes.labelcolor": self.theme["text"],
                "xtick.color": self.theme["text"],
                "ytick.color": self.theme["text"],
                "font.family": self.theme["font_family"],
                "font.size": self.theme["font_size"],
            }
        )

    def plot_code_flow(self, entities: List[Dict], output_path: Optional[Path] = None):
        """Visualize code structure and flow"""
        G = nx.DiGraph()

        # Add nodes with attributes
        for entity in entities:
            G.add_node(
                entity["id"],
                label=entity.get("name", ""),
                type=entity.get("type", ""),
                complexity=entity.get("cognitive_complexity", 1),
            )

        # Add edges (simplified example)
        for i in range(len(entities) - 1):
            G.add_edge(entities[i]["id"], entities[i + 1]["id"])

        # Draw the graph
        plt.figure(figsize=(12, 8))
        pos = nx.spring_layout(G)

        # Draw nodes with size based on complexity
        node_sizes = [G.nodes[n].get("complexity", 1) * 500 for n in G.nodes()]
        nx.draw_networkx_nodes(
            G, pos, node_size=node_sizes, node_color=self.theme["highlight"]
        )

        # Draw edges
        nx.draw_networkx_edges(G, pos, edge_color=self.theme["accent"])

        # Draw labels
        nx.draw_networkx_labels(G, pos, font_size=8)

        plt.title("Code Structure Visualization", color=self.theme["highlight"])
        plt.axis("off")

        if output_path:
            plt.savefig(output_path, bbox_inches="tight", dpi=300)
            plt.close()
        else:
            plt.show()
