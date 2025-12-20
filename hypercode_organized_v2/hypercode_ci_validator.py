#!/usr/bin/env python3
"""
HyperCode Research Database Validator
Ensures all research files conform to schema requirements.
Run in CI to prevent schema violations from merging.

Usage:
    python validate_research_db.py [path_to_research_db]
    
Exit codes:
    0: All files valid
    1: Validation errors found
"""

import os
import sys
import re
from pathlib import Path
from typing import List, Dict, Set, Tuple
import yaml

# Color codes for terminal output
class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    BOLD = '\033[1m'
    END = '\033[0m'

class ValidationError:
    def __init__(self, file_path: str, line: int, error: str, severity: str = "error"):
        self.file_path = file_path
        self.line = line
        self.error = error
        self.severity = severity
    
    def __str__(self):
        color = Colors.RED if self.severity == "error" else Colors.YELLOW
        return f"{color}{self.file_path}:{self.line} - {self.error}{Colors.END}"

class ResearchDBValidator:
    def __init__(self, db_path: str):
        self.db_path = Path(db_path)
        self.errors: List[ValidationError] = []
        self.warnings: List[ValidationError] = []
        self.all_ids: Set[str] = set()
        self.all_links: Dict[str, List[str]] = {}  # file -> [linked_ids]
        
        # Valid values for enum fields
        self.VALID_TYPES = {'research_note', 'decision', 'experiment', 'glossary'}
        self.VALID_STATUSES = {'draft', 'reviewed', 'adopted', 'deprecated', 'superseded', 'in_progress', 'completed', 'proposed', 'implemented', 'rolled_back', 'pending', 'inconclusive'}
        self.VALID_SOURCE_QUALITY = {'peer_reviewed', 'industry_report', 'anecdotal', 'interview'}
        self.VALID_CONFIDENCE = {'high', 'medium', 'low'}
        self.VALID_METHODOLOGIES = {'usability_test', 'AB_test', 'pilot', 'prototype', 'survey', 'interview'}
        self.VALID_RESULTS = {'success', 'partial', 'failed', 'inconclusive', 'pending'}
        
    def validate_all(self) -> bool:
        """Run all validations. Returns True if all valid, False otherwise."""
        print(f"{Colors.BOLD}Validating HyperCode Research Database...{Colors.END}\n")
        
        # Find all markdown files
        md_files = list(self.db_path.rglob("*.md"))
        
        # Exclude template files and schema
        md_files = [f for f in md_files if not any(
            part.startswith('_') for part in f.parts
        )]
        
        if not md_files:
            print(f"{Colors.YELLOW}No markdown files found to validate.{Colors.END}")
            return True
        
        print(f"Found {len(md_files)} files to validate\n")
        
        # First pass: collect all IDs and validate individual files
        for md_file in md_files:
            self._validate_file(md_file)
        
        # Second pass: validate links
        self._validate_all_links()
        
        # Report results
        return self._report_results()
    
    def _validate_file(self, file_path: Path) -> None:
        """Validate a single markdown file."""
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract YAML front matter
        front_matter, body = self._extract_front_matter(content)
        
        if not front_matter:
            self.errors.append(ValidationError(
                str(file_path.relative_to(self.db_path)),
                1,
                "Missing YAML front matter"
            ))
            return
        
        # Parse YAML
        try:
            metadata = yaml.safe_load(front_matter)
        except yaml.YAMLError as e:
            self.errors.append(ValidationError(
                str(file_path.relative_to(self.db_path)),
                1,
                f"Invalid YAML: {e}"
            ))
            return
        
        # Validate metadata
        self._validate_metadata(file_path, metadata)
        
        # Validate body content
        self._validate_body(file_path, metadata.get('type'), body)
        
        # Store ID for link validation
        if 'id' in metadata:
            file_id = metadata['id']
            if file_id in self.all_ids:
                self.errors.append(ValidationError(
                    str(file_path.relative_to(self.db_path)),
                    0,
                    f"Duplicate ID: '{file_id}'"
                ))
            self.all_ids.add(file_id)
        
        # Extract links for later validation
        links = self._extract_links(body)
        self.all_links[str(file_path)] = links
    
    def _extract_front_matter(self, content: str) -> Tuple[str, str]:
        """Extract YAML front matter and body from markdown."""
        pattern = r'^---\s*\n(.*?)\n---\s*\n(.*)$'
        match = re.match(pattern, content, re.DOTALL)
        
        if match:
            return match.group(1), match.group(2)
        return None, content
    
    def _validate_metadata(self, file_path: Path, metadata: dict) -> None:
        """Validate YAML front matter."""
        rel_path = str(file_path.relative_to(self.db_path))
        
        # Required fields for all types
        required_fields = ['type', 'title', 'id', 'created', 'status', 'tags']
        
        for field in required_fields:
            if field not in metadata:
                self.errors.append(ValidationError(
                    rel_path, 0, f"Missing required field: '{field}'"
                ))
        
        # Validate type
        if 'type' in metadata:
            doc_type = metadata['type']
            if doc_type not in self.VALID_TYPES:
                self.errors.append(ValidationError(
                    rel_path, 0,
                    f"Invalid type '{doc_type}'. Must be one of: {self.VALID_TYPES}"
                ))
            
            # Type-specific validations
            if doc_type == 'research_note':
                self._validate_research_note(file_path, metadata)
            elif doc_type == 'decision':
                self._validate_decision(file_path, metadata)
            elif doc_type == 'experiment':
                self._validate_experiment(file_path, metadata)
        
        # Validate status
        if 'status' in metadata and metadata['status'] not in self.VALID_STATUSES:
            self.errors.append(ValidationError(
                rel_path, 0,
                f"Invalid status '{metadata['status']}'. Must be one of: {self.VALID_STATUSES}"
            ))
        
        # Validate tags
        if 'tags' in metadata:
            if not isinstance(metadata['tags'], list):
                self.errors.append(ValidationError(
                    rel_path, 0, "Tags must be a list"
                ))
            elif len(metadata['tags']) == 0:
                self.warnings.append(ValidationError(
                    rel_path, 0, "No tags specified", "warning"
                ))
        
        # Validate date format
        date_fields = ['created', 'updated']
        for field in date_fields:
            if field in metadata:
                date_str = str(metadata[field])
                if not re.match(r'^\d{4}-\d{2}-\d{2}$', date_str):
                    self.errors.append(ValidationError(
                        rel_path, 0,
                        f"Invalid date format for '{field}': '{date_str}'. Use YYYY-MM-DD"
                    ))
    
    def _validate_research_note(self, file_path: Path, metadata: dict) -> None:
        """Validate research_note specific fields."""
        rel_path = str(file_path.relative_to(self.db_path))
        
        if 'source' not in metadata:
            self.warnings.append(ValidationError(
                rel_path, 0, "Research note should have 'source' field", "warning"
            ))
        
        if 'source_quality' in metadata:
            if metadata['source_quality'] not in self.VALID_SOURCE_QUALITY:
                self.errors.append(ValidationError(
                    rel_path, 0,
                    f"Invalid source_quality. Must be one of: {self.VALID_SOURCE_QUALITY}"
                ))
        
        if 'confidence' in metadata:
            if metadata['confidence'] not in self.VALID_CONFIDENCE:
                self.errors.append(ValidationError(
                    rel_path, 0,
                    f"Invalid confidence. Must be one of: {self.VALID_CONFIDENCE}"
                ))
    
    def _validate_decision(self, file_path: Path, metadata: dict) -> None:
        """Validate decision (ADR) specific fields."""
        rel_path = str(file_path.relative_to(self.db_path))
        
        # ADR naming convention
        if not re.match(r'adr-\d+-', metadata.get('id', '')):
            self.warnings.append(ValidationError(
                rel_path, 0,
                "Decision ID should follow pattern: adr-XXX-title", "warning"
            ))
    
    def _validate_experiment(self, file_path: Path, metadata: dict) -> None:
        """Validate experiment specific fields."""
        rel_path = str(file_path.relative_to(self.db_path))
        
        if 'hypothesis' not in metadata:
            self.warnings.append(ValidationError(
                rel_path, 0, "Experiment should have 'hypothesis' field", "warning"
            ))
        
        if 'methodology' in metadata:
            if metadata['methodology'] not in self.VALID_METHODOLOGIES:
                self.errors.append(ValidationError(
                    rel_path, 0,
                    f"Invalid methodology. Must be one of: {self.VALID_METHODOLOGIES}"
                ))
        
        if 'result' in metadata:
            if metadata['result'] not in self.VALID_RESULTS:
                self.errors.append(ValidationError(
                    rel_path, 0,
                    f"Invalid result. Must be one of: {self.VALID_RESULTS}"
                ))
    
    def _validate_body(self, file_path: Path, doc_type: str, body: str) -> None:
        """Validate markdown body content."""
        rel_path = str(file_path.relative_to(self.db_path))
        
        # Check for Relations section
        if '## Relations' not in body:
            self.errors.append(ValidationError(
                rel_path, 0, "Missing '## Relations' section"
            ))
        
        # Type-specific body validation
        if doc_type == 'research_note':
            required_sections = ['## Summary', '## Key Findings', '## Implications for HyperCode']
            for section in required_sections:
                if section not in body:
                    self.warnings.append(ValidationError(
                        rel_path, 0, f"Missing recommended section: '{section}'", "warning"
                    ))
        
        elif doc_type == 'decision':
            required_sections = ['## Context', '## Decision', '## Rationale', '## Consequences']
            for section in required_sections:
                if section not in body:
                    self.errors.append(ValidationError(
                        rel_path, 0, f"Missing required section: '{section}'"
                    ))
        
        elif doc_type == 'experiment':
            required_sections = ['## Hypothesis', '## Methodology', '## Results', '## Analysis']
            for section in required_sections:
                if section not in body:
                    self.errors.append(ValidationError(
                        rel_path, 0, f"Missing required section: '{section}'"
                    ))
    
    def _extract_links(self, body: str) -> List[str]:
        """Extract all [[wiki-style]] links from body."""
        pattern = r'\[\[([^\]]+)\]\]'
        return re.findall(pattern, body)
    
    def _validate_all_links(self) -> None:
        """Validate that all [[links]] point to existing IDs."""
        for file_path, links in self.all_links.items():
            rel_path = str(Path(file_path).relative_to(self.db_path))
            for link in links:
                if link not in self.all_ids:
                    self.warnings.append(ValidationError(
                        rel_path, 0,
                        f"Broken link: '[[{link}]]' does not exist", "warning"
                    ))
    
    def _report_results(self) -> bool:
        """Print validation results and return success status."""
        print(f"\n{Colors.BOLD}Validation Results:{Colors.END}\n")
        
        if self.errors:
            print(f"{Colors.RED}✗ {len(self.errors)} error(s) found:{Colors.END}\n")
            for error in self.errors:
                print(f"  {error}")
            print()
        
        if self.warnings:
            print(f"{Colors.YELLOW}⚠ {len(self.warnings)} warning(s):{Colors.END}\n")
            for warning in self.warnings:
                print(f"  {warning}")
            print()
        
        if not self.errors and not self.warnings:
            print(f"{Colors.GREEN}✓ All files valid!{Colors.END}\n")
            return True
        elif not self.errors:
            print(f"{Colors.GREEN}✓ No errors (warnings can be addressed later){Colors.END}\n")
            return True
        else:
            print(f"{Colors.RED}✗ Validation failed. Please fix errors before merging.{Colors.END}\n")
            return False


def main():
    if len(sys.argv) < 2:
        db_path = "."
    else:
        db_path = sys.argv[1]
    
    if not os.path.exists(db_path):
        print(f"{Colors.RED}Error: Path '{db_path}' does not exist{Colors.END}")
        sys.exit(1)
    
    validator = ResearchDBValidator(db_path)
    success = validator.validate_all()
    
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
