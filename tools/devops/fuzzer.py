import requests
import json

def test_path_traversal(base_url: str):
    """Fuzzing for path traversal vulnerabilities."""
    payloads = ["/../../../../etc/passwd", "/..%2f..%2f..%2f..%2fetc/passwd"]
    results = []
    for payload in payloads:
        url = f"{base_url}{payload}"
        try:
            response = requests.get(url, timeout=5)
            if "root:x:0:0:" in response.text:
                results.append({"url": url, "vulnerable": True})
            else:
                results.append({"url": url, "vulnerable": False})
        except Exception as e:
            results.append({"url": url, "error": str(e)})
    return json.dumps(results)

def test_cors_exposure(url: str):
    """Fuzzing for weak CORS settings."""
    headers = {"Origin": "https://evil-attacker.com"}
    try:
        response = requests.options(url, headers=headers, timeout=5)
        allow_origin = response.headers.get("Access-Control-Allow-Origin", "")
        return json.dumps({"url": url, "vulnerable": allow_origin == "*"})
    except Exception as e:
        return json.dumps({"error": str(e)})
