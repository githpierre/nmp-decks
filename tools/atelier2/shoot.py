"""Render the atelier: for every item, the current slide and 3 variants (CSS + JS injected live on the real deck).
Usage: python3 tools/atelier2/shoot.py decks/edtech-full <out dir> [item ids...]"""
import json, pathlib, sys, io, importlib.util
from playwright.sync_api import sync_playwright
from PIL import Image

HERE = pathlib.Path(__file__).parent
deck = pathlib.Path(sys.argv[1]).resolve(); out = pathlib.Path(sys.argv[2]); (out / 'img').mkdir(parents=True, exist_ok=True)
spec = importlib.util.spec_from_file_location('items', HERE / (__import__('os').environ.get('ITEMS','items') + '.py')); M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
items = M.ITEMS
only = set(sys.argv[3:])
if only: items = [i for i in items if str(i['id']) in only]
ICONS = (HERE / 'icons.json').read_text(); LIB = (HERE / 'lib.js').read_text()

with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width': 960, 'height': 672}, device_scale_factor=2)
    pg.goto(deck.joinpath('deck.html').as_uri()); pg.wait_for_function('window.__rawfit === true && window.__decided !== false', timeout=120000)
    pg.add_style_tag(content='.slide{margin:0!important}body{background:#062A3C}')
    pg.evaluate('ic => { window.ICONS = JSON.parse(ic); }', ICONS); pg.add_script_tag(content=LIB)
    pg.evaluate("""() => { window.__pristine = {}; document.querySelectorAll('.slide').forEach(s => window.__pristine[s.dataset.n] = s.cloneNode(true)); }""")
    for it in items:
        n = it['shot']
        for key in ['0', 'A', 'B', 'C']:
            v = it.get(key) or {}
            css = (v.get('css') or '').replace('S ', f'.slide[data-n="{n}"] ').replace('S{', f'.slide[data-n="{n}"]{{')
            err = pg.evaluate("""([n, css, js]) => {
                const old = document.querySelector(`.slide[data-n="${n}"]`); const fresh = window.__pristine[n].cloneNode(true); old.replaceWith(fresh);
                document.querySelectorAll('style.atl').forEach(s => s.remove());
                if (css) { const st = document.createElement('style'); st.className = 'atl'; st.textContent = css; document.head.appendChild(st); }
                try { if (js) (new Function('sl', 'A', 'C', js))(fresh, window.A, window.A.C); } catch (e) { return String(e); }
                return null; }""", [n, css, v.get('js') or ''])
            if err: print('JS error', it['id'], key, err)
            pg.wait_for_timeout(60)
            el = pg.query_selector(f'.slide[data-n="{n}"]'); el.scroll_into_view_if_needed()
            im = Image.open(io.BytesIO(el.screenshot(type='png'))).convert('RGB')
            if it.get('clip'):
                x, y, w, h = it['clip']; im = im.crop((x * 2, y * 2, (x + w) * 2, (y + h) * 2))
                if im.width > 1400: im = im.resize((1400, round(im.height * 1400 / im.width)))
            else: im = im.resize((1200, 840))
            im.save(out / 'img' / f'{it["id"]}{key}.jpg', quality=82)
        print('ok', it['id'], flush=True)
    b.close()
json.dump([{k: v for k, v in i.items()} for i in M.ITEMS], open(out / 'items.json', 'w'), ensure_ascii=False)
