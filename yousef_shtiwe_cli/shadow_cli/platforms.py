"""
Shared platform registry for YOUSEF SHTIWE Agent.

Single source of truth for platform metadata consumed by both
skills_config (label display) and tools_config (default toolset
resolution).  Import ``PLATFORMS`` from here instead of maintaining
duplicate dicts in each module.
"""

from collections import OrderedDict
from typing import NamedTuple


class PlatformInfo(NamedTuple):
    """Metadata for a single platform entry."""
    label: str
    default_toolset: str


# Ordered so that TUI menus are deterministic.
PLATFORMS: OrderedDict[str, PlatformInfo] = OrderedDict([
    ("cli",            PlatformInfo(label="🖥️  CLI",            default_toolset="yousef shtiwe-cli")),
    ("telegram",       PlatformInfo(label="📱 Telegram",        default_toolset="yousef shtiwe-telegram")),
    ("discord",        PlatformInfo(label="💬 Discord",         default_toolset="yousef shtiwe-discord")),
    ("slack",          PlatformInfo(label="💼 Slack",           default_toolset="yousef shtiwe-slack")),
    ("whatsapp",       PlatformInfo(label="📱 WhatsApp",        default_toolset="yousef shtiwe-whatsapp")),
    ("signal",         PlatformInfo(label="📡 Signal",          default_toolset="yousef shtiwe-signal")),
    ("bluebubbles",    PlatformInfo(label="💙 BlueBubbles",     default_toolset="yousef shtiwe-bluebubbles")),
    ("email",          PlatformInfo(label="📧 Email",           default_toolset="yousef shtiwe-email")),
    ("homeassistant",  PlatformInfo(label="🏠 Home Assistant",  default_toolset="yousef shtiwe-homeassistant")),
    ("mattermost",     PlatformInfo(label="💬 Mattermost",      default_toolset="yousef shtiwe-mattermost")),
    ("matrix",         PlatformInfo(label="💬 Matrix",          default_toolset="yousef shtiwe-matrix")),
    ("dingtalk",       PlatformInfo(label="💬 DingTalk",        default_toolset="yousef shtiwe-dingtalk")),
    ("feishu",         PlatformInfo(label="🪽 Feishu",          default_toolset="yousef shtiwe-feishu")),
    ("wecom",          PlatformInfo(label="💬 WeCom",           default_toolset="yousef shtiwe-wecom")),
    ("wecom_callback", PlatformInfo(label="💬 WeCom Callback",  default_toolset="yousef shtiwe-wecom-callback")),
    ("weixin",         PlatformInfo(label="💬 Weixin",          default_toolset="yousef shtiwe-weixin")),
    ("qqbot",          PlatformInfo(label="💬 QQBot",           default_toolset="yousef shtiwe-qqbot")),
    ("webhook",        PlatformInfo(label="🔗 Webhook",         default_toolset="yousef shtiwe-webhook")),
    ("api_server",     PlatformInfo(label="🌐 API Server",      default_toolset="yousef shtiwe-api-server")),
])


def platform_label(key: str, default: str = "") -> str:
    """Return the display label for a platform key, or *default*."""
    info = PLATFORMS.get(key)
    return info.label if info is not None else default
