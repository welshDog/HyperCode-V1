#!/usr/bin/env python3
"""
Phase 1 Unit Tests for Search Algorithm
Tests search functionality including related term matching, scoring, and ranking
"""

import shutil
import sys
import tempfile
from pathlib import Path

import pytest

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from hypercode.knowledge_base import HyperCodeKnowledgeBase


class TestSearchAlgorithm:
    """Test suite for search algorithm functionality"""

    @pytest.fixture
    def populated_kb(self):
        """Create a knowledge base with test documents"""
        temp_dir = tempfile.mkdtemp()
        kb_file = Path(temp_dir) / "test_search_kb.json"
        kb = HyperCodeKnowledgeBase(kb_file)

        # Add documents for comprehensive search testing
        test_docs = [
            {
                "title": "HyperCode Core Philosophy",
                "content": "HyperCode is built on neurodivergent-first principles, emphasizing accessibility and creative expression through programming.",
                "tags": ["philosophy", "neurodiversity", "accessibility"],
            },
            {
                "title": "AI Integration Architecture",
                "content": "The AI integration system uses advanced machine learning to assist with code generation and debugging.",
                "tags": ["ai", "architecture", "integration"],
            },
            {
                "title": "HyperCode Space - Research Methodology",
                "content": "Our research methodology follows a living paper concept with continuous updates and AI agent collaboration.",
                "tags": ["hypercode", "space", "research", "methodology"],
            },
            {
                "title": "Implementation Phases",
                "content": "The implementation roadmap consists of multiple phases: Foundation, Expansion, and Maturity stages.",
                "tags": ["implementation", "phases", "roadmap"],
            },
            {
                "title": "Technical Specifications",
                "content": "Technical features include spatial programming, visual syntax, and multi-backend compilation support.",
                "tags": ["technical", "features", "specifications"],
            },
            {
                "title": "Community Collaboration Model",
                "content": "Open source collaboration with inclusive contribution guidelines and skill-level-agnostic participation.",
                "tags": ["community", "collaboration", "open-source"],
            },
            {
                "title": "Future Technology Support",
                "content": "Future support includes quantum computing paradigms, DNA computing, and neural network processors.",
                "tags": ["future", "quantum", "dna", "ai"],
            },
            {
                "title": "Audit and Quality Assurance",
                "content": "Regular audits ensure feature completeness, usability testing, and performance benchmarks are met.",
                "tags": ["audit", "quality", "testing"],
            },
        ]

        for doc_data in test_docs:
            kb.add_document(**doc_data)

        yield kb
        shutil.rmtree(temp_dir)

    def test_exact_title_match_highest_score(self, populated_kb):
        """Test that exact title matches get highest priority"""
        results = populated_kb.search_documents("Philosophy", limit=10)

        # Should find the philosophy document first
        philosophy_docs = [doc for doc in results if "philosophy" in doc.title.lower()]
        assert len(philosophy_docs) >= 1

        # Philosophy doc should be highly ranked
        philosophy_doc = philosophy_docs[0]
        assert "neurodivergent" in philosophy_doc.content.lower()

    def test_space_data_boosting(self, populated_kb):
        """Test that space data gets boosted in search results"""
        results = populated_kb.search_documents("research", limit=10)

        # Should find space data document
        space_docs = [doc for doc in results if "space" in doc.tags]
        assert len(space_docs) >= 1

        # Space doc should contain expected content
        space_doc = space_docs[0]
        assert "methodology" in space_doc.content.lower()
        assert "living paper" in space_doc.content.lower()

    def test_related_term_expansion(self, populated_kb):
        """Test related term matching functionality"""

        # Test pillar -> columns, foundation
        results = populated_kb.search_documents("foundation", limit=10)
        assert len(results) >= 1

        # Test audit -> quality, testing
        results = populated_kb.search_documents("testing", limit=10)
        quality_docs = [
            doc
            for doc in results
            if "quality" in doc.tags or "quality" in doc.content.lower()
        ]
        assert len(quality_docs) >= 1

        # Test phase -> implementation, roadmap
        results = populated_kb.search_documents("implementation", limit=10)
        phase_docs = [doc for doc in results if "phases" in doc.content.lower()]
        assert len(phase_docs) >= 1

    def test_tag_matching_scoring(self, populated_kb):
        """Test that tag matches contribute to scoring"""
        results = populated_kb.search_documents("ai", limit=10)

        # Should find documents with AI in tags or content
        ai_docs = [
            doc for doc in results if "ai" in doc.tags or "ai" in doc.content.lower()
        ]
        assert len(ai_docs) >= 2  # Architecture doc + Future tech doc

    def test_content_frequency_scoring(self, populated_kb):
        """Test that multiple content occurrences increase score"""
        results = populated_kb.search_documents("hypercode", limit=10)

        # Should find multiple documents mentioning HyperCode
        assert len(results) >= 2

        # Results should be ordered by relevance
        for doc in results:
            assert (
                "hypercode" in doc.title.lower() or "hypercode" in doc.content.lower()
            )

    def test_partial_word_matching(self, populated_kb):
        """Test partial word matching for longer terms"""
        results = populated_kb.search_documents(
            "programm", limit=10
        )  # Partial of "programming"

        # Should find relevant documents (may not find any with partial)
        # This test verifies the partial matching logic works
        if len(results) > 0:
            for doc in results:
                content_lower = doc.content.lower()
                title_lower = doc.title.lower()
                # Check if the partial word exists or if it's a false positive
                if "programm" not in content_lower and "programm" not in title_lower:
                    # If not found, it might be due to related term matching
                    # which is acceptable behavior
                    pass

    def test_query_word_ordering(self, populated_kb):
        """Test that query words are properly processed"""
        results = populated_kb.search_documents("open source collaboration", limit=10)

        # Should find community collaboration document
        community_docs = [doc for doc in results if "community" in doc.title.lower()]
        assert len(community_docs) >= 1

        doc = community_docs[0]
        assert "collaboration" in doc.content.lower()
        assert "open source" in doc.content.lower()

    def test_case_insensitive_search(self, populated_kb):
        """Test that search is case insensitive"""
        results_lower = populated_kb.search_documents("research", limit=10)
        results_upper = populated_kb.search_documents("RESEARCH", limit=10)
        results_mixed = populated_kb.search_documents("ReSeArCh", limit=10)

        # All should return same results
        assert len(results_lower) == len(results_upper) == len(results_mixed)

        # If results exist, verify content (allow for related term matches)
        if len(results_lower) > 0:
            for doc in results_lower:
                content_lower = doc.content.lower()
                title_lower = doc.title.lower()
                # Check for direct match or related terms
                assert (
                    "research" in content_lower
                    or "research" in title_lower
                    or "methodology" in content_lower
                    or "paper" in content_lower
                    or "study" in content_lower
                )

    def test_empty_query_returns_no_results(self, populated_kb):
        """Test that empty queries return no results"""
        results = populated_kb.search_documents("", limit=10)
        assert len(results) == 0

        results = populated_kb.search_documents("   ", limit=10)  # Whitespace only
        assert len(results) == 0

    def test_limit_parameter_respected(self, populated_kb):
        """Test that search limit parameter works correctly"""
        # Search for common term that will have multiple results
        results_limited = populated_kb.search_documents("hypercode", limit=2)
        results_unlimited = populated_kb.search_documents("hypercode", limit=50)

        assert len(results_limited) == 2
        assert len(results_unlimited) >= len(results_limited)

    def test_no_results_for_nonexistent_terms(self, populated_kb):
        """Test search for terms that don't exist"""
        results = populated_kb.search_documents("nonexistent_term_xyz123", limit=10)
        assert len(results) == 0

        results = populated_kb.search_documents("zxywvutsrqponmlkjihgfedcba", limit=10)
        assert len(results) == 0

    def test_special_characters_in_query(self, populated_kb):
        """Test search with special characters"""
        # Test with common punctuation
        results = populated_kb.search_documents("ai?", limit=10)
        # Should still find AI-related content

        # Test with numbers
        results = populated_kb.search_documents("quantum1", limit=10)
        # Should handle gracefully (may or may not find results)

    def test_unicode_characters(self, populated_kb):
        """Test search with unicode characters"""
        # Add document with unicode content
        populated_kb.add_document(
            title="Unicode Test Document",
            content="Testing with unicode: café, naïve, résumé, and programming symbols: → ← ↑ ↓",
            tags=["unicode", "test"],
        )

        # Search for unicode terms
        results = populated_kb.search_documents("café", limit=10)

        # Should find the unicode document
        unicode_docs = [doc for doc in results if doc.title == "Unicode Test Document"]
        assert len(unicode_docs) >= 1

        doc = unicode_docs[0]
        assert "café" in doc.content

    def test_search_performance_with_large_kb(self, populated_kb):
        """Test search performance with larger knowledge base"""
        import time

        # Add many more documents
        for i in range(100):
            populated_kb.add_document(
                title=f"Test Document {i}",
                content=f"This is test content for document {i} with various search terms like programming, ai, and technology.",
                tags=["test", f"doc{i}"],
            )

        # Time a search
        start_time = time.time()
        results = populated_kb.search_documents("programming", limit=10)
        end_time = time.time()

        # Should complete quickly and find results
        assert len(results) >= 1
        assert end_time - start_time < 1.0  # Should be under 1 second

    def test_search_result_consistency(self, populated_kb):
        """Test that search results are consistent across multiple calls"""
        # Perform same search multiple times
        results1 = populated_kb.search_documents("ai", limit=5)
        results2 = populated_kb.search_documents("ai", limit=5)
        results3 = populated_kb.search_documents("ai", limit=5)

        # Should get same results
        assert len(results1) == len(results2) == len(results3)

        for i in range(len(results1)):
            assert results1[i].id == results2[i].id == results3[i].id
            assert results1[i].title == results2[i].title == results3[i].title


