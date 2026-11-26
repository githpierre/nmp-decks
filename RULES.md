# Rules: what a deck slide must look like

One line per rule. A rule is here only if Pierre said it or the reference deck shows it. `CHECK` = verified by code (build.py, tools/audit_layout.py, tools/pp/audit_pp.py): no need to remember it,
the build tells you. Rules without CHECK need the eye. The process is in PROTOCOL.md. Full history: archive/RULES-log-2026-11.md.

## Content
- US English, plain words for a smart non-expert, short sentences, no em dash, no exclamation mark, no semicolon (the import
  writes two sentences).
- Every figure sourced and dated. A demo video or a CEO target is not a fact about the market.
- Money as people say it: $285M, $4.2B, ≈5% (no space). CHECK MONEY_FORMAT.
- One sentence: no final dot. Two or more: dots.
- No past year that will look old in a note (« latest 2025 estimates »): write « the latest estimates ».
- Relative time (« this year », « so far », « today ») is rewritten at each deck update.
- Pure players only; Big Tech is never a startup. Company and product names are never shortened to fit.
- A segment keeps exactly the same name everywhere (divider, subtitle, tables, cards).
- Categories stay inside the market definition (nmp-seo market_definitions.csv).
- A slide that cannot be filled completely is removed, never shown with a hole. CHECK GRID_HOLES.
- At least 2 logos per category; otherwise merge categories or drop the slide.
- Database figures: equity rounds only, complete since January 2024 only (no yearly sums before 2024); recomputed after any
  base correction; a fast repeat round is checked at the source before it is used.
- Category split and market size can be our estimate: the note says so and how it is built. No 0% slice.

## Titles and notes
- Slide title: always 2 lines, the most balanced cut, a market or company name never cut. CHECK TITLE_NOT_2_LINES, TITLE_BALANCE.
- Extra-slide titles state the fact (who, what, how much), say « recent » rather than « since 2024 ».
- Chapter kicker is the chapter, never the market name. CHECK KICKER_IS_MARKET.
- Note (bottom left): 2 balanced lines by default (YAML list, no dots), 1 line if one idea fits,
  3 only for 3 important ideas; never runs into the footer label. CHECK NOTE_BALANCE, NOTE_WIDTH.
- Centred sentences of 2 lines or more (stories, why texts): lines as equal as possible, like titles (fixlib `balance`).
- Footer label: Pierre's list `data/market_labels.txt`, one line. CHECK in build.py, FOOT_LABEL.

## Text boxes and grids
- Sibling boxes: same width, same font size, same number of lines (labels too). A text too long is shortened, never shrunk.
  CHECK FONT_MIXED, LABEL_LINES, BODY_LINES.
- Lines balanced (no orphan word), a number stays with its unit (automatic, rawfit.js).
- Card labels on 2 lines; a one-word label gets a second word (« CAR MAKERS »). CHECK LABEL_LINES (build), and before the
  import `tools/check_results.py` refuses a one-word label where the model has two lines (Neocloud, 19 Nov 2026).
- A box of 2 lines or more is filled: its longest line takes at least 58 % of the inner width; a text too short gets one more
  fact (about 2 full lines). CHECK HALF_FILLED. Sibling boxes start at the same height. CHECK SIBLING_TOP.
- A text never sits on a line, an arrow or a card border; a word or a figure is never cut in two lines.
  CHECK TEXT_ON_LINE, TEXT_ON_BORDER, WORD_SPLIT.
- Text never touches its bubble. CHECK TEXT_PAD. Card text centered vertically; pill + text centered together.
- Icon-card grids: every text on 4 lines. Dated rails (rounds, deals, news): 6 dates per page, every entry on 2 lines.
- Body inside x 90-870. CHECK MARGIN, MARGIN_ALL.
- The layout follows the number of items: 4 cards of a 6-slot grid go 2 + 2, N categories use a template that takes N.
- Same slide type = same look on every page of a series (1/2, 2/2): decisions are copied by make_decisions.py; a page built
  with another template takes the series' template name (base.html.j2). CHECK SERIES_ICON_MIX.
- « Which categories will we use? »: names in capitals on 2 lines, the same names as the dividers, identical cards (fixlib
  `catsGrid`). Segment dividers: one line, one title size for the whole deck, clear of the side arrows (fixlib `deck`;
  Pierre chose it on 13 Nov 2026 over 2-line names and over removing the arrows: never propose those again).

