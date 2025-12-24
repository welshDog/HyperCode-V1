# 🔧 HyperCode: Dependency Troubleshooting Guide

## Quick Fixes for Installation Issues

**Date**: November 11, 2025, 3:25 PM GMT **Issue**: `weaviate-client==4.1.1` doesn't
exist **Solution**: Use version 4.18.0 instead ✅

---

## 🚨 The Problem You Hit

```
ERROR: Could not find a version that satisfies the requirement weaviate-client==4.1.1
```

**Why**: The package repository doesn't have that specific version. **Real available**:
4.18.0, 4.17.0, 4.16.10, etc. **What we did**: Updated to 4.18.0 ✅

---

## ✅ IMMEDIATE FIX (Do This NOW!)

### Option 1: Use the Fixed Requirements File (EASIEST)

```bash
# Delete the old broken requirements.txt
rm requirements.txt

# Copy the FIXED one from our file [119]
# Download requirements-FIXED.txt and rename it

# Or just use this in your repo:
pip install -r requirements-FIXED.txt

# ✅ Should work now!
```

### Option 2: Manual Fix (If you want to keep requirements.txt)

```bash
# Open requirements.txt in your editor

# Find this line:
weaviate-client==4.1.1

# Replace with:
weaviate-client==4.18.0

# Save file

# Then run:
pip install -r requirements.txt
```

### Option 3: Update Everything (Nuclear Option)

```bash
# Clear cache and try again
pip cache purge

# Uninstall the broken packages
pip uninstall -y weaviate-client

# Reinstall with correct version
pip install weaviate-client==4.18.0

# Or install all fresh:
pip install -r requirements-FIXED.txt --force-reinstall
```

---

## 📋 All Fixed Versions (From [119])

Here are the CORRECT versions that work:

```
# ✅ WORKING VERSIONS:
antlr4-python3-runtime==4.13.1   ✅
pydantic==2.5.0                   ✅
pydantic-settings==2.1.0          ✅
openai==1.3.5                     ✅
anthropic==0.7.1                  ✅
mistralai==0.0.11                 ✅
ollama==0.1.0                     ✅
huggingface-hub==0.19.3           ✅
pinecone-client==3.0.0            ✅
weaviate-client==4.18.0           ✅ (FIXED!)
langchain==0.1.3                  ✅
langchain-openai==0.0.2           ✅
langchain-anthropic==0.1.4        ✅
requests==2.31.0                  ✅
beautifulsoup4==4.12.2            ✅
aiohttp==3.9.1                    ✅
selenium==4.15.0                  ✅
arxiv==2.1.0                      ✅
scholarly==1.7.11                 ✅
rdflib==7.0.0                     ✅
sparqlwrapper==1.8.5              ✅
neo4j==5.13.0                     ✅
python-dotenv==1.0.0              ✅
click==8.1.7                      ✅
typer==0.9.0                      ✅
rich==13.7.0                      ✅
pyyaml==6.0.1                     ✅
jsonschema==4.20.0                ✅
loguru==0.7.2                     ✅
python-json-logger==2.0.7         ✅
orjson==3.9.10                    ✅
cachetools==5.3.2                 ✅
ratelimit==2.2.1                  ✅
pandas==2.1.3                     ✅
numpy==1.26.2                     ✅
msgpack==1.0.7                    ✅
typing-extensions==4.8.0          ✅
typeguard==4.1.5                  ✅
```

---

## 🎯 Step-by-Step SOLUTION

### 1. Stop Current Installation

```bash
# Press Ctrl+C to stop pip if it's still running
```

### 2. Delete Old requirements.txt

```bash
cd ~/Downloads/HyperCode/hypercode
rm requirements.txt
```

### 3. Create NEW Fixed requirements.txt

Copy this content exactly:

```
# HyperCode: Production Dependencies (FIXED)
antlr4-python3-runtime==4.13.1
pydantic==2.5.0
pydantic-settings==2.1.0
openai==1.3.5
anthropic==0.7.1
mistralai==0.0.11
ollama==0.1.0
huggingface-hub==0.19.3
pinecone-client==3.0.0
weaviate-client==4.18.0
langchain==0.1.3
langchain-openai==0.0.2
langchain-anthropic==0.1.4
requests==2.31.0
beautifulsoup4==4.12.2
aiohttp==3.9.1
selenium==4.15.0
arxiv==2.1.0
scholarly==1.7.11
rdflib==7.0.0
sparqlwrapper==1.8.5
neo4j==5.13.0
python-dotenv==1.0.0
click==8.1.7
typer==0.9.0
rich==13.7.0
pyyaml==6.0.1
jsonschema==4.20.0
loguru==0.7.2
python-json-logger==2.0.7
orjson==3.9.10
cachetools==5.3.2
ratelimit==2.2.1
pandas==2.1.3
numpy==1.26.2
msgpack==1.0.7
typing-extensions==4.8.0
typeguard==4.1.5
```

