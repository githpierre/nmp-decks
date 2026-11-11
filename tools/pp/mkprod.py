"""Production decks of the product-page slides, markets 131-225 (Pierre, 11 Nov 2026: 'je te laisse procéder à tout').
usage: python3 mkprod.py <slug> <handle> [...]   -> decks/<slug>/deck.yaml + decks/<slug>/jobs.json (file name, section, title per slide)
Same builders as mkpp (S01, S03-S12), donut layout B (pp_donutv), title families rotated (titles.vary), all logo folders.
S02 comes from a separate pass (Google Trends CSVs from Pierre or a public curve)."""
import json, os, re, sys, yaml
sys.path.insert(0, os.path.dirname(__file__))
import mkpp, titles
from mkpp import logo, J, ROOT
W1, W = '/root/w/m101', '/root/w/m131'
mkpp.LOGO_DIRS += [f'{W1}/s01/logos', '/root/w/logos_all', '/root/w/s11/logos', '/root/w/s11/m/logos', '/root/w/s11/s3prod/logos', '/root/w/s11/s3prod/logos_fill',
                   f'{W1}/s05/newlogos', f'{W1}/s12/newlogos', f'{W1}/s12/newlogos2', f'{W}/logos_ok']
SHORT = {'workforce-management-software': 'workforce management', 'targeted-protein-degradation': 'protein degradation', 'post-quantum-cryptography': 'post-quantum crypto',
         'patient-engagement-software': 'patient engagement', 'non-human-identity-security': 'non-human identity', 'neuropsychiatric-therapeutics': 'neuropsychiatric drug',
         'metal-additive-manufacturing': 'metal 3D printing', 'managing-general-agent': 'MGA', 'generative-engine-optimization': 'GEO', 'employee-benefits-platform': 'employee benefits',
         'digital-identity-verification': 'identity verification', 'data-security-posture-management': 'DSPM', 'property-management-software': 'property management',
         'decentralized-exchange': 'DEX'}
_N0 = mkpp.NAME
def _name(h):
    n = SHORT.get(h) or _N0(h).strip()
    return re.sub(r'\s+', ' ', n)
mkpp.NAME = _name
_L0 = mkpp.logo
def _logo(slug):
    return _L0(slug) or f'MISSING:{slug}'
mkpp.logo = _logo
NAMETILE = {'pp_grid', 'pp_killers', 'pp_raises', 'pp_survivors'}   # these slides draw a name tile themselves
def ini_tile(slug):
    """initials tile in the charter for a missing logo (radar, donut, tech, value, winner)"""
    from PIL import Image, ImageDraw, ImageFont
    f = f'{ROOT}/assets/logos/pp/_ini_{slug}.png'
    if not os.path.exists(f):
        t = ''.join(w[0] for w in re.findall(r'[a-z0-9]+', slug)[:2]).upper()
        im = Image.new('RGB', (256, 256), (255, 255, 255)); d = ImageDraw.Draw(im)
        F = ImageFont.truetype(f'{ROOT}/assets/fonts/Lexend-SemiBold.ttf', 110); w = d.textlength(t, font=F)
        d.text(((256 - w) / 2, 58), t, font=F, fill=(6, 42, 60)); im.save(f)
    return f'../../assets/logos/pp/_ini_{slug}.png'
MISSING = {}
def fix_missing(o, typ, h):
    if isinstance(o, dict): return {k: fix_missing(v, typ, h) for k, v in o.items()}
    if isinstance(o, list): return [fix_missing(v, typ, h) for v in o]
    if isinstance(o, str) and o.startswith('MISSING:'):
        MISSING.setdefault(o[8:], set()).add((h, typ))
        return '' if typ in NAMETILE else ini_tile(o[8:])
    return o
FILE = {'pp_radar': '01-01', 'pp_trends': '02-01', 'pp_curve': '02-02', 'pp_cagr': '03-01', 'pp_donutv': '03-02', 'pp_pains': '04-01', 'pp_tech': '05-01',
        'pp_value': '06-01', 'pp_risks': '07-01', 'pp_drivers': '08-01', 'pp_raises': '09-02', 'pp_grid': '10-01', 'pp_killers': '11-01', 'pp_survivors': '11-02', 'pp_winner': '12-01'}
def market(h):
    out = []
    for s in mkpp.slides(h):
        if s['type'] == 'pp_curve': continue
        if s['type'] == 'pp_cagr':
            src = s['note'][0].replace('We compared forecasts from ', '')
            L2 = ['We adjusted each one to our market definition', 'We adjusted each one to our own definition of the market', 'We adjusted them to our market definition and built a range',
                  'We adjusted each one to our own definition of the market and built a realistic range']
            W = mkpp._F.getlength; l1 = f'We compared forecasts from {src}'
            C = [mkpp.balance_note([l1, a + sf]) for a in L2 for sf in mkpp.SUFS]
            s['note'] = min(C, key=lambda n: abs(W(n[0]) - W(n[1])) / max(W(n[0]), W(n[1])))
        if s['type'] == 'pp_donut':
            s['type'] = 'pp_donutv'; s['variant'] = 'B'
        s['_h'] = h; out.append(s)
    return out
if __name__ == '__main__':
    slug, hs = sys.argv[1], sys.argv[2:]
    S = [x for h in hs for x in market(h)]
    for x in S:
        if x['type'] == 'pp_grid': x['srcs'] = {k: mkpp.logo(k) for row in x['cells'] for cell in row for k in cell}
    S = [fix_missing(x, x['type'], x['_h']) for x in S]
    titles.vary(S, mkpp.NAME)
    jobs = []
    for s in S:
        t = s['title'] if isinstance(s['title'], str) else ' '.join(s['title'])
        jobs.append(dict(handle=s['_h'], type=s['type'], name=f"{s['_h']}-slide-{FILE[s['type']]}.webp", title=re.sub(r'\s+', ' ', t).strip()))
        s.pop('_h')
    os.makedirs(f'{ROOT}/decks/{slug}', exist_ok=True)
    yaml.safe_dump(dict(market='Product page slides', quarter='production', label='', keep_together=[mkpp.NAME(h) for h in hs], slides=S),
                   open(f'{ROOT}/decks/{slug}/deck.yaml', 'w'), sort_keys=False, allow_unicode=True, width=200)
    json.dump(jobs, open(f'{ROOT}/decks/{slug}/jobs.json', 'w'), indent=0)
    json.dump({k: sorted(v) for k, v in MISSING.items()}, open(f'{ROOT}/decks/{slug}/missing_logos.json', 'w'), indent=0)
    print(len(S), 'slides', len(MISSING), 'missing logos')
