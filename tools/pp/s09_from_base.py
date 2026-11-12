"""S09 « Where did investors put their money this past year? » from the latest nmp-seo startups base, by the market's
categories (markets.category). Writes the rows of the twin (live.yaml key given) ; companies without a logo are skipped for
the logo tiles (product-page rule: a missing logo is replaced by the next company that has one).

    python3 tools/pp/s09_from_base.py humanoid-robotics ed168p --today 2026-11-12 --short "Long category=Short label;..." """
import argparse, collections, sys, yaml
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, '/home/claude/nmp-seo/outils/startups'); sys.path.insert(0, str(ROOT / 'tools'))
import gen_lib as g, import_research as ir

ap = argparse.ArgumentParser(); ap.add_argument('handle'); ap.add_argument('key'); ap.add_argument('--today', default='2026-11-12'); ap.add_argument('--short', default='')
a = ap.parse_args()
SHORT = dict(x.split('=') for x in a.short.split(';') if '=' in x)
ir.MARKET = a.handle; ir.OUTDIR = ROOT / 'decks' / a.handle
b = g.Base(); M = {m['company_id']: m for m in b.markets[a.handle]}
since = f'{int(a.today[:4]) - 1}{a.today[4:]}'
S = collections.defaultdict(float); T = collections.defaultdict(lambda: collections.defaultdict(float))
for cid, m in M.items():
    for r in g.rounds_for(b, cid, 'deals'):
        if (r['round_type'] or '').upper() == 'IPO' or 'IPO' in (r['round_label'] or ''): continue   # equity rounds only
        if r['date'] >= since: v = float(r['amount_usd'] or 0); S[m['category']] += v; T[m['category']][b.companies[cid]['name']] += v
tot, mx = sum(S.values()), max(S.values())
mon = lambda v: f'${v/1e9:.1f}B' if v >= 1e9 else f'${v/1e6:.0f}M'
rows = []
for c, v in sorted(S.items(), key=lambda x: -x[1]):
    top = [n for n, x in sorted(T[c].items(), key=lambda x: -x[1]) if x > 0]
    ok = [(n, ir.logo(n)) for n in top]; ok = [(n, p) for n, p in ok if '/ini/' not in p][:3]
    p = 100 * v / tot
    rows.append(dict(name=SHORT.get(c, c), names=[n for n, _ in ok][:2], v=mon(v), pct=f'{p:.0f}% of total' if p >= 1 else 'under 1% of total',
                     w=round(100 * v / mx, 1), logos=[dict(src=s) for _, s in ok]))
f = ROOT / 'decks' / a.handle / 'live.yaml'; L = yaml.safe_load(f.read_text()); L[a.key]['rows'] = rows
f.write_text(yaml.dump(L, allow_unicode=True, sort_keys=False, width=1000))
print(f'{mon(tot)} since {since}, base to {a.today}')
for r in rows: print(r['name'], r['v'], r['pct'], r['names'], len(r['logos']))
