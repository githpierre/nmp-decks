"""Faithful PPTX -> HTML converter for one slide (used for slides that have no template yet).
Usage from code: convert(slide, theme, media_dir, media_prefix) -> dict(section, title, page, note, html)
- the common chrome (pink triangle, section label, title, page marker, footnote, footer) is detected and returned as fields,
  so the deck keeps its own chrome (balanced titles, footnote rules, footer label/button);
- every other shape becomes an absolutely positioned element: geometry drawn in SVG, text in a div on top.
Canvas: 960 x 672 px (10 x 7 in, 1 px = 9525 EMU). Font sizes stay in pt (CSS pt = 1/72 in, same as PowerPoint)."""
import hashlib, html, math, re
from pptx.enum.shapes import MSO_SHAPE_TYPE

A = '{http://schemas.openxmlformats.org/drawingml/2006/main}'
R = '{http://schemas.openxmlformats.org/officeDocument/2006/relationships}'
E = 9525.0
esc = lambda s: html.escape(s, quote=False)


def theme_colors(prs):
    part = prs.slide_master.part.part_related_by('http://schemas.openxmlformats.org/officeDocument/2006/relationships/theme')
    x = part.blob.decode('utf8'); out = {}
    for k in ['dk1', 'lt1', 'dk2', 'lt2', 'accent1', 'accent2', 'accent3', 'accent4', 'accent5', 'accent6', 'hlink', 'folHlink']:
        m = re.search(rf'<a:{k}>.*?val="([0-9A-Fa-f]{{6}})"', x, re.S)
        if m: out[k] = m.group(1)
    out.update(tx1=out.get('dk1'), bg1=out.get('lt1'), tx2=out.get('dk2'), bg2=out.get('lt2'))
    return out


def color(el, theme):
    """Colour of a fill element (solidFill / ln/solidFill...): returns css rgba() or None."""
    if el is None: return None
    c = el.find(A + 'srgbClr'); v = None
    if c is not None: v = c.get('val')
    else:
        c = el.find(A + 'schemeClr')
        if c is not None: v = theme.get(c.get('val'))
    if c is None or v is None: return None
    r, g, b = int(v[0:2], 16), int(v[2:4], 16), int(v[4:6], 16); a = 1.0
    for m in c:
        t, val = m.tag.replace(A, ''), int(m.get('val', '100000')) / 100000
        if t == 'alpha': a = val
        elif t == 'lumMod': r, g, b = r * val, g * val, b * val
        elif t == 'lumOff': r, g, b = r + 255 * val, g + 255 * val, b + 255 * val
    r, g, b = [max(0, min(255, round(x))) for x in (r, g, b)]
    return f'rgba({r},{g},{b},{a:.3g})' if a < 1 else f'#{r:02X}{g:02X}{b:02X}'


def fill_of(spPr, theme):
    if spPr is None: return None
    if spPr.find(A + 'noFill') is not None: return None
    return color(spPr.find(A + 'solidFill'), theme)


def line_of(spPr, theme):
    ln = spPr.find(A + 'ln') if spPr is not None else None
    if ln is None or ln.find(A + 'noFill') is not None: return None
    c = color(ln.find(A + 'solidFill'), theme)
    if c is None: return None
    w = int(ln.get('w', '9525')) / E
    d = ln.find(A + 'prstDash'); dash = d.get('val') if d is not None else 'solid'
    he, te = ln.find(A + 'headEnd'), ln.find(A + 'tailEnd')
    return dict(c=c, w=max(w, .5), dash=dash, head=he.get('type') if he is not None else None, tail=te.get('type') if te is not None else None)


def shadow_of(spPr):
    e = spPr.find(A + 'effectLst') if spPr is not None else None
    if e is None or e.find(A + 'outerShdw') is None: return ''
    s = e.find(A + 'outerShdw'); blur = int(s.get('blurRad', '0')) / E; dist = int(s.get('dist', '0')) / E
    ang = int(s.get('dir', '5400000')) / 60000 * math.pi / 180
    return f'drop-shadow({dist * math.cos(ang):.1f}px {dist * math.sin(ang):.1f}px {blur / 2:.1f}px rgba(0,0,0,.5))'


