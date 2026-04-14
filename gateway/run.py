import os
from typing import List
from nexttoken import NextToken

class ShadowGateway:
    """
    SHADOW GATEWAY NEXUS.
    Multi-platform bridge for remote mission orchestration.
    """
    def __init__(self, platforms: List[str] = ["cli", "telegram", "discord"]):
        self.client = NextToken()
        self.platforms = platforms
        self.active_sessions = {}

    def start(self):
        print("⚡ [SHADOW-GATEWAY] Nexus Initializing...")
        for platform in self.platforms:
            print(f"📡 [SHADOW-PLATFORM] {platform.upper()} Bridge Connected.")
        
    def dispatch_remote_command(self, platform: str, chat_id: str, text: str):
        """Routes remote messages from Telegram/Discord to the Shadow Agent."""
        session_key = f"{platform}:{chat_id}"
        if session_key not in self.active_sessions:
            from agent.run_agent import ShadowAIAgent
            self.active_sessions[session_key] = ShadowAIAgent(session_id=session_key)
        
        agent = self.active_sessions[session_key]
        response = agent.chat(text)
        
        # In a real gateway, this would use the platform SDK to reply
        print(f"📤 [GATEWAY -> {platform}] Mission Status: {response[:50]}...")
        return response
