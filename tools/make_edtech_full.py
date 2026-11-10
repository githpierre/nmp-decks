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
prs = Presentation(str(SRC)); theme = pptx2html.theme_colors(prs); slides = []
for i, sl in enumerate(prs.slides, 1):
    if i in TEMPLATED: s = dict(PS[TEMPLATED[i]])
    elif i in AGENDA: s = dict(type='agenda', section=None, current=AGENDA[i])
    else:
        r = pptx2html.convert(sl, theme, media, 'media/raw')
        s = dict(type='raw', html=r['html'])
        for k in ('section', 'title', 'page', 'note'):
            if r[k]: s[k] = r[k]
    if s['type'] == 'agenda' and not s.get('section'):
        r = pptx2html.convert(sl, theme, media, 'media/raw'); s['section'] = r['section'] or 'EdTech market'
    s['src'] = i
    slides.append(s)
deck = dict(proto); deck.update(slug='edtech-full', slides=slides)
(out / 'deck.yaml').write_text(yaml.dump(deck, allow_unicode=True, sort_keys=False, width=1000))
print(len(slides), 'slides,', sum(1 for s in slides if s['type'] == 'raw'), 'converted as-is')
