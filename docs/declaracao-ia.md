# Declaração de uso de IA

Esta seção declara, de forma explícita e auditável, o uso de ferramentas de Inteligência
Artificial generativa pela equipe T02 RADIA PERLMAN na produção dos artefatos da Entrega
da Unidade 1 (EU1). A declaração segue o princípio de **transparência sobre ferramenta,
tarefa e revisão humana**, conforme exigido pela rubrica da disciplina FGA315.

A equipe entende que ferramentas de IA são instrumentos auxiliares de produtividade e
**não substituem** o juízo técnico nem a responsabilidade autoral dos integrantes. Toda
saída gerada por IA foi **lida, criticada e ajustada** pelos autores humanos da seção
correspondente antes de integrar o relatório.

## 1. Princípios adotados pela equipe

Antes do início dos trabalhos, a equipe acordou as seguintes diretrizes para o uso de IA
na EU1:

1. **A IA não é coautora.** A autoria intelectual de cada seção pertence aos integrantes
   indicados na tabela "Histórico de versão" da própria seção. A IA é tratada como
   ferramenta, equivalente a um corretor ortográfico ou a um buscador.
2. **Nenhum trecho é colado em bruto.** Toda saída textual passou por reescrita,
   reorganização ou recorte humano antes de entrar no relatório.
3. **Decisões técnicas são humanas.** A seleção das características (§5), a adaptação do
   modelo de qualidade (§4), o recorte de escopo (§6) e a escolha dos ODS (§7) foram
   discutidas pela equipe em reunião e **não** delegadas à IA. A IA foi usada apenas para
   apoiar a redação, a verificação cruzada e a padronização.
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
fluxo de trabalho da equipe na EU1, com a tarefa típica e a forma de revisão associada.

| Ferramenta | Versão / acesso | Tarefas típicas | Forma de revisão humana |
|---|---|---|---|
| **ChatGPT (OpenAI)** | GPT-5.4 / GPT-5.5, via interface web (conta pessoal dos integrantes) | Brainstorm inicial sobre estrutura de seções; sugestão de sinônimos e correção de coesão textual; explicação rápida de cláusulas das normas ISO. | Reescrita pelo autor humano; conferência das normas em fontes primárias (ISO/IEC 25010/25040/25051). |
| **Claude (Anthropic)** | Claude 4.7 / 4.6, via interface web e via Claude Code | Revisão de texto longo (concisão, eliminação de redundância); padronização tipográfica das tabelas; auxílio na escrita de blocos Mermaid; revisão final de coesão entre seções. | Comparação trecho a trecho com a versão anterior; leitura cruzada por um segundo integrante antes do *commit*. |
| **GitHub Copilot** | Plugin no editor (uso individual) | Auto-completar Markdown e sintaxe de Mermaid; sugerir nomes de cabeçalhos consistentes com os já existentes. | Aceite somente quando a sugestão coincidia com o que o autor já estava digitando; nada de aceite cego. |
| **Gemini (Google)** | Gemini 3.1, via interface web (uso esporádico) | Consulta pontual sobre redação em português acadêmico e sobre nomenclatura oficial de metas/indicadores dos ODS. | Conferência da nomenclatura no site oficial da ONU Brasil. |

A equipe **não** usou IA para: gerar dados de medição, simular resultados, fabricar
referências bibliográficas, produzir diagramas finais sem revisão, redigir o histórico
de versão ou atribuir notas na matriz de priorização.

## 3. Uso de IA por integrante

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

## 4. Uso de IA por seção do relatório

Esta tabela registra, por seção entregue na EU1, o **tipo de apoio** que a IA prestou e o
**limite** desse apoio. O objetivo é deixar explícito que o conteúdo técnico das decisões
é humano; a IA atuou na superfície textual e na padronização.

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

## 5. O que a equipe explicitamente não fez

Para evitar ambiguidade na auditoria da rubrica, a equipe registra que **não**:

- Submeteu seções inteiras à IA pedindo para "gerar a Fase 1";
- Usou IA para gerar dados, métricas ou resultados de medição (a EU1 não contém
  medição; quando houver, na Fase 2, os dados brutos serão coletados por instrumentos
  declarados, não por IA);
- Pediu à IA que inventasse referências bibliográficas — todas as referências foram
  conferidas em suas fontes primárias;
- Manteve qualquer emoji, figurinha ou ícone de IA no corpo do relatório, das tabelas ou
  dos diagramas.

## 6. Compromisso para as próximas fases

A equipe se compromete a:

1. **Atualizar esta declaração** a cada nova entrega (EU2, EU3), descrevendo o uso
   adicional de IA — em especial em tarefas de Fase 2 (definição de métricas) e Fase 3
   (medição), nas quais o uso de IA deve ser ainda mais restrito.
2. **Registrar como achado** qualquer caso em que a IA tenha induzido a equipe ao erro
   (alucinações de referência, afirmações factualmente incorretas sobre o AcheiUnB), no
   próprio repositório, para fins de aprendizado.
3. **Não usar IA para gerar dados de medição** nem para sintetizar análises
   estatísticas — esses passos serão executados por instrumentos com saída auditável
   (Bandit, Safety, Ruff, Coverage, scripts próprios).

## Histórico de versão

| Versão | Data       | Descrição                                                          | Autor(es)                                                                          | Revisor(es)                                                                       |
|--------|------------|--------------------------------------------------------------------|------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| 1.0    | 2026-05-13 | Versão inicial da declaração de uso de IA para a entrega EU1.      | Davi Casseb, Luis Lima, Ana Joyce, Julia Vitória, Samuel Afonso, Letícia Hladczuk  | Davi Casseb, Luis Lima, Ana Joyce, Julia Vitória, Samuel Afonso, Letícia Hladczuk |

## Referências

1. RAMOS, Cristiane. *Plano de Ensino da disciplina FGA315 Qualidade de Software 1*. FCTE/UnB, 2026/1.
2. RAMOS, Cristiane. *Trabalho Final - Critérios de Avaliação (EU1)*. FCTE/UnB, 2026/1.
3. ANTHROPIC. *Claude - Model Card and Usage Guidelines*. Disponível em: <https://www.anthropic.com/>. Acesso em: 13 maio 2026.
4. OPENAI. *ChatGPT - Model Behavior and Usage*. Disponível em: <https://openai.com/>. Acesso em: 13 maio 2026.
5. GITHUB. *GitHub Copilot Documentation*. Disponível em: <https://docs.github.com/copilot>. Acesso em: 13 maio 2026.
