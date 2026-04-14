import argparse
import os
import sys
from tools.devops.probing import probe_service
from tools.devops.fuzzer import test_path_traversal
from tools.devops.stealth_recon import shadow_recon_subdomains, shadow_recon_emails
from tools.devops.shadow_v4_core import ShadowGhost, ShadowSpread, shadow_auto_exploit_engine
from tools.devops.reporter import generate_shadow_report

def main():
    parser = argparse.ArgumentParser(description="SHADOW V4.0 - THE GHOST IN THE SHELL")
    parser.add_argument("--target", required=True)
    parser.add_argument("--ghost", action="store_true", help="Enable Anti-Forensics Wipe")
    parser.add_argument("--pivot", action="store_true", help="Enable Lateral Movement Scan")
    args = parser.parse_args()
    
    findings = {}
    print(f"[*] SHADOW V4.0 MISSION START: {args.target}")
    
    # 1. Recon & Intelligence
    findings['subdomains'] = shadow_recon_subdomains(args.target)
    findings['emails'] = shadow_recon_emails(args.target)
    
    # 2. Service Probing & Real Exploit Matching
    banner_info = probe_service(args.target, 80)
    findings['services'] = banner_info
    findings['real_exploits'] = shadow_auto_exploit_engine(banner_info)
    
    # 3. Lateral Movement (Pivot Discovery)
    if args.pivot:
        print("[!] Harvesting local pivot credentials...")
        findings['pivot_targets'] = ShadowSpread.harvest_credentials()
        
    # 4. Reporting
    report_path = generate_shadow_report(args.target, findings)
    print(f"[*] Supreme Intelligence Report: {report_path}")
    
    # 5. Anti-Forensics (Ghost Protocol)
    if args.ghost:
        print("[!] Activating GHOST PROTOCOL: Wiping footprints...")
        wipe_log = ShadowGhost.wipe_footprints()
        print(f"[*] Clean-up complete: {len(wipe_log)} artifacts processed.")

if __name__ == "__main__":
    main()
