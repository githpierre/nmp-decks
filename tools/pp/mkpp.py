"""Product-page slides (S01-S12) as an HTML deck: m131 JSON data -> decks/<slug>/deck.yaml.
usage: python3 mkpp.py <slug> <handle> [<handle> ...]"""
import json, os, re, shutil, sys, yaml
import pandas as pd
ROOT = '/home/claude/nmp-decks'; W = '/root/w/m131'; S10 = '/root/w/s10'
LOGO_DIRS = [f'{W}/logos', '/root/w/s9/logos', f'{ROOT}/assets/logos']
NAME0 = {'low-carbon-cement': 'low-carbon cement', 'metal-additive-manufacturing': 'metal 3D printing'}
LABEL0 = {'low-carbon-cement': 'LOW-CARBON CEMENT', 'metal-additive-manufacturing': 'METAL 3D PRINTING'}
SRC = ' All the sources are included at the end of the report.'
os.makedirs(f'{ROOT}/assets/logos/pp', exist_ok=True)
import csv as _csv
_MK = {r['handle']: r for r in _csv.DictReader(open('/root/w/nmp_slide_kit/markets_225.csv'))}
def NAME(h):
    for f in (f'{W}/data/mc_{h}.json', f'/root/w/m101/s07/mc/{h}.json', f'{S10}/gd/{h}.json'):
        if os.path.exists(f): return json.load(open(f))['name']
    return _MK[h]['nom_market'].replace(' market', '')
def LABEL(h): return ' '.join(''.join(w.split()) for w in re.split(r'\s{2,}', _MK[h]['market_name_for_slide'].strip()))
slides_old = None

_BL = {}
def blank(f):
    """a logo that is almost one flat colour (white on white, empty canvas) counts as missing (11 Nov: blank tiles on the pilot)"""
    if f not in _BL:
        from PIL import Image, ImageStat
        im = Image.open(f).convert('RGBA'); bg = Image.new('RGBA', im.size, (255, 255, 255, 255)); bg.alpha_composite(im)
        _BL[f] = max(ImageStat.Stat(bg.convert('L')).stddev[0], 0) < 6
    return _BL[f]
def logo(slug):
    """copy the logo into assets/logos/pp and return its path from the deck, or None"""
    for d in LOGO_DIRS:
        f = f'{d}/{slug}.png'
        if os.path.exists(f) and not blank(f):
            dst = f'{ROOT}/assets/logos/pp/{slug}.png'
            if not os.path.exists(dst): shutil.copy(f, dst)
            return f'../../assets/logos/pp/{slug}.png'
    return ''
def ini(name): return ''.join(w[0] for w in re.findall(r'[A-Za-z0-9]+', name)[:2]).upper()
def J(p): return json.load(open(p))
from PIL import ImageFont as _IF
_F = _IF.truetype(os.path.join(ROOT, 'assets/fonts/Lexend-Regular.ttf'), 100)
SUFS = [', and you will find all the sources we used at the end of the report', ', and all the sources we used are listed at the end of the report', ', and all the sources are included at the end of the report', ', and all our sources are listed at the end of the report',
        ', and all our sources are at the end of the report', ', with all the sources at the end of the report']
def balance_note(note):
    """Notes workshop: 2 lines within 12% of each other. Picks the sources wording (and, if needed, a shorter first line) that balances best."""
    if not isinstance(note, list) or len(note) != 2: return note
    l1, l2 = note; core = None
    for sf in SUFS:
        if l2.endswith(sf): core = l2[:-len(sf)]
    if core is None: return note
    W = _F.getlength
    l1s = [x.rstrip(' ,') for x in [l1] + ([l1.split(', from ')[0]] if ', from ' in l1 else []) + ([l1.split(' from ')[0]] if ' from ' in l1 and len(l1.split(' from ')[0]) > 40 else [])]
    cores = {core, core.replace(' of the market', ''), core.replace(' our own ', ' our '), core.replace(' our own ', ' our ').replace(' of the market', '')}
    best = min(((abs(W(a) - W(c + sf)) / max(W(a), W(c + sf)), a, c + sf) for a in l1s for c in cores for sf in SUFS), key=lambda t: t[0])
    return [best[1], best[2]]

