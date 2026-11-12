# Extra slides library (slides complémentaires)

Name: "extra slides" / « slides complémentaires ». Do not call them "signal slides" any more (Pierre, 12 Nov 2026: ambiguous). File and template names (sig_*) are historical.

Pierre, 12 Nov 2026: signal slides are NOT part of the base deck. They go into a deck only when the research finds a strong,
sourced data point that fits one of the formats below. Each format is a visual shape (4 bars + a story, horizontal bars,
a dot grid…), not a chapter: the same format can sit in Market opportunity (the market is hot), Market challenges,
Growth drivers, Investor bets… The kicker on top is set from the chapter where the slide is placed.

- Templates: `templates/slides/x/sig_<format>*.j2` (converted from the series PowerPoints of the Drive folder
  « temp - <format> - to add to other decks »). Examples: `decks/signals` (`python3 tools/make_signals_lib.py <pptx dir>`),
  first slide of each series + every cell-therapy slide (usable as is for in vivo CAR-T, data already researched).
- EdTech signal slides carry `signal: <format>` in `decks/edtech-full/deck.yaml`; new decks start without them.
- Process for a new market: (1) the research prompt screens EVERY format below and returns only candidates that pass
  the conditions, with numbers, dates, sources and a strength score; (2) we keep the strongest (2 to 4 per chapter at most,
  never far-fetched); (3) one slide per kept signal, title = the striking fact, kicker = the chapter where it goes;
  (4) complementary research when a figure needs it. Rules of the series (nmp-slide-generation) still apply:
  no date words in titles of trends, every number of the title visible on the chart, one measure per chart,
  the pink bar is the one the title talks about, notes start with "We".

## Process notes (Pierre, 12 Nov 2026)
- The library is evolving. None of these designs is final: the converted series slides are legacy and will be retouched.
  When a signal slide is made for a real deck (in vivo CAR-T first), Pierre reviews its design; once validated, the template
  is marked validated here and the new example replaces the old one in `decks/signals`.
- Integrated in a deck, a signal slide shows the deck's market name bottom right (never "Signals library") and the kicker of
  the chapter where it is placed.
- 5 to 15 extra slides per deck, never 60. Two steps, never skipped: (1) Claude shows the candidate slides on a review page and Pierre validates the design; (2) Claude proposes for each one its place "between slide N and slide N+1" (with both titles), Pierre approves. Only then the slide goes into the deck.
- Sources of signals: the deck research (prompt 11, all formats screened), our startups database (nmp-seo, data/startups:
  funding, valuations, metrics, employees), and complementary research when a figure needs it.
- The cell-therapy examples of the library are not reused for in vivo CAR-T: its own research finds its own signals.

## Pill on extra slides
Only in the Market opportunity chapter, and it says SIGNAL. No pill anywhere else (Pierre, 12 Nov).

## Validated templates
Validated by Pierre on 12 Nov 2026 (in vivo CAR-T examples in `decks/extra-invivo`, ids in brackets; inserted in the deck through `decks/in-vivo-car-t/extras.yaml`):
- deal-timeline (1B), key-trend with proportional bars (1C, 2B), kpi-trio (2A, 3A).
Refused: value-ladder as a list of deal values (1A), key-trend for a fall in a tiny cohort (4A).
- Pierre, 12 Nov: the TEMP series formats (sig_*: dominance, announced-vs-built, funnels, curves, dot grids…) must be used too, not only the EdTech signal templates. Each review round shows them.

## Formats

