#!/usr/bin/env python3
"""
Comprehensive Test Suite for HyperCode Knowledge Base
Covers all scenarios: unit, integration, and performance tests
"""

import sys
import tempfile
import time
from pathlib import Path

import pytest

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from hypercode.knowledge_base import HyperCodeKnowledgeBase, ResearchDocument


class TestKnowledgeBaseUnit:
    """Unit tests for Knowledge Base functionality"""

    @pytest.fixture
    def temp_kb(self):
        """Create a temporary knowledge base for testing"""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            temp_path = f.name

        kb = HyperCodeKnowledgeBase(temp_path)
        yield kb

        # Cleanup
        Path(temp_path).unlink(missing_ok=True)

    @pytest.fixture
    def sample_docs(self):
        """Sample documents for testing"""
        return [
            {
                "title": "HyperCode Language Specification",
                "content": "HyperCode is a neurodivergent-first programming language with multiple syntax modes",
                "url": "https://hypercode.dev/spec",
                "tags": ["specification", "language", "neurodivergent"],
            },
            {
                "title": "AI Integration Architecture",
                "content": "The AI integration uses GPT-4 and Claude for code generation and debugging",
                "url": "https://hypercode.dev/ai",
                "tags": ["ai", "architecture", "integration"],
            },
            {
                "title": "Spatial Programming Paradigm",
                "content": "2D spatial code execution for visual thinkers with wrapping support",
                "url": "https://hypercode.dev/spatial",
                "tags": ["spatial", "2d", "visual", "paradigm"],
            },
        ]

    def test_init_empty_kb(self, temp_kb):
        """Test knowledge base initialization"""
        assert len(temp_kb.documents) == 0
        # File is created during initialization to ensure directory exists
        assert temp_kb.kb_path.exists() == True

    def test_add_single_document(self, temp_kb, sample_docs):
        """Test adding a single document"""
        doc = sample_docs[0]
        doc_id = temp_kb.add_document(**doc)

        assert doc_id in temp_kb.documents
        assert len(temp_kb.documents) == 1
        assert temp_kb.documents[doc_id].title == doc["title"]

    def test_add_multiple_documents(self, temp_kb, sample_docs):
        """Test adding multiple documents"""
        doc_ids = []
        for doc in sample_docs:
            doc_id = temp_kb.add_document(**doc)
            doc_ids.append(doc_id)

        assert len(temp_kb.documents) == len(sample_docs)
        assert all(doc_id in temp_kb.documents for doc_id in doc_ids)

    def test_save_and_load(self, temp_kb, sample_docs):
        """Test saving and loading knowledge base"""
        # Add documents
        for doc in sample_docs:
            temp_kb.add_document(**doc)

        # Save
        temp_kb.save()
        assert temp_kb.kb_path.exists()

        # Create new instance and load
        kb2 = HyperCodeKnowledgeBase(temp_kb.kb_path)
        assert len(kb2.documents) == len(sample_docs)

        # Verify content
        for doc_id, doc in kb2.documents.items():
            assert doc.title in [d["title"] for d in sample_docs]

    def test_search_exact_match(self, temp_kb, sample_docs):
        """Test exact search matching"""
        # Add documents
        for doc in sample_docs:
            temp_kb.add_document(**doc)

        # Search for exact title
        results = temp_kb.search_documents("HyperCode Language Specification")
        assert len(results) == 1
        assert results[0].title == "HyperCode Language Specification"

    def test_search_partial_match(self, temp_kb, sample_docs):
        """Test partial search matching"""
        # Add documents
        for doc in sample_docs:
            temp_kb.add_document(**doc)

        # Search for partial term
        results = temp_kb.search_documents("neurodivergent")
        assert len(results) == 1
        assert "neurodivergent" in results[0].content.lower()

    def test_search_tag_matching(self, temp_kb, sample_docs):
        """Test tag-based search"""
        # Add documents
        for doc in sample_docs:
            temp_kb.add_document(**doc)

        # Search by tag
        results = temp_kb.search_documents("ai")
        assert len(results) == 1
        assert "ai" in results[0].tags

    def test_search_case_insensitive(self, temp_kb, sample_docs):
        """Test case insensitive search"""
        # Add documents
        for doc in sample_docs:
            temp_kb.add_document(**doc)

        # Test different cases
        queries = ["hypercode", "HYPERCODE", "HyperCode"]
        for query in queries:
            results = temp_kb.search_documents(query)
            assert len(results) >= 1

    def test_empty_search(self, temp_kb):
        """Test empty search query"""
        results = temp_kb.search_documents("")
        assert len(results) == 0

        results = temp_kb.search_documents("   ")
        assert len(results) == 0

    def test_nonexistent_search(self, temp_kb, sample_docs):
        """Test search for nonexistent terms"""
        # Add documents
        for doc in sample_docs:
            temp_kb.add_document(**doc)

        # Search for nonexistent term
        results = temp_kb.search_documents("nonexistent_term_xyz123")
        assert len(results) == 0

    def test_get_context_for_query(self, temp_kb, sample_docs):
        """Test context extraction"""
        # Add documents
        for doc in sample_docs:
            temp_kb.add_document(**doc)

        # Get context
        context = temp_kb.get_context_for_query("HyperCode")
        assert "HyperCode" in context
        assert "Relevant HyperCode Research Data:" in context

    def test_context_length_limit(self, temp_kb, sample_docs):
        """Test context length limiting"""
        # Add documents with long content
        long_content = "This is a very long content. " * 1000
        temp_kb.add_document("Long Document", long_content, tags=["test"])

        # Get context with limit
        context = temp_kb.get_context_for_query("long", max_context_length=100)
        assert len(context) <= 103  # Allow for "..."

    def test_document_update(self, temp_kb, sample_docs):
        """Test updating existing documents"""
        # Add document
        doc_id = temp_kb.add_document(**sample_docs[0])
        original_time = temp_kb.documents[doc_id].last_updated

        # Wait a bit to ensure timestamp difference
        time.sleep(0.1)

        # Add same document (should update)
        temp_kb.add_document(**sample_docs[0])

        # Check update
        assert len(temp_kb.documents) == 1
        assert temp_kb.documents[doc_id].last_updated != original_time

    def test_list_documents(self, temp_kb, sample_docs):
        """Test listing all documents"""
        # Add documents
        for doc in sample_docs:
            temp_kb.add_document(**doc)

        # List documents
        docs = temp_kb.list_documents()
        assert len(docs) == len(sample_docs)
        assert all(isinstance(doc, ResearchDocument) for doc in docs)

    def test_delete_document(self, temp_kb, sample_docs):
        """Test document deletion"""
        # Add document
        doc_id = temp_kb.add_document(**sample_docs[0])
        assert doc_id in temp_kb.documents

        # Delete document
        result = temp_kb.delete_document(doc_id)
        assert result == True
        assert doc_id not in temp_kb.documents

        # Try to delete again
        result = temp_kb.delete_document(doc_id)
        assert result == False


