# Database Models for HyperCode Auto-Research System
# SQLAlchemy ORM with Knowledge Graph Integration

from datetime import datetime
from typing import Optional, List
from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, ForeignKey, JSON, Enum, Float, Table, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import enum

Base = declarative_base()

# ============================================================================
# Association Tables (for Many-to-Many relationships)
# ============================================================================

paper_agents = Table(
    'paper_agents',
    Base.metadata,
    Column('paper_id', Integer, ForeignKey('research_papers.id'), primary_key=True),
    Column('agent_id', Integer, ForeignKey('research_agents.id'), primary_key=True)
)

task_dependencies = Table(
    'task_dependencies',
    Base.metadata,
    Column('parent_task_id', Integer, ForeignKey('research_tasks.id'), primary_key=True),
    Column('child_task_id', Integer, ForeignKey('research_tasks.id'), primary_key=True)
)

# ============================================================================
# Core Research Models
# ============================================================================

class ResearchPaper(Base):
    """
    Core research document storage.
    Represents papers, articles, and data sources for knowledge graph enrichment.
    """
    __tablename__ = 'research_papers'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(500), nullable=False, index=True)
    authors = Column(String(1000))
    abstract = Column(Text)
    content = Column(Text)
    source_url = Column(String(500), unique=True, index=True)
    doi = Column(String(100), unique=True, index=True)
    published_date = Column(DateTime, index=True)
    ingested_date = Column(DateTime, default=datetime.utcnow, index=True)
    
    # Processing metadata
    processing_status = Column(String(50), default='pending')  # pending, processing, completed, failed
    confidence_score = Column(Float, default=0.0)
    
    # Relations
    agents = relationship("ResearchAgent", secondary=paper_agents, back_populates="papers")
    tasks = relationship("ResearchTask", back_populates="source_paper")
    entities = relationship("KnowledgeNode", back_populates="source_paper")
    relationships = relationship("KnowledgeRelationship", back_populates="source_paper")
    
    __table_args__ = (
        UniqueConstraint('doi', 'source_url', name='unique_paper_source'),
    )


class ResearchAgent(Base):
    """
    Autonomous research agents for multi-agent system.
    Each agent specializes in a specific task (retrieval, filtering, extraction, etc).
    Based on KARMA architecture: 9 specialized agents + 1 controller.
    """
    __tablename__ = 'research_agents'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False, index=True)
    agent_type = Column(String(50), nullable=False)  # retrieval, filtering, summarization, entity_extraction, etc.
    description = Column(Text)
    model_name = Column(String(100))  # GPT-4, Claude, DeepSeek, etc.
    system_prompt = Column(Text)
    status = Column(String(50), default='active')  # active, inactive, testing
    version = Column(String(50), default='1.0')
    
    # Performance metrics
    success_rate = Column(Float, default=0.0)
    avg_processing_time = Column(Float)  # seconds
    last_used = Column(DateTime)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relations
    papers = relationship("ResearchPaper", secondary=paper_agents, back_populates="agents")
    tasks = relationship("ResearchTask", back_populates="assigned_agent")
    
    # Configuration
    config = Column(JSON)  # Agent-specific configuration


class ResearchTask(Base):
    """
    Task queue for autonomous research operations.
    Tracks research tasks, their status, and dependencies.
    """
    __tablename__ = 'research_tasks'
    
    id = Column(Integer, primary_key=True)
    task_type = Column(String(100), nullable=False)  # document_retrieval, filtering, extraction, etc.
    description = Column(Text)
    status = Column(String(50), default='pending')  # pending, running, completed, failed
    priority = Column(Integer, default=0)  # Higher = more urgent
    
    # Relations
    source_paper_id = Column(Integer, ForeignKey('research_papers.id'))
    assigned_agent_id = Column(Integer, ForeignKey('research_agents.id'))
    
    source_paper = relationship("ResearchPaper", back_populates="tasks")
    assigned_agent = relationship("ResearchAgent", back_populates="tasks")
    
    # Dependencies (for workflow orchestration)
    parent_tasks = relationship(
        "ResearchTask",
        secondary=task_dependencies,
        primaryjoin=id == task_dependencies.c.child_task_id,
        secondaryjoin=id == task_dependencies.c.parent_task_id,
        foreign_keys=[task_dependencies.c.parent_task_id, task_dependencies.c.child_task_id]
    )
    
    # Metadata
    created_at = Column(DateTime, default=datetime.utcnow, index=True)
    started_at = Column(DateTime)
    completed_at = Column(DateTime)
    result = Column(JSON)  # Task output/result
    error_message = Column(Text)
    execution_time = Column(Float)  # seconds


# ============================================================================
# Knowledge Graph Models (Neo4j-inspired, but stored in SQL)
# ============================================================================

