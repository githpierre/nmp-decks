"""S09 investor bets: startups base (nmp-seo) -> JSON per market (top 6 categories, amounts, names, logo candidates).
Rules (11 Nov 2026): equity rounds of the last 12 months, not aggregated, no IPO / post-IPO / secondary / debt / grant,
startups only, sourcing rule of the base applied everywhere (article, or two agreeing databases under $100M);
logos are examples: fill to 3 with the category's other active startups (window raisers first, then all-time raisers).
Usage: python3 prep2.py out.json handle [handle ...]"""
import sys, os, re, json, datetime
os.environ['NMP_SOURCING_RULE'] = 'all'
sys.path.insert(0, '/home/claude/nmp-seo/outils/startups'); os.chdir('/home/claude/nmp-seo/data/startups')
import gen_lib as G
from PIL import Image
B = G.Base()
TODAY = datetime.date.today(); START = (TODAY.replace(year=TODAY.year - 1)).isoformat()
EXCL_TYPES = {'IPO', 'Post-IPO', 'Secondary', 'Debt', 'Grant'}
SKIP = {('ai-powered-market-research', 'strella')}          # merged identity, to split (inbox/2026-11-11-s09-a-separer.csv)
SHORT = json.load(open('/home/claude/s09/short_cats.json'))
LOGOS = ['/home/claude/nmp-decks/assets/logos', '/home/claude/s09/lib', '/home/claude/s09/logos_g', '/home/claude/nmp-product-pages/w/logos_all',
         '/home/claude/nmp-product-pages/w/s9/logos']

def in_window(d):
    d = d[:10]
    if len(d) == 4: return False
    return d >= START[:len(d)] if len(d) == 7 else d >= START

def short_name(n):
    n = re.sub(r'\s*\(.*?\)', '', n or '')
    n = re.sub(r'\s+(Technologies|Technology|Industries|Inc\.?|Ltd\.?|Limited|Corp\.?|Pharmaceuticals|Therapeutics|Oncology|Holdings)$', '', n)
    return n.strip()

def logo(cid, name, web):
    cands = [cid, re.sub(r'[^a-z0-9]', '', (name or '').lower()), re.sub(r'[^a-z0-9]', '', re.sub(r'\(.*?\)', '', name or '').lower())]
    if web:
        dom = re.sub(r'^https?://(www\.)?', '', web).split('/')[0]; cands.append(re.sub(r'[^a-z0-9]', '', dom.split('.')[0]))
    for d in LOGOS:
        for c in cands:
            f = f'{d}/{c}.png'
            if c and os.path.exists(f):
                w, h = Image.open(f).size
                if max(w, h) / min(w, h) <= 1.15: return f          # square logos only (Pierre, 11 Nov 2026)
    return None

def ok_company(cid, active=False):
    c = B.companies.get(cid, {})
    if c.get('company_type') != 'Startup': return False
    if active and c.get('status') in ('Acquired', 'Shutdown', 'IPO'): return False
    return True

def market(h):
    rows = {}
    members = {m['company_id']: m for m in B.markets[h] if (h, m['company_id']) not in SKIP}
    win = []
    for cid, mrow in members.items():
        if not ok_company(cid): continue
        src = G.rounds_sourcing(B, cid)
        for r in B.rounds.get(cid, []):
            if r['is_equity'] != 'true' or r.get('aggregate') == 'true' or not r['amount_usd']: continue
            if r['round_type'] in EXCL_TYPES or not in_window(r['date']): continue
            if not src.get(r['round_id'], (False,))[0]: continue
            win.append((cid, mrow.get('category') or '', float(r['amount_usd'])))
    tot = sum(a for _, _, a in win)
    bycat = {}
    for cid, cat, a in win:
        if not cat: continue
        bycat.setdefault(cat, {}).setdefault(cid, 0); bycat[cat][cid] += a
    cats = sorted(bycat.items(), key=lambda kv: -sum(kv[1].values()))
    out = []
    for cat, comp in cats:
        v = sum(comp.values())
        if v < 1e6: continue
        ranked = sorted(comp.items(), key=lambda kv: -kv[1])
        names = [short_name(members[cid].get('display_name') or B.companies[cid].get('name')) for cid, _ in ranked[:2]]
        cand = [cid for cid, _ in ranked if ok_company(cid, active=True)]
        alltime = sorted([cid for cid, m in members.items() if m.get('category') == cat and cid not in comp and ok_company(cid, active=True)],
                         key=lambda cid: -sum(float(r['amount_usd'] or 0) for r in B.rounds.get(cid, []) if r['is_equity'] == 'true'))
        logos = []
        for cid in cand + alltime:
            c = B.companies[cid]; nm = short_name(members[cid].get('display_name') or c.get('name'))
            logos.append(dict(id=cid, name=nm, web=c.get('website'), path=logo(cid, nm, c.get('website'))))
            if sum(1 for l in logos if l['path']) >= 3 or len(logos) >= 25: break
        out.append(dict(cat=cat, short=SHORT.get(h, {}).get(cat, cat), v=v, pct=v / tot, names=names, logos=logos))
        if len(out) == 6: break
    return dict(handle=h, total=tot, n=len(win), start=START, rows=out)

if __name__ == '__main__':
    OUT = os.path.abspath(os.path.join('/home/claude/s09', sys.argv[1])); D = {h: market(h) for h in sys.argv[2:]}
    json.dump(D, open(OUT, 'w'), indent=1, default=str)
    for h, d in D.items():
        print(f"\n== {h} ${d['total']/1e9:.2f}B {d['n']} rounds")
        for r in d['rows']:
            print(f"  {r['cat'][:44]:44s} ${r['v']/1e6:7.0f}M {r['pct']*100:3.0f}% | {', '.join(r['names'])} | logos {sum(1 for l in r['logos'] if l['path'])}/{len(r['logos'])}")
