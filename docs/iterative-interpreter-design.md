# Technical Design: Recursive-to-Iterative Interpreter Rewrite

**Status:** Draft
**Date:** 2025-12-12
**Target:** Phase 9 (Execution)

## 1. Problem Statement
The current HyperCode interpreter is **recursive**. It relies on the host Python call stack (`evaluate` calls `evaluate`).
- **Limitation 1:** `RecursionError`. Python's stack limit (~1000) limits HyperCode recursion depth.
- **Limitation 2:** Overhead. Python stack frames are heavy.
- **Limitation 3:** Inflexibility. Hard to implement "pause/resume", coroutines, or step-debugging.

## 2. Proposed Solution: Explicit Stack Machine
We will refactor the `Interpreter` to use an **iterative loop** with an explicit, heap-allocated stack.

### 2.1 The "Frame" Concept
Instead of Python function calls, we define a lightweight `Frame` or `Task` object.

```python
class Task:
    def __init__(self, node, env):
        self.node = node
        self.env = env
        self.pc = 0 # Program Counter (for block statements)
```

### 2.2 The Evaluation Loop
The core `evaluate` method transforms into a loop:

```python
def run(self, root_node):
    stack = [Task(root_node, self.globals)]
    value_stack = [] # Operands
    
    while stack:
        frame = stack.pop()
        # Dispatch based on node type
        # Push new frames to stack instead of recursive calls
```

## 3. Detailed Architecture

### 3.1 Handling Expressions (Post-Order Traversal)
For a binary operation `A + B`:
1.  Push `BinaryOp(A, B)` task.
2.  Loop pops `BinaryOp`:
    - Checks if children evaluated.
    - If not, push `BinaryOp` back, push `Task(B)`, push `Task(A)`.
    - If yes, pop 2 values from `value_stack`, add, push result.

*Alternative:* Use a compilation step to flatten AST to bytecode, which is naturally iterative.
*Decision:* For this phase, we stick to **AST-walking with a trampoline** or explicit stack to avoid writing a full compiler yet.

### 3.2 Trampolining (Simpler Intermediate Step)
To avoid managing a complex instruction pointer, we can use generators logic.
`evaluate(node)` yields sub-nodes to evaluate. The central loop sends results back.

```python
def evaluate(self, node):
    if isinstance(node, Binary):
        left = yield node.left
        right = yield node.right
        return left + right
```

## 4. Implementation Stages

### Stage 1: The `IterativeInterpreter` Stub
Create a parallel class `core.src.core.iterative_interpreter.IterativeInterpreter`.
Does not replace `Interpreter` yet.

### Stage 2: The Core Loop
Implement the `while` loop that drives execution. Support literals and basic math.

### Stage 3: Control Flow
Implement `If`, `While`, `Block` using the stack.
*Crucial:* `While` loops shouldn't grow the stack indefinitely.

### Stage 4: Function Calls
Reimplement `Call` to push a new `Frame` (with new Environment) rather than calling a Python method.
**Benefit:** Infinite recursion (until RAM exhausted) becomes possible.

## 5. Risks & Mitigations
- **Complexity:** Iterative AST walkers are harder to read than recursive ones.
    - *Mitigation:* Extensive documentation and type hinting.
- **Performance:** Python overhead for object creation (`Task` objects) might be slower than C-stack recursion for shallow programs.
    - *Mitigation:* Use `slots`, reuse objects, or eventually move to bytecode.

## 6. Verification
- **Unit Tests:** Must pass 100% of existing `tests/`.
- **Benchmark:** Compare `fib(22)` on Iterative vs Recursive. 
    - *Goal:* Parity or Speedup. Even parity is a win due to safety (no stack overflow).
