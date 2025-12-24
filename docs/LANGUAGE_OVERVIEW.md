# 🧩 HyperCode Language Overview

> **ADHD-friendly syntax guide** — Quick scan, visual patterns, zero jargon.

---

## 🎯 Core Philosophy

HyperCode uses **chunked syntax** and **visual flow indicators** so your brain can:
- ✅ **See the structure** at a glance
- ✅ **Skip back easily** without losing context
- ✅ **Predict what comes next** (no hidden surprises)

---

## 🚀 Basic Syntax

### Variables
```hypercode
let name = "Alex"
let age = 25
let isActive = true
```

### Functions
```hypercode
func greet(name) {
  return "Hello, " + name
}
```

### Conditional Flow
```hypercode
if age > 18 {
  print("Adult")
} else {
  print("Minor")
}
```

### Loops
```hypercode
for item in list {
  print(item)
}

while count < 10 {
  count = count + 1
}
```

---

## 🧠 Neurodivergent-Friendly Features

### 1. Visual Flow Indicators
```hypercode
func process() {
  ↓ step 1
  loadData()
  
  ↓ step 2
  validateData()
  
  ↓ step 3
  saveData()
}
```

### 2. Explicit State Markers
```hypercode
let status = @loading    // @ indicates state
let error = @error("Failed to load")
let data = @success(result)
```

### 3. Chunked Blocks
```hypercode
// Clear visual boundaries
block authentication {
  checkCredentials()
  verifyToken()
  grantAccess()
}

block dataProcessing {
  fetchData()
  transformData()
  storeData()
}
```

### 4. Predictable Error Handling
```hypercode
try {
  riskyOperation()
} catch error {
  💚 "Something went wrong: " + error.message
  // Friendly, not scary
}
```

---

## 🎨 Style Conventions

| Pattern | Meaning | Example |
|---------|---------|----------|
| `let` | Variable | `let count = 0` |
| `func` | Function | `func add(a, b)` |
| `@` | State marker | `@loading`, `@error` |
| `↓` | Flow direction | `↓ next step` |
| `💚` | Friendly error | `💚 "Oops!"` |
| `//` | Comment | `// This explains why` |

---

## 📦 Data Types

```hypercode
// Primitives
let text = "string"
let number = 42
let decimal = 3.14
let boolean = true
let nothing = null

// Collections
let list = [1, 2, 3, 4]
let map = {name: "Alex", age: 25}

// Special
let state = @pending
let result = @success(data)
```

---

## 🔗 Importing Modules

```hypercode
import "utils" as utils
import "api" as api

utils.formatDate(today)
api.fetchUser(123)
```

---

## ✨ Quick Tips

1. **Use visual markers** (`↓`, `@`, `💚`) to guide your eyes
2. **Chunk related code** into named blocks
3. **Write comments for *why*, not *what*** — the code shows *what*
4. **Keep functions short** — aim for 5-10 lines max
5. **Use consistent spacing** — your future self will thank you

---

## 🆘 Need Help?

- 📖 [Full Documentation](../README.md)
- ❓ [FAQ](community/FAQ.md)
- 💬 [Community Discussions](https://github.com/welshDog/hypercode/discussions)
- 🐛 [Report Issues](https://github.com/welshDog/hypercode/issues)

---

**Built for brains that think differently** 🧠✨
