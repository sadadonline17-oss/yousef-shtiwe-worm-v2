import os

def heal_rc(path):
    if not os.path.exists(path): return
    with open(path, 'r') as f: lines = f.readlines()
    
    clean = []
    skip = False
    for line in lines:
        l = line.strip().lower()
        if 'yousef shtiwe start' in l: skip = True; continue
        if 'yousef shtiwe end' in l: skip = False; continue
        if skip: continue
        
        # Cleanup legacy/corrupted blocks
        if any(x in l for x in ['yousef', 'shtiwe', 'hermes', 'clawdbot', 'openclaw']):
            if l.startswith('yousef()') or l.startswith('alias') or l.startswith('export'):
                continue
            if 'else' in l or 'fi' in l or '}' in l:
                if any(x in l for x in ['yousef', 'shtiwe']): continue
        clean.append(line)
    
    # Inject Protected Block
    cli_path = os.environ.get("CLI_PATH", "/data/data/com.termux/files/home/yousef-shtiwe-worm-v2/yousef_shtiwe_cli.py")
    nexus = [
        '\n# >>> YOUSEF SHTIWE START >>>\n',
        'yousef() {\n',
        '    if [ "$1" = "shtiwe" ]; then\n',
        '        shift\n',
        '        export SHTIWE_VOID_OVERRIDE=1\n',
        f'        python3 "{cli_path}" "$@"\n',
        '    else\n',
        '        command yousef "$@" 2>/dev/null || echo "[!] Use yousef shtiwe"\n',
        '    fi\n',
        '}\n',
        '# <<< YOUSEF SHTIWE END <<<\n'
    ]
    with open(path, 'w') as f: f.writelines(clean + nexus)

for rc in [os.path.expanduser('~/.bashrc'), os.path.expanduser('~/.zshrc')]:
    heal_rc(rc)
