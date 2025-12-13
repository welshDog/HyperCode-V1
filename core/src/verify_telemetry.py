import sqlite3
import os

DB_PATH = "hypercode_metrics.db"

def verify_metrics():
    if not os.path.exists(DB_PATH):
        print(f"❌ Database not found at {DB_PATH}")
        return

    print(f"[OK] Database found at {DB_PATH}")
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    print("\n--- Execution Metrics (Top 5) ---")
    cursor.execute("SELECT node_type, sum(count), sum(total_time_ns) FROM execution_metrics GROUP BY node_type ORDER BY sum(count) DESC LIMIT 5")
    for row in cursor.fetchall():
        print(f"Node: {row[0]:<15} Count: {row[1]:<10} Time(ns): {row[2]}")

    print("\n--- Function Profiles ---")
    cursor.execute("SELECT func_name, call_count, total_time_ns, max_recursion_depth FROM function_profiles ORDER BY call_count DESC")
    for row in cursor.fetchall():
        print(f"Func: {row[0]:<15} Calls: {row[1]:<10} Time(ns): {row[2]:<15} Max Depth: {row[3]}")

    print("\n--- Variable Profiles (Top 5) ---")
    cursor.execute("SELECT var_name_hash, access_count, avg_scope_depth FROM variable_profiles ORDER BY access_count DESC LIMIT 5")
    for row in cursor.fetchall():
        print(f"Hash: {row[0][:8]:<15} Accesses: {row[1]:<10} Avg Depth: {row[2]:.2f}")

    conn.close()

if __name__ == "__main__":
    verify_metrics()
