"""Draft of decks/<handle>/sources_key.yaml (point 5, Pierre 18 Nov 2026): the 20 source URLs most cited in the research
files, one row each, with the claims they backed, so Claude only writes the « why we trust it » and « how we used it » lines.

    python3 tools/draft_sources_key.py <handle> [--n 20]    -> decks/<handle>/sources_key.draft.yaml (never overwrites sources_key.yaml)

Rows: name (publisher + subject, 2 short lines, to rewrite), url, count, claims (up to 3), why/how left as TO WRITE.
Same publisher label as the slides (PUB of build_sources.py). Our own site is never a source (Pierre's rule)."""
import collections, re, sys, yaml
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
H = sys.argv[1]; N = int(sys.argv[sys.argv.index('--n') + 1]) if '--n' in sys.argv else 20
_src = (ROOT / 'tools/build_sources.py').read_text(); exec(_src[_src.index('PUB = {'):_src.index('def title(')])
C = collections.Counter(); CL = collections.defaultdict(list)
for f in sorted((ROOT / 'decks' / H / 'research').glob('*.md')):
    for blk in re.findall(r'```yaml\n(.*?)```', f.read_text(), re.S):
        try: d = yaml.safe_load(blk) or {}
        except Exception: continue
        for s in (d.get('sources') or []) if isinstance(d, dict) else []:
            u = (s or {}).get('url') if isinstance(s, dict) else None
            if not u or 'newmarketpitch.com' in u: continue
            u = u.rstrip('/'); C[u] += 1
            if s.get('claim') and s['claim'] not in CL[u] and len(CL[u]) < 3: CL[u].append(s['claim'])
rows = []
for u, n in C.most_common(N):
    rows.append({'name': f"{pub(u)},\n{(CL[u] or [''])[0][:28]}", 'why': 'TO WRITE', 'how': 'TO WRITE', 'url': u, 'count': n, 'claims': CL[u]})
out = ROOT / 'decks' / H / 'sources_key.draft.yaml'
out.write_text(yaml.safe_dump({'rows': rows}, allow_unicode=True, sort_keys=False, width=150))
print(len(rows), 'rows ->', out)
