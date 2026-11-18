"""Product-page twins read from the LIVE slides (point 4, Pierre 18 Nov 2026): radar S01 (ed007p), Google Trends S02
(ed039p), market size S03 (ed052p) and market grid S10 (ed171p) written into decks/<handle>/live.yaml, so nobody types
them by hand. Texts come from OCR of the live 2400x1680 webp (tesseract, word boxes), logos from live_tiles.py.

    python3 tools/pp/twins_auto.py <handle> <folder of the live webp named SS-NN.webp> [--check]

The live slides of all 225 markets share the V1 layout: the slide sits at (80, 16), scale 2240/960 (page_lift), so the
zones below are in deck pixels (960 x 672). --check prints the result without writing. ALWAYS put each twin next to its
live slide after (PROTOCOL step 5): OCR can misread a word (« AG1 » read « AG31 »), the look catches it.
Run it AFTER live_from_specs.py (which writes the other twins). Trends: the CSV term comes from the slide caption; the
CSV itself is Pierre's (assets/trends/<handle>/<term>.csv)."""
import re, subprocess, sys, yaml
from pathlib import Path
from PIL import Image
ROOT = Path(__file__).resolve().parents[2]
H, IMG = sys.argv[1], Path(sys.argv[2]); CHECK = '--check' in sys.argv
OX, OY, SC = 80, 16, 2240 / 960
REF = yaml.safe_load((ROOT / 'decks/advanced-nuclear/live.yaml').read_text())   # shapes and fixed fields of each twin type


def words(f):
    im = Image.open(f).convert('RGBA'); bg = Image.new('RGBA', im.size, (6, 42, 60, 255)); bg.alpha_composite(im)
    g = bg.convert('L').point(lambda v: 255 - v); tmp = Path('/tmp/twins_ocr.png'); g.save(tmp)
    out = subprocess.run(['tesseract', str(tmp), '-', '--psm', '3', 'tsv'], capture_output=True, text=True).stdout.splitlines()
    W = []
    for l in out[1:]:
        c = l.split('\t')
        if len(c) < 12 or not c[11].strip() or float(c[10]) < 0: continue
        x, y, w, h = (int(c[i]) for i in (6, 7, 8, 9))
        W.append(dict(t=c[11], x=(x - OX) / SC, y=(y - OY) / SC, x2=(x + w - OX) / SC, y2=(y + h - OY) / SC, key=(c[2], c[3], c[4])))
    return W


def zone(W, x0, y0, x1, y1):
    """words whose centre is in the zone, as lines (tesseract block/par/line), top to bottom"""
    sel = [w for w in W if x0 <= (w['x'] + w['x2']) / 2 <= x1 and y0 <= (w['y'] + w['y2']) / 2 <= y1]
    L = {}
    for w in sel: L.setdefault(w['key'], []).append(w)
    lines = sorted(L.values(), key=lambda ws: (min(w['y'] for w in ws), min(w['x'] for w in ws)))
    return [' '.join(w['t'] for w in sorted(ws, key=lambda w: w['x'])) for ws in lines]


def text(W, *z): return re.sub(r'\s+', ' ', ' '.join(zone(W, *z))).strip()


def crop(f, x0, y0, x1, y1, psm=6, lines=False):
    """OCR of one deck zone on its own (upscaled): sees short labels the full-page pass drops (« $29B », « Multi-system / tools »)"""
    im = Image.open(f).convert('RGBA'); bg = Image.new('RGBA', im.size, (6, 42, 60, 255)); bg.alpha_composite(im)
    b = tuple(int(v) for v in (OX + x0 * SC, OY + y0 * SC, OX + x1 * SC, OY + y1 * SC))
    g = bg.crop(b).convert('L').point(lambda v: 255 - v); g = g.resize((g.width * 2, g.height * 2)); tmp = Path('/tmp/twins_crop.png'); g.save(tmp)
    o = subprocess.run(['tesseract', str(tmp), '-', '--psm', str(psm)], capture_output=True, text=True).stdout
    if lines: return [l.strip(' .|:;') for l in o.splitlines() if re.search(r'[A-Za-z]{3}', l)]
    return re.sub(r'\s+', ' ', o).strip(' .|:;')
def title(W): return '\n'.join(zone(W, 60, 55, 900, 160)[:2])
def notes(W): return [l for l in zone(W, 0, 595, 600, 645) if len(l) > 25]


def split_name(t):
    """« Function Health runs over 100 lab tests… » -> (Function Health, runs over…): the name is the capitalised head"""
    w = t.split(); i = 0
    while i < len(w) and (w[i][:1].isupper() or w[i][:1].isdigit() or w[i] in ('&', 'of', 'de')): i += 1
    return ' '.join(w[:i]), ' '.join(w[i:])


