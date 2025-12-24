# HyperCode Syntax Specification

> **Version**: 0.1.0-alpha
> **Status**: Draft
> **Last Updated**: 2025-12-18

## Core Principles

1. **Minimal Visual Noise** - Reduce visual clutter that distracts from code structure
2. **Spatial Clarity** - Use indentation and alignment to show relationships
3. **Consistent Patterns** - Predictable syntax reduces cognitive load
4. **Dyslexia-Friendly** - Avoid visually similar characters
5. **AI-Native** - Optimized for both human and AI understanding

## Table of Contents
- [Variables & Assignment](#variables--assignment)
- [Control Flow](#control-flow)
- [Functions](#functions)
- [Data Structures](#data-structures)
- [Error Handling](#error-handling)
- [Concurrency](#concurrency)
- [Comments & Documentation](#comments--documentation)

## Variables & Assignment

### Basic Assignment
```hypercode
// Type inference with clear visual separation
name: "Alice"
age: 30
is_active: true

// Constants (immutable)
@MAX_RETRIES: 3
@API_URL: "https://api.example.com"
```

### Multiple Assignment
```hypercode
// Parallel assignment
x, y: 10, 20
name, age: "Bob", 42

// Swap values
a, b: b, a  // No temporary variable needed
```

## Control Flow

### Conditionals
```hypercode
// If-Else with clear visual hierarchy
IF score > 90
   GRADE: 'A'
ELSE IF score > 70
   GRADE: 'B'
ELSE
   GRADE: 'C'

// Ternary-like expression
result: IF x > 0 THEN "positive" ELSE "non-positive"
```

### Loops
```hypercode
// Range-based loop
FOR i IN 1..5
   PRINT i * 2

// While loop
WHILE counter > 0
   process(counter)
   counter: counter - 1

// List comprehension
squares: [x * x FOR x IN 1..10]
```

## Functions

### Basic Function
```hypercode
// Function definition
FUNCTION add(a: Number, b: Number) -> Number
   RETURN a + b

// Single-expression function
square: x -> x * x

// Default parameters
greet: (name, greeting: "Hello") -> "${greeting}, ${name}!"
```

### Higher-Order Functions
```hypercode
// Function as parameter
apply_twice: (f, x) -> f(f(x))
double: x -> x * 2
result: apply_twice(double, 5)  // 20

// Anonymous function
numbers.map(x -> x * x)
```

## Data Structures

### Lists
```hypercode
// List creation
numbers: [1, 2, 3, 4, 5]
fruits: ["apple", "banana", "cherry"]

// List operations
first: numbers[0]      // 1
rest: numbers[1..]     // [2, 3, 4, 5]
combined: [0, ...numbers]  // [0, 1, 2, 3, 4, 5]
```

### Dictionaries
```hypercode
// Dictionary creation
person: {
   name: "Alice"
   age: 30
   active: true
}

// Access and update
name: person.name
person.age: 31
```

## Error Handling

### Try-Catch
```hypercode
TRY
   result: 10 / 0
CATCH error
   PRINT "Error:", error.message
FINALLY
   cleanup_resources()
```

### Optional Chaining
```hypercode
// Safe navigation
user_name: user?.profile?.name ?? "Anonymous"
```

## Concurrency

### Async/Await
```hypercode
// Asynchronous function
fetch_data: ASYNC (url) -> {
   response: AWAIT http.get(url)
   RETURN response.data
}

// Parallel execution
user_data, posts: AWAIT ALL [
   fetch_user(user_id),
   fetch_posts(user_id)
]
```

## Comments & Documentation

### Single-line Comments
```hypercode
// This is a single-line comment
x: 42  // End-of-line comment
```

### Documentation Blocks
```hypercode
/// Calculates the factorial of a number
///
/// @param n {Number} - A non-negative integer
/// @returns {Number} - The factorial of n
FUNCTION factorial(n)
   IF n <= 1
      RETURN 1
   RETURN n * factorial(n - 1)
```

## Next Steps
1. Review and provide feedback on this syntax
2. Implement the lexer/parser for core syntax
3. Create more examples and test cases
4. Gather community feedback

## Contributing
Please open an issue or submit a PR with suggested improvements to the syntax design.
