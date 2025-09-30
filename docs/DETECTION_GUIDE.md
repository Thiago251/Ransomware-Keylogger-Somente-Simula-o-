# DETECTION_GUIDE — Coleta e detecção (resumo)

## Instrumentação
- Sysmon (config adequada) — registra criação de processos, hashes, operações de arquivo.
- Procmon (Sysinternals) — monitorar operações de arquivos em tempo real.
- Wireshark/tcpdump — capturar tráfego (caso haja transferência).
- Ferramentas de análise de memória: Volatility.

## Indicadores (exemplos educativos)
- Renomeações em massa de arquivos para sufixos incomuns (ex.: .locked_simulado).
- Padrões de I/O elevado por um processo não associado a backup legítimo.
- Arquivos de texto com conteúdo de resgate (note: aqui usamos arquivo de simulação).

## Como gerar IOCs
- Nomes/paths de arquivos renomeados.
- Hashes de binários executados durante a simulação.
- Timelines correlacionando eventos Sysmon e Procmon.

## Coleta
- Salve EVTX (Sysmon) e pcap em `/forensics/` para anexar ao relatório.
