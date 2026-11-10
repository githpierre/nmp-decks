"""python3 tools/dump_slide.py decks/<slug> N [N...] -> shapes and texts (boxes in px) of raw slides, after decisions."""
import sys, pathlib, json
from playwright.sync_api import sync_playwright
deck = pathlib.Path(sys.argv[1]).resolve(); ns = [int(x) for x in sys.argv[2:]]
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width': 960, 'height': 672})
    pg.goto(deck.joinpath('deck.html').as_uri()); pg.wait_for_function('window.__rawfit === true && window.__decided !== false', timeout=120000)
    pg.add_style_tag(content='.slide{margin:0!important}')
    for n in ns:
        r = pg.evaluate("""n => { const sl=document.querySelector(`.slide[data-n="${n}"]`); const A=window.A;
          const f=v=>Math.round(v);
          const sh=A.shapes(sl).map((s,i)=>`S${i} k${s.el.dataset.k||''} ${f(s.x)},${f(s.y)} ${f(s.w)}x${f(s.h)} fill=${s.fill} st=${s.stroke} sw=${s.sw} ${s.dash?'dash':''} ${s.line?'LINE':''} ${s.el.style.visibility==='hidden'?'HID':''}`);
          const tx=A.texts(sl).map(t=>`T k${t.k} ${f(t.x)},${f(t.y)} ${f(t.w)}x${f(t.h)} [${t.text.slice(0,50)}] ${getComputedStyle(t.el.querySelector('span')||t.el).color} ${getComputedStyle(t.el.querySelector('span')||t.el).fontWeight}`);
          const im=A.imgs(sl).map(t=>`I ${f(t.x)},${f(t.y)} ${f(t.w)}x${f(t.h)}`);
          return sh.concat(tx,im).join('\\n'); }""", n)
        print(f'===== {n}\n{r}')
    b.close()
