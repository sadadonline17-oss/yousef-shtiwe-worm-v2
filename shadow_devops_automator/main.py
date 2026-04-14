import argparse
import sys
from tools.devops.shadow_v6_orchestrator import ShadowOrchestrator
from tools.devops.shadow_v7_ghost.py import shadow_apt_simulation

def main():
    parser = argparse.ArgumentParser(description="SHADOW V7.0 - THE GHOST OVERLORD")
    parser.add_argument("--target", required=True)
    parser.add_argument("--apt", action="store_true", help="Launch Full APT Simulation Mode")
    parser.add_argument("--stealth", action="store_true", help="Enable EDR Evasion & LotL")
    args = parser.parse_args()
    
    print("█"*60)
    print(f" 👹 SHADOW V7.0 - THE GHOST OVERLORD - SUPREME COMMAND 👹")
    print("█"*60)
    
    if args.apt:
        print(f"[!] Launching APT-Level Mission for: {args.target}")
        results = shadow_apt_simulation(args.target)
        for k, v in results.items():
            print(f"[+] {k.upper()}: {v}")
    
    # Orchestrator handles the base automation
    orchestrator = ShadowOrchestrator(args.target)
    orchestrator.run_autonomous_mission()

if __name__ == "__main__":
    main()