DASH = {'dash': '6 4', 'sysDash': '3 2', 'sysDot': '1 2', 'dot': '1 3', 'lgDash': '10 5', 'dashDot': '6 3 1 3'}


def adj(sh, name='adj', default=None):
    g = sh._element.find('.//' + A + 'prstGeom')
    if g is not None:
        for gd in g.iter(A + 'gd'):
            if gd.get('name') == name: return int(gd.get('fmla').split()[-1])
    return default


def geom_path(prst, w, h, sh):
    """SVG path for a preset shape in a w x h box."""
    if prst == 'frame':
        k = min(w, h) * adj(sh, 'adj1', 12500) / 100000
        return f'M0 0H{w}V{h}H0Z M{k} {k}V{h - k}H{w - k}V{k}Z'
    if prst in ('rect', None): return f'M0 0H{w}V{h}H0Z'
    if prst == 'roundRect':
        r = min(w, h) * adj(sh, 'adj', 16667) / 100000
        return f'M{r} 0H{w - r}A{r} {r} 0 0 1 {w} {r}V{h - r}A{r} {r} 0 0 1 {w - r} {h}H{r}A{r} {r} 0 0 1 0 {h - r}V{r}A{r} {r} 0 0 1 {r} 0Z'
    if prst == 'ellipse': return f'M0 {h / 2}A{w / 2} {h / 2} 0 1 0 {w} {h / 2}A{w / 2} {h / 2} 0 1 0 0 {h / 2}Z'
    if prst == 'rtTriangle': return f'M0 0L0 {h}L{w} {h}Z'
    if prst == 'triangle': return f'M{w / 2} 0L{w} {h}L0 {h}Z'
    if prst == 'chevron':
        a = min(w, h) * adj(sh, 'adj', 50000) / 100000
        return f'M0 0H{w - a}L{w} {h / 2}L{w - a} {h}H0L{a} {h / 2}Z'
    if prst == 'homePlate':
        a = min(w, h) * adj(sh, 'adj', 50000) / 100000
        return f'M0 0H{w - a}L{w} {h / 2}L{w - a} {h}H0Z'
    if prst in ('rightArrow', 'leftRightArrow', 'upArrow'):
        a1, a2 = adj(sh, 'adj1', 50000) / 100000, adj(sh, 'adj2', 50000) / 100000
        if prst == 'upArrow':
            hw = min(w, h) * a2; t = w * (1 - a1) / 2
            return f'M{w / 2} 0L{w} {hw}H{w - t}V{h}H{t}V{hw}H0Z'
        hh = min(w, h) * a2; t = h * (1 - a1) / 2
        if prst == 'rightArrow': return f'M0 {t}H{w - hh}V0L{w} {h / 2}L{w - hh} {h}V{h - t}H0Z'
        return f'M0 {h / 2}L{hh} 0V{t}H{w - hh}V0L{w} {h / 2}L{w - hh} {h}V{h - t}H{hh}V{h}Z'
    if prst == 'mathMultiply':
        k = min(w, h) * .18
        return (f'M{k} 0L{w / 2} {h / 2 - k}L{w - k} 0L{w} {k}L{w / 2 + k} {h / 2}L{w} {h - k}L{w - k} {h}L{w / 2} {h / 2 + k}'
                f'L{k} {h}L0 {h - k}L{w / 2 - k} {h / 2}L0 {k}Z')
    if prst == 'mathNotEqual':
        t = h * .12
        return (f'M{w * .1} {h * .3}H{w * .9}V{h * .3 + t}H{w * .1}Z M{w * .1} {h * .6}H{w * .9}V{h * .6 + t}H{w * .1}Z '
                f'M{w * .62} {h * .1}L{w * .7} {h * .14}L{w * .38} {h * .9}L{w * .3} {h * .86}Z')
    if prst in ('rightBrace', 'leftBrace'):
        p = f'M0 0Q{w / 2} 0 {w / 2} {h * .08}V{h * .42}Q{w / 2} {h / 2} {w} {h / 2}Q{w / 2} {h / 2} {w / 2} {h * .58}V{h * .92}Q{w / 2} {h} 0 {h}'
        return p if prst == 'rightBrace' else f'M{w} 0Q{w / 2} 0 {w / 2} {h * .08}V{h * .42}Q{w / 2} {h / 2} 0 {h / 2}Q{w / 2} {h / 2} {w / 2} {h * .58}V{h * .92}Q{w / 2} {h} {w} {h}'
    if prst in ('star5', 'irregularSeal1'):
        n = 5 if prst == 'star5' else 12; pts = []
        for i in range(n * 2):
            r = (1 if i % 2 == 0 else (.4 if prst == 'star5' else .7)); a = -math.pi / 2 + i * math.pi / n
            pts.append(f'{w / 2 + w / 2 * r * math.cos(a):.1f} {h / 2 + h / 2 * r * math.sin(a):.1f}')
        return 'M' + 'L'.join(pts) + 'Z'
    return f'M0 0H{w}V{h}H0Z'


