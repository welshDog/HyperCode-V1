#!/usr/bin/env python3
"""
HyperCode Perplexity Space Import Helper
Streamlines the process of converting your Perplexity Space data into the HyperCode knowledge base
"""

import json
import sys
from pathlib import Path
from typing import Dict, List


class SpaceImportHelper:
    """Helper class for managing Perplexity Space imports"""

    def __init__(self, output_dir: str = "data"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        self.documents: List[Dict] = []

    def validate_document(self, doc: Dict) -> tuple[bool, str]:
        """
        Validate a document structure
        Returns (is_valid, error_message)
        """
        required_fields = ["title", "content", "tags"]
        optional_fields = ["url"]

        # Check required fields
        for field in required_fields:
            if field not in doc:
                return False, f"Missing required field: {field}"
            if not doc[field]:
                return False, f"Empty required field: {field}"

        # Validate title
        if not isinstance(doc["title"], str) or len(doc["title"]) < 3:
            return False, "Title must be a non-empty string (min 3 chars)"

        # Validate content
        if not isinstance(doc["content"], str) or len(doc["content"]) < 10:
            return False, "Content must be a meaningful string (min 10 chars)"

        # Validate tags
        if not isinstance(doc["tags"], list):
            return False, "Tags must be a list"
        if len(doc["tags"]) < 1 or len(doc["tags"]) > 10:
            return False, "Tags should be 1-10 items"

        for tag in doc["tags"]:
            if not isinstance(tag, str):
                return False, "All tags must be strings"
            if not tag.islower() or " " in tag:
                return False, f"Tag '{tag}' must be lowercase with hyphens (not spaces)"

        # Validate URL (optional)
        if "url" in doc and doc["url"] is not None:
            if not isinstance(doc["url"], str):
                return False, "URL must be a string or null"

        return True, ""

    def load_template(self, filepath: str) -> bool:
        """Load documents from JSON template file"""
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)

            if "documents" not in data:
                print("❌ Error: JSON must contain 'documents' key")
                return False

            self.documents = data["documents"]
            print(f"✅ Loaded {len(self.documents)} documents from template")
            return True
        except json.JSONDecodeError as e:
            print(f"❌ JSON Parse Error: {e}")
            return False
        except FileNotFoundError:
            print(f"❌ File not found: {filepath}")
            return False

    def validate_all(self) -> tuple[bool, List[str]]:
        """Validate all loaded documents"""
        errors = []
        for i, doc in enumerate(self.documents):
            is_valid, error = self.validate_document(doc)
            if not is_valid:
                errors.append(
                    f"Document {i} ('{doc.get('title', 'UNKNOWN')}'): {error}"
                )

        return len(errors) == 0, errors

    def generate_report(self) -> str:
        """Generate a validation report"""
        report = [
            "\n" + "=" * 60,
            "🔍 HyperCode Space Import Validation Report",
            "=" * 60,
            "\n📊 Statistics:",
            f"   • Total Documents: {len(self.documents)}",
        ]

        # Calculate stats
        total_content = sum(len(doc.get("content", "")) for doc in self.documents)
        all_tags = set()
        urls_count = sum(1 for doc in self.documents if doc.get("url"))

        for doc in self.documents:
            all_tags.update(doc.get("tags", []))

        report.extend(
            [
                f"   • Total Tags: {len(all_tags)}",
                f"   • Documents with URLs: {urls_count}",
                f"   • Total Content Size: {total_content:,} characters",
            ]
        )

        # Tag breakdown
        report.append("\n🏷️  Tags Used:")
        tag_list = sorted(all_tags)
        for tag in tag_list:
            count = sum(1 for doc in self.documents if tag in doc.get("tags", []))
            report.append(f"   • {tag}: {count} document(s)")

        # Document list
        report.append("\n📋 Documents:")
        for i, doc in enumerate(self.documents, 1):
            tags = ", ".join(doc.get("tags", []))
            report.append(f"   {i}. {doc.get('title', 'UNTITLED')}")
            report.append(f"      Tags: {tags}")
            report.append(f"      Size: {len(doc.get('content', '')):,} chars")
            if doc.get("url"):
                report.append(f"      URL: {doc['url']}")

        report.append("\n" + "=" * 60 + "\n")
        return "\n".join(report)

    def create_import_script(self, output_file: str) -> bool:
        """Generate a Python script to import the data"""
        script = '''#!/usr/bin/env python3
"""Auto-generated HyperCode Space import script"""

import json
from pathlib import Path

def import_space_data():
    """Import Perplexity Space data into HyperCode knowledge base"""

    # Load the template
    template_file = Path("perplexity_space_import_template.json")
    with open(template_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Initialize knowledge base
    kb_file = Path("data/hypercode_knowledge_base.json")
    if kb_file.exists():
        with open(kb_file, "r", encoding="utf-8") as f:
            kb = json.load(f)
    else:
        kb = {"documents": [], "imported_at": []}

    # Add new documents
    print(f"📥 Importing {len(data['documents'])} documents...")

    for doc in data['documents']:
        kb["documents"].append(doc)
        print(f"   ✅ {doc['title']}")

    # Save updated knowledge base
    kb_file.parent.mkdir(exist_ok=True)
    with open(kb_file, "w", encoding="utf-8") as f:
        json.dump(kb, f, indent=2, ensure_ascii=False)

    print(f"\\n🎉 Import complete! {len(kb['documents'])} documents in knowledge base")
    return True

if __name__ == "__main__":
    import_space_data()
'''

        try:
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(script)
            print(f"✅ Generated import script: {output_file}")
            return True
        except Exception as e:
            print(f"❌ Failed to create script: {e}")
            return False

    def create_template_instructions(self, output_file: str) -> bool:
        """Generate detailed instructions for filling the template"""
        instructions = """# 📝 How to Fill the Import Template

## Quick Start

1. Open `perplexity_space_import_template.json` in your text editor
2. Replace the example documents with your actual Perplexity Space data
3. For each document, fill:
   - **title**: Clear, descriptive name (e.g., "HyperCode Language Specification v0.1")
   - **content**: The actual research/findings (copy-paste from your Space)
   - **tags**: 1-5 relevant tags (lowercase, hyphen-separated)
   - **url**: Link to the Perplexity Space (or null if not available)

## Template Structure

```json
{
  "documents": [
    {
      "title": "Your Document Title",
      "content": "Full content here...",
      "url": "https://perplexity.ai/...",
      "tags": ["tag1", "tag2", "tag3"]
    }
  ]
}
```

## Recommended Tags

- **Core**: core-language, specification, syntax, grammar
- **Features**: spatial-programming, natural-language, accessibility, neurodivergent
- **Backend**: quantum, dna-computing, gpu, fpga, neuromorphic
- **AI**: ai-integration, gpt, claude, mistral, llm-compatibility
- **Implementation**: roadmap, architecture, phases, development
- **Research**: research, findings, analysis, proof-of-concept
- **Community**: community, open-source, contributions, collaboration

## Common Mistakes to Avoid

1. ❌ Tags with spaces: "natural language" → ✅ "natural-language"
2. ❌ UPPERCASE tags: "AI" → ✅ "ai"
3. ❌ Too many tags: [tag1, tag2, tag3, tag4, tag5, tag6] → ✅ Max 5
4. ❌ Empty content → Always include meaningful content
5. ❌ Duplicate documents → Check for duplicates before import

## Validation

Run this to check your template:

```bash
python3 -c "import json; json.load(open('perplexity_space_import_template.json'))" && echo "✅ Valid!"
```

## Need Help?

If a document doesn't validate, the import helper will tell you exactly what's wrong.
Check the error message and fix accordingly.
"""

        try:
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(instructions)
            print(f"✅ Generated instructions: {output_file}")
            return True
        except Exception as e:
            print(f"❌ Failed to create instructions: {e}")
            return False


