# Markets already built (read before starting any market)

A market listed here is UPDATED, never rebuilt: see « A market already built? » at the top of PROTOCOL.md
and run `python3 tools/stale.py <handle>`.

| Market | Handle | uuid | Last delivered PDF | Research dated |
|---|---|---|---|---|
| In Vivo CAR-T | in-vivo-car-t | | Q4 2026 (18 Nov 2026) | Nov 2026 |
| Humanoid Robotics | humanoid-robotics | 42 | Q4 2026 (18 Nov 2026) | Nov 2026 |
| Healthcare AI | healthcare-ai | 19 | Q4 2026 (18 Nov 2026) | Nov 2026 |
| Advanced Nuclear | advanced-nuclear | 63 | Q4 2026 (18 Nov 2026) | 18 Nov 2026 |
| Longevity | longevity | 2 | Q4 2026 (18 Nov 2026) | 18 Nov 2026 |
| Neocloud | neocloud | 60 | Q4 2026 (19 Nov 2026) | 19 Nov 2026 |
| AI in drug discovery | ai-drug-discovery | 45 | Q4 2026 (20 Nov 2026) | 20 Nov 2026 |
| Natural hydrogen | natural-hydrogen | 176 | Q4 2026 (21 Nov 2026) | 21 Nov 2026 |
| Stablecoin payments | stablecoin-payments | 80 | Q4 2026 (22 Nov 2026) | 22 Nov 2026 |
| Managing general agent (MGA) | managing-general-agent | 151 | Q4 2026 (22 Nov 2026) | 22 Nov 2026 |
| AI in insurance | ai-in-insurance | 123 | Q4 2026 (22 Nov 2026) | 22 Nov 2026 |
| AI data center | ai-data-center | 61 | Q4 2026 (23 Nov 2026) | 23 Nov 2026 |
| MedTech | medtech | 57 | Q4 2026 (23 Nov 2026) | 23 Nov 2026 |

Add a line at each delivery (same commit as the PDF).

## Pending common fixes (time rule 2, PROTOCOL « Fast builds »)
- (22 Nov 2026, MGA) `make_db_slides.py`: « an $80M » instead of « a $80M », plural nouns of people never read as verbs, + 9 characters
  kept for « for its » (some long descriptions fall back to the category), optional `cat_phrase.yaml`, « Intact Private Capital » ->
  « Intact »; `build_sources.py` ~90 insurance publishers: the latest-rounds and sources slides of the other decks change wording
  at their next rebuild. specs/overrides.yaml: wordmax 10 on behind_these_categories 5 and where_did_most_capital_go 6.
- (22 Nov 2026, AI in insurance conversation) Google slide (ed039p / live S02) of EVERY delivered deck: all stored Trends curves
  (gpu cloud, ai drug discovery, longevity, humanoid robot, in vivo car-t, ai in healthcare, advanced nuclear, stablecoins) rise
  x5 to x30 after mid-2025 and collapse in October 2026 while « youtube » and « weather » stay flat. Their « searches rose » titles
  describe Google's counting change: redo them with the RULES « Google Trends » rule (22 Nov) and the new `cut` option of pp_trends.
A fix common to several decks, made while a new market is in progress, is listed here; the other decks take it at their next
pass or in one background run after delivery (one build after the other).
- 19 Nov 2026 (Neocloud): `import_research.nmp_logo` / `logo()` now refuse a wide wordmark (content wider than 2.5x its height,
  RULES « Logos »): the other decks may lose a few wordmark tiles (initials or favicon instead, listed in logos_missing.txt)
  at their next rebuild. Rebuild them after Neocloud is delivered and ask Pierre for the square symbols they list.
- 19 Nov 2026 (Neocloud): `build_sources.py` names ~25 more publishers (CoreWeave, SemiAnalysis, IEA, IR hosts, SEC CIK files)
  and keeps lower-case brands: the sources pages of the other decks change wording at their next rebuild (no layout change).
