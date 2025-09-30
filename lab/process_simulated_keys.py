"""
Processa `simulated_keystrokes.txt` e gera um log formatado.
Uso educativo: demonstra como analisar um artefato que simula captura de teclas.
"""
from pathlib import Path
from datetime import datetime

IN_FILE = Path('simulated_keystrokes.txt')
OUT_FILE = Path('simulated_keys_parsed.log')

if not IN_FILE.exists():
    print('Arquivo simulated_keystrokes.txt não encontrado.')
    exit(1)

with IN_FILE.open('r', encoding='utf-8') as inf, OUT_FILE.open('w', encoding='utf-8') as outf:
    for line in inf:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        parts = line.split('|')
        if len(parts) != 2:
            continue
        ts_str, key = parts
        try:
            ts = int(ts_str)
            dt = datetime.utcfromtimestamp(ts).isoformat() + 'Z'
        except Exception:
            dt = 'UNKNOWN'
        outf.write(f"{dt}\t{key}\n")

print(f'Arquivo processado. Saída: {OUT_FILE.resolve()}')
