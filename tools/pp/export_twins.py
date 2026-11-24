"""Product-page images from the twins of a built deck (24 Nov 2026): deck.html -> x3 PNG of the slide -> page_lift WebP 2400x1680 RGBA,
named {handle}-slide-{ss}-{vv}.webp. usage: export_twins.py <handle> <outdir> 09-01=ed168p 02-01=ed039p ..."""
import sys, subprocess, pathlib
from playwright.sync_api import sync_playwright
h = sys.argv[1]; out = pathlib.Path(sys.argv[2]); out.mkdir(parents=True, exist_ok=True)
want = dict(a.split('=') for a in sys.argv[3:])
d = pathlib.Path(__file__).resolve().parents[2] / 'decks' / h
done = []
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width': 960, 'height': 672}, device_scale_factor=3)
    pg.goto((d / 'deck.html').as_uri()); pg.wait_for_load_state('load'); pg.evaluate('document.fonts.ready')
    pg.wait_for_function('window.__rawfit === true && window.__decided !== false', timeout=180000)
    pg.add_style_tag(content='.slide{margin:0!important}body{background:#062A3C}.tag,.ytag{display:none!important}')
    for sv, sid in want.items():
        el = pg.query_selector(f'.slide[data-id="{sid}"]')
        if not el: print('MISSING', h, sv, sid); continue
        png = out / f'{h}-slide-{sv}.png'; el.screenshot(path=str(png)); done.append((png, out / f'{h}-slide-{sv}.webp'))
    b.close()
for a, w in done:
    subprocess.run(['python3', '/home/claude/nmp-product-pages/w/s10/pagetest/page_lift.py', str(a), str(w)], check=True); a.unlink()
print(len(done), 'webp')
