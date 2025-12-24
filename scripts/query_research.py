#!/usr/bin/env python3
"""
Query and display the imported research data.
"""

import asyncio
from sqlalchemy import select
from sqlalchemy.orm import selectinload

# Add the project root to the Python path
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from config.database import AsyncSessionLocal
from models.core import KnowledgeNode, KnowledgeRelationship, NodeType

async def query_research_data():
    """Query and display the imported research data."""
    print("Querying research data...\n")
    
    async with AsyncSessionLocal() as session:
        # Get all research papers (nodes of type 'paper')
        result = await session.execute(
            select(KnowledgeNode)
            .where(KnowledgeNode.node_type == NodeType.PAPER.value)
            .options(selectinload(KnowledgeNode.source_relationships).selectinload(KnowledgeRelationship.target_node))
            .order_by(KnowledgeNode.label)
        )
        papers = result.scalars().all()
        
        print(f"Found {len(papers)} research papers:\n")
        
        for paper in papers:
            print(f"📄 {paper.label}")
            print(f"   📅 {paper.metadata_.get('date', 'No date')}")
            print(f"   📍 Source: {paper.metadata_.get('source', 'No source')}")
            
            # Get related tags
            tags = [
                rel.target_node.label 
                for rel in paper.source_relationships 
                if rel.relationship_type == "TAGGED_WITH"
            ]
            
            if tags:
                print(f"   🏷️  Tags: {', '.join(tags)}")
            
            if paper.description:
                print(f"   📝 {paper.description[:200]}..." if len(paper.description) > 200 else f"   📝 {paper.description}")
            
            print()  # Add a blank line between papers
        
        # Get all unique tags
        result = await session.execute(
            select(KnowledgeNode)
            .where(KnowledgeNode.node_type == NodeType.CONCEPT.value)
            .order_by(KnowledgeNode.label)
        )
        tags = result.scalars().all()
        
        print(f"\nFound {len(tags)} unique tags across all research:")
        print(", ".join(tag.label for tag in tags))

if __name__ == "__main__":
    asyncio.run(query_research_data())
