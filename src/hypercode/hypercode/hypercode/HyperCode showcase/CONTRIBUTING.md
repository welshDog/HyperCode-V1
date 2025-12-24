# 🤝 Contributing to HyperCode

First off, **thank you** for considering contributing to HyperCode! 💓 Whether you're
fixing a typo, proposing a feature, or building an entire module, you're helping reshape
how minds interact with code.

**This is a judgment-free, inclusive space.** We welcome contributions from all
backgrounds, skill levels, and neurotypes. No gatekeeping. Period.

---

## 🎯 Code of Conduct

We are committed to providing a welcoming and inclusive environment for all
contributors. We expect all community members to:

- **Be respectful** of different perspectives, experiences, and identities
- **Be patient** with beginners and those learning
- **Be constructive** in feedback and discussion
- **Report harm** privately to maintainers without public shaming
- **Celebrate differences** — neurodivergence, backgrounds, cultures, abilities

**Zero tolerance for discrimination, harassment, or exclusion.** If you experience or
witness this, report it immediately.

---

## 🚀 Getting Started

### Prerequisites

- Node.js 16+ and npm 8+
- Git
- A GitHub account
- A text editor or IDE of your choice

### Setting Up Your Development Environment

```bash
# 1. Fork the repository
# Click "Fork" on the GitHub repository page

# 2. Clone your fork
git clone https://github.com/YOUR-USERNAME/HyperCode.git
cd HyperCode

# 3. Add upstream remote
git remote add upstream https://github.com/HyperCode-Labs/HyperCode.git

# 4. Install dependencies
npm install

# 5. Create a new branch for your work
git checkout -b your-feature-name
```

### Running Tests

```bash
# Run all tests
npm test

# Run tests in watch mode
npm test -- --watch

# Run with coverage report
npm test -- --coverage
```

### Building HyperCode

```bash
# Build the project
npm run build

# Watch mode (rebuilds on file changes)
npm run dev
```

---

## 📝 Types of Contributions

### 🐛 Bug Reports

Found a bug? **Help us fix it!**

