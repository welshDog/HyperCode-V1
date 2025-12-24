// Fibonacci sequence in HyperCode
func fib(n) {
    if n <= 1 {
        return n
    }
    return fib(n-1) + fib(n-2)
}

// Print first 10 Fibonacci numbers
for i in 0..10 {
    print(f"fib({i}) = {fib(i)}")
}
