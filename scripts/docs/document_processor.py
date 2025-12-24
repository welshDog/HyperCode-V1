"""Document processing utilities for HyperCode knowledge base."""

import hashlib
from datetime import datetime
from pathlib import Path
from typing import Dict, Union

import docx
import frontmatter
import markdown
import pandas as pd
import PyPDF2
from bs4 import BeautifulSoup


class DocumentProcessor:
    """Process various document types and extract content."""

    @staticmethod
    def get_file_hash(file_path: Union[str, Path]) -> str:
        """Generate a hash for file content."""
        file_path = Path(file_path)
        hasher = hashlib.md5()
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hasher.update(chunk)
        return hasher.hexdigest()

    @staticmethod
    def extract_metadata(file_path: Union[str, Path]) -> Dict:
        """Extract basic metadata from any file."""
        path = Path(file_path)
        return {
            "file_name": path.name,
            "file_path": str(path.absolute()),
            "file_size": path.stat().st_size,
            "created": datetime.fromtimestamp(path.stat().st_ctime).isoformat(),
            "modified": datetime.fromtimestamp(path.stat().st_mtime).isoformat(),
            "file_type": path.suffix.lower(),
            "content_hash": DocumentProcessor.get_file_hash(path),
        }

    @staticmethod
    def extract_pdf_content(file_path: Union[str, Path]) -> Dict:
        """Extract text content from PDF files."""
        content = {"content_type": "text", "content": "", "pages": 0, "metadata": {}}

        try:
            with open(file_path, "rb") as f:
                pdf = PyPDF2.PdfReader(f)
                content["pages"] = len(pdf.pages)
                content["content"] = "\n\n".join(
                    page.extract_text() for page in pdf.pages
                )

                # Extract metadata if available
                if hasattr(pdf, "metadata") and pdf.metadata:
                    content["metadata"] = {
                        "title": pdf.metadata.get("/Title", ""),
                        "author": pdf.metadata.get("/Author", ""),
                        "subject": pdf.metadata.get("/Subject", ""),
                        "keywords": pdf.metadata.get("/Keywords", ""),
                        "creator": pdf.metadata.get("/Creator", ""),
                        "producer": pdf.metadata.get("/Producer", ""),
                        "creation_date": pdf.metadata.get("/CreationDate", ""),
                        "mod_date": pdf.metadata.get("/ModDate", ""),
                    }

        except Exception as e:
            content["error"] = f"Error processing PDF: {str(e)}"

        return content

    @staticmethod
    def extract_markdown_content(file_path: Union[str, Path]) -> Dict:
        """Extract content from Markdown files with frontmatter support."""
        content = {"content_type": "markdown", "content": "", "metadata": {}}

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                # Parse frontmatter if exists
                post = frontmatter.load(f)
                content["metadata"] = dict(post.metadata)
                content["content"] = post.content

                # Extract headers for better search
                soup = BeautifulSoup(markdown.markdown(post.content), "html.parser")
                headers = [
                    h.get_text() for h in soup.find_all(["h1", "h2", "h3", "h4"])
                ]
                if headers:
                    content["metadata"]["headers"] = headers

        except Exception as e:
            content["error"] = f"Error processing Markdown: {str(e)}"

        return content

    @staticmethod
    def extract_docx_content(file_path: Union[str, Path]) -> Dict:
        """Extract text content from DOCX files."""
        content = {"content_type": "text", "content": "", "metadata": {}}

        try:
            doc = docx.Document(file_path)
            content["content"] = "\n".join(
                paragraph.text for paragraph in doc.paragraphs
            )

            # Extract core properties
            core_props = doc.core_properties
            content["metadata"] = {
                "title": core_props.title,
                "author": core_props.author,
                "subject": core_props.subject,
                "keywords": core_props.keywords,
                "category": core_props.category,
                "comments": core_props.comments,
                "created": (
                    core_props.created.isoformat() if core_props.created else None
                ),
                "modified": (
                    core_props.modified.isoformat() if core_props.modified else None
                ),
                "last_modified_by": core_props.last_modified_by,
            }

        except Exception as e:
            content["error"] = f"Error processing DOCX: {str(e)}"

        return content

    @staticmethod
    def extract_csv_content(file_path: Union[str, Path]) -> Dict:
        """Extract content from CSV files."""
        content = {"content_type": "table", "content": "", "metadata": {}}

        try:
            # Read CSV with pandas
            df = pd.read_csv(file_path)

            # Convert to a more JSON-serializable format
            content["content"] = {
                "columns": df.columns.tolist(),
                "sample": df.head(5).to_dict(orient="records"),
                "row_count": len(df),
            }

        except Exception as e:
            content["error"] = f"Error processing CSV: {str(e)}"

        return content

    @staticmethod
    def extract_text_content(file_path: Union[str, Path]) -> Dict:
        """Extract content from plain text files."""
        content = {"content_type": "text", "content": "", "metadata": {}}

        try:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                content["content"] = f.read()
        except Exception as e:
            content["error"] = f"Error reading text file: {str(e)}"

        return content

    @classmethod
    def process_document(cls, file_path: Union[str, Path]) -> Dict:
        """Process a document based on its file type."""
        path = Path(file_path)
        if not path.exists():
            return {"error": f"File not found: {file_path}"}

        # Get basic metadata
        result = cls.extract_metadata(path)

        # Process based on file type
        file_ext = path.suffix.lower()

        if file_ext == ".pdf":
            result.update(cls.extract_pdf_content(path))
        elif file_ext in (".md", ".markdown"):
            result.update(cls.extract_markdown_content(path))
        elif file_ext == ".docx":
            result.update(cls.extract_docx_content(path))
        elif file_ext == ".csv":
            result.update(cls.extract_csv_content(path))
        elif file_ext in (".txt", ".py", ".js", ".ts", ".html", ".css", ".json"):
            result.update(cls.extract_text_content(path))
        else:
            # Try to process as text by default
            try:
                result.update(cls.extract_text_content(path))
                result["content_type"] = "text/unknown"
            except Exception as e:
                result["error"] = f"Unsupported file type: {file_ext}. Error: {str(e)}"

        return result
