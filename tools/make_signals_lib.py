"""Signal slides library (Pierre, 12 Nov 2026): the complementary slides that go into a deck only when the research finds a strong signal.
Source: the 33 series PowerPoints of the Drive folder « temp - … - to add to other decks » (one file per format).

    python3 tools/make_signals_lib.py /home/claude/sig/src     -> decks/signals/deck.yaml + templates/slides/x/sig_*.j2

Per format: its first slide (the example) + every cell-therapy slide (usable for in vivo CAR-T).
A signal slide has no fixed chapter: its kicker is set when it is placed (Market opportunity, Market challenges, Growth drivers…)."""
import pathlib, re, sys, yaml
from pptx import Presentation
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import pptx2html, templatize
ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = pathlib.Path(sys.argv[1])
out = ROOT / 'decks/signals'; media = out / 'media/raw'; media.mkdir(parents=True, exist_ok=True)
slides = []
for f in sorted(SRC.glob('*.pptx')):
    fmt = f.stem
    prs = Presentation(str(f)); theme = pptx2html.theme_colors(prs)
    for i, sl in enumerate(prs.slides, 1):
        tx = ' '.join(sh.text_frame.text for sh in sl.shapes if sh.has_text_frame)
        cell = 'C E L L' in tx          # the market label of the slide (letter-spaced) says cell therapy
        if i != 1 and not cell: continue
        r = pptx2html.convert(sl, theme, media, 'media/raw')
        s = dict(type='raw', html=r['html'], signal=fmt, src=f'{fmt}#{i}', tpl_hint=f'sig_{fmt.replace("-", "_")}')
        for k in ('section', 'title', 'page', 'note'):
            if r[k]: s[k] = r[k]
        if cell: s['market'] = 'cell therapy'
        slides.append(s)
deck = dict(market='Signals library', label='Signals library', quarter='', slug='signals', slides=slides)
(out / 'deck.yaml').write_text(yaml.dump(deck, allow_unicode=True, sort_keys=False, width=1000))
templatize.main(out)
print(len(slides), 'signal slides')
