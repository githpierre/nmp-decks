# nmp-decks

NewMarketPitch market decks in HTML/CSS, exported to PDF (10 x 7 in, same design as the PowerPoint decks).

```
python3 build.py edtech            # decks/edtech/deck.yaml -> PDF in decks/edtech/out/ (~3 s) + layout audit
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
