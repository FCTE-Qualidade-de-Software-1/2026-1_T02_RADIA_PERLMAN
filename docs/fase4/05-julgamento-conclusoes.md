# 5. Julgamento, Conclusões e Sugestões de Melhoria

Esta seção emite o **julgamento final da qualidade** do AcheiUnB com base nas 14
métricas medidas e comparadas aos critérios da [Fase 2, §5](../fase2/05-niveis-pontuacao.md),
apresenta as **conclusões** alinhadas ao propósito da
[Fase 1](../fase1/01-proposito.md) e converte os achados em **sugestões de melhoria
acionáveis**. Na EU3 a execução foi **completa**: as 7 instruções pendentes da EU2
foram realizadas e a coleta inválida de M2.1.1 foi recoletada, eliminando todas as
ressalvas de incompletude do julgamento da entrega anterior.

## 5.1 Julgamento por característica

**Tabela 5.1: julgamento consolidado, derivado da [análise GQM](03-analise-resposta-gqm.md).**

| Característica | Métricas medidas | Julgamento (EU3) | Observação |
|---|---|---|---|
| **Segurança (P1)** | M1.1.1 Aceitável, M1.1.2 Aceitável, M1.2.1 Regular, M1.2.2 Ruim, M1.3.1 Bom, M1.3.2 Aceitável | **Regular, com risco alto restrito à configuração de produção** | Autenticação dinâmica e gestão de segredos sólidas; *hardening* de produção deficiente é o único vetor crítico aberto. |
| **Manutenibilidade (P2)** | M2.1.1 Ruim (83), M2.1.2 Ruim (2 ciclos), M2.2.1/M2.2.2 Regular (combinado), M2.3.1 Bom (83%), M2.3.2 Inaceitável (0) | **Regular, com forte assimetria *backend* / *frontend*** | *Backend* é simples na média, testado e mantém débito de estilo/acoplamento; *frontend* não possui qualquer teste automatizado. |
| **Confiabilidade (P3)** | M3.1.1 Bom (degrada graciosamente), M3.2.1 Bom (reconecta), M3.2.2 Regular (0/13 *retry*) | **Bom, com ressalva no Celery** | Resiliência arquitetural verificada na prática; única pendência é o *retry* nas 13 tarefas assíncronas. |

O julgamento de Manutenibilidade permanece **Regular** e não migra para nível superior:
embora a cobertura do *backend* (83%) seja Boa e a complexidade média seja grau A, a
combinação com (a) 83 violações Ruff, (b) 2 ciclos de *imports* e (c) ausência total
de testes no *frontend* mantém a característica no nível **Regular** quando avaliada
como um todo. O julgamento de Confiabilidade migra de **Regular (parcial) na EU2**
para **Bom (consolidado) na EU3**, refletindo as duas evidências dinâmicas positivas
que entraram (degradação graciosa do Redis e reconexão automática do WebSocket).

## 5.2 Conclusões

O AcheiUnB apresenta um **contraste característico de MVP acadêmico**: uma base de
código **estruturalmente manutenível** (complexidade média grau A, 83% de cobertura
no *backend*) e **arquiteturalmente resiliente** (degradação graciosa frente à queda
do Redis e reconexão automática do WebSocket), convivendo com **imaturidade
operacional** nas configurações de segurança, com **débito de estilo e acoplamento**
no *backend* e com **ausência total de testes no *frontend***.

Quanto ao propósito central da avaliação
([Fase 1, §1](../fase1/01-proposito.md)), conclui-se que:

1. **Não há evidência que justifique uma reescrita completa do *backend*.** A
   manutenibilidade Regular (média grau A, cobertura 83%, débito de estilo
   identificável e ciclos discretos) sustenta a **evolução incremental** pela equipe
   sucessora, em apoio à decisão D2.
2. **O *frontend* exige introdução de testes automatizados.** A inexistência de
   testes (M2.3.2 = 0) é o achado de qualidade mais agudo da avaliação e o único que
   atinge nível **Inaceitável**. O sucessor precisa **adicionar** uma camada nova,
   não refatorar.
3. **O produto não está pronto para produção.** Os 6 itens críticos de configuração
   (M1.2.2, Ruim) precisam ser tratados antes de qualquer implantação aberta à
   comunidade UnB; a ausência de *retry* no Celery (M3.2.2) é um vetor secundário,
   mas precede a operação institucional.
4. **A camada de autenticação está sólida.** A combinação de *cookie* JWT endurecido
   (M1.3.1 = 0 atributos faltantes) com rejeição de manipulação (M1.3.2 = Válida)
   confirma que o trabalho da equipe original em autenticação MSAL+JWT está bem
   feito; não é alvo de refatoração prioritária.
5. **O diagnóstico final está completo** dentro do escopo declarado e é seguro para
   embasar D1 e D2.

## 5.3 Sugestões de melhoria

Em ordem de prioridade, traduzindo os achados em ações concretas para o requisitante:

