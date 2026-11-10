"""Geometry for the 12 product-page slide types (HTML version of the live PowerPoint look).
deck.yaml only holds data (texts, numbers, logos); every position is computed here, in px on the 960 x 672 canvas."""
import math, hashlib

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
    vals = [v for _, v in pts]; mx = max(vals) * 1.05
    n = len(pts) - 1; fc = s.get('forecast', 0); real = n - fc
    P = [dict(lab=l, v=v, x=xl + i * (xr - xl) / n, y=base - v / mx * (base - top), fc=i > real, last=i == n) for i, (l, v) in enumerate(pts)]
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
    n = len(F); x0, x1 = 402, 748; xs = [x0 + i * (x1 - x0) / max(1, n - 1) for i in range(n)] if n > 1 else [575]
    rows = []
    for k, j in enumerate(order):
        y = 317 if k == 0 else 382 + (k - 1) * 43
        rows.append(dict(c=C[j], y=y, v=[f['values'][j] for f in F], lead=k == 0))
    s['geo'] = dict(xs=xs, rows=rows, heads=[f['header'].split('|') for f in F])

def value(s):
    X0, X1, Y0, Y1 = 208, 802, 520, 252
    for g in s['groups']:
        g['px'] = 290 + g['x'] * 440; g['py'] = 547 - 298 * g['y']
    s['geo'] = dict(X0=X0, X1=X1, Y0=Y0, Y1=Y1)

def risks(s):
    E = sorted(s['events'], key=lambda e: -e['odds'])
    cols = [(90, E[:4]), (503, E[4:8])]
    s['geo'] = dict(cols=[dict(x=x, rows=[dict(e=e, y=266 + i * 71) for i, e in enumerate(es)]) for x, es in cols])

def drivers(s):
    E = s['events']; cols = [(144, E[:15]), (517, E[15:30])]
    hot = sorted(range(len(E)), key=lambda i: -E[i]['impact'])[:3]; hot = {i for i in hot if E[i]['impact'] >= 2.5}
    for i, e in enumerate(E): e['hot'] = i in hot
    out = []
    for x, es in cols:
        rows, prev = [], None
        for i, e in enumerate(es):
            rows.append(dict(e=e, y=251 + i * 22.3, dim=e['year'] == prev, hl=e['hot'])); prev = e['year']
        out.append(dict(x=x, rows=rows))
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
    if s['mode'] == 'dead':
        xs = [464, 555, 651, 750][:len(s['causes'])]
        for r in s['rows']: r['years'] = int(r['end']) - int(r['start'])
    else:
        xs = [395, 498, 580, 671][:len(s['signs'])]
        for r in s['rows']:
            n = sum(1 for c in r['cells'] if c); r['risk'] = 'High risk' if n >= 3 else 'Medium risk'; r['rn'] = 3 if n >= 3 else 1
    n = len(s['rows']); st = 52 if n >= 5 else 58
    s['geo'] = dict(xs=xs, ys=[318 + i * st for i in range(n)])

def survivors(s):
    s['geo'] = dict(ys=[281 + i * 61 for i in range(len(s['rows']))])

def winner(s):
    n = len(s['companies']); xs = [433 + i * 77 for i in range(n)]
    s['geo'] = dict(xs=xs, ys=[305 + i * 35.8 for i in range(len(s['criteria']))],
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
