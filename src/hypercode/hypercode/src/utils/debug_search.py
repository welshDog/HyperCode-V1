#!/usr/bin/env python3
"""
Debug search results
"""

import sys
from pathlib import Path

# The following path manipulation is necessary to run this script directly
# and allow it to find the 'hypercode' module.
# We add a noqa comment to suppress the E402 flake8 warning.
sys.path.insert(0, str(Path(__file__).parent.parent))  # noqa: E402

from hypercode.enhanced_perplexity_client import EnhancedPerplexityClient


def debug_search():
    """Debug why space data isn't being found"""
    client = EnhancedPerplexityClient()

    print("🔍 DEBUGGING SEARCH RESULTS")
    print("=" * 40)

    # Test a specific query
    query = "What is HyperCode and who created it?"
    print(f"Query: {query}")

    # Get search results
    results = client.knowledge_base.search_documents(query, limit=10)

    print(f"\n📊 Search Results ({len(results)} found):")
    for i, doc in enumerate(results, 1):
        print(f"\n{i}. {doc.title}")
        print(f"   Tags: {doc.tags}")
        print(f"   Content preview: {doc.content[:100]}...")

    # Check space data specifically
    print("\n🚀 SPACE DATA DOCUMENTS:")
    space_docs = [
        doc
        for doc in client.knowledge_base.list_documents()
        if "space-data" in doc.tags
    ]
    for doc in space_docs:
        print(f"\n📄 {doc.title}")
        print(f"   Tags: {doc.tags}")
        print(f"   Content preview: {doc.content[:100]}...")

    # Test context extraction
    context = client.knowledge_base.get_context_for_query(query)
    print(f"\n📝 Extracted Context ({len(context)} chars):")
    print(context[:500] + "..." if len(context) > 500 else context)


if __name__ == "__main__":
    debug_search()