def cust_path(sh, w, h):
    out = []
    for path in sh._element.iter(A + 'path'):
        pw, ph = int(path.get('w', '0')) or 1, int(path.get('h', '0')) or 1
        sx, sy = w / pw, h / ph
        P = lambda pt: f'{int(pt.get("x")) * sx:.1f} {int(pt.get("y")) * sy:.1f}'
        for c in path:
            t = c.tag.replace(A, ''); pts = c.findall(A + 'pt')
            if t == 'moveTo': out.append('M' + P(pts[0]))
            elif t == 'lnTo': out.append('L' + P(pts[0]))
            elif t == 'cubicBezTo': out.append('C' + ' '.join(P(p) for p in pts))
            elif t == 'quadBezTo': out.append('Q' + ' '.join(P(p) for p in pts))
            elif t == 'close': out.append('Z')
    return ''.join(out)


FONTS = {'Montserrat': 'Montserrat', 'Arial': 'Arial'}


def runs_html(p, theme, scale):
    out = []
    for r in p._p:
        t = r.tag.replace(A, '')
        if t == 'br': out.append(' '); continue
        if t not in ('r', 'fld'): continue
        rp = r.find(A + 'rPr'); tx = ''.join(x.text or '' for x in r.iter(A + 't'))
        if not tx: continue
        st = []
        if rp is not None:
            if rp.get('sz'): st.append(f'font-size:{int(rp.get("sz")) / 100 * scale:.2f}pt')
            if rp.get('b') == '1': st.append('font-weight:700')
            if rp.get('i') == '1': st.append('font-style:italic')
            if rp.get('u') not in (None, 'none'): st.append('text-decoration:underline')
            if rp.get('spc'): st.append(f'letter-spacing:{int(rp.get("spc")) / 100:.2f}pt')
            c = color(rp.find(A + 'solidFill'), theme)
            if c: st.append(f'color:{c}')
            lt = rp.find(A + 'latin')
            if lt is not None:
                tf = lt.get('typeface', '')
                if 'SemiBold' in tf: st.append('font-weight:600')
                if tf.startswith('Montserrat'): st.append('font-family:Montserrat')
                elif tf.startswith('Arial'): st.append('font-family:Arial,sans-serif')
        if re.fullmatch(r'(?:[A-Z0-9&.\-] ){3,}[A-Z0-9&.\-]|(?:(?:[A-Z0-9&.\-] )+[A-Z0-9&.\-] {2,})+(?:[A-Z0-9&.\-] )*[A-Z0-9&.\-]', tx.strip()):
            tx = unspace(tx); st.append('letter-spacing:.42em')   # 'W H Y    I T' -> 'WHY IT' + letter spacing (spaces were the spacing)
        tx = esc(tx).replace('\x0b', ' ').replace('\n', ' ')   # manual line breaks dropped: the browser balances the lines
        out.append(f'<span style="{";".join(st)}">{tx}</span>' if st else tx)
    return ''.join(out)


