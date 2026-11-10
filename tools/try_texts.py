"""Try rewrites of raw-slide texts before writing them in overrides.yaml (Pierre's text-box rules).
Input JSON: [{"n": slide, "k": shape, "lines": N or null, "texts": [candidates...]}]
For each candidate: line count, line widths, balance (max-min)/max and fill (longest line / inner width).
Usage: python3 tools/try_texts.py decks/<slug> cands.json"""
import json, pathlib, sys
from playwright.sync_api import sync_playwright

JS = r"""(C) => C.map(c => {
  const el = document.querySelector(`.slide[data-n="${c.n}"] .rx-t[data-k="${c.k}"]`); if (!el) return {err: 'no box'};
  const F = window.__fitapi, p = F.main(el), sp = p.querySelector('span') || p, inner = p.getBoundingClientRect().width;
  return c.texts.map(t => {
    sp.innerHTML = ''; sp.textContent = t; [...p.childNodes].forEach(x => { if (x !== sp) x.remove(); }); p._segs = null;
    const nat = F.rows(p); F.fit(p, c.lines || nat);
    const rows = {}; p.querySelectorAll('.fw').forEach(s => [...s.getClientRects()].forEach(r => { const k = Math.round(r.top / 3); rows[k] = [Math.min(r.left, (rows[k] || [1e9])[0]), Math.max(r.right, (rows[k] || [0, 0])[1])]; }));
    const w = Object.values(rows).map(r => Math.round(r[1] - r[0])), mx = Math.max(...w);
    return {t, nat, lines: w.length, w, bal: Math.round((mx - Math.min(...w)) / mx * 100), fill: Math.round(mx / inner * 100)};
  });
})"""

d = pathlib.Path(sys.argv[1]).resolve(); C = json.load(open(sys.argv[2]))
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width': 960, 'height': 672})
    pg.goto((d / 'deck.html').as_uri()); pg.wait_for_function('window.__rawfit === true', timeout=90000)
    R = pg.evaluate(JS, C); b.close()
for c, r in zip(C, R):
    print(f"== {c['n']} k{c['k']}")
    for x in (r if isinstance(r, list) else [r]):
        print(f"   L{x.get('lines')} bal{x.get('bal')}% fill{x.get('fill')}% {x.get('w')} | {x.get('t')}")
