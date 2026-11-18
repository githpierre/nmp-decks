"""Templates whose emojis are redrawn as line icons (piste A, 18 Nov 2026): only there an emoji must be in tools/atelier2/icons.json.
Elsewhere (personas, ratings 💰💰💰) the emoji stays an emoji. Read from the built decks: a template is « icon » when its slides
have emojis in deck.yaml and none left in the rendered page.   python3 tools/icon_templates.py -> specs/icon_templates.json"""
import json, re, sys, yaml, pathlib
from playwright.sync_api import sync_playwright
ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'tools')); import spec
DECKS = ['healthcare-ai', 'humanoid-robotics', 'in-vivo-car-t', 'advanced-nuclear']
icon, keep = set(), set()
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width': 960, 'height': 672})
    for h in DECKS:
        S = yaml.safe_load((ROOT / 'decks' / h / 'deck.yaml').read_text())['slides']
        pg.goto((ROOT / 'decks' / h / 'deck.html').as_uri()); pg.wait_for_function('window.__rawfit === true && window.__decided !== false', timeout=180000)
        left = pg.evaluate("""() => [...document.querySelectorAll('.slide')].map(sl => (sl.innerText.match(/\\p{Extended_Pictographic}/gu) || []).length)""")
        for s, n in zip(S, left):
            if not any(spec.EMOJI.search(v) for _, v in spec.leaves(s)): continue
            (icon if n == 0 else keep).add(spec.tpl(s))
    b.close()
icon -= keep
(ROOT / 'specs/icon_templates.json').write_text(json.dumps(sorted(icon), indent=0)); print(len(icon), 'icon templates; emoji kept on', sorted(keep))
