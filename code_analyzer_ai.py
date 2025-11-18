#!/usr/bin/env python3
"""
Perplexity AI Code Analyzer for HyperCode
Provides intelligent code analysis and improvement suggestions
"""

import ast
import json
import os
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from hypercode.perplexity_client import PerplexityClient


class CodeAnalyzerAI:
    """AI-powered code analyzer for HyperCode"""
    
    def __init__(self):
        self.perplexity = PerplexityClient()
        
    def analyze_file(self, file_path: str) -> Dict:
        """Analyze a Python file with AI assistance"""
        print(f"Analyzing {file_path}...")
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Parse AST for basic analysis
            tree = ast.parse(content)
            
            basic_analysis = {
                "file_path": file_path,
                "lines_of_code": len(content.splitlines()),
                "functions": len([node for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]),
                "classes": len([node for node in ast.walk(tree) if isinstance(node, ast.ClassDef)]),
                "imports": len([node for node in ast.walk(tree) if isinstance(node, (ast.Import, ast.ImportFrom))]),
                "complexity_indicators": self._analyze_complexity(tree),
                "docstrings": self._check_docstrings(tree)
            }
            
            # Get AI analysis
            ai_analysis = self._get_ai_code_analysis(content, file_path)
            
            return {
                **basic_analysis,
                "ai_insights": ai_analysis
            }
            
        except Exception as e:
            return {
                "file_path": file_path,
                "error": str(e),
                "ai_insights": f"Error analyzing file: {e}"
            }
    
    def _analyze_complexity(self, tree: ast.AST) -> Dict:
        """Analyze code complexity indicators"""
        complexity = {
            "nested_loops": 0,
            "nested_conditions": 0,
            "long_functions": 0,
            "large_classes": 0
        }
        
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                # Check for long functions
                if len(node.body) > 20:
                    complexity["long_functions"] += 1
                
                # Check for nested structures
                for child in ast.walk(node):
                    if isinstance(child, (ast.For, ast.While)):
                        # Count nested loops
                        parent_count = sum(1 for parent in ast.walk(node) 
                                          if isinstance(parent, (ast.For, ast.While)))
                        if parent_count > 1:
                            complexity["nested_loops"] += 1
                    elif isinstance(child, ast.If):
                        # Count nested conditions
                        parent_count = sum(1 for parent in ast.walk(node) 
                                          if isinstance(parent, ast.If))
                        if parent_count > 2:
                            complexity["nested_conditions"] += 1
            
            elif isinstance(node, ast.ClassDef):
                # Check for large classes
                if len(node.body) > 15:
                    complexity["large_classes"] += 1
        
        return complexity
    
    def _check_docstrings(self, tree: ast.AST) -> Dict:
        """Check for docstring coverage"""
        docstrings = {
            "functions_with_docs": 0,
            "functions_total": 0,
            "classes_with_docs": 0,
            "classes_total": 0,
            "module_has_docstring": False
        }
        
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                docstrings["functions_total"] += 1
                if (node.body and 
                    isinstance(node.body[0], ast.Expr) and 
                    isinstance(node.body[0].value, ast.Constant) and 
                    isinstance(node.body[0].value.value, str)):
                    docstrings["functions_with_docs"] += 1
            
            elif isinstance(node, ast.ClassDef):
                docstrings["classes_total"] += 1
                if (node.body and 
                    isinstance(node.body[0], ast.Expr) and 
                    isinstance(node.body[0].value, ast.Constant) and 
                    isinstance(node.body[0].value.value, str)):
                    docstrings["classes_with_docs"] += 1
        
        # Check module docstring (first statement in module)
        if (tree.body and 
            isinstance(tree.body[0], ast.Expr) and 
            isinstance(tree.body[0].value, ast.Constant) and 
            isinstance(tree.body[0].value.value, str)):
            docstrings["module_has_docstring"] = True
        
        return docstrings
    
    def _get_ai_code_analysis(self, code: str, file_path: str) -> str:
        """Get AI analysis of code from Perplexity"""
        prompt = f"""
        You are an expert Python code reviewer analyzing the HyperCode project.
        
        Please analyze this Python file ({file_path}) and provide:
        
        1. Code quality assessment (1-10 scale)
        2. Specific improvement suggestions
        3. Potential bugs or issues
        4. Best practices recommendations
        5. Neurodivergent-friendly code suggestions (clear naming, explicit logic, good documentation)
        
        Code to analyze:
        ```python
        {code[:2000]}  # Limit to first 2000 chars for context
        ```
        
        Provide specific, actionable feedback with line numbers where relevant.
        """
        
        response = self.perplexity.query(prompt)
        
        if "choices" in response and response["choices"]:
            return response["choices"][0]["message"]["content"]
        else:
            return "Failed to get AI analysis"
    
    def analyze_project(self, project_path: str = ".") -> Dict:
        """Analyze entire project"""
        print(f"Analyzing project at {project_path}...")
        
        project_path = Path(project_path)
        python_files = list(project_path.rglob("*.py"))
        
        # Skip certain directories
        python_files = [
            f for f in python_files 
            if not any(skip in str(f) for skip in ["__pycache__", ".git", "venv", "env"])
        ]
        
        analyses = []
        project_stats = {
            "total_files": len(python_files),
            "total_lines": 0,
            "total_functions": 0,
            "total_classes": 0,
            "files_with_errors": 0
        }
        
        for file_path in python_files:
            analysis = self.analyze_file(str(file_path))
            analyses.append(analysis)
            
            # Update project stats
            if "error" not in analysis:
                project_stats["total_lines"] += analysis["lines_of_code"]
                project_stats["total_functions"] += analysis["functions"]
                project_stats["total_classes"] += analysis["classes"]
            else:
                project_stats["files_with_errors"] += 1
        
        # Get project-level AI insights
        project_ai_insights = self._get_project_ai_insights(analyses, project_stats)
        
        return {
            "project_path": str(project_path),
            "project_stats": project_stats,
            "file_analyses": analyses,
            "ai_project_insights": project_ai_insights
        }
    
    def _get_project_ai_insights(self, analyses: List[Dict], stats: Dict) -> str:
        """Get AI insights for the entire project"""
        prompt = f"""
        You are an expert software architect reviewing the HyperCode project.
        
        Based on this project analysis, provide strategic recommendations:
        
        Project Statistics:
        - Total files: {stats['total_files']}
        - Total lines of code: {stats['total_lines']}
        - Total functions: {stats['total_functions']}
        - Total classes: {stats['total_classes']}
        - Files with errors: {stats['files_with_errors']}
        
        Key findings from file analyses:
        {json.dumps([a.get('ai_insights', 'No insights') for a in analyses[:5]], indent=2)[:1000]}
        
        Please provide:
        1. Overall project architecture assessment
        2. Code quality trends and patterns
        3. Recommendations for improving maintainability
        4. Suggestions for better neurodivergent-friendly code organization
        5. Priority areas for refactoring
        """
        
        response = self.perplexity.query(prompt)
        
        if "choices" in response and response["choices"]:
            return response["choices"][0]["message"]["content"]
        else:
            return "Failed to get project AI insights"
    
    def save_analysis(self, analysis: Dict, filename: str = "code_analysis_report.json"):
        """Save analysis to file"""
        with open(filename, 'w') as f:
            json.dump(analysis, f, indent=2)
        print(f"Code analysis saved to {filename}")
    
    def print_summary(self, analysis: Dict):
        """Print analysis summary"""
        print("\n" + "=" * 60)
        print("HYPERCODE CODE ANALYSIS SUMMARY")
        print("=" * 60)
        
        stats = analysis["project_stats"]
        print(f"Files analyzed: {stats['total_files']}")
        print(f"Total lines of code: {stats['total_lines']}")
        print(f"Total functions: {stats['total_functions']}")
        print(f"Total classes: {stats['total_classes']}")
        print(f"Files with errors: {stats['files_with_errors']}")
        
        print("\nPROJECT AI INSIGHTS:")
        print("-" * 40)
        print(analysis["ai_project_insights"])


def main():
    """Main function"""
    analyzer = CodeAnalyzerAI()
    
    # Analyze current project
    analysis = analyzer.analyze_project()
    
    # Save and display results
    analyzer.save_analysis(analysis)
    analyzer.print_summary(analysis)
    
    print(f"\n[SUCCESS] Code analysis completed!")


if __name__ == "__main__":
    main()
