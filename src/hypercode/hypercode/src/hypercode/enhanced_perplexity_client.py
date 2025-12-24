#!/usr/bin/env python3
"""
Enhanced Perplexity Client with Knowledge Base Integration
Provides context-aware queries using HyperCode research data
"""

import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

# Add parent directory for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from hypercode.knowledge_base import HyperCodeKnowledgeBase
from hypercode.perplexity_client import PerplexityClient


class EnhancedPerplexityClient:
    """Enhanced Perplexity client with knowledge base integration"""

    def __init__(self, kb_path: str = "data/hypercode_knowledge_base.json"):
        self.perplexity = PerplexityClient()
        self.knowledge_base = HyperCodeKnowledgeBase(kb_path)

    def query_with_context(
        self, prompt: str, use_knowledge_base: bool = True, model: str = "sonar-pro"
    ) -> Dict:
        """Send a query with relevant knowledge base context"""

        if use_knowledge_base:
            # Get relevant context from knowledge base
            context = self.knowledge_base.get_context_for_query(prompt)

            # Build enhanced prompt with context
            enhanced_prompt = f"""
            You are HyperCode AI, an expert assistant for the HyperCode programming language project.

            Use the following research data to inform your response:

            {context}

            User Query: {prompt}

            Please provide a comprehensive response that:
            1. Directly addresses the user's query
            2. Incorporates relevant information from the research data
            3. Provides practical insights for the HyperCode project
            4. Suggests next steps or implementation considerations where appropriate
            """
        else:
            enhanced_prompt = f"""
            You are HyperCode AI, an expert assistant for the HyperCode programming language project.

            User Query: {prompt}

            Please provide a comprehensive response for the HyperCode project.
            """

        return self.perplexity.query(enhanced_prompt, model)

    def add_research_data(
        self,
        title: str,
        content: str,
        url: Optional[str] = None,
        tags: List[str] = None,
    ) -> str:
        """Add research data to the knowledge base"""
        return self.knowledge_base.add_document(title, content, url, tags)

    def search_research_data(self, query: str, limit: int = 5) -> List[Any]:
        """Search the knowledge base"""
        return self.knowledge_base.search_documents(query, limit)

    def list_research_documents(self) -> List[Any]:
        """List all research documents"""
        return self.knowledge_base.list_documents()

    def get_document(self, doc_id: str) -> Optional[Any]:
        """Get a specific document"""
        return self.knowledge_base.get_document(doc_id)

    def delete_document(self, doc_id: str) -> bool:
        """Delete a document"""
        return self.knowledge_base.delete_document(doc_id)

    def import_from_perplexity_space(self, space_data: Dict) -> int:
        """Import data from Perplexity Space export"""
        """
        Expected format for space_data:
        {
            "documents": [
                {
                    "title": "Document Title",
                    "content": "Document content...",
                    "url": "optional_url",
                    "tags": ["tag1", "tag2"]
                },
                ...
            ]
        }
        """
        imported_count = 0

        if "documents" in space_data:
            for doc in space_data["documents"]:
                try:
                    self.add_research_data(
                        title=doc.get("title", "Untitled Document"),
                        content=doc.get("content", ""),
                        url=doc.get("url"),
                        tags=doc.get("tags", []),
                    )
                    imported_count += 1
                except Exception as e:
                    print(
                        f"❌ Error importing document '{doc.get('title', 'Unknown')}': {e}"
                    )

        print(f"✅ Imported {imported_count} documents from Perplexity Space")
        return imported_count

    def test_context_integration(self) -> bool:
        """Test the context integration"""
        print("🧪 Testing context integration...")

        test_queries = [
            "What are the key features of HyperCode?",
            "How does HyperCode support neurodivergent developers?",
            "What backends does HyperCode support?",
            "Explain the spatial programming paradigm",
        ]

        for i, query in enumerate(test_queries, 1):
            print(f"\n🔍 Test Query {i}: {query}")

            # Test with context
            response_with_context = self.query_with_context(
                query, use_knowledge_base=True
            )

            # Test without context
            response_without_context = self.query_with_context(
                query, use_knowledge_base=False
            )

            # Compare responses
            with_context_content = ""
            without_context_content = ""

            if "choices" in response_with_context and response_with_context["choices"]:
                with_context_content = response_with_context["choices"][0]["message"][
                    "content"
                ]
                print(f"✅ With context: {with_context_content[:100]}...")

            if (
                "choices" in response_without_context
                and response_without_context["choices"]
            ):
                without_context_content = response_without_context["choices"][0][
                    "message"
                ]["content"]
                print(f"📝 Without context: {without_context_content[:100]}...")

            # Check if context added value
            if len(with_context_content) > len(without_context_content):
                print("✅ Context enhanced the response")
            else:
                print("⚠️ Context may not have added significant value")

        return True


def create_perplexity_space_import_template():
    """Create a template for importing Perplexity Space data"""
    template = {
        "documents": [
            {
                "title": "Example: HyperCode Overview",
                "content": """
                HyperCode is a revolutionary programming language designed for neurodivergent developers.
                It features multiple syntax modes, AI integration, and advanced compilation backends.
                Key innovations include spatial programming, natural language interfaces, and
                built-in accessibility features.
                """,
                "url": "https://www.perplexity.ai/spaces/hypercode-8B7p3SNcRcWhtGCk5ZGzjQ",
                "tags": ["overview", "introduction", "concepts"],
            },
            {
                "title": "Example: Implementation Roadmap",
                "content": """
                Phase 1: Core language specification and basic compiler
                Phase 2: AI integration and neurodivergent features
                Phase 3: Multi-backend support (quantum, DNA)
                Phase 4: Spatial programming paradigm
                Phase 5: Natural language programming
                """,
                "url": None,
                "tags": ["roadmap", "implementation", "phases"],
            },
        ]
    }

    import json

    with open("perplexity_space_import_template.json", "w") as f:
        json.dump(template, f, indent=2)

    print("📄 Created perplexity_space_import_template.json")
    print("   Use this as a template for importing your Perplexity Space data")


if __name__ == "__main__":
    # Initialize the enhanced client
    client = EnhancedPerplexityClient()

    # Test the integration
    client.test_context_integration()

    # Create import template
    create_perplexity_space_import_template()

    print("\n🎉 Enhanced Perplexity Client is ready!")
    print("\n📋 Next steps:")
    print("   1. Export your Perplexity Space data")
    print("   2. Use client.import_from_perplexity_space() to import it")
    print("   3. Use client.query_with_context() for context-aware queries")
    print("   4. Add new research data with client.add_research_data()")
