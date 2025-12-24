# HyperCode CLI - Main Entry Point
# Integrated CLI with database management and auto-research controls

import logging
import sys
from datetime import datetime
from typing import Optional

import click

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


# ============================================================================
# Main CLI Group
# ============================================================================


@click.group()
@click.version_option()
@click.option("--verbose", "-v", is_flag=True, help="Enable verbose logging")
def cli(verbose):
    """
    🚀 HyperCode - Programming Language for Neurodivergent Brains & AI Systems

    A living research language bridging forgotten innovations with quantum/molecular computing.
    Built for ADHD, dyslexic, autistic minds. Universal AI compatibility. Open source.
    """
    if verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    pass


# ============================================================================
# Database Commands
# ============================================================================


@cli.group()
def database():
    """Database management commands."""
    pass


@database.command()
def init():
    """Initialize database schema."""
    from database_utils.db import init_db

    try:
        if click.confirm("Initialize database? This will create all tables."):
            init_db()
            click.echo("✓ Database initialized successfully")
    except Exception as e:
        click.echo(f"✗ Error: {e}", err=True)
        sys.exit(1)


@database.command()
def reset():
    """Reset database (DESTRUCTIVE - DELETE ALL DATA)."""
    from database_utils.db import init_db

    if not click.confirm("⚠️  WARNING: This will DELETE ALL DATA. Continue?"):
        click.echo("Cancelled.")
        return

    if not click.confirm('Type "yes" to confirm permanent deletion', default=False):
        click.echo("Cancelled.")
        return

    try:
        init_db(drop_all=True)
        click.echo("✓ Database reset complete")
    except Exception as e:
        click.echo(f"✗ Error: {e}", err=True)
        sys.exit(1)


@database.command()
def status():
    """Check database connection and status."""
    from database_utils.db import check_db_connection, get_db_stats

    try:
        if check_db_connection():
            click.echo("✓ Database connected")

            stats = get_db_stats()
            click.echo("\nDatabase Statistics:")
            click.echo("=" * 50)

            table_data = []
            for key, value in stats.items():
                label = key.replace("_", " ").title()
                table_data.append(f"  {label:.<35} {value:>5}")

            for line in table_data:
                click.echo(line)
        else:
            click.echo("✗ Database connection failed", err=True)
            sys.exit(1)

    except Exception as e:
        click.echo(f"✗ Error: {e}", err=True)
        sys.exit(1)


# ============================================================================
# Research/Auto-Research Commands
# ============================================================================


@cli.group()
def research():
    """Auto-research mode and knowledge graph management."""
    pass


@research.command()
@click.option("--query", "-q", required=True, help="Search query for papers")
@click.option(
    "--sources",
    "-s",
    multiple=True,
    default=["arxiv", "pubmed"],
    help="Document sources (arxiv, pubmed, scholar)",
)
@click.option("--limit", "-l", type=int, default=10, help="Max papers to retrieve")
@click.option("--continuous", is_flag=True, help="Run in continuous monitoring mode")
def auto_research(query: str, sources: tuple, limit: int, continuous: bool):
    """
    Start auto-research mode.

    Automatically fetches, analyzes, and indexes research papers.
    Updates knowledge graph continuously.
    """
    import asyncio

    from database_utils.research_agent import AutoResearchManager

    try:
        manager = AutoResearchManager()
        manager.initialize_agents()

        click.echo(f"🔬 Auto-Research Mode")
        click.echo(f"  Query: {query}")
        click.echo(f"  Sources: {', '.join(sources)}")
        click.echo(f"  Limit: {limit}")
        click.echo(f"  Continuous: {continuous}")
        click.echo()

        async def run():
            await manager.auto_research_mode(query=query, limit=limit)

        if continuous:
            click.echo("⚡ Running in continuous mode (Ctrl+C to stop)...")
            try:
                asyncio.run(run())
            except KeyboardInterrupt:
                click.echo("\n✓ Auto-research stopped")
        else:
            asyncio.run(run())
            click.echo("✓ Auto-research complete")

    except Exception as e:
        click.echo(f"✗ Error: {e}", err=True)
        sys.exit(1)


