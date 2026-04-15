import subprocess
import os

class ShtiweRecon:
    def __init__(self):
        self.masscan = "masscan"
        self.nmap = "nmap"

    def execute_recon(self, target, ports="1-65535"):
        print(f"\033[38;5;220m[👁] YOUSEF SHTIWE | Initiating Atomic Scan on {target}\033[0m")
        try:
            # Reality: Direct Process execution for masscan
            cmd = [self.masscan, target, "-p", ports, "--rate=1000", "--wait=0"]
            result = subprocess.run(cmd, capture_output=True, text=True)
            return result.stdout if result.stdout else "No open ports found via masscan."
        except Exception:
            # Fallback to Nmap reality
            cmd = [self.nmap, "-T4", "-F", target]
            result = subprocess.run(cmd, capture_output=True, text=True)
            return result.stdout
