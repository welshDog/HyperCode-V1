#!/usr/bin/env python3
"""
Import organized research data into the SQLite database.
"""

import json
import os
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any, Optional
import asyncio
from sqlalchemy import select, text
from sqlalchemy.orm import Session

# Add the project root to the Python path
import sys
sys.path.append(str(Path(__file__).parent.parent))

from config.database import engine, Base, AsyncSessionLocal
from models.core import KnowledgeNode, KnowledgeRelationship, NodeType

# Configuration
PROJECT_ROOT = Path(__file__).parent.parent
RESEARCH_DIR = PROJECT_ROOT / "data" / "reseach data json"
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed_research"

async def create_tables():
    """Create database tables if they don't exist."""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("Database tables created successfully.")

async def get_or_create_node(session, node_data: Dict[str, Any], node_type: NodeType) -> KnowledgeNode:
    """Get an existing node or create a new one if it doesn't exist."""
    # Try to find an existing node with the same label and type
    result = await session.execute(
        select(KnowledgeNode).where(
            KnowledgeNode.label == node_data["label"],
            KnowledgeNode.node_type == node_type.value
        )
    )
    node = result.scalars().first()
    
    if not node:
        # Create a new node if it doesn't exist
        node = KnowledgeNode(
            node_type=node_type.value,
            label=node_data["label"],
            description=node_data.get("summary", ""),
            metadata_={
                "source": node_data.get("source", ""),
                "date": node_data.get("date", ""),
                "tags": node_data.get("tags", []),
                "file_name": node_data.get("file_name", "")
            }
        )
        session.add(node)
        await session.commit()
        await session.refresh(node)
    
    return node

async def import_research_data():
    """Import organized research data into the database."""
    print("Starting research data import...")
    
    # Create database tables if they don't exist
    await create_tables()
    
    async with AsyncSessionLocal() as session:
        # Process each topic directory
        for topic_dir in PROCESSED_DIR.iterdir():
            if not topic_dir.is_dir() or topic_dir.name in ["analysis", "visualizations"]:
                continue
                
            print(f"\nProcessing topic: {topic_dir.name}")
            
            # Process each JSON file in the topic directory
            for json_file in topic_dir.glob("*.json"):
                with open(json_file, 'r', encoding='utf-8') as f:
                    try:
                        research_item = json.load(f)
                        
                        # Create or update the research node
                        research_node = await get_or_create_node(
                            session,
                            {
                                "label": research_item.get("topic", topic_dir.name),
                                "summary": research_item.get("summary", ""),
                                "source": research_item.get("source", ""),
                                "date": research_item.get("date", ""),
                                "tags": research_item.get("tags", []),
                                "file_name": research_item.get("file_name", json_file.name)
                            },
                            NodeType.PAPER
                        )
                        
                        # Create relationships with tags
                        for tag in research_item.get("tags", []):
                            tag_node = await get_or_create_node(
                                session,
                                {"label": tag, "summary": f"Tag: {tag}"},
                                NodeType.CONCEPT
                            )
                            
                            # Create relationship between research and tag
                            relationship = KnowledgeRelationship(
                                source_id=research_node.id,
                                target_id=tag_node.id,
                                relationship_type="TAGGED_WITH",
                                weight={"strength": 1.0}
                            )
                            session.add(relationship)
                        
                        await session.commit()
                        print(f"  - Imported: {research_node.label}")
                        
                    except json.JSONDecodeError as e:
                        print(f"Error decoding {json_file}: {e}")
                    except Exception as e:
                        print(f"Error processing {json_file}: {e}")
                        await session.rollback()
    
    print("\nResearch data import completed!")

if __name__ == "__main__":
    asyncio.run(import_research_data())
