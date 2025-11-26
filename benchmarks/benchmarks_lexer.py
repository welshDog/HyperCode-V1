# benchmarks/benchmark_lexer.py
import time
from pathlib import Path
from src.core.lexer import Lexer

def benchmark_lexer(source: str, iterations: int = 1000) -> dict:
    """Benchmark the lexer with the given source code."""
    total_time = 0
    tokens_count = 0
    errors = []
    
    for _ in range(iterations):
        start_time = time.perf_counter()
        lexer = Lexer(source)
        tokens = lexer.scan_tokens()
        end_time = time.perf_counter()
        
        total_time += (end_time - start_time)
        tokens_count = len(tokens)
        errors = lexer.errors
    
    avg_time = (total_time / iterations) * 1000  # Convert to milliseconds
    return {
        'avg_time_ms': avg_time,
        'tokens_count': tokens_count,
        'errors': errors,
        'iterations': iterations
    }

def print_benchmark_results(results: dict):
    """Print benchmark results in a readable format."""
    print("\n" + "=" * 50)
    print("Lexer Benchmark Results")
    print("=" * 50)
    print(f"Average time per lex: {results['avg_time_ms']:.4f}ms")
    print(f"Total tokens: {results['tokens_count']}")
    print(f"Iterations: {results['iterations']}")
    
    if results['errors']:
        print("\nErrors encountered:")
        for error in results['errors']:
            print(f"  - {error.message} at line {error.line}, column {error.column}")
    else:
        print("\nNo errors found.")
    print("=" * 50 + "\n")

if __name__ == "__main__":
    # Test with a sample source file
    sample_code = """
    // Sample HyperCode program
    fun factorial(n) {
        if (n <= 1) return 1;
        return n * factorial(n - 1);
    }
    
    // Calculate factorial of 5
    var result = factorial(5);
    print("Factorial of 5 is: " + result);
    """
    
    print("Running lexer benchmark with sample code...")
    results = benchmark_lexer(sample_code, iterations=1000)
    print_benchmark_results(results)