class KnowledgeNode(Base):
    """
    Knowledge graph nodes representing entities and concepts.
    Examples: researchers, institutions, concepts, methodologies, tools, etc.
    """
    __tablename__ = 'knowledge_nodes'
    
    id = Column(Integer, primary_key=True)
    node_type = Column(String(100), nullable=False, index=True)  # person, institution, concept, methodology, tool, etc.
    label = Column(String(500), nullable=False, index=True)  # Entity name/label
    canonical_form = Column(String(500))  # Normalized canonical form
    description = Column(Text)
    
    # Source tracking
    source_paper_id = Column(Integer, ForeignKey('research_papers.id'))
    source_paper = relationship("ResearchPaper", back_populates="entities")
    
    # Confidence & metadata
    confidence_score = Column(Float, default=0.0)  # 0-1, how confident we are in this entity
    frequency = Column(Integer, default=1)  # How many times appeared in documents
    
    # Knowledge management
    is_verified = Column(Boolean, default=False)
    is_canonical = Column(Boolean, default=False)
    last_updated = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Attributes (flexible schema)
    properties = Column(JSON)  # Additional metadata as JSON
    
    # Relations
    outgoing_relationships = relationship(
        "KnowledgeRelationship",
        foreign_keys="KnowledgeRelationship.source_node_id",
        back_populates="source_node"
    )
    incoming_relationships = relationship(
        "KnowledgeRelationship",
        foreign_keys="KnowledgeRelationship.target_node_id",
        back_populates="target_node"
    )
    
    __table_args__ = (
        UniqueConstraint('node_type', 'canonical_form', name='unique_entity'),
    )


class KnowledgeRelationship(Base):
    """
    Knowledge graph relationships between nodes.
    Represents how concepts, researchers, and methodologies are connected.
    """
    __tablename__ = 'knowledge_relationships'
    
    id = Column(Integer, primary_key=True)
    relationship_type = Column(String(100), nullable=False, index=True)  # author_of, uses, extends, contradicts, etc.
    source_node_id = Column(Integer, ForeignKey('knowledge_nodes.id'), nullable=False)
    target_node_id = Column(Integer, ForeignKey('knowledge_nodes.id'), nullable=False)
    
    # Source tracking
    source_paper_id = Column(Integer, ForeignKey('research_papers.id'))
    source_paper = relationship("ResearchPaper", back_populates="relationships")
    
    source_node = relationship("KnowledgeNode", foreign_keys=[source_node_id], back_populates="outgoing_relationships")
    target_node = relationship("KnowledgeNode", foreign_keys=[target_node_id], back_populates="incoming_relationships")
    
    # Confidence & metadata
    confidence_score = Column(Float, default=0.0)
    strength = Column(Float, default=1.0)  # How strong is this relationship
    
    # Attributes
    properties = Column(JSON)  # Additional relationship metadata
    
    created_at = Column(DateTime, default=datetime.utcnow)
    last_updated = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class ConflictRecord(Base):
    """
    Track conflicts detected between new research and existing knowledge.
    Used by conflict resolution agent.
    """
    __tablename__ = 'conflict_records'
    
    id = Column(Integer, primary_key=True)
    node_id = Column(Integer, ForeignKey('knowledge_nodes.id'))
    relationship_id = Column(Integer, ForeignKey('knowledge_relationships.id'))
    
    conflict_type = Column(String(100))  # contradiction, duplicate, version_mismatch, etc.
    severity = Column(String(50))  # low, medium, high
    new_value = Column(Text)  # The conflicting new value
    existing_value = Column(Text)  # The existing value in KG
    
    resolution_status = Column(String(50), default='unresolved')  # unresolved, resolved, merged, deprecated
    resolution_method = Column(String(100))  # evidence_based, majority_voting, timestamp_based, etc.
    
    evidence_count = Column(Integer, default=0)
    supporting_papers = Column(JSON)  # List of paper IDs supporting the conflict
    
    created_at = Column(DateTime, default=datetime.utcnow)
    resolved_at = Column(DateTime)


class ResearchMetrics(Base):
    """
    Track metrics about the research system and auto-research mode.
    For monitoring, optimization, and reporting.
    """
    __tablename__ = 'research_metrics'
    
    id = Column(Integer, primary_key=True)
    metric_name = Column(String(200), nullable=False, index=True)
    metric_value = Column(Float)
    metric_data = Column(JSON)  # Complex metric data
    
    timestamp = Column(DateTime, default=datetime.utcnow, index=True)
    
    # Scope
    agent_id = Column(Integer, ForeignKey('research_agents.id'))
    task_id = Column(Integer, ForeignKey('research_tasks.id'))
    
    # Examples:
    # - papers_ingested_today
    # - avg_confidence_score
    # - conflict_resolution_rate
    # - agent_success_rate
    # - knowledge_graph_size
