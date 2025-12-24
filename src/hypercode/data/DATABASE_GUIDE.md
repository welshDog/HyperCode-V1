# HyperCode Database & Auto-Research System - Quick Start Guide

## 🎯 What You Now Have

### Database Architecture
✅ **SQLAlchemy ORM** - Modern, async-ready SQL ORM
✅ **Multi-Database Support** - SQLite (dev), PostgreSQL, MySQL (prod)
✅ **Connection Pooling** - Production-grade connection management
✅ **Context Managers** - Safe transaction handling

### Database Schema
✅ **ResearchPaper** - Document storage with metadata
✅ **ResearchAgent** - 9 specialized agents + 1 controller
✅ **ResearchTask** - Task queue with dependencies
✅ **KnowledgeNodes** - Entities (people, concepts, tools, institutions)
✅ **KnowledgeRelationships** - Links between entities
✅ **ConflictRecords** - Track and resolve knowledge contradictions
✅ **ResearchMetrics** - System monitoring and analytics

### Auto-Research Mode (KARMA-inspired)
✅ **Multi-Agent System** - 9 specialized agents
✅ **Document Retrieval Agent** - Fetches papers from arXiv, PubMed, Scholar
✅ **Filtering Agent** - Removes noise, segments content
✅ **Summarization Agent** - Condenses text while preserving structure
✅ **Entity Extraction Agent** - Identifies people, concepts, tools, institutions
✅ **Relationship Extraction Agent** - Maps connections between entities
✅ **Schema Alignment Agent** - Maintains ontology consistency
✅ **Conflict Resolution Agent** - Handles knowledge contradictions
✅ **Evaluation Agent** - Quality control and confidence scoring
✅ **Controller Agent** - Orchestrates the entire pipeline

---

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install sqlalchemy alembic psycopg2-binary click
```

### 2. Initialize Database

```bash
# Initialize empty database
python -m database_utils.db init

# Check database status
python -m database_utils.db stats
```

### 3. Basic Database Operations

```python
from database_utils.db import get_db_context
from database_utils.models import ResearchPaper, ResearchAgent

# Add a research paper
with get_db_context() as session:
    paper = ResearchPaper(
        title="My Research Paper",
        authors="John Doe",
        source_url="https://example.com/paper.pdf",
        processing_status="pending"
    )
    session.add(paper)
    # Auto-commits on success, auto-rollbacks on error

# Query papers
with get_db_context() as session:
    papers = session.query(ResearchPaper).filter_by(
        processing_status="pending"
    ).all()
    for paper in papers:
        print(f"{paper.title} by {paper.authors}")
```

### 4. Initialize Auto-Research Mode

```python
from database_utils.research_agent import AutoResearchManager

# Initialize the multi-agent system
manager = AutoResearchManager()
manager.initialize_agents()

# Process a research task
import asyncio
async def run_research():
    result = await manager.process_research_task(task_id=1)
    print(f"Task completed with status: {result.status}")

asyncio.run(run_research())
```

---

## 📊 Database Configuration

### Environment Variables

```bash
# Database type: sqlite, postgresql, mysql
export DB_TYPE=sqlite

# Database location (SQLite)
export DB_PATH=data/research.db

# PostgreSQL credentials (if using PostgreSQL)
export DB_USER=postgres
export DB_PASSWORD=your_password
export DB_HOST=localhost
export DB_PORT=5432
export DB_NAME=hypercode

# Connection pooling
export DB_POOL_SIZE=10
export DB_MAX_OVERFLOW=20
export DB_POOL_RECYCLE=3600

# Debug SQL queries
export DB_ECHO_SQL=false
```

### Switch Between Databases

```bash
# Development: SQLite
export DB_TYPE=sqlite
export DB_PATH=data/research.db

# Production: PostgreSQL
export DB_TYPE=postgresql
export DB_USER=prod_user
export DB_PASSWORD=prod_password
export DB_HOST=prod.db.example.com
```

---

## 🔄 Auto-Research Pipeline

The pipeline processes research documents through 9 specialized agents:

```
┌─────────────────────────────────────────────────────────┐
│           Document Ingestion                            │
└──────────────────┬──────────────────────────────────────┘
                   ↓
