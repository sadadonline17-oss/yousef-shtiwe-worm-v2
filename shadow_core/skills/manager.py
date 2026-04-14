import json
from tools.devops.shadow_void_walker import shadow_recon_subdomains, shadow_loot_file, shadow_ghost_wipe
from tools.devops.probing import probe_service

class SkillManager:
    """Orchestrates SHADOW's offensive toolset."""
    def __init__(self):
        self.tools = {
            "recon_subdomains": shadow_recon_subdomains,
            "loot_file": shadow_loot_file,
            "wipe_logs": shadow_ghost_wipe,
            "probe_service": probe_service
        }

    def get_tool_schemas(self):
        # Professional tool schemas matching the agent loop needs
        return [
            {
                "type": "function",
                "function": {
                    "name": "recon_subdomains",
                    "description": "Discover subdomains for a target domain using SSL scraping.",
                    "parameters": {"type": "object", "properties": {"domain": {"type": "string"}}, "required": ["domain"]}
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "loot_file",
                    "description": "Extract sensitive files via Path Traversal.",
                    "parameters": {"type": "object", "properties": {"base_url": {"type": "string"}, "remote_path": {"type": "string"}}, "required": ["base_url", "remote_path"]}
                }
            }
            # ... more schemas mapping to the tools dict
        ]

    def execute(self, name, args):
        if name in self.tools:
            return self.tools[name](**args)
        raise ValueError(f"Skill {name} not found.")
