import sqlite3
import os
from typing import List, Dict, Any, Optional

class TodoStore:
    """
    REAL PERSISTENT TODO STORE.
    Replaces the in-memory simulation with a SQLite-backed task manager.
    Ensures long-running mission steps are preserved across agent cycles.
    """
    def __init__(self, db_path: str = "data/memory/shadow_tasks.db"):
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
        self._init_db()

    def _init_db(self):
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS todos (
                id TEXT PRIMARY KEY,
                content TEXT NOT NULL,
                status TEXT NOT NULL DEFAULT 'pending',
                updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)
        self.conn.commit()

    def write(self, todos: List[Dict[str, Any]], merge: bool = False) -> List[Dict[str, Any]]:
        """Write or update tasks. Absolute reality: No placeholders."""
        if not merge:
            self.conn.execute("DELETE FROM todos")
        
        for t in todos:
            self.conn.execute("""
                INSERT INTO todos (id, content, status, updated_at)
                VALUES (?, ?, ?, CURRENT_TIMESTAMP)
                ON CONFLICT(id) DO UPDATE SET
                    content=excluded.content,
                    status=excluded.status,
                    updated_at=CURRENT_TIMESTAMP
            """, (t.get('id'), t.get('content'), t.get('status', 'pending')))
        
        self.conn.commit()
        return self.list_all()

    def list_all(self) -> List[Dict[str, Any]]:
        cursor = self.conn.execute("SELECT id, content, status FROM todos ORDER BY updated_at ASC")
        return [dict(row) for row in cursor.fetchall()]

    def has_items(self) -> bool:
        cursor = self.conn.execute("SELECT COUNT(*) FROM todos")
        return cursor.fetchone()[0] > 0

    def format_for_injection(self) -> str:
        items = self.list_all()
        if not items:
            return ""
        
        output = "\n### 📋 CURRENT MISSION TASKS (TODO)\n"
        for i in items:
            check = " [x] " if i['status'] == 'completed' else " [ ] "
            output += f"{check} {i['id']}: {i['content']} ({i['status']})\n"
        return output
