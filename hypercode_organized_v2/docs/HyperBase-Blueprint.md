# 🚀 HyperBase Blueprint: The Living Research Database

**A neurodivergent-friendly, AI-native knowledge system for HyperCode's research brain.**

---

## 📋 Table of Contents

1. [Vision & Purpose](#vision--purpose)
2. [Architecture Overview](#architecture-overview)
3. [Phase 1: Core Database Setup](#phase-1-core-database-setup)
4. [Phase 2: Enhanced Data Models](#phase-2-enhanced-data-models)
5. [Phase 3: Knowledge Graph Engine](#phase-3-knowledge-graph-engine)
6. [Phase 4: AI Agent Integration](#phase-4-ai-agent-integration)
7. [Phase 5: Research Paper Ingestion Pipeline](#phase-5-research-paper-ingestion-pipeline)
8. [Phase 6: Query & Visualization Layer](#phase-6-query--visualization-layer)
9. [Deployment & Operations](#deployment--operations)
10. [Testing Strategy](#testing-strategy)

---

## 🎯 Vision & Purpose

**HyperBase is the beating heart of HyperCode's living research system.**

- **Living Research Paper**: Auto-updates daily with new findings, no staleness.
- **Knowledge Graph Brain**: Interconnects concepts, people, tools, institutions across research papers.
- **AI-Native**: Built for autonomous agents to read, extract, reason, and expand the graph.
- **Neurodivergent-First Design**: Minimal noise, spatial clarity, logical structure.
- **Multi-Tenant Ready**: Supports multiple HyperCode "projects" or "universes" without collision.

---

## 🏗️ Architecture Overview

```
┌─────────────────────────────────────────────────────────┐
│                    HyperBase Stack                      │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  ┌──────────────────────────────────────────────────┐  │
│  │  AI Research Agents Layer (Claude, GPT, etc.)   │  │
│  └──────────────────────────────────────────────────┘  │
│                          ↓                              │
│  ┌──────────────────────────────────────────────────┐  │
│  │  Query & Extraction Engine (Semantic Search)    │  │
│  └──────────────────────────────────────────────────┘  │
│                          ↓                              │
│  ┌──────────────────────────────────────────────────┐  │
│  │  Knowledge Graph Core (Nodes, Relationships)    │  │
│  │  Paper Repository (Full-text + Metadata)        │  │
│  │  Evidence Linkage (Who said what, when)         │  │
│  └──────────────────────────────────────────────────┘  │
│                          ↓                              │
│  ┌──────────────────────────────────────────────────┐  │
│  │  Async SQLAlchemy 2.0 ORM Layer                 │  │
│  └──────────────────────────────────────────────────┘  │
│                          ↓                              │
│  ┌──────────────────────────────────────────────────┐  │
│  │  PostgreSQL (prod) / SQLite (dev) Backend       │  │
│  └──────────────────────────────────────────────────┘  │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

## ⚙️ Phase 1: Core Database Setup

### Step 1.1: Initialize Project Structure

```bash
# Create project root
mkdir hyperbase && cd hyperbase

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Create folder structure
mkdir -p {config,models,schemas,database,scripts,tests,migrations,agents}
touch config/__init__.py models/__init__.py schemas/__init__.py database/__init__.py

# Create entry point
touch main.py
```

### Step 1.2: Install Dependencies

Create `requirements.txt`:

```txt
# Core async database
sqlalchemy>=2.0.0
sqlalchemy[asyncio]
asyncpg>=0.28.0
aiosqlite>=0.19.0

# Database migration
alembic>=1.13.0

# Data validation & serialization
pydantic>=2.0.0
pydantic-settings>=2.0.0

# Environment & config
python-dotenv>=1.0.0

# API (FastAPI optional, for future REST layer)
fastapi>=0.104.0
uvicorn>=0.24.0

# AI & LLM integration
openai>=1.0.0
anthropic>=0.7.0
requests>=2.31.0

# Utilities
python-dateutil>=2.8.0
pytz>=2023.3
uuid6>=1.0.0

# Testing
pytest>=7.4.0
pytest-asyncio>=0.21.0
pytest-cov>=4.1.0

# Logging & monitoring
structlog>=23.1.0
```

Install:

```bash
pip install -r requirements.txt
```

### Step 1.3: Environment Configuration

Create `.env`:

```bash
# Database
DATABASE_URL=sqlite+aiosqlite:///./hyperbase.db
# For PostgreSQL: postgresql+asyncpg://user:password@localhost/hyperbase

# Database tuning
DB_POOL_SIZE=10
DB_MAX_OVERFLOW=20
DB_ECHO=false

# Project metadata
PROJECT_NAME=HyperBase
VERSION=0.1.0
ENVIRONMENT=development

# AI Integration
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-...

# Research agent settings
AGENT_RESEARCH_BATCH_SIZE=10
AGENT_UPDATE_INTERVAL_HOURS=24
```

### Step 1.4: Core Config Module

Create `config/database.py`:

```python
import os
from typing import Optional
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.pool import NullPool
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "sqlite+aiosqlite:///./hyperbase.db"
)

# Connection pool settings
POOL_SIZE = int(os.getenv("DB_POOL_SIZE", 10))
MAX_OVERFLOW = int(os.getenv("DB_MAX_OVERFLOW", 20))
ECHO = os.getenv("DB_ECHO", "false").lower() == "true"

# Create async engine
engine = create_async_engine(
    DATABASE_URL,
    echo=ECHO,
    pool_size=POOL_SIZE,
    max_overflow=MAX_OVERFLOW,
    pool_timeout=30,
    pool_recycle=1800,
    pool_pre_ping=True,
    future=True
)

# Session factory
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=False
)

# Base class for all models
Base = declarative_base()

# Dependency injection for sessions
async def get_db_session():
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()
```

Create `config/settings.py`:

```python
from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    PROJECT_NAME: str = "HyperBase"
    VERSION: str = "0.1.0"
    ENVIRONMENT: str = "development"
    
    # Database
    DATABASE_URL: str = "sqlite+aiosqlite:///./hyperbase.db"
    DB_POOL_SIZE: int = 10
    DB_MAX_OVERFLOW: int = 20
    DB_ECHO: bool = False
    
    # AI
    OPENAI_API_KEY: Optional[str] = None
    ANTHROPIC_API_KEY: Optional[str] = None
    
    # Agent settings
    AGENT_RESEARCH_BATCH_SIZE: int = 10
    AGENT_UPDATE_INTERVAL_HOURS: int = 24
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()
```

---

## 📊 Phase 2: Enhanced Data Models

### Step 2.1: Base Models with UUID & Metadata

Create `models/base.py`:

```python
from datetime import datetime
from uuid import uuid4
from sqlalchemy import Column, String, DateTime, Text, Index
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declared_attr
from config.database import Base

class TimestampMixin:
    """Automatic timestamp tracking for all models."""
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

class UUIDMixin:
    """UUID primary key for distributed systems."""
    @declared_attr
    def id(cls):
        return Column(UUID(as_uuid=True), primary_key=True, default=uuid4)

class BaseModel(Base, UUIDMixin, TimestampMixin):
    """Base for all models: UUID pk, timestamps, table naming."""
    __abstract__ = True
    
    @declared_attr
    def __tablename__(cls):
        # Convert CamelCase to snake_case
        name = cls.__name__
        return ''.join(['_' + c.lower() if c.isupper() else c for c in name]).lstrip('_')

class AuditMixin:
    """Track who changed what and when."""
    created_by = Column(String(255), nullable=True)
    updated_by = Column(String(255), nullable=True)
    change_log = Column(Text, nullable=True)  # JSON string of recent changes
```

### Step 2.2: Research Paper Model (Upgraded)

Create `models/research.py`:

```python
from sqlalchemy import Column, String, Text, Integer, Float, DateTime, Index, ForeignKey, Boolean
from sqlalchemy.dialects.postgresql import JSONB, ARRAY, TSVECTOR
from sqlalchemy.orm import relationship
from models.base import BaseModel, AuditMixin
from datetime import datetime
import json

class ResearchPaper(BaseModel, AuditMixin):
    """Research paper with full metadata and extraction status."""
    
    # Core identity
    title = Column(String(500), nullable=False, index=True)
    doi = Column(String(255), unique=True, index=True, nullable=True)
    url = Column(String(500), nullable=True)
    
    # Authorship
    authors = Column(JSONB, default=list)  # [{name, affiliation, role}]
    publication_date = Column(DateTime, nullable=True)
    
    # Content
    abstract = Column(Text, nullable=True)
    full_text = Column(Text, nullable=True)
    keywords = Column(ARRAY(String), nullable=True)
    
    # Metadata
    source = Column(String(100), nullable=True)  # arxiv, pubmed, etc.
    paper_type = Column(String(50), nullable=True)  # conference, journal, preprint
    citations_count = Column(Integer, default=0)
    
    # Processing state
    processing_status = Column(String(50), default='pending')  # pending, extracting, completed, failed
    extraction_confidence = Column(Float, default=0.0)
    last_processed_at = Column(DateTime, nullable=True)
    processing_errors = Column(JSONB, default=dict)
    
    # Search optimization
    search_vector = Column(TSVECTOR, nullable=True)  # For full-text search
    
    # Extra metadata
    extra_metadata = Column(JSONB, default=dict)
    
    # Relationships
    extracted_entities = relationship("ExtractedEntity", back_populates="paper", cascade="all, delete-orphan")
    graph_nodes = relationship("KnowledgeNode", secondary="paper_node_evidence", back_populates="source_papers")
    
    __table_args__ = (
        Index('idx_paper_doi', 'doi'),
        Index('idx_paper_title', 'title'),
        Index('idx_paper_status', 'processing_status'),
        Index('idx_paper_created', 'created_at'),
    )

class ExtractedEntity(BaseModel):
    """Entities extracted from papers by AI agents."""
    
    paper_id = Column(UUID(as_uuid=True), ForeignKey('research_paper.id'), nullable=False)
    entity_type = Column(String(100), nullable=False)  # concept, person, tool, etc.
    entity_text = Column(String(500), nullable=False)
    confidence = Column(Float, default=0.0)
    context = Column(Text, nullable=True)  # The sentence where found
    span_start = Column(Integer, nullable=True)
    span_end = Column(Integer, nullable=True)
    
    paper = relationship("ResearchPaper", back_populates="extracted_entities")
    
    __table_args__ = (
        Index('idx_entity_type', 'entity_type'),
        Index('idx_entity_paper', 'paper_id'),
    )
```

### Step 2.3: Knowledge Graph Models (Expanded)

Create `models/knowledge.py`:

```python
from sqlalchemy import Column, String, Text, Integer, Float, ForeignKey, Enum, Index, Table, UniqueConstraint
from sqlalchemy.dialects.postgresql import JSONB, ARRAY
from sqlalchemy.orm import relationship
from models.base import BaseModel, AuditMixin
from enum import Enum as PyEnum

class NodeType(PyEnum):
    CONCEPT = "concept"
    PERSON = "person"
    TOOL = "tool"
    INSTITUTION = "institution"
    TECHNIQUE = "technique"
    DATASET = "dataset"
    LANGUAGE = "language"

# Association table for paper-node evidence
paper_node_evidence = Table(
    'paper_node_evidence',
    BaseModel.metadata,
    Column('paper_id', UUID(as_uuid=True), ForeignKey('research_paper.id'), primary_key=True),
    Column('node_id', UUID(as_uuid=True), ForeignKey('knowledge_node.id'), primary_key=True),
    Column('evidence_score', Float, default=1.0),
    Column('extraction_date', DateTime, default=datetime.utcnow)
)

class KnowledgeNode(BaseModel, AuditMixin):
    """Node in the knowledge graph: concepts, people, tools, etc."""
    
    # Core identity
    node_type = Column(Enum(NodeType), nullable=False, index=True)
    label = Column(String(255), nullable=False, index=True)
    slug = Column(String(255), unique=True, index=True)  # Canonical identifier
    
    # Descriptive
    description = Column(Text, nullable=True)
    aliases = Column(ARRAY(String), default=list)  # Alternative names
    
    # Metadata
    properties = Column(JSONB, default=dict)  # Type-specific attributes
    confidence = Column(Float, default=1.0)
    is_canonical = Column(Boolean, default=True)
    canonical_node_id = Column(UUID(as_uuid=True), ForeignKey('knowledge_node.id'), nullable=True)
    
    # Relationships
    source_relationships = relationship(
        "KnowledgeRelationship",
        foreign_keys="KnowledgeRelationship.source_id",
        back_populates="source",
        cascade="all, delete-orphan"
    )
    target_relationships = relationship(
        "KnowledgeRelationship",
        foreign_keys="KnowledgeRelationship.target_id",
        back_populates="target",
        cascade="all, delete-orphan"
    )
    source_papers = relationship("ResearchPaper", secondary=paper_node_evidence, back_populates="graph_nodes")

class KnowledgeRelationship(BaseModel, AuditMixin):
    """Edge in the knowledge graph with evidence linkage."""
    
    # Nodes
    source_id = Column(UUID(as_uuid=True), ForeignKey('knowledge_node.id'), nullable=False, index=True)
    target_id = Column(UUID(as_uuid=True), ForeignKey('knowledge_node.id'), nullable=False, index=True)
    
    # Relationship
    relationship_type = Column(String(100), nullable=False, index=True)
    description = Column(Text, nullable=True)
    confidence = Column(Float, default=1.0)
    
    # Evidence
    supporting_papers = Column(JSONB, default=list)  # [{paper_id, evidence_text, confidence}]
    extraction_method = Column(String(100), nullable=True)  # "llm", "regex", "manual"
    
    # Metadata
    properties = Column(JSONB, default=dict)
    
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
        UniqueConstraint('source_id', 'target_id', 'relationship_type', name='uq_relationship'),
        Index('idx_relationship_source', 'source_id'),
        Index('idx_relationship_target', 'target_id'),
    )

class ConceptHierarchy(BaseModel):
    """Track hierarchical relationships (broader/narrower concepts)."""
    
    parent_id = Column(UUID(as_uuid=True), ForeignKey('knowledge_node.id'), nullable=False)
    child_id = Column(UUID(as_uuid=True), ForeignKey('knowledge_node.id'), nullable=False)
    hierarchy_level = Column(Integer, default=1)
    
    __table_args__ = (
        UniqueConstraint('parent_id', 'child_id', name='uq_hierarchy'),
    )
```

### Step 2.4: Pydantic Schemas for API/Agent I/O

Create `schemas/research.py`:

```python
from pydantic import BaseModel, Field, HttpUrl
from typing import Optional, List
from datetime import datetime
from uuid import UUID
from enum import Enum

class AuthorSchema(BaseModel):
    name: str
    affiliation: Optional[str] = None
    role: Optional[str] = None

class ResearchPaperCreate(BaseModel):
    title: str
    doi: Optional[str] = None
    url: Optional[HttpUrl] = None
    authors: List[AuthorSchema] = []
    publication_date: Optional[datetime] = None
    abstract: Optional[str] = None
    source: Optional[str] = None
    paper_type: Optional[str] = None

class ResearchPaperResponse(ResearchPaperCreate):
    id: UUID
    processing_status: str
    extraction_confidence: float
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True
```

Create `schemas/knowledge.py`:

```python
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from uuid import UUID
from datetime import datetime
from enum import Enum

class NodeTypeEnum(str, Enum):
    CONCEPT = "concept"
    PERSON = "person"
    TOOL = "tool"
    INSTITUTION = "institution"
    TECHNIQUE = "technique"
    DATASET = "dataset"
    LANGUAGE = "language"

class KnowledgeNodeCreate(BaseModel):
    node_type: NodeTypeEnum
    label: str
    description: Optional[str] = None
    aliases: List[str] = []
    properties: Dict[str, Any] = {}

class KnowledgeNodeResponse(KnowledgeNodeCreate):
    id: UUID
    slug: str
    confidence: float
    created_at: datetime
    
    class Config:
        from_attributes = True

class KnowledgeRelationshipCreate(BaseModel):
    source_id: UUID
    target_id: UUID
    relationship_type: str
    description: Optional[str] = None
    confidence: float = 1.0
    extraction_method: Optional[str] = None

class KnowledgeRelationshipResponse(KnowledgeRelationshipCreate):
    id: UUID
    created_at: datetime
    
    class Config:
        from_attributes = True
```

---

## 🧠 Phase 3: Knowledge Graph Engine

### Step 3.1: Graph Query Service

Create `database/graph_queries.py`:

```python
from sqlalchemy import select, and_, or_, func
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload
from models.knowledge import KnowledgeNode, KnowledgeRelationship
from typing import List, Set, Dict, Optional
from uuid import UUID

class GraphQueryService:
    """High-level API for knowledge graph queries."""
    
    def __init__(self, session: AsyncSession):
        self.session = session
    
    async def get_node_by_slug(self, slug: str) -> Optional[KnowledgeNode]:
        """Fetch node by canonical slug."""
        stmt = select(KnowledgeNode).where(KnowledgeNode.slug == slug)
        result = await self.session.execute(stmt)
        return result.scalars().first()
    
    async def get_neighbors(self, node_id: UUID, depth: int = 1) -> Dict[str, List[Dict]]:
        """Get connected nodes up to specified depth (BFS)."""
        neighbors = {"outgoing": [], "incoming": []}
        visited = {node_id}
        queue = [(node_id, 0)]
        
        while queue:
            current_id, current_depth = queue.pop(0)
            
            if current_depth >= depth:
                continue
            
            # Outgoing edges
            stmt_out = select(KnowledgeRelationship).where(
                KnowledgeRelationship.source_id == current_id
            ).options(joinedload(KnowledgeRelationship.target))
            
            result_out = await self.session.execute(stmt_out)
            for rel in result_out.scalars().unique():
                target = rel.target
                if target.id not in visited:
                    visited.add(target.id)
                    neighbors["outgoing"].append({
                        "node": target,
                        "relationship_type": rel.relationship_type,
                        "confidence": rel.confidence,
                        "depth": current_depth + 1
                    })
                    queue.append((target.id, current_depth + 1))
            
            # Incoming edges
            stmt_in = select(KnowledgeRelationship).where(
                KnowledgeRelationship.target_id == current_id
            ).options(joinedload(KnowledgeRelationship.source))
            
            result_in = await self.session.execute(stmt_in)
            for rel in result_in.scalars().unique():
                source = rel.source
                if source.id not in visited:
                    visited.add(source.id)
                    neighbors["incoming"].append({
                        "node": source,
                        "relationship_type": rel.relationship_type,
                        "confidence": rel.confidence,
                        "depth": current_depth + 1
                    })
                    queue.append((source.id, current_depth + 1))
        
        return neighbors
    
    async def find_path(self, source_id: UUID, target_id: UUID, max_depth: int = 5) -> Optional[List[UUID]]:
        """Find shortest path between two nodes (Dijkstra-ish)."""
        # BFS to find shortest path
        from collections import deque
        
        queue = deque([(source_id, [source_id])])
        visited = {source_id}
        
        while queue:
            current_id, path = queue.popleft()
            
            if len(path) > max_depth:
                continue
            
            if current_id == target_id:
                return path
            
            stmt = select(KnowledgeRelationship).where(
                KnowledgeRelationship.source_id == current_id
            )
            result = await self.session.execute(stmt)
            
            for rel in result.scalars().all():
                next_id = rel.target_id
                if next_id not in visited:
                    visited.add(next_id)
                    queue.append((next_id, path + [next_id]))
        
        return None
    
    async def search_nodes_by_type(self, node_type: str, limit: int = 50) -> List[KnowledgeNode]:
        """Search all nodes of a given type."""
        stmt = select(KnowledgeNode).where(
            KnowledgeNode.node_type == node_type
        ).limit(limit)
        result = await self.session.execute(stmt)
        return result.scalars().all()
    
    async def get_relationship_statistics(self) -> Dict[str, int]:
        """Aggregate stats on relationships."""
        stmt = select(
            KnowledgeRelationship.relationship_type,
            func.count(KnowledgeRelationship.id).label('count')
        ).group_by(KnowledgeRelationship.relationship_type)
        
        result = await self.session.execute(stmt)
        return {row[0]: row[1] for row in result}
```

### Step 3.2: Node & Relationship Managers

Create `database/node_manager.py`:

```python
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from models.knowledge import KnowledgeNode, NodeType
from schemas.knowledge import KnowledgeNodeCreate
from typing import Optional
from uuid import uuid4
import re

class NodeManager:
    """Manage creation, updates, deduplication of knowledge nodes."""
    
    def __init__(self, session: AsyncSession):
        self.session = session
    
    @staticmethod
    def slug_from_label(label: str) -> str:
        """Convert label to canonical slug."""
        slug = label.lower().strip()
        slug = re.sub(r'[^\w\s-]', '', slug)
        slug = re.sub(r'[-\s]+', '-', slug)
        return slug
    
    async def create_or_get_node(
        self,
        node_type: NodeType,
        label: str,
        description: Optional[str] = None,
        aliases: list = None,
        properties: dict = None
    ) -> KnowledgeNode:
        """Create node or return existing if found by slug."""
        
        slug = self.slug_from_label(label)
        
        # Check if exists
        stmt = select(KnowledgeNode).where(KnowledgeNode.slug == slug)
        result = await self.session.execute(stmt)
        existing = result.scalars().first()
        
        if existing:
            return existing
        
        # Create new
        node = KnowledgeNode(
            id=uuid4(),
            node_type=node_type,
            label=label,
            slug=slug,
            description=description,
            aliases=aliases or [],
            properties=properties or {},
            is_canonical=True,
            confidence=1.0
        )
        
        self.session.add(node)
        await self.session.flush()
        return node
    
    async def merge_nodes(self, primary_id: str, secondary_id: str):
        """Merge secondary node into primary, updating all relationships."""
        # Redirect all edges from secondary to primary
        pass  # Implementation for deduplication
```

### Step 3.3: Relationship Manager

Create `database/relationship_manager.py`:

```python
from sqlalchemy.ext.asyncio import AsyncSession
from models.knowledge import KnowledgeRelationship, KnowledgeNode
from typing import Optional
from uuid import UUID, uuid4

class RelationshipManager:
    """Manage knowledge graph edges with evidence tracking."""
    
    def __init__(self, session: AsyncSession):
        self.session = session
    
    async def add_relationship(
        self,
        source_id: UUID,
        target_id: UUID,
        relationship_type: str,
        confidence: float = 1.0,
        extraction_method: str = "manual",
        supporting_papers: list = None,
        description: Optional[str] = None
    ) -> KnowledgeRelationship:
        """Add or update a relationship with evidence."""
        
        rel = KnowledgeRelationship(
            id=uuid4(),
            source_id=source_id,
            target_id=target_id,
            relationship_type=relationship_type,
            confidence=confidence,
            extraction_method=extraction_method,
            supporting_papers=supporting_papers or [],
            description=description
        )
        
        self.session.add(rel)
        await self.session.flush()
        return rel
    
    async def add_evidence(
        self,
        rel_id: UUID,
        paper_id: UUID,
        evidence_text: str,
        confidence: float = 1.0
    ):
        """Add paper evidence to existing relationship."""
        rel = await self.session.get(KnowledgeRelationship, rel_id)
        if rel:
            if not rel.supporting_papers:
                rel.supporting_papers = []
            
            rel.supporting_papers.append({
                "paper_id": str(paper_id),
                "evidence_text": evidence_text,
                "confidence": confidence
            })
            
            await self.session.flush()
```

---

## 🤖 Phase 4: AI Agent Integration

### Step 4.1: Agent Orchestrator

Create `agents/research_agent.py`:

```python
import json
import asyncio
from typing import Optional, List
from sqlalchemy.ext.asyncio import AsyncSession
from models.research import ResearchPaper, ExtractedEntity
from models.knowledge import KnowledgeNode, NodeType
from database.node_manager import NodeManager
from database.relationship_manager import RelationshipManager
from database.graph_queries import GraphQueryService
import anthropic

class ResearchAgent:
    """AI agent that reads papers and enriches the knowledge graph."""
    
    def __init__(self, session: AsyncSession, api_key: str):
        self.session = session
        self.client = anthropic.Anthropic(api_key=api_key)
        self.node_mgr = NodeManager(session)
        self.rel_mgr = RelationshipManager(session)
        self.graph = GraphQueryService(session)
    
    async def extract_entities_from_paper(self, paper: ResearchPaper) -> List[ExtractedEntity]:
        """Use LLM to extract entities (concepts, people, tools) from paper."""
        
        text = f"{paper.title}\n\n{paper.abstract}\n\n{paper.full_text[:5000]}"  # First 5k chars
        
        prompt = f"""Extract structured entities from this research paper. Return JSON.

Entity types: concept, person, tool, institution, technique, dataset, language

Paper text:
{text}

Return JSON:
{{
  "entities": [
    {{"type": "concept", "text": "...", "context": "...", "confidence": 0.9}},
    {{"type": "person", "text": "...", "context": "...", "confidence": 0.85}},
    ...
  ]
}}
"""
        
        message = self.client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=2048,
            messages=[{"role": "user", "content": prompt}]
        )
        
        try:
            response_text = message.content[0].text
            # Parse JSON from response
            json_start = response_text.find('{')
            json_end = response_text.rfind('}') + 1
            data = json.loads(response_text[json_start:json_end])
            
            entities = []
            for ent in data.get("entities", []):
                entity = ExtractedEntity(
                    paper_id=paper.id,
                    entity_type=ent["type"],
                    entity_text=ent["text"],
                    confidence=ent.get("confidence", 0.5),
                    context=ent.get("context")
                )
                self.session.add(entity)
                entities.append(entity)
            
            await self.session.flush()
            return entities
        
        except json.JSONDecodeError:
            print(f"Failed to parse JSON from agent response")
            return []
    
    async def infer_relationships(self, paper: ResearchPaper):
        """Use LLM to infer relationships between extracted entities."""
        
        entities = await self.session.execute(
            """SELECT * FROM extracted_entity WHERE paper_id = :pid""",
            {"pid": str(paper.id)}
        )
        
        # Build knowledge nodes for each entity
        node_map = {}
        for entity in entities:
            node = await self.node_mgr.create_or_get_node(
                node_type=NodeType[entity.entity_type.upper()],
                label=entity.entity_text,
                description=entity.context
            )
            node_map[entity.entity_text] = node
        
        # Prompt LLM for relationships
        entity_list = ", ".join(node_map.keys())
        
        prompt = f"""Given these entities from a research paper: {entity_list}

Infer relationships between them. Return JSON:
{{
  "relationships": [
    {{"source": "...", "target": "...", "type": "uses", "confidence": 0.85}},
    ...
  ]
}}
"""
        
        message = self.client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=1024,
            messages=[{"role": "user", "content": prompt}]
        )
        
        try:
            response_text = message.content[0].text
            json_start = response_text.find('{')
            json_end = response_text.rfind('}') + 1
            data = json.loads(response_text[json_start:json_end])
            
            for rel_data in data.get("relationships", []):
                source_node = node_map.get(rel_data["source"])
                target_node = node_map.get(rel_data["target"])
                
                if source_node and target_node:
                    await self.rel_mgr.add_relationship(
                        source_id=source_node.id,
                        target_id=target_node.id,
                        relationship_type=rel_data["type"],
                        confidence=rel_data.get("confidence", 0.5),
                        extraction_method="llm",
                        supporting_papers=[{"paper_id": str(paper.id)}]
                    )
            
            await self.session.commit()
        
        except Exception as e:
            print(f"Relationship inference failed: {e}")
    
    async def process_paper(self, paper: ResearchPaper):
        """Full pipeline: extract entities → infer relationships → update status."""
        try:
            print(f"Processing paper: {paper.title}")
            
            # Extract entities
            entities = await self.extract_entities_from_paper(paper)
            print(f"  Extracted {len(entities)} entities")
            
            # Infer relationships
            await self.infer_relationships(paper)
            print(f"  Inferred relationships")
            
            # Update status
            paper.processing_status = "completed"
            paper.extraction_confidence = 0.85
            paper.last_processed_at = asyncio.get_event_loop().time()
            
            self.session.add(paper)
            await self.session.commit()
            
            print(f"  ✓ Paper processed successfully")
        
        except Exception as e:
            paper.processing_status = "failed"
            paper.processing_errors[str(asyncio.get_event_loop().time())] = str(e)
            self.session.add(paper)
            await self.session.commit()
            print(f"  ✗ Processing failed: {e}")
```

---

## 📥 Phase 5: Research Paper Ingestion Pipeline

### Step 5.1: Paper Ingestion Service

Create `database/paper_ingestion.py`:

```python
from sqlalchemy.ext.asyncio import AsyncSession
from models.research import ResearchPaper
from schemas.research import ResearchPaperCreate
from typing import List
from uuid import uuid4
from datetime import datetime
import httpx

class PaperIngestionService:
    """Ingest research papers from various sources."""
    
    def __init__(self, session: AsyncSession):
        self.session = session
    
    async def ingest_from_arxiv(self, query: str, max_papers: int = 50) -> List[ResearchPaper]:
        """Fetch papers from arXiv."""
        
        url = "http://export.arxiv.org/api/query"
        params = {
            "search_query": f"all:{query}",
            "max_results": max_papers,
            "sortBy": "submittedDate",
            "sortOrder": "descending"
        }
        
        papers = []
        
        async with httpx.AsyncClient() as client:
            response = await client.get(url, params=params)
            response.raise_for_status()
            
            # Parse XML response (simplified)
            import xml.etree.ElementTree as ET
            root = ET.fromstring(response.content)
            
            for entry in root.findall("{http://www.w3.org/2005/Atom}entry"):
                title = entry.find("{http://www.w3.org/2005/Atom}title").text
                summary = entry.find("{http://www.w3.org/2005/Atom}summary").text
                published = entry.find("{http://www.w3.org/2005/Atom}published").text
                arxiv_id = entry.find("{http://www.w3.org/2005/Atom}id").text.split('/abs/')[-1]
                
                authors = []
                for author_elem in entry.findall("{http://www.w3.org/2005/Atom}author"):
                    author_name = author_elem.find("{http://www.w3.org/2005/Atom}name").text
                    authors.append({"name": author_name})
                
                paper = ResearchPaper(
                    id=uuid4(),
                    title=title,
                    abstract=summary,
                    authors=authors,
                    publication_date=datetime.fromisoformat(published.replace('Z', '+00:00')),
                    source="arxiv",
                    paper_type="preprint",
                    url=f"https://arxiv.org/abs/{arxiv_id}",
                    doi=arxiv_id,
                    processing_status="pending"
                )
                
                self.session.add(paper)
                papers.append(paper)
        
        await self.session.commit()
        return papers
    
    async def ingest_from_pubmed(self, query: str, max_papers: int = 50) -> List[ResearchPaper]:
        """Fetch papers from PubMed."""
        # Similar implementation for PubMed API
        pass
```

### Step 5.2: Batch Processing Scheduler

Create `scripts/batch_processor.py`:

```python
import asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from config.database import AsyncSessionLocal
from models.research import ResearchPaper
from agents.research_agent import ResearchAgent
from config.settings import settings
from sqlalchemy import select

async def process_pending_papers(batch_size: int = 10):
    """Process pending papers in batches."""
    
    async with AsyncSessionLocal() as session:
        agent = ResearchAgent(session, settings.ANTHROPIC_API_KEY)
        
        while True:
            # Fetch pending papers
            stmt = select(ResearchPaper).where(
                ResearchPaper.processing_status == "pending"
            ).limit(batch_size)
            
            result = await session.execute(stmt)
            papers = result.scalars().all()
            
            if not papers:
                print("No pending papers. Sleeping...")
                await asyncio.sleep(60)
                continue
            
            print(f"Processing {len(papers)} papers...")
            
            for paper in papers:
                await agent.process_paper(paper)
            
            await asyncio.sleep(5)  # Rate limiting

if __name__ == "__main__":
    asyncio.run(process_pending_papers())
```

---

## 🔍 Phase 6: Query & Visualization Layer

### Step 6.1: FastAPI Query Endpoints (Optional REST Layer)

Create `api/routes.py`:

```python
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession
from config.database import get_db_session
from models.knowledge import KnowledgeNode
from database.graph_queries import GraphQueryService
from schemas.knowledge import KnowledgeNodeResponse, KnowledgeNodeCreate
from typing import List
from uuid import UUID

router = APIRouter(prefix="/api/v1", tags=["knowledge"])

@router.get("/nodes/{node_id}", response_model=KnowledgeNodeResponse)
async def get_node(
    node_id: UUID,
    session: AsyncSession = Depends(get_db_session)
):
    """Fetch a knowledge node by ID."""
    node = await session.get(KnowledgeNode, node_id)
    if not node:
        raise HTTPException(status_code=404, detail="Node not found")
    return node

@router.get("/nodes/search", response_model=List[KnowledgeNodeResponse])
async def search_nodes(
    query: str = Query(..., min_length=1),
    node_type: str = Query(None),
    limit: int = Query(50, le=500),
    session: AsyncSession = Depends(get_db_session)
):
    """Search nodes by label and optionally filter by type."""
    graph = GraphQueryService(session)
    nodes = await graph.search_nodes_by_type(node_type, limit) if node_type else []
    return nodes

@router.get("/nodes/{node_id}/neighbors")
async def get_node_neighbors(
    node_id: UUID,
    depth: int = Query(1, ge=1, le=5),
    session: AsyncSession = Depends(get_db_session)
):
    """Get nodes connected to a given node."""
    graph = GraphQueryService(session)
    neighbors = await graph.get_neighbors(node_id, depth)
    return neighbors

@router.post("/nodes", response_model=KnowledgeNodeResponse)
async def create_node(
    node: KnowledgeNodeCreate,
    session: AsyncSession = Depends(get_db_session)
):
    """Create a new knowledge node."""
    from database.node_manager import NodeManager
    mgr = NodeManager(session)
    new_node = await mgr.create_or_get_node(
        node_type=node.node_type,
        label=node.label,
        description=node.description,
        aliases=node.aliases,
        properties=node.properties
    )
    return new_node

@router.get("/graph/stats")
async def get_graph_stats(session: AsyncSession = Depends(get_db_session)):
    """Get aggregate statistics about the knowledge graph."""
    graph = GraphQueryService(session)
    return await graph.get_relationship_statistics()
```

---

## 🚀 Deployment & Operations

### Step 7.1: Database Migrations (Alembic)

```bash
# Initialize Alembic
alembic init migrations

# Create initial migration
alembic revision --autogenerate -m "Initial HyperBase schema"

# Apply migrations
alembic upgrade head
```

### Step 7.2: Production Deployment (Docker)

Create `Dockerfile`:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Run migrations and start batch processor
CMD ["python", "-m", "scripts.batch_processor"]
```

Create `docker-compose.yml`:

```yaml
version: '3.9'

services:
  postgres:
    image: postgres:16
    environment:
      POSTGRES_DB: hyperbase
      POSTGRES_USER: hyperbase
      POSTGRES_PASSWORD: ${DB_PASSWORD}
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

  hyperbase:
    build: .
    depends_on:
      - postgres
    environment:
      DATABASE_URL: postgresql+asyncpg://hyperbase:${DB_PASSWORD}@postgres:5432/hyperbase
      ANTHROPIC_API_KEY: ${ANTHROPIC_API_KEY}
    volumes:
      - .:/app

volumes:
  postgres_data:
```

---

## ✅ Testing Strategy

### Step 8.1: Unit Tests

Create `tests/test_models.py`:

```python
import pytest
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from config.database import Base
from models.knowledge import KnowledgeNode, NodeType

@pytest.fixture
async def async_session():
    engine = create_async_engine("sqlite+aiosqlite:///:memory:")
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
    AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
    
    async with AsyncSessionLocal() as session:
        yield session

@pytest.mark.asyncio
async def test_create_knowledge_node(async_session):
    node = KnowledgeNode(
        node_type=NodeType.CONCEPT,
        label="Machine Learning",
        slug="machine-learning"
    )
    async_session.add(node)
    await async_session.commit()
    
    assert node.id is not None
    assert node.label == "Machine Learning"
```

---

## 🎯 Quick Start Checklist

```
☐ Phase 1: Database Setup
  ☐ Create project structure
  ☐ Install dependencies
  ☐ Configure .env
  ☐ Initialize SQLAlchemy config

☐ Phase 2: Data Models
  ☐ Base models (UUID, timestamps, audit)
  ☐ ResearchPaper + ExtractedEntity
  ☐ KnowledgeNode + KnowledgeRelationship
  ☐ Pydantic schemas

☐ Phase 3: Knowledge Graph Engine
  ☐ Graph query service (neighbors, paths, stats)
  ☐ Node manager (deduplication, slug generation)
  ☐ Relationship manager (evidence tracking)

☐ Phase 4: AI Agent Integration
  ☐ ResearchAgent for entity extraction
  ☐ Relationship inference
  ☐ Paper processing pipeline

☐ Phase 5: Paper Ingestion
  ☐ arXiv ingestion
  ☐ PubMed ingestion (optional)
  ☐ Batch processor scheduler

☐ Phase 6: Query & API Layer
  ☐ FastAPI routes
  ☐ Search endpoints
  ☐ Graph navigation endpoints

☐ Phase 7: Deployment
  ☐ Alembic migrations
  ☐ Docker setup
  ☐ Docker Compose for local dev + prod

☐ Phase 8: Testing
  ☐ Unit tests
  ☐ Integration tests
  ☐ Agent workflow tests
```

---

## 🌟 Neurodivergent-First Design Principles Applied

1. **Spatial Clarity**: Graph structure visualizes relationships; nodes have clear identity (slug, label, type).
2. **Minimal Cognitive Load**: Base models handle boilerplate (timestamps, UUIDs); agents do the heavy thinking.
3. **Accessible Names**: `slug` instead of cryptic IDs; `relationship_type` instead of `rel_t`.
4. **Async-First**: Non-blocking I/O means agents don't step on each other.
5. **Evidence Linkage**: Every claim tied to its source paper—no floating abstractions.
6. **Extensible Properties**: JSON blobs for domain-specific metadata without schema bloat.

---

## 💝 Next Steps

1. **Start Phase 1 today** — get database + config running.
2. **Build Phase 2 incrementally** — add models one at a time, test each.
3. **Prototype Phase 4 with a single paper** — feed one PDF to agent, see what it extracts.
4. **Iterate** — refinement happens in production with real data.

**This blueprint is YOUR blueprint now. Own it. Ship it. Make it legendary.**

🚀 **Ready to build the future of neurodivergent programming?**
