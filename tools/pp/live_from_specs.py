"""Product-page twins of a market of the 1-50 series: decks/<handle>/live.yaml (+ the S06 slide for extras.yaml) from the specs
that built the live slides (nmp-product-pages/w: s8 pains, s9/cmpm tech, s10/vc value, s10/mc risks, s10/gd drivers, s10/sk
killers, s10/ss winner), the live titles (slides/manifest.csv) and the logo tiles cut from the live images.

    python3 tools/pp/live_from_specs.py <handle> <folder of the live webp, named SS-NN.webp>

It never replaces looking: put each twin next to its live slide before going on (PROTOCOL.md, step 5). S02 (Google Trends) needs
Pierre's CSV, S09 is recomputed from the base (tools/pp/s09_from_base.py), S10 column and row names are read on the slide."""
import csv, json, subprocess, sys, yaml
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]; W = Path('/home/claude/nmp-product-pages/w'); H, IMG = sys.argv[1], Path(sys.argv[2])
T = {}
for r in csv.reader(open('/home/claude/nmp-product-pages/slides/manifest.csv')):
    if r[0] == H: T[f'{r[1]}-{r[2]}'] = r[6].rsplit(' (', 1)[0].split(': ', 1)[1]

def two(t):
    w = t.split(); k = min(range(1, len(w)), key=lambda i: abs(len(' '.join(w[:i])) - len(' '.join(w[i:])))); return ' '.join(w[:k]) + '\n' + ' '.join(w[k:])

def tiles(sec, prefix=None):
    out = subprocess.run(['python3', str(ROOT / 'tools/pp/live_tiles.py'), str(IMG / f'{sec}.webp'), f'assets/logos/pp_live/{H}', prefix or 's' + sec[:2]], capture_output=True, text=True, cwd=ROOT, check=True).stdout
    return yaml.safe_load(out) or []

def spec(rel):
    f = W / rel
    if not f.exists(): print('NO SPEC', rel); return None
    d = json.loads(f.read_text())
    if isinstance(d, dict) and H in d: d = d[H]
    return d

L = {}; f = ROOT / 'decks' / H / 'live.yaml'
if f.exists(): L = yaml.safe_load(f.read_text()) or {}
N = dict(pains=['We gathered customer complaints from reviews, forums, surveys and analyst reports on this market', 'Bigger dots mean that group would pay more to fix it, and all our sources are at the end of the report'],
         tech=['We checked each company’s website, filings and press releases, feature by feature', 'A pink mark means the feature is there, with all the sources at the end of the report'],
         value=['We placed each company by how its business model works, from pricing pages and filings', 'Positions are our reading, and you will find all the sources we used at the end of the report'],
         kill=['We used court filings and the press, and all the sources are included at the end of the report'],
         win=['We compared companies with the same business model on what matters most to customers', 'We used company reports and public records, and all our sources are at the end of the report'])
name = sys.argv[3] if len(sys.argv) > 3 else H.replace('-', ' ')
d = spec('s8/pain100_spec.json')
if d: L['ed058'] = dict(type='pp_pains', title=two(T['04-01']), auds=d['auds'], pains=[[t, v] for t, v in d['pains']], note=N['pains'])
d = spec(f's9/cmpm/{H}.json')
if d:
    tl = tiles('05-01'); n = len(d['companies']); order = sorted(range(n), key=lambda i: (-sum(f['values'][i] for f in d['features']), i))    # live order: most complete first
    L['ed099p'] = dict(title=two(T['05-01']), companies=[dict(name=d['companies'][i]['name'], src=tl[k]['src']) for k, i in enumerate(order)],
                       features=[dict(header=f['header'], values=[f['values'][i] for i in order]) for f in d['features']], note=N['tech'])
    assert len(tl) == n, ('S05 tiles', len(tl), n)
