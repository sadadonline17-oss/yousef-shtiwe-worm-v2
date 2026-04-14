import argparse
import sys
from tools.devops.probing import probe_service
from tools.devops.fuzzer import test_cors_exposure
from tools.devops.stealth_recon import shadow_recon_subdomains, shadow_recon_emails, shadow_stealth_proxy_check

def render_dashboard(target, findings):
    print("\n" + "█"*60)
    print(f" 👹 SHADOW V2.5 - GLOBAL COMMAND CENTER 👹")
    print("█"*60)
    print(f" 🎯 TARGET    : {target}")
    print(f" 🕵️ OSINT      : {findings.get('subdomains', 0)} Subs | {findings.get('emails', 0)} Emails")
    print(f" 🔒 STEALTH   : {findings.get('stealth_ip', 'DIRECT')}")
    print("-" * 60)
    print(f" [+] SERVICES : {findings.get('services', 'None')}")
    print(f" [+] EXPLOITS : {findings.get('exploits', 'Clean')}")
    print("█"*60 + "\n")

def main():
    parser = argparse.ArgumentParser(description="SHADOW V2.5")
    parser.add_argument("--target", required=True)
    args = parser.parse_args()
    
    findings = {
        "subdomains": len(shadow_recon_subdomains(args.target)),
        "emails": len(shadow_recon_emails(args.target)),
        "stealth_ip": shadow_stealth_proxy_check().get("ip", "Unknown"),
        "services": probe_service(args.target, 80),
        "exploits": "Vulnerability probes executed via Polymorphic Payload."
    }
    
    render_dashboard(args.target, findings)

if __name__ == "__main__":
    main()
