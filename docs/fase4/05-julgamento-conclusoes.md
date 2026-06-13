# 5. Julgamento, Conclusões e Sugestões de Melhoria

Esta seção emite o **julgamento final da qualidade** do AcheiUnB com base nas métricas já
medidas e comparadas aos critérios da [Fase 2, §5](../fase2/05-niveis-pontuacao.md),
apresenta as **conclusões** alinhadas ao propósito da
[Fase 1](../fase1/01-proposito.md) e converte os achados em **sugestões de melhoria
acionáveis**. O julgamento respeita o estado parcial da execução
([Fase 4, Tabela 4.1](index.md#estado-da-execucao)): caracteriza com firmeza o que foi
medido e mantém em aberto o que ainda depende de coleta.

## 5.1 Julgamento por característica

**Tabela 5.1: julgamento consolidado, derivado da [análise GQM](03-analise-resposta-gqm.md).**

| Característica | Métricas medidas | Julgamento (EU2) | Observação |
|---|---|---|---|
| **Segurança (P1)** | M1.1.1 Aceitável, M1.1.2 Aceitável, M1.2.1 Regular, M1.2.2 Ruim | **Regular, com risco alto de configuração** | Gestão de segredos controlada; *hardening* de produção deficiente. Q1.3 (autenticação dinâmica) pendente. |
| **Manutenibilidade (P2)** | M2.2.1 grau A + M2.2.2 (5 funções > 10) → Regular | **Regular** | Código simples na média, com débito pontual concentrado em `users`. Evidência do Ruff (M2.1.1) invalidada; cobertura (Q2.3) pendente. |
| **Confiabilidade (P3)** | M3.2.2 Regular (0/13 tarefas com *retry*) | **Regular (parcial)** | Fragilidade confirmada nas tarefas Celery; reconexão WS (M3.2.1) e queda do Redis (M3.1.1) pendentes. |

O julgamento de Manutenibilidade é **Regular**, e não "Excelente": embora a complexidade
média seja grau A, a presença de **5 funções acima do limiar de complexidade** enquadra a
característica, pelo critério conjunto da [Fase 2, §5](../fase2/05-niveis-pontuacao.md),
no nível **Regular**. Atribuir "Excelente" contrariaria os próprios critérios de
julgamento definidos no plano. Além disso, o resultado do Ruff (M2.1.1) **não** é
considerado: o arquivo de log foi gravado com 0 byte e a métrica precisa ser recoletada
([§3.1](03-analise-resposta-gqm.md#31-sintese-dos-resultados)).

## 5.2 Conclusões

O AcheiUnB apresenta um **contraste característico de MVP acadêmico**: uma base de código
**estruturalmente manutenível** - complexidade média baixa (grau A) e débito técnico
localizado e identificável - convivendo com **imaturidade operacional** nas configurações
de segurança e na resiliência dos serviços assíncronos.

Quanto ao propósito central da avaliação
([Fase 1, §1](../fase1/01-proposito.md)), conclui-se que:

1. **Não há evidência que justifique uma reescrita completa do *backend*.** A
   manutenibilidade Regular (média grau A, com pontos pontuais de refatoração) sustenta a
   **evolução incremental** pela equipe sucessora, em apoio à decisão D2.
2. **O produto não está pronto para produção.** Os 6 itens críticos de configuração
   (M1.2.2, Ruim) e a ausência de *retry* no Celery (M3.2.2) precisam ser tratados antes
   de qualquer implantação aberta à comunidade UnB.
3. **O diagnóstico ainda é parcial.** As características de Segurança dinâmica,
   Testabilidade e Confiabilidade em laboratório dependem das instruções pendentes; o
   julgamento atual é firme apenas sobre as quatro questões respondidas e **não deve ser
   lido como veredito final de qualidade do produto**.

## 5.3 Sugestões de melhoria

Em ordem de prioridade, traduzindo os achados em ações concretas para o requisitante:

1. **Blindagem do ambiente de produção (Django) - prioridade alta.** Tratar os 6 itens
   críticos de M1.2.2: desativar `DEBUG`, gerar `SECRET_KEY` criptograficamente segura via
   variável de ambiente, e habilitar `SECURE_SSL_REDIRECT`, `SESSION_COOKIE_SECURE`,
   `CSRF_COOKIE_SECURE` e `SECURE_HSTS_SECONDS`.
2. **Resiliência assíncrona (Celery) - prioridade alta.** Implementar política de `retry`
   com *exponential backoff* nas 13 tarefas de `chat` e `users` identificadas em M3.2.2,
   priorizando as tarefas críticas (notificações e *matching* de itens).
3. **Correção das chamadas HTTP sem *timeout* - prioridade média.** Resolver as 3
   ocorrências de B113 (M1.2.1) em `users/views.py`, definindo *timeout* explícito.
4. **Refatoração dos pontos de complexidade - prioridade média.** Reduzir a complexidade
   das 5 funções grau C (M2.2.2), concentradas em `UserProfileView`/`UserListView`
   (`users`) e `ReportViewSet._get_reported_user` (`reports`).
5. **Conclusão da avaliação - prioridade de processo.** Executar as **sete instruções
   pendentes** (I-05, I-06, I-08, I-10, I-11, I-12, I-13) e **recoletar M2.1.1 (Ruff)**,
   para que Q1.3, Q2.1, Q2.3 e Q3.1 sejam respondidas e o diagnóstico de qualidade fique
   completo, embasando plenamente as decisões D1 e D2.

## 5.4 Encerramento

Com base no exposto, a equipe T02 emite, para a EU2, um julgamento de qualidade
**parcial e Regular** para o AcheiUnB nas três características priorizadas, com recomendação
explícita de **não implantação em produção** até a mitigação dos riscos de configuração e
de resiliência, e de **conclusão das instruções pendentes** para o fechamento do
diagnóstico na entrega final.

## Histórico de versão

| Versão | Data       | Descrição | Autor(es) | Revisor(es) |
| :-- | :-- | :-- | :-- | :-- |
| 1.0 | 2026-06-12 | Julgamento final de qualidade, conclusões e sugestões de melhoria. | Samuel Afonso | Davi Casseb, Letícia Hladczuk |
| 2.0 | 2026-06-12 | Correção do julgamento de Manutenibilidade (Excelente → Regular) conforme critérios da Fase 2; exclusão da evidência inválida do Ruff; declaração do caráter parcial do julgamento. | Samuel Afonso | Davi Casseb, Letícia Hladczuk |

## Referências

1. ISO/IEC 25040:2011. *Systems and software engineering: Systems and software Quality Requirements and Evaluation (SQuaRE): Evaluation process*. International Organization for Standardization, 2011.
2. BASILI, Victor R.; CALDIERA, Gianluigi; ROMBACH, H. Dieter. *The Goal Question Metric Approach*. In: Encyclopedia of Software Engineering. Wiley, 1994.
3. Django Software Foundation. *Deployment checklist e Security in Django*. Disponível em: <https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/>. Acesso em: 12 jun. 2026.
4. PyCQA. *Bandit Documentation*. Disponível em: <https://bandit.readthedocs.io/>. Acesso em: 12 jun. 2026.
5. Radon. *Radon Documentation: Cyclomatic Complexity*. Disponível em: <https://radon.readthedocs.io/>. Acesso em: 12 jun. 2026.