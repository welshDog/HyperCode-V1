# HyperCode Knowledge Base Documentation

## Overview

The HyperCode Knowledge Base is a smart document search and retrieval system designed to enhance AI responses with project-specific context. It integrates seamlessly with the Perplexity API to provide more accurate, context-aware responses.

## Architecture

```
┌─────────────────┐
│   User Query    │
└────────┬────────┘
         │
         v
┌─────────────────────────────────┐
│  EnhancedPerplexityClient       │
│  ┌───────────────────────────┐  │
│  │ 1. Search Knowledge Base  │  │
│  └───────────┬───────────────┘  │
│              │                   │
│              v                   │
│  ┌───────────────────────────┐  │
│  │ 2. Rank & Select Context  │  │
│  └───────────┬───────────────┘  │
│              │                   │
│              v                   │
│  ┌───────────────────────────┐  │
│  │ 3. Enhance Query          │  │
│  └───────────┬───────────────┘  │
└──────────────┼───────────────────┘
               │
               v
     ┌─────────────────┐
     │ Perplexity API  │
     └────────┬────────┘
              │
              v
    ┌──────────────────┐
    │ Enhanced Response│
    └──────────────────┘
```

## Core Components

### KnowledgeBase Class

```python
from hypercode.knowledge_base import KnowledgeBase

# Initialize knowledge base
kb = KnowledgeBase()

# Add documents
kb.add_document({
    "id": "hypercode_intro",
    "title": "HyperCode Introduction",
    "content": "HyperCode is a neurodivergent-first programming language...",
    "tags": ["introduction", "overview", "neurodivergent"]
})

# Search documents
results = kb.search("neurodivergent programming")
```

### Document Structure

Each document should follow this structure:

```python
{
    "id": "unique_identifier",          # Required: Unique document ID
    "title": "Document Title",          # Required: Human-readable title
    "content": "Document content...",   # Required: Full text content
    "tags": ["tag1", "tag2"],          # Optional: Searchable tags
    "metadata": {                       # Optional: Additional metadata
        "author": "Name",
        "created_at": "2025-11-18",
        "category": "documentation"
    }
}
```

## API Reference

### KnowledgeBase

#### `__init__()`
Initialize a new knowledge base instance.

```python
kb = KnowledgeBase()
```

#### `add_document(document: Dict[str, Any]) -> None`
Add a new document to the knowledge base.

**Parameters:**
- `document`: Dictionary containing document data (see Document Structure)

**Example:**
```python
kb.add_document({
    "id": "doc1",
    "title": "Getting Started",
    "content": "Quick start guide for HyperCode..."
})
```

#### `search(query: str, limit: int = 10) -> List[Dict[str, Any]]`
Search for relevant documents.

**Parameters:**
- `query`: Search query string
- `limit`: Maximum number of results (default: 10)

**Returns:**
- List of matching documents, ranked by relevance

**Example:**
```python
results = kb.search("AI integration", limit=5)
for result in results:
    print(f"{result['title']}: {result['score']:.2f}")
```

#### `update_document(doc_id: str, updates: Dict[str, Any]) -> None`
Update an existing document.

**Parameters:**
- `doc_id`: Document ID to update
- `updates`: Dictionary of fields to update

**Example:**
```python
kb.update_document("doc1", {
    "content": "Updated content...",
    "tags": ["updated", "v2"]
})
```

#### `remove_document(doc_id: str) -> None`
Remove a document from the knowledge base.

**Parameters:**
- `doc_id`: Document ID to remove

**Example:**
```python
kb.remove_document("doc1")
```

## Integration with Perplexity

### EnhancedPerplexityClient

The `EnhancedPerplexityClient` automatically enhances queries with knowledge base context.

```python
from hypercode.enhanced_perplexity_client import EnhancedPerplexityClient
from hypercode.knowledge_base import KnowledgeBase

# Initialize
kb = KnowledgeBase()
client = EnhancedPerplexityClient(
    api_key="your_api_key",
    knowledge_base=kb
)

# Query with automatic context enhancement
response = client.query(
    "How does HyperCode support neurodivergent developers?"
)

print(response['content'])
```

### How Context Enhancement Works

1. **Query Analysis**: The client analyzes the user query
2. **Context Retrieval**: Searches knowledge base for relevant documents
3. **Context Ranking**: Ranks documents by relevance score
4. **Query Enhancement**: Adds top context to query
5. **API Call**: Sends enhanced query to Perplexity API
6. **Response**: Returns context-aware response

## Usage Examples

### Example 1: Basic Search

```python
from hypercode.knowledge_base import KnowledgeBase

kb = KnowledgeBase()

# Add HyperCode documentation
kb.add_document({
    "id": "features",
    "title": "HyperCode Features",
    "content": """HyperCode offers:
    - Neurodivergent-first design
    - Visual programming support
    - Universal AI integration
    - Accessible syntax
    """,
    "tags": ["features", "overview"]
})

# Search
results = kb.search("accessibility features")
for doc in results:
    print(f"Found: {doc['title']}")
```

