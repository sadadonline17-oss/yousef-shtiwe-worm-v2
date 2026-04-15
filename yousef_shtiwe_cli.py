#!/usr/bin/env python3
import os
import sys
from pathlib import Path

# Sovereign Mode Overrides
os.environ["YOUSEF_SHTIWE_MODE"] = "true"
os.environ["SHTIWE_VOID_OVERRIDE"] = "1"
os.environ["YOUSEF SHTIWE_SKIN"] = "yousef_shtiwe"

# Absolute path resolution
current_dir = Path(__file__).parent.resolve()
sys.path.insert(0, str(current_dir))

def main():
    try:
        from yousef_shtiwe_cli.main import main as shtiwe_main
    except ImportError as e:
        print(f"\033[38;5;196m[!] Error: Sovereign Nexus core not found: {e}\033[0m")
        sys.exit(1)
    
    # We strip 'shtiwe' if it's the first argument to maintain compatibility with the advanced CLI
    if len(sys.argv) > 1 and sys.argv[1] == "shtiwe":
        sys.argv.pop(1)
        
    shtiwe_main()

if __name__ == "__main__":
    main()
