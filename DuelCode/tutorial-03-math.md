# Tutorial 03: Math Operations 🔢

## 🎯 Learning Objectives

By the end of this tutorial, you will:
- ✅ Perform basic arithmetic operations
- ✅ Use math operators (+, -, *, /)
- ✅ Store calculation results
- ✅ Combine math with variables

---

## 📋 Prerequisites & Checklist

- [ ] Completed Tutorial 01: Hello World
- [ ] Completed Tutorial 02: Variables & Memory
- [ ] Understand basic math concepts
- [ ] Have HyperCode environment ready

**Stuck?** Check [Tutorial 02](tutorial-02-variables.md) for variable basics.

---

## 🧠 Concept Overview

**Math Operations** = Using operators to calculate values

**Key Points:**
- HyperCode supports +, -, *, / operators
- Operations follow order of operations
- Results can be stored in variables

### 📊 Visual Representation

```ascii
┌─────────────────────────────────────────┐
│           Math Operations               │
│                                         │
│  5 + 3  ──►  8                          │
│  10 - 4 ──►  6                          │
│  7 * 2  ──►  14                         │
│  15 / 3 ──►  5                          │
│                                         │
│  Calculate → Store → Output             │
└─────────────────────────────────────────┘
```

---

## Part 1: Basic Math 💻

### Step 1: Addition

**Adding numbers is simple with the + operator.**

```hypercode
; Basic addition
result = 5 + 3
H result
```

**What this does:**
- Calculates 5 + 3
- Stores result (8) in 'result' variable
- Outputs the value

### Step 2: All Operations

**Try all basic math operations.**

```hypercode
; Addition
sum = 10 + 5
H sum

; Subtraction
diff = 20 - 8
H diff

; Multiplication
prod = 6 * 7
H prod

; Division
quot = 100 / 4
H quot
```

**Expected output:**
```text
15
12
42
25
```

---

## Part 2: Combining Operations 🚀

### 🔄 Interactive Demo

<details>
<summary>Click to expand interactive example</summary>

```hypercode
; Store initial values
x = 10
y = 3

; Multiple operations
result1 = x + y
result2 = x * y
result3 = x / y

; Show all results
H "Results:"
H result1
H result2
H result3
```

**Try it yourself:**
1. Change x and y values
2. Add more operations
3. Mix operations in one line

</details>

---

## Part 3: Common Pitfalls & Solutions ⚠️

### ❌ Common Mistake 1

**Problem:** Forgetting order of operations

```hypercode
; WRONG - might give unexpected result
result = 2 + 3 * 4
H result
```

**Why it fails:** Multiplication happens before addition (3*4=12, then 2+12=14)

### ✅ Fix 1

**Solution:** Use parentheses to control order

```hypercode
; RIGHT - clear order of operations
result = (2 + 3) * 4
H result
```

---

## 🎯 Challenges

### Challenge 1: Simple Calculator (Easy ⭐)

**Goal**: Create a program that adds two numbers and outputs the result

**Hint**: Use variables to store the numbers first

<details>
<summary>Solution</summary>

```hypercode
; Store numbers
num1 = 15
num2 = 27

; Add them
total = num1 + num2

; Show result
H "Sum:"
H total
```

</details>

### Challenge 2: Average Calculator (Medium ⭐⭐)

**Goal**: Calculate the average of 4 numbers

**Hint**: Sum all numbers, then divide by 4

<details>
<summary>Solution</summary>

```hypercode
; Store numbers
n1 = 10
n2 = 20
n3 = 30
n4 = 40

; Calculate average
sum = n1 + n2 + n3 + n4
avg = sum / 4

; Show result
H "Average:"
H avg
```

</details>

### Challenge 3: Temperature Converter (Hard ⭐⭐⭐)

**Goal**: Convert Celsius to Fahrenheit (F = C * 9/5 + 32)

**Hint**: Be careful with order of operations!

<details>
<summary>Solution</summary>

```hypercode
; Store Celsius temperature
celsius = 25

; Convert to Fahrenheit
fahrenheit = (celsius * 9) / 5 + 32

; Show both
H "Celsius:"
H celsius
H "Fahrenheit:"
H fahrenheit
```

</details>

---

## 🎉 Conclusion

Congratulations! You've successfully:
- Learned all basic math operations
- Understood order of operations
- Created calculator programs
- Combined math with variables

**Key Takeaways:**
- Use +, -, *, / for math operations
- Parentheses control the order
- Store results in variables
- Math powers up your programs!

---

## 🚀 What's Next?

Ready to level up? Here's your learning path:

1. **Tutorial 04: Loops & Repetition** - Learn to repeat actions
2. **Tutorial 05: Conditional Logic** - Make decisions in code
3. **Tutorial 06: Functions** - Create reusable code blocks

**Recommended next step:** Try [Tutorial 04: Loops](tutorial-04-loops.md) to learn about repetition!

---

## 📚 See Also

- [Math Operations Reference](math-ref.md)
- [Variable Guide](variables-guide.md)
- [Order of Operations Cheat Sheet](order-of-ops.md)
- [HyperCode Community Forum](https://forum.hypercode.dev)

---

## 🎓 Glossary

- **Operator**: A symbol that performs an operation (+, -, *, /)
- **Operand**: A value that an operator acts on
- **Expression**: A combination of operators and operands
- **Order of Operations**: Rules for which operations happen first
- **Variable**: A named storage location for data

---

## ❓ FAQ

**Q: Can I do complex math like square roots?**
A: Basic HyperCode supports simple arithmetic. Advanced math functions are covered in Tutorial 15.

**Q: What happens if I divide by zero?**
A: HyperCode will show an error. Always check your divisor isn't zero!

**Q: Can I mix text and numbers?**
A: Not directly. Numbers and text are different types. We'll cover type conversion in Tutorial 08.

---

## 🙏 Acknowledgments

Special thanks to:
- The HyperCode math team for operator implementation
- Tutorial testers who found edge cases
- You, for completing this tutorial!

---

**Ready to continue your journey?** 🚀👊

_Keep calculating!_ 🔢
