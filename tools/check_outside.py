"""OUTSIDE PLAYER: a company that the S01 radar (ed007p) places outside the market is shown as a player on another slide.
Rule (Stablecoin payments, 22 Nov 2026): the live S05 and S12 compared Tether, Circle, PayPal and Ripple, the four companies of
S01's corners, so the twins were rewritten with players from inside the market. A company may still be named in a sentence
(« bought by Stripe »): only a « name: » field (a column, a bar, a card, a logo tile) counts.
    python3 tools/check_outside.py <handle>        (run by rebuild.sh after the import; blocks --png)"""
import sys, yaml
from pathlib import Path

D = Path(__file__).resolve().parent.parent / 'decks' / sys.argv[1]
live = yaml.safe_load((D / 'live.yaml').read_text()) if (D / 'live.yaml').exists() else {}
radar = (live or {}).get('ed007p') or {}
OUT = {radar[k]['name'] for k in ('TL', 'TR', 'BL', 'BR') if isinstance(radar.get(k), dict) and radar[k].get('name')}
deck = yaml.safe_load((D / 'deck.yaml').read_text()) if (D / 'deck.yaml').exists() else None
slides = deck.get('slides', []) if isinstance(deck, dict) else (deck or [])


def names(x):
    if isinstance(x, dict):
        for k, v in x.items():
            if k in ('name', 'short', 'firm', 'company') and isinstance(v, str): yield v   # 'short': a scorecard column (Neocloud ed209p IREN, 24 Nov 2026)
            else: yield from names(v)
    elif isinstance(x, list):
        for v in x: yield from names(v)


n = 0
for s in slides:
    if not isinstance(s, dict) or s.get('id') == 'ed007p': continue
    for nm in set(names(s)) & OUT:
        print(f"OUTSIDE PLAYER: {s.get('id')} shows {nm}, placed outside the market on S01 (ed007p): rewrite with players from inside"); n += 1
print(f'{n} outside players ({", ".join(sorted(OUT)) or "no S01 twin"})')
