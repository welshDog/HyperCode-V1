# test_db.py
import asyncio
from sqlalchemy import select
from config.database import engine, Base, AsyncSessionLocal
from models.core import KnowledgeNode, KnowledgeRelationship

async def test_db_connection():
    """Test database connection and basic operations."""
    # Drop and recreate all tables
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    
    async with AsyncSessionLocal() as session:
        # Test creating nodes
        node1 = KnowledgeNode(
            node_type="concept",
            label="Test Node 1",
            description="First test node",
            metadata_={"test": True}
        )
        node2 = KnowledgeNode(
            node_type="concept",
            label="Test Node 2",
            description="Second test node",
            metadata_={"test": True}
        )
        session.add_all([node1, node2])
        await session.commit()
        
        # Test querying nodes
        result = await session.execute(
            select(KnowledgeNode).where(KnowledgeNode.label == "Test Node 1")
        )
        test_node = result.scalars().first()
        print(f"Found node: {test_node}")
        
        # Create a relationship
        relationship = KnowledgeRelationship(
            source_id=node1.id,
            target_id=node2.id,
            relationship_type="related_to",
            weight={"strength": 0.8}
        )
        session.add(relationship)
        await session.commit()
        
        # Test querying relationship
        result = await session.execute(
            select(KnowledgeRelationship)
            .where(KnowledgeRelationship.source_id == node1.id)
        )
        rel = result.scalars().first()
        print(f"Found relationship: {rel}")

if __name__ == "__main__":
    asyncio.run(test_db_connection())