def text_html(sh, theme, x, y, w, h, k=None, ov=None, boxed=False):
    tf = sh.text_frame; bp = tf._txBody.find(A + 'bodyPr')
    ins = lambda k, d: int(bp.get(k, d)) / E if bp is not None else d / E
    L, T, Rr, B = ins('lIns', 91440), ins('tIns', 45720), ins('rIns', 91440), ins('bIns', 45720)
    anchor = {'t': 'flex-start', 'ctr': 'center', 'b': 'flex-end'}.get(bp.get('anchor', 't') if bp is not None else 't', 'flex-start')
    scale = 1.0
    na = bp.find(A + 'normAutofit') if bp is not None else None
    if na is not None and na.get('fontScale'): scale = int(na.get('fontScale')) / 100000
    wrap = bp is None or bp.get('wrap', 'square') != 'none'
    paras = []; ovt = (ov or {}).get('text')
    if (ov or {}).get('join') and not ovt: ovt = ' '.join(re.sub(r'\s+', ' ', q.text).strip() for q in tf.paragraphs if q.text.strip())   # join = one paragraph
    if isinstance(ovt, str):      # one string = the whole text of the box (paragraphs without letters, like an emoji, are kept)
        ne = [q.text for q in tf.paragraphs if q.text.strip()]; li = [i for i, t in enumerate(ne) if re.search(r'[A-Za-z0-9]', t)]
        ovt = [None if i not in li else (ovt if i == li[0] else '') for i in range(len(ne))]
    pi = -1
    for p in tf.paragraphs:
        pp = p._p.find(A + 'pPr'); st = []
        al = pp.get('algn') if pp is not None else None
        st.append('text-align:' + {'ctr': 'center', 'r': 'right', 'just': 'justify', 'dist': 'justify'}.get(al, 'left'))
        if pp is not None:
            ls = pp.find(A + 'lnSpc/' + A + 'spcPct')
            if ls is not None: st.append(f'line-height:{int(ls.get("val")) / 100000 * 1.2:.3f}')
            sb = pp.find(A + 'spcBef/' + A + 'spcPts'); sa = pp.find(A + 'spcAft/' + A + 'spcPts')
            if sb is not None and int(sb.get('val')): st.append(f'margin-top:{int(sb.get("val")) / 100}pt')
            if sa is not None and int(sa.get('val')): st.append(f'margin-bottom:{int(sa.get("val")) / 100}pt')
        # paragraph font size = largest run size (else endParaRPr): the line strut must not come from the 18 pt default
        sizes = [int(r.get('sz')) for r in p._p.iter(A + 'rPr') if r.get('sz')]
        dflt = p._p.find(A + 'endParaRPr')
        fs = str(max(sizes)) if sizes else (dflt.get('sz') if dflt is not None and dflt.get('sz') else None)
        inner = runs_html(p, theme, scale)
        if p.text.strip(): pi += 1
        if ovt and p.text.strip() and pi < len(ovt) and ovt[pi] == '': continue      # '' in overrides = drop this paragraph
        if ovt and p.text.strip() and pi < len(ovt) and ovt[pi] is not None:
            r0 = p._p.find(A + 'r'); keep = runs_html(type('P', (), {'_p': [r0]})(), theme, scale) if r0 is not None else ''
            m = re.match(r'<span style="([^"]*)">', keep)
            inner = (f'<span style="{m.group(1)}">' if m else '') + esc(ovt[pi]).replace('\n', '<br>') + ('</span>' if m else '')
        plain = ''.join(x.text or '' for x in p._p.iter(A + 't'))
        if plain.strip() and all(ord(c) > 0x2000 or c.isspace() for c in plain): st.append('white-space:nowrap')   # emoji-only lines never wrap
        if fs: st.append(f'font-size:{int(fs) / 100 * scale:.2f}pt')
        paras.append(f'<p style="{";".join(st)}">{inner or "&nbsp;"}</p>')
    ws = '' if wrap else 'white-space:nowrap;'
    if boxed: L, Rr = max(L, 10), max(Rr, 10)        # text inside a drawn bubble never touches its border (Pierre, 10 Nov)
    if ov and ov.get('pad') is not None: L = Rr = ov['pad']
    da = (f' data-lines="{ov["lines"]}"' if ov and ov.get('lines') else '') + (' data-nofit="1"' if ov and ov.get('nofit') else '')
    return (f'<div class="rx-t" data-k="{k}"{da} style="left:{x:.1f}px;top:{y:.1f}px;width:{w:.1f}px;height:{h:.1f}px;'
            f'padding:{T:.1f}px {Rr:.1f}px {B:.1f}px {L:.1f}px;justify-content:{anchor};{ws}">' + ''.join(paras) + '</div>')


