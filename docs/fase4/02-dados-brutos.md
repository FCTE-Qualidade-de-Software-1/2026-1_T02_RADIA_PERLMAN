# Dados Brutos

Os dados brutos coletados na execução da avaliação estão armazenados no diretório `docs/fase4/Dados_Brutos`. Para garantir a rastreabilidade e a transparência (critério F4-C2), a Tabela 2.1 abaixo cataloga todos os artefatos gerados, vinculando-os à métrica correspondente e à instrução de coleta que os originou.

**Tabela 2.1: Catálogo de dados brutos coletados.**

| Arquivo (Dado Bruto) | Métrica | Instrução | Ferramenta / Método |
| :--- | :--- | :--- | :--- |
| `M1.1.1_trufflehog_consolidado.md` | M1.1.1 | I-01 | Trufflehog (achado consolidado e triado; 2.497 falsos positivos categorizados, 0 segredos confirmados) |
| `M1.2.1_bandit_1206.html` | M1.2.1 | I-03 | Bandit (relatório HTML de varredura) |
| `Screenshot 2026-06-12 at 20-47-18 Bandit Report.png` | M1.2.1 | I-03 | Bandit (captura de tela do sumário) |
| `M1.3.1_cookie_attrs_2306.txt` | M1.3.1 | I-05 | Inspeção do produtor do cookie (`API/users/views.py`) |
| `M1.3.2_jwt_tampered_2306.txt` | M1.3.2 | I-06 | Ensaio com token forjado (SimpleJWT) |
| `M2.1.1_ruff_1206.json` | M2.1.1 | I-07 | Ruff (relatório JSON do linter, **coleta da EU2 inválida**: 0 byte) |
| `M2.1.1_ruff_2306.json` | M2.1.1 | I-07 | Ruff (relatório JSON do linter, **recoleta da EU3**: 83 violações) |
| `M2.1.2_imports_2306.txt` | M2.1.2 | I-08 | Listagem bruta de `imports` entre apps |
| `M2.1.2_matriz_2306.txt` | M2.1.2 | I-08 | Matriz consolidada de dependências e ciclos |
| `M2.2_radon_1206.html` | M2.2.1, M2.2.2 | I-09 | Radon (relatório consolidado em HTML) |
| `M2.2_radon_1206.txt` | M2.2.1, M2.2.2 | I-09 | Radon (saída raw em texto do terminal) |
| `M2.3.1_coverage_2306.txt` | M2.3.1 | I-10 | `coverage report` (saída textual) |
| `M2.3.1_coverage_2306.xml` | M2.3.1 | I-10 | `coverage xml` (relatório estruturado) |
| `M2.3.2_frontend_2306.txt` | M2.3.2 | I-11 | Busca por `*.spec.*`/`*.test.*` em `web/src/` e inspeção do `package.json` |
| `M3.1.1_redis_kill_2306.txt` | M3.1.1 | I-12 | Roteiro de queda do Redis (logs + sondagens HTTP) |
| `M3.2.1_websocket_reconnect_2306.txt` | M3.2.1 | I-13 | Inspeção do produtor da conexão `socket.io-client` |
| `M3.2.2_tasks_1206.txt` | M3.2.2 | I-14 | Inspeção de Celery Tasks (evidência textual) |

> **Nota de versionamento:** Devido a restrições de tamanho no GitHub, alguns relatórios extensos em JSON foram particionados (ex: `.aa`, `.ab`). Eles devem ser concatenados localmente caso necessitem ser analisados integralmente.

## Histórico de versão

| Versão | Data       | Descrição | Autor(es) | Revisor(es) |
| :-- | :-- | :-- | :-- | :-- |
| 1.0 | 2026-06-12 | Organização e catalogação dos dados brutos coletados. | Samuel Afonso | Davi Casseb, Letícia Hladczuk |
| 2.0 | 2026-06-23 | Inclusão dos dados brutos das 7 instruções executadas na EU3 (I-05, I-06, I-08, I-10, I-11, I-12, I-13). | Luis Eduardo Castro M Lima, Ana Joyce Guedes | Julia Vitória |

## Referências

1. ISO/IEC 25040:2011. *Systems and software engineering: Systems and software Quality Requirements and Evaluation (SQuaRE): Evaluation process*. International Organization for Standardization, 2011.
2. BASILI, Victor R.; CALDIERA, Gianluigi; ROMBACH, H. Dieter. *The Goal Question Metric Approach*. In: Encyclopedia of Software Engineering. Wiley, 1994.
3. Django Software Foundation. *Deployment checklist e Security in Django*. Disponível em: <https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/>. Acesso em: 12 jun. 2026.
4. PyCQA. *Bandit Documentation*. Disponível em: <https://bandit.readthedocs.io/>. Acesso em: 12 jun. 2026.
5. Radon. *Radon Documentation: Cyclomatic Complexity*. Disponível em: <https://radon.readthedocs.io/>. Acesso em: 12 jun. 2026.
