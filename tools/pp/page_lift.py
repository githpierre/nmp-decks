"""Usage: python3 page_lift.py in.png out.webp [--w 2400 --h 1680 --blur 20 --distance 30 --curve 50 --intensity 50 --quality 92]"""
import argparse
from PIL import Image, ImageDraw, ImageFilter

def page_lift(src, W=2400, H=1680, blur=20, distance=30, curve=50, intensity=50, ss=2):
    k = W / 1000 * ss
    CW, CH = W*ss, H*ss
    d = distance * k * 0.6
    b = blur * k * 0.5
    margin_bottom = d + b*1.6
    sh = int(CH - margin_bottom - 30*ss)
    img = Image.open(src).convert("RGBA")
    sw = int(sh * img.width / img.height)
    x0, y0 = (CW - sw)//2, int(30*ss*0.6)
    slide = img.resize((sw, sh), Image.LANCZOS)
    sag = d * (curve/50)
    inset = sw * 0.02
    pts = [(x0+inset, y0+sh-d)]
    n = 60
    for i in range(n+1):
        t = i/n
        pts.append((x0+inset + t*(sw-2*inset), y0 + sh + d*0.25 + sag*(1-(2*t-1)**2)))
    pts.append((x0+sw-inset, y0+sh-d))
    mask = Image.new("L", (CW, CH), 0)
    ImageDraw.Draw(mask).polygon(pts, fill=int(255*intensity/100))
    mask = mask.filter(ImageFilter.GaussianBlur(b))
    canvas = Image.new("RGBA", (CW, CH), (0, 0, 0, 0))
    canvas.putalpha(mask)
    canvas.alpha_composite(slide, (x0, y0))
    return canvas.resize((W, H), Image.LANCZOS)

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("src"); p.add_argument("dst")
    for a, v in [("w",2400),("h",1680),("blur",20),("distance",30),("curve",50),("intensity",50)]:
        p.add_argument(f"--{a}", type=int, default=v)
    p.add_argument("--quality", type=int, default=92)
    a = p.parse_args()
    out = page_lift(a.src, a.w, a.h, a.blur, a.distance, a.curve, a.intensity)
    if a.dst.lower().endswith(".webp"):
        out.save(a.dst, "WEBP", quality=a.quality, alpha_quality=100, method=6)
    else:
        out.save(a.dst, optimize=True)
