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
def N2(note):
    """Workshop rule: 2 lines, one idea per line, no dots. Second sentence (if any) joins the sources line."""
    p = [x.strip().rstrip('.') for x in note.split('. ') if x.strip()]
    if len(p) == 1: return [p[0], 'We checked each point against its source, and all the sources are included at the end of the report']
    return [p[0], p[1][0].upper() + p[1][1:] + ', and all the sources are included at the end of the report']

out = []
def B(h, **k): d = dict(label=label(h), _h=h); d.update({a: b for a, b in k.items() if b is not None}); out.append(d)

# S01 radar
S1 = {m['handle']: m for m in J(f'{W1}/s01/spec.json')['markets']}; N1 = J(f'{W}/data/s01.json')
for h in OLD + list(NEW):
    if h in N1:
        d = N1[h]; s = dict(type='pp_radar', pill='MARKET MAP', label=label(h), title=two(d['title']), caption=d['caption'], inside=[logo(x) for x in d['inside']])
        for k in ('TL', 'TR', 'BL', 'BR'): s[k] = dict(src=logo(d[k][0]), name=d[k][1], text=d[k][2])
    else:
        d = S1[h]; s = dict(type='pp_radar', pill='MARKET MAP', label=label(h), title=two(d['title']), caption=d['caption'], inside=[logo(x) for x in d['inside']])
        for k in ('TL', 'TR', 'BL', 'BR'): s[k] = dict(src=logo(d[k]['logo']), name=d[k]['name'], text=d[k]['text'])
    out.append(s)
# S02 Google Trends
for g in [x for x in J(f'{W1}/s02/spec.json') if any(x['csv'].endswith(f'-{h}.csv') for h in ('ai-marketing', 'radiopharmaceuticals', 'cross-border-b2b-payments', 'fraud-prevention', 'carbon-removal'))]:
    h = re.sub(r'^\d+-', '', os.path.basename(g['csv'])[:-4])
    B(h, type='pp_trends', section='Market opportunity', pill='SIGNAL', title=two(g['title']), csv=g['csv'], term=g['term'], expl=g['expl'], date=g['date'],
      note=['We tracked how often people around the world googled this term on Google Trends', 'We used the last five years of searches, and all the sources are included at the end of the report'])
# S02 curve (markets 131-225 with a strong public series)
CUR = [
 ('prediction-markets', 'Kalshi trades nine times more than it did in February', 'We used the monthly trading volume of Kalshi, the largest US prediction market. We took it from DeFi Rate and pm.wiki.',
  [['Feb', 10.4], ['Mar', 12.4], ['Apr', 14.8], ['May', 17.9], ['Sep', 60.9], ['Oct', 98.2]], [1, 2, 3, 4, 8, 9], '$%.1fB', ['traded on Kalshi', 'in October 2026'], '9.4x', ' in 8 months',
  ['Kalshi traded $98.2B in October 2026, up 61% in a single month.', 'Combo bets made up at least $66.9B of it.', 'All US prediction markets together reached $120.7B in October.']),
 ('buy-now-pay-later', 'Shoppers keep paying more with Affirm, year after year', 'We used the yearly gross merchandise volume Affirm reports for its fiscal years ending in June. The 2027 point is the company\'s own outlook.',
  [['FY2022', 15.5], ['FY2023', 20.2], ['FY2024', 26.6], ['FY2025', 36.7], ['FY2026', 50.2], ['FY2027', 64.0]], None, '$%.1fB', ['paid with Affirm', 'in fiscal 2027'], '3.2x', ' in 4 years',
  ['Affirm handled $50.2B of purchases in its fiscal year 2026.', 'Its volume grew 30% or more for 11 quarters in a row.', 'It expects at least $64B in fiscal 2027.']),
 ('electric-two-wheeler', 'More Indians ride electric scooters every year', 'We used yearly electric two-wheeler registrations in India from the Vahan portal. Fiscal years end in March.',
  [['FY2022', 0.25], ['FY2023', 0.73], ['FY2024', 0.95], ['FY2025', 1.15], ['FY2026', 1.40]], None, '%.2fM', ['electric two-wheelers', 'sold in India in FY2026'], '5.6x', ' in 4 years',
  ['India sold 1.40 million electric two-wheelers in fiscal 2026, up 22%.', 'They now make up 6.5% of all two-wheeler sales.', 'TVS took the lead from Ola Electric.']),
]
for h, title, note, pts, xs, fmt, ll, big, unit, paras in CUR:
    fc = 1 if pts[-1][0] == 'FY2027' else 0
    B(h, type='pp_curve', section='Market opportunity', title=title, note=N2(note), points=pts, labs=[fmt % v for _, v in pts], forecast=fc, zero=True,
      xs=[x / xs[-1] for x in xs] if xs else None, lastlines=ll, big=big, unit=unit, paras=paras)
d = [s for s in mkpp.slides('metal-additive-manufacturing') if s['type'] == 'pp_curve'][0]; d['labs'] = [f'${v:.1f}B' for _, v in d['points']]; out.append(d)
# S03 cagr
FAM = {'can': 'Yes, but ', 'fast': 'To grow this fast, ', 'room': 'To fill that room, ', 'ten': 'To get there, ', 'far': 'To go that far, ', 'still': 'Yes, but ',
       'real': 'To hit this growth, ', 'bigger': 'To get that big, ', 'decade': 'To get there, ', 'worth': 'To be worth that much, ', 'pace': 'To keep that pace, '}
