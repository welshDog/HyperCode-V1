# 🔥 HyperCode Space-to-Main Sync - Complete Setup Guide

**Last Updated:** 2025-11-30  
**Status:** Production-Ready ✅

---

## 📋 What You Have

| File/Folder | Purpose |
|-------------|---------|
| `scripts/sync-space-to-main.py` | Core sync engine (Python) |
| `.hypercode/sync.toml` | Configuration (TOML) |
| `.vscode/tasks.json` | VS Code/Windsurf tasks |
| `setup-hypercode-sync.ps1` | One-shot setup script |
| `space_sync/` | Source folders (Space exports) |
| `docs/`, `data/`, `assets/` | Destination folders (synced) |
| `logs/sync-space-to-main.log` | Audit trail |

---

## 🚀 QUICK START (One Command)

### Option A: Automatic Setup (RECOMMENDED)

```powershell
# Run from repo root
./setup-hypercode-sync.ps1
```

**This does everything:**
- ✅ Creates `.hypercode/` + `.vscode/` directories
- ✅ Places config file in right location
- ✅ Creates VS Code tasks for Windsurf
- ✅ Creates test folders and sample data
- ✅ Runs dry-run (safe preview)
- ✅ Runs live sync
- ✅ Shows results and summary

**Output:** Everything is ready. Grab coffee. ☕

---

### Option B: Manual Step-by-Step

```powershell
# 1. Create directories
mkdir .hypercode -Force
mkdir .vscode -Force
mkdir space_sync/raw_docs, space_sync/raw_data, space_sync/raw_assets -Force

# 2. Move config
Move-Item -Path sync.toml -Destination .hypercode\sync.toml -Force

# 3. Copy tasks.json
Copy-Item -Path tasks.json -Destination .vscode\tasks.json -Force

# 4. Test with sample data
"# HyperCode Test" | Out-File space_sync/raw_docs/test.md -Encoding utf8

# 5. Run sync (preview first)
python scripts/sync-space-to-main.py --dry-run

# 6. Go live
python scripts/sync-space-to-main.py

# 7. Verify
ls docs/
```

---

## 📂 Folder Structure After Setup

```
hypercode/
├── .hypercode/
│   └── sync.toml                           # Config
├── .vscode/
│   └── tasks.json                          # VS Code tasks
├── scripts/
│   ├── sync-space-to-main.py               # Sync engine
│   └── build-hyper-database-fixed.py       # AI indexer
├── space_sync/                             # SOURCE (from Space)
│   ├── raw_docs/
│   ├── raw_data/
│   └── raw_assets/
├── docs/                                   # DESTINATION (synced)
├── data/                                   # DESTINATION (synced)
├── assets/                                 # DESTINATION (synced)
└── logs/
    └── sync-space-to-main.log              # Audit trail
```

---

## 🔄 How Sync Works

```
┌─────────────────────────────────────────────┐
│ Your HyperCode Space                        │
│ (Research docs, data, diagrams)             │
└────────────────┬────────────────────────────┘
                 │ EXPORT
                 ▼
┌─────────────────────────────────────────────┐
│ space_sync/                                 │
│ ├─ raw_docs/    (research markdown)         │
│ ├─ raw_data/    (JSON, embeddings)          │
│ └─ raw_assets/  (diagrams, PDFs)            │
└────────────────┬────────────────────────────┘
                 │ RUN SYNC
                 ▼
┌─────────────────────────────────────────────┐
│ Main Repo Folders                           │
│ ├─ docs/       ← copied from raw_docs       │
│ ├─ data/       ← copied from raw_data       │
│ └─ assets/     ← copied from raw_assets     │
└────────────────┬────────────────────────────┘
                 │ BUILD DATABASE
                 ▼
┌─────────────────────────────────────────────┐
│ Hyper Database                              │
│ (Full codebase + research indexed)          │
└────────────────┬────────────────────────────┘
                 │ OPEN WINDSURF
                 ▼
┌─────────────────────────────────────────────┐
│ Windsurf Cascade + Hyper Builder Role       │
│ FULL CONTEXT READY 🧠💪🔥                  │
└─────────────────────────────────────────────┘
```

---

## 💻 Using in Windsurf / VS Code

### Method 1: Command Palette (Easiest)

1. Press `Ctrl+Shift+P`
2. Type `Tasks: Run Task`
3. Select one:
   - **"HyperCode: Sync Space → Main (Dry-Run)"** → Preview changes
   - **"HyperCode: Sync Space → Main (LIVE)"** → Execute sync
   - **"HyperCode: Build Hyper Database"** → Rebuild AI index

### Method 2: Keyboard Shortcut

- `Ctrl+Shift+B` → Runs default task (or pick from menu)

### Method 3: Terminal

```bash
python scripts/sync-space-to-main.py --dry-run    # Preview
python scripts/sync-space-to-main.py               # Live sync
python scripts/build-hyper-database-fixed.py       # Rebuild index
```

