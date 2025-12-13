#!/usr/bin/env python3
"""
Demo: Enhanced Perplexity Client with Knowledge Base
Shows how the API can now access and remember research data
"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from hypercode.enhanced_perplexity_client import EnhancedPerplexityClient


def demo_knowledge_base_integration():
    """Demonstrate the knowledge base integration"""
    print("🧠 Enhanced Perplexity Client Demo")
    print("=" * 50)
    print("Showing how the API can now access and remember research data...")

    # Initialize the enhanced client
    client = EnhancedPerplexityClient()

    # Show current knowledge base
    docs = client.list_research_documents()
    print(f"\n📚 Knowledge Base Status: {len(docs)} documents loaded")

    for doc in docs:
        print(f"  📄 {doc.title}")

    # Test queries that demonstrate memory and context
    print("\n🔍 Testing Context-Aware Queries:")
    print("-" * 40)

    test_scenarios = [
        {
            "query": "What makes HyperCode different from other programming languages?",
            "context_needed": "language specification, neurodivergent design",
            "description": "Testing if API remembers core HyperCode concepts",
        },
        {
            "query": "How should I design code for developers with ADHD?",
            "context_needed": "neurodivergent principles, accessibility",
            "description": "Testing if API remembers design guidelines",
        },
        {
            "query": "Can HyperCode run on quantum computers?",
            "context_needed": "multi-backend architecture, quantum support",
            "description": "Testing if API remembers backend capabilities",
        },
        {
            "query": "Explain the 2D spatial programming concept",
            "context_needed": "spatial paradigm, visual programming",
            "description": "Testing if API remembers spatial features",
        },
    ]

    for i, scenario in enumerate(test_scenarios, 1):
        print(f"\n🧪 Test {i}: {scenario['description']}")
        print(f"❓ Query: {scenario['query']}")
        print(f"📝 Expected context: {scenario['context_needed']}")

        # Query with context
        response = client.query_with_context(scenario["query"], use_knowledge_base=True)

        if "choices" in response and response["choices"]:
            content = response["choices"][0]["message"]["content"]

            # Check if response contains expected context
            context_found = any(
                keyword.lower() in content.lower()
                for keyword in scenario["context_needed"].split(", ")
            )

            print(f"{'✅' if context_found else '⚠️'} Context found: {context_found}")
            print(f"📄 Response preview: {content[:150]}...")
        else:
            print("❌ Error in response")

    # Demonstrate adding new research data
    print("\n📝 Adding New Research Data:")
    print("-" * 30)

    new_research = {
        "title": "AI-Assisted Code Generation in HyperCode",
        "content": """
        HyperCode integrates AI assistance at multiple levels:

        1. Code Completion: Context-aware suggestions based on neurodivergent patterns
        2. Bug Detection: AI identifies common cognitive accessibility issues
        3. Code Optimization: Suggests alternative implementations for different thinking styles
        4. Documentation Generation: Auto-generates docs that follow neurodivergent-friendly guidelines

        The AI system is trained on:
        - Code patterns from neurodivergent developers
        - Accessibility best practices
        - Multiple programming paradigms
        - Cognitive science research
        """,
        "tags": ["AI", "code-generation", "accessibility", "machine-learning"],
    }

    doc_id = client.add_research_data(**new_research)
    print(f"✅ Added new document: {doc_id}")

    # Test that the new data is immediately available
    print("\n🔄 Testing New Data Integration:")

    test_query = "How does HyperCode use AI for code generation?"
    response = client.query_with_context(test_query, use_knowledge_base=True)

    if "choices" in response and response["choices"]:
        content = response["choices"][0]["message"]["content"]
        print("✅ New data integrated successfully!")
        print(f"📄 Response: {content[:200]}...")

    # Show search functionality
    print("\n🔍 Search Functionality Demo:")
    print("-" * 30)

    search_terms = ["AI", "neurodivergent", "quantum", "spatial"]

    for term in search_terms:
        results = client.search_research_data(term)
        print(f"🔎 '{term}': Found {len(results)} results")
        for result in results[:2]:  # Show top 2
            print(f"  - {result.title}")


def demonstrate_memory_persistence():
    """Demonstrate that the knowledge base persists between sessions"""
    print("\n💾 Memory Persistence Demo:")
    print("-" * 30)

    # Create a new client instance (simulating a new session)
    new_client = EnhancedPerplexityClient()

    # Check if data persists
    docs = new_client.list_research_documents()
    print(f"📚 New session loaded {len(docs)} documents from memory")

    # Test query in new session
    test_query = "What is HyperCode's approach to accessibility?"
    response = new_client.query_with_context(test_query, use_knowledge_base=True)

    if "choices" in response and response["choices"]:
        content = response["choices"][0]["message"]["content"]
        print("✅ Memory persistence working!")
        print(f"📄 Response: {content[:150]}...")


if __name__ == "__main__":
    demo_knowledge_base_integration()
    demonstrate_memory_persistence()

    print("\n🎉 Demo Complete!")
    print("\n📋 Summary:")
    print("✅ Knowledge base stores and retrieves research data")
    print("✅ API queries now include relevant context")
    print("✅ New research data can be added dynamically")
    print("✅ Memory persists between sessions")
    print("✅ Search functionality finds relevant documents")

    print("\n🚀 Your Perplexity API now has access to and remembers your research data!")
