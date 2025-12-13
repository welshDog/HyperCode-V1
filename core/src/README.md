# 💻 HyperCode Source Code Structure

> Guide to navigating the HyperCode codebase

---

## 📚 Directory Overview

This directory contains the core source code for the HyperCode programming language.

```
src/
├── compiler/           # Compiler implementation
│   ├── lexer/          # Tokenization and lexical analysis
│   ├── parser/         # Syntax parsing and AST generation
│   ├── semantic/       # Semantic analysis and type checking
│   └── codegen/        # Code generation and optimization
│
├── runtime/            # Runtime environment
│   ├── vm/             # Virtual machine implementation
│   ├── gc/             # Garbage collector
│   └── stdlib/         # Standard library primitives
│
├── cli/                # Command-line interface
│   ├── repl/           # Interactive REPL
│   └── commands/       # CLI commands and utilities
│
├── lsp/                # Language Server Protocol
│   ├── diagnostics/    # Error and warning reporting
│   ├── completion/     # Code completion
│   └── formatting/     # Code formatting
│
├── utils/              # Shared utilities
│   ├── error-handling/ # Error message formatting
│   ├── source-map/     # Source map generation
│   └── logger/         # Logging utilities
│
└── tests/              # Unit and integration tests
    ├── unit/           # Unit tests
    ├── integration/    # Integration tests
    └── fixtures/       # Test fixtures and samples
```

---

## 🔧 Key Components

### Compiler

The compiler transforms HyperCode source code into executable bytecode.

**Lexer** (`compiler/lexer/`)
- Converts source text into tokens
- Handles neurodivergent-friendly symbols (`↓`, `@`, `💚`)
- Preserves whitespace for formatting

**Parser** (`compiler/parser/`)
- Builds Abstract Syntax Tree (AST) from tokens
- Enforces chunked syntax rules
- Generates helpful error messages

**Semantic Analyzer** (`compiler/semantic/`)
- Type checking and inference
- Scope analysis
- Error detection with actionable suggestions

**Code Generator** (`compiler/codegen/`)
- Converts AST to optimized bytecode
- Inline optimizations
- Debug information generation

### Runtime

The runtime executes compiled HyperCode programs.

**Virtual Machine** (`runtime/vm/`)
- Bytecode interpreter
- JIT compilation for hot paths
- Performance monitoring

**Garbage Collector** (`runtime/gc/`)
- Automatic memory management
- Generational collection
- Low-pause optimization

**Standard Library** (`runtime/stdlib/`)
- Core data structures
- I/O operations
- String manipulation
- Math utilities

### CLI

**REPL** (`cli/repl/`)
- Interactive coding environment
- Syntax highlighting
- History and completion

**Commands** (`cli/commands/`)
- `hypercode run` - Execute files
- `hypercode build` - Compile projects
- `hypercode test` - Run tests
- `hypercode fmt` - Format code

### Language Server Protocol

**LSP Server** (`lsp/`)
- Powers IDE integrations
- Real-time diagnostics
- Code completion
- Go-to-definition
- Hover documentation

---

## 🛠️ Development Workflow

### Building from Source

```bash
# Install dependencies
npm install

# Build the project
npm run build

# Run tests
npm test

# Start development mode
npm run dev
```

### Testing

```bash
# Run all tests
npm test

# Run unit tests only
npm run test:unit

# Run integration tests
npm run test:integration

# Run with coverage
npm run test:coverage
```

### Code Style

- **TypeScript** - All source code
- **ESLint** - Linting and style enforcement
- **Prettier** - Code formatting
- **Conventional Commits** - Commit message format

---

## 🧠 Neurodivergent-Friendly Design Principles

### Code Organization

1. **Chunked Modules**: Small, focused files (<200 lines)
2. **Clear Names**: Descriptive function/variable names
3. **Inline Comments**: Explain *why*, not *what*
4. **Consistent Patterns**: Predictable structure across modules

### Error Handling

- **Friendly Messages**: Plain language, no jargon
- **Actionable Suggestions**: Tell how to fix, not just what's wrong
- **Visual Cues**: Use emojis and colors for quick scanning
- **Context**: Show surrounding code with error location

### Testing

- **Descriptive Test Names**: Read like sentences
- **AAA Pattern**: Arrange, Act, Assert
- **Focused Tests**: One concept per test
- **Visual Diffs**: Clear expected vs actual output

---

## 📚 Further Reading

- [Contributing Guide](../CONTRIBUTING.md)
- [Architecture Documentation](../docs/ARCHITECTURE.md)
- [Language Specification](../docs/SPEC.md)
- [API Reference](../docs/API.md)

---

## 👥 Contributing

Want to contribute? See our [Contributing Guide](../CONTRIBUTING.md) for:

- Code style guidelines
- Pull request process
- Development setup
- Testing requirements

---

*Built with 💜 for neurodivergent minds*
