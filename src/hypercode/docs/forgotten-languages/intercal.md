---
title: "INTERCAL: The Original Parody Programming Language"
category: forgotten-languages
date_added: 2025-11-22
last_updated: 2025-11-22
tags: [intercal, esoteric, parody, satire, humor]
relevance_to_hypercode: medium
key_insights:
  - "Created in 1972 as satire of contemporary languages"
  - "Features intentionally absurd operators and keywords"
  - "'Politeness enforcer' requires correct number of PLEASEs"
  - "COME FROM as opposite of GOTO"
  - "Demonstrates how language design can be humorously painful"
related_topics:
  - malbolge
  - befunge
  - esoteric-overview
  - language-design-principles
citations:
  - url: "https://sphere-engine.com/supported-languages/preview/9"
    title: "INTERCAL Language Overview"
    date: 2025-11-22
  - url: "https://runme.org/feature/read/+INTERCAL/+101/"
    title: "INTERCAL 101"
    date: 2005-07-14
  - url: "https://www.reddit.com/r/ProgrammerHumor/comments/71j14o/til_that_programs_written_in_intercal_will_fail/"
    title: "INTERCAL Politeness Enforcement"
    date: 2017-09-21
---

# INTERCAL: The Original Parody Programming Language

**Created by:** Don Woods and James Lyon  
**Year:** 1972  
**Full Name:** "Compiler Language With No Pronounceable Acronym"  
**Status:** 🎭 **The grandfather of esoteric parody languages**

## Overview

INTERCAL was created as **satire** of the programming language landscape of the early 1970s. It deliberately incorporated the worst features of FORTRAN, COBOL, and assembly language while adding absurd "innovations" of its own.

**The Original Esolang:**
- First language designed to be **deliberately difficult**
- Inspired decades of esoteric language design
- Still maintained and updated (C-INTERCAL, CLC-INTERCAL)
- Turing-complete despite the absurdity

## Revolutionary (Ridiculous) Features

### 1. 🎩 The Politeness Enforcer

**Programs MUST use the keyword `PLEASE`.**

But there's a catch:
- **Too few PLEASEs:** Compiler error: `PROGRAMMER IS INSUFFICIENTLY POLITE`
- **Too many PLEASEs:** Compiler error: `PROGRAMMER IS INSINCERE`
- **Just right:** Somewhere between 10-30% of statements

**Example:**
```intercal
DO ,1 <- #13
PLEASE DO ,1 SUB #1 <- #234
DO ,1 SUB #2 <- #112
PLEASE DO ,1 SUB #3 <- #112
```

**Why This Matters:**
- Parodies "code etiquette" and style guides
- Enforces arbitrary social norms via compiler
- Makes politeness **mandatory but not absolute**

### 2. ↩️ COME FROM (The Anti-GOTO)

**Instead of GOTO, INTERCAL has COME FROM.**

**GOTO:** "Jump to this label"  
**COME FROM:** "When execution reaches this label, jump HERE instead"

```intercal
(1) PLEASE COME FROM (2)
    DO SOMETHING
(2) DO SOMETHING ELSE
```

**Execution flow:**
1. Start at (2)
2. When (2) is reached, jump to (1)
3. Execute "DO SOMETHING"
4. Continue to (2)
5. Execute "DO SOMETHING ELSE"

**Why This Is Insane:**
- Control flow is **non-local** (jump happens FROM elsewhere)
- Code reading requires **scanning entire program** for COME FROMs
- Debugging is a nightmare
- Perfect satire of spaghetti code

### 3. 🤡 Bizarre Operators

INTERCAL uses symbols that look like emoticons:

- **`$` ("Big Money")** — Variable prefix
- **`¢` ("Cent")** — Another variable prefix
- **`"` ("Rabbit Ears")** — Grouping (like parentheses)
- **`~` ("Sqiggle")** — Select operation
- **`∀` ("Bookworm")** — Array dimension separator
- **`#` ("Mesh")** — Literal number prefix

**Example:**
```intercal
DO .1 <- #1 ~ #2
```

**Translation:** "Assign the SELECT of 1 and 2 to variable .1"

### 4. 🎲 The SELECT (~) and MINGLE ($) Operations

**SELECT (~):** Extracts specific bits based on a mask  
**MINGLE ($):** Interleaves bits from two numbers  

**Example:**
```
5 (binary: 101)
3 (binary: 011)

MINGLE: 100111 (alternating bits)
```

**Why These Exist:**
- Parody of overly-complex bitwise operations
- Deliberately unintuitive
- Forces programmers to think in bizarre ways

### 5. 📜 Verbose Syntax

**Normal language:**
```python
x = 5
```

**INTERCAL:**
```intercal
DO .1 <- #5
```

**Array assignment in INTERCAL:**
```intercal
PLEASE DO ,1 SUB #1 <- #234
```

**Everything is verbose and ceremonial.**

### 6. 🚫 ABSTAIN and REINSTATE

**ABSTAIN:** Temporarily disable a line of code  
**REINSTATE:** Re-enable it  

```intercal
PLEASE ABSTAIN FROM (100)
(100) DO SOMETHING DANGEROUS
PLEASE REINSTATE (100)
```

