# hypercode/research/visualization/plotter.py
from pathlib import Path
from typing import Any, Dict, List

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


class ResearchPlotter:
    def __init__(self, theme: str = "high_contrast"):
        self.theme = theme
        self.setup_theme()

    def setup_theme(self):
        """Configure plotting style"""
        if self.theme == "high_contrast":
            plt.style.use("dark_background")
            self.colors = ["#4ec9b0", "#569cd6", "#9cdcfe", "#ce9178", "#dcdcaa"]
        else:
            plt.style.use("seaborn")
            self.colors = sns.color_palette("husl")

        plt.rcParams["figure.figsize"] = (12, 6)
        plt.rcParams["font.size"] = 12

    def plot_complexity_distribution(self, entities: List[Any], save_path: Path = None):
        """Plot distribution of cognitive complexity"""
        complexities = [
            e.cognitive_complexity
            for e in entities
            if hasattr(e, "cognitive_complexity")
        ]

        plt.figure()
        sns.histplot(complexities, kde=True, color=self.colors[0])
        plt.title("Distribution of Cognitive Complexity")
        plt.xlabel("Cognitive Complexity")
        plt.ylabel("Count")

        if save_path:
            plt.savefig(save_path, bbox_inches="tight", dpi=300)
            plt.close()
        else:
            plt.show()

    def plot_attention_patterns(self, analysis: Dict[str, Any], save_path: Path = None):
        """Visualize attention pattern analysis"""
        data = {
            "Attention Level": ["High", "Medium", "Low"],
            "Count": [
                len(analysis["high_attention"]),
                len(analysis["medium_attention"]),
                len(analysis["low_attention"]),
            ],
        }

        df = pd.DataFrame(data)
        plt.figure()
        sns.barplot(x="Attention Level", y="Count", data=df, palette=self.colors[:3])
        plt.title("Code Entities by Attention Requirements")

        if save_path:
            plt.savefig(save_path, bbox_inches="tight", dpi=300)
            plt.close()
        else:
            plt.show()
