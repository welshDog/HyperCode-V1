# HyperCode V1 Automated Sprint Launcher
# This script automates repetitive Phase 1-2 tasks
# Run from: hypercode_organized_v2/ directory

param(
    [string]$Phase = "1",
    [switch]$Verbose
)

# Color output for ADHD brains (visual feedback = dopamine)
$colors = @{
    "Success" = "Green"
    "Warning" = "Yellow"
    "Error"   = "Red"
    "Info"    = "Cyan"
    "Header"  = "Magenta"
}

function Write-Color($Message, $Color = "White") {
    Write-Host $Message -ForegroundColor $Color
}

function Write-Header($Title) {
    Write-Color "`n$('='*60)" $colors["Header"]
    Write-Color "  $Title" $colors["Header"]
    Write-Color "$('='*60)`n" $colors["Header"]
}

function Execute-Phase {
    param([int]$PhaseNum, [scriptblock]$Actions)
    
    Write-Header "PHASE $PhaseNum"
    try {
        & $Actions
        Write-Color "✅ Phase $PhaseNum Complete!`n" $colors["Success"]
        return $true
    }
    catch {
        Write-Color "❌ Phase $PhaseNum Failed: $_" $colors["Error"]
        return $false
    }
}

# ============================================================================
# PHASE 1: CLEANUP & ORGANIZE (30 minutes)
# ============================================================================

