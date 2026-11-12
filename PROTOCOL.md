# Protocol: a new market deck, step by step

Read this file, then RULES.md (what a slide must look like). Nothing else is required.
The reference deck is `decks/in-vivo-car-t`. Every new market is built from it (EdTech is retired, `archive/`).
Speak French to Pierre. Each step ends with a gate: do not go to the next step until the gate is green.

## Step 0. Start (Claude, 10 min)
- Clone the logo libraries: githpierre/nmp-pages and githpierre/nmp-product-pages (add_repo, then `git clone --depth 1`
  into /home/claude). The import reads them.
- Footer label: the market's line in `data/market_labels.txt`. Market uuid and handle: nmp-seo `data/catalogues`.
- Startups base: last `searched_until` of the market in nmp-seo `data/startups/coverage.csv`. Tell Pierre the date and the gap
  with today. Never ask him for a prompt that adds rounds: he updates the base himself, the deck takes its latest state.
- Market definition and categories: nmp-seo `data/startups/market_definitions.csv` and `market_categories.csv`.
- Product page: `https://newmarketpitch.com/pages/<handle>`. List its 12 slides (S01-S12) and their types.
- Cover: slide number = uuid in the Google Slides « nmp - cover deck (1-225) ». Take the PHOTO element only (not the slide
  thumbnail, which already carries the title) into `assets/covers/<handle>.jpg`.
- Send Pierre the 7-step plan below and the starting questions, numbered at the end:
  1) pain-point segments (where the problem is felt), 2) value-creation segments (types of solution), both INSIDE the market
  definition, 3) Google Trends terms (he sends the CSVs).

## Step 1. Spec and prompts (Claude)
- Write `plans/<handle>.yaml` (copy `plans/humanoid-robotics.yaml`): name, segments, `reask` (slides the reference market had
  no data for), `pierre_dropped`, `live_twins` (deck slides the product page already gives, same type), `retarget` (slides
  specific to the reference market, given a new subject), `extra` (per-slide instructions).
- `python3 tools/make_market_prompts.py --spec plans/<handle>.yaml --out /home/claude/prompts_<handle>`: 12 TXT in one zip
  (10 chapters, 11 signals, 12 startup killers). Each slide shows its In Vivo version as the model.
- Gate: open one chapter file and the signals file and read them as the other LLM would.

## Step 2. Research (Pierre)
- He runs each TXT in its own conversation and returns the 12 `.md` files, plus the Google Trends CSVs.

## Step 3. Import and first build (Claude)
1. `python3 tools/make_market_demo.py --spec plans/<handle>.yaml` (structure deck from the reference).
2. `tools/import_research.py <results> --demo decks/<handle>-demo --out decks/<handle> --model decks/in-vivo-car-t
   --model-name "in vivo CAR-T" --model-words "..." --pain "..." --value "..." --drop-no-data` (script: `/home/claude/rbh.sh`).
   The import swaps the reference market's name everywhere, fetches missing logos from the domains the research gives,
   and drops slides answered `no_data`.
3. `python3 build.py <handle> --png`, then `python3 tools/audit_layout.py <handle>`.
- Gate: the import prints no `MODEL MARKET LEFT`; `research_report.md` read (length warnings = texts to shorten);
  `logos_missing.txt` short (initials are accepted for the rest).

## Step 4. Fix until clean (Claude)
- Texts too long or uneven: rewrite in `decks/<handle>/edits.yaml` (short, same facts). Never shrink fonts by hand.
- A grid with another number of items than the model: use or extend a template that takes N items (`sx_categories_n`,
  4-of-6 cards in 2 + 2). Never leave a hole, never 3 + 1.
- Gate: build issues = only OUTSIDE {}; audit_layout = 0; every slide looked at on contact sheets of 12.

## Step 5. Product-page twins, database slides, sources (Claude)
- Twins: copy the live slide's data into `decks/<handle>/live.yaml` (same title, same data, logos from the page).
- Database slides (Investor bets, rounds, top players by stage): `decks/<handle>/db.yaml` from the latest base, last of all.
- Sources: `decks/<handle>/sources_key.yaml` (20 key sources), then `python3 tools/build_sources.py <handle>`, then re-import.
- Gate: no yellow tag left (`PRODUCT PAGE`, `FROM OUR DATABASE`, `SOURCES`); gate of step 4 again.

## Step 6. Extra slides (Claude, then Pierre)
- From the signals file: build every candidate with solid data, in ONE review page (design, data, proposed place
  « between slide N and N+1 », the phrase of slide N that leads to it). Market opportunity: 6-8 SIGNAL slides.
- Pierre validates once. Validated slides go in `decks/<handle>/extras.yaml` (`after`, `link`, `slide`).

## Step 7. Delivery (Claude, then Pierre)
- Full rebuild, gates of step 4, every slide looked at, PDF « <Market> - Q<n> <year> - newmarketpitch.com ©.pdf »
  (quarter of today). Commit, push.
- Pierre reads the whole deck. Each remark: find WHY it happened, fix the cause (template, import, check), add or update
  ONE line in RULES.md, and remove any rule it makes useless.

## Why the steps are built this way (errors of 12 Nov 2026, Humanoid Robotics)
- In Vivo words left on slides nobody rewrote (agenda, sources divider): the import now swaps the model market's name and
  stops on `MODEL MARKET LEFT`.
- Logos as tiny wordmarks or initials: the libraries in Pierre's other repos were not searched. The import now looks there first.
- Logos blank on the audit images: the PNGs were taken after the PDF step had hidden images. PNGs are now taken first.
- Many texts too long: the research exceeds target lengths; the import report lists them, step 4 fixes them before anything is shown.
- 4 or 5 categories in a 3- or 4-slot layout: templates must take N items; the layout follows the data.
