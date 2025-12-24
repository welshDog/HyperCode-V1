# hypercode/db/query.py
from dataclasses import dataclass, field
from typing import Dict, List, Optional

from .models import CodeEntity, CognitiveTrait, NeuroProfile


@dataclass
class QueryContext:
    """Context for neurodivergent-aware queries"""

    user_profile: Optional[NeuroProfile] = None
    current_focus: float = 0.5  # 0-1 scale
    time_of_day: str = "morning"  # morning, afternoon, evening, night
    sensory_environment: Dict[str, bool] = field(
        default_factory=lambda: {
            "low_light": False,
            "quiet": True,
            "minimal_distractions": True,
        }
    )


class NeuroAwareQueryEngine:
    def __init__(self, db):
        self.db = db

    def find_optimal_work_items(
        self, context: QueryContext, limit: int = 5
    ) -> List[CodeEntity]:
        """Find the best code entities to work on based on current context"""
        entities = self.db.entities

        # Score each entity based on context
        scored = []
        for entity in entities:
            score = self._calculate_entity_score(entity, context)
            scored.append((score, entity))

        # Sort by score and return top N
        scored.sort(key=lambda x: x[0], reverse=True)
        return [entity for score, entity in scored[:limit]]

    def _calculate_entity_score(
        self, entity: CodeEntity, context: QueryContext
    ) -> float:
        """Calculate how well this entity matches the user's current state"""
        score = 1.0

        # Adjust based on cognitive load
        if context.user_profile:
            # If user is a visual learner, prefer entities with visual documentation
            if CognitiveTrait.VISUAL_LEARNER in context.user_profile.traits:
                if any("diagram" in tag for tag in entity.metadata.get("tags", [])):
                    score *= 1.5

            # Adjust for time of day and focus patterns
            if context.time_of_day in context.user_profile.focus_patterns:
                focus_modifier = (
                    context.user_profile.focus_patterns[context.time_of_day] / 10.0
                )
                score *= 1.0 + focus_modifier

        # Adjust based on entity complexity
        complexity_modifier = 1.0 - (entity.attention_requirements * 0.1)
        score *= complexity_modifier

        return score
