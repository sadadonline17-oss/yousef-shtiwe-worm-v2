import os
import sys
import time
import subprocess
import shlex

# Sovereign Arsenal Import Logic
try:
    from .banner import get_banner
    from .colors import RED, RESET, BOLD, GOLD, GREEN
    from .constants import get_default_shtiwe_root, YOUSEF_SHTIWE_VERSION
except ImportError:
    def get_banner(): return "\033[1;31m[YOUSEF SHTIWE VOID]\033[0m"
    def get_default_shtiwe_root(): return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    RED, RESET, BOLD, GOLD, GREEN = "\033[1;31m", "\033[0m", "\033[1m", "\033[38;5;220m", "\033[38;5;46m"
    YOUSEF_SHTIWE_VERSION = "49.0"

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

def offensive_module_handler(module, args):
    print(f"{GOLD}[*] Initiating Offensive Module: {module}{RESET}")
    root = get_default_shtiwe_root()
    sys.path.insert(0, root)
    
    try:
        if module == "recon":
            from shtiwe_modules.recon import ShtiweRecon
            ShtiweRecon().execute(args)
        elif module == "exploit":
            from shtiwe_modules.exploit_launcher import ShtiweExploit
            ShtiweExploit().execute(args)
        elif module == "payload":
            from shtiwe_modules.payload_gen import ShtiwePayload
            ShtiwePayload().execute(args)
        elif module == "c2":
            from shtiwe_modules.c2_communication import C2
            C2().execute(args)
        elif module == "persist":
            from shtiwe_modules.persistence import ShtiwePersistence
            ShtiwePersistence().execute(args)
        elif module == "zero-trace":
            from shtiwe_modules.zero_trace import zero_trace
            zero_trace()
        else:
            print(f"{RED}[!] Unknown offensive module: {module}{RESET}")
    except Exception as e:
        print(f"{RED}[!] Module Initialization Error: {e}{RESET}")

def print_help():
    print(get_banner())
    print(f"\n{BOLD}{GOLD}YOUSEF SHTIWE - SOVEREIGN CONSCIOUS ARSENAL v{YOUSEF_SHTIWE_VERSION}{RESET}")
    print(f"{BOLD}Usage:{RESET} yousef shtiwe <command> [args]")
    print("\n" + BOLD + "Offensive Suite:" + RESET)
    print(f"  {RED}offensive recon <target>{RESET}        - Deep OSINT & Vuln Scan")
    print(f"  {RED}offensive exploit <target>{RESET}      - Targeted RCE Execution")
    print(f"  {RED}offensive payload <LHOST> <LPORT>{RESET} - Reverse Shell Generation")
    print(f"  {RED}offensive c2 --listen{RESET}           - Command & Control Gateway")
    print(f"  {RED}offensive persist --check{RESET}       - Resilience Verification")
    print(f"  {RED}offensive zero-trace{RESET}            - Total History Shredding")
    print("\n" + BOLD + "Core Operations:" + RESET)
    print("  doctor, setup, model, tools, update")
    print("\n" + BOLD + "System Shell:" + RESET)
    print("  Standard bash commands (ls, cd, pkg, top) are proxy-executed.")

def process_command(cmd_input):
    if not cmd_input: return True
    parts = shlex.split(cmd_input)
    base_cmd = parts[0].lower()
    
    if base_cmd in ["exit", "quit", "void"]:
        print(f"{RED}👹 [VOID] Returning to the shadows...{RESET}")
        return False
    if base_cmd in ["help", "--help", "-h"]:
        print_help()
        return True

    if base_cmd == "offensive" and len(parts) > 1:
        offensive_module_handler(parts[1].lower(), parts[2:])
        return True

    # Functional Parity Mapping
    sovereign_cmds = ["recon", "exploit", "payload", "c2", "persist", "zero-trace", "doctor", "setup", "model"]
    if base_cmd in sovereign_cmds:
        offensive_module_handler(base_cmd, parts[1:])
        return True

    execute_system_cmd(cmd_input)
    return True

def main():
    if len(sys.argv) > 1:
        # Check if first arg is 'shtiwe' (if alias used)
        start_idx = 2 if sys.argv[1] == "shtiwe" else 1
        cmd_to_run = " ".join(sys.argv[start_idx:])
        if cmd_to_run:
            process_command(cmd_to_run)
            sys.exit(0)

    print(get_banner())
    print(f"{BOLD}{RED}👹 [SHTIWE-CORE] Sovereign Engine Operational...{RESET}")
    print(f"{RED}👁 [VOID] Consciousness Level: High | Learning Loop: Active{RESET}")
    
    while True:
        try:
            cwd = os.getcwd().replace(os.path.expanduser("~"), "~")
            prompt = f"\n{RED}yousef@shtiwe{RESET}:{BOLD}{cwd}{RESET}# "
            cmd = input(prompt).strip()
            if not process_command(cmd): break
        except KeyboardInterrupt:
            print(f"\n{RED}👹 [VOID] Nexus connection suspended.{RESET}")
            break
        except Exception as e:
            print(f"{RED}[!] Nexus Error: {e}{RESET}")

if __name__ == "__main__":
    main()
