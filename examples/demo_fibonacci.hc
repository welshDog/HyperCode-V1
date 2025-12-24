// Demo 2: Fibonacci - Recursion Made Simple
// This demonstrates functions and recursion

func fib(n) {
    if n <= 1 {
        return n;
    }
    return fib(n - 1) + fib(n - 2);
}

// Calculate first 10 Fibonacci numbers
print("Fibonacci sequence:");
print("fib(0) =", fib(0));
print("fib(1) =", fib(1));
print("fib(2) =", fib(2));
print("fib(3) =", fib(3));
print("fib(4) =", fib(4));
print("fib(5) =", fib(5));
print("fib(6) =", fib(6));
print("fib(7) =", fib(7));