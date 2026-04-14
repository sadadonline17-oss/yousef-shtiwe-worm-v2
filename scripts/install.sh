#!/bin/bash
set -e

echo "👹 [SHADOW-INSTALLER] Initializing Void Protocol..."

# Identify the OS
OS="$(uname)"
case "${OS}" in
    Linux*)     PLATFORM=Linux;;
    Darwin*)    PLATFORM=Mac;;
    *)          PLATFORM="UNKNOWN:${OS}"
esac

echo "📡 [SHADOW-INSTALLER] Detected Platform: ${PLATFORM}"

# Install uv if not present
if ! command -v uv &> /dev/null; then
    echo "📦 [SHADOW-INSTALLER] Installing 'uv' (Fast Python package manager)..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    source $HOME/.cargo/env
fi

# Create virtual environment
echo "🐍 [SHADOW-INSTALLER] Creating Supreme Virtual Environment..."
uv venv .venv --python 3.12
source .venv/bin/activate

# Install dependencies
echo "🛠️ [SHADOW-INSTALLER] Injecting Dependencies..."
uv pip install -e ".[all]"

# Setup the 'shadow' command globally
echo "🔗 [SHADOW-INSTALLER] Linking 'shadow' to your path..."
SHADOW_BIN_PATH="$(pwd)/shadow"
chmod +x "$SHADOW_BIN_PATH"

# Add to shell profile
BASH_PROFILE="$HOME/.bashrc"
ZSH_PROFILE="$HOME/.zshrc"

if [ -f "$BASH_PROFILE" ]; then
    if ! grep -q "alias shadow=" "$BASH_PROFILE"; then
        echo "alias shadow='$SHADOW_BIN_PATH'" >> "$BASH_PROFILE"
    fi
fi

if [ -f "$ZSH_PROFILE" ]; then
    if ! grep -q "alias shadow=" "$ZSH_PROFILE"; then
        echo "alias shadow='$SHADOW_BIN_PATH'" >> "$ZSH_PROFILE"
    fi
fi

echo "✅ [SHADOW-INSTALLER] Installation Complete."
echo "👹 Type 'source ~/.bashrc' and then 'shadow' to enter the Void."