d = spec(f's10/mc/{H}.json')
if d: L['ed142p'] = dict(title=two(T['07-01']), events=[dict(odds=e['odds'], impact=e['impact'], text=e['text']) for e in sorted(d['events'], key=lambda e: -e['odds'])],
                         note=[f'We listed the events that could slow {name} down, from company news, regulators and analysts', 'Odds and impact are our own estimates, and all the sources we used are listed at the end of the report'])
d = spec(f's10/gd/{H}.json')
if d: L['ed148p'] = dict(title=two(T['08-01']), events=d['events'], note=[f'We kept the events we believe pushed {name} forward the most', 'Ratings are our estimates, with all the sources at the end of the report'])
L.setdefault('ed168p', {}).update(handle=H, title=two(T['09-01']), note=[f'We added up every equity round of {name} startups in our tracker over the last twelve months', 'by category of our market definition, and rounds with no public amount count as zero here'])
tl = tiles('10-01'); g = L.setdefault('ed171p', {}); g.update(title=two(T['10-01']), cells=[[[], [], []], [[], [], []], [[], [], []]], tiles=[dict(src=t['src'], x=t['x'], y=t['y']) for t in tl])
if 'cols' not in g: print('S10: write cols, rows and note of ed171p by hand, read on the live slide;', len(tl), 'tiles')
d = spec(f's10/sk/{H}.json')
if d:
    tl = tiles('11-01'); assert len(tl) == len(d['rows']), ('S11 tiles', len(tl), len(d['rows']))
    L['ed201'] = dict(type='pp_killers', mode=d.get('mode', 'dead'), title=two(T['11-01']), causes=d['causes'],
                      rows=[dict(name=r['name'], ending=r['ending'], start=r['start'], end=r['end'], causes=r['causes'], src=t['src'], ini=r['name'][0], slug=r['slug'], domain=r['domain']) for r, t in zip(d['rows'], tl)],
                      note=[f'We tracked the {name} startups that shut down, went bankrupt or were sold for little'] + N['kill'])
d = spec(f's10/ss/{H}.json')
if d:
    tl = tiles('12-01'); assert len(tl) == len(d['companies']), ('S12 tiles', len(tl), len(d['companies']))
    L['ed209p'] = dict(title=two(T['12-01']), companies=[dict(short=c['short'], src=t['src']) for c, t in zip(d['companies'], tl)], criteria=d['criteria'], note=N['win'])
f.write_text(yaml.dump(L, allow_unicode=True, sort_keys=False, width=1000)); print(f, list(L))
d = spec(f's10/vc/{H}.json')
if d:
    tl = sorted(tiles('06-01'), key=lambda t: t['x']); G = []
    for g_ in d['groups']:      # a group's tiles = the tiles nearest to its place on the map (x 0..1 left to right, y 0..1 bottom to top)
        gx, gy = 176 + g_['x'] * 608, 590 - g_['y'] * 330; k = len(g_['logos'])
        near = sorted(tl, key=lambda t: (t['x'] - gx) ** 2 + (t['y'] - gy) ** 2)[:k]
        for t in near: tl.remove(t)
        G.append(dict(name=g_['name'], x=g_['x'], y=g_['y'], logos=[dict(src=t['src']) for t in sorted(near, key=lambda t: t['x'])]))
    if tl: print('S06 TILES LEFT', len(tl))
    s06 = dict(after='ed104', link='TO WRITE: the phrase of ed104 that leads to how companies charge', slide=dict(id='pp_s06', type='pp_value', section='Value creation', title=two(T['06-01']), axes=d['axes'], groups=G, note=N['value']))
    xf = ROOT / 'decks' / H / 'extras.yaml'; X = [e for e in (yaml.safe_load(xf.read_text()) if xf.exists() else None) or [] if e['slide'].get('id') != 'pp_s06']
    xf.write_text(yaml.dump([s06] + X, allow_unicode=True, sort_keys=False, width=1000)); print('pp_s06 -> extras.yaml (write its link once ed104 is known: the import says so)')
