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
  const centerText = sl => { const cs = A.cards(sl);
    sl.querySelectorAll('.raw > .rx-t').forEach(el => { if (!vis(el) || el.style.justifyContent !== 'flex-start') return; const b = rect(el, sl), k = ink(el, sl); if (!k) return;
      if (!cs.some(c => Math.abs(c.x - b.x) < 4 && Math.abs(c.y - b.y) < 4 && Math.abs(c.w - b.w) < 4 && Math.abs(c.h - b.h) < 4)) return;
      if (k.h > b.h * .8 || (k.y - b.y) - (b.b - k.b) > -12) return; el.style.justifyContent = 'center'; mark('centerText', sl); }); };

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

  // generic rules, every raw slide
  const all = sl => { if (!sl.querySelector('.raw')) return; [centerText, headers, gauges, snapLines, trimBus, grid].forEach(f => { try { f(sl); } catch (e) { console.error('fix', f.name, sl.dataset.n, e); } }); };
  return {all, snapLines, trimBus, centerText, headers, gauges, grid, pillText, rail, arrowheads, lines, rect, ink, mv, mark, vis};
})();
