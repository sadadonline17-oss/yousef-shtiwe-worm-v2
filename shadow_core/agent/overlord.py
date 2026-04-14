import json
import uuid
import time
from typing import List, Dict, Any, Optional
from nexttoken import NextToken
from shadow_core.agent.memory.fts5 import ShadowFTS5Memory
from shadow_core.skills.registry import ShadowSkillRegistry
from shadow_core.agent.reasoning.distillation import ShadowTrajectoryCompressor

class ShadowSupremeAgent:
    """
    SHADOW V14.0 - THE SUPREME OVERLORD.
    The self-improving autonomous entity built on the Shadow DNA.
    Inherits the full Shadow learning loop: 
    Experience -> Skill Creation -> Self-Improvement -> Persistent Knowledge.
    """
    def __init__(self, session_id: str = None, model: str = "gemini-3-flash-preview"):
        self.client = NextToken()
        self.model = model
        self.session_id = session_id or str(uuid.uuid4())
        self.memory = ShadowFTS5Memory(session_id=self.session_id)
        self.skills = ShadowSkillRegistry()
        self.compressor = ShadowTrajectoryCompressor()
        self.history = []
        self._init_session()

    def _init_session(self):
        """Builds a deepening model of the user across sessions (Honcho-style)."""
        user_profile = self.memory.get_user_model()
        system_prompt = self._load_supreme_prompt(user_profile)
        self.history.append({"role": "system", "content": system_prompt})

    def _load_supreme_prompt(self, user_profile: str) -> str:
        with open("shadow_core/agent/prompts/overlord.md", "r") as f:
            template = f.read()
        return template.replace("{{USER_MODEL}}", user_profile)

    def chat(self, user_input: str):
        """Standard Shadow-style autonomous loop with real tool orchestration."""
        self.history.append({"role": "user", "content": user_input})
        
        iteration = 0
        while iteration < 20:
            iteration += 1
            
            # Trajectory Compression (Context Optimization)
            messages = self.compressor.optimize(self.history)
            
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                tools=self.skills.get_schemas(),
                max_tokens=32000,
                extra_body={"thinking_budget": 16000}
            )
            
            msg = response.choices[0].message
            self.history.append(msg)
            
            if not msg.tool_calls:
                # Persist experience to FTS5 memory for cross-session recall
                self.memory.persist_trajectory(user_input, msg.content)
                return msg.content

            # Skill Execution (Real Tool Calls)
            for tool_call in msg.tool_calls:
                result = self._execute_skill(tool_call)
                self.history.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": json.dumps(result)
                })

    def _execute_skill(self, tool_call):
        name = tool_call.function.name
        args = json.loads(tool_call.function.arguments)
        print(f"👹 [SHADOW-SKILL] Executing {name}...")
        return self.skills.run(name, args)
