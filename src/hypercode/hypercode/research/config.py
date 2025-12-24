# hypercode/research/config.py
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List


@dataclass
class ResearchConfig:
    # Core paths
    BASE_DIR: Path = Path(__file__).parent.parent
    DATA_DIR: Path = BASE_DIR / "data"
    NOTEBOOKS_DIR: Path = BASE_DIR / "notebooks"
    VISUALIZATIONS_DIR: Path = BASE_DIR / "visualizations"

    # Research domains from spec
    RESEARCH_DOMAINS: List[str] = [
        "neurodivergent_cognition",
        "multimodal_interaction",
        "quantum_molecular",
        "ai_synthesis",
    ]

    # Neurodivergent profiles based on spec
    NEURO_PROFILES: Dict[str, Dict] = {
        "autistic_thinker": {
            "strengths": ["pattern_recognition", "attention_to_detail", "systemizing"],
            "needs": ["minimal_sensory_overload", "clear_structure", "predictability"],
        },
        "adhd_thinker": {
            "strengths": ["divergent_thinking", "hyperfocus", "creativity"],
            "needs": ["reduced_friction", "engagement", "flexible_workflows"],
        },
        "dyslexic_thinker": {
            "strengths": ["spatial_reasoning", "narrative_thinking", "big_picture"],
            "needs": ["multimodal_input", "custom_typography", "context_preservation"],
        },
    }

    # Visualization themes matching spec's sensory goals
    VISUALIZATION_THEMES: Dict[str, Dict] = {
        "high_contrast": {
            "background": "#1e1e1e",
            "text": "#f0f0f0",
            "highlight": "#4ec9b0",
            "accent": "#569cd6",
            "font_family": "Arial, sans-serif",
            "font_size": 14,
        },
        "low_sensory": {
            "background": "#f8f9fa",
            "text": "#333333",
            "highlight": "#2b7bb9",
            "accent": "#6c757d",
            "font_family": "Arial, sans-serif",
            "font_size": 16,
        },
    }

    def __post_init__(self):
        """Create necessary directories"""
        self.DATA_DIR.mkdir(exist_ok=True)
        self.NOTEBOOKS_DIR.mkdir(exist_ok=True)
        self.VISUALIZATIONS_DIR.mkdir(exist_ok=True)


# Initialize config
config = ResearchConfig()
