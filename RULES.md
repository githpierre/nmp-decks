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

### Créativité dans les ateliers (Pierre, 11 Nov 2026)
- Quand Pierre demande d'être créatif, il faut CHANGER LA MISE EN PAGE, pas un détail : ne pas garder la structure existante (ex. flèche + 3 bulles)
  en ne variant que la couleur ou une barre. Chaque variante = une autre façon de représenter l'information (règle graduée, tableau,
  menu, pyramide, compteur, plans SaaS, quadrillage…). Mieux vaut une idée osée qu'une 30e retouche du même dessin.
- Pages de revue, 2e tour et suivants : ne remontrer QUE ce que Pierre doit revoir (ce qu'il a refusé ou ce qui a changé) ; ce qu'il a validé est appliqué et disparaît de la page (11 Nov).
- Quand il demande N variations, en montrer vraiment N, toutes différentes, auditées visuellement (texte complet, rien qui dépasse).
- 11 Nov : les 30 refontes (arbre « Qui paie », intercalaires, « Maximum customer value ») toutes refusées : Pierre garde ses mises en page d'origine. Sur un format qu'il a dessiné, proposer des corrections ciblées (alignement, lisibilité) plutôt qu'une refonte, sauf s'il la demande.
- Choix retenu : prix (slide 13) = quadrillage de fond (gammes posées sur une grille prix, items5 ZB).

### Audit visuel (11 Nov 2026, tools/atelier2/fixlib.js + fixes.py, appliqué à tous les decks)
- Chiffres : « $192B », « ≈5% » (pas d'espace), « ASIA-PACIFIC » ; un lien souligné ne l'est pas sur l'espace final.
- NE PLUS PROPOSER (Pierre a déjà dit non) : en-têtes de colonnes des slides modèles (FIRM / MARKET SIZE / COMMENTS, PAIN POINT / PRIORITY) restent dans la couleur des traits ; emoji 🤬 grisé des slides « maximum customer value » ; tête de la slide 152 qui passe derrière le pied de page (voulu) ; espace au bout des connecteurs ; refontes des formats qu'il a dessinés.
- Connecteurs : on garde le petit espace entre le bout d'un trait et sa cible (Pierre trouve ça joli) ; la ligne d'un arbre peut dépasser ses branches.
- Une flèche refaite relie exactement les deux éléments que reliait l'original (vérifier chaque liaison une par une, 11 Nov : erreur sur la slide 154).
- Un segment porte le même nom partout (intercalaire, sous-titres, tableaux, cartes) ; même règle pour les chiffres : la typographie s'applique aux slides modèles ET converties.
- Une flèche ne coupe jamais une bulle : elle part d'un bord et arrive au milieu d'un bord, pointe rose identique partout.
- Noms de catégories en titre de carte : toujours sur 2 lignes ; un nom d'un seul mot en reçoit un second (CREDENTIALING → DIGITAL CREDENTIALING).
- Une étiquette posée sur une ligne de grille est centrée sur cette ligne (la ligne s'interrompt derrière elle).
- Texte d'une carte centré verticalement ; pastille + texte centrés ensemble, 8 px d'écart.
- Cartes d'une même rangée alignées au pixel ; en-têtes de colonnes jamais dans la couleur des traits (#334D54).
- Même type de slide = même rendu sur toutes ses pages (ex. frises datées 1/2 et 2/2, matrices de priorité).
- Logos : posés dans une tuile blanche avec une vraie marge blanche (logo = 66 % de la tuile, coins arrondis), tuile avec un fin contour clair.

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

## The 12 product-page slides live in the decks too (Pierre, 11 Nov 2026)
- The 12 illustrative slides of the product pages (S01 to S12 and their second formats) are built in HTML/CSS here, with the same
  look as the slides already live on the first 100 product pages. No new PowerPoint builder.
- Every deck CREATION or UPDATE must include these slides for its market (same data, same title, same alt), in the matching chapter.
  If a slide is missing for that market, build it with the HTML templates before delivering the deck.
- Slide types: radar (S01), frise (S01-02), trends and curve (S02), cagr and donut (S03), pains (S04), techtable (S05), valuemap (S06),
  risks (S07), drivers (S08), invbets and topraises (S09), grid (S10), killers and survivors (S11), winner (S12).

## Product-page slides (pp_*): Pierre's review of 11 Nov 2026 (checked by tools/pp/audit_pp.py, run after every build)
- Air under the title: no content closer than 30 px to the title (20 px to the pill). TITLE_GAP / PILL_GAP.
- Nothing overlaps or touches: text boxes and logo tiles at least 4 px apart (value above a logo, pink marker before a year...). TOO_CLOSE.
- Logos: never a tile with initials when a slide shows logos; fetch the whole chain, then ask Pierre (name + domain) in one list. LOGO_MISSING.
- S04 pain points: always 6 pains; audience headers always on exactly 2 lines (2 or 3 words); no Mild/Strong/Strongest legend; block centered vertically.
- S06 value map: logo tiles 34 px; a group label may run a little past its card, never much (2 lines instead).
- S07 risks: every event on exactly 3 lines (write 110-125 characters).
- S08 growth drivers: always 30 events, 2 columns of 15; the 3 biggest events highlighted (impact >= 2.5), like the live slides.
- S11 killers and survivors: at least 5 rows.
- S12 winner: 6 or 7 criteria, 5 or 6 companies.
- S10 grid: positions mean something (biggest raiser on the left inside its stage), never random.
- Visual audit by Claude of every slide before sending, on top of the script.

## Checklist d'audit visuel d'un deck (process, 11 Nov 2026 — à passer sur CHAQUE deck, tous marchés)
Appliquée automatiquement par tools/atelier2/fixlib.js (règles générales), build.py (typographie) et tools/atelier2/fixes.py (correctifs par type). Avant de livrer un deck, repasser cette liste slide par slide.

Typographie (build.py, toutes les slides, modèles ET converties)
1. Montants collés : « $192B », « $1.3M », jamais « $ 192 B ».
2. Pourcentages collés : « 5% », « ≈35% » (le ≈ colle aussi au chiffre).
3. Régions avec trait d'union sans espaces : « ASIA-PACIFIC ».
4. Lien souligné : jamais souligné sur l'espace final.
5. Notes de bas de slide : deux phrases jamais collées sans point (« …phases. These… »).
6. Un segment porte le même nom partout (ex. DIGITAL CREDENTIALING : intercalaire, sous-titres, tableaux, cartes).

Mise en page
7. Même type de slide = même modèle partout (matrices de priorité, frises datées 1/2 et 2/2, lignes « regular vs startup » 210-214…). Une slide convertie qui a un modèle passe sur le modèle (le convertisseur détecte les matrices +/++/+++).
8. Cartes : arrondies, trait gris-bleu #334D54 ; pas de cadres carrés à bord clair.
9. Texte d'une carte centré verticalement ; avec une pastille en bas de carte : 4 lignes max, centré dans l'espace au-dessus de la pastille.
10. Pastille d'icône d'une carte : ronde, icône au trait, centrée sur le bord BAS (le haut porte le titre) ; jamais un emoji à cheval sur un coin.
11. Pastille numérotée + texte centrés ensemble, 8 px d'écart.
12a. Titre d'une ligne posé au-dessus de sa carte : calé en bas de sa boîte, 8 px au-dessus de la carte (pas flottant au milieu).
12. Titres de catégories dans les cartes : toujours sur 2 lignes (un nom d'un mot en reçoit un second).
13. Cartes d'une même rangée alignées au pixel ; titres alignés sur leur carte.
14. Étiquettes le long d'une barre rose verticale : ~7 px de la barre, et les textes de droite gardent leur écart (on les décale d'autant).
15. Étiquette posée sur une ligne de grille : centrée sur la ligne, fond navy pour couper la ligne ; étiquette posée sur des points/barres : fond navy (pastille).
16. Un texte ne déborde jamais de sa boîte et n'est jamais écrit à la verticale (« 33% ») ; « nom + valeur » : nom sur une ligne, valeur sur la suivante.
17. Taille de texte homogène entre éléments frères (une bulle à 6 pt au milieu de bulles à 11 pt = défaut).
18. Axes de graphique : années sous l'axe, jamais au-dessus des courbes.
19. Points d'un graphique / radar qui représentent des sociétés : reliés à leur étiquette.
20. Flèches : une flèche refaite relie exactement les deux éléments de l'original ; elle part d'un bord, arrive au milieu d'un bord, pointe rose identique, ne coupe jamais une bulle.
21. Logos : tuile blanche, logo à 66 % (marge blanche), coins arrondis, fin contour clair.
24. Le surtitre de chapitre d'une slide n'est jamais le nom du marché (« EDTECH MARKET ») : la slide garde son chapitre. Fréquent : contrôlé automatiquement par tools/visual_audit.py (KICKER_IS_MARKET) à chaque audit final, et corrigé par le convertisseur.
22. Rose : interdit en TEXTE fin et en petites icônes / petits signes fins sur navy (mettre en gras ou en aplat). Un cadre rose de 2 px autour d'une carte (TODAY, classement) est OK, ne pas l'épaissir.

À NE PAS toucher (Pierre a tranché, ne plus proposer)
- Espace au bout des connecteurs, ligne d'arbre qui dépasse ses branches.
- En-têtes de colonnes des slides modèles dans la couleur des traits.
- Emoji 🤬 grisé des slides « maximum customer value ».
- Épaissir les cadres roses de 2 px (TODAY des frises, classement de la slide 89).
- Tête de la slide 152 derrière le pied de page.
- ✕ roses posés sur le rebord des cases (slide 23) ; flèche ↔ au-dessus des barres (slide 164) : ils structurent.
- Refontes des formats qu'il a dessinés (arbre « Qui paie », intercalaires, expérience client).

- Slide « bold bets » : modèle deux colonnes « Next 5 years / 5 to 10 years », icône à gauche de chaque pari (choix 11 Nov).
- Slides de contraste « How X turned… » : logo centré entre les deux blocs, sans flèche (choix 11 Nov, CSS du modèle).

Séries (1/2, 2/3…)
25. Les pages d'une même série (même titre) ont EXACTEMENT le même design et les mêmes décisions (icônes, pastilles, rails…). Automatique : make_decisions.py recopie toute décision d'une page aux autres pages de la série ; l'audit final compare les pages d'une série côte à côte. (Raté le 11/11 : 208 avait gardé ses emojis alors que 207 avait les icônes, parce que la décision avait été listée par numéro de slide et pas par série.)

Process de revue
- Chaque erreur trouvée = une règle écrite ici + appliquée par script à tous les decks, pas une retouche ponctuelle.
- Pages de revue : 2e tour et suivants, ne montrer que ce que Pierre doit revoir ; le validé disparaît.
- S02: a strong public series (company volume, official statistics) reaching the current year beats Google Trends. Otherwise Google Trends,
  CSV asked to Pierre. Window: 5 years by default, 12 months only when the last year alone rises x3 or more and beats the 5-year ratio
  (tools/pp/pp_prepare.py trends_window). The curve never touches the text above it (CURVE_HITS_TEXT).
- S02 (11 Nov): raw Google Trends are distorted since August 2025 (every low-volume term jumps x5 to x10, then drops in Oct 2026). Never read a raw rise as a signal: correct with the cross-term control index (/root/w/m131/gt/corr.py) and look for public series first (prompt s02-signals). Trends only when nothing passes, and only if the corrected curve rises.
- S02 curve: x-axis labels never overlap (audit XLABEL_OVERLAP). When two dates are too close, drop the intermediate point rather than shrink the labels.
- S02 formats (Pierre, 11 Nov): 1) public curve, 2) leader results card (growth in light blue #7FA9C9, company line at the bottom), 3) milestones staircase (80% width), 4) share bars, 5) rules staircase (mandates), 6) demand vs supply bars only when nothing else, 7) Google Trends last. Rejected: before/now big numbers, pictograms, customer wall, funding from our base (overlaps S09), valuation step-up.
- Every slide has the dotted foot line under the note (base template, audit FOOT_LINE). The 100 live radars S01 of markets 1-100 (PPTX era) miss it.
- Product-page notes follow the notes workshop on EVERY slide (Pierre, 11 Nov, after finding pp notes written as a paragraph with dots): a YAML list of 2 lines, one idea per line, no dot inside or at the end, line 1 starts with We, line 2 ends with the sources clause, widths within 12%. Cause: the pp builders glued note + SRC as one paragraph, and build.py added a dot between list lines. Fixed in mkpp (balance_note picks the wording that balances), build.py (no dot between .nl lines) and audit_pp (NOTE_FORMAT). The radar keeps its 2-line caption (Pierre).
- S03 donut: layout B (labels beside their slice, no line). Every category shows at least 2 logos (1 only if no company in it raised money).
  A missing logo is never dropped silently: mkpp2 prints MISSING LOGOS, the audit flags DONUT_LOGOS.
- Titles rotate between families market by market (tools/pp/titles.py) for S05, S09-02, S10; never cut the market name.
- Tables (killers, survivors, winner, pains, tech) centered vertically between title and note; separator lines reach the last column.
- Ticks and crosses are drawn with lines (SVG), never a font glyph, centered in their circle or square.
- S12 score bars: 90% of the column width.
- Prototypes and new slides work only on markets 131-225 (101-130 are done).


## Slides complémentaires (data points) : comment les penser (Pierre, 11-12 Nov 2026)
Nom : « slides complémentaires » (extra slides). Ne plus dire « slides signal » (Pierre, 12 Nov : le mot est ambigu). Catalogue : SIGNALS.md (nom de fichier historique).
Exemples : « 22 US states banned phones in schools in 2025 alone », « Singapore teachers use AI tools 5x more often than French ones », « Only 3% of people who start a free online course finish it », « Byju's IPO was always within the next year », « Coursera still loses 10.2¢ per $1 », « Online course star Coursera lost 91% of its value », « Tutoring firm Nerdy has lost 79% », « Since ChatGPT launched, Chegg lost almost all its value », « One university pays almost 90% of Grand Canyon Education's revenue ».
- Ce ne sont PAS des emplacements fixes (« après And more recently, il faut une slide à barres »). Ce sont des TEMPLATES qui montrent un signal, positif ou négatif.
- Process : 1) un prompt de recherche bien construit ramène beaucoup de signaux récents et variés sur l'état du marché (adoption, régulation, chute d'un acteur, concentration, comparaison entre pays, unit economics…) ; 2) on fait une slide par signal fort, avec le template qui va le mieux à la forme de la donnée (barres, courbe de cours, nuage, waffle, chiffre géant…) ; 3) on place chaque slide dans le chapitre où elle sert le propos, n'importe où dans le deck.
- Le nombre et l'emplacement de ces slides varient d'un marché à l'autre ; ne jamais copier la position EdTech.