class TestKnowledgeBaseIntegration:
    """Integration tests for Knowledge Base"""

    @pytest.fixture
    def populated_kb(self):
        """Create a populated knowledge base for integration testing"""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            temp_path = f.name

        kb = HyperCodeKnowledgeBase(temp_path)

        # Add comprehensive test data
        test_docs = [
            {
                "title": "HyperCode Core Philosophy",
                "content": "HyperCode is designed as a neurodivergent-first programming language that supports multiple syntax modes including visual, text, and spatial programming. The core philosophy emphasizes cognitive flexibility, sensory accommodation, executive function support, and communication clarity.",
                "tags": ["philosophy", "neurodivergent", "accessibility"],
            },
            {
                "title": "AI Integration Architecture",
                "content": "The AI integration layer supports GPT-4, Claude, and local models. It provides context-aware code generation, automated debugging, and natural language programming interfaces. The architecture is designed to be modular and extensible.",
                "tags": ["ai", "architecture", "integration", "gpt-4", "claude"],
            },
            {
                "title": "Spatial Programming Implementation",
                "content": "Spatial programming in HyperCode supports 2D and 3D code execution with wrapping similar to Befunge. It's particularly beneficial for visual thinkers and provides intuitive data flow visualization. Multiple instruction streams are supported.",
                "tags": ["spatial", "2d", "3d", "visual", "befunge"],
            },
            {
                "title": "Multi-Backend Compilation",
                "content": "HyperCode supports multiple compilation targets including traditional (x86, ARM, WebAssembly), AI-based (neural networks), and exotic (quantum computing, DNA strand displacement). Backend selection is automatic but manually overrideable.",
                "tags": ["compilation", "backend", "quantum", "dna", "webassembly"],
            },
            {
                "title": "Community and Open Source",
                "content": "HyperCode is developed as an open source project with community contributions. The project follows neurodivergent-friendly practices and provides multiple ways to contribute including code, documentation, testing, and community support.",
                "tags": ["community", "open-source", "contribution", "collaboration"],
            },
        ]

        for doc in test_docs:
            kb.add_document(**doc)

        yield kb

        # Cleanup
        Path(temp_path).unlink(missing_ok=True)

    def test_complex_search_queries(self, populated_kb):
        """Test complex search scenarios"""
        # Multi-word query
        results = populated_kb.search_documents("neurodivergent programming language")
        assert len(results) >= 1

        # Query with special characters
        results = populated_kb.search_documents("AI-based")
        assert len(results) >= 1

        # Query that should match multiple documents
        results = populated_kb.search_documents("HyperCode")
        assert len(results) >= 3

    def test_search_ranking_quality(self, populated_kb):
        """Test that search results are properly ranked"""
        # Search for term that appears in title vs content
        results = populated_kb.search_documents("spatial")

        # Title match should rank higher
        if len(results) > 1:
            title_match = any("spatial" in r.title.lower() for r in results[:2])
            assert title_match, "Title matches should rank higher"

    def test_related_term_expansion(self, populated_kb):
        """Test that related terms are properly expanded"""
        # Search for term with related terms
        results = populated_kb.search_documents("quantum")

        # Should find documents with related terms
        assert len(results) >= 1

        # Check if related terms are working
        results = populated_kb.search_documents("future")
        assert len(results) >= 1

    def test_performance_with_large_dataset(self, populated_kb):
        """Test performance with larger dataset"""
        # Add many documents
        for i in range(100):
            populated_kb.add_document(
                f"Test Document {i}",
                f"This is test content for document {i} with various keywords",
                tags=["test", f"category-{i % 10}"],
            )

        # Time search performance
        start_time = time.time()
        results = populated_kb.search_documents("test")
        end_time = time.time()

        # Should complete quickly
        assert end_time - start_time < 1.0
        assert len(results) > 0

    def test_concurrent_access_simulation(self, populated_kb):
        """Test simulated concurrent access"""
        # Simulate multiple operations
        operations = []

        # Add documents
        for i in range(10):
            operations.append(("add", f"Concurrent Doc {i}", f"Content {i}"))

        # Search operations
        for i in range(5):
            operations.append(("search", "test"))

        # Execute operations
        for op in operations:
            if op[0] == "add":
                populated_kb.add_document(op[1], op[2])
            elif op[0] == "search":
                populated_kb.search_documents(op[1])

        # Verify integrity
        assert len(populated_kb.documents) > 0


