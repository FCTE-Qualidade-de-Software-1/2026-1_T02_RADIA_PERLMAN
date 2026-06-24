# Obtenção de Medidas

!!! note "Snapshot do objeto avaliado"
    Todas as medições desta seção incidem sobre o **commit fixado**
    `e91773380c5259007d748d85e998a27362537339` (branch `main` do `unb-mds/2024-2-AcheiUnB`),
    registrado em [`dados/00-snapshot.md`](https://github.com/FCTE-Qualidade-de-Software-1/2026-1_T02_RADIA_PERLMAN/blob/main/dados/00-snapshot.md). A fixação por hash
    garante a repetibilidade e a auditoria exigidas pela Fase 3.

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




* **I-05 (M1.3.1) | Inspeção do Cookie de Sessão JWT:**
* **Método:** MA3 ajustado para inspeção do produtor do cookie (login real exige MSAL com credenciais da UnB; ver `Limites` da Fase 4).
* **Evidência:** `API/users/views.py` linhas 517-525 (callback de login Microsoft).
* **Resultado:** **Bom.** Os três atributos críticos estão presentes: `httponly=True`, `secure=True`, `samesite="Strict"`. Valor da métrica: **0 atributos faltantes** (`M1.3.1_cookie_attrs_2306.txt`).


* **I-06 (M1.3.2) | Ensaio de Manipulação de Token JWT:**
* **Ação:** Geração de token forjado (payload válido + assinatura HS256 com chave incorreta) e envio para o endpoint protegido `/api/auth/user/`.
* **Resultado:** **Bom (Válida).** O sistema rejeitou o token com `HTTP 401 Unauthorized` e mensagem `"Token is invalid"` (`M1.3.2_jwt_tampered_2306.txt`). O fluxo SimpleJWT (`SIGNING_KEY=SECRET_KEY`, `ALGORITHM=HS256`) detecta a divergência de assinatura.


### Qualidade de Código e Arquitetura (M2)

* **I-07 (M2.1.1) | Linter e Formatação:**
* **Ferramenta:** `Ruff`
* **Resultado da EU2:** Coleta inválida. O arquivo `M2.1.1_ruff_1206.json` foi gravado com **0 byte** por falha silenciosa na inicialização do `.ruff_cache`, invalidando a métrica e desativando o uso de M2.1.1 no julgamento daquela entrega.
* **Recoleta na EU3:** Executado com `ruff check API/ --output-format json --no-cache` após limpeza do cache. **Resultado: Ruim.** **83 violações** ativas, predominando `PLR6301` (57 ocorrências, *no-self-use*) e `PLC0415` (12, *import-outside-top-level*); demais: `PLW0717`, `F401`, `PLW1514`, `PLC1901`, `PLR2044`. Arquivo: `M2.1.1_ruff_2306.json`. Critério da Fase 2 §5: contagem > 20 → **Ruim**.


* **I-08 (M2.1.2) | Mapa de Dependências entre Apps:**
* **Ação:** Análise estática de `imports` entre os módulos `chat`, `users`, `reports`, `support` (excluindo testes e *migrations*).
* **Resultado:** **Atenção Necessária.** Identificados **2 ciclos** de dependência direta: `chat <-> users` e `users <-> reports`. O módulo `support` não tem dependências de saída nem de entrada (`M2.1.2_imports_2306.txt`, `M2.1.2_matriz_2306.txt`).


* **I-09 (M2.2.1 e M2.2.2) | Complexidade Ciclomática:**
* **Ferramenta:** `Radon`
* **Resultado:** **Regular (boa média, com pontos de atenção).** Foram analisados 350 blocos de código (classes, funções e métodos), alcançando uma **nota média A** (score de 2.75 - M2.2.1). Entretanto, **5 blocos** possuem complexidade ciclomática > 10 (grau C: `UserProfileView`, `UserListView`, `UserProfileView.get`, `UserListView.get` e `ReportViewSet._get_reported_user` - M2.2.2). Pelo critério conjunto da Fase 2 §5 (média < 5 **e** contagem(>10) entre 1 e 5), o julgamento combinado é **Regular**, conforme detalhado na [análise §3.3](03-analise-resposta-gqm.md).


* **I-10 (M2.3.1) | Cobertura de Testes (Backend):**
* **Ferramenta:** `coverage` + `pytest` no contêiner `api-web-1`.
* **Resultado:** **Bom.** Cobertura total de linhas: **83%** sobre 2.389 linhas instrumentadas (`M2.3.1_coverage_2306.txt`, `M2.3.1_coverage_2306.xml`). 108 de 109 testes passaram (uma falha em `users/tests/test_signals.py::test_send_welcome_email_on_first_login` por *mismatch* de *mock*, sem impacto estrutural).


* **I-11 (M2.3.2) | Contagem de Testes (Frontend):**
* **Ação:** Busca por `*.spec.*` e `*.test.*` em `web/src/`; inspeção de `web/package.json`.
* **Resultado:** **Ruim.** **0 arquivos de teste** encontrados. Não há `script` de teste no `package.json` (`scripts` contém apenas `dev`, `build`, `build:vm`, `preview`, `format`) nem dependências de teste em `devDependencies` (sem `vitest`, `jest`, `@testing-library/*`).


### Resiliência e Tolerância a Falhas (M3)

* **I-12 (M3.1.1) | Cenário de Queda do Redis:**
* **Ação:** `docker compose stop redis` por 3 minutos com sondagem de endpoints REST, e `docker compose start redis` para restauração.
* **Resultado:** **Bom (Degradação Graciosa).** Durante a queda, todos os endpoints REST testados (`/api/items/`, `/api/categories/`, `/api/locations/`, `/api/brands/`, `/admin/login/`) responderam **HTTP 200 OK**. Nenhuma exceção do Django nos logs; nenhum HTTP 500 emitido. Após `docker compose start redis`, o sistema retornou ao normal sem intervenção (`M3.1.1_redis_kill_2306.txt`). A funcionalidade de chat (via Channels com layer no Redis) fica temporariamente indisponível, mas isso não derruba a API.


* **I-13 (M3.2.1) | Cenário de Reconexão do WebSocket:**
* **Método:** MA3 ajustado para inspeção do produtor da conexão (cliente real exige login MSAL; ver `Limites` da Fase 4).
* **Evidência:** `web/src/views/Chats.vue` linhas 211-216 e `web/src/views/Message.vue` linhas 168-173 instanciam `socket.io-client` via `io(WS_URL, { transports: ["websocket"] })`.
* **Resultado:** **Bom (Sim).** A biblioteca `socket.io-client` tem **reconexão automática habilitada por padrão** (backoff exponencial, `reconnection=true`, `reconnectionAttempts=Infinity`). O código não desabilita esses *defaults* (`M3.2.1_websocket_reconnect_2306.txt`).


* **I-14 (M3.2.2) | Inspeção de `Retry` em Tarefas Celery:**
* **Ação:** Mapeamento de tarefas assíncronas decoradas com `@shared_task` ou `@app.task` nas APIs de `chat` e `users`.
* **Resultado:** **Atenção Necessária.** Foram identificadas 13 tarefas distribuídas pelo sistema, porém **nenhuma delas** possui uma política de *retry* configurada para lidar com falhas transitórias.



---

## Histórico de versão

| Versão | Data       | Descrição | Autor(es) | Revisor(es) |
| :-- | :-- | :-- | :-- | :-- |
| 1.0 | 2026-06-12 | Execução das instruções de coleta e registro dos resultados das medições. | Samuel Afonso | Davi Casseb, Letícia Hladczuk |
| 2.0 | 2026-06-23 | Execução das 7 instruções pendentes (I-05, I-06, I-08, I-10, I-11, I-12, I-13) na EU3, com dados brutos arquivados em `Dados_Brutos/`. | Luis Eduardo Castro M Lima, Davi Casseb | Letícia Hladczuk |

## Referências

1. ISO/IEC 25040:2011. *Systems and software engineering: Systems and software Quality Requirements and Evaluation (SQuaRE): Evaluation process*. International Organization for Standardization, 2011.
2. BASILI, Victor R.; CALDIERA, Gianluigi; ROMBACH, H. Dieter. *The Goal Question Metric Approach*. In: Encyclopedia of Software Engineering. Wiley, 1994.
3. Django Software Foundation. *Deployment checklist e Security in Django*. Disponível em: <https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/>. Acesso em: 12 jun. 2026.
4. PyCQA. *Bandit Documentation*. Disponível em: <https://bandit.readthedocs.io/>. Acesso em: 12 jun. 2026.
5. Radon. *Radon Documentation: Cyclomatic Complexity*. Disponível em: <https://radon.readthedocs.io/>. Acesso em: 12 jun. 2026.
