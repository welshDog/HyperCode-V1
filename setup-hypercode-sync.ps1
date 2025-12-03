#!/usr/bin/env powershell
<#
.SYNOPSIS
HyperCode Space-to-Main Setup Script
Complete one-shot setup for sync system, config, tasks, and test run.

.DESCRIPTION
This script automates the entire setup process:
1. Creates .hypercode directory and moves config
2. Creates .vscode directory and tasks.json
3. Creates space_sync source folders
4. Creates test files for dry-run verification
5. Runs dry-run sync
6. Runs live sync
7. Shows results and log

.EXAMPLE
./setup-hypercode-sync.ps1

.NOTES
Run from repo root. PowerShell 5.0+
#>

param(
    [switch]$SkipDryRun,
    [switch]$SkipLive,
    [switch]$VerboseOutput
)

# ============================================================================
# COLORS & LOGGING
# ============================================================================

function Write-Success {
    Write-Host "✅ $args" -ForegroundColor Green
}

function Write-Info {
    Write-Host "ℹ️  $args" -ForegroundColor Cyan
}

function Write-Warning {
    Write-Host "⚠️  $args" -ForegroundColor Yellow
}

function Write-Error-Custom {
    Write-Host "❌ $args" -ForegroundColor Red
}

function Write-Bullet {
    Write-Host "  • $args" -ForegroundColor White
}

# ============================================================================
# STEP 1: SETUP DIRECTORIES
# ============================================================================

Write-Host "`n$('='*70)" -ForegroundColor Magenta
Write-Host "🚀 HyperCode Space-to-Main Sync Setup" -ForegroundColor Magenta
Write-Host "$('='*70)`n" -ForegroundColor Magenta

Write-Info "Step 1/6: Setting up directories..."

# Create .hypercode
if (!(Test-Path .hypercode)) {
    New-Item -ItemType Directory -Path .hypercode -Force | Out-Null
    Write-Success "Created .hypercode directory"
} else {
    Write-Bullet ".hypercode already exists"
}

# Create .vscode
if (!(Test-Path .vscode)) {
    New-Item -ItemType Directory -Path .vscode -Force | Out-Null
    Write-Success "Created .vscode directory"
} else {
    Write-Bullet ".vscode already exists"
}

# Create scripts
if (!(Test-Path scripts)) {
    New-Item -ItemType Directory -Path scripts -Force | Out-Null
    Write-Success "Created scripts directory"
} else {
    Write-Bullet "scripts already exists"
}

# ============================================================================
# STEP 2: MOVE CONFIG FILE
# ============================================================================

Write-Info "Step 2/6: Configuring sync settings..."

if (Test-Path sync.toml) {
    Move-Item -Path sync.toml -Destination .hypercode\sync.toml -Force
    Write-Success "Moved sync.toml to .hypercode/"
} else {
    Write-Warning "sync.toml not found, creating from template..."
    
    $syncTomlContent = @'
# HyperCode Space-to-Main Sync Configuration
# Last Updated: 2025-11-30

[sync]
source_root = "space_sync"
target_root = "."

[sync.mappings]
raw_docs   = "docs"
raw_data   = "data"
raw_assets = "assets"

strict_mirror = false
delete_orphans = false
log_file = "logs/sync-space-to-main.log"

[filters]
exclude_extensions = [".tmp", ".bak", ".swp", ".lock"]
exclude_dirs = ["__pycache__", ".pytest_cache", ".git", "node_modules", ".venv", "venv"]
exclude_names = [".DS_Store", "Thumbs.db", ".env", ".env.local"]
'@
    
    $syncTomlContent | Out-File -FilePath .hypercode\sync.toml -Encoding utf8
    Write-Success "Created .hypercode/sync.toml from template"
}

# ============================================================================
# STEP 3: CREATE VS CODE TASKS
# ============================================================================

Write-Info "Step 3/6: Creating VS Code tasks..."

$tasksContent = @'
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "HyperCode: Sync Space → Main (Dry-Run)",
      "type": "shell",
      "command": "python",
      "args": ["scripts/sync-space-to-main.py", "--dry-run"],
      "group": { "kind": "test", "isDefault": false },
      "presentation": { "echo": true, "reveal": "always", "panel": "new" },
      "problemMatcher": []
    },
    {
      "label": "HyperCode: Sync Space → Main (LIVE)",
      "type": "shell",
      "command": "python",
      "args": ["scripts/sync-space-to-main.py"],
      "group": { "kind": "build", "isDefault": false },
      "presentation": { "echo": true, "reveal": "always", "panel": "new" },
      "problemMatcher": []
    },
    {
      "label": "HyperCode: Build Hyper Database",
      "type": "shell",
      "command": "python",
      "args": ["scripts/build-hyper-database-fixed.py"],
      "group": { "kind": "build", "isDefault": false },
      "presentation": { "echo": true, "reveal": "always", "panel": "new" },
      "problemMatcher": []
    }
  ]
}
'@

$tasksContent | Out-File -FilePath .vscode\tasks.json -Encoding utf8
Write-Success "Created .vscode/tasks.json with HyperCode tasks"

# ============================================================================
# STEP 4: CREATE SOURCE DIRECTORIES & TEST FILES
# ============================================================================

Write-Info "Step 4/6: Creating test data structure..."

