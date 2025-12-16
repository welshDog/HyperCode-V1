# 🚀 HyperCode Project Organizer

A powerful, user-friendly Python script to organize HyperCode project files and documentation with advanced features like conflict handling, automated backups, and validation.

## ⚡ Quick Wins Implemented

### 1. ✅ File Conflict Handling (15 min)
Automatically detects and resolves file conflicts by renaming duplicates with numeric suffixes:
```
Duplicate detected: `config.json` → renamed to `config_1.json`
```

### 2. ✅ Automated Backup Creation (20 min)
Create timestamped backups before organization:
```bash
python scripts/project_organizer.py --backup
# Creates: backups/org_backup_20251216_162700/
```

### 3. ✅ Documentation Validation (10 min)
Check which expected docs are missing without making changes:
```bash
python scripts/project_organizer.py --validate
```

### 4. ✅ Rich Color Output (5 min)
Beautiful, neurodivergent-friendly colored output (with graceful fallback):
- 🟢 **Green**: Success messages (files moved, backup created)
- 🟡 **Yellow**: Warnings (conflicts detected, missing docs)
- 🔴 **Red**: Errors (operation failures)
- 🔵 **Cyan**: Info messages (start/completion)

## 📦 Installation

### Basic Setup (Works Without Rich)
```bash
# No dependencies required!
python scripts/project_organizer.py --dry-run
```

### Enhanced Experience (With Colors)
```bash
# Install optional dependency for colored output
pip install rich

# Now run with beautiful colors
python scripts/project_organizer.py --validate
```

## 🎯 Usage Examples

### Preview Changes (Safe)
```bash
python scripts/project_organizer.py --dry-run
```
**Output**: Shows what WOULD happen without making any changes.

### Validate Documentation Structure
```bash
python scripts/project_organizer.py --validate
```
**Output**: Lists missing documentation files in each category.

### Full Organization with Backup
```bash
python scripts/project_organizer.py --backup
```
**Actions**:
1. Creates timestamped backup in `backups/org_backup_YYYYMMDD_HHMMSS/`
2. Organizes all files into correct directories
3. Moves documentation to categorized folders
4. Generates comprehensive report

### Skip Specific Phases
```bash
# Only organize files (skip docs)
python scripts/project_organizer.py --skip-docs

# Only organize docs (skip files)
python scripts/project_organizer.py --skip-files
```

### Dry Run with Validation
```bash
python scripts/project_organizer.py --dry-run --validate
```
**Output**: Preview changes AND see missing documentation.

## 📋 Features

### 🛡️ Safety First
- **Dry-run mode** - Preview all changes before execution
- **Automatic backups** - Timestamped copies before moving files
- **Conflict detection** - Smart renaming prevents data loss
- **Comprehensive logging** - Full audit trail in `project_organizer.log`

### 🎨 Neurodivergent-Friendly
- **Color-coded output** - Visual feedback for different actions
- **No overwhelming info** - Clean, focused reporting
- **Graceful degradation** - Works perfectly without Rich library
- **Clear status messages** - Immediate feedback on what's happening

### 📊 Organization Structure

#### Files Organized By Type
```
test_*.py          → tests/unit/
*.md               → docs/
*.txt              → docs/
*.yaml, *.yml      → config/
*.json, *.toml     → config/
```

#### Documentation Organized By Category
```
Getting Started      guides/               Reference
├─ QUICK_START.md    ├─ TUTORIAL.md       ├─ API_REFERENCE.md
├─ INSTALL.md        ├─ RECIPES.md        └─ LANGUAGE_REFERENCE.md
├─ Dev-Setup-Guide   ├─ TROUBLESHOOTING
└─ ... (13 total)    └─ ... (11 total)
```

### ✨ Advanced Features

#### Conflict Handling
```python
# If config.json already exists in target:
config.json       →  stays as-is
config_new.json   →  renamed to config_1.json (if moved)
```