## Google Trends slides (pp_trends), Pierre 12 Nov 2026
- Google's counts jumped for almost every term in late July / August 2025: every curve is corrected after the week of 2025-07-27 (`tools/pp/pp_prepare.py`, `_trend_rows`). With the control terms of the slide kit in `tools/pp/trends_ctrl/*.csv`, each week is divided by their median jump; without them, by `aug25` (default 2.0). The note (2 lines) says the curve was corrected for a jump in Google's counts in August 2025.
- The curve always stops at its last peak: the fall at the end (weeks Google has not finished counting) is never shown. The goal is to show a rising trend.
- CSVs live with the deck (`decks/<slug>/media/trends/<term>.csv`), worldwide, 5 years, weekly. The term shown is the one in the CSV header.
- Precision is not the goal (Pierre, 12 Nov 2026): the slide shows the movement of the real curve. The August 2025 correction is a fixed /2 (no control terms needed), and a light 3-week median smooths one-week spikes and dips.

## Grids and timelines (Pierre, 12 Nov 2026)
- Labels of one grid (short upper-case headers, company names): all on one line or all on two lines, never mixed. If every label has 2+ words, all go on 2 lines; otherwise the group shrinks (down to 80%) until all fit on one line (`rawfit.js`). Checked by LABEL_LINES_MIXED (build).
- Card grids with an icon on top ("Which drivers compound…", "What slows adoption…"): every card text on exactly 4 lines, so the icons line up. Set with data-lines="4" in the template; a text that does not fit shrinks slightly (down to 85%). Checked by LINES_OVER.
- Timelines of rounds or deals ("Which rounds were announced last?", pharma deals): every entry on 2 lines, of about the same length (data-lines="2").
- "Who are the current market leaders?": the star sits on the top-left corner of its card.
- The product-page tech table ("Which players can already do the most today?") is centered on the page whatever the number of columns.
- "And over the years?" follows the template of the slide before it (pp_raises, with logos), with a 2-line title.

