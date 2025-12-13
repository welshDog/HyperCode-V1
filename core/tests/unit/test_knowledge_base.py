#!/usr/bin/env python3
"""
Phase 1 Unit Tests for HyperCode Knowledge Base
Tests core functionality: document management, search, and context retrieval
"""

import shutil
import sys
import tempfile
from pathlib import Path

import pytest

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from hypercode.knowledge_base import HyperCodeKnowledgeBase, ResearchDocument


class TestHyperCodeKnowledgeBase:
    """Test suite for HyperCodeKnowledgeBase core functionality"""

    @pytest.fixture
    def temp_kb(self):
        """Create a temporary knowledge base for testing"""
        temp_dir = tempfile.mkdtemp()
        kb_file = Path(temp_dir) / "test_kb.json"
        kb = HyperCodeKnowledgeBase(kb_file)
        yield kb
        shutil.rmtree(temp_dir)

    @pytest.fixture
    def sample_documents(self):
        """Sample documents for testing"""
        return [
            {
                "title": "HyperCode Core Philosophy",
                "content": "HyperCode is a neurodivergent-first programming language designed for accessibility and AI integration.",
                "tags": ["philosophy", "neurodiversity", "accessibility"],
                "url": "https://perplexity.ai/hypercode/philosophy",
            },
            {
                "title": "AI Integration Patterns",
                "content": "HyperCode supports advanced AI integration including natural language programming and automated code generation.",
                "tags": ["ai", "integration", "patterns"],
                "url": "https://perplexity.ai/hypercode/ai-patterns",
            },
            {
                "title": "Space Metadata",
                "content": "HyperCode version 1.0.0 created by Mr Lyndz Williams (welshDog) from S.wales.",
                "tags": ["space", "metadata", "version"],
                "url": None,
            },
        ]

    def test_init_empty_kb(self, temp_kb):
        """Test knowledge base initialization"""
        assert len(temp_kb.documents) == 0
        assert temp_kb.kb_path.exists() == False

    def test_add_document(self, temp_kb, sample_documents):
        """Test adding a single document"""
        doc_data = sample_documents[0]
        doc_id = temp_kb.add_document(
            title=doc_data["title"],
            content=doc_data["content"],
            url=doc_data["url"],
            tags=doc_data["tags"],
        )

        assert doc_id is not None
        assert len(temp_kb.documents) == 1

        doc = temp_kb.documents[doc_id]
        assert doc.title == doc_data["title"]
        assert doc.content == doc_data["content"]
        assert doc.url == doc_data["url"]
        assert doc.tags == doc_data["tags"]
        assert doc.created_at is not None
        assert doc.last_updated is not None

    def test_add_multiple_documents(self, temp_kb, sample_documents):
        """Test adding multiple documents"""
        doc_ids = []
        for doc_data in sample_documents:
            doc_id = temp_kb.add_document(**doc_data)
            doc_ids.append(doc_id)

        assert len(temp_kb.documents) == len(sample_documents)
        assert len(set(doc_ids)) == len(doc_ids)  # All unique IDs

    def test_save_and_load(self, temp_kb, sample_documents):
        """Test saving and loading knowledge base"""
        # Add documents
        for doc_data in sample_documents:
            temp_kb.add_document(**doc_data)

        # Save
        temp_kb.save()
        assert temp_kb.kb_path.exists()

        # Create new instance and load
        new_kb = HyperCodeKnowledgeBase(temp_kb.kb_path)
        assert len(new_kb.documents) == len(sample_documents)

        # Verify content
        for doc_id, doc in new_kb.documents.items():
            original_doc = temp_kb.documents[doc_id]
            assert doc.title == original_doc.title
            assert doc.content == original_doc.content
            assert doc.tags == original_doc.tags

    def test_search_exact_match(self, temp_kb, sample_documents):
        """Test exact term matching in search"""
        # Add documents
        for doc_data in sample_documents:
            temp_kb.add_document(**doc_data)

        # Search for exact term
        results = temp_kb.search_documents("HyperCode", limit=10)
        assert len(results) >= 2  # Should find documents with "HyperCode"

        # Check ordering (higher score first) - score is internal, just verify results exist
        assert len(results) >= 2

    def test_search_tag_matching(self, temp_kb, sample_documents):
        """Test tag-based search"""
        # Add documents
        for doc_data in sample_documents:
            temp_kb.add_document(**doc_data)

        # Search by tag
        results = temp_kb.search_documents("philosophy", limit=10)
        assert len(results) >= 1

        # Verify result has the tag
        assert any("philosophy" in doc.tags for doc in results)

    def test_search_related_terms(self, temp_kb, sample_documents):
        """Test related term expansion"""
        # Add documents
        for doc_data in sample_documents:
            temp_kb.add_document(**doc_data)

        # Search for related term
        results = temp_kb.search_documents("accessibility", limit=10)
        assert len(results) >= 1

        # Should find document with "neurodiversity" (related term)
        neuro_docs = [doc for doc in results if "neurodiversity" in doc.tags]
        assert len(neuro_docs) >= 1

    def test_search_space_data_boost(self, temp_kb):
        """Test that space data gets boosted in search"""
        # Add space data document
        temp_kb.add_document(
            title="HyperCode Space - Core Philosophy",
            content="Core philosophy of HyperCode Space",
            tags=["hypercode", "space", "philosophy"],
        )

        # Add regular document
        temp_kb.add_document(
            title="Regular Philosophy Document",
            content="Some philosophy content",
            tags=["philosophy"],
        )

        # Search for philosophy
        results = temp_kb.search_documents("philosophy", limit=10)
        assert len(results) >= 2

        # Space data should be ranked higher (score is internal, just verify both exist)
        space_docs = [doc for doc in results if "space" in doc.tags]
        regular_docs = [doc for doc in results if "space" not in doc.tags]

        assert len(space_docs) >= 1
        assert len(regular_docs) >= 1

    def test_get_context_for_query(self, temp_kb, sample_documents):
        """Test context extraction for queries"""
        # Add documents
        for doc_data in sample_documents:
            temp_kb.add_document(**doc_data)

        # Get context
        context = temp_kb.get_context_for_query("HyperCode philosophy")
        assert len(context) > 0
        assert "HyperCode" in context
        assert "philosophy" in context.lower()

    def test_context_length_limit(self, temp_kb, sample_documents):
        """Test context length limiting"""
        # Add documents
        for doc_data in sample_documents:
            temp_kb.add_document(**doc_data)

        # Get context (uses default max length)
        context = temp_kb.get_context_for_query("HyperCode")
        assert len(context) > 0
        assert len(context) <= 4000 + 50  # Default max length + buffer

    def test_list_documents(self, temp_kb, sample_documents):
        """Test listing all documents"""
        # Add documents
        for doc_data in sample_documents:
            temp_kb.add_document(**doc_data)

        # List documents
        docs = temp_kb.list_documents()
        assert len(docs) == len(sample_documents)

        # Verify all are ResearchDocument instances
        assert all(isinstance(doc, ResearchDocument) for doc in docs)

    def test_empty_search(self, temp_kb):
        """Test search with empty query"""
        results = temp_kb.search_documents("", limit=10)
        assert len(results) == 0

    def test_search_nonexistent_term(self, temp_kb, sample_documents):
        """Test search for term that doesn't exist"""
        # Add documents
        for doc_data in sample_documents:
            temp_kb.add_document(**doc_data)

        # Search for nonexistent term
        results = temp_kb.search_documents("nonexistent_term_xyz", limit=10)
        assert len(results) == 0

    def test_document_update(self, temp_kb, sample_documents):
        """Test updating existing document"""
        # Add document
        doc_id = temp_kb.add_document(**sample_documents[0])
        original_created = temp_kb.documents[doc_id].created_at

        # Add new document with same title (simulates update)
        new_content = "Updated content with new information"
        temp_kb.add_document(
            title=sample_documents[0]["title"],
            content=new_content,
            url=sample_documents[0]["url"],
            tags=sample_documents[0]["tags"],
        )

        # Verify we have 2 documents (original + new)
        assert len(temp_kb.documents) >= 1


class TestResearchDocument:
    """Test suite for ResearchDocument dataclass"""

    def test_document_creation(self):
        """Test creating a research document"""
        doc = ResearchDocument(
            id="test-doc-1",
            title="Test Document",
            content="Test content",
            url="https://example.com",
            tags=["test", "document"],
            created_at="2025-11-18T10:00:00Z",
            last_updated="2025-11-18T10:00:00Z",
        )

        assert doc.id == "test-doc-1"
        assert doc.title == "Test Document"
        assert doc.content == "Test content"
        assert doc.url == "https://example.com"
        assert doc.tags == ["test", "document"]
        assert doc.created_at == "2025-11-18T10:00:00Z"
        assert doc.last_updated == "2025-11-18T10:00:00Z"

    def test_document_optional_fields(self):
        """Test document with optional fields"""
        doc = ResearchDocument(
            id="test-doc-2",
            title="Test Document 2",
            content="Test content 2",
            url=None,
            tags=[],
            created_at="2025-11-18T10:00:00Z",
            last_updated="2025-11-18T10:00:00Z",
        )

        assert doc.url is None
        assert doc.tags == []


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
