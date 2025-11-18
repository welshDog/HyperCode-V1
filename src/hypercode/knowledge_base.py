#!/usr/bin/env python3
"""
HyperCode Knowledge Base - Perplexity Space Integration
Manages research data from Perplexity Space for API context
"""

import hashlib
import json
import uuid
import hashlib
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Any
from dataclasses import dataclass, asdict, field
from collections import defaultdict
import re
import unicodedata

@dataclass
class ResearchDocument:
    """Represents a research document from Perplexity Space"""

    id: str
    title: str
    content: str
    url: Optional[str] = None
    tags: List[str] = None
    created_at: str = None
    last_updated: str = None

    def __post_init__(self):
        if self.tags is None:
            self.tags = []
        if self.created_at is None:
            self.created_at = datetime.now().isoformat()
        if self.last_updated is None:
            self.last_updated = datetime.now().isoformat()

    def generate_id(self) -> str:
        """Generate unique ID from content hash"""
        content_hash = hashlib.md5(self.content.encode()).hexdigest()[:8]
        return f"doc_{content_hash}"
    
    def validate(self) -> bool:
        """Validate document data"""
        if not self.title or len(self.title.strip()) == 0:
            raise ValueError("Document title cannot be empty")
        if not self.content or len(self.content.strip()) == 0:
            raise ValueError("Document content cannot be empty")
        if len(self.title) > 1000:
            raise ValueError("Title too long (max 1000 characters)")
        if len(self.content) > 1000000:
            raise ValueError("Content too long (max 1MB)")
        return True
    
    def update_timestamp(self):
        """Update the last_updated timestamp"""
        self.last_updated = datetime.now().isoformat()
        if hasattr(self, 'version'):
            self.version += 1


# Related terms dictionary for search expansion
RELATED_TERMS = {
    "pillar": ["pillars", "column", "foundation", "core"],
    "pillars": ["pillar", "column", "foundation", "core"],
    "audit": ["auditing", "checklist", "review", "assessment"],
    "auditing": ["audit", "checklist", "review", "assessment"],
    "phase": ["phases", "stage", "step", "milestone"],
    "phases": ["phase", "stage", "step", "milestone"],
    "neurodiversity": ["neurodivergent", "adhd", "autism", "dyslexia"],
    "neurodivergent": ["neurodiversity", "adhd", "autism", "dyslexia"],
    "implementation": ["implement", "deploy", "execute", "build"],
    "implement": ["implementation", "deploy", "execute", "build"],
    "metadata": ["space", "author", "creator", "project"],
    "space": ["metadata", "author", "creator", "project"],
    "philosophy": ["principles", "ideas", "concepts", "beliefs"],
    "principles": ["philosophy", "ideas", "concepts", "beliefs"],
    "future": ["quantum", "dna", "ai", "technologies"],
    "quantum": ["future", "dna", "ai", "technologies"],
    "dna": ["future", "quantum", "ai", "technologies"],
    "ai": ["future", "quantum", "dna", "technologies"],
    "technologies": ["future", "quantum", "dna", "ai"],
    "message": ["core", "mission", "vision", "statement"],
    "core": ["message", "mission", "vision", "statement"],
    "technical": ["features", "specifications", "architecture"],
    "features": ["technical", "specifications", "architecture"],
    "research": ["methodology", "paper", "living", "study"],
    "methodology": ["research", "paper", "living", "study"],
    "community": ["collaboration", "open source", "contribution"],
    "collaboration": ["community", "open source", "contribution"],
    "roadmap": ["phases", "timeline", "milestones", "implementation"],
    "timeline": ["roadmap", "phases", "milestones", "implementation"],
    "impact": ["vision", "societal", "innovation", "long-term"],
    "vision": ["impact", "societal", "innovation", "long-term"],
    "resources": ["references", "historical", "languages", "brainfuck"],
    "references": ["resources", "historical", "languages", "brainfuck"],
    "action": ["call", "join", "contribute", "movement"],
    "call": ["action", "join", "contribute", "movement"],
}


