# HyperCode V1 Phase 1 Cleanup
Write-Host "🚀 Starting HyperCode V1 Cleanup" -ForegroundColor Cyan

# Set error action preference
$ErrorActionPreference = "Stop"

# 1. Remove problematic files
$filesToRemove = @(
    "to-do list",
    "🔥 ALL-IN DEPLOY - LET'S GO RIGHT NOW 🚀",
    "e -Force .hypercode",
    "add more Ai likes",
    "data analyze"
)

Write-Host "`n🧹 Removing problematic files..." -ForegroundColor Yellow
foreach ($file in $filesToRemove) {
    $path = Join-Path "hypercode_organized_v2" $file
    if (Test-Path $path) {
        Remove-Item -Path $path -Force -Recurse -ErrorAction SilentlyContinue
        Write-Host "  ✓ Removed: $file" -ForegroundColor Green
    }
}

# 2. Create necessary directories
$dirsToCreate = @(
    "data/processed",
    "config",
    "scripts",
    "database",
    "docs"
)

Write-Host "`n📂 Organizing files into proper directories..." -ForegroundColor Yellow
foreach ($dir in $dirsToCreate) {
    $fullPath = Join-Path "hypercode_organized_v2" $dir
    if (-not (Test-Path $fullPath)) {
        New-Item -ItemType Directory -Path $fullPath -Force | Out-Null
        Write-Host "  ✓ Created: /$dir" -ForegroundColor Green
    }
}

# 3. Move files to appropriate locations
$fileMoves = @{
    "*.json" = "data/processed"
    "*.db" = "database"
    "*.py" = "scripts"
    "*.md" = "docs"
}

Write-Host "`n🔄 Moving files to proper locations..." -ForegroundColor Yellow
foreach ($move in $fileMoves.GetEnumerator()) {
    $source = $move.Key
    $dest = Join-Path "hypercode_organized_v2" $move.Value
    Get-ChildItem -Path "hypercode_organized_v2" -Filter $source -File | ForEach-Object {
        Move-Item -Path $_.FullName -Destination $dest -Force
        Write-Host "  ✓ Moved: $($_.Name) → /$($move.Value)" -ForegroundColor Green
    }
}

Write-Host "`n✨ Phase 1 Cleanup Complete! Ready for development." -ForegroundColor Green