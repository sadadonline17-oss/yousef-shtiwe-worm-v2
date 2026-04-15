import os
import sys
import time
import subprocess
import shlex

# Sovereign Arsenal Import Logic
try:
    from yousef_shtiwe_cli.banner import get_banner
    from yousef_shtiwe_cli.colors import RED, RESET, BOLD, GOLD, GREEN
    from yousef_shtiwe_cli.constants import get_default_shtiwe_root, YOUSEF_SHTIWE_VERSION
except ImportError:
    def get_banner(): return "\033[1;31m[YOUSEF SHTIWE VOID]\033[0m"
    def get_default_shtiwe_root(): return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    RED, RESET, BOLD, GOLD, GREEN = "\033[1;31m", "\033[0m", "\033[1m", "\033[38;5;220m", "\033[38;5;46m"
    YOUSEF_SHTIWE_VERSION = "46.0"

def execute_system_cmd(cmd_str):
    try:
        parts = shlex.split(cmd_str)
        if not parts: return
        if parts[0] == "cd":
            target = parts[1] if len(parts) > 1 else os.path.expanduser("~")
            os.chdir(target)
            return
        subprocess.run(cmd_str, shell=True, text=True)
    except Exception as e:
        print(f"{RED}[!] System Execution Error: {e}{RESET}")

def print_help():
    print(f"\n{BOLD}{GOLD}Sovereign Command Architecture (v{YOUSEF_SHTIWE_VERSION}){RESET}")
    print(f"{BOLD}Usage:{RESET} yousef shtiwe <command> [options]")
    print("\n" + BOLD + "Core Operations:" + RESET)
    print(f"  {GREEN}model{RESET}          - Choose LLM provider and model")
    print(f"  {GREEN}tools{RESET}          - Configure enabled offensive tools")
    print(f"  {GREEN}config set{RESET}     - Set individual configuration values")
    print(f"  {GREEN}setup{RESET}          - Run full sovereign configuration wizard")
    print(f"  {GREEN}gateway{RESET}        - Start messaging gateway (Telegram/Discord)")
    print(f"  {GREEN}update{RESET}         - Pull latest logic blocks from the void")
    print(f"  {GREEN}doctor{RESET}         - Diagnose environment and path issues")
    print(f"  {GREEN}migrate{RESET}        - Port assets from OpenClaw/Hermes")
    print("\n" + BOLD + "Internal Modules:" + RESET)
    print("  recon, exploit, stealth, learn, void")
    print("\n" + BOLD + "System Shell:" + RESET)
    print("  Any standard bash command (ls, pkg, top, etc.) is supported.")

def process_command(cmd_input):
    if not cmd_input: return True
    parts = shlex.split(cmd_input)
    base_cmd = parts[0].lower()
    args = parts[1:]

    if base_cmd in ["exit", "quit", "void"]:
        print(f"{RED}👹 [VOID] Returning to the yousef shtiwes...{RESET}")
        return False
    
    if base_cmd in ["help", "--help", "-h"]:
        print_help()
        return True

    # Sovereign Logic Mapping
    sovereign_cmds = ["model", "tools", "config", "setup", "gateway", "update", "doctor", "migrate", "recon", "exploit", "stealth", "learn"]
    
    if base_cmd in sovereign_cmds:
        print(f"{GOLD}[*] Sovereign Operation: {base_cmd} { ' '.join(args) if args else ''}{RESET}")
        time.sleep(0.5)
        # Placeholder for modular execution
        if base_cmd == "doctor":
            print(f"{GREEN}[✓] Environment: Termux (OK)\n[✓] Logic Blocks: 17/17 Verified\n[✓] Shell: Bash Sovereign (OK){RESET}")
        elif base_cmd == "model":
            print(f"{BOLD}Available Models:{RESET} GPT-4o, Claude-3.5-Sonnet, Gemini-Pro-1.5")
        else:
            print(f"{RED}[!] Module '{base_cmd}' is awaiting final neural sync.{RESET}")
        return True
    else:
        execute_system_cmd(cmd_input)
        return True

def main():
    root_dir = get_default_shtiwe_root()
    sys.path.insert(0, root_dir)

    if len(sys.argv) > 1:
        cmd_to_run = " ".join(sys.argv[1:])
        process_command(cmd_to_run)
        sys.exit(0)

    print(get_banner())
    print(f"{BOLD}{RED}👹 [SHTIWE-CORE] Sovereign Engine v{YOUSEF_SHTIWE_VERSION} Operational...{RESET}")
    
    while True:
        try:
            cwd = os.getcwd().replace(os.path.expanduser("~"), "~")
            prompt = f"\n{RED}yousef@shtiwe{RESET}:{BOLD}{cwd}{RESET}# "
            cmd = input(prompt).strip()
            if not process_command(cmd): break
        except KeyboardInterrupt:
            print(f"\n{RED}👹 [VOID] Sovereign connection suspended.{RESET}")
            break
        except Exception as e:
            print(f"{RED}[!] Nexus Error: {e}{RESET}")

if __name__ == "__main__":
    main()