@research.command()
@click.option("--paper-id", "-p", type=int, help="Specific paper ID to process")
@click.option(
    "--status",
    "-s",
    type=click.Choice(["pending", "all"]),
    default="pending",
    help="Filter by status",
)
def process_papers(paper_id: Optional[int], status: str):
    """Process papers through the research pipeline."""
    import asyncio

    from database_utils.db import get_db_context
    from database_utils.models import ResearchPaper, ResearchTask
    from database_utils.research_agent import AutoResearchManager, TaskStatus

    try:
        with get_db_context() as session:
            query = session.query(ResearchPaper)

            if paper_id:
                query = query.filter_by(id=paper_id)
            elif status == "pending":
                query = query.filter_by(processing_status="pending")

            papers = query.all()

            if not papers:
                click.echo("No papers to process")
                return

            click.echo(f"Processing {len(papers)} paper(s)...")

            manager = AutoResearchManager()
            manager.initialize_agents()

            async def process_all():
                for paper in papers:
                    click.echo(f"  Processing: {paper.title[:60]}...")

                    # Create task
                    task = ResearchTask(
                        task_type="document_processing",
                        source_paper_id=paper.id,
                        status=TaskStatus.PENDING.value,
                        priority=0,
                    )
                    session.add(task)
                    session.commit()

                    result = await manager.process_research_task(task.id)
                    click.echo(f"    ✓ Status: {result.status.value}")
                    if result.error:
                        click.echo(f"    ✗ Error: {result.error}")

            asyncio.run(process_all())
            click.echo("✓ Processing complete")

    except Exception as e:
        click.echo(f"✗ Error: {e}", err=True)
        sys.exit(1)


@research.command()
def agents():
    """List registered research agents."""
    from database_utils.db import get_db_context
    from database_utils.models import ResearchAgent

    try:
        with get_db_context() as session:
            agents_list = session.query(ResearchAgent).all()

            if not agents_list:
                click.echo("No agents registered")
                return

            click.echo("Registered Research Agents:")
            click.echo("=" * 80)

            for agent in agents_list:
                click.echo(f"\n  Name: {agent.name}")
                click.echo(f"  Type: {agent.agent_type}")
                click.echo(f"  Model: {agent.model_name or 'N/A'}")
                click.echo(f"  Status: {agent.status}")
                click.echo(f"  Success Rate: {agent.success_rate:.1%}")

    except Exception as e:
        click.echo(f"✗ Error: {e}", err=True)
        sys.exit(1)


# ============================================================================
# Knowledge Graph Commands
# ============================================================================


@cli.group()
def knowledge():
    """Knowledge graph management and query."""
    pass


@knowledge.command()
@click.option("--node-type", "-t", help="Filter by node type")
@click.option("--limit", "-l", type=int, default=20, help="Max results")
def nodes(node_type: Optional[str], limit: int):
    """List knowledge graph nodes."""
    from database_utils.db import get_db_context
    from database_utils.models import KnowledgeNode

    try:
        with get_db_context() as session:
            query = session.query(KnowledgeNode)

            if node_type:
                query = query.filter_by(node_type=node_type)

            nodes_list = (
                query.order_by(KnowledgeNode.frequency.desc()).limit(limit).all()
            )

            if not nodes_list:
                click.echo("No nodes found")
                return

            click.echo("Knowledge Graph Nodes:")
            click.echo("=" * 80)

            for node in nodes_list:
                click.echo(f"\n  ID: {node.id}")
                click.echo(f"  Type: {node.node_type}")
                click.echo(f"  Label: {node.label}")
                click.echo(f"  Confidence: {node.confidence_score:.2%}")
                click.echo(f"  Frequency: {node.frequency}")
                if node.description:
                    click.echo(f"  Description: {node.description[:60]}...")

    except Exception as e:
        click.echo(f"✗ Error: {e}", err=True)
        sys.exit(1)


