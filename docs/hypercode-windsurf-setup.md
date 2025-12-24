# HyperCode + Windsurf: Self-Healing AI Setup Guide 🚀

A complete setup to turn Windsurf into your HyperCode maintenance daemon. This file walks you through everything—rules, cascade prompts, test setup, and memory config.

---

## 🎯 PART 1: Project Structure & Commands

Before Cascade can fix itself, it needs to know how to succeed. Set these up first.

### Step 1A: Your test & build commands

In your HyperCode repo root, make sure these work:

```bash
# Pick your stack—here are examples:

# Node/JavaScript/TypeScript
npm test              # Your unit tests
npm run lint          # Code quality
npm run build         # Build step

# Python
pytest                # Run tests
pylint *.py           # Linting
python setup.py build # Build

# Go
go test ./...         # Tests
go vet ./...          # Vet
go build ./...        # Build

# Rust
cargo test            # Tests
cargo clippy          # Linter
cargo build           # Build
```

**Test all of these NOW** to make sure they're bulletproof. Windsurf will rely on them.

### Step 1B: Create a `.gitignore` for safety

```gitignore
# Windsurf
.windsurf/
.windsurfrules

# Build artifacts
dist/
build/
*.o
*.a

# Dependencies
node_modules/
venv/
__pycache__/

# Secrets (if any)
.env
.env.local
```

---

## 🧠 PART 2: Windsurf Rules File

Create this at your repo root: `.windsurfrules`

This tells Windsurf how to behave when in Cascade agent mode.

```yaml
# .windsurfrules
# HyperCode Windsurf Agent Configuration

# ============================================================================
# IDENTITY & CONTEXT
# ============================================================================
project_name: "HyperCode"
purpose: "Neurodivergent-first, AI-compatible programming language"
philosophy: |
  - Accessibility first: spatial logic, minimal noise, inclusive design
  - Neurodivergent brain patterns matter: ADHD, dyslexia, autism considered
  - AI-native: works with GPT, Claude, Mistral, Ollama without rewrites
  - Experimental but reliable: test coverage is non-negotiable
  - Open source, professional DevOps from day one

# ============================================================================
# SAFETY BOUNDARIES (What Cascade CAN'T do)
# ============================================================================
forbidden_actions:
  - "Never commit to main without explicit user approval"
  - "Never delete directories without asking first"
  - "Never change secrets, env vars, or .env files"
  - "Never pull new dependencies without listing them in the plan"
  - "Never modify CI/CD or GitHub Actions without review"
  - "Never run rm -rf or destructive commands without confirmation"

protected_directories:
  - ".git/"
  - ".github/"
  - "node_modules/"
  - "venv/"
  - "__pycache__/"
  - ".windsurf/"

# ============================================================================
# SAFE ACTIONS (What Cascade CAN do freely)
# ============================================================================
safe_commands:
  - "npm test"
  - "npm run lint"
  - "npm run build"
  - "npm run dev"
  - "pytest"
  - "pylint"
  - "go test ./..."
  - "go vet ./..."
  - "cargo test"
  - "cargo clippy"
  - "git status"
  - "git diff"

# ============================================================================
# CODE STYLE & ARCHITECTURE
# ============================================================================
code_standards:
  - "Use descriptive variable names; avoid abbreviations except well-known ones (e.g., idx, msg)"
  - "Every function should have a docstring/comment explaining intent"
  - "Neurodivergent accessibility: prefer clarity over cleverness"
  - "SOLID principles: single responsibility, open/closed, etc."
  - "Test-driven: write tests before or alongside code"
  - "No magic numbers; use named constants"
  - "Keep functions <100 lines; break into smaller units"

naming_conventions:
  - "Classes/Types: PascalCase (e.g., HyperLexer, ASTNode)"
  - "Functions/methods: camelCase (e.g., parseExpression, buildAST)"
  - "Constants: UPPER_SNAKE_CASE (e.g., MAX_RECURSION_DEPTH)"
  - "Private members: _leadingUnderscore (e.g., _internalState)"

# ============================================================================
# TESTING REQUIREMENTS
# ============================================================================
testing_rules:
  - "All PRs/diffs must have passing tests before merge"
  - "Aim for 80%+ test coverage on core logic"
  - "Test names should be descriptive: test_parseExpression_withValidInput"
  - "Include edge cases: empty input, null, overflow, etc."
  - "Run full test suite after any refactor: `npm test` or `pytest`"

# ============================================================================
# DOCUMENTATION RULES
# ============================================================================
docs_updates:
  - "If you add or change an API, update README.md"
  - "If you add a new module, add a docstring and reference in ARCHITECTURE.md"
  - "If you fix a bug, add a test case for it so it doesn't regress"
  - "Keep examples in docs runnable and up-to-date"

# ============================================================================
# BRANCHING & VERSION CONTROL
# ============================================================================
git_workflow:
  - "Work on feature branches, never directly on main"
  - "Branch naming: feature/*, bugfix/*, docs/*, refactor/*"
  - "Commit messages should be clear: 'Fix parser loop condition' not 'stuff'"
  - "Squash related commits before asking for review"
  - "Never force-push to shared branches"

# ============================================================================
# WHEN SOMETHING BREAKS: Self-Fix Protocol
# ============================================================================
self_fix_protocol: |
  1. Run tests: `npm test` / `pytest` / `cargo test`
  2. Capture the failure output and line numbers
  3. Read the relevant source file(s)
  4. Propose a minimal fix (usually <20 lines changed)
  5. Apply the diff
  6. Re-run tests
  7. If tests pass, update CHANGELOG.md with the fix
  8. If tests still fail, iterate (don't give up after one try)
  9. Never make unrequested changes to unrelated code

# ============================================================================
# CASCADE AGENT MODE INSTRUCTIONS
# ============================================================================
cascade_mode: |
  When running in Cascade Write/Agent mode:
  
  - Always start by reading the error/failing test completely
  - Show your plan before making changes
  - Make one surgical change at a time, then re-test
  - If you're unsure, ask the user before acting
  - Use git diff to review your own changes
  - Stop when all tests pass; don't over-engineer
  - Respect the protected_directories and forbidden_actions lists
  - If a fix requires new dependencies, list them and wait for approval

# ============================================================================
# HyperCode-Specific Context
# ============================================================================
hypercode_context: |
  - HyperCode is a neurodivergent-first DSL, not a general-purpose language
  - Core features: spatial logic, visual semantics, minimal syntax noise
  - It should work with any major AI model without major rewrites
  - Every feature should have a test and an example
  - Documentation should be inclusive: explain the "why", not just the "what"
  - Think about ADHD/dyslexia/autism brain patterns when designing features
