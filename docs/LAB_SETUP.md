# LAB_SETUP — Configuração segura do laboratório

Objetivo: preparar um ambiente controlado para executar as simulações educativas.

## Requisitos mínimos
- 2 VMs (recomendado): `target` (onde roda o laboratório) e `analyst` (onde se analisa).
- Rede: Host-only / Internal (sem acesso à Internet).
- Ferramentas em `analyst`: Wireshark, Sysinternals (Procmon), Volatility, Python, editor de texto.
- Snapshots: tire snapshot do `target` antes de qualquer experimento.

## Passos resumidos
1. Criar VMs; aplicar atualizações de SO apenas se necessário e com snapshots.
2. Isolar rede (sem NAT/Internet).
3. Habilitar logs (Sysmon) no `target` com configuração mínima:
   - Log de criação de processos
   - Log de criação/modificação/renomeação de arquivos
4. Copiar o diretório `/lab/` para `target`.
5. Executar os scripts conforme README e coletar logs (evtx, pcap).
