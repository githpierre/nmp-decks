# Rules for HTML decks (validated with Pierre)

The rules of the PowerPoint kit (cahier des charges v6.18) still apply to the CONTENT: US English, no em dashes, clarity first,
one sentence = no final dot, 2+ sentences = dots, footnotes max 3 lines starting with "We", sourced dated facts, pure players,
Big Tech never as startups, market size / categories / CAGR consistency, etc. Below: what changes with HTML.

## Format
- PDF only, 10 x 7 in (960 x 672 px canvas), Lexend + Montserrat, dark navy theme. White theme later = CSS variables.
- File name: `{Market} - Q# YYYY - newmarketpitch.com ©.pdf`.

## Layout (handled by code, never by hand)
- Line breaks are balanced by the browser (`text-wrap: balance`): no orphan word, no manual re-breaking.
- Charts are computed from numbers in deck.yaml (bar heights, dot sizes, % of categories). Never type a pixel size in deck.yaml.
- Titles: 2 lines, explicit `\n` in the YAML. The build flags TITLE_LINES, NOTE_LINES (> 3), OVERFLOW, OUTSIDE, HITS_NOTE, HITS_TITLE.
- YAML: always quote a text that contains a comma inside `{...}` (the build refuses a cut sentence).

## Pierre's rules (10 Nov 2026, first review of the EdTech prototype)
- Cover: "© NEW MARKET PITCH" without the year. The disclaimer is left-aligned with the title (x = 52), narrower and taller,
  its bottom aligned with the NEWMARKETPITCH.COM button, and it never runs over a light part of the photo (check on each cover).
- Footer button shadow: half the normal shadow (`--shadow-soft`).
- Footnotes: never glued to the dotted footer line (bottom 40 px, about twice the old gap). Lines balanced, no orphan word.
  Two sentences of similar length go on two lines (`note:` as a YAML list), rewritten to the same length, with NO final dots;
  dots only when the note is one running paragraph of several sentences.
- Map leader lines (dotted): start just under the end of the region text (or just above its title when the dot is above),
  always slightly inclined and curved, never a straight vertical, and stop at the dot. Drawn by the template after layout.
- Small arrows that only decorate a chart (funding annotations) are muted (#789096), never sand/yellow: they are not important.
- Top companies grid: logos are scattered in their cell (position inside the cell means something, never a robotic pattern);
  a company between two stages sits ON the border (`name>` / `<name` in deck.yaml), `namev` between two rows.
- Logo next to a winner's contrast rows: same white rounded tile as the top companies grid.

## Pierre's rules (10 Nov 2026, second review)
- Cover disclaimer: A3 chosen (6.5 pt, narrow block, left-aligned with the title, bottom aligned with the button). Width is picked
  automatically (300 -> 200 px) so the block stays on a dark part of the photo.
- Cover title: every line on one line; the font shrinks only when the longest line would run into the photo (title_maxw, default 520 px).
  "NEW MARKET PITCH" follows right under the title, never at a fixed height.
- Two-sentence footnotes on two lines: lengths close, not to the character; never too short.
- Chapter menu (agenda): vertically centered on the whole slide.
- Dated lists (what has changed): wider block (~620 px of text), centered, every item on exactly 2 balanced lines (audit DATED_LINES);
  rewrite items to ~180-195 characters to fill the width. No star on the rail (style chosen in the timeline workshop).
- Estimates table: no header rule above the arrow column.
- Map leader lines: dot under the text -> start under the end of the last line; dot above -> start above the title;
  dot beside -> start at the side of the middle line (Latin America: right of "AI tools to"). Always curved and inclined.
- Projection: the last value is bigger, an elbow arrow goes from the intro text to it; the dotted axis ends with an arrowhead.
- Priority tables: fixed geometry (same left/right start on every slide of the series), half the old gap between pain and scores.
- Decorative arrows on funding charts: muted color, centered on their bar (audit ARROW_OFFCENTER).
- Top companies grid: positions are meaningful, never random. x = stage (0-3) authored from funding, revenue and reach
  (1.0 / 2.0 = between two stages, on the line); y lanes computed so logos never overlap. One SVG for all grid lines
  (same dash, same color, same ends). Soft shadows on logo tiles.
- Winner contrast rows: each sentence fills 70-90% of its box (audit FILL); soft shadows.
- Visual audit of every slide by Claude before anything is sent to Pierre.

## Judge workshops (atelier du juge) — how Claude runs them
- Any design doubt goes to a workshop before it becomes a default. One workshop = one question (e.g. where the cover disclaimer goes).
- 6 cases x 3 variants: 6 different real-looking cases (new photo / market / content each time), the same 3 variants on each case,
  built with the real templates and CSS (never a mockup). Claude's pick is the same variant on every case unless a case truly differs.
- Delivered as ONE scrolling HTML page (artifact): yellow band per workshop = what changes + Claude's pick and why;
  each variant shown in place with Oui / Non buttons; Claude's pick framed in green with "Mon choix"; click to enlarge;
  a x2 zoom under the slide when the detail is small (notes, timeline dots). "Copier mes réponses" gives Pierre a text to paste back.
- Tooling: `tools/make_atelier4.py` (cases -> decks/atelierN/deck.yaml + manifest.json with the workshop texts), `build.py atelierN`,
  `tools/atelier/shoot.py <deck dir> <img dir>` (x2 renders + zooms), `tools/atelier/make_page.py <deck dir> <page dir>`.
- Pierre's answers become the default (template / CSS) + a rule here + a history line; unused variants are removed once settled.

## Pierre's rules (10 Nov 2026, workshop 3)
- Cover disclaimer: right UNDER the title block (it follows the title, 26 px under "NEW MARKET PITCH", 330 px wide), on every cover.
  This replaces A3 (bottom, aligned with the button). `disc_pos: bottom` keeps the old placement if ever needed.
- Judge workshops: only ONE thing changes between the 3 variants (say which in the yellow band); variants are named A / B / C
  and are the same on all 6 cases; the page must be easy to scan (Pierre's UX matters as much as the slides).

## Workflow
1. Research: Claude writes ONE prompt file (.md) per research block; Pierre drops it in another LLM and says "go";
   that LLM does the research AND returns the final JSON/CSV in the same answer (never research first, then a second "go").
2. Claude turns the returned files into deck.yaml (content only), runs `build.py`, checks the PNGs, delivers the PDF.
3. Update of an existing deck: edit deck.yaml only, rebuild.
4. Every correction from Pierre becomes a line here (or a template/CSS change), never a one-off fix in a single deck.

## History
- 2026-11-10: workshop 4 = B-E redone (one change only, variants A/B/C, compact page); A settled: disclaimer under the title.
- 2026-11-10: workshop 3 (A-E, 6 cases x 3 variants each, HTML page with Oui/Non) sent to Pierre. Cover title width now computed from the photo
  (title_maxw = free dark width of the title band; the pink line shrinks with the title); disclaimer variants `disc_style` / `disc_pos: under`.
- 2026-11-10: second review (rules above) + workshops A (6 covers), B (6 notes x 3), C (7 timelines), D (4 definitions), E (3 map curves).
- 2026-11-10: first review by Pierre (rules above) + workshop A (cover disclaimer), B (two-line notes), C (timeline style).
- 2026-11-10: prototype on EdTech (16 slide types rebuilt from the Q3 2026 PowerPoint deck).