1. **Bootstrap de testes automatizados no *frontend* - prioridade alta.** Introduzir
   uma suíte mínima com Vitest (testes unitários sobre `web/src/utils/` e
   `web/src/store/`) e/ou Playwright (testes E2E sobre os fluxos principais de busca
   e visualização de itens), adicionando o *script* `test` no `package.json`. Sem
   isso, a equipe sucessora opera com ponto cego total no *client*.
2. **Blindagem do ambiente de produção (Django) - prioridade alta.** Tratar os 6
   itens críticos de M1.2.2: desativar `DEBUG`, gerar `SECRET_KEY`
   criptograficamente segura via variável de ambiente, e habilitar
   `SECURE_SSL_REDIRECT`, `SESSION_COOKIE_SECURE`, `CSRF_COOKIE_SECURE` e
   `SECURE_HSTS_SECONDS`.
3. **Resolução dos 2 ciclos de *imports* - prioridade alta.** Quebrar os ciclos
   `chat ↔ users` e `users ↔ reports` identificados em M2.1.2 (ex.: extrair
   *models* de `Item` para um *app* compartilhado, ou inverter dependências de
   *tasks* via *signals*).
4. **Resiliência assíncrona (Celery) - prioridade alta.** Implementar política de
   `retry` com *exponential backoff* nas 13 tarefas de `chat` e `users`
   identificadas em M3.2.2, priorizando as tarefas críticas (notificações e
   *matching* de itens).
5. **Limpeza dos 83 *warnings* do Ruff - prioridade média.** Tratar
   sistematicamente PLR6301 (*no-self-use*) e PLC0415 (*import-outside-top-level*)
   para reduzir a contagem de M2.1.1 abaixo do limiar de 20 (nível Regular).
6. **Correção das chamadas HTTP sem *timeout* - prioridade média.** Resolver as 3
   ocorrências de B113 (M1.2.1) em `users/views.py`, definindo *timeout* explícito.
7. **Refatoração dos pontos de complexidade - prioridade média.** Reduzir a
   complexidade das 5 funções grau C (M2.2.2), concentradas em
   `UserProfileView`/`UserListView` (`users`) e `ReportViewSet._get_reported_user`
   (`reports`).
8. **Correção do teste em falha - prioridade baixa.** Ajustar o *mock* de
   `test_send_welcome_email_on_first_login` (`users/tests/test_signals.py`) para
   restabelecer 100% de testes passando.

## 5.4 Encerramento

Com base no exposto, a equipe T02 emite, para a EU3, um julgamento de qualidade
**consolidado** para o AcheiUnB nas três características priorizadas:
**Regular em Segurança** (com risco alto restrito à configuração de produção),
**Regular em Manutenibilidade** (com assimetria *backend*/*frontend*) e
**Bom em Confiabilidade** (com ressalva no *retry* das tarefas Celery). A
recomendação explícita é de **não implantação em produção** até a mitigação dos 6
itens de M1.2.2 e da introdução de uma camada mínima de testes no *frontend*. O
diagnóstico fecha-se aqui dentro do escopo declarado e pode embasar diretamente as
decisões D1 (priorização de *backlog*) e D2 (manter / refatorar / introduzir
componentes) pela equipe sucessora.

## Histórico de versão

| Versão | Data       | Descrição | Autor(es) | Revisor(es) |
| :-- | :-- | :-- | :-- | :-- |
| 1.0 | 2026-06-12 | Julgamento final de qualidade, conclusões e sugestões de melhoria. | Samuel Afonso | Davi Casseb, Letícia Hladczuk |
| 2.0 | 2026-06-12 | Correção do julgamento de Manutenibilidade (Excelente → Regular) conforme critérios da Fase 2; exclusão da evidência inválida do Ruff; declaração do caráter parcial do julgamento. | Samuel Afonso | Davi Casseb, Letícia Hladczuk |
| 3.0 | 2026-06-23 | Julgamento consolidado para a EU3: tabela 5.1 com todas as 14 métricas, conclusões reescritas incorporando autenticação dinâmica, *frontend* sem testes e resiliência confirmada; sugestões de melhoria reordenadas em 8 itens. | Luis Eduardo Castro M Lima, Davi Casseb | Letícia Hladczuk |

## Referências

1. ISO/IEC 25040:2011. *Systems and software engineering: Systems and software Quality Requirements and Evaluation (SQuaRE): Evaluation process*. International Organization for Standardization, 2011.
2. BASILI, Victor R.; CALDIERA, Gianluigi; ROMBACH, H. Dieter. *The Goal Question Metric Approach*. In: Encyclopedia of Software Engineering. Wiley, 1994.
3. Django Software Foundation. *Deployment checklist e Security in Django*. Disponível em: <https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/>. Acesso em: 12 jun. 2026.
4. PyCQA. *Bandit Documentation*. Disponível em: <https://bandit.readthedocs.io/>. Acesso em: 12 jun. 2026.
5. Radon. *Radon Documentation: Cyclomatic Complexity*. Disponível em: <https://radon.readthedocs.io/>. Acesso em: 12 jun. 2026.