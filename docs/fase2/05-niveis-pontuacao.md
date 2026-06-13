# 5. Estabelecimento de Níveis de Pontuação e Critérios de Julgamento

Esta seção detalha, para cada métrica definida anteriormente, os **níveis de pontuação** e os **critérios de julgamento** que serão utilizados para interpretar os resultados. Este passo é fundamental para traduzir os dados brutos coletados na [Fase 3](../fase3/index.md) em respostas qualitativas e acionáveis para as questões GQM, permitindo confirmar ou refutar as hipóteses.

Os critérios são explícitos, detalhados e diretamente alinhados com as necessidades dos stakeholders e o propósito da avaliação.

## Critérios de Julgamento por Métrica

### G1. Objetivo de Medição - Segurança (P1)

**M1.1.1:** Número de segredos (chaves de API, senhas, `SECRET_KEY`) encontrados no código-fonte.

**Tabela 5.1: Níveis de Pontuação M1.1.1**

| Nível (Valor Medido) | Critério de Julgamento |
| :--- | :--- |
| 0 | **Aceitável:** Nenhum segredo foi encontrado no código-fonte. A gestão de segredos segue a boa prática de separação de configuração e código. |
| > 0 | **Inaceitável:** Pelo menos um segredo foi encontrado. Esta é uma falha crítica de segurança que expõe o sistema a comprometimento imediato. |

**M1.1.2:** Existência de arquivo de variáveis de ambiente (`.env`) no `.gitignore`.

**Tabela 5.2: Níveis de Pontuação M1.1.2**

| Nível (Valor Medido) | Critério de Julgamento |
| :--- | :--- |
| Sim | **Aceitável:** O arquivo de variáveis de ambiente é corretamente ignorado pelo controle de versão, prevenindo o vazamento acidental de segredos. |
| Não | **Inaceitável:** O arquivo não é ignorado, criando um risco de que segredos sejam versionados acidentalmente em commits futuros. |

**M1.2.1:** Contagem de vulnerabilidades de segurança de criticidade Média ou Alta reportadas pela ferramenta `Bandit`.

**Tabela 5.3: Níveis de Pontuação M1.2.1**

| Nível (Contagem) | Critério de Julgamento |
| :--- | :--- |
| 0 | **Bom:** Nenhuma vulnerabilidade de criticidade média ou alta foi reportada, indicando uma boa aderência a práticas de codificação segura. |
| 1-3 | **Regular:** Um baixo número de vulnerabilidades foi encontrado. Requer investigação e correção, mas não indica um problema sistêmico. |
| > 3 | **Ruim:** Um número significativo de vulnerabilidades foi reportado, sugerindo falhas sistêmicas na aplicação de práticas de codificação segura. |

**M1.2.2:** Checklist de conformidade das configurações de segurança do Django.

**Tabela 5.4: Níveis de Pontuação M1.2.2**

| Nível (% de Conformidade) | Critério de Julgamento |
| :--- | :--- |
| > 90% | **Bom:** As configurações de segurança do framework estão robustas e bem alinhadas com as melhores práticas recomendadas pela documentação. |
| 70-90% | **Regular:** A maioria das configurações essenciais está aplicada, mas existem lacunas que representam riscos de segurança a serem mitigados. |
| < 70% | **Ruim:** A configuração de segurança é deficiente, expondo o sistema a múltiplos vetores de ataque conhecidos para o framework. |

**M1.3.1:** Checklist de atributos de segurança do *cookie* de sessão JWT.

**Tabela 5.5: Níveis de Pontuação M1.3.1**

| Nível (Atributos Faltantes) | Critério de Julgamento |
| :--- | :--- |
| 0 (`HttpOnly`, `Secure`, `SameSite` presentes) | **Bom:** O cookie de sessão está adequadamente protegido contra ataques de script (XSS) e de falsificação de solicitação entre sites (CSRF). |
| 1 | **Regular:** A ausência de um dos atributos de segurança representa uma proteção parcial e um risco que precisa ser endereçado. |
| > 1 | **Ruim:** A proteção do cookie é deficiente, tornando-o vulnerável a múltiplos vetores de ataque e comprometendo a segurança da sessão. |

**M1.3.2:** Validade da assinatura do token JWT sob tentativa de manipulação.

**Tabela 5.6: Níveis de Pontuação M1.3.2**

| Nível (Valor Medido) | Critério de Julgamento |
| :--- | :--- |
| Válida (manipulação foi rejeitada) | **Aceitável:** O mecanismo de assinatura e validação do token está funcionando como esperado, protegendo contra falsificação. |
| Inválida (manipulação foi aceita) | **Inaceitável:** Uma falha crítica foi identificada no mecanismo de validação do token, permitindo que um ator malicioso forje identidades. |

### G2. Objetivo de Medição - Manutenibilidade (P2)

**M2.1.1:** Contagem de violações reportadas pelo linter `Ruff`.

**Tabela 5.7: Níveis de Pontuação M2.1.1**

| Nível (Contagem) | Critério de Julgamento |
| :--- | :--- |
| 0 | **Bom:** O código está em total conformidade com os padrões de estilo e qualidade definidos no projeto. |
| 1-20 | **Regular:** Existem pequenas inconsistências de estilo ou qualidade, mas que têm baixo impacto na manutenibilidade e podem ser corrigidas facilmente. |
| > 20 | **Ruim:** Há uma inconsistência sistêmica nos padrões do código, o que pode dificultar a leitura, a análise e a contribuição de novos desenvolvedores. |

