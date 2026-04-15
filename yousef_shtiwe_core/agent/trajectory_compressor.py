import json
from typing import List, Dict, Any
from nexttoken import NextToken

class Yousef ShtiweTrajectoryCompressor:
    """
    YOUSEF SHTIWE TRAJECTORY COMPRESSOR (STC).
    Professional context management system designed to handle infinite mission history 
    by distilling core mission milestones and state transitions.
    """
    def __init__(self, model: str = "gemini-2.5-flash-lite"):
        self.client = NextToken()
        self.model = model

    def compress(self, history: List[Dict[str, Any]], max_chars: int = 12000) -> str:
        """Distill the mission trajectory into a high-density intelligence summary."""
        if not history or len(str(history)) < max_chars:
            return str(history)

        print("🧬 [YOUSEF SHTIWE-STC] Distilling Trajectory to Core Intel...")
        
        prompt = f"""
        # YOUSEF SHTIWE TRAJECTORY DISTILLATION PROTOCOL 👁👹
        Analyze the following mission history and extract ONLY the supreme technical intel:
        1. Current objective and progress.
        2. Verified target vulnerabilities and discovered assets.
        3. Successful vs. Failed tool executions.
        4. Crucial state variables (IPs, Paths, Tokens).

        Output a high-density technical summary that YOUSEF SHTIWE can use as its perfect mental map.

        MISSION HISTORY:
        {json.dumps(history[-20:])}  # Focus on the most recent 20 events
        """

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=4000
        )
        
        summary = response.choices[0].message.content
        print(f"🧬 [YOUSEF SHTIWE-STC] Distillation Complete: {len(summary)} chars.")
        return summary
