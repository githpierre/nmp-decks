"""Builds decks/edtech-full: the whole EdTech deck (221 slides) from the original PowerPoint.
Slides that already have a template keep the prototype content (decks/edtech/deck.yaml); chapter pages use the agenda template;
every other slide is converted as-is by tools/pptx2html.py (type raw) until it gets its own template."""
import pathlib, sys, yaml
from pptx import Presentation
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import pptx2html
ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else pathlib.Path('/home/claude/src/edtech.pptx')
proto = yaml.safe_load((ROOT / 'decks/edtech/deck.yaml').read_text())
PS = proto['slides']
TEMPLATED = {1: 0, 4: 1, 6: 2, 14: 3, 17: 4, 24: 5, 25: 6, 33: 7, 42: 8, 46: 9, 47: 10, 49: 11, 52: 12, 65: 13, 69: 14, 73: 15,
             158: 16, 171: 17, 210: 18, 211: 19, 212: 20, 213: 21, 214: 22}
AGENDA = {5: 1, 26: 2, 40: 3, 53: 4, 86: 5, 100: 6, 131: 7, 146: 8, 155: 9, 170: 10, 191: 11, 203: 12}
out = ROOT / 'decks/edtech-full'; media = out / 'media/raw'; media.mkdir(parents=True, exist_ok=True)
(out / 'media/cover.jpg').write_bytes((ROOT / 'decks/edtech/media/cover.jpg').read_bytes())
OV = yaml.safe_load((out / 'overrides.yaml').read_text()) if (out / 'overrides.yaml').exists() else {}
def priority(sl, r):
    """A converted priority matrix (+ / ++ / +++ cells) becomes the 'priority' template, like the hand-made ones (same type, same look)."""
    T = [(sh.left, sh.top, sh.text_frame.text.strip()) for sh in sl.shapes if sh.has_text_frame and sh.text_frame.text.strip()]
    cells = [t for t in T if t[2] in ('+', '++', '+++')]
    if len(cells) < 15: return None
    xs = sorted({c[0] for c in cells}); x0, x1 = xs[0], xs[-1]
    rows = sorted({min((c[1] for c in cells), key=lambda v: abs(v - y)) for y in [c[1] for c in cells]})
    ys = []
    for y in sorted(c[1] for c in cells):
        if not ys or y - ys[-1] > 12700 * 8: ys.append(y)
    near = lambda a, b: abs(a - b) < 12700 * 8
    pains = [t for t in T if t[0] < x0 and len(t[2]) > 12 and any(near(t[1], y) for y in ys)]
    pr = [t for t in T if t[0] > x1 and t[2].isupper() and any(near(t[1], y) for y in ys)]
    icons = [t[2] for t in sorted((t for t in T if x0 - 12700 * 5 <= t[0] <= x1 + 12700 * 5 and t[1] < ys[0] - 12700 * 10 and len(t[2]) <= 3 and not t[2].isalnum()), key=lambda t: t[0])]
    sub = [t[2] for t in T if 12700 * 100 < t[1] < 12700 * 140 and t[2].isupper() and len(t[2]) > 3]
    out = []
    for y in ys:
        p_ = next((t[2] for t in pains if near(t[1], y)), ''); q = next((t[2] for t in pr if near(t[1], y)), '')
        out.append(dict(pain=' '.join(p_.split()), s=[len(c[2]) for c in sorted((c for c in cells if near(c[1], y)), key=lambda c: c[0])], p=q))
    title = '\n'.join(l.strip() for l in (r['title'] or '').split('\n')) if r.get('title') else 'Which pains deserve\nattention first?'
    return dict(type='priority', section=r.get('section') or 'Pain points', title=title, subtitle=(sub[0].capitalize() if sub else ''), icons=icons, rows=out, note=r.get('note'))


prs = Presentation(str(SRC)); theme = pptx2html.theme_colors(prs); slides = []
for i, sl in enumerate(prs.slides, 1):
    if i in TEMPLATED: s = dict(PS[TEMPLATED[i]])
    elif i in AGENDA: s = dict(type='agenda', section=None, current=AGENDA[i])
    else:
        r = pptx2html.convert(sl, theme, media, 'media/raw', {int(k): v for k, v in (OV.get(i) or {}).items()})
        s = priority(sl, r) or dict(type='raw', html=r['html'])
        if s['type'] == 'raw':
            for k in ('section', 'title', 'page', 'note'):
                if r[k]: s[k] = r[k]
    if s['type'] == 'agenda' and not s.get('section'):
        r = pptx2html.convert(sl, theme, media, 'media/raw'); s['section'] = r['section'] or 'EdTech market'
    s['src'] = i
    slides.append(s)
deck = dict(proto)
# a section kicker that is just the market name ('EDTECH MARKET') is a converter slip: the slide keeps its chapter (11 Nov)
for i, sl_ in enumerate(slides):
    if i and sl_['type'] == 'raw' and str(sl_.get('section') or '').lower().endswith(' market') and slides[i - 1].get('section'):
        sl_['section'] = slides[i - 1]['section']
deck.update(slug='edtech-full', slides=slides, scripts=['decisions.js'])
(out / 'deck.yaml').write_text(yaml.dump(deck, allow_unicode=True, sort_keys=False, width=1000))
print(len(slides), 'slides,', sum(1 for s in slides if s['type'] == 'raw'), 'converted as-is')
