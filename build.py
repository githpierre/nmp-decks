#!/usr/bin/env python3
"""Build a NewMarketPitch deck: decks/<slug>/deck.yaml -> deck.html -> PDF (+ PNG previews + layout audit).

Usage:
  python3 build.py edtech                 # HTML + PDF + audit
  python3 build.py edtech --png           # also one PNG per slide in decks/<slug>/out/png
  python3 build.py edtech --only 3,7      # PNG of some slides only (fast review)
"""
import sys, re, json, argparse, pathlib, yaml
from jinja2 import Environment, FileSystemLoader
from markupsafe import Markup, escape

ROOT = pathlib.Path(__file__).resolve().parent

def nl(t):
    return Markup('<br>'.join(escape(x.strip()) for x in str(t).split('\n')))

def sentences(t):
    """Two sentences in a dated item = two lines (one sentence per line), so every item of the list has the same shape."""
    parts = re.split(r'(?<=[.!?])\s+(?=[A-Z0-9$])', str(t).strip())
    return Markup('<br>'.join(str(md(p)) for p in parts))

def md(t):
    s = str(escape(str(t)))
    s = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', s)
    s = re.sub(r'\[(.+?)\]\((https?://[^)\s]+)\)', r'<a href="\2">\1</a>', s)
    return Markup(s.replace('\n', '<br>'))

AUDIT_JS = r"""
() => {
  const out = [];
  document.querySelectorAll('.slide').forEach((sl) => {
    const n = sl.dataset.n, R = sl.getBoundingClientRect();
    sl.querySelectorAll('*').forEach(el => {
      const cs = getComputedStyle(el);
      if (cs.display === 'none' || !el.textContent.trim() && el.children.length === 0 && !el.matches('img,.bar,.fill,.dot')) return;
      const r = el.getBoundingClientRect();
      if (r.width === 0 || r.height === 0) return;
      if (r.left < R.left - 1 || r.right > R.right + 1 || r.top < R.top - 1 || r.bottom > R.bottom + 1)
        out.push([n, 'OUTSIDE', el.className || el.tagName, el.textContent.trim().slice(0, 50)]);
      if ((el.scrollWidth > el.clientWidth + 2 && cs.overflow !== 'visible') || el.scrollHeight > el.clientHeight + 2 && cs.overflow === 'hidden')
        if (!el.classList.contains('slide')) out.push([n, 'OVERFLOW', el.className || el.tagName, el.textContent.trim().slice(0, 50)]);
    });
    // body content must not collide with the footnote or the title
    const note = sl.querySelector('.note'), body = sl.querySelector('.body > *'), title = sl.querySelector('.title,.subtitle:last-of-type');
    if (note && body) { const a = body.getBoundingClientRect(), b = note.getBoundingClientRect(); if (a.bottom > b.top - 4) out.push([n, 'HITS_NOTE', '', '']); }
    if (title && body) { const a = body.getBoundingClientRect(), b = sl.querySelector('.title').getBoundingClientRect(); if (a.top < b.bottom + 4) out.push([n, 'HITS_TITLE', '', '']); }
    // dated lists: every item on the same number of lines
    const dl = [...sl.querySelectorAll('.dated .tx')].map(e => { const lh = parseFloat(getComputedStyle(e).lineHeight); return Math.round((e.getBoundingClientRect().height - 20) / lh); });
    if (dl.length && new Set(dl).size > 1) out.push([n, 'DATED_LINES', dl.join(','), '']);
    // contrast boxes: text fills 70-90% of the box width
    sl.querySelectorAll('.contrast .a, .contrast .b').forEach(el => { const rg = document.createRange(); rg.selectNodeContents(el);
      const w = rg.getBoundingClientRect().width, cs = getComputedStyle(el), inner = el.clientWidth - parseFloat(cs.paddingLeft) - parseFloat(cs.paddingRight);
      const f = w / inner; if (f < 0.70 || f > 0.90) out.push([n, 'FILL', Math.round(f * 100) + '%', el.textContent.trim()]); });
    // decorative arrows centered on their bar
    sl.querySelectorAll('.vbars .col').forEach(c => { const a = c.querySelector('.down'), b = c.querySelector('.bar'); if (!a || !b) return;
      const ra = a.getBoundingClientRect(), rb = b.getBoundingClientRect(); if (Math.abs((ra.left + ra.right) / 2 - (rb.left + rb.right) / 2) > 1.5) out.push([n, 'ARROW_OFFCENTER', '', '']); });
    // titles: max 2 lines
    const t = sl.querySelector('.title'); if (t) { const lh = parseFloat(getComputedStyle(t).lineHeight); if (t.getBoundingClientRect().height > lh * 2.2) out.push([n, 'TITLE_LINES', '', t.textContent.slice(0, 50)]); }
    // footnote must stop before the footer label (x 690)
    { const ntb = sl.querySelector('.note'); if (ntb) { const r = Math.max(...[...ntb.querySelectorAll('.nl')].map(e => e.getBoundingClientRect().right), ntb.getBoundingClientRect().right) - sl.getBoundingClientRect().left; if (r > 690) out.push([n, 'NOTE_WIDTH', Math.round(r) + 'px', ntb.textContent.slice(0, 50)]); } }
    // footnote lines (YAML list): widths within 12% of each other (Pierre, 10 Nov 2026)
    const nls = [...sl.querySelectorAll('.note .nl')].map(e => e.getBoundingClientRect().width);
    if (nls.length > 1) { const mx = Math.max(...nls), mn = Math.min(...nls); if ((mx - mn) / mx > 0.12) out.push([n, 'NOTE_BALANCE', Math.round((mx - mn) / mx * 100) + '%', sl.querySelector('.note').textContent.slice(0, 50)]); }
    const nt = sl.querySelector('.note'); if (nt) { const lh = parseFloat(getComputedStyle(nt).lineHeight); if (nt.getBoundingClientRect().height > lh * 3.2) out.push([n, 'NOTE_LINES', '', nt.textContent.slice(0, 50)]); }
  });
  return out;
}
"""

