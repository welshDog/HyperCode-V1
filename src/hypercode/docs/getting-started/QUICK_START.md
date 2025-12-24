# ⚡ HyperCode Quick Start Guide

> **From zero to running HyperCode in 5 minutes. Designed for ADHD-friendly flow.**

## 🎯 What You'll Do

1. Install HyperCode (1 minute)
2. Run your first program (30 seconds)
3. Try an interactive example (2 minutes)
4. Explore next steps (1 minute)

**Total time: ~5 minutes**

---

## Step 1: Install HyperCode ⏱️ 1 min

### Option A: One-Line Install (Recommended)

**macOS/Linux:**
```bash
curl -sSL https://raw.githubusercontent.com/welshDog/hypercode/main/install.sh | bash
```

**Windows (PowerShell):**
```powershell
iwr https://raw.githubusercontent.com/welshDog/hypercode/main/install.ps1 | iex
```

### Option B: Manual Install

```bash
# Clone the repo
git clone https://github.com/welshDog/hypercode.git
cd hypercode

# Install dependencies
pip install -r requirements.lock

# Verify installation
python -m src.hypercode --version
```

**🟢 ADHD Checkpoint:** Installation done? Nice! Take a breath. Next step is running code.

---

## Step 2: Run Your First Program ⏱️ 30 sec

Let's run the classic "Hello, World!" example:

```bash
python -m src.hypercode examples/demo_hello.hc
```

**Expected output:**
```
👋 Hello from HyperCode!
✨ Your first program is running!
```

### What Just Happened?

You executed a `.hc` (HyperCode) file! The interpreter:
1. Read your code
2. Parsed the syntax
3. Executed the instructions
4. Displayed the output

**🟡 Dyslexia Tip:** Code files end in `.hc` → easy to remember: **H**yper**C**ode

---

## Step 3: Try an Interactive Example ⏱️ 2 min

### Create Your Own Program

**Create a file called `my_first.hc`:**

```hypercode
# This is a comment - it's just for humans!

define greet with name:
  show "Hello, " plus name plus "!"
  show "Welcome to HyperCode!"

greet with "BROski"
```

**Run it:**
```bash
python -m src.hypercode my_first.hc
```

**Expected output:**
```
Hello, BROski!
Welcome to HyperCode!
```

### Modify It!

Change `"BROski"` to your name and run it again. See? You're coding!

**🟯 Autism Tip:** HyperCode follows predictable patterns. `define...with` always means "create a function."

---

## Step 4: Explore Examples ⏱️ 1 min

HyperCode comes with example programs to learn from:

```bash
# List all examples
ls examples/

# Try the calculator
python -m src.hypercode examples/demo_calculator.hc

# Try a game
python -m src.hypercode examples/demo_game.hc

# See AI features
python -m src.hypercode examples/demo_ai_assist.hc
```

### Example Categories

- **Basics** - Variables, functions, loops
- **Games** - Simple interactive programs
- **Tools** - Utilities and automations
- **AI** - AI-assisted coding examples

---

## 🎓 Next Steps

### Want to Learn More?

**Beginner Path:**
1. [Language Tutorial](guides/TUTORIAL.md) - Learn syntax step-by-step
2. [Best Practices](reference/BEST_PRACTICES.md) - Write clean HyperCode
3. [Recipes](RECIPES.md) - Copy-paste solutions

**Builder Path:**
1. [Architecture Overview](architecture/ARCHITECTURE.md) - How HyperCode works
2. [API Reference](reference/API_REFERENCE.md) - Built-in functions
3. [Contributing Guide](community/CONTRIBUTING.md) - Add features

**Power User Path:**
1. [AI Integration Guide](guides/AI_INTEGRATION_GUIDE.md) - Supercharge with AI
2. [VS Code Extension](../vscode-extension/README.md) - Editor support
3. [Advanced Examples](../examples/advanced/) - Complex programs

---

## 🛠️ Troubleshooting

### "Command not found: python"

**Try:** `python3 -m src.hypercode` instead

**Still broken?** Install Python 3.10+: [python.org/downloads](https://www.python.org/downloads/)

### "ModuleNotFoundError"

**Fix:** Re-run installation
```bash
pip install -r requirements.lock
```

### "SyntaxError in my .hc file"

**Check:**
- Are you using HyperCode syntax (not Python/JS)?
- Did you close all quotes and brackets?
- Check the [Syntax Cheatsheet](reference/LANGUAGE_REFERENCE.md)

### Still Stuck?

- 🐛 [Report a Bug](https://github.com/welshDog/hypercode/issues/new?labels=bug)
- 🤔 [Ask for Help](https://github.com/welshDog/hypercode/discussions/new?category=q-a)
- 💬 [Join Discord](https://discord.gg/hypercode) (coming soon!)

---

## 🎮 Challenge: Build Something!

Now that you've run HyperCode, try building:

### Easy Challenges (5-10 min each)
- [ ] A greeting program that asks for your name
- [ ] A simple calculator (add, subtract, multiply, divide)
- [ ] A number guessing game

### Medium Challenges (15-30 min each)
- [ ] A to-do list manager
- [ ] A password generator
- [ ] A dice roller for games

### Hard Challenges (1+ hour)
- [ ] A text-based adventure game
- [ ] A file organizer
- [ ] A chatbot using AI

**Share your creations!** Tag them with `#HyperCode` on social media.

---

## ✨ Pro Tips for Neurodivergent Coders

### For ADHD:
- **Use timers** - Code in 25-min sprints (Pomodoro)
- **Start small** - One feature at a time
- **Visual progress** - Use `show` statements to see results
- **Quick wins** - Run code often to stay motivated

### For Dyslexia:
- **Syntax highlighting** - Install the VS Code extension
- **Readable fonts** - Use OpenDyslexic or Comic Sans
- **Autocomplete** - Let the editor help you
- **Read aloud** - Use screen readers for docs

### For Autism:
- **Predictable structure** - HyperCode has consistent patterns
- **Clear errors** - Error messages explain what's wrong
- **Documentation** - Everything is documented
- **Routine** - Follow tutorials step-by-step

---

## 🚀 You're Ready!

Congrats, you've completed the Quick Start! You can now:

✅ Run HyperCode programs  
✅ Write basic HyperCode syntax  
✅ Explore examples  
✅ Know where to find help  

**What's next?** Pick a path from [Next Steps](#-next-steps) above and keep building!

---

**Made with 💜 by neurodivergent developers, for neurodivergent developers**

[Back to Main README](../README.md) | [Full Documentation](README.md) | [Contributing](community/CONTRIBUTING.md)
