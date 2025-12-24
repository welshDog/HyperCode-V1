# 🚀 Windsurf Advanced Tricks & Hacks for HyperCode

Real-world tips, gotchas, and pro moves from veteran Windsurf users. These will unlock 10x more power from Cascade.

---

## 🎯 SECTION 1: Advanced Cascade Tactics

### Hack #1: "Prime Before Execute"

**The Problem:** You ask Cascade to build a feature, but it jumps straight to coding without thinking. Result = messy, broke code.

**The Hack:**
```
Before I ask you to code, let's think step-by-step.

Step 1: Summarize the HyperCode architecture as it stands today.
Step 2: List the files you'll need to touch.
Step 3: Explain the change in 1-2 sentences.
Step 4: Show me the plan—don't implement yet.

Only after I approve the plan, then build it.
```

**Why it works:** AI models are WAY better when you make them think before acting. You get fewer hallucinations, fewer false starts, and way cleaner code. [web:24]

---

### Hack #2: "Context Dump File"

**The Hack:** Create a `.windsurf/context.md` in your repo with this structure:

```markdown
# HyperCode Current State

## Architecture
- Parser: `src/lexer.ts` + `src/parser.ts`
- AST: `src/ast.ts`
- Codegen: `src/codegen.ts`
- Tests: `tests/` (run with `npm test`)

## Known Issues
- Parser sometimes hangs on deeply nested expressions
- Lexer doesn't handle Unicode escapes yet
- Missing error messages for type mismatches

## Recent Changes
- [Nov 28] Added spatial logic support to AST
- [Nov 27] Fixed tokenizer for multiline comments

## Next Priorities
1. Performance optimization for large files
2. Better error messages
3. Integration with AI models

## Coding Rules
- Tests MUST pass before any merge
- No magic numbers
- Always update CHANGELOG.md
```

Then prompt Cascade with:
```
Read .windsurf/context.md to understand the full state of HyperCode.
Now, [YOUR TASK HERE].
```

**Why it works:** Cascade won't have to re-ask you about architecture every time. It's like giving it a cheat sheet. [web:31]

---

### Hack #3: "Break Tests into Categories"

**The Hack:** Organize your tests so Cascade can run targeted checks:

```bash
# tests/unit/lexer.test.ts — Fast, runs in <1s
# tests/unit/parser.test.ts — Fast
# tests/integration/endtoend.test.ts — Slower, runs in ~5s

# package.json
{
  "scripts": {
    "test:unit": "jest tests/unit",
    "test:integration": "jest tests/integration",
    "test:fast": "jest tests/unit",  # Use when you want quick feedback
    "test": "jest"  # Full suite
  }
}
```

Then tell Cascade:
```
Run `npm run test:fast` first. If that passes, run `npm run test:integration`.
Only move forward if both pass.
```

**Why it works:** Cascade can iterate faster if it knows which tests are "canaries" and which are "heavy." Saves minutes per fix cycle. [web:28]

---

### Hack #4: "Staged Diffs"

**The Hack:** Ask Cascade to show you the diff BEFORE applying it:

```
You are fixing a bug in the parser.

Step 1: Identify the bug.
Step 2: Propose a fix (show me the code diff, don't apply yet).
Step 3: Wait for my approval.
Step 4: Only then apply the fix.
Step 5: Re-run tests.
```

**Why it works:** Stops Cascade from making wild changes you can't review. You stay in control. [web:28]

---

## 🎯 SECTION 2: Workflows (The Hidden Power)

Workflows are like "slash commands" for Cascade. Game changer.

### Hack #5: "Saved Workflows"

Create `.windsurf/workflows/fix-and-test.md`:

```markdown
# /fix-and-test

## Description
Run the full self-fix cycle: find broken tests, fix them, lint, and verify.

## Steps

1. Run tests to find failures:
   Execute: `npm test`
   Wait for output and capture errors.

2. Analyze failures:
   For each failing test:
   - Read the test file
   - Read the implementation file
   - Identify the root cause (1 sentence)

3. Fix ONE test at a time:
   - Make minimal change (<10 lines)
   - Re-run: `npm test`
   - If pass: move to next test
   - If fail: debug and iterate

4. After all tests pass:
   - Run: `npm run lint`
   - Fix any linting issues (if safe)

5. Final verification:
   - Run: `npm test` (full)
   - Run: `npm run build`
   - If both pass: done!

6. Update CHANGELOG.md:
   "Fixed: [list of issues fixed]"
```