1. Check [existing issues](https://github.com/HyperCode-Labs/HyperCode/issues) to avoid
   duplicates
2. [Create a new issue](https://github.com/HyperCode-Labs/HyperCode/issues/new) with:
   - Clear title describing the bug
   - Steps to reproduce
   - Expected vs. actual behavior
   - Your environment (OS, Node version, etc.)
   - Screenshots or code examples if relevant

**Bug Report Template:**

```
### Description
[Clear explanation of the issue]

### Steps to Reproduce
1. [First step]
2. [Second step]
3. [...]

### Expected Behavior
[What should happen]

### Actual Behavior
[What actually happens]

### Environment
- OS: [e.g., macOS 12.1]
- Node: [e.g., 18.0.0]
- npm: [e.g., 8.5.0]

### Additional Context
[Any other relevant information]
```

---

### ✨ Feature Requests

Have a killer idea? **We want to hear it!**

1. Check [discussions](https://github.com/HyperCode-Labs/HyperCode/discussions) for
   similar ideas
2. [Open a new discussion](https://github.com/HyperCode-Labs/HyperCode/discussions/new)
   or issue with:
   - Compelling title and description
   - Use cases and examples
   - Why this feature matters for HyperCode's vision
   - Possible implementation approaches (if you have thoughts)

**Feature Request Template:**

```
### Feature Description
[What should HyperCode be able to do?]

### Motivation
[Why is this feature important? How does it align with HyperCode's vision?]

### Use Cases
- [Example 1]
- [Example 2]
- [Example 3]

### Example Usage
[Show how users would use this feature]

### Alternatives Considered
[Other approaches you've thought about]
```

---

### 📚 Documentation Improvements

Good documentation makes HyperCode accessible to everyone.

**What we need:**

- Clearer explanations
- More examples (especially for neurodivergent learners)
- Better accessibility (alt text, captions, dyslexia-friendly formatting)
- Translations
- Tutorials and guides

**How to contribute:**

1. Identify what needs improvement
2. Create a branch: `git checkout -b docs/your-improvement`
3. Make clear, accessible edits
4. Submit a PR with explanations of your changes

---

### 💻 Code Contributions

Ready to code? **Awesome!**

**Before you start:**

1. Check [open issues](https://github.com/HyperCode-Labs/HyperCode/issues) and
   [discussions](https://github.com/HyperCode-Labs/HyperCode/discussions) for what's
   needed
2. Comment on an issue to claim it (avoid duplicate work)
3. For major features, open a discussion first to align with the vision

**Code Quality Standards:**

- Follow the existing code style
- Write clear, self-documenting code
- Add comments for non-obvious logic
- Test your changes (coverage ≥ 80%)
- Keep commits atomic and with clear messages
- Format code with `npm run lint`

**Accessibility in Code:**

- Use accessible variable and function names
- Avoid deeply nested logic
- Add comments explaining "why," not just "what"
- Test with screen readers if UI-related

---

## 📋 Submission Process

### 1. Create a Feature Branch

```bash
git checkout -b feature/amazing-feature
# or
git checkout -b fix/bug-description
# or
git checkout -b docs/improvement
```

### 2. Make Your Changes

- Write clean, readable code
- Add tests for new functionality
- Update documentation as needed
- Follow the code style

### 3. Commit Regularly

```bash
# Use clear, descriptive commit messages
git commit -m "feat: add spatial syntax support"
git commit -m "fix: resolve parser edge case with nested flows"
git commit -m "docs: clarify AI integration guide"
```

**Commit Message Format:**

```
<type>: <subject>

<body (optional)>

<footer (optional)>
```

**Types:** `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

### 4. Push and Create a Pull Request

```bash
git push origin feature/amazing-feature
```

Then on GitHub:

1. Click "Create Pull Request"
2. Fill out the PR template with:
   - What this PR does
   - Why it's needed
   - How to test it
   - Screenshots/examples if relevant
   - Any breaking changes

**PR Template:**

```
## Description
[Brief description of changes]

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Breaking change

## Testing
- [ ] Added unit tests
- [ ] Added integration tests
- [ ] Tested manually

## Checklist
- [ ] Code follows style guide
- [ ] Documentation updated
- [ ] Tests pass locally
- [ ] Commit messages are clear

## Screenshots (if applicable)
[Add screenshots here]
```

### 5. Respond to Reviews

- Be open to feedback
- Ask clarifying questions if review comments aren't clear
- Make requested changes in new commits
- Re-request review after updates

### 6. Merge and Celebrate 🎉

Once approved, your contribution gets merged and you're in the credits!

---

## 🧠 Accessibility & Neurodivergent Contributions

**HyperCode is neurodivergent-first.** We welcome and support different work styles:

- Need more time? No problem—we don't have arbitrary deadlines.
- Prefer async communication? We've got you.
- Get distracted? Totally valid—break tasks into smaller pieces.
- Need breaks? Take them—this is healthy.
- Prefer detailed instructions? Ask—we'll provide them.
- Like minimalist feedback? We'll adjust our style.

**Tell us what you need.** We'll adapt.

---

## 🎓 Learning Resources

**New to open source?**

- [How to Contribute to Open Source](https://opensource.guide/how-to-contribute/)
- [First Timers Only](https://www.firsttimersonly.com/)
- [Good First Issue](https://goodfirstissue.dev/)

**HyperCode-specific:**

- [Getting Started Guide](../docs/getting-started.md)
- [Language Reference](../docs/language-reference.md)
- [Architecture Overview](../docs/architecture.md)

---

## 🤔 Questions?

- **Confused about something?** Open an issue or discussion—no question is dumb.
- **Need help setting up?** Ask in discussions.
- **Want feedback on an idea?** Start a discussion first.
- **Struggling with something?** Reach out—we're here to help.

---

## 🌟 Recognition

Contributors are recognized in:

- [CONTRIBUTORS.md](./CONTRIBUTORS.md)
- GitHub contributors graph
- Release notes for major contributions
- Hall of Fame section in README (coming soon)

---

## 📚 More Info

- [Roadmap](../ROADMAP.md) — Where HyperCode is heading
- [Architecture](../docs/architecture.md) — How HyperCode works
- [Neurodivergent Design Principles](../docs/neurodivergent-design.md) — Our core values

---

<div align="center">

### Ready to Contribute?

**[Pick an Issue](https://github.com/HyperCode-Labs/HyperCode/issues)** |
**[Start a Discussion](https://github.com/HyperCode-Labs/HyperCode/discussions)** |
**[Read Docs](../docs/)**

_HyperCode grows because of people like you. Thank you! 💓_

</div>
