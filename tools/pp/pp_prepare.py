"""Geometry for the 12 product-page slide types (HTML version of the live PowerPoint look).
deck.yaml only holds data (texts, numbers, logos); every position is computed here, in px on the 960 x 672 canvas."""
import math, hashlib, re

def _h(s):
    return int(hashlib.md5(s.encode()).hexdigest()[:8], 16)

def _two(t):
    w = t.split()
    if len(w) < 2: return [t, '']
    best = min(range(1, len(w)), key=lambda i: abs(len(' '.join(w[:i])) - len(' '.join(w[i:]))))
    return [' '.join(w[:best]), ' '.join(w[best:])]

def radar(s):
    cx, cy, R = 480, 384, 150
    pos = [(0.18, 205), (0.30, 330), (0.36, 95), (0.50, 245), (0.56, 20), (0.62, 150), (0.80, 290), (0.84, 60)]
    s['geo'] = dict(cx=cx, cy=cy, R=R, rings=[R * k for k in (1, .76, .52, .28)],
        inside=[dict(src=l, x=cx + R * r * math.cos(math.radians(a)), y=cy - R * r * math.sin(math.radians(a))) for l, (r, a) in zip(s['inside'], pos)],
        edge={k: dict(x=cx + dx, y=cy + dy) for k, dx, dy in (('TL', -128, -108), ('TR', 154, -110), ('BL', -104, 96), ('BR', 108, 92))})

def curve(s):
    pts = s['points']; xl, xr, top, base = 160, 520, 300, 556
    vals = [v for _, v in pts]; mx = max(vals) * 1.05; mn = 0 if s.get('zero', True) else min(vals) * 0.85
    n = len(pts) - 1; fc = s.get('forecast', 0); real = n - fc
    XS = s.get('xs'); P = [dict(xl_=l, v=v, x=xl + (XS[i] if XS else i / n) * (xr - xl), y=base - (v - mn) / (mx - mn) * (base - top), lab=(s.get('labs') or [None]*len(pts))[i], fc=i > real, last=i == n) for i, (l, v) in enumerate(pts)]
    area = f"M{P[0]['x']:.1f},{base} " + ' '.join(f"L{p['x']:.1f},{p['y']:.1f}" for p in P[:real + 1]) + f" L{P[real]['x']:.1f},{base} Z"
    s['geo'] = dict(P=P, area=area, base=base, xl=xl, xr=xr, real=real)

def cagr(s):
    v0, r = float(s['size']), float(s['cagr']) / 100
    vals = [v0 * (1 + r) ** i for i in range(11)]; mx = vals[-1]
    def money(v): return f'$ {v:.1f} B'.replace('.0 B', ' B') if v < 10 else f'$ {v:.0f} B'
    X0, X1, base, H = 175, 770, 496, 184; slot = (X1 - X0) / 11; bw = slot * 0.78
    s['geo'] = dict(bars=[dict(x=X0 + i * slot + (slot - bw) / 2, w=bw, h=max(6, H * v / mx), lab=money(v), year=s.get('y0', 2026) + i) for i, v in enumerate(vals)],
                    base=base, X0=X0, X1=X1, lastx=X0 + 10.5 * slot, lasttop=base - H - 30)

