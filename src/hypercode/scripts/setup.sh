#!/bin/bash

# 🧠 HyperCode Research Database Setup Script
# Neurodivergent-friendly installation with clear feedback

set -e  # Exit on any error

# Colors for clear visual feedback
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
PURPLE='\033[0;35m'
NC='\033[0m' # No Color

# Clear, emoji-based output functions
print_header() {
    echo -e "${PURPLE}"
    echo "┌──────────────────────────────────────────────────┐"
    echo "│  🧠 HyperCode Research Database Setup    │"
    echo "└──────────────────────────────────────────────────┘"
    echo -e "${NC}"
}

print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_info() {
    echo -e "${BLUE}📌 $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

print_step() {
    echo -e "${PURPLE}🔹 $1${NC}"
}

# Check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Main setup function
main() {
    print_header
    
    echo ""
    print_info "This script will set up your local HyperCode Research environment."
    print_info "It will check dependencies and configure your workspace."
    echo ""
    
    # Step 1: Check Git
    print_step "Step 1/5: Checking Git installation..."
    if command_exists git; then
        GIT_VERSION=$(git --version | cut -d' ' -f3)
        print_success "Git is installed (version $GIT_VERSION)"
    else
        print_error "Git is not installed. Please install Git first."
        print_info "Visit: https://git-scm.com/downloads"
        exit 1
    fi
    echo ""
    
    # Step 2: Check Python (optional for research scripts)
    print_step "Step 2/5: Checking Python installation..."
    if command_exists python3; then
        PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
        print_success "Python 3 is installed (version $PYTHON_VERSION)"
    else
        print_warning "Python 3 is not installed (optional for AI research scripts)"
        print_info "To install: Visit https://www.python.org/downloads/"
    fi
    echo ""
    
    # Step 3: Check Node.js (optional for visualization tools)
    print_step "Step 3/5: Checking Node.js installation..."
    if command_exists node; then
        NODE_VERSION=$(node --version)
        print_success "Node.js is installed (version $NODE_VERSION)"
    else
        print_warning "Node.js is not installed (optional for research visualizations)"
        print_info "To install: Visit https://nodejs.org/"
    fi
    echo ""
    
    # Step 4: Clone or update repository
    print_step "Step 4/5: Setting up repository..."
    if [ -d ".git" ]; then
        print_info "Repository already exists. Pulling latest changes..."
        git pull origin main
        print_success "Repository updated to latest version"
    else
        print_info "Cloning HyperCode Research Database..."
        git clone https://github.com/welshDog/hypercode-research.git .
        print_success "Repository cloned successfully"
    fi
    echo ""
    
    # Step 5: Setup complete
    print_step "Step 5/5: Finalizing setup..."
    
    # Create local research workspace if it doesn't exist
    if [ ! -d "workspace" ]; then
        mkdir -p workspace
        print_success "Created local workspace directory"
    fi
    
    # Install Python dependencies if requirements.txt exists
    if [ -f "requirements.txt" ] && command_exists pip3; then
        print_info "Installing Python dependencies..."
        pip3 install -r requirements.txt --quiet
        print_success "Python dependencies installed"
    fi
    
    # Install Node dependencies if package.json exists
    if [ -f "package.json" ] && command_exists npm; then
        print_info "Installing Node.js dependencies..."
        npm install --silent
        print_success "Node.js dependencies installed"
    fi
    
    echo ""
    echo -e "${PURPLE}──────────────────────────────────────────────────${NC}"
    print_success "Setup complete! You're ready to contribute research."
    echo ""
    
    print_info "Next steps:"
    echo "  1. Read the documentation: cat README.md"
    echo "  2. Check contribution guidelines: cat CONTRIBUTING.md"
    echo "  3. Browse research topics: ls docs/"
    echo "  4. Start contributing your research!"
    echo ""
    
    print_info "Quick links:"
    echo "  📚 Documentation: https://github.com/welshDog/hypercode-research"
    echo "  🤝 Contributing: https://github.com/welshDog/hypercode-research/blob/main/CONTRIBUTING.md"
    echo "  💬 Discussions: https://github.com/welshDog/hypercode-research/discussions"
    echo ""
    
    echo -e "${PURPLE}💜 Every forgotten language matters. Every neurodivergent perspective counts.${NC}"
    echo ""
}

# Run main function
main "$@"
