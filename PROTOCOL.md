# Protocol: a new market deck, step by step

Read MARKETS.md (markets already built), this file, then RULES.md (what a slide must look like). Nothing else is required.
The reference deck is `decks/in-vivo-car-t`. Every new market is built from it (EdTech is retired, `archive/`).
Speak French to Pierre. Each step ends with a gate: do not go to the next step until the gate is green.

## A market already built? (a client orders it again, Pierre 18 Nov 2026)
Look at `MARKETS.md` first. If the market is there, NEVER rebuild it from step 0:
1. `python3 tools/stale.py <handle>`: chapters to redo (dated chapters older than 60 days), SIGNAL slides past their limit,
   relative time words to rewrite, product-page twins to compare with the live page.
2. ONE zip of research prompts for the chapters marked TO REDO only (`make_market_prompts.py`, same spec in `plans/`),
   plus the signals prompt. Evergreen chapters (01, 04, 06) are only re-read by Claude.
3. Pierre returns the results: put them in `decks/<handle>/research` (they replace the old files of the same chapter),
   then `tools/rebuild.sh <handle> --png`. Base figures re-flow by themselves (`{db.key}`), sources are rebuilt.
4. Gate of step 4, then the review page (only the slides that changed), then the PDF of the current quarter.

## Fast builds (piste C, 18 Nov 2026)
- While fixing: `tools/rebuild.sh <handle> --fast` renders only the slides whose data changed (about 35 s instead of 5 min); the
  in-browser audit still checks every slide. A change in a template, `fixlib.js` or `build.py` makes it a full build by itself.
- Before ANY review page or PDF: one full build, `tools/rebuild.sh <handle> --png`, then the look at the changed slides.
- Several decks to rebuild after a common fix: run them in the background, one after the other, and keep working.

## Step 0. Start (Claude, 10 min)
- Clone the logo libraries: githpierre/nmp-pages and githpierre/nmp-product-pages (add_repo, then `git clone --depth 1`
  into /home/claude). The import reads them.
- Footer label: the market's line in `data/market_labels.txt`. Market uuid and handle: nmp-seo `data/catalogues`.
- Startups base: last `searched_until` of the market in nmp-seo `data/startups/coverage.csv`. Tell Pierre the date and the gap
  with today. Never ask him for a prompt that adds rounds: he updates the base himself, the deck takes its latest state.
- Market definition and categories: nmp-seo `data/startups/market_definitions.csv` and `market_categories.csv`.
- Product page: `https://newmarketpitch.com/pages/<handle>`. List its 12 slides (S01-S12) and their types.
- Cover: it is COPIED from Pierre's cover slide (Google Slides « nmp - cover deck (1-225) », slide number = uuid), never laid
  out by a general rule: read the slide, save the answer as `decks/<handle>/cover_slide.json`, run
  `python3 tools/cover_from_slides.py <handle>` (fields and steps in its header). Gate: the built cover next to the slide
  thumbnail, side by side.
- Send Pierre the 7-step plan below and the starting questions, numbered at the end:
  1) pain-point segments (where the problem is felt), 2) value-creation segments (types of solution), both INSIDE the market
  definition, 3) Google Trends terms (he sends the CSVs).

## Step 1. Spec and prompts (Claude)
- Write `plans/<handle>.yaml` (copy `plans/humanoid-robotics.yaml`): name, segments, `reask` (slides the reference market had
  no data for), `pierre_dropped`, `live_twins` (deck slides the product page already gives, same type), `retarget` (slides
  specific to the reference market, given a new subject), `extra` (per-slide instructions).
  `examples` (the bad / good examples shown in the prompts) are written for THIS market: the tool refuses a spec without them, so
  no prompt carries another market's words. `model_words` lists only words the new market never uses (« patients » and « FDA »
  are In Vivo words for a robot deck, not for a healthcare deck).
- `python3 tools/make_market_prompts.py --spec plans/<handle>.yaml --out /home/claude/prompts_<handle>`: 12 TXT in one zip
  (10 chapters, 11 signals, 12 startup killers). Each slide shows its In Vivo version as the model.
  The prompts ask for: texts between 80 % and 100 % of each length, no semicolon, 8 rows on contrast slides, and for the
  signals a `fresh` period (a « hot right now » figure is recent, or a current-year estimate with its arithmetic).
- Gate: open one chapter file and the signals file and read them as the other LLM would.

## Step 2. Research (Pierre)
- He runs each TXT in its own conversation and returns the 12 `.md` files, plus the Google Trends CSVs.

## Step 3. Import and first build (Claude)
1. `python3 tools/make_market_demo.py --spec plans/<handle>.yaml` (structure deck from the reference).
2. Write the import arguments once in `decks/<handle>/import.args` (results folder, `--demo decks/<handle>-demo --out
   decks/<handle> --name "..." --pain "..." --value "..." --drop-no-data --model decks/in-vivo-car-t --model-name "in vivo CAR-T"
   --model-words "..."`), copy `decks/humanoid-robotics/import.args`.
