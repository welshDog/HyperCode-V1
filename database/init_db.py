# database/init_db.py
import asyncio

from sqlalchemy import text

from config.database import AsyncSessionLocal, Base, engine
from models.core import KnowledgeNode, KnowledgeRelationship, NodeType


async def init_models():
    """Create all database tables."""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def init_data():
    """Initialize with sample data."""
    async with AsyncSessionLocal() as session:
        # Check if data already exists
        result = await session.execute(text("SELECT COUNT(*) FROM knowledge_nodes"))
        count = result.scalar()

        if count == 0:
            # Create sample nodes
            nodes = [
                KnowledgeNode(
                    node_type=NodeType.CONCEPT.value,
                    label="Machine Learning",
                    description="Field of AI that enables systems to learn from data",
                    metadata_={"category": "AI", "complexity": "high"},
                ),
                KnowledgeNode(
                    node_type=NodeType.CONCEPT.value,
                    label="Neural Networks",
                    description="Computational models inspired by biological neural networks",
                    metadata_={"category": "AI", "complexity": "high"},
                ),
            ]
            session.add_all(nodes)
            await session.commit()

            # Create relationships
            ml_node = await session.execute(
                text("SELECT id FROM knowledge_nodes WHERE label = 'Machine Learning'")
            )
            nn_node = await session.execute(
                text("SELECT id FROM knowledge_nodes WHERE label = 'Neural Networks'")
            )

            relationship = KnowledgeRelationship(
                source_id=ml_node.scalar(),
                target_id=nn_node.scalar(),
                relationship_type="includes",
                weight={"confidence": 0.95, "source": "expert_knowledge"},
            )
            session.add(relationship)
            await session.commit()


async def main():
    """Initialize database and data."""
    print("Initializing database...")
    await init_models()
    print("Database tables created.")

    print("Initializing sample data...")
    await init_data()
    print("Sample data initialized.")


if __name__ == "__main__":
    asyncio.run(main())
