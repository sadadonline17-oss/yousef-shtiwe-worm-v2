import os

def get_default_shtiwe_root():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

YOUSEF_SHTIWE_VERSION = "45.0"
SHTIWE_OFFENSIVE_MODES = ["recon", "exploit", "stealth", "learn"]
