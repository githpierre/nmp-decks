# In Vivo CAR-T deck: plan validated by Pierre (12 Nov 2026)

- Base: the EdTech deck (decks/edtech-full), same 12 chapters, same templates. No slide removed: every EdTech slide is kept or adapted.
  - Price ranges (13) -> "How much will a treatment cost?" (ex vivo CAR-T list prices vs in vivo targets).
  - Commoditized (101-102) -> LNP / vector manufacturing at CDMOs, anti-CD19 CARs.
  - Unicorns (188-190) -> startups sold for $1B+ and how fast.
  - "How X..." contrasts (210-214) -> pharma acquisitions (Capstan / AbbVie, EsoBiotec / AstraZeneca...), amounts to confirm by research.
  - Signal slides: template kept, content from the signals research.
- Pain points chapter (EdTech 62-85): 3 categories by disease (blood cancers, autoimmune diseases, solid tumors) x 4 slides.
- Value creation chapter (EdTech 106-130): 4 technical approaches (mRNA-LNP, lentiviral, gene editing, beyond T cells) x 4 slides.
- 4 biotech slides added, each on an existing template:
  - Clinical pipeline (Tech and infra, after 98; template of 143).
  - Pharma deals (Investor bets, after 157; template of 156).
  - FDA pathway (Market challenges, after 138; template of 147).
  - Safety (Market challenges, after 140; template of 54).
- Product-page slides: they replace their twin slide (done in EdTech, tools/pp/pp_edtech.py). Slide 51 (realistic CAGR) stays, it is a different slide.
- Cover: Pierre's Google Slides cover "I N  V I V O".
- Signal slides (12 Nov): out of the base deck. The research first screens the 33+ formats of SIGNALS.md and keeps only strong, sourced signals;
  each kept signal becomes a slide in the chapter where it makes sense. The 16 cell-therapy signals already researched (decks/signals) are in the demo.

## Research (12 Nov 2026)
- Prompts: `python3 tools/make_research_prompts.py decks/invivo-demo --uuid 109 --handle in-vivo-car-t ...` -> 11 TXT in one zip:
  10 chapters (each slide shows its EdTech model, same keys and lengths, answer as YAML blocks with sources) + 1 signals screening (31 formats).
- Not asked (filled by Claude from the startups database, nmp-seo data/startups: 52 companies, 126 rounds, coverage full since 2024):
  rounds announced, fundraising evolution, raised each year, what stands out, what changed, top deal weight, biggest rounds (pp_raises x2),
  where capital went, where investors put money (invbets), most active investors, top players grid (pp_grid), "scored big recently".
- Google Trends: CSVs downloaded by Pierre (worldwide, 5 years).
- Next: Pierre runs the 11 prompts, returns the 11 .md files; Claude imports them into deck.yaml, builds, audits, proposes 5-15 signal slides with their placement.
- The cell-therapy signals of the library are not reused (Pierre).
