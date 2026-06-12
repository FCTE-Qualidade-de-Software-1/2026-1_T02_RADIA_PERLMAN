# Fase 3: Projeto da Avaliação (Plano de Avaliação)

A [Fase 2](../fase2/index.md) especificou **o que medir**: três objetivos GQM (G1
Segurança, G2 Manutenibilidade, G3 Confiabilidade), oito questões (Q1.1 a Q3.2), as
hipóteses associadas, treze métricas (M1.1.1 a M3.2.2) e os níveis de pontuação com
critérios de julgamento explícitos.

A Fase 3, conforme a ISO/IEC 25040, responde a **como executar a medição**. Ela produz o
**Plano de Avaliação**: o documento que torna a coleta da [Fase 4](../fase4/index.md)
**repetível e reprodutível**, isto é, capaz de ser reexecutada por outro avaliador (ou por
uma futura equipe da disciplina) chegando aos mesmos resultados sobre o mesmo
*snapshot* do AcheiUnB.

## Estrutura da Fase 3

| Seção | Conteúdo | Critério da rubrica atendido |
|---|---|---|
| [1. Método e repetibilidade das instruções](01-metodo-instrucoes.md) | Justificativa dos métodos de avaliação escolhidos e instruções passo a passo, por métrica, para obtenção das medidas. | F3-C1 |
| [2. Recursos e ambiente de avaliação](02-recursos-ambiente.md) | Requisitos de hardware e software, massa de dados, conhecimento exigido dos avaliadores e procedimento de preparação do ambiente. | F3-C2 |
| [3. Cronograma da avaliação](03-cronograma.md) | Distribuição das atividades de execução (Fase 4) no tempo e entre os membros da equipe. | F3-C3 |

## Rastreabilidade com as fases anteriores

O Plano de Avaliação foi construído **a partir da especificação de medição da Fase 2**,
e não de forma isolada:

- Cada **instrução de coleta** da seção [1](01-metodo-instrucoes.md) referencia
  explicitamente a métrica (M) da [Fase 2, §4](../fase2/04-metricas.md) que ela
  operacionaliza, preservando o instrumento/método ali declarado;
- O **ambiente** da seção [2](02-recursos-ambiente.md) implementa a decisão de execução
  **local containerizada (Docker)** registrada na
  [Fase 1, §6.2.3](../fase1/06-escopo.md#623-ambiente-de-execucao) e suporta tanto a
  análise estática (G1, G2) quanto os cenários de falha em laboratório (G3);
- O **cronograma** da seção [3](03-cronograma.md) aloca esforço na ordem de prioridade
  P1 > P2 > P3 estabelecida na [Fase 1, §5.5](../fase1/05-caracteristicas.md#55-resultado-da-priorizacao)
  e respeita a estratégia de **cobertura progressiva em anéis** da
  [Fase 1, §6.4](../fase1/06-escopo.md#64-plano-de-cobertura-progressiva).

## Limites desta fase

!!! info "O que a Fase 3 não faz"
    A Fase 3 **não coleta dados** nem emite julgamentos. Toda execução (obtenção das
    medidas, registro dos dados brutos, comparação com os níveis de pontuação e
    respostas às questões GQM) pertence à [Fase 4](../fase4/index.md), que seguirá
    integralmente as instruções aqui definidas.

## Histórico de versão

| Versão | Data       | Descrição | Autor(es) | Revisor(es) |
| :-- | :-- | :-- | :-- | :-- |
| 1.0 | 2026-06-12 | Versão inicial da visão geral da Fase 3. | Davi Casseb | Samuel Afonso |
