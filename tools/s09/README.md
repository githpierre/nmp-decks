# S09 Investor bets (product pages, section 9)

Built 11 Nov 2026 for markets 101-130 (then 131-225). Rules validated by Pierre in `RULES.md` and in the skill nmp-12-slides-illustratives.

1. `prep2.py out.json <handles…>`: reads the startups base of githpierre/nmp-seo (`data/startups/`). Equity rounds of the last 12 months,
   no IPO / post-IPO / secondary, startups only, sourcing rule of the base applied everywhere. Top 6 categories (markets.csv category),
   short display names from `short_cats.json` (22 characters max). Logos are examples: up to 3 square logos per row, filled with other
   active startups of the same category. Never a name tile.
2. `mkdeck.py <slug> <json>`: writes `decks/<slug>/deck.yaml` (slide type `invbets`), copies the logos into `assets/logos/`.
   Bottom-right label = `market_name_for_slide`.
3. `python3 build.py <slug> --png` (layout audit), then `export.py <slug> <outdir>`: x3 screenshot + page_lift, WebP 2400x1680,
   named `{handle}-slide-09-01.webp`.
4. Upload: stagedUploadsCreate + POST + fileCreate (alt), then Matrixify Pages import of `custom.v1_sections` (section 9 img + alt).