| format | what it shows | data needed | usual chapters | keep only if |
|---|---|---|---|---|
| key-trend | one measure, before vs after (2-5 bars) | a sourced measure at 2+ comparable dates | Market opportunity, Market challenges | the change is big (≥ 1.5x or a clear break) |
| rules-wave | yearly count of laws, bills, approvals or suits (4 bars + story per bar) | one source counting the same thing each year | Market challenges, Market opportunity | the last bars clearly jump; partial year marked |
| funnel | counts by stage, last stage pink | stage counts from one source | Market challenges, Pain points | the drop is striking (few reach the end) |
| country-gap | one measure by country | same measure, same year, 3-6 countries | Tech and infra, Market challenges | a ≥ 2x contrast |
| waiting-line | backlog or waiting time vs capacity | waitlist and served counts | Pain points | waiting ≥ capacity |
| incident-count | yearly official count or loss | official series (not one that only rises with activity) | Pain points | clear rise |
| announced-vs-built | planned vs actually built or launched | announcements + delivered counts | Market challenges | big gap |
| idle-capacity | built capacity vs used | capacity and usage | Market challenges | ≥ 30% idle |
| promise-tracker | the same target date moved again and again | ≥ 3 dated promises for one milestone | Market challenges | ≥ 3 slips |
| lobbying-spend | federal lobbying of a company or rivals | LD-2 filings | Market challenges | a jump or a striking amount |
| cost-threshold | a cost or price over time vs a reference it crosses | 4-10 sourced prices + a reference | Tech and infra, Value creation | it crosses or misses the line |
| penetration-curve | share of people using it, by year since launch | survey series | Growth drivers | fast rise vs earlier tech |
| adoption-race | months to a milestone ($100M, 1M users…), new vs earlier leaders | dated milestones of 2+ companies | Growth drivers | clear speed-up (Pierre's favourite) |
| earnings-mentions | companies citing the theme on earnings calls, by quarter | FactSet / IoT Analytics series | Market opportunity | ≥ 3x over the series |
| searches-vs-funding | Google searches vs funding rounds, both vs 2024 | Trends CSV + our rounds | Market opportunity | a clear lead or gap |
| real-world-vs-funding | a real-world price or use vs funding bars | sourced line + our quarterly funding | Market opportunity | the two move apart |
| incumbent-crash | a listed incumbent's share price since a market event | quarterly closes + dated event | Market opportunity | ≥ 50% fall since the event |
| fallen-star | the market's once-famous listed company vs its peak | share price, splits adjusted | Market opportunity, Startup killers | ≥ 80% below peak |
| challenger | a private challenger catching up with a listed giant | valuations / revenue of both | Top players | the gap closes fast |
| dominance | the leader's share over time | share series of one source | Top players | a rising or crushing share |
| contract-share | public contract money to newcomers vs incumbents | award amounts | Top players | newcomers jump |
| multiple-gap | market value per $1 of sales vs peers | market caps + revenue | Value creation | ≥ 3x gap |
| profit-gap | operating result per $1 of sales | filings | Value creation | striking loss or a turnaround |
| revenue-per-head | revenue per employee, new vs old players | revenue + headcount | Value creation | ≥ 2x gap |
| dollar-split | where each $1 paid by the customer goes | a published price breakdown | Value creation | a surprising split |
| single-customer | a company's revenue share from its largest customer | filings over years | Value creation, Startup killers | ≥ 30% from one customer |
| funding-by-region | share of rounds by region, 3 years of dots | our funding database | Investor bets | the share moves clearly |
| funding-by-segment | share of rounds of one segment | our funding database | Investor bets | a rising segment |
| funding-by-stage | share of rounds by stage | our funding database | Investor bets | clear shift (late vs new) |
| funding-share | top startups' share of all funding | our funding database | Investor bets | 2-3 take ≥ 50% |
| mega-rounds | share of $100M+ rounds | our funding database | Investor bets | a jump |
| corporate-backers | rounds with a large company among investors | our funding database | Investor bets | a rising share |
| repeat-raisers | rounds raised by startups that raised in the past 12 months | our funding database | Investor bets | a rising share |
| round-size | median round of one stage by year | our funding database | Investor bets | ≥ 1.5x |
| forecast-gap | every forecast for the same year, ranked | ≥ 5 publishers, same year | Market size | ≥ 3x even without one extreme |
| google-trends | one search curve (product-page slide S02) | Trends CSV | Market opportunity | always one per deck (corrected, cut at the peak) |
| kpi-trio | 3 big numbers of one leader (EdTech 33) | 3 sourced metrics | Market opportunity | strong growth |
| deal-timeline | dated deals on a line (EdTech 35) | 4-6 dated deals | Market opportunity | a wave of deals |
| value-ladder | ranked values of the biggest players (EdTech 36) | 4-6 valuations | Market opportunity | several $1B+ |
| icon-grid | a rate shown as a grid of icons (EdTech 37) | one striking rate | Market opportunity | easy to picture |
| funding-event | 4 dated steps of a funding story (EdTech 38) | yearly funding + one event | Market opportunity | ≥ 2x |

## New share templates (12 Nov 2026, to validate)
`templates/slides/share_*.j2` (bars100, rings, slope, waffle, hero, gauges, bubbles): one share per year, fully data-driven (`years: [{x, k, n, p}]`, `big`, `story`, `on`, `off`, `what`). Examples in `decks/extra-invivo-v`. Pierre (12 Nov): the dot rows of the converted TEMP slides are ugly with few rounds; never show 40 slides in the same format, vary the templates.
Refused on 12 Nov: N8 searches vs funding (reads as hype, not opportunity), N10 dollar split (unclear), N11 key trend 2021 vs 2025 (backward-looking), N7 funding share bars.

## Designs sx_* validés le 12/11/2026
- Gardés : C01 sx_split_compare, C02 sx_faceoff, C03 sx_side, C04 sx_stacked_cols, C05 sx_round_timeline, C08 sx_butterfly, C09 sx_league. Nouveau : sx_stat_strip (bandeau de chiffres).
- Refusés : C06, C07, C10 (ne plus proposer).
- Exemple In Vivo CAR-T : decks/in-vivo-car-t/extras.yaml (14 slides).
