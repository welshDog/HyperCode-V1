# HYPERcode - Getting Started Visual Guide

*Your step-by-step journey into neurodivergent-friendly programming*

---

## 🚀 Quick Start (5 minutes)

```
┌─────────────────────────────────────┐
│  Step 1: Install HYPERcode          │
│  $ pip install hypercode            │
└─────────────────────────────────────┘
                 ↓
┌─────────────────────────────────────┐
│  Step 2: Open Your Editor           │
│  $ code my_first_program.hyp        │
└─────────────────────────────────────┘
                 ↓
┌─────────────────────────────────────┐
│  Step 3: Write Your First Program   │
│  (See examples below)               │
└─────────────────────────────────────┘
                 ↓
┌─────────────────────────────────────┐
│  Step 4: Run It                     │
│  $ hypercode my_first_program.hyp   │
└─────────────────────────────────────┘
                 ↓
🎉 Congratulations!
```

---

## 💡 Basic Concepts

### Concept 1: THINK (Intention)

```hypercode
THINK about calculate_average

What this means:
- You're about to write a function
- It's going to calculate an average
- Clear purpose from the start
```

**Visual:**
```
Your Brain        HYPERcode           Compiler
┌────────┐       ┌──────────┐       ┌─────────┐
│ Idea:  │──────▶│ THINK    │──────▶│ def     │
│ Average├───────┤ about    ├───────┤ func(): │
│        │       │ average  │       │         │
└────────┘       └──────────┘       └─────────┘
```

---

### Concept 2: INPUT (What Goes In)

```hypercode
INPUT: numbers, data_type

What this means:
- numbers: A list of numbers
- data_type: How to treat them
- These are your function parameters
```

**Visual:**
```
Outside World     HYPERcode        Your Function
┌───────────────┐ ┌─────────────┐ ┌──────────────┐
│ Your data:    │ │ INPUT:      │ │ Use these    │
│ [1,2,3,4,5]   │─│ numbers     │─│ inside the   │
│ 'integers'    │ │ data_type   │ │ function     │
└───────────────┘ └─────────────┘ └──────────────┘
```

---

### Concept 3: OUTPUT (What Comes Out)

```hypercode
OUTPUT: average_value

What this means:
- average_value: What the function returns
- This is what you'll get back
```

**Visual:**
```
Inside Function   HyperCode      To Your Program
┌──────────────┐ ┌───────────┐ ┌────────────────┐
│ Calculated   │ │ OUTPUT:   │ │ You receive:   │
│ average = 3.5│─│ average   │─│ 3.5            │
│              │ │ value     │ │                │
└──────────────┘ └───────────┘ └────────────────┘
```

---

## 📝 Example 1: Hello World

**The simplest program:**

```hypercode
THINK about greet_user

INPUT: name
OUTPUT: greeting

COMMENT: Build a greeting message
greeting = "Hello, " + name + "!"

RETURN greeting
```

**What it does:**
1. ✅ Takes a name (e.g., "Alice")
2. ✅ Creates a greeting (e.g., "Hello, Alice!")
3. ✅ Gives it back to you

**Run it:**
```bash
$ hypercode examples/hello.hyp
Enter name: Alice
Hello, Alice!
```

---

## 📝 Example 2: Calculate Sum

```hypercode
THINK about add_numbers

INPUT: list_of_numbers
OUTPUT: total_sum

COMMENT: Start with zero
total = 0

COMMENT: Add each number
FOR each_number IN list_of_numbers
    total = total + each_number
END_FOR

RETURN total
```

**Breaking it down:**

```
Step 1: Set total to 0
        total = 0
        
Step 2: Loop through numbers
        FOR 1 IN [1,2,3,4,5]  ──▶ Add to total
        FOR 2 IN [1,2,3,4,5]  ──▶ Add to total
        FOR 3 IN [1,2,3,4,5]  ──▶ Add to total
        FOR 4 IN [1,2,3,4,5]  ──▶ Add to total
        FOR 5 IN [1,2,3,4,5]  ──▶ Add to total
        
Step 3: Return result
        total = 15  ◀──── Done!
```

