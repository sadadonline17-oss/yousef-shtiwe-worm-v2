#!/bin/bash
{
    set -e
    export LANG=en_US.UTF-8

    echo -e "\033[38;5;220m"
    echo "╔══════════════════════════════════════════════════════════════════════╗"
    echo "║   YOUSEF SHTIWE - SOVEREIGN INSTALLER v48.0 (TERMUX CORE)     ║"
    echo "╚══════════════════════════════════════════════════════════════════════╝"
    echo -e "\033[0m"

    if [ -d "/data/data/com.termux" ] || [ -n "$TERMUX_VERSION" ]; then
        IS_TERMUX=true
        PREFIX="/data/data/com.termux/files/usr"
        HOME_DIR="/data/data/com.termux/files/home"
    else
        IS_TERMUX=false
        PREFIX="/usr/local"
        HOME_DIR="$HOME"
    fi

    TARGET_DIR="$HOME_DIR/yousef-shtiwe-worm-v2"
    mkdir -p "$TARGET_DIR"
    cd "$TARGET_DIR"

    # Dependency check for Termux
    if [ "$IS_TERMUX" = true ]; then
        echo "[⚙️] Termux Environment Detected. Synchronizing Packages..."
        pkg update -y || true
        pkg install python nmap curl unzip git openssl make clang -y || true
        # [PHASE 2 FIX] Commented pip upgrade as requested
        # python3 -m pip install --upgrade pip --break-system-packages --quiet || true
    fi

    install_sqlmap_termux() {
        echo "[→] Installing sqlmap via git clone..."
        rm -rf "$PREFIX/opt/sqlmap"
        git clone --depth=1 https://github.com/sqlmapproject/sqlmap.git "$PREFIX/opt/sqlmap"
        ln -sf "$PREFIX/opt/sqlmap/sqlmap.py" "$PREFIX/bin/sqlmap"
    }

    install_masscan_termux() {
        echo "[→] Installing masscan from source..."
        rm -rf "$PREFIX/opt/masscan"
        git clone https://github.com/robertdavidgraham/masscan.git "$PREFIX/opt/masscan"
        cd "$PREFIX/opt/masscan" && make -j4
        ln -sf "$PREFIX/opt/masscan/bin/masscan" "$PREFIX/bin/masscan"
        cd "$TARGET_DIR"
    }

    if [ "$IS_TERMUX" = true ]; then
        install_sqlmap_termux
        install_masscan_termux
    fi

    # 1. ATOMIC SYNC
    echo "[⚡] Fetching Sovereign Logic Components..."
    # We use a python script to pull individual files if git fails on slow connections
    curl -fsSL "https://raw.githubusercontent.com/sadadonline17-oss/yousef-shtiwe-worm-v2/main/scripts/void_sync.py" -o void_sync.py
    python3 void_sync.py
    rm void_sync.py

    # 2. INSTALL PYTHON DEPENDENCIES
    echo "[📦] Installing Sovereign Python Modules..."
    python3 -m pip install -r requirements.txt --break-system-packages --quiet || true

    # 3. SHELL SOVEREIGNTY
    echo "[⚓] Finalizing Shell Integration..."
    BASHRC="$HOME_DIR/.bashrc"
    [ -f "$HOME_DIR/.zshrc" ] && BASHRC="$HOME_DIR/.zshrc"

    # Atomic Injection of Alias and function
    if ! grep -q "yousef shtiwe" "$BASHRC"; then
        echo "alias \"yousef shtiwe\"=\"python3 $TARGET_DIR/yousef_shtiwe_cli.py\"" >> "$BASHRC"
    fi

    echo -e "\033[38;5;46m"
    echo "✅ [YOUSEF SHTIWE] SYSTEM TRANSFORMATION COMPLETE (V48.0)."
    echo "✅ [SUCCESS] sqlmap & masscan installed from source."
    echo "✅ [SUCCESS] Sovereign Alias 'yousef shtiwe' injected."
    echo "🚀 ACTION: Run 'source $BASHRC' then 'yousef shtiwe offensive recon <target>'"
    echo -e "\033[0m"
}