def tiles(sec, prefix):
    out = subprocess.run(['python3', str(ROOT / 'tools/pp/live_tiles.py'), str(IMG / f'{sec}.webp'), f'assets/logos/pp_live/{H}', prefix],
                         capture_output=True, text=True, cwd=ROOT, check=True).stdout
    return yaml.safe_load(out) or []


T = {}
# S01 radar: 4 corner texts, captions; the 12 tiles: the one nearest each corner text is that corner's logo
if (IMG / '01-01.webp').exists():
    W = words(IMG / '01-01.webp'); tl = tiles('01-01', 's01')
    Z = dict(TL=(20, 235, 320, 330), TR=(650, 235, 945, 330), BL=(20, 445, 340, 540), BR=(630, 445, 945, 540))
    r = {k: v for k, v in REF['ed007p'].items() if k in ('type',)}; r['title'] = title(W); used = set()
    for c, z in Z.items():
        name, body = split_name(text(W, *z))
        cx = z[2] if c in ('TL', 'BL') else z[0]; cy = (z[1] + z[3]) / 2
        t = min((t for t in tl if t['src'] not in used), key=lambda t: (t['x'] - cx) ** 2 + (t['y'] - cy) ** 2); used.add(t['src'])
        r[c] = dict(name=name, src=t['src'], text=body)
    r['caption'] = notes(W)
    r['inside'] = [t['src'] for t in tl if t['src'] not in used]
    r['inside_xy'] = [dict(src=t['src'], x=t['x'], y=t['y']) for t in tl if t['src'] not in used]
    T['ed007p'] = r
# S02 Google Trends
if (IMG / '02-01.webp').exists():
    W = words(IMG / '02-01.webp'); r = {k: v for k, v in REF['ed039p'].items() if k in ('pill', 'signal', 'window')}
    ex = text(W, 90, 290, 600, 420); m = re.match(r'(\w[\w ]*\.)\s+(.*)', ex)
    cap = text(W, 200, 470, 760, 520); term = (re.search(r"for ['‘’\"](.+?)['‘’\"]", cap) or [None, H.replace('-', ' ')])[1]
    r.update(title=title(W), date=m.group(1) if m else '', expl=m.group(2) if m else ex, term=term, note=notes(W),
             csv=f'assets/trends/{H}/{term.replace(" ", "-")}.csv')
    T['ed039p'] = r
# S03 market size: lead + condition, first bar, CAGR
for f in ('03-01.webp',):
    if not (IMG / f).exists(): continue
    W = words(IMG / f); r = {k: v for k, v in REF['ed052p'].items() if k in ('type',)}
    lead = text(W, 200, 175, 700, 255); m = re.match(r'(To get there, |To fill that room, )(.*)', lead)
    bars = [float(x) for x in re.findall(r'\$\s?(\d+(?:\.\d+)?)\s?B', crop(IMG / f, 150, 230, 330, 470, 11))]   # left bars only: the first one is the base year
    cg = re.search(r'(\d+(?:\.\d+)?)\s?%\s?CAGR', text(W, 300, 520, 700, 575))
    yrs = re.findall(r'20\d\d', text(W, 150, 470, 820, 500))
    r.update(title=title(W), lead=m.group(1) if m else '', condition=m.group(2) if m else lead, note=notes(W),
             size=min(bars) if bars else None, cagr=float(cg.group(1)) if cg else None, y0=int(yrs[0]) if yrs else None)
    if r['cagr'] and r['cagr'] == int(r['cagr']): r['cagr'] = int(r['cagr'])
    if r['size'] and r['size'] == int(r['size']): r['size'] = int(r['size'])
    T['ed052p'] = r
# S10 market grid: column and row names, notes (tiles and cells come from live_from_specs.py)
if (IMG / '10-01.webp').exists():
    W = words(IMG / '10-01.webp')
    cols = [crop(IMG / '10-01.webp', a, 185, b, 215, 7) for a, b in ((150, 380), (380, 610), (610, 840))]
    rows = []   # the row label sits at the top of its band, left of the first logos: find the label line in each band
    for a, b in ((215, 300), (300, 390), (390, 520)):
        ls = [l for l in zone(W, 30, a, 245, b) if re.search(r'[A-Za-z]{3}', l)] or crop(IMG / '10-01.webp', 40, a, 245, b, 6, True)
        rows.append(re.sub(r'^\W*[A-Z]{1,2}\s+(?=[A-Z])', '', ls[0]) if ls else '')   # a logo read as « SJ » before the label
    T['ed171p'] = dict(cols=cols, rows=rows, note=notes(W))
f = ROOT / 'decks' / H / 'live.yaml'; L = yaml.safe_load(f.read_text()) if f.exists() else {}
for k, v in T.items(): L[k] = {**L.get(k, {}), **v} if k == 'ed171p' else v
print(yaml.safe_dump(T, allow_unicode=True, sort_keys=False, width=150))
if not CHECK: f.write_text(yaml.safe_dump(L, allow_unicode=True, sort_keys=False, width=150)); print('->', f)
