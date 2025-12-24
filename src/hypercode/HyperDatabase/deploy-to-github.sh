#!/bin/bash

###############################################################################
# HyperCode Research Database - GitHub Push Script
# Run this to deploy everything to GitHub in one go!
# 
# Usage: bash deploy-to-github.sh "YOUR_GITHUB_USERNAME"
# 
# Prerequisites:
# - Git installed
# - GitHub account created
# - GitHub CLI installed (optional, makes it easier)
###############################################################################

set -e  # Exit on error

echo "🚀 HyperCode Research Database - GitHub Deployment"
echo "=================================================="
echo ""

# Check if username provided
if [ -z "$1" ]; then
  echo "❌ Usage: bash deploy-to-github.sh YOUR_GITHUB_USERNAME"
  echo ""
  echo "Example: bash deploy-to-github.sh johndoe"
  exit 1
fi

USERNAME=$1
REPO_NAME="hypercode-research-db"
REPO_URL="https://github.com/$USERNAME/$REPO_NAME.git"

echo "📋 Configuration:"
echo "  GitHub Username: $USERNAME"
echo "  Repository: $REPO_NAME"
echo "  URL: $REPO_URL"
echo ""

# Step 1: Check Git installation
echo "✓ Step 1: Checking Git installation..."
if ! command -v git &> /dev/null; then
  echo "❌ Git is not installed. Install from: https://git-scm.com/download"
  exit 1
fi
echo "  ✅ Git version: $(git --version)"
echo ""

# Step 2: Initialize Git (if not already)
echo "✓ Step 2: Initializing Git repository..."
if [ ! -d ".git" ]; then
  git init
  echo "  ✅ Repository initialized"
else
  echo "  ✅ Repository already exists"
fi
echo ""

# Step 3: Configure Git user (if not already set)
echo "✓ Step 3: Configuring Git user..."
if [ -z "$(git config user.name)" ]; then
  read -p "  Enter your name: " GIT_NAME
  git config user.name "$GIT_NAME"
fi

if [ -z "$(git config user.email)" ]; then
  read -p "  Enter your email: " GIT_EMAIL
  git config user.email "$GIT_EMAIL"
fi
echo "  ✅ Git user configured"
echo ""

# Step 4: Create necessary files if they don't exist
echo "✓ Step 4: Checking required files..."
REQUIRED_FILES=(
  "hypercode_db.json"
  "hypercode_schema.json"
  "package.json"
  "README.md"
  ".gitignore"
)

for file in "${REQUIRED_FILES[@]}"; do
  if [ -f "$file" ]; then
    echo "  ✅ $file"
  else
    echo "  ⚠️  $file (MISSING - Please create this file)"
  fi
done
echo ""

# Step 5: Create scripts directory and files
echo "✓ Step 5: Organizing scripts..."
mkdir -p scripts .github/workflows docs

if [ -f "validate.js" ] && [ ! -f "scripts/validate.js" ]; then
  mv validate.js scripts/
  echo "  ✅ Moved validate.js to scripts/"
fi

if [ -f "sync-firebase.js" ] && [ ! -f "scripts/sync-firebase.js" ]; then
  mv sync-firebase.js scripts/
  echo "  ✅ Moved sync-firebase.js to scripts/"
fi

if [ -f "version-bump.js" ] && [ ! -f "scripts/version-bump.js" ]; then
  mv version-bump.js scripts/
  echo "  ✅ Moved version-bump.js to scripts/"
fi

if [ -f "update-timestamp.js" ] && [ ! -f "scripts/update-timestamp.js" ]; then
  mv update-timestamp.js scripts/
  echo "  ✅ Moved update-timestamp.js to scripts/"
fi

if [ -f "resolve-conflicts.js" ] && [ ! -f "scripts/resolve-conflicts.js" ]; then
  mv resolve-conflicts.js scripts/
  echo "  ✅ Moved resolve-conflicts.js to scripts/"
fi

if [ -f "sync_workflow.yml" ] && [ ! -f ".github/workflows/sync.yml" ]; then
  mv sync_workflow.yml .github/workflows/sync.yml
  echo "  ✅ Moved sync_workflow.yml to .github/workflows/"
fi
echo ""

# Step 6: Create LICENSE file
echo "✓ Step 6: Creating LICENSE file..."
if [ ! -f "LICENSE" ]; then
  cat > LICENSE << 'EOF'
MIT License

Copyright (c) 2025 HyperCode Contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
EOF
  echo "  ✅ LICENSE file created (MIT)"
else
  echo "  ✅ LICENSE file already exists"
fi
echo ""

# Step 7: Create CONTRIBUTING.md
echo "✓ Step 7: Creating CONTRIBUTING.md..."
if [ ! -f "CONTRIBUTING.md" ]; then
  cat > CONTRIBUTING.md << 'EOF'
# Contributing to HyperCode Research Database

We welcome contributions from neurodivergent programmers, AI researchers, quantum computing enthusiasts, and everyone!

