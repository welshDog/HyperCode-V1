# Script to organize the HyperCode repository

# Define paths
$root = "$PSScriptRoot\.."
$src = "$root\src"
$docs = "$root\docs"
$tests = "$root\tests"
$examples = "$root\examples"
$config = "$root\config"
$tools = "$root\tools"

# Create directories if they don't exist
@($src, $docs, $tests, $examples, $config, $tools) | ForEach-Object {
    if (-not (Test-Path $_)) { New-Item -ItemType Directory -Path $_ | Out-Null }
}

# Move documentation files
$docFiles = @("*.md", "*.txt", "*.rst")
$docFiles | ForEach-Object {
    Get-ChildItem -Path $root -Filter $_ -File | 
    Where-Object { $_.Name -notin @('README.md', 'CONTRIBUTING.md', 'CODE_OF_CONDUCT.md', 'LICENSE') } |
    Move-Item -Destination $docs -Force
}

# Move test files
Move-Item -Path "$root\test_*.py" -Destination $tests -ErrorAction SilentlyContinue

# Move example files
if (Test-Path "$root\showcase") {
    Move-Item -Path "$root\showcase\*" -Destination $examples -Force
    Remove-Item -Path "$root\showcase" -Recurse -Force
}

# Move config files
$configFiles = @("*.yaml", "*.yml", "*.json", "*.toml", "*.ini")
$configFiles | ForEach-Object {
    Get-ChildItem -Path $root -Filter $_ -File | 
    Where-Object { $_.Name -notin @('pyproject.toml', 'pytest.ini') } |
    Move-Item -Destination $config -Force
}

# Move tooling files
$toolFiles = @("*.ps1", "*.sh", "*.bat")
$toolFiles | ForEach-Object {
    Get-ChildItem -Path $root -Filter $_ -File | 
    Move-Item -Destination $tools -Force -ErrorAction SilentlyContinue
}

# Move source files
$srcDirs = @("hypercode-", "DuelCode", "ai_gateway", "spatial_visualizer")
$srcDirs | ForEach-Object {
    if (Test-Path "$root\$_") {
        Move-Item -Path "$root\$_\*" -Destination $src -Force -ErrorAction SilentlyContinue
        Remove-Item -Path "$root\$_" -Recurse -Force -ErrorAction SilentlyContinue
    }
}

# Clean up empty directories
Get-ChildItem -Path $root -Directory | 
    Where-Object { $_.GetFiles().Count -eq 0 -and $_.GetDirectories().Count -eq 0 } | 
    Remove-Item -Force -Recurse

Write-Host "Repository organization complete!" -ForegroundColor Green
