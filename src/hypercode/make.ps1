<# 
.SYNOPSIS
    Hypercode project build and test script for Windows

.DESCRIPTION
    This script provides similar functionality to the Makefile but works natively in PowerShell.
#>

param(
    [Parameter(Position=0)]
    [ValidateSet("install", "test", "test-cov", "lint", "format", "typecheck", "clean", "dev-setup", "help")]
    [string]$Command = "help"
)

function Show-Help {
    Write-Host @"
Available commands:

  .\make.ps1 install     - Install development dependencies
  .\make.ps1 test        - Run unit tests
  .\make.ps1 test-cov    - Run tests with coverage reporting
  .\make.ps1 lint        - Run code linters
  .\make.ps1 format      - Format code
  .\make.ps1 typecheck   - Run type checking
  .\make.ps1 clean       - Clean temporary files
  .\make.ps1 dev-setup   - Set up development environment (install + test + lint + typecheck)
  .\make.ps1 help        - Show this help message
"@
}

function Invoke-Install {
    Write-Host "Installing dependencies..." -ForegroundColor Green
    pip install -e ".[dev]"
}

function Invoke-Test {
    Write-Host "Running tests..." -ForegroundColor Green
    python -m pytest tests/ -v
}

function Invoke-TestWithCoverage {
    Write-Host "Running tests with coverage..." -ForegroundColor Green
    python -m pytest tests/ --cov=hypercode --cov-report=term-missing --cov-report=xml:coverage.xml --cov-report=html:htmlcov
}

function Invoke-Lint {
    Write-Host "Running linters..." -ForegroundColor Green
    flake8 hypercode/ tests/
    black --check hypercode/ tests/
    isort --check-only hypercode/ tests/
}

function Invoke-Format {
    Write-Host "Formatting code..." -ForegroundColor Green
    black hypercode/ tests/
    isort hypercode/ tests/
}

function Invoke-TypeCheck {
    Write-Host "Running type checking..." -ForegroundColor Green
    mypy hypercode/ tests/
}

function Invoke-Clean {
    Write-Host "Cleaning up..." -ForegroundColor Green
    Get-ChildItem -Path . -Include "*.pyc" -Recurse | Remove-Item -Force
    Get-ChildItem -Path . -Include "__pycache__" -Directory -Recurse | Remove-Item -Recurse -Force
    
    $dirsToClean = @("build", "dist", ".pytest_cache", ".mypy_cache", "htmlcov", ".coverage", "coverage.xml")
    foreach ($dir in $dirsToClean) {
        if (Test-Path $dir) {
            Remove-Item -Path $dir -Recurse -Force
        }
    }
}

function Invoke-DevSetup {
    Invoke-Install
    Invoke-TestWithCoverage
    Invoke-Lint
    Invoke-TypeCheck
}

# Main script execution
switch ($Command) {
    "install"    { Invoke-Install }
    "test"       { Invoke-Test }
    "test-cov"   { Invoke-TestWithCoverage }
    "lint"       { Invoke-Lint }
    "format"     { Invoke-Format }
    "typecheck"  { Invoke-TypeCheck }
    "clean"      { Invoke-Clean }
    "dev-setup"  { Invoke-DevSetup }
    "help"       { Show-Help }
    default      { Show-Help }
}