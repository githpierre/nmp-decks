"""python3 tools/atelier2/fixshot.py decks/<slug> <out dir> <before|after> -> 2x crops of every fix's clip (fixes.py)."""
import sys, pathlib, io, importlib.util
from playwright.sync_api import sync_playwright
from PIL import Image
H = pathlib.Path(__file__).parent
s = importlib.util.spec_from_file_location('fixes', H / 'fixes.py'); M = importlib.util.module_from_spec(s); s.loader.exec_module(M)
deck = pathlib.Path(sys.argv[1]).resolve(); out = pathlib.Path(sys.argv[2]); tag = sys.argv[3]; (out / 'img').mkdir(parents=True, exist_ok=True)
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width': 960, 'height': 672}, device_scale_factor=2)
    pg.goto(deck.joinpath('deck.html').as_uri()); pg.wait_for_function('window.__rawfit === true && window.__decided !== false', timeout=120000)
    pg.add_style_tag(content='.slide{margin:0!important}body{background:#062A3C}'); pg.wait_for_timeout(300)
    cache = {}
    for f in M.FIXES:
        n, x, y, w, h = f['clip']
        if n not in cache:
            el = pg.query_selector(f'.slide[data-n="{n}"]'); el.scroll_into_view_if_needed(); cache[n] = Image.open(io.BytesIO(el.screenshot(type='png'))).convert('RGB')
        im = cache[n].crop((x * 2, y * 2, (x + w) * 2, (y + h) * 2))
        if im.width > 1400: im = im.resize((1400, round(im.height * 1400 / im.width)))
        im.save(out / 'img' / f'f{f["id"]:02d}_{tag}.jpg', quality=85)
    for n in sorted({s for f in M.FIXES for s in f['slides']} | set(cache)):
        el = pg.query_selector(f'.slide[data-n="{n}"]'); el.scroll_into_view_if_needed()
        Image.open(io.BytesIO(el.screenshot(type='png'))).convert('RGB').resize((960, 672)).save(out / 'img' / f's{n:03d}_{tag}.jpg', quality=80)
    if tag == 'after':
        fx = pg.evaluate("() => Object.fromEntries(Object.entries(window.__fixed || {}).map(([k, v]) => [k, [...v].sort((a, b) => a - b)]))")
        import json; (out / 'fixed.json').write_text(json.dumps(fx)); print(fx)
    b.close()
print('ok', tag)