## Colors, icons, logos
- Pink never as thin text or thin small icons on navy; pink fills (pill, bar, bold) or a 2 px frame are fine. CHECK PINK_TEXT.
- No big pink numbers on navy (white). Never white and sand mixed in one text. Second bar color: light blue #7FA9C9, navy text on it.
- Pink pill only on Market opportunity extra slides (« SIGNAL »). MARKET MAP pill only on the product page.
- Every emoji has a line icon in tools/atelier2/icons.py. CHECK EMOJI_UNMAPPED, EMOJI_MIX.
- Logos: white rounded tile, logo at 66 %, thin light border. The only logo library is githpierre/nmp-logos (cloned next to
  nmp-decks, read its `LOGOS.md`). `assets/logos/` is a generated copy (`<id>.png`, `<id>--symbol.png`, `ini/`, `pp_live/`):
  never add a logo there by hand, add it to nmp-logos (`add_logo.py`) then run `../nmp-logos/tools/decks_sync.py` and `--check`
  (18 Nov 2026). Order in `logo()`: nmp-logos, then assets/logos, then the site favicon (to add to nmp-logos).
  Wordmarks (content wider than 2.5x its height) are refused: unreadable in a square tile. CHECK in import_research.nmp_logo
  and logo() (Neocloud S09, 19 Nov 2026: PaleBlueDot's wordmark showed a blank tile); listed in logos_missing.txt. Still missing: ask Pierre in one
  list; initials meanwhile. Decoration images (assets/deco) are never logos.
- Short date labels of timelines in capitals (« EARLY 2024 », « TODAY »). CHECK DATE_CASE.
- A chart label never touches a bubble or another label. CHECK LABEL_ON_SHAPE.

## Guards
- Every hand-written sentence that quotes the startups base uses `{db.key}` (facts written by make_db_slides.py in
  db_facts.yaml), never a typed figure: a base update re-flows every slide. A YAML value starting with `{` is quoted.
- A key written twice in edits.yaml / live.yaml / db_text.yaml stops the import (DUPLICATE KEY).
- Icons copied from the reference market and still identical are listed by the import (MODEL ICON LEFT).
- Broken images and script errors fail the audit (BROKEN_IMG, JS_ERROR).
- A date is never cut short (« Q3 2 » for 2025). CHECK DATE_CUT. Sentences on rounds read « a $787M growth equity round »,
  « for its life science AI », and name a real publisher: `make_db_slides.py` prints PUBLISHER UNKNOWN for a name it guessed.
- `diff_slides.py` sees a changed word in small text (12 clearly different pixels at 960 px), not only big moves.
- The examples inside the research prompts are written per market in the spec (`examples:`), never left from another market.
- Latest rounds (« Which rounds were announced last? »): when more than half of the 12 latest rounds are under $10M, the slides
  list the 12 latest rounds of $10M or more and the note says so (Pierre, 13 Nov 2026, Healthcare AI: 25 rounds a month).
- A twin whose live slide shows amounts older than the base (S09 after a definition change) is recomputed from the base
  (`tools/pp/s09_from_base.py`) and the live image is replaced in place, same file name (Pierre, 13 Nov 2026).
- A company the live radar (S01) puts outside the market is on no other slide as a player (Tempus, Healthcare AI).
- A converted chart (`x/sig_*`) keeps the bar sizes of its original data: give `vbars` or `hbars` with the values, or use a
  data template. The import prints FIXED CHART, and a chart whose bars cannot be matched to its values is a script error
  (13 Nov 2026: Humanoid slide 51 showed the bars of another market).
- `x/broke_these_startups_did_each` draws its cause dots for the reference market: a new market uses the live S11 twin
  (`pp_killers`) or drops the slide (import: FIXED CHART). Advanced Nuclear, 18 Nov 2026.
- The S09 twin (`invbets`) is computed from the base by `tools/pp/s09_from_base.py`: the build stops when it has no rows
  (Advanced Nuclear, 18 Nov 2026: the slide was empty). Short category names live in `decks/<h>/cat_short.yaml`,
  read by the S09 script and the database slides, as on the live S09 slide.
- A label that the refit puts on two lines must have two words: a single word is cut in the middle (« UTILITI / ES »,
  check WORD_SPLIT). Use the same two-word name on every slide (« Power utilities »).
- Piste A (18 Nov 2026): the research self-check also refuses a word longer than the key's WORDMAX (longest word seen in a
  validated deck, `make_spec.py`), an emoji not in `icons.json` on templates that redraw emojis as icons (`specs/icon_templates.json`,
  made by `tools/icon_templates.py`), and list notes with a line too long or lines of unequal length (shortest under 82%).
  The import prints the same as TEXT LENGTH, `check_results.py` too. Goal: the first import arrives at 0.
