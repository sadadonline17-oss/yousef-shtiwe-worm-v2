import argparse
import sys
from tools.devops.shadow_v6_orchestrator import ShadowOrchestrator

def main():
    parser = argparse.ArgumentParser(description="SHADOW V6.0 - THE SINGULARITY")
    parser.add_argument("--target", required=True, help="Target for autonomous mission")
    parser.add_argument("--auto", action="store_true", help="Launch Autonomous Orchestrator")
    args = parser.parse_args()
    
    print("█"*60)
    print(f" 👹 SHADOW V6.0 - THE SINGULARITY - SUPREME COMMAND 👹")
    print("█"*60)
    
    if args.auto:
        print(f"[!] Launching Master Mind Orchestrator for: {args.target}")
        orchestrator = ShadowOrchestrator(args.target)
        orchestrator.run_autonomous_mission()
    else:
        # Standard manual mode
        print("[*] Running in Manual Command Mode. Use --auto for Full Singularity.")

if __name__ == "__main__":
    main()
