# 🚀 HyperCode Perplexity Space Import Guide

## 📋 Template Overview

Your import template is a clean JSON structure designed to organize your Perplexity
Space research into a structured knowledge base. Here's the anatomy:

```json
{
  "documents": [
    {
      "title": "Your Research Title",
      "content": "Full text of your research or findings",
      "url": "Optional URL to the source or Perplexity Space link",
      "tags": ["category", "keyword", "topic"]
    }
  ]
}
```

### Required Fields

- **title**: Give each document a clear, descriptive name (20-50 characters ideal)
- **content**: The actual research text or findings from your Perplexity Space
- **tags**: Array of 2-5 tags for searchability (lowercase, hyphen-separated if
  multi-word)

### Optional Fields

- **url**: Link to the original Perplexity Space or source (use `null` if unavailable)

---

## 🎯 Step-by-Step Import Process

### Step 1: Gather Your Space Data

1. Navigate to your HyperCode Perplexity Space
2. Identify key documents, research notes, and findings
3. For each item, copy:
   - A descriptive title
   - The main content/findings
   - Relevant URL (if applicable)
   - 2-5 relevant tags

### Step 2: Edit the Template

Open `perplexity_space_import_template.json` in your text editor and replace the example
entries:

```json
{
  "documents": [
    {
      "title": "HyperCode Language Specification v1.0.0",
      "content": "Core syntax features including spatial blocks, natural language parsing, neurodivergent-friendly operators...",
      "url": "https://www.perplexity.ai/spaces/hypercode-...",
      "tags": ["specification", "core-language", "syntax"]
    },
    {
      "title": "Quantum Backend Integration Research",
      "content": "Findings on integrating quantum computing backends with HyperCode compilation pipeline...",
      "url": null,
      "tags": ["quantum", "backend", "implementation"]
    },
    {
      "title": "AI Model Compatibility Matrix",
      "content": "Analysis of GPT-4, Claude, Mistral, and custom model integration capabilities...",
      "url": "https://www.perplexity.ai/spaces/hypercode-...",
      "tags": ["ai-integration", "models", "compatibility"]
    }
  ]
}
```

### Step 3: Import Your Data

**Option A: Using the Collector Script**

```bash
python perplexity_space_collector.py
# Choose option 3: Import from JSON template
# Select your edited template file
# Confirm import
```

**Option B: Direct Python Import**

```python
from hypercode.perplexity_client import PerplexityClient

client = PerplexityClient()
client.import_from_json("perplexity_space_import_template.json")
print("✅ Import complete!")
```

---

## 🏷️ Smart Tagging Strategy

Tags are crucial for searchability. Use these categories:

| Category           | Examples                                                     | Use Case                      |
| ------------------ | ------------------------------------------------------------ | ----------------------------- |
| **Core**           | `core-language`, `specification`, `syntax`                   | Fundamental language features |
| **Features**       | `spatial-programming`, `neurodivergent`, `accessibility`     | Unique capabilities           |
| **Backends**       | `quantum`, `dna-computing`, `gpu`, `fpga`                    | Compilation targets           |
| **AI**             | `ai-integration`, `model-compatibility`, `llm-api`           | AI system integration         |
| **Implementation** | `roadmap`, `phases`, `timeline`, `architecture`              | Development stages            |
| **Research**       | `research`, `findings`, `analysis`, `proof-of-concept`       | Research content              |
| **Community**      | `community`, `contributions`, `open-source`, `collaboration` | Community aspects             |

**Pro Tip:** Use 2-3 tags minimum, 5 maximum. Be specific but not over-detailed.

---

## 💡 Content Best Practices

### Keep Content Focused

- One main idea per document
- Include key takeaways in the first sentence
- Reference related documents using tags

### Format for AI Readability

```
# Main Finding
Brief description of what this document covers

## Key Points
- Point 1: explanation
- Point 2: explanation

## Technical Details
Specific implementation notes, code snippets, or technical specs

## Related Areas
Links or references to connected topics
```

### Content Chunking Strategy

- **Short documents**: 200-500 words (quick reference)
- **Medium documents**: 500-2000 words (detailed findings)
- **Long documents**: Split into multiple smaller documents with linked tags

**Example:**

- Create: "Quantum Backend: Core Concepts" (overview)
- Create: "Quantum Backend: Compilation Pipeline" (technical detail)
- Tag both with `quantum`, `backend`

---

## 🔍 Querying Your Imported Data

Once imported, query your knowledge base:

```python
from hypercode.perplexity_client import PerplexityClient

client = PerplexityClient()

# Search by keyword
results = client.search_knowledge_base("neurodivergent features")

# Search by tag
results = client.search_knowledge_base(tag="ai-integration")

# Get AI response using your knowledge base
response = client.query(
    "Explain HyperCode's neurodivergent design principles",
    use_knowledge_base=True
)
print(response)
```

---

## ✅ Quality Checklist

Before importing, verify:

- [ ] All required fields are filled (title, content, tags)
- [ ] Content is well-formatted and readable
- [ ] Tags are lowercase and consistent
- [ ] URLs (if included) are valid and point to relevant sources
- [ ] JSON is valid (no syntax errors)
- [ ] No duplicate documents
- [ ] Content doesn't exceed reasonable length (split if needed)
- [ ] Each document has 2-5 tags

**Validate JSON:**

```bash
python -m json.tool perplexity_space_import_template.json > /dev/null && echo "✅ Valid JSON!"
```

---

## 🚨 Common Issues & Fixes

### Issue: "Invalid JSON" error

**Solution:** Ensure all quotes are straight quotes (`"` not `""`), no trailing commas
in arrays/objects.

### Issue: Tags not working in searches

**Solution:** Tags should be lowercase, hyphen-separated, no spaces or special
characters.

### Issue: Content not appearing in queries

**Solution:** Ensure the knowledge base file exists at
`data/hypercode_knowledge_base.json`. Re-import if necessary.

### Issue: Special characters breaking import

**Solution:** Escape special characters: use `\\n` for newlines, `\\t` for tabs, `\\"`
for quotes.

---

## 🔄 Updating Imported Data

To modify existing documents:

```python
from hypercode.perplexity_client import PerplexityClient

client = PerplexityClient()

# Update a document
client.update_document(
    document_id="doc_12345",
    title="Updated Title",
    content="Updated content",
    tags=["new", "tags"]
)

# Delete if needed
client.delete_document(document_id="doc_12345")
```

---

## 📊 Bulk Operations

Import multiple spaces or large datasets:

```python
import json

# Combine multiple templates
combined_docs = {"documents": []}

for space_file in ["space1.json", "space2.json", "space3.json"]:
    with open(space_file, "r") as f:
        data = json.load(f)
        combined_docs["documents"].extend(data["documents"])

# Save combined file
with open("all_spaces_combined.json", "w") as f:
    json.dump(combined_docs, f, indent=2)

# Import all at once
client.import_from_json("all_spaces_combined.json")
```

---

## 🎯 Next Steps

1. **Edit the template** with your actual HyperCode Space data
2. **Validate the JSON** using the validation command above
3. **Run the import** using your preferred method
4. **Test queries** to ensure data is accessible
5. **Iterate** - add more documents as your research grows

---

## 📚 Integration with Your Workflow

Your imported data integrates with:

- ✅ Enhanced Perplexity API client with memory
- ✅ Knowledge base search and retrieval
- ✅ AI-powered responses using your research
- ✅ Automatic backups and versioning
- ✅ CI/CD pipeline documentation

**Your research now powers your code. Build with confidence! 🚀**