┌─────────────────────────────────────────────────────────┐
│ 1. Document Retrieval Agent                             │
│    Fetches papers from arXiv, PubMed, Google Scholar   │
└──────────────────┬──────────────────────────────────────┘
                   ↓
┌─────────────────────────────────────────────────────────┐
│ 2. Filtering Agent                                      │
│    Removes boilerplate, segments content                │
└──────────────────┬──────────────────────────────────────┘
                   ↓
┌─────────────────────────────────────────────────────────┐
│ 3. Summarization Agent                                  │
│    Condenses text, preserves structure                  │
└──────────────────┬──────────────────────────────────────┘
                   ↓
┌─────────────────────────────────────────────────────────┐
│ 4. Entity Extraction Agent                              │
│    Identifies entities: people, concepts, tools, etc.   │
└──────────────────┬──────────────────────────────────────┘
                   ↓
┌─────────────────────────────────────────────────────────┐
│ 5. Relationship Extraction Agent                        │
│    Maps connections: author_of, uses, extends, etc.    │
└──────────────────┬──────────────────────────────────────┘
                   ↓
┌─────────────────────────────────────────────────────────┐
│ 6. Schema Alignment Agent                               │
│    Validates against KG ontology                        │
└──────────────────┬──────────────────────────────────────┘
                   ↓
┌─────────────────────────────────────────────────────────┐
│ 7. Conflict Resolution Agent                            │
│    Handles contradictions, merges duplicates            │
└──────────────────┬──────────────────────────────────────┘
                   ↓
┌─────────────────────────────────────────────────────────┐
│ 8. Evaluation Agent                                     │
│    Quality control, confidence scoring                  │
└──────────────────┬──────────────────────────────────────┘
                   ↓
┌─────────────────────────────────────────────────────────┐
│ 9. Knowledge Graph Writer                               │
│    Persists entities & relationships to database        │
└──────────────────┬──────────────────────────────────────┘
                   ↓
┌─────────────────────────────────────────────────────────┐
│           Updated Knowledge Graph                       │
└─────────────────────────────────────────────────────────┘
```

---

## 📝 Working with Knowledge Graphs

### Add Entities (Concepts, People, Tools)

```python
from database_utils.models import KnowledgeNode, KnowledgeRelationship

with get_db_context() as session:
    # Create entity nodes
    researcher = KnowledgeNode(
        node_type="person",
        label="John Doe",
        canonical_form="john_doe",
        description="AI researcher",
        confidence_score=0.95
    )
    
    tool = KnowledgeNode(
        node_type="tool",
        label="PyTorch",
        canonical_form="pytorch",
        description="Deep learning framework"
    )
    
    session.add(researcher)
    session.add(tool)
    session.flush()  # Get the IDs
    
    # Create relationship
    relationship = KnowledgeRelationship(
        relationship_type="uses",
        source_node_id=researcher.id,
        target_node_id=tool.id,
        confidence_score=0.9
    )
    
    session.add(relationship)
```

### Query Knowledge Graph

```python
# Find all entities of a type
researchers = session.query(KnowledgeNode).filter_by(
    node_type="person"
).all()

# Find relationships from an entity
node = session.query(KnowledgeNode).filter_by(
    canonical_form="john_doe"
).first()

uses_relationships = session.query(KnowledgeRelationship).filter_by(
    source_node_id=node.id,
    relationship_type="uses"
).all()

# Get connected entities
for rel in uses_relationships:
    target = session.query(KnowledgeNode).filter_by(
        id=rel.target_node_id
    ).first()
    print(f"{node.label} uses {target.label}")
```

---

## 🛠️ Database Migrations (Alembic)

### Initialize Alembic

```bash
alembic init alembic
```

### Create Migration

```bash
# Auto-generate migration from model changes
alembic revision --autogenerate -m "Add new_column to ResearchPaper"

