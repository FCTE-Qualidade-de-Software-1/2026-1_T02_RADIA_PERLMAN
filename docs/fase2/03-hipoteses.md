# 3. Definição de Hipóteses (Nível Operacional)

Para cada **questão (Q)** definida, formulamos uma **hipótese (H)** correspondente. A hipótese é uma afirmação ou suposição que se espera verificar durante a medição. É uma "resposta esperada" para a questão, baseada na análise preliminar do produto realizada na [Fase 1](../fase1/index.md). As métricas, a serem definidas na próxima seção, servirão como instrumento para confirmar ou refutar cada uma destas hipóteses.

## Hipóteses por Questão

### G1. Objetivo de Medição - Segurança (P1)

| ID | Questão | Hipótese |
| :--- | :--- | :--- |
| **Q1.1** | A gestão de segredos está adequadamente protegida? | **H1.1:** Acredita-se que existem segredos, como a `SECRET_KEY` do Django, versionados diretamente no código-fonte (em `settings.py`), representando uma falha crítica de confidencialidade, conforme [suspeita inicial na Fase 1](../fase1/03-software.md#36-restricoes-e-premissas-tecnicas). |
| **Q1.2** | As configurações de segurança do framework estão alinhadas com as boas práticas? | **H1.2:** A hipótese é que a configuração padrão do Django oferece uma boa linha de base de proteção, mas que existem lacunas (configurações não otimizadas ou ausentes) na implementação específica do AcheiUnB, especialmente em relação a cabeçalhos de segurança HTTP e políticas de CORS. |
| **Q1.3** | O fluxo de autenticação e sessão é seguro? | **H1.3:** Espera-se que o fluxo de validação de token JWT no backend seja funcional, mas que a configuração dos *cookies* de sessão (atributos `Secure`, `HttpOnly`, `SameSite`) possa não ser a mais restritiva, abrindo vetores de ataque em potencial. |

### G2. Objetivo de Medição - Manutenibilidade (P2)

| ID | Questão | Hipótese |
| :--- | :--- | :--- |
| **Q2.1** | O código segue padrões e é modular? | **H2.1:** A hipótese é que o código do *backend* demonstra alta conformidade com os formatadores (Black) e linters (Ruff) já presentes no CI, mas que a análise de acoplamento revelará dependências circulares ou acoplamento excessivo entre alguns *apps* Django. |
| **Q2.2** | Qual o nível de complexidade do código? | **H2.2:** Acredita-se que a maioria do código terá baixa complexidade ciclomática, mas que módulos específicos com lógica de negócio mais densa (ex: `users` com o *matching* de itens, ou `chat`) apresentarão funções com complexidade elevada, sendo os principais candidatos a refatoração. |
| **Q2.3** | A cobertura de testes é suficiente? | **H2.3:** A hipótese é que a cobertura de testes do *backend* será intermediária (na faixa de 60-80%), com áreas críticas (autenticação, CRUDs principais) bem testadas, mas com falhas de cobertura em casos de borda. A ausência de testes no *frontend* será confirmada como um ponto cego total para a qualidade da SPA. |

### G3. Objetivo de Medição - Confiabilidade (P3)

| ID | Questão | Hipótese |
| :--- | :--- | :--- |
| **Q3.1** | O sistema é tolerante a falhas em serviços externos? | **H3.1:** Espera-se que uma falha no Redis cause a interrupção imediata de todas as funcionalidades que dependem dele (fila de tarefas Celery e *layer* de canais do WebSocket), sem um mecanismo de *fallback* ou degradação graciosa, impactando o chat e o *matching* de itens. |
| **Q3.2** | O sistema é capaz de se recuperar de falhas de conexão ou de tarefas? | **H3.2:** A hipótese é que nem o cliente WebSocket (`socket.io-client`) nem o servidor (Django Channels) possuem uma lógica de *retry* ou reconexão automática configurada por padrão, exigindo que o usuário recarregue a página para restabelecer o chat. Para o Celery, espera-se que tarefas falhas não sejam automaticamente reenfileiradas, a menos que explicitamente programadas para isso. |

## Histórico de versão

| Versão | Data       | Descrição | Autor(es) | Revisor(es) |
| :-- | :-- | :-- | :-- | :-- |
| 1.0 | 2026-06-12 | Definição das hipóteses para cada questão GQM. | Júlia | Luis |
