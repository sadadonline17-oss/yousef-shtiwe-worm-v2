import sqlite3
import os
import json
import logging
from datetime import datetime
from nexttoken import NextToken

client = NextToken()
DB_DIR = "SHADOW_AGENT/data/db"
DB_PATH = os.path.join(DB_DIR, "shadow_intel.db")

def _init_db():
    os.makedirs(DB_DIR, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("""
        CREATE TABLE IF NOT EXISTS targets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            domain TEXT UNIQUE,
            status TEXT,
            last_audit TEXT
        )
    """)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS intel (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            target_id INTEGER,
            type TEXT, -- 'subdomain', 'email', 'vuln', 'loot'
            content TEXT,
            timestamp TEXT DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(target_id) REFERENCES targets(id)
        )
    """)
    conn.commit()
    return conn

class ShadowOrchestrator:
    """The Master Mind: Autonomous Mission Execution."""
    def __init__(self, target_domain):
        self.target = target_domain
        self.db = _init_db()
        self._register_target()

    def _register_target(self):
        cursor = self.db.cursor()
        cursor.execute("INSERT OR IGNORE INTO targets (domain, status) VALUES (?, ?)", (self.target, "INITIALIZING"))
        self.db.commit()

    def run_autonomous_mission(self):
        """Execute Full Cyber Kill Chain automatically."""
        steps = [
            ("RECON", self._recon_phase),
            ("PROBE", self._probe_phase),
            ("EXPLOIT", self._exploit_phase),
            ("LOOT", self._loot_phase),
            ("REPORT", self._report_phase)
        ]
        
        for name, phase in steps:
            print(f"[SHADOW-AI] Entering Phase: {name}")
            phase()
        
        print("[SHADOW-AI] Mission Success. System Purged.")

    def _recon_phase(self):
        from tools.devops.stealth_recon import shadow_recon_subdomains, shadow_recon_emails
        subs = shadow_recon_subdomains(self.target)
        emails = shadow_recon_emails(self.target)
        self._save_intel("subdomain", subs)
        self._save_intel("email", emails)

    def _probe_phase(self):
        from tools.devops.probing import probe_service
        banner = probe_service(self.target, 80)
        self._save_intel("vuln", {"banner": banner})

    def _exploit_phase(self):
        # AI Logic to decide next tool based on probe
        pass

    def _loot_phase(self):
        # Exfiltration logic
        pass

    def _report_phase(self):
        from tools.devops.reporter import generate_shadow_report
        # Fetch all from DB
        cursor = self.db.cursor()
        cursor.execute("SELECT type, content FROM intel WHERE target_id = (SELECT id FROM targets WHERE domain=?)", (self.target,))
        findings = cursor.fetchall()
        generate_shadow_report(self.target, {"raw_db_intel": findings})

    def _save_intel(self, intel_type, data):
        cursor = self.db.cursor()
        target_id = cursor.execute("SELECT id FROM targets WHERE domain=?", (self.target,)).fetchone()[0]
        cursor.execute("INSERT INTO intel (target_id, type, content) VALUES (?, ?, ?)", (target_id, intel_type, json.dumps(data)))
        self.db.commit()
