"""Series review deck: 5 markets in a row for each product-page slide type, from the existing data of markets 1-132.
usage: python3 mkpp2.py <slug>"""
import json, os, re, sys, csv, yaml
sys.path.insert(0, os.path.dirname(__file__))
import mkpp
from mkpp import logo, ini, J, two, SRC, ROOT
W1, S10, W = '/root/w/m101', '/root/w/s10', '/root/w/m131'
mkpp.LOGO_DIRS += [f'{W1}/s01/logos', '/root/w/logos_all', '/root/w/s11/logos', '/root/w/s11/m/logos', '/root/w/s11/s3prod/logos', '/root/w/s11/s3prod/logos_fill', f'{W1}/s05/newlogos', f'{W1}/s12/newlogos', f'{W1}/s12/newlogos2']
MK = {r['handle']: r for r in csv.DictReader(open('/root/w/nmp_slide_kit/markets_225.csv'))}
def label(h): return ' '.join(''.join(w.split()) for w in re.split(r'\s{2,}', MK[h]['market_name_for_slide'].strip()))
def nm(h):
    for f in (f'{W}/data/mc_{h}.json', f'{W1}/s07/mc/{h}.json', f'{S10}/gd/{h}.json'):
        if os.path.exists(f): return J(f)['name']
    return MK[h]['nom_market'].replace(' market', '')
NEW = ('low-carbon-cement', 'metal-additive-manufacturing')
OLD = ['ai-marketing', 'radiopharmaceuticals', 'cross-border-b2b-payments']
out = []
def B(h, **k): d = dict(label=label(h)); d.update(k); out.append(d)

# S01 radar
S1 = {m['handle']: m for m in J(f'{W1}/s01/spec.json')['markets']}; N1 = J(f'{W}/data/s01.json')
for h in OLD + list(NEW):
    if h in N1:
        d = N1[h]; s = dict(type='pp_radar', pill='MARKET MAP', label='', title=two(d['title']), caption=d['caption'], inside=[logo(x) for x in d['inside']])
        for k in ('TL', 'TR', 'BL', 'BR'): s[k] = dict(src=logo(d[k][0]), name=d[k][1], text=d[k][2])
    else:
        d = S1[h]; s = dict(type='pp_radar', pill='MARKET MAP', label='', title=two(d['title']), caption=d['caption'], inside=[logo(x) for x in d['inside']])
        for k in ('TL', 'TR', 'BL', 'BR'): s[k] = dict(src=logo(d[k]['logo']), name=d[k]['name'], text=d[k]['text'])
    out.append(s)
# S02 Google Trends
for g in [x for x in J(f'{W1}/s02/spec.json') if any(x['csv'].endswith(f'-{h}.csv') for h in ('ai-marketing', 'radiopharmaceuticals', 'cross-border-b2b-payments', 'fraud-prevention', 'carbon-removal'))]:
    h = re.sub(r'^\d+-', '', os.path.basename(g['csv'])[:-4])
    B(h, type='pp_trends', section='Market opportunity', pill='SIGNAL', title=two(g['title']), csv=g['csv'], term=g['term'], expl=g['expl'], date=g['date'],
      note='With the help of Google Trends, we tracked how often people around the world googled this term over the last five years')
# S02 curve
src = open('/root/w/s11/s2prod/build.py').read().split('if __name__')[0]; G = {}; exec(src, G)
for a, k in G['M']:
    if a[0] in ('edtech', 'resale', 'defense-tech', 'ai-chip'):
        H, title, note, D, fmt, ll, big, unit, paras = a
        B(H, type='pp_curve', section='Market opportunity', title=title, note=note + SRC, points=[[l, float(v)] for l, v in D], labs=[fmt(v) for _, v in D],
          forecast=k.get('fc', 0), zero=k.get('zero', True), lastlines=ll, big=big, unit=unit, paras=paras)
d = [s for s in mkpp.slides('metal-additive-manufacturing') if s['type'] == 'pp_curve'][0]; d['labs'] = [f'${v:.1f}B' for _, v in d['points']]; out.append(d)
# S03 cagr
FAM = {'can': 'Yes, but ', 'fast': 'To grow this fast, ', 'room': 'To fill that room, ', 'ten': 'To get there, ', 'far': 'To go that far, ', 'still': 'Yes, but ',
       'real': 'To hit this growth, ', 'bigger': 'To get that big, ', 'decade': 'To get there, ', 'worth': 'To be worth that much, ', 'pace': 'To keep that pace, '}
D3 = {x['handle']: x for x in J(f'{W1}/s03/data.json') + J(f'{W}/data/s03.json')}
for h in OLD + list(NEW):
    d = D3[h]; B(h, type='pp_cagr', section='Market size', title=two(d['title']), size=d['size_usd_bn'], cagr=d['cagr_pct'], lead=FAM.get(d.get('family'), 'To grow this fast, '),
                 condition=d['growth_condition'], note=f"We compared forecasts from {d['sources_note']}, adjusted each one to our definition, and built a realistic range")
