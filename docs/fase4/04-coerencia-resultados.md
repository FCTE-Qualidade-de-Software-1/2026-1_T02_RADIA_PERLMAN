# 4. Coerência dos Resultados com o Propósito

Esta seção confronta os resultados da [análise GQM](03-analise-resposta-gqm.md) com a
**declaração de propósito** e as **decisões a apoiar** definidas na
[Fase 1, §1.3](../fase1/01-proposito.md#13-uso-pretendido-dos-resultados). O objetivo é
demonstrar que os achados desta avaliação alimentam diretamente as decisões para as quais
ela foi planejada - **D1** (priorização do *backlog* de qualidade) e **D2**
(manter / refatorar / substituir componentes específicos) - respeitando os limites da
execução parcial desta entrega.

!!! info "Leitura honesta da coerência nesta entrega"
    Quatro das oito questões GQM têm resposta com dados suficientes (Q1.1, Q1.2, Q2.2 e
    a parte do Celery em Q3.2); as demais permanecem indeterminadas por pendência de
    coleta ([Fase 4, Tabela 4.1](index.md#estado-da-execucao)). Portanto, a avaliação
    **já produz subsídio acionável** para D1 e D2 nas características de maior prioridade
    (Segurança e Manutenibilidade), mas **ainda não é um diagnóstico completo** - o que
    é coerente com a estratégia de cobertura progressiva da
    [Fase 1, §6.4](../fase1/06-escopo.md#64-plano-de-cobertura-progressiva).

## 4.1 Apoio à priorização do *backlog* de qualidade (Decisão D1)

A **D1** ([Fase 1, §1.3](../fase1/01-proposito.md#13-uso-pretendido-dos-resultados))
consiste em **ranquear itens de melhoria por característica e por risco residual**, com
corte por capacidade da equipe. Os resultados já permitem montar um *backlog* inicial
priorizado:

| Prioridade | Item de *backlog* | Origem (métrica / questão) | Risco residual |
|---|---|---|---|
| Alta | *Hardening* de configuração do Django para produção | M1.2.2 (Ruim, ~50%) / Q1.2 | Alto |
| Alta | Política de `retry` nas 13 tarefas Celery | M3.2.2 (Regular, 0/13) / Q3.2 | Médio-Alto |
| Média | Correção das 3 chamadas HTTP sem *timeout* (B113) | M1.2.1 (Regular) / Q1.2 | Médio |
| Média | Refatoração dos 5 pontos de complexidade elevada em `users`/`reports` | M2.2.2 (Regular, 5 funções grau C) / Q2.2 | Médio |

Esse ranqueamento é exatamente o artefato que a D1 demanda e está apto a receber o corte
por *story points* da equipe sucessora. As pendências (cobertura de testes, cenários de
falha) entrarão no *backlog* assim que as instruções correspondentes forem concluídas.

## 4.2 Apoio à decisão manter / refatorar / substituir (Decisão D2)

A **D2** decide, **por componente**, entre manter, refatorar ou substituir, comparando o
estado medido aos critérios da Fase 2. Os componentes nomeados na D2 recebem, com os
dados atuais, a seguinte orientação preliminar:

| Componente (D2) | Evidência atual | Orientação preliminar |
|---|---|---|
| *Secret management* | M1.1.1 = 0 segredos versionados (Aceitável); porém `SECRET_KEY` fraca em M1.2.2 | **Refatorar** a geração da chave (via variável de ambiente), **sem substituir** o mecanismo. |
| Autenticação MSAL+JWT | Q1.3 pendente (I-05, I-06) | **Decisão adiada** - depende dos ensaios dinâmicos. |
| Fila Celery+Redis | M3.2.2 = 0/13 tarefas com *retry* (Regular); Q3.1 (queda do Redis) pendente | **Refatorar** para adicionar resiliência; substituição não se justifica pelos dados atuais. |
| Camada de testes do *frontend* | Q2.3 pendente (I-11) | **Decisão adiada** - aguarda contagem de testes. |
| Módulo de chat (WebSocket) | Q3.2 (reconexão) pendente (I-13) | **Decisão adiada**. |

A estrutura geral do *backend* - boa complexidade média (M2.2.1, grau A) com pontos
localizados de atenção - sustenta a orientação de que **o backend é viável e
manutenível**, favorecendo **evolução incremental em vez de reescrita completa**. Vale
registrar que essa conclusão de manutenibilidade apoia-se em M2.2; a evidência do Ruff
(M2.1.1) está **invalidada** ([§3.1](03-analise-resposta-gqm.md#31-sintese-dos-resultados))
e, portanto, **não** é usada como base para esta orientação.

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

A avaliação **cumpre parcialmente** seu propósito: entrega subsídio robusto para D1 e D2
em Segurança e Manutenibilidade, mas as decisões sobre **autenticação dinâmica, cobertura
de testes e tolerância a falhas em tempo de execução** dependem das sete instruções
pendentes. Em coerência com o princípio de cortes declarados da
[Fase 1, §6.3](../fase1/06-escopo.md#63-fora-do-escopo), essas decisões ficam
**explicitamente adiadas**, e não silenciosamente assumidas - preservando a validade dos
julgamentos já emitidos.

## Histórico de versão

| Versão | Data       | Descrição | Autor(es) | Revisor(es) |
| :-- | :-- | :-- | :-- | :-- |
| 1.0 | 2026-06-12 | Verificação da coerência dos resultados com o propósito da avaliação (Fase 1). | Samuel Afonso | Davi Casseb, Letícia Hladczuk |
| 2.0 | 2026-06-12 | Correção da atribuição D1/D2 conforme a Fase 1; alinhamento com a análise GQM revisada; declaração explícita do escopo parcial. | Samuel Afonso | Davi Casseb, Letícia Hladczuk |

## Referências

1. ISO/IEC 25040:2011. *Systems and software engineering: Systems and software Quality Requirements and Evaluation (SQuaRE): Evaluation process*. International Organization for Standardization, 2011.
2. BASILI, Victor R.; CALDIERA, Gianluigi; ROMBACH, H. Dieter. *The Goal Question Metric Approach*. In: Encyclopedia of Software Engineering. Wiley, 1994.
3. Django Software Foundation. *Deployment checklist e Security in Django*. Disponível em: <https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/>. Acesso em: 12 jun. 2026.
4. PyCQA. *Bandit Documentation*. Disponível em: <https://bandit.readthedocs.io/>. Acesso em: 12 jun. 2026.
5. Radon. *Radon Documentation: Cyclomatic Complexity*. Disponível em: <https://radon.readthedocs.io/>. Acesso em: 12 jun. 2026.