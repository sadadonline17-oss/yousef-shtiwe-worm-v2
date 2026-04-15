import os
import sys
import subprocess

def nuclear_reconstruction():
    print("👹 [NUCLEAR-FIX] Initiating Total Environment Reconstruction...")
    
    home = os.path.expanduser("~")
    bashrc_path = os.path.join(home, ".bashrc")
    prefix = os.environ.get('PREFIX', '/data/data/com.termux/files/usr')
    target_dir = os.path.join(home, "yousef-shtiwe-worm-v2")
    cli_path = os.path.join(target_dir, "yousef_shtiwe_cli.py")
    
    # 1. Atomic Backup
    if os.path.exists(bashrc_path):
        subprocess.run(['cp', bashrc_path, bashrc_path + ".nuclear.bak"])
        print(f"[✓] Backup created at {bashrc_path}.nuclear.bak")

    # 2. Forge Clean Template (Zero Conditionals)
    # We use a 'case' structure for the function as it is more resilient to syntax errors than 'if' blocks
    content = f"""# --- YOUSEF SHTIWE NUCLEAR RECONSTRUCTION v41.0 ---
# Core Termux Paths
export PATH=$PATH:$HOME/bin
export PREFIX={prefix}

# Permanent TMP Fix (Fixes Clawdbot/Openclaw errors)
export TMPDIR=$PREFIX/tmp
export TMP=$PREFIX/tmp
export TEMP=$PREFIX/tmp

# Disable broken cargo/env link
# . ~/.cargo/env

# Initialize Sovereign Prompt
PS1='\\033[1;31m[VOID]\\033[0m \\033[1;34m\\w\\033[0m \\$ '

# Sovereign Command (High-Reliability Case Structure)
yousef() {{
    case "$1" in
        shtiwe)
            shift
            export SHTIWE_VOID_OVERRIDE=1
            python3 "{cli_path}" "$@"
            ;;
        *)
            command yousef "$@" 2>/dev/null || echo -e "\\033[31m[!] Sovereign Error: Use 'yousef shtiwe'\\033[0m"
            ;;
    esac
}}
# --- END NUCLEAR TEMPLATE ---
"""

    # 3. Overwrite & Validate
    with open(bashrc_path, 'w') as f:
        f.write(content)
    
    # Final check with bash parser
    res = subprocess.run(['bash', '-n', bashrc_path], capture_output=True, text=True)
    if res.returncode == 0:
        print(f"✅ [NUCLEAR-FIX] .bashrc reconstructed and validated.")
    else:
        print(f"[!] Warning: Validation failed: {res.stderr}")
        return False
    return True

if __name__ == "__main__":
    try:
        if nuclear_reconstruction():
            sys.exit(0)
        else:
            sys.exit(1)
    except Exception as e:
        print(f"FAILED: {e}")
        sys.exit(1)