# S03 donut (layout A, Pierre to confirm)
COV = J('/root/w/s11/s3prod/cover.json')
def cname(s):
    s = s.lower().replace(' & ', ' and '); s = re.sub(r'\b(ai|smrs?|haleu|triso|ev|evs|us|r&d|gpu|gpus)\b', lambda m: m.group(0).upper().replace('SMRS', 'SMRs'), s); return s[0].upper() + s[1:]
for h in ('advanced-nuclear', 'ai-accounting', 'agritech'):  # varied shapes
    cats = [dict(name=cname(c['name']), p=round(c['p']), logos=[x for x in (logo(s) for s in c['logos']) if x][:3]) for c in COV[h]]
    m = nm(h); B(h, type='pp_donutv', variant='B', section='Market size', title=f'How is the {m} market split between its categories?', cats=cats,
                 note='We built these estimates from company revenue, filings and industry reports, then split the market by category. They are defensible but directional: orders of magnitude, not exact shares.' + SRC)
for h in NEW:
    d = [s for s in mkpp.slides(h) if s['type'] == 'pp_donut'][0]; d['type'] = 'pp_donutv'; d['variant'] = 'B'; out.append(d)
# S04 pains
P4 = J(f'{W1}/s04/spec.json'); P4.update(J(f'{W}/data/s04.json'))
for h in OLD + list(NEW):
    d = P4[h]; FIXA = {'Agencies': 'Marketing agencies', 'Oncologists': 'Cancer doctors', 'Hospitals': 'Hospital systems', 'Patients': 'Cancer patients', 'Regulators': 'Drug regulators', 'Importers': 'Goods importers', 'Exporters': 'Goods exporters', 'SMEs': 'Small businesses', 'Treasurers': 'Corporate treasurers'}
    B(h, type='pp_pains', section='Pain points', title=two(d['title']), auds=[FIXA.get(a, a) for a in d['auds']], pains=d['pains'],
                 note='We gathered customer complaints from reviews, forums and analyst reports, then checked how often and how strongly each problem comes up for each customer group.' + SRC + ' Bigger dots mean that group would pay more to fix it.')
# S05 tech, S06 value, S07 risks, S08 drivers, S10 grid, S11 killers, S12 winner: same builders as mkpp, other data folders
def from_mkpp(h, T):
    if h in NEW: return [s for s in mkpp.slides(h) if s['type'] == T]
    return [s for s in mkpp.slides_old(h) if s['type'] == T]
for T in ('pp_tech', 'pp_value', 'pp_risks', 'pp_drivers', 'pp_raises', 'pp_grid', 'pp_killers'):
    for h in OLD + list(NEW): out += from_mkpp(h, T)
# S11 survivors
SV = J(f'{S10}/surv/survivors_v2.json')
for h in ('ai-accounting', 'ai-recruiting', 'vibe-coding', 'ai-governance'):
    rows = [dict(lesson=r['lesson'], explanation=r['explanation'], failed_company=r['failed_company'], why_it_failed=r['why_it_failed'],
                 src=logo(re.sub(r'[^a-z0-9]', '', r['failed_company'].lower())) or logo(re.sub(r'[^a-z0-9]+', '-', r['failed_company'].lower()).strip('-')), ini=ini(r['failed_company'])) for r in SV if r['market'] == h]
    B(h, type='pp_survivors', section='Startup killers', title=f'What do {nm(h)} survivors do differently?', rows=rows,
      note=f'We looked at {nm(h)} companies that shut down, went bankrupt or hit a major setback, and at what the survivors do instead, from company statements, filings and the press.' + SRC)
out += from_mkpp('metal-additive-manufacturing', 'pp_survivors')
for h in OLD + list(NEW): out += from_mkpp(h, 'pp_winner')
RISKFIX = {'Novartis, Lilly, AstraZeneca and Bristol Myers Squibb dominate radioligand therapy and buy the best startups cheaply': 'Novartis, Lilly, AstraZeneca and BMS dominate radioligand therapy and buy the best startups cheaply'}
for s in out:
    if s['type'] == 'pp_risks':
        for e in s['events']: e['text'] = RISKFIX.get(e['text'], e['text'])
    if s['type'] == 'pp_grid': s['srcs'] = {k: logo(k) for row in s['cells'] for cell in row for k in cell}
slug = sys.argv[1]; os.makedirs(f'{ROOT}/decks/{slug}', exist_ok=True)
deck = dict(market='Product page slides', quarter='series review', label='', keep_together=sorted({nm(h) for h in OLD + list(NEW)}), slides=out)
yaml.safe_dump(deck, open(f'{ROOT}/decks/{slug}/deck.yaml', 'w'), sort_keys=False, allow_unicode=True, width=200)
print(len(out), 'slides')
