# Rules: what a deck slide must look like

One line per rule. `CHECK` = verified by code (build.py, tools/audit_layout.py, tools/pp/audit_pp.py): no need to remember it,
the build tells you. Rules without CHECK need the eye. The process is in PROTOCOL.md. Full history: archive/RULES-log-2026-11.md.

## Content
- US English, plain words for a smart non-expert, short sentences, no em dash, no exclamation mark.
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
- Note (bottom left): starts with « We », 2 balanced lines by default (YAML list, no dots), 1 line if one idea fits,
  3 only for 3 important ideas; never runs into the footer label. CHECK NOTE_BALANCE, NOTE_WIDTH.
- Centred sentences of 2 lines or more (stories, why texts): lines as equal as possible, like titles (fixlib `balance`).
- Footer label: Pierre's list `data/market_labels.txt`, one line. CHECK in build.py, FOOT_LABEL.

## Text boxes and grids
- Sibling boxes: same width, same font size, same number of lines (labels too). A text too long is shortened, never shrunk.
  CHECK FONT_MIXED, LABEL_LINES, BODY_LINES.
- Lines balanced (no orphan word), a number stays with its unit (automatic, rawfit.js).
- Card labels on 2 lines; a one-word label gets a second word (« CAR MAKERS »).
- Text never touches its bubble. CHECK TEXT_PAD. Card text centered vertically; pill + text centered together.
- Icon-card grids: every text on 4 lines. Dated rails (rounds, deals, news): 6 dates per page, every entry on 2 lines.
- Body inside x 90-870. CHECK MARGIN, MARGIN_ALL.
- The layout follows the number of items: 4 cards of a 6-slot grid go 2 + 2, N categories use a template that takes N.
- Same slide type = same look on every page of a series (1/2, 2/2): decisions are copied by make_decisions.py.

## Colors, icons, logos
- Pink never as thin text or thin small icons on navy; pink fills (pill, bar, bold) or a 2 px frame are fine. CHECK PINK_TEXT.
- No big pink numbers on navy (white). Never white and sand mixed in one text. Second bar color: light blue #7FA9C9, navy text on it.
- Pink pill only on Market opportunity extra slides (« SIGNAL »). MARKET MAP pill only on the product page.
- Every emoji has a line icon in tools/atelier2/icons.py. CHECK EMOJI_UNMAPPED, EMOJI_MIX.
- Logos: white rounded tile, logo at 66 %, thin light border. Order of search (tools/import_research.py `logo()`):
  assets/logos, then Pierre's libraries (clone githpierre/nmp-pages `nmp-funding/logos/*/tile|fav` and
  githpierre/nmp-product-pages `w/logos_all`, market-prefixed first), then assets/logos/pp, then the site favicon.
  Wordmarks (content wider than 2.5x its height) are refused: unreadable in a square tile. Still missing: ask Pierre in one
  list; initials meanwhile. Decoration images (assets/deco) are never logos.
- Short date labels of timelines in capitals (« EARLY 2024 », « TODAY »). CHECK DATE_CASE.
- A chart label never touches a bubble or another label. CHECK LABEL_ON_SHAPE.

## Charts and maps
- Charts are computed from the data in deck.yaml (`vbars`, `hbars`, `split`, `dots`, `curves`); never a pixel size by hand.
- Decorative arrows on charts are muted (#789096) and centered on their bar. CHECK ARROW_OFFCENTER.
- World map: each region text on 3 lines, short enough that its box does not widen; leader lines start at the middle of the
  text edge, rounded elbow, end on the dot. CHECK MAP_TEXT_LINES, MAP_BOX_WIDENED. A missing region is added to the template.
- Top players grid: the place of a logo means something (stage, size), never the automatic pattern. CHECK GRID_ROBOTIC.
- Google Trends: curve divided by 2 after Google's August 2025 jump, 3-week median, stops at its last peak; the generic term
  with the clearest rise is kept (no ambiguous or near-zero term).

## Fixed designs (Pierre decided, never propose again)
- Cover: photo, title in spaced capitals, NEW MARKET PITCH under it, disclaimer right under the title; navy button background
  only on a busy photo.
- « In simple terms » framed sentence; dated lists with hollow pink circles; priority tables with fixed geometry.
- Contrast slides « How X turned… »: grey left box, small grey arrow, white logo tile, right box with 2 px pink frame.
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
- SIGNAL slides: the content block is centred between the pill and the note, never stuck under the pill (fixlib
  `pillCentre`, skipped on product-page twins).

## Delivery
- Name « <Market> - Q<n> <year> - newmarketpitch.com ©.pdf », quarter of the day of production.
- PDF = screen render of each slide (2x JPEG q72) over the vector page (text selectable, links clickable), qpdf compression.
- Audit images (PNG) are the screen render with images; look at every slide before showing anything.

## Review pages for Pierre
- One scrolling HTML page: yellow band (what changes, Claude's pick and why), Oui / Non per item, Claude's pick in green,
  « Copier mes réponses ». Round 2+: only what he must see again.
- Atelier du juge = a recurring judgment (6 real cases, variants A/B/C, one thing changes). Design choice = 6-9 truly different
  variants, large. « Sois créatif » = change the layout, not a detail.
