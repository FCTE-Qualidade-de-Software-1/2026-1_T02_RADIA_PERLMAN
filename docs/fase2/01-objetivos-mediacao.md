# 1. Objetivos de Medição (Nível Conceitual)

A Fase 2 do processo de avaliação da ISO/IEC 25040 inicia-se pela definição dos **objetivos de medição**. Estes objetivos traduzem o propósito da avaliação ([Fase 1, §1](../fase1/01-proposito.md)) em metas concretas, estruturadas e rastreáveis, utilizando o paradigma GQM (*Goal-Question-Metric*). Cada objetivo é formulado a partir de um *template* padronizado que explicita o objeto, o propósito, o foco da qualidade, o ponto de vista e o contexto da medição.

Os objetivos definidos aqui derivam diretamente das **três características priorizadas** na [Fase 1 (§5)](../fase1/05-caracteristicas.md): Segurança (P1), Manutenibilidade (P2) e Confiabilidade (P3).

## 1.1 Template GQM para Objetivos

O *template* utilizado para estruturar cada objetivo de medição segue o padrão proposto por Basili et al.:

**Tabela 1.1: Template GQM para Objetivos**

| Estrutura | Campo | Descrição |
|---|---|---|
| **Analisar** | `Objeto da análise` | O que está sendo medido. |
| **para o propósito de** | `Propósito da análise` | Por que está sendo medido (geralmente caracterizar, entender, avaliar, prever, melhorar). |
| **com respeito a** | `Foco da qualidade` | Qual aspecto ou característica de qualidade está em foco. |
| **do ponto de vista do/a**| `Ponto de vista` | Quem está interessado na medição (o stakeholder primário). |
| **no contexto de** | `Contexto` | O ambiente e as circunstâncias da medição. |

## 1.2 Objetivos de Medição Definidos

### G1. Objetivo de Medição - Segurança (P1)

**Tabela 1.2: Objetivo G1 - Segurança**

| Campo | Descrição |
|---|---|
| **Analisar** | o software AcheiUnB (código-fonte, configuração e fluxo de autenticação). |
| **para o propósito de** | **caracterizar** o seu nível de exposição a vulnerabilidades comuns de software web. |
| **com respeito a** | **confidencialidade** na gestão de segredos, **integridade** das configurações de segurança e **autenticidade** no fluxo de login. |
| **do ponto de vista da** | **próxima equipe de desenvolvimento (sucessora)** e do hipotético operador institucional. |
| **no contexto de** | uma avaliação de qualidade para apoiar a decisão de **manter/refatorar** os componentes de autenticação MSAL+JWT e gestão de segredos ([Decisão D2, Fase 1](../fase1/01-proposito.md#13-uso-pretendido-dos-resultados)). |

### G2. Objetivo de Medição - Manutenibilidade (P2)

**Tabela 1.3: Objetivo G2 - Manutenibilidade**

| Campo | Descrição |
|---|---|
| **Analisar** | o código-fonte do *backend* e os artefatos de processo (testes, CI) do AcheiUnB. |
| **para o propósito de** | **diagnosticar** a sua complexidade estrutural, testabilidade e conformidade com padrões de codificação. |
| **com respeito a** | **analisabilidade**, **modificabilidade** e **testabilidade**. |
| **do ponto de vista da** | **próxima equipe de desenvolvimento (sucessora)**. |
| **no contexto de** | uma avaliação de qualidade para **priorizar o backlog** de dívidas técnicas ([Decisão D1, Fase 1](../fase1/01-proposito.md#13-uso-pretendido-dos-resultados)). |

### G3. Objetivo de Medição - Confiabilidade (P3)

**Tabela 1.4: Objetivo G3 - Confiabilidade**

| Campo | Descrição |
|---|---|
| **Analisar** | os componentes de comunicação assíncrona e tempo real (Celery/Redis, WebSockets) do AcheiUnB. |
| **para o propósito de** | **entender** seu comportamento sob condições de falha simuladas. |
| **com respeito a** | **tolerância a falhas** e **recuperabilidade**. |
| **do ponto de vista da** | **próxima equipe de desenvolvimento (sucessora)**. |
| **no contexto de** | uma avaliação em **laboratório (Docker)** para apoiar a decisão de **manter/refatorar** o módulo de chat e a fila de tarefas ([Decisão D2, Fase 1](../fase1/01-proposito.md#13-uso-pretendido-dos-resultados)). |

## Referências

1. BASILI, Victor R.; CALDIERA, Gianluigi; ROMBACH, H. Dieter. The Goal Question Metric Approach. *Encyclopedia of Software Engineering*, 1994.
2. ISO/IEC 25040:2011. *Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Evaluation process*.

## Histórico de versão

| Versão | Data       | Descrição | Autor(es) | Revisor(es) |
| :-- | :-- | :-- | :-- | :-- |
| 1.0 | 2026-06-12 | Definição dos objetivos de medição GQM para as características priorizadas. | Ana Joyce | Júlia, Letícia |