class TestKnowledgeBasePerformance:
    """Performance tests for Knowledge Base"""

    @pytest.fixture
    def large_kb(self):
        """Create a large knowledge base for performance testing"""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            temp_path = f.name

        kb = HyperCodeKnowledgeBase(temp_path)

        # Add many documents
        categories = ["ai", "spatial", "compilation", "community", "philosophy"]
        for i in range(1000):
            category = categories[i % len(categories)]
            kb.add_document(
                f"Document {i}",
                f"This is content for document {i} in category {category}. " * 10,
                tags=[category, f"tag-{i % 20}", f"type-{i % 5}"],
            )

        yield kb

        # Cleanup
        Path(temp_path).unlink(missing_ok=True)

    def test_search_performance_large_dataset(self, large_kb):
        """Test search performance with large dataset"""
        # Test various search queries
        queries = ["document", "category", "ai", "spatial", "compilation"]

        for query in queries:
            start_time = time.time()
            results = large_kb.search_documents(query, limit=10)
            end_time = time.time()

            # Should complete quickly even with 1000 documents
            assert end_time - start_time < 0.5
            assert len(results) <= 10

    def test_save_performance_large_dataset(self, large_kb):
        """Test save performance with large dataset"""
        start_time = time.time()
        large_kb.save()
        end_time = time.time()

        # Should save quickly
        assert end_time - start_time < 2.0

        # Verify file size is reasonable
        file_size = large_kb.kb_path.stat().st_size
        assert file_size > 0  # Should have content

    def test_load_performance_large_dataset(self, large_kb):
        """Test load performance with large dataset"""
        # Save first
        large_kb.save()

        # Test loading
        start_time = time.time()
        kb2 = HyperCodeKnowledgeBase(large_kb.kb_path)
        end_time = time.time()

        # Should load quickly
        assert end_time - start_time < 1.0
        assert len(kb2.documents) == 1000

    def test_memory_usage_large_dataset(self, large_kb):
        """Test memory usage with large dataset"""
        import os

        import psutil

        # Get current process
        process = psutil.Process(os.getpid())

        # Measure memory before and after operations
        mem_before = process.memory_info().rss

        # Perform operations
        for _ in range(10):
            large_kb.search_documents("test")

        mem_after = process.memory_info().rss

        # Memory growth should be reasonable
        mem_growth = (mem_after - mem_before) / 1024 / 1024  # MB
        assert mem_growth < 100  # Should not grow more than 100MB


