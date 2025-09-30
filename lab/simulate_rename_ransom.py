"""
Simulação educativa: renomeia arquivos adicionando o sufixo `.locked_simulado`.
NÃO altera o conteúdo dos arquivos — apenas renomeia para demonstrar comportamento observável.
Use em `test_files/` gerado pelo `generate_test_files.py`.
"""
import time
from pathlib import Path

DIR = Path('test_files')
SUFFIX = '.locked_simulado'
LOG = Path('ransom_simulation_log.txt')

if not DIR.exists():
    print('Diretório test_files/ não encontrado. Rode generate_test_files.py primeiro.')
    exit(1)

with LOG.open('a', encoding='utf-8') as log:
    for f in sorted(DIR.iterdir()):
        if f.is_file() and not f.name.endswith(SUFFIX):
            new_name = f.with_name(f.name + SUFFIX)
            try:
                f.rename(new_name)
                log.write(f"{time.time()} RENAMED {f} -> {new_name}\n")
                print(f"Renomeado: {f.name} -> {new_name.name}")
                time.sleep(0.15)  # pequena pausa para observação
            except Exception as e:
                log.write(f"{time.time()} ERROR renaming {f}: {e}\n")

print('Simulação de renomeação concluída. Confira ransom_simulation_log.txt')