#### Backup Structure
```
backups/
└── org_backup_20251216_162700/
    ├── test_sample.py
    ├── config.json
    ├── QUICK_START.md
    └── ... (all files that would be moved)
```

#### Report Generation
Detailed report saved to `organization_report.txt` with:
- Files moved (count & list)
- Files skipped (with error reasons)
- Documentation moved (with categories)
- Missing documentation (by category)
- Timestamp of execution

## 🔍 Validation Output Example

```
⚠ Missing documentation files:

[getting-started]
  - QUICK_START.md
  - Developer-Quickstart.md

[guides]
  - BETA_TESTER_GUIDE.md
  - VIDEO_SCRIPTS.md

[reference]
  - LANGUAGE_REFERENCE.md
```

## 📝 Logging

All operations logged to `project_organizer.log`:
```
2025-12-16 16:27:37,123 - INFO - Starting file organization...
2025-12-16 16:27:37,456 - INFO - Moved: test_sample.py -> tests/unit/test_sample.py
2025-12-16 16:27:37,789 - WARNING - File conflict handled: config.json -> config_1.json
2025-12-16 16:27:38,012 - INFO - Organization completed successfully!
```

## 🚨 Error Handling

Graceful handling of:
- **Missing files** - Skipped without error
- **Permission errors** - Logged and reported
- **File conflicts** - Automatically renamed
- **Missing directories** - Created automatically

## 🛠️ Customization

Edit these sections in the script to customize:

### Add New File Types
```python
self.file_mappings = {
    "*.ts": self.dirs["src"],      # Add TypeScript files
    "*.rs": self.dirs["src"],      # Add Rust files
    # ...
}
```

### Add Documentation Categories
```python
self.docs_structure = {
    "examples": [
        "EXAMPLE_1.md",
        "EXAMPLE_2.md",
        # ...
    ],
    # ...
}
```

### Exclude Additional Files
```python
self.exclude_files = {
    "README.md",
    "MY_SPECIAL_FILE.md",
    # ...
}
```

## 🎓 Use Cases

### First-Time Setup
```bash
# 1. Preview what will happen
python scripts/project_organizer.py --dry-run

# 2. Validate docs structure
python scripts/project_organizer.py --validate

# 3. Run with backup
python scripts/project_organizer.py --backup
```

### Regular Maintenance
```bash
# Weekly check
python scripts/project_organizer.py --validate

# Clean up when needed
python scripts/project_organizer.py --skip-docs
```

### Before Major Refactor
```bash
# Create backup + organize
python scripts/project_organizer.py --backup

# Files are now in `backups/org_backup_*` if you need to restore
```

## 🐛 Troubleshooting

### "File not found" errors
**Cause**: Running from wrong directory  
**Solution**: Run from project root: `python scripts/project_organizer.py`

### No colors showing
**Cause**: `rich` library not installed  
**Solution**: Either install `pip install rich` or script works fine in grayscale

### Backup not created
**Cause**: Forgot `--backup` flag  
**Solution**: Use `python scripts/project_organizer.py --backup`

### Files not moving (dry-run)
**Cause**: Normal behavior - dry-run never moves files  
**Solution**: Remove `--dry-run` flag to actually move files

## 📊 Performance

- **Speed**: ~50-100 files/sec depending on I/O
- **Memory**: Minimal - processes files iteratively
- **Storage**: Backup size = size of files being moved

## 🔐 Safety

✅ **Zero data loss**
- Dry-run preview before changes
- Automatic backups available
- Detailed logging of all operations
- Conflict detection and resolution

✅ **Non-destructive**
- Files are moved, never deleted
- Original directory structure backups kept
- Easy rollback via backup folder

## 📜 License

Part of HyperCode project. See main LICENSE file.

## 🤝 Contributing

Found a bug? Have a feature idea? Open an issue on GitHub!

---

**Built with 💙 for neurodivergent developers by HyperCode**  
*Making programming accessible for every brain type.*
