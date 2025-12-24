Let's start by setting up the database structure. I'll create the necessary files and directories for the database configuration and models. **Note:** the canonical async entrypoint now lives in `database_utils.async_db` (exported via `database_utils`); older references to `config/database.py` should be updated to that path.

### 1. First, let's create the database configuration (canonical helpers):

```python
# database_utils async helpers (canonical)
from database_utils import Base, async_engine, AsyncSessionLocal, get_async_db as get_db
```

### 2. Create the base model:

```python
# models/base.py
from datetime import datetime
from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.ext.declarative import declared_attr
from database_utils import Base

class TimestampMixin:
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

class BaseModel(Base, TimestampMixin):
    __abstract__ = True
    id = Column(Integer, primary_key=True, index=True)

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()
```

### 3. Create the research paper model:

```python
# models/research.py
from sqlalchemy import Column, String, Text, JSON, DateTime, Index
from sqlalchemy.dialects.postgresql import JSONB
from .base import BaseModel

class ResearchPaper(BaseModel):
    __tablename__ = 'research_papers'
    
    title = Column(String(500), nullable=False, index=True)
    abstract = Column(Text)
    authors = Column(JSON)  # Store as JSON array
    source_url = Column(String(500))
    doi = Column(String(255), unique=True, index=True)
    published_date = Column(DateTime)
    source = Column(String(100))
    metadata = Column(JSONB)  # For additional metadata
    processing_status = Column(String(50), default='pending')
    confidence_score = Column(Integer, default=0)
    
    __table_args__ = (
        Index('idx_paper_title_ft', 'title', postgresql_using='gin', 
              postgresql_ops={'title': 'gin_trgm_ops'}),
        Index('idx_paper_doi', 'doi', unique=True),
    )
```

### 4. Create the knowledge graph models:

```python
# models/knowledge.py
from sqlalchemy import Column, String, Text, Integer, ForeignKey, Enum, JSON
from sqlalchemy.orm import relationship
from .base import BaseModel
import enum

class NodeType(enum.Enum):
    CONCEPT = "concept"
    PERSON = "person"
    TOOL = "tool"
    INSTITUTION = "institution"

class KnowledgeNode(BaseModel):
    __tablename__ = 'knowledge_nodes'
    
    node_type = Column(Enum(NodeType), nullable=False, index=True)
    label = Column(String(255), nullable=False, index=True)
    canonical_form = Column(String(255), index=True)
    description = Column(Text)
    properties = Column(JSON)  # For additional properties
    
    # Relationships
    source_relationships = relationship(
        "KnowledgeRelationship",
        foreign_keys="KnowledgeRelationship.source_id",
        back_populates="source"
    )
    target_relationships = relationship(
        "KnowledgeRelationship",
        foreign_keys="KnowledgeRelationship.target_id",
        back_populates="target"
    )

class KnowledgeRelationship(BaseModel):
    __tablename__ = 'knowledge_relationships'
    
    source_id = Column(Integer, ForeignKey('knowledgenodes.id'), nullable=False)
    target_id = Column(Integer, ForeignKey('knowledgenodes.id'), nullable=False)
    relationship_type = Column(String(100), nullable=False, index=True)
    confidence = Column(Integer, default=100)
    
    # Relationships
    source = relationship(
        "KnowledgeNode",
        foreign_keys=[source_id],
        back_populates="source_relationships"
    )
    target = relationship(
        "KnowledgeNode",
        foreign_keys=[target_id],
        back_populates="target_relationships"
    )
    
    __table_args__ = (
        Index('idx_relationship', 'source_id', 'target_id', 'relationship_type', unique=True),
    )
```

### 5. Create the database initialization script:

```python
# database/init_db.py
import asyncio
from sqlalchemy import text
from database_utils import async_engine as engine, Base, AsyncSessionLocal
from models.research import ResearchPaper
from models.knowledge import KnowledgeNode, KnowledgeRelationship, NodeType

async def init_db():
    async with engine.begin() as conn:
        # Create all tables
        await conn.run_sync(Base.metadata.create_all)
        
        # Add any initial data
        async with AsyncSessionLocal() as session:
            # Check if we already have data
            result = await session.execute(text("SELECT COUNT(*) FROM knowledge_nodes"))
            count = result.scalar()
            
            if count == 0:
                # Add some initial knowledge nodes
                nodes = [
                    KnowledgeNode(
                        node_type=NodeType.CONCEPT,
                        label="Machine Learning",
                        canonical_form="machine_learning",
                        description="Field of study that gives computers the ability to learn without being explicitly programmed"
                    ),
                    KnowledgeNode(
                        node_type=NodeType.CONCEPT,
                        label="Deep Learning",
                        canonical_form="deep_learning",
                        description="Subset of machine learning based on artificial neural networks"
                    )
                ]
                session.add_all(nodes)
                await session.commit()
                
                # Add relationships
                ml_node = await session.execute(
                    text("SELECT id FROM knowledge_nodes WHERE label = 'Machine Learning'")
                )
                dl_node = await session.execute(
                    text("SELECT id FROM knowledge_nodes WHERE label = 'Deep Learning'")
                )
                
                relationship = KnowledgeRelationship(
                    source_id=dl_node.scalar(),
                    target_id=ml_node.scalar(),
                    relationship_type="is_subfield_of",
                    confidence=95
                )
                session.add(relationship)
                await session.commit()

if __name__ == "__main__":
    asyncio.run(init_db())
```

### 6. Create a `.env` file:

```bash
# .env
DATABASE_URL=sqlite+aiosqlite:///./hypercode.db
# For PostgreSQL:
# DATABASE_URL=postgresql+asyncpg://username:password@localhost/hypercode
```

### 7. Create a test script to verify everything works:

```python
# test_db.py
import asyncio
from sqlalchemy import select
from database_utils import get_async_db as get_db
from models.research import ResearchPaper

async def test_connection():
    async with get_db() as session:
        # Test connection
        result = await session.execute("SELECT version()")
        print("Database version:", result.scalar())
        
        # Test model
        paper = ResearchPaper(
            title="Test Paper",
            abstract="This is a test paper",
            authors=["Author 1", "Author 2"],
            source="test",
            processing_status="processed"
        )
        session.add(paper)
        await session.commit()
        print("Created paper with ID:", paper.id)

if __name__ == "__main__":
    asyncio.run(test_connection())
```

### 8. Create a [requirements.txt](cci:7://file:///c:/Users/lyndz/Downloads/hypercode%20PROJECT/hypercode/requirements.txt:0:0-0:0) file:

```
sqlalchemy>=2.0.0
sqlalchemy[asyncio]
asyncpg
psycopg2-binary
python-dotenv
alembic
pydantic
```

### 9. Run the setup:

```bash
# Create and activate virtual environment
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Unix/MacOS:
# source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Initialize the database
python -m database.init_db

# Test the connection
python test_db.py
```

This sets up a complete database structure with:
- Async SQLAlchemy 2.0
- SQLite (default) or PostgreSQL
- Models for research papers and knowledge graph
- Basic initialization with sample data
- Test script to verify everything works
