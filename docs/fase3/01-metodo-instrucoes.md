# 1. Definição do Método e Repetibilidade das Instruções

Esta seção define e justifica os **métodos de avaliação** que serão empregados na
[Fase 4](../fase4/index.md) e fornece, para **cada métrica** especificada na
[Fase 2, §4](../fase2/04-metricas.md), as **instruções passo a passo** para obtenção das
medidas. O objetivo é garantir **repetibilidade** (o mesmo avaliador obtém o mesmo
resultado em execuções sucessivas) e **reprodutibilidade** (um avaliador diferente obtém
o mesmo resultado seguindo as instruções), conforme exigido por processos formais de
avaliação da família SQuaRE (ISO/IEC 25040).

## 1.1 Métodos de avaliação adotados

A avaliação combina **três métodos complementares**, escolhidos em função do tipo de
evidência exigido por cada métrica da Fase 2 e do contexto registrado na Fase 1 (MVP
acadêmico, sem produção pública, executável localmente via Docker -
[Fase 1, §3.6](../fase1/03-software.md#36-restricoes-e-premissas-tecnicas)):

**Tabela 1.1: métodos de avaliação e justificativa.**

| Método | Descrição | Métricas atendidas | Justificativa |
|---|---|---|---|
| **MA1. Análise estática automatizada** | Execução de ferramentas de análise sobre o código-fonte, sem executar o sistema. Saída em formato legível por máquina (JSON/relatório), arquivada como dado bruto. | M1.1.1, M1.2.1, M2.1.1, M2.1.2, M2.2.1, M2.2.2, M2.3.1 | É o método mais barato, objetivo e reprodutível; reaproveita o ferramental já adotado no CI do AcheiUnB (Bandit, Ruff, Coverage), conforme o princípio de reaproveitamento da [Fase 1, §6.1](../fase1/06-escopo.md#61-principios-de-delimitacao). |
| **MA2. Inspeção documental guiada por checklist** | Leitura dirigida de arquivos de código/configuração contra uma lista de verificação fechada, com registro item a item (atende / não atende / não se aplica + evidência). | M1.1.2, M1.2.2, M2.3.2, M3.2.2 | Algumas evidências (ex.: configuração do `settings.py`, presença de `retry` em tarefas Celery) não são plenamente capturáveis por ferramenta; o checklist fechado elimina a subjetividade da inspeção livre. |
| **MA3. Ensaio dinâmico em laboratório (cenário controlado)** | Execução do sistema em Docker com roteiro de cenário pré-definido (estado inicial, ação de perturbação, observação, registro em vídeo/log). | M1.3.1, M1.3.2, M3.1.1, M3.2.1 | Métricas de autenticação em tempo de execução e de tolerância a falhas exigem o sistema em operação; o roteiro fixo e a gravação garantem auditabilidade ([premissa de dados auditáveis](../index.md) do plano da disciplina). |

A correspondência completa métrica → método → instrução é dada na Tabela 1.2, que serve
de **índice de rastreabilidade** entre a especificação da Fase 2 e este plano (critério
F3-C8 da rubrica).

**Tabela 1.2: mapa métrica → método → instrução de coleta.**

| Métrica (Fase 2, §4) | Questão | Método | Instrução |
|---|---|---|---|
| M1.1.1 - Segredos no código-fonte | Q1.1 | MA1 | [I-01](#i-01-m111-varredura-de-segredos) |
| M1.1.2 - `.env` no `.gitignore` | Q1.1 | MA2 | [I-02](#i-02-m112-inspecao-do-gitignore) |
| M1.2.1 - Vulnerabilidades Bandit (média/alta) | Q1.2 | MA1 | [I-03](#i-03-m121-execucao-do-bandit) |
| M1.2.2 - Checklist de configuração Django | Q1.2 | MA2 | [I-04](#i-04-m122-checklist-de-configuracao-django) |
| M1.3.1 - Atributos do *cookie* de sessão | Q1.3 | MA3 | [I-05](#i-05-m131-inspecao-dinamica-do-cookie-de-sessao) |
| M1.3.2 - Rejeição de JWT manipulado | Q1.3 | MA3 | [I-06](#i-06-m132-ensaio-de-manipulacao-de-token-jwt) |
| M2.1.1 - Violações Ruff | Q2.1 | MA1 | [I-07](#i-07-m211-execucao-do-ruff) |
| M2.1.2 - Dependências circulares entre *apps* | Q2.1 | MA1 | [I-08](#i-08-m212-mapa-de-dependencias-entre-apps) |
| M2.2.1 / M2.2.2 - Complexidade ciclomática | Q2.2 | MA1 | [I-09](#i-09-m221-e-m222-complexidade-ciclomatica-com-radon) |
| M2.3.1 - Cobertura de testes do *backend* | Q2.3 | MA1 | [I-10](#i-10-m231-cobertura-de-testes-do-backend) |
| M2.3.2 - Arquivos de teste no *frontend* | Q2.3 | MA2 | [I-11](#i-11-m232-contagem-de-testes-no-frontend) |
| M3.1.1 - Comportamento após queda do Redis | Q3.1 | MA3 | [I-12](#i-12-m311-cenario-de-queda-do-redis) |
| M3.2.1 - Reconexão automática do WebSocket | Q3.2 | MA3 | [I-13](#i-13-m321-cenario-de-reconexao-do-websocket) |
| M3.2.2 - Política de `retry` no Celery | Q3.2 | MA2 | [I-14](#i-14-m322-inspecao-de-retry-em-tarefas-celery) |

## 1.2 Regras gerais de execução (válidas para todas as instruções)

1. **Snapshot fixo.** Todas as medições incidem sobre o *commit* fixado no início da
   execução, registrado em `dados/00-snapshot.md` (hash completo, data e comando de
   *checkout*). Nenhuma instrução pode ser executada sobre `main` flutuante
   ([Fase 1, §1.4](../fase1/01-proposito.md#14-cenario-de-aplicacao)).
2. **Dados brutos primeiro.** A saída integral de cada ferramenta/cenário é salva no
   diretório `dados/fase4/` do repositório da equipe **antes** de qualquer
   consolidação, com o nome padronizado `<metrica>_<AAAA-MM-DD>.<ext>`
   (ex.: `M1.2.1_bandit_2026-06-20.json`).
3. **Registro de proveniência.** Cada arquivo de dado bruto é acompanhado de um
   cabeçalho/arquivo `*.meta.md` com: executor, data/hora, versão da ferramenta,
   comando exato executado e hash do *snapshot*.
4. **Dupla execução.** Toda instrução MA1 é executada **duas vezes** pelo mesmo
   avaliador; divergência entre execuções invalida a coleta e dispara investigação
   (controle de repetibilidade). Instruções MA3 são executadas por um avaliador e
   **assistidas/gravadas** por um segundo (controle de reprodutibilidade).
5. **Sem correção do objeto.** O avaliador **não altera** o código do AcheiUnB. Ajustes
   estritamente necessários para executar o ambiente (ex.: criação de `.env` local)
   são documentados no `*.meta.md` e não contam como modificação do objeto avaliado.
6. **Julgamento adiado.** A comparação dos valores com os níveis de pontuação da
   [Fase 2, §5](../fase2/05-niveis-pontuacao.md) ocorre apenas na Fase 4; durante a
   coleta registra-se somente o valor medido.

## 1.3 Instruções por métrica

As instruções a seguir assumem o ambiente preparado conforme a
[seção 2](02-recursos-ambiente.md). Comandos são executados na raiz do repositório
clonado do AcheiUnB, salvo indicação contrária.

### I-01 (M1.1.1): varredura de segredos

1. Executar a varredura automatizada no *snapshot*:
   `trufflehog git file://. --branch <commit-fixado> --json > dados/fase4/M1.1.1_trufflehog_<data>.json`
2. Executar a inspeção manual complementar: abrir `API/AcheiUnB/settings.py` e
   registrar, em formulário próprio, toda atribuição literal de `SECRET_KEY`, senhas,
   tokens ou chaves de API (arquivo, linha, tipo do segredo).
3. Consolidar o **valor da métrica** como o número de segredos **distintos** confirmados
   (a mesma chave reportada duas vezes conta uma vez). Falsos positivos do `trufflehog`
   são descartados com justificativa escrita no formulário.
4. **Saída registrada:** JSON do `trufflehog`, formulário de inspeção preenchido e o
   inteiro consolidado.

### I-02 (M1.1.2): inspeção do `.gitignore`

1. Abrir o(s) arquivo(s) `.gitignore` da raiz e de `API/`.
2. Verificar a presença de padrão que ignore arquivos de ambiente (`.env`, `*.env`,
   `.env.*`). Registrar o trecho exato encontrado (ou sua ausência).
3. Verificação cruzada: executar `git ls-files | grep -i "\.env"` e registrar a saída
   (um `.env` versionado contradiz o `.gitignore` e deve ser anotado como observação
   para a Q1.1).
4. **Saída registrada:** valor booleano (Sim/Não) + evidências textuais.

### I-03 (M1.2.1): execução do Bandit

1. Executar: `bandit -r API/ -f json -o dados/fase4/M1.2.1_bandit_<data>.json`
   (mesma raiz de varredura usada pelo CI do AcheiUnB).
2. Filtrar os achados com `issue_severity` igual a `MEDIUM` ou `HIGH`.
3. Registrar o **valor da métrica**: contagem de achados após o filtro. Achados
   duplicados (mesmo teste, mesmo arquivo, mesma linha) contam uma vez.
4. **Saída registrada:** JSON integral + planilha de consolidação com o filtro aplicado.

### I-04 (M1.2.2): checklist de configuração Django

1. Utilizar o checklist fechado de 12 itens definido em
   `dados/instrumentos/checklist-django.md` (derivado da documentação oficial de
   *deployment* do Django e do *security middleware*), cobrindo no mínimo: `DEBUG`,
   `ALLOWED_HOSTS`, `SECURE_SSL_REDIRECT`, `SESSION_COOKIE_SECURE`,
   `CSRF_COOKIE_SECURE`, `SECURE_HSTS_SECONDS`, `X_FRAME_OPTIONS`,
   `SECURE_CONTENT_TYPE_NOSNIFF`, configuração de CORS (origens explícitas),
   `CsrfViewMiddleware` ativo, `SecurityMiddleware` ativo e ausência de
   `CORS_ALLOW_ALL_ORIGINS=True`.
2. Para cada item, registrar: **atende / não atende / não se aplica**, com a linha do
   `settings.py` (ou arquivo de configuração) como evidência.
3. Executar adicionalmente `python manage.py check --deploy` no contêiner e arquivar a
   saída como evidência de apoio.
4. **Valor da métrica:** percentual de itens "atende" sobre os itens aplicáveis.
5. **Saída registrada:** checklist preenchido + saída do `check --deploy`.

### I-05 (M1.3.1): inspeção dinâmica do *cookie* de sessão

1. Subir o ambiente (`docker compose up`) e realizar um login completo pelo fluxo
   MSAL com a conta de teste definida na [seção 2.4](02-recursos-ambiente.md#24-massa-de-dados).
2. Com as ferramentas de desenvolvedor do navegador (aba *Network*), capturar a resposta
   HTTP que define o *cookie* de sessão JWT (`Set-Cookie`).
3. Registrar a presença/ausência dos atributos `HttpOnly`, `Secure` e `SameSite`
   (e seu valor), com *screenshot* do cabeçalho.
4. **Valor da métrica:** número de atributos faltantes (0, 1 ou >1), conforme os níveis
   da [Fase 2, §5](../fase2/05-niveis-pontuacao.md).
5. **Saída registrada:** *screenshot* + cabeçalho bruto copiado para arquivo de texto +
   vídeo curto da sessão de teste.

### I-06 (M1.3.2): ensaio de manipulação de token JWT

1. A partir da sessão autenticada de I-05, copiar o token JWT emitido.
2. Decodificar o *payload* (ex.: `jwt.io` em modo local ou `pyjwt` sem verificação),
   alterar um campo de identidade (ex.: `user_id`) e **reassinar com chave incorreta**
   (ou manter a assinatura original com *payload* alterado).
3. Reenviar uma requisição autenticada a um *endpoint* protegido (ex.: `GET /api/`)
   usando o token manipulado, via `curl`, registrando requisição e resposta completas.
4. **Valor da métrica:** `Válida` se o sistema **rejeitar** o token manipulado
   (HTTP 401/403); `Inválida` se aceitar.
5. **Saída registrada:** *script*/comandos utilizados, requisições e respostas brutas.

!!! warning "Limite ético do ensaio"
    O ensaio I-06 ocorre **exclusivamente** no ambiente local da equipe, com contas
    sintéticas e sem qualquer interação com instâncias ou credenciais reais da UnB ou
    da Microsoft.

### I-07 (M2.1.1): execução do Ruff

1. Executar com a configuração **do próprio projeto** (`pyproject.toml` do AcheiUnB),
   sem regras adicionais: `ruff check API/ --output-format json > dados/fase4/M2.1.1_ruff_<data>.json`
2. **Valor da métrica:** número total de violações reportadas.
3. **Saída registrada:** JSON integral + versão do Ruff utilizada (deve ser a mesma
   fixada no CI do AcheiUnB; divergência é registrada no `*.meta.md`).

### I-08 (M2.1.2): mapa de dependências entre *apps*

1. No contêiner do *backend*, gerar o grafo de modelos/dependências com
   `django-extensions`: `python manage.py graph_models -a -o dados/fase4/M2.1.2_grafo_<data>.png`
2. Complementar com análise de *imports* entre *apps* (`users`, `chat`, `reports`,
   `support`): `grep -rn "from API\.\|import API\." API/ > dados/fase4/M2.1.2_imports_<data>.txt`
   e montar a matriz de dependência app × app.
3. **Valor da métrica:** número de **ciclos** identificados na matriz (A depende de B e
   B depende de A, direta ou transitivamente).
4. **Saída registrada:** imagem do grafo, listagem de *imports* e matriz preenchida.

### I-09 (M2.2.1 e M2.2.2): complexidade ciclomática com Radon

1. Executar: `radon cc API/ -s -j > dados/fase4/M2.2_radon_<data>.json`
2. Calcular **M2.2.1** (média da complexidade por função/método em todo o *backend*) e
   **M2.2.2** (contagem de funções/métodos com complexidade > 10) a partir do JSON, por
   *script* de consolidação versionado em `scripts/consolida_radon.py`.
3. **Saída registrada:** JSON do Radon + *script* + tabela consolidada por módulo
   (insumo direto para a decisão D1 de priorização de *backlog*).

### I-10 (M2.3.1): cobertura de testes do *backend*

1. No contêiner do *backend*, executar a suíte com cobertura:
   `pytest --cov=API --cov-report=xml:dados/fase4/M2.3.1_coverage_<data>.xml --cov-report=term`
2. Registrar o percentual de **line coverage** total e a tabela por módulo.
3. Em caso de testes falhando por dependência de ambiente, registrar quais e por quê;
   o percentual reportado deve indicar explicitamente a base de testes executada.
4. **Saída registrada:** XML de cobertura + saída de terminal arquivada.

### I-11 (M2.3.2): contagem de testes no *frontend*

1. Executar a busca padronizada em `web/`:
   `find web/src -type f \( -name "*.spec.*" -o -name "*.test.*" \) | tee dados/fase4/M2.3.2_frontend_<data>.txt`
2. Verificar também a existência de diretórios `tests/`/`__tests__/` e de *script* de
   teste no `web/package.json`.
3. **Valor da métrica:** número de arquivos de teste encontrados.
4. **Saída registrada:** listagem da busca + trecho relevante do `package.json`.

### I-12 (M3.1.1): cenário de queda do Redis

Roteiro de cenário (executar com gravação de tela ativa):

1. **Estado inicial:** sistema completo no ar (`docker compose up`), dois usuários de
   teste logados, conversa de chat ativa entre eles e uma tarefa Celery agendada.
2. **Perturbação:** parar o contêiner do Redis: `docker compose stop redis`.
3. **Observação (10 min):** exercitar, nesta ordem: (a) envio de mensagem no chat;
   (b) navegação e operações CRUD na API que não dependem do Redis; (c) logs de
   `api`, `worker` e `beat` (`docker compose logs -f`).
4. **Classificação:** atribuir o nível ordinal 1-4 definido na
   [Fase 2, §5](../fase2/05-niveis-pontuacao.md) (crash total / erro 500 / erro
   amigável / degradação graciosa), justificando com as evidências observadas.
5. **Restauração:** `docker compose start redis` e registrar se o sistema retorna ao
   normal sem intervenção adicional.
6. **Saída registrada:** vídeo do cenário, logs exportados e formulário de observação.

### I-13 (M3.2.1): cenário de reconexão do WebSocket

1. **Estado inicial:** chat ativo entre dois usuários de teste (mesmo setup de I-12).
2. **Perturbação:** interromper a conectividade do cliente por 30 segundos (modo
   *offline* nas ferramentas de desenvolvedor do navegador) **ou** reiniciar o serviço
   de WebSocket (`docker compose restart api`), executando ambas as variantes em
   ensaios separados.
3. **Observação:** após restabelecer a rede/serviço, aguardar até 60 segundos **sem
   recarregar a página** e verificar se o cliente reconecta e volta a receber mensagens.
4. **Valor da métrica:** `Sim` (reconexão automática em até 60 s) ou `Não`.
5. **Saída registrada:** vídeo, console do navegador exportado e formulário de
   observação para cada variante.

### I-14 (M3.2.2): inspeção de `retry` em tarefas Celery

1. Localizar todas as definições de tarefa: `grep -rn "@shared_task\|@app.task" API/ | tee dados/fase4/M3.2.2_tasks_<data>.txt`
2. Para cada tarefa encontrada, inspecionar e registrar em formulário: nome, módulo,
   presença de `autoretry_for`/`retry_backoff`/`max_retries`/chamada explícita a
   `self.retry()` ou tratamento `try...except` com reenfileiramento.
3. **Valor da métrica:** `Sim` se as tarefas **críticas** (notificações e *matching*
   de itens, conforme [Fase 1, §3.3.4](../fase1/03-software.md#334-servicos-auxiliares))
   possuírem política de `retry`; `Não` caso contrário.
4. **Saída registrada:** listagem do `grep` + formulário por tarefa.

## 1.4 Garantias de repetibilidade e reprodutibilidade

| Mecanismo | Como atua |
|---|---|
| *Snapshot* fixado por hash | Elimina variação do objeto medido entre execuções. |
| Versões de ferramentas fixadas ([seção 2.3](02-recursos-ambiente.md#23-software)) | Elimina variação do instrumento de medição. |
| Comandos literais e checklists fechados | Elimina ambiguidade de procedimento; o avaliador não decide "como" medir durante a coleta. |
| Dupla execução (MA1) e segundo observador (MA3) | Detecta variação residual e erro humano. |
| Dados brutos + `*.meta.md` versionados | Permitem auditoria externa e reexecução por terceiros (premissa de dados auditáveis da disciplina). |

## Histórico de versão

| Versão | Data       | Descrição | Autor(es) | Revisor(es) |
| :-- | :-- | :-- | :-- | :-- |
| 1.0 | 2026-06-12 | Definição dos métodos de avaliação e das instruções de coleta por métrica. | Davi Casseb, Letícia Hladczuk | Julia Vitória, Luis Lima |

## Referências

1. ISO/IEC 25040:2011. *Systems and software engineering: Systems and software Quality Requirements and Evaluation (SQuaRE): Evaluation process*. International Organization for Standardization, 2011.
2. BASILI, Victor R.; CALDIERA, Gianluigi; ROMBACH, H. Dieter. *The Goal Question Metric Approach*. In: Encyclopedia of Software Engineering. Wiley, 1994.
3. Django Software Foundation. *Deployment checklist e Security in Django*. Disponível em: <https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/>. Acesso em: 12 jun. 2026.
4. PyCQA. *Bandit Documentation*. Disponível em: <https://bandit.readthedocs.io/>. Acesso em: 12 jun. 2026.
5. Radon. *Radon Documentation: Cyclomatic Complexity*. Disponível em: <https://radon.readthedocs.io/>. Acesso em: 12 jun. 2026.
