# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Initial project setup and repository structure
- Lexer implementation for HyperCode syntax tokenization
- Parser foundation for AST generation
- Core interpreter for executing HyperCode programs
- Example programs (hello, fibonacci, todo)
- CI/CD pipeline with GitHub Actions
- Comprehensive CONTRIBUTING.md with neurodivergent-friendly guidelines
- Security policy for vulnerability reporting
- This changelog

### Changed
- (None yet)

### Deprecated
- (None yet)

### Removed
- (None yet)

### Fixed
- (None yet)

### Security
- (None yet)

---

## [0.1.0] - 2025-11-26

### Added
- ✨ Initial release of HyperCode
- 📝 Lexer for basic tokenization
- 🔧 Parser for syntax analysis
- 🚀 Interpreter for program execution
- 🧪 Test suite with pytest
- 📚 Documentation and README
- 🤝 Community guidelines

### Known Issues
- Limited error handling (improvement planned)
- Parser doesn't handle all edge cases yet
- Performance optimization pending

---

## How to Update This File

**After Each PR Merge:**

1. Move items from [Unreleased] to a new version section
2. Add the date in YYYY-MM-DD format
3. Use these categories:
   - **Added**: New features
   - **Changed**: Modifications to existing features
   - **Deprecated**: Features to be removed soon
   - **Removed**: Deleted features
   - **Fixed**: Bug fixes
   - **Security**: Security fixes

**Example:**
```markdown
## [0.2.0] - 2025-12-15

### Added
- New syntax for function definitions
- Better error messages

### Fixed
- Lexer crash on unicode characters (#42)

### Security
- Sanitize user input in REPL
```

---

**Questions?** See [CONTRIBUTING.md](./CONTRIBUTING.md)