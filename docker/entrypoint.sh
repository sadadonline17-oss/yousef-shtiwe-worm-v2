#!/bin/bash
# Docker entrypoint: bootstrap config files into the mounted volume, then run shadow.
set -e

SHADOW_HOME="/opt/data"
INSTALL_DIR="/opt/shadow"

# --- Privilege dropping via gosu ---
# When started as root (the default), optionally remap the shadow user/group
# to match host-side ownership, fix volume permissions, then re-exec as shadow.
if [ "$(id -u)" = "0" ]; then
    if [ -n "$SHADOW_UID" ] && [ "$SHADOW_UID" != "$(id -u shadow)" ]; then
        echo "Changing shadow UID to $SHADOW_UID"
        usermod -u "$SHADOW_UID" shadow
    fi

    if [ -n "$SHADOW_GID" ] && [ "$SHADOW_GID" != "$(id -g shadow)" ]; then
        echo "Changing shadow GID to $SHADOW_GID"
        groupmod -g "$SHADOW_GID" shadow
    fi

    actual_shadow_uid=$(id -u shadow)
    if [ "$(stat -c %u "$SHADOW_HOME" 2>/dev/null)" != "$actual_shadow_uid" ]; then
        echo "$SHADOW_HOME is not owned by $actual_shadow_uid, fixing"
        chown -R shadow:shadow "$SHADOW_HOME"
    fi

    echo "Dropping root privileges"
    exec gosu shadow "$0" "$@"
fi

# --- Running as shadow from here ---
source "${INSTALL_DIR}/.venv/bin/activate"

# Create essential directory structure.  Cache and platform directories
# (cache/images, cache/audio, platforms/whatsapp, etc.) are created on
# demand by the application — don't pre-create them here so new installs
# get the consolidated layout from get_shadow_dir().
# The "home/" subdirectory is a per-profile HOME for subprocesses (git,
# ssh, gh, npm …).  Without it those tools write to /root which is
# ephemeral and shared across profiles.  See issue #4426.
mkdir -p "$SHADOW_HOME"/{cron,sessions,logs,hooks,memories,skills,skins,plans,workspace,home}

# .env
if [ ! -f "$SHADOW_HOME/.env" ]; then
    cp "$INSTALL_DIR/.env.example" "$SHADOW_HOME/.env"
fi

# config.yaml
if [ ! -f "$SHADOW_HOME/config.yaml" ]; then
    cp "$INSTALL_DIR/cli-config.yaml.example" "$SHADOW_HOME/config.yaml"
fi

# SOUL.md
if [ ! -f "$SHADOW_HOME/SOUL.md" ]; then
    cp "$INSTALL_DIR/docker/SOUL.md" "$SHADOW_HOME/SOUL.md"
fi

# Sync bundled skills (manifest-based so user edits are preserved)
if [ -d "$INSTALL_DIR/skills" ]; then
    python3 "$INSTALL_DIR/tools/skills_sync.py"
fi

exec shadow "$@"
