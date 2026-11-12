# nmp-decks

NewMarketPitch market decks in HTML/CSS, exported to PDF (10 x 7 in, same design as the PowerPoint decks).

```
python3 build.py edtech-full       # decks/edtech-full/deck.yaml -> PDF in decks/edtech-full/out/ (~3 s) + layout audit
python3 build.py edtech --png      # + one PNG per slide (visual check)
python3 build.py edtech --only 4,9 # PNG of a few slides only
```

- `css/nmp.css` — design system (colors as variables at the top: change them for a white version).
- `templates/base.html.j2` — slide chrome (section label, title, footnote, footer).
- `templates/slides/*.j2` — one file per slide type (the slide library). See `SLIDES.md`.
- `decks/<slug>/deck.yaml` — all the content of a deck (text and numbers only; charts are computed).
- `assets/logos/` — shared logo library (one PNG per company, reused across decks).
- `assets/img/` — shared images (world map).
- `tools/` — group2svg.py (PPTX freeform group -> SVG), compare.py (old vs new render sheets).
- `RULES.md` — every rule Pierre validated. Read it before writing a deck.

Requirements: `pip install jinja2 pyyaml playwright` and a Chromium for Playwright.

## Templates (12 Nov 2026)
- Every slide is now built from a template: `templates/slides/<name>.j2` (data templates) or `templates/slides/x/<name>.j2` (converted from the PowerPoint, words in deck.yaml `t` / `img`). See `CATALOG.md`.
- Text box format in `t`: one line per paragraph, `{n|text}` = a run in another style, `<br>` = line break inside a paragraph.
- New slides from a PPTX: `tools/pptx2html.py`, then `python3 tools/templatize.py decks/<slug>`.
- Decisions and fixes (`tools/atelier2`) are written with EdTech slide numbers; `ref_slides.json` turns them into selectors by template, type or slide id, so they follow the slides into any deck.
- `python3 tools/catalog.py decks/edtech-full` rebuilds CATALOG.md and the gallery page.
