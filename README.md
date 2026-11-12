# nmp-decks

NewMarketPitch market decks in HTML/CSS, exported to PDF (10 x 7 in).

Start here:
1. `PROTOCOL.md` — how a new market deck is made, step by step, with a gate at each step.
2. `RULES.md` — what a slide must look like (one line per rule; most are checked by code).
3. `SIGNALS.md` — catalogue of extra-slide formats.

```
python3 build.py <slug> --png      # decks/<slug>/deck.yaml -> PDF in decks/<slug>/out/ + one PNG per slide
python3 build.py <slug> --only 4,9 # PNG of a few slides only
python3 tools/audit_layout.py <slug>
```

- Reference deck: `decks/in-vivo-car-t` (EdTech is retired: `decks/edtech-full/DEPRECATED.md`, still read by some tools for geometry).
- `templates/slides/*.j2` data templates, `templates/slides/x/*.j2` templates converted from the PowerPoint (words in `t`). See `CATALOG.md`.
- `decks/<slug>/`: `deck.yaml` (built by the import, never edited by hand), `edits.yaml` (text fixes), `db.yaml` (database slides),
  `live.yaml` (product-page twins), `extras.yaml` (extra slides), `sources_key.yaml`.
- `tools/atelier2/` decisions and generic fixes (fixlib.js) applied to every deck; `icons.py` emoji -> line icons.
- `assets/logos/` shared logos, `assets/covers/` cover photos.

Requirements: `pip install jinja2 pyyaml playwright pillow img2pdf pypdf` + Chromium, `qpdf`.
