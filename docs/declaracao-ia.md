# Declaração de uso de IA

Esta seção declara, de forma explícita e auditável, o uso de ferramentas de Inteligência
Artificial generativa pela equipe T02 RADIA PERLMAN na produção dos artefatos das Entregas
da Unidade 1 (EU1) e da Unidade 2 (EU2). A declaração segue o princípio de **transparência
sobre ferramenta, tarefa e revisão humana**, conforme exigido pela rubrica da disciplina
FGA315.

A equipe entende que ferramentas de IA são instrumentos auxiliares de produtividade e
**não substituem** o juízo técnico nem a responsabilidade autoral dos integrantes. Toda
saída gerada por IA foi **lida, criticada e ajustada** pelos autores humanos da seção
correspondente antes de integrar o relatório.

## 1. Princípios adotados pela equipe

Antes do início dos trabalhos, a equipe acordou as seguintes diretrizes para o uso de IA.
Estas diretrizes foram mantidas integralmente da EU1 para a EU2:

1. **A IA não é coautora.** A autoria intelectual de cada seção pertence aos integrantes
   indicados na tabela "Histórico de versão" da própria seção. A IA é tratada como
   ferramenta, equivalente a um corretor ortográfico ou a um buscador.
2. **Nenhum trecho é colado em bruto.** Toda saída textual passou por reescrita,
   reorganização ou recorte humano antes de entrar no relatório.
3. **Decisões técnicas são humanas.** Na EU1, a seleção das características (§5), a
   adaptação do modelo de qualidade (§4), o recorte de escopo (§6) e a escolha dos ODS
   (§7) foram discutidas pela equipe em reunião e **não** delegadas à IA. Na EU2, a
   definição dos objetivos GQM, a formulação das questões e hipóteses, a seleção das
   métricas, os critérios de julgamento, os métodos de avaliação, o cronograma, a
   execução da coleta de dados e o julgamento final foram igualmente decididos pela
   equipe. A IA foi usada apenas para apoiar a redação, a
   verificação cruzada e a padronização.
4. **Nada de figurinhas, emojis ou ícones de IA.** O relatório segue padrão visual
   acadêmico; nenhum marcador visual gerado por IA foi mantido.
