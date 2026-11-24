"""Slides whose data changed since the last build (piste C, Pierre 18 Nov 2026): compares decks/<h>/deck.yaml with
decks/<h>/out/last_deck.yaml slide by slide (by id) and prints their numbers « 4,9,31 » (empty: nothing changed, ALL: first build).
    python3 tools/changed_slides.py <handle> [--save]"""
import sys, yaml, pathlib
D = pathlib.Path(__file__).resolve().parent.parent / 'decks' / sys.argv[1]; last = D / 'out/last_deck.yaml'
if '--save' in sys.argv: last.write_text((D / 'deck.yaml').read_text()); sys.exit()
new = yaml.safe_load((D / 'deck.yaml').read_text())['slides']
if not last.exists(): print('ALL'); sys.exit()
R = D.parent.parent; code = [R / 'build.py', R / 'templates/rawfit.js', R / 'tools/pp/pp_prepare.py',   # pp_prepare lays out the product-page twins (Neocloud, 19 Nov 2026: a donut fix was not rebuilt)
        *R.glob('templates/**/*.j2'), *R.glob('tools/atelier2/*.js'), *R.glob('tools/atelier2/*.json')]
if max(p.stat().st_mtime for p in code if p.exists()) > last.stat().st_mtime: print('ALL'); sys.exit()   # a template or a fix changed: it can move any slide
old = {s.get('id'): s for s in yaml.safe_load(last.read_text())['slides']}
ch = [str(i) for i, s in enumerate(new, 1) if old.get(s.get('id')) != s]
print('ALL' if len(new) != len(old) or len(ch) > 40 else ','.join(ch))   # slides added or removed: numbers move, full build
