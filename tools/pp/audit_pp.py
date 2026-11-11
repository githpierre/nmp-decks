"""Visual and rule audit of the product-page slides (pp_*), run after build.py. usage: audit_pp.py <slug>
Every rule Pierre gave on 11 Nov 2026 is checked here, so he never has to repeat it."""
import sys, json
from playwright.sync_api import sync_playwright
JS = r"""() => {
const out = []; const R = e => e.getBoundingClientRect();
const lines = e => { const lh = parseFloat(getComputedStyle(e).lineHeight) || parseFloat(getComputedStyle(e).fontSize) * 1.3; return Math.round(R(e).height / lh); };
document.querySelectorAll('.slide').forEach((s, i) => {
  const n = i + 1, T = s.dataset.type; if (!T.startsWith('pp_')) return; const S = R(s);
  const add = (k, d) => out.push([n, T, k, d]);
  const t = s.querySelector('.title'); const tb = t ? R(t).bottom - S.top : 0;
  const pill = s.querySelector('.pillrow .pill'); const pb = pill ? R(pill).bottom - S.top : 0;
  // 1. air under the title: content never closer than 30 px to the title (20 px to the pill)
  const skip = new Set(['title', 'section', 'pillrow', 'pill', 'tri', 'note', 'foot-line', 'foot-label', 'foot-brand', 'pp-abs']);
  let top = 1e9;
  s.querySelectorAll(':scope > *').forEach(e => { if ([...e.classList].some(c => skip.has(c))) return; const r = R(e); if (r.height > 0 && r.width > 0) top = Math.min(top, r.top - S.top); });
  s.querySelectorAll('.pp-abs *').forEach(e => { const r = R(e); if (r.height > 1 && r.width > 1) top = Math.min(top, r.top - S.top); });
  if (pill) { if (top - pb < 20) add('PILL_GAP', Math.round(top - pb)); }
  else if (top - tb < 30) add('TITLE_GAP', Math.round(top - tb));
  // 2. nothing overlaps or touches: text boxes and logo tiles at least 4 px apart
  const els = [...s.querySelectorAll('.lt, [class^="pp-"]')].filter(e => !e.closest('.pp-abs') && e.offsetParent && !['pp-abs', 'pp-lead', 'pp-wcol', 'pp-rl', 'pp-kl', 'pp-pl', 'pp-dhl', 'pp-rs', 'pp-bar', 'pp-rbar', 'pp-rb', 'pp-vcard', 'pp-dlogos', 'pp-risk', 'pp-big', 'pp-rtr'].some(c => e.classList.contains(c)));
  for (let a = 0; a < els.length; a++) for (let b = a + 1; b < els.length; b++) {
    const A = els[a], B = els[b]; if (A.contains(B) || B.contains(A)) continue;
    const ra = R(A), rb = R(B); const gx = Math.max(ra.left, rb.left) - Math.min(ra.right, rb.right), gy = Math.max(ra.top, rb.top) - Math.min(ra.bottom, rb.bottom);
    if (gx < 0 && gy < 4) add('TOO_CLOSE', `${A.className.split(' ')[0]}|${(A.innerText||'logo').slice(0,18)} / ${B.className.split(' ')[0]}|${(B.innerText||'logo').slice(0,18)} gap ${Math.round(gy)}`);
  }
  // 2b. nothing leaves the slide band, no text clipped in its box
  s.querySelectorAll('[class^="pp-"], .lt').forEach(e => { if (e.closest('.pp-abs')) return; const r = R(e); if (!r.width) return;
    if (r.left - S.left < 12 || S.right - r.right < 12) add('OFF_SLIDE', (e.innerText || e.className).slice(0, 24));
    if (e.scrollWidth > e.clientWidth + 2 && getComputedStyle(e).overflow !== 'visible' ) add('CLIPPED', (e.innerText || '').slice(0, 24)); });
  // 2c. axis labels never overlap (Pierre 11 Nov: 'Dec 23 Apr 24' collided, labels sit inside pp-abs so 2. skipped them)
  const xl = [...s.querySelectorAll('.pp-xl')].map(e => { const r = e.getBoundingClientRect(); return [r.left, r.right, e.innerText]; }).sort((a, b) => a[0] - b[0]);
  for (let i = 1; i < xl.length; i++) if (xl[i][0] - xl[i - 1][1] < 6) add('XLABEL_OVERLAP', xl[i - 1][2].split('\n')[0] + ' / ' + xl[i][2].split('\n')[0]);
  // 2d. dotted foot line under the note on every slide (Pierre 11 Nov: missing on the 100 live radars)
  const fl = s.querySelector('.foot-line'); if (!fl || !fl.getBoundingClientRect().width) add('FOOT_LINE', 'missing');
  // 3. logos: no initials tile
  const nt = s.querySelectorAll('.nt').length; if (nt) add('LOGO_MISSING', nt + ' name tile(s)');

  // 5. tables centered vertically between title and note, horizontal lines reach the last column
  if (['pp_killers', 'pp_survivors', 'pp_winner', 'pp_pains', 'pp_tech'].includes(T)) {
    const items = [...s.querySelectorAll('[class^="pp-"], .lt')].filter(e => e.offsetParent && R(e).height > 0); let a = 1e9, b = -1e9;
    items.forEach(e => { const r = R(e); a = Math.min(a, r.top - S.top); b = Math.max(b, r.bottom - S.top); });
    const note = s.querySelector('.note'); const nt = note ? R(note).top - S.top : 600; const mid = (tb + nt) / 2, c = (a + b) / 2;
    if (Math.abs(c - mid) > 22) add('NOT_VCENTERED', `block center ${Math.round(c)} vs ${Math.round(mid)}`);
    const lines = [...s.querySelectorAll('.pp-kl')]; if (lines.length) {
      const L = Math.max(...lines.map(l => R(l).right)); const C = Math.max(...[...s.querySelectorAll('.pp-kc, .pp-kz, .pp-td, .pp-wk, .pp-kh')].map(e => R(e).right));
      if (C > L + 2) add('LINES_SHORT', `content ends ${Math.round(C - S.left)}, lines end ${Math.round(L - S.left)}`); }
  }
  // 6. donut: every category shows at least 2 logos
  if (T.startsWith('pp_donut')) s.querySelectorAll('.pp-dl').forEach(d => { const k = d.querySelectorAll('.lt').length; if (k < 2) add('DONUT_LOGOS', `${k} logo(s): ${d.innerText.split('\n')[0]}`); });
  // 7. ticks and crosses: the mark is drawn, never a font glyph
  s.querySelectorAll('.pp-ok, .pp-no, .pp-wk').forEach(e => { if (getComputedStyle(e, '::after').content !== 'none') add('MARK_GLYPH', e.className); });
  if (T === 'pp_trends') { const pl = s.querySelector('polyline'), ex = s.querySelector('.pp-expl'); if (pl && ex && R(pl).top < R(ex).bottom + 10) add('CURVE_HITS_TEXT', Math.round(R(ex).bottom - R(pl).top)); }
  s.querySelectorAll('.pp-big, .pp-stat, .pp-cagr, .pp-rv, .pp-bv').forEach(e => { if (lines(e) > 1 && e.className !== 'pp-stat') add('ONE_LINE', e.innerText.slice(0, 20)); });
  // 4. per series rules
  if (T === 'pp_pains') { const r = s.querySelectorAll('.pp-pt').length; if (r !== 6) add('PAINS_ROWS', r); s.querySelectorAll('.pp-ph').forEach(h => { if (lines(h) !== 2) add('AUD_LINES', h.innerText); }); }
  if (T === 'pp_drivers') { const c = [...s.querySelectorAll('.pp-dy')].length; if (c !== 30) add('DRIVERS_ROWS', c); }
  if (T === 'pp_killers' || T === 'pp_survivors') { const c = s.querySelectorAll('.pp-kn, .pp-sl').length / (T === 'pp_survivors' ? 2 : 1); if (c < 5) add('KILLERS_ROWS', c); }
  if (T === 'pp_winner') { const c = s.querySelectorAll('.pp-wc').length, k = s.querySelectorAll('.pp-wn').length; if (c < 6 || c > 7) add('WINNER_ROWS', c); if (k < 5 || k > 6) add('WINNER_COLS', k); }
  if (T === 'pp_risks') s.querySelectorAll('.pp-rt').forEach(e => { if (lines(e) !== 3) add('RISK_LINES', lines(e) + ' ' + e.innerText.slice(0, 30)); });
  if (T === 'pp_value') s.querySelectorAll('.pp-vg').forEach(g => { const p = g.querySelector('p'), c = g.querySelector('.pp-vcard'); const over = R(p).width - R(c).width; if (over > 75) add('VALUE_LABEL', p.innerText.slice(0, 30) + ' +' + Math.round(over)); });
  if (T === 'pp_drivers') s.querySelectorAll('.pp-dt').forEach(e => { const col = e.getBoundingClientRect(); const push = [...s.querySelectorAll('.pp-dp')].find(p => Math.abs(R(p).top - col.top) < 12 && R(p).left > col.left); if (push && R(push).left - col.right < 8) add('DRIVER_TEXT_LONG', e.innerText.slice(0, 30)); });
});
return out; }"""
def run(slug):
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={'width': 960, 'height': 672})
        pg.goto(f'file:///home/claude/nmp-decks/decks/{slug}/deck.html'); pg.wait_for_timeout(1500)
        pg.add_style_tag(content='.slide{margin:0!important}')
        r = pg.evaluate(JS); b.close()
    for x in r: print(*x, sep=' | ')
    print(len(r), 'issues'); return r
if __name__ == '__main__': run(sys.argv[1])
