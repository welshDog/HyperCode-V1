# HyperCode Tutorial: Getting Started

## Table of Contents

1. [Setting Up](#setting-up)
2. [Your First Program](#your-first-program)
3. [Working with Variables](#working-with-variables)
4. [Control Flow](#control-flow)
5. [Functions and Reusability](#functions-and-reusability)
6. [Working with Collections](#working-with-collections)
7. [Building a Simple Project](#building-a-simple-project)
8. [Next Steps](#next-steps)

## Setting Up

### Prerequisites

- Python 3.8+
- Git (optional, for version control)

### Installation

1. Clone the HyperCode repository:

   ```bash
   git clone https://github.com/yourusername/hypercode.git
   cd hypercode
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Verify installation:
   ```bash
   python -m hypercode --version
   ```

## Your First Program

1. Create a new file called `hello.hc`:

   ```javascript
   // hello.hc
   print("Welcome to HyperCode!");

   // Variables and basic math
   const name = "Learner";
   var age = 25;
   print(`Hello ${name}, you are ${age} years old!`);
   ```

2. Run the program:
   ```bash
   python -m hypercode hello.hc
   ```

## Working with Variables

### Basic Types

```javascript
// Numbers
var count = 10;
var price = 9.99;

// Strings
const greeting = "Hello";
const name = "HyperCoder";

// Booleans
var isActive = true;
var hasPermission = false;

// Null
var emptyValue = null;
```

### Type Conversion

```javascript
// String to number
const strNum = "42"
const num = strNum.toNumber()

// Number to string
const numStr = 42.toString()

// Boolean conversion
const truthy = !!1       // true
const falsy = !!0        // false
```

## Control Flow

### If-Else Statements

```javascript
var temperature = 22

if temperature > 30 {
    print("It's hot!")
} else if temperature > 15 {
    print("It's pleasant.")
} else {
    print("It's cold!")
}
```

### Loops

```javascript
// While loop
var i = 0
while i < 5 {
    print("Count: " + i)
    i = i + 1
}

// For loop
for var j = 0; j < 5; j = j + 1 {
    print("For count: " + j)
}
```

## Functions and Reusability

### Basic Functions

```javascript
function greet(name) {
  return `Hello, ${name}!`;
}

print(greet("Developer")); // "Hello, Developer!"
```

### Higher-Order Functions

```javascript
// Function as argument
function applyOperation(x, y, operation) {
    return operation(x, y)
}

const add = fn(a, b) { return a + b }
const multiply = fn(a, b) { return a * b }

print(applyOperation(5, 3, add))       // 8
print(applyOperation(5, 3, multiply))  // 15
```

## Working with Collections

### Lists

```javascript
const fruits = ["apple", "banana", "cherry"]

// Add/remove items
fruits.push("date")
fruits.pop()

// Iteration
for var i = 0; i < fruits.length(); i = i + 1 {
    print(f"Fruit {i + 1}: {fruits[i]}")
}
```

### Maps

```javascript
const user = {
  name: "Alice",
  age: 30,
  isAdmin: true,
};

// Access values
print(user["name"]); // "Alice"
print(user.age); // 30

// Add/update
user["email"] = "alice@example.com";
```

## Building a Simple Project

Let's create a simple task manager:

```javascript
// task_manager.hc
const tasks = []

function addTask(description) {
    const task = {
        id: Date.now(),
        description: description,
        completed: false,
        createdAt: new Date().toISOString()
    }
    tasks.push(task)
    return task
}

function completeTask(taskId) {
    for var i = 0; i < tasks.length(); i = i + 1 {
        if tasks[i].id == taskId {
            tasks[i].completed = true
            return tasks[i]
        }
    }
    return null
}

// Example usage
addTask("Learn HyperCode")
addTask("Build a project")

const task = completeTask(tasks[0].id)
print(`Task completed: ${task.description}`)
```

## Next Steps

1. **Explore More Features**

   - Error handling with try/catch
   - Modules and imports
   - File I/O operations

2. **Join the Community**

   - [GitHub Discussions](https://github.com/yourusername/hypercode/discussions)
   - [Discord Channel](#) (coming soon)

3. **Contribute**

   - Report issues
   - Submit pull requests
   - Improve documentation

4. **Build Something Cool!**
   - Web applications
   - Command-line tools
   - Automation scripts

---

_Tutorial last updated: November 12, 2025_
