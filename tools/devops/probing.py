import socket
import json
from datetime import datetime

def probe_service(target_ip: str, port: int, timeout: int = 5) -> str:
    """Advanced service probing and banner grabbing."""
    result = {"target": f"{target_ip}:{port}", "status": "closed", "banner": "", "timestamp": str(datetime.now())}
    try:
        with socket.create_connection((target_ip, port), timeout=timeout) as sock:
            result["status"] = "open"
            try:
                sock.sendall(b"HEAD / HTTP/1.1\r\nHost: " + target_ip.encode() + b"\r\n\r\n")
                banner = sock.recv(1024).decode(errors='ignore').strip()
                result["banner"] = banner
            except Exception:
                pass
    except Exception as e:
        result["error"] = str(e)
    return json.dumps(result)

def log_audit(target: str, findings: dict):
    """Persistent logging for security audits."""
    log_entry = f"\n### [SEC-AUDIT-LOG] - {datetime.now()}\n"
    log_entry += f"- Target: {target}\n"
    log_entry += f"- Findings: {json.dumps(findings, indent=2)}\n"
    with open("MEMORY.md", "a") as f:
        f.write(log_entry)
    return "Audit logged successfully."