---

## 📊 Configuration Reference

### `.hypercode/sync.toml`

```toml
[sync]
source_root = "space_sync"      # Where Space exports go
target_root = "."               # Where to sync to (repo root)
delete_orphans = false          # Keep manual edits safe
log_file = "logs/sync-space-to-main.log"

[sync.mappings]
raw_docs   = "docs"             # docs/
raw_data   = "data"             # data/
raw_assets = "assets"           # assets/

[filters]
exclude_extensions = [".tmp", ".bak", ".swp"]
exclude_dirs = ["__pycache__", ".git", "node_modules"]
exclude_names = [".DS_Store", "Thumbs.db"]
```

**Key Settings:**
- `delete_orphans = false` → Keeps your manual edits safe (recommended)
- `delete_orphans = true` → Strict mirror (deletes anything not in source)

---

## 🔑 Common Commands

| Command | Purpose |
|---------|---------|
| `python scripts/sync-space-to-main.py --dry-run` | Preview changes (SAFE) |
| `python scripts/sync-space-to-main.py` | Execute sync (LIVE) |
| `python scripts/sync-space-to-main.py --config custom.toml` | Use custom config |
| `type logs/sync-space-to-main.log` | View sync history |
| `ls space_sync/` | Check source files |
| `ls docs/` | Check synced files |

---

## 🐛 Troubleshooting

### "Config file not found"
- Make sure `.hypercode/sync.toml` exists
- Or run `./setup-hypercode-sync.ps1` to auto-create

### "No files copied"
- Check that `space_sync/raw_docs`, `raw_data`, `raw_assets` have files
- Run `python scripts/sync-space-to-main.py --dry-run` to see what it would do
- Check that files aren't in the `exclude_extensions` or `exclude_dirs` list

### "Permission denied"
- Make sure you have write access to the repo folder
- Some antivirus software may block file operations
- Try running as Administrator

### "Python not found"
- Install Python 3.8+ from https://www.python.org
- Add to PATH during installation (check "Add Python to PATH")
- Verify: `python --version`

### "toml module not found"
- Install: `pip install toml`

---

## ⚡ Workflow Example

**Step 1: Export Space Data**
```
Your HyperCode Space
  ↓ Download/Export
space_sync/raw_docs/research-2025-11-30.md
space_sync/raw_data/embeddings.json
space_sync/raw_assets/architecture.png
```

**Step 2: Run Sync**
```powershell
python scripts/sync-space-to-main.py
```

**Output:**
```
[✓] Loaded config from .hypercode/sync.toml
[INFO] Copied: research-2025-11-30.md
[INFO] Copied: embeddings.json
[INFO] Copied: architecture.png
Copied: 3 | Updated: 0 | Deleted: 0 | Errors: 0
```

**Step 3: Rebuild Database**
```powershell
python scripts/build-hyper-database-fixed.py
```

**Step 4: Open Windsurf + Hyper Builder**
```
Windsurf sees:
  ✅ All HyperCode source code
  ✅ All research documents
  ✅ All data/embeddings
  ✅ Full Hyper Database index
  → FULL CONTEXT READY 🧠💪
```

---

## 🎯 Pro Tips

### Tip 1: Automate on Schedule
Add to GitHub Actions (`.github/workflows/daily-sync.yml`):
```yaml
schedule:
  - cron: '0 0 * * *'  # Daily at midnight
run: python scripts/sync-space-to-main.py
```

### Tip 2: Pre-commit Hook
Auto-sync before every commit (`.git/hooks/pre-commit`):
```bash
#!/bin/bash
python scripts/sync-space-to-main.py
git add docs/ data/ assets/
```

### Tip 3: Monitor Logs
```powershell
# Watch logs in real-time
Get-Content -Path logs/sync-space-to-main.log -Wait
```

### Tip 4: Backup Before Delete
If using `delete_orphans = true`, always commit first:
```bash
git add .
git commit -m "Backup before sync with orphan deletion"
python scripts/sync-space-to-main.py
```

---

## 📞 Support

- **Dry-run first:** Always use `--dry-run` to see what will change
- **Check logs:** `type logs/sync-space-to-main.log`
- **Test with samples:** Run `./setup-hypercode-sync.ps1` for test data
- **Read config comments:** `.hypercode/sync.toml` has inline docs

---

## 🔥 You're Ready!

```
✅ Setup complete
✅ Sync system active
✅ VS Code tasks configured
✅ Test files created and synced
✅ Logs created and tracked
✅ Windsurf ready to launch

Next: Export your Space data → space_sync/ → Run sync → Build database → CODE WITH FULL CONTEXT 🚀
```

**BRO, you're LEGENDARY now!** 👊💪🔥

Go build the future. HyperCode is ready. ✨

---

*Questions? Check the troubleshooting section or review the inline docs in the Python script and TOML config.*
