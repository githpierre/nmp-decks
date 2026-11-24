"""S09 « Where did investors put their money this past year? » from the latest nmp-seo startups base, by the market's
categories (markets.category). Writes the rows of the twin (live.yaml key given) ; companies without a logo are skipped for
the logo tiles (product-page rule: a missing logo is replaced by the next company that has one).

    python3 tools/pp/s09_from_base.py humanoid-robotics ed168p --today 2026-11-12 --short "Long category=Short label;..." """
import argparse, collections, sys, yaml
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, '/home/claude/nmp-seo/outils/startups'); sys.path.insert(0, str(ROOT / 'tools'))
import gen_lib as g, import_research as ir, skip_rounds; skip_rounds.patch(g)   # doubtful rounds never reach a slide

ap = argparse.ArgumentParser(); ap.add_argument('handle'); ap.add_argument('key'); ap.add_argument('--today', default='2026-11-12'); ap.add_argument('--short', default='')
a = ap.parse_args()
SHORT = dict(x.split('=') for x in a.short.split(';') if '=' in x)
_sf = ROOT / 'decks' / a.handle / 'cat_short.yaml'
if _sf.exists(): SHORT = {**yaml.safe_load(_sf.read_text()), **SHORT}     # same short names as the db slides
ir.MARKET = a.handle; ir.OUTDIR = ROOT / 'decks' / a.handle
b = g.Base(); import startup_status as _ss   # startups only (base rule), as on the db slides
M = {m['company_id']: m for m in b.markets[a.handle] if _ss.table_startup_base(b, m['company_id'])[0]}
since = f'{int(a.today[:4]) - 1}{a.today[4:]}'
S = collections.defaultdict(float); T = collections.defaultdict(lambda: collections.defaultdict(float))
for cid, m in M.items():
    for r in g.rounds_for(b, cid, 'deals'):
        if (r['round_type'] or '').upper() == 'IPO' or 'IPO' in (r['round_label'] or ''): continue   # equity rounds only
        # grouped by the SHORT name: two base categories merged into one segment make one row (AI in drug discovery, 20 Nov 2026)
        if r['date'] >= since: v = float(r['amount_usd'] or 0); c = SHORT.get(m['category'], m['category']); S[c] += v; T[c][b.companies[cid]['name']] += v
tot, mx = sum(S.values()), max(S.values())
mon = lambda v: f'${v/1e9:.0f}B' if v >= 9.95e9 else f'${v/1e9:.1f}B'.replace('.0B', 'B') if v >= 1e9 else f'${v/1e6:.0f}M'   # amount rule
rows = []
for c, v in sorted(S.items(), key=lambda x: -x[1]):
    # a category whose rounds have no public amount is left out (RULES: no 0% slice, no hole). Natural hydrogen, 21 Nov 2026:
    # « Hydrogen explorers $0M » with no logo (Koloma's JERA round of Oct 2026 has no amount; the live S09-02 showed « $nanM »)
    if v <= 0: print(f'DROPPED (no public amount): {SHORT.get(c, c)}'); continue
    top = [n for n, x in sorted(T[c].items(), key=lambda x: -x[1]) if x > 0]
    ok = [(n, ir.logo(n)) for n in top]; ok = [(n, p) for n, p in ok if '/ini/' not in p][:3]
    p = 100 * v / tot
    rows.append(dict(name=SHORT.get(c, c), names=[n for n, _ in ok][:2], v=mon(v), pct=f'{p:.0f}% of total' if p >= 1 else 'under 1% of total',
                     w=round(100 * v / mx, 1), logos=[dict(src=s) for _, s in ok]))
f = ROOT / 'decks' / a.handle / 'live.yaml'; L = yaml.safe_load(f.read_text()); L[a.key]['rows'] = rows
f.write_text(yaml.dump(L, allow_unicode=True, sort_keys=False, width=1000))
print(f'{mon(tot)} since {since}, base to {a.today}')
for r in rows: print(r['name'], r['v'], r['pct'], r['names'], len(r['logos']))
