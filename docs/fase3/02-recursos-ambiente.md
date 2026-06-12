# 2. Especificação dos Recursos e do Ambiente de Avaliação

Esta seção especifica os **recursos** (humanos, de hardware, de software e de dados) e o
**ambiente** necessários para executar as instruções da [seção 1](01-metodo-instrucoes.md)
na [Fase 4](../fase4/index.md). A especificação concretiza a decisão de
**execução local containerizada** registrada na
[Fase 1, §6.2.3](../fase1/06-escopo.md#623-ambiente-de-execucao) e é dimensionada para
suportar os três métodos de avaliação (MA1, MA2 e MA3) e as treze métricas da
[Fase 2, §4](../fase2/04-metricas.md).

## 2.1 Recursos humanos e conhecimento exigido

A avaliação é executada pelos seis integrantes da [equipe T02](../equipe.md), nenhum dos
quais participou do desenvolvimento do AcheiUnB (independência registrada na
[Fase 1, §6.5](../fase1/06-escopo.md#65-limites-de-validade-dos-resultados)). A Tabela 2.1
define os **papéis** e o **nível de conhecimento mínimo** exigido para executar cada
grupo de instruções com segurança e sem comprometer a validade dos dados.

**Tabela 2.1: papéis, instruções atribuídas e conhecimento exigido.**

| Papel | Instruções | Conhecimento exigido (nível) |
|---|---|---|
| **Avaliador de Segurança** (2 pessoas) | I-01 a I-06 | Python/Django intermediário; fundamentos de segurança web (OWASP Top 10, sessão/cookies, JWT/OAuth) intermediários; uso de ferramentas de desenvolvedor do navegador e `curl`. |
| **Avaliador de Manutenibilidade** (2 pessoas) | I-07 a I-11 | Python intermediário; leitura de configuração de linters e `pyproject.toml`; noções de métricas de código (complexidade ciclomática, cobertura) básicas a intermediárias. |
| **Avaliador de Confiabilidade** (2 pessoas) | I-12 a I-14 | Docker/docker-compose intermediário; noções de mensageria (Redis/Celery) e WebSocket básicas; leitura de logs de aplicação. |
| **Segundo observador** (rotativo) | Todas as MA3 | Mesmo nível do avaliador titular do cenário; responsável pela gravação e pelo preenchimento independente do formulário de observação. |
| **Curador de dados** (1 pessoa, acumulado) | Transversal | Git intermediário; responsável por validar nomenclatura, `*.meta.md` e integridade dos dados brutos em `dados/fase4/` antes do *merge*. |

Todos os integrantes possuem domínio da aplicação suficiente (a leitura sistemática da
documentação do AcheiUnB foi realizada na Fase 1) e nível de informática compatível com
estudantes de Engenharia de Software em fim de curso, atendendo ao requisito de
explicitar o conhecimento exigido de usuários/avaliadores.

## 2.2 Hardware

Requisitos por estação de avaliação (cada dupla utiliza ao menos uma estação que os
atenda):

**Tabela 2.2: requisitos de hardware.**

| Item | Mínimo | Recomendado | Justificativa |
|---|---|---|---|
| CPU | 4 núcleos x86-64 | 8 núcleos | O `docker-compose` do AcheiUnB sobe simultaneamente API, worker, beat, PostgreSQL e Redis; os cenários MA3 exigem o sistema completo no ar. |
| Memória RAM | 8 GB | 16 GB | PostgreSQL 15 + Redis 7 + Django/Daphne + SPA em build de desenvolvimento + navegador com ferramentas de desenvolvedor abertas. |
| Armazenamento livre | 20 GB | 40 GB SSD | Imagens Docker, volumes do banco, repositório e dados brutos (incluindo vídeos dos cenários). |
| Rede | Banda larga doméstica | - | Download de imagens/dependências e autenticação MSAL em modo desenvolvimento. |
| Periféricos | Captura de tela com áudio opcional | - | Gravação dos cenários MA3 (M1.3.x, M3.x.x), exigida como dado bruto auditável. |

## 2.3 Software

**Tabela 2.3: software do ambiente de avaliação, com versões fixadas.**

| Categoria | Item | Versão fixada | Uso |
|---|---|---|---|
| Sistema operacional | Linux (Ubuntu 24.04 LTS ou equivalente) | - | Plataforma definida na [Fase 1, §6.2.3](../fase1/06-escopo.md#623-ambiente-de-execucao). |
| Containerização | Docker Engine + Docker Compose v2 | 27.x / v2.x | Execução reproduzível do AcheiUnB (`docker-compose.yml` do próprio projeto). |
| Objeto avaliado | AcheiUnB (`unb-mds/2024-2-AcheiUnB`) | *Commit* fixado em `dados/00-snapshot.md` | Objeto único de todas as medições. |
| Linguagem | Python | 3.12.x (a do contêiner do projeto) | Execução de testes e ferramentas de análise no mesmo runtime do produto. |
| Análise estática - segurança | `trufflehog`, `bandit` | 3.x / 1.7.x | I-01, I-03. |
| Análise estática - manutenibilidade | `ruff`, `radon`, `pytest` + `pytest-cov`, `django-extensions` + `graphviz` | Versões do `pyproject.toml` do AcheiUnB; `radon` 6.x | I-07 a I-10; I-08. |
| Análise dinâmica | Navegador Chromium/Firefox atualizado, `curl`, gravador de tela (OBS Studio ou nativo) | - | I-05, I-06, I-12, I-13. |
| Apoio | Git, planilha (LibreOffice/Google Sheets) para consolidação | - | Versionamento dos dados brutos e tabelas de consolidação. |

!!! info "Regra de fixação de versões"
    Onde o AcheiUnB já fixa a versão (linters, pytest), a avaliação **usa a versão do
    projeto**, pois o objetivo é medir o produto sob o seu próprio contrato de
    qualidade. Ferramentas externas ao projeto (`trufflehog`, `radon`) têm a versão
    instalada registrada no `*.meta.md` de cada coleta ([seção 1.2](01-metodo-instrucoes.md#12-regras-gerais-de-execucao-validas-para-todas-as-instrucoes)).

## 2.4 Massa de dados

O AcheiUnB não possui produção pública nem dados reais disponíveis
([Fase 1, §3.6](../fase1/03-software.md#36-restricoes-e-premissas-tecnicas)); a avaliação
utiliza **massa de dados sintética**, necessária e suficiente para os ensaios dinâmicos:

**Tabela 2.4: massa de dados sintética.**

| Conjunto | Conteúdo | Uso | Justificativa |
|---|---|---|---|
| **Contas de teste** | 2 contas Microsoft de desenvolvimento vinculadas a uma aplicação Azure AD de teste própria da equipe. | Login MSAL (I-05, I-06), chat entre dois usuários (I-12, I-13). | O fluxo de autenticação e o chat exigem usuários autenticados; contas reais da UnB não são utilizadas. |
| **Itens cadastrados** | 20 itens perdidos/achados fictícios (10 por usuário), com 5 imagens sintéticas enviadas via conta Cloudinary de teste. | Estado inicial dos cenários MA3; exercício do CRUD durante I-12. | Garante que a queda do Redis seja observada com a aplicação em uso plausível, e não vazia. |
| **Conversa de chat** | 1 conversa ativa com ao menos 10 mensagens entre as duas contas. | I-12 (chat durante queda do Redis) e I-13 (reconexão). | A métrica M3.2.1 exige tráfego em tempo real para verificar a retomada da comunicação. |
| **Tarefa agendada** | 1 tarefa Celery de teste agendada via Celery Beat. | I-12 (comportamento da fila sob falha). | Permite observar o efeito da indisponibilidade do *broker* sobre tarefas pendentes. |

O *script* de carga (`scripts/seed_avaliacao.py`) e os arquivos de mídia sintéticos são
versionados no repositório da equipe, tornando a massa de dados **reproduzível** por
qualquer auditor.

## 2.5 Procedimento de preparação do ambiente

Procedimento executado **uma única vez por estação**, antes do início da Fase 4, e
verificado pelo curador de dados:

1. Clonar o repositório do AcheiUnB e fazer *checkout* do *commit* fixado
   (`git checkout <hash>`); registrar o hash em `dados/00-snapshot.md`.
2. Criar o arquivo `.env` local a partir do modelo do projeto, com credenciais
   **sintéticas** (Azure AD de teste, Cloudinary de teste); o `.env` **não** é
   versionado.
3. Subir o ambiente: `docker compose up -d --build` e aguardar a saúde de todos os
   serviços (`docker compose ps`).
4. Executar o *smoke test* de aceitação do ambiente: API responde em `/api/`,
   documentação Swagger acessível, login MSAL com conta de teste conclui, mensagem de
   chat trafega entre as duas contas.
5. Executar `scripts/seed_avaliacao.py` para carregar a massa de dados da
   [seção 2.4](#24-massa-de-dados).
6. Instalar as ferramentas de análise nas versões da Tabela 2.3 e registrar
   `pip freeze`/versões em `dados/fase4/ambiente_<estacao>.meta.md`.

Somente após o passo 6 concluído em ao menos duas estações o cronograma da
[seção 3](03-cronograma.md) é disparado.

## 2.6 Restrições e salvaguardas do ambiente

- **Isolamento:** todos os ensaios (inclusive os de manipulação de token, I-06) ocorrem
  em ambiente local, sem qualquer interação com sistemas institucionais reais.
- **Dados pessoais:** nenhuma informação pessoal real é inserida no sistema; toda a
  massa de dados é fictícia.
- **Indisponibilidade de serviços externos:** caso MSAL/Azure AD ou Cloudinary fiquem
  indisponíveis durante uma coleta, a coleta é suspensa e reagendada (a falha de um
  provedor externo **não** é evidência sobre o AcheiUnB e não pode contaminar M3.1.1).
- **Reset entre cenários:** os cenários MA3 (I-12, I-13) partem sempre de
  `docker compose down -v` seguido do procedimento da [seção 2.5](#25-procedimento-de-preparacao-do-ambiente),
  garantindo estado inicial idêntico entre ensaios e entre estações.

## Histórico de versão

| Versão | Data       | Descrição | Autor(es) | Revisor(es) |
| :-- | :-- | :-- | :-- | :-- |
| 1.0 | 2026-06-12 | Especificação de recursos, ambiente, massa de dados e procedimento de preparação. | Samuel Afonso, Ana Joyce | Davi Casseb, Letícia Hladczuk |

## Referências

1. ISO/IEC 25040:2011. *Systems and software engineering: Systems and software Quality Requirements and Evaluation (SQuaRE): Evaluation process*. International Organization for Standardization, 2011.
2. AcheiUnB. *Repositório do projeto da disciplina MDS/UnB 2024-2*. Disponível em: <https://github.com/unb-mds/2024-2-AcheiUnB>. Acesso em: 12 jun. 2026.
3. Docker Inc. *Docker Compose Documentation*. Disponível em: <https://docs.docker.com/compose/>. Acesso em: 12 jun. 2026.
