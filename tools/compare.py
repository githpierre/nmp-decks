"""Side-by-side sheets: original render (left) vs HTML render (right). Usage: compare.py orig_dir new_dir out_prefix n1,n2,..."""
import sys, glob
from PIL import Image, ImageDraw
od, nd, pre, ns = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4].split(',')
pairs = [x.split(':') for x in ns]
W, H = 720, 504
for k in range(0, len(pairs), 3):
    sh = Image.new('RGB', (W * 2 + 10, (H + 10) * 3), 'white')
    for j, (o, n) in enumerate(pairs[k:k+3]):
        a = Image.open(glob.glob(f'{od}/s{int(o):03d}*.jpg')[0]).resize((W, H)); b = Image.open(f'{nd}/{int(n):03d}.png').convert('RGB').resize((W, H))
        sh.paste(a, (0, j * (H + 10))); sh.paste(b, (W + 10, j * (H + 10)))
    sh.save(f'{pre}_{k//3+1}.jpg', quality=82)
