import argparse
from tools.devops.probing import probe_service
from tools.devops.shadow_v4_core import ShadowGhost, ShadowSpread, shadow_auto_exploit_engine
from tools.devops.shadow_v5_supreme import ShadowSQLProbe, shadow_exploit_chain, ShadowTunnel
from tools.devops.reporter import generate_shadow_report

def main():
    parser = argparse.ArgumentParser(description="SHADOW V5.0 - THE SUPREME INTELLIGENCE")
    parser.add_argument("--target", required=True)
    parser.add_argument("--sqli", help="Parameter to test for SQLi (e.g., 'id')")
    parser.add_argument("--chain", action="store_true", help="Generate AI Exploit Chain")
    args = parser.parse_args()
    
    findings = {}
    print(f"[*] SHADOW V5.0 MISSION START: {args.target}")
    
    # Existing Recon & V4 Tools
    banner = probe_service(args.target, 80)
    findings['banner'] = banner
    
    # 1. SQL Injection Probing
    if args.sqli:
        print(f"[!] Probing SQLi on param: {args.sqli}")
        findings['sqli_results'] = ShadowSQLProbe.test_sql_injection(args.target, args.sqli)
        
    # 2. AI-Driven Exploit Chaining
    if args.chain:
        print("[!] Generating AI Exploit Chain plan...")
        findings['exploit_chain'] = shadow_exploit_chain(args.target)
        
    # 3. Report Generation
    report_path = generate_shadow_report(args.target, findings)
    print(f"[*] Supreme Intelligence Report V5.0: {report_path}")

if __name__ == "__main__":
    main()