def shape_svg(sh, theme, x, y, w, h, kind):
    spPr = sh._element.find('.//' + '{http://schemas.openxmlformats.org/presentationml/2006/main}spPr')
    if spPr is None: spPr = sh._element.find('.//' + A + 'spPr')
    fill, ln, shd = fill_of(spPr, theme), line_of(spPr, theme), shadow_of(spPr)
    if not fill and not ln: return ''
    g = sh._element.find('.//' + A + 'prstGeom'); prst = g.get('prst') if g is not None else None
    flipH = sh._element.find('.//' + A + 'xfrm') is not None and sh._element.find('.//' + A + 'xfrm').get('flipH') == '1'
    flipV = sh._element.find('.//' + A + 'xfrm') is not None and sh._element.find('.//' + A + 'xfrm').get('flipV') == '1'
    rot = sh.rotation if hasattr(sh, 'rotation') else 0
    pad = (ln['w'] if ln else 0) + 8
    if kind == 'line':
        x1, y1, x2, y2 = 0, 0, w, h
        if flipH: x1, x2 = w, 0
        if flipV: y1, y2 = h, 0
        if prst and prst.startswith('curvedConnector'):
            d = f'M{x1} {y1}C{(x1 + x2) / 2} {y1} {(x1 + x2) / 2} {y2} {x2} {y2}'
        else: d = f'M{x1} {y1}L{x2} {y2}'
        fill = None
    elif prst is None and sh._element.find('.//' + A + 'custGeom') is not None: d = cust_path(sh, w, h)
    else: d = geom_path(prst, w, h, sh)
    st = [f'fill="{fill or "none"}"']
    if ln:
        st.append(f'stroke="{ln["c"]}" stroke-width="{ln["w"]:.2f}"')
        if ln['dash'] in DASH: st.append(f'stroke-dasharray="{DASH[ln["dash"]]}"')
    else: st.append('stroke="none"')
    defs, mk = '', ''
    if ln and (ln['head'] not in (None, 'none') or ln['tail'] not in (None, 'none')):
        mid = 'm' + hashlib.md5(f'{x}{y}{w}{h}'.encode()).hexdigest()[:8]
        defs = (f'<defs><marker id="{mid}" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="4" markerHeight="4" orient="auto-start-reverse">'
                f'<path d="M0 0L10 5L0 10Z" fill="{ln["c"]}"/></marker></defs>')
        if ln['tail'] not in (None, 'none'): mk += f' marker-end="url(#{mid})"'
        if ln['head'] not in (None, 'none'): mk += f' marker-start="url(#{mid})"'
    tr = []
    if kind != 'line' and (flipH or flipV): tr.append(f'translate({w if flipH else 0} {h if flipV else 0}) scale({-1 if flipH else 1} {-1 if flipV else 1})')
    tf = f' transform="{" ".join(tr)}"' if tr else ''
    css = f'left:{x - pad:.1f}px;top:{y - pad:.1f}px;width:{w + 2 * pad:.1f}px;height:{h + 2 * pad:.1f}px'
    if rot: css += f';transform:rotate({rot}deg)'
    if shd: css += f';filter:{shd}'
    return (f'<svg class="rx-s" style="{css}" viewBox="{-pad:.1f} {-pad:.1f} {w + 2 * pad:.1f} {h + 2 * pad:.1f}">{defs}'
            f'<path d="{d}" fill-rule="evenodd" {" ".join(st)}{mk}{tf}/></svg>')