## How to Contribute

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feat/your-feature`
3. **Edit** hypercode_db.json or other files
4. **Validate**: `npm run validate` ✅
5. **Commit** with clear message: `git commit -m "feat: description [schema:2025-12]"`
6. **Push**: `git push origin feat/your-feature`
7. **Open PR** on GitHub

## Commit Message Format

```
feat: add quantum computing feature [schema:2025-12]
fix: correct neurodivergent description
chore: update freshness metrics
docs: clarify AI integration
```

## Before Pushing

```bash
npm install
npm run validate        # Schema + quality checks
npm run schema-check   # Quick schema only
npm run dev           # Full pipeline
```

## Questions?

- Open an issue for bugs
- Start a discussion on GitHub
- Join our community

---

"Programming languages express how minds think." — HyperCode Manifesto
EOF
  echo "  ✅ CONTRIBUTING.md created"
else
  echo "  ✅ CONTRIBUTING.md already exists"
fi
echo ""

# Step 8: Create docs/SETUP.md
echo "✓ Step 8: Creating docs/SETUP.md..."
mkdir -p docs
if [ ! -f "docs/SETUP.md" ]; then
  cat > docs/SETUP.md << 'EOF'
# HyperCode Research Database - Setup Guide

## Quick Start (5 minutes)

### Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/hypercode-research-db.git
cd hypercode-research-db
```

### Install Dependencies
```bash
npm install
```

### Validate Your Setup
```bash
npm run validate
```

Expected output:
```
✅ Schema validation PASSED
✅ All required fields present
📊 Data quality metrics...
✅ ALL VALIDATIONS PASSED!
```

## Development Workflow

### Make Changes
Edit `hypercode_db.json` with your research updates.

### Validate Locally
```bash
npm run validate
```

### Commit & Push
```bash
git add hypercode_db.json
git commit -m "feat: add new research findings [schema:2025-12]"
git push origin main
```

### Watch CI/CD
Go to **Actions** tab → See automatic validation! ✅

For more details, see [README.md](../README.md)
EOF
  echo "  ✅ docs/SETUP.md created"
else
  echo "  ✅ docs/SETUP.md already exists"
fi
echo ""

# Step 9: Stage all files
echo "✓ Step 9: Staging files for commit..."
git add .
STAGED=$(git status --porcelain | wc -l)
echo "  ✅ Staged $STAGED files"
echo ""

# Step 10: Create initial commit
echo "✓ Step 10: Creating initial commit..."
if [ -z "$(git log --oneline 2>/dev/null)" ]; then
  git commit -m "feat: initialize HyperCode research database

- Neurodivergent-first programming language research
- Historical roots: Plankalkül, Brainfuck, Befunge
- AI compatibility: GPT-4, Claude, Mistral, Ollama
- Quantum/molecular computing integration
- Automated schema validation and CI/CD
- Multi-device synchronization ready
- Professional DevOps from day one

[schema:2025-12-v1.0.0]"
  echo "  ✅ Initial commit created"
else
  echo "  ⚠️  Repository already has commits"
fi
echo ""

# Step 11: Set up remote
echo "✓ Step 11: Setting up GitHub remote..."

# Remove existing origin if present
git remote remove origin 2>/dev/null || true

git remote add origin "$REPO_URL"
echo "  ✅ Remote added: $REPO_URL"
echo ""

# Step 12: Configure main branch
echo "✓ Step 12: Configuring main branch..."
git branch -M main
echo "  ✅ Branch set to: main"
echo ""

# Step 13: Check if repo exists on GitHub
echo "✓ Step 13: Checking GitHub repository..."
echo ""
echo "  ⚠️  MANUAL STEP REQUIRED:"
echo ""
echo "    1. Go to: https://github.com/new"
echo "    2. Create repository with these settings:"
echo "       - Name: $REPO_NAME"
echo "       - Visibility: Public"
echo "       - DON'T initialize with README/gitignore/license"
echo ""
echo "    3. After creating, return here and press ENTER to continue"
read -p "  Press ENTER when repository is created on GitHub... "
echo ""

# Step 14: Push to GitHub
echo "✓ Step 14: Pushing to GitHub..."
echo "  (This may prompt you for authentication)"
echo ""

if git push -u origin main; then
  echo ""
  echo "  ✅ Successfully pushed to GitHub!"
else
  echo ""
  echo "  ❌ Push failed. Check your credentials and try:"
  echo "     git push -u origin main"
  exit 1
fi
echo ""

# Step 15: Success!
echo "=================================================="
echo "✅ DEPLOYMENT COMPLETE!"
echo "=================================================="
echo ""
echo "📊 Your repository is now LIVE:"
echo "   $REPO_URL"
echo ""
echo "🎯 Next Steps:"
echo "   1. Go to your repository on GitHub"
echo "   2. Settings → Secrets and variables → Actions"
echo "   3. Add FIREBASE_PROJECT and FIREBASE_KEY (optional)"
echo "   4. Go to Actions tab → Enable workflows"
echo "   5. Push a test change to trigger CI/CD"
echo ""
echo "🚀 To test locally:"
echo "   npm install"
echo "   npm run validate"
echo "   npm run dev"
echo ""
echo "📢 Share your repository:"
echo "   \"Building HyperCode - a programming language FOR neurodivergent brains\""
echo "   \"Star us on GitHub: $REPO_URL\""
echo ""
echo "=================================================="
echo "The future is NOW. Let's GOOOOO! 🌍👊💓"
echo "=================================================="
