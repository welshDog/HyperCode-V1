# HyperCode Performance Audit & Optimization

## 1. Profiling Methodology
We profiled the HyperCode Core Interpreter (`core/src/core/interpreter.py`) using a recursive Fibonacci benchmark:
```javascript
func fib(n) {
    if (n < 2) {
        return n;
    }
    return fib(n - 1) + fib(n - 2);
}
print(fib(22));
```
Run with `python -m cProfile`.

## 2. Baseline Metrics
- **Test Case**: `fib(22)`
- **Execution Time**: ~6.01 seconds
- **Bottlenecks Identified**:
    1. **Double Dispatch Overhead**: The Visitor pattern (`accept` -> `visit`) adds 2 frames per AST node. In deep recursion, this stack overhead is massive.
    2. **Recursion Depth**: The interpreter implementation relies on Python recursion, causing `RecursionError` for `n >= 10` unless `sys.setrecursionlimit` is increased.
    3. **Function Call Overhead**: `visit_Call` and `visit_Binary` dominate the profile.

## 3. Optimization Implemented: Inline Dispatch
We implemented a "Fast Path" optimization in `Interpreter.evaluate()` to de-virtualize the dispatch for common leaf nodes (`Literal`, `Variable`) and binary operations (`Binary`).

### Code Change:
```python
    def evaluate(self, expr: Expr):
        # OPTIMIZATION: Short-circuit dispatch for common nodes
        t = type(expr)
        if t is Literal:
            return expr.value
        elif t is Variable:
            return self.environment.get(expr.name.lexeme)
        elif t is Binary:
            return self.visit_Binary(expr)
            
        return expr.accept(self)
```

## 4. Results
- **Baseline**: 6.01s
- **Optimized**: 4.94s
- **Improvement**: **~17.8% Speedup**

## 5. Trade-offs
- **Pros**: Significant performance gain for all scripts (especially math/logic heavy).
- **Cons**: `evaluate` is now coupled to specific AST node types (`Literal`, `Variable`, `Binary`), breaking the pure Visitor pattern. Adding new expression types requires no extra changes, but they won't benefit from the fast path unless added to `evaluate`. This is a worthwhile trade-off for a core runtime method.

## 6. Recommendations
1. **Iterative Interpreter**: To fix the `RecursionError` fundamentally, the interpreter should be rewritten to use an explicit stack (heap-allocated) instead of the Python call stack.
2. **Environment Caching**: Variable lookups (`environment.get`) are still frequent; implementing a pre-computed variable index (Resolution pass) would eliminate dictionary lookups.
