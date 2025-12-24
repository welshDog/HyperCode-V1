# Contributing to HyperCode 🧠⚡

**Welcome, neurodivergent developer!** We built this project WITH you in mind. No gatekeeping. No BS. Just code.

---

## 🎯 Why Contribute?

- **Your brain works differently.** Help build a tool for minds like yours.
- **Get paid.** Bounties for contributions (seriously).
- **Build community.** Join developers who GET IT.
- **Shape the future.** Your code literally shapes programming for millions.

---

## 🚀 Ways to Contribute (Pick Your Style)

### 🟢 Super Easy (5-30 minutes)

**No coding experience? No problem.**

- [ ] **Fix a typo** in docs or code comments
- [ ] **Add your HyperCode story** (1-2 paragraphs about why it matters to you)
- [ ] **Report a bug** (screenshot + description of what broke)
- [ ] **Suggest an example** (what would help you learn?)
- [ ] **Improve wording** in README or docs

**Where to start**: [GitHub Issues - Good First Issue](https://github.com/welshDog/hypercode/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22)

**Bounty**: $25 ✅

---

### 🟡 Medium (30 min - 2 hours)

**You know basic coding.**

- [ ] **Write a new example** (3-5 HyperCode programs showing different use cases)
- [ ] **Create a tutorial** (step-by-step guide for beginners)
- [ ] **Improve docs clarity** (rewrite a confusing section)
- [ ] **Fix a minor bug** (issues labeled "bug" or "help wanted")
- [ ] **Add test cases** (improve code reliability)

**Where to start**: [GitHub Issues - Help Wanted](https://github.com/welshDog/hypercode/issues?q=is%3Aissue+is%3Aopen+label%3A%22help+wanted%22)

**Bounty**: $50 ✅

---

### 🔴 Advanced (2 hours - full day)

**You're comfortable building features.**

- [ ] **Build a new language feature** (let's pair program!)
- [ ] **Create an IDE plugin** (VSCode syntax highlighting)
- [ ] **Integrate with AI** (GPT/Claude code generation)
- [ ] **Optimize performance** (make HyperCode faster)
- [ ] **Build a visual playground** (browser-based editor)

**Where to start**: [GitHub Discussions](https://github.com/welshDog/hypercode/discussions) (let's talk first)

**Bounty**: $100-$500+ (depends on scope)

---

## 💬 Before You Code

### For Small Contributions
No need to ask permission. Just:
1. Fork the repo
2. Make your change
3. Submit a PR
4. We'll review and merge

### For Medium/Large Features
**Please discuss first** in [GitHub Discussions](https://github.com/welshDog/hypercode/discussions):
- Share your idea
- We'll give feedback
- We'll collaborate on approach
- No surprises, no wasted work

---

## 🛠️ Setup Your Dev Environment

### Step 1: Fork & Clone
```bash
# Fork on GitHub first, then:
git clone https://github.com/YOUR-USERNAME/hypercode.git
cd hypercode
git remote add upstream https://github.com/welshDog/hypercode.git
```

### Step 2: Install Dev Dependencies
```bash
pip install -r requirements.lock
pip install -r requirements-dev.lock  # Testing, linting, etc
```

### Step 3: Create a Branch
```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/the-bug-you-found
```

### Step 4: Code & Test
```bash
# Make your changes
python -m pytest tests/  # Run tests
python -m black src/     # Format code
```

### Step 5: Commit & Push
```bash
git add .
git commit -m "Clear description of what you did"
git push origin feature/your-feature-name
```

### Step 6: Open a Pull Request
Go to GitHub, click "New Pull Request", and describe your changes.

---

## ✨ Coding Standards

### 1. Clarity Over Cleverness
Write code that's easy to understand, not impressive.

```python
# ✅ Good
user_count = len(active_users)

# ❌ Bad (too clever)
user_count = sum(1 for u in active_users if u.active)
```

### 2. Add Comments (Especially for ADHD Brains)
Explain the WHY, not the what.

```python
# ✅ Good
# We filter for active users first to avoid processing inactive accounts
active = [u for u in users if u.active]

# ❌ Bad (comment just repeats code)
# Filter for active users
active = [u for u in users if u.active]
```

### 3. Test Your Code
```bash
# Add tests for new features
python -m pytest tests/test_your_feature.py -v
```

### 4. Use Type Hints
```python
# ✅ Good
def process_data(data: list[str]) -> dict[str, int]:
    return {"count": len(data)}

# ❌ Bad (no types)
def process_data(data):
    return {"count": len(data)}
```

---

## 📝 Commit Messages (ADHD-Friendly Format)

```
[type] Brief description

Optional longer explanation if needed.

Fixes #123
```

**Types**:
- `[feat]` - New feature
- `[fix]` - Bug fix
- `[docs]` - Documentation
- `[test]` - Tests
- `[refactor]` - Code cleanup

**Examples**:
```
[feat] Add pipe operator to syntax
[fix] Handle empty lists in sum function
[docs] Improve README clarity
```

---

## 🐛 Bug Reports: Help Us Help You

When reporting a bug, include:

1. **What you did** (exact steps)
2. **What you expected** (what should happen)
3. **What actually happened** (error message, screenshot)
4. **Your environment** (Python version, OS)

**Example**:
```
### What I did
1. Created file test.hc with: [1, 2, 3] | sum → output
2. Ran: python -m src.hypercode test.hc

### Expected
Output: 6

### Actually got
Error: NameError: 'sum' is not defined

### Environment
- Python 3.11
- macOS 13.2
```

---

## 🤝 Community Guidelines

### We Celebrate
✅ Neurodivergent developers  
✅ Diverse thinking styles  
✅ Mistakes & learning  
✅ Slow progress  
✅ Questions (no question is dumb)  
✅ Passion & authenticity

### We Don't Tolerate
❌ Gatekeeping  
❌ Shame for mistakes  
❌ Discrimination (any form)  
❌ Pressure to be "productive"  
❌ "Broken brain" language  
❌ Ableism

---

## 💰 Bounty System

### How Bounties Work

1. **Issue posted** with bounty amount (usually $25-$500)
2. **You claim it** by commenting "I'll take this"
3. **You build it** (with help if needed)
4. **You submit PR** (when ready)
5. **We merge it** ✅
6. **You get paid** (via PayPal/Stripe/Crypto)

### Current Bounties

Check [BOUNTIES.md](./BOUNTIES.md) for active opportunities.

### Create Your Own Bounty

Found an issue? Offer a bounty and we'll build it faster.

---

## 🎓 Learning Resources

### If You're New to HyperCode
- [HyperCode Syntax](./docs/SYNTAX.md)
- [Examples](./examples/)
- [Design Philosophy](./docs/PHILOSOPHY.md)

### If You're New to Open Source
- [How to Make a GitHub Pull Request](https://opensource.guide/how-to-contribute/#opening-a-pull-request)
- [GitHub Discussions Guide](https://docs.github.com/en/discussions)

### Getting Help
- **Confused?** [Ask in Discussions](https://github.com/welshDog/hypercode/discussions)
- **Stuck?** [Create an Issue](https://github.com/welshDog/hypercode/issues)
- **Want to chat?** [Join Discord](https://discord.gg/hypercode) (coming soon)

---

## 🎯 Your First Contribution Checklist

- [ ] Fork & clone the repo
- [ ] Create a branch with a clear name
- [ ] Make a small, focused change
- [ ] Test your change (if applicable)
- [ ] Write a clear commit message
- [ ] Push & open a Pull Request
- [ ] Describe what you did & why
- [ ] We'll review & merge (or give feedback)
- [ ] 🎉 **You're a HyperCode contributor!**

---

## 🙌 Thank You

You're not just contributing code. You're building a movement.

**Thank you for believing in HyperCode.** 💙

---

*Built with ❤️ by neurodivergent developers, for neurodivergent developers.*
