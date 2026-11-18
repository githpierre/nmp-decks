#!/bin/bash
# One command for a deck: import -> decisions -> build -> audits. Stops on the first failure (12 Nov 2026: a crashed import went
# unseen behind a grep and the old deck was rebuilt). usage: tools/rebuild.sh <handle> [--png]
# --fast (piste C, 18 Nov 2026): only the slides whose data changed are rendered (seconds instead of 5 min). The in-browser
# audit still checks every slide. A full build (--png) is REQUIRED before any review page or PDF.
# The import arguments of the deck live in decks/<handle>/import.args (results folder, --demo, --out, --name, --pain, --value, --model…).
set -o pipefail; cd "$(dirname "$0")/.." || exit 1; H=$1; D=decks/$H
[ -f "$D/import.args" ] || { echo "no $D/import.args"; exit 1; }
# database slides are regenerated from the latest base only for decks made with make_db_slides.py (they have a db_text.yaml)
[ -f "$D/db_text.yaml" ] && { python3 tools/make_db_slides.py "$H" --name "$(grep -o -- '--name "[^"]*"' "$D/import.args" | cut -d'"' -f2)" > /tmp/db_$H.log 2>&1 || { tail -5 /tmp/db_$H.log; echo "DATABASE SLIDES FAILED"; exit 1; }; }
eval "python3 -I tools/import_research.py $(cat "$D/import.args")" > /tmp/import_$H.log 2>&1 || { tail -8 /tmp/import_$H.log; echo "IMPORT FAILED"; exit 1; }
grep -E "MODEL MARKET LEFT|MODEL ICON LEFT|SIGNAL (STALE|NO DATE)|CONTRAST ROWS|COVER NOT COPIED|DUPLICATE KEY|PROMPT TALK|NO ANSWER|SERIES MIXED|MAP PLACE|STAGE LABEL|ICON TWICE|VENN WORDS|TEXT LENGTH|FIXED CHART|extra slide|slide dropped|logos missing" /tmp/import_$H.log | cut -c1-170
# piste B (18 Nov 2026): a slide that still shows the reference market blocks the full build, so it can never reach a review page
# or a PDF. While drafting, --fast builds anyway and only lists them.
if [ "$2" = "--png" ] && grep -qE "MODEL MARKET LEFT|MODEL ICON LEFT|MODEL SOURCES LEFT|NO ANSWER|FIXED CHART|SERIES MIXED|STAGE LABEL|ICON TWICE" /tmp/import_$H.log; then echo "REFERENCE MARKET LEFT: fix the lines above (or build a draft with --fast)"; exit 1; fi
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
