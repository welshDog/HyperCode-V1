"""
Canonical database utilities package for HyperCode.
Exports ORM models, engine/session helpers, and the research agent orchestrator.
"""

from .db import (
    Base,
    DatabaseConfig,
    check_db_connection,
    close_db,
    engine,
    get_db,
    get_db_context,
    get_db_stats,
    init_db,
    SessionLocal,
)
from .async_db import (
    async_engine,
    AsyncSessionLocal,
    get_async_db,
    ASYNC_DATABASE_URL,
)
from .metrics import record_metric
from .schemas import (
    DocumentRetrievalPayload,
    Entity,
    ExtractionResult,
    FilterPayload,
    Relationship,
    SummarizePayload,
)
from .canonicalization import slugify_label, entity_key
from .models import (
    ConflictRecord,
    KnowledgeNode,
    KnowledgeRelationship,
    ResearchAgent,
    ResearchMetrics,
    ResearchPaper,
    ResearchTask,
    paper_agents,
    task_dependencies,
)
from .research_agent import (
    AgentType,
    AutoResearchManager,
    BaseResearchAgent,
    ControllerAgent,
    DocumentRetrievalAgent,
    EntityExtractionAgent,
    EvaluationAgent,
    FilteringAgent,
    ConflictResolutionAgent,
    RelationshipExtractionAgent,
    SchemaAlignmentAgent,
    SummarizationAgent,
    TaskResult,
    TaskStatus,
)

__all__ = [
    # DB primitives
    "Base",
    "DatabaseConfig",
    "engine",
    "SessionLocal",
    "async_engine",
    "AsyncSessionLocal",
    "init_db",
    "get_db",
    "get_async_db",
    "get_db_context",
    "close_db",
    "check_db_connection",
    "get_db_stats",
    "ASYNC_DATABASE_URL",
    # Canonicalization
    "slugify_label",
    "entity_key",
    # Models
    "ResearchPaper",
    "ResearchAgent",
    "ResearchTask",
    "KnowledgeNode",
    "KnowledgeRelationship",
    "ConflictRecord",
    "ResearchMetrics",
    "paper_agents",
    "task_dependencies",
    # Agents
    "AgentType",
    "TaskStatus",
    "TaskResult",
    "BaseResearchAgent",
    "DocumentRetrievalAgent",
    "FilteringAgent",
    "SummarizationAgent",
    "EntityExtractionAgent",
    "RelationshipExtractionAgent",
    "SchemaAlignmentAgent",
    "ConflictResolutionAgent",
    "EvaluationAgent",
    "ControllerAgent",
    "AutoResearchManager",
    # Metrics
    "record_metric",
    # Schemas
    "DocumentRetrievalPayload",
    "FilterPayload",
    "SummarizePayload",
    "Entity",
    "Relationship",
    "ExtractionResult",
]
