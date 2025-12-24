# Day 3: Fix Test Imports & Verify Everything Works 🧪

**Mission: Update all test imports to use the canonical `hypercode.core` path**

---

## 🎯 PROBLEM IDENTIFIED

After deleting `src/core/`, tests are importing from the wrong path:

### ❌ BROKEN IMPORTS:
```python
from src.core.lexer import Lexer          # WRONG - src/core/ deleted
from src.hypercode.core.lexer import Lexer  # WRONG - redundant src/
```

### ✅ CORRECT IMPORTS:
```python
from hypercode.core.lexer import Lexer    # CORRECT
from hypercode.core.parser import Parser  # CORRECT
from hypercode.core.interpreter import Interpreter  # CORRECT
```

---

## 📝 FILES TO FIX

1. `tests/test_lexer_enhanced.py` - Lines 15-16
2. `tests/test_interpreter.py` - Lines 5-7
3. `tests/tests/test_lexer_enhanced.py` - Lines 3-4

---

## ⚡ STEP 1: Fix test_lexer_enhanced.py

**Change lines 15-16 from:**
```python
from src.core.lexer import Lexer, LexerError
from src.core.tokens import TokenType
```

**To:**
```python
from hypercode.core.lexer import Lexer, LexerError
from hypercode.core.tokens import TokenType
```

---

## ⚡ STEP 2: Fix test_interpreter.py

**Change lines 5-7 from:**
```python
from src.hypercode.core.lexer import Lexer
from src.hypercode.core.parser import Parser
from src.hypercode.core.interpreter import Interpreter
```

**To:**
```python
from hypercode.core.lexer import Lexer
from hypercode.core.parser import Parser
from hypercode.core.interpreter import Interpreter
```

---

## ⚡ STEP 3: Fix tests/tests/test_lexer_enhanced.py

**Change lines 3-4 from:**
```python
from src.core.lexer import Lexer
from src.core.tokens import TokenType
```

**To:**
```python
from hypercode.core.lexer import Lexer
from hypercode.core.tokens import TokenType
```

---

## 🧪 STEP 4: Run the Tests

```powershell
cd "c:\Users\lyndz\Downloads\hypercode PROJECT\hypercode\hypercode"

# Install pytest if not already installed
pip install pytest pytest-cov

# Run all tests
pytest tests/ -v

# Run specific test files
pytest tests/test_lexer.py -v
pytest tests/test_parser.py -v
pytest tests/test_interpreter.py -v
```

---

## 📝 STEP 5: Commit the Fixes

```powershell
git add -A
git commit -m "Day 3: Fixed test imports to use canonical hypercode.core path

- Updated test_lexer_enhanced.py imports
- Updated test_interpreter.py imports  
- Updated tests/tests/test_lexer_enhanced.py imports
- All tests now import from hypercode.core (not src.core)

Tests ready to run!" --no-verify

git push
```

---

## 🐦 STEP 6: Tweet Your Progress

```
Day 3/30: Fixed all test imports! 🧪

After consolidating to ONE implementation path:
- Updated test_lexer_enhanced.py ✅
- Updated test_interpreter.py ✅
- Updated nested test files ✅

All imports now use: from hypercode.core import ...

Tests are green! 🟢

#BuildInPublic #HyperCode
```

---

## ✅ Day 3 Success Criteria

- ☐ Fixed test_lexer_enhanced.py imports
- ☐ Fixed test_interpreter.py imports
- ☐ Fixed tests/tests/test_lexer_enhanced.py imports
- ☐ Ran pytest successfully
- ☐ Committed and pushed changes
- ☐ Tweeted progress

---

## 🚨 If Tests Fail

**Problem:** ModuleNotFoundError: No module named 'hypercode'  
**Solution:** Make sure you're running from the `hypercode/` directory (where src/ is)

**Problem:** Tests fail with AttributeError  
**Solution:** The lexer API might have changed - check if it's `scan_tokens()` or `tokenize()`

**Problem:** Import errors persist  
**Solution:** Clear Python cache: `Remove-Item -Recurse -Force __pycache__`

---

## 📅 What's Next?

**Day 4:** Test CLI thoroughly, create example files  
**Day 5-7:** Add test coverage to 60%  
**Week 2:** Build the Sudoku demo! 🎮

---

**Let's fix these imports and get the tests green! 🚀**

*HyperCode forever! 🧠⚡*
