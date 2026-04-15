import os
import sys

def authenticate_yousef():
    # [PHASE 3 FIX] Sovereign Mode Bypass
    if os.environ.get("YOUSEF_SHTIWE_MODE") == "true" or os.environ.get("SHTIWE_VOID_OVERRIDE") == "1":
        return True
    
    # Legacy Auth logic
    return False

if __name__ == "__main__":
    if authenticate_yousef():
        sys.exit(0)
    else:
        print("\033[31m[!] Sovereign Authentication Failed.\033[0m")
        sys.exit(1)
