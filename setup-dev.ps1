<#
.SYNOPSIS
    Sets up the HyperCode development environment.
.DESCRIPTION
    This script automates the setup of the HyperCode development environment,
    including virtual environment creation, package installation, and configuration.
#>

# Stop on first error
$ErrorActionPreference = "Stop"

# Configuration
$VENV_NAME = "hypercode_venv"
$VENV_PATH = Join-Path $env:USERPROFILE $VENV_NAME
$REQUIREMENTS = @"
# Core Dependencies
pytest>=7.0.0
pytest-cov>=3.0.0
black>=22.0.0
isort>=5.10.0
mypy>=0.910
flake8>=4.0.0
pre-commit>=2.17.0
lark-parser>=0.11.0
sphinx>=5.0.0
sphinx-rtd-theme>=1.0.0
"@

function Write-Header {
    param([string]$message)
    Write-Host "`n" + ("=" * 80) -ForegroundColor Cyan
    Write-Host "  $message" -ForegroundColor Cyan
    Write-Host ("=" * 80) + "`n" -ForegroundColor Cyan
}

function Test-Command {
    param([string]$command)
    try {
        $null = Get-Command $command -ErrorAction Stop
        return $true
    } catch {
        return $false
    }
}

function Test-Admin {
    $identity = [Security.Principal.WindowsIdentity]::GetCurrent()
    $principal = New-Object Security.Principal.WindowsPrincipal($identity)
    return $principal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
}

function Initialize-Environment {
    Write-Header "1. Checking System Requirements"
    
    # Check Python version
    $pythonVersion = (python --version 2>&1).ToString().Split()[-1]
    if (-not $pythonVersion) {
        throw "Python is not installed or not in PATH. Please install Python 3.8 or higher."
    }
    
    $majorVersion = [int]$pythonVersion.Split('.')[0]
    $minorVersion = [int]$pythonVersion.Split('.')[1]
    
    if ($majorVersion -lt 3 -or ($majorVersion -eq 3 -and $minorVersion -lt 8)) {
        throw "Python 3.8 or higher is required. Found Python $pythonVersion"
    }
    
    Write-Host "✓ Python $pythonVersion is installed" -ForegroundColor Green
    
    # Check for git
    if (-not (Test-Command "git")) {
        Write-Warning "Git is not installed. Some features may be limited."
    } else {
        Write-Host "✓ Git is installed" -ForegroundColor Green
    }
    
    # Create project structure
    $directories = @(
        "docs",
        "docs/images",
        "examples/01-hello-world",
        "examples/02-data-pipeline",
        "examples/03-api-integration",
        "examples/04-spatial-game",
        "examples/05-ai-integration",
        "spec",
        "experiments/quantum-ops",
        "experiments/dna-syntax",
        "src/parser",
        "src/interpreter",
        "src/stdlib",
        "tests"
    )
    
    foreach ($dir in $directories) {
        $fullPath = Join-Path $PSScriptRoot $dir
        if (-not (Test-Path $fullPath)) {
            New-Item -ItemType Directory -Path $fullPath -Force | Out-Null
            Write-Host "✓ Created directory: $dir" -ForegroundColor Green
        }
    }
}

function Initialize-VirtualEnvironment {
    Write-Header "2. Setting Up Virtual Environment"
    
    # Clean up any existing environment
    if (Test-Path $VENV_PATH) {
        Write-Host "Removing existing virtual environment..."
        Remove-Item -Recurse -Force $VENV_PATH -ErrorAction SilentlyContinue
    }
    
    # Create new virtual environment
    Write-Host "Creating virtual environment at $VENV_PATH..."
    python -m venv $VENV_PATH
    
    if (-not $?) {
        throw "Failed to create virtual environment. Please check your Python installation."
    }
    
    # Activate the virtual environment
    $activateScript = Join-Path $VENV_PATH "Scripts\Activate.ps1"
    . $activateScript
    
    if (-not $?) {
        throw "Failed to activate virtual environment."
    }
    
    Write-Host "✓ Virtual environment created and activated" -ForegroundColor Green
    
    # Upgrade pip
    Write-Host "Upgrading pip..."
    python -m pip install --upgrade pip
    
    # Install requirements
    Write-Host "Installing development dependencies..."
    $REQUIREMENTS | Out-File -FilePath (Join-Path $PSScriptRoot "requirements-dev.txt") -Force
    python -m pip install -r (Join-Path $PSScriptRoot "requirements-dev.txt")
    
    if (-not $?) {
        throw "Failed to install development dependencies."
    }
    
    Write-Host "✓ Dependencies installed" -ForegroundColor Green
}

