"""deck.html -> hi-res PNG per slide (x3) -> page_lift WebP 2400x1680 q92 named {handle}-slide-09-01.webp"""
import sys, yaml, subprocess, pathlib
slug=sys.argv[1]; out=pathlib.Path(sys.argv[2]); out.mkdir(parents=True,exist_ok=True)
d=pathlib.Path(f'/home/claude/nmp-decks/decks/{slug}'); deck=yaml.safe_load((d/'deck.yaml').read_text())
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':960,'height':672},device_scale_factor=3)
    pg.goto((d/'deck.html').as_uri()); pg.wait_for_load_state('load'); pg.evaluate('document.fonts.ready')
    pg.wait_for_function('window.__rawfit === true && window.__decided !== false', timeout=60000)
    pg.add_style_tag(content='.slide{margin:0!important}body{background:#062A3C}')
    for s,el in zip(deck['slides'],pg.query_selector_all('.slide')):
        png=out/f"{s['handle']}-09.png"; el.screenshot(path=str(png))
        subprocess.run(['python3','/home/claude/nmp-product-pages/w/s10/pagetest/page_lift.py',str(png),str(out/f"{s['handle']}-slide-09-01.webp")],check=True)
    b.close()