3. `tools/rebuild.sh <handle> --png`: import, decisions, build, audits, list of changed slides. It stops on the first failure.
- Gate: the import prints no warning in capitals (`MODEL MARKET LEFT`, `MODEL ICON LEFT`, `SIGNAL STALE`, `SIGNAL NO DATE`,
  `CONTRAST ROWS`, `COVER NOT COPIED`, `DUPLICATE KEY`); `research_report.md` read; `logos_missing.txt` short, and the
  missing ones asked to Pierre in one list.

## Step 4. Fix until clean (Claude)
- Texts too long, too short or uneven: rewrite in `decks/<handle>/edits.yaml` (same facts; a text too short gets one more
  concrete fact). Never shrink fonts by hand.
- A grid with another number of items than the model: use or extend a template that takes N items (`sx_categories_n`,
  4-of-6 cards in 2 + 2). Never leave a hole, never 3 + 1.
- Gate: `tools/rebuild.sh` ends with « N slides, 0 issues », « 0 layout issues » and no line above them. Then the eye: the first time, every
  slide on sheets of 6 (a sheet of 12 hides overlaps); run `tools/diff_slides.py <handle> --snap`; after each later round,
  look only at the slides the rebuild lists as changed (`tools/diff_slides.py <handle> --sheets`), then `--snap` again.

## Step 5. Product-page twins, database slides, sources (Claude)
- Twins: copy the live slide's data into `decks/<handle>/live.yaml` (same title, same data, logos from the page).
- Database slides (Investor bets, rounds, top players by stage): `decks/<handle>/db.yaml` from the latest base, last of all.
- Sources: `decks/<handle>/sources_key.yaml` (20 key sources), then `python3 tools/build_sources.py <handle>`, then re-import.
- Gate: no yellow tag left (`PRODUCT PAGE`, `FROM OUR DATABASE`, `SOURCES`); gate of step 4 again.

## Step 6. Extra slides (Claude, then Pierre)
- From the signals file: build every candidate with solid data, in ONE review page (design, data, proposed place
  « between slide N and N+1 », the phrase of slide N that leads to it). Market opportunity: 6-8 SIGNAL slides, each with
  its `fresh` period (RULES.md, Extra slides).
- Pierre validates once. Validated slides go in `decks/<handle>/extras.yaml` (`after`, `link`, `slide`).

## Step 7. Delivery (Claude, then Pierre)
- Full rebuild, gates of step 4. Pierre sees the whole deck on a review page BEFORE the PDF. Then the PDF
  « <Market> - Q<n> <year> - newmarketpitch.com ©.pdf » (quarter of today). Commit, push.
- Pierre reads the whole deck. Each remark: find WHY it happened, fix the cause (template, import, check), add or update
  ONE line in RULES.md, and remove any rule it makes useless.

## Why the steps are built this way (errors found on Humanoid Robotics, 12 Nov 2026)
- Copy, do not re-lay out. What Pierre already drew (cover, product-page slides) is copied with its geometry. The cover was
  laid out by a general rule from the bare photo: title over the robots, wrong crop, wrong size.
- The reference market leaves traces: its name, its icons, its figures. The import swaps the name and lists the icons and
  stops on a key written twice. Figures of the base are never typed in a sentence (`{db.key}`).
- A check covers every slide. The cover, the dividers and the title-less slides were skipped by the audit, and that is where
  the errors were. An exception is written in the rule, never hidden in the code.
- A rule that silently stops working is worse than no rule: script errors fail the audit (JS_ERROR), a crashed import stops
  the rebuild. In the one-line JS files, comments are `/* */` only (a `//` comment killed the rest of a line twice).
- Fixes run after the refit and treat sibling boxes together; a page of a series built with another template takes the
  series' template name. One-off scripts inside a slide template are refused (they ran too early and were undone).
- The layout follows the data: N items need a template that takes N; texts have a minimum length as well as a maximum.
- A rule enters RULES.md only if Pierre said it or the reference deck shows it (an invented « notes start with We » rule
  contradicted the reference and was removed).

## Method v2 (14 Nov 2026), replaces the corresponding parts above
- Step 2: `python3 tools/make_market_prompts.py --spec plans/<handle>.yaml --out <dir>` puts chapters 01, 04 and 06 in decks/<handle>/evergreen/
  for Claude to write, and the other chapters in the zip. Every slide shows its MIN-MAX per key.
- Step 4: Claude writes the evergreen results in decks/<handle>/research/ (same format), runs tools/check_results.py on every result file,
  imports, and the gate includes TEXT LENGTH at 0.
- After a deck is validated: `python3 tools/make_spec.py` so the spec learns from it.
