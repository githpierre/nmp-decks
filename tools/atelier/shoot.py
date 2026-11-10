import json, sys, pathlib
from playwright.sync_api import sync_playwright
from PIL import Image
import io
D = pathlib.Path(sys.argv[1]); OUT = pathlib.Path(sys.argv[2])
man = json.load(open(D / 'manifest.json'))
man = man['items'] if isinstance(man, dict) else man
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width': 960, 'height': 672}, device_scale_factor=2)
    pg.goto((D / 'deck.html').as_uri()); pg.wait_for_load_state('networkidle'); pg.evaluate('document.fonts.ready')
    pg.add_style_tag(content='.slide{margin:0!important}body{background:#062A3C}'); pg.wait_for_timeout(300)
    els = pg.query_selector_all('.slide')
    for m in man:
        im = Image.open(io.BytesIO(els[m['n'] - 1].screenshot())).convert('RGB')   # 1920 x 1344
        name = f"{m['at']}{m['case']}{m['var']}"
        im.resize((1280, 896), Image.LANCZOS).save(OUT / f'{name}.jpg', quality=82)
        if m['at'] == 'B': im.crop((0, 1160, 1240, 1272)).save(OUT / f'{name}z.jpg', quality=88)
        if m['at'] == 'C':
            px = im.load(); top = next(y for y in range(300, 1300) if any(px[x, y][0] > 180 and px[x, y][1] < 90 for x in range(60, 260, 2)))
            im.crop((40, top - 30, 720, top + 330)).save(OUT / f'{name}z.jpg', quality=88)
    b.close()
