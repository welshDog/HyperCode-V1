# ✅ HyperCode Perplexity Space Import Quick-Start Checklist

## 🎯 Your Mission (3 Simple Steps)

### Step 1: Prepare Your Data

- [ ] Open your HyperCode Perplexity Space
- [ ] Identify 5-10 key research documents/findings
- [ ] Copy the title, content, and URL for each
- [ ] Note 2-5 relevant tags per document

### Step 2: Fill the Template

- [ ] Open `perplexity_space_import_template.json`
- [ ] Replace example documents with your actual data
- [ ] Use the example format in `hypercode-example-data.json` as a guide
- [ ] Ensure all tags are lowercase with hyphens (no spaces)
- [ ] Validate JSON syntax is correct

### Step 3: Import Your Data

- [ ] Run validation:
      `python import_helper.py validate perplexity_space_import_template.json`
- [ ] Fix any errors if validation fails
- [ ] Import: `python import_helper.py generate-script`
- [ ] Execute: `python import_space.py`
- [ ] Confirm: Check `data/hypercode_knowledge_base.json` exists

---

## 📚 Files You Now Have

| File                                    | Purpose                 | Action                             |
| --------------------------------------- | ----------------------- | ---------------------------------- |
| `perplexity_space_import_template.json` | Your data import file   | **EDIT THIS** with your Space data |
| `hypercode-example-data.json`           | Reference example       | **COPY FORMAT** from this          |
| `hypercode-import-guide.md`             | Full documentation      | Read for deep dive                 |
| `import-helper.py`                      | Validation & automation | Run to validate & import           |

---

## 🏷️ Quick Tag Reference

Pick from these categories (lowercase, hyphen-separated):

**Core Language**: `core-language`, `specification`, `syntax`, `grammar`

**Neurodivergent**: `neurodivergent`, `accessibility`, `adhd-friendly`,
`dyslexia-support`

**Features**: `spatial-programming`, `natural-language`, `multi-syntax`, `modes`

**Backends**: `quantum`, `dna-computing`, `gpu`, `quantum-compilation`

**AI Integration**: `ai-integration`, `gpt-compatible`, `claude-compatible`,
`mistral-support`

**Research**: `research`, `findings`, `analysis`, `proof-of-concept`

**History**: `forgotten-languages`, `plankalkul`, `brainfuck`, `befunge`

**Implementation**: `roadmap`, `architecture`, `phases`, `development`

**Community**: `open-source`, `community`, `contributions`, `collaboration`

---

## 📋 Document Template Example

```json
{
  "title": "Your Document Title Here",
  "content": "Full content from your Perplexity Space research. Can be multiple paragraphs. Should be substantive and meaningful.",
  "url": "https://www.perplexity.ai/spaces/hypercode-...",
  "tags": ["tag1", "tag2", "tag3"]
}
```

### Field Guidelines

| Field       | Min      | Max       | Type           | Example                                 |
| ----------- | -------- | --------- | -------------- | --------------------------------------- |
| **title**   | 3 chars  | 100 chars | String         | "HyperCode Quantum Backend Integration" |
| **content** | 10 chars | unlimited | String         | Full research text, paragraphs ok       |
| **url**     | -        | -         | String or null | "https://..." or null                   |
| **tags**    | 1        | 5         | Array          | ["ai-integration", "quantum"]           |

---

## ⚡ Speed Run (5 Minutes)

1. **Clone/Copy Template** (30 seconds)

   ```bash
   cp perplexity_space_import_template.json my-hypercode-space.json
   ```

2. **Edit with Your Data** (3 minutes)

   - Replace example documents
   - Use lowercase hyphen-separated tags
   - Keep URLs or set to null

3. **Validate** (1 minute)

   ```bash
   python import_helper.py validate my-hypercode-space.json
   ```

4. **Generate & Import** (30 seconds)

   ```bash
   python import_helper.py generate-script
   python import_space.py
   ```

5. **Verify Success** (30 seconds)
   ```bash
   ls -la data/hypercode_knowledge_base.json
   ```

**Done!** Your space is now imported! 🚀

---

## 🔍 Validation Checklist

Before clicking import, verify:

- [ ] All documents have a title (non-empty string)
- [ ] All documents have content (meaningful text, 10+ chars)
- [ ] All documents have tags (1-5 items, lowercase, no spaces)
- [ ] All URLs are valid or set to `null`
- [ ] No duplicate documents
- [ ] JSON syntax is correct (valid brackets and quotes)
- [ ] No special characters breaking JSON

**Quick Test:**

```bash
python -m json.tool my-hypercode-space.json > /dev/null && echo "✅ Valid JSON!"
```

---

## 🆘 Troubleshooting

### "Invalid JSON" Error

- Check for unescaped quotes: use `\"` not `"`
- Check for trailing commas in arrays/objects
- Validate with: `python -m json.tool yourfile.json`

### "Tags must be lowercase" Error

- Example: Change `["AI-Integration"]` → `["ai-integration"]`
- Remove spaces: Change `["natural language"]` → `["natural-language"]`

### "Content too short" Error

- Add more detail to your content (minimum 10 characters)
- Combine short entries if needed

### Import Completes but Data Doesn't Appear

- Check file was created: `ls data/hypercode_knowledge_base.json`
- Check permissions: Can Python write to `data/` directory?
- Check JSON template loaded: Look for "Imported X documents" message

---

## 🎓 Learning Path

1. **Start Here**: Read this checklist (you are here!)
2. **Deep Dive**: Read `hypercode-import-guide.md`
3. **See Examples**: Study `hypercode-example-data.json`
4. **Get Technical**: Review `import-helper.py` source code
5. **Experiment**: Create a small test import first
6. **Integrate**: Add to your CI/CD pipeline

---

## 💡 Pro Tips

1. **Start Small**: Import 3-5 documents first, test, then add more
2. **Use Descriptions**: Detailed content helps AI queries later
3. **Tag Consistently**: Use same tag names across documents
4. **URL Matters**: Include Perplexity Space URLs for traceability
5. **Version Your Data**: Keep backups of JSON templates
6. **Update Regularly**: Add new research as your Space grows

---

## 🚀 Next: Using Your Imported Data

Once imported, your knowledge base powers:

```python
from hypercode.perplexity_client import PerplexityClient

client = PerplexityClient()

# Search by keyword
results = client.search_knowledge_base("quantum backend")

# Get AI response using your space data
response = client.query(
    "Explain HyperCode's neurodivergent design",
    use_knowledge_base=True
)
```

Your research is now part of your AI system! 🧠⚡

---

**Ready? Start editing that template and import your Space data now!** 🎯🚀
