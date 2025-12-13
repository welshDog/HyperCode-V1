# HyperCode Knowledge Base Builder

This directory contains scripts for building and maintaining the HyperCode knowledge base.

## Overview

The knowledge base builder scans the HyperCode repository and processes various file types to create a searchable, structured knowledge base. It extracts metadata and content from different file formats and builds a unified index.

## File Structure

```
scripts/
├── build_knowledge_base.py  # Main script for building the knowledge base
├── document_processor.py    # Document processing utilities
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## Setup

1. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

2. Make the scripts executable (Linux/macOS):
    ```bash
    chmod +x build_knowledge_base.py
    ```

## Usage

### Building the Knowledge Base

To build the knowledge base:

```bash
python build_knowledge_base.py
```

### Rebuilding the Knowledge Base

To force a complete rebuild of the knowledge base:

```bash
python build_knowledge_base.py --rebuild
```

### Specifying an Output Directory

To specify a custom output directory:

```bash
python build_knowledge_base.py --output-dir ../custom_output
```

## Output

The knowledge base will be generated in the `data/processed/knowledge_base` directory by default, containing:

-   `documents/`: Processed document files (one JSON file per document)
-   `index.json`: Index of all documents
-   `metadata.json`: Metadata about the knowledge base

## Supported File Types

-   **Code Files**: `.py`, `.js`, `.ts`, `.java`, `.c`, `.cpp`, etc.
-   **Markdown**: `.md`, `.markdown`
-   **Documents**: `.pdf`, `.docx`, `.doc`, `.xlsx`, `.xls`, `.pptx`, `.ppt`
-   **Data Files**: `.csv`, `.json`, `.yaml`, `.yml`, `.toml`
-   **Text Files**: `.txt`, `.log`, `.ini`, `.cfg`, `.conf`

## Customization

### Adding New File Types

To add support for a new file type, modify the `DocumentProcessor` class in `document_processor.py` to include a new method for processing that file type.

### Updating the Index

The index is automatically updated when you run the build script. To customize the index format, modify the `build_index` method in `build_knowledge_base.py`.

## License

This project is part of the HyperCode repository and is licensed under the same terms.