---

## 📝 Example 3: Decision Making

```hypercode
THINK about check_grade

INPUT: score
OUTPUT: letter_grade

IF score >= 90
    letter_grade = "A"
ELSE_IF score >= 80
    letter_grade = "B"
ELSE_IF score >= 70
    letter_grade = "C"
ELSE
    letter_grade = "F"
END_IF

RETURN letter_grade
```

**Visual flow:**

```
                    score = 85
                        │
                        ▼
        Is score >= 90?  No
                        │
                        ▼
        Is score >= 80?  Yes
                        │
                        ▼
                     Return "B"
```

---

## 🔧 Common Patterns

### Pattern 1: Process Data

```hypercode
THINK about process_list

INPUT: data_list
OUTPUT: processed_data

COMMENT: Create empty result container
processed_data = []

COMMENT: Handle each item
FOR item IN data_list
    COMMENT: Transform the item
    new_item = item * 2
    
    COMMENT: Add to results
    processed_data.add(new_item)
END_FOR

RETURN processed_data
```

### Pattern 2: Check and Filter

```hypercode
THINK about filter_valid

INPUT: items, validation_rule
OUTPUT: valid_items

COMMENT: Start with empty list
valid_items = []

COMMENT: Check each item
FOR item IN items
    IF validation_rule(item) == TRUE
        valid_items.add(item)
    END_IF
END_FOR

RETURN valid_items
```

### Pattern 3: Combine Functions

```hypercode
THINK about pipeline

INPUT: raw_data
OUTPUT: final_result

COMMENT: Step 1: Clean data
clean_data = clean(raw_data)

COMMENT: Step 2: Process data
processed = process(clean_data)

COMMENT: Step 3: Analyze results
final_result = analyze(processed)

RETURN final_result
```

---

## 🎓 Learning Path

```
Week 1: Foundations
├─ Read GETTING_STARTED (this file)
├─ Write Hello World example
├─ Try simple calculations
└─ Understand INPUT/OUTPUT

Week 2: Control Flow
├─ Learn IF/ELSE statements
├─ Write decision programs
├─ Use FOR/WHILE loops
└─ Practice with patterns

Week 3: Functions
├─ Combine multiple functions
├─ Use THINK keyword correctly
├─ Handle errors gracefully
└─ Write clean, readable code

Week 4: Advanced
├─ Use AI suggestions
├─ Optimize your code
├─ Contribute to HYPERcode
└─ Build real projects
```

---

## ❌ Common Mistakes (and How to Fix Them)

### Mistake 1: Forgetting INPUT/OUTPUT

```hypercode
❌ WRONG:
THINK about add
result = 5 + 3
RETURN result

✅ RIGHT:
THINK about add

INPUT: number1, number2
OUTPUT: sum_result

sum_result = number1 + number2
RETURN sum_result
```

**Why?** INPUT/OUTPUT make it clear what the function expects and returns.

---

### Mistake 2: Unclear Variable Names

```hypercode
❌ WRONG:
x = data[0]
y = data[1]
z = x + y

✅ RIGHT:
first_number = data[0]
second_number = data[1]
total = first_number + second_number
```

**Why?** Variable names should tell you what they contain.

---

### Mistake 3: Missing COMMENTS

```hypercode
❌ WRONG:
count = 0
FOR i IN list
    if i > 5
        count = count + 1
    end_if
end_for

✅ RIGHT:
COMMENT: Count numbers greater than 5
count = 0

FOR i IN list
    COMMENT: Check if number is large enough
    IF i > 5
        COMMENT: Increment counter
        count = count + 1
    END_IF
END_FOR
```

**Why?** Comments help YOU understand later, and other neurodivergent coders.

