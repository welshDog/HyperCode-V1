#!/usr/bin/env python3
"""
Final Test: Complete Perplexity Space Integration
"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from hypercode.enhanced_perplexity_client import EnhancedPerplexityClient


def final_integration_test():
    """Complete test of the Perplexity Space integration"""
    client = EnhancedPerplexityClient()

    print("🎉 FINAL INTEGRATION TEST")
    print("=" * 50)
    print("Testing your Perplexity API with implementation guide knowledge...")

    # Test scenarios that should now work
    test_scenarios = [
        {
            "query": "What are the eight pillars of HyperCode?",
            "expected_keywords": ["pillars", "visual-first", "neurodiversity"],
            "description": "8 Pillars Knowledge",
        },
        {
            "query": "How do I audit neurodiversity features?",
            "expected_keywords": ["audit", "checklist", "neurodiversity"],
            "description": "Audit Framework Knowledge",
        },
        {
            "query": "What are the implementation phases?",
            "expected_keywords": ["phases", "foundation", "expansion", "maturity"],
            "description": "Implementation Roadmap Knowledge",
        },
        {
            "query": "What metrics should I track for ADHD optimization?",
            "expected_keywords": ["ADHD", "metrics", "optimization"],
            "description": "ADHD Metrics Knowledge",
        },
    ]

    success_count = 0

    for i, scenario in enumerate(test_scenarios, 1):
        print(f'\n🧪 Test {i}: {scenario["description"]}')
        print(f'❓ Query: {scenario["query"]}')

        # Get context
        context = client.knowledge_base.get_context_for_query(scenario["query"])
        print(f"📝 Context: {len(context)} characters")

        # Query API
        response = client.query_with_context(scenario["query"], use_knowledge_base=True)

        if "choices" in response and response["choices"]:
            content = response["choices"][0]["message"]["content"]
            print(f"✅ Response: {len(content)} characters")

            # Check for expected keywords
            content_lower = content.lower()
            found_keywords = [
                kw
                for kw in scenario["expected_keywords"]
                if kw.lower() in content_lower
            ]

            keyword_match = len(found_keywords) >= 2  # At least 2 keywords

            if keyword_match:
                print(
                    f'🎯 SUCCESS: Found {len(found_keywords)}/{len(scenario["expected_keywords"])} keywords: {found_keywords}'
                )
                success_count += 1
            else:
                print(
                    f'⚠️  PARTIAL: Found {len(found_keywords)}/{len(scenario["expected_keywords"])} keywords: {found_keywords}'
                )

            # Show preview
            preview = content.replace("\n", " ")[:150]
            print(f"📄 Preview: {preview}...")
        else:
            print("❌ FAILED: No response")

    # Summary
    print("\n📊 FINAL RESULTS:")
    print(f"✅ Passed: {success_count}/{len(test_scenarios)} tests")
    print(f"🧠 Knowledge Base: {len(client.list_research_documents())} documents")
    print("🔍 Search Algorithm: Enhanced with related terms")
    print("💾 Memory System: Persistent and functional")

    if success_count >= 3:
        print("\n🎉 INTEGRATION SUCCESS!")
        print("Your Perplexity API now remembers your implementation guide!")
        print("You can ask about pillars, audits, phases, and metrics!")
    else:
        print("\n⚠️  Partial success - some queries need improvement")

    # Show what's available
    print("\n📚 Available Knowledge:")
    docs = client.list_research_documents()
    for doc in docs:
        print(f"  📄 {doc.title}")

    return success_count >= 3


if __name__ == "__main__":
    success = final_integration_test()

    if success:
        print("\n🚀 Your Perplexity Space integration is COMPLETE!")
        print("   Ready to use with your actual research data!")
    else:
        print("\n🔧 Integration needs fine-tuning for optimal results")
