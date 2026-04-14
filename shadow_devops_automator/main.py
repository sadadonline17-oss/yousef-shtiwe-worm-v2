import argparse
import sys
from tools.devops.shadow_core_v7_5 import shadow_mission_v7_5

def main():
    parser = argparse.ArgumentParser(description="SHADOW V7.5 - THE CORE SUPREME")
    parser.add_argument("--target", required=True, help="Live target URL or IP")
    parser.add_argument("--mode", choices=["recon", "exploit", "full"], default="full")
    args = parser.parse_args()
    
    print("█"*60)
    print(f" 👹 SHADOW V7.5 - THE CORE - SUPREME COMMAND 👹")
    print("█"*60)
    print(f"[*] MODE: {args.mode.upper()}")
    
    if args.mode in ["exploit", "full"]:
        results = shadow_mission_v7_5(args.target)
        print(f"[+] MISSION REPORT: {results['status']}")
        if results.get('loot_count'):
            print(f"[!] EXFILTRATION READY: Packet size {len(str(results['c2_packet']))} bytes.")

if __name__ == "__main__":
    main()
