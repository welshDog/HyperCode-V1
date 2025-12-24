#!/usr/bin/env python3
"""
Test Implementation Guide Integration
"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from hypercode.enhanced_perplexity_client import EnhancedPerplexityClient


def test_search_functionality():
    """Test search for implementation guide terms"""
    client = EnhancedPerplexityClient()

    print("🔍 Testing Search Functionality:")
    print("=" * 40)

    # Test search for implementation guide terms
    search_terms = ["pillars", "audit", "phases", "neurodiversity", "implementation"]

    for term in search_terms:
        results = client.search_research_data(term)
        print(f'🔎 "{term}": Found {len(results)} results')
        for result in results:
            print(f"  - {result.title}")
            # Check if it's the implementation guide
            if "Implementation" in result.title:
                content_snippet = result.content[:100].replace("\n", " ")
                print(f"    📄 Snippet: {content_snippet}...")
        print()


def test_implementation_guide_content():
    """Test the implementation guide document directly"""
    client = EnhancedPerplexityClient()

    print("📄 Testing Implementation Guide Content:")
    print("=" * 45)

    # Find the implementation guide
    docs = client.list_research_documents()
    impl_guide = None

    for doc in docs:
        if "Implementation" in doc.title:
            impl_guide = doc
            break

    if impl_guide:
        print(f"✅ Found: {impl_guide.title}")
        print(f"📏 Length: {len(impl_guide.content)} characters")
        print(f'🏷️ Tags: {", ".join(impl_guide.tags)}')

        # Check for key terms in the content
        key_terms = [
            "pillars",
            "audit",
            "phases",
            "neurodiversity",
            "ADHD",
            "implementation",
        ]
        content_lower = impl_guide.content.lower()

        print("\n🔍 Key Terms Found:")
        for term in key_terms:
            found = term in content_lower
            count = content_lower.count(term)
            print(f'  {"✅" if found else "❌"} {term}: {count} occurrences')

        # Show a snippet
        snippet = impl_guide.content[:200].replace("\n", " ")
        print(f"\n📄 Content Snippet: {snippet}...")
    else:
        print("❌ Implementation guide not found!")


def test_context_queries():
    """Test context-aware queries"""
    client = EnhancedPerplexityClient()

    print("\n🧪 Testing Context-Aware Queries:")
    print("=" * 40)

    test_queries = [
        "What are the eight pillars of HyperCode?",
        "How do I audit neurodiversity features?",
        "What are the implementation phases?",
    ]

    for query in test_queries:
        print(f"\n❓ Query: {query}")

        # Get context first
        context = client.knowledge_base.get_context_for_query(query)
        print(f"📝 Context length: {len(context)} characters")
        if context:
            print(f"📄 Context preview: {context[:100]}...")

        # Query with context
        response = client.query_with_context(query, use_knowledge_base=True)

        if "choices" in response and response["choices"]:
            content = response["choices"][0]["message"]["content"]
            print(f"✅ Response length: {len(content)} characters")
            print(f"📄 Response preview: {content[:150]}...")
        else:
            print("❌ Error in response")


if __name__ == "__main__":
    test_search_functionality()
    test_implementation_guide_content()
    test_context_queries()
