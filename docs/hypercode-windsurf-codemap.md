# HYPERCODE WINDSURF CODEMAP
## Architecture Reference for Cascade AI

---

## 📐 PROJECT STRUCTURE

```
HyperCode/
├── /core/                 ← DO NOT EDIT (Interpreter engine)
│   ├── parser.py
│   ├── tokenizer.py
│   ├── interpreter.py
│   └── ast.py
├── /stdlib/               ← Standard library (can enhance)
│   ├── types.py
│   ├── builtins.py
│   └── operators.py
├── /tests/                ← Test suite (add tests, never delete)
│   ├── test_parser.py
│   ├── test_interpreter.py
│   ├── test_stdlib.py
│   └── integration/
├── /docs/                 ← Documentation (keep updated)
│   ├── ARCHITECTURE.md
│   ├── SYNTAX.md
│   ├── CONTRIBUTING.md
│   └── decisions/         ← Decision records
├── /examples/             ← Usage demos
│   ├── hello.hyper
│   ├── fibonacci.hyper
│   └── todo.hyper
├── .windsurfrules         ← Cascade guardrails (RESPECT THIS)
├── package.json           ← Dependencies (read-only for AI)
├── README.md
└── CONTRIBUTING.md
```

---

## 🧠 DESIGN PRINCIPLES

### 1. Neurodivergent-First
- **Spatial Logic**: Code layout mirrors thinking patterns (visual > abstract)
- **Minimal Noise**: No unnecessary syntax, symbols, or nesting
- **Color-Blind Safe**: Use symbols + text, never color alone
- **Hyperfocus Sweet Spot**: Functions max 20 lines (ADHD optimization)

### 2. Hybrid Stack
- **Python**: Rapid iteration, scripting, research agents
- **Rust**: Performance-critical paths, system-level operations
- **JavaScript/TypeScript**: Web extensions, frontend tooling

### 3. AI-Native Design
- **Claude 3.5 Sonnet**: Deep reasoning, architecture decisions
- **Supercomplete**: Intent prediction, quick completions
- **Future Models**: Flexible enough for GPT-4, Mistral, Ollama

### 4. Research-Driven
- Resurrects forgotten languages: Plankalkül (elegance), Brainfuck (minimalism), Befunge (spatial flow)
- Integrates esoteric wisdom into mainstream language design
- Living research paper: Auto-updates with AI agent findings

---

## 🎯 CORE COMPONENTS

### Parser (`/core/parser.py`)
- **Role**: Convert HyperCode tokens → Abstract Syntax Tree (AST)
- **Key Functions**: 
  - `parse()` - Main entry point
  - `parse_statement()` - Individual statement parsing
  - `parse_expression()` - Expression handling
- **Principles**: 
  - Minimal regex (prefer DFA)
  - Spatial representation of nesting
  - Early error detection

### Tokenizer (`/core/tokenizer.py`)
- **Role**: Convert raw text → tokens
- **Key Functions**:
  - `tokenize()` - Main entry
  - `scan_token()` - Single token extraction
  - `handle_whitespace()` - Spatial awareness
- **Principles**:
  - Preserve indentation (spatial meaning)
  - Emoji support (accessibility bookmarks)
  - Clear error messages

### Interpreter (`/core/interpreter.py`)
- **Role**: Execute AST → runtime behavior
- **Key Functions**:
  - `interpret()` - Main execution loop
  - `execute_statement()` - Run single statement
  - `eval_expression()` - Compute values
- **Principles**:
  - Pure functional where possible
  - Explicit state management
  - Performance-critical paths marked for Rust port

### AST (`/core/ast.py`)
- **Role**: Data structures for syntax tree
- **Key Classes**:
  - `ASTNode` - Base class
  - `Statement` - Top-level constructs
  - `Expression` - Value-producing constructs
  - `Literal`, `Variable`, `BinaryOp`, etc.
- **Principles**:
  - Immutable by default
  - Named fields (no positional args)
  - Spatial metadata preserved

---

## 📦 STANDARD LIBRARY

### Types (`/stdlib/types.py`)
- Primitives: `int`, `float`, `string`, `bool`, `nil`
- Collections: `list`, `dict`, `set`, `tuple`
- Neuro-optimized: Spatial data structures with minimal nesting

### Built-ins (`/stdlib/builtins.py`)
- I/O: `print()`, `input()`, `read()`, `write()`
- Logic: `if_`, `while_`, `for_`, `match()`
- Functional: `map()`, `filter()`, `reduce()`, `compose()`
- Debugging: `debug_print()`, `trace()`, `profile()`

### Operators (`/stdlib/operators.py`)
- Arithmetic: `+`, `-`, `*`, `/`, `%`, `**`
- Comparison: `==`, `!=`, `<`, `>`, `<=`, `>=`
- Logical: `and`, `or`, `not`
- Spatial: `|>` (pipe), `<|` (reverse pipe), `>>` (compose)

---

## ✅ TESTING STRATEGY