class TestKnowledgeBaseEdgeCases:
    """Edge case tests for Knowledge Base"""

    @pytest.fixture
    def edge_case_kb(self):
        """Create knowledge base for edge case testing"""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            temp_path = f.name

        kb = HyperCodeKnowledgeBase(temp_path)

        # Add edge case documents
        edge_docs = [
            {
                "title": "",  # Empty title
                "content": "Document with empty title",
                "tags": ["edge-case"],
            },
            {
                "title": "Document with special chars !@#$%^&*()",
                "content": "Content with unicode: ñáéíóú 🚀 🧠",
                "tags": ["special-chars", "unicode"],
            },
            {
                "title": "Very " * 100 + "Long Title",  # Very long title
                "content": "Normal content",
                "tags": ["long-title"],
            },
            {
                "title": "Normal Document",
                "content": "",  # Empty content
                "tags": ["empty-content"],
            },
            {
                "title": "Document with no tags",
                "content": "Content without tags",
                "tags": None,
            },
        ]

        for doc in edge_docs:
            kb.add_document(**doc)

        yield kb

        # Cleanup
        Path(temp_path).unlink(missing_ok=True)

    def test_empty_title_handling(self, edge_case_kb):
        """Test handling of documents with empty titles"""
        results = edge_case_kb.search_documents("empty title")
        assert len(results) >= 1

    def test_special_characters_handling(self, edge_case_kb):
        """Test handling of special characters and unicode"""
        results = edge_case_kb.search_documents("ñáéíóú")
        assert len(results) >= 1

        results = edge_case_kb.search_documents("!@#$%^&*()")
        assert len(results) >= 1

    def test_very_long_titles(self, edge_case_kb):
        """Test handling of very long titles"""
        results = edge_case_kb.search_documents("Long Title")
        assert len(results) >= 1

    def test_empty_content_handling(self, edge_case_kb):
        """Test handling of documents with empty content"""
        results = edge_case_kb.search_documents("Normal Document")
        assert len(results) >= 1

    def test_none_tags_handling(self, edge_case_kb):
        """Test handling of None tags"""
        # Explicitly add a document with None tags
        doc_id = edge_case_kb.add_document(
            title="Document with None tags",
            content="This document has None tags",
            tags=None,
        )

        doc_with_no_tags = edge_case_kb.get_document(doc_id)
        assert doc_with_no_tags is not None
        # Tags should be converted to empty list
        assert doc_with_no_tags.tags == []

    def test_malformed_json_handling(self):
        """Test handling of malformed JSON files"""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            f.write("{ invalid json")
            temp_path = f.name

        # Should handle gracefully
        kb = HyperCodeKnowledgeBase(temp_path)
        assert len(kb.documents) == 0

        # Cleanup
        Path(temp_path).unlink(missing_ok=True)

    def test_file_permission_handling(self):
        """Test handling of file permission issues"""
        # This is more difficult to test on Windows, but we can simulate
        # by trying to use a directory instead of a file
        with tempfile.TemporaryDirectory() as temp_dir:
            kb_path = Path(temp_dir) / "test.json"

            # Create as directory (should cause issues)
            kb_path.mkdir()

            # Should handle gracefully
            kb = HyperCodeKnowledgeBase(str(kb_path))
            # Should still work but might not be able to save


if __name__ == "__main__":
    # Run tests
    pytest.main([__file__, "-v", "--tb=short"])
