# Relatório do Projeto — Simulações Educacionais (Safe)

**Autor:** Seu Nome  
**Curso:** Formação em Cyber Security  
**Data:** YYYY-MM-DD

---

## 1. Resumo executivo
Este relatório descreve experimentos educativos que demonstram conceitos de ransomware e keylogger de forma segura e controlada. O objetivo é entender TTPs, instrumentar a detecção e propor mitigação.

## 2. Ambiente
- VM target: Windows/Linux (detalhes)
- VM analyst: Ferramentas: Wireshark, Sysmon, Procmon, Volatility
- Rede: Host-only / internal (isolada)

## 3. Artefatos usados
- Scripts: `generate_test_files.py`, `simulate_rename_ransom.py`, `process_simulated_keys.py`
- Arquivos gerados: `test_files/`, `ransom_simulation_log.txt`, `simulated_keys_parsed.log`

## 4. Execução dos experimentos
### 4.1 Geração de arquivos de teste
Comando: `python generate_test_files.py`  
Observações: criou 10 txts, 3 binários e um CSV.

### 4.2 Simulação tipo 'ransomware' (renomeação)
Comando: `python simulate_rename_ransom.py`  
Observações: Todos os arquivos foram renomeados com o sufixo `.locked_simulado`. Foi possível detectar atividade via Sysmon (ver anexos).

### 4.3 Simulação tipo 'keylogger' (processamento de artefato)
Comando: `python process_simulated_keys.py`  
Observações: Processou `simulated_keystrokes.txt` para `simulated_keys_parsed.log`.

## 5. Análise forense e detecção
- Timeline correlacionada (incluir timestamps do Sysmon e do log de renomeações).
- IOCs: nomes de arquivos renomeados, entradas de log, hashes de binário (se houver).
- Prints / screenshots: (incluir imagens em /lab/images/)

## 6. Mitigação recomendada
(Use /docs/MITIGATION.md como referência.)

## 7. Conclusão
Resumo do que aprendeu e próximos passos (testes adicionais, integração com EDR, criação de regras YARA/Suricata).

---

## Anexos
- sysmon_example.evtx (se coletado)
- capture_example.pcap (se coletado)
- ransom_simulation_log.txt
- simulated_keys_parsed.log
