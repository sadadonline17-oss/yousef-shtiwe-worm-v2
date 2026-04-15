import fire
import sys
import os
from agent.run_agent import Yousef ShtiweAIAgent
from gateway.run import Yousef ShtiweGateway

class Yousef ShtiweCLI:
    """👹 YOUSEF SHTIWE V12.0 - THE VOID WALKER SUPREME CLI 👹"""
    
    def chat(self, query=None):
        """Interactive YOUSEF SHTIWE TUI with full memory and skill access."""
        agent = Yousef ShtiweAIAgent()
        print("👹 [YOUSEF SHTIWE-TUI] Connection Established. Void is listening...")
        while True:
            try:
                user_input = query or input("yousef shtiwe> ")
                if user_input.lower() in ["exit", "quit"]: break
                response = agent.chat(user_input)
                print(f"\n👹 [VOID] {response}\n")
                if query: break
            except KeyboardInterrupt: break

    def gateway(self):
        """Launch the Multi-Platform Nexus (Telegram/Discord/Signal)."""
        nexus = Yousef ShtiweGateway()
        nexus.start()

    def mission(self, target, goal="Execute full exfiltration"):
        """Launch a high-end autonomous mission via the Agentic Loop."""
        agent = Yousef ShtiweAIAgent()
        agent.chat(f"Target: {target} | Objective: {goal}")

    def version(self):
        """Show the Supreme Version."""
        print("YOUSEF SHTIWE V12.0 'THE SINGULARITY' - VOID WALKER EDITION")

if __name__ == "__main__":
    fire.Fire(Yousef ShtiweCLI)