5. **Fatos sobre o AcheiUnB são conferidos no repositório original.** Quando a IA gerou
   afirmações sobre o software avaliado (módulos, dependências, fluxos), a equipe
   confirmou cada afirmação consultando o repositório
   [`unb-mds/2024-2-AcheiUnB`](https://github.com/unb-mds/2024-2-AcheiUnB) e a
   documentação interna do projeto.
6. **Citações e referências são verificadas manualmente.** Nenhuma referência da seção
   "Referências" das subseções foi inserida sem confirmação humana da existência da
   fonte (normas ISO, ODS oficiais da ONU, documentação técnica dos frameworks).

## 2. Ferramentas utilizadas

A tabela abaixo lista as ferramentas de IA generativa que apareceram em algum momento do
fluxo de trabalho da equipe nas entregas EU1 e EU2, com a tarefa típica e a forma de
revisão associada. As mesmas ferramentas foram utilizadas em ambas as entregas.

| Ferramenta | Versão / acesso | Tarefas típicas | Forma de revisão humana |
|---|---|---|---|
| **ChatGPT (OpenAI)** | GPT-5.4 / GPT-5.5, via interface web (conta pessoal dos integrantes) | Brainstorm inicial sobre estrutura de seções; sugestão de sinônimos e correção de coesão textual; explicação rápida de cláusulas das normas ISO. | Reescrita pelo autor humano; conferência das normas em fontes primárias (ISO/IEC 25010/25040/25051). |
| **Claude (Anthropic)** | Claude 4.7 / 4.6, via interface web e via Claude Code | Revisão de texto longo (concisão, eliminação de redundância); padronização tipográfica das tabelas; auxílio na escrita de blocos Mermaid; revisão final de coesão entre seções. | Comparação trecho a trecho com a versão anterior; leitura cruzada por um segundo integrante antes do *commit*. |
| **GitHub Copilot** | Plugin no editor (uso individual) | Auto-completar Markdown e sintaxe de Mermaid; sugerir nomes de cabeçalhos consistentes com os já existentes. | Aceite somente quando a sugestão coincidia com o que o autor já estava digitando; nada de aceite cego. |
| **Gemini (Google)** | Gemini 3.1, via interface web (uso esporádico) | Consulta pontual sobre redação em português acadêmico e sobre nomenclatura oficial de metas/indicadores dos ODS. | Conferência da nomenclatura no site oficial da ONU Brasil. |

A equipe **não** usou IA para: gerar dados de medição, simular resultados, fabricar
referências bibliográficas, produzir diagramas finais sem revisão, redigir o histórico
de versão, atribuir notas na matriz de priorização, definir os objetivos GQM, selecionar
métricas, formular os critérios de julgamento, executar as ferramentas de coleta nem
produzir o julgamento final ou as conclusões da avaliação.

## 3. Uso de IA por integrante

### 3.1 EU1 (Fase 1)

A tabela abaixo declara, por integrante, qual ferramenta foi mais usada, em quais tarefas
da EU1, e como o próprio integrante conferiu/ajustou as saídas. As seções listadas em
cada linha são aquelas em que o integrante atuou como autor (conforme o "Histórico de
versão" de cada subseção).

| Integrante | Ferramenta principal | Tarefa | Como conferiu/ajustou |
|---|---|---|---|
| **Davi Casseb** | Claude (interface web + Claude Code) | Apoio na estruturação das seções §1, §3, §5 e §7; padronização de tabelas em Markdown; revisão de coesão geral do relatório. | Reescreveu integralmente as introduções; conferiu os indicadores oficiais dos ODS no site da ONU Brasil; confrontou afirmações sobre o AcheiUnB com o `settings.py` e o `docker-compose.yml` do repositório original. |
| **Luis Lima** | Claude (Claude Code) | Revisão de redação técnica das seções §2, §4 e §6 nas quais atuou como autor ou revisor; uniformização do português. | Leu a sugestão da IA em paralelo com a versão da equipe e adotou apenas trechos que mantinham o sentido técnico; descartou reformulações que mudavam o significado das decisões registradas. |
| **Ana Joyce Guedes** | ChatGPT (GPT-5.5) | Apoio na redação das seções §1, §4, §6 e §7; verificação de sinônimos em português acadêmico. | Comparou a saída da IA com a literatura da disciplina (slides e ISO/IEC 25010) e ajustou termos para preservar a nomenclatura SQuaRE. |
| **Julia Vitória Freire** | ChatGPT (ChatGPT-5.5) | Apoio na redação das seções §2, §4 e §5; sugestão de quebra de parágrafos longos. | Revisou cada bloco gerado contra a ata interna da reunião de seleção de características; corrigiu pontos em que a IA generalizou conclusões que ainda dependiam de medição na Fase 2. |
| **Samuel Afonso** | GitHub Copilot + ChatGPT (GPT-5.4) | Auto-completar Markdown nas seções §1, §3 e §5; consulta pontual sobre frameworks (Django Channels, Celery). | Validou cada fato sobre a stack do AcheiUnB contra o `requirements.txt`, o `pyproject.toml` e a documentação oficial dos frameworks; descartou afirmações que não puderam ser confirmadas. |
| **Letícia Hladczuk** | Google Gemini (interface web) | Apoio na redação das seções §2, §3 e §6 e na padronização de tabelas; revisão final de português antes do *merge*. | Conferiu a estrutura de stakeholders contra a ISO/IEC 25040; comparou as tabelas de escopo com a divisão de responsabilidades acordada pela equipe; ajustou pontuação e estilo. |

### 3.2 EU2 (Fases 2, 3 e 4)

Na EU2, o uso de IA manteve o mesmo perfil de apoio textual e de padronização. As decisões
técnicas da EU2 (definição dos objetivos GQM, formulação de questões e hipóteses, seleção
das métricas, definição dos critérios de julgamento, escolha dos métodos de avaliação,
especificação do ambiente, elaboração do cronograma, execução da coleta de dados e
julgamento final) foram tomadas pela equipe com base nas normas ISO/IEC 25040, no
paradigma GQM (Basili et al.) e nas definições da Fase 1.

| Integrante | Ferramenta principal | Tarefa na EU2 | Como conferiu/ajustou |
|---|---|---|---|
| **Ana Joyce Guedes** | ChatGPT (GPT-5.5) | Apoio na redação da Fase 2: estruturação dos objetivos de medição, formulação textual das questões e descrição das métricas. | Conferiu cada objetivo GQM contra o template de Basili et al. e contra as características priorizadas na Fase 1 (§5); validou que as subcaracterísticas ISO 25010 referenciadas nas questões eram as corretas. |
| **Julia Vitória Freire** | ChatGPT (GPT-5.5) | Apoio na redação da Fase 2: hipóteses, métricas e níveis de pontuação; padronização das tabelas de critérios de julgamento. | Verificou que cada hipótese era testável pelas métricas definidas e que os níveis de pontuação tinham faixas numéricas coerentes com os instrumentos de medição declarados. |
| **Luis Lima** | Claude (Claude Code) | Apoio na redação da Fase 2: níveis de pontuação, hierarquia GQM e diagrama Mermaid; uniformização do português entre as seções. | Validou a rastreabilidade do diagrama GQM (3 G → 8 Q → 13 M) contra as tabelas das seções anteriores; conferiu que nenhuma métrica ficava sem questão associada e vice-versa. |
| **Davi Casseb** | Claude (interface web + Claude Code) | Redação integral da Fase 3: métodos de avaliação, instruções de coleta (I-01 a I-14), recursos e ambiente, cronograma e plano de contingência. | Confrontou cada instrução de coleta com o instrumento/método declarado na Fase 2 §4; verificou que os comandos literais (Bandit, Ruff, radon, trufflehog) correspondiam à documentação oficial de cada ferramenta; validou o cronograma contra o calendário da disciplina. |
| **Samuel Afonso** | GitHub Copilot + ChatGPT (GPT-5.4) | Redação da Fase 4: obtenção das medidas, documentação dos dados brutos, análise e resposta GQM, coerência com o propósito, julgamento e conclusões. | Verificou a correspondência entre os dados coletados e as instruções da Fase 3; conferiu que cada métrica foi comparada com os níveis de pontuação da Fase 2 §5; validou que o julgamento final era coerente com o propósito da Fase 1. |
| **Letícia Hladczuk** | Claude + Google Gemini (interface Antigravity) | Revisão geral das Fases 2, 3 e 4: verificação de consistência entre fases, padronização de tabelas e referências cruzadas, revisão de português. | Conferiu a rastreabilidade Fase 1 → Fase 2 → Fase 3 → Fase 4 (características priorizadas → objetivos GQM → métodos e instruções → dados e julgamento); identificou inconsistências de nomenclatura e referências cruzadas quebradas antes do *merge*. |

## 4. Uso de IA por seção do relatório

As tabelas abaixo registram, por seção entregue, o **tipo de apoio** que a IA prestou e o
**limite** desse apoio. O objetivo é deixar explícito que o conteúdo técnico das decisões
é humano; a IA atuou na superfície textual e na padronização.

### 4.1 EU1 (Fase 1)

| Seção | Tipo de apoio da IA | O que **não** veio da IA |
|---|---|---|
| §1 Propósito | Sugestão de redação para a declaração de propósito; padronização da tabela D1/D2/D3. | A definição das três decisões D1/D2/D3, quem decide e como os dados são usados — discutidas em reunião da equipe. |
| §2 Stakeholders | Reescrita do texto introdutório; ajuste de coesão das colunas "Critério de sucesso" e "Influência". | A identificação dos stakeholders, papéis ISO/IEC 25040 e a influência concreta sobre as escolhas. |
| §3 Software | Revisão de redação técnica; auxílio em alguns trechos do diagrama Mermaid. | A classificação do tipo de produto, a leitura da arquitetura e a lista de implicações — feitas por inspeção direta do repositório do AcheiUnB. |
| §4 Modelo de qualidade | Padronização da tabela "Decisão / Justificativa central"; auxílio na sintaxe do diagrama. | A escolha das características mantidas/excluídas e os graus de aplicabilidade (✓ / ~ / ✗) — atribuídos pela equipe com base nas premissas e em §3. |
| §5 Características | Padronização de tabela e diagrama; revisão de redação dos *trade-offs*. | Os pesos da matriz, as notas atribuídas e o ranking P1–P3 — definidos em reunião presencial; a IA **não** atribuiu notas. |
| §6 Escopo | Reescrita de trechos da tabela "Fora do escopo"; auxílio no diagrama de cobertura progressiva. | A definição do que entra/fica fora e a condição de reabertura de cada item — decididos pela equipe. |
| §7 ODS | Auxílio na redação do vínculo de cada ODS com o software. | A seleção dos ODS, das metas (4.3, 9.c, 11.7, 12.5) e dos indicadores oficiais — verificados manualmente no portal da ONU Brasil. |
| Páginas auxiliares (`index.md`, `equipe.md`, `rastreabilidade.md`, esta declaração) | Apoio na padronização e na redação. | Conteúdo factual sobre a equipe e os links de rastreabilidade — preenchidos manualmente. |

### 4.2 EU2 (Fases 2, 3 e 4)

| Seção | Tipo de apoio da IA | O que **não** veio da IA |
|---|---|---|
| Fase 2, §1 Objetivos de Medição | Auxílio na redação dos campos do template GQM; padronização das tabelas. | A escolha dos objetos de análise, dos propósitos, dos focos de qualidade e dos pontos de vista, derivados pela equipe a partir das características priorizadas e dos stakeholders definidos na Fase 1. |
| Fase 2, §2 Questões | Revisão de coesão textual; sugestão de formulação interrogativa. | A identificação das subcaracterísticas ISO 25010 a cobrir e a formulação conceitual de cada questão. |
| Fase 2, §3 Hipóteses | Revisão de redação e ajuste de clareza das afirmações. | As expectativas sobre o estado do AcheiUnB (ex.: segredos no código, cobertura de testes, ausência de retry), formuladas com base na análise do repositório realizada na Fase 1. |
| Fase 2, §4 Métricas | Padronização das tabelas (tipo, instrumento, qualidade da métrica). | A seleção das métricas, dos instrumentos de coleta e a avaliação de qualidade (simplicidade, objetividade, validade), foram decididas pela equipe considerando o que é mensurável no contexto do AcheiUnB. |
| Fase 2, §5 Níveis de Pontuação | Padronização das tabelas de faixas e critérios; revisão de clareza dos textos de julgamento. | As faixas numéricas, os rótulos de julgamento (Bom/Regular/Ruim/Aceitável/Inaceitável) e os critérios textuais. |
| Fase 2, §6 Hierarquia GQM | Auxílio na sintaxe Mermaid do diagrama `graph TD`. | A estrutura hierárquica G→Q→M e a rastreabilidade completa (3 objetivos → 8 questões → 13 métricas). |
| Fase 3, §1 Método e Instruções | Apoio na estruturação das instruções passo a passo; padronização de comandos em blocos de código. | A escolha dos três métodos de avaliação (MA1, MA2, MA3), os comandos literais de cada ferramenta (verificados na documentação oficial), as regras de repetibilidade e as 14 instruções de coleta, foram elaborados pela equipe. |
| Fase 3, §2 Recursos e Ambiente | Padronização das tabelas de hardware, software e massa de dados. | A especificação de requisitos de hardware, as versões fixadas de software, a definição da massa de dados sintética e o procedimento de preparação, foi decidido com base na arquitetura do AcheiUnB. |
| Fase 3, §3 Cronograma | Auxílio na sintaxe Mermaid do diagrama de Gantt; revisão de redação do plano de contingência. | A distribuição de atividades, as datas dos marcos, a alocação de responsáveis por dupla/característica e os cenários de risco com contingências (planejado com base no calendário da disciplina). |
| Fase 4, §1 Obtenção das Medidas | Apoio na padronização da apresentação dos resultados e formatação de tabelas de dados. | A execução integral das instruções de coleta (I-01 a I-14) com as ferramentas declaradas (Bandit, trufflehog, Ruff, radon, pytest-cov).|
| Fase 4, §2 Dados Brutos | Apoio na organização e padronização dos metadados (`*.meta.md`). | Os arquivos de dados, logs, screenshots e vídeos dos testes. |
| Fase 4, §3 Análise e Resposta GQM | Apoio na redação dos textos de análise; padronização de gráficos e tabelas comparativas. | O processamento dos dados brutos em métricas, a comparação com os níveis de pontuação (Fase 2 §5), a resposta a cada questão (Q) e a confirmação/refutação das hipóteses. |
| Fase 4, §4 Coerência com o Propósito | Revisão de redação e coesão textual. | A conexão entre os resultados da avaliação e o propósito declarado na Fase 1 (decisões D1, D2, D3); essa conexão foi articulada pela equipe. |
| Fase 4, §5 Julgamento e Conclusões | Revisão de clareza e concisão das recomendações. | O julgamento final de qualidade, as conclusões e as sugestões de melhoria concretas; o julgamento e a conclusão foram formulados pela equipe com base nos dados coletados e nos critérios estabelecidos na EU2. |

## 5. O que a equipe explicitamente não fez

Para evitar ambiguidade na auditoria da rubrica, a equipe registra que **não**:

- Submeteu seções inteiras à IA pedindo para "gerar a Fase X";
- Usou IA para definir os objetivos GQM, selecionar métricas, formular hipóteses ou
  estabelecer os critérios de julgamento;
- Usou IA para gerar dados, métricas ou resultados de medição;
- Usou IA para produzir o julgamento final, as conclusões ou as sugestões de melhoria;
- Delegou à IA a escolha dos métodos de avaliação (MA1, MA2, MA3) nem a elaboração
  do cronograma;
- Pediu à IA que inventasse referências bibliográficas, todas as referências foram conferidas em suas fontes primárias;
- Manteve qualquer emoji, figurinha ou ícone de IA no corpo do relatório, das tabelas ou
  dos diagramas.

## 6. Compromisso para a EU3

A equipe se compromete a:

1. **Atualizar esta declaração** na entrega EU3, caso haja revisões ou complementos
   significativos aos artefatos já entregues.
2. **Registrar como achado** qualquer caso em que a IA tenha induzido a equipe ao erro
   (alucinações de referência, afirmações factualmente incorretas sobre o AcheiUnB), no
   próprio repositório, para fins de aprendizado.
3. **Manter a rastreabilidade** entre os dados brutos e as
   conclusões apresentadas no relatório, garantindo que qualquer auditor possa verificar
   que os resultados não foram fabricados ou influenciados por IA.

## Histórico de versão

| Versão | Data       | Descrição                                                          | Autor(es)                                                                          | Revisor(es)                                                                       |
|--------|------------|--------------------------------------------------------------------|------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| 1.0    | 2026-05-13 | Versão inicial da declaração de uso de IA para a entrega EU1.      | Davi Casseb, Luis Lima, Ana Joyce, Julia Vitória, Samuel Afonso, Letícia Hladczuk  | Davi Casseb, Luis Lima, Ana Joyce, Julia Vitória, Samuel Afonso, Letícia Hladczuk |
| 2.0    | 2026-06-12 | Expansão da declaração para cobrir a EU2 (Fases 2, 3 e 4).         | Davi Casseb, Luis Lima, Ana Joyce, Julia Vitória, Samuel Afonso, Letícia Hladczuk                                                                   | Davi Casseb, Luis Lima, Ana Joyce, Julia Vitória, Samuel Afonso, Letícia Hladczuk                   |

## Referências

1. RAMOS, Cristiane. *Plano de Ensino da disciplina FGA315 Qualidade de Software 1*. FCTE/UnB, 2026/1.
2. RAMOS, Cristiane. *Trabalho Final - Critérios de Avaliação (EU1)*. FCTE/UnB, 2026/1.
3. ANTHROPIC. *Claude - Model Card and Usage Guidelines*. Disponível em: <https://www.anthropic.com/>. Acesso em: 13 maio 2026.
4. OPENAI. *ChatGPT - Model Behavior and Usage*. Disponível em: <https://openai.com/>. Acesso em: 13 maio 2026.
5. GITHUB. *GitHub Copilot Documentation*. Disponível em: <https://docs.github.com/copilot>. Acesso em: 13 maio 2026.
