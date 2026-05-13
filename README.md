# Equipe T02 RADIA PERLMAN - Avaliação da Qualidade do AcheiUnB

**Disciplina:** FGA315 - Qualidade de Software 1
**Professora:** Cristiane Ramos
**Semestre:** 2026/1
**Software avaliado:** [AcheiUnB](https://github.com/unb-mds/2024-2-AcheiUnB)
**Norma de referência:** ISO/IEC 25000 (SQuaRE) - em particular ISO/IEC 25010 (modelo de qualidade) e ISO/IEC 25040 (processo de avaliação).

## Sobre o projeto

Este repositório consolida todos os artefatos da avaliação de qualidade do software AcheiUnB, conduzida como trabalho final da disciplina. A documentação completa é publicada via MkDocs (GitHub Pages).

- **GitPage:** https://fcte-qualidade-de-software-1.github.io/2026-1_T02_RADIA_PERLMAN/
- **Release atual:** [`EU1`](https://github.com/FCTE-Qualidade-de-Software-1/2026-1_T02_RADIA_PERLMAN/releases/tag/EU1)

## Organização do repositório

```
.
├── docs/                  # Conteúdo do site MkDocs (fonte do relatório)
│   ├── index.md           # Página inicial
│   ├── fase1/             # Artefatos da Fase 1 (EU1)
│   ├── equipe.md          # Tabela de contribuição da equipe
│   ├── declaracao-ia.md   # Declaração de uso de IA
│   └── rastreabilidade.md # Links repo/release/GitPage
├── mkdocs.yml             # Configuração do site
├── .github/workflows/     # Deploy automático da GitPage
└── README.md
```

## Como rodar a documentação localmente

```bash
pip install mkdocs-material
mkdocs serve
```

O site fica disponível em `http://127.0.0.1:8000`.

## Como gerar o PDF do relatório

```bash
# A partir da raiz do repositório
mkdocs build
# Em seguida, exportar usando o navegador ou Pandoc a partir dos .md
```

Para o PDF entregue no Aprender 3, ver `docs/relatorio-eu1.pdf` (gerado a partir dos arquivos `fase1/*.md`).

## Equipe T02 RADIA PERLMAN

| Matrícula  | Nome                                  |
|------------|---------------------------------------|
| 211031083  | Julia Vitória Freire Silva            |
| 221008285  | Luis Eduardo Castro M Lima            |
| 211031566  | Ana Joyce Guedes Amorim da Silva      |
| 211031682  | Davi Araújo Bady Casseb               |
| 221039209  | Letícia de Cássia Hladczuk Rodrigues  |
| 211062473  | Samuel Afonso da Silva Santos         |

A tabela de contribuição da EU1 está em [`docs/equipe.md`](docs/equipe.md).