def main():
    """CLI interface for the import helper"""

    if len(sys.argv) < 2:
        print(
            """
🚀 HyperCode Perplexity Space Import Helper

Usage:
  python import_helper.py validate <template.json>     # Validate template
  python import_helper.py report <template.json>       # Generate report
  python import_helper.py generate-script              # Create import script
  python import_helper.py generate-instructions        # Create instruction guide
        """
        )
        return

    helper = SpaceImportHelper()
    command = sys.argv[1]

    if command == "validate":
        if len(sys.argv) < 3:
            print("❌ Please specify template file")
            return

        if helper.load_template(sys.argv[2]):
            is_valid, errors = helper.validate_all()
            if is_valid:
                print("✅ Template is valid and ready for import!")
            else:
                print("❌ Validation errors found:")
                for error in errors:
                    print(f"   • {error}")

    elif command == "report":
        if len(sys.argv) < 3:
            print("❌ Please specify template file")
            return

        if helper.load_template(sys.argv[2]):
            is_valid, errors = helper.validate_all()
            print(helper.generate_report())
            if not is_valid:
                print("⚠️  Validation errors:")
                for error in errors:
                    print(f"   • {error}")

    elif command == "generate-script":
        helper.create_import_script("import_space.py")

    elif command == "generate-instructions":
        helper.create_template_instructions("FILL_TEMPLATE_GUIDE.md")

    else:
        print(f"❌ Unknown command: {command}")


if __name__ == "__main__":
    main()
