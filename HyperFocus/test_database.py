"""Test script for HyperFocus database operations."""

import sys
from datetime import datetime, timedelta
from pathlib import Path

# Add the project root to the Python path
sys.path.append(str(Path(__file__).parent))

from hyperfocus.database import Session, Task
from hyperfocus.db_utils import create_task, get_db, get_task


def test_database_operations():
    """Test basic database operations."""
    print("\n=== Testing Database Operations ===")

    # Test creating a task
    with get_db() as session:
        print("\nCreating a new task...")
        task = create_task(
            session,
            title="Test Database Integration",
            description="Verify database operations are working",
            priority=1,  # High priority
            status="pending",
        )
        print(f"Created task: {task.id} - {task.title} (Status: {task.status})")

        # Test retrieving the task
        print("\nRetrieving the created task...")
        retrieved_task = get_task(session, task.id)
        if retrieved_task:
            print(
                f"Retrieved task: {retrieved_task.title} (Status: {retrieved_task.status})"
            )
        else:
            print("Error: Could not retrieve the created task!")
            return

        # Create a session for the task
        print("\nCreating a work session for the task...")
        work_session = Session(
            task_id=task.id,
            start_time=datetime.now() - timedelta(minutes=30),
            end_time=datetime.now(),
            duration=30 * 60,  # 30 minutes in seconds
            focus_score=8,
        )
        session.add(work_session)
        session.commit()
        print(f"Created session: {work_session.id} for task {task.id}")

        # Query tasks with their sessions
        print("\nQuerying tasks with their sessions...")
        tasks_with_sessions = session.query(Task).all()
        for t in tasks_with_sessions:
            print(f"\nTask: {t.title}")
            print(f"  - Status: {t.status}")
            print(f"  - Priority: {t.priority}")
            print(f"  - Created: {t.created_at}")
            print("  Sessions:")
            for s in t.sessions:
                print(
                    f"    - Duration: {s.duration // 60} minutes, Focus: {s.focus_score}/10"
                )


if __name__ == "__main__":
    print("Starting database tests...")
    try:
        test_database_operations()
        print("\n✅ Database tests completed successfully!")
    except Exception as e:
        print(f"\n❌ Error during database tests: {e}", file=sys.stderr)
        raise