- 19 Nov 2026 (Neocloud, Pierre's remarks): CARD_LINES (audit_layout) now checks the cards of template slides: the other decks may
  show CARD_LINES at their next rebuild (fix the texts). fundbars notes: one line per comma part (all decks). pp_winner (S12)
  centred (all decks). ed048 must cover every donut category (CATEGORIES MISMATCH blocks --png): decks whose donut has more than
  3 categories need an ed048-2 page (checked: In Vivo, Humanoid and Advanced Nuclear have 3 and 3, nothing to redo).
- 20 Nov 2026 (AI drug discovery): `make_db_slides.py` notes over bars are now 3 fixed lines (top company, top round, rounds),
  categories are grouped by the short name of cat_short.yaml, long lead names are dropped, examples use short names: the
  database slides of the other decks change wording at their next rebuild. `import_research.tidy_numbers` rounds halves up
  ($64.5M -> $65M). `build_sources.py` names ~30 more publishers and prints PUBLISHER GUESSED. `sx_faceoff` tighter letter
  spacing for names over 9 letters. `make_market_prompts.py`: ed175 model pairs shown together (prompts of the next markets).
  nmp-logos `find_logo.py` finds a company that has only a symbol file.
- 20 Nov 2026 (AI drug discovery, Pierre's review): new checks CATEGORY_LINES (category descriptions, 2 lines max) and
  BOX_LINES (sibling boxes mixing short and long texts); new spec ranges for the myths slides and category descriptions;
  series pages take the template of page 1 (SERIES GEOMETRY blocks --png otherwise); _2 templates of news and setbacks aligned
  on page 1; share_waffle with one year sits next to the side line. The delivered decks (Neocloud, Longevity…) have category
  descriptions on 3 lines and short myths: they will show these checks at their next rebuild, rewrite the texts then.
- 21 Nov 2026 (Natural hydrogen): `make_db_slides.py` completes ed156/ed157 with older rounds when a market has fewer than 12
  since 2024 (stops if still short), skips undisclosed rounds in the biggest-rounds bars, writes « undisclosed amount » over a
  $0M bar, « 1 round » singular, drops the lead investor when a row passes 118 characters, reads « Electrically stimulates » as a
  verb. `import_research.py`: ed205 takes ed204's title (PAGE TITLE; every delivered deck has the mismatch, fixed at next rebuild).
  `check_results.py`: British spelling, one round written two ways. `audit_layout.py`: HYPHEN_SPLIT. `build.py`: « Word N »
  non-breaking. `s09_from_base.py`: a category with no amount is dropped. `css/nmp.css`: maturity score box 180 px. The delivered
  decks keep « licence / cancelled » in research files: the British spelling check will show them at their next import.
- 21 Nov 2026 (Natural hydrogen, Pierre's review): `sx_categories_n` icon moved up onto the box corner (every deck with 3, 5 or 6
  categories changes at its next rebuild); ranking template `every_layer_carry_same_weight` key 18 centered; new check ALIGN_ODD
  (build.py) and « estimates value with a year » (check_results).
- 22 Nov 2026 (Stablecoin payments): new `tools/check_outside.py` (rebuild.sh, OUTSIDE PLAYER blocks --png). Run on the delivered
  decks: Neocloud ed199p (S11) shows IREN, a company of its S01 corners: rewrite that row at its next rebuild (blocks --png).
- 22 Nov 2026 (Stablecoin payments): `skip_rounds.yaml` + `tools/skip_rounds.py` (make_db_slides, s09_from_base, mkpp,
  borderline): rounds listed there never reach a slide. MoonPay 2026-06 and 2022-04 are in it: the main conversation decides
  whether the base drops them too. New warnings WEAK ROUND SOURCE and ROUND EXTENSION; on the delivered decks they list
  Healthcare AI anumana-2025-04 ($95M) and unlearn-2023-03, AI drug discovery accutar-biotechnology-2017-12-h, Longevity
  cambrian-biopharma-2019-11-2, Advanced Nuclear ultra-safe-nuclear-2022-01-2 (all sourced only by Forge Global): check each at
  the deck's next pass.
- 22 Nov 2026 (Stablecoin payments): `pp_prepare.py` keeps the Trends curve to today with `to_today: true` (default unchanged).
  `make_db_slides.py`: GENERIC_INV (no « led by Blockchain ») and acronyms kept in category words: database slides of other decks
  may change wording at their next rebuild. `import_research.py`: NO_FAVICON and FAVICON SHARED (a deck's favicon tile can turn
  into initials). `build_sources.py`: ~15 more publishers. specs/overrides.yaml: behind_these_categories '5' and
  where_did_most_capital_go '6' wordmax 10.
- 22 Nov 2026 (AI data center, Pierre's Trends choice C): `pp_trends` takes `dash_from`, `stat`, `stat_text`, `dash_caption`
  (pp_prepare.trends, pp_trends.j2, css .pp-dashcap). Delivered decks whose S02 term is a small term (Neocloud « GPU cloud »,
  AI drug discovery) still show the whole curve in pink with a ratio that includes the mid-2025 effect: give them the dashed part,
  a stat on the solid part and no SIGNAL pill at their next pass, and correct the live S02 slides in the retour.
- 23 Nov 2026 (AI data center): new audit checks ROW_LINES, LIST_LINES and VALUE_WRAP, key-trend value boxes widened (nowrap). Delivered
  decks: run `tools/audit_layout.py <handle>` at their next pass and fix any ROW_LINES (priority tables) or LIST_LINES (league tables) they show.
- 23 Nov 2026 (MedTech): `make_db_slides.py` line limit counts the joining words around the publisher (margin 10): some
  database rows of the other decks may be shortened at their next rebuild. `pp_prepare.money()` writes $1,000B and more in
  trillions. `pp_trends.j2` shows `period:` under a cut curve. `share_waffle.j2` prints thousands commas. `check_results.py`
  fails on the reference market name. `import_research.py` prints LOGO AMBIGUOUS when two nmp-logos ids share a domain
  (18 such pairs exist, e.g. intuitive / intuitive-surgical, bostondyn / boston-dynamics: merge them in nmp-logos).
  `build_sources.py` names ~100 more publishers (medical device IR hosts, FDA, trade press).
