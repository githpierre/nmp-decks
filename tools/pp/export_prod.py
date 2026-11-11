"""deck.html -> x3 PNG per slide -> page_lift WebP 2400x1680, named from jobs.json ({handle}-slide-{ss}-{vv}.webp). usage: export_prod.py <slug> <outdir>"""
import sys, json, subprocess, pathlib
from concurrent.futures import ThreadPoolExecutor
slug = sys.argv[1]; out = pathlib.Path(sys.argv[2]); out.mkdir(parents=True, exist_ok=True)
d = pathlib.Path(f'/home/claude/nmp-decks/decks/{slug}'); jobs = json.load(open(d / 'jobs.json'))
from playwright.sync_api import sync_playwright
pngs = []
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width': 960, 'height': 672}, device_scale_factor=3)
    pg.goto((d / 'deck.html').as_uri()); pg.wait_for_load_state('load'); pg.evaluate('document.fonts.ready')
    pg.wait_for_function('window.__rawfit === true && window.__decided !== false', timeout=120000)
    pg.add_style_tag(content='.slide{margin:0!important}body{background:#062A3C}')
    els = pg.query_selector_all('.slide'); assert len(els) == len(jobs), (len(els), len(jobs))
    for j, el in zip(jobs, els):
        png = out / (j['name'][:-5] + '.png'); el.screenshot(path=str(png)); pngs.append((png, out / j['name']))
    b.close()
def lift(a): subprocess.run(['python3', '/home/claude/nmp-product-pages/w/s10/pagetest/page_lift.py', str(a[0]), str(a[1])], check=True); a[0].unlink()
if '--nolift' not in sys.argv:
    with ThreadPoolExecutor(4) as ex: list(ex.map(lift, pngs))
print(len(pngs), 'webp')
