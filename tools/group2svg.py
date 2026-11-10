"""Convert a PPTX group of freeform shapes (e.g. the world map) to an SVG file.
Usage: python3 group2svg.py deck.pptx slide_no shape_id out.svg"""
import sys
from pptx import Presentation
from lxml import etree
A='{http://schemas.openxmlformats.org/drawingml/2006/main}'
def xf(el):
    x=el.find(f'.//{A}xfrm'); o=x.find(f'{A}off'); e=x.find(f'{A}ext')
    r=[int(o.get('x')),int(o.get('y')),int(e.get('cx')),int(e.get('cy'))]
    co=x.find(f'{A}chOff'); ce=x.find(f'{A}chExt')
    if co is not None: r+= [int(co.get('x')),int(co.get('y')),int(ce.get('cx')),int(ce.get('cy'))]
    return r
p=Presentation(sys.argv[1]); s=p.slides[int(sys.argv[2])-1]
g=[sh for sh in s.shapes if sh.shape_id==int(sys.argv[3])][0]
gx,gy,gw,gh,cx,cy,cw,ch=xf(g._element.find(f'{{http://schemas.openxmlformats.org/presentationml/2006/main}}grpSpPr'))
sx,sy=gw/cw,gh/ch
out=[]
for sp in g._element.iter('{http://schemas.openxmlformats.org/presentationml/2006/main}sp'):
    x,y,w,h=xf(sp)[:4]
    col=sp.find(f'.//{A}solidFill/{A}srgbClr'); fill='#'+col.get('val') if col is not None else 'none'
    for path in sp.iter(f'{A}path'):
        pw=int(path.get('w') or w) or 1; ph=int(path.get('h') or h) or 1
        def P(pt):
            X=(x+int(pt.get('x'))*w/pw-cx)*sx; Y=(y+int(pt.get('y'))*h/ph-cy)*sy
            return f'{X/9525:.1f} {Y/9525:.1f}'
        d=[]
        for c in path:
            t=etree.QName(c).localname; pts=c.findall(f'{A}pt')
            if t=='moveTo': d.append('M'+P(pts[0]))
            elif t=='lnTo': d.append('L'+P(pts[0]))
            elif t=='cubicBezTo': d.append('C'+' '.join(P(q) for q in pts))
            elif t=='quadBezTo': d.append('Q'+' '.join(P(q) for q in pts))
            elif t=='close': d.append('Z')
        out.append(f'<path d="{"".join(d)}" fill="{fill}"/>')
W,H=gw/9525,gh/9525
open(sys.argv[4],'w').write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W:.1f} {H:.1f}">'+''.join(out)+'</svg>')
print(len(out),'paths',round(W),round(H))
