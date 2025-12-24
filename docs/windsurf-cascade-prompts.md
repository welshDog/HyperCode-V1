# HyperCode Cascade Prompts: Ready-to-Paste AI Automation 🤖

These are **battle-tested prompts** you copy directly into Windsurf's Cascade Write/Agent mode.
Each one sets up a different "self-healing" workflow. Pick the one that fits your need.

---

## 🎯 PROMPT 1: "Full Self-Fix Mode" (The Main One)

**Use this when tests are failing and you want Windsurf to debug + fix + verify automatically.**

Paste this into Cascade Write mode:

```
You are HyperCode's autonomous maintenance agent.

Your mission: Read the repo, identify failing tests or build errors, then iteratively fix them.

Protocol:
1. Run the test/build command (npm test / pytest / cargo test)
2. Capture the FULL error output
3. Read the source file(s) causing the failure
4. Propose a minimal fix (surgical edits only, <20 lines changed per cycle)
5. Apply the fix
6. Re-run tests
7. If tests pass: update CHANGELOG.md with what you fixed
8. If tests fail: analyze why and iterate (don't give up)

Constraints:
- NEVER modify protected directories (.git, .github, node_modules, venv, .windsurf)
- NEVER commit or push; only show diffs for approval
- NEVER add dependencies without asking first
- Keep each change reversible
- Respect the .windsurfrules file

Go. Show your work as you go.
```

---

## 🎯 PROMPT 2: "Build New Feature + Self-Fix While Building"

**Use this when you want Windsurf to implement a new feature AND keep tests green the whole time.**

```
You are building a new HyperCode feature.

Step 1: Create a plan.md file that lists every step to implement [FEATURE NAME].
  - Be detailed: what files get created/modified, what tests get added, what's the success criteria.
  - Format: numbered checklist with brief descriptions.

Step 2: Follow your plan step by step.
  - After each checklist item:
    - Update plan.md to mark it done
    - Run the full test suite (npm test / pytest / cargo test)
    - If tests fail: stop, debug, fix, then continue
    - Only move to the next item when tests are green

Step 3: When done:
  - Verify ALL tests pass
  - Verify NO new linting warnings (npm run lint / pylint)
  - Update README.md with the new feature
  - Summarize what was added in CHANGELOG.md

Constraints:
- Write tests ALONGSIDE code, not after
- Keep functions < 100 lines
- Use descriptive names (no abbreviations)
- Follow HyperCode neurodivergent-first philosophy: clarity > cleverness
- Ask before adding new dependencies

Start by creating the plan.md file.
```

---

## 🎯 PROMPT 3: "Refactor + Self-Fix" (For Code Cleanup)

**Use this when you want to modernize or reorganize code without breaking functionality.**

```
You are refactoring HyperCode code for clarity and maintainability.

Objective: [DESCRIBE THE REFACTOR: e.g., "Move all parser logic into separate module", "Simplify the AST node structure", etc.]

Workflow:
1. Read the current code structure
2. Design a plan for the refactor (show it to me first)
3. Create new files/modules as needed
4. Move and adapt code gradually (not all at once)
5. After each major change: run tests (npm test / pytest / cargo test)
6. Keep old tests passing; don't break public APIs
7. Update imports and documentation
8. Once complete: update CHANGELOG.md

Guardrails:
- NEVER delete code without tests confirming it's unused
- NEVER change public function signatures without updating all call sites
- Keep backward compatibility unless explicitly breaking (then document it)
- Test coverage should stay >= 80%

Start by showing me the refactor plan. I'll approve before you make changes.
```

---

## 🎯 PROMPT 4: "Surgical Inline Fix" (For Tiny Bugs)

**Use this for ONE broken function or section—keep changes super focused.**

```
You are making a surgical fix to a specific bug.

Context:
- File: [PATH/TO/FILE]
- Problem: [DESCRIBE THE BUG: e.g., "Parser hangs on recursive input", "Lexer skips whitespace incorrectly"]
- Expected behavior: [WHAT SHOULD HAPPEN]

Workflow:
1. Read the buggy function carefully
2. Identify the root cause (1-2 lines usually)
3. Propose a fix (minimal, <5 lines changed if possible)
4. Apply it
5. Run tests to verify the bug is fixed and nothing else broke
6. Update CHANGELOG.md with the fix

Constraints:
- ONLY modify the buggy function, not surrounding code
- Don't refactor while fixing (separate concerns)
- Add a test case that catches this bug if it doesn't exist
- Keep the public interface unchanged

Go. Show me the diff before you commit anything.
```

---

## 🎯 PROMPT 5: "Linting + Format Fix" (Keep Code Clean)

**Use this when you want to auto-fix lint warnings and code style issues.**

