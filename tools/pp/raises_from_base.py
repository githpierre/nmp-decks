"""S09-02 « Which <market> startups got the biggest checks lately? » (pp_raises, 6 bars) from the latest startups base, as mkpp.py
built it: the biggest equity round of each startup of the market over the last two years, one bar per company, IPO, debt, grants
and secondaries left out. Prints the slide as YAML (27 Nov 2026: the live S09-02 of deepfake detection and quantum sensing were
older than the base: Incode with a Form D only, Pramaana outside the market, Q-CTRL's $290M missing).
    python3 tools/pp/raises_from_base.py <handle> --name "<short name>" [--today YYYY-MM-DD]"""
import argparse, datetime, os, re, sys, yaml
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, '/home/claude/nmp-seo/outils/startups'); sys.path.insert(0, str(ROOT / 'tools'))
import gen_lib as g, import_research as ir, skip_rounds; skip_rounds.patch(g)
import startup_status as ss
ap = argparse.ArgumentParser(); ap.add_argument('handle'); ap.add_argument('--name', required=True)
ap.add_argument('--today', default=datetime.date.today().isoformat()); a = ap.parse_args()
ir.MARKET = a.handle; ir.OUTDIR = ROOT / 'decks' / a.handle
b = g.Base(); since = f'{int(a.today[:4]) - 2}{a.today[4:]}'
best = {}
for m in b.markets[a.handle]:
    cid = m['company_id']
    if not ss.table_startup_base(b, cid)[0]: continue
    for r in g.rounds_for(b, cid, 'deals'):
        t = (r['round_type'] or '')
        if r['date'] < since or t in ('IPO', 'Post-IPO', 'Secondary', 'Debt', 'Grant') or 'IPO' in (r['round_label'] or ''): continue
        v = float(r['amount_usd'] or 0)
        if v > 0 and v > best.get(cid, (0,))[0]: best[cid] = (v, r)
R = []
for cid, (v, r) in sorted(best.items(), key=lambda x: -x[1][0])[:6]:
    n = b.companies[cid]['name']; d = r['date']
    if len(n) > 18: n = re.sub(r'\s+(Imaging |Quantum )?(Technologies|Technology|Systems|Labs)$', '', n)   # one line under the bar (NVision Imaging Technologies)
    dt = datetime.date(int(d[:4]), int(d[5:7]), 1).strftime('%b %Y') if len(d) >= 7 else d[:4]
    st = {'Series D+': 'Late stage', 'Other': 'Round', 'Unknown': 'Round', '': 'Round'}.get(r['round_type'] or '', r['round_type'])
    # the logo of the base company, never one looked up from the short name (« NVision » fetched another firm's favicon)
    src = f'../../assets/logos/{cid}.png' if (ROOT / 'assets/logos' / f'{cid}.png').exists() else ir.logo(b.companies[cid]['name'])
    R.append(dict(name=n, amt=int(v), src=src, stage=st, date=dt))
nm = a.name
print(yaml.safe_dump(dict(id='pp_s0902', type='pp_raises', section='Investor bets', title=f'Which {nm} startups\ngot the biggest checks lately?', rounds=R,
    note=[f'We listed the biggest equity rounds raised by {nm} startups over the last few years', 'We used company announcements and the press, and all our sources are at the end of the report']),
    allow_unicode=True, sort_keys=False, width=1000))