def donut(s):
    cx, cy, ro, ri = 481, 395, 116, 76
    cols = ['#FB0161', '#7FA9C9', '#C5CDD2', '#5E7E8E', '#2E5A70', '#1C4A60', '#9DB4C0']
    tot = sum(c['p'] for c in s['cats']); a = -90.0; segs = []
    for i, c in enumerate(s['cats']):
        sw = 360 * c['p'] / tot; a0, a1 = a, a + sw; a = a1
        large = 1 if sw > 180 else 0
        p = lambda ang, r: (cx + r * math.cos(math.radians(ang)), cy + r * math.sin(math.radians(ang)))
        (x0, y0), (x1, y1), (x2, y2), (x3, y3) = p(a0, ro), p(a1, ro), p(a1, ri), p(a0, ri)
        d = f'M{x0:.1f},{y0:.1f} A{ro},{ro} 0 {large} 1 {x1:.1f},{y1:.1f} L{x2:.1f},{y2:.1f} A{ri},{ri} 0 {large} 0 {x3:.1f},{y3:.1f} Z'
        mid = (a0 + a1) / 2; right = math.cos(math.radians(mid)) >= 0
        ex, ey = p(mid, ro + 4)
        segs.append(dict(d=d, col=cols[i % len(cols)], mid=mid, right=right, ex=ex, ey=ey, name=c['name'], p=round(c['p']), logos=c['logos'][:3]))
    # labels: stack per side, keep 62 px between labels
    for side in (True, False):
        L = sorted([g for g in segs if g['right'] == side], key=lambda g: g['ey'])
        y = 0
        for g in L:
            g['ly'] = max(g['ey'], y + 62); y = g['ly']
        over = (L[-1]['ly'] - 560) if L else 0
        if over > 0:
            for g in L: g['ly'] -= over
        for g in L:
            g['lx'] = cx + ro + 30 if side else cx - ro - 30
    s['geo'] = dict(cx=cx, cy=cy, ro=ro, ri=ri, segs=segs)

def pains(s):
    xs = [369, 465, 561, 658, 753]; n = len(s['pains']); step = 49
    top = 218 + (590 - 218 - (48 + n * step)) / 2          # header + rows centered between title and note
    s['geo'] = dict(xs=xs[:len(s['auds'])], head=top, rows=[dict(text=t, y=top + 48 + step / 2 + i * step, d=v) for i, (t, v) in enumerate(s['pains'])])
    s['auds2'] = [_two(a) for a in s['auds']]

def tech(s):
    C = s['companies']; F = s['features']
    sc = [sum(f['values'][j] for f in F) for j in range(len(C))]
    order = sorted(range(len(C)), key=lambda j: -sc[j])
    n = len(F); x0, x1 = 402, 748
    if n > 1:   # headers never touch: the pitch follows the widest header line (11 Nov, 'ApprovedExtrahepatic')
        need = max(_tw(l, 10.7) for f in F for l in f['header'].split('|')) + 12
        x1 = max(x1, min(845, x0 + need * (n - 1)))
    xs = [x0 + i * (x1 - x0) / max(1, n - 1) for i in range(n)] if n > 1 else [575]
    rows = []
    for k, j in enumerate(order):
        y = 317 if k == 0 else 382 + (k - 1) * 43
        rows.append(dict(c=C[j], y=y, v=[f['values'][j] for f in F], lead=k == 0))
    wl = xs[-1] + 49 - 167; dx = round(480 - (167 + wl / 2))     # the whole table is centered on the page (Pierre, 12 Nov 2026)
    s['geo'] = dict(xs=[x + dx for x in xs], rows=rows, heads=[f['header'].split('|') for f in F], wl=wl, dx=dx)

def value(s):
    X0, X1, Y0, Y1 = 208, 802, 520, 252
    for g in s['groups']:
        g['px'] = X0 + 95 + g['x'] * (X1 - X0 - 190); g['py'] = Y0 - 55 - g['y'] * (Y0 - Y1 - 85)
        n = len(g['logos']); g['bw'] = max(n * 44 + 16, min(max(n * 44 + 46, 125), len(g['name']) * 5.6)); g['bh'] = 34 + 52 + (14 if len(g['name']) * 5.6 > g['bw'] else 0)
    G = s['groups']
    for _ in range(200):
        moved = False
        for i in range(len(G)):
            for j in range(i + 1, len(G)):
                a, b = G[i], G[j]; ox = (a['bw'] + b['bw']) / 2 + 10 - abs(a['px'] - b['px']); oy = (a['bh'] + b['bh']) / 2 + 8 - abs(a['py'] - b['py'])
                if ox > 0 and oy > 0:
                    moved = True
                    if ox < oy: d = ox / 2 * (1 if a['px'] >= b['px'] else -1); a['px'] += d; b['px'] -= d
                    else: d = oy / 2 * (1 if a['py'] >= b['py'] else -1); a['py'] += d; b['py'] -= d
        for g in G:
            g['px'] = min(max(g['px'], X0 + g['bw'] / 2 + 12), X1 - g['bw'] / 2); g['py'] = min(max(g['py'], Y1 + g['bh'] / 2 - 10), Y0 - g['bh'] / 2 - 6)
        if not moved: break
    s['geo'] = dict(X0=X0, X1=X1, Y0=Y0, Y1=Y1)

