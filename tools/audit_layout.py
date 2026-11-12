"""Layout audit for template slides (12 Nov 2026, Pierre: "il n'y a pas de marge à droite et à gauche").
MARGIN: any visible element of the slide body outside x 90..870 (the side margins of the deck).
TEXT_OVERLAP: two text elements whose boxes overlap. PINK_TEXT: pink text on navy.
Usage: python3 tools/audit_layout.py <slug>"""
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright
JS = r"""() => { const out = []; document.querySelectorAll('section.slide').forEach(sl => { const n = +sl.dataset.n, R = sl.getBoundingClientRect();
  const body = sl.querySelector('.body'); if (!body) return;
  const els = [...body.querySelectorAll('*')].filter(e => { const s = getComputedStyle(e); return s.visibility !== 'hidden' && s.display !== 'none' && e.getBoundingClientRect().width > 0; });
  let mn = 1e9, mx = -1e9; els.forEach(e => { if (e.children.length && e.tagName !== 'svg') return; const r = e.getBoundingClientRect(); mn = Math.min(mn, r.left - R.left); mx = Math.max(mx, r.right - R.left); });
  if (mn < 90 || mx > 870) out.push([n, 'MARGIN', Math.round(mn) + '..' + Math.round(mx)]);
  const T = els.filter(e => [...e.childNodes].some(c => c.nodeType === 3 && c.textContent.trim()) || e.tagName === 'text').map(e => { const g = document.createRange(); g.selectNodeContents(e); return {e, r: g.getBoundingClientRect()}; }).filter(o => o.r.width > 0);
  for (let i = 0; i < T.length; i++) for (let j = i + 1; j < T.length; j++) { const a = T[i].r, b = T[j].r; if (T[i].e.contains(T[j].e) || T[j].e.contains(T[i].e)) continue;
    const ox = Math.min(a.right, b.right) - Math.max(a.left, b.left), oy = Math.min(a.bottom, b.bottom) - Math.max(a.top, b.top); if (ox > 2 && oy > 2) out.push([n, 'TEXT_OVERLAP', T[i].e.textContent.trim().slice(0, 25) + ' / ' + T[j].e.textContent.trim().slice(0, 25)]); }
  T.forEach(o => { const c = getComputedStyle(o.e).color + ' ' + (o.e.getAttribute && o.e.getAttribute('fill') || ''); if (/251, 1, 97|FB0161/i.test(c)) out.push([n, 'PINK_TEXT', o.e.textContent.trim().slice(0, 30)]); });
}); return out; }"""
def run(slug):
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1000, 'height': 800})
        pg.goto((Path(__file__).resolve().parent.parent / 'decks' / slug / 'deck.html').as_uri()); pg.wait_for_timeout(1500)
        out = pg.evaluate(JS); b.close()
    for o in out: print(' | '.join(map(str, o)))
    print(len(out), 'layout issues')
if __name__ == '__main__': run(sys.argv[1])
