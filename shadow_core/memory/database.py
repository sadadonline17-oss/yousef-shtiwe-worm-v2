import sqlite3
import os

class ShadowMemory:
    """Long-term intelligence and skill persistence for SHADOW."""
    def __init__(self, db_path="data/shadow_memory.db"):
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        self.conn = sqlite3.connect(db_path)
        self._init_db()

    def _init_db(self):
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS memory (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                task TEXT,
                intel TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)
        self.conn.commit()

    def persist(self, task, intel):
        self.conn.execute("INSERT INTO memory (task, intel) VALUES (?, ?)", (task, intel))
        self.conn.commit()

    def search(self, query):
        # Basic keyword search for now
        cursor = self.conn.execute("SELECT intel FROM memory WHERE task LIKE ? LIMIT 3", (f"%{query}%",))
        rows = cursor.fetchall()
        return "\n---\n".join([r[0] for r in rows]) if rows else None