**Why This Exists:**
- Parody of self-modifying code
- Enables/disables lines during runtime
- Makes debugging even harder

### 7. 📝 IGNORE and REMEMBER

**Variables can be temporarily "forgotten":**

```intercal
DO IGNORE .1
// .1 is now unavailable
DO REMEMBER .1
// .1 is back
```

**Parodies:**
- Variable scope management
- Resource allocation
- Memory management nightmares

## Example: Hello World

```intercal
DO ,1 <- #13
PLEASE DO ,1 SUB #1 <- #238
DO ,1 SUB #2 <- #108
DO ,1 SUB #3 <- #112
DO ,1 SUB #4 <- #0
DO ,1 SUB #5 <- #64
DO ,1 SUB #6 <- #194
DO ,1 SUB #7 <- #48
PLEASE DO ,1 SUB #8 <- #22
DO ,1 SUB #9 <- #248
DO ,1 SUB #10 <- #168
DO ,1 SUB #11 <- #24
DO ,1 SUB #12 <- #16
DO ,1 SUB #13 <- #162
PLEASE READ OUT ,1
PLEASE GIVE UP
```

**Yes, this prints "Hello, World!"**

**Key points:**
- Numbers are encoded characters
- `,1` is an array
- `READ OUT` prints the array
- `GIVE UP` terminates the program

## Why INTERCAL Exists

### 🎯 Satire of 1970s Language Design

**What INTERCAL mocked:**
- FORTRAN's cryptic syntax
- COBOL's verbose keywords
- Assembly's low-level operations
- General complexity of contemporary languages

### 🧠 Exploring Language Usability

**By being deliberately bad, INTERCAL reveals what makes languages good:**

❌ **COME FROM** → ✅ Clear control flow  
❌ **Politeness enforcer** → ✅ Style guidelines (not compiler errors)  
❌ **Bizarre operators** → ✅ Intuitive symbols  
❌ **Verbose syntax** → ✅ Balance between clarity and brevity  

### 🎭 Humor in Programming

INTERCAL proved that:
- Programming languages can be **art**
- Satire can reveal **design principles**
- Humor makes **learning engaging**
- Absurdity highlights **assumptions**

## INTERCAL in Modern Times

### Implementations

- **C-INTERCAL** (Eric Raymond, 1990) — Most popular implementation
- **CLC-INTERCAL** (Claudio Calvelli, 2006) — Compiler with extensions
- **J-INTERCAL** — Java-based interpreter

### Cultural Impact

- Inspired countless esoteric languages (Brainfuck, Malbolge, etc.)
- Referenced in programming humor
- Used in coding challenges
- Symbol of "deliberately bad design"

## What INTERCAL Teaches Us

### ❌ Anti-Patterns for HyperCode

1. **Non-local control flow** (COME FROM) = unreadable code
2. **Arbitrary style enforcement** (politeness) = frustration
3. **Unintuitive operators** = steep learning curve
4. **Verbose syntax** = typing fatigue
5. **Self-modifying code** (ABSTAIN/REINSTATE) = debugging hell

### ✅ Positive Insights

1. **Clarity over cleverness** — Intuitive > obscure
2. **Local reasoning** — Code should be understandable in isolation
3. **Optional style guides** — Suggestions, not compiler errors
4. **Balanced verbosity** — Not too short, not too long
5. **Stable code** — Execution shouldn't modify itself

## INTERCAL Philosophy

**From the INTERCAL manual:**

> "The philosophy of INTERCAL is that a language should be as different from conventional languages as possible while still being usable."

**Our takeaway:**

**Innovation is good. Gratuitous difficulty is not.**

## HyperCode Applications

### What We're Avoiding:

🚫 **COME FROM** → ✅ Clear, predictable control flow  
🚫 **Politeness enforcer** → ✅ Optional style suggestions  
🚫 **Bizarre operators** → ✅ Visual, intuitive symbols  
🚫 **Excessive verbosity** → ✅ Concise but readable syntax  

### What We're Embracing:

✅ **Humor and creativity** — Language can be fun  
✅ **Learning from satire** — Bad examples teach good principles  
✅ **Accessibility** — Languages should invite, not alienate  
✅ **Clear documentation** — Unlike INTERCAL's intentionally obtuse manual  

## Research Questions

🔍 Can "reverse satire" guide good language design?  
🔍 What's the optimal balance between brevity and clarity?  
🔍 How do we enforce style without compiler errors?  
🔍 Can humor make programming more accessible?  

## References

1. [INTERCAL Overview - Sphere Engine](https://sphere-engine.com/supported-languages/preview/9)
2. [INTERCAL 101 - runme.org](https://runme.org/feature/read/+INTERCAL/+101/)
3. [INTERCAL Politeness - Reddit](https://www.reddit.com/r/ProgrammerHumor/comments/71j14o/til_that_programs_written_in_intercal_will_fail/)

---

**Related Research:**
- [Malbolge: Hardest Language](malbolge.md)
- [Befunge: 2D Spatial Programming](befunge.md)
- Language Design Principles *(coming soon)*
- Esoteric Languages Overview *(coming soon)*

---

*Research added: 2025-11-22*  
*Next update: Check for new INTERCAL variants or community activity*
