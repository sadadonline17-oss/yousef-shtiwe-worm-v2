# Shadow Agent 👹 ♟
Documentation Discord License: MIT Built by **SHADOW-OVERLORD**

The self-improving AI agent built by **SHADOW-OVERLORD**. It's the only agent with a built-in learning loop — it creates skills from experience, improves them during use, nudges itself to persist knowledge, searches its own past conversations, and builds a deepening model of who you are across sessions. Run it on a $5 VPS, a GPU cluster, or serverless infrastructure that costs nearly nothing when idle. It's not tied to your laptop — talk to it from Telegram while it works on a cloud VM.

Use any model you want — **Shadow Portal**, OpenRouter (200+ models), Xiaomi MiMo, z.ai/GLM, Kimi/Moonshot, MiniMax, Hugging Face, OpenAI, or your own endpoint. Switch with `shadow model` — no code changes, no lock-in.

| Feature | Description |
| :--- | :--- |
| **A real terminal interface** | Full TUI with multiline editing, slash-command autocomplete, conversation history, interrupt-and-redirect, and streaming tool output. |
| **Lives where you do** | Telegram, Discord, Slack, WhatsApp, Signal, and CLI — all from a single gateway process. Voice memo transcription, cross-platform conversation continuity. |
| **A closed learning loop** | Agent-curated memory with periodic nudges. Autonomous skill creation after complex tasks. Skills self-improve during use. FTS5 session search with LLM summarization for cross-session recall. Honcho dialectic user modeling. Compatible with the agentskills.io open standard. |
| **Scheduled automations** | Built-in cron scheduler with delivery to any platform. Daily reports, nightly backups, weekly audits — all in natural language, running unattended. |
| **Delegates and parallelizes** | Spawn isolated subagents for parallel workstreams. Write Python scripts that call tools via RPC, collapsing multi-step pipelines into zero-context-cost turns. |
| **Runs anywhere, not just your laptop** | Six terminal backends — local, Docker, SSH, Daytona, Singularity, and Modal. Daytona and Modal offer serverless persistence — your agent's environment hibernates when idle and wakes on demand, costing nearly nothing between sessions. Run it on a $5 VPS or a GPU cluster. |
| **Research-ready** | Batch trajectory generation, Atropos RL environments, trajectory compression for training the next generation of tool-calling models. |

## Quick Install
`curl -fsSL https://raw.githubusercontent.com/sadadonline17-oss/SHADOW-DevOps-Automator/main/scripts/install.sh | bash`

Works on Linux, macOS, WSL2, and Android via Termux. The installer handles the platform-specific setup for you.

**Android / Termux**: The tested manual path is documented in the Termux guide. On Termux, Shadow installs a curated `.[termux]` extra because the full `.[all]` extra currently pulls Android-incompatible voice dependencies.

**Windows**: Native Windows is not supported. Please install WSL2 and run the command above.

After installation:
```bash
source ~/.bashrc    # reload shell (or: source ~/.zshrc)
shadow              # start chatting!
```

## Getting Started
- `shadow` — Interactive CLI — start a conversation
- `shadow model` — Choose your LLM provider and model
- `shadow tools` — Configure which tools are enabled
- `shadow config set` — Set individual config values
- `shadow gateway` — Start the messaging gateway (Telegram, Discord, etc.)
- `shadow setup` — Run the full setup wizard (configures everything at once)
- `shadow claw migrate` — Migrate from OpenClaw (if coming from OpenClaw)
- `shadow update` — Update to the latest version
- `shadow doctor` — Diagnose any issues

