# Method v2 for market decks (Pierre's go-ahead, 14 Nov 2026)

Why the first three decks were slow: research texts were not delivered in their final format, so Claude rewrote them one by one
(about 400 lines of edits.yaml for Healthcare AI); several converted templates kept the drawing of the original PowerPoint
(bars, curves, icons), found one at a time by eye; evergreen content went through external research; the full visual pass
existed to catch what the first two let through.

## Target
About one hour of Claude's work per market, several times fewer tokens, almost nothing left for the visual pass.

## Pieces
1. `specs/slides.yaml`: one entry per slide template, written once. For every text box: min and max characters, number of
   lines, tone, number of items (e.g. signals: 6 to 8 bubbles of 45 to 60 characters; dated rows 120 to 140 characters with
   the source label; myth answers about 125; « truths that flipped » right boxes about 70; Venn terms 2 words).
   Generated from the templates (box size, font size) and then corrected with Pierre's remarks (RULES.md).
2. Research prompts give, per slide, the exact keys with their min/max and the format rules (amounts: $56B, $2.1B, $787M;
   names in capitals where the slide shows them in capitals; no em dash, no semicolon). The self-check script refuses any
   text out of its range; the LLM delivers at « 0 problems ».
3. Import: a text out of range comes back as an error with its key (TEXT LENGTH), never rewritten by hand.
4. Evergreen chapters (market definition, pain points, value creation, tech layers): written by Claude directly in the spec
   format, in one pass, without external research. External research only for dated facts: signals, figures, rounds, news,
   failures, top players, sources.
5. Templates with fixed drawings: either driven by data (done: vbars, hbars, spans for « How long to pass $1B », growth for
   « How fast are startups growing », worldmap places) or removed from the model.
6. Visual pass: only the slides whose look depends on the market (charts, logos, maps) plus a thumbnail sheet of all slides.

## Order of work
1. specs/slides.yaml from the templates (script) + Pierre's targets.
2. make_market_prompts.py reads the spec (ranges, format rules) and the self-check uses it.
3. import_research.py: TEXT LENGTH check from the spec.
4. Evergreen generator: one file per chapter written by Claude from the spec.
5. Remaining fixed-drawing templates: list them (x/sig_*, x/* with charts) and convert or drop.
6. Pending for delivered decks: Humanoid Robotics and In Vivo CAR-T research-text rows (dated timelines, myths, truths)
   to bring to the new lengths.

## Status (14 Nov 2026, 03:40)
Done: 1 (specs/slides.yaml from the validated decks, not measured in the browser: rawfit and fixlib change the boxes),
2 (prompts print MIN-MAX, self-check uses it), 3 (TEXT LENGTH gate), 4 (evergreen chapters out of the zip, briefs in
decks/<handle>/evergreen/, tools/check_results.py), 5 (no other converted chart with a fixed drawing in use: x/sig_* and
fast_startups_growing are guarded by FIXED CHART), 6 (Humanoid and In Vivo texts in range, lengths.yaml).
Also: PDF printed in ranges of 50 pages (Chromium failed on the whole deck).
Next market: first one made end to end with this method; measure Claude's time and tokens and tell Pierre.
