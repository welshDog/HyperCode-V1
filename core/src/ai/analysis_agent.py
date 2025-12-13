import sqlite3
import os
from datetime import datetime

# Configuration
DB_PATH = "../hypercode_metrics.db"  # Relative to core/src/ai/
REPORT_PATH = "../../../optimization_proposal.md" # Relative to core/src/ai/ (Project root/artifacts usually, but putting in root for now as requested or artifacts dir)
# Actually, artifacts dir is C:\Users\lyndz\.gemini\antigravity\brain\7c145a5b-8944-49bd-83ee-d0ffd443641d
# I will output to a local file first, then use a tool to move/write to artifact if needed, or just write directly if I know the path.
# For simplicity, let's output to the artifacts directory directly if I can, otherwise just print to stdout or a local file.
# I'll use a local file "optimization_proposal.md" in the same dir for now, then read it.

class AnalysisAgent:
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = None
        
    def connect(self):
        if not os.path.exists(self.db_path):
            raise FileNotFoundError(f"Database not found at {self.db_path}")
        self.conn = sqlite3.connect(self.db_path)
        
    def analyze_hot_paths(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT node_type, sum(count) as total_calls, sum(total_time_ns) as total_time
            FROM execution_metrics 
            GROUP BY node_type 
            ORDER BY total_time DESC
            LIMIT 5
        """)
        return cursor.fetchall()
        
    def analyze_functions(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT func_name, call_count, total_time_ns, max_recursion_depth
            FROM function_profiles
            ORDER BY total_time_ns DESC
            LIMIT 5
        """)
        return cursor.fetchall()

    def analyze_variables(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT var_name_hash, access_count, avg_scope_depth
            FROM variable_profiles
            ORDER BY access_count DESC
            LIMIT 5
        """)
        return cursor.fetchall()
        
    def generate_report(self):
        hot_nodes = self.analyze_hot_paths()
        hot_funcs = self.analyze_functions()
        hot_vars = self.analyze_variables()
        
        report = f"# HyperCode Optimization Proposal\n"
        report += f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        
        report += "## 1. Hot Path Analysis (Node Level)\n"
        report += "Telemetry shows where the interpreter spends the most time. These are candidates for 'Fast Path' optimizations or Bytecode specialization.\n\n"
        report += "| Node Type | Calls | Total Time (ns) |\n"
        report += "| :--- | :--- | :--- |\n"
        for node in hot_nodes:
            report += f"| `{node[0]}` | {node[1]:,} | {node[2]:,} |\n"
            
        report += "\n## 2. Function Profile Analysis\n"
        report += "Identifies computationally expensive functions and recursion risks.\n\n"
        report += "| Function | Calls | Total Time (ns) | Max Depth |\n"
        report += "| :--- | :--- | :--- | :--- |\n"
        for func in hot_funcs:
            report += f"| `{func[0]}` | {func[1]:,} | {func[2]:,} | {func[3]} |\n"
            
        report += "\n## 3. Variable Usage Analysis\n"
        report += "High-frequency variable lookups that could benefit from caching or index-based resolution.\n\n"
        report += "| Variable Hash | Accesses | Avg Scope Depth |\n"
        report += "| :--- | :--- | :--- |\n"
        for var in hot_vars:
            report += f"| `{var[0][:8]}...` | {var[1]:,} | {var[2]:.2f} |\n"

        report += "\n## 4. AI Recommendations\n"
        
        # Heuristic Logic
        top_node = hot_nodes[0][0] if hot_nodes else None
        
        if top_node == 'Binary':
             report += "- **CRITICAL**: `Binary` operations are the top bottleneck. Recommend implementing a threaded bytecode dispatch or JIT compilation for math-heavy workloads.\n"
        elif top_node == 'Variable':
             report += "- **CRITICAL**: Variable lookups are dominating. Recommend implementing 'Resolution Pass' to replace string lookups with integer array indices.\n"
        elif top_node == 'Call':
             report += "- **CRITICAL**: Function call overhead is high. Recommend implementing 'Tail Call Optimization' (TCO) if recursion depth is high.\n"
             
        if hot_vars and hot_vars[0][1] > 1000:
             report += "- **High Traffic Variables**: Detailed variable analysis suggests implementing an 'Inline Cache' for global/closure variables.\n"

        if any(f[3] > 100 for f in hot_funcs):
             report += "- **Recursion Risk**: Detected deep recursion (>100 frames). Recommend automatic switch to iterative interpreter or TCO.\n"

        return report

    def run(self):
        try:
            self.connect()
            report = self.generate_report()
            print(report)
            
            # Write to file
            with open("optimization_proposal.md", "w", encoding="utf-8") as f:
                f.write(report)
                
            print(f"\n[SUCCESS] Report generated: optimization_proposal.md")
        except Exception as e:
            print(f"[ERROR] Analysis failed: {e}")
        finally:
            if self.conn:
                self.conn.close()

if __name__ == "__main__":
    # Assuming run from core/src/ai/
    agent = AnalysisAgent("../hypercode_metrics.db")
    agent.run()
