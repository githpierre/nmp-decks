# Slide library (type -> fields in deck.yaml)

| type | used for | fields |
|---|---|---|
| cover | cover | image, big ("EdTech\nmarket"), disclaimer |
| agenda | chapter menu / section dividers | current (0 = full menu, 1-12 = highlight a chapter) |
| definition | one-sentence definition in a framed box | text, icon_tl, icon_br |
| cards | emoji + short sentence grid | items [{e, t}], cols, w, h |
| maturity | maturity score on an axis | score (0-100), text |
| dated | dated list on a vertical rail (news, changes, rounds) | items [{d, t}], page |
| kpis | signal with 3 key numbers | pill, items [{label, value, down}], why |
| estimates | market size estimates table | rows [{firm, value, comment}] |
| compare | horizontal bars vs other markets | rows [{name, v, hl}] (v in $B) |
| catbars | revenue categories (vertical, % of total) | cats [{name, v}] (v in $B) |
| worldmap | regional split | regions {na, eu, apac, mea, latam: {pct, text}} |
| projection | yearly projection bars | intro, bars [{x, v}], cagr |
| priority | pain priority table | subtitle, icons, rows [{pain, s: [1-3...], p}] |
| fundbars | funding by quarter/year with annotations | bars [{x, v, ann}] (v in $M) |
| logogrid | top companies 3 x 3 grid | cols, rows [{name, cells: [[logo x3] x3]}] |
| contrast | "how X won" vs fictional baseline | left, right, logo, rows [[baseline, winner]] |

Common fields on every slide: section, title ("line 1\nline 2"), subtitle or page, pill, note (footnote; `[label](url)` links, `**bold**`).
