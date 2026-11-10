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
  const els = [...s.querySelectorAll('.lt, [class^="pp-"]')].filter(e => !e.closest('.pp-abs') && e.offsetParent && !['pp-abs', 'pp-lead', 'pp-wcol', 'pp-rl', 'pp-kl', 'pp-pl', 'pp-dhl', 'pp-sdiv', 'pp-rs', 'pp-bar', 'pp-rbar', 'pp-rb', 'pp-vcard', 'pp-dlogos', 'pp-risk', 'pp-big', 'pp-rtr'].some(c => e.classList.contains(c)));
  for (let a = 0; a < els.length; a++) for (let b = a + 1; b < els.length; b++) {
    const A = els[a], B = els[b]; if (A.contains(B) || B.contains(A)) continue;
    const ra = R(A), rb = R(B); const gx = Math.max(ra.left, rb.left) - Math.min(ra.right, rb.right), gy = Math.max(ra.top, rb.top) - Math.min(ra.bottom, rb.bottom);
    if (gx < 0 && gy < 4) add('TOO_CLOSE', `${A.className.split(' ')[0]}|${(A.innerText||'logo').slice(0,18)} / ${B.className.split(' ')[0]}|${(B.innerText||'logo').slice(0,18)} gap ${Math.round(gy)}`);
  }
  // 3. logos: no initials tile
  const nt = s.querySelectorAll('.nt').length; if (nt) add('LOGO_MISSING', nt + ' name tile(s)');
  // 4. per series rules
  if (T === 'pp_pains') { const r = s.querySelectorAll('.pp-pt').length; if (r !== 6) add('PAINS_ROWS', r); s.querySelectorAll('.pp-ph').forEach(h => { if (lines(h) !== 2) add('AUD_LINES', h.innerText); }); }
  if (T === 'pp_drivers') { const c = [...s.querySelectorAll('.pp-dy')].length; if (c !== 30) add('DRIVERS_ROWS', c); }
  if (T === 'pp_killers' || T === 'pp_survivors') { const c = s.querySelectorAll('.pp-kn, .pp-sl').length / (T === 'pp_survivors' ? 2 : 1); if (c < 5) add('KILLERS_ROWS', c); }
  if (T === 'pp_winner') { const c = s.querySelectorAll('.pp-wc').length, k = s.querySelectorAll('.pp-wn').length; if (c < 6 || c > 7) add('WINNER_ROWS', c); if (k < 5 || k > 6) add('WINNER_COLS', k); }
  if (T === 'pp_risks') s.querySelectorAll('.pp-rt').forEach(e => { if (lines(e) !== 3) add('RISK_LINES', lines(e) + ' ' + e.innerText.slice(0, 30)); });
  if (T === 'pp_value') s.querySelectorAll('.pp-vg').forEach(g => { const p = g.querySelector('p'), c = g.querySelector('.pp-vcard'); const over = R(p).width - R(c).width; if (over > 40) add('VALUE_LABEL', p.innerText.slice(0, 30) + ' +' + Math.round(over)); });
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