def walk(shapes, tf=None):
    """Yield (shape, x, y, w, h) in slide px, applying group transforms."""
    tf = tf or (lambda X, Y, W, H: (X, Y, W, H))
    for sh in shapes:
        X, Y, W, H = (sh.left or 0) / E, (sh.top or 0) / E, (sh.width or 0) / E, (sh.height or 0) / E
        if sh.shape_type == MSO_SHAPE_TYPE.GROUP:
            x = sh._element.find(A + 'grpSpPr/' + A + 'xfrm') if sh._element.find(A + 'grpSpPr') is not None else None
            x = sh._element.find('{http://schemas.openxmlformats.org/presentationml/2006/main}grpSpPr/' + A + 'xfrm')
            co, ce = x.find(A + 'chOff'), x.find(A + 'chExt')
            cx, cy = int(co.get('x')) / E, int(co.get('y')) / E; cw, chh = int(ce.get('cx')) / E or 1, int(ce.get('cy')) / E or 1
            gx, gy, gw, gh = tf(X, Y, W, H)
            sub = lambda a, b, c, d, gx=gx, gy=gy, gw=gw, gh=gh, cx=cx, cy=cy, cw=cw, chh=chh: (
                gx + (a - cx) * gw / cw, gy + (b - cy) * gh / chh, c * gw / cw, d * gh / chh)
            yield from walk(sh.shapes, sub)
        else:
            yield (sh, *tf(X, Y, W, H))


def unspace(s):
    """'P A I N    P O I N T S' -> 'PAIN POINTS' (letters split by 1 space, words by 2+)."""
    return ' '.join(w.replace(' ', '') for w in re.split(r' {2,}', s.strip()))


def convert(slide, theme, media_dir, media_url, overrides=None):
    overrides = overrides or {}
    out = dict(section=None, title=None, page=None, note=None); body = []
    for k, (sh, x, y, w, h) in enumerate(walk(slide.shapes)):
        ov = overrides.get(k, {})
        if ov.get('hide'): continue
        if ov.get('dy'): y += ov['dy']
        if ov.get('dx'): x += ov['dx']
        if ov.get('scale'): s_ = ov['scale']; x, y, w, h = x + w * (1 - s_) / 2, y + h * (1 - s_) / 2, w * s_, h * s_
        txt = sh.text_frame.text.strip() if sh.has_text_frame else ''
        g = sh._element.find('.//' + A + 'prstGeom'); prst = g.get('prst') if g is not None else None
        # ---- chrome ----
        if prst == 'rtTriangle' and x < 5 and y < 5 and w < 40: continue
        if txt and abs(y - 19) < 4 and w > 800 and len(txt) < 60 and re.match(r'^([A-Z0-9&] ?)+', txt.replace('  ', ' ')) and txt.count(' ') > 2:
            out['section'] = unspace(txt).capitalize() if txt.upper() == txt else txt; continue
        if txt and 34 < y < 70 and w > 800 and out['title'] is None and not re.fullmatch(r'([A-Z] )+[A-Z]', txt.strip()):
            out['title'] = re.sub(r'\s*\n\s*', '\n', txt.replace('\x0b', '\n')); continue
        if txt and re.fullmatch(r'\d/\d', txt) and y < 175: out['page'] = txt; continue
        if txt and x < 30 and y > 575 and w > 500: out['note'] = re.sub(r'\s+', ' ', txt.replace('\x0b', ' ')).strip(); continue
        if txt and x > 690 and y > 600 and w < 240 and ('NEWMARKETPITCH' in txt.replace(' ', '') or y < 625): continue
        if not txt and sh.shape_type == MSO_SHAPE_TYPE.LINE and y > 638 and y < 648 and w > 600: continue
        # ---- body ----
        if sh.shape_type == MSO_SHAPE_TYPE.PICTURE:
            blob = sh.image.blob; ext = sh.image.ext; name = hashlib.md5(blob).hexdigest()[:12] + '.' + ext
            (media_dir / name).write_bytes(blob)
            body.append(f'<img class="rx-i" src="{media_url}/{name}" style="left:{x:.1f}px;top:{y:.1f}px;width:{w:.1f}px;height:{h:.1f}px">')
            continue
        kind = 'line' if sh.shape_type == MSO_SHAPE_TYPE.LINE or (prst or '').endswith('Connector1') or (prst or '').startswith('curvedConnector') or (prst or '').startswith('straightConnector') else 'shape'
        sv = shape_svg(sh, theme, x, y, w, h, kind); body.append(sv)
        if txt: body.append(text_html(sh, theme, x, y, w, h, k, ov, boxed=bool(sv) and kind != 'line'))
    out['html'] = '\n'.join(b for b in body if b)
    return out
