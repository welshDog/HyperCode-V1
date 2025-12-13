import os
import re
import ast
import sys
from pathlib import Path
from typing import List, Dict, Any

# Configuration
SCAN_DIR = "."
REPORT_FILE = "scan_results.txt"

# Regex Patterns for Secrets
SECRET_PATTERNS = {
    "AWS Access Key": r"AKIA[0-9A-Z]{16}",
    "Generic API Key": r"api_key\s*=\s*['\"][a-zA-Z0-9_\-]{20,}['\"]",
    "Private Key": r"-----BEGIN RSA PRIVATE KEY-----",
    "Hardcoded Password": r"password\s*=\s*['\"][a-zA-Z0-9@#$%^&*]{8,}['\"]",
    "IPv4 Address": r"\b(?!0\.0\.0\.0)(?!127\.0\.0\.1)(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b"
}

# Dangerous Python Functions (AST Analysis)
DANGEROUS_FUNCTIONS = {
    "eval": "Arbitrary code execution risk.",
    "exec": "Arbitrary code execution risk.",
    "subprocess.call": "Command injection risk.",
    "subprocess.Popen": "Command injection risk.",
    "os.system": "Command injection risk.",
    "pickle.loads": "Insecure deserialization risk.",
    "input": "User input trust issue."
}

class SecurityScanner:
    def __init__(self, target_dir: str):
        self.target_dir = Path(target_dir)
        self.findings = []

    def scan(self):
        print(f"Starting Security Scan on: {self.target_dir.absolute()}")
        for root, _, files in os.walk(self.target_dir):
            for file in files:
                file_path = Path(root) / file
                if file_path.name == "security_scan.py":
                    continue
                
                # simple extension check
                if file_path.suffix in ['.py', '.js', '.hc', '.md', '.txt']:
                    self.scan_file(file_path)

        self.print_report()

    def scan_file(self, file_path: Path):
        try:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()

            # 1. Regex Scan for Secrets
            for name, pattern in SECRET_PATTERNS.items():
                matches = re.finditer(pattern, content)
                for match in matches:
                    self.add_finding("Secret", name, file_path, match.start(), "Potential hardcoded secret")

            # 2. AST Scan for Dangerous Functions (Python only)
            if file_path.suffix == '.py':
                self.scan_ast(file_path, content)

        except Exception as e:
            print(f"Error scanning {file_path}: {e}")

    def scan_ast(self, file_path: Path, content: str):
        try:
            tree = ast.parse(content)
            for node in ast.walk(tree):
                if isinstance(node, ast.Call):
                    func_name = self.get_func_name(node.func)
                    if func_name in DANGEROUS_FUNCTIONS:
                        self.add_finding(
                            "Vulnerability", 
                            func_name, 
                            file_path, 
                            getattr(node, 'lineno', 0), 
                            DANGEROUS_FUNCTIONS[func_name]
                        )
        except SyntaxError:
            pass # Ignore syntax errors in working files

    def get_func_name(self, node):
        if isinstance(node, ast.Name):
            return node.id
        elif isinstance(node, ast.Attribute):
            return f"{self.get_func_name(node.value)}.{node.attr}"
        return ""

    def add_finding(self, category, name, file_path, location, description):
        self.findings.append({
            "category": category,
            "name": name,
            "file": str(file_path),
            "location": location,
            "description": description
        })

    def print_report(self):
        print("\n=== HyperCode Security Audit Report ===")
        if not self.findings:
            print("✅ No critical issues found.")
            return

        print(f"⚠️  Found {len(self.findings)} potential issues:\n")
        
        # Group by Category
        for finding in self.findings:
            loc_str = f"Line {finding['location']}" if isinstance(finding['location'], int) else f"Pos {finding['location']}"
            print(f"[{finding['category'].upper()}] {finding['name']}")
            print(f"  File: {finding['file']}")
            print(f"  Loc:  {loc_str}")
            print(f"  Desc: {finding['description']}")
            print("-" * 40)

if __name__ == "__main__":
    scanner = SecurityScanner(SCAN_DIR)
    scanner.scan()
