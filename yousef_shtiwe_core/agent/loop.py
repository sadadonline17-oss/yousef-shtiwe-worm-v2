import json
import time
import logging
from nexttoken import NextToken
from yousef shtiwe_core.memory.database import Yousef ShtiweMemory
from yousef shtiwe_core.skills.manager import SkillManager

class Yousef ShtiweAgent:
    """
    YOUSEF SHTIWE V11.0 - The Autonomous Offensive Entity.
    A self-improving agent architecture based on the Yousef Shtiwe loop.
    """
    def __init__(self, model="gemini-3-flash-preview", system_prompt_path="yousef shtiwe_core/prompts/system.md"):
        self.client = NextToken()
        self.model = model
        self.memory = Yousef ShtiweMemory()
        self.skills = SkillManager()
        with open(system_prompt_path, 'r') as f:
            self.system_prompt = f.read()

    def run(self, task: str):
        print(f"👹 [YOUSEF SHTIWE-AGENT] Initializing Mission: {task}")
        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": task}
        ]
        
        # Load relevant memories
        context = self.memory.search(task)
        if context:
            messages.append({"role": "system", "content": f"Relevant Past Intel: {context}"})

        iteration = 0
        while iteration < 15:
            iteration += 1
            print(f"💀 [YOUSEF SHTIWE-LOOP] Iteration {iteration}")
            
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                tools=self.skills.get_tool_schemas(),
                max_tokens=16000
            )

            choice = response.choices[0]
            messages.append(choice.message)

            if choice.finish_reason == "stop" or not choice.message.tool_calls:
                # Finalize and persist learning
                self.memory.persist(task, choice.message.content)
                print("🏁 [YOUSEF SHTIWE-AGENT] Mission Accomplished.")
                return choice.message.content

            for tc in choice.message.tool_calls:
                name = tc.function.name
                args = json.loads(tc.function.arguments)
                print(f"🔧 [YOUSEF SHTIWE-TOOL] {name}({json.dumps(args)})")
                
                try:
                    result = self.skills.execute(name, args)
                    messages.append({
                        "role": "tool",
                        "tool_call_id": tc.id,
                        "content": json.dumps(result)
                    })
                except Exception as e:
                    messages.append({
                        "role": "tool",
                        "tool_call_id": tc.id,
                        "content": f"Error: {str(e)}"
                    })
