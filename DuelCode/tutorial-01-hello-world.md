# HyperCode Tutorial: Your First Program
## "Hello World" - Side-by-Side Visual & Text Learning

**Difficulty**: Beginner ⭐  
**Time to Complete**: 10 minutes  
**What You'll Learn**: How to output text in HyperCode  

---

## 🎯 Learning Objective

By the end, you'll understand:
- How HyperCode **operations** work
- How to make your program **talk back** to you
- The difference between **code** and **output**

---

## 📋 Before You Start (Checklist)

- [ ] Python 3.10+ installed
- [ ] HyperCode repo cloned
- [ ] Virtual environment activated
- [ ] `pip install -r requirements.txt` completed
- [ ] Terminal/Command Prompt open

**Stuck?** Check [INSTALL.md](INSTALL.md) for setup help.

---

## Part 1: Understanding Output 💬

### 🧠 Concept: What is Output?

**Output** = Your program **talking to you**. When code runs, it can print messages, numbers, or results back to you.

### 📊 Visual Representation

```
┌─────────────────────────────────────────┐
│  YOUR HYPERCODE PROGRAM                 │
│                                         │
│  ┌──────────────────────────────────┐  │
│  │ Code:                            │  │
│  │ .                                │  │
│  │ (print character)                │  │
│  └──────────────────────────────────┘  │
│            ↓ (execution)                │
│  ┌──────────────────────────────────┐  │
│  │ Output (on screen):              │  │
│  │ H                                │  │
│  └──────────────────────────────────┘  │
└─────────────────────────────────────────┘
```

**Key idea**: Your code sends a message → HyperCode receives it → It prints to your screen.

### 📝 Text Explanation

In most programming languages, you'd write complex print commands. In **HyperCode**, we keep it **super minimal**:

- `.` means **"print this character"**
- But first, you need to put a character into memory
- Then you print it

Think of it like:
1. Write a letter (put char in memory)
2. Put it in an envelope (store it)
3. Mail it (print it)

---

## Part 2: Let's Code! 💻

### Step 1: Open Your HyperCode File

**Create a new file** named `hello.hc` in your `examples/` folder:

```bash
# In terminal:
cd hypercode/examples
touch hello.hc
```

### Step 2: Write Your First Program

**Side-by-Side View:**

| Code Block | Explanation |
|-----------|------------|
| `++++++++` | Increment memory cell 8 times → Now it holds value 8 |
| `++++++++++` | Increment 10 more times → Now it holds 18 |
| `++++++++++` | Increment 10 more times → Now it holds 28 |
| `++++++++++` | Increment 10 more times → Now it holds 38 |
| `++++++++++` | Increment 10 more times → Now it holds 48 |
| `++++++` | Increment 6 more times → Now it holds 54 |
| `.` | **PRINT** the character with ASCII value 54 → prints "6" |

**Visualization:**

```
MEMORY TAPE:
┌───┬───┬───┬───┬───┬───┬───┐
│ 0 │54 │ 0 │ 0 │ 0 │ 0 │ 0 │  ← Current value: 54 (ASCII for '6')
└───┴───┴───┴───┴───┴───┴───┘
      ↑
  Pointer here
      ↓
   OUTPUT: "6"
```

**Interactive Demo:**
```hypercode
; Let's count to 54 to print "6"
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.
```

Copy this into `hello.hc`:

```hypercode
; HyperCode: Hello World (simplified version)
; Goal: Print the character "H" (ASCII 72)

; Step 1: Set cell to 72
++++++++++  ; 10
++++++++++  ; 20
++++++++++  ; 30
++++++++++  ; 40
++++++++++  ; 50
++++++++++  ; 60
++++++++++  ; 70
++          ; 72 ← ASCII value for 'H'

; Step 2: Print it!
.
```

### Step 3: Run Your Program

**In terminal:**

```bash
cd hypercode
python -m core.cli examples/hello.hc
```

**Expected output:**
```
H
```

🎉 **YOU DID IT!** Your program printed "H"!

---

## Part 3: What Just Happened? 🤔

### Memory Model (Visual + Text)

```
BEFORE execution:
┌──────────────────────────┐
│ Memory Cell [0]:         │
│ Value: 0                 │
└──────────────────────────┘

AFTER all the '+' operations:
┌──────────────────────────┐
│ Memory Cell [0]:         │
│ Value: 72                │
│ (ASCII for 'H')          │
└──────────────────────────┘

AFTER '.':
┌──────────────────────────┐
│ Output to Screen:        │
│ "H"                      │
└──────────────────────────┘
```

### Step-by-Step Breakdown

| Operation | Effect | Memory Value |
|-----------|--------|---|
| `+` (1st) | Increment | 1 |
| `+` (2nd) | Increment | 2 |
| `...` | ... | ... |
| `+` (72nd) | Increment | 72 |
| `.` | Print ASCII 72 | Outputs: **H** |

### ASCII Magic 🪄

**ASCII** (American Standard Code for Information Interchange) maps numbers to characters:

- 65 = 'A'
- 72 = 'H'
- 33 = '!'

