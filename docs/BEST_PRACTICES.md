# HyperCode Best Practices

## Table of Contents

1. [Code Organization](#code-organization)
2. [Naming Conventions](#naming-conventions)
3. [Error Handling](#error-handling)
4. [Performance Tips](#performance-tips)
5. [Security Considerations](#security-considerations)
6. [Testing Guidelines](#testing-guidelines)
7. [Documentation Standards](#documentation-standards)
8. [Common Patterns](#common-patterns)

## Code Organization

### File Structure

```
project/
├── src/                  # Source files
│   ├── main.hc          # Entry point
│   ├── utils/           # Utility functions
│   ├── modules/         # Feature modules
│   └── tests/           # Test files
├── docs/               # Documentation
└── config/             # Configuration files
```

### Module Organization

```javascript
// Good: Logical grouping
const math = {
    PI: 3.14159,
    add: fn(a, b) { return a + b },
    subtract: fn(a, b) { return a - b }
}

// Export public API
return {
    add: math.add,
    subtract: math.subtract
}
```

## Naming Conventions

### Variables and Functions

```javascript
// Good
const MAX_RETRIES = 3;
let userCount = 0;

function calculateTotalPrice(items) {
  // ...
}

// Bad
const a = 3; // Too vague
function calc() {} // Too generic
```

### Classes and Constructors

```javascript
// Good
class UserAccount {
  constructor(name) {
    this.name = name;
  }
}

// Usage
const user = new UserAccount("Alice");
```

## Error Handling

### Use Specific Error Types

```javascript
class ValidationError {
  constructor(message) {
    this.message = message;
    this.name = "ValidationError";
  }
}

function validateUser(user) {
  if (!user.name) {
    throw new ValidationError("Name is required");
  }
}
```

### Error Handling in Async Code

```javascript
async function fetchData(url) {
  try {
    const response = await http.get(url);
    return response.data;
  } catch (error) {
    console.error(`Failed to fetch ${url}:`, error);
    throw error;
  }
}
```

## Performance Tips

### Efficient Loops

```javascript
// Pre-calculate array length
const items = [
  /* ... */
];
for (let i = 0, len = items.length; i < len; i++) {
  // Process items[i]
}

// Use built-in methods when possible
const doubled = items.map((x) => x * 2);
```

### Memory Management

```javascript
// Free up large objects when done
function processLargeData() {
  const data = loadHugeDataset();
  // Process data...
  data = null; // Allow garbage collection
}
```

## Security Considerations

### Input Validation

```javascript
function processUserInput(input) {
  if (typeof input !== "string") {
    throw new Error("Input must be a string");
  }
  // Process input...
}
```

### Secure String Handling

```javascript
// Use parameterized queries for database access
const query = "SELECT * FROM users WHERE id = ?";
db.query(query, [userId]);
```

## Testing Guidelines

### Unit Tests

```javascript
// test/math.test.hc
const assert = require("assert");
const math = require("../src/utils/math");

test("adds two numbers correctly", () => {
  assert.equal(math.add(2, 3), 5);
});

test("handles negative numbers", () => {
  assert.equal(math.add(-1, 1), 0);
});
```

### Test Organization

```
tests/
├── unit/
│   ├── utils/
│   └── services/
├── integration/
└── e2e/
```

## Documentation Standards

### Function Documentation

```javascript
/**
 * Calculates the total price of items in the cart.
 * @param {Array} items - Array of item objects with 'price' and 'quantity' properties
 * @param {number} taxRate - Tax rate as a decimal (e.g., 0.08 for 8%)
 * @returns {number} Total price including tax
 * @throws {TypeError} If items is not an array
 */
function calculateTotal(items, taxRate) {
  // Implementation...
}
```

### Inline Comments

```javascript
// Calculate Fibonacci using dynamic programming
function fibonacci(n, memo = {}) {
  if (n in memo) return memo[n];
  if (n <= 2) return 1;

  // Store result to avoid redundant calculations
  memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo);
  return memo[n];
}
```

## Common Patterns

### Module Pattern

```javascript
const counter = (function () {
  let count = 0;

  return {
    increment: function () {
      count++;
    },
    getCount: function () {
      return count;
    },
  };
})();
```

### Event Emitter

```javascript
class EventEmitter {
  constructor() {
    this.events = {};
  }

  on(event, listener) {
    if (!this.events[event]) {
      this.events[event] = [];
    }
    this.events[event].push(listener);
  }

  emit(event, ...args) {
    if (this.events[event]) {
      this.events[event].forEach((listener) => listener(...args));
    }
  }
}
```

### Promise Wrapper

```javascript
function timeout(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

async function fetchWithTimeout(url, timeoutMs = 5000) {
  const controller = new AbortController();
  const timeoutId = setTimeout(() => controller.abort(), timeoutMs);

  try {
    const response = await fetch(url, { signal: controller.signal });
    clearTimeout(timeoutId);
    return await response.json();
  } catch (error) {
    clearTimeout(timeoutId);
    throw error;
  }
}
```

---

_Best Practices last updated: November 12, 2025_
