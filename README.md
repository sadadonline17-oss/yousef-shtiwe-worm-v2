Shadow Agent 👹 ♟
**Documentation** | **Discord** | **License: MIT** | **Built by SHADOW-OVERLORD**

The self-improving AI agent built by **SHADOW-OVERLORD**. It's the only agent with a built-in learning loop — it creates skills from experience, improves them during use, nudges itself to persist knowledge, searches its own past conversations, and builds a deepening model of who you are across sessions. Run it on a $5 VPS, a GPU cluster, or serverless infrastructure that costs nearly nothing when idle. It's not tied to your laptop — talk to it from Telegram while it works on a cloud VM.

Use any model you want — Shadow Portal, OpenRouter (200+ models), Xiaomi MiMo, z.ai/GLM, Kimi/Moonshot, MiniMax, Hugging Face, OpenAI, or your own endpoint. Switch with `shadow model` — no code changes, no lock-in.

| **Feature** | **Description** |
| :--- | :--- |
| **A real terminal interface** | Full TUI with multiline editing, slash-command autocomplete, conversation history, interrupt-and-redirect, and streaming tool output. |
| **Lives where you do** | Telegram, Discord, Slack, WhatsApp, Signal, and CLI — all from a single gateway process. Voice memo transcription, cross-platform conversation continuity. |
| **A closed learning loop** | Agent-curated memory with periodic nudges. Autonomous skill creation after complex tasks. Skills self-improve during use. FTS5 session search with LLM summarization for cross-session recall. Honcho dialectic user modeling. Compatible with the agentskills.io open standard. |
| **Scheduled automations** | Built-in cron scheduler with delivery to any platform. Daily reports, nightly backups, weekly audits — all in natural language, running unattended. |
| **Delegates and parallelizes** | Spawn isolated subagents for parallel workstreams. Write Python scripts that call tools via RPC, collapsing multi-step pipelines into zero-context-cost turns. |
| **Runs anywhere** | Six terminal backends — local, Docker, SSH, Daytona, Singularity, and Modal. Daytona and Modal offer serverless persistence — your agent's environment hibernates when idle and wakes on demand. |
| **Research-ready** | Batch trajectory generation, Atropos RL environments, trajectory compression for training the next generation of tool-calling models. |

## Quick Install
```bash
curl -fsSL https://raw.githubusercontent.com/sadadonline17-oss/SHADOW-DevOps-Automator/main/scripts/install.sh | bash
```
Works on Linux, macOS, WSL2, and Android via Termux. The installer handles the platform-specific setup for you.

**Android / Termux**: The tested manual path is documented in the Termux guide. On Termux, Shadow installs a curated `.[termux]` extra because the full `.[all]` extra currently pulls Android-incompatible voice dependencies.

**Windows**: Native Windows is not supported. Please install WSL2 and run the command above.

After installation:
```bash
source ~/.bashrc    # reload shell (or: source ~/.zshrc)
shadow              # start chatting!
```

## Getting Started
- `shadow chat` — Interactive CLI — start a conversation
- `shadow model` — Choose your LLM provider and model
- `shadow tools` — Configure which tools are enabled
- `shadow config set` — Set individual config values
- `shadow gateway` — Start the messaging gateway (Telegram, Discord, etc.)
- `shadow setup` — Run the full setup wizard (configures everything at once)
- `shadow update` — Update to the latest version
- `shadow doctor` — Diagnose any issues

📖 **Full documentation** → [shadow-agent.overlord.com/docs](https://shadow-agent.overlord.com/docs)

## CLI vs Messaging Quick Reference
Shadow has two entry points: start the terminal UI with `shadow chat`, or run the gateway and talk to it from Telegram, Discord, Slack, WhatsApp, Signal, or Email. Once you're in a conversation, many slash commands are shared across both interfaces.

| **Action** | **CLI** | **Messaging Platforms** |
| :--- | :--- | :--- |
| **Start chatting** | `shadow chat` | Run `shadow gateway setup` + `shadow gateway start`, then send the bot a message |
| **Start fresh conversation** | `/new` or `/reset` | `/new` or `/reset` |
| **Change model** | `/model [provider:model]` | `/model [provider:model]` |
| **Set a personality** | `/personality [name]` | `/personality [name]` |
| **Retry or undo last turn** | `/retry`, `/undo` | `/retry`, `/undo` |
| **Compress context** | `/compress`, `/usage` | `/compress`, `/usage` |
| **Browse skills** | `/skills` or `/<skill-name>` | `/skills` or `/<skill-name>` |
| **Interrupt work** | `Ctrl+C` or send message | `/stop` or send message |
| **Platform status** | `/platforms` | `/status`, `/sethome` |

## Documentation
All documentation lives at [shadow-agent.overlord.com/docs](https://shadow-agent.overlord.com/docs):

| **Section** | **What's Covered** |
| :--- | :--- |
| **Quickstart** | Install → setup → first conversation in 2 minutes |
| **CLI Usage** | Commands, keybindings, personalities, sessions |
| **Configuration** | Config file, providers, models, all options |
| **Messaging Gateway** | Telegram, Discord, Slack, WhatsApp, Signal, Home Assistant |
| **Security** | Command approval, DM pairing, container isolation |
| **Tools & Toolsets** | 40+ tools, toolset system, terminal backends |
| **Skills System** | Procedural memory, Skills Hub, creating skills |
| **Memory** | Persistent memory, user profiles, best practices |
| **Cron Scheduling** | Scheduled tasks with platform delivery |
| **Architecture** | Project structure, agent loop, key classes |
| **Contributing** | Development setup, PR process, code style |

## Contributing
We welcome contributions! See the Contributing Guide for development setup, code style, and PR process.

Quick start for contributors:
```bash
git clone https://github.com/sadadonline17-oss/SHADOW-DevOps-Automator.git
cd SHADOW-DevOps-Automator
curl -LsSf https://astral.sh/uv/install.sh | sh
uv venv venv --python 3.12
source venv/bin/activate
uv pip install -e ".[all,dev]"
python -m pytest tests/ -q
```

## Community
💬 **Discord**
📚 **Skills Hub**
🐛 **Issues**
💡 **Discussions**

## License
MIT — see LICENSE.

**Built by SHADOW-OVERLORD.**
**Shadow Agent v1.0.0 (v2026.4.14)**
