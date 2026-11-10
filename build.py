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
    // titles: max 2 lines
    const t = sl.querySelector('.title'); if (t) { const lh = parseFloat(getComputedStyle(t).lineHeight); if (t.getBoundingClientRect().height > lh * 2.2) out.push([n, 'TITLE_LINES', '', t.textContent.slice(0, 50)]); }
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

def build(slug, png=False, only=None):
    d = ROOT / 'decks' / slug
    deck = yaml.safe_load((d / 'deck.yaml').read_text())
    check_yaml(deck)
    env = Environment(loader=FileSystemLoader(str(ROOT / 'templates')), autoescape=True)
    env.filters['nl'] = nl; env.filters['md'] = md
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