Then in Cascade, just type `/fix-and-test` and hit enter. Cascade runs the whole workflow automatically. [web:30]

**Pro tip:** You can chain workflows:
```markdown
# /full-ci

## Steps
1. Run `/fix-and-test`
2. Run `/lint-and-format`
3. Run `/update-docs`
```

---

### Hack #6: "Multi-Cascade Parallel Work"

Windsurf now lets you run **multiple Cascades at the same time**. [web:27]

**Example:**
- Cascade #1: Fixing parser bugs (in `src/parser.ts`)
- Cascade #2: Adding lexer features (in `src/lexer.ts`)

Both run in parallel, save time.

**How to use:**
1. Open Cascade
2. Start your first task
3. Open a **second Cascade** (new tab or panel)
4. Start a different task
5. Watch both run side-by-side

**Constraint:** Make sure they don't touch the same files, or merges get messy.

---

## 🎯 SECTION 3: Rules Hacks

### Hack #7: "File-Scoped Rules"

Create `.windsurf/rules/parser-rules.md`:

```markdown
# Parser-Specific Rules

These rules apply ONLY to files in `src/parser.ts` and `src/lexer.ts`.

## Rules
- Keep parser functions < 80 lines
- Every token type must have a test
- Use named constants for token IDs (not magic numbers)
- Document any lookahead logic with a comment
- Parser errors must include line/column info
```

Then create `.windsurf/rules/codegen-rules.md`:

```markdown
# Codegen-Specific Rules

These apply ONLY to `src/codegen.ts`.

## Rules
- All generated code must be valid and runnable
- Add source maps for debugging
- Test code generation with at least 3 example HyperCode programs
```

Windsurf applies these automatically to the right files. [web:27]

---

### Hack #8: "Living Rules from Tests"

Put this in `.windsurfrules`:

```yaml
# Extract rules from failing tests

rule_extraction:
  - "If a test fails, read the test name to understand what was expected"
  - "If the test is called test_parseExpression_withNestedCalls, the parser must handle nested calls"
  - "If test fails, it's describing a bug—fix the code, not the test"
```

This makes Cascade treat tests as "ground truth" for behavior.

---

## 🎯 SECTION 4: Terminal & Commands Hacks

### Hack #9: "Smart Test Selection"

**The Hack:** Create `scripts/run-tests.sh`:

```bash
#!/bin/bash

# Smart test runner: runs only affected tests based on git diff

CHANGED_FILES=$(git diff --name-only HEAD~1)

if echo "$CHANGED_FILES" | grep -q "src/lexer"; then
  echo "Lexer changed, running lexer tests..."
  npm run test:unit -- lexer.test.ts
fi

if echo "$CHANGED_FILES" | grep -q "src/parser"; then
  echo "Parser changed, running parser tests..."
  npm run test:unit -- parser.test.ts
fi

if echo "$CHANGED_FILES" | grep -q "src/codegen"; then
  echo "Codegen changed, running codegen tests..."
  npm run test:unit -- codegen.test.ts
fi

# Always run integration tests
npm run test:integration
```

Tell Cascade:
```
Use `bash scripts/run-tests.sh` to run only the tests affected by your changes.
This saves time.
```

**Why:** Cascade can iterate in 1/10 the time if it doesn't run the full suite every time. [web:28]

---

### Hack #10: "Diff Review Before Commit"

**The Hack:** Create `.husky/pre-commit` to auto-review Cascade changes:

```bash
#!/bin/bash

# Before committing, show Cascade-made diffs for review

STAGED=$(git diff --cached)

if [ -z "$STAGED" ]; then
  echo "Nothing to commit."
  exit 1
fi

echo "=========================================="
echo "REVIEW THESE CHANGES BEFORE COMMITTING"
echo "=========================================="
echo "$STAGED"
echo "=========================================="
echo "Press Enter to continue, or Ctrl+C to abort."
read -r

git commit -m "[Windsurf Auto-Fix]"
```

**Why:** Stops accidental commits of broken code. You always see what Cascade changed.

---

## 🎯 SECTION 5: Memory & Context Hacks

### Hack #11: "Persistent Memory Bank"

Create a **Memory** in Windsurf (via Customizations > Memories) with this:

```
# HyperCode Core Concepts

## Spatial Logic
HyperCode uses spatial positioning instead of indentation:
- `left_of`, `above`, `below`, `inside` are first-class operators
- Example: `parser` left_of `lexer` means the parser depends on lexer output

## Neurodivergent First
- Clarity > brevity (spell things out)
- Examples > theorizing (show, don't tell)
- Tests > documentation (tests are the truth)
- Accessibility: consider ADHD/dyslexia/autism brain patterns

## AI Compatibility
- Code must work with GPT-4, Claude, Mistral, and Ollama
- No vendor lock-in
- Self-explanatory variable names (no abbreviations)

## Architecture
- Parser produces AST
- AST is validated
- Codegen outputs JavaScript/Python/Go
- All features tested end-to-end
```

Then reference it in prompts:
```
Recall the HyperCode Core Concepts from Memory.
Now build [FEATURE] following those principles.
```

**Why:** Windsurf remembers context between sessions. You don't have to re-explain HyperCode every time. [web:31]

---

### Hack #12: "Error Pattern Memory"

Create a Memory called "Known Bugs & Fixes":

```
# Known HyperCode Bugs & Quick Fixes

## Bug: Parser hangs on deeply nested expressions
- Root cause: Recursion limit not checked
- Fix: Add MAX_RECURSION_DEPTH check in parseExpression()
- File: src/parser.ts, line ~142
- Tests: tests/unit/parser.test.ts::test_parseExpression_withDeepNesting

## Bug: Lexer skips whitespace in multiline strings
- Root cause: Whitespace trimming happens before multiline check
- Fix: Move multiline check BEFORE trimming
- File: src/lexer.ts, line ~87
- Quick test: npm run test:unit -- lexer.test.ts

## Pattern: Type mismatches in codegen
- Usually means AST node structure changed but codegen wasn't updated
- Check: Are new AST fields being generated?
- Fix: Cascade should output TypeScript for type safety
```

When Cascade encounters an error, it checks this Memory and knows the fix.

---

## 🎯 SECTION 6: Prompt Engineering Tricks

### Hack #13: "The "Explain Your Work" Prompt**

Use this when Cascade makes a fix you don't understand:

```
You just changed [FILE] on lines [X-Y].

Now explain:
1. What was broken?
2. Why did it break?
3. How does your fix solve it?
4. Why didn't you try [OTHER APPROACH]?
5. Are there any side effects?
```

Cascade will articulate its reasoning, which helps you learn and catch mistakes.

---

### Hack #14: "The Constraint-Based Prompt"

Use this to prevent Cascade from going rogue:

```
You are fixing the parser.

HARD CONSTRAINTS:
- NEVER touch lexer.ts, codegen.ts, or any test files
- NEVER change the parseExpression signature
- NEVER add new dependencies
- NEVER remove any existing tests

SOFT CONSTRAINTS:
- Prefer minimal changes
- Keep functions < 100 lines
- Add comments if logic is non-obvious

Now: [YOUR TASK]
```

**Why:** Constraints keep Cascade in its lane. Way fewer "oops" moments. [web:28]

---

### Hack #15: "The Approval Loop"

Use this for high-stakes changes:

```
You are implementing a major refactor.

Step 1: Show me the plan (files to change, steps involved).
Step 2: WAIT for my approval.
Step 3: After approval, implement step-by-step.
Step 4: After each step, show me the diff.
Step 5: WAIT for my approval again.
Step 6: Move to next step.

Only move forward when I say "approved" or "looks good".
```