**M2.1.2:** Número de dependências circulares entre *apps* Django.

**Tabela 5.8: Níveis de Pontuação M2.1.2**

| Nível (Contagem) | Critério de Julgamento |
| :--- | :--- |
| 0 | **Bom:** Os módulos do sistema estão bem desacoplados, o que facilita a modificação, o teste e o reuso de forma isolada. |
| > 0 | **Ruim:** Existe acoplamento excessivo entre os módulos, uma condição que dificulta a manutenção, aumenta a complexidade e pode gerar efeitos colaterais inesperados durante o desenvolvimento. |

**M2.2.1 & M2.2.2:** Complexidade Ciclomática (`radon`).

**Tabela 5.9: Níveis de Pontuação M2.2.1 & M2.2.2**

| Nível (Valor Medido) | Critério de Julgamento |
| :--- | :--- |
| Média < 5 **e** Contagem(>10) = 0 | **Bom:** O código é predominantemente simples, de fácil entendimento, teste e modificação. |
| Média entre 5-10 **ou** Contagem(>10) entre 1 e 5 | **Regular:** Existem alguns pontos de complexidade no código que merecem atenção e são candidatos a uma futura refatoração para melhorar a manutenibilidade. |
| Média > 10 **ou** Contagem(>10) > 5 | **Ruim:** A complexidade do código é alta, seja na média ou em múltiplos pontos específicos, indicando um débito técnico que dificulta a manutenção. |

**M2.3.1:** Percentual de cobertura de linha (*line coverage*) da suíte de testes do *backend*.

**Tabela 5.10: Níveis de Pontuação M2.3.1**

| Nível (% de Cobertura) | Critério de Julgamento |
| :--- | :--- |
| > 80% | **Bom:** A suíte de testes automatizados fornece um alto grau de confiança para detectar regressões em futuras alterações. |
| 60-80% | **Regular:** A cobertura é intermediária. As funcionalidades críticas provavelmente estão cobertas, mas casos de borda e fluxos menos comuns podem estar expostos a regressões. |
| < 60% | **Ruim:** A baixa cobertura de testes representa um risco significativo de que alterações no código introduzam regressões não detectadas. |

**M2.3.2:** Número de arquivos de teste no diretório do *frontend*.

**Tabela 5.11: Níveis de Pontuação M2.3.2**

| Nível (Contagem) | Critério de Julgamento |
| :--- | :--- |
| > 0 | **Aceitável:** Existe uma iniciativa, mesmo que inicial, de implementar testes automatizados no frontend. |
| 0 | **Inaceitável:** A ausência total de testes automatizados no frontend representa um ponto cego completo para a qualidade da SPA, impossibilitando a detecção de regressões de forma automatizada. |

### G3. Objetivo de Medição - Confiabilidade (P3)

**M3.1.1:** Comportamento observado do sistema após a parada do contêiner Redis.

**Tabela 5.12: Níveis de Pontuação M3.1.1**

| Nível (Ordinal) | Critério de Julgamento |
| :--- | :--- |
| 4. Degrada graciosamente | **Bom:** O sistema demonstra resiliência, tratando a falha de forma controlada e informando o usuário ou mantendo outras funcionalidades operantes. |
| 3. Erro amigável | **Regular:** O sistema falha, mas de forma controlada, apresentando uma mensagem de erro que não expõe detalhes internos. |
| 2. Erro 500 (Crash) | **Ruim:** A falha no serviço dependente causa um erro não tratado na aplicação, impactando negativamente a experiência do usuário. |
| 1. Crash total | **Inaceitável:** A falha de um componente secundário causa a parada completa de toda a aplicação, demonstrando baixa tolerância a falhas. |

**M3.2.1:** Capacidade de reconexão automática do cliente WebSocket.

**Tabela 5.13: Níveis de Pontuação M3.2.1**

| Nível (Valor Medido) | Critério de Julgamento |
| :--- | :--- |
| Sim | **Bom:** A aplicação oferece uma boa experiência de usuário ao recuperar a comunicação em tempo real de forma transparente após uma interrupção. |
| Não | **Ruim:** A ausência de reconexão automática prejudica a usabilidade do chat, exigindo uma ação manual do usuário (ex: recarregar a página) para restabelecer a comunicação. |

**M3.2.2:** Existência de política de `retry` para tarefas Celery.

**Tabela 5.14: Níveis de Pontuação M3.2.2**

| Nível (Valor Medido) | Critério de Julgamento |
| :--- | :--- |
| Sim (para tarefas críticas) | **Bom:** O sistema está preparado para lidar com falhas transitórias durante a execução de tarefas assíncronas importantes. |
| Não | **Regular:** Existe um risco de perda de execução de tarefas em caso de falhas transitórias. A criticidade deste achado depende da importância da tarefa. |

## Referências

1. ISO/IEC 25040:2011. *Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Evaluation process*.
2. BASILI, Victor R.; CALDIERA, Gianluigi; ROMBACH, H. Dieter. The Goal Question Metric Approach. *Encyclopedia of Software Engineering*, 1994.

## Histórico de versão

| Versão | Data       | Descrição | Autor(es) | Revisor(es) |
| :-- | :-- | :-- | :-- | :-- |
| 1.0 | 2026-06-12 | Definição dos níveis de pontuação e critérios de julgamento para cada métrica. | Luis | Ana Joyce, Letícia |
