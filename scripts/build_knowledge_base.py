#!/usr/bin/env python3
"""
HyperCode Knowledge Base Builder

This script scans the HyperCode repository and builds a comprehensive
knowledge base from various document types including code, markdown, PDFs, etc.

Usage:
  python build_knowledge_base.py [--rebuild] [--output-dir OUTPUT_DIR]

Options:
  --rebuild       Rebuild the entire knowledge base from scratch
  --output-dir    Directory to store the generated knowledge base [default: ../data/processed]
"""

import argparse
import hashlib
import json
import os
import shutil

# Add the current directory to the path so we can import document_processor
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Optional

from tqdm import tqdm

sys.path.append(str(Path(__file__).parent.absolute()))

from document_processor import DocumentProcessor


class KnowledgeBaseBuilder:
    """Build a knowledge base from the HyperCode repository."""

    def __init__(self, repo_root: str = ".", output_dir: str = "../data/processed"):
        """Initialize the knowledge base builder.

        Args:
            repo_root: Root directory of the HyperCode repository
            output_dir: Directory to store the generated knowledge base
        """
        self.repo_root = Path(repo_root).resolve()
        self.output_dir = Path(output_dir).resolve()
        self.knowledge_base_dir = self.output_dir / "knowledge_base"
        self.documents_dir = self.knowledge_base_dir / "documents"
        self.index_file = self.knowledge_base_dir / "index.json"
        self.metadata_file = self.knowledge_base_dir / "metadata.json"

        # Create output directories if they don't exist
        self.documents_dir.mkdir(parents=True, exist_ok=True)

        # Initialize metadata
        self.metadata = {
            "name": "HyperCode Knowledge Base",
            "version": "1.0.0",
            "created_at": datetime.utcnow().isoformat(),
            "updated_at": datetime.utcnow().isoformat(),
            "document_count": 0,
            "file_types": {},
            "stats": {
                "code_files": 0,
                "markdown_files": 0,
                "pdf_files": 0,
                "document_files": 0,
                "other_files": 0,
                "total_files": 0,
                "processing_errors": 0,
            },
        }

        # Load existing metadata if it exists
        if self.metadata_file.exists():
            with open(self.metadata_file, "r", encoding="utf-8") as f:
                self.metadata.update(json.load(f))

    def should_skip(self, path: Path) -> bool:
        """Check if a path should be skipped during processing."""
        # Skip hidden directories and files
        if any(part.startswith(".") for part in path.parts):
            return True

        # Skip common directories
        skip_dirs = {
            "node_modules",
            ".git",
            "__pycache__",
            ".venv",
            "venv",
            ".pytest_cache",
            "dist",
            "build",
            ".egg-info",
            "coverage",
            ".nyc_output",
            ".DS_Store",
            ".idea",
            ".vscode",
            "data",
            "docs/_build",
            "docs/_static",
            "docs/_templates",
            "tests",
        }

        if path.name in skip_dirs:
            return True

        # Skip binary files and other non-text files
        skip_extensions = {
            ".pyc",
            ".pyo",
            ".pyd",
            ".so",
            ".dll",
            ".exe",
            ".dylib",
            ".class",
            ".jar",
            ".war",
            ".ear",
            ".zip",
            ".tar",
            ".gz",
            ".bz2",
            ".7z",
            ".rar",
            ".png",
            ".jpg",
            ".jpeg",
            ".gif",
            ".bmp",
            ".ico",
            ".svg",
            ".woff",
            ".woff2",
            ".ttf",
            ".eot",
            ".mp3",
            ".wav",
            ".ogg",
            ".mp4",
            ".avi",
            ".mov",
            ".mkv",
            ".pdf",  # We'll handle PDFs separately
            ".doc",
            ".docx",
            ".xls",
            ".xlsx",
            ".ppt",
            ".pptx",  # Handled separately
        }

        if path.suffix.lower() in skip_extensions:
            return True

        return False

    def get_file_type(self, path: Path) -> str:
        """Get the file type category."""
        ext = path.suffix.lower()

        code_extensions = {
            ".py",
            ".js",
            ".ts",
            ".jsx",
            ".tsx",
            ".java",
            ".c",
            ".cpp",
            ".h",
            ".hpp",
            ".cs",
            ".go",
            ".rb",
            ".php",
            ".swift",
            ".kt",
            ".scala",
            ".rs",
            ".sh",
            ".bash",
            ".zsh",
            ".fish",
            ".ps1",
            ".bat",
            ".cmd",
            ".m",
            ".r",
            ".lua",
            ".pl",
            ".pm",
            ".t",
            ".sql",
            ".html",
            ".css",
            ".scss",
            ".sass",
            ".less",
            ".styl",
            ".json",
            ".yaml",
            ".yml",
            ".toml",
            ".ini",
            ".cfg",
            ".conf",
            ".xml",
            ".md",
            ".markdown",
            ".txt",
        }

        doc_extensions = {
            ".pdf",
            ".doc",
            ".docx",
            ".xls",
            ".xlsx",
            ".ppt",
            ".pptx",
            ".odt",
            ".ods",
            ".odp",
            ".rtf",
            ".tex",
            ".epub",
            ".mobi",
        }

        if ext in code_extensions:
            return "code"
        elif ext in doc_extensions:
            return "document"
        elif ext in {".md", ".markdown"}:
            return "markdown"
        else:
            return "other"

    def process_file(self, file_path: Path) -> Optional[Dict[str, Any]]:
        """Process a single file and return its metadata."""
        try:
            # Process the document based on its type
            result = DocumentProcessor.process_document(file_path)

            # Add additional metadata
            result["file_type"] = self.get_file_type(file_path)
            result["relative_path"] = str(file_path.relative_to(self.repo_root))

            # Generate a unique ID for the document
            doc_id = hashlib.md5(result["relative_path"].encode("utf-8")).hexdigest()
            result["id"] = doc_id

            # Save the document content
            doc_path = self.documents_dir / f"{doc_id}.json"
            with open(doc_path, "w", encoding="utf-8") as f:
                json.dump(result, f, ensure_ascii=False, indent=2)

            # Update statistics
            self.metadata["stats"]["total_files"] += 1
            if result["file_type"] == "code":
                self.metadata["stats"]["code_files"] += 1
            elif result["file_type"] == "markdown":
                self.metadata["stats"]["markdown_files"] += 1
            elif result["file_type"] == "document":
                self.metadata["stats"]["document_files"] += 1
            else:
                self.metadata["stats"]["other_files"] += 1

            # Update file type statistics
            ext = file_path.suffix.lower()
            self.metadata["file_types"][ext] = (
                self.metadata["file_types"].get(ext, 0) + 1
            )

            return result

        except Exception as e:
            print(f"[ERROR] Error processing {file_path}: {str(e)}")
            self.metadata["stats"]["processing_errors"] += 1
            return None

    def build_index(self):
        """Build the knowledge base index."""
        print(f"[SEARCH] Building knowledge base for {self.repo_root}")
        print(f"[OUTPUT] Output directory: {self.output_dir}")
        print()

        # Clear existing documents if rebuilding
        if self.documents_dir.exists():
            shutil.rmtree(self.documents_dir)
        self.documents_dir.mkdir(parents=True, exist_ok=True)

        # Reset metadata
        self.metadata.update(
            {
                "created_at": datetime.utcnow().isoformat(),
                "updated_at": datetime.utcnow().isoformat(),
                "document_count": 0,
                "file_types": {},
                "stats": {
                    "code_files": 0,
                    "markdown_files": 0,
                    "pdf_files": 0,
                    "document_files": 0,
                    "other_files": 0,
                    "total_files": 0,
                    "processing_errors": 0,
                },
            }
        )

        # Walk through the repository
        index = []
        file_count = 0

        # Get all files first to show progress
        all_files = []
        for root, dirs, files in os.walk(self.repo_root):
            # Skip ignored directories
            dirs[:] = [d for d in dirs if not self.should_skip(Path(root) / d)]

            for file in files:
                file_path = Path(root) / file
                if not self.should_skip(file_path):
                    all_files.append(file_path)

        # Process files with progress bar
        for file_path in tqdm(all_files, desc="[FILES] Processing files..."):
            result = self.process_file(file_path)
            if result:
                index.append(
                    {
                        "id": result["id"],
                        "file_name": result["file_name"],
                        "relative_path": result["relative_path"],
                        "file_type": result["file_type"],
                        "content_type": result.get("content_type", "unknown"),
                        "created": result.get("created", ""),
                        "modified": result.get("modified", ""),
                    }
                )
                file_count += 1

        # Update document count
        self.metadata["document_count"] = file_count
        self.metadata["updated_at"] = datetime.utcnow().isoformat()

        # Save the index
        with open(self.index_file, "w", encoding="utf-8") as f:
            json.dump(
                {"metadata": self.metadata, "documents": index},
                f,
                ensure_ascii=False,
                indent=2,
            )

        # Save metadata
        with open(self.metadata_file, "w", encoding="utf-8") as f:
            json.dump(self.metadata, f, ensure_ascii=False, indent=2)

        # Print summary
        print("[DONE] Knowledge base built successfully!")
        print(f"[STATS] Documents processed: {self.metadata['document_count']}")
        print(
            f"[FILETYPES] File types: {', '.join(f'{k} ({v})' for k, v in self.metadata['file_types'].items())}"
        )
        print(f"[STATS] Stats: {json.dumps(self.metadata['stats'], indent=2)}")
        print(f"[OUTPUT] Index saved to: {self.index_file}")


def main():
    """Main entry point for the script."""
    parser = argparse.ArgumentParser(description="Build the HyperCode knowledge base.")
    parser.add_argument(
        "--rebuild", action="store_true", help="Rebuild the entire knowledge base"
    )
    parser.add_argument(
        "--output-dir",
        default="../data/processed",
        help="Output directory for the knowledge base",
    )

    args = parser.parse_args()

    # Initialize the builder
    builder = KnowledgeBaseBuilder(output_dir=args.output_dir)

    # Build the knowledge base
    builder.build_index()


if __name__ == "__main__":
    main()
