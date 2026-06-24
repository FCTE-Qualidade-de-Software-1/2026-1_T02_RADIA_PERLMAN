# Snapshot do objeto avaliado

Este arquivo registra o **commit fixado** do repositório do AcheiUnB sobre o qual
**todas** as medições da [Fase 4](../docs/fase4/index.md) incidem, conforme exigido pela
[Fase 3, §1.2 (regra 1)](../docs/fase3/01-metodo-instrucoes.md) e pela
[Fase 3, §2.5](../docs/fase3/02-recursos-ambiente.md). A fixação por hash elimina a
variação do objeto medido entre execuções, garantindo repetibilidade e auditoria
(critério F4-C2).

## Identificação do snapshot

| Item | Valor |
| :-- | :-- |
| Repositório | `unb-mds/2024-2-AcheiUnB` |
| URL | <https://github.com/unb-mds/2024-2-AcheiUnB> |
| Branch | `main` |
| **Commit (SHA-1)** | `e91773380c5259007d748d85e998a27362537339` |
| Data do commit | 2025-07-13 |
| Data de fixação para a avaliação | 2026-06-12 (EU2); reconfirmado em 2026-06-23 (EU3) |

## Comando de fixação

```bash
git clone https://github.com/unb-mds/2024-2-AcheiUnB.git
cd 2024-2-AcheiUnB
git checkout e91773380c5259007d748d85e998a27362537339
git rev-parse HEAD   # deve retornar e91773380c5259007d748d85e998a27362537339
```

## Validade

Toda execução posterior, incluindo eventuais reexecuções para fins de auditoria, utiliza
**exclusivamente** este snapshot. Mudanças posteriores ao código original **não
invalidam** os resultados — apenas restringem sua validade ao instantâneo avaliado, em
coerência com o princípio de instantâneo único declarado na
[Fase 1, §6.5](../docs/fase1/06-escopo.md). Como o repositório do AcheiUnB não recebe
commits desde julho de 2025, o HEAD do `main` na janela das entregas EU2/EU3 coincide com
o hash acima.

## Histórico de versão

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
| :-- | :-- | :-- | :-- | :-- |
| 1.0 | 2026-06-23 | Registro formal do commit fixado do AcheiUnB (`e917733`) usado em toda a Fase 4. | Davi Casseb | Letícia Hladczuk |
