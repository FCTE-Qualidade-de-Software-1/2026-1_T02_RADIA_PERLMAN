# Obtenção de Medidas

---

### Segurança e Configurações (M1)

* **I-01 (M1.1.1) | Varredura de Segredos:**
* **Ferramenta:** `trufflehog`
* **Ação:** Varredura realizada na branch `main` do repositório `2024-2-AcheiUnB`.
* **Resultado:** O relatório completo foi gerado e exportado no formato JSON para o diretório de dados (`M1.1.1_trufflehog_1206.json`).


* **I-02 (M1.1.2) | Inspeção do `.gitignore`:**
* **Ação:** Verificação de rastreamento indevido de variáveis de ambiente.
* **Resultado:** **Aprovado.** O comando `git ls-files | grep -i ".env"` não retornou resultados, confirmando que nenhum arquivo `.env` está exposto no repositório.


* **I-03 (M1.2.1) | Análise Estática de Segurança:**
* **Ferramenta:** `Bandit`
* **Resultado:** Os apontamentos de segurança foram gerados e podem ser consultados no relatório visual em anexo (*Bandit Report*).


* **I-04 (M1.2.2) | Checklist de Configuração Django:**
* **Ação:** Validação das configurações de segurança em ambiente de deploy.
* **Resultado:** **Atenção Necessária.** Foram identificados 6 alertas críticos que precisam de correção para produção:
* **HSTS e SSL:** Ausência de configuração do `SECURE_HSTS_SECONDS` e `SECURE_SSL_REDIRECT`.
* **Cookies:** `SESSION_COOKIE_SECURE` e `CSRF_COOKIE_SECURE` não estão configurados como `True`.
* **Chave de Segurança:** A `SECRET_KEY` atual é fraca/gerada automaticamente e precisa ser substituída por um valor longo e aleatório.
* **Modo Debug:** O parâmetro `DEBUG` está configurado como `True`, o que é um risco grave em produção.




* **I-05 (M1.3.1) | Inspeção Dinâmica do Cookie de Sessão:** **[Pendente]**
* **I-06 (M1.3.2) | Ensaio de Manipulação de Token JWT:** **[Pendente]**

### Qualidade de Código e Arquitetura (M2)

* **I-07 (M2.1.1) | Linter e Formatação:**
* **Ferramenta:** `Ruff`
* **Resultado:** **Excelente.** Nenhuma violação de estilo ou qualidade foi reportada no arquivo de log (`M2.1.1_ruff_1206.json`).


* **I-08 (M2.1.2) | Mapa de Dependências entre Apps:** **[Pendente]**
* **I-09 (M2.2.1 e M2.2.2) | Complexidade Ciclomática:**
* **Ferramenta:** `Radon`
* **Resultado:** **Excelente.** Foram analisados 350 blocos de código (classes, funções e métodos), alcançando uma **nota média A** (score de 2.75).


* **I-10 (M2.3.1) | Cobertura de Testes (Backend):** **[Pendente]**
* **I-11 (M2.3.2) | Contagem de Testes (Frontend):** **[Pendente]**

### Resiliência e Tolerância a Falhas (M3)

* **I-12 (M3.1.1) | Cenário de Queda do Redis:** **[Pendente]**
* **I-13 (M3.2.1) | Cenário de Reconexão do WebSocket:** **[Pendente]**
* **I-14 (M3.2.2) | Inspeção de `Retry` em Tarefas Celery:**
* **Ação:** Mapeamento de tarefas assíncronas decoradas com `@shared_task` ou `@app.task` nas APIs de `chat` e `users`.
* **Resultado:** **Atenção Necessária.** Foram identificadas 13 tarefas distribuídas pelo sistema, porém **nenhuma delas** possui uma política de *retry* configurada para lidar com falhas transitórias.



---

## Histórico de versão

| Versão | Data       | Descrição | Autor(es) | Revisor(es) |
| :-- | :-- | :-- | :-- | :-- |
| 1.0 | 2026-06-12 | Cronograma de execução da avaliação com marcos, distribuição de atividades e contingências. | Julia Vitória, Luis Lima | Ana Joyce, Samuel Afonso |

## Referências

1. ISO/IEC 25040:2011. *Systems and software engineering: Systems and software Quality Requirements and Evaluation (SQuaRE): Evaluation process*. International Organization for Standardization, 2011.
2. BASILI, Victor R.; CALDIERA, Gianluigi; ROMBACH, H. Dieter. *The Goal Question Metric Approach*. In: Encyclopedia of Software Engineering. Wiley, 1994.
3. Django Software Foundation. *Deployment checklist e Security in Django*. Disponível em: <https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/>. Acesso em: 12 jun. 2026.
4. PyCQA. *Bandit Documentation*. Disponível em: <https://bandit.readthedocs.io/>. Acesso em: 12 jun. 2026.
5. Radon. *Radon Documentation: Cyclomatic Complexity*. Disponível em: <https://radon.readthedocs.io/>. Acesso em: 12 jun. 2026.
