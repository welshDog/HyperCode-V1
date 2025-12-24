#!/usr/bin/env python3
"""
Research Data Organizer for HyperCode Project

This script organizes research JSON files by topic, standardizes naming,
and generates analysis and visualizations.
"""

import os
import sys
import json
import re
from datetime import datetime
from pathlib import Path
from collections import defaultdict
import matplotlib.pyplot as plt
from typing import Dict, List, Any, Optional

# Get the directory where this script is located
SCRIPT_DIR = Path(__file__).parent.absolute()
PROJECT_ROOT = SCRIPT_DIR.parents[1]  # Go up two levels to reach project root

# Configuration
RESEARCH_DIR = PROJECT_ROOT / "data" / "reseach data json"
OUTPUT_DIR = PROJECT_ROOT / "data" / "processed_research"
ANALYSIS_DIR = OUTPUT_DIR / "analysis"
VISUALIZATIONS_DIR = OUTPUT_DIR / "visualizations"

# Ensure output directories exist
for directory in [OUTPUT_DIR, ANALYSIS_DIR, VISUALIZATIONS_DIR]:
    directory.mkdir(parents=True, exist_ok=True)

def load_research_files() -> List[Dict[str, Any]]:
    """Load all JSON research files."""
    research_data = []
    for file_path in RESEARCH_DIR.glob("*.json"):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                data["file_name"] = file_path.name
                research_data.append(data)
        except (json.JSONDecodeError, UnicodeDecodeError) as e:
            print(f"Error loading {file_path}: {e}")
    return research_data

def organize_by_topic(research_data: List[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
    """Organize research data by topic."""
    topics = defaultdict(list)
    
    for item in research_data:
        # Extract topic from tags or generate from content
        if "tags" in item and item["tags"]:
            topic = item["tags"][0]  # Use first tag as topic
        elif "topic" in item:
            topic = str(item["topic"]).lower().replace(" ", "_")
        else:
            topic = "uncategorized"
        
        # Standardize naming
        topic = re.sub(r'[^a-z0-9_]', '', topic.lower())
        topics[topic].append(item)
    
    return dict(topics)

def save_organized_data(organized_data: Dict[str, List[Dict[str, Any]]]) -> None:
    """Save organized data to topic-based directories."""
    for topic, items in organized_data.items():
        topic_dir = OUTPUT_DIR / topic
        topic_dir.mkdir(exist_ok=True)
        
        for item in items:
            # Create standardized filename
            date = item.get("date", "0000-00-00")
            source = item.get("source", "unknown").lower().replace(" ", "_")
            source = re.sub(r'[^a-z0-9_]', '', source)
            
            # Create a unique identifier
            file_id = item.get("id", item.get("file_name", str(hash(str(item)))))
            
            # Save the file
            output_file = topic_dir / f"{date}_{source}_{file_id}.json"
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(item, f, indent=2, ensure_ascii=False)

def generate_research_summary(organized_data: Dict[str, List[Dict[str, Any]]]) -> str:
    """Generate a markdown summary of the research."""
    summary = "# HyperCode Research Summary\n\n"
    
    # General statistics
    total_files = sum(len(items) for items in organized_data.values())
    summary += f"## Overview\n"
    summary += f"- Total research items: {total_files}\n"
    summary += f"- Number of topics: {len(organized_data)}\n\n"
    
    # Summary by topic
    summary += "## Research by Topic\n"
    for topic, items in sorted(organized_data.items()):
        summary += f"### {topic.title().replace('_', ' ')}\n"
        summary += f"- Number of items: {len(items)}\n"
        
        # Get unique sources
        sources = set()
        for item in items:
            if "source" in item:
                sources.add(item["source"])
        
        if sources:
            summary += f"- Sources: {', '.join(sources)}\n"
        
        # Add a brief summary if available
        if items and "summary" in items[0]:
            summary += f"- Summary: {items[0]['summary']}\n"
        summary += "\n"
    
    # Save the summary
    with open(ANALYSIS_DIR / "research_summary.md", 'w', encoding='utf-8') as f:
        f.write(summary)
    
    return summary

def create_visualizations(organized_data: Dict[str, List[Dict[str, Any]]]) -> None:
    """Create visualizations of the research data."""
    # 1. Topics distribution
    topics = list(organized_data.keys())
    counts = [len(items) for items in organized_data.values()]
    
    plt.figure(figsize=(12, 6))
    plt.bar(topics, counts)
    plt.title("Research Items by Topic")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(VISUALIZATIONS_DIR / "topics_distribution.png")
    plt.close()
    
    # 2. Timeline of research
    dates = []
    for items in organized_data.values():
        for item in items:
            if "date" in item:
                try:
                    date = datetime.strptime(item["date"], "%Y-%m-%d")
                    dates.append(date)
                except (ValueError, TypeError):
                    continue
    
    if dates:
        plt.figure(figsize=(12, 6))
        plt.hist(dates, bins=20, color='skyblue', edgecolor='black')
        plt.title("Research Timeline")
        plt.xlabel("Date")
        plt.ylabel("Number of Items")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(VISUALIZATIONS_DIR / "research_timeline.png")
        plt.close()

def create_readme() -> None:
    """Create a README.md file for the research directory."""
    readme = """# HyperCode Research Data

This directory contains organized research data for the HyperCode project.

## Directory Structure

- `raw/`: Original research files (read-only)
- `processed/`: Cleaned and organized research data
  - `analysis/`: Generated analysis and summaries
  - `visualizations/`: Generated visualizations

## Usage

1. Browse the organized research by topic in the `processed` directory
2. Check the `analysis` directory for summaries and insights
3. View visualizations in the `visualizations` directory

## Adding New Research

1. Place new research JSON files in the `raw` directory
2. Run the research organizer script:
   ```bash
   python scripts/research_analysis/research_organizer.py
   ```
3. Commit the organized data and generated files
"""
    
    with open(OUTPUT_DIR / "README.md", 'w', encoding='utf-8') as f:
        f.write(readme)

def main():
    # Print paths for debugging
    print(f"Script directory: {SCRIPT_DIR}")
    print(f"Project root: {PROJECT_ROOT}")
    print(f"Research directory: {RESEARCH_DIR}")
    print(f"Output directory: {OUTPUT_DIR}")
    
    # Check if research directory exists
    if not RESEARCH_DIR.exists():
        print(f"Error: Research directory not found at {RESEARCH_DIR}")
        print("Please ensure the research data is in the correct location.")
        return
    
    # Count JSON files in research directory
    json_files = list(RESEARCH_DIR.glob("*.json"))
    print(f"Found {len(json_files)} JSON files in research directory")
    
    print("\nLoading research data...")
    research_data = load_research_files()
    print(f"Loaded {len(research_data)} research items")
    
    if not research_data:
        print("No research data loaded. Please check the input files and try again.")
        return
    
    print("\nOrganizing by topic...")
    organized_data = organize_by_topic(research_data)
    print(f"Organized into {len(organized_data)} topics")
    
    print("\nSaving organized data...")
    save_organized_data(organized_data)
    
    print("\nGenerating research summary...")
    summary = generate_research_summary(organized_data)
    print("\n" + summary)
    
    print("\nCreating visualizations...")
    create_visualizations(organized_data)
    
    print("\nCreating README...")
    create_readme()
    
    print(f"\nDone! Organized research data saved to: {OUTPUT_DIR}")
    print(f"- Research summary: {ANALYSIS_DIR / 'research_summary.md'}")
    print(f"- Visualizations: {VISUALIZATIONS_DIR}")

if __name__ == "__main__":
    main()
