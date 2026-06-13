# Julgamento, Conclusões e Sugestões de Melhoria

### Julgamentos

A análise das métricas revela um forte contraste entre a excelente qualidade estrutural do código e a fragilidade das configurações de infraestrutura e segurança. O código-fonte apresenta alta legibilidade e modularidade, com zero violações apontadas pelo Ruff e uma nota "A" em complexidade ciclomática pelo Radon. Isso evidencia que houve um foco louvável na eficiência da escrita e na clareza estrutural. No entanto, as falhas críticas nas configurações do Django (como `DEBUG=True` e ausência de proteção em cookies) e a falta de resiliência nas tarefas do Celery demonstram que a aplicação ainda carece de maturidade operacional para enfrentar um ambiente de produção.

---

### Conclusões

O projeto AcheiUnB possui uma base de código legada altamente viável e manutenível. A baixa complexidade e a boa formatação indicam que não há necessidade de uma reescrita completa do *backend*; a fundação atual permite que a equipe assuma a evolução do software com previsibilidade. Contudo, para garantir a efetividade da entrega final do produto, o direcionamento estratégico deve mudar temporariamente. O sistema não pode ser considerado pronto para o usuário final até que os riscos de segurança sejam mitigados e os serviços assíncronos sejam capazes de se recuperar de falhas transitórias.

---

### Sugestões de Melhoria

* **Blindagem do Ambiente de Produção (Django):** Tratar imediatamente os 6 alertas críticos gerados no checklist de configuração. É estritamente necessário desativar o modo `DEBUG`, gerar uma `SECRET_KEY` criptograficamente segura via variáveis de ambiente, e forçar o tráfego seguro habilitando `SECURE_SSL_REDIRECT`, `SESSION_COOKIE_SECURE` e `CSRF_COOKIE_SECURE`.
* **Resiliência Assíncrona (Celery):** Implementar mecanismos de *retry* nas 13 tarefas identificadas nos módulos de `chat` e `users`. A adoção de uma política de retentativa com *exponential backoff* garantirá que o sistema lide de forma robusta com instabilidades temporárias de rede ou do *broker*, sem perder o processamento de dados.
* **Gestão da Dívida Técnica:** Incorporar a resolução desses apontamentos no planejamento estratégico do próximo ciclo de trabalho da equipe de desenvolvimento. Além disso, é essencial priorizar a execução das métricas operacionais que seguem pendentes (como a cobertura de testes e os cenários de queda do Redis) para que a avaliação da saúde do software seja completa e embase as próximas decisões arquiteturais.

---
## Histórico de versão

| Versão | Data       | Descrição | Autor(es) | Revisor(es) |
| :-- | :-- | :-- | :-- | :-- |
| 1.0 | 2026-06-12 | Cronograma de execução da avaliação com marcos, distribuição de atividades e contingências. | Samuel Afonso | Davi Casseb, Letícia Hladczuk |

## Referências

1. ISO/IEC 25040:2011. *Systems and software engineering: Systems and software Quality Requirements and Evaluation (SQuaRE): Evaluation process*. International Organization for Standardization, 2011.
2. BASILI, Victor R.; CALDIERA, Gianluigi; ROMBACH, H. Dieter. *The Goal Question Metric Approach*. In: Encyclopedia of Software Engineering. Wiley, 1994.
3. Django Software Foundation. *Deployment checklist e Security in Django*. Disponível em: <https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/>. Acesso em: 12 jun. 2026.
4. PyCQA. *Bandit Documentation*. Disponível em: <https://bandit.readthedocs.io/>. Acesso em: 12 jun. 2026.
5. Radon. *Radon Documentation: Cyclomatic Complexity*. Disponível em: <https://radon.readthedocs.io/>. Acesso em: 12 jun. 2026.