```
You are fixing all linting and formatting issues in HyperCode.

Workflow:
1. Run linter: `npm run lint` / `pylint *.py` / `cargo clippy`
2. Capture ALL warnings
3. Fix them one category at a time:
   - Unused imports
   - Inconsistent naming
   - Code style issues
   - Type hints (if applicable)
4. After fixing each category: re-run linter
5. Verify tests still pass
6. Update CHANGELOG.md: "Fixed linting and formatting"

Constraints:
- ONLY fix style issues, don't change logic
- Respect HyperCode naming conventions (PascalCase for types, camelCase for functions)
- Don't over-engineer; just clean up what's there

Go. Show what you're fixing as you go.
```

---

## 🎯 PROMPT 6: "Docs Sync" (Keep Documentation Fresh)

**Use this when code changes and docs need updating.**

```
You are keeping HyperCode documentation in sync with the code.

Workflow:
1. Read the code and existing README.md / ARCHITECTURE.md / docs/
2. Identify what's out of date or missing:
   - New APIs not documented
   - Examples that don't match current code
   - Architecture changes not reflected
   - Missing explanation for features
3. Update docs to match reality
4. Run tests to verify examples (if they're executable)
5. Update CHANGELOG.md: "Updated documentation for X, Y, Z"

Standards:
- Docs should be inclusive: explain the "why", not just the "what"
- Include examples for every major feature
- Keep language accessible (neurodivergent-friendly)
- Link between related docs

Go. Show me what you're updating as you go.
```

---

## 📋 HOW TO USE THESE IN WINDSURF

1. **Open Windsurf with your HyperCode repo open** (whole folder, not single file)
2. **Open Cascade** (usually right panel or keyboard shortcut)
3. **Switch to Write or Agent mode** (depending on your Windsurf version)
4. **Paste the prompt** that matches what you need (Prompt 1–6 above)
5. **Fill in [BRACKETED] placeholders** with your specifics
6. **Hit Enter/Send**
7. **Watch it work**: Windsurf will edit files, run commands, iterate until tests pass
8. **Review diffs** in the Cascade panel before approving each change
9. **Let it loop**: It'll keep going until everything is green

---

## 🚨 SAFETY CHECK: Before You Use These

Make sure:
- ✅ `npm test` / `pytest` / `cargo test` runs and is reliable
- ✅ `.windsurfrules` file is in repo root
- ✅ `.gitignore` includes `.windsurf/` and `.windsurfrules`
- ✅ You have git set up (so Windsurf can see `git status` / `git diff`)
- ✅ You're NOT on the `main` branch (work on `feature/` or `bugfix/` branches)
- ✅ You have a recent backup (just in case)

---

## 🎓 Pro Tips

### Tip 1: Chain Prompts
Run Prompt 1 (self-fix) → then Prompt 5 (lint fix) → then Prompt 6 (docs sync). 
Full CI-like pipeline in Windsurf.

### Tip 2: Use Memories for Context
Create a Memory in Windsurf's memory panel with HyperCode's core concepts:
- "Spatial logic principle: code should represent visual/spatial thinking"
- "Neurodivergent-first means: clarity > brevity, accessibility > cleverness"
- Paste relevant snippets from HyperCode's manifesto

Then reference it in prompts: "Remember the spatial logic principle when naming variables."

### Tip 3: Iterate Prompts
If a prompt doesn't work perfectly, tweak it:
- "Run tests first" → tell it which tests to run
- "Minimal fix" → add "max 10 lines changed"
- "Don't break tests" → add "check git diff before finishing"

### Tip 4: One Branch Per Feature
Always make a new branch for Cascade work:
```bash
git checkout -b feature/parser-optimization
# Then run Cascade prompts
# Then review diffs
# Then merge to main
```

---

## 🎯 Quick Start: Do This Right Now

1. **Copy `.windsurfrules` content** from the previous file into your repo root as `.windsurfrules`
2. **Test your build**: `npm test` / `pytest` / `cargo test` (make it work)
3. **Open Windsurf**, point it at your HyperCode repo
4. **Open Cascade**, paste **Prompt 1** (Self-Fix Mode)
5. **Watch the magic** ✨

That's it. Windsurf is now your maintenance daemon.

---

## 📝 NOTES

- These prompts assume you're using Windsurf **v2.0+** with Cascade Write/Agent mode
- If you're on an older version, some features might differ (adjust as needed)
- For custom stacks or unusual setups, modify the prompts to fit your test/build commands
- Always run prompts on non-main branches first to test

---

**NOW GO BUILD SOMETHING AMAZING.** 🚀
The future of HyperCode is you + Windsurf working as one.

Bro, you've got this. 💓👊
