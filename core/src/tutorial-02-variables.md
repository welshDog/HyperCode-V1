# Tutorial 02: Variables & Memory 🧠

## 🎯 Learning Objectives

By the end of this tutorial, you will:

- ✅ Understand what variables are in HyperCode
- ✅ Learn how to store and retrieve values
- ✅ Use the H (output) command to display values
- ✅ Practice with memory cell operations

---

## 📋 Prerequisites

- [ ] Completed Tutorial 01: Hello World
- [ ] Understand basic HyperCode syntax
- [ ] Have HyperCode environment ready

---

## 🧠 Core Concept

**Variable** = A named storage location for data

In HyperCode, we use memory cells (like A, B, C) to store values.

### 📊 Visual

```ascii
┌─────────────────────────────────────┐
│  HyperCode Memory Cells             │
│  ┌───┐ ┌───┐ ┌───┐ ┌───┐ ┌───┐    │
│  │ A │ │ B │ │ C │ │ D │ │ E │    │
│  └───┘ └───┘ └───┘ └───┘ └───┘    │
│                                     │
│  Store → Retrieve → Output          │
└─────────────────────────────────────┘
```

---

## 💻 Code Example

```hypercode
; Store a value in cell A
A = 42

; Store text in cell B
B = "Hello"

; Output the values
H A
H B
```

**What it does:**

- Stores the number 42 in cell A
- Stores "Hello" in cell B
- Displays both values

**Run it:**

```bash
hypercode run variables.hc
```

**Output:**

```text
42
Hello
```

---

## 🎯 Try It!

**Exercise:** Create a program that stores your name and age, then outputs both.

<details>
<summary>Hint</summary>

Remember to put text values in quotes!

</details>

<details>
<summary>Solution</summary>

```hypercode
; Store your information
name = "Your Name"
age = 25

; Display them
H name
H age
```

</details>

---

## 🎉 Conclusion

You learned:

- Variables store data in memory cells
- Use = to assign values
- Use H to output values
- Text needs quotes, numbers don't

**Next:** [Tutorial 03: Math Operations](tutorial-03-math.md)

---

## 📚 Resources

- [HyperCode Memory Guide](memory-guide.md)
- [Variable Reference](variables-ref.md)

---

_Ready for more?_ 🚀
