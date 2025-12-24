# hypercode/db/models.py
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Dict, List


class CognitiveTrait(Enum):
    VISUAL_LEARNER = "visual_learner"
    AUDITORY_LEARNER = "auditory_learner"
    KINESTHETIC_LEARNER = "kinesthetic_learner"
    PATTERN_THINKER = "pattern_thinker"
    VERBAL_THINKER = "verbal_thinker"


@dataclass
class NeuroProfile:
    """Model for individual neurodivergent traits and preferences"""

    traits: List[CognitiveTrait]
    preferred_modalities: List[str]  # visual, auditory, etc.
    focus_patterns: Dict[str, int]  # Time of day to focus score
    sensory_sensitivities: List[str]  # e.g., "bright_lights", "loud_sounds"
    assistive_technologies: List[str]  # e.g., "screen_reader", "high_contrast"


@dataclass
class CodeEntity:
    id: str
    type: str
    name: str
    file: str
    lineno: int
    snippet: str = ""
    has_test: bool = False
    has_doc: bool = False
    metadata: Dict = field(default_factory=dict)
    cognitive_complexity: float = 1.0
    attention_requirements: int = 1  # 1-5 scale
    last_modified: datetime = field(default_factory=datetime.utcnow)
    neuro_optimizations: List[str] = field(default_factory=list)
