import os
import sys
import time
import sqlite3
import uuid
from pathlib import Path

# Paths
CORE_DIR = Path(__file__).parent
BENCHMARKS_DIR = CORE_DIR.parent / "benchmarks"
DB_PATH = CORE_DIR / "hypercode_metrics.db"

# Configuration
BENCHMARKS = ["fib_22.hc", "loop_ops.hc", "string_ops.hc"]
REGRESSION_THRESHOLD = 0.05 # 5%

def run_benchmark(filename):
    filepath = BENCHMARKS_DIR / filename
    if not filepath.exists():
        print(f"[ERROR] Benchmark not found: {filename}")
        return None

    print(f"Running {filename}...", end="", flush=True)
    
    start_ns = time.time_ns()
    try:
        # In-process execution for accurate telemetry hooks
        from core.lexer import Lexer
        from core.parser import Parser
        from core.interpreter import Interpreter
        
        # Reset modules if needed or just instantiate new classes
        # Since python modules cache, classes are reused but instances are new.
        
        with open(filepath, 'r') as f:
            source = f.read()

        lexer = Lexer(source)
        tokens = lexer.scan_tokens()
        parser = Parser(tokens)
        statements = parser.parse()
        
        interpreter = Interpreter()
        interpreter.interpret(statements)
        
        # Flush telemetry (if any was collected buffer-wise)
        if hasattr(interpreter, 'telemetry'):
             interpreter.telemetry.close()
        
        duration_ns = time.time_ns() - start_ns
        print(f" DONE ({duration_ns / 1e9:.4f}s)")
        return duration_ns

    except Exception as e:
        print(f" FAILED: {e}")
        return None

def check_regression(current_results):
    print("\n--- AI Regression Check ---")
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    regressions = []
    
    for bench, curr_duration in current_results.items():
        if curr_duration is None: continue
        
        # Get average of last 5 successful runs for this benchmark
        cursor.execute("""
            SELECT AVG(duration_ns) FROM (
                SELECT duration_ns FROM ci_runs 
                WHERE benchmark = ? 
                ORDER BY timestamp DESC 
                LIMIT 5
            )
        """, (bench,))
        row = cursor.fetchone()
        
        if row and row[0]:
            baseline = row[0]
            diff = (curr_duration - baseline) / baseline
            
            print(f"[{bench}] Current: {curr_duration/1e9:.4f}s | Baseline: {baseline/1e9:.4f}s | Diff: {diff*100:+.2f}%")
            
            if diff > REGRESSION_THRESHOLD:
                regressions.append(f"{bench} is {diff*100:.1f}% slower")
        else:
            print(f"[{bench}] First run (New Baseline).")

    if regressions:
        print("\n[FAIL] Performance Regression Detected:")
        for r in regressions:
            print(f" - {r}")
        return False
    
    print("\n[PASS] No performance regressions.")
    return True

def record_ci_run(build_id, results):
    conn = sqlite3.connect(DB_PATH)
    with conn:
        conn.execute("CREATE TABLE IF NOT EXISTS ci_runs (build_id TEXT, benchmark TEXT, duration_ns INTEGER, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)")
        
        for bench, duration in results.items():
            if duration is not None:
                conn.execute("INSERT INTO ci_runs (build_id, benchmark, duration_ns) VALUES (?, ?, ?)", (build_id, bench, duration))
    print(f"[OK] CI Run {build_id} recorded.")

def main():
    sys.path.append(str(CORE_DIR))
    
    build_id = f"CI-{uuid.uuid4().hex[:8]}"
    print(f"[START] HyperCode CI Pipeline [Build: {build_id}]")
    print(f"Benchmarks: {BENCHMARKS_DIR}")

    results = {}
    execution_failure = False

    for bench in BENCHMARKS:
        duration = run_benchmark(bench)
        results[bench] = duration
        if duration is None:
            execution_failure = True

    record_ci_run(build_id, results)

    if execution_failure:
        print("[FAIL] Pipeline Failed: One or more benchmarks crashed.")
        sys.exit(1)
        
    # Regression Check
    if not check_regression(results):
        sys.exit(1) # Fail build on regression
    
    print("[SUCCESS] Pipeline Complete.")

if __name__ == "__main__":
    main()
