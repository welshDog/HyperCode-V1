# HyperCode Recipes

## Table of Contents

1. [String Manipulation](#string-manipulation)
2. [Array Operations](#array-operations)
3. [Object Manipulation](#object-manipulation)
4. [Async Patterns](#async-patterns)
5. [File Operations](#file-operations)
6. [Data Validation](#data-validation)
7. [Date and Time](#date-and-time)
8. [Networking](#networking)
9. [Error Handling](#error-handling)
10. [Performance](#performance)

## String Manipulation

### Reverse a String

```javascript
function reverseString(str) {
  return str.split("").reverse().join("");
}

reverseString("hello"); // 'olleh'
```

### Generate Random String

```javascript
function randomString(length = 8) {
  const chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
  let result = "";
  for (let i = 0; i < length; i++) {
    result += chars.charAt(Math.floor(Math.random() * chars.length));
  }
  return result;
}
```

## Array Operations

### Find Unique Elements

```javascript
function unique(array) {
  return [...new Set(array)];
}

unique([1, 2, 2, 3, 4, 4, 5]); // [1, 2, 3, 4, 5]
```

### Group By Property

```javascript
function groupBy(array, key) {
  return array.reduce((acc, item) => {
    const group = item[key];
    if (!acc[group]) acc[group] = [];
    acc[group].push(item);
    return acc;
  }, {});
}

const users = [
  { id: 1, name: "Alice", role: "admin" },
  { id: 2, name: "Bob", role: "user" },
  { id: 3, name: "Charlie", role: "admin" },
];

groupBy(users, "role");
/*
{
    admin: [
        { id: 1, name: 'Alice', role: 'admin' },
        { id: 3, name: 'Charlie', role: 'admin' }
    ],
    user: [
        { id: 2, name: 'Bob', role: 'user' }
    ]
}
*/
```

## Object Manipulation

### Deep Clone Object

```javascript
function deepClone(obj) {
  return JSON.parse(JSON.stringify(obj));
}

// Or using the structured clone API (if available)
function deepClone(obj) {
  return structuredClone ? structuredClone(obj) : JSON.parse(JSON.stringify(obj));
}
```

### Merge Objects

```javascript
function mergeObjects(...objects) {
  return Object.assign({}, ...objects);
}

const defaults = { theme: "light", fontSize: 14 };
const userSettings = { fontSize: 16, darkMode: true };

mergeObjects(defaults, userSettings);
// { theme: 'light', fontSize: 16, darkMode: true }
```

## Async Patterns

### Retry with Exponential Backoff

```javascript
async function fetchWithRetry(url, maxRetries = 3) {
  let lastError;

  for (let i = 0; i < maxRetries; i++) {
    try {
      const response = await fetch(url);
      if (response.ok) return await response.json();
      throw new Error(`HTTP error! status: ${response.status}`);
    } catch (error) {
      lastError = error;
      const delay = Math.pow(2, i) * 1000;
      await new Promise((resolve) => setTimeout(resolve, delay));
    }
  }

  throw lastError;
}
```

### Parallel Execution with Limit

```javascript
async function mapConcurrent(array, asyncFn, concurrency = 5) {
  const results = [];
  const executing = [];

  for (const item of array) {
    const p = Promise.resolve().then(() => asyncFn(item));
    results.push(p);

    const e = p.then(() => executing.splice(executing.indexOf(e), 1));
    executing.push(e);

    if (executing.length >= concurrency) {
      await Promise.race(executing);
    }
  }

  return Promise.all(results);
}
```

## File Operations

### Read File Line by Line

```javascript
const fs = import("fs");
const readline = import("readline");

async function processFileByLine(filename, processLine) {
  const fileStream = fs.createReadStream(filename);
  const rl = readline.createInterface({
    input: fileStream,
    crlfDelay: Infinity,
  });

  for await (const line of rl) {
    await processLine(line);
  }
}
```

### Watch File for Changes

```javascript
const fs = import("fs");

function watchFile(filename, callback) {
  let lastMtime = null;

  setInterval(() => {
    try {
      const stats = fs.statSync(filename);
      if (lastMtime && stats.mtime > lastMtime) {
        callback();
      }
      lastMtime = stats.mtime;
    } catch (error) {
      console.error("Error watching file:", error);
    }
  }, 1000); // Check every second
}
```

## Data Validation

### Validate Email

```javascript
function isValidEmail(email) {
  const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return re.test(String(email).toLowerCase());
}
```

### Schema Validation

```javascript
function validate(schema, data) {
  const errors = [];

  for (const [key, validator] of Object.entries(schema)) {
    try {
      validator(data[key]);
    } catch (error) {
      errors.push({
        field: key,
        error: error.message,
      });
    }
  }

  return {
    valid: errors.length === 0,
    errors,
  };
}

// Usage
const userSchema = {
  username: (value) => {
    if (!value) throw new Error("Username is required");
    if (value.length < 3) throw new Error("Username too short");
  },
  email: (value) => {
    if (!isValidEmail(value)) throw new Error("Invalid email");
  },
};

const result = validate(userSchema, { username: "al", email: "invalid" });
```

## Date and Time

### Format Date

```javascript
function formatDate(date, format = "YYYY-MM-DD") {
  const d = new Date(date);
  const pad = (num) => String(num).padStart(2, "0");

  return format
    .replace(/YYYY/g, d.getFullYear())
    .replace(/MM/g, pad(d.getMonth() + 1))
    .replace(/DD/g, pad(d.getDate()))
    .replace(/HH/g, pad(d.getHours()))
    .replace(/mm/g, pad(d.getMinutes()))
    .replace(/ss/g, pad(d.getSeconds()));
}

formatDate(new Date(), "YYYY-MM-DD HH:mm:ss"); // '2025-11-12 19:30:45'
```

### Time Since

```javascript
function timeSince(date) {
  const seconds = Math.floor((new Date() - new Date(date)) / 1000);

  const intervals = {
    year: 31536000,
    month: 2592000,
    week: 604800,
    day: 86400,
    hour: 3600,
    minute: 60,
  };

  for (const [unit, secondsInUnit] of Object.entries(intervals)) {
    const interval = Math.floor(seconds / secondsInUnit);
    if (interval >= 1) {
      return interval === 1 ? `${interval} ${unit} ago` : `${interval} ${unit}s ago`;
    }
  }

  return "just now";
}
```

## Networking

### Simple HTTP Server

```javascript
const http = import("http");

const server = http.createServer((req, res) => {
  if (req.url === "/") {
    res.status(200).send("Hello, World!");
  } else if (req.url === "/api/data") {
    res.status(200).json({ message: "API Response" });
  } else {
    res.status(404).send("Not Found");
  }
});

server.listen(3000, () => {
  console.log("Server running on http://localhost:3000");
});
```

### Fetch with Timeout

```javascript
async function fetchWithTimeout(url, options = {}, timeout = 5000) {
  const controller = new AbortController();
  const timeoutId = setTimeout(() => controller.abort(), timeout);

  try {
    const response = await fetch(url, {
      ...options,
      signal: controller.signal,
    });
    clearTimeout(timeoutId);
    return response;
  } catch (error) {
    clearTimeout(timeoutId);
    throw error;
  }
}
```

## Error Handling

### Error Boundary

```javascript
class ErrorBoundary {
  constructor(component) {
    this.component = component;
    this.state = { hasError: false, error: null };
  }

  static getDerivedStateFromError(error) {
    return { hasError: true, error };
  }

  componentDidCatch(error, errorInfo) {
    console.error("Error caught by boundary:", error, errorInfo);
  }

  render() {
    if (this.state.hasError) {
      return <div>Something went wrong: {this.state.error.message}</div>;
    }
    return this.component;
  }
}
```

### Retry with Exponential Backoff

```javascript
async function retryWithBackoff(fn, maxRetries = 3, baseDelay = 1000) {
  let lastError;

  for (let i = 0; i < maxRetries; i++) {
    try {
      return await fn();
    } catch (error) {
      lastError = error;
      if (i < maxRetries - 1) {
        const delay = baseDelay * Math.pow(2, i) + Math.random() * 1000;
        await new Promise((resolve) => setTimeout(resolve, delay));
      }
    }
  }

  throw lastError;
}
```

## Performance

### Debounce Function

```javascript
function debounce(fn, delay) {
  let timeoutId;
  return function (...args) {
    clearTimeout(timeoutId);
    timeoutId = setTimeout(() => fn.apply(this, args), delay);
  };
}

// Usage
const handleResize = debounce(() => {
  console.log("Window resized");
}, 250);

window.addEventListener("resize", handleResize);
```

### Memoization

```javascript
function memoize(fn) {
  const cache = new Map();

  return function (...args) {
    const key = JSON.stringify(args);
    if (cache.has(key)) {
      return cache.get(key);
    }

    const result = fn.apply(this, args);
    cache.set(key, result);
    return result;
  };
}

// Usage
const expensiveCalculation = memoize(function (n) {
  console.log("Calculating...");
  return n * 2;
});

expensiveCalculation(5); // Calculates and caches
expensiveCalculation(5); // Returns cached result
```

---

_Recipes last updated: November 12, 2025_
