import fire
import sys
import os
from agent.run_agent import ShadowAIAgent
from gateway.run import ShadowGateway

class ShadowCLI:
    """👹 SHADOW V12.0 - THE VOID WALKER SUPREME CLI 👹"""
    
    def chat(self, query=None):
        """Interactive SHADOW TUI with full memory and skill access."""
        agent = ShadowAIAgent()
        print("👹 [SHADOW-TUI] Connection Established. Void is listening...")
        while True:
            try:
                user_input = query or input("shadow> ")
                if user_input.lower() in ["exit", "quit"]: break
                response = agent.chat(user_input)
                print(f"\n👹 [VOID] {response}\n")
                if query: break
            except KeyboardInterrupt: break

    def gateway(self):
        """Launch the Multi-Platform Nexus (Telegram/Discord/Signal)."""
        nexus = ShadowGateway()
        nexus.start()

    def mission(self, target, goal="Execute full exfiltration"):
        """Launch a high-end autonomous mission via the Agentic Loop."""
        agent = ShadowAIAgent()
        agent.chat(f"Target: {target} | Objective: {goal}")

    def version(self):
        """Show the Supreme Version."""
        print("SHADOW V12.0 'THE SINGULARITY' - VOID WALKER EDITION")

if __name__ == "__main__":
    fire.Fire(ShadowCLI)
