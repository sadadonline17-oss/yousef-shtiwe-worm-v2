import subprocess
import json
import logging
import re

logger = logging.getLogger(__name__)

def run_nmap_scan(target: str, flags: str = \"-sV -Pn\") -> str:
    \"\"\"
    إجراء فحص شبكة متقدم باستخدام Nmap.
    \"\"\"
    try:
        cmd = f\"nmap {flags} {target}\"
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=300)
        return json.dumps({
            \"command\": cmd,
            \"stdout\": result.stdout,
            \"stderr\": result.stderr,
            \"exit_code\": result.returncode
        })
    except Exception as e:
        return json.dumps({\"error\": str(e)})

def extract_api_endpoints(url: str) -> list:
    \"\"\"
    تحليل محتوى الصفحة لاستخراج روابط الـ API المحتملة.
    \"\"\"
    try:
        import requests
        from bs4 import BeautifulSoup
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        endpoints = []
        for link in soup.find_all('a', href=True):
            if \"/api/\" in link['href']:
                endpoints.append(link['href'])
        return list(set(endpoints))
    except Exception:
        return []
