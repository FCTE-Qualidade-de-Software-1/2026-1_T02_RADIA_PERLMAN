# 4. Coerência dos Resultados com o Propósito

Esta seção confronta os resultados da [análise GQM](03-analise-resposta-gqm.md) com a
**declaração de propósito** e as **decisões a apoiar** definidas na
[Fase 1, §1.3](../fase1/01-proposito.md#13-uso-pretendido-dos-resultados). O objetivo é
demonstrar que os achados desta avaliação alimentam diretamente as decisões para as quais
ela foi planejada - **D1** (priorização do *backlog* de qualidade) e **D2**
(manter / refatorar / substituir componentes específicos) - respeitando os limites da
execução parcial desta entrega.

!!! info "Leitura honesta da coerência nesta entrega"
    Na EU3, todas as **oito questões GQM** têm resposta com dados auditáveis. A análise
    a seguir trata a avaliação como **diagnóstico completo** dentro do escopo declarado
    ([Fase 1, §6.2](../fase1/06-escopo.md#62-dentro-do-escopo)) e produz subsídio
    acionável para D1 e D2 nas três características priorizadas. Decisões que
    permaneciam adiadas na EU2 (autenticação dinâmica, cobertura de testes, tolerância
    a falhas em tempo de execução) agora são endereçáveis.

## 4.1 Apoio à priorização do *backlog* de qualidade (Decisão D1)

A **D1** ([Fase 1, §1.3](../fase1/01-proposito.md#13-uso-pretendido-dos-resultados))
consiste em **ranquear itens de melhoria por característica e por risco residual**, com
corte por capacidade da equipe. Os resultados já permitem montar um *backlog* inicial
priorizado:

| Prioridade | Item de *backlog* | Origem (métrica / questão) | Risco residual |
|---|---|---|---|
| Alta | Bootstrap de testes automatizados no *frontend* (Vitest/Playwright + cobertura mínima) | M2.3.2 (Inaceitável, 0 testes) / Q2.3 | Alto |
| Alta | *Hardening* de configuração do Django para produção | M1.2.2 (Ruim, ~50%) / Q1.2 | Alto |
| Alta | Resolução dos 2 ciclos de *imports* (`chat↔users`, `users↔reports`) | M2.1.2 (Ruim, 2 ciclos) / Q2.1 | Médio-Alto |
| Alta | Política de `retry` nas 13 tarefas Celery | M3.2.2 (Regular, 0/13) / Q3.2 | Médio-Alto |
| Média | Limpeza dos 83 *warnings* do Ruff (PLR6301, PLC0415 majoritários) | M2.1.1 (Ruim, 83) / Q2.1 | Médio |
| Média | Correção das 3 chamadas HTTP sem *timeout* (B113) | M1.2.1 (Regular) / Q1.2 | Médio |
| Média | Refatoração dos 5 pontos de complexidade elevada em `users`/`reports` | M2.2.2 (Regular, 5 funções grau C) / Q2.2 | Médio |

Esse ranqueamento é exatamente o artefato que a D1 demanda e está apto a receber o
corte por *story points* da equipe sucessora. Vale registrar que **nada da
Confiabilidade aparece como item de alta prioridade**: a resiliência ao Redis
(M3.1.1 = Bom) e a reconexão automática do WebSocket (M3.2.1 = Bom) já se mostraram
adequadas, sobrando apenas o `retry` do Celery como pendência de Confiabilidade.

## 4.2 Apoio à decisão manter / refatorar / substituir (Decisão D2)

A **D2** decide, **por componente**, entre manter, refatorar ou substituir, comparando o
estado medido aos critérios da Fase 2. Os componentes nomeados na D2 recebem, com os
dados atuais, a seguinte orientação preliminar:

| Componente (D2) | Evidência atual | Orientação |
|---|---|---|
| *Secret management* | M1.1.1 = 0 segredos versionados (Aceitável); porém `SECRET_KEY` fraca em M1.2.2 | **Refatorar** a geração da chave (via variável de ambiente), **sem substituir** o mecanismo. |
| Autenticação MSAL+JWT | M1.3.1 = 0 atributos faltantes (Bom); M1.3.2 = rejeita JWT manipulado (Aceitável) | **Manter.** Mecanismo de assinatura e endurecimento de *cookie* funcionando como esperado. |
| Fila Celery+Redis | M3.2.2 = 0/13 tarefas com *retry* (Regular); M3.1.1 = degrada graciosamente sob queda do Redis (Bom) | **Refatorar** para adicionar `retry` nas tarefas; o componente Redis em si **mantém-se**, dado o bom comportamento do isolamento de falha. |
| Camada de testes do *frontend* | M2.3.2 = 0 testes (Inaceitável) | **Substituir** o estado atual (ausência) **por uma camada nova** (bootstrap de Vitest ou Playwright + suíte mínima). Não é refatoração, é introdução. |
| Camada de testes do *backend* | M2.3.1 = 83% de cobertura (Bom), 108/109 testes aprovados | **Manter** o investimento existente; pequena correção do teste em falha (`test_send_welcome_email_on_first_login`). |
| Módulo de chat (WebSocket) | M3.2.1 = reconexão automática Sim (Bom) | **Manter**. Comportamento padrão do `socket.io-client` é suficiente. |
| Estilo / acoplamento do *backend* | M2.1.1 = 83 violações Ruff (Ruim); M2.1.2 = 2 ciclos de *imports* (Ruim) | **Refatorar** para reduzir violações e quebrar os ciclos `chat↔users` e `users↔reports`. |

A estrutura geral do *backend* - boa complexidade média (M2.2.1, grau A) com pontos
localizados de atenção e 83% de cobertura de testes - sustenta a orientação de que
**o *backend* é viável e manutenível**, favorecendo **evolução incremental em vez de
reescrita completa**. A combinação Manutenibilidade-Confiabilidade do *backend*
(estilo Ruim mas testes Bons e degradação graciosa) é coerente com um sistema que
**precisa de cuidado de estilo/arquitetura**, mas **não de reescrita**.

## 4.3 Coerência com os stakeholders e o cenário de aplicação

Os resultados atendem aos públicos primários definidos na
[Fase 1, §1.2](../fase1/01-proposito.md#12-para-quem-e-a-avaliacao):

- **Próximas equipes MDS (sucessoras):** recebem um *backlog* priorizado (D1) e
  orientações por componente (D2), reduzindo a incerteza técnica da sucessão.
- **Equipe AcheiUnB 2024-2:** o diagnóstico usa o ferramental que ela própria já adotou
  no CI (Bandit, Radon), aumentando a aceitação dos achados.
- **Operador institucional hipotético:** os achados de configuração (M1.2.2) sinalizam
  claramente que o produto **não está pronto para produção** sem *hardening* prévio.

## 4.4 Limites da coerência nesta entrega

A avaliação **cumpre integralmente** seu propósito declarado na Fase 1, com 14 de 14
métricas medidas e todas as 8 questões respondidas com dados auditáveis. Permanecem
fora do escopo, por declaração explícita na [Fase 1, §6.3](../fase1/06-escopo.md#63-fora-do-escopo):
Usabilidade (vedada pela disciplina), Eficiência de *performance*, Compatibilidade e
Portabilidade. Decisões D1 e D2 sobre essas características exigiriam **nova fase de
medição** com instrumentos próprios e estão sinalizadas como pontos a reabrir em
eventuais avaliações sucessoras (ver [§4.4 da Fase 1, §6.6](../fase1/06-escopo.md#66-relacao-com-avaliacoes-anteriores-e-futuras)).

Limites pontuais a considerar na interpretação dos resultados:

- **I-05 e I-13** foram conduzidas via **inspeção do produtor** (código do
  *view*/cliente) em vez do *cenário* MA3 puro, porque o *login* real exige
  credenciais MSAL da UnB. A evidência por inspeção é equivalente em força para
  auditoria, mas o registro dessa equivalência fica explicitado aqui.
- **I-06** foi conduzida com ensaio dinâmico real (curl + token forjado), confirmando
  o comportamento do código sob ataque sintético.
- **M2.3.1** apresenta **1 teste em falha** (`test_send_welcome_email_on_first_login`)
  por *mismatch* de *mock*, sem impacto estrutural; a falha é registrada para
  consideração da equipe sucessora.

## Histórico de versão

| Versão | Data       | Descrição | Autor(es) | Revisor(es) |
| :-- | :-- | :-- | :-- | :-- |
| 1.0 | 2026-06-12 | Verificação da coerência dos resultados com o propósito da avaliação (Fase 1). | Samuel Afonso | Davi Casseb, Letícia Hladczuk |
| 2.0 | 2026-06-12 | Correção da atribuição D1/D2 conforme a Fase 1; alinhamento com a análise GQM revisada; declaração explícita do escopo parcial. | Samuel Afonso | Davi Casseb, Letícia Hladczuk |
| 3.0 | 2026-06-23 | Atualização para a EU3: *backlog* D1 ampliado com itens das métricas recém-medidas; tabela D2 com orientação para todos os componentes; reescrita dos limites de coerência. | Luis Eduardo Castro M Lima, Davi Casseb | Samuel Afonso |

## Referências

1. ISO/IEC 25040:2011. *Systems and software engineering: Systems and software Quality Requirements and Evaluation (SQuaRE): Evaluation process*. International Organization for Standardization, 2011.
2. BASILI, Victor R.; CALDIERA, Gianluigi; ROMBACH, H. Dieter. *The Goal Question Metric Approach*. In: Encyclopedia of Software Engineering. Wiley, 1994.
3. Django Software Foundation. *Deployment checklist e Security in Django*. Disponível em: <https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/>. Acesso em: 12 jun. 2026.
4. PyCQA. *Bandit Documentation*. Disponível em: <https://bandit.readthedocs.io/>. Acesso em: 12 jun. 2026.
5. Radon. *Radon Documentation: Cyclomatic Complexity*. Disponível em: <https://radon.readthedocs.io/>. Acesso em: 12 jun. 2026.