"""Audit visuel fin du deck construit : texte qui déborde / chevauche une forme ou un autre texte, connecteurs qui n'arrivent sur rien,
éléments presque alignés (1-6 px d'écart). python3 tools/visual_audit.py decks/<slug> -> <deck>/visual_audit.json"""
import json, pathlib, sys
from playwright.sync_api import sync_playwright
JS = r"""() => { const out = [];
 document.querySelectorAll('.slide').forEach(sl => { const n = +sl.dataset.n; const R = sl.getBoundingClientRect(); const raw = sl.querySelector('.raw'); if (!raw) return;
  const rel = r => ({x: r.left - R.left, y: r.top - R.top, w: r.width, h: r.height, r: r.right - R.left, b: r.bottom - R.top});
  const vis = e => getComputedStyle(e).visibility !== 'hidden' && getComputedStyle(e).display !== 'none';
  const T = [...raw.querySelectorAll(':scope > .rx-t')].filter(vis).map(e => { const rg = document.createRange(); rg.selectNodeContents(e); const q = rg.getBoundingClientRect(); return {e, k: e.dataset.k, box: rel(e.getBoundingClientRect()), ink: q.width ? rel(q) : null, t: e.textContent.trim().slice(0, 40)}; }).filter(t => t.ink && t.t);
  const S = [...raw.querySelectorAll(':scope > svg.rx-s')].filter(vis).map(e => { const p = e.querySelector(':scope > path'); if (!p) return null; const d = p.getAttribute('d') || '';
    const line = /^M[-\d.\s]+L[-\d.\s]+$/.test(d) || p.getAttribute('fill') === 'none' && /^M[-\d.\s]+(L|C)/.test(d) && !/Z/.test(d);
    return {e, p, box: rel(p.getBoundingClientRect()), fill: p.getAttribute('fill'), stroke: p.getAttribute('stroke'), line, d}; }).filter(Boolean);
  const inter = (a, b) => Math.max(0, Math.min(a.r, b.r) - Math.max(a.x, b.x)) * Math.max(0, Math.min(a.b, b.b) - Math.max(a.y, b.y));
  const inside = (a, b, m = 1) => a.x >= b.x - m && a.y >= b.y - m && a.r <= b.r + m && a.b <= b.b + m;
  // 1. text ink outside the slide or crossing its own box by > 3px
  T.forEach(t => { if (t.ink.x < 4 || t.ink.r > 956 || t.ink.y < 2 || t.ink.b > 668) out.push({n, kind: 'TEXT_OFF_SLIDE', k: t.k, t: t.t});
    if (t.ink.b > t.box.b + 4 || t.ink.r > t.box.r + 4) out.push({n, kind: 'TEXT_OVERFLOW', k: t.k, t: t.t, by: Math.round(Math.max(t.ink.b - t.box.b, t.ink.r - t.box.r))}); });
  // 2. text ink over a filled shape it is not inside (text on a bar)
  T.forEach(t => S.filter(s => !s.line && s.fill && s.fill !== 'none' && s.box.w > 6 && s.box.h > 6).forEach(s => { const a = inter(t.ink, s.box);
    if (a > 30 && !inside(t.ink, s.box, 2) && a < t.ink.w * t.ink.h * .95) out.push({n, kind: 'TEXT_ON_SHAPE', k: t.k, t: t.t, shape: [Math.round(s.box.x), Math.round(s.box.y), Math.round(s.box.w), Math.round(s.box.h)], fill: s.fill, area: Math.round(a)}); }));
  // 3. text over text
  for (let i = 0; i < T.length; i++) for (let j = i + 1; j < T.length; j++) { const a = inter(T[i].ink, T[j].ink); if (a > 20) out.push({n, kind: 'TEXT_ON_TEXT', k: T[i].k + '/' + T[j].k, t: T[i].t + ' | ' + T[j].t, area: Math.round(a)}); }
  // 4. connector endpoints that land on nothing (gap 4-30 px to the nearest box edge)
  const boxes = S.filter(s => !s.line && s.box.w > 20 && s.box.h > 12).map(s => s.box).concat(T.map(t => t.ink));
  S.filter(s => s.line && (s.box.w > 14 || s.box.h > 14)).forEach(s => { const L = s.p.getTotalLength(); const m = s.p.getScreenCTM();
    [0, L].forEach(at => { const pt = s.p.getPointAtLength(at), q = pt.matrixTransform(m); const x = q.x - R.left, y = q.y - R.top;
      let best = 1e9; boxes.forEach(b => { const dx = Math.max(b.x - x, 0, x - b.r), dy = Math.max(b.y - y, 0, y - b.b); best = Math.min(best, Math.hypot(dx, dy)); });
      if (best > 4 && best < 40) out.push({n, kind: 'LINE_GAP', at: [Math.round(x), Math.round(y)], gap: Math.round(best)}); }); });
  // 5. near-alignment of same-size siblings (x or y differs by 1-5 px)
  const B = S.filter(s => !s.line && s.box.w > 30 && s.box.h > 20).map(s => s.box);
  for (let i = 0; i < B.length; i++) for (let j = i + 1; j < B.length; j++) { const a = B[i], b = B[j]; if (Math.abs(a.w - b.w) > 3 || Math.abs(a.h - b.h) > 3) continue;
    const dx = Math.abs(a.x - b.x), dy = Math.abs(a.y - b.y); if ((dx >= 1.5 && dx <= 6 && dy > 10) || (dy >= 1.5 && dy <= 6 && dx > 10)) out.push({n, kind: 'MISALIGNED', a: [Math.round(a.x), Math.round(a.y)], b: [Math.round(b.x), Math.round(b.y)], d: Math.round(Math.max(dx < 10 ? dx : 0, dy < 10 ? dy : 0) * 10) / 10}); }
 }); return out; }"""
d = pathlib.Path(sys.argv[1]).resolve()
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width': 960, 'height': 672})
    pg.goto((d / 'deck.html').as_uri()); pg.wait_for_function('window.__rawfit === true && window.__decided !== false', timeout=120000)
    pg.add_style_tag(content='.slide{margin:0!important}')
    r = pg.evaluate(JS); b.close()
(d / 'visual_audit.json').write_text(json.dumps(r, ensure_ascii=False, indent=0))
from collections import Counter
print(Counter(x['kind'] for x in r)); print(len({x['n'] for x in r}), 'slides')
