"""Renders every slide of a workshop deck at x2: python3 shoot.py <deck dir> <img dir>
Writes s<n>.jpg (1280 px wide) and, when the section asks for it, s<n>z.jpg (x2 zoom of the note or of the dated rail)."""
import io, json, sys, pathlib
from playwright.sync_api import sync_playwright
from PIL import Image
D = pathlib.Path(sys.argv[1]).resolve(); OUT = pathlib.Path(sys.argv[2])
M = json.load(open(D / 'manifest.json'))
zoom = {}
for sec in M['sections']:
    ns = [n for c in sec.get('cases', []) for n in c['n'].values()] + [n for v in sec.get('variants', []) if isinstance(v, dict) for n in v['n']]
    for n in ns: zoom[n] = sec.get('zoom')
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width': 960, 'height': 672}, device_scale_factor=2)
    pg.goto((D / 'deck.html').as_uri()); pg.wait_for_load_state('networkidle'); pg.evaluate('document.fonts.ready')
    pg.add_style_tag(content='.slide{margin:0!important}body{background:#062A3C}'); pg.wait_for_timeout(300)
    els = pg.query_selector_all('.slide')
    for n, z in zoom.items():
        im = Image.open(io.BytesIO(els[n - 1].screenshot())).convert('RGB')          # 1920 x 1344
        im.resize((1280, 896), Image.LANCZOS).save(OUT / f's{n}.jpg', quality=84)
        if z == 'region':
            hl = els[n - 1].evaluate("s => { const r = s.querySelector('.reg[data-k=\"' + (s.dataset.hl || '') + '\"]'); return r ? r.dataset.zoom : null; }")
            if hl:
                x0, y0, x1, y1 = [int(v) * 2 for v in hl.split(',')]
                im.crop((max(0, x0), max(0, y0), min(1920, x1), min(1344, y1))).save(OUT / f's{n}z.jpg', quality=90)
        if z == 'button': im.crop((1180, 1150, 1920, 1344)).save(OUT / f's{n}z.jpg', quality=90)
        if z == 'note': im.crop((0, 1150, 1400, 1270)).save(OUT / f's{n}z.jpg', quality=90)
        if z == 'rail': im.crop((60, 380, 820, 900)).save(OUT / f's{n}z.jpg', quality=88)
    b.close()
