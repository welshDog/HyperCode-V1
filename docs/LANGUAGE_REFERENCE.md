# HyperCode Language Reference

## Table of Contents

1. [Introduction](#introduction)
2. [Getting Started](#getting-started)
3. [Language Syntax](#language-syntax)
   - [Variables](#variables)
   - [Data Types](#data-types)
   - [Operators](#operators)
   - [Control Flow](#control-flow)
   - [Functions](#functions)
4. [Examples](#examples)
   - [Hello World](#hello-world)
   - [FizzBuzz](#fizzbuzz)
   - [Fibonacci Sequence](#fibonacci-sequence)
5. [Best Practices](#best-practices)
6. [FAQ](#faq)

## Introduction

HyperCode is a modern, dynamically-typed programming language designed for simplicity
and readability. It combines the best features of traditional scripting languages with a
clean, minimal syntax.

## Getting Started

### Installation

```bash
# Coming soon: package manager installation
# For now, clone the repository and run the interpreter directly
```

### Running Code

```bash
# Run a HyperCode file
hypercode program.hc

# Start REPL
hypercode
```

## Language Syntax

### Variables

```javascript
// Variable declaration with type inference
var name = "HyperCode";
var version = 1.0;
var isAwesome = true;

// Constants
const PI = 3.14159;
```

### Data Types

- **Numbers**: `42`, `3.14`, `1e3`
- **Strings**: `"Hello"`, `'World'`
- **Booleans**: `true`, `false`
- **Null**: `null`
- **Lists**: `[1, 2, 3]`
- **Maps**: `{"key": "value"}`

### Operators

```javascript
// Arithmetic
1 +
  2 *
    3(
      // 7
      1 + 2,
    ) *
    3; // 9
10 % 3; // 1
2 ** 3; // 8

// Comparison
1 == 1; // true
1 != 2; // true
1 < 2; // true

// Logical
true && false; // false
true || false; // true
!true; // false
```

### Control Flow

#### If/Else

```javascript
var temp = 25

if temp > 30 {
    print("It's hot!")
} else if temp > 20 {
    print("It's warm.")
} else {
    print("It's cool.")
}
```

#### Loops

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

### Functions

```javascript
// Function definition
function greet(name) {
    return "Hello, " + name + "!"
}

// Function call
var message = greet("Developer")
print(message)  // "Hello, Developer!"

// Lambda functions
const square = fn(x) { return x * x }
print(square(5))  // 25
```

## Examples

### Hello World

```javascript
// Simple Hello World
print("Hello, HyperCode!");

// With string interpolation
const name = "World";
print(`Hello, ${name}!`); // "Hello, World!"
```

### FizzBuzz

```javascript
for var i = 1; i <= 100; i = i + 1 {
    if i % 15 == 0 {
        print("FizzBuzz")
    } else if i % 3 == 0 {
        print("Fizz")
    } else if i % 5 == 0 {
        print("Buzz")
    } else {
        print(i)
    }
}
```

### Fibonacci Sequence

```javascript
function fibonacci(n) {
    if n <= 1 {
        return n
    }
    return fibonacci(n - 1) + fibonacci(n - 2)
}

// Print first 10 Fibonacci numbers
for var i = 0; i < 10; i = i + 1 {
    print(fibonacci(i))
}
```

## Best Practices

1. **Naming Conventions**

   - Use `camelCase` for variables and functions
   - Use `UPPER_SNAKE_CASE` for constants
   - Be descriptive with names

2. **Code Organization**

   - Group related functionality together
   - Use comments to explain complex logic
   - Keep functions small and focused

3. **Error Handling**
   - Always validate input
   - Provide meaningful error messages

## FAQ

**Q: Is HyperCode compiled or interpreted?** A: HyperCode is an interpreted language,
though we're exploring JIT compilation for performance improvements.

**Q: Can I contribute to HyperCode?** A: Absolutely! Check out our
[GitHub repository](https://github.com/yourusername/hypercode) for contribution
guidelines.

**Q: What's the performance like?** A: While not as fast as compiled languages,
HyperCode is designed for developer productivity. We're continuously working on
performance improvements.

---

_Documentation last updated: November 12, 2025_