@knowledge.command()
@click.option("--rel-type", "-t", help="Filter by relationship type")
@click.option("--limit", "-l", type=int, default=20, help="Max results")
def relationships(rel_type: Optional[str], limit: int):
    """List knowledge graph relationships."""
    from database_utils.db import get_db_context
    from database_utils.models import KnowledgeNode, KnowledgeRelationship

    try:
        with get_db_context() as session:
            query = session.query(KnowledgeRelationship)

            if rel_type:
                query = query.filter_by(relationship_type=rel_type)

            relationships_list = (
                query.order_by(KnowledgeRelationship.confidence_score.desc())
                .limit(limit)
                .all()
            )

            if not relationships_list:
                click.echo("No relationships found")
                return

            click.echo("Knowledge Graph Relationships:")
            click.echo("=" * 80)

            for rel in relationships_list:
                source = (
                    session.query(KnowledgeNode)
                    .filter_by(id=rel.source_node_id)
                    .first()
                )
                target = (
                    session.query(KnowledgeNode)
                    .filter_by(id=rel.target_node_id)
                    .first()
                )

                source_label = source.label if source else f"Node {rel.source_node_id}"
                target_label = target.label if target else f"Node {rel.target_node_id}"

                click.echo(f"\n  {source_label}")
                click.echo(f"    --[{rel.relationship_type}]--> ")
                click.echo(f"  {target_label}")
                click.echo(f"  Confidence: {rel.confidence_score:.2%}")

    except Exception as e:
        click.echo(f"✗ Error: {e}", err=True)
        sys.exit(1)


@knowledge.command()
@click.option("--node-id", "-n", type=int, required=True, help="Node ID to explore")
def graph(node_id: int):
    """Explore knowledge graph around a node."""
    from database_utils.db import get_db_context
    from database_utils.models import KnowledgeNode, KnowledgeRelationship

    try:
        with get_db_context() as session:
            node = session.query(KnowledgeNode).filter_by(id=node_id).first()

            if not node:
                click.echo(f"Node {node_id} not found")
                return

            click.echo(f"Node: {node.label} ({node.node_type})")
            click.echo("=" * 80)

            # Outgoing relationships
            outgoing = (
                session.query(KnowledgeRelationship)
                .filter_by(source_node_id=node_id)
                .all()
            )

            if outgoing:
                click.echo("\nOutgoing relationships:")
                for rel in outgoing:
                    target = (
                        session.query(KnowledgeNode)
                        .filter_by(id=rel.target_node_id)
                        .first()
                    )
                    if target:
                        click.echo(f"  → {rel.relationship_type} → {target.label}")

            # Incoming relationships
            incoming = (
                session.query(KnowledgeRelationship)
                .filter_by(target_node_id=node_id)
                .all()
            )

            if incoming:
                click.echo("\nIncoming relationships:")
                for rel in incoming:
                    source = (
                        session.query(KnowledgeNode)
                        .filter_by(id=rel.source_node_id)
                        .first()
                    )
                    if source:
                        click.echo(f"  ← {rel.relationship_type} ← {source.label}")

    except Exception as e:
        click.echo(f"✗ Error: {e}", err=True)
        sys.exit(1)


# ============================================================================
# Admin/System Commands
# ============================================================================


@cli.group()
def system():
    """System and configuration commands."""
    pass


@system.command()
def version():
    """Show HyperCode version and system info."""
    try:
        import database_utils
        from database_utils.db import DatabaseConfig

        click.echo("HyperCode System Information")
        click.echo("=" * 50)
        click.echo(f"Database Type: {DatabaseConfig.DB_TYPE}")
        click.echo(f"Database: {DatabaseConfig.DATABASE_URL}")
        click.echo(f"Python: {sys.version.split()[0]}")
        click.echo(f"Timestamp: {datetime.utcnow().isoformat()}")

    except Exception as e:
        click.echo(f"✗ Error: {e}", err=True)
        sys.exit(1)


@system.command()
def health():
    """System health check."""
    from database_utils.db import check_db_connection, get_db_stats

    try:
        click.echo("HyperCode Health Check")
        click.echo("=" * 50)

        # Database
        if check_db_connection():
            click.echo("✓ Database: Connected")
            stats = get_db_stats()
            click.echo(f"  Total papers: {stats.get('papers', 0)}")
            click.echo(f"  Total agents: {stats.get('agents', 0)}")
            click.echo(f"  Knowledge nodes: {stats.get('knowledge_nodes', 0)}")
        else:
            click.echo("✗ Database: Failed")

        click.echo("\n✓ System ready")

    except Exception as e:
        click.echo(f"✗ Error: {e}", err=True)
        sys.exit(1)


# ============================================================================
# Entry Point
# ============================================================================

if __name__ == "__main__":
    cli()
