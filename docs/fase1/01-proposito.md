# 1. Propósito da avaliação e uso pretendido

## 1.1 Declaração de propósito

O propósito desta avaliação é **caracterizar a qualidade atual do AcheiUnB sob a perspectiva
da ISO/IEC 25010 (família SQuaRE)**, gerando evidências objetivas que apoiem decisões
técnicas e acadêmicas relacionadas à **continuidade evolutiva do produto entre semestres**
da disciplina de **Métodos de Desenvolvimento de Software (MDS) da UnB**. O AcheiUnB nasceu
em 2024/2 como projeto acadêmico em estágio de MVP, é mantido por uma equipe estudantil que
se renova periodicamente e não dispõe, até o momento, de um diagnóstico sistemático de
qualidade. Essa ausência limita a capacidade de novas equipes herdarem o produto com
previsibilidade técnica e expõe a iniciativa ao risco de regressões silenciosas durante a
sucessão.

A avaliação **não** se destina a certificar o produto e **não** fundamenta nenhuma decisão
comercial. Ela serve a **três decisões concretas e identificáveis**, descritas na seção
[1.3](#13-uso-pretendido-dos-resultados), todas vinculadas a stakeholders nomeados na
seção [2](02-stakeholders.md).

## 1.2 Para quem é a avaliação

A avaliação atende a **três públicos primários**:

1. **Próximas equipes da disciplina MDS**, que herdarão o código do AcheiUnB e precisam de
   um diagnóstico independente sobre maturidade, riscos e dívidas técnicas antes de
   planejar novas funcionalidades.
2. **Coordenação acadêmica das disciplinas envolvidas** (MDS e FGA315 Qualidade de
   Software 1), interessada em evidência empírica sobre a qualidade dos artefatos
   produzidos em projetos de ensino orientado a engenharia de software.
3. **Equipe atual e ex‑desenvolvedores do AcheiUnB**, que podem usar os resultados para
   priorizar correções de curto prazo e *backlog* de qualidade.

Stakeholders secundários (usuários finais - comunidade da UnB; potenciais operadores
institucionais; órgãos da UnB que poderiam adotar o sistema) são considerados na
**definição de critérios de sucesso** e na **interpretação dos resultados**, mas **não**
participam diretamente das atividades de medição da Fase 2. Essa restrição é justificada
em [Escopo, profundidade e objetos](06-escopo.md).

## 1.3 Uso pretendido dos resultados

Os resultados desta avaliação serão utilizados para apoiar **três decisões específicas**.
A coluna *Como os dados são usados* descreve a operação concreta sobre os resultados, e
não apenas uma intenção genérica.

| # | Decisão a apoiar | Quem decide | Como os dados são usados |
|---|------------------|-------------|--------------------------|
| **D1** | Priorização do *backlog* de qualidade do AcheiUnB para o próximo semestre da disciplina MDS. | Equipe atual / próxima do AcheiUnB. | Ranqueamento de itens por característica e por nível de risco residual identificado na Fase 4, com corte por capacidade de equipe (story points). |
| **D2** | Decisão **manter / refatorar / substituir** sobre componentes específicos: autenticação MSAL+JWT, *secret management*, fila Celery+Redis, módulo de chat em tempo real e camada de testes do frontend. | Equipe atual / próxima do AcheiUnB. | Comparação entre o estado medido na Fase 3 e os critérios de aceitação derivados na Fase 2 (por subcaracterística da ISO/IEC 25010). |
| **D3** | Avaliação acadêmica da equipe T02 nas entregas EU1, EU2 e EU3 da disciplina FGA315. | Profa. Cristiane Ramos. | Auditoria dos artefatos publicados na GitPage e no repositório (atas, dados brutos, *releases*, rastreabilidade git) à luz dos critérios da rubrica da disciplina. |

## 1.4 Cenário de aplicação

A avaliação ocorre no **semestre 2026/1**, sobre a versão do AcheiUnB disponível no *branch*
`main` do repositório `unb-mds/2024-2-AcheiUnB` no **instante de início da medição da
Fase 2** (a *tag* / *commit* exato será fixado nessa data e registrado em
[Escopo](06-escopo.md)). A coleta será conduzida pela equipe T02 a partir do código-fonte,
da documentação, dos arquivos de configuração e de execuções controladas em ambiente local
containerizado (Docker), conforme o modelo proposto pela própria equipe do AcheiUnB. Os
resultados são entregues nos relatórios EU1, EU2 e EU3, com versão consolidada publicada
nesta GitPage e na *release* final do repositório.

!!! info "Decisão registrada - versão sob avaliação"
    Define-se como **objeto da avaliação** o estado do repositório
    `unb-mds/2024-2-AcheiUnB` na *tag* ou *commit* a ser fixado no início da Fase 2.
    Mudanças posteriores ao código original **não invalidam** os resultados - apenas
    restringem sua validade ao instantâneo (*snapshot*) avaliado. Esse princípio é
    reforçado em [Escopo, profundidade e objetos](06-escopo.md).

## 1.5 Como este propósito guia o resto do trabalho

A escolha do propósito tem três implicações imediatas sobre o restante da Fase 1:

- **Sobre a seleção de características** ([§5](05-caracteristicas.md)): a decisão D2 exige
  que a avaliação produza informação acionável sobre **componentes** internos (não apenas
  uma nota global). Isso favorece características em que a evidência é majoritariamente
  obtida por análise estática e dinâmica do código - **Manutenibilidade**, **Segurança**,
  **Confiabilidade** e **Adequação Funcional** - e desfavorece características que
  demandam pesquisa com usuários finais (cujo acesso é restrito no escopo acadêmico).
- **Sobre o escopo** ([§6](06-escopo.md)): a decisão D1 só é viável se a profundidade da
  medição for compatível com o tempo da disciplina (1 semestre). O escopo se concentra
  no *backend* e nos artefatos de processo (CI/CD, configuração, testes), tratando o
  *frontend* em profundidade reduzida.
- **Sobre o vínculo com ODS** ([§7](07-ods.md)): por se tratar de produto universitário
  voltado à comunidade da UnB, os ODS pertinentes orientam a interpretação dos resultados
  em termos de **impacto institucional e social**, não apenas técnico.

## Histórico de versão

| Versão | Data       | Descrição                | Autor(es)                              | Revisor(es)                       |
|--------|------------|--------------------------|----------------------------------------|-----------------------------------|
| 1.0    | 2026-05-13 | Versão inicial da seção. | Davi Casseb, Ana Joyce, Samuel Afonso  | Letícia Hladczuk, Julia Vitória, Luis Lima |

## Referências

1. ISO/IEC 25010:2011. *Systems and software engineering: Systems and software Quality Requirements and Evaluation (SQuaRE): System and software quality models*. International Organization for Standardization, 2011.
2. ISO/IEC 25040:2011. *Systems and software engineering: Systems and software Quality Requirements and Evaluation (SQuaRE): Evaluation process*. International Organization for Standardization, 2011.
3. AcheiUnB. *Repositório do projeto da disciplina MDS/UnB 2024-2*. Disponível em: <https://github.com/unb-mds/2024-2-AcheiUnB>. Acesso em: 13 maio 2026.
