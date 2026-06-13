# Dados Brutos

Os dados brutos coletados na execução da avaliação estão armazenados no diretório `docs/fase4/Dados_Brutos`. Para garantir a rastreabilidade e a transparência (critério F4-C2), a Tabela 2.1 abaixo cataloga todos os artefatos gerados, vinculando-os à métrica correspondente e à instrução de coleta que os originou.

**Tabela 2.1: Catálogo de dados brutos coletados.**

| Arquivo (Dado Bruto) | Métrica | Instrução | Ferramenta / Método |
| :--- | :--- | :--- | :--- |
| `M1.1.1_trufflehog_1206.json.aa` a `.ae` | M1.1.1 | I-01 | Trufflehog (relatório JSON dividido em partes devido ao tamanho) |
| `M1.2.1_bandit_1206.html` | M1.2.1 | I-03 | Bandit (relatório HTML de varredura) |
| `Screenshot 2026-06-12 at 20-47-18 Bandit Report.png` | M1.2.1 | I-03 | Bandit (captura de tela do sumário) |
| `M2.1.1_ruff_1206.json` | M2.1.1 | I-07 | Ruff (relatório JSON do linter) |
| `M2.2_radon_1206.html` | M2.2.1, M2.2.2 | I-09 | Radon (relatório consolidado em HTML) |
| `M2.2_radon_1206.txt` | M2.2.1, M2.2.2 | I-09 | Radon (saída raw em texto do terminal) |
| `M3.2.2_tasks_1206.txt` | M3.2.2 | I-14 | Inspeção de Celery Tasks (evidência textual) |

> **Nota de versionamento:** Devido a restrições de tamanho no GitHub, alguns relatórios extensos em JSON foram particionados (ex: `.aa`, `.ab`). Eles devem ser concatenados localmente caso necessitem ser analisados integralmente.

## Histórico de versão

| Versão | Data       | Descrição | Autor(es) | Revisor(es) |
| :-- | :-- | :-- | :-- | :-- |
| 1.0 | 2026-06-12 | Organização e catalogação dos dados brutos coletados. | Samuel Afonso | Davi Casseb, Letícia Hladczuk |

## Referências

1. ISO/IEC 25040:2011. *Systems and software engineering: Systems and software Quality Requirements and Evaluation (SQuaRE): Evaluation process*. International Organization for Standardization, 2011.
2. BASILI, Victor R.; CALDIERA, Gianluigi; ROMBACH, H. Dieter. *The Goal Question Metric Approach*. In: Encyclopedia of Software Engineering. Wiley, 1994.
3. Django Software Foundation. *Deployment checklist e Security in Django*. Disponível em: <https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/>. Acesso em: 12 jun. 2026.
4. PyCQA. *Bandit Documentation*. Disponível em: <https://bandit.readthedocs.io/>. Acesso em: 12 jun. 2026.
5. Radon. *Radon Documentation: Cyclomatic Complexity*. Disponível em: <https://radon.readthedocs.io/>. Acesso em: 12 jun. 2026.
