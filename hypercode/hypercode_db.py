""
HyperCode Database Module

This module provides database functionality for the HyperCode project,
including data storage, retrieval, and management of code entities.
"""

from typing import Dict, List, Optional, Any, Union
from dataclasses import dataclass, field
import json
import os
from pathlib import Path
import sqlite3
from datetime import datetime

@dataclass
class CodeEntity:
    """Represents a code entity in the HyperCode database."""
    
    id: str
    name: str
    entity_type: str  # e.g., 'function', 'class', 'variable', 'module'
    file_path: str
    line_number: int
    docstring: Optional[str] = None
    source_code: Optional[str] = None
    metadata: Dict[str, Any] = field(default_factory=dict)
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert the entity to a dictionary for serialization."""
        return {
            "id": self.id,
            "name": self.name,
            "entity_type": self.entity_type,
            "file_path": self.file_path,
            "line_number": self.line_number,
            "docstring": self.docstring,
            "source_code": self.source_code,
            "metadata": self.metadata,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'CodeEntity':
        """Create a CodeEntity from a dictionary."""
        return cls(
            id=data['id'],
            name=data['name'],
            entity_type=data['entity_type'],
            file_path=data['file_path'],
            line_number=data['line_number'],
            docstring=data.get('docstring'),
            source_code=data.get('source_code'),
            metadata=data.get('metadata', {}),
            created_at=datetime.fromisoformat(data['created_at']),
            updated_at=datetime.fromisoformat(data['updated_at'])
        )

class HypercodeDB:
    """Manages a database of code entities for the HyperCode project."""
    
    def __init__(self, db_path: Optional[str] = None):
        """Initialize the Hypercode database.
        
        Args:
            db_path: Path to the SQLite database file. If None, uses an in-memory database.
        """
        if db_path is None:
            # Use in-memory database by default
            self.connection = sqlite3.connect(":memory:")
        else:
            # Ensure the directory exists
            os.makedirs(os.path.dirname(os.path.abspath(db_path)), exist_ok=True)
            self.connection = sqlite3.connect(db_path)
        
        self._initialize_database()
    
    def _initialize_database(self) -> None:
        """Initialize the database schema if it doesn't exist."""
        cursor = self.connection.cursor()
        
        # Create entities table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS entities (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            entity_type TEXT NOT NULL,
            file_path TEXT NOT NULL,
            line_number INTEGER NOT NULL,
            docstring TEXT,
            source_code TEXT,
            metadata TEXT,
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL
        )
        ''')
        
        # Create indexes for faster lookups
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_entity_name ON entities(name)')
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_entity_type ON entities(entity_type)')
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_file_path ON entities(file_path)')
        
        self.connection.commit()
    
    def add_entity(self, entity: CodeEntity) -> None:
        """Add a code entity to the database.
        
        Args:
            entity: The code entity to add
        """
        cursor = self.connection.cursor()
        
        # Update timestamps
        entity.updated_at = datetime.utcnow()
        
        cursor.execute('''
        INSERT OR REPLACE INTO entities 
        (id, name, entity_type, file_path, line_number, docstring, source_code, metadata, created_at, updated_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            entity.id,
            entity.name,
            entity.entity_type,
            entity.file_path,
            entity.line_number,
            entity.docstring,
            entity.source_code,
            json.dumps(entity.metadata),
            entity.created_at.isoformat(),
            entity.updated_at.isoformat()
        ))
        
        self.connection.commit()
    
    def get_entity(self, entity_id: str) -> Optional[CodeEntity]:
        """Retrieve a code entity by its ID.
        
        Args:
            entity_id: The ID of the entity to retrieve
            
        Returns:
            The code entity, or None if not found
        """
        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM entities WHERE id = ?', (entity_id,))
        row = cursor.fetchone()
        
        if not row:
            return None
        
        return self._row_to_entity(row)
    
    def find_entities(
        self,
        name: Optional[str] = None,
        entity_type: Optional[str] = None,
        file_path: Optional[str] = None
    ) -> List[CodeEntity]:
        """Find code entities matching the given criteria.
        
        Args:
            name: Filter by entity name (case-insensitive partial match)
            entity_type: Filter by entity type (exact match)
            file_path: Filter by file path (case-sensitive partial match)
            
        Returns:
            A list of matching code entities
        """
        cursor = self.connection.cursor()
        query = 'SELECT * FROM entities WHERE 1=1'
        params = []
        
        if name is not None:
            query += ' AND name LIKE ?'
            params.append(f'%{name}%')
        
        if entity_type is not None:
            query += ' AND entity_type = ?'
            params.append(entity_type)
        
        if file_path is not None:
            query += ' AND file_path LIKE ?'
            params.append(f'%{file_path}%')
        
        cursor.execute(query, params)
        return [self._row_to_entity(row) for row in cursor.fetchall()]
    
    def delete_entity(self, entity_id: str) -> bool:
        """Delete a code entity from the database.
        
        Args:
            entity_id: The ID of the entity to delete
            
        Returns:
            True if the entity was deleted, False if not found
        """
        cursor = self.connection.cursor()
        cursor.execute('DELETE FROM entities WHERE id = ?', (entity_id,))
        self.connection.commit()
        return cursor.rowcount > 0
    
    def _row_to_entity(self, row: tuple) -> CodeEntity:
        """Convert a database row to a CodeEntity object."""
        return CodeEntity(
            id=row[0],
            name=row[1],
            entity_type=row[2],
            file_path=row[3],
            line_number=row[4],
            docstring=row[5],
            source_code=row[6],
            metadata=json.loads(row[7]) if row[7] else {},
            created_at=datetime.fromisoformat(row[8]),
            updated_at=datetime.fromisoformat(row[9])
        )
    
    def close(self) -> None:
        """Close the database connection."""
        self.connection.close()
    
    def __enter__(self):
        """Context manager entry."""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.close()

# Example usage
if __name__ == "__main__":
    # Create an in-memory database
    with HypercodeDB() as db:
        # Create a sample code entity
        entity = CodeEntity(
            id="func_hello_world",
            name="hello_world",
            entity_type="function",
            file_path="/path/to/file.py",
            line_number=10,
            docstring="A simple hello world function.",
            source_code="def hello_world():\n    print('Hello, world!')",
            metadata={"author": "John Doe", "version": "1.0.0"}
        )
        
        # Add the entity to the database
        db.add_entity(entity)
        
        # Retrieve the entity by ID
        retrieved = db.get_entity("func_hello_world")
        print(f"Retrieved entity: {retrieved.name} ({retrieved.entity_type})")
        
        # Search for entities
        results = db.find_entities(name="hello")
        print(f"Found {len(results)} matching entities")
