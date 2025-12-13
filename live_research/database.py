import sqlite3
from pathlib import Path
from typing import List, Dict, Any, Optional
import json


class ResearchDatabase:
    def __init__(self, db_path: str = "research.db"):
        """Initialize the database connection and create tables if they don't exist."""
        self.db_path = db_path
        self._create_tables()

    def _get_connection(self):
        """Create and return a database connection."""
        return sqlite3.connect(self.db_path)

    def _create_tables(self):
        """Create the necessary tables if they don't exist."""
        with self._get_connection() as conn:
            cursor = conn.cursor()

            # Research entries table
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS research_entries (
                id TEXT PRIMARY KEY,
                date TEXT NOT NULL,
                topic TEXT NOT NULL,
                source TEXT,
                summary TEXT,
                details TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """)

            # Tags table
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS tags (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL
            )
            """)

            # Research entry tags junction table
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS research_entry_tags (
                entry_id TEXT,
                tag_id INTEGER,
                PRIMARY KEY (entry_id, tag_id),
                FOREIGN KEY (entry_id) REFERENCES research_entries(id) ON DELETE CASCADE,
                FOREIGN KEY (tag_id) REFERENCES tags(id) ON DELETE CASCADE
            )
            """)

            # Create triggers for updated_at
            cursor.execute("""
            CREATE TRIGGER IF NOT EXISTS update_research_entries_timestamp
            AFTER UPDATE ON research_entries
            FOR EACH ROW
            BEGIN
                UPDATE research_entries SET updated_at = CURRENT_TIMESTAMP
                WHERE id = OLD.id;
            END;
            """)

            conn.commit()

    def add_research_entry(self, entry_data: Dict[str, Any]) -> bool:
        """Add a new research entry to the database."""
        required_fields = ["id", "date", "topic"]
        if not all(field in entry_data for field in required_fields):
            raise ValueError(f"Missing required fields. Required: {required_fields}")

        with self._get_connection() as conn:
            cursor = conn.cursor()

            try:
                # Insert or replace research entry
                cursor.execute(
                    """
                INSERT OR REPLACE INTO research_entries 
                (id, date, topic, source, summary, details)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                    (
                        entry_data["id"],
                        entry_data["date"],
                        entry_data["topic"],
                        entry_data.get("source", ""),
                        entry_data.get("summary", ""),
                        entry_data.get("details", ""),
                    ),
                )

                # Handle tags
                if "tags" in entry_data and isinstance(entry_data["tags"], list):
                    for tag_name in entry_data["tags"]:
                        # Insert tag if it doesn't exist
                        cursor.execute(
                            """
                        INSERT OR IGNORE INTO tags (name) VALUES (?)
                        """,
                            (tag_name,),
                        )

                        # Get tag ID
                        cursor.execute(
                            "SELECT id FROM tags WHERE name = ?", (tag_name,)
                        )
                        tag_id = cursor.fetchone()[0]

                        # Link tag to research entry
                        cursor.execute(
                            """
                        INSERT OR IGNORE INTO research_entry_tags (entry_id, tag_id)
                        VALUES (?, ?)
                        """,
                            (entry_data["id"], tag_id),
                        )

                conn.commit()
                return True

            except sqlite3.Error as e:
                print(f"Database error: {e}")
                return False

    def get_research_entry(self, entry_id: str) -> Optional[Dict[str, Any]]:
        """Retrieve a research entry by its ID."""
        with self._get_connection() as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()

            cursor.execute(
                """
            SELECT * FROM research_entries WHERE id = ?
            """,
                (entry_id,),
            )

            entry = cursor.fetchone()
            if not entry:
                return None

            # Get tags for this entry
            cursor.execute(
                """
            SELECT t.name FROM tags t
            JOIN research_entry_tags ret ON t.id = ret.tag_id
            WHERE ret.entry_id = ?
            """,
                (entry_id,),
            )

            tags = [row[0] for row in cursor.fetchall()]

            return dict(entry) | {"tags": tags}

    def search_entries(
        self, query: str = "", tag: str = None, limit: int = 100
    ) -> List[Dict[str, Any]]:
        """Search research entries by content or tags."""
        with self._get_connection() as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()

            sql = """
            SELECT DISTINCT re.* FROM research_entries re
            """

            params = []
            conditions = []

            if query:
                conditions.append("""
                (re.topic LIKE ? OR re.summary LIKE ? OR re.details LIKE ?)
                """)
                search_term = f"%{query}%"
                params.extend([search_term, search_term, search_term])

            if tag:
                conditions.append("""
                re.id IN (
                    SELECT ret.entry_id FROM research_entry_tags ret
                    JOIN tags t ON ret.tag_id = t.id
                    WHERE t.name = ?
                )
                """)
                params.append(tag)

            if conditions:
                sql += " WHERE " + " AND ".join(conditions)

            sql += " ORDER BY re.date DESC, re.updated_at DESC"

            if limit:
                sql += " LIMIT ?"
                params.append(limit)

            cursor.execute(sql, params)
            entries = cursor.fetchall()

            # Get tags for each entry
            result = []
            for entry in entries:
                entry_id = entry["id"]
                cursor.execute(
                    """
                SELECT t.name FROM tags t
                JOIN research_entry_tags ret ON t.id = ret.tag_id
                WHERE ret.entry_id = ?
                """,
                    (entry_id,),
                )
                tags = [row[0] for row in cursor.fetchall()]
                result.append(dict(entry) | {"tags": tags})

            return result

    def import_from_json(self, json_path: str) -> int:
        """Import research entries from a JSON file."""
        try:
            with open(json_path, "r", encoding="utf-8") as f:
                entries = json.load(f)

            if not isinstance(entries, list):
                entries = [entries]

            success_count = 0
            for entry in entries:
                if self.add_research_entry(entry):
                    success_count += 1

            return success_count

        except (json.JSONDecodeError, FileNotFoundError, IOError) as e:
            print(f"Error importing from {json_path}: {e}")
            return 0


def setup_database() -> ResearchDatabase:
    """Initialize and return a configured ResearchDatabase instance."""
    # Create data directory if it doesn't exist
    data_dir = Path("c:\\Users\\lyndz\\Downloads\\hypercode PROJECT\\hypercode\\data")
    data_dir.mkdir(parents=True, exist_ok=True)

    # Initialize database
    db_path = str(data_dir / "research.db")
    db = ResearchDatabase(db_path)

    # Import existing JSON files if database is empty
    with db._get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM research_entries")
        if cursor.fetchone()[0] == 0:
            json_dir = data_dir / "reseach data json"
            if json_dir.exists() and json_dir.is_dir():
                for json_file in json_dir.glob("*.json"):
                    db.import_from_json(str(json_file))

    return db


# Example usage
if __name__ == "__main__":
    db = setup_database()
    print(f"Database initialized at: {db.db_path}")

    # Example search
    print("\nRecent entries:")
    for entry in db.search_entries(limit=3):
        print(
            f"- {entry['date']}: {entry['topic']} ({', '.join(entry['tags']) if 'tags' in entry else 'No tags'})"
        )
