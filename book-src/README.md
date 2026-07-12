# Fonte de geração do livro (book-src)

Scripts Python (reportlab) que geram `CRF-GO_Livro_Formacao_Farmaceutica_GO.pdf` — a
edição revisada 17×24cm com sumário navegável, ficha catalográfica, mapa e 15
figuras. **Rode tudo com o diretório de trabalho dentro de `book-src/`** (os
caminhos de imagem em `book_content.py` são relativos a essa pasta).

## Dependências

```
pip install reportlab pypdf pillow matplotlib
```

Fontes: usa Georgia do Windows (`C:\Windows\Fonts\georgia*.ttf`), registrada em
`build_edition_v2.py`. Em outro SO, troque `FONTS_DIR` e os nomes dos arquivos
`.ttf` por uma fonte serifada equivalente instalada localmente.

## Como reconstruir o PDF do zero

```bash
cd book-src
python build_charts.py       # gera 10 dos 15 fig_*.png (a partir de current_data.json)
python build_charts2.py      # gera mais 4 fig_*.png (situação, avaliação, centro-oeste, cenários)
python build_map.py          # gera fig_mapa_oferta.png (a partir de go_geo.json)
python build_edition_v2.py   # monta o miolo completo -> edition_body_17x24.pdf (67 páginas com capa)
```

`build_edition_v2.py` já mescla a capa original (`book_with_cover_logo.pdf`,
página 1 — **nunca regenerar essa capa**, é o arquivo institucional preservado)
com o miolo gerado, produzindo o PDF final de 67 páginas.

Depois, para reincrustar no HTML do observatório:

```bash
# edite embed_pdf.py se o caminho do HTML/Desktop mudou de máquina
python embed_pdf.py
```

## Arquivos

| Arquivo | Papel |
|---|---|
| `book_content.py` + `book_content_part2.py` | Todo o conteúdo do livro (238 blocos: partes, capítulos, parágrafos, tabelas, figuras) como tuplas Python. **Editar aqui para mudar texto/dados.** |
| `build_edition_v2.py` | Motor de composição: estilos, página 17×24cm, sumário navegável (multiBuild + TableOfContents), bookmarks, cabeçalho par/ímpar, ficha catalográfica, expediente, colofão. |
| `build_charts.py`, `build_charts2.py` | Geram os 14 gráficos matplotlib (paleta navy `#16304F` / dourado `#B8893B`). |
| `build_map.py` | Gera o mapa coroplético de Goiás (246 municípios) a partir do GeoJSON. |
| `logo_reportlab.py` | Desenha a logo CRF-GO (ícone vetorizado + wordmark) em qualquer canvas reportlab — usado nos cabeçalhos. |
| `icon_traced3.svg` | Traçado vetorial do ícone (modo polígono — fiel ao original, com o entalhe central e o floreio na base preservados). |
| `current_data.json` | Snapshot do `DATA` do HTML (`obs-data`) usado para gerar os gráficos/mapa — se os dados do observatório mudarem, re-extrair este JSON antes de rodar os builders. |
| `go_geo.json` | GeoJSON dos 246 municípios de Goiás (extraído do HTML). |
| `book_with_cover_logo.pdf` | **Capa institucional preservada** (A4, página 1) — nunca alterar. |
| `embed_pdf.py` | Reincrusta o PDF final como base64 no `window.PDF_B64` do HTML do observatório. |

## Gotchas

- `book_content.py`/`FIGURE()` guarda `width_mm` calibrado para a página A4 antiga;
  `build_edition_v2.py::add_figure()` já limita (`min(width_mm, CONTENT_W_MM)`)
  para a página 17×24cm menor — não precisa reduzir os valores manualmente.
- O sumário e a lista de figuras/tabelas usam paginação real via
  `doc.multiBuild()` (múltiplas passadas até convergir) — **não** trocar por
  `doc.build()` simples, ou os números de página somem.
- Cabeçalho par/ímpar lê `toc._lastEntries` (não `toc._entries`) dentro do
  `EditionDocTemplate.build()` override — ver comentário no código, é
  contraintuitivo (`multiBuild()` já limpou `_entries` antes de chamar `build()`).
- Se re-extrair `current_data.json` do HTML, rode os 3 scripts de figura de
  novo antes do `build_edition_v2.py` (os PNGs não são gerados automaticamente
  por ele).
