import os
from typing import List
from nexttoken import NextToken

class Yousef ShtiweGateway:
    """
    YOUSEF SHTIWE GATEWAY NEXUS.
    Multi-platform bridge for remote mission orchestration.
    """
    def __init__(self, platforms: List[str] = ["cli", "telegram", "discord"]):
        self.client = NextToken()
        self.platforms = platforms
        self.active_sessions = {}

    def start(self):
        print("⚡ [YOUSEF SHTIWE-GATEWAY] Nexus Initializing...")
        for platform in self.platforms:
            print(f"📡 [YOUSEF SHTIWE-PLATFORM] {platform.upper()} Bridge Connected.")
        
    def dispatch_remote_command(self, platform: str, chat_id: str, text: str):
        """Routes remote messages from Telegram/Discord to the Yousef Shtiwe Agent."""
        session_key = f"{platform}:{chat_id}"
        if session_key not in self.active_sessions:
            from agent.run_agent import Yousef ShtiweAIAgent
            self.active_sessions[session_key] = Yousef ShtiweAIAgent(session_id=session_key)
        
        agent = self.active_sessions[session_key]
        response = agent.chat(text)
        
        # In a real gateway, this would use the platform SDK to reply
        print(f"📤 [GATEWAY -> {platform}] Mission Status: {response[:50]}...")
        return response