# Manual migration
alembic revision -m "Custom migration"
```

### Apply Migrations

```bash
# Upgrade to latest version
alembic upgrade head

# Upgrade to specific version
alembic upgrade abc123def45

# Downgrade one step
alembic downgrade -1

# See current version
alembic current
```

---

## 📊 Monitoring & Metrics

### Get Database Statistics

```python
from database_utils.db import get_db_stats

stats = get_db_stats()
print(f"Papers: {stats['papers']}")
print(f"Agents: {stats['agents']}")
print(f"Tasks: {stats['tasks']}")
print(f"Knowledge Nodes: {stats['knowledge_nodes']}")
print(f"Relationships: {stats['knowledge_relationships']}")
```

### Track Task Execution

```python
with get_db_context() as session:
    # Get recent completed tasks
    tasks = session.query(ResearchTask).filter(
        ResearchTask.status == "completed"
    ).order_by(
        ResearchTask.completed_at.desc()
    ).limit(10).all()
    
    for task in tasks:
        print(f"Task {task.id}: {task.execution_time}s")
```

---

## 🚀 Next Steps: Implement AI Integration

### 1. Connect LLM Models

```python
# In each agent, replace TODO comments with actual LLM calls
# Support: OpenAI, Claude, DeepSeek, Ollama, custom models

async def extract_entities(self, text: str) -> List[Dict]:
    """Use LLM for entity extraction."""
    response = await call_llm(
        model=self.model,
        prompt=f"Extract entities from: {text}",
        system_prompt="You are an entity extraction expert"
    )
    return parse_entities(response)
```

### 2. Document Source Integration

```python
# Implement document retrieval from:
# - arXiv API (preprints)
# - PubMed API (biomedical)
# - Google Scholar (general)
# - Direct PDF downloads
# - Local file system
```

### 3. Knowledge Graph Enhancement

```python
# Add:
# - Neo4j backend for graph queries
# - Full-text search indexing
# - Vector embeddings for semantic search
# - Graph visualization
```

### 4. Production Deployment

```python
# Use PostgreSQL for data integrity
# Add Redis for caching and task queue
# Implement Celery for distributed agent execution
# Set up monitoring with Prometheus/Grafana
# Add logging with ELK stack
```

---

## 🔐 Best Practices

1. **Always use context managers** for database sessions:
   ```python
   with get_db_context() as session:
       # Your code here - auto-commits/rollbacks
   ```

2. **Use parameterized queries** to prevent SQL injection:
   ```python
   # ✅ Good
   session.query(ResearchPaper).filter_by(title=user_input).all()
   
   # ❌ Bad
   session.query(ResearchPaper).filter(f"title = '{user_input}'").all()
   ```

3. **Index frequently queried columns** - already done in models

4. **Use bulk operations** for large datasets:
   ```python
   session.bulk_insert_mappings(ResearchPaper, papers_list)
   ```

5. **Set reasonable pool sizes** based on workload

---

## 🐛 Troubleshooting

### Database Connection Issues
```bash
# Test connection
python -m database_utils.db stats

# Check connection string
export DB_TYPE=postgresql && python -c "from database_utils.db import DatabaseConfig; print(DatabaseConfig.DATABASE_URL)"
```

### Migration Problems
```bash
# See migration history
alembic history

# Check current schema version
alembic current

# Downgrade and retry
alembic downgrade -1
```

### Performance Issues
```python
# Enable SQL logging to see queries
export DB_ECHO_SQL=true

# Check query performance
session.query(...).statement.compile(compile_kwargs={"literal_binds": True})
```

---

## 📚 Resources

- **SQLAlchemy Docs**: https://docs.sqlalchemy.org
- **Alembic Docs**: https://alembic.sqlalchemy.org
- **KARMA Paper**: Knowledge Augmentation via Reasoning with Multiple Agents
- **arXiv API**: https://arxiv.org/help/api
- **PubMed API**: https://www.ncbi.nlm.nih.gov/pmc/tools/openapi/

---

**Ready to launch into auto-research mode! 🚀🔬**
