# Análise e Resposta GQM

De acordo com os dados obtidos foi possivel retomar as questçoes levantadas na Fase 2, conforme a seguinte tabela.

| Objetivo (Goal) | ID Questão | Questão (Nível Operacional) | Métricas Correspondentes |
| --- | --- | --- | --- |
| G1: Analisar Segurança | Q1.1 | A gestão de segredos da aplicação (ex: `SECRET_KEY`, senhas de banco de dados, chaves de API) está adequadamente protegida contra exposição acidental no código-fonte ou em logs? | M1.1.1: N° de segredos no códigoM1.1.2: .env no .gitignore |
| G1: Analisar Segurança | Q1.2 | As configurações de segurança do framework web (Django) e do servidor de aplicação estão alinhadas com as boas práticas para mitigar ataques comuns (ex: XSS, CSRF, Clickjacking)? | M1.2.1: Contagem de M/H (Bandit)M1.2.2: Checklist de config. Django |
| G1: Analisar Segurança | Q1.3 | O fluxo de autenticação (MSAL + JWT) valida corretamente a identidade do usuário e protege os tokens de sessão contra interceptação e uso indevido? | M1.3.1: Checklist de atributos do cookieM1.3.2: Validade da assinatura JWT |
| G2: Analisar Manutenibilidade | Q2.1 | O código-fonte segue consistentemente os padrões de estilo e formatação definidos pela equipe original, e a sua estrutura de módulos (apps Django) é coesa e fracamente acoplada? | M2.1.1: Violações (Ruff)M2.1.2: Dependências circulares |
| G2: Analisar Manutenibilidade | Q2.2 | Qual é o nível de complexidade ciclomática e o tamanho das funções/métodos nos principais módulos do backend? Existem pontos de alta complexidade que dificultam alterações futuras? | M2.2.1: Complexidade ciclomática médiaM2.2.2: Contagem de funções complexas |
| G2: Analisar Manutenibilidade | Q2.3 | A suíte de testes automatizados do backend fornece cobertura de código suficiente para garantir que novas alterações não introduzam regressões? A ausência de testes no frontend representa um risco significativo? | M2.3.1: Cobertura de testes (backend)M2.3.2: N° de testes (frontend) |
| G3: Analisar Confiabilidade | Q3.1 | O sistema se comporta de maneira previsível e degrada graciosamente na ocorrência de falhas em serviços externos dos quais depende (ex: indisponibilidade do broker Redis)? | M3.1.1: Comportamento sob queda do Redis |
| G3: Analisar Confiabilidade | Q3.2 | O componente de chat (WebSocket) é capaz de restabelecer a comunicação automaticamente após uma queda de conexão? As tarefas assíncronas (Celery) são automaticamente reexecutadas em caso de falha transitória? | M3.2.1: Reconexão do WebSocketM3.2.2: Política de retry (Celery) |


## Histórico de versão

| Versão | Data       | Descrição | Autor(es) | Revisor(es) |
| :-- | :-- | :-- | :-- | :-- |
| 1.0 | 2026-06-12 | Análise dos dados coletados e resposta às questões e objetivos GQM. | Samuel Afonso | Davi Casseb, Letícia Hladczuk |

## Referências

1. ISO/IEC 25040:2011. *Systems and software engineering: Systems and software Quality Requirements and Evaluation (SQuaRE): Evaluation process*. International Organization for Standardization, 2011.
2. BASILI, Victor R.; CALDIERA, Gianluigi; ROMBACH, H. Dieter. *The Goal Question Metric Approach*. In: Encyclopedia of Software Engineering. Wiley, 1994.
3. Django Software Foundation. *Deployment checklist e Security in Django*. Disponível em: <https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/>. Acesso em: 12 jun. 2026.
4. PyCQA. *Bandit Documentation*. Disponível em: <https://bandit.readthedocs.io/>. Acesso em: 12 jun. 2026.
5. Radon. *Radon Documentation: Cyclomatic Complexity*. Disponível em: <https://radon.readthedocs.io/>. Acesso em: 12 jun. 2026.