---

## 🆘 Troubleshooting

### Problem: "Syntax Error on Line 5"

```
❌ Common cause: Missing END_IF or END_FOR

CODE:
IF x > 0
    RETURN "positive"
RETURN "not positive"

✅ FIX:
IF x > 0
    RETURN "positive"
ELSE
    RETURN "not positive"
END_IF
```

---

### Problem: "INPUT expects 3 values, got 2"

```
❌ You called the function with wrong number of arguments

CODE:
greet("Alice")  ◀─── Only 1 argument

❌ But function expects:
INPUT: name, age, city  ◀─── 3 arguments

✅ FIX:
greet("Alice", 25, "NYC")  ✅ Now 3 arguments
```

---

### Problem: "Variable not defined"

```
❌ You used a variable that doesn't exist

CODE:
THINK about example
total = 0
RETURN sum  ◀─── "sum" was never created!

✅ FIX:
THINK about example
total = 0
sum = total + 5
RETURN sum
```

---

## 🚀 Next Steps

### After You Complete Basics:

1. **Read the Full Documentation**
   - [ARCHITECTURE_VISUAL.md](./ARCHITECTURE_VISUAL.md) - How it works inside
   - [API.md](./API.md) - All available functions
   - [CONTRIBUTING.md](../CONTRIBUTING.md) - Join the community

2. **Try Intermediate Examples**
   - Data processing scripts
   - AI-assisted code generation
   - Multi-function programs

3. **Use IDE Features**
   - Syntax highlighting
   - Auto-complete suggestions
   - Error checking in real-time

4. **Leverage AI**
   - Ask for optimization suggestions
   - Get code explanations
   - Receive improvement tips

5. **Join Community**
   - GitHub Discussions
   - Neurodivergent Dev Community
   - HYPERcode Discord

---

## 📚 Cheat Sheet

| Keyword | Meaning | Example |
|---------|---------|---------|
| `THINK about X` | Start a function | `THINK about calculate` |
| `INPUT: a, b` | Function parameters | `INPUT: name, age` |
| `OUTPUT: result` | What returns | `OUTPUT: greeting` |
| `RETURN value` | Send back result | `RETURN answer` |
| `IF condition` | Decision point | `IF x > 0` |
| `FOR item IN list` | Loop through items | `FOR i IN numbers` |
| `COMMENT: text` | Explanation | `COMMENT: Initialize` |
| `END_IF` | End decision | `END_IF` |
| `END_FOR` | End loop | `END_FOR` |

---

## 💡 Pro Tips for Success

✅ **Read your code out loud** - If it sounds confusing, it is  
✅ **Use COMMENTS generously** - You'll thank yourself later  
✅ **Start simple** - Learn basics before advanced features  
✅ **Name variables clearly** - `user_age` not `ua`  
✅ **Test often** - Run your code frequently  
✅ **Ask for help** - Community loves to help!  
✅ **Use AI wisely** - Get suggestions, understand why  

---

## 📞 Get Help

- 🐛 Found a bug? [GitHub Issues](https://github.com/welshdog/HYPERcode-V1/issues)
- 💬 Questions? [GitHub Discussions](https://github.com/welshdog/HYPERcode-V1/discussions)
- 👥 Community? [Discord](https://discord.gg/hypercode)
- 📧 Direct? [hello@hypercode-project.dev](mailto:hello@hypercode-project.dev)

---

## 🎉 Celebrate Your Progress!

**First Hello World?** 🎊 Awesome!  
**First Function?** 🚀 You're a coder!  
**First Loop?** ⚡ Power user incoming!  
**Contribution?** 💪 Welcome to the community!

---

**Last Updated:** December 20, 2025  
**Version:** 1.0  
**Status:** Neurodivergent-Tested ✅

*Remember: Code is for humans to read, computers just execute it. Make it clear, make it kind, make it yours.*