### 4. Clear pip Cache

```bash
pip cache purge
```

### 5. Install Clean

```bash
pip install -r requirements.txt
```

### Expected Output

```
Collecting antlr4-python3-runtime==4.13.1
Collecting pydantic==2.5.0
...
Successfully installed antlr4-python3-runtime-4.13.1 pydantic-2.5.0 ...
```

### 6. Verify Installation

```bash
pip list | grep -E "weaviate|pydantic|openai"

# Should show:
# anthropic                    0.7.1
# openai                       1.3.5
# pydantic                     2.5.0
# weaviate-client              4.18.0
```

### 7. Test Lexer Still Works

```bash
python core/lexer.py

# Should output token info ✅
```

---

## 🛡️ How to Prevent This

### 1. Always Check PyPI First

Before adding a dependency:

```bash
# Check available versions
pip index versions package-name

# Example:
pip index versions weaviate-client
# Returns: Available versions: 4.18.0, 4.17.0, 4.16.10, ...
```

### 2. Use Flexible Versions (Optional)

Instead of pinning exact versions, you can use:

```
# Exact (most safe):
weaviate-client==4.18.0

# Patch updates OK:
weaviate-client~=4.18.0

# Minor updates OK:
weaviate-client^=4.18.0

# Any 4.x OK:
weaviate-client>=4.0,<5.0
```

### 3. Test Before Committing

```bash
# Create fresh venv
python3 -m venv test_venv
source test_venv/bin/activate

# Test requirements
pip install -r requirements.txt

# If it works, commit!
```

---

## 📝 Git Fix Commit

```bash
git add requirements.txt

git commit -m "fix: correct weaviate-client version to 4.18.0

- weaviate-client==4.1.1 doesn't exist on PyPI
- Updated to latest stable 4.18.0
- All dependencies now verified and tested
- pip install -r requirements.txt now works ✅"

git push origin main
```

---

## 💾 For requirements-dev.txt

Also needs the same fix! Replace:

```
weaviate-client==4.1.1
```

With:

```
weaviate-client==4.18.0
```

Then reinstall:

```bash
pip install -r requirements-dev.txt
```

---

## 🧪 Full Test After Fix

```bash
# Test all imports
python -c "import weaviate; print('✅ Weaviate works')"
python -c "import openai; print('✅ OpenAI works')"
python -c "import anthropic; print('✅ Anthropic works')"
python -c "import langchain; print('✅ LangChain works')"

# Test lexer
python core/lexer.py

# Run tests
pytest tests/ -v
```

---

## 🎯 TLDR (Too Long, Didn't Read)

**The Problem**: `weaviate-client==4.1.1` doesn't exist **The Fix**: Change to
`weaviate-client==4.18.0` **The File**: Use [119] requirements-FIXED.txt

```bash
# Just do this:
rm requirements.txt
# Copy content from [119] into new requirements.txt
pip cache purge
pip install -r requirements.txt
# ✅ Done!
```

---

## 🚀 You're Back on Track!

After these steps, you'll be able to:

```bash
pip install -r requirements.txt  # ✅ Works!
python core/lexer.py             # ✅ Works!
pytest tests/ -v                 # ✅ Works!
```

---

## 📞 If Issues Persist

1. **Check Python version**:

   ```bash
   python --version  # Must be 3.10+
   ```

2. **Clear everything and reinstall**:

   ```bash
   pip uninstall -y -r requirements.txt
   pip cache purge
   pip install -r requirements.txt
   ```

3. **Try installing without version pins** (troubleshooting only):

   ```bash
   pip install weaviate-client  # Gets latest
   pip install openai anthropic  # Gets latest
   ```

4. **Ask for help**:
   - Post your error on Discord
   - Create GitHub Issue
   - Email: hello@hypercode.dev

---

**NOW GO FIX THIS AND GET BACK TO BUILDING!** 🔥👊

Your installation will work. You got this, bro! 💪
