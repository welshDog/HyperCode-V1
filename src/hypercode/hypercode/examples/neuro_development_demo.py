# examples/neuro_development_demo.py
import os
from datetime import datetime

from hypercode.db.models import CodeEntity, CognitiveTrait, NeuroProfile
from hypercode.db.query import NeuroAwareQueryEngine, QueryContext
from hypercode.visualization.neuro_visualizer import NeuroVisualizer


def create_sample_database():
    """Create a sample database for demonstration purposes"""
    # Create some sample code entities
    entities = [
        CodeEntity(
            id=f"func_{i}",
            type="function",
            name=f"process_data_{i}",
            file="data_processor.py",
            lineno=i * 10 + 1,
            snippet=f"def process_data_{i}(data):\n    # Process data here\n    return processed_data",
            has_test=i % 2 == 0,
            has_doc=i % 3 == 0,
            cognitive_complexity=1.0 + (i * 0.2),
            attention_requirements=1 + (i % 5),
            last_modified=datetime.utcnow(),
            metadata={
                "tags": ["diagram", "data"] if i % 2 == 0 else ["data"],
                "description": f"Process data using algorithm {i}",
                "complexity": "medium" if i % 3 == 0 else "high",
            },
        )
        for i in range(1, 11)
    ]

    # Add some classes
    entities.extend(
        [
            CodeEntity(
                id="class_DataProcessor",
                type="class",
                name="DataProcessor",
                file="data_processor.py",
                lineno=1,
                snippet="class DataProcessor:\n    def __init__(self):\n        self.data = None",
                has_test=True,
                has_doc=True,
                cognitive_complexity=2.5,
                attention_requirements=3,
                metadata={
                    "tags": ["diagram", "core"],
                    "description": "Main data processing class",
                },
            )
        ]
    )

    return entities


def main():
    # Create output directory
    os.makedirs("output", exist_ok=True)

    # Create sample database
    entities = create_sample_database()

    # Create a mock database
    class MockDB:
        def __init__(self, entities):
            self.entities = entities

    db = MockDB(entities)

    # Create a sample user profile
    user_profile = NeuroProfile(
        traits=[CognitiveTrait.VISUAL_LEARNER, CognitiveTrait.PATTERN_THINKER],
        preferred_modalities=["visual", "interactive"],
        focus_patterns={"morning": 9, "afternoon": 7, "evening": 5, "night": 3},
        sensory_sensitivities=["bright_lights"],
        assistive_technologies=["dark_theme"],
    )

    # Create query context
    context = QueryContext(
        user_profile=user_profile,
        current_focus=0.7,
        time_of_day="morning",
        sensory_environment={"low_light": True, "quiet": True},
    )

    # Create query engine and get recommendations
    query_engine = NeuroAwareQueryEngine(db)
    recommendations = query_engine.find_optimal_work_items(context, limit=3)

    # Print recommendations
    print("Recommended work items:")
    for i, entity in enumerate(recommendations, 1):
        print(
            f"{i}. {entity.name} (Complexity: {entity.cognitive_complexity:.1f}, "
            f"Attention: {entity.attention_requirements}/5)"
        )
        print(f"   {entity.file}:{entity.lineno}")
        print(f"   Tags: {', '.join(entity.metadata.get('tags', []))}")
        print()

    # Visualize the code flow
    visualizer = NeuroVisualizer()
    output_path = "output/code_flow.png"
    visualizer.visualize_code_flow(recommendations, output_path)
    print(f"Visualization saved to {output_path}")


if __name__ == "__main__":
    main()