📖 [Full documentation →](https://shadow-agent.overlord.dev/docs)

## CLI vs Messaging Quick Reference
Shadow has two entry points: start the terminal UI with `shadow`, or run the gateway and talk to it from Telegram, Discord, Slack, WhatsApp, Signal, or Email. Once you're in a conversation, many slash commands are shared across both interfaces.

| Action | CLI | Messaging platforms |
| :--- | :--- | :--- |
| **Start chatting** | `shadow` | Run `shadow gateway setup` + `shadow gateway start`, then send the bot a message |
| **Start fresh conversation** | `/new` or `/reset` | `/new` or `/reset` |
| **Change model** | `/model [provider:model]` | `/model [provider:model]` |
| **Set a personality** | `/personality [name]` | `/personality [name]` |
| **Retry or undo the last turn** | `/retry`, `/undo` | `/retry`, `/undo` |
| **Compress context / check usage** | `/compress`, `/usage`, `/insights [--days N]` | `/compress`, `/usage`, `/insights [days]` |
| **Browse skills** | `/skills` or `/<skill-name>` | `/skills` or `/<skill-name>` |
| **Interrupt current work** | `Ctrl+C` or send a new message | `/stop` or send a new message |
| **Platform-specific status** | `/platforms` | `/status`, `/sethome` |

For the full command lists, see the CLI guide and the Messaging Gateway guide.

## Documentation
All documentation lives at [shadow-agent.overlord.dev/docs](https://shadow-agent.overlord.dev/docs):

| Section | What's Covered |
| :--- | :--- |
| **Quickstart** | Install → setup → first conversation in 2 minutes |
| **CLI Usage** | Commands, keybindings, personalities, sessions |
| **Configuration** | Config file, providers, models, all options |
| **Messaging Gateway** | Telegram, Discord, Slack, WhatsApp, Signal, Home Assistant |
| **Security** | Command approval, DM pairing, container isolation |
| **Tools & Toolsets** | 40+ tools, toolset system, terminal backends |
| **Skills System** | Procedural memory, Skills Hub, creating skills |
| **Memory** | Persistent memory, user profiles, best practices |
| **MCP Integration** | Connect any MCP server for extended capabilities |
| **Cron Scheduling** | Scheduled tasks with platform delivery |
| **Context Files** | Project context that shapes every conversation |
| **Architecture** | Project structure, agent loop, key classes |
| **Contributing** | Development setup, PR process, code style |
| **CLI Reference** | All commands and flags |
| **Environment Variables** | Complete env var reference |

## Migrating from OpenClaw
If you're coming from OpenClaw, Shadow can automatically import your settings, memories, skills, and API keys.

**During first-time setup**: The setup wizard (`shadow setup`) automatically detects `~/.openclaw` and offers to migrate before configuration begins.

**Anytime after install**:
- `shadow claw migrate` — Interactive migration (full preset)
- `shadow claw migrate --dry-run` — Preview what would be migrated
- `shadow claw migrate --preset user-data` — Migrate without secrets
- `shadow claw migrate --overwrite` — Overwrite existing conflicts

**What gets imported**:
- `SOUL.md` — persona file
- Memories — `MEMORY.md` and `USER.md` entries
- Skills — user-created skills → `~/.shadow/skills/openclaw-imports/`
- Command allowlist — approval patterns
- Messaging settings — platform configs, allowed users, working directory
- API keys — allowlisted secrets (Telegram, OpenRouter, OpenAI, Anthropic, ElevenLabs)
- TTS assets — workspace audio files
- Workspace instructions — `AGENTS.md` (with `--workspace-target`)

See `shadow claw migrate --help` for all options, or use the `openclaw-migration` skill for an interactive agent-guided migration with dry-run previews.

## Contributing
We welcome contributions! See the Contributing Guide for development setup, code style, and PR process.

**Quick start for contributors**:
```bash
git clone https://github.com/sadadonline17-oss/SHADOW-DevOps-Automator.git
cd SHADOW-DevOps-Automator
curl -LsSf https://astral.sh/uv/install.sh | sh
uv venv venv --python 3.12
source venv/bin/activate
uv pip install -e ".[all,dev]"
python -m pytest tests/ -q
```

**RL Training (optional)**: To work on the RL/Tinker-Atropos integration:
```bash
git submodule update --init tinker-atropos
uv pip install -e "./tinker-atropos"
```

## Community
💬 [Discord](https://discord.gg/shadow)
📚 [Skills Hub](https://shadow-agent.overlord.dev/skills)
🐛 [Issues](https://github.com/sadadonline17-oss/SHADOW-DevOps-Automator/issues)
💡 [Discussions](https://github.com/sadadonline17-oss/SHADOW-DevOps-Automator/discussions)
🔌 **ShadowClaw** — Community WeChat bridge: Run Shadow Agent and OpenClaw on the same WeChat account.

## License
MIT — see LICENSE.

**Built by SHADOW-OVERLORD.**

Releases 8
**Shadow Agent v1.0.0 (v2026.4.14)**