class HyperCodeKnowledgeBase:
    """Knowledge base for HyperCode research data"""

    def __init__(self, kb_path: str = "data/hypercode_knowledge_base.json"):
        self.kb_path = Path(kb_path)
        self.kb_path.parent.mkdir(exist_ok=True)
        self.documents: Dict[str, ResearchDocument] = {}
        self.load()

    def load(self):
        """Load knowledge base from file"""
        if self.kb_path.exists():
            try:
                with open(self.kb_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    for doc_id, doc_data in data.items():
                        self.documents[doc_id] = ResearchDocument(**doc_data)
                print(f"✅ Loaded {len(self.documents)} documents from knowledge base")
            except Exception as e:
                print(f"⚠️ Error loading knowledge base: {e}")
                self.documents = {}
        else:
            print("📝 Creating new knowledge base")
            self.documents = {}

    def save(self):
        """Save knowledge base to file"""
        try:
            data = {doc_id: asdict(doc) for doc_id, doc in self.documents.items()}
            with open(self.kb_path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            print(f"💾 Saved {len(self.documents)} documents to knowledge base")
        except Exception as e:
            print(f"❌ Error saving knowledge base: {e}")

    def add_document(
        self,
        title: str,
        content: str,
        url: Optional[str] = None,
        tags: List[str] = None,
    ) -> str:
        """Add a new research document"""
        doc = ResearchDocument(
            id="",  # Will be generated
            title=title,
            content=content,
            url=url,
            tags=tags or [],
        )
        doc.id = doc.generate_id()

        # Check if document already exists
        if doc.id in self.documents:
            print(f"🔄 Updating existing document: {doc.title}")
            self.documents[doc.id].last_updated = datetime.now().isoformat()
        else:
            print(f"📄 Adding new document: {doc.title}")

        self.documents[doc.id] = doc
        self.save()
        return doc.id

    def search_documents(self, query: str, limit: int = 5) -> List[ResearchDocument]:
        """Search documents by query"""
        query_lower = query.lower().strip()

        # Handle empty queries
        if not query_lower:
            return []

        results = []

        for doc in self.documents.values():
            score = 0

            # Title matches (highest weight)
            if query_lower in doc.title.lower():
                score += 10

            # Content matches (count occurrences)
            content_lower = doc.content.lower()
            content_words = content_lower.split()
            query_words = query_lower.split()
            for word in query_words:
                count = content_lower.count(word)
                if count > 0:
                    score += count

            # Tag matches
            if doc.tags:
                tags_lower = " ".join(doc.tags).lower()
                if query_lower in tags_lower:
                    score += 5

            # Partial word matching for better coverage
            query_words = query_lower.split()
            for word in query_words:
                if len(word) > 3:  # Only match longer words
                    if word in content_lower:
                        score += 1
                    if word in doc.title.lower():
                        score += 3

            # Related term matching (only if query is exact match to a key)
            if query_lower in RELATED_TERMS:
                for related in RELATED_TERMS[query_lower]:
                    if related in content_lower:
                        score += 2
                    if related in doc.title.lower():
                        score += 4

            # Boost space data for general queries (but not for specific terms)
            if (
                "space-data" in doc.tags
                and len(query_words) == 1
                and query_words[0] in ["hypercode", "what", "tell", "explain", "about"]
            ):
                score += 3

            if score > 0:
                results.append((doc, score))

        # Sort by score and return top results
        results.sort(key=lambda x: x[1], reverse=True)
        return [doc for doc, score in results[:limit]]

    def get_context_for_query(self, query: str, max_context_length: int = 4000) -> str:
        """Get relevant context for a query"""
        relevant_docs = self.search_documents(query, limit=3)

        if not relevant_docs:
            return "No relevant research data found."

        context_parts = ["Relevant HyperCode Research Data:\n"]

        for doc in relevant_docs:
            context_parts.append(f"## {doc.title}")

            # Truncate content if too long
            content = doc.content
            if len(content) > 1000:
                content = content[:1000] + "..."

            context_parts.append(content)
            if doc.url:
                context_parts.append(f"Source: {doc.url}")
            context_parts.append("")  # Empty line

        # Join and truncate if necessary
        full_context = "\n".join(context_parts)

        if len(full_context) > max_context_length:
            full_context = full_context[:max_context_length] + "..."

        return full_context

    def list_documents(self) -> List[ResearchDocument]:
        """List all documents"""
        return list(self.documents.values())

    def get_document(self, doc_id: str) -> Optional[ResearchDocument]:
        """Get a specific document by ID"""
        return self.documents.get(doc_id)

    def delete_document(self, doc_id: str) -> bool:
        """Delete a document"""
        if doc_id in self.documents:
            del self.documents[doc_id]
            self.save()
            return True
        return False
    
    def update_document(self, doc_id: str, **kwargs) -> bool:
        """Update an existing document"""
        if doc_id not in self.documents:
            return False
        
        doc = self.documents[doc_id]
        for key, value in kwargs.items():
            if hasattr(doc, key):
                setattr(doc, key, value)
        
        doc.update_timestamp()
        self.save()
        return True
    
    def search_by_tags(self, tags: List[str], operator: str = "AND") -> List[ResearchDocument]:
        """Search documents by tags with AND/OR operators"""
        results = []
        
        for doc in self.documents.values():
            doc_tags = set(doc.tags)
            search_tags = set(tags)
            
            if operator == "AND":
                if search_tags.issubset(doc_tags):
                    results.append(doc)
            elif operator == "OR":
                if doc_tags.intersection(search_tags):
                    results.append(doc)
        
        return results
    
    def get_document_statistics(self) -> Dict[str, Any]:
        """Get statistics about the knowledge base"""
        total_docs = len(self.documents)
        tag_counts = defaultdict(int)
        total_content_length = 0
        
        for doc in self.documents.values():
            for tag in doc.tags:
                tag_counts[tag] += 1
            total_content_length += len(doc.content)
        
        return {
            "total_documents": total_docs,
            "total_content_length": total_content_length,
            "average_content_length": total_content_length / max(total_docs, 1),
            "unique_tags": len(tag_counts),
            "tag_distribution": dict(tag_counts),
            "oldest_document": min((doc.created_at for doc in self.documents.values()), default=None),
            "newest_document": max((doc.created_at for doc in self.documents.values()), default=None),
        }
    
    def export_format(self, format_type: str = "json") -> str:
        """Export knowledge base in different formats"""
        if format_type == "json":
            return json.dumps({doc_id: asdict(doc) for doc_id, doc in self.documents.items()}, indent=2)
        elif format_type == "markdown":
            lines = ["# HyperCode Knowledge Base Export\n"]
            for doc in self.documents.values():
                lines.append(f"## {doc.title}")
                lines.append(f"**Tags:** {', '.join(doc.tags)}")
                lines.append(f"**Created:** {doc.created_at}")
                if doc.url:
                    lines.append(f"**URL:** {doc.url}")
                lines.append("")
                lines.append(doc.content)
                lines.append("\n---\n")
            return "\n".join(lines)
        else:
            raise ValueError(f"Unsupported format: {format_type}")
    
    def validate_all_documents(self) -> List[str]:
        """Validate all documents and return list of errors"""
        errors = []
        for doc_id, doc in self.documents.items():
            try:
                doc.validate()
            except ValueError as e:
                errors.append(f"Document {doc_id} ({doc.title}): {str(e)}")
        return errors
    
    def cleanup_duplicates(self) -> int:
        """Remove duplicate documents based on content hash"""
        seen_hashes = set()
        duplicates = []
        
        for doc_id, doc in self.documents.items():
            content_hash = hashlib.md5(doc.content.encode()).hexdigest()
            if content_hash in seen_hashes:
                duplicates.append(doc_id)
            else:
                seen_hashes.add(content_hash)
        
        for doc_id in duplicates:
            del self.documents[doc_id]
        
        if duplicates:
            self.save()
        
        return len(duplicates)


def initialize_sample_data():
    """Initialize with sample HyperCode research data"""
    kb = HyperCodeKnowledgeBase()

    # Sample documents based on what would likely be in your Perplexity Space
    sample_docs = [
        {
            "title": "HyperCode Language Specification v0.1",
            "content": """
            HyperCode is a neurodivergent-first programming language that supports:
            - Multiple syntax modes (visual, text, spatial)
            - AI-assisted code generation and debugging
            - Multi-backend compilation (quantum, DNA, traditional)
            - Built-in accessibility features

            Core syntax elements include:
            - Declarative statements with visual markers
            - Pattern matching for cognitive flexibility
            - Spatial code execution (2D and 3D)
            - Natural language programming interfaces
            """,
            "tags": ["specification", "language", "syntax"],
        },
        {
            "title": "Neurodivergent-First Design Principles",
            "content": """
            Design principles for neurodivergent developers:

            1. Cognitive Flexibility:
            - Multiple ways to express the same concept
            - No single "right" way to write code
            - Support for different thinking patterns

            2. Sensory Accommodation:
            - Customizable visual themes
            - Adjustable information density
            - Optional sound/haptic feedback

            3. Executive Function Support:
            - Built-in reminders and planning tools
            - Automatic code organization
            - Progress tracking and milestones

            4. Communication Clarity:
            - Explicit, literal error messages
            - No ambiguous metaphors or idioms
            - Clear, structured documentation
            """,
            "tags": ["design", "accessibility", "neurodiversity"],
        },
        {
            "title": "Multi-Backend Architecture",
            "content": """
            HyperCode's compilation architecture supports:

            Traditional Backends:
            - x86/ARM assembly
            - WebAssembly
            - LLVM IR

            AI Backends:
            - GPT-4/ Claude integration
            - Local model execution
            - Hybrid AI-human compilation

            Exotic Backends:
            - Quantum computing circuits
            - DNA strand displacement
            - Neural network processors

            Backend Selection:
            - Automatic based on problem type
            - Manual override available
            - Multi-backend optimization
            """,
            "tags": ["architecture", "compilation", "backends"],
        },
        {
            "title": "Spatial Programming Paradigm",
            "content": """
            2D Spatial Code Execution:

            Benefits:
            - Visual representation of program flow
            - Intuitive for visual thinkers
            - Natural for diagram-based reasoning

            Implementation:
            - Code execution follows directional arrows
            - Supports wrapping (Befunge-style)
            - Multiple instruction streams

            Use Cases:
            - Data flow visualization
            - Algorithm animation
            - Educational visualization
            """,
            "tags": ["spatial", "2d", "visual"],
        },
    ]

    for doc_data in sample_docs:
        kb.add_document(**doc_data)

    print(f"✅ Initialized knowledge base with {len(sample_docs)} sample documents")
    return kb


if __name__ == "__main__":
    # Initialize sample data
    kb = initialize_sample_data()

    # Test search functionality
    print("\n🔍 Testing search functionality:")
    test_queries = ["neurodivergent", "compilation", "spatial", "AI"]

    for query in test_queries:
        results = kb.search_documents(query)
        print(f"\nQuery: '{query}' - Found {len(results)} results")
        for doc in results:
            print(f"  - {doc.title}")