def risks(s):
    E = sorted(s['events'], key=lambda e: -e['odds'])
    cols = [(64, E[:4]), (508, E[4:8])]   # wider text column so long events stay on 3 lines (11 Nov, markets 131-225)
    s['geo'] = dict(cols=[dict(x=x, rows=[dict(e=e, y=266 + i * 71) for i, e in enumerate(es)]) for x, es in cols])

def drivers(s):
    E = s['events']; halves = [E[:15], E[15:30]]
    tw = [max([len(e['text']) for e in h] + [10]) * 6.4 for h in halves]; cw = [42 + t + 14 + 22 for t in tw]; gap = 34
    L = (960 - (sum(cw) + gap)) / 2; cols = [(L, halves[0]), (L + cw[0] + gap, halves[1])]; s['cw'] = cw
    hot = sorted(range(len(E)), key=lambda i: -E[i]['impact'])[:3]; hot = {i for i in hot if E[i]['impact'] >= 2.5}
    for i, e in enumerate(E): e['hot'] = i in hot
    out = []
    for x, es in cols:
        rows, prev = [], None
        for i, e in enumerate(es):
            rows.append(dict(e=e, y=251 + i * 22.3, dim=e['year'] == prev, hl=e['hot'])); prev = e['year']
        out.append(dict(x=x, rows=rows, w=cw[len(out)]))
    s['geo'] = dict(cols=out)

def raises(s):
    R = s['rounds']; k = len(R); mx = R[0]['amt']; SP = min(111, 690 / k); L = (960 - SP * k) / 2; base, HM = 523, 208
    step = 10 ** math.floor(math.log10(mx / 3)); step *= 5 if mx / step > 15 else 2 if mx / step > 6 else 1
    while mx / step > 4.2: step *= 2
    grid = []; v = step
    while v < mx * 1.02:
        grid.append(dict(y=base - HM * v / mx, lab=f'${v/1e9:.1f}B' if v >= 1e9 else f'${v/1e6:.0f}M')); v += step
    bars = []
    for i, r in enumerate(R):
        h = max(10, HM * r['amt'] / mx); a = r['amt']
        bars.append(dict(r=r, cx=L + SP * (i + .5), h=h, lab=f'${a/1e9:.1f}B' if a >= 1e9 else f'${a/1e6:.0f}M', lead=i == 0))
    s['geo'] = dict(bars=bars, grid=grid, base=base, L=L, R=L + SP * k, SP=SP)

def grid(s):
    XB = [157, 377, 616, 833]; YB = [232, 336, 440, 543]; tiles = []
    for r in range(3):
        for c in range(3):
            L = s['cells'][r][c]
            W = s.get('weight', {})
            for i, slug in enumerate(sorted(L, key=lambda k: -W.get(k, 0))):
                fx = .28 + .44 * (i / max(1, len(L) - 1)) if len(L) > 1 else .5; fy = .38 if i % 2 == 0 else .62
                tiles.append(dict(slug=slug, src=s.get('srcs', {}).get(slug, ''), ini=slug[:2].upper(), x=XB[c] + (XB[c + 1] - XB[c]) * fx, y=YB[r] + (YB[r + 1] - YB[r]) * fy))
    s['geo'] = dict(XB=XB, YB=YB, tiles=tiles)

