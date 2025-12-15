#!/bin/bash

# HyperCode Installation Script
# One-liner installer for macOS and Linux

set -e

echo "🚀 Installing HyperCode..."
echo ""

# Check if Python 3.10+ is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.10 or higher first."
    exit 1
fi

# Check Python version
PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
REQUIRED_VERSION="3.10"

if [ "$(printf '%s\n' "$REQUIRED_VERSION" "$PYTHON_VERSION" | sort -V | head -n1)" != "$REQUIRED_VERSION" ]; then
    echo "❌ Python $PYTHON_VERSION found, but HyperCode requires Python $REQUIRED_VERSION or higher."
    exit 1
fi

echo "✅ Python $PYTHON_VERSION detected"
echo ""

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo "❌ Git is not installed. Please install git first."
    exit 1
fi

echo "📦 Cloning HyperCode repository..."

# Clone if not already in hypercode directory
if [ ! -d "hypercode" ]; then
    git clone https://github.com/welshDog/hypercode.git
    cd hypercode
else
    cd hypercode
    git pull origin main
fi

echo "✅ Repository ready"
echo ""

echo "📦 Installing dependencies..."
pip3 install -r requirements.lock

echo ""
echo "✅ HyperCode installed successfully!"
echo ""
echo "🎯 Quick Start:"
echo "   cd hypercode"
echo "   python3 -m src.hypercode examples/demo_hello.hc"
echo ""
echo "📖 Documentation: https://github.com/welshDog/hypercode/blob/main/docs/"
echo "💬 Discussions: https://github.com/welshDog/hypercode/discussions"
echo ""
echo "🚀 Happy coding with HyperCode!"
  
