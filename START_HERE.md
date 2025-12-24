# 🚀 HyperCode: First Hour Guide

Welcome to HyperCode! This guide will help you get started with the codebase in under an hour.

## 🛠️ Quick Setup

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/your-username/hypercode.git
   cd hypercode
   ```

2. **Set Up Environment** (macOS/Linux):

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -e ".[dev]"
   ```

## 🧪 Your First Run

1. **Create a Test File**:

   ```bash
   echo 'print("Hello from HyperCode!")' > hello.hc
   ```

2. **Run It**:

   ```bash
   python -m hypercode run hello.hc
   # Output: Hello from HyperCode!
   ```

## 🔍 Codebase Tour

### Core Components

1. **Lexer** (`src/hypercode/core/lexer.py`):
   - Converts source code to tokens
   - Try adding a new token type

2. **Parser** (`src/hypercode/core/parser.py`):
   - Converts tokens to AST
   - Uses recursive descent parsing

3. **Interpreter** (`src/hypercode/core/interpreter.py`):
   - Executes the AST
   - Manages variables and scope

### AI Integration

```python
# In a Python shell
from hypercode.ai import EnhancedPerplexityClient

ai = EnhancedPerplexityClient()
print(ai.generate("Explain how the parser works"))
```

## 🛠️ First Task: Add a Built-in Function

Let's add a simple `square` function:

1. **Add Test**:

   ```python
   # tests/unit/test_builtins.py
   def test_square():
       assert run_hypercode('square(4)') == 16
   ```

2. **Implement**:

   ```python
   # src/hypercode/core/builtins.py
   @builtin
   def square(x: int) -> int:
       """Returns the square of a number."""
       return x * x
   ```

3. **Test It**:

   ```bash
   pytest tests/unit/test_builtins.py -v
   ```

## 🧠 AI-Powered Development

### Get Code Help

```python
# In your editor with AI plugin
# Select code and use "Explain" or "Refactor"
def example():
    # AI can help here
    pass
```

### Generate Documentation

```python
def calculate_fibonacci(n):
    """
    Calculate the nth Fibonacci number.
    
    Args:
        n: The position in the Fibonacci sequence
        
    Returns:
        The nth Fibonacci number
    """
```

## 📚 Next Steps

1. Explore `examples/` for more complex usage
2. Check `ARCHITECTURE.md` for system design
3. Look for "good first issue" labels
4. Join our community chat for help

---

✨ **You're all set!** Start exploring and happy coding! ✨
