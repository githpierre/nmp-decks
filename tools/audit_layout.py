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
# Harmony audit (12 Nov 2026, Pierre: "truffé d'erreurs"): what a reader sees at a glance on ANY slide (raw, pp, templates).
# MARGIN_ALL: content outside x 60..900 (hard) ; LABEL_LINES / BODY_LINES: sibling boxes with different line counts ;
# TEXT_PAD: a text closer than 5 px to the border of its bubble (or out of it) ; EMOJI_MIX: emojis left among line icons ;
# EMOJI_UNMAPPED: emoji with no icon in icons.py ; MONEY_FORMAT: "$0.285B", "4.228 billion" ; GRID_HOLES: emptied cards ; DATE_CASE: timeline date label not in capitals.
JS2 = r"""() => { const out = []; const miss = [...new Set(window.__emojiMiss || [])]; if (miss.length) out.push([0, 'EMOJI_UNMAPPED', miss.join(' ')]);
 const rowsOf = p => { const g = document.createRange(); g.selectNodeContents(p); const t = new Set(); [...g.getClientRects()].forEach(r => { if (r.width > 1) t.add(Math.round(r.top / 4)); }); return t.size; };
 const ink = el => { const g = document.createRange(); g.selectNodeContents(el); const rs = [...g.getClientRects()].filter(r => r.width > 1 && r.height > 1); if (!rs.length) return null;
   return {l: Math.min(...rs.map(r => r.left)), r: Math.max(...rs.map(r => r.right)), t: Math.min(...rs.map(r => r.top)), b: Math.max(...rs.map(r => r.bottom))}; };
 const EMO = /\p{Extended_Pictographic}/u;
 document.querySelectorAll('section.slide').forEach(sl => { const n = +sl.dataset.n, R = sl.getBoundingClientRect(), type = sl.dataset.type || '';
  if (/^(cover|agenda)$/.test(type) || /divider/.test(sl.dataset.tpl || '')) return;
  const vis = e => { const c = getComputedStyle(e); return c.visibility !== 'hidden' && c.display !== 'none' && +c.opacity !== 0; };
  // --- margins of everything between the title and the footer
  const skip = e => e.closest('.title,.kicker,.subtitle,.note,.foot,.foot-line,.foot-label,.foot-brand,.corner,.pill');
  let mn = 1e9, mx = -1e9, who = '';
  sl.querySelectorAll('*').forEach(e => { if (skip(e) || !vis(e) || (e.children.length && !/^(svg|path|line|rect|circle|img)$/i.test(e.tagName) && ![...e.childNodes].some(c => c.nodeType === 3 && c.textContent.trim()))) return;
    if (/^(svg)$/i.test(e.tagName) && e.querySelector('*')) return;
    let r = e.getBoundingClientRect(); if ([...e.childNodes].some(c => c.nodeType === 3 && c.textContent.trim())) { const k = ink(e); if (k) r = {left: k.l, right: k.r, top: k.t, bottom: k.b, width: k.r - k.l, height: k.b - k.t}; }
    if (r.width < 2 || r.height < 1 || r.width > 940) return; const y = r.top - R.top; if (y < 120 || y > 600) return;
    if (r.left - R.left < mn) { mn = r.left - R.left; } if (r.right - R.left > mx) { mx = r.right - R.left; who = (e.textContent || e.tagName).trim().slice(0, 20); } });
  sl.querySelectorAll('.map .reg').forEach(r => { if (+r.dataset.grew > 8) out.push([n, 'MAP_BOX_WIDENED', '+' + r.dataset.grew + 'px: the text is too long for its place on the map, shorten it', r.textContent.trim().slice(0, 30)]); });
  sl.querySelectorAll('.map .reg p').forEach(p => { if (p.textContent.trim().length > 135) out.push([n, 'MAP_TEXT_LONG', p.textContent.trim().length + ' characters (max 135, or the box widens to the edge)', p.textContent.trim().slice(0, 30)]); });
  if ((mn < 56 || mx > 904) && type !== 'worldmap' && !/could_make_market_grow_faster|happened_between|happened_since_then/.test(sl.dataset.tpl || '')) out.push([n, 'MARGIN_ALL', Math.round(mn) + '..' + Math.round(mx), who]);
  // --- raw slides: sibling boxes
  const T = [...sl.querySelectorAll('.raw .rx-t')].filter(vis).map(el => { const ps = [...el.querySelectorAll('p')].filter(p => /[A-Za-z0-9]/.test(p.textContent) && !EMO.test(p.textContent.trim().slice(0, 2)));
    if (!ps.length) return null; const b = el.getBoundingClientRect(), txt = ps.map(p => p.textContent.trim()).join(' ');
    if (txt.length < 6) return null; let lab = 0, body = 0;
    if (txt.length <= 34 && txt.split(/\s+/).length <= 5) lab = ps.reduce((a, p) => a + rowsOf(p), 0);
    else if (ps.length >= 2 && ps[0].textContent.trim().length <= 30 && ps[0].textContent.trim().split(/\s+/).length <= 4 && ps.slice(1).join && ps.slice(1).map(p => p.textContent).join(' ').length > 40) { lab = rowsOf(ps[0]); body = ps.slice(1).reduce((a, p) => a + rowsOf(p), 0); }
    else body = ps.reduce((a, p) => a + rowsOf(p), 0);
    const fp = ps[ps.length - 1], cs = getComputedStyle(fp.querySelector('span') || fp);
    return {el, x: b.left - R.left, y: b.top - R.top, w: b.width, h: b.height, fs: Math.round(parseFloat(getComputedStyle(fp).fontSize) * 10), col: cs.color, lab, body, txt, k: ink(el)}; }).filter(Boolean);
  const used = new Set();
  T.forEach((a, i) => { if (used.has(i)) return; const g = [i]; used.add(i);
    for (let q = 0; q < g.length; q++) T.forEach((b, j) => { if (used.has(j)) return; const c = T[g[q]];
      if (Math.abs(b.w - c.w) <= 3 && b.fs === c.fs && (!!b.lab === !!c.lab) && (!!b.body === !!c.body) && (Math.abs(b.y - c.y) <= 4 || Math.abs(b.x - c.x) <= 4)) { used.add(j); g.push(j); } });
    if (g.length < 2) return; const G = g.map(j => T[j]);
    const L = G.filter(b => b.lab).map(b => b.lab), B = G.filter(b => b.body).map(b => b.body);
    if (new Set(L).size > 1) out.push([n, 'LABEL_LINES', L.join(','), G.filter(b => b.lab).map(b => b.txt.slice(0, 14)).join(' / ').slice(0, 90)]);
    if (new Set(B).size > 1 && Math.max(...B) <= 9) out.push([n, 'BODY_LINES', B.join(','), G.filter(b => b.body).map(b => b.txt.slice(0, 12)).join(' / ').slice(0, 90)]); });
  // --- same boxes, same font size (a text shrunk to fit is shortened instead)
  { const seen = new Set(); T.forEach((a, i) => { if (seen.has(i) || !a.body) return; const g = T.filter((b, j) => b.body && Math.abs(b.w - a.w) <= 3 && Math.abs(b.h - a.h) <= 3 && (Math.abs(b.y - a.y) <= 4 || Math.abs(b.x - a.x) <= 4));
      g.forEach(b => seen.add(T.indexOf(b))); const F = [...new Set(g.map(b => b.fs))]; if (g.length >= 3 && F.length > 1) out.push([n, 'FONT_MIXED', F.map(f => (f / 10 * 0.75).toFixed(1) + 'pt').join(','), g.filter(b => b.fs === Math.min(...F)).map(b => b.txt.slice(0, 25)).join(' / ')]); }); }
  // --- text inside its bubble with air around it
  const SH = [...sl.querySelectorAll('.raw > svg.rx-s')].filter(vis).map(el => { const p = el.querySelector('path'); if (!p) return null; const d = p.getAttribute('d') || ''; if (!/Z\s*$/i.test(d.trim())) return null;
    const r = p.getBoundingClientRect(); if (r.width < 50 || r.height < 22) return null; if (Math.abs(r.width - r.height) < 4 && r.width > 120) return null;   /* circles of a Venn diagram */ const st = p.getAttribute('stroke'), fi = p.getAttribute('fill'); if ((!st || st === 'none') && (!fi || fi === 'none')) return null; return r; }).filter(Boolean);
  T.forEach(b => { if (!b.k) return; const cx = (b.k.l + b.k.r) / 2, cy = (b.k.t + b.k.b) / 2;
    const c = SH.filter(r => cx > r.left && cx < r.right && cy > r.top && cy < r.bottom).sort((p, q) => p.width * p.height - q.width * q.height)[0]; if (!c || c.width > 700) return;
    const pad = Math.min(b.k.l - c.left, c.right - b.k.r, b.k.t - c.top, c.bottom - b.k.b); if (pad < 2.5) out.push([n, 'TEXT_PAD',, Math.round(pad) + 'px', b.txt.slice(0, 40)]); });
  // --- emojis left among line icons
  const ic = sl.querySelectorAll('.raw span[style*="inline-flex"] svg, .raw .ico-pill svg').length;
  const em = [...sl.querySelectorAll('.raw .rx-t')].filter(vis).filter(el => { const t = el.textContent.trim(); return t && [...t.replace(/[\s\uFE0F\u200D]/g, '')].length <= 3 && EMO.test(t); });
  if (ic >= 2 && em.length) out.push([n, 'EMOJI_MIX', em.length + ' emoji / ' + ic + ' icons', em.map(e => e.textContent.trim()).join(' ')]);
  // --- timeline date labels in capitals (Pierre, 12 Nov 2026)
  { const DR = /^(?=.*(\b(19|20)\d{2}\b|\b\d{2}\b|\btoday\b|\bnow\b))((early|mid|late|since|before|after|by|until|from|end of|start of|today|now|q[1-4]|h[12]|jan|feb|mar|apr|may|jun|jul|aug|sep|sept|oct|nov|dec)[a-z]*\.?|(19|20)?\d{2}|[-–/&+, ])+$/i;
    [...sl.querySelectorAll('.raw .rx-t')].filter(vis).forEach(el => { const t = el.textContent.replace(/\s+/g, ' ').trim(); if (t && t.length <= 20 && DR.test(t) && el.innerText.trim() !== el.innerText.trim().toUpperCase()) out.push([n, 'DATE_CASE', t]); }); }
  // --- chart labels sitting on a bubble or another label (sx_round_timeline)
  sl.querySelectorAll('.rtl-lab[data-clash]').forEach(t => out.push([n, 'LABEL_ON_SHAPE', t.textContent.trim()]));
  // --- money written the way people say it
  const nt = sl.querySelector('.note'); if (nt && nt.textContent.trim() && !/^We\b/.test(nt.textContent.trim())) out.push([n, 'NOTE_WE', nt.textContent.trim().slice(0, 40)]);   // RULES: a note starts with « We »
  sl.querySelectorAll('img').forEach(im => { if (!im.naturalWidth) out.push([n, 'BROKEN_IMG', (im.getAttribute('src') || '').split('/').pop()]); });   // 12 Nov 2026: contrast slides showed broken logo images
  const tx = sl.querySelector('.srcl') ? '' : sl.innerText; const m = tx.match(/\$0\.\d+ ?(B|billion)\b|\b\d+\.\d{3,} ?(B|billion|M|million)\b|\$ ?\d{4,} ?M\b/); if (m) out.push([n, 'MONEY_FORMAT', m[0]]);   // $1787M must read $1.8B (12 Nov 2026)
  // --- the slide title is always on two lines (Pierre, 12 Nov 2026)
  { const tt = sl.querySelector('.title'); if (tt) { const lh = parseFloat(getComputedStyle(tt).lineHeight), k = Math.round(tt.getBoundingClientRect().height / lh); if (k !== 2) out.push([n, 'TITLE_NOT_2_LINES', k + ' line(s)', tt.textContent.trim().slice(0, 50)]); } }
  if (sl.querySelector('[data-robotic]')) out.push([n, 'GRID_ROBOTIC', 'top players grid placed by the automatic pattern: give `pos` (meaning) or `tiles` (live page)']);
  // --- cards emptied by the import
  const holes = sl.querySelectorAll('[data-emptied]').length; if (holes && !sl.dataset.holesOk && !(holes === 1 && sl.querySelector('.raw'))) out.push([n, 'GRID_HOLES', holes + ' empty cards']);
 }); return out; }"""
def run(slug):
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1000, 'height': 800})
        pg.goto((Path(__file__).resolve().parent.parent / 'decks' / slug / 'deck.html').as_uri()); pg.wait_for_timeout(1500)
        out = pg.evaluate(JS); out += pg.evaluate(JS2); b.close()
    for o in out: print(' | '.join(map(str, o)))
    print(len(out), 'layout issues')
if __name__ == '__main__': run(sys.argv[1])