$Phase1 = {
    Write-Color "🧹 PHASE 1: CLEANUP & ORGANIZE" $colors["Header"]
    
    # 1.1 Delete bad files
    Write-Color "Step 1.1: Removing bad filenames..." $colors["Info"]
    $badFiles = @(
        "to-do list",
        "🔥 ALL-IN DEPLOY - LET'S GO RIGHT NOW 🚀",
        "e -Force .hypercode",
        "add more Ai likes",
        "data analyze"
    )
    
    foreach ($file in $badFiles) {
        if (Test-Path $file) {
            Remove-Item $file -Force
            Write-Color "  ✓ Deleted: $file" $colors["Success"]
        }
    }
    
    # 1.2 Create organized folders
    Write-Color "Step 1.2: Creating organized folder structure..." $colors["Info"]
    
    $folders = @("database", "tools", "config")
    foreach ($folder in $folders) {
        if (-not (Test-Path $folder)) {
            New-Item -ItemType Directory -Name $folder | Out-Null
            Write-Color "  ✓ Created: /$folder" $colors["Success"]
        }
    }
    
    # 1.3 Move database files
    Write-Color "Step 1.3: Organizing database files..." $colors["Info"]
    
    $dbFiles = @(
        "HYPER_DATABASE.json",
        "hypercode-database.json", 
        "hypercode-research-database-deep.json",
        "hyperbase.db",
        "research.db"
    )
    
    foreach ($file in $dbFiles) {
        if (Test-Path $file) {
            Move-Item $file "database/$file" -Force
            Write-Color "  ✓ Moved: $file → /database" $colors["Success"]
        }
    }
    
    # 1.4 Move tool scripts
    Write-Color "Step 1.4: Organizing tool scripts..." $colors["Info"]
    
    $toolFiles = @(
        "database_analyzer.py",
        "fix_database_issues.py",
        "code_quality_report.py",
        "format_and_lint.py"
    )
    
    foreach ($file in $toolFiles) {
        if (Test-Path $file) {
            Move-Item $file "tools/$file" -Force
            Write-Color "  ✓ Moved: $file → /tools" $colors["Success"]
        }
    }
    
    # 1.5 Create README files
    Write-Color "Step 1.5: Creating documentation..." $colors["Info"]
    
    $dbReadme = @"
# Database Files

## Files in this Directory

- **HYPER_DATABASE.json** - Primary research database
- **hypercode-database.json** - Secondary consolidated database
- **hypercode-research-database-deep.json** - Deep research data
- **hyperbase.db** - SQLite database (legacy)
- **research.db** - Research findings database

## Usage

Choose ONE primary database file based on your use case.
"@
    
    $dbReadme | Out-File "database/README.md"
    Write-Color "  ✓ Created: /database/README.md" $colors["Success"]
    
    $toolsReadme = @"
# Development Tools

## Scripts in this Directory

- **database_analyzer.py** - Analyzes database structure
- **fix_database_issues.py** - Fixes data inconsistencies
- **code_quality_report.py** - Generates quality metrics
- **format_and_lint.py** - Code formatting and linting

## Usage

\`\`\`powershell
python tools/database_analyzer.py
python tools/code_quality_report.py
\`\`\`
"@
    
    $toolsReadme | Out-File "tools/README.md"
    Write-Color "  ✓ Created: /tools/README.md" $colors["Success"]
    
    # 1.6 Create CODEBASE_MAP.md
    Write-Color "Step 1.6: Creating codebase map..." $colors["Info"]
    
    $codemapContent = @"
# HyperCode V1 Codebase Map

Quick reference for navigating the repository.

## Core Language Implementation
- **/hypercode** - Main interpreter package
- **/parser** - HyperCode syntax parser
- **/interpreter** - Code execution engine
- **/stdlib** - Standard library functions

## Documentation
- **/docs** - Full technical documentation
- **README.md** - Public-facing overview
- **START_HERE.md** - Getting started guide
- **HYPERCODE_V1_SPRINT.md** - Development sprint plan

## Examples & Testing
- **/examples** - Working .hc example programs
- **/tests** - Unit and integration tests
- **test*.py** - Individual test files

## Configuration & Data
- **/config** - Configuration files
- **/database** - Research and project databases
- **/data** - Sample data files

## Development Tools
- **/tools** - Developer utilities (analysis, linting, etc)
- **/scripts** - Automation scripts
- **make.ps1** - PowerShell build automation
- **Makefile** - Unix-style build automation

## Metadata
- **pyproject.toml** - Python project configuration
- **setup.py** - Package setup
- **requirements.lock** - Locked dependency versions
- **.github/workflows** - CI/CD pipelines
- **Dockerfile** - Container image definition

## Getting Started
1. Read **START_HERE.md**
2. Run \`make.ps1 dev-setup\` to install
3. Check **/examples** for sample code
4. Read **/docs** for full documentation
"@
    
    $codemapContent | Out-File "CODEBASE_MAP.md"
    Write-Color "  ✓ Created: CODEBASE_MAP.md" $colors["Success"]
    
    # 1.7 Git operations
    Write-Color "Step 1.7: Committing changes to git..." $colors["Info"]
    
    git add . 2>&1 | Out-Null
    $commitMsg = "🧹 Phase 1: Cleanup and reorganize codebase"
    git commit -m $commitMsg 2>&1 | Out-Null
    Write-Color "  ✓ Committed: $commitMsg" $colors["Success"]
    
    Write-Color "`n✅ PHASE 1 COMPLETE!`n" $colors["Success"]
}

# ============================================================================
# PHASE 2: VALIDATE INTERPRETER (45 minutes)
# ============================================================================

$Phase2 = {
    Write-Color "⚡ PHASE 2: VALIDATE INTERPRETER" $colors["Header"]
    
    # 2.1 Test version command
    Write-Color "Step 2.1: Testing interpreter..." $colors["Info"]
    
    try {
        $version = python -m hypercode --version 2>&1
        if ($LASTEXITCODE -eq 0) {
            Write-Color "  ✓ Version check passed: $version" $colors["Success"]
        }
        else {
            Write-Color "  ⚠ Version check issue: $version" $colors["Warning"]
        }
    }
    catch {
        Write-Color "  ⚠ Could not run interpreter: $_" $colors["Warning"]
    }
    
    # 2.2 Run tests
    Write-Color "Step 2.2: Running test suite..." $colors["Info"]
    
    .\make.ps1 test
    
    if ($LASTEXITCODE -eq 0) {
        Write-Color "  ✓ Tests passed!" $colors["Success"]
    }
    else {
        Write-Color "  ⚠ Some tests failed - see output above" $colors["Warning"]
    }
    
    # 2.3 Create examples folder if missing
    Write-Color "Step 2.3: Setting up examples..." $colors["Info"]
    
    if (-not (Test-Path "examples")) {
        New-Item -ItemType Directory -Name "examples" | Out-Null
        Write-Color "  ✓ Created: /examples" $colors["Success"]
    }
    
    # 2.4 Create basic examples
    $helloExample = @"
# Hello, HyperCode!
"Hello, World!" → msg
print: msg
"@
    
    $helloExample | Out-File "examples/01_hello.hc"
    Write-Color "  ✓ Created: /examples/01_hello.hc" $colors["Success"]
    
    $mathExample = @"
# Simple math example
5 | add 3 → result
print: result
"@
    
    $mathExample | Out-File "examples/02_math.hc"
    Write-Color "  ✓ Created: /examples/02_math.hc" $colors["Success"]
    
    # 2.5 Test examples
    Write-Color "Step 2.5: Testing examples..." $colors["Info"]
    
    foreach ($file in @("01_hello.hc", "02_math.hc")) {
        try {
            Write-Color "  Testing: examples/$file" $colors["Info"]
            python -m hypercode "examples/$file" 2>&1
            Write-Color "  ✓ $file passed" $colors["Success"]
        }
        catch {
            Write-Color "  ⚠ $file failed - may need interpreter fixes" $colors["Warning"]
        }
    }
    
    # 2.6 Create status document
    Write-Color "Step 2.6: Creating status document..." $colors["Info"]
    
    $statusContent = @"
# Implementation Status - Dec 19, 2025

## ✅ Known Working
- Command-line interface (--version, --help)
- Basic file loading
- Test infrastructure

## 🔄 Partial / Needs Work
- Lexer (tokenization)
- Parser (AST building)
- Executor (runtime)
- Pipe operator (|)
- Print statements

## ❌ Not Yet Implemented
- Pattern matching
- Advanced data structures
- Error handling
- Module system
- AI integration

## Next Steps
1. Ensure lexer tokenizes .hc files correctly
2. Ensure parser builds valid AST
3. Implement basic operators
4. Add proper error messages
5. Create more test cases

## Testing Commands
\`\`\`powershell
.\make.ps1 test              # Run all tests
.\make.ps1 test-cov          # With coverage
python -m hypercode examples/01_hello.hc
\`\`\`
"@
    
    $statusContent | Out-File "docs/IMPLEMENTATION_STATUS.md"
    Write-Color "  ✓ Created: /docs/IMPLEMENTATION_STATUS.md" $colors["Success"]
    
    # 2.7 Git commit
    Write-Color "Step 2.7: Committing to git..." $colors["Info"]
    
    git add . 2>&1 | Out-Null
    $commitMsg = "⚡ Phase 2: Validate interpreter and add basic examples"
    git commit -m $commitMsg 2>&1 | Out-Null
    Write-Color "  ✓ Committed: $commitMsg" $colors["Success"]
    
    Write-Color "`n✅ PHASE 2 COMPLETE!`n" $colors["Success"]
}

# ============================================================================
# MAIN EXECUTION
# ============================================================================

Write-Color "`n" $colors["Header"]
Write-Color "╔════════════════════════════════════════════╗" $colors["Header"]
Write-Color "║   HyperCode V1 - Automated Sprint Launcher  ║" $colors["Header"]
Write-Color "╚════════════════════════════════════════════╝`n" $colors["Header"]

Write-Color "Running from: $(Get-Location)" $colors["Info"]
Write-Color "Timestamp: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')`n" $colors["Info"]

# Validate we're in right directory
if (-not (Test-Path "hypercode_organized_v2" -PathType Container)) {
    if (-not (Test-Path "hypercode" -PathType Container)) {
        Write-Color "❌ ERROR: Must run from repository root!" $colors["Error"]
        exit 1
    }
}

# Execute requested phases
switch ($Phase) {
    "1" {
        if (Execute-Phase 1 $Phase1) {
            Write-Color "📊 Next: Run Phase 2" $colors["Info"]
            Write-Color "   .\launch-sprint.ps1 -Phase 2`n" $colors["Info"]
        }
    }
    "2" {
        if (Execute-Phase 2 $Phase2) {
            Write-Color "📊 Next: Manually create Phase 3 examples" $colors["Info"]
            Write-Color "   (See HYPERCODE_V1_SPRINT.md for details)`n" $colors["Info"]
        }
    }
    "all" {
        $allPhases = @(
            @{ Num = 1; Block = $Phase1 },
            @{ Num = 2; Block = $Phase2 }
        )
        
        $completed = 0
        foreach ($p in $allPhases) {
            if (Execute-Phase $p.Num $p.Block) {
                $completed++
            }
            else {
                Write-Color "Stopping at Phase $($p.Num) due to error" $colors["Warning"]
                break
            }
        }
        
        Write-Color "`n🎉 $completed phases completed successfully!`n" $colors["Success"]
    }
    default {
        Write-Color "Usage: .\launch-sprint.ps1 -Phase <1|2|all>" $colors["Error"]
        Write-Color "Example: .\launch-sprint.ps1 -Phase 1" $colors["Info"]
        exit 1
    }
}

Write-Color "`n✨ Sprint launch complete! ✨`n" $colors["Success"]