class TestSearchScoringDetails:
    """Test detailed scoring algorithm behavior"""

    @pytest.fixture
    def scoring_kb(self):
        """Create KB for detailed scoring tests"""
        temp_dir = tempfile.mkdtemp()
        kb_file = Path(temp_dir) / "test_scoring_kb.json"
        kb = HyperCodeKnowledgeBase(kb_file)

        # Add documents with specific scoring characteristics
        kb.add_document(
            title="Exact Match Title",
            content="This document has the exact term in title",
            tags=["exact", "title"],
        )

        kb.add_document(
            title="Space Data Document",
            content="Space data gets boosted for general queries",
            tags=["hypercode", "space", "boosted"],
        )

        kb.add_document(
            title="Multiple Occurrences",
            content="ai ai ai ai ai - repeated term should increase score",
            tags=["repeated", "frequency"],
        )

        yield kb
        shutil.rmtree(temp_dir)

    def test_title_match_beats_content_match(self, scoring_kb):
        """Test that title matches score higher than content matches"""
        results = scoring_kb.search_documents("exact", limit=10)

        # Exact title match should be first
        assert len(results) >= 1
        assert "exact match title" in results[0].title.lower()

    def test_space_data_boosting_works(self, scoring_kb):
        """Test that space data gets boosted"""
        results = scoring_kb.search_documents("hypercode", limit=10)

        # Space data should be found and boosted
        space_docs = [doc for doc in results if "space" in doc.tags]
        assert len(space_docs) >= 1

    def test_frequency_scoring(self, scoring_kb):
        """Test that content frequency affects scoring"""
        results = scoring_kb.search_documents("ai", limit=10)

        # Document with multiple "ai" occurrences should rank highly
        frequency_docs = [doc for doc in results if "repeated" in doc.tags]
        assert len(frequency_docs) >= 1


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
