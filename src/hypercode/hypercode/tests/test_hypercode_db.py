# tests/test_hypercode_db.py
import unittest
from datetime import datetime, timedelta

from hypercode.db.models import CodeEntity, CognitiveTrait, NeuroProfile
from hypercode.db.query import NeuroAwareQueryEngine, QueryContext
from hypercode.visualization.neuro_visualizer import NeuroVisualizer, VisualTheme


class TestHypercodeDB(unittest.TestCase):
    def setUp(self):
        # Create test data
        self.entities = [
            CodeEntity(
                id=f"func_{i}",
                type="function",
                name=f"test_function_{i}",
                file=f"test_file_{i//5}.py",
                lineno=i * 10,
                snippet=f"def test_function_{i}(): pass",
                has_test=i % 2 == 0,
                has_doc=i % 3 == 0,
                cognitive_complexity=1.0 + (i * 0.1),
                attention_requirements=1 + (i % 5),
                last_modified=datetime.utcnow() - timedelta(days=i),
                metadata={
                    "tags": ["diagram"] if i % 4 == 0 else [],
                    "description": f"Test function {i}",
                },
            )
            for i in range(20)
        ]

        # Create a test user profile
        self.user_profile = NeuroProfile(
            traits=[CognitiveTrait.VISUAL_LEARNER, CognitiveTrait.PATTERN_THINKER],
            preferred_modalities=["visual", "interactive"],
            focus_patterns={"morning": 8, "afternoon": 5, "evening": 7, "night": 4},
            sensory_sensitivities=["bright_lights", "loud_noises"],
            assistive_technologies=["dark_theme", "code_lens"],
        )

        # Create a mock database class
        class MockDB:
            def __init__(self, entities):
                self.entities = entities

        self.db = MockDB(self.entities)
        self.query_engine = NeuroAwareQueryEngine(self.db)

    def test_entity_creation(self):
        """Test that entities are created with correct attributes"""
        entity = self.entities[0]
        self.assertEqual(entity.type, "function")
        self.assertTrue(hasattr(entity, "cognitive_complexity"))
        self.assertTrue(hasattr(entity, "attention_requirements"))

    def test_query_engine_prioritization(self):
        """Test that the query engine prioritizes entities correctly"""
        context = QueryContext(
            user_profile=self.user_profile,
            current_focus=0.8,
            time_of_day="morning",
            sensory_environment={"low_light": True, "quiet": True},
        )

        # Get optimal work items
        results = self.query_engine.find_optimal_work_items(context, limit=5)

        # Should return the requested number of items
        self.assertEqual(len(results), 5)

        # Should prioritize items with visual documentation for visual learners
        visual_entities = [
            e for e in results if "diagram" in e.metadata.get("tags", [])
        ]
        self.assertGreater(len(visual_entities), 0)

    def test_visualization(self):
        """Test the visualization of code entities"""
        visualizer = NeuroVisualizer()

        # Test with a subset of entities
        test_entities = self.entities[:5]

        # Test visualization
        import os

        os.makedirs("test_output", exist_ok=True)
        output_path = "test_output/code_flow.png"
        visualizer.visualize_code_flow(test_entities, output_path)

        # Verify the file was created
        self.assertTrue(os.path.exists(output_path))

        # Clean up
        if os.path.exists(output_path):
            os.remove(output_path)

    def test_theme_customization(self):
        """Test custom theme creation and application"""
        custom_theme = VisualTheme(
            name="high_contrast_light",
            background_color="#ffffff",
            text_color="#000000",
            highlight_color="#0066cc",
            font_family="Arial",
            font_size=12,
        )

        visualizer = NeuroVisualizer(theme=custom_theme)
        self.assertEqual(visualizer.theme.name, "high_contrast_light")
        self.assertEqual(visualizer.theme.background_color, "#ffffff")


if __name__ == "__main__":
    unittest.main()