def killers(s):
    """table centered vertically between title and note, lines span the whole table (Pierre, 11 Nov)"""
    n = len(s['rows']); st = 52 if n >= 5 else 58; head = 40
    if s['mode'] != 'dead':
        xs, ws, lx0, nx = _warn_cols(s)
        ml = max([c.count('|') + 1 for r in s['rows'] for c in r['cells'] if c] + [1]); st = max(st, 13.5 * ml + 14)
    if s['mode'] == 'dead':
        k = len(s['causes']); xs = [464 + i * min(96, 330 / max(1, k - 1)) for i in range(k)]
        for r in s['rows']: r['years'] = int(r['end']) - int(r['start'])
        lx0 = 158
    else:
        for r in s['rows']:
            m = sum(1 for c in r['cells'] if c); r['risk'] = 'High risk' if m >= 3 else 'Medium risk'; r['rn'] = 3 if m >= 3 else 1
    lx1 = xs[-1] + (45 if s['mode'] == 'dead' else ws[-1] + 8)
    H = head + n * st; top = 392 - H / 2
    s['geo'] = dict(xs=xs, ys=[top + head + st / 2 + i * st for i in range(n)], hy=top, lx0=lx0, lx1=lx1, st=st)
    if s['mode'] != 'dead': s['geo'].update(ws=ws, cx=lx0 + 16, nx=lx0 + 44)

def survivors(s):
    n = len(s['rows']); st = 66; H = 30 + n * st; top = 392 - H / 2
    s['geo'] = dict(hy=top, ys=[top + 30 + st / 2 + i * st for i in range(n)])

def winner(s):
    n = len(s['companies']); cw = max(_tw(c['name'], 12, True) for c in s['criteria'])
    x0 = max(433, 181 + cw + 46); p = min(77, (835 - x0) / max(1, n - 1)); xs = [x0 + i * p for i in range(n)]   # long criteria push the columns right (11 Nov)
    m = len(s['criteria']); y0 = 305 + max(0, 6 - m) * 35.8 / 2   # fewer than 6 rows: block stays centered (11 Nov)
    pitch = 35.8 if m <= 6 else 35.8 * 6 / m                       # more than 6 rows: tighter rows, the block never climbs into the title (12 Nov)
    s['geo'] = dict(xs=xs, dy=y0 - 305, pitch=pitch, ys=[y0 + i * pitch for i in range(m)],
                    score=[sum(c['ticks'][j] for c in s['criteria']) for j in range(n)])


