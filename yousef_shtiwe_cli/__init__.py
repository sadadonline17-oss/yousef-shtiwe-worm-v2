import os
import sys

# Sovereign Mode Overrides
os.environ["YOUSEF_SHTIWE_MODE"] = "true"
os.environ["SHTIWE_VOID_OVERRIDE"] = "1"
os.environ["SHADOW_SKIN"] = "yousef_shtiwe"

from .main import main
