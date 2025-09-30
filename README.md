# Simulações Educacionais: Ransomware & Keylogger (Safe)

**Objetivo:** Demonstrar, de forma educativa e segura, conceitos relacionados a ransomware e keylogger através de simulações controladas, análise forense e recomendações de defesa.

> ⚠️ **Aviso importante:** Este repositório contém **apenas simulações educativas**. **Não há código malicioso real.**
> - Não criptografamos conteúdo real — apenas demonstramos comportamentos observáveis (por exemplo, renomeações).
> - Não capturamos teclas do sistema em tempo real — usamos arquivos simulados como artefato de análise.
> - Sempre execute em **VMs isoladas** e com **snapshot**.

## Estrutura do repositório

```
/Simulacoes-Educacionais-Safe/
├─ README.md
├─ LICENSE
├─ .gitignore
├─ /lab/
│  ├─ generate_test_files.py
│  ├─ simulate_rename_ransom.py
│  ├─ simulated_keystrokes.txt
│  ├─ process_simulated_keys.py
│  └─ /images/
├─ /docs/
│  ├─ LAB_SETUP.md
│  ├─ DETECTION_GUIDE.md
│  └─ MITIGATION.md
├─ /forensics/
│  └─ README.md
└─ /deliverables/
   ├─ project_report.md
   └─ slides_outline.md
```

## Como usar (resumo, ambiente isolado)

1. Crie uma VM `target` (snapshot) e uma VM `analyst` (para análise) em rede isolada (host-only / internal), sem Internet.
2. Copie a pasta `/lab/` para a VM `target`.
3. Em `target`:
   - Instale Python 3.8+ e (opcional) Pillow: `pip install pillow`
   - Rode `python generate_test_files.py` — isso criará `test_files/` com arquivos inofensivos.
   - Rode `python simulate_rename_ransom.py` — isso renomeará arquivos adicionando `.locked_simulado` (NÃO cifra).
   - Abra `simulated_keystrokes.txt` (está na raiz do repo) e rode `python process_simulated_keys.py` — processa esse arquivo em `simulated_keys_parsed.log`.
4. Em `analyst`:
   - Use Sysmon/ProcMon/Wireshark para coletar evidências (tudo em rede isolada).
   - Salve os artefatos em `/forensics/` (ex.: pcap, evtx) e inclua no relatório.

## Entregáveis sugeridos para o curso

- `README.md` (este arquivo)
- `/lab/` com scripts educativos
- `/docs/` com guias de setup, detecção e mitigação
- `project_report.md` convertido para PDF com screenshots e análises
- `/deliverables/slides_outline.md` para sua apresentação

## Dependências (recomendadas)
- Python 3.8+
- Pillow (para gerar placeholder image) — `pip install pillow`
- Ferramentas de análise (no analista): Wireshark, Sysinternals (Procmon), Volatility, Sysmon

## Licença
MIT — veja o arquivo LICENSE.

---
