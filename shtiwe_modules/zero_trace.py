import os

class ZeroTrace:
    def purge_footprints(self):
        print("\033[35m[!] YOUSEF SHTIWE | Neutralizing Digital Footprints...\033[0m")
        targets = [
            os.path.expanduser("~/.bash_history"),
            os.path.expanduser("~/.zsh_history"),
            "/var/log/auth.log",
            "/var/log/syslog"
        ]
        for path in targets:
            if os.path.exists(path):
                # Reality: Physical wipe with zero bytes
                size = os.path.getsize(path)
                with open(path, "wb") as f:
                    f.write(b"\x00" * size)
                os.remove(path)
        return "[✓] Footprints neutralized. Trace: ZERO."
