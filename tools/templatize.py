"""Turn every raw slide of a deck into a template + data (Pierre, 12 Nov 2026: « un modèle par slide distinct »).

    python3 tools/templatize.py decks/edtech-full

For each raw slide:
  - the HTML skeleton (shapes, positions, styles) goes to templates/slides/x/<name>.j2;
  - the words and images go to deck.yaml: `t: {box_k: text}` and `img: [src, ...]`.
Slides whose skeleton is byte-identical share one template (the pages of a series).

Text format in deck.yaml (one string per text box):
  - one line per paragraph ("\n"); an empty line is an empty paragraph;
  - the paragraph styles of the template are used in order (extra paragraphs reuse the last one);
  - a run in another style than the paragraph's main one is written {n|text}, n = run style index in the template.
The rendering filter `rt` lives in build.py.
"""
import sys, re, json, html as H, hashlib, yaml
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BOX = re.compile(r'(<div class="rx-t"[^>]*>)(.*?)</div>', re.S)
PAR = re.compile(r'<p style="([^"]*)">(.*?)</p>', re.S)
RUN = re.compile(r'<span style="([^"]*)">(.*?)</span>', re.S)
IMG = re.compile(r'(<img class="rx-i" src=")([^"]+)(")')


def box_split(inner):
    """-> (paragraph styles, run styles, text) for one text box."""
    pst, rst, lines, mains = [], [], [], []
    for ps, body in PAR.findall(inner):
        if ps not in pst: pst.append(ps)
        runs = [(a, b, c) for a, b, c in re.findall(r'<span style="([^"]*)">(.*?)</span>((?:(?!<span).)*)', body, re.S)]
        lead = re.split(r'<span', body, maxsplit=1)[0] if '<span' in body else ''
        assert not lead.strip(), lead
        if not runs:
            assert body.strip() in ('&nbsp;', ''), body
            lines.append(('', ps, [])); continue
        for s, _, _ in runs:
            if s not in rst: rst.append(s)
        lines.append((None, ps, runs))
    # main run style of each paragraph = its first run's style; paragraph i takes paragraph style i (last one repeats)
    out, pmap, mmap = [], [], []
    for _, ps, runs in lines:
        pmap.append(pst.index(ps)); mmap.append(rst.index(runs[0][0]) if runs else -1)
    # the template keeps the per-paragraph style sequence; the text only marks runs that differ from their paragraph's first run
    for (_, ps, runs), m in zip(lines, mmap):
        if not runs: out.append(''); continue
        t = ''
        for i, (s, txt, gap) in enumerate(runs):
            txt = H.unescape(txt); gap = H.unescape(gap)
            assert '{' not in txt + gap and '|' not in txt + gap and '}' not in txt + gap, txt
            t += txt if (i == 0 or rst.index(s) == m) else '{%d|%s}' % (rst.index(s), txt)
            t += gap                     # text between two runs (a space, a <br>) joins the main run
        out.append(t)
    return pst, rst, pmap, mmap, '\n'.join(out)


def slug(s, n=5):
    w = re.findall(r'[a-z0-9]+', (s or '').lower())
    stop = {'the', 'a', 'an', 'of', 'in', 'on', 'to', 'and', 'is', 'are', 'what', 'how', 'which', 'who', 'do', 'does', 'it', 'its', 'for', 'we', 'by', 'with', 'that', 'this', 'they', 'can', 'be'}
    w = [x for x in w if x not in stop and x != 'edtech'][:n]
    return '_'.join(w) or 'untitled'


def main(deck_dir):
    deck_dir = Path(deck_dir); f = deck_dir / 'deck.yaml'
    deck = yaml.safe_load(f.read_text())
    tdir = ROOT / 'templates/slides/x'; tdir.mkdir(parents=True, exist_ok=True)
    seen, names = {}, set(p.stem for p in tdir.glob('*.j2'))
    made = 0
    for s in deck['slides']:
        if s.get('type') != 'raw': continue
        src_html = s['html']; texts = {}; boxes = []

        def sub_box(m):
            head, inner = m.group(1), m.group(2)
            k = re.search(r'data-k="(\d+)"', head).group(1)
            pst, rst, pmap, mmap, txt = box_split(inner)
            texts[int(k)] = txt
            return '%s{{ rt(s.t[%s], %s, %s, %s, %s) }}</div>' % (head, k, json.dumps(pst), json.dumps(rst), json.dumps(pmap), json.dumps(mmap))
        sk = BOX.sub(sub_box, src_html)
        imgs = []
        def sub_img(m):
            imgs.append(m.group(2)); return '%s{{ s.img[%d] }}%s' % (m.group(1), len(imgs) - 1, m.group(3))
        sk = IMG.sub(sub_img, sk)
        sk = '{# raw-derived template: geometry from the PPTX, words in deck.yaml (t, img) #}\n<div class="raw">' + sk + '</div>\n'
        hsh = hashlib.sha1(sk.encode()).hexdigest()
        if hsh not in seen:
            base = s.pop('tpl_hint', None) or slug(s.get('title') or (s.get('section', '') + ' divider')); name = base; i = 2
            while name in names: name = f'{base}_{i}'; i += 1
            names.add(name); seen[hsh] = name
            (tdir / f'{name}.j2').write_text(sk); made += 1
        s.pop('tpl_hint', None); s['type'] = 'x/' + seen[hsh]; del s['html']
        s['t'] = texts
        if imgs: s['img'] = imgs
    f.write_text(yaml.dump(deck, allow_unicode=True, sort_keys=False, width=1000))
    print(f'{made} templates written to templates/slides/x/, deck.yaml rewritten')


if __name__ == '__main__':
    main(sys.argv[1])
