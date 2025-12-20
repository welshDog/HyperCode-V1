"""
Knowledge Base Module for HyperCode

This module provides functionality for managing a knowledge base of research documents,
including storage, retrieval, and search capabilities.
"""

from typing import List, Dict, Optional, Any, Union
from dataclasses import dataclass, field
from datetime import datetime
import json
import os
from pathlib import Path
import hashlib


@dataclass
class ResearchDocument:
    """Represents a research document in the knowledge base."""

    title: str
    content: str
    source: str
    document_type: str = "article"
    metadata: Dict[str, Any] = field(default_factory=dict)
    id: str = field(init=False)
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)

    def __post_init__(self):
        """Generate a unique ID for the document based on its content and metadata."""
        content_hash = hashlib.sha256(self.content.encode("utf-8")).hexdigest()
        self.id = f"doc_{content_hash[:16]}"

    def to_dict(self) -> Dict[str, Any]:
        """Convert the document to a dictionary for serialization."""
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "source": self.source,
            "document_type": self.document_type,
            "metadata": self.metadata,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ResearchDocument":
        """Create a ResearchDocument from a dictionary."""
        doc = cls(
            title=data["title"],
            content=data["content"],
            source=data["source"],
            document_type=data.get("document_type", "article"),
            metadata=data.get("metadata", {}),
        )
        doc.id = data["id"]
        doc.created_at = datetime.fromisoformat(data["created_at"])
        doc.updated_at = datetime.fromisoformat(data["updated_at"])
        return doc


class HyperCodeKnowledgeBase:
    """Manages a knowledge base of research documents with search capabilities."""

    def __init__(self, storage_path: Optional[str] = None):
        """Initialize the knowledge base with an optional storage path.

        Args:
            storage_path: Path to store the knowledge base data. If None, uses a default location.
        """
        if storage_path is None:
            # Default to a 'knowledge_base' directory in the current working directory
            self.storage_path = os.path.join(os.getcwd(), "knowledge_base")
        else:
            self.storage_path = storage_path

        # Create storage directory if it doesn't exist
        os.makedirs(self.storage_path, exist_ok=True)

        # In-memory storage for documents
        self.documents: Dict[str, ResearchDocument] = {}

        # Load existing documents from storage
        self._load_documents()

    def _get_document_path(self, doc_id: str) -> str:
        """Get the file path for a document."""
        return os.path.join(self.storage_path, f"{doc_id}.json")

    def _load_documents(self):
        """Load documents from the storage directory."""
        self.documents = {}

        for filename in os.listdir(self.storage_path):
            if filename.endswith(".json"):
                filepath = os.path.join(self.storage_path, filename)
                try:
                    with open(filepath, "r", encoding="utf-8") as f:
                        doc_data = json.load(f)
                        doc = ResearchDocument.from_dict(doc_data)
                        self.documents[doc.id] = doc
                except (json.JSONDecodeError, KeyError) as e:
                    print(f"Error loading document {filename}: {e}")

    def add_document(self, document: ResearchDocument) -> str:
        """Add a document to the knowledge base.

        Args:
            document: The document to add

        Returns:
            The ID of the added document
        """
        # Update timestamps
        document.updated_at = datetime.utcnow()

        # Save to storage
        filepath = self._get_document_path(document.id)
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(document.to_dict(), f, indent=2, default=str)

        # Update in-memory storage
        self.documents[document.id] = document

        return document.id

    def get_document(self, doc_id: str) -> Optional[ResearchDocument]:
        """Retrieve a document by its ID.

        Args:
            doc_id: The ID of the document to retrieve

        Returns:
            The requested document, or None if not found
        """
        return self.documents.get(doc_id)

    def search(self, query: str, limit: int = 10) -> List[Dict[str, Any]]:
        """Search for documents matching a query.

        This is a simple implementation that performs a case-insensitive
        substring search in document titles and content. A production
        implementation would use a proper search engine like Elasticsearch.

        Args:
            query: The search query
            limit: Maximum number of results to return

        Returns:
            A list of matching documents with relevance scores
        """
        query = query.lower()
        results = []

        for doc in self.documents.values():
            # Simple relevance scoring based on query term frequency
            title_score = doc.title.lower().count(query) * 2
            content_score = doc.content.lower().count(query)
            total_score = title_score + content_score

            if total_score > 0:
                results.append(
                    {
                        "document": doc,
                        "score": total_score,
                        "highlights": {
                            "title": doc.title,
                            "content_preview": doc.content[:200] + "..."
                            if len(doc.content) > 200
                            else doc.content,
                        },
                    }
                )

        # Sort by score in descending order
        results.sort(key=lambda x: x["score"], reverse=True)

        return results[:limit]

    def delete_document(self, doc_id: str) -> bool:
        """Delete a document from the knowledge base.

        Args:
            doc_id: The ID of the document to delete

        Returns:
            True if the document was deleted, False if not found
        """
        if doc_id not in self.documents:
            return False

        # Remove from storage
        filepath = self._get_document_path(doc_id)
        if os.path.exists(filepath):
            os.remove(filepath)

        # Remove from memory
        del self.documents[doc_id]

        return True


# Example usage
if __name__ == "__main__":
    # Create a knowledge base
    kb = HyperCodeKnowledgeBase()

    # Add a document
    doc = ResearchDocument(
        title="Introduction to HyperCode",
        content="HyperCode is a powerful programming language and environment...",
        source="internal",
        document_type="manual",
        metadata={"author": "HyperCode Team", "version": "1.0.0"},
    )
    doc_id = kb.add_document(doc)
    print(f"Added document with ID: {doc_id}")

    # Search for documents
    results = kb.search("HyperCode")
    print(f"Found {len(results)} matching documents:")
    for result in results:
        print(f"- {result['document'].title} (Score: {result['score']})")
        print(f"  {result['highlights']['content_preview']}\n")
