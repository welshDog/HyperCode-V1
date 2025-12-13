import sqlite3
import time
import uuid
import hashlib
from dataclasses import dataclass
from typing import Optional, Dict, Any
from pathlib import Path

# Database Schema Definitions
SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS execution_metrics (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    node_type TEXT NOT NULL,
    count INTEGER DEFAULT 1,
    total_time_ns INTEGER DEFAULT 0,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    build_id TEXT
);

CREATE TABLE IF NOT EXISTS function_profiles (
    func_name TEXT PRIMARY KEY,
    call_count INTEGER DEFAULT 0,
    total_time_ns INTEGER DEFAULT 0,
    max_recursion_depth INTEGER DEFAULT 0,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS variable_profiles (
    var_name_hash TEXT PRIMARY KEY,
    access_count INTEGER DEFAULT 0,
    avg_scope_depth REAL DEFAULT 0,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS error_profiles (
    error_type TEXT,
    message_hash TEXT,
    count INTEGER DEFAULT 0,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (error_type, message_hash)
);
"""

@dataclass
class TelemetryConfig:
    db_path: str = "hypercode_metrics.db"
    enabled: bool = True
    batch_size: int = 100

class TelemetryCollector:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(TelemetryCollector, cls).__new__(cls)
        return cls._instance

    def __init__(self, config: TelemetryConfig = None):
        if hasattr(self, 'initialized'):
            return
        
        self.config = config or TelemetryConfig()
        self.buffer = []
        self.build_id = str(uuid.uuid4())[:8]
        self.conn = None
        self.initialized = True
        
        if self.config.enabled:
            self._init_db()

    def _init_db(self):
        try:
            db_path = Path(self.config.db_path)
            self.conn = sqlite3.connect(db_path)
            with self.conn:
                self.conn.executescript(SCHEMA_SQL)
        except Exception as e:
            print(f"Telemetry DB Init Failed: {e}")
            self.config.enabled = False

    def log_node_exec(self, node_type: str, duration_ns: int):
        if not self.config.enabled:
            return
        
        # Simple buffering strategy
        self.buffer.append((node_type, duration_ns))
        
        if len(self.buffer) >= self.config.batch_size:
            self._flush_buffer()

    def _flush_buffer(self):
        if not self.buffer or not self.conn:
            return

        # Aggregate buffer to reduce inserts
        agg: Dict[str, list] = {}  # type: [count, total_time]
        for n_type, duration in self.buffer:
            if n_type not in agg:
                agg[n_type] = [0, 0]
            agg[n_type][0] += 1
            agg[n_type][1] += duration
        
        data = [
            (n_type, stats[0], stats[1], self.build_id)
            for n_type, stats in agg.items()
        ]

        try:
            with self.conn:
                self.conn.executemany(
                    "INSERT INTO execution_metrics (node_type, count, total_time_ns, build_id) VALUES (?, ?, ?, ?)",
                    data
                )
            self.buffer.clear()
        except Exception as e:
            print(f"Telemetry Flush Failed: {e}")

    def log_variable_access(self, var_name: str, scope_depth: int):
        if not self.config.enabled:
            return
            
        var_hash = hashlib.sha256(var_name.encode()).hexdigest()[:16]
        
        try:
            with self.conn:
                self.conn.execute("""
                    INSERT INTO variable_profiles (var_name_hash, access_count, avg_scope_depth)
                    VALUES (?, 1, ?)
                    ON CONFLICT(var_name_hash) DO UPDATE SET
                    access_count = access_count + 1,
                    avg_scope_depth = (avg_scope_depth * access_count + excluded.avg_scope_depth) / (access_count + 1)
                """, (var_hash, scope_depth))
        except Exception as e:
            # Silently fail for perf
            pass

    def log_function_call(self, func_name: str, duration_ns: int, recursion_depth: int):
         if not self.config.enabled:
            return
         
         try:
            with self.conn:
                self.conn.execute("""
                    INSERT INTO function_profiles (func_name, call_count, total_time_ns, max_recursion_depth)
                    VALUES (?, 1, ?, ?)
                    ON CONFLICT(func_name) DO UPDATE SET
                    call_count = call_count + 1,
                    total_time_ns = total_time_ns + excluded.total_time_ns,
                    max_recursion_depth = MAX(max_recursion_depth, excluded.max_recursion_depth)
                """, (func_name, duration_ns, recursion_depth))
         except Exception as e:
            pass

    def log_error(self, error_type: str, message: str):
        if not self.config.enabled:
            return
            
        msg_hash = hashlib.sha256(message.encode()).hexdigest()[:16]
        
        try:
            with self.conn:
                self.conn.execute("""
                    INSERT INTO error_profiles (error_type, message_hash, count)
                    VALUES (?, ?, 1)
                    ON CONFLICT(error_type, message_hash) DO UPDATE SET
                    count = count + 1
                """, (error_type, msg_hash))
        except Exception:
            pass

    def close(self):
        self._flush_buffer()
        if self.conn:
            self.conn.close()