## Research prompts for a new market deck (12 Nov 2026)
- `tools/make_research_prompts.py` writes one TXT per chapter + one signals TXT, zipped, no README. Each slide shows its EdTech model as YAML (same keys, target lengths ±15%) and the other LLM answers the same YAML with sources (claim, url, date, quote), or `status: no_data` instead of inventing.
- Slides built from our startups database (funding, investors, grids by stage) are never asked to the other LLM.
- File names: <uuid>-<handle>-deck-<NN>-<chapter>-results-research-<date>.md.

## Category splits, market size, logos, extra slides (Pierre, 12 Nov 2026)
- Donut / split by category: exact figures never exist. The split is OUR best estimate, and the note bottom left says so plainly (e.g. "We estimate the split from deal counts and pipelines; no public source splits this market by category."). Never leave a 0% slice: merge it or drop it.
- Market size: our estimate is fine when the note says it is ours and how it is built. The forecast-gap slide (growth-rate estimates by source) shows the spread between published forecasts.
- Slides whose research came back without data (status no_data) are removed from the deck (`import_research.py --drop-no-data`). Never invent to fill them. If a chapter ends up nearly empty, tell Pierre.
- When asking Pierre for logos: always list each company with its domain (e.g. "Capstan Therapeutics — capstantx.com"). Homonyms are common.
- Extra slides (slides complémentaires): never place them directly in a deck. Step 1: show the candidates to Pierre on a review page (design + data), he validates or retouches the design (the designs are still temporary). Step 2: for each validated slide, propose its exact place, "between slide N (title) and slide N+1 (title)", and Pierre approves or moves it. Only then integrate.

