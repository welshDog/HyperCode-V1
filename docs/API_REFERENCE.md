# HyperCode API Reference

## Table of Contents

1. [Built-in Functions](#built-in-functions)
   - [Input/Output](#inputoutput)
   - [Type Conversion](#type-conversion)
   - [Math Operations](#math-operations)
   - [String Operations](#string-operations)
   - [Collection Methods](#collection-methods)
2. [Standard Library](#standard-library)
   - [File System](#file-system)
   - [Date and Time](#date-and-time)
   - [JSON Handling](#json-handling)
3. [Error Handling](#error-handling)
4. [Modules](#modules)
   - [HTTP Module](#http-module)
   - [Random Module](#random-module)

## Built-in Functions

### Input/Output

#### `print(value1, value2, ..., valueN)`

Prints values to the standard output.

```javascript
print("Hello", "World"); // Hello World
print(42, "is the answer"); // 42 is the answer
```

#### `input([prompt])`

Reads a line from standard input.

```javascript
const name = input("Enter your name: ");
print(`Hello, ${name}!`);
```

### Type Conversion

#### `Number(value)`

Converts a value to a number.

```javascript
Number("42"); // 42
Number("3.14"); // 3.14
Number("abc"); // null
```

#### `String(value)`

Converts a value to a string.

```javascript
String(42); // "42"
String(true); // "true"
String([1, 2, 3]); // "1,2,3"
```

#### `Boolean(value)`

Converts a value to a boolean.

```javascript
Boolean(1); // true
Boolean(0); // false
Boolean("text"); // true
Boolean(""); // false
```

### Math Operations

#### `Math` Object

```javascript
Math.PI; // 3.141592653589793
Math.E; // 2.718281828459045
Math.abs(-5); // 5
Math.ceil(4.2); // 5
Math.floor(4.9); // 4
Math.round(4.5); // 5
Math.max(1, 2, 3); // 3
Math.min(1, 2, 3); // 1
Math.random(); // Random number between 0 and 1
Math.sqrt(16); // 4
Math.pow(2, 3); // 8
```

### String Operations

#### String Methods

```javascript
const str = "Hello, World!";

str.length(); // 13
str.upper(); // "HELLO, WORLD!"
str.lower(); // "hello, world!"
str.trim(); // Removes whitespace
str.indexOf("World"); // 7
str.substring(0, 5); // "Hello"
str.split(","); // ["Hello", " World!"]
str.replace("World", "HyperCode"); // "Hello, HyperCode!"
```

### Collection Methods

#### Array Methods

```javascript
const arr = [1, 2, 3]

arr.length()           // 3
arr.push(4)           // [1, 2, 3, 4]
arr.pop()             // 4, arr is now [1, 2, 3]
arr.unshift(0)        // [0, 1, 2, 3]
arr.shift()           // 0, arr is now [1, 2, 3]
arr.includes(2)       // true
arr.indexOf(2)        // 1
arr.join(", ")         // "1, 2, 3"
arr.map(fn(x) { return x * 2 }) // [2, 4, 6]
arr.filter(fn(x) { return x > 1 }) // [2, 3]
arr.reduce(fn(acc, x) { return acc + x }, 0) // 6
```

#### Map Methods

```javascript
const map = { a: 1, b: 2 };

map.keys(); // ["a", "b"]
map.values(); // [1, 2]
map.entries(); // [["a", 1], ["b", 2]]
map.has("a"); // true
map.get("a"); // 1
map.set("c", 3);
map.delete("a");
map.clear();
```

## Standard Library

### File System

```javascript
const fs = import("fs");

// Read file
const content = fs.readFile("file.txt");

// Write file
fs.writeFile("output.txt", "Hello, World!");

// Check if file exists
if (fs.exists("file.txt")) {
  print("File exists");
}
```

### Date and Time

```javascript
const now = new Date();
now.toString(); // "Wed Nov 12 2025 19:23:45 GMT-0500"
now.getFullYear(); // 2025
now.getMonth(); // 10 (0-based)
now.getDate(); // 12
now.getHours(); // 19
now.getMinutes(); // 23
now.getSeconds(); // 45
now.getTime(); // Timestamp in milliseconds
```

### JSON Handling

```javascript
const obj = { name: "Alice", age: 30 };
const json = JSON.stringify(obj); // '{"name":"Alice","age":30}'
const parsed = JSON.parse(json); // {name: "Alice", age: 30}
```

## Error Handling

### Try/Catch

```javascript
try {
  const result = 10 / 0;
  if (!isFinite(result)) {
    throw "Division by zero";
  }
} catch (error) {
  print(`Error: ${error}`);
} finally {
  print("Cleanup code here");
}
```

## Modules

### HTTP Module

```javascript
const http = import("http")

// Create server
const server = http.createServer(fn(req, res) {
    res.status(200).send("Hello, World!")
})

server.listen(3000, fn() {
    print("Server running at http://localhost:3000/")
})
```

### Random Module

```javascript
const random = import("random");

random.int(1, 10); // Random integer between 1 and 10
random.float(0, 1); // Random float between 0 and 1
random.choice([1, 2, 3]); // Random element from array
random.shuffle([1, 2, 3]); // Shuffled array
```

---

_API Reference last updated: November 12, 2025_
