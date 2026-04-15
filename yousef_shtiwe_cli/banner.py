from .colors import RED, GOLD, PURPLE, RESET, BOLD

def get_banner():
    # Using a raw string (r""") to avoid SyntaxWarning with backslashes in ASCII art
    banner = rf"""
{RED}{BOLD}    __  ______  __  _______  ________ {GOLD}   _____ __  _________________      _______
{RED}{BOLD}   / / / / __ \/ / / / ___/ / ____/  {GOLD}  / ___// / / /_  __/  _/ __ \ | /| / / ____/
{RED}{BOLD}  / /_/ / / / / / / /\__ \ / __/     {GOLD}  \__ \/ /_/ / / /  / // / / / |/ |/ / __/   
{RED}{BOLD} / __  / /_/ / /_/ /___/ // /____    {GOLD} ___/ / __  / / / _/ // /_/ /|  /|  / /____  
{RED}{BOLD}/_/ /_/\____/\____//____//________/  {GOLD}/____/_/ /_/ /_/ /___/\____/ |_/ |_/________/
{PURPLE}
                      [ SOVEREIGN OFFENSIVE INTELLIGENCE ]
                      [        VERSION 2026.4.15         ]
{RESET}
    """
    return banner
