# 4. Seleção de Métricas (Nível Quantitativo)

Nesta seção, cada **questão (Q)** é associada a uma ou mais **métricas (M)**. As métricas são as medidas quantitativas ou qualitativas que serão coletadas para responder às questões e, consequentemente, testar as hipóteses.

Para cada métrica, são definidos seu tipo, o instrumento ou método de coleta e uma avaliação de suas próprias características de qualidade (simplicidade, objetividade, validade), garantindo que a medição seja confiável e reprodutível.

## Métricas por Questão

### G1. Objetivo de Medição - Segurança (P1)

#### Q1.1: A gestão de segredos está adequadamente protegida?

| ID | Métrica | Tipo | Instrumento / Método | Qualidade da Métrica |
| :--- | :--- | :--- | :--- | :--- |
| **M1.1.1** | Número de segredos (chaves de API, senhas, `SECRET_KEY`) encontrados no código-fonte. | Contagem | Análise estática com `trufflehog` e inspeção manual do `settings.py`. | Objetividade, Simplicidade |
| **M1.1.2** | Existência de arquivo de variáveis de ambiente (`.env`) no `.gitignore`. | Booleano | Inspeção do arquivo `.gitignore`. | Objetividade, Simplicidade |

#### Q1.2: As configurações de segurança do framework estão alinhadas com as boas práticas?

| ID | Métrica | Tipo | Instrumento / Método | Qualidade da Métrica |
| :--- | :--- | :--- | :--- | :--- |
| **M1.2.1** | Contagem de vulnerabilidades de segurança de criticidade Média ou Alta reportadas pela ferramenta `Bandit`. | Contagem | Execução do `Bandit` sobre o código-fonte do *backend*. | Objetividade, Validade |
| **M1.2.2** | Checklist de conformidade das configurações de segurança do Django. | Percentual | Inspeção manual do `settings.py` contra uma lista de verificação baseada na documentação do Django. | Validade, Objetividade |

#### Q1.3: O fluxo de autenticação e sessão é seguro?

| ID | Métrica | Tipo | Instrumento / Método | Qualidade da Métrica |
| :--- | :--- | :--- | :--- | :--- |
| **M1.3.1** | Checklist de atributos de segurança do *cookie* de sessão JWT. | Checklist | Análise dinâmica inspecionando cabeçalhos de resposta HTTP durante o login. | Objetividade, Validade |
| **M1.3.2** | Validade da assinatura do token JWT sob tentativa de manipulação. | Booleano | Análise dinâmica tentando decodificar e verificar um token capturado. | Validade |

### G2. Objetivo de Medição - Manutenibilidade (P2)

#### Q2.1: O código segue padrões e é modular?

| ID | Métrica | Tipo | Instrumento / Método | Qualidade da Métrica |
| :--- | :--- | :--- | :--- | :--- |
| **M2.1.1** | Contagem de violações reportadas pelo linter `Ruff`. | Contagem | Execução do `Ruff` sobre o código do *backend*. | Objetividade, Validade |
| **M2.1.2** | Número de dependências circulares entre *apps* Django. | Contagem | Análise estática com `django-extensions` (`./manage.py graph_models`). | Objetividade |

#### Q2.2: Qual o nível de complexidade do código?

| ID | Métrica | Tipo | Instrumento / Método | Qualidade da Métrica |
| :--- | :--- | :--- | :--- | :--- |
| **M2.2.1** | Complexidade ciclomática média por função/método. | Média | Análise estática com a ferramenta `radon`. | Objetividade, Validade |
| **M2.2.2** | Contagem de funções/métodos com complexidade ciclomática "Alta" (>10). | Contagem | Análise estática com `radon`. | Simplicidade, Objetividade |

#### Q2.3: A cobertura de testes é suficiente?

| ID | Métrica | Tipo | Instrumento / Método | Qualidade da Métrica |
| :--- | :--- | :--- | :--- | :--- |
| **M2.3.1** | Percentual de cobertura de linha (*line coverage*) da suíte de testes do *backend*. | Percentual | Execução do `pytest` com o plugin `pytest-cov`. | Objetividade, Validade |
| **M2.3.2** | Número de arquivos de teste no diretório do *frontend* (`web/`). | Contagem | Inspeção manual da estrutura de diretórios. | Simplicidade, Objetividade |

### G3. Objetivo de Medição - Confiabilidade (P3)

#### Q3.1: O sistema é tolerante a falhas em serviços externos?

| ID | Métrica | Tipo | Instrumento / Método | Qualidade da Métrica |
| :--- | :--- | :--- | :--- | :--- |
| **M3.1.1** | Comportamento observado do sistema após a parada do contêiner Redis. | Ordinal | Execução de cenário de teste em laboratório (Docker) e observação da resposta da API. | Validade |

#### Q3.2: O sistema é capaz de se recuperar de falhas de conexão ou de tarefas?

| ID | Métrica | Tipo | Instrumento / Método | Qualidade da Métrica |
| :--- | :--- | :--- | :--- | :--- |
| **M3.2.1** | Capacidade de reconexão automática do cliente WebSocket. | Booleano | Cenário de teste em laboratório: derrubar e restaurar a conexão de rede do cliente e observar o comportamento do chat. | Validade, Objetividade |
| **M3.2.2** | Existência de política de `retry` para tarefas Celery. | Booleano | Inspeção do código onde as tarefas são definidas e chamadas (busca por `retry=True` ou blocos `try...except` com lógica de `retry`). | Objetividade |

## Histórico de versão

| Versão | Data       | Descrição | Autor(es) | Revisor(es) |
| :-- | :-- | :-- | :-- | :-- |
| 1.0 | 2026-06-12 | Definição das métricas para cada questão GQM. | Julia | Ana Joyce |
