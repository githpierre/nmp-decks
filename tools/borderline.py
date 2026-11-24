"""Step 0: the companies that weigh most in a market (money raised over 24 months, then the rest of the top by total raised),
with what they do, to test each one against the market's decision_rule (nmp-seo market_definitions.csv) BEFORE the build.
Claude decides with the rule and fixes the base itself (markets.csv, market_fit.csv, decision): never a question to Pierre
(Pierre, 18 Nov 2026: Oura, WHOOP, then Eight Sleep left Longevity after the PDF went to the client).
    python3 tools/borderline.py <handle> [--n 25]"""
import argparse, collections, csv, sys, datetime
sys.path.insert(0, '/home/claude/nmp-seo/outils/startups'); import gen_lib as g, startup_status as _ss
import skip_rounds; skip_rounds.patch(g)   # doubtful rounds never reach a slide
ap = argparse.ArgumentParser(); ap.add_argument('handle'); ap.add_argument('--n', type=int, default=25); a = ap.parse_args()
b = g.Base(); M = {m['company_id']: m for m in b.markets[a.handle]}
since = (datetime.date.today() - datetime.timedelta(days=730)).isoformat()
tot = collections.Counter(); rec = collections.Counter()
for cid in M:
    for r in g.rounds_for(b, cid, 'deals'):
        v = float(r['amount_usd'] or 0); tot[cid] += v
        if r['date'] >= since: rec[cid] += v
D = {r['market_handle']: r for r in csv.DictReader(open('/home/claude/nmp-seo/data/startups/market_definitions.csv'))}
print('RULE:', D[a.handle]['decision_rule'][:1500], '\n')
for cid in list(dict.fromkeys([c for c, _ in rec.most_common(a.n)] + [c for c, _ in tot.most_common(a.n)])):
    m = M[cid]; c = b.companies[cid]; fy = str(c.get('founded_year') or '')
    r0 = ' (non-startup: kept as history, left out of the slides)' if not _ss.table_startup_base(b, cid)[0] else ''
    print(f"{b.companies[cid]['name'][:28]:28} {rec[cid]/1e6:7.0f}M/24m {tot[cid]/1e6:7.0f}M | {m.get('category','')[:30]:30} | {(m.get('what_they_do') or '')[:90]}{r0}")