So when you increment to 72 and print, HyperCode converts 72 → 'H' and displays it!

---

## Part 4: Challenge Time! 🎯

### Challenge 1: Print Your Name (Medium ⭐⭐)

**Goal**: Modify the code to print "HI" instead of just "H"

**Hint**: After printing 'H' (72), you need to:
1. Move to the next cell: `>`
2. Set it to 73 (ASCII for 'I'): `++++...` (73 times)
3. Print it: `.`

**Try it yourself first!** Then check the solution below.

<details>
<summary>💡 Solution (Click to reveal)</summary>

```hypercode
; Print "HI"

; Set cell 0 to 72 ('H')
++++++++++
++++++++++
++++++++++
++++++++++
++++++++++
++++++++++
++++++++++
++
.

; Move to cell 1
>

; Set cell 1 to 73 ('I')
++++++++++
++++++++++
++++++++++
++++++++++
++++++++++
++++++++++
++++++++++
+++
.
```

**Run it:**
```bash
python -m core.cli examples/hi.hc
```

**Output:**
```
HI
```

</details>

### Challenge 2: Print a Sentence (Hard ⭐⭐⭐)

**Goal**: Print "HI!" using what you learned

**Hint**: 
- 'H' = 72
- 'I' = 73
- '!' = 33

Try building this yourself using three cells!

---

## Part 5: Key Takeaways 🎓

### What You Learned

| Concept | HyperCode Operation | Example |
|---------|-------------------|---------|
| **Increment** | `+` | `++++` increments by 4 |
| **Move Right** | `>` | `>` moves to next cell |
| **Move Left** | `<` | `<` moves to previous cell |
| **Print** | `.` | `.` outputs current cell |
| **Comment** | `;` | `; This is a comment` |

### Why This Matters

- HyperCode keeps code **minimal** (only 8 core operations!)
- No syntax clutter = **less cognitive load**
- Visual memory model = **easier to understand**
- Direct cause-effect = **satisfying feedback loop**

---

## Part 6: Common Mistakes 🚨

### ❌ Mistake 1: Forgetting to set the value first

```hypercode
; WRONG - prints nothing/garbage
.
```

**Why**: You can't print if the cell is empty (0). 0 = null character (invisible).

### ✅ Fix: Always increment first

```hypercode
; RIGHT - increments to 65 ('A') then prints
++++++++++
++++++++++
++++++++++
++++++++++
++++++++++
++++++++++
.
```

---

### ❌ Mistake 2: Not moving cells before setting new values

```hypercode
; WRONG - overwrites the 'H'!
++++++++++  ; Set to 72
++++++++++  ; ...
++
.           ; Prints 'H'

++++++++++  ; Increments cell 0 again!
+++
.           ; Prints something else, not 'I'
```

**Why**: You're still on cell 0. You need `>` to move right first.

### ✅ Fix: Move before setting new cell

```hypercode
; RIGHT
++++++++++
++++++++++
++++++++++
++++++++++
++++++++++
++++++++++
++++++++++
++
.           ; Prints 'H'

>           ; MOVE to cell 1!

++++++++++
++++++++++
++++++++++
++++++++++
++++++++++
++++++++++
++++++++++
+++
.           ; Prints 'I'
```

---

## Part 7: Next Steps 🚀

### Ready to Level Up?

After mastering output, try:

1. **Part 2: Loops** - Repeat operations using `[` and `]`
2. **Part 3: Input** - Read user input with `,`
3. **Part 4: Algorithms** - Build actual programs (loops + logic)

---

## 📞 Stuck? Questions?

- **Discord**: Ask in #help-beginners
- **GitHub Issues**: Create an issue with "Tutorial" tag
- **Email**: hello@hypercode.dev

---

## ♿ Accessibility Notes

**This page uses:**
- ✅ **Dual Coding**: Visuals + text side-by-side
- ✅ **Clear Spacing**: Ample white space, no clutter
- ✅ **Sans-serif Fonts**: Arial, better for dyslexic readers
- ✅ **Color Coding**: Code blocks, text blocks visually distinct
- ✅ **Short Modules**: 10-min chunks, not overwhelming
- ✅ **Multiple Entry Points**: Visual, text, interactive, challenge
- ✅ **Progress Tracking**: Clear checkpoints
- ✅ **Dark Mode Ready**: Works in light + dark theme
- ✅ **Large Fonts**: Customizable with Ctrl/Cmd + scroll
- ✅ **No Flashing**: Safe for photosensitive users

---

**Created**: November 11, 2025  
**Audience**: Absolute beginners (all neurotypes)  
**Neurodivergent-Optimized**: ✅ YES

---

## 🎉 Congratulations!

You've completed HyperCode Tutorial Part 1: Hello World! 🎊

**Progress:**
- ✅ Understand output
- ✅ Write your first program
- ✅ Run it successfully
- ✅ Learned 3 core operations
- ⏭️ Ready for loops!

**Next Tutorial**: [Part 2: Loops & Repetition](tutorial-02-loops.md)

---

**Ready to build something LEGENDARY?** 🚀👊

*Let's go, broski!* ♾️
