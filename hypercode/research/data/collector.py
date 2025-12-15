# hypercode/research/data/collector.py
import json
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List

import pandas as pd


class ResearchDataCollector:
    def __init__(self, db_path: str):
        self.db_path = Path(db_path)
        self.data = self._load_database()

    def _load_database(self) -> Dict:
        """Load the HyperCode database"""
        with open(self.db_path, "r") as f:
            return json.load(f)

    def get_entities_by_type(self, entity_type: str) -> List[Dict]:
        """Get entities by their type (function, class, etc.)"""
        return [
            e for e in self.data.get("entities", []) if e.get("type") == entity_type
        ]

    def analyze_cognitive_load(self, profile_type: str) -> Dict[str, Any]:
        """Analyze code patterns based on neurodivergent profile"""
        profile = config.NEURO_PROFILES.get(profile_type, {})
        results = {"profile": profile_type, "analysis": {}, "recommendations": []}

        # Example analysis based on profile needs
        if "minimal_sensory_overload" in profile.get("needs", []):
            results["analysis"]["sensory_factors"] = self._analyze_sensory_factors()

        if "reduced_friction" in profile.get("needs", []):
            results["analysis"]["workflow_efficiency"] = self._analyze_workflow()

        return results

    def _analyze_sensory_factors(self) -> Dict:
        """Analyze visual and cognitive complexity"""
        return {
            "visual_density": self._calculate_visual_density(),
            "cognitive_complexity": self._calculate_cognitive_complexity(),
        }

    def export_to_csv(self, data: List[Dict], filename: str) -> Path:
        """Export analysis results to CSV"""
        output_path = (
            config.DATA_DIR
            / f"{filename}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        )
        df = pd.DataFrame(data)
        df.to_csv(output_path, index=False)
        return output_path
