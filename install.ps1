# HyperCode Installation Script for Windows
# PowerShell one-liner installer

$ErrorActionPreference = "Stop"

Write-Host "🚀 Installing HyperCode..." -ForegroundColor Cyan
Write-Host ""

# Check if Python 3.10+ is installed
try {
    $pythonVersion = python --version 2>&1 | Select-String "Python (\d+\.\d+)"
    if ($pythonVersion) {
        $version = [version]$pythonVersion.Matches.Groups[1].Value
        $requiredVersion = [version]"3.10"
        
        if ($version -lt $requiredVersion) {
            Write-Host "❌ Python $version found, but HyperCode requires Python 3.10 or higher." -ForegroundColor Red
            exit 1
        }
        Write-Host "✅ Python $version detected" -ForegroundColor Green
    } else {
        throw "Python version not detected"
    }
} catch {
    Write-Host "❌ Python 3 is not installed. Please install Python 3.10 or higher first." -ForegroundColor Red
    Write-Host "Download from: https://www.python.org/downloads/" -ForegroundColor Yellow
    exit 1
}

Write-Host ""

# Check if git is installed
try {
    git --version | Out-Null
} catch {
    Write-Host "❌ Git is not installed. Please install git first." -ForegroundColor Red
    Write-Host "Download from: https://git-scm.com/download/win" -ForegroundColor Yellow
    exit 1
}

Write-Host "📦 Cloning HyperCode repository..." -ForegroundColor Cyan

# Clone if not already in hypercode directory
if (-Not (Test-Path "hypercode")) {
    git clone https://github.com/welshDog/hypercode.git
    Set-Location hypercode
} else {
    Set-Location hypercode
    git pull origin main
}

Write-Host "✅ Repository ready" -ForegroundColor Green
Write-Host ""

Write-Host "📦 Installing dependencies..." -ForegroundColor Cyan
python -m pip install -r requirements.lock

Write-Host ""
Write-Host "✅ HyperCode installed successfully!" -ForegroundColor Green
Write-Host ""
Write-Host "🎯 Quick Start:" -ForegroundColor Yellow
Write-Host "   cd hypercode" -ForegroundColor White
Write-Host "   python -m src.hypercode examples/demo_hello.hc" -ForegroundColor White
Write-Host ""
Write-Host "📖 Documentation: https://github.com/welshDog/hypercode/blob/main/docs/" -ForegroundColor Cyan
Write-Host "💬 Discussions: https://github.com/welshDog/hypercode/discussions" -ForegroundColor Cyan
Write-Host ""
Write-Host "🚀 Happy coding with HyperCode!" -ForegroundColor Magenta
