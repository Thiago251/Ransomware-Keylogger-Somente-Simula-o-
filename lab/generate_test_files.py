"""
Cria arquivos de teste em uma pasta `test_files/` para usar no laboratório.
Script inofensivo — gera arquivos de texto, binários simulados e uma imagem placeholder.
"""
import os
from pathlib import Path
import random
import string

OUT_DIR = Path('test_files')
OUT_DIR.mkdir(exist_ok=True)

def random_text(size=256):
    return ''.join(random.choices(string.ascii_letters + string.digits + ' ', k=size))

# Cria N arquivos txt
for i in range(1, 11):
    p = OUT_DIR / f'document_{i}.txt'
    with p.open('w', encoding='utf-8') as f:
        f.write(f"Este é um arquivo de teste #{i}\n")
        f.write(random_text(512))

# Cria alguns arquivos binários (simulados)
for i in range(1, 4):
    p = OUT_DIR / f'binary_simulated_{i}.bin'
    with p.open('wb') as f:
        f.write(os.urandom(1024 * i))

# Cria um CSV simulado
with (OUT_DIR / 'financials.csv').open('w', encoding='utf-8') as f:
    f.write('id,valor,descricao\n')
    for i in range(1, 6):
        f.write(f"{i},{random.randint(10,10000)},Item_{i}\n")

# Imagem placeholder (requer Pillow); se Pillow não estiver instalado, ignore
try:
    from PIL import Image, ImageDraw
    img = Image.new('RGB', (400, 200), color=(30, 30, 30))
    d = ImageDraw.Draw(img)
    d.text((10,80), 'Placeholder Image', fill=(200,200,200))
    img.save(OUT_DIR / 'placeholder.png')
except Exception:
    # Pillow não instalado — ignore a imagem
    pass

print(f'Arquivos de teste criados em: {OUT_DIR.resolve()}')
