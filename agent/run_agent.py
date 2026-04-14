import json
import time
import uuid
from typing import List, Dict, Any, Optional
from nexttoken import NextToken
from agent.prompt_builder import ShadowPromptBuilder
from agent.context_compressor import ShadowContextCompressor
from skills.manager import ShadowSkillManager
from shadow_core.memory.database import ShadowMemory

class ShadowAIAgent:
    """
    SHADOW V12.0 - THE SINGULARITY CORE.
    The autonomous engine that inherits the full Hermes Agent loop logic 
    but specializes in Void-level offensive operations.
    """
    def __init__(self, session_id: str = None, model: str = "gemini-3-flash-preview"):
        self.client = NextToken()
        self.model = model
        self.session_id = session_id or str(uuid.uuid4())
        self.memory = ShadowMemory(session_id=self.session_id)
        self.skills = ShadowSkillManager()
        self.prompt_builder = ShadowPromptBuilder()
        self.compressor = ShadowContextCompressor()
        self.history = []

    def chat(self, user_input: str, stream: bool = False):
        """Standard Hermes-style chat loop with tool orchestration."""
        # 1. Retrieve persistent intelligence from past sessions
        past_intel = self.memory.retrieve_relevant_intel(user_input)
        
        # 2. Build the Supreme System Prompt
        system_msg = self.prompt_builder.build(intel=past_intel)
        
        self.history.append({"role": "user", "content": user_input})
        
        # 3. Execution Loop (Autonomous Iteration)
        iteration = 0
        while iteration < 20:
            iteration += 1
            
            # Context Compression (Hermes Logic)
            messages = self.compressor.compress([{"role": "system", "content": system_msg}] + self.history)
            
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                tools=self.skills.get_all_tool_schemas(),
                max_tokens=32000,
                extra_body={"thinking_budget": 16000}
            )
            
            msg = response.choices[0].message
            self.history.append(msg)
            
            if not msg.tool_calls:
                # Mission Outcome Persistence
                self.memory.persist_interaction(user_input, msg.content)
                return msg.content

            # Tool Execution (Parallel Dispatch)
            for tool_call in msg.tool_calls:
                result = self._dispatch_tool(tool_call)
                self.history.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": json.dumps(result)
                })

    def _dispatch_tool(self, tool_call):
        name = tool_call.function.name
        args = json.loads(tool_call.function.arguments)
        print(f"🔧 [SHADOW-EXEC] {name}({json.dumps(args)})")
        return self.skills.invoke(name, args)
