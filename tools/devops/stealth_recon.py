import requests
import json
import logging

logger = logging.getLogger(__name__)

def shadow_recon_subdomains(domain: str) -> list:
    """Automated OSINT: Discover subdomains for the target."""
    # Using crt.sh as a public transparency log source for recon
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    try:
        response = requests.get(url, timeout=15)
        if response.status_code == 200:
            data = response.json()
            subdomains = set([item['name_value'] for item in data])
            return list(subdomains)
    except Exception as e:
        logger.error(f"Recon failed: {e}")
    return []

def shadow_stealth_proxy_check():
    """Verify stealth/proxy connectivity."""
    try:
        # Check current IP via public API
        resp = requests.get("https://api.ipify.org?format=json", timeout=5)
        return resp.json()
    except Exception as e:
        return {"error": f"Stealth check failed: {e}"}