- Research results are kept in `decks/<handle>/research`. Each chapter prompt ends with a self-check script (lengths, em dash,
  semicolon): the other LLM delivers at « 0 problems », so the fit to the boxes is not redone here.

## Charts and maps
- Splits by category (donut, shares): never copied from a study. Our own best estimate, explained in the note (up to 3
  lines). Too weak to defend: drop the slide (Claude judges). Categories = the base's (markets.category).
- Charts are computed from the data in deck.yaml (`vbars`, `hbars`, `split`, `dots`, `curves`); never a pixel size by hand.
- Decorative arrows on charts are muted (#789096) and centered on their bar. CHECK ARROW_OFFCENTER.
- World map: each region text on 3 lines, short enough that its box does not widen; leader lines start at the middle of the
  text edge, rounded elbow, end on the dot. CHECK MAP_TEXT_LINES, MAP_BOX_WIDENED. A missing region is added to the template.
- Top players grid: the place of a logo means something (stage, size), never the automatic pattern. CHECK GRID_ROBOTIC.
- Google Trends: curve divided by 2 after Google's August 2025 jump, 3-week median, stops at its last peak; the generic term
  with the clearest rise is kept (no ambiguous or near-zero term).

## Fixed designs (Pierre decided, never propose again)
- Cover: copied from Pierre's cover slide (tools/cover_from_slides.py: photo layers with crop and transparency, title size
  and place); disclaimer under the title, never over the photo's subject; navy button background only on a busy photo.
  CHECK COVER_TEXT_ON_SUBJECT, and the eye: next to the slide thumbnail.
- « In simple terms » framed sentence; dated lists with hollow pink circles; priority tables with fixed geometry.
- Contrast slides « How X turned… »: 8 rows, grey left box, small grey arrow, white logo tile, right box with 2 px pink frame.
  Row spacing and text size stay as they are (more air or bigger text refused, 13 Nov 2026). CHECK CONTRAST ROWS (import), FILL.
- Keep: the small gap at the end of connectors, column headers in line color, the grey emoji of « bad customer experience »,
  2 px pink frames, Pierre's own layouts (no redesign unless he asks; targeted fixes only).
- Last slide « Thank you for your time »: title left-aligned.

## Product-page slides (pp_*, S01-S12)
- In a deck, a twin copies the live slide exactly (decks/<slug>/live.yaml); twins are not listed in the sources.
- S04 pains: 6 pains, audience headers on 2 lines. S07 risks: each event on 3 lines. S08 drivers: 30 events, 3 highlighted,
  46 characters max. S11: at least 5 rows. S12: 6-7 criteria, 5-6 companies. S03 donut: labels beside slices, 2 logos per category.
  CHECK in tools/pp/audit_pp.py.

## Extra slides (slides complémentaires)
- A strong, sourced fact shown with the template that fits the data; 5 to 15 per deck, placed where they serve the story.
- The slide before must already raise the idea (`link:` in extras.yaml; the import warns without it).
- One design at most twice among a deck's extra slides. Side text never wider than its kicker, centered.
- Market opportunity: the signals slide lists 6-8 signals, each followed by its SIGNAL slide, in the same order;
  its first sentence says why the fact shows the market is hot.
- SIGNAL slides: the content block sits a little lower than the middle between the pill and the note (55 % of the free
  space above), never stuck under the pill (fixlib `pillCentre`, skipped on product-page twins).
- A SIGNAL shows momentum now. `fresh: {period, end}` on each: month at most 6 months old, quarter 9, half-year 12, a
  cumulative total at a date 12; a yearly figure is the current year (last year until April). No fresh figure published:
  estimate the current year from the latest half-year or quarter (« should sell… »), with the arithmetic in the note.
  An estimate is shown as 2 bars, last year against this year « (EST.) » (chosen over 3 bars and over a strip of figures).
  CHECK SIGNAL STALE, SIGNAL NO DATE (import). Older figures stay fine on the other slides.

## Delivery
- Name « <Market> - Q<n> <year> - newmarketpitch.com ©.pdf », quarter of the day of production.
- PDF = screen render of each slide (2x PNG, lossless: JPEG 72 turned soft shadows on navy into blocks, Pierre 14 Nov 2026) over the vector page (text selectable, links clickable), qpdf compression.
- Audit images (PNG) are the screen render with images. First build: every slide, on sheets of 6. Later rounds: the slides
  listed as changed (tools/diff_slides.py). Pierre sees the deck on a review page before the PDF.

