"""Logo tiles of a live product-page slide (2400x1680 webp with the page-lift border): crop each white tile and give its
center in deck coordinates (960 x 672), so a deck twin shows exactly the logos of the live slide.

    python3 tools/pp/live_tiles.py <slide.webp> <out dir> <prefix> [--box x0,y0,x1,y1]   -> prints YAML: [{src, x, y, w}]

The slide sits at (80, 16), scale 2240/960 in the export (tools/pp/page_lift.py). A tile = a near-white blob 20-80 deck px wide."""
import argparse, sys
from pathlib import Path
from PIL import Image
import numpy as np
from scipy import ndimage

OX, OY, SC = 80, 16, 2240 / 960


def tiles(f, box=None):
    im = Image.open(f).convert('RGB'); a = np.asarray(im).astype(int)
    white = (a.min(axis=2) > 225)
    lab, n = ndimage.label(white)
    out = []
    for sl in ndimage.find_objects(lab):
        h, w = sl[0].stop - sl[0].start, sl[1].stop - sl[1].start
        if not (20 * SC <= w <= 80 * SC and 20 * SC <= h <= 80 * SC and 0.75 < w / h < 1.33): continue
        cx, cy = (sl[1].start + sl[1].stop) / 2, (sl[0].start + sl[0].stop) / 2
        x, y = (cx - OX) / SC, (cy - OY) / SC
        if box and not (box[0] <= x <= box[2] and box[1] <= y <= box[3]): continue
        out.append(dict(x=round(x, 1), y=round(y, 1), w=round(w / SC, 1), crop=(sl[1].start, sl[0].start, sl[1].stop, sl[0].stop)))
    out = [t for t in out if not any(o is not t and o['w'] > t['w'] and abs(o['x'] - t['x']) < o['w'] / 2 and abs(o['y'] - t['y']) < o['w'] / 2 for o in out)]   # a white shape inside a tile is not a tile (13 Nov 2026)
    return im, sorted(out, key=lambda t: (round(t['y'] / 30), t['x']))


if __name__ == '__main__':
    ap = argparse.ArgumentParser(); ap.add_argument('img'); ap.add_argument('out'); ap.add_argument('prefix'); ap.add_argument('--box')
    a = ap.parse_args(); box = [float(v) for v in a.box.split(',')] if a.box else None
    im, T = tiles(a.img, box); Path(a.out).mkdir(parents=True, exist_ok=True)
    for i, t in enumerate(T):
        p = Path(a.out) / f'{a.prefix}-{i:02d}.png'; im.crop(t['crop']).save(p); t['src'] = '../../' + str(p)
        print(f"- {{src: {t['src']}, x: {t['x']}, y: {t['y']}, w: {t['w']}}}")
