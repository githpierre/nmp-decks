"""Which slides changed since the last look? (12 Nov 2026: 205 slides cannot be re-read at every round, and a fix can break another slide.)

    python3 tools/diff_slides.py <handle> --snap     save the current audit images as the reference (after a full visual pass)
    python3 tools/diff_slides.py <handle>            list the slides whose image changed since the snapshot -> look at these, 6 per sheet
    python3 tools/diff_slides.py <handle> --sheets   also write the contact sheets (/tmp/<handle>_changed_N.png)"""
import glob, shutil, sys
from pathlib import Path
from PIL import Image, ImageChops, ImageDraw, ImageStat
ROOT = Path(__file__).resolve().parent.parent
d = ROOT / 'decks' / sys.argv[1] / 'out'; snap = d / 'snap'; new = sorted(glob.glob(str(d / 'png' / '*.png')))
if '--snap' in sys.argv:
    snap.mkdir(exist_ok=True)
    for f in snap.glob('*.jpg'): f.unlink()
    for f in new: Image.open(f).convert('RGB').resize((480, 336)).save(snap / (Path(f).stem + '.jpg'), quality=85)
    print('snapshot of', len(new), 'slides'); sys.exit()
old = sorted(snap.glob('*.jpg'))
if len(old) != len(new): print(f'slide count changed ({len(old)} -> {len(new)}): do a full pass, then --snap'); sys.exit(1)
ch = []
for i, (a, b) in enumerate(zip(old, new), 1):
    x = ImageChops.difference(Image.open(a).convert('L'), Image.open(b).convert('L').resize((480, 336))).point(lambda v: 255 if v > 40 else 0)
    if ImageStat.Stat(x).mean[0] / 255 > 0.0025: ch.append(i)
print(len(ch), 'slides changed:', ' '.join(map(str, ch)))
if '--sheets' in sys.argv:
    for k in range(0, len(ch), 6):
        part = ch[k:k + 6]; sh = Image.new('RGB', (1440, 504 * ((len(part) + 1) // 2)), 'white'); dr = ImageDraw.Draw(sh)
        for j, n in enumerate(part):
            x, y = (j % 2) * 720, (j // 2) * 504; sh.paste(Image.open(new[n - 1]).convert('RGB').resize((720, 504)), (x, y)); dr.rectangle([x, y, x + 30, y + 14], fill='yellow'); dr.text((x + 3, y + 2), str(n), fill='black')
        sh.save(f'/tmp/{sys.argv[1]}_changed_{k // 6}.png')