function Initialize-Project {
    Write-Header "3. Configuring Project"
    
    # Create setup.py if it doesn't exist
    $setupPyPath = Join-Path $PSScriptRoot "setup.py"
    if (-not (Test-Path $setupPyPath)) {
        @"
from setuptools import setup, find_packages

setup(
    name="hypercode",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.8",
    install_requires=[],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "black>=22.0.0",
            "isort>=5.10.0",
            "mypy>=0.910",
            "flake8>=4.0.0",
            "pre-commit>=2.17.0",
            "lark-parser>=0.11.0",
            "sphinx>=5.0.0",
            "sphinx-rtd-theme>=1.0.0",
        ]
    }
)
"@ | Out-File -FilePath $setupPyPath -Force
        Write-Host "✓ Created setup.py" -ForegroundColor Green
    }
    
    # Install package in development mode
    Write-Host "Installing package in development mode..."
    python -m pip install -e .
    
    # Initialize pre-commit
    if (Test-Command "pre-commit") {
        Write-Host "Setting up pre-commit hooks..."
        pre-commit install
        Write-Host "✓ Pre-commit hooks installed" -ForegroundColor Green
    }
    
    # Create .gitignore if it doesn't exist
    $gitignorePath = Join-Path $PSScriptRoot ".gitignore"
    if (-not (Test-Path $gitignorePath)) {
        @"
# Virtual Environment
$VENV_NAME/
venv/
ENV/

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# IDE
.vscode/
.idea/
*.swp
*.swo

# Logs
logs/
*.log

# Local development
.DS_Store
Thumbs.db
"@ | Out-File -FilePath $gitignorePath -Force
        Write-Host "✓ Created .gitignore" -ForegroundColor Green
    }
}

function Complete-Setup {
    Write-Header "Setup Complete!"
    
    Write-Host "🎉 HyperCode development environment is ready!" -ForegroundColor Green
    Write-Host ""
    Write-Host "To activate the virtual environment in a new terminal, run:" -ForegroundColor Cyan
    Write-Host "    .\$VENV_PATH\Scripts\Activate.ps1" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Available commands:" -ForegroundColor Cyan
    Write-Host "    pytest        - Run tests" -ForegroundColor Yellow
    Write-Host "    black .       - Format code" -ForegroundColor Yellow
    Write-Host "    isort .       - Sort imports" -ForegroundColor Yellow
    Write-Host "    flake8        - Lint code" -ForegroundColor Yellow
    Write-Host "    pre-commit run --all-files  - Run all pre-commit hooks" -ForegroundColor Yellow
    Write-Host ""
}

# Main execution
try {
    Write-Header "🚀 HyperCode Development Environment Setup"
    
    # Check if running as admin (not required, but good to know)
    if (Test-Admin) {
        Write-Host "Running as Administrator" -ForegroundColor Yellow
    } else {
        Write-Host "Running as standard user" -ForegroundColor Yellow
    }
    
    # Change to script directory
    Push-Location $PSScriptRoot
    
    # Run setup steps
    Initialize-Environment
    Initialize-VirtualEnvironment
    Initialize-Project
    Complete-Setup
    
} catch {
    Write-Host "❌ Error: $_" -ForegroundColor Red
    exit 1
} finally {
    Pop-Location
}