## Review pages for Pierre
- One scrolling HTML page: yellow band (what changes, Claude's pick and why), Oui / Non per item, Claude's pick in green,
  « Copier mes réponses ». Round 2+: only what he must see again.
- Atelier du juge = a recurring judgment (6 real cases, variants A/B/C, one thing changes). Design choice = 6-9 truly different
  variants, large. « Sois créatif » = change the layout, not a detail.

## Pierre's review of Healthcare AI (14 Nov 2026), each with its check
- Amounts read at a glance: $10B or more without decimal ($56B, never $56.01B), under $10B one decimal at most ($2.1B), same for M.
  A share keeps one decimal at most. Applied by the import to every text except notes (notes keep the exact arithmetic). Given to the research LLM as a format rule.
- The pages of a series (1/2, 2/3…) share one design and one number of items. CHECK SERIES MIXED (import). The three « How can we categorize companies » pages are ALWAYS one series 1/3, 2/3, 3/3 (solution, buyer, business model) in the same design with the number of base categories on every page: buyers and business models get as many rows as the categories (Pierre, 18 Nov 2026, said twice). `page: null` is never used to silence the check on them.
- One icon per category on a slide: never the same icon twice (18 Nov 2026, HAI buyers). CHECK ICON TWICE (import, blocks --png). Labels of a categorize page all on the same number of lines.
- The three circles (markets it sits between): two words each, one word per line. CHECK VENN WORDS.
- Top companies slide: company names in capitals (import).
- Segment dividers: no slide title on top. Their name takes the largest size, up to 34pt (Pierre, 18 Nov 2026: 40pt was too big), at which the longest name of the deck stays clear of the side arrows, and every divider uses that size (fixlib deck()).
- A map region renamed to a country puts its dot on that country (worldmap PL table). CHECK MAP PLACE for a name the map does not know.
- Text lengths Pierre asked for (targets for the research prompts): myth answers ~125 characters, « truths that flipped » right boxes ~70,
  rows of dated timelines (latest developments, deals, news, scored big, rounds) 120-140 characters with one more concrete fact.
  Rounds rows from the base say what the company does (markets.csv what_they_do).

## Method v2: one text spec for every slide (Pierre, 14 Nov 2026)
- specs/slides.yaml (tools/make_spec.py) gives every template key its range: max = the longest text that fits in a validated deck,
  min = 0.85 x the median length in the deck filled to Pierre's remarks (body texts only), caps and words from specs/overrides.yaml.
- The research prompts print the range under every slide and the self-check refuses any text out of it, plus em dash, semicolon and
  amount format. tools/check_results.py runs the same checks on any result file before import.
- The import prints TEXT LENGTH for every text out of range (gate, like the other capital warnings) and writes CAPS keys in capitals.
  A sentence built from the base (db.yaml) is only held to its maximum.
- Market definition, pain points and value creation are written by Claude from the same brief (decks/<handle>/evergreen/),
  in the result format, checked with tools/check_results.py. The research zip holds only the chapters with dated facts.
- Texts brought into range after a deck was built go in decks/<handle>/lengths.yaml (applied last, `__replace2__` for nested texts).

## Longevity first build (18 Nov 2026), each with its check
- Deck logos sit in square tiles: the import takes the `--symbol` file of nmp-logos when there is one (a wide wordmark like Function Health is unreadable at 30 px). Check: `nmp_logo(..., symbol=True)` in import_research.py.
- Database sentences use the names people use: investor suffixes are cut (« Fidelity », « Lightspeed », never « Fidelity Management & Research Company »), company suffixes too on narrow slides (« Character Bio, Aeovian »), the category is the short slide name of cat_short.yaml, never the base label, and place names keep their capital (« in India »). Check: make_db_slides.py inv_short, co_short, CS, PROPER.
- A publisher label on a slide is a real name (« SEC filing », « Mint »), never a domain stem (« Formds », « Mentionfox »). Check: PUBLISHER UNKNOWN in make_db_slides.py, PUB in build_sources.py.
- The stage pill of the pipeline slide holds 6 characters at most (« PH 1 »). Check: STAGE LABEL in the import.
- Key sources written but build_sources.py not run leaves the reference market's sources: the import says MODEL SOURCES LEFT when sources_key.yaml is newer than sources_slides.yaml (piste B gate).
- Labels and texts on the same card belong to the same company: read every card of a « stand out » or radar slide against its name (NewLimit and Neko Health texts were swapped by the research; CoreWeave and Fireworks on Neocloud). CHECK: `check_results.py` prints each header-text pair of x/startups_stand_out as a REVIEW line when the text does not name the company: read them.
- A KPI slide with up arrows only shows rises: a falling funnel (600 teams to 10) takes a face-off or a funnel.
- The footer label is the exact line of data/market_labels.txt (« Longevity market »), in plans/<handle>.yaml.
- The cover title can contain « M A R K E T »: cover_from_slides.py finds the subtitle by « P I T C H ».
- « What is behind these categories? » (ed048) only follows a split of the market by category (ed047p); without it the slide is dropped by the import (Pierre, 18 Nov 2026).
- Number badges (1-8 in the corner of cards) keep their numbers: the import ignores an emoji given for a badge (empty circles on Longevity and Advanced Nuclear, 18 Nov 2026).
- Segment dividers of one chapter all have their name on 2 balanced lines, so every divider of the series has the same number of lines (Pierre, 18 Nov 2026).
- A doubt on whether a company belongs to the market is settled by Claude with the market's decision rule
  (nmp-seo market_definitions.csv), at step 0 with `tools/borderline.py`, never asked to Pierre (18 Nov 2026, said many times).
- Database slides and the S09 twin count only startups by the base's own rule (`startup_status.table_startup_base`): the base keeps
  non-startups in a market as history (Lanserhof, founded 1984, sat among Longevity rounds; Rolls-Royce SMR among Advanced Nuclear
  rounds, 18 Nov 2026). Never remove a non-startup from markets.csv to hide it: filter in the tool.

## Neocloud first build (19 Nov 2026), each with its check
- A title copied from the reference deck must be about this market (ed140 kept « developers, doctors and regulators » from In Vivo CAR-T). CHECK: `check_results.py` REVIEW line for a model title shared by 3 other full decks or fewer.
- A product-page twin is fixed when the live slide contradicts its own title (S04 « customers » listed the neoclouds' own pains and a « Crypto miners » column): the twin follows the pain segments, the new version goes to the retour.
- An extra slide carries its own `sources:` in extras.yaml, so the sources list includes them (import_research).
- Sources pages: publisher names come from the PUB table of build_sources.py; an IR host (x.gcs-web.com) gives the company, a CDN file with /CIK-/ is a SEC filing, a lower-case brand (fal) keeps its case.
- « What is behind these categories? » (ed048) explains every category of the donut just before it (ed047p), in the same order: 3 cards per page, so 6 categories make 2 pages (ed048 1/2 + ed048-2 2/2 in extras.yaml). CHECK CATEGORIES MISMATCH (import, blocks --png) (Pierre, 19 Nov 2026: 6 categories on the donut, 3 behind it).
- The card labels of a series of pages share one line count: if one label needs 2 lines, every label of the series goes on 2 balanced lines (import).
- Sibling cards of every slide, template slides included, have the same number of lines (Pierre, 19 Nov 2026, slide 12: cards on 3 and 4 lines). CHECK CARD_LINES (audit_layout): BODY_LINES only read the converted (raw) slides, so the cards template was never checked. Chart notes above bars (fundbars) put each comma part on its own line for the same reason.
- The block of the pp_winner table (criteria + company columns) is centred on the slide (Pierre, 19 Nov 2026, slide 187: 36 px to the right).

## AI in drug discovery first build (20 Nov 2026)
- ed175: each capital header is the company of the sentence just under it in the prompt model (pairs 19/18, 23/22…). The
  prompt now shows the pairs together; check_results flags a header whose text's source names another header's company.
- Amount rule applies to slide text and claims, never to source quotes (copied word for word). Halves round up ($64.5M -> $65M).
- Notes over bars from the startups base: always three short lines (top company, top round, number of rounds).
- A cover title that runs past the slide edge gets a smaller size in cover.yaml, and Pierre is told.
- In YAML, write the keys 'on' and 'off' in quotes (bare, they become true/false).
- Market size and CAGR: the deck follows the live page (S03) unless the research is clearly better sourced; then the deck takes
  the research figures and the new S03 goes into the retour (AI drug discovery, 20 Nov 2026: $3.4B / 26 % instead of $4B / 20 %,
  Pierre left it to my judgment). Always say which one was kept and why.
- Source slides: build_sources prints PUBLISHER GUESSED for a name made from a domain (« Chaidiscovery »): add the real name to PUB
  before the review (AI drug discovery, 20 Nov 2026: 30 such labels).
- Pierre, 20 Nov 2026 (AI drug discovery review):
  - Myths slides: the myth (left box) always on 2 lines, the answer (right box) 3 to 6 words longer than the old 105-125
    characters, so 125-150 (specs/overrides.yaml). CHECK BOX_LINES (audit_layout): sibling boxes where one short text counted
    as a label and the others as bodies were never compared (« Big deals mean big cash » on 1 line).
  - Categories slides: each description on 2 lines and well filled, 60-72 characters (3 lines touch the box). CHECK
    CATEGORY_LINES.
  - Pages of one series (1/2, 2/2) have exactly the same boxes. Converted PowerPoint pages (« …_2 ») had other widths
    (value bubbles 307 px against 268 px, news texts 539 against 583): import now gives every page the template of page 1
    when the keys match, the _2 templates of news and setbacks are aligned on page 1, and SERIES GEOMETRY blocks --png
    when widths still differ.
  - A single waffle grid sits next to the dashed line of the side text, with bigger squares, never at the far left.
  - specs/slides.yaml is generated: Pierre's targets go in specs/overrides.yaml, then run tools/make_spec.py.
- Google Trends (22 Nov 2026, rewritten after the control curves): « weather » and « youtube » stay flat, but every small
  term moves together (stablecoins, AI insurance, managing general agent, general agent, chatgpt insurance): up from July
  2025, same drop the week of 12 July 2026, collapse in October 2026. Google changed how it counts small terms, not big ones,
  so dividing by a control term fixes nothing. Never present a move since mid-2025 as a rise, a fall or a signal. The title
  of the Google slide is about the long rise since 2021, and a note explains the Google effect. Show Pierre the curves of
  each new market before applying this rule.

## Natural hydrogen first build (21 Nov 2026), each with its check
- A young market can have fewer than 12 rounds since 2024: ed156/ed157 are completed with the latest older rounds of the same
  startups, never left with the template rows (an in vivo CAR-T round, Starna Therapeutics, sat on Natural hydrogen's ed157).
  CHECK make_db_slides stops when it still has fewer than 12 rounds.
- An undisclosed round is never a « biggest round » bar ($0M Koloma on ed165p), and a half-year with only undisclosed rounds says
  « Koloma, undisclosed amount, in 1 round » over its bar, never a bare arrow. « 1 round », never « 1 rounds ». CHECK in
  make_db_slides (raises() skips amount 0, ann() writes the zero case, plural by count).
- S09 twin: a category with no public amount is left out of the rows (it drew « $nanM »). CHECK s09_from_base prints DROPPED.
- No word split by a hyphen at a line end (« iron- / rich », « source- / to-trap »): build.py wraps every hyphenated word in
  <nobr> (24 Nov 2026, our fonts have no non-breaking hyphen), CHECK HYPHEN_SPLIT (audit_layout) stays as the safety net.
- A name and its number stay on one line (« Ramsay / 3 »): build.py binds « Word N » with a non-breaking space.
- US English on every slide (« modeled », « license »); a proper name keeps its spelling (« Petroleum Exploration Licence »).
  CHECK check_results « British spelling ».
- One round, one figure across chapters: Koloma was « $245M » on 3 slides and « $246M » on 6. Use the base figure. CHECK
  check_results « one round written two ways » (same company, amounts within 3%).
- A summary line that names several startups keeps each backer with its own startup (« Koloma $400M and Mantle8 $36M, with bp and
  Rio Tinto as backers » gave Snowfox's backers to the others). No check can see it: read every multi-company line once.
- One unit per fact in a deck: « 4,100 square kilometers » everywhere, not « 1,600 square miles » on one slide.
- Page 2/2 takes the title of page 1/2 (ed205 kept « Which startups scored big recently? » in every deck). CHECK import prints
  PAGE TITLE and copies it.
- Maturity score box (.maturity .score) is 180 px wide: at 330 px a low score ran past the left margin.
- Pierre, 21 Nov 2026 (Natural hydrogen review):
  - Category slides (sx_categories_n): the icon circle overlaps the top-left corner of the label box, as in the 4-row
    PowerPoint model (icon top = box top - 5.3 px). It sat 9 px lower on every slide made with sx_categories_n.
  - Estimates slide: the value cell holds the amount alone (« $4.6B »), never « $4.6B 2026 »; the year goes in the comment.
    CHECK check_results « estimates value with a year »; the research prompt says it.
  - A column of numbers is aligned the same way top to bottom (ranking « 4 » was left-aligned among centered numbers, a copy
    defect of the PowerPoint template). CHECK ALIGN_ODD (build.py) on every x/ template of the deck.

## Stablecoin payments first build (22 Nov 2026), each with its check
- A company that the S01 radar (ed007p) places outside the market is never a player on another slide. The live S05 and S12
  compared Tether, Circle, PayPal and Ripple: both twins were rewritten with players from inside (Bridge, BVNK, Rain…), as the
  S04 Neocloud rule does for pains. A sentence may still name it (« bought by Stripe »). CHECK tools/check_outside.py (run by
  rebuild.sh, OUTSIDE PLAYER blocks --png).
- (skip_rounds line of 22 Nov 2026: replaced by the 24 Nov 2026 rule below, the base rules decide.)
- A favicon that two sites share is the host's icon, not the company's (MoonPay showed Vercel's triangle). CHECK
  import_research refuses it and prints FAVICON SHARED; known cases go in NO_FAVICON.
- (Stablecoin payments Trends line of 22 Nov 2026, `to_today` and ÷2: replaced by the 24 Nov 2026 rule below.)
- Market size is the revenue of the companies, never the money that flows through them. When the research only measures flows
  ($643B of stablecoin payments a year), the deck keeps the live revenue figure and explains it as flows × a take rate written as
  our assumption (0.8%, slides 43-44). Pierre approved, 22 Nov 2026. No check: read the size slides against the live S03.
- The market name of import.args (--name) is written as in a sentence (« stablecoin payments »), so titles never capitalize it
  mid-sentence; a proper name keeps its capitals (« In Vivo CAR-T »).
- Investor names: a lead whose short form is a generic word (« led by Blockchain » for Blockchain Capital) keeps its full name.
  Category words keep acronyms (« payment APIs », never « payment apis »). Done by make_db_slides (GENERIC_INV, case rule).
- Pierre, 22 Nov 2026 (Stablecoin payments review): every recommendation of the review page accepted (7 SIGNAL slides, the
  domestic-share and Circle-margin extras, the donut shares, the rewritten S04, S05, S09 and S12, the S11 live slide replaced by
  the deck's ed199p in the retour).
- Step and risk cards (`LABEL\n\nbody`): the label is everything before the blank line, written on ONE line; the box wraps it. A line break inside the label pushes its second word into the body (AI in insurance, 22 Nov 2026). CHECK LABEL SPLIT (import).

## MGA first build (22 Nov 2026)
- Segment names (pain and value) are checked BEFORE they are proposed to Pierre: no word over 10 letters, since they go in capital
  card labels (« Business policyholders » had to become « Business clients » after approval). CHECK SEGMENT WORD TOO LONG
  (make_market_prompts.py).
- Round sentences from the base read « an $80M Series C » and never « for its specialty commercial »: when the company's own
  description is too long, the sentence uses `decks/<h>/cat_phrase.yaml` (« for its specialty business insurance »); a plural
  noun of people (« Homeowners insurance… ») is never read as a verb (make_db_slides.py).
- A market whose Google curve is noise (Pierre's call, MGA) has no Google slide: `ed039p: {drop: true}` in edits.yaml, and
  ed032 lists seven SIGNAL slides instead of six plus Google.

## AI data center first build (22-23 Nov 2026)
- (AI data center Trends rendering C of 22 Nov 2026, `dash_from`: replaced by the 24 Nov 2026 rule below.)
- Sibling rows of a table hold the same number of lines (Pierre, 23 Nov 2026, AI data center « Which pains deserve attention
  first? »: pains on 1 line next to pains on 2). Short values (« 17 GW », « $1.4B ») never wrap. CHECK: audit_layout ROW_LINES, LIST_LINES (rows with only inline styles, e.g. league tables)
  (same-class siblings in a mixed grid, which CARD_LINES skipped) and VALUE_WRAP; the key-trend template's value boxes are
  100px wide and nowrap (they were 36-43px).

## MedTech first build (23 Nov 2026), each with its check
- The research prompts copy the structure of the reference deck (in vivo CAR-T); a market name the other LLM leaves in a
  result (ed097 kept « in vivo CAR-T » in its title) is now a problem in tools/check_results.py, not a REVIEW line. The
  import already refused it (MODEL MARKET LEFT blocks --png); the check now catches it as soon as a result comes back.
- One company = one id in nmp-logos. Two ids with the same domain (pear-therapeutics + peartherapeutics) make find_logo give
  up and the deck draws an initials tile. Check: import_research.py prints LOGO AMBIGUOUS with the ids; merge them in
  nmp-logos/index.csv (keep the base id, old file in bad_files). index.csv is CRLF: keep it CRLF when rewriting it.
- Market sizes of $1,000B and more are written in trillions ($1.06T): tools/pp/pp_prepare.py money().
- A Trends curve cut before mid-2025 shows its real period under the chart (live.yaml `period:`, pp_trends.j2), never
  « last five years ».
- Database rows: the line limit counts the joining words around the publisher (tools/make_db_slides.py, margin 10).
- Numbers of 1,000 and more always carry a thousands comma, in templates too (share_waffle printed « 1230 of 1614 », MedTech).

## Pierre, 24 Nov 2026 (merge of the 8 delegated returns), each with its check
- Google Trends, ONE look for every deck: the curve is cut at 2025-07-27 (`cut: '2025-07-27'` in live.yaml ed039p), the caption
  gives the period (« November 2021 to July 2025 »), the title and the ed032 line speak of the rise up to mid-2025, and the note
  says Google changed how it counts small terms in mid-2025. This replaces `to_today` (Stablecoin payments), `dash_from`
  (AI data center) and the cut in May 2025 (AI in insurance): the options stay in pp_prepare only so old states rebuild. A term
  at 0 or « <1 » most weeks before the cut has no Google slide (MGA). CHECK: pp_prepare.trends applies the cut by default
  and prints TRENDS TEXT (blocks --png) when the date or note still speaks of « the last five years » or « lately ».
- A doubtful round is fixed in the base by the base rules (nmp-seo RULES 131: a round sourced only by a database such as Forge
  stays counted, low confidence; a repeat of an earlier round is removed), never hidden from the slides by a deck conversation.
  skip_rounds.yaml is empty and stays for a round the base cannot fix yet. A round already ruled on goes to checked_rounds.yaml
  (round id + rule), so WEAK ROUND SOURCE and ROUND EXTENSION do not warn about it again.
- A Trends title that names a multiple (« doubled », « tripled ») matches the stat shown (« doubled » on ×2.5 slipped
  through on Longevity, 24 Nov 2026). CHECK: TRENDS TEXT in pp_prepare.trends.
- Database slides of a thin market (24 Nov 2026, Natural hydrogen): a bar with rounds but no public amount reads « Undisclosed »,
  never « $0M » (make_db_slides sets lab, fundbars shows it); « most active investors » with one deal each is dropped.
- A company the radar places outside but the market definition includes (Function Health, preventive testing in Longevity v3)
  leaves the radar corner, replaced by a clearly outside company with a logo (Calm). OUTSIDE PLAYER finds it.
- The PDF name starts with a capital letter whatever the deck header says (build.py).
- Google curves are drawn smooth: 3-week median, then a 5-week average for the drawing only (Pierre, 24 Nov 2026, « lisse toi-même »:
  small whole numbers drew steps). The stat (×N) is computed before the average, so it never moves. No re-download needed for that.
- S09 (ed168p) has 7 rows at most: a category that would make an 8th row is merged into « Other » in cat_short.yaml (Advanced
  nuclear, 24 Nov 2026: 8 rows pushed the table into the title). cat_short.yaml keeps the short names of the live S09 slide.
- A logo found by adding a suffix to the name (« Wyre » -> wyre-ai) must belong to the same company: same domain in nmp-logos, and
  never an « -ai » guess without a domain (Wyre showed the logo of Wyre AI, Stablecoin S11-01, 24 Nov 2026). import_research.logo checks it.
- A market term too rare on Google (0 most weeks before the cut) gives way to its wider parent term, and the text says so
  (In vivo CAR-T follows « car-t », Pierre, 24 Nov 2026). A curve with values of only 0 to 8 before the cut draws a staircase:
  the drawing is smoothed (rule above), no new download is needed.
- « a » or « an » before an amount follows the figure as printed, after rounding (« an $11.9B » became « an $12B »,
  Neocloud): tidy_numbers fixes the article, CHECK: tools/check_article.py (ARTICLE AMOUNT, blocks --png).
- OUTSIDE PLAYER on a hand-made slide: the outside company leaves the slide, the note counts what is left (IREN left the
  Neocloud setbacks grid, now five operators).
- Companies shared by two markets are described the same way in both decks (AI in insurance and MGA, Neocloud and AI data
  center): the later deck copies the earlier one's wording for the same fact.

## Synthetic biology first build (26 Nov 2026), each with its check
- A segment name that does not fit a two-line label (one long word: « Biofoundries », « Therapeutics ») gets a second word or a
  hyphen before the deck is built (« Robotic biofoundries », « Bio-manufacturing »), and keeps it everywhere. CHECK check_results
  (one-word label, word longer than WORDMAX).
- A list of company names (« EvolutionaryScale, eGenesis ») is never cut or renamed to pass WORDMAX: the layout audit (WORD_SPLIT)
  judges it. A label measured on a build that holds on one line raises its WORDMAX in specs/overrides.yaml, never a shorter name.
- The S03 twin (ed052p) takes the market size of the deck's own size chapter (ed045), never an older figure of the live page;
  the live image is replaced at delivery. CHECK: read ed045 and ed052p side by side at step 5.
