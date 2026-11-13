"""Check research result files (the other LLM's, or the evergreen chapters Claude writes) against specs/slides.yaml before importing.

    python3 tools/check_results.py <model deck> <result.md> [...]      e.g. decks/in-vivo-car-t decks/x/research/*.md

Same checks as the self-check given to the research LLM: lengths, words, em dash, semicolon, amount format. Prints « N problems »."""
import re, sys, yaml
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent)); import spec
ROOT = Path(__file__).resolve().parent.parent
model = {s['id']: s for s in yaml.safe_load((ROOT / sys.argv[1] / 'deck.yaml').read_text())['slides']}
F = chr(96) * 3; n = 0
for f in sys.argv[2:]:
    for sid, body in re.findall(r'### (\S+)\s+' + F + r'yaml\n(.*?)' + F, Path(f).read_text(), re.S):
        d = yaml.safe_load(body) or {}
        if d.get('status') != 'ok': continue
        m = model.get(sid) or model.get(re.sub(r'-s\d+$', '-s1', sid)) or {}
        d['type'] = d.get('type') or m.get('type')
        P = [p for p in spec.problems(d, sid) if 'capitals' not in p]
        flat = yaml.dump(d, allow_unicode=True)
        P += [f'{sid} | {w}' for c, w in ((chr(8212), 'em dash'), (chr(8211), 'en dash'), ('; ', 'semicolon')) if c in flat]
        P += [f'{sid} | amount format {a}' for a in re.findall(r'\$\d+\.\d{2,}[BMK]|\$\d{2,}\.\d[B]|\$\d+\.0[BMK]|\d+\.\d{2,}%', flat)]
        for p in P: print(p)
        n += len(P)
print(n, 'problems')
