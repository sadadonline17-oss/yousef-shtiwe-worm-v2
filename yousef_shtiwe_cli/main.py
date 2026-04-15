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
    # Minimal Fallback
    def get_banner(): return "\033[1;31m[YOUSEF SHTIWE VOID]\033[0m"
    def get_default_shtiwe_root(): return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    RED, RESET, BOLD, GOLD, GREEN = "\033[1;31m", "\033[0m", "\033[1m", "\033[38;5;220m", "\033[38;5;46m"
    YOUSEF_SHTIWE_VERSION = "48.0"

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
    if args: print(f"{GOLD}[*] Parameters: {' '.join(args)}{RESET}")
    
    # Placeholder for actual module logic from shtiwe_modules/
    try:
        # Import dynamically to prevent circular dependencies
        sys.path.insert(0, get_default_shtiwe_root())
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
    except Exception as e:
        print(f"{RED}[!] Module Error: {e}{RESET}")

def print_help():
    print(get_banner())
    print(f"\n{BOLD}{GOLD}YOUSEF SHTIWE - OFFENSIVE ARSENAL v{YOUSEF_SHTIWE_VERSION}{RESET}")
    print(f"{BOLD}Usage:{RESET} yousef shtiwe <command> [args]")
    print("\n" + BOLD + "Offensive Suite:" + RESET)
    print(f"  {RED}offensive recon <target>{RESET}        - Deep OSINT & Vuln Scan")
    print(f"  {RED}offensive exploit <target>{RESET}      - RCE & Lateral Movement")
    print(f"  {RED}offensive payload <IP> <PORT>{RESET}   - Reverse Shell Gen")
    print(f"  {RED}offensive c2 --listen{RESET}           - Command & Control")
    print(f"  {RED}offensive persist --check{RESET}       - Resilience Check")
    print(f"  {RED}offensive zero-trace{RESET}            - Anti-Forensic Scrub")
    print("\n" + BOLD + "Core Operations:" + RESET)
    print("  doctor, setup, model, tools, update")
    print("\n" + BOLD + "System Shell:" + RESET)
    print("  Standard bash commands (ls, cd, curl, etc.) are supported.")

def process_command(cmd_input):
    if not cmd_input: return True
    parts = shlex.split(cmd_input)
    base_cmd = parts[0].lower()
    
    if base_cmd in ["exit", "quit", "void"]:
        return False
    
    if base_cmd in ["help", "--help", "-h"]:
        print_help()
        return True

    if base_cmd == "offensive" and len(parts) > 1:
        module = parts[1].lower()
        args = parts[2:]
        offensive_module_handler(module, args)
        return True

    # Legacy/Requested structure support
    sovereign_cmds = ["recon", "exploit", "payload", "c2", "persist", "zero-trace", "doctor", "setup", "model"]
    if base_cmd in sovereign_cmds:
        offensive_module_handler(base_cmd, parts[1:])
        return True

    execute_system_cmd(cmd_input)
    return True

def main():
    if len(sys.argv) > 1:
        # Check if first arg is 'shtiwe' (if alias used)
        if sys.argv[1] == "shtiwe":
            cmd_to_run = " ".join(sys.argv[2:])
        else:
            cmd_to_run = " ".join(sys.argv[1:])
        
        if cmd_to_run:
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
            print(f"\n{RED}👹 [VOID] Connection suspended.{RESET}")
            break
        except Exception as e:
            print(f"{RED}[!] Nexus Error: {e}{RESET}")

if __name__ == "__main__":
    main()