def donut_var(s):
    """layout variants of the donut labels (design choice, Pierre 11 Nov 2026)"""
    donut(s); G = s['geo']; v = s.get('variant', 'D'); cx, cy, ro = G['cx'], G['cy'], G['ro']; segs = G['segs']
    P = lambda a, r: (cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)))
    for g in segs: g['path'] = ''; g['inner'] = False
    if v in ('A', 'E', 'F'):                      # donut on the left, list on the right (or below for E)
        G['cx'] = cx = 330 if v != 'E' else 480; G['cy'] = cy = 385 if v != 'E' else 340
        donut_geo = dict(s); donut_geo['geo'] = None
        tot = sum(c['p'] for c in s['cats']); a = -90.0
        for g in segs:
            sw = 360 * g['p'] / tot; a0, a1 = a, a + sw; a = a1; large = 1 if sw > 180 else 0
            r_o, r_i = (ro, G['ri']) if v != 'E' else (95, 60)
            (x0, y0), (x1, y1), (x2, y2), (x3, y3) = P(a0, r_o), P(a1, r_o), P(a1, r_i), P(a0, r_i)
            g['d'] = f'M{x0:.1f},{y0:.1f} A{r_o},{r_o} 0 {large} 1 {x1:.1f},{y1:.1f} L{x2:.1f},{y2:.1f} A{r_i},{r_i} 0 {large} 0 {x3:.1f},{y3:.1f} Z'
            g['mid'] = (a0 + a1) / 2; g['tx'], g['ty'] = P(g['mid'], (r_o + r_i) / 2)
        n = len(segs)
        for i, g in enumerate(sorted(segs, key=lambda q: -q['p'])):
            if v == 'E': g['lx'] = 175 + (i % 3) * 215; g['ly'] = 470 + (i // 3) * 58; g['right'] = True
            else: g['lx'] = 520; g['ly'] = 250 + i * (300 / max(1, n - 1)); g['right'] = True
            g['swatch'] = True; g['inner'] = v == 'E' and g['p'] >= 8
        G['ri_'] = 60 if v == 'E' else G['ri']
        return
    for g in segs: g['right'] = math.cos(math.radians(g['mid'])) >= 0
    if v in ('B', 'C', 'G'):
        for side in (True, False):                 # keep labels 58 px apart on each side
            L = sorted([g for g in segs if g['right'] == side], key=lambda g: g.get('ly', g['ey']))
            y = -1e9
            for g in L:
                g.setdefault('ly', g['ey']); g['ly'] = max(g['ly'], y + 58); y = g['ly']
            if L and L[-1]['ly'] > 560:
                d = L[-1]['ly'] - 560
                for g in L: g['ly'] -= d
            for g in L:
                g['lx'] = cx + (ro + 46 if side else -ro - 46); x0, y0 = P(g['mid'], ro + 4); ex = g['lx'] + (-6 if side else 6)
                if v == 'C': g['path'] = f'M{x0:.1f},{y0:.1f} L{ex:.1f},{g["ly"]:.1f}'
            if v == 'G':
                for g in L:
                    x0, y0 = P(g['mid'], ro + 4); g['lx'] = cx + (ro + 46 if side else -ro - 46)
                    ex = g['lx'] + (-6 if side else 6); c1x = x0 + (18 if side else -18)
                    g['path'] = f'M{x0:.1f},{y0:.1f} Q{c1x:.1f},{g["ly"]:.1f} {ex:.1f},{g["ly"]:.1f}'
    if v == 'D':                                   # horizontal leader at the slice height, elbow only when a label had to move
        for side in (True, False):
            L = sorted([g for g in segs if g['right'] == side], key=lambda g: g['ey']); y = -1e9
            for g in L: g['ly'] = max(g['ey'], y + 58); y = g['ly']
            for g in L:
                g['lx'] = cx + (ro + 34 if side else -ro - 34); ex = g['lx'] + (-6 if side else 6)
                if abs(g['ly'] - g['ey']) < 2: g['path'] = f'M{g["ex"]:.1f},{g["ey"]:.1f} L{ex:.1f},{g["ly"]:.1f}'
                else: g['path'] = f'M{g["ex"]:.1f},{g["ey"]:.1f} L{g["ex"] + (10 if side else -10):.1f},{g["ly"]:.1f} L{ex:.1f},{g["ly"]:.1f}'

PREP = dict(donutv=donut_var, radar=radar, curve=curve, cagr=cagr, donut=donut, pains=pains, tech=tech, value=value, risks=risks,
            drivers=drivers, raises=raises, grid=grid, killers=killers, survivors=survivors, winner=winner)

JUMP_FROM = '2025-07-27'      # Google's counts jumped for almost every term that week (nmp-slide-generation, section Google Trends)

def _trend_rows(s):
    """weekly (date, value) of a Trends CSV, corrected for Google's August 2025 jump (Pierre's rule, 12 Nov 2026: always correct it):
    - with control CSVs in tools/pp/trends_ctrl/ (the everyday terms of the slide kit): each week after the jump is divided by the
      median ratio of the control terms to their own level before the jump;
    - without them: divided by s['aug25'] (default 2.0, the documented size of the jump)."""
    import csv as _c, statistics as st, glob, os
    rd = lambda f: [(r[0], float(r[1].replace('<1', '0.5'))) for r in _c.reader(open(f)) if len(r) == 2 and re.match(r'\d{4}-', r[0])]
    rows = rd(s['csv'])
    ctrl = [rd(f) for f in sorted(glob.glob(os.path.join(os.path.dirname(__file__), 'trends_ctrl', '*.csv')))]
    fac = {}
    if ctrl:
        for c in ctrl:
            pre = [v for d, v in c if '2024-07' <= d < JUMP_FROM]; b = st.median(pre) if pre else 0
            for d, v in c:
                if d >= JUMP_FROM and b > 0: fac.setdefault(d, []).append(v / b)
        fac = {d: st.median(x) for d, x in fac.items()}
    k = float(s.get('aug25', 2.0))
    out = [(d, v / (fac.get(d, k) if fac else k) if d >= JUMP_FROM else v) for d, v in rows]
    s['corrected'] = any(d >= JUMP_FROM for d, _ in rows)
    return out

def trends_window(s):
    """5 years by default; 1 year only when the last 12 months alone show a strong surge (x3 or more), Pierre 11 Nov 2026"""
    import statistics as st
    w = [v for _, v in _trend_rows(s)]; v = w[-52:]
    m = max(v); pk = max(i for i, x in enumerate(v) if x == m); base = st.median(v[:max(1, int(pk * .75))]) if pk > 4 else m
    r1 = m / max(base, 1)
    k = max(i for i, x in enumerate(w) if x == max(w)); w = w[:k + 1]; r5 = max(w) / max(st.median(w[:max(1, int(len(w) * .75))]), 1)
    return '1y' if r1 >= 3 and r1 > r5 and pk > 26 else '5y'

def trends(s):
    """the curve stops at its last peak: the trailing fall (weeks Google has not finished counting) is never shown (Pierre, 12 Nov 2026)"""
    if not s.get('window'): s['window'] = trends_window(s)
    import statistics as st
    v = [x for _, x in _trend_rows(s)]
    if s.get('window') == '1y': v = v[-52:]
    # light smoothing (Pierre, 12 Nov 2026: « on lisse un peu les incohérences et on montre le mouvement »): 3-week median drops one-week spikes and dips
    v = [sorted(v[max(0, i - 1):i + 2])[len(v[max(0, i - 1):i + 2]) // 2] for i in range(len(v))]
    pk = max(i for i, x in enumerate(v) if x == max(v)); v = v[:pk + 1]
    m = max(v); v = [x * 100 / m for x in v]
    n = len(v); r = max(v) / max(st.median(v[:max(1, int(n * .75))]), 1)
    lab = '×20+' if r >= 20 else (f'×{int(round(r / 5) * 5)}' if r >= 10 else f'×{round(r * 2) / 2:.1f}'.replace('.0', ''))
    x0, x1, y0, y1 = 136, 824, 500, 410
    s['geo'] = dict(ratio=r, stat=lab, pts=' '.join(f'{x0 + i / (n - 1) * (x1 - x0):.1f},{y0 - x / 100 * (y0 - y1):.1f}' for i, x in enumerate(v)), base=y0 + 16)
PREP['trends'] = trends



_KF = {}
def _tw(t, size, bold=False):
    """text width in px on the 960 canvas (Lexend)"""
    from PIL import ImageFont
    k = (size, bold)
    if k not in _KF: _KF[k] = ImageFont.truetype('/home/claude/nmp-decks/assets/fonts/' + ('Lexend-SemiBold.ttf' if bold else 'Lexend-Regular.ttf'), size * 4)
    return _KF[k].getlength(t) / 4
def _wrap(text, W, size):
    w = text.replace('|', ' ').split(); L = ['']
    for x in w:
        t = (L[-1] + ' ' + x).strip()
        if _tw(t, size) <= W or not L[-1]: L[-1] = t
        else: L.append(x)
    return L
def _warn_cols(s):
    """warning-mode killers: column widths follow the texts, table centered, cells rewrapped (up to 3 lines) when the table would be too wide (11 Nov: texts overlapped)"""
    K = len(s['signs']); F = 10; HF = 12
    name_w = max(_tw(r['name'], 12.7, True) for r in s['rows']); name_w = max(name_w, 122) + 52   # logo 32 + gap, name or risk dots
    head_w = [max(_tw(p, HF, True) for p in h.split('|')) for h in s['signs']]
    best = None
    for maxl in (3, 4):
        for W in (175, 160, 145, 130, 118, 106, 96, 88):
            cols = []
            for i in range(K):
                L = [_wrap(r['cells'][i], W, F) for r in s['rows'] if r['cells'][i]]
                if any(len(x) > maxl for x in L): break
                cols.append(max([head_w[i]] + [_tw(l, F) for x in L for l in x]) + 8)
            else:
                total = name_w + sum(c + 20 for c in cols); best = (W, cols, total)
                if total <= 890: break
        if best and best[2] <= 890: break
    W, cols, total = best
    for r in s['rows']:
        r['cells'] = ['|'.join(_wrap(c, W, F)) if c else '' for c in r['cells']]
    lx0 = max(50, (960 - total) / 2); xs = []; x = lx0 + name_w
    for c in cols: xs.append(x); x += c + 20
    return xs, cols, lx0, lx0 + 44
