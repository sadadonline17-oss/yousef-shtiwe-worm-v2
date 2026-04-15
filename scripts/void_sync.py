import os
import requests
import time

BASE = 'https://raw.githubusercontent.com/sadadonline17-oss/yousef-shtiwe-worm-v2/main/'
FILES = [
    'yousef_shtiwe_cli.py', 'auth_yousef.py', 'pyproject.toml', 'SOUL.md', 'VERSION', 'requirements.txt',
    'yousef_shtiwe_cli/banner.py', 'yousef_shtiwe_cli/colors.py', 'yousef_shtiwe_cli/main.py', 'yousef_shtiwe_cli/constants.py', 
    'agent/worm_learning.py', 'shtiwe_modules/recon.py', 'shtiwe_modules/exploit_launcher.py', 'shtiwe_modules/zero_trace.py',
    'agentic/prompts/base.py', 'agentic/prompts/__init__.py', 'scripts/radical_fix.py'
]

def sync_file(f):
    print(f"  [⚡] Syncing: {f}...", end="\r")
    for attempt in range(5):
        try:
            r = requests.get(BASE + f, timeout=20)
            if r.status_code == 200:
                os.makedirs(os.path.dirname(f), exist_ok=True) if os.path.dirname(f) else None
                with open(f, 'wb') as out: out.write(r.content)
                return True
        except:
            time.sleep(2)
    return False

print("👹 [VOID-SYNC] Syncing logic blocks...")
success = 0
for f in FILES:
    if sync_file(f): success += 1
print(f"\n[✓] Atomic Sync Complete ({success}/{len(FILES)} blocks).")