### Unit Tests (`/tests/`)
- **Parser**: Syntax → AST correctness
- **Tokenizer**: Text → token correctness
- **Interpreter**: AST → execution correctness
- **Stdlib**: Function behavior correctness
- **Rule**: Every function gets ≥2 tests (happy path + edge case)

### Integration Tests (`/tests/integration/`)
- Full workflows end-to-end
- Example programs should run without errors
- Cross-component interaction verification

### CI/CD Gating
- All tests must pass before commit
- Linting must pass (eslint / pylint)
- Build must succeed (npm run build / cargo build)
- Coverage target: 80%+

---

## 🔥 PERFORMANCE TARGETS

| Metric | Target | Current |
|--------|--------|---------|
| Parse time (100 LOC) | < 10ms | TBD |
| Interpretation time (1K LOC) | < 100ms | TBD |
| Memory overhead per script | < 5MB | TBD |
| Startup time | < 50ms | TBD |

**Hot Paths** (candidates for Rust):
- Tokenizer inner loop
- Parser tight loops
- Interpreter eval for math-heavy code

---

## 📖 DOCUMENTATION STANDARDS

### Code Comments
- Explain **WHY**, not **WHAT** (code shows what)
- 3-5 lines max per comment
- Use ASCII diagrams for complex flows
- Link to decision records when relevant

### Function Documentation (JSDoc/Python Docstring)
```python
def parse_expression():
    """
    Parse a HyperCode expression into AST node.
    
    Returns: AST node or raises ParseError
    """
```

### API Documentation
- Location: `/docs/ARCHITECTURE.md`
- Update whenever function signature changes
- Include examples for complex APIs

### Decision Records
- Location: `/docs/decisions/`
- File format: `YYYYMMDD-description.md`
- Template: Problem | Decision | Rationale | Consequences

---

## 🚀 DEPLOYMENT

### Development
```bash
npm install           # Install deps
npm test              # Run all tests
npm run lint          # Check style
npm start             # Run REPL
```

### Build
```bash
npm run build         # Compile TypeScript
npm run docs          # Generate docs
npm run profile       # Performance profiling
```

### Release
```bash
npm version patch     # Bump version
npm publish           # Push to registry
npm run changelog     # Generate release notes
```

---

## 🧩 EXTENSION POINTS

### New Features
1. Discuss design in `/docs/decisions/`
2. Write failing tests in `/tests/`
3. Implement in `/stdlib/` or `/core/` (coordinate for core changes)
4. Update `/docs/ARCHITECTURE.md`
5. Add examples to `/examples/`

### Integration with Other Systems
- **Web Runtime**: JavaScript/TypeScript adapter in `/web/`
- **IDE Support**: Language server protocol in `/lsp/`
- **AI Systems**: Export AST/metadata for AI comprehension

---

## 🎓 LEARNING PATH (For Hyper Builder)

### Week 1: Foundation
- Understand tokenizer → parser → interpreter flow
- Study AST data structures
- Write 5+ unit tests

### Week 2: Extensions
- Add 1-2 new stdlib functions
- Implement 1 new operator
- Update documentation

### Week 3: Performance
- Profile bottlenecks
- Port 1 hot path to Rust (if needed)
- Benchmark improvements

### Week 4+: Research Integration
- Integrate esoteric language pattern (Plankalkül, Brainfuck insight)
- Enhance spatial optimization
- Update living research paper

---

## 🤝 COLLABORATION RULES

### Human-AI Coordination
- **Humans**: Architecture decisions, accessibility reviews, strategic direction
- **Hyper Builder AI**: Coding, testing, debugging, documentation, research synthesis

### Git Workflow
```
[feat] Add new stdlib function
- Implements X functionality
- Tests: 5 new tests, 0 failures
- Docs: Updated ARCHITECTURE.md
- Performance: ~1% overhead

[fix] Handle edge case in parser
- Bug: Parser crashed on empty input
- Fix: Added null check
- Tests: Added regression test

[docs] Update ARCHITECTURE.md for parser changes
```

### Review Cycle
- Code passes tests ✅
- Code passes linting ✅
- Documentation updated ✅
- Performance regression tested ✅
- **Auto-approved** (no human review unless architecture change)

---

## 📊 SUCCESS METRICS

- **Productivity**: 2-3x faster feature delivery vs. manual coding
- **Accessibility**: Neurodivergent developers find code intuitive (subjective survey)
- **AI Compatibility**: Works seamlessly with Claude, Supercomplete, future models
- **Community**: Open source adoption, contributor growth
- **Performance**: Meets targets for parse/interpret/memory

---

## 🔗 REFERENCE LINKS

- **GitHub**: [your-hypercode-repo-url]
- **Docs**: `/docs/ARCHITECTURE.md`, `/docs/SYNTAX.md`
- **Research**: Plankalkül, Brainfuck, Befunge papers
- **Testing**: Jest / pytest documentation

---

**CODEMAP LOADED ✅**

This codemap gives Hyper Builder the full architecture context to build, test, 
and maintain HyperCode autonomously. Combine with .windsurfrules and Cascade Agent 
Mode for maximum productivity.

Ready? Fire up Windsurf. Paste the init prompt. Let's go. 🚀