def N2(note):
    p = [x.strip().rstrip('.') for x in note.split('. ') if x.strip()]
    if len(p) == 1: return [p[0], 'We checked each point against its source, and all the sources are included at the end of the report']
    return [p[0], p[1][0].upper() + p[1][1:] + ', and all the sources are included at the end of the report']

def NGRID(note):
    """Market grid note in 2 lines: who is in and where they sit / who is left out, plus sources."""
    p = [x.strip().rstrip('.') for x in note.split('. ') if x.strip()]
    out = [x for x in p if x.startswith('We left out')]
    l2 = (out[0] if out else 'We left out listed companies and incumbents') + ', and all the sources are included at the end of the report'
    L1 = ['We placed private pure players by their main product and their stage, from funding news, company websites and the press',
          'We placed private pure players by main product and stage, from funding news, company websites and the press',
          'We placed private pure players by main product and stage, from funding news and the press',
          'We placed private pure players by their main product and their stage']
    return [min(L1, key=lambda a: abs(_F.getlength(a) - _F.getlength(l2))), l2]

def two(t): return t if isinstance(t, str) else '\n'.join(t)

def slides(h):
    nm, lab = NAME(h), LABEL(h); out = []
    base = dict(label=lab)
    NEWD = h in J(f'{W}/data/s01.json')
    # S01 radar
    d = J(f'{W}/data/s01.json').get(h) or J('/root/w/m131/data/s01.json')['low-carbon-cement']
    sl = dict(type='pp_radar', pill='MARKET MAP', label=lab, title=two(d['title']), caption=d['caption'], inside=[logo(x) for x in d['inside']])
    for k in ('TL', 'TR', 'BL', 'BR'): sl[k] = dict(src=logo(d[k][0]), name=d[k][1], text=d[k][2])
    if NEWD: out.append(sl)
    # S02 curve (only where a series exists)
    if h == 'metal-additive-manufacturing':
        out.append(dict(base, type='pp_curve', section='Market opportunity', title='Spending on 3D printing keeps climbing, year after year',
            note=['We used the global additive manufacturing revenue of the yearly Wohlers Report', 'The 2026 point is our own forecast, and all the sources are included at the end of the report'],
            points=[['2020', 12.8], ['2021', 15.2], ['2022', 18.0], ['2023', 20.0], ['2024', 21.9], ['2025', 24.2], ['2026', 26.8]], forecast=1, fmt='${}B',
            lastlines=['spent on 3D printing', 'worldwide in 2026'], big='1.9x', unit=' in 5 years',
            paras=['Global 3D printing revenue grew from $12.8B in 2020 to $24.2B in 2025.', 'Printing services grew fastest, up 15.5% in 2025.', 'Metal printing alone reached about $6.3B in 2025.']))
    # S03 cagr
    d = ([x for x in J(f'{W}/data/s03.json') if x['handle'] == h] or [None])[0]
    if d: out.append(dict(base, type='pp_cagr', section='Market size', title=two(d['title']), size=d['size_usd_bn'], cagr=d['cagr_pct'], lead={'room':'To fill that room, ','ten':'To get there, ','bigger':'To get that big, '}.get(d.get('family'),'To grow this fast, '), condition=d['growth_condition'],
        note=[f"We compared forecasts from {d['sources_note']}", 'We adjusted each forecast to our own definition of the market and built a realistic range, and all the sources are included at the end of the report']))
    # S03 donut
    d = J(f'{W}/data/donut.json').get(h)
    if d: out.append(dict(base, type='pp_donut', section='Market size', title=f"How is the {nm} market split between its categories?",
        cats=[dict(name=a, p=b, logos=[x for x in (logo(s) for s in c) if x]) for a, b, c in d['cats']],
        note=['We built these estimates from company revenue, company filings and industry reports on the market', 'They give orders of magnitude, not exact shares, and all the sources are included at the end of the report']))
    # S04 pains
    d = J(f'{W}/data/s04.json').get(h)
    if d: out.append(dict(base, type='pp_pains', section='Pain points', title=two(d['title']), auds=d['auds'], pains=d['pains'],
        note=['We gathered customer complaints from reviews, forums, surveys and analyst reports on this market', 'Bigger dots mean that group would pay more to fix it, and all the sources are included at the end of the report']))
    # S05 tech
    d = J(f'{W}/data/s05_{h}.json') if os.path.exists(f'{W}/data/s05_{h}.json') else J(f'/root/w/m101/s05/data/{h}.json')
    out.append(dict(base, type='pp_tech', section='Tech and infra', title=two(d['title']), companies=[dict(name=c['name'], src=logo(c['slug'])) for c in d['companies']],
        features=[dict(header=f['header'], values=f['values']) for f in d['features']],
        note=["We checked each company's website, filings and press releases, feature by feature", 'A pink mark means the feature is there, and all the sources are included at the end of the report']))
    # S06 value
    d = J(f'{S10}/vc/{h}.json')
    out.append(dict(base, type='pp_value', section='Value creation', title=two(d['title']), axes=d['axes'],
        groups=[dict(name=g['name'], x=g['x'], y=g['y'], logos=[dict(src=logo(l['slug']))for l in g['logos']]) for g in d['groups']],
        note=['We placed each company by how its business model works, from pricing pages and filings', 'Positions are our own reading, and all the sources are included at the end of the report']))
    # S07 risks
    d = J(f'{W}/data/mc_{h}.json') if os.path.exists(f'{W}/data/mc_{h}.json') else J(f'/root/w/m101/s07/mc/{h}.json')
    out.append(dict(base, type='pp_risks', section='Market challenges', title=f'What could go wrong for {nm}?' if h == 'low-carbon-cement' else f'What are the biggest threats to the {nm} market?', events=d['events'],
        note=[f'We listed the events that could slow {nm} down, from company news, regulators and analysts', 'Odds and impact are our own estimates, and all the sources are included at the end of the report']))
    # S08 drivers
    d = J(f'{S10}/gd/{h}.json')
    out.append(dict(base, type='pp_drivers', section='Growth drivers', title=f'What pushed the {nm} market forward, year after year?', events=d['events'],
        note=[f'We kept the events we believe pushed {nm} forward the most, from company news and filings', 'Ratings are our own estimates, and all the sources are included at the end of the report']))
    # S09-02 raises (from the startups base)
    B = '/home/claude/nmp-seo/data/startups'
    c = pd.read_csv(f'{B}/companies.csv'); mk = pd.read_csv(f'{B}/markets.csv'); r = pd.read_csv(f'{B}/rounds.csv')
    r['amount_usd'] = pd.to_numeric(r.amount_usd, errors='coerce'); r['d'] = pd.to_datetime(r.date, format='mixed', errors='coerce')
    ids = set(mk[mk.market_handle == h].company_id) & set(c[c.company_type == 'Startup'].company_id)
    x = r[r.company_id.isin(ids) & (r.is_equity == True) & ~r.round_type.isin({'IPO', 'Post-IPO', 'Secondary', 'Debt', 'Grant'}) & (r.d >= '2024-11-11') & (r.aggregate != True)]
    x = x.sort_values('amount_usd', ascending=False).drop_duplicates('company_id').head(6)
    CN = c.set_index('company_id')['name']; R = []
    alias = {'divergent-technologies': 'divergent'}
    for _, y in x.iterrows():
        n = CN[y.company_id]
        R.append(dict(name={'Divergent Technologies': 'Divergent'}.get(n, n), amt=float(y.amount_usd), src=logo(alias.get(y.company_id, y.company_id)) or logo(re.sub('[^a-z0-9]', '', n.lower())),
            stage={'Series D+': 'Late stage', 'Other': 'Round', 'Unknown': 'Round'}.get(y.round_type, y.round_type), date=y.d.strftime('%b %Y')))
    out.append(dict(base, type='pp_raises', section='Investor bets', title=f'Which {nm} startups got the biggest checks lately?', rounds=R,
        note=[f'We listed the biggest equity rounds raised by {nm} startups in recent years', 'We used company announcements, investor releases and the press, and all the sources are included at the end of the report']))
    # S10 grid
    d = J(f'{S10}/grid/{h}.json')
    import pandas as _pd
    _r = _pd.read_csv('/home/claude/nmp-seo/data/startups/rounds.csv'); _r['amount_usd'] = _pd.to_numeric(_r.amount_usd, errors='coerce')
    _t = _r[_r.is_equity == True].groupby('company_id').amount_usd.sum().to_dict()
    _al = {'sublime-systems': 'sublime-systems', 'carboncure': 'carboncure-technologies', 'divergent': 'divergent-technologies', 'seurat': 'seurat-technologies', 'cura': 'cura', 'co-reactive': 'reactive'}
    g = dict(base, type='pp_grid', weight={k: float(_t.get(_al.get(k, k), 0) or 0) for row in d['cells'] for cell in row for k in cell}, section=lab, title=d['title'], handle=h, cols=d['cols'], rows=d['rows'], cells=d['cells'], note=NGRID(d['note']) if isinstance(d['note'], str) else d['note'])
    out.append(g)
    # S11 killers
    d = J(f'{S10}/sk/{h}.json')
    for row in d['rows']: row['src'] = logo(row['slug']); row['ini'] = ini(row['name'])
    if d['mode'] == 'dead':
        out.append(dict(base, type='pp_killers', mode='dead', section='Startup killers', title=f'What broke these {nm} startups, and how did they end?', causes=d['causes'], rows=d['rows'],
            note=[f'We tracked the {nm} startups that shut down, went bankrupt or were sold for little', 'We used court filings and the press, and all the sources are included at the end of the report']))
    else:
        out.append(dict(base, type='pp_killers', mode='warning', section='Startup killers', title=f'Which {nm} companies have shown warning signs lately?', signs=d['signs'], rows=d['rows'],
            note=[f'We looked for warning signs among well-known {nm} companies, from layoffs to lawsuits', 'We used company filings and the press, and all the sources are included at the end of the report']))
    sv = J(f'{W}/data/surv.json').get(h)
    if sv:
        for row in sv: row['src'] = logo(row['slug']); row['ini'] = ini(row['failed_company'])
        out.append(dict(base, type='pp_survivors', section='Startup killers', title=f'What do {nm} survivors do differently?', rows=sv,
            note=[f'We compared {nm} companies that failed or hit a major setback with the ones that survived', 'We used company statements and the press, and all the sources are included at the end of the report']))
    # S12 winner
    d = J(f'{S10}/ss/{h}.json')
    out.append(dict(base, type='pp_winner', section='Startup strategies', title=two(d['title']), companies=[dict(short=x['short'], src=logo(x['slug'])) for x in d['companies']], criteria=d['criteria'],
        note=['We compared companies with the same business model on what matters most to customers', 'We used company reports and public records, and all the sources are included at the end of the report']))
    # grid tiles need logos
    for _s in out:
        if isinstance(_s.get('note'), list): _s['note'] = balance_note(_s['note'])
    return out
slides_old = slides

if __name__ == '__main__':
    slug, hs = sys.argv[1], sys.argv[2:]
    S = [x for h in hs for x in slides(h)]
    for s in S:
        if s['type'] == 'pp_grid':
            s['srcs'] = {k: logo(k) for row in s['cells'] for cell in row for k in cell}
    os.makedirs(f'{ROOT}/decks/{slug}', exist_ok=True)
    deck = dict(market='Product page slides', quarter='prototypes', label='', keep_together=[NAME(h) for h in hs], slides=S)
    yaml.safe_dump(deck, open(f'{ROOT}/decks/{slug}/deck.yaml', 'w'), sort_keys=False, allow_unicode=True, width=200)
    print(len(S), 'slides')