D3 = {x['handle']: x for x in J(f'{W1}/s03/data.json') + J(f'{W}/data/s03.json')}
for h in OLD + list(NEW):
    d = D3[h]; B(h, type='pp_cagr', section='Market size', title=two(d['title']), size=d['size_usd_bn'], cagr=d['cagr_pct'], lead=FAM.get(d.get('family'), 'To grow this fast, '),
                 condition=d['growth_condition'], note=[f"We compared forecasts from {d['sources_note']}", 'We adjusted each forecast to our own definition of the market and built a realistic range, and all the sources are included at the end of the report'])
# S03 donut, layout B (Pierre, 11 Nov), markets 131-225 only
DN = J(f'{W}/data/donut.json')
for h in ('buy-now-pay-later', 'prediction-markets', 'electric-two-wheeler', 'low-carbon-cement', 'metal-additive-manufacturing'):
    d = DN[h]; miss = [x for c in d['cats'] for x in c[2] if not logo(x)]
    if miss: print('MISSING LOGOS', h, miss)
    B(h, type='pp_donutv', variant='B', section='Market size', title=d.get('t') or f"How is the {d['m']} market split between its categories?",
      cats=[dict(name=a, p=b, logos=[logo(x) for x in c if logo(x)]) for a, b, c in d['cats']],
      note=['We built these estimates from company revenue, company filings and industry reports on the market', 'They give orders of magnitude, not exact shares, and all the sources are included at the end of the report'])
# S04 pains
P4 = J(f'{W1}/s04/spec.json'); P4.update(J(f'{W}/data/s04.json'))
for h in OLD + list(NEW):
    d = P4[h]; FIXA = {'Agencies': 'Marketing agencies', 'Oncologists': 'Cancer doctors', 'Hospitals': 'Hospital systems', 'Patients': 'Cancer patients', 'Regulators': 'Drug regulators', 'Importers': 'Goods importers', 'Exporters': 'Goods exporters', 'SMEs': 'Small businesses', 'Treasurers': 'Corporate treasurers'}
    B(h, type='pp_pains', section='Pain points', title=two(d['title']), auds=[FIXA.get(a, a) for a in d['auds']], pains=d['pains'],
                 note=['We gathered customer complaints from reviews, forums, surveys and analyst reports on this market', 'Bigger dots mean that group would pay more to fix it, and all the sources are included at the end of the report'])
# S05 tech, S06 value, S07 risks, S08 drivers, S10 grid, S11 killers, S12 winner: same builders as mkpp, other data folders
def from_mkpp(h, T):
    L = [s for s in mkpp.slides(h) if s['type'] == T]
    for s in L: s['_h'] = h
    return L
for T in ('pp_tech', 'pp_value', 'pp_risks', 'pp_drivers', 'pp_raises', 'pp_grid', 'pp_killers'):
    for h in OLD + list(NEW): out += from_mkpp(h, T)
# S11 survivors
SV = J(f'{S10}/surv/survivors_v2.json')
for h in ('ai-accounting', 'ai-recruiting', 'vibe-coding', 'ai-governance'):
    rows = [dict(lesson=r['lesson'], explanation=r['explanation'], failed_company=r['failed_company'], why_it_failed=r['why_it_failed'],
                 src=logo(re.sub(r'[^a-z0-9]', '', r['failed_company'].lower())) or logo(re.sub(r'[^a-z0-9]+', '-', r['failed_company'].lower()).strip('-')), ini=ini(r['failed_company'])) for r in SV if r['market'] == h]
    B(h, type='pp_survivors', section='Startup killers', title=f'What do {nm(h)} survivors do differently?', rows=rows,
      note=[f'We compared {nm(h)} companies that failed or hit a major setback with the ones that survived', 'We used company statements and the press, and all the sources are included at the end of the report'])
out += from_mkpp('metal-additive-manufacturing', 'pp_survivors')
for h in OLD + list(NEW): out += from_mkpp(h, 'pp_winner')
RISKFIX = {'Novartis, Lilly, AstraZeneca and Bristol Myers Squibb dominate radioligand therapy and buy the best startups cheaply': 'Novartis, Lilly, AstraZeneca and BMS dominate radioligand therapy and buy the best startups cheaply'}
import titles; titles.vary(out, nm)
for s in out:
    s.pop('_h', None)
    if isinstance(s.get('note'), list): s['note'] = mkpp.balance_note(s['note'])
    if s['type'] == 'pp_risks':
        for e in s['events']: e['text'] = RISKFIX.get(e['text'], e['text'])
    if s['type'] == 'pp_grid': s['srcs'] = {k: logo(k) for row in s['cells'] for cell in row for k in cell}
slug = sys.argv[1]; os.makedirs(f'{ROOT}/decks/{slug}', exist_ok=True)
deck = dict(market='Product page slides', quarter='series review', label='', keep_together=sorted({nm(h) for h in OLD + list(NEW)}), slides=out)
yaml.safe_dump(deck, open(f'{ROOT}/decks/{slug}/deck.yaml', 'w'), sort_keys=False, allow_unicode=True, width=200)
print(len(out), 'slides')
