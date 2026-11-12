"""Cover geometry copied from Pierre's cover slide (Google Slides « nmp - cover deck (1-225) », slide number = market uuid).

    1. Read the slide with the Google Slides tool, fields:
       pageElements(size,transform,image(contentUrl,imageProperties(cropProperties,transparency)),shape(shapeProperties.contentAlignment,text.textElements(textRun(content,style(fontSize)))))
       and save the answer as decks/<handle>/cover_slide.json
    2. python3 tools/cover_from_slides.py <handle>      -> decks/<handle>/cover.yaml (read by the import)
                                                          + assets/covers/<handle>.jpg : every image layer of the slide, cropped, with its
                                                          transparency, flattened on the navy page (run it at once: the image links expire)
    3. Compare the built cover with the slide thumbnail, side by side, before going on.

Every cover of the deck has its own layout (photo crop, title size, where the disclaimer sits): the HTML cover copies it,
it is never laid out by a general rule (12 Nov 2026: Humanoid Robotics title drawn over the robots)."""
import json, sys, yaml
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
PX = 1 / 9525                       # EMU -> px on the 960 x 672 canvas
INSET = 9.6                         # default text-box inset of Google Slides (0.1 in)
d = ROOT / 'decks' / sys.argv[1]; P = json.loads((d / 'cover_slide.json').read_text())
P = P.get('content', P)['pageElements']; G = {}
import subprocess
from PIL import Image
W, H, K = 1920, 1344, 2                  # flattened photo, 2 px per canvas px
flat = Image.new('RGBA', (W, H), (6, 42, 60, 255)); n = 0
for e in P:
    if 'image' in e:                # image layers, back to front: a cut-out under the full photo at 50 % dims the background only (Humanoid Robotics)
        n += 1; f = d / f'cover_layer{n}.png'; ip = e['image'].get('imageProperties') or {}; c = ip.get('cropProperties') or {}; t = e.get('transform') or {}
        if not f.exists(): subprocess.run(['curl', '-sS', '-L', '-o', str(f), e['image']['contentUrl']], check=True)
        im = Image.open(f).convert('RGBA'); w, h = im.size
        im = im.crop((int(c.get('leftOffset', 0) * w), int(c.get('topOffset', 0) * h), int(w - c.get('rightOffset', 0) * w), int(h - c.get('bottomOffset', 0) * h)))
        bw, bh = e['size']['width']['magnitude'] * t.get('scaleX', 1) * PX * K, e['size']['height']['magnitude'] * t.get('scaleY', 1) * PX * K
        im = im.resize((round(bw), round(bh)), Image.LANCZOS); a = 1 - ip.get('transparency', 0)
        if a < 1: im.putalpha(im.getchannel('A').point(lambda v: int(v * a)))
        flat.alpha_composite(im, (round(t.get('translateX', 0) * PX * K), round(t.get('translateY', 0) * PX * K)) if t.get('translateX', 0) >= 0 and t.get('translateY', 0) >= 0 else (0, 0))
    sh = e.get('shape') or {}; runs = [r['textRun'] for r in (sh.get('text') or {}).get('textElements', []) if r.get('textRun')]
    if not runs: continue
    txt = ''.join(r['content'] for r in runs); pt = max(r['style']['fontSize']['magnitude'] for r in runs); t = e['transform']
    mid = (sh.get('shapeProperties') or {}).get('contentAlignment') == 'MIDDLE'
    box = dict(left=round(t.get('translateX', 0) * PX, 1), top=round(t.get('translateY', 0) * PX + (0 if mid else INSET), 1), width=round(3000000 * t.get('scaleX', 1) * PX, 1),
               height=round(3000000 * t.get('scaleY', 1) * PX, 1) if mid else 0, pt=pt)
    key = 'copyright' if txt.startswith('©') else 'disc' if 'This report' in txt else 'button' if 'NEWMARKETPITCH' in txt else 'sub' if 'M A R K E T' in txt else 'title'
    if key != 'button': G[key] = box
assert n and {'title', 'sub', 'disc'} <= set(G), G
flat.convert('RGB').save(ROOT / 'assets/covers' / f'{sys.argv[1]}.jpg', quality=92)
(d / 'cover.yaml').write_text(yaml.dump(dict(geo=G), sort_keys=False)); print(G)
