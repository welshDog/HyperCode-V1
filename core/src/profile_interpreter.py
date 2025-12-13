import sys
import os
import time
import cProfile
import pstats
from io import StringIO

sys.setrecursionlimit(3000)

# Add source directory to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

print("Starting Profiler...", flush=True)

try:
    from core.lexer import Lexer
    from core.parser import Parser
    from core.interpreter import Interpreter
    print("Imports Successful.", flush=True)
except ImportError as e:
    print(f"Import Error: {e}", flush=True)
    # Fallback for different execution contexts
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "core/src")))
    try:
        from core.lexer import Lexer
        from core.parser import Parser
        from core.interpreter import Interpreter
        print("Fallback Imports Successful.", flush=True)
    except ImportError as e2:
        print(f"Fallback Failed: {e2}", flush=True)
        sys.exit(1)

def profile_hypercode():
    # Recursive Fibonacci to stress function calls and variable lookups
    source = """
    func fib(n) {
        if (n < 2) {
            return n;
        }
        return fib(n - 1) + fib(n - 2);
    }
    
    let start = clock();
    print(fib(22));
    print("Time running (s):");
    print(clock() - start);
    """

    print("--- Parsing ---", flush=True)
    try:
        lexer = Lexer(source)
        tokens = lexer.scan_tokens()
        print(f"Tokens: {len(tokens)}", flush=True)
        # for t in tokens: print(t)
        parser = Parser(tokens)
        statements = parser.parse()
        print(f"Parsed {len(statements)} statements.", flush=True)
    except Exception as e:
        print(f"Parsing Error: {e}", flush=True)
        return

    interpreter = Interpreter()

    print("--- Profiling Execution ---", flush=True)
    
    # Profile the interpret call
    pr = cProfile.Profile()
    pr.enable()
    
    try:
        interpreter.interpret(statements)
    except Exception as e:
        print(f"Runtime Error: {e}", flush=True)
        import traceback
        traceback.print_exc()
    
    pr.disable()
    
    s = StringIO()
    sortby = 'cumulative'
    ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    ps.print_stats(20)
    print(s.getvalue(), flush=True)

if __name__ == "__main__":
    profile_hypercode()
