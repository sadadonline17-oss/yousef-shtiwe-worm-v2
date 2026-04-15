#!/bin/bash
{
    set -e
    export LANG=en_US.UTF-8

    echo -e "\033[38;5;220m"
    echo "╔══════════════════════════════════════════════════════════════════════╗"
    echo "║   YOUSEF SHTIWE - VOID INSTALLER v47.0 (ATOMIC NEXUS)          ║"
    echo "╚══════════════════════════════════════════════════════════════════════╝"
    echo -e "\033[0m"

    echo "👹 [VOID-CORE] Initiating Sovereign Core Integration..."

    if [ -d "/data/data/com.termux" ] || [ -n "$TERMUX_VERSION" ]; then
        TARGET_DIR="$HOME/yousef-shtiwe-worm-v2"
        IS_TERMUX=true
    else
        TARGET_DIR="$(pwd)/yousef-shtiwe-worm-v2"
        IS_TERMUX=false
    fi

    mkdir -p "$TARGET_DIR"
    cd "$TARGET_DIR"

    # Dependency check
    if [ "$IS_TERMUX" = true ]; then
        pkg update -y || true
        pkg install python nmap curl unzip git openssl -y || true
        python3 -m pip install --upgrade pip --break-system-packages --quiet || true
    fi

    # 1. ATOMIC CLONE & SYNC
    echo "[⚙️] Fetching Advanced Autonomous Logic (Shadow v1.0.0)..."
    if [ ! -d ".git" ]; then
        git clone https://github.com/sadadonline17-oss/yousef-shtiwe-worm-v2.git .
    else
        git pull origin main --force
    fi

    # 2. INSTALL DEPENDENCIES
    echo "[📦] Installing Sovereign Dependencies..."
    python3 -m pip install -r requirements.txt --break-system-packages --quiet || true

    # 3. RADICAL SHELL RECONSTRUCTION
    echo "[⚓] Executing Sovereign Shell Patching..."
    export CLI_PATH="$TARGET_DIR/yousef_shtiwe_cli.py"
    chmod +x "$CLI_PATH"
    
    # We use a special 'yousef' function to handle commands and interactive mode
    BASHRC="$HOME/.bashrc"
    [ -f "$HOME/.zshrc" ] && BASHRC="$HOME/.zshrc"

    # Injecting the permanent alias and function
    cat << EOF > scripts/heal_rc.py
import os
def heal():
    home = os.path.expanduser("~")
    bashrc = os.path.join(home, ".bashrc")
    prefix = os.environ.get('PREFIX', '/data/data/com.termux/files/usr')
    cli = os.path.join(home, "yousef-shtiwe-worm-v2", "yousef_shtiwe_cli.py")
    
    with open(bashrc, 'r') as f: lines = f.readlines()
    
    clean = []
    for line in lines:
        if any(x in line for x in ["yousef", "shtiwe", "shadow", "VOID CORE"]): continue
        clean.append(line)
        
    logic = f"""
# --- YOUSEF SHTIWE VOID CORE v47.0 ---
export TMPDIR="{prefix}/tmp"
yousef() {{
    if [ "$1" = "shtiwe" ]; then
        shift
        export SHTIWE_VOID_OVERRIDE=1
        python3 "{cli}" "$@"
    else
        command yousef "$@" 2>/dev/null || echo -e "\\033[31m[!] Use: yousef shtiwe\\033[0m"
    fi
}}
# --- END VOID CORE ---
"""
    with open(bashrc, 'w') as f: f.write("".join(clean) + logic)
    print("✅ Shell Healed.")

if __name__ == "__main__": heal()
EOF
    python3 scripts/heal_rc.py
    rm scripts/heal_rc.py

    echo -e "\033[38;5;46m"
    echo "✅ [YOUSEF SHTIWE] SYSTEM FULLY INTEGRATED (V47.0)."
    echo "✅ [SUCCESS] Advanced Shadow v1.0.0 logic merged with Sovereign Identity."
    echo "🚀 ACTION: Run 'source ~/.bashrc' then 'yousef shtiwe doctor'"
    echo -e "\033[0m"
}
