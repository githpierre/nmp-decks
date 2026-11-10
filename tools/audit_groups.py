"""Audit of parallel text boxes (Pierre's rules, 10 Nov 2026), on a built deck.html:
 - boxes of the same group (same width, aligned on a row or a column) must have the SAME number of lines;
 - every multi-line text is balanced (lines within 12 % of each other, last line included);
 - a box is well filled: the longest line uses at least 70 % of the inner width (else add words);
Usage: python3 tools/audit_groups.py decks/<slug> [slide numbers...]  -> prints issues, writes <deck>/audit_groups.json"""
import json, pathlib, sys
from playwright.sync_api import sync_playwright

JS = r"""(only) => {
  const res = [];
  document.querySelectorAll('.slide').forEach((sl, si) => {
    const n = si + 1; if (only.length && !only.includes(n)) return;
    const S = sl.getBoundingClientRect();
    const T = [...sl.querySelectorAll('.raw .rx-t')].map(el => {
      const ps = [...el.querySelectorAll('p')].filter(p => p.textContent.trim() && /[a-z]/i.test(p.textContent));
      if (!ps.length) return null;
      const p = ps[ps.length - 1];                       // main text = last paragraph with letters
      const rows = {}; const tw = document.createTreeWalker(p, NodeFilter.SHOW_TEXT); let nd;
      while ((nd = tw.nextNode())) { const rg = document.createRange(); rg.selectNodeContents(nd);
        [...rg.getClientRects()].forEach(r => { if (r.width < 1) return; const k = Math.round(r.top); rows[k] = (rows[k] || 0) + r.width; }); }
      const tops = Object.keys(rows).map(Number).sort((a, b) => a - b);
      const merged = []; tops.forEach(t => { if (merged.length && t - merged[merged.length - 1][0] < 4) merged[merged.length - 1][1] += rows[t]; else merged.push([t, rows[t]]); });
      const b = el.getBoundingClientRect(), cs = getComputedStyle(el);
      const inner = b.width - parseFloat(cs.paddingLeft) - parseFloat(cs.paddingRight);
      return {k: el.dataset.k, x: Math.round(b.left - S.left), y: Math.round(b.top - S.top), w: Math.round(b.width), lines: merged.length,
              widths: merged.map(m => Math.round(m[1])), inner: Math.round(inner), text: p.textContent.trim(), np: ps.length, fs: getComputedStyle(p).fontSize, col: getComputedStyle(p.querySelector('span') || p).color};
    }).filter(Boolean).filter(t => t.text.length > 12);
    // groups: same width (+-3) and same row (y +-4) or same column (x +-4)
    const used = new Set(), groups = [];
    T.forEach((a, i) => { if (used.has(i)) return;
      const g = T.map((b, j) => [b, j]).filter(([b, j]) => !used.has(j) && Math.abs(b.w - a.w) <= 3 && b.fs === a.fs && b.col === a.col && (Math.abs(b.y - a.y) <= 4 || Math.abs(b.x - a.x) <= 4));
      if (g.length >= 2) { g.forEach(([b, j]) => used.add(j)); groups.push(g.map(([b]) => b)); } });
    // also: groups linked through a common member (row of a grid shares y with another row member)
    groups.forEach(g => {
      const L = g.map(t => t.lines), maxL = Math.max(...L);
      const issues = [];
      if (new Set(L).size > 1) issues.push('LINES ' + L.join(','));
      g.forEach(t => {
        if (t.lines > 1 && t.lines <= 4) { const mx = Math.max(...t.widths), mn = Math.min(...t.widths); if ((mx - mn) / mx > (t.lines == 2 ? 0.12 : 0.25)) issues.push(`BALANCE ${t.k} ${Math.round((mx - mn) / mx * 100)}%`); }
        const fill = Math.max(...t.widths) / t.inner; if (fill < 0.7 && t.lines <= 6 && t.text.split(/\s+/).length >= 6) issues.push(`FILL ${t.k} ${Math.round(fill * 100)}%`);
      });
      res.push({n, issues, items: g});
    });
  });
  return res;
}"""

def run(deck, only=()):
    d = pathlib.Path(deck).resolve()
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={'width': 960, 'height': 672})
        pg.goto((d / 'deck.html').as_uri()); pg.wait_for_load_state('load'); pg.evaluate('document.fonts.ready'); pg.wait_for_function('window.__rawfit === true', timeout=60000)
        r = pg.evaluate(JS, list(only)); b.close()
    (d / 'audit_groups.json').write_text(json.dumps(r, ensure_ascii=False, indent=1))
    return r

if __name__ == '__main__':
    r = run(sys.argv[1], [int(x) for x in sys.argv[2:]])
    bad = [g for g in r if g['issues']]
    for g in bad: print(g['n'], '|', '; '.join(g['issues'][:6]))
    print(len(bad), 'groups with issues out of', len(r))