def check_yaml(node, path='deck'):
    """YAML trap: an unquoted comma inside {k: v, ...} silently cuts a sentence into an empty key. Refuse it."""
    if isinstance(node, dict):
        for k, v in node.items():
            if v is None: raise SystemExit(f'YAML: empty value at {path}.{k!r} (quote texts that contain a comma)')
            check_yaml(v, f'{path}.{k}')
    elif isinstance(node, list):
        for i, v in enumerate(node): check_yaml(v, f'{path}[{i}]')

def prepare_cover(s, d, W=960, H=672):
    """Cover disclaimer: left-aligned with the title (x 52), bottom aligned with the button, 6.5 pt.
    Take the widest width (300 -> 200 px) whose area stays on a dark part of the photo (95th percentile luminance < 110)."""
    from PIL import Image
    im = Image.open(d / s['image']).convert('L'); iw, ih = im.size
    sc = max(W / iw, H / ih); im = im.resize((round(iw * sc), round(ih * sc))); ox, oy = (im.width - W) // 2, (im.height - H) // 2
    n = len(s.get('disclaimer', ''))
    for w in (300, 280, 260, 240, 220, 200):
        h = -(-n * 4.05 // w) * 13                      # lines x line height at 6.5 pt
        box = im.crop((ox + 50, oy + H - 20 - h - 2, ox + 52 + w + 4, oy + H - 18))
        px = sorted(box.getdata()); p95 = px[int(len(px) * .95)]
        if p95 < 110: break
    s.setdefault('disc_style', f'width:{w}px'); s['_disc_p95'] = p95
    # title: free dark width = first column (x >= 300) of the title band (rows 180-460) where the photo gets bright
    if not s.get('title_maxw'):
        band = im.crop((ox, oy + 180, ox + W, oy + 460)); free = W
        for x in range(300, W, 4):
            col = sorted(band.crop((x, 0, x + 4, band.height)).getdata())
            if col[int(len(col) * .97)] > 110: free = x; break
        s['title_maxw'] = max(300, min(560, free - 52 - 28))

def hash_int(s):
    import hashlib
    return int(hashlib.md5(s.encode()).hexdigest(), 16)

def prepare_logogrid(s, CW=235, RH=112, L=36):
    """Place the logos of the top companies grid. x is authored (0-3 stage scale, 1.0/2.0 = on a border): it carries meaning.
    y is computed: 3 lanes per row, each logo takes the lane farthest from its neighbours, so nothing overlaps (no randomness)."""
    lanes = [0.30, 0.72, 0.51]
    for r in s['rows']:
        pos = []
        for lg in sorted(r['logos'], key=lambda d: d['x']):
            best = max(lanes, key=lambda y: min([((lg['x'] - p['x']) * CW) ** 2 + ((y - p['y']) * RH) ** 2 for p in pos] or [9e9]))
            j = ((hash_int(lg['l']) % 13) - 6) / 100      # -0.06..+0.06, stable per company
            pos.append({'l': lg['l'], 'x': lg['x'], 'y': best + j})
        for a in pos:
            for b in pos:
                if a is not b and abs((a['x'] - b['x']) * CW) < L + 4 and abs((a['y'] - b['y']) * RH) < L + 4:
                    raise SystemExit(f"logogrid: {a['l']} and {b['l']} overlap in row {r['name']}: change their x")
        r['_pos'] = pos

def build(slug, png=False, only=None):
    d = ROOT / 'decks' / slug
    deck = yaml.safe_load((d / 'deck.yaml').read_text())
    check_yaml(deck)
    for s in deck['slides']:
        if s.get('type') == 'logogrid': prepare_logogrid(s)
        if s.get('type') == 'cover': prepare_cover(s, d)
        if s.get('type') == 'dated' and len(s.get('items', [])) != 6:
            raise SystemExit(f"dated list must have exactly 6 dates (has {len(s.get('items', []))}): {s.get('title')}")
        if s.get('type') == 'contrast':
            for r in s['rows']:
                if len(r) != 2: raise SystemExit(f'contrast row cut by a comma (quote it): {r}')
    env = Environment(loader=FileSystemLoader(str(ROOT / 'templates')), autoescape=True)
    env.filters['nl'] = nl; env.filters['md'] = md; env.filters['sentences'] = sentences
    import math; env.filters['cos'] = math.cos; env.filters['sin'] = math.sin
    html = env.get_template('base.html.j2').render(deck=deck, slides=deck['slides'])
    (d / 'deck.html').write_text(html)
    out = d / 'out'; out.mkdir(exist_ok=True)
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={'width': 960, 'height': 672})
        pg.goto((d / 'deck.html').as_uri()); pg.wait_for_load_state('networkidle')
        pg.evaluate('document.fonts.ready')
        issues = pg.evaluate(AUDIT_JS)
        name = f"{deck['market']} - {deck['quarter']} - newmarketpitch.com ©.pdf"
        pg.emulate_media(media='print')
        pg.pdf(path=str(out / name), width='10in', height='7in', print_background=True, prefer_css_page_size=True)
        if png or only:
            pg.emulate_media(media='screen')
            (out / 'png').mkdir(exist_ok=True)
            pg.add_style_tag(content='.slide{margin:0!important}body{background:#062A3C}')
            for i, el in enumerate(pg.query_selector_all('.slide'), 1):
                if only and i not in only: continue
                el.screenshot(path=str(out / 'png' / f'{i:03d}.png'))
        b.close()
    for x in issues: print(*x, sep=' | ')
    print(f'{len(deck["slides"])} slides, {len(issues)} issues ->', out / name)
    return issues

if __name__ == '__main__':
    a = argparse.ArgumentParser(); a.add_argument('slug'); a.add_argument('--png', action='store_true'); a.add_argument('--only')
    o = a.parse_args()
    build(o.slug, o.png, [int(x) for x in o.only.split(',')] if o.only else None)