$sourceDirs = @("space_sync/raw_docs", "space_sync/raw_data", "space_sync/raw_assets")
foreach ($dir in $sourceDirs) {
    if (!(Test-Path $dir)) {
        New-Item -ItemType Directory -Path $dir -Force | Out-Null
        Write-Success "Created $dir"
    } else {
        Write-Bullet "$dir already exists"
    }
}

# Create test files
Write-Info "Creating test files..."

$testDoc = @'
# HyperCode Research Notes

## Overview
This is a test document to verify the sync system.

## Key Points
- Sync works when files are copied correctly
- This proves the automation is active
- Test files can be deleted after verification

## Findings
Research automation is functioning as expected.
'@

$testDoc | Out-File -FilePath "space_sync/raw_docs/HYPERCODE_RESEARCH.md" -Encoding utf8
Write-Success "Created test document: HYPERCODE_RESEARCH.md"

$testData = @'
{
  "hypercode": {
    "version": "1.0.0",
    "status": "active",
    "neurodivergent_optimized": true,
    "ai_compatible": true,
    "test_run": true
  },
  "research_summary": {
    "languages_researched": ["Plankalkül", "Brainfuck", "Befunge"],
    "target_audience": "Neurodivergent Developers",
    "sync_timestamp": "2025-11-30T23:54:00Z"
  }
}
'@

$testData | Out-File -FilePath "space_sync/raw_data/hypercode_manifest.json" -Encoding utf8 -Force
Write-Success "Created test data: hypercode_manifest.json"

$testAsset = "HyperCode Test Asset - Automated Sync Verification"
$testAsset | Out-File -FilePath "space_sync/raw_assets/test_asset.txt" -Encoding utf8
Write-Success "Created test asset: test_asset.txt"

# ============================================================================
# STEP 5: DRY-RUN SYNC
# ============================================================================

if (-not $SkipDryRun) {
    Write-Info "Step 5/6: Running DRY-RUN sync (safe preview)..."
    Write-Host ""
    
    python scripts/sync-space-to-main.py --dry-run
    
    Write-Host ""
}

# ============================================================================
# STEP 6: LIVE SYNC
# ============================================================================

if (-not $SkipLive) {
    Write-Info "Step 6/6: Running LIVE sync..."
    Write-Host ""
    
    python scripts/sync-space-to-main.py
    
    Write-Host ""
}

# ============================================================================
# VERIFICATION & SUMMARY
# ============================================================================

Write-Host "`n$('='*70)" -ForegroundColor Magenta
Write-Host "📊 SETUP VERIFICATION" -ForegroundColor Magenta
Write-Host "$('='*70)`n" -ForegroundColor Magenta

# Check synced files
Write-Info "Checking synced files..."

$syncDirs = @("docs", "data", "assets")
$totalSynced = 0

foreach ($dir in $syncDirs) {
    if (Test-Path $dir) {
        $files = @(Get-ChildItem -Path $dir -Recurse -File 2>$null)
        $count = $files.Count
        $totalSynced += $count
        Write-Success "$dir/ - $count file(s)"
        
        foreach ($file in $files) {
            $relPath = $file.FullName -replace [regex]::Escape((Get-Location).Path + '\'), ''
            Write-Bullet $relPath
        }
    }
}

Write-Host ""

# Check logs
Write-Info "Log file location..."
if (Test-Path "logs/sync-space-to-main.log") {
    Write-Success "logs/sync-space-to-main.log (last 10 entries):"
    Write-Host ""
    Get-Content -Path "logs/sync-space-to-main.log" -Tail 10 | ForEach-Object { Write-Bullet $_ }
    Write-Host ""
} else {
    Write-Warning "No log file yet (will be created on sync)"
}

# Final summary
Write-Host "$('='*70)" -ForegroundColor Magenta
Write-Host "✨ SETUP COMPLETE!" -ForegroundColor Green
Write-Host "$('='*70)`n" -ForegroundColor Magenta

Write-Host "📋 What's been set up:" -ForegroundColor Cyan
Write-Bullet ".hypercode/sync.toml - Configuration file"
Write-Bullet ".vscode/tasks.json - VS Code/Windsurf tasks"
Write-Bullet "space_sync/ - Source folders for Space exports"
Write-Bullet "scripts/sync-space-to-main.py - Sync script"
Write-Bullet "docs/, data/, assets/ - Sync destination folders"

Write-Host "`n🚀 NEXT STEPS:" -ForegroundColor Green
Write-Bullet "In Windsurf: Ctrl+Shift+B → 'HyperCode: Sync Space → Main (Dry-Run)'"
Write-Bullet "Or run: python scripts/sync-space-to-main.py --dry-run"
Write-Bullet "Export your Space data to space_sync/raw_docs, raw_data, raw_assets"
Write-Bullet "Run sync again to mirror everything into the main repo"
Write-Bullet "Open Windsurf Cascade with full context ready! 🔥"

Write-Host "`n💡 TIP:" -ForegroundColor Yellow
Write-Host "After exporting Space data:" -ForegroundColor White
Write-Bullet "python scripts/sync-space-to-main.py          (full sync)"
Write-Bullet "python scripts/build-hyper-database-fixed.py  (rebuild AI index)"
Write-Bullet "Open Windsurf + Hyper Builder role = FULL CONTEXT! 🧠💪"

Write-Host ""
Write-Success "HyperCode automation is LIVE! BRO! 🔥👊"
Write-Host "`n"
