// Visual-audit fixes (11 Nov 2026): generic rules applied to every raw slide after the atelier decisions, plus helpers
// for slide-type fixes. Needs window.A (lib.js). Each rule marks the slides it changed in window.__fixed[rule] (for the report).
window.F = (() => {
  const A = window.A, C = A.C;
  const mark = (rule, sl) => { window.__fixed = window.__fixed || {}; (window.__fixed[rule] = window.__fixed[rule] || new Set()).add(+sl.dataset.n); };
  const vis = el => { for (let e = el; e && e.classList && !e.classList.contains('slide'); e = e.parentElement) { const s = getComputedStyle(e); if (s.visibility === 'hidden' || s.display === 'none') return false; } return true; };
  const rect = (el, sl) => { const r = el.getBoundingClientRect(), R = sl.getBoundingClientRect(); return {x: r.left - R.left, y: r.top - R.top, w: r.width, h: r.height, r: r.right - R.left, b: r.bottom - R.top}; };
  const ink = (el, sl) => { const g = document.createRange(); g.selectNodeContents(el); const q = g.getBoundingClientRect(), R = sl.getBoundingClientRect(); return q.height ? {x: q.left - R.left, y: q.top - R.top, w: q.width, h: q.height, r: q.right - R.left, b: q.bottom - R.top} : null; };
  const mv = (el, dx, dy) => { const s = el.style; if (dx) s.left = (parseFloat(s.left) + dx) + 'px'; if (dy) s.top = (parseFloat(s.top) + dy) + 'px'; };

  // straight two-point lines (connectors): endpoints in slide px + a setter that rewrites the path in its own coordinates
  const lines = sl => { const R = sl.getBoundingClientRect(), out = [];
    sl.querySelectorAll('.raw > svg.rx-s').forEach(svg => { if (!vis(svg)) return; const p = svg.querySelector(':scope > path'); if (!p) return;
      const m = (p.getAttribute('d') || '').match(/^M\s*([-\d.]+)[ ,]+([-\d.]+)\s*L\s*([-\d.]+)[ ,]+([-\d.]+)\s*$/); if (!m) return;
      const M = p.getScreenCTM(); if (!M) return; const toS = (x, y) => { const q = new DOMPoint(x, y).matrixTransform(M); return {x: q.x - R.left, y: q.y - R.top}; };
      const a = toS(+m[1], +m[2]), b = toS(+m[3], +m[4]);
      const set = (na, nb) => { const I = M.inverse(), f = pt => new DOMPoint(pt.x + R.left, pt.y + R.top).matrixTransform(I);
        const A_ = f(na), B_ = f(nb); p.setAttribute('d', `M${A_.x} ${A_.y}L${B_.x} ${B_.y}`); svg.style.overflow = 'visible'; };
      out.push({svg, p, a, b, set, mk: !!(p.getAttribute('marker-end') || p.getAttribute('marker-start')), horiz: Math.abs(a.y - b.y) < 1, vert: Math.abs(a.x - b.x) < 1}); });
    return out; };
  const solids = sl => A.shapes(sl).filter(s => s.p && !s.line && vis(s.el) && s.w > 12 && s.h > 12 && !/^M[-\d.\s]+L[-\d.\s]+$/.test(s.d || ''));

  // 1. connectors that stop 3-45 px before the box or dot they point to are extended to touch it
  const snapLines = sl => { const T = solids(sl); let n = 0;
    lines(sl).forEach(L => { if (!L.horiz && !L.vert) return; let a = {...L.a}, b = {...L.b}, ch = false;
      [[a, b], [b, a]].forEach(([e, o]) => { const dir = L.horiz ? Math.sign(e.x - o.x) : Math.sign(e.y - o.y); if (!dir) return; let best = null;
        T.forEach(t => { const tb = {x: t.x, y: t.y, r: t.x + t.w, b: t.y + t.h};
          if (L.horiz) { if (e.y < tb.y + 2 || e.y > tb.b - 2) return; const edge = dir > 0 ? tb.x : tb.r, g = (edge - e.x) * dir; if (g > 3 && g < 45 && (!best || g < best.g)) best = {g, v: edge - dir * (L.mk ? 2 : 0.5)}; }
          else { if (e.x < tb.x + 2 || e.x > tb.r - 2) return; const edge = dir > 0 ? tb.y : tb.b, g = (edge - e.y) * dir; if (g > 3 && g < 45 && (!best || g < best.g)) best = {g, v: edge - dir * (L.mk ? 2 : 0.5)}; } });
        if (best) { if (L.horiz) e.x = best.v; else e.y = best.v; ch = true; } });
      if (ch) { L.set(a, b); n++; } });
    if (n) mark('snapLines', sl); };

  // 2. a horizontal "bus" line never runs past its outermost stems (tree diagrams)
  const trimBus = sl => { const Ls = lines(sl);
    Ls.filter(L => L.horiz && Math.abs(L.a.x - L.b.x) > 150).forEach(L => { const y = L.a.y, x0 = Math.min(L.a.x, L.b.x), x1 = Math.max(L.a.x, L.b.x);
      const st = Ls.filter(V => V.vert && [V.a.y, V.b.y].some(v => Math.abs(v - y) < 7) && V.a.x > x0 - 2 && V.a.x < x1 + 2).map(V => V.a.x);
      if (st.length < 2) return; const l = Math.min(...st), r = Math.max(...st); if (x0 < l - 8 || x1 > r + 8) { L.set({x: Math.max(x0, l), y}, {x: Math.min(x1, r), y}); mark('trimBus', sl); } }); };

  // 3. a text box drawn as a card (same rectangle) has its text centred vertically, not stuck to the top
  const centerText = sl => { const cs = A.cards(sl), G = {};   // sibling boxes (same row, same size) are centred together or not at all (12 Nov 2026: one header higher than its neighbours). CHECK SIBLING_TOP
    sl.querySelectorAll('.raw > .rx-t').forEach(el => { if (!vis(el) || el.style.justifyContent !== 'flex-start') return; const b = rect(el, sl), k = ink(el, sl); if (!k) return;
      if (!cs.some(c => Math.abs(c.x - b.x) < 4 && Math.abs(c.y - b.y) < 4 && Math.abs(c.w - b.w) < 4 && Math.abs(c.h - b.h) < 4)) return;
      const ok = !(k.h > b.h * .8 || (k.y - b.y) - (b.b - k.b) > -12), key = Math.round(b.y) + '|' + Math.round(b.h) + '|' + Math.round(b.w); (G[key] = G[key] || []).push({el, ok}); });
    Object.values(G).forEach(g => { if (!g.every(o => o.ok)) return; g.forEach(o => { o.el.style.justifyContent = 'center'; }); mark('centerText', sl); }); };

  // 4. column headers drawn in the line colour (#334D54) are invisible on navy: readable grey
  const headers = sl => sl.querySelectorAll('.raw > .rx-t').forEach(el => { const t = el.textContent.trim(); if (!t || t.length > 40 || !vis(el)) return;
    const sp = [...el.querySelectorAll('span')].filter(s => s.textContent.trim() && !s.querySelector('span')); if (!sp.length) return;
    if (!sp.every(s => getComputedStyle(s).color === 'rgb(51, 77, 84)') || parseFloat(getComputedStyle(sp[0]).fontSize) > 17) return;
    sp.forEach(s => { s.style.color = '#8FA3AB'; }); mark('headers', sl); });

  // 5. priority matrices: + / ++ / +++ become mini-gauges (Pierre's choice 30 B, also on raw slides)
  const gauges = sl => sl.querySelectorAll('.raw > .rx-t').forEach(el => { const t = el.textContent.trim(); if (!/^\+{1,3}$/.test(t)) return; const v = t.length, p = el.querySelector('p');
    p.innerHTML = `<span style="display:inline-flex;gap:3px;vertical-align:middle">${[1, 2, 3].map(i => `<i style="display:block;width:9px;height:9px;border-radius:2px;background:${i <= v ? (v === 3 ? C.pink : '#9FB0B7') : '#1E4558'}"></i>`).join('')}</span>`;
    mark('gauges', sl); });

  // 6. same-size cards a few px off their row / column are snapped (contents and connectors of the row move with them)
  const grid = sl => { const cs = A.cards(sl).filter(c => vis(c.el)); if (cs.length < 4) return;
    const all = [...sl.querySelectorAll('.raw > *')].filter(e => vis(e));
    const sizeOK = (a, b) => Math.abs(a.w - b.w) < 3 && Math.abs(a.h - b.h) < 3;
    // rows: cards on the same row (y within 8) moved as a block in x when every card of the row is off by the same 1.5-5 px
    const rows = []; cs.forEach(c => { const r = rows.find(r => Math.abs(r[0].y - c.y) < 8 && sizeOK(r[0], c)); r ? r.push(c) : rows.push([c]); });
    if (rows.length >= 2) { const ref = rows[0].map(c => c.x);
      rows.slice(1).forEach(r => { const d = r.map(c => { const m = ref.reduce((best, x) => Math.abs(x - c.x) < Math.abs(best - c.x) ? x : best, ref[0]); return m - c.x; });
        if (!d.every(v => Math.abs(v - d[0]) < .6) || Math.abs(d[0]) < 1.5 || Math.abs(d[0]) > 5) return;
        const y0 = Math.min(...r.map(c => c.y)) - 24, y1 = Math.max(...r.map(c => c.y + c.h)) + 8;
        all.forEach(e => { const b = rect(e, sl); const cy = b.y + b.h / 2; if (cy > y0 && cy < y1 && b.w < 700) mv(e, d[0], 0); }); mark('grid', sl); }); }
    // single cards a few px off the row's majority y: the card and what sits inside it move
    rows.forEach(r => { if (r.length < 3) return; const ys = r.map(c => Math.round(c.y)), mode = ys.sort((a, b) => ys.filter(v => v === a).length - ys.filter(v => v === b).length).pop();
      r.forEach(c => { const d = mode - c.y; if (Math.abs(d) < 1.5 || Math.abs(d) > 5) return;
        all.forEach(e => { const b = rect(e, sl); if (b.x > c.x - 4 && b.y > c.y - 4 && b.x + b.w < c.x + c.w + 4 && b.y + b.h < c.y + c.h + 4) mv(e, 0, d); }); mark('grid', sl); }); }); };

  // pastille + text centred together in the card, 8 px apart (Pierre's rule)
  const pillText = (sl, gap = 8) => { const R = sl.getBoundingClientRect();
    A.cards(sl).forEach(c => { const inC = t => t.cx > c.x - 4 && t.cx < c.x + c.w + 4 && t.cy > c.y - 30 && t.cy < c.y + c.h + 4;
      const ts = A.texts(sl).filter(inC), pill = ts.find(t => /^\d{1,2}$/.test(t.text)), txt = ts.find(t => t !== pill && t.text.length > 8); if (!pill || !txt) return;
      const ps = pill.el.querySelector('p > span') || pill.el, pr = ps.getBoundingClientRect(), k = ink(txt.el, sl); if (!k) return;
      const H = pr.height + gap + k.h, top = c.y + (c.h - H) / 2;
      mv(pill.el, 0, top - (pr.top - R.top)); mv(txt.el, 0, top + pr.height + gap - k.y); });
    mark('pillText', sl); };

  // dated lists (decision 34 A): the rail is re-drawn even when the original was the wide arrow bar of the "2/2" slides
  const rail = sl => { const sh = A.shapes(sl), R = sh.filter(s => vis(s.el) && s.fill && s.fill.toUpperCase() === C.pink && s.w < 30 && s.h > 150)[0]; if (!R) return;
    const ticks = sh.filter(s => s.stroke === '#789096' && s.h < 22 && s.w > 30 && s.w < 50);
    const dates = A.texts(sl).filter(t => /^\d{4}( \([A-Z]{3}\))?$/.test(t.text) && t.x > R.x && t.x < R.x + 90);
    const ys = ticks.length ? ticks.map(t => t.cy) : dates.map(t => t.cy); if (ys.length < 2) return;
    const cx = R.x + Math.min(R.w, 11) / 2 + (R.w > 14 ? (R.w - 11) / 2 : 0); A.hide(sh.filter(s => s.fill && s.fill.toUpperCase() === C.pink && s.w < 30));
    const y0 = Math.min(...ys), y1 = Math.max(...ys); A.div(sl, cx - 1.5, y0 - 14, 3, y1 - y0 + 28, 'background:#FB0161;border-radius:2px');
    ys.forEach(y => A.div(sl, cx - 5, y - 5, 10, 10, 'border-radius:50%;background:#FB0161;box-shadow:0 0 0 3px #062A3C')); mark('rail', sl); };

  // small arrowheads drawn next to curved connectors become the connector's own arrow (at the end it pointed to)
  const arrowheads = sl => { const sh = A.shapes(sl), heads = sh.filter(s => vis(s.el) && s.fill && s.fill.toUpperCase() === C.pink && s.w < 40 && s.h < 40 && (!s.stroke || s.stroke === 'none')),
      cons = sh.filter(s => vis(s.el) && s.p && s.dash && (s.fill === 'none' || !s.fill)), Rr = sl.getBoundingClientRect();
    heads.forEach(h => { const pts = []; const d = h.p.getAttribute('d').match(/-?\d+(\.\d+)?/g).map(Number); const M = h.p.getScreenCTM();
      for (let i = 0; i + 1 < d.length; i += 2) { const q = new DOMPoint(d[i], d[i + 1]).matrixTransform(M); pts.push({x: q.x - Rr.left, y: q.y - Rr.top}); }
      const cx = pts.reduce((a, p) => a + p.x, 0) / pts.length, cy = pts.reduce((a, p) => a + p.y, 0) / pts.length;
      const o = new DOMPoint(0, 0).matrixTransform(M), u = new DOMPoint(1, 0).matrixTransform(M); const dir = {x: u.x - o.x, y: u.y - o.y};   // block arrows point along their local +x
      let best = null; cons.forEach(c => { const L = c.p.getTotalLength(), M2 = c.p.getScreenCTM();
        for (let s = 0; s <= 40; s++) { const q = c.p.getPointAtLength(L * s / 40).matrixTransform(M2), x = q.x - Rr.left, y = q.y - Rr.top, dd = Math.hypot(x - cx, y - cy);
          if (!best || dd < best.dd) best = {dd, c, s}; } });
      if (!best || best.dd > 60) return; const c = best.c, L = c.p.getTotalLength(), M2 = c.p.getScreenCTM();
      const p0 = c.p.getPointAtLength(Math.max(0, L * best.s / 40 - 2)).matrixTransform(M2), p1 = c.p.getPointAtLength(Math.min(L, L * best.s / 40 + 2)).matrixTransform(M2);
      const fwd = (p1.x - p0.x) * dir.x + (p1.y - p0.y) * dir.y > 0, id = 'ah' + Math.random().toString(36).slice(2, 8);
      const svg = c.el; svg.style.overflow = 'visible'; const defs = document.createElementNS('http://www.w3.org/2000/svg', 'defs');
      defs.innerHTML = `<marker id="${id}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M0 0L10 5L0 10Z" fill="${C.pink}"/></marker>`;
      svg.insertBefore(defs, svg.firstChild); c.p.setAttribute(fwd ? 'marker-end' : 'marker-start', `url(#${id})`); A.hide([h]); });
    mark('arrowheads', sl); };

  // logos (Pierre, 11 Nov): the logo sits inside its white tile with a clear white margin (70 % of the tile), and the tile has a thin light contour
  const logos = sl => { const R = sl.getBoundingClientRect(); const tiles = [...sl.querySelectorAll('.raw > svg.rx-s path')].filter(p => (p.getAttribute('fill') || '').toUpperCase() === '#FFFFFF');
    sl.querySelectorAll('.raw > .rx-i').forEach(i => { const q = i.getBoundingClientRect(); if (q.width > 80) return;
      const t = tiles.find(p => { const z = p.getBoundingClientRect(); return z.left <= q.left + 1 && z.top <= q.top + 1 && z.right >= q.right - 1 && z.bottom >= q.bottom - 1 && z.width < q.width * 2; }); if (!t) return;
      const z = t.getBoundingClientRect(), s = Math.min(z.width, z.height) * .66;
      i.style.left = (z.left - R.left + (z.width - s) / 2) + 'px'; i.style.top = (z.top - R.top + (z.height - s) / 2) + 'px'; i.style.width = s + 'px'; i.style.height = s + 'px'; i.style.borderRadius = '3px';
      t.setAttribute('stroke', '#5E7E8E'); t.setAttribute('stroke-width', '1.5'); t.closest('svg').style.overflow = 'visible'; mark('logos', sl); }); };

  // one name per category everywhere (Pierre, 11 Nov): CREDENTIALING -> DIGITAL CREDENTIALING (titles, subtitles, table rows)
  const names = sl => sl.querySelectorAll('.raw > .rx-t, .subtitle').forEach(el => { const t = el.innerText.replace(/\s+/g, ' ').trim();
    if (!/^credentialing$/i.test(t)) return; const up = t === t.toUpperCase(); const sp = [...el.querySelectorAll('span')].filter(s => s.textContent.trim()).pop() || el;
    sp.textContent = up ? 'DIGITAL CREDENTIALING' : 'Digital credentialing'; mark('names', sl); });

  // category names used as card titles: all on 2 lines when some already are (Pierre, 11 Nov); a one-word name gets a second word
  const CAT2 = {CREDENTIALING: 'DIGITAL CREDENTIALING'};
  const cats = sl => { const ts = A.texts(sl).filter(t => vis(t.el) && t.w < 260 && /^([A-Z][A-Z \-&]{3,40}|.*K-12.*)$/.test(clean2(t)) && getComputedStyle(t.el.querySelector('span') || t.el).fontWeight >= 700);
    const nl = t => t.el.querySelectorAll('p').length > 1 || !!t.el.querySelector('br') || (t.el.querySelector('p').getClientRects()[0] || {}).height > 26; const two = ts.filter(nl); if (two.length < 2) return;
    ts.forEach(t => { const p = t.el.querySelector('p'); let s = clean2(t); if (CAT2[s]) s = CAT2[s]; const w = s.split(' '); if (w.length < 2 || nl(t)) return;
      const sp = p.querySelector('span'); const st = sp ? sp.getAttribute('style') : ''; const cut = Math.ceil(w.length / 2);
      p.innerHTML = `<span style="${st}">${w.slice(0, cut).join(' ')}</span><br><span style="${st}">${w.slice(cut).join(' ')}</span>`; mark('cats', sl); }); };
  const clean2 = t => t.el.innerText.replace(/\s+/g, ' ').trim();

  // labels stuck to a vertical pink bar get the same 12 px gap as slide 143 (Pierre, 11 Nov, fix 32)
  const barGap = sl => { const bars = A.shapes(sl).filter(s => vis(s.el) && s.fill && s.fill.toUpperCase() === C.pink && s.h > 150 && s.w < 30);
    bars.forEach(b => { const R = b.x + b.w, labs = A.texts(sl).filter(t => t.w < 100 && t.x - R >= -2 && t.x - R < 6 && t.cy > b.y && t.cy < b.y + b.h); if (!labs.length) return;
      const lr = Math.max(...labs.map(t => t.x + t.w)), d = R + 7 - Math.min(...labs.map(t => t.x));
      labs.forEach(t => { t.el.style.left = (t.x + d) + 'px'; });
      A.hide(A.shapes(sl).filter(s => s.line && Math.abs(s.x - b.x) < 3 && s.w < 40 && s.h < 20));   // the little ticks would now show as dashes before the labels
      A.texts(sl).filter(t => !labs.includes(t) && t.x >= lr - 2 && t.cy > b.y - 20 && t.cy < b.y + b.h + 20).forEach(t => { t.el.style.left = (t.x + d + 6) + 'px'; });   // the texts on the right keep (and widen) their gap
      mark('barGap', sl); }); };

  // a one-line bold title sitting right above its card is set down on the card (8 px gap), not floating in the middle of its box (Pierre, 11 Nov)
  const titleDown = sl => { const cs = A.cards(sl);
    A.texts(sl).forEach(t => { if (!vis(t.el) || t.h > 70) return; const c = cs.find(c => Math.abs(c.y - (t.y + t.h)) < 5 && Math.abs(c.cx - t.cx) < 6); if (!c) return;
      const sp = t.el.querySelector('span'); if (!sp || +getComputedStyle(sp).fontWeight < 700) return; const k = ink(t.el, sl); if (!k || k.h > 26) return;
      const gap = (t.y + t.h) - k.b; if (gap < 12) return; t.el.style.justifyContent = 'flex-end'; t.el.style.paddingBottom = '8px'; mark('titleDown', sl); }); };

  // pink frames are never a thin line on navy (rule 22): any pink-stroked frame thinner than 3 px gets 4 px (11 Nov)
  const pinkStroke = sl => A.shapes(sl).forEach(s => { if (!vis(s.el) || !s.p || s.line || s.w < 50 || s.h < 30 || !/z/i.test(s.d || '')) return;
    if ((s.stroke || '').toUpperCase() !== C.pink || (s.fill && s.fill !== 'none' && s.fill.toUpperCase() !== '#062A3C')) return;
    const M = s.p.getScreenCTM(), k = M ? Math.hypot(M.a, M.b) : 1; if (!(s.sw * k < 3)) return; s.p.setAttribute('stroke-width', String(4 / k)); s.el.style.overflow = 'visible'; mark('pinkStroke', sl); });

  // a card whose texts are all empty (the research found fewer items than the model has, e.g. 3 categories instead of 6) is hidden,
  // and the cards left are centered vertically in the body (12 Nov)
  const emptyCards = sl => { const R = sl.getBoundingClientRect(); const box = e => { const r = e.getBoundingClientRect(); return {x: r.left - R.left, y: r.top - R.top, r: r.right - R.left, b: r.bottom - R.top}; };
    const T = [...sl.querySelectorAll('.raw > .rx-t')].map(e => ({e, ...box(e), empty: !e.textContent.trim()}));
    let hid = 0;
    sl.querySelectorAll('.raw > svg.rx-s').forEach(sv => { const b = box(sv); if (b.r - b.x < 60 || b.b - b.y < 20) return; const pd = sv.querySelector('path'); if (!pd || !/Z\s*$/i.test((pd.getAttribute('d') || '').trim())) return;   // only closed shapes are cards: a connector line is never hidden (12 Nov: slide 118 lost its lines)
      const ins = T.filter(t => t.x >= b.x - 2 && t.r <= b.r + 2 && t.y >= b.y - 2 && t.b <= b.b + 2);
      if (ins.length && ins.every(t => t.empty)) { sv.style.display = 'none'; sv.dataset.emptied = 1; hid++; } });
    if (!hid) return;
    // what sat on an emptied card goes with it: its icon tile, its pastille, its image (12 Nov 2026: two orphan tiles stayed under the 3 cards kept)
    { const H = [...sl.querySelectorAll('.raw > svg.rx-s[data-emptied]')].map(e => { e.style.display = ''; const b = box(e); e.style.display = 'none'; return b; });
      const V = [...sl.querySelectorAll('.raw > svg.rx-s')].filter(e => !e.dataset.emptied && vis(e)).map(box).filter(b => b.r - b.x >= 60 && b.b - b.y >= 20);
      const hit = (a, b, m) => a.x < b.r + m && a.r > b.x - m && a.y < b.b + m && a.b > b.y - m;
      sl.querySelectorAll('.raw > svg.rx-s, .raw > img, .raw > .rx-i, .raw > .rx-t').forEach(e => { if (e.dataset.emptied || !vis(e)) return; const b = box(e); if (b.r - b.x >= 60 || b.b - b.y >= 60) return;
        if (e.classList.contains('rx-t') && e.textContent.trim().length > 3) return;
        if (H.some(h => hit(b, h, 6)) && !V.some(v => hit(b, v, 6))) { e.style.display = 'none'; e.dataset.emptiedDeco = 1; } }); }
    const body = [...sl.querySelectorAll('.raw > .rx-t, .raw > svg.rx-s, .raw > img')].filter(e => vis(e) && !(e.classList.contains('rx-t') && !e.textContent.trim())).map(e => ({e, ...box(e)})).filter(o => o.y > 140 && o.b < 600);
    if (!body.length) return; const top = Math.min(...body.map(o => o.y)), bot = Math.max(...body.map(o => o.b)), dy = Math.round((150 + 590) / 2 - (top + bot) / 2);
    if (Math.abs(dy) > 4) body.forEach(o => mv(o.e, 0, dy)); mark('emptyCards', sl); };

  // converted bar charts with fixed bar heights (key-trend…): `vbars: [a, b, …]` in deck.yaml sets the heights of the tall pink bars,
  // left to right, in proportion (the tallest keeps its height, bottoms stay put), and the value label above each bar follows it (12 Nov)
  const vbars = sl => { if (!sl.dataset.vbars) return; const V = (sl.dataset.vbars || '').split(',').map(Number).filter(v => !isNaN(v)); if (!V.length) return;
    const R = sl.getBoundingClientRect();
    const bars = [...sl.querySelectorAll('.raw > svg.rx-s')].filter(sv => { const p = sv.querySelector('path'); if (!p) return false;   // plain filled rectangles, pink or grey, tall and narrow
      const f = (p.getAttribute('fill') || '').toUpperCase(), d = (p.getAttribute('d') || '').replace(/\s/g, ''), r = sv.getBoundingClientRect();
      return f && f !== 'NONE' && !/062A3C|0A3243/.test(f) && /^M0,?0H[\d.]+V[\d.]+H0Z$/.test(d) && r.height > 60 && r.width < 140 && r.width < r.height * 1.5; })
      .sort((a, b) => a.getBoundingClientRect().left - b.getBoundingClientRect().left);
    if (bars.length !== V.length) { console.error('vbars: slide ' + sl.dataset.n + ' has ' + bars.length + ' bars for ' + V.length + ' values'); return; }
    const hs = bars.map(b => parseFloat(b.querySelector('path').getAttribute('d').match(/V([\d.]+)/)[1])), H = Math.max(...hs), mx = Math.max(...V);
    const T = [...sl.querySelectorAll('.raw > .rx-t')];
    bars.forEach((b, i) => { const p = b.querySelector('path'), h0 = hs[i], h = Math.max(4, H * V[i] / mx), d = h0 - h, br = b.getBoundingClientRect();
      p.setAttribute('d', p.getAttribute('d').replace(/V[\d.]+/, 'V' + h.toFixed(2)));
      const top0 = parseFloat(b.style.top); b.style.top = (top0 + d) + 'px'; b.style.height = (parseFloat(b.style.height) - d) + 'px'; b.setAttribute('viewBox', b.getAttribute('viewBox').replace(/([\d.]+)$/, (parseFloat(b.style.height)).toFixed(1)));
      const lab = T.find(t => { const r = t.getBoundingClientRect(); return Math.abs((r.left + r.right) / 2 - (br.left + br.right) / 2) < 40 && r.bottom <= br.top + 6 && br.top - r.bottom < 40; });
      if (lab) mv(lab, 0, d); });
    mark('vbars', sl); };


  // ---- data-driven geometry for the converted TEMP series slides (12 Nov): hbars, dots, curves, split
  const rects = sl => [...sl.querySelectorAll('.raw > svg.rx-s')].filter(sv => { const p = sv.querySelector('path'); if (!p || !vis(sv)) return false;
      const f = (p.getAttribute('fill') || '').toUpperCase(), d = (p.getAttribute('d') || '').replace(/\s/g, '');
      return f && f !== 'NONE' && !/062A3C|0A3243/.test(f) && /^M0,?0H[\d.]+V[\d.]+H0Z$/.test(d); });
  const setW = (sv, w) => { const p = sv.querySelector('path'), d = p.getAttribute('d'); const w0 = parseFloat(d.match(/H([\d.]+)/)[1]); p.setAttribute('d', d.replace(/H[\d.]+/, 'H' + w.toFixed(2))); const dw = w - w0; sv.style.width = (parseFloat(sv.style.width) + dw) + 'px'; const vb = sv.getAttribute('viewBox').split(/\s+/).map(Number); vb[2] += dw; sv.setAttribute('viewBox', vb.join(' ')); return dw; };
  const hbars = sl => { if (!sl.dataset.hbars) return; const V = (sl.dataset.hbars || '').split(',').map(Number).filter(v => !isNaN(v)); if (!V.length) return;
    /* bars of one chart share their left edge: a very short bar (the smallest value) is still a bar (13 Nov 2026: the 5th bar was skipped, so nothing was resized and nobody saw it) */
    const cand = rects(sl).filter(sv => { const r = sv.getBoundingClientRect(); return r.height < 44 && r.height > 6; }), G = {};
    cand.forEach(sv => { const k = Math.round(sv.getBoundingClientRect().left / 4); (G[k] = G[k] || []).push(sv); });
    const bars = (Object.values(G).find(g => g.length === V.length) || []).sort((a, b) => a.getBoundingClientRect().top - b.getBoundingClientRect().top);
    if (bars.length !== V.length) { console.error('hbars: slide ' + sl.dataset.n + ' has no group of ' + V.length + ' bars for its ' + V.length + ' values'); return; } const ws = bars.map(b => parseFloat(b.querySelector('path').getAttribute('d').match(/H([\d.]+)/)[1])), W = Math.max(...ws), mx = Math.max(...V);
    const T = [...sl.querySelectorAll('.raw > .rx-t')];
    bars.forEach((b, i) => { const r = b.getBoundingClientRect(); const lab = T.filter(t => { const q = t.getBoundingClientRect(); return q.left > r.right - 12 && q.left - r.right < 40 && Math.abs((q.top + q.bottom) / 2 - (r.top + r.bottom) / 2) < 14; });
      const dw = setW(b, Math.max(3, W * V[i] / mx)); lab.forEach(t => mv(t, dw, 0));
      const hp = +(sl.dataset.hpink || 0); if (hp) b.querySelector('path').setAttribute('fill', i < hp ? '#FB0161' : i === bars.length - 1 ? '#334D54' : '#789096'); });
    mark('hbars', sl); };
  const split = sl => { if (!sl.dataset.split) return; const V = (sl.dataset.split || '').split(',').map(Number); if (V.length !== 2) return;
    const bars = rects(sl).filter(sv => sv.getBoundingClientRect().height > 100).sort((a, b) => a.getBoundingClientRect().left - b.getBoundingClientRect().left); if (bars.length !== 2) return;
    const w = bars.map(b => parseFloat(b.querySelector('path').getAttribute('d').match(/H([\d.]+)/)[1])), tot = w[0] + w[1], w0 = Math.max(4, tot * V[0] / (V[0] + V[1]));
    const T = [...sl.querySelectorAll('.raw > .rx-t')], r1 = bars[1].getBoundingClientRect(); const right = T.filter(t => { const q = t.getBoundingClientRect(); return q.left >= r1.left - 2 && q.left < r1.right + 40 && q.top > r1.top - 5 && q.bottom < r1.bottom + 5; });
    const d0 = setW(bars[0], w0); setW(bars[1], tot - w0); mv(bars[1], d0, 0); mark('split', sl); };   // the right edge does not move, nor the labels right of it
  const dots = sl => { let G; try { G = JSON.parse(sl.dataset.dots || 'null'); } catch (e) { return; } if (!G) return;
    const D = [...sl.querySelectorAll('.raw > svg.rx-s')].filter(sv => { const p = sv.querySelector('path'), r = sv.getBoundingClientRect(); return p && r.width < 30 && r.height < 30 && /A/.test(p.getAttribute('d') || '') && /FB0161|FFFFFF|334D54|5E7E8E|789096/i.test(p.getAttribute('fill') || ''); });
    const TT = [...sl.querySelectorAll('.raw > .rx-t')].filter(t => t.textContent.trim()).map(t => t.getBoundingClientRect());
    const legend = D.filter(sv => { const r = sv.getBoundingClientRect(); return TT.some(q => q.left - r.right > -14 && q.left - r.right < 14 && Math.abs((q.top + q.bottom) / 2 - (r.top + r.bottom) / 2) < 10); });   // a legend dot has its label right next to it
    const cells = D.filter(d => !legend.includes(d)).map(sv => ({sv, r: sv.getBoundingClientRect()})).sort((a, b) => a.r.left - b.r.left);
    const groups = []; cells.forEach(c => { const g = groups[groups.length - 1]; if (g && c.r.left - g[g.length - 1].r.left < 30) g.push(c); else groups.push([c]); });
    if (groups.length !== G.length) return; const col = ['#FB0161', '#FFFFFF', '#334D54'];
    groups.forEach((g, gi) => { g.sort((a, b) => (b.r.top - a.r.top) || (a.r.left - b.r.left)); let k = 0;
      g.forEach((c, i) => { let n = 0, ci = -1; for (let j = 0; j < G[gi].length; j++) { n += G[gi][j]; if (i < n) { ci = j; break; } }
        if (ci < 0) c.sv.style.visibility = 'hidden'; else { c.sv.style.visibility = ''; c.sv.querySelector('path').setAttribute('fill', col[ci]); } }); });
    mark('dots', sl); };
  const curves = sl => { let C; try { C = JSON.parse(sl.dataset.curves || 'null'); } catch (e) { return; } if (!C) return;
    const P = [...sl.querySelectorAll('.raw > svg.rx-s path')].filter(p => ((p.getAttribute('d') || '').match(/L/g) || []).length > 5).sort((a, b) => b.getAttribute('d').length - a.getAttribute('d').length).slice(0, C.length);
    if (P.length !== C.length) return; const R = sl.getBoundingClientRect();
    const bb = P.map(p => p.getBoundingClientRect()); const top = Math.min(...bb.map(b => b.top)), bot = Math.max(...bb.map(b => b.bottom));
    const all = C.flat(), lo = Math.min(...all), hi = Math.max(...all);
    P.forEach((p, i) => { const b = bb[i], M = p.getScreenCTM(); if (!M) return; const I = M.inverse(), s = C[i];
      const pts = s.map((v, j) => { const x = b.left + (b.width) * j / (s.length - 1), y = bot - (bot - top) * (v - lo) / ((hi - lo) || 1); const q = new DOMPoint(x, y).matrixTransform(I); return q.x.toFixed(1) + ' ' + q.y.toFixed(1); });
      p.setAttribute('d', 'M' + pts.join('L')); p.closest('svg').style.overflow = 'visible'; });
    sl.querySelectorAll('.raw > svg.rx-s').forEach(sv => { const r = sv.getBoundingClientRect(), d = sv.querySelector('path')?.getAttribute('d') || ''; if ((r.width < 32 && r.height < 32 && /A/.test(d)) || (r.width < 22 && r.height > 120 && /^M0 0L0/.test(d))) sv.style.visibility = 'hidden'; });
    mark('curves', sl); };

  // generic rules, every raw slide

  // short date labels of timelines ("Early 2024", "Oct - Dec 24", "Today") are always written in capitals (Pierre, 12 Nov 2026)
  const DATE_RX = /^(?=.*(\b(19|20)\d{2}\b|\b\d{2}\b|\btoday\b|\bnow\b))((early|mid|late|since|before|after|by|until|from|end of|start of|today|now|q[1-4]|h[12]|jan|feb|mar|apr|may|jun|jul|aug|sep|sept|oct|nov|dec)[a-z]*\.?|(19|20)?\d{2}|[-–/&+, ])+$/i;
  const dateCaps = sl => { sl.querySelectorAll('.raw .rx-t').forEach(el => { const t = el.textContent.replace(/\s+/g, ' ').trim();
    if (!t || t.length > 20 || !DATE_RX.test(t) || t === t.toUpperCase()) return; const h0 = el.getBoundingClientRect().height, sp = el.querySelector('span') || el, ink0 = ink(sp, sl);
    el.style.textTransform = 'uppercase'; mark('dateCaps', sl);
    /* capitals are wider: a label that fitted on one line must stay on one line (shrink a little, never wrap) */
    const lh = parseFloat(getComputedStyle(sp).lineHeight) || 20; let k = 0;
    while (ink0 && ink(sp, sl) && ink(sp, sl).h > ink0.h + lh * 0.5 && k++ < 12) el.querySelectorAll('span').forEach(x => { x.style.fontSize = (parseFloat(getComputedStyle(x).fontSize) * 0.96) + 'px'; }); }); };

  // centred sentences of 2 lines or more: lines as equal as possible, like the titles (Pierre, 12 Nov 2026). CHECK TEXT_BALANCE
  const balance = sl => { sl.querySelectorAll('p, div').forEach(el => { if (el.closest('.title, .note, .foot-label, .foot-brand, .section, .pillrow')) return;
    if (el.querySelector('p, div, br, svg, img')) return; const t = el.textContent.trim(); if (t.length < 50) return;
    const cs = getComputedStyle(el); if (cs.textAlign !== 'center') return; const lh = parseFloat(cs.lineHeight) || parseFloat(cs.fontSize) * 1.3;
    if (el.getBoundingClientRect().height < lh * 1.6) return; el.style.textWrap = 'balance'; mark('balance', sl); }); };
  // SIGNAL slides: the content block sits centred between the pill and the note, never stuck under the pill (Pierre, 12 Nov 2026). CHECK PILL_GAP
  const SKIP = '.tri, .section, .title, .subtitle, .pillrow, .note, .wtag, .foot-line, .foot-label, .foot-brand, script, style';
  const contentBox = sl => { const R = sl.getBoundingClientRect(); let top = 1e9, bot = -1e9; const els = [];
    [...sl.children].forEach(c => { if (c.matches(SKIP)) return; (c.classList.contains('raw') ? [...c.children] : [c]).forEach(e => { if (e.matches && e.matches(SKIP)) return;
      let r = e.classList && e.classList.contains('rx-t') ? ink(e, sl) : rect(e, sl); els.push(e);
      if (e.tagName && e.tagName.toLowerCase() === 'svg') { const ks = [...e.querySelectorAll('path, rect, line, circle, ellipse, polyline, polygon, text')].filter(k => !k.closest('defs')).map(k => rect(k, sl)).filter(q => q.w > 0.5 || q.h > 0.5); if (ks.length) { const y = Math.min(...ks.map(q => q.y)), b = Math.max(...ks.map(q => q.b)); r = {y, b, h: Math.max(1, b - y), w: 2}; } }   /* the drawing, not the padded svg box */
      if (!e.classList || !e.classList.contains('rx-t')) { const ts = [...e.querySelectorAll('*')].filter(k => !k.children.length && k.textContent.trim()); if (!e.tagName || e.tagName.toLowerCase() !== 'svg') { const all = [...e.querySelectorAll('*')].filter(k => getComputedStyle(k).visibility !== 'hidden' && k.getBoundingClientRect().height > 0.5 && !k.children.length).map(k => rect(k, sl)); if (all.length) { const y = Math.min(...all.map(q => q.y)), b = Math.max(...all.map(q => q.b)); r = {y, b, h: Math.max(1, b - y), w: 2}; } } }   /* template slides: the visible leaves, not the stretched body box */ if (!r || r.h < 1 || r.w < 1 || getComputedStyle(e).visibility === 'hidden') return; top = Math.min(top, r.y); bot = Math.max(bot, r.b); }); });
    return {top, bot, els}; };
  const pillCentre = sl => { const pr = sl.querySelector('.pillrow .pill'); if (!pr || /^pp_/.test(sl.dataset.type || '')) return;   /* product-page twins keep the live layout */ const R = sl.getBoundingClientRect(), p = pr.getBoundingClientRect().bottom - R.top;
    const n = sl.querySelector('.note') || sl.querySelector('.foot-line'); const nb = n.getBoundingClientRect().top - R.top; const c = contentBox(sl); if (c.top > 1e8) return;
    const free = (nb - p) - (c.bot - c.top), dy = Math.round(free * 0.55 - (c.top - p)); if (dy < 6 || free < 30) return;   // a little lower than the middle: 55 % of the free space above (Pierre, 12 Nov: « plus proche du bas que du SIGNAL »)
    c.els.forEach(e => { e.style.transform = ((e.style.transform || '') + ' translateY(' + dy + 'px)').trim(); }); sl.dataset.pillDy = dy; mark('pillCentre', sl); };
  // « Which categories will we use? »: names in capitals on 2 lines at most (one size for all), every card the same size and on the same lines
  // (the PPTX slots differ by 2 px), filled cards centred: 4 = 2 + 2, others up to 3 per row (Pierre, 12 Nov 2026). Runs after the refit.
  const catsGrid = sl => { const raw = sl.querySelector('.raw'), K = k => raw.querySelector(`.rx-t[data-k="${k}"]`), S = [...raw.querySelectorAll(':scope > svg.rx-s')];
    const cards = [[7,6],[9,8],[11,10],[13,12],[15,14],[17,16]].map(([l, d], i) => ({l: K(l), d: K(d), s: S[i]})), full = cards.filter(c => c.l && c.l.textContent.trim()); if (!full.length) return;
    cards.filter(c => !full.includes(c)).forEach(c => [c.l, c.d, c.s].forEach(e => e && (e.style.display = 'none')));
    const n = full.length, cols = n === 4 ? 2 : Math.min(n, 3), W = 165.8, G = 13, x0 = (960 - (cols * W + (cols - 1) * G)) / 2, LT = [199, 381.7], DT = [256, 438.7], model = S[0].cloneNode(true);
    full.forEach((c, i) => { const col = i % cols, row = Math.floor(i / cols), x = x0 + col * (W + G);
      c.l.style.cssText += `;left:${x - 6}px;top:${LT[row]}px;width:${W + 12}px;height:54.7px;padding:0 2px 8px;text-transform:uppercase;justify-content:flex-end`;
      c.d.style.cssText += `;left:${x}px;top:${DT[row]}px;width:${W}px;height:105.6px`;
      const sv = model.cloneNode(true); sv.style.left = (x - 9) + 'px'; sv.style.top = (DT[row] - 9) + 'px'; sv.style.display = ''; c.s.replaceWith(sv); });
    const lines = e => { const i = ink(e, sl); const lh = parseFloat(getComputedStyle(e.querySelector('p') || e).lineHeight) || 18; return i ? Math.round(i.h / lh) : 0; };
    let fs = 11; const set = () => full.forEach(c => c.l.querySelectorAll('p, span').forEach(x => { x.style.fontSize = fs + 'pt'; x.style.textWrap = 'balance'; })); set();
    while (fs > 8.5 && full.some(c => lines(c.l) > 2)) { fs -= 0.5; set(); }
    const mx = Math.max(...full.map(c => lines(c.l))); full.forEach(c => { let p = 2; while (lines(c.l) < mx && p < 60) { p += 3; c.l.style.paddingLeft = c.l.style.paddingRight = p + 'px'; } });   // same number of lines for every name
    mark('catsGrid', sl); };
  // a figure is never cut in two lines (12 Nov 2026: « 12,0 / 00 » above its bar). CHECK WORD_SPLIT
  const figures = sl => sl.querySelectorAll('.raw > .rx-t').forEach(el => { const t = el.textContent.trim(); if (t && t.length <= 12 && /^[≈~×x$€£+\-]?[\d][\d.,]*\s?[%KMBx+]*$/.test(t)) { el.style.whiteSpace = 'nowrap'; el.style.overflow = 'visible'; el.querySelectorAll('p, span').forEach(x => { x.style.whiteSpace = 'nowrap'; }); } });
  const all = sl => { try { names(sl); } catch (e) {} try { balance(sl); } catch (e) {} try { figures(sl); } catch (e) {}
    if (sl.querySelector('.raw')) { [dateCaps, vbars, hbars, split, dots, curves, emptyCards, centerText, headers, gauges, grid, logos, cats, barGap, titleDown].forEach(f => { try { f(sl); } catch (e) { console.error('fix', f.name, sl.dataset.n, e); } });
      try { if (window.__fitapi && window.__fitapi.slideFit) window.__fitapi.slideFit(sl); } catch (e) { console.error('refit', sl.dataset.n, e); } }   // equal line counts on the final geometry
    try { if (sl.dataset.tpl === 'categories_will_use') catsGrid(sl); } catch (e) { console.error('catsGrid', sl.dataset.n, e); }
    try { pillCentre(sl); } catch (e) { console.error('pillCentre', sl.dataset.n, e); } };   // last: on the final geometry
  // segment dividers: ONE title size for the whole deck, the largest at which the longest name stays clear of the side arrows
  // (Pierre, 12 Nov 2026: the arrows ran over « BIPEDAL GENERAL-PURPOSE HUMANOIDS »). CHECK TEXT_ON_LINE
  const deck = () => { const D = [...document.querySelectorAll('.slide[data-tpl="divider_3"]')].map(sl => ({sl, el: sl.querySelector('.rx-t[data-k="3"]')})).filter(o => o.el && o.el.textContent.trim());
    if (!D.length) return; let k = 1; D.forEach(o => { o.el.querySelectorAll('span').forEach(x => { x.style.whiteSpace = 'nowrap'; }); const i = ink(o.el, o.sl); if (i) k = Math.min(k, 640 / i.w); });
    if (k < 1) D.forEach(o => { o.el.querySelectorAll('span').forEach(x => { x.style.fontSize = (parseFloat(getComputedStyle(x).fontSize) * k) + 'px'; }); mark('dividerSize', o.sl); }); };
  return {deck, all, logos, cats, snapLines, trimBus, centerText, headers, gauges, grid, pillText, rail, arrowheads, lines, rect, ink, mv, mark, vis};
})();
