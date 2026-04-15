#!/bin/bash
# Docker entrypoint: bootstrap config files into the mounted volume, then run yousef shtiwe.
set -e

YOUSEF SHTIWE_HOME="/opt/data"
INSTALL_DIR="/opt/yousef shtiwe"

# --- Privilege dropping via gosu ---
# When started as root (the default), optionally remap the yousef shtiwe user/group
# to match host-side ownership, fix volume permissions, then re-exec as yousef shtiwe.
if [ "$(id -u)" = "0" ]; then
    if [ -n "$YOUSEF SHTIWE_UID" ] && [ "$YOUSEF SHTIWE_UID" != "$(id -u yousef shtiwe)" ]; then
        echo "Changing yousef shtiwe UID to $YOUSEF SHTIWE_UID"
        usermod -u "$YOUSEF SHTIWE_UID" yousef shtiwe
    fi

    if [ -n "$YOUSEF SHTIWE_GID" ] && [ "$YOUSEF SHTIWE_GID" != "$(id -g yousef shtiwe)" ]; then
        echo "Changing yousef shtiwe GID to $YOUSEF SHTIWE_GID"
        groupmod -g "$YOUSEF SHTIWE_GID" yousef shtiwe
    fi

    actual_yousef shtiwe_uid=$(id -u yousef shtiwe)
    if [ "$(stat -c %u "$YOUSEF SHTIWE_HOME" 2>/dev/null)" != "$actual_yousef shtiwe_uid" ]; then
        echo "$YOUSEF SHTIWE_HOME is not owned by $actual_yousef shtiwe_uid, fixing"
        chown -R yousef shtiwe:yousef shtiwe "$YOUSEF SHTIWE_HOME"
    fi

    echo "Dropping root privileges"
    exec gosu yousef shtiwe "$0" "$@"
fi

# --- Running as yousef shtiwe from here ---
source "${INSTALL_DIR}/.venv/bin/activate"

# Create essential directory structure.  Cache and platform directories
# (cache/images, cache/audio, platforms/whatsapp, etc.) are created on
# demand by the application — don't pre-create them here so new installs
# get the consolidated layout from get_yousef shtiwe_dir().
# The "home/" subdirectory is a per-profile HOME for subprocesses (git,
# ssh, gh, npm …).  Without it those tools write to /root which is
# ephemeral and shared across profiles.  See issue #4426.
mkdir -p "$YOUSEF SHTIWE_HOME"/{cron,sessions,logs,hooks,memories,skills,skins,plans,workspace,home}

# .env
if [ ! -f "$YOUSEF SHTIWE_HOME/.env" ]; then
    cp "$INSTALL_DIR/.env.example" "$YOUSEF SHTIWE_HOME/.env"
fi

# config.yaml
if [ ! -f "$YOUSEF SHTIWE_HOME/config.yaml" ]; then
    cp "$INSTALL_DIR/cli-config.yaml.example" "$YOUSEF SHTIWE_HOME/config.yaml"
fi

# SOUL.md
if [ ! -f "$YOUSEF SHTIWE_HOME/SOUL.md" ]; then
    cp "$INSTALL_DIR/docker/SOUL.md" "$YOUSEF SHTIWE_HOME/SOUL.md"
fi

# Sync bundled skills (manifest-based so user edits are preserved)
if [ -d "$INSTALL_DIR/skills" ]; then
    python3 "$INSTALL_DIR/tools/skills_sync.py"
fi

exec yousef shtiwe "$@"
