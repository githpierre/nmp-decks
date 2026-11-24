#!/bin/bash
# One command for a deck: import -> decisions -> build -> audits. Stops on the first failure (12 Nov 2026: a crashed import went
# unseen behind a grep and the old deck was rebuilt). usage: tools/rebuild.sh <handle> [--png]
# --fast (piste C, 18 Nov 2026): only the slides whose data changed are rendered (seconds instead of 5 min). The in-browser
# audit still checks every slide. A full build (--png) is REQUIRED before any review page or PDF.
# The import arguments of the deck live in decks/<handle>/import.args (results folder, --demo, --out, --name, --pain, --value, --model…).
set -o pipefail; cd "$(dirname "$0")/.." || exit 1; H=$1; D=decks/$H
[ -f "$D/import.args" ] || { echo "no $D/import.args"; exit 1; }
# database slides are regenerated from the latest base only for decks made with make_db_slides.py (they have a db_text.yaml)
[ -f "$D/db_text.yaml" ] && { python3 tools/make_db_slides.py "$H" --name "$( [ -f "$D/db_name.txt" ] && cat "$D/db_name.txt" || grep -o -- '--name "[^"]*"' "$D/import.args" | cut -d'"' -f2)" > /tmp/db_$H.log 2>&1 || { tail -5 /tmp/db_$H.log; echo "DATABASE SLIDES FAILED"; exit 1; }; }
grep -E "WEAK ROUND SOURCE|ROUND EXTENSION" /tmp/db_$H.log 2>/dev/null | cut -c1-170
eval "python3 -I tools/import_research.py $(cat "$D/import.args")" > /tmp/import_$H.log 2>&1 || { tail -8 /tmp/import_$H.log; echo "IMPORT FAILED"; exit 1; }
grep -E "LABEL SPLIT|FAVICON SHARED|CATEGORIES MISMATCH|MODEL MARKET LEFT|MODEL ICON LEFT|SIGNAL (STALE|NO DATE)|CONTRAST ROWS|COVER NOT COPIED|DUPLICATE KEY|PROMPT TALK|NO ANSWER|SERIES MIXED|SERIES GEOMETRY|MAP PLACE|STAGE LABEL|ICON TWICE|VENN WORDS|TEXT LENGTH|TRENDS TEXT|FIXED CHART|extra slide|slide dropped|logos missing" /tmp/import_$H.log | cut -c1-170
# piste B (18 Nov 2026): a slide that still shows the reference market blocks the full build, so it can never reach a review page
# or a PDF. While drafting, --fast builds anyway and only lists them.
if [ "$2" = "--png" ] && grep -qE "CATEGORIES MISMATCH|MODEL MARKET LEFT|MODEL ICON LEFT|MODEL SOURCES LEFT|NO ANSWER|FIXED CHART|SERIES MIXED|SERIES GEOMETRY|STAGE LABEL|ICON TWICE|TRENDS TEXT" /tmp/import_$H.log; then echo "REFERENCE MARKET LEFT: fix the lines above (or build a draft with --fast)"; exit 1; fi
# a company placed outside the market on S01 never shows as a player elsewhere (Stablecoin payments, 22 Nov 2026): blocks --png
python3 tools/check_outside.py "$H" > /tmp/outside_$H.log; grep "OUTSIDE PLAYER" /tmp/outside_$H.log
python3 tools/check_article.py "$H" > /tmp/article_$H.log; cat /tmp/article_$H.log; [ "$2" = "--png" ] && [ -s /tmp/article_$H.log ] && { echo "ARTICLE AMOUNT: fix the lines above"; exit 1; }
if [ "$2" = "--png" ] && grep -q "OUTSIDE PLAYER" /tmp/outside_$H.log; then echo "OUTSIDE PLAYER: rewrite these slides before the full build"; exit 1; fi
python3 tools/atelier2/make_decisions.py "$D" > /dev/null || { echo "DECISIONS FAILED"; exit 1; }
MODE=$2
if [ "$2" = "--fast" ]; then ONLY=$(python3 tools/changed_slides.py "$H"); if [ "$ONLY" = "ALL" ]; then MODE=--png; elif [ -z "$ONLY" ]; then echo "no slide changed"; exit 0; else MODE="--only $ONLY"; echo "fast: slides $ONLY"; fi; fi
python3 build.py "$H" $MODE > /tmp/build_$H.log 2>&1 || { tail -5 /tmp/build_$H.log; echo "BUILD FAILED"; exit 1; }
grep -E "^[0-9]+ \||issues" /tmp/build_$H.log | cut -c1-150
python3 tools/audit_layout.py "$H" > /tmp/audit_$H.txt; grep -v TEXT_PAD /tmp/audit_$H.txt | cut -c1-170
grep TEXT_PAD /tmp/audit_$H.txt | awk -F'|' '{print $1}' | sort -n | uniq -c | awk '{printf "PAD slide %s (%s) ", $2, $1} END {if (NR) print ""}'
[ -d "$D/out/snap" ] && python3 tools/diff_slides.py "$H"
python3 tools/changed_slides.py "$H" --save
[ "$MODE" != "--png" ] && echo "FAST BUILD: run tools/rebuild.sh $H --png before the review page or the PDF"
exit 0
