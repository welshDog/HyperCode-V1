#!/bin/bash
# HyperCode-V1 Repository Structure Setup
# Run this from your repo root: bash setup_research_db.sh

set -e

echo "🚀 Setting up HyperCode Research Database..."
echo ""

# Create main research database structure
echo "📁 Creating directory structure..."
mkdir -p docs/research_db/_templates
mkdir -p docs/research_db/research/cognitive_science
mkdir -p docs/research_db/research/accessibility
mkdir -p docs/research_db/research/neurodivergent_ux
mkdir -p docs/research_db/research/language_comparisons
mkdir -p docs/research_db/design_decisions
mkdir -p docs/research_db/experiments/usability_tests
mkdir -p docs/research_db/experiments/pilots
mkdir -p docs/research_db/user_studies/interviews
mkdir -p docs/research_db/user_studies/surveys
mkdir -p docs/research_db/references/papers
mkdir -p docs/research_db/references/bibtex

# Create additional documentation structure
mkdir -p docs/architecture
mkdir -p docs/tutorials
mkdir -p docs/api

# Create .github workflows directory if it doesn't exist
mkdir -p .github/workflows

echo "✅ Directory structure created"
echo ""

# Create .gitkeep files to ensure empty directories are tracked
find docs/research_db -type d -empty -exec touch {}/.gitkeep \;

echo "📝 Creating placeholder files..."

# Create a basic .editorconfig if it doesn't exist
if [ ! -f .editorconfig ]; then
    cat > .editorconfig << 'EOF'
root = true

[*]
charset = utf-8
end_of_line = lf
insert_final_newline = true
trim_trailing_whitespace = true

[*.{md,markdown}]
trim_trailing_whitespace = false

[*.{yml,yaml}]
indent_style = space
indent_size = 2

[*.py]
indent_style = space
indent_size = 4
EOF
    echo "✅ Created .editorconfig"
fi

# Create requirements.txt for validation if it doesn't exist
if [ ! -f requirements-dev.txt ]; then
    cat > requirements-dev.txt << 'EOF'
# Development dependencies for HyperCode
pytest>=7.0.0
pytest-cov>=4.0.0
pyyaml>=6.0
black>=23.0.0
flake8>=6.0.0
mypy>=1.0.0
EOF
    echo "✅ Created requirements-dev.txt"
fi

echo ""
echo "🎉 Setup complete!"
echo ""
echo "Next steps:"
echo "1. Copy the schema, templates, and validation files (provided separately)"
echo "2. Run: python validate_research_db.py docs/research_db/"
echo "3. Review and customize the ADRs and research notes"
echo "4. Commit and push!"
echo ""
echo "Directory structure created:"
tree -L 3 docs/ 2>/dev/null || find docs/ -type d | sed 's|[^/]*/| |g'
