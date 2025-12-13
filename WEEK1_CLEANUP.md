# Week 1: The Great Consolidation 🔥
**Day 1-7 Execution Checklist**

## ⚡ STEP 1: Delete Duplicate Directories (20 minutes)

Run these commands from the project root:

```powershell
# Navigate to project root
cd "c:\Users\lyndz\Downloads\hypercode PROJECT\hypercode"

# DELETE duplicate/distraction directories
Remove-Item -Recurse -Force ".\hypercode-1"
Remove-Item -Recurse -Force ".\hypercode_backup_20251205_183301"
Remove-Item -Recurse -Force ".\core"
Remove-Item -Recurse -Force ".\knowledge_graph"
Remove-Item -Recurse -Force ".\live_research"
Remove-Item -Recurse -Force ".\mcp"
Remove-Item -Recurse -Force ".\ai"

# DELETE duplicate lexer files
Remove-Item -Force ".\hypercode\src\hypercode-lexer-COMPLETE.py"
Remove-Item -Force ".\hypercode\src\hypercode_lexer_fixed.py"
Remove-Item -Force ".\hypercode\src\hypercode_poc.py"

# Commit the cleanup
git add -A
git commit -m "Week 1 Day 1: Ruthless consolidation - deleted duplicate dirs and files"
git push
```

**✅ Success Criteria:** Repo is 50% smaller, only ONE implementation path exists

---

## 📝 STEP 2: Create Parking Lot for Future Ideas (10 minutes)

Already created below as `ideas_for_v0.3_and_beyond.md`

---

## 🛠️ STEP 3: Consolidate to ONE Implementation

**Canonical structure:**
```
hypercode/
├── src/
│   └── hypercode/
│       ├── __init__.py
│       ├── __main__.py          # CLI entry point (create this)
│       └── core/
│           ├── __init__.py
│           ├── lexer.py         # THE lexer
│           ├── parser.py        # THE parser
│           ├── interpreter.py   # THE interpreter
│           ├── ast.py           # THE AST
│           └── tokens.py        # Token definitions
├── tests/
│   ├── test_lexer.py
│   ├── test_parser.py
│   └── test_interpreter.py
└── examples/
    └── hello.hc
```

---

## 🧪 STEP 4: Fix the CLI (Day 3-4)

Create `hypercode/src/hypercode/__main__.py` (see separate file)

Test it works:
```powershell
python -m hypercode --version
# Expected: HyperCode v0.2.0

python -m hypercode examples/hello.hc
# Expected: Hello, HyperCode!
```

---

## ✅ STEP 5: Test Coverage (Day 5-7)

```powershell
# Install test dependencies
pip install pytest pytest-cov

# Run tests with coverage
pytest tests/ --cov=src/hypercode/core --cov-report=html

# Open coverage report
start htmlcov/index.html
```

**Target:** 60% coverage on critical path (lexer → parser → interpreter)

---

## 📊 Daily Accountability

**Every day, do this:**
1. Make at least ONE commit (even if small)
2. Tweet progress with #BuildInPublic
3. Update this checklist

**Day 1:** ☐ Deleted duplicate directories
**Day 2:** ☐ Consolidated to ONE lexer/parser/interpreter
**Day 3:** ☐ Created CLI entry point
**Day 4:** ☐ CLI works (`python -m hypercode --version`)
**Day 5:** ☐ Added tests for lexer
**Day 6:** ☐ Added tests for parser
**Day 7:** ☐ Hit 60% coverage, ready for Week 2

---

## 🚨 If You Get Stuck

**Blocker:** Can't decide which lexer to keep
**Solution:** Keep `hypercode/src/hypercode/core/lexer.py`, delete the rest

**Blocker:** Tests are failing
**Solution:** Comment out failing tests, fix ONE at a time

**Blocker:** Lost motivation
**Solution:** Tweet your progress, read the 30-day plan, remember the mission

---

**Week 1 Success = Clean codebase + working CLI + 60% test coverage**

Let's ship it! 🚀
