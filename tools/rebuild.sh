#!/bin/bash
# One command for a deck: import -> decisions -> build -> audits. Stops on the first failure (12 Nov 2026: a crashed import went
# unseen behind a grep and the old deck was rebuilt). usage: tools/rebuild.sh <handle> [--png]
# The import arguments of the deck live in decks/<handle>/import.args (results folder, --demo, --out, --name, --pain, --value, --model…).
set -o pipefail; cd "$(dirname "$0")/.." || exit 1; H=$1; D=decks/$H
[ -f "$D/import.args" ] || { echo "no $D/import.args"; exit 1; }
# database slides are regenerated from the latest base only for decks made with make_db_slides.py (they have a db_text.yaml)
[ -f "$D/db_text.yaml" ] && { python3 tools/make_db_slides.py "$H" --name "$(grep -o -- '--name "[^"]*"' "$D/import.args" | cut -d'"' -f2)" > /tmp/db_$H.log 2>&1 || { tail -5 /tmp/db_$H.log; echo "DATABASE SLIDES FAILED"; exit 1; }; }
eval "python3 -I tools/import_research.py $(cat "$D/import.args")" > /tmp/import_$H.log 2>&1 || { tail -8 /tmp/import_$H.log; echo "IMPORT FAILED"; exit 1; }
grep -E "MODEL MARKET LEFT|MODEL ICON LEFT|SIGNAL (STALE|NO DATE)|CONTRAST ROWS|COVER NOT COPIED|DUPLICATE KEY|extra slide|slide dropped|logos missing" /tmp/import_$H.log | cut -c1-170
python3 tools/atelier2/make_decisions.py "$D" > /dev/null || { echo "DECISIONS FAILED"; exit 1; }
python3 build.py "$H" $2 > /tmp/build_$H.log 2>&1 || { tail -5 /tmp/build_$H.log; echo "BUILD FAILED"; exit 1; }
grep -E "^[0-9]+ \||issues" /tmp/build_$H.log | cut -c1-150
python3 tools/audit_layout.py "$H" > /tmp/audit_$H.txt; grep -v TEXT_PAD /tmp/audit_$H.txt | cut -c1-170
grep TEXT_PAD /tmp/audit_$H.txt | awk -F'|' '{print $1}' | sort -n | uniq -c | awk '{printf "PAD slide %s (%s) ", $2, $1} END {if (NR) print ""}'
[ -d "$D/out/snap" ] && python3 tools/diff_slides.py "$H"
exit 0
