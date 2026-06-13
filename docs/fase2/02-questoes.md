# 2. Definição de Questões (Nível Operacional)

A partir dos **objetivos de medição (G)** definidos na seção anterior, esta seção deriva um conjunto de **questões (Q)** específicas. Cada questão refina um objetivo, decompondo-o em perguntas concretas que podem ser respondidas por meio de métricas. As questões são o elo entre o nível conceitual (objetivos) e o nível quantitativo (métricas).

Elas são formuladas para cobrir os **atributos de qualidade** em foco (ex: confidencialidade, testabilidade) e para serem diretamente úteis ao **ponto de vista** do stakeholder principal (a próxima equipe de desenvolvimento).

## Questões por Objetivo

### G1. Objetivo de Medição - Segurança (P1)

O objetivo G1 visa caracterizar o nível de exposição a vulnerabilidades. As questões a seguir decompõem este objetivo:

| ID | Questão (Nível Operacional) | Subcaracterística(s) ISO/IEC 25010 |
| :--- | :--- | :--- |
| **Q1.1** | A gestão de segredos da aplicação (ex: `SECRET_KEY`, senhas de banco de dados, chaves de API) está adequadamente protegida contra exposição acidental no código-fonte ou em logs? | Confidencialidade |
| **Q1.2** | As configurações de segurança do framework web (Django) e do servidor de aplicação estão alinhadas com as boas práticas para mitigar ataques comuns (ex: XSS, CSRF, Clickjacking)? | Integridade |
| **Q1.3** | O fluxo de autenticação (MSAL + JWT) valida corretamente a identidade do usuário e protege os tokens de sessão contra interceptação e uso indevido? | Autenticidade, Confidencialidade |

### G2. Objetivo de Medição - Manutenibilidade (P2)

O objetivo G2 foca em diagnosticar a complexidade, testabilidade e conformidade do código. As questões derivadas são:

| ID | Questão (Nível Operacional) | Subcaracterística(s) ISO/IEC 25010 |
| :--- | :--- | :--- |
| **Q2.1** | O código-fonte segue consistentemente os padrões de estilo e formatação definidos pela equipe original, e a sua estrutura de módulos (*apps* Django) é coesa e fracamente acoplada? | Analisabilidade, Modularidade |
| **Q2.2** | Qual é o nível de complexidade ciclomática e o tamanho das funções/métodos nos principais módulos do *backend*? Existem pontos de alta complexidade que dificultam alterações futuras? | Modificabilidade, Analisabilidade |
| **Q2.3** | A suíte de testes automatizados do *backend* fornece cobertura de código suficiente para garantir que novas alterações não introduzam regressões? A ausência de testes no *frontend* representa um risco significativo? | Testabilidade |

### G3. Objetivo de Medição - Confiabilidade (P3)

O objetivo G3 busca entender o comportamento do sistema sob falha em ambiente de laboratório. Suas questões são:

| ID | Questão (Nível Operacional) | Subcaracterística(s) ISO/IEC 25010 |
| :--- | :--- | :--- |
| **Q3.1** | O sistema se comporta de maneira previsível e degrada graciosamente na ocorrência de falhas em serviços externos dos quais depende (ex: indisponibilidade do *broker* Redis)? | Tolerância a Falhas |
| **Q3.2** | O componente de chat (WebSocket) é capaz de restabelecer a comunicação automaticamente após uma queda de conexão? As tarefas assíncronas (Celery) são automaticamente reexecutadas em caso de falha transitória? | Recuperabilidade |

## Histórico de versão

| Versão | Data       | Descrição | Autor(es) | Revisor(es) |
| :-- | :-- | :-- | :-- | :-- |
| 1.0 | 2026-06-12 | Definição das questões GQM para cada objetivo de medição. | Ana Joyce | Luis |
