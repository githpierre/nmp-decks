#!/usr/bin/env python3
"""ARTICLE AMOUNT (24 Nov 2026): « an $12B » is wrong. Before an amount, « an » only goes with a number read with a vowel
sound (8…, 11, 18, 11.9, 18,000). Checks the generated deck.yaml of each deck given (all decks when none)."""
import re, sys, pathlib
R = pathlib.Path(__file__).resolve().parent.parent / 'decks'
bad_an = re.compile(r'\b[Aa]n \$(?!8|1[18](?!\d))\d')
bad_a = re.compile(r'\b[Aa] \$(?=8|1[18](?!\d))')
n = 0
for d in (sys.argv[1:] or sorted(p.name for p in R.iterdir() if (p / 'deck.yaml').exists())):
    for i, line in enumerate((R / d / 'deck.yaml').read_text().splitlines(), 1):
        for m in list(bad_an.finditer(line)) + list(bad_a.finditer(line)):
            n += 1; print(f'ARTICLE AMOUNT: {d} deck.yaml:{i} | {line[max(0,m.start()-40):m.end()+20].strip()}')
        if ('«' in line or '»' in line) and not line.lstrip().startswith('link:'):   # slides are in US English (24 Nov 2026)
            n += 1; print(f'ARTICLE AMOUNT: French quote marks in {d} deck.yaml:{i}, use “ ” | {line.strip()[:80]}')
sys.exit(1 if n else 0)
