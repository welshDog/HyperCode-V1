# Script to organize files moved from 'need cleaning' folder

# Define paths
$root = "$PSScriptRoot\.."
$src = "$root\src"
$docs = "$root\docs"
$tests = "$root\tests"
$examples = "$root\examples"
$config = "$root\config"
$tools = "$root\tools"

# Create necessary directories if they don't exist
@("$src\ai_gateway", "$src\duelcode", "$src\spatial_visualizer", "$tests\unit", "$tests\integration") | ForEach-Object {
    if (-not (Test-Path $_)) { New-Item -ItemType Directory -Path $_ -Force | Out-Null }
}

# Move AI Gateway files
Move-Item -Path "$root\ai_gateway\*" -Destination "$src\ai_gateway\" -Force -ErrorAction SilentlyContinue

# Move DuelCode files
Move-Item -Path "$root\DuelCode\*" -Destination "$src\duelcode\" -Force -ErrorAction SilentlyContinue

# Move spatial visualizer files
Move-Item -Path "$root\spatial_visualizer\*" -Destination "$src\spatial_visualizer\" -Force -ErrorAction SilentlyContinue

# Move test files
$testFiles = @("test_*.py")
$testFiles | ForEach-Object {
    Get-ChildItem -Path $root -Filter $_ -File | Move-Item -Destination "$tests\unit\" -Force -ErrorAction SilentlyContinue
}

# Move documentation files
$docFiles = @("*.md", "*.txt")
$excludeFiles = @('README.md', 'CONTRIBUTING.md', 'CODE_OF_CONDUCT.md', 'LICENSE')

$docFiles | ForEach-Object {
    Get-ChildItem -Path $root -Filter $_ -File | 
    Where-Object { $_.Name -notin $excludeFiles } |
    Move-Item -Destination $docs -Force -ErrorAction SilentlyContinue
}

# Move config files
$configFiles = @("*.yaml", "*.yml", "*.json", "*.toml")
$configFiles | ForEach-Object {
    Get-ChildItem -Path $root -Filter $_ -File | 
    Where-Object { $_.Name -notin @('pyproject.toml', 'pytest.ini') } |
    Move-Item -Destination $config -Force -ErrorAction SilentlyContinue
}

# Move script files
$scriptFiles = @("*.ps1", "*.sh", "*.bat")
$scriptFiles | ForEach-Object {
    Get-ChildItem -Path $root -Filter $_ -File | 
    Move-Item -Destination $tools -Force -ErrorAction SilentlyContinue
}

# Move Python files to utils
Get-ChildItem -Path $root -Filter "*.py" -File | 
    Where-Object { $_.Name -notlike "test_*" } |
    Move-Item -Destination "$src\utils\" -Force -ErrorAction SilentlyContinue

# Clean up empty directories
Get-ChildItem -Path $root -Directory | 
    Where-Object { $_.GetFiles().Count -eq 0 -and $_.GetDirectories().Count -eq 0 } | 
    Remove-Item -Force -Recurse -ErrorAction SilentlyContinue

Write-Host "Files have been organized successfully!" -ForegroundColor Green
