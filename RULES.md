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

## Two kinds of review pages (Claude decides which one fits)
- ATELIER DU JUGE = a judgment call that will come back on every deck (how many lines for a footnote, when to add a caption...).
  6 real cases, the same variants A/B/C on every case, ONE thing changes between them (say which in the yellow band).
  Pick cases where Claude truly hesitates, so the right answer can change from case to case; say per case what Claude takes and why.
  Never propose the same obvious winner six times: that is not a workshop.
- CHOIX DE DESIGN = a design decided once (a template's look). No cases: many real variants (6-9, all different and polished),
  one per row, large; when the detail is small (dots, lines, notes) show a x2 zoom; show it on 2 markets if text length can break it.
- Both: one scrolling HTML page (artifact), yellow band = what changes + Claude's pick and why, variants named by letters,
  Oui / Non on each, Claude's pick framed in green, "Copier mes réponses". Visual audit of every image before sending (wraps, overlaps, keys).
- Tooling: write `tools/make_atelierN.py` (deck + manifest.json with the texts; see git history for workshop 5), `build.py atelierN`,
  `tools/atelier/shoot.py <deck dir> <img dir>` (x2 renders + zooms), `tools/atelier/make_page.py <deck dir> <page dir>`.
- Pierre's answers become the default (template / CSS) + a rule here + a history line; unused variants are removed once settled.

## Pierre's rules (10 Nov 2026, workshop 3)
- Cover disclaimer: right UNDER the title block (it follows the title, 26 px under "NEW MARKET PITCH", 330 px wide), on every cover.
  This replaces A3 (bottom, aligned with the button). `disc_pos: bottom` keeps the old placement if ever needed.
- Footnotes as a list (one line per idea): lines within 12% of each other in rendered width (audit NOTE_BALANCE);
  a note never runs into the footer label (audit NOTE_WIDTH). 2 lines is the usual case; 3 lines when the content needs it.
- Dated lists: always exactly 6 dates per page (build refuses otherwise); page 1 and page 2 use the same template.
  Circles are centred on the rail axis and on the date line; the rail runs from the first circle to the last.

## Pierre's rules (10 Nov 2026, workshop 5)
- Footnotes: 2 lines by default (it reads as a clearer explanation). 1 line when one idea fits on it (e.g. the map).
  3 lines only for 3 really important things, and then 3 long lines. Lines within 12% (NOTE_BALANCE).
- Never date a source with a past year that will look old ("latest 2025 estimates"): write "the latest estimates",
  or find a more recent figure (audit NOTE_YEAR).
- Dated list: hollow pink circles "classique" (k1: rail 8 px, circles 14 px centred on the rail axis), rail from first to last circle.
- "What is the X market, in simple terms?": keep Pierre's design (framed sentence with two icons). All 12 alternatives rejected.
- Colours, for every new design: never pink text on the navy background; always a colour hierarchy (not every piece of text in white);
  never mix white and sand/yellow inside one text; respect the side margins (no block as wide as 840 px; stay within the usual width).
- Map lines, start (workshop 6, M1, 6/6): always from the MIDDLE of the text edge facing the dot (under the last line, above the title,
  or the side of the middle line). Default `line_start: middle`.
- Map lines, arrival (M2): at a right angle to the start, so the line makes a real elbow (leaves down/up -> arrives on the dot's side;
  leaves from the side -> arrives from below/above). Default `line_end: auto`.
- Map lines, bend (M3, 6/6): rounded elbow everywhere (`line_bend: 0.67`).
- Map lines: rounded elbows ("coudes arrondis"). They start almost touching the text (4 px, within the text's width) and end
  on the dot's axis, 3 px from its edge (horizontal arrival when the line comes from above or below, vertical when it comes from the side).

## Pierre's rules (10 Nov 2026, evening)
- Titles on 2 lines: the build measures every possible cut and keeps the one where both lines have the closest width
  (script in base.html.j2; the manual \n in deck.yaml is only a hint). A market or company name is never cut
  (deck.market + `keep_together` list become non-breaking). Audit TITLE_BALANCE. Example: "How Multiverse turned training / into a unicorn"
  = 593 vs 267 px (55 %) -> "How Multiverse turned / training into a unicorn" = 429 vs 431 px (0 %).
- Cover button NEWMARKETPITCH.COM (workshop 7, B): navy background (85 %) only when the photo under it is busy or bright
  (p90 luminance > 90, detected by prepare_cover); otherwise unchanged. Default `btn: b`.
- World map region texts: exactly 3 lines each (audit MAP_TEXT_LINES). Write them long enough; a box widens around its
  centre (up to +110 px, inside the margins) when 3 lines are not enough.
- Footer market label: always one line, never on the button (letter spacing tightens for long names; audit FOOT_LABEL).
- KPI arrows point down automatically when the value is negative. A page marker "1/1" is never shown.
- Funding-bar arrows: one symmetric SVG (shaft + head on the same axis), centred on the bar.

## Text boxes (Pierre's oral review of the full EdTech deck, slides 8-32, 10 Nov 2026)
Rules deduced from his remarks, checked by code (templates/rawfit.js at build time, tools/audit_groups.py after):
- Parallel boxes = same width, same font size and colour, on one row or one column. They always have the SAME number
  of lines (slide 8: 5 lines each; slide 10: 6; slide 22: 5; slides 29-30: 10; slide 31-32: 3). The build forces the
  group's largest count; `lines: N` in overrides.yaml sets another target. A one-line label is never stretched.
- Every multi-line text is balanced: the build picks the line breaks that make the lines as equal as possible
  (dynamic programming on measured word widths), last line included. Never "..., and / degrees online".
  A number stays with its unit ("$1 billion", "24 hours" never split).
- Bubbles are well filled: the longest line uses about 80-95 % of the inner width. When a text is short, ADD 2-3 words
  (same facts, no new figure) rather than leave 25-30 % of the bubble empty (slides 15, 16, 18-20, 23). Answers in one
  row/column have about the same word count (reference: the longest well-filled one).
- Text never touches its bubble: at least 10 px inside padding (14 px on narrow columns, slide 10).
- Small elements beside text: badges sit on the bubble's top edge, never close to the text (slide 32);
  decorative crosses/icons are not oversized (slide 23: 80 %).
- Content block is vertically centred between the title (or subtitle) and the note.
- How: rewrites go in decks/<slug>/overrides.yaml (`text`, `join`, `lines`, `pad`, `dy`, `scale`), candidates are measured
  first with `tools/try_texts.py` (it reports lines, balance and fill for each candidate; keep the best).
  Audit thresholds: same line count in a group; balance <= 12 % (2 lines) / 25 % (3-4 lines); fill >= 70 %.

## Atelier « 100 améliorations » (10 Nov 2026)
- Pierre veut un atelier où chaque point moche du deck est montré : l'actuel + 3 variantes dont Claude est convaincu qu'elles sont
  toutes plus jolies (pas de variante au hasard), Oui/Non par variante, choix de Claude encadré en vert, bandeau jaune.
- Quand un format se répète (sommaire, intercalaires, matrices de priorité…), la variante s'applique à toutes les slides qui le
  partagent ; la page le dit sous chaque titre.
- Outil : tools/atelier2/ (items.py = les points et leurs variantes en CSS/JS injectés sur le vrai deck ; lib.js = helpers ;
  icons.json = emojis -> icônes Lucide / Phosphor ; shoot.py = captures ; make_page.py = page).
- Bug corrigé au passage : les libellés espacés à la main (« W H Y    I T ») deviennent un texte normal + letter-spacing,
  sinon le navigateur colle les mots (« WHYITMATTERS »).

### Retours de Pierre sur l'atelier 100 (10 Nov 2026, 23h)
- Jamais de texte ou de trait rose FIN sur le bleu marine (flèche fine rose, libellé rose fin, « WHY IT MATTERS » en rose) : c'est moche.
  Le rose se met en aplat (pastille pleine, barre, étiquette) ou en gras épais.
- Les emojis colorés ne sont pas à remplacer par réflexe : sur beaucoup de grilles de cartes ils restent (plus colorés que des icônes au trait).
  Quand on met une icône dans une pastille, le contenu de la carte (pastille + texte) se recentre verticalement ensemble ;
  une pastille d'angle se pose pile à cheval sur le coin de la carte.
- Slide 22 (« ce qui est rare ») : 4 lignes par carte, pas 5.
- Une décision vaut pour tous les decks, même si le PowerPoint d'origine est différent : on l'applique au gabarit / au convertisseur,
  pas à une slide.
- Atelier : chaque variante est un vrai design différent (pas un seul paramètre qui change), auditée visuellement avant envoi
  (rien qui chevauche, rien qui dépasse, bien centré) ; ne jamais représenter le même changement deux fois pour un même type de slide.

## Workflow
1. Research: Claude writes ONE prompt file (.md) per research block; Pierre drops it in another LLM and says "go";
   that LLM does the research AND returns the final JSON/CSV in the same answer (never research first, then a second "go").
2. Claude turns the returned files into deck.yaml (content only), runs `build.py`, checks the PNGs, delivers the PDF.
3. Update of an existing deck: edit deck.yaml only, rebuild.
4. Every correction from Pierre becomes a line here (or a template/CSS change), never a one-off fix in a single deck.

## History
- 2026-11-10: oral review of slides 8-32 of the full EdTech deck -> "Text boxes" rules, rawfit.js (equal line counts +
  balanced breaks), 200+ rewrites in overrides.yaml (slides 8-32 by hand, 33-220 chosen with try_texts.py).
- 2026-11-10: workshop 6 settled (map lines: start middle of the edge, right-angle arrival, rounded elbow).
- 2026-11-10: workshop 5 answers applied (notes, no ageing years, k1 timeline, definition kept, colour rules, elbow map lines landing on dots); EdTech notes rewritten.
- 2026-11-10: workshop 5 (B judge: 1/2/3-line notes; C/D/E design choices: 6 dated-list finishes, 9 definition designs, 6 map line shapes).
- 2026-11-10: workshop 4 = B-E redone (one change only, variants A/B/C, compact page); A settled: disclaimer under the title.
- 2026-11-10: workshop 3 (A-E, 6 cases x 3 variants each, HTML page with Oui/Non) sent to Pierre. Cover title width now computed from the photo
  (title_maxw = free dark width of the title band; the pink line shrinks with the title); disclaimer variants `disc_style` / `disc_pos: under`.
- 2026-11-10: second review (rules above) + workshops A (6 covers), B (6 notes x 3), C (7 timelines), D (4 definitions), E (3 map curves).
- 2026-11-10: first review by Pierre (rules above) + workshop A (cover disclaimer), B (two-line notes), C (timeline style).
- 2026-11-10: prototype on EdTech (16 slide types rebuilt from the Q3 2026 PowerPoint deck).