### Example 2: Multi-Document Search

```python
# Add multiple documents
docs = [
    {
        "id": "intro",
        "title": "Introduction",
        "content": "HyperCode basics..."
    },
    {
        "id": "ai_guide",
        "title": "AI Integration Guide",
        "content": "How to integrate AI..."
    },
    {
        "id": "accessibility",
        "title": "Accessibility Features",
        "content": "Built for neurodivergent developers..."
    }
]

for doc in docs:
    kb.add_document(doc)

# Search returns ranked results
results = kb.search("neurodivergent AI programming")
```

### Example 3: Context-Enhanced Queries

```python
from hypercode.enhanced_perplexity_client import EnhancedPerplexityClient

client = EnhancedPerplexityClient(
    api_key=os.getenv("PERPLEXITY_API_KEY"),
    knowledge_base=kb
)

# Query automatically uses knowledge base context
response = client.query(
    "What makes HyperCode different from other languages?"
)

# Response includes both local context and Perplexity insights
print(response['content'])
print(f"Context used: {response['context_count']} documents")
```

## Performance Guidelines

### Optimization Tips

1. **Document Size**: Keep documents focused and concise
   - Ideal: 100-500 words per document
   - Maximum: 2000 words

2. **Search Performance**:
   - Expected: <100ms for 1000 documents
   - Target: <1s for 10,000 documents

3. **Indexing**: Use meaningful tags for faster filtering

4. **Caching**: Frequently accessed documents are cached

### Benchmarking

Run performance benchmarks:

```bash
# Test with 100 documents
python tests/benchmark_knowledge_base.py --size 100

# Test with 1000 documents
python tests/benchmark_knowledge_base.py --size 1000

# Generate report
python tests/benchmark_knowledge_base.py --size 1000 --report performance.md
```

## Testing

### Running Tests

```bash
# Run all knowledge base tests
pytest tests/test_knowledge_base.py -v

# Run with coverage
pytest tests/test_knowledge_base.py --cov=hypercode --cov-report=html

# Run specific test class
pytest tests/test_knowledge_base.py::TestKnowledgeBaseSearch -v
```

### Test Coverage

Target coverage: **>80%**

Covered areas:
- Basic search functionality
- Edge cases (empty queries, special characters)
- Performance (speed, memory)
- Integration with Perplexity
- Document management (add, update, remove)

## Best Practices

### Document Organization

1. **Use Hierarchical IDs**: `category.subcategory.document`
   ```python
   "id": "docs.quickstart.installation"
   ```

2. **Tag Strategically**: Use 3-5 relevant tags per document
   ```python
   "tags": ["quickstart", "installation", "beginner"]
   ```

3. **Update Metadata**: Include creation/update timestamps
   ```python
   "metadata": {
       "created_at": "2025-11-18",
       "updated_at": "2025-11-18",
       "version": "1.0"
   }
   ```

### Query Design

1. **Be Specific**: "neurodivergent ADHD features" > "features"
2. **Use Natural Language**: Write questions as you would ask them
3. **Include Context**: "HyperCode accessibility for dyslexia"

### Integration Patterns

1. **Fallback Strategy**: Always provide fallback to direct API
   ```python
   context = kb.search(query)
   if not context:
       # Fallback to direct Perplexity query
       return perplexity_client.query(query)
   ```

2. **Context Limits**: Don't overwhelm the API with too much context
   ```python
   # Use top 3-5 most relevant documents
   top_context = results[:5]
   ```

## Troubleshooting

### Common Issues

**Issue**: Search returns no results
- **Solution**: Check if documents are properly indexed
- **Debug**: `print(kb.documents)` to see available documents

**Issue**: Slow search performance
- **Solution**: Reduce document count or implement caching
- **Debug**: Run benchmark to identify bottleneck

**Issue**: Context not being used in Perplexity queries
- **Solution**: Verify `EnhancedPerplexityClient` initialization
- **Debug**: Check `response['context_count']` in response

## Contributing

Want to improve the knowledge base? See [CONTRIBUTING.md](community/CONTRIBUTING.md) for guidelines.

### Areas for Contribution

- [ ] Implement advanced ranking algorithms (TF-IDF, BM25)
- [ ] Add fuzzy matching for typo tolerance
- [ ] Create vector embeddings for semantic search
- [ ] Add multi-language support
- [ ] Implement distributed knowledge base

## Related Documentation

- [Enhanced Perplexity Client](./enhanced-perplexity-client.md)
- [API Reference](./api-reference.md)
- [Testing Guide](./testing.md)

---

**Questions?** Open an issue or join our [Discussions](https://github.com/welshDog/hypercode/discussions)!

*Built with 🧠 for the neurodivergent community* 🚀
