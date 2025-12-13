#!/bin/bash

# Deploy HyperCode Playground to GitHub Pages
# Usage: ./deploy.sh

echo "🚀 Deploying HyperCode Playground to GitHub Pages..."

# Check if we're in the right directory
if [ ! -f "index.html" ]; then
    echo "❌ Error: index.html not found. Run this from the web-playground directory."
    exit 1
fi

# Create a temporary gh-pages branch if it doesn't exist
git checkout --orphan gh-pages 2>/dev/null || git checkout gh-pages

# Remove all files except our playground files
git rm -rf . 2>/dev/null || true

# Copy only the necessary files
cp index.html README.md ./

# Create .nojekyll file
touch .nojekyll

# Add and commit
git add .
git commit -m "Deploy HyperCode Playground to GitHub Pages"

# Push to GitHub
git push origin gh-pages --force

echo "✅ Playground deployed!"
echo "🌐 Visit: https://welshdog.github.io/hypercode/web-playground/"
echo ""
echo "To enable GitHub Pages:"
echo "1. Go to https://github.com/welshDog/hypercode/settings/pages"
echo "2. Select 'Deploy from a branch'"
echo "3. Choose 'gh-pages' branch and '/' folder"
echo "4. Click Save"

# Return to main branch
git checkout main
