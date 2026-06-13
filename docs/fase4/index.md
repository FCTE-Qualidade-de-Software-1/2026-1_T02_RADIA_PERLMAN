# Fase 4: Execução da Avaliação

As fases anteriores estabeleceram **por que** avaliar ([Fase 1](../fase1/index.md)),
**o que** medir ([Fase 2](../fase2/index.md)) e **como** medir
([Fase 3](../fase3/index.md)). A Fase 4, conforme a ISO/IEC 25040, é a fase de
**execução**: as medidas são obtidas seguindo as instruções do Plano de Avaliação, os
dados brutos são arquivados de forma auditável, os resultados são comparados aos níveis
de pontuação da [Fase 2, §5](../fase2/05-niveis-pontuacao.md) e, por fim, é emitido o
**julgamento da qualidade** do AcheiUnB, com conclusões e sugestões de melhoria
acionáveis para os stakeholders definidos na
[Fase 1, §2](../fase1/02-stakeholders.md).

## Estrutura da Fase 4

| Seção | Conteúdo | Critério da rubrica atendido |
|---|---|---|
| [1. Obtenção das medidas](01-medidas.md) | Resultado da execução de cada instrução de coleta (I-01 a I-14) definida na [Fase 3, §1](../fase3/01-metodo-instrucoes.md). | F4-C1 |
| [2. Dados brutos](02-dados-brutos.md) | Repositório das evidências de coleta (relatórios de ferramentas, listagens e capturas), com rastreabilidade entre dado bruto e métrica. | F4-C2 |
| [3. Análise e respostas GQM](03-analise-resposta-gqm.md) | Processamento dos dados, comparação com os níveis de pontuação e resposta às questões e hipóteses da Fase 2. | F4-C3 |
| [4. Coerência dos resultados com o propósito](04-coerencia-resultados.md) | Demonstração de como os resultados apoiam as decisões D1 e D2 declaradas na [Fase 1, §1.3](../fase1/01-proposito.md#13-uso-pretendido-dos-resultados). | F4-C4 |
| [5. Julgamento, conclusões e sugestões de melhoria](05-julgamento-conclusoes.md) | Julgamento final da qualidade, conclusões e ações concretas recomendadas ao requisitante. | F4-C5 |

## Estado da execução

A execução seguiu a estratégia de **cobertura progressiva em anéis** da
[Fase 1, §6.4](../fase1/06-escopo.md#64-plano-de-cobertura-progressiva): as coletas dos
Anéis 1 e 2 (análise estática e inspeção documental, métodos MA1/MA2) foram priorizadas,
e parte dos ensaios do Anel 3 (cenários dinâmicos em laboratório, método MA3) permanece
pendente, conforme detalhado em [Obtenção das medidas](01-medidas.md).

**Tabela 4.1: estado das instruções de coleta na entrega EU2.**

| Estado | Instruções | Métricas correspondentes |
|---|---|---|
| **Concluídas** | I-01, I-02, I-03, I-04, I-07, I-09, I-14 | M1.1.1, M1.1.2, M1.2.1, M1.2.2, M2.1.1, M2.2.1, M2.2.2, M3.2.2 |
| **Pendentes** | I-05, I-06, I-08, I-10, I-11, I-12, I-13 | M1.3.1, M1.3.2, M2.1.2, M2.3.1, M2.3.2, M3.1.1, M3.2.1 |

!!! info "Implicação das pendências"
    As questões **Q1.3** (autenticação dinâmica), **Q2.3** (cobertura de testes) e
    **Q3.1** (tolerância a falhas sob queda do Redis) ainda não dispõem de dados
    suficientes para resposta definitiva; suas conclusões nesta entrega são parciais. A
    conclusão da execução dessas instruções está registrada como ação prioritária nas
    [sugestões de melhoria](05-julgamento-conclusoes.md), preservando a transparência
    exigida pelo processo de avaliação.

## Rastreabilidade com as fases anteriores

- Cada resultado da seção [1](01-medidas.md) identifica a **instrução (I)** da Fase 3 e
  a **métrica (M)** da Fase 2 que ele atende;
- Os dados brutos da seção [2](02-dados-brutos.md) seguem a identificação por métrica
  (`M<x.y.z>_<ferramenta>_<data>`) para permitir auditoria externa;
- A análise da seção [3](03-analise-resposta-gqm.md) retoma a hierarquia GQM consolidada
  na [Fase 2, §6](../fase2/06-hierarquia-gqm.md);
- O julgamento das seções [4](04-coerencia-resultados.md) e
  [5](05-julgamento-conclusoes.md) é confrontado com o propósito e as decisões da
  [Fase 1, §1](../fase1/01-proposito.md).

## Histórico de versão

| Versão | Data       | Descrição | Autor(es) | Revisor(es) |
| :-- | :-- | :-- | :-- | :-- |
| 1.0 | 2026-06-12 | Versão inicial da visão geral da Fase 4, com estrutura, estado da execução e rastreabilidade. | Samuel Afonso | Davi Casseb, Letícia Hladczuk |

## Referências

1. ISO/IEC 25040:2011. *Systems and software engineering: Systems and software Quality Requirements and Evaluation (SQuaRE): Evaluation process*. International Organization for Standardization, 2011.
2. BASILI, Victor R.; CALDIERA, Gianluigi; ROMBACH, H. Dieter. *The Goal Question Metric Approach*. In: Encyclopedia of Software Engineering. Wiley, 1994.