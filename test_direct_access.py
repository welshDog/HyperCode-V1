#!/usr/bin/env python3
"""
Direct Test of Implementation Guide Content
"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from hypercode.enhanced_perplexity_client import EnhancedPerplexityClient


def test_direct_implementation_access():
    """Test direct access to implementation guide content"""
    client = EnhancedPerplexityClient()

    print("🎯 Direct Implementation Guide Test:")
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

        # Test specific content extraction
        content = impl_guide.content

        # Look for the 8 pillars section
        if "eight pillars" in content.lower() or "8 pillars" in content.lower():
            print('✅ Found "8 pillars" in content')

            # Extract the pillars section
            lines = content.split("\n")
            in_pillars_section = False
            pillars_content = []

            for line in lines:
                if "pillars" in line.lower() and (
                    "eight" in line.lower() or "8" in line.lower()
                ):
                    in_pillars_section = True
                    pillars_content.append(line)
                elif in_pillars_section and line.startswith("###"):
                    # Next section starts
                    break
                elif in_pillars_section:
                    pillars_content.append(line)

            if pillars_content:
                print("\n📄 Pillars Section:")
                for line in pillars_content[:10]:  # Show first 10 lines
                    print(f"  {line}")
        else:
            print('❌ "8 pillars" not found in content')

        # Test search with different terms
        print("\n🔍 Testing Search Terms:")
        test_terms = ["pillar", "visual-first", "neurodiversity", "audit", "phases"]

        for term in test_terms:
            results = client.search_research_data(term)
            impl_results = [r for r in results if "Implementation" in r.title]
            print(f'  🔎 "{term}": {len(impl_results)} impl guide results')

        # Test context with broader terms
        print("\n🧪 Testing Context with Broader Terms:")
        broad_queries = [
            "HyperCode features",
            "implementation guide",
            "neurodiversity audit",
        ]

        for query in broad_queries:
            context = client.knowledge_base.get_context_for_query(query)
            print(f'  ❓ "{query}": {len(context)} chars context')
            if len(context) > 50:
                print(f"    📄 Preview: {context[:100]}...")

    else:
        print("❌ Implementation guide not found!")


if __name__ == "__main__":
    test_direct_implementation_access()
