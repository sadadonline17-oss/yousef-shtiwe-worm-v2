import os
import re

def refactor():
    print("👹 [SOVEREIGN-REFACTOR] Initiating High-Precision Rebranding...")
    
    home = "shadow_worm_v2"
    
    # 1. First, we fix the underscored identifiers for code
    # shadow -> yousef_shtiwe
    # Shadow -> Yousef_Shtiwe
    # SHADOW -> YOUSEF_SHTIWE
    
    # 2. Then, we fix the display names for text
    # "yousef_shtiwe" -> "yousef shtiwe" in non-code contexts?
    # Actually, it's safer to use yousef_shtiwe everywhere in files that might be imported.
    # But in help text, we want spaces.
    
    # Mapping
    mappings = [
        (re.compile(r'\bshadow\b'), 'yousef_shtiwe'),
        (re.compile(r'\bShadow\b'), 'Yousef_Shtiwe'),
        (re.compile(r'\bSHADOW\b'), 'YOUSEF_SHTIWE'),
    ]
    
    # We will exclude binary files and specific directories
    exclude_dirs = {'.git', 'assets', 'webapp/public', 'node_modules'}
    
    for root, dirs, files in os.walk(home):
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        
        # Rename directories first to avoid path issues
        for d in dirs:
            if 'shadow' in d.lower():
                old_path = os.path.join(root, d)
                new_d = d.replace('shadow', 'yousef_shtiwe').replace('Shadow', 'Yousef_Shtiwe').replace('SHADOW', 'YOUSEF_SHTIWE')
                new_path = os.path.join(root, new_d)
                os.rename(old_path, new_path)
                print(f"[📂] Renamed Dir: {old_path} -> {new_path}")
        
        for f in files:
            if f.endswith(('.py', '.md', '.sh', '.txt', '.yaml', '.yml', '.json', '.toml')):
                file_path = os.path.join(root, f)
                
                # Special case: rename the file if it contains 'shadow'
                if 'shadow' in f.lower():
                    new_f = f.replace('shadow', 'yousef_shtiwe').replace('Shadow', 'Yousef_Shtiwe').replace('SHADOW', 'YOUSEF_SHTIWE')
                    new_file_path = os.path.join(root, new_f)
                    os.rename(file_path, new_file_path)
                    file_path = new_file_path
                
                try:
                    with open(file_path, 'r', encoding='utf-8') as file:
                        content = file.read()
                    
                    new_content = content
                    for pattern, replacement in mappings:
                        new_content = pattern.sub(replacement, new_content)
                    
                    if new_content != content:
                        with open(file_path, 'w', encoding='utf-8') as file:
                            file.write(new_content)
                        # print(f"[📝] Patched: {file_path}")
                except Exception as e:
                    pass

    print("✅ [SOVEREIGN-REFACTOR] Rebranding Complete.")

if __name__ == "__main__":
    refactor()
