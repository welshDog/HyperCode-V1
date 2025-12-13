#!/usr/bin/env python3
"""
Generate README.md files for documentation directories.
"""

from pathlib import Path


def create_readme(directory, content):
    """Create or update a README.md file with the given content."""
    readme_path = directory / "README.md"
    if not readme_path.exists():
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"✅ Created {readme_path}")
    else:
        print(f"ℹ️  {readme_path} already exists, skipping")


def main():
    base_dir = Path(__file__).parent.parent
    docs_dir = base_dir / "docs"

    # Define README content for each directory
    readme_contents = {
        "getting-started": """# Getting Started

This directory contains guides and resources to help you get started with HyperCode.

## What's Here

- **Installation guides** - How to set up HyperCode on your system
- **Quick start tutorials** - Get up and running quickly
- **First steps** - Your first HyperCode program
- **Development environment setup** - Configure your IDE and tools

## Next Steps

1. Check out the [installation guide](INSTALL.md)
2. Try the [quick start tutorial](quickstart-checklist.md)
3. Explore the [examples](../examples) directory
""",
        "guides": """# Guides

Step-by-step tutorials and how-to guides for HyperCode.

## Available Guides

- [AI Integration Guide](AI_INTEGRATION_GUIDE.md) - Connect with AI models
- [Troubleshooting](TROUBLESHOOTING.md) - Common issues and solutions
- [Build Guide](HyperCode-Build-Guide.md) - Building from source
- [GitHub Setup](GitHub-Setup-Guide.md) - Configure GitHub for development

## Contributing

Want to add a new guide? See our [contributing guidelines](../../CONTRIBUTING.md).
""",
        "reference": """# Reference Documentation

Technical reference for HyperCode's language features and APIs.

## Contents

- [Language Reference](LANGUAGE_REFERENCE.md) - Complete language specification
- [API Reference](API_REFERENCE.md) - Core library documentation
- [Design Patterns](Design_Patterns_Examples.md) - Common patterns and examples
- [Style Guide](STYLE_GUIDE_DRAFT.md) - Code style and conventions

## Quick Links

- [Syntax Cheatsheet](hypercode_syntax.md)
- [Visual Syntax Guide](hypercode_visual_syntax.md)
""",
        "concepts": """# Core Concepts

Deep dives into HyperCode's design philosophy and architecture.

## Key Topics

- [Vision & Mission](0-vision.md) - What is HyperCode and why it exists
- [Neurodivergent-First Design](HyperCode_NeuroFirst_Design.md)
- [Research Foundation](HyperCode-Research-Foundation.md)
- [Esoteric Language Influences](HyperCode_Esoteric_Study.md)

## Related

- [Roadmap](../roadmaps/1-roadmap.md) - Upcoming features and milestones
- [Architecture](../architecture/ARCHITECTURE.md) - System design overview
""",
        "roadmaps": """# Project Roadmaps

Planning and tracking for HyperCode's development.

## Current Focus

- [Active Roadmap](1-roadlog.md) - Current development priorities
- [Backlog](2-backlog.md) - Upcoming features and improvements
- [90-Day Plan](HyperCode-90day.md) - Short-term development goals

## Long-Term Planning

- [V3 Build Blueprint](HyperCode_V3_Build_Blueprint.md)
- [AI Optimization Roadmap](AI_OPTIMIZATION_ROADMAP.md)

## Contributing

See something you'd like to work on? Check our [contributing guidelines](../../CONTRIBUTING.md).
""",
        "architecture": """# System Architecture

Technical documentation of HyperCode's architecture and design decisions.

## Overview

- [Architecture Overview](ARCHITECTURE.md) - High-level system design
- [Implementation Guide](HyperCode_Implementation_Guide.md)
- [Knowledge Base Architecture](knowledge-base-architecture.md)

## Components

- Parser
- Compiler
- Runtime
- Standard Library

## Related

- [Core Concepts](../concepts/0-vision.md)
- [API Reference](../reference/API_REFERENCE.md)
""",
        "ai": """# AI Integration

Documentation for HyperCode's AI capabilities and integrations.

## Features

- AI-assisted code completion
- Natural language to code
- Code explanation and documentation
- Bug detection and fixes

## Guides

- [AI Integration Guide](AI_INTEGRATION_GUIDE.md)
- [AI Compatibility](AI_COMPAT.md)
- [DuelCore Deep Dive](AI_DUELCORE_DEEP_DIVE.md)

## Development

- [AI Optimization Roadmap](../roadmaps/AI_OPTIMIZATION_ROADMAP.md)
- [AI Upgrade Tasks](AI_UPGRADE_TASKS.md)
""",
        "database": """# Database Documentation

HyperCode's data storage and persistence layer.

## Contents

- [Database Setup](hyper-database-setup.md)
- [Integration Guide](hyper-database-integration.md)
- [Knowledge Base](knowledge-base.md)

## Related

- [API Reference](../reference/API_REFERENCE.md)
- [Architecture](../architecture/ARCHITECTURE.md)
""",
        "community": """# Community & Contribution

Resources for HyperCode contributors and community members.

## Getting Involved

- [Contributing Guidelines](CONTRIBUTING.md) - How to contribute
- [Bounties](BOUNTIES.md) - Earn rewards for contributions
- [FAQ](FAQ.md) - Common questions

## Project Information

- [Changelog](CHANGELOG.md)
- [Security Policy](SECURITY.md)
- [Code of Conduct](../../CODE_OF_CONDUCT.md)

## Connect

- [GitHub Discussions](https://github.com/welshDog/hypercode/discussions)
- [Report Issues](https://github.com/welshDog/hypercode/issues)
""",
    }

    # Create READMEs for each directory
    for dir_name, content in readme_contents.items():
        dir_path = docs_dir / dir_name
        if dir_path.exists():
            create_readme(dir_path, content)
        else:
            print(f"⚠️  Directory not found: {dir_path}")

    print("\n✅ All documentation READMEs have been generated")


if __name__ == "__main__":
    main()