## Research import: what the 12 Nov in vivo audit taught (generic fixes)
- The prompts list the keys of a converted slide in reading order (top to bottom, left to right, `key_pos` in make_research_prompts.py). Listed by key number, the other LLM paired a label with the card of another row (categorize slides 1/3 to 3/3, products quadrant, bottom-up steps out of order).
- Company and product names are never cut to fit a length target (CAPSTAN, not "CAPSTAN TX"; KELONIA, not "KELONI").
- The segment label under the title (pain and value blocks) is always the segment name given to the import (`--pain` / `--value`), the same as on the chapter divider.
- A card whose texts are all empty is hidden and the cards left are centered vertically (fixlib.js `emptyCards`).
- Market sizes under $1B are written in millions on the CAGR bars ($285M, not $285B).
- A literal "\n" written by the other LLM is a line break in every field, not only in slide texts.
- Emoji icons of converted slides are chosen for the market (no graduation caps in a biotech deck).

## Startup killers chapter and database slides (Pierre, 12 Nov 2026)
- The Startup killers chapter always keeps "Which startups stumbled lately?" (1/2 and 2/2), the warning-signs grid and "Why do startups fail?": at least 4 slides. A chapter with one slide is an anomaly. Setbacks count, not only failures (layoffs, lost partners, dropped programs, delayed readouts).
- Investor bets slides are built from our startups database (nmp-seo data/startups), never asked to the other LLM: `decks/<slug>/db.yaml`, applied by import_research.py before the edits. Equity rounds only (no IPO, debt, grants); rounds with no public amount count as zero, and the note says so.
- Converted bar charts with fixed bar heights get `vbars: [values]` (fixlib.js `vbars`): bars and their value labels follow the data. A year chart whose bars cannot follow the data uses the `fundbars` template (`unit: pct` for shares).