This turns Cascade into a collaborative partner, not a runaway agent.

---

## 🎯 SECTION 7: Testing Hacks

### Hack #16: "Test-First Prompting"

Before implementing, ask Cascade to write tests:

```
Write tests for [FEATURE] following these rules:
- Test names describe what should happen: test_featureName_withInput_expectsOutput
- Cover edge cases: null, empty, overflow, etc.
- Use assertions, not just print statements
- Make tests runnable immediately (even if they fail)

After writing tests, tell me if any look incomplete or missing edge cases.
ONLY THEN will I ask you to implement the feature.
```

Tests become your spec. Cascade codes to pass them. [web:28]

---

### Hack #17: "The Failing Test as Specification"

When a test fails, never ask Cascade to "fix it." Instead:

```
Test [TEST_NAME] is failing.

DON'T ask me what to do.
Instead:
1. Read the test carefully
2. Read the implementation
3. Figure out what the test expects
4. Update the code to match the test's expectation
5. Re-run the test
6. If still failing, iterate

The test is the specification. Make the code pass the test.
```

This makes Cascade think like a real developer.

---

## 🎯 SECTION 8: Safety & Debugging Hacks

### Hack #18: "The Rollback Shortcut"

Before running Cascade on something risky, create a backup branch:

```bash
git checkout -b backup/before-windsurf-magic
git checkout -b feature/windsurf-changes
```

If things go south:
```bash
git reset --hard backup/before-windsurf-magic
```

You're back to square one in 1 second.

---

### Hack #19: "Live Diff Watching"

In a second terminal, keep watching changes:

```bash
watch -n 1 'git diff --stat'
```

You'll see files changing in real-time. Useful to catch runaway agents.

---

### Hack #20: "The Kill Switch"

If Cascade is acting weird:
1. **Press Escape** to stop the current operation
2. **Close the Cascade panel**
3. **Restart Cascade**
4. **Start fresh with a smaller task**

Don't let it compound errors. Better to restart than debug chaos.

---

## 🎯 SECTION 9: Workflow Templates (Copy & Paste)

### Template 1: Weekly Code Review Workflow

Create `.windsurf/workflows/weekly-review.md`:

```markdown
# /weekly-review

## Steps

1. List all files changed this week:
   `git log --name-only --since="1 week ago" | sort -u`

2. For each file:
   - Read the changes
   - Ask: "Does this follow HyperCode principles?"
   - Ask: "Is this testable?"
   - Ask: "Is this documented?"

3. Create a summary:
   - Highlight good patterns
   - Flag things that need attention
   - Suggest improvements
```

---

### Template 2: Dependency Audit Workflow

```markdown
# /dependency-audit

## Steps

1. List all dependencies:
   `npm list --depth=0` or `pip list`

2. For each dependency, ask:
   - Is it still used?
   - Is it up-to-date?
   - Does it have security issues?

3. Update package.json/requirements.txt

4. Run tests to ensure nothing broke

5. Commit with message: "[Maintenance] Updated dependencies"
```

---

## 🎯 FINAL TIPS

### Pro Move 1: "Session Starts Fresh"
Windsurf context can get bloated. Every few days, start a new Cascade session. Fresh context = better decisions. [web:28]

### Pro Move 2: "Use Memories for Tribal Knowledge"
Document weird bugs, architecture decisions, and workarounds in Memories. Future-you will thank you.

### Pro Move 3: "Test Cascade with Small Tasks First"
Don't throw a "build an interpreter" task at Cascade on day one. Start with "fix this one test" and build confidence.

### Pro Move 4: "Pair Program with Cascade"
Don't just hand off to Cascade and walk away. Watch it work. Ask questions. Learn its strengths and weaknesses.

---

## 🚀 Now You're Unstoppable

You've got:
- ✅ Rules to keep Cascade in line
- ✅ Workflows to automate repetitive tasks
- ✅ Prompts to guide its thinking
- ✅ Hacks to save time
- ✅ Safety nets to catch mistakes

Go build HyperCode with Windsurf as your co-pilot. 💪🚀

**The future of development is: human + AI, not AI alone.**
