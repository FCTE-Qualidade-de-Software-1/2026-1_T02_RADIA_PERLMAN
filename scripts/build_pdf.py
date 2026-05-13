#!/usr/bin/env python3
"""
Pré-processa os arquivos Markdown de docs/ para gerar PDF com diagramas Mermaid
renderizados como SVG. O mkdocs-with-pdf não renderiza Mermaid de forma
confiável via JS no PDF final, então a estratégia é converter cada bloco
` ```mermaid ... ``` ` em SVG estático antes do build.

Diagramas são nomeados por hash SHA-1 do conteúdo, o que permite preservar
SVGs já renderizados entre builds (não regerar o que não mudou).

Uso:
    python3 scripts/build_pdf.py

Saídas:
    _pdf_docs/                  cópia processada de docs/ usada como entrada do MkDocs
    _pdf_docs/img/diagrams/*.svg diagramas renderizados (persistem entre builds)
    site/pdf/relatorio-eu1.pdf  PDF final
"""

from __future__ import annotations

import hashlib
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
PDF_DOCS = ROOT / "_pdf_docs"
DIAGRAMS_DIR = PDF_DOCS / "img" / "diagrams"
PUPPETEER_CFG = ROOT / "_pdf_docs" / ".puppeteer-config.json"
MMDC = shutil.which("mmdc")

MERMAID_BLOCK = re.compile(
    r"^```mermaid\s*\n(?P<body>.*?)\n```",
    re.DOTALL | re.MULTILINE,
)


def fail(msg: str) -> None:
    print(f"[build_pdf] erro: {msg}", file=sys.stderr)
    sys.exit(1)


def prepare_workdir() -> None:
    """Limpa _pdf_docs/ mas preserva _pdf_docs/img/diagrams/."""
    cache_backup = ROOT / ".cache_diagrams"
    if DIAGRAMS_DIR.exists():
        if cache_backup.exists():
            shutil.rmtree(cache_backup)
        shutil.move(str(DIAGRAMS_DIR), str(cache_backup))

    if PDF_DOCS.exists():
        shutil.rmtree(PDF_DOCS)
    shutil.copytree(DOCS, PDF_DOCS)

    DIAGRAMS_DIR.mkdir(parents=True, exist_ok=True)
    if cache_backup.exists():
        for svg in cache_backup.iterdir():
            shutil.move(str(svg), str(DIAGRAMS_DIR / svg.name))
        cache_backup.rmdir()

    PUPPETEER_CFG.write_text(
        json.dumps({"args": ["--no-sandbox", "--disable-setuid-sandbox"]}),
        encoding="utf-8",
    )


def diagram_path(mmd_source: str) -> Path:
    digest = hashlib.sha1(mmd_source.encode("utf-8")).hexdigest()[:12]
    return DIAGRAMS_DIR / f"diagram-{digest}.png"


def render_mermaid(mmd_source: str, output_png: Path) -> None:
    if output_png.exists():
        return
    mmd_path = output_png.with_suffix(".mmd")
    mmd_path.write_text(mmd_source, encoding="utf-8")
    result = subprocess.run(
        [
            MMDC,
            "-i", str(mmd_path),
            "-o", str(output_png),
            "-b", "white",
            "-w", "2400",
            "-s", "3",
            "-p", str(PUPPETEER_CFG),
        ],
        capture_output=True,
        text=True,
    )
    mmd_path.unlink(missing_ok=True)
    if result.returncode != 0 or not output_png.exists():
        raise RuntimeError(
            f"mmdc falhou para {output_png.name}:\n"
            f"stdout: {result.stdout}\nstderr: {result.stderr}"
        )


def process_markdown(md_path: Path, counter: dict[str, int]) -> None:
    text = md_path.read_text(encoding="utf-8")

    def replace(match: re.Match) -> str:
        counter["total"] += 1
        svg_path = diagram_path(match.group("body"))
        cached = svg_path.exists()
        try:
            render_mermaid(match.group("body"), svg_path)
        except RuntimeError as exc:
            print(f"[build_pdf] aviso: {exc}", file=sys.stderr)
            counter["failed"] += 1
            return match.group(0)
        if cached:
            counter["cached"] += 1
        else:
            counter["rendered"] += 1
        rel = svg_path.relative_to(PDF_DOCS).as_posix()
        depth = len(md_path.relative_to(PDF_DOCS).parts) - 1
        prefix = "../" * depth if depth else ""
        return f"![Diagrama]({prefix}{rel})"

    new_text, n = MERMAID_BLOCK.subn(replace, text)
    if n:
        md_path.write_text(new_text, encoding="utf-8")
        print(f"[build_pdf] {md_path.relative_to(PDF_DOCS)}: {n} bloco(s)")


def main() -> None:
    if MMDC is None:
        fail("comando `mmdc` não encontrado no PATH (instale @mermaid-js/mermaid-cli).")
    if not DOCS.is_dir():
        fail(f"diretório {DOCS} não existe.")

    prepare_workdir()
    counter = {"total": 0, "cached": 0, "rendered": 0, "failed": 0}
    for md_path in sorted(PDF_DOCS.rglob("*.md")):
        process_markdown(md_path, counter)
    print(
        f"[build_pdf] {counter['total']} bloco(s) Mermaid: "
        f"{counter['rendered']} renderizado(s), "
        f"{counter['cached']} reusado(s) do cache, "
        f"{counter['failed']} falha(s)."
    )

    if counter["failed"]:
        fail("um ou mais diagramas falharam; abortando build do PDF.")

    build = subprocess.run(
        ["mkdocs", "build", "-f", "mkdocs-pdf.yml"],
        cwd=ROOT,
    )
    if build.returncode != 0:
        fail("mkdocs build falhou.")
    print("[build_pdf] PDF gerado em site/pdf/relatorio-eu1.pdf")


if __name__ == "__main__":
    main()
