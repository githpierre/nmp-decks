// Helpers injected in deck.html for the "100 improvements" atelier: find shapes, texts, emojis on a raw slide and restyle them.
window.A = (() => {
  const C = {navy: '#062A3C', navy2: '#0B3850', navy3: '#123F57', line: '#334D54', cream: '#E7CDA8', pink: '#FB0161', white: '#FFFFFF', grey: '#7E949E'};
  const S = n => document.querySelector(`.slide[data-n="${n}"]`);
  const box = (el, sl) => { const r = el.getBoundingClientRect(), R = sl.getBoundingClientRect(); return {x: r.left - R.left, y: r.top - R.top, w: r.width, h: r.height, cx: r.left - R.left + r.width / 2, cy: r.top - R.top + r.height / 2}; };
  const shapes = sl => [...sl.querySelectorAll('.raw > svg.rx-s')].map(el => { const p = el.querySelector(':scope > path'); let b = box(p || el, sl); if (b.w < 1 || b.h < 1) { const e = box(el, sl); b = Object.assign(e, {w: Math.max(b.w, 1), h: Math.max(b.h, 1)}); b = box(el, sl); }
    return Object.assign(b, {el, p, fill: p && p.getAttribute('fill'), stroke: p && p.getAttribute('stroke'), dash: p && p.getAttribute('stroke-dasharray'), sw: p && +p.getAttribute('stroke-width'), d: p && p.getAttribute('d'), line: !!(p && /^M[\d.\s-]+L[\d.\s-]+$/.test(p.getAttribute('d')))}); });
  const texts = sl => [...sl.querySelectorAll('.raw > .rx-t')].map(el => Object.assign(box(el, sl), {el, text: el.textContent.trim(), k: +el.dataset.k}));
  const imgs = sl => [...sl.querySelectorAll('.raw > .rx-i')].map(el => Object.assign(box(el, sl), {el}));
  const isEmoji = t => t && [...t.replace(/\s|️|‍/g, '')].every(ch => ch.codePointAt(0) > 0x2000) && /\p{Extended_Pictographic}|✓/u.test(t);
  const emojis = sl => [...sl.querySelectorAll('span, div')].filter(s => !s.children.length && isEmoji(s.textContent.trim()));
  const split = t => (t.match(/(\p{Extended_Pictographic}(️)?(‍\p{Extended_Pictographic}(️)?)*)|✓/gu) || []);
  const svg = (e, style, size, color, sw) => {
    let I = (window.ICONS || {})[e] || (window.ICONS || {})[e + '️'] || (window.ICONS || {})[e.replace('️', '')];
    if (!I) { (window.__emojiMiss = window.__emojiMiss || []).push(e); I = (window.ICONS || {})['__default__']; }  // 12 Nov: an unmapped emoji never stays an emoji among icons (audit EMOJI_UNMAPPED)
    if (!I) return null;
    let s = style === 'line' ? I.line : style === 'fill' ? I.fill : I.duo;
    s = s.replace(/<svg([^>]*)>/, (m, a) => '<svg' + a.replace(/\s(width|height|class)="[^"]*"/g, '') + ` width="${size}" height="${size}" style="display:block;color:${color}">`);
    if (style === 'line') s = s.replace(/stroke-width="[^"]*"/, `stroke-width="${sw || 1.75}"`);
    return s;
  };
  // Replace every emoji by an icon. o = {style:'line'|'duo'|'fill', color, scale, ring:{bg,border,pad}, sw}
  const swap = (sl, o = {}) => emojis(sl).forEach(sp => {
    const fs = parseFloat(getComputedStyle(sp).fontSize), size = o.size || Math.round(fs * (o.scale || 1));
    const parts = split(sp.textContent).map(e => {
      const ic = svg(e, o.style || 'line', size, o.color || C.cream, o.sw); if (!ic) return null;
      if (!o.ring) return `<span style="display:inline-flex">${ic}</span>`;
      const pad = Math.round(size * (o.ring.pad || .45));
      return `<span style="display:inline-flex;align-items:center;justify-content:center;width:${size + 2 * pad}px;height:${size + 2 * pad}px;border-radius:${o.ring.radius || '50%'};background:${o.ring.bg || 'transparent'};border:${o.ring.border || 'none'};box-sizing:border-box">${ic}</span>`;
    });
    if (parts.some(x => !x)) return;
    sp.innerHTML = parts.join(''); sp.classList.add('aic'); sp.style.display = 'inline-flex'; sp.style.gap = (o.gap || Math.round(size * .25)) + 'px'; sp.style.verticalAlign = 'middle';
    const p = sp.closest('p'); if (p) { p.style.lineHeight = '1'; p.style.display = 'flex'; p.style.justifyContent = p.style.textAlign === 'left' ? 'flex-start' : 'center'; }
  });
  const add = (sl, html) => { const d = document.createElement('div'); d.innerHTML = html; const r = sl.querySelector('.raw') || sl; [...d.children].forEach(c => r.appendChild(c)); return r.lastChild; };
  const div = (sl, x, y, w, h, css, inner = '') => add(sl, `<div style="position:absolute;left:${x}px;top:${y}px;width:${w}px;height:${h}px;${css}">${inner}</div>`);
  const hide = arr => arr.forEach(o => (o.el || o).style.visibility = 'hidden');
  const restroke = (arr, st) => arr.forEach(o => { if (!o.p) return; Object.entries(st).forEach(([k, v]) => v === null ? o.p.removeAttribute(k) : o.p.setAttribute(k, v)); });
  const unfilter = arr => arr.forEach(o => o.el.style.filter = 'none');
  const color = (el, c) => (el.el || el).querySelectorAll('span').forEach(s => s.style.color = c);
  const near = (a, b, d = 6) => Math.abs(a - b) <= d;
  // cards = drawn boxes (not lines, not tiny marks)
  const cards = sl => shapes(sl).filter(s => s.p && s.stroke && s.stroke !== 'none' && !s.line && s.w > 90 && s.h > 40 && s.w < 700);
  const inside = (b, c, m = 2) => b.cx > c.x - m && b.cx < c.x + c.w + m && b.cy > c.y - m && b.cy < c.y + c.h + m;
  const contentRect = el => { const r = document.createRange(); r.selectNodeContents(el); const q = r.getBoundingClientRect(); return q; };
  // centre the content of each card (icon + text together) vertically; off = extra px down
  const centerCards = (sl, off = 0, list) => { const R = sl.getBoundingClientRect();
    (list || cards(sl)).forEach(c => { const ts = texts(sl).filter(t => inside(t, c) && t.el.style.visibility !== 'hidden' && !/^\d{1,2}$/.test(t.text) && t.w > 40); if (!ts.length) return;
      let y0 = 1e9, y1 = -1e9; ts.forEach(t => { const q = contentRect(t.el); if (!q.height) return; y0 = Math.min(y0, q.top - R.top); y1 = Math.max(y1, q.bottom - R.top); });
      if (y1 < 0) return; const d = (c.y + c.h / 2) - (y0 + y1) / 2 + off; ts.forEach(t => t.el.style.top = (parseFloat(t.el.style.top) + d) + 'px'); }); };
  // put every swapped icon (class aic) exactly on the nearest card corner
  const toCorner = sl => { const R = sl.getBoundingClientRect(), cs = cards(sl);
    sl.querySelectorAll('.aic').forEach(sp => { const q = sp.getBoundingClientRect(), x = q.left - R.left + q.width / 2, y = q.top - R.top + q.height / 2;
      let best = null; cs.forEach(c => [[c.x, c.y], [c.x + c.w, c.y], [c.x, c.y + c.h], [c.x + c.w, c.y + c.h]].forEach(([px, py]) => { const d = Math.hypot(px - x, py - y); if (!best || d < best.d) best = {d, px, py}; }));
      if (!best || best.d > 60) return; const t = sp.closest('.rx-t'); if (!t) return;
      t.style.left = (parseFloat(t.style.left) + best.px - x) + 'px'; t.style.top = (parseFloat(t.style.top) + best.py - y) + 'px'; t.style.zIndex = 3; }); };
  // emoji -> icon in a pastille, repositioned with the card text. mode: 'flow' (above the text, block centred), 'top' (on the top edge), 'corner' (on the top-left corner)
  const cardPill = (sl, mode, o = {}) => { const R = sl.getBoundingClientRect(), cs = cards(sl), D = o.d || 32, ic = o.ic || 16;
    emojis(sl).forEach(sp => { const t = sp.closest('.rx-t'); if (!t) return; const tb = box(t, sl);
      const c = cs.filter(c => inside(tb, c, 4)).sort((a, b) => a.w * a.h - b.w * b.h)[0]; if (!c) return;
      const e = sp.textContent.trim(), svgs = split(e).map(x => svg(x, 'line', ic, o.color || C.cream, o.sw || 1.8)).join(''); if (!svgs) return;
      const p = sp.closest('p'), others = [...t.querySelectorAll('p')].filter(q => q !== p && q.textContent.trim());
      if (others.length) p.style.display = 'none'; else t.style.visibility = 'hidden';
      const pill = div(sl, 0, 0, D, D, `border-radius:${o.radius || '50%'};background:${o.bg || '#0E3A50'};border:${o.border || '1px solid rgba(231,205,168,.28)'};box-sizing:border-box;display:flex;align-items:center;justify-content:center;z-index:3;box-shadow:${o.shadow || 'none'}`, svgs);
      const ts = texts(sl).filter(x => inside(x, c, 2) && x.el.style.visibility !== 'hidden' && !isEmoji(x.text) && !/^\d{1,2}$/.test(x.text) && x.w > 40);
      let y0 = 1e9, y1 = -1e9; ts.forEach(x => { const q = contentRect(x.el); if (!q.height) return; y0 = Math.min(y0, q.top - R.top); y1 = Math.max(y1, q.bottom - R.top); });
      const gap = o.gap || 10; let dy = 0, px, py;
      if (mode === 'flow') { const tot = D + gap + (y1 - y0), st = c.y + (c.h - tot) / 2; px = c.cx - D / 2; py = st; dy = st + D + gap - y0; }
      else { const off = mode === 'top' ? D / 4 : 0; dy = c.y + c.h / 2 - (y0 + y1) / 2 + off; if (mode === 'top') { px = c.cx - D / 2; py = c.y - D / 2; } else { px = c.x - D / 2 + 2; py = c.y - D / 2 + 2; } }
      pill.style.left = px + 'px'; pill.style.top = py + 'px';
      ts.forEach(x => x.el.style.top = (parseFloat(x.el.style.top) + dy) + 'px'); }); };
  // open the gap between card rows so a pill posed on the top edge never touches the row above; keeps the block centred
  const spaceRows = (sl, need) => { const cs = cards(sl).filter(c => c.w > 120); const rows = [];
    cs.sort((a, b) => a.y - b.y).forEach(c => { const r = rows.find(r => Math.abs(r.y - c.y) < 8); if (r) { r.c.push(c); r.b = Math.max(r.b, c.y + c.h); } else rows.push({y: c.y, b: c.y + c.h, c: [c]}); });
    if (rows.length < 2) return; let tot = 0; const sh = [0];
    for (let i = 1; i < rows.length; i++) { const g = rows[i].y - rows[i - 1].b; tot += Math.max(0, need - g); sh.push(tot); }
    if (!tot) return; const R = sl.getBoundingClientRect(), half = tot / 2;
    [...sl.querySelectorAll('.raw > *')].forEach(e => { const b = e.getBoundingClientRect(), cy = b.top - R.top + b.height / 2; if (b.height > 400) return;
      let k = -1; rows.forEach((r, i) => { if (cy >= r.y - 30 && cy <= r.b + 6) k = i; }); if (k < 0) return;
      e.style.top = (parseFloat(e.style.top) + sh[k] - half) + 'px'; }); };
  // the type rule (Pierre, 10 Nov): numbered card grids -> pill above the text in the flow; plain grids -> pill on the top edge, rows spaced
  const cardPillAuto = sl => { const numbered = shapes(sl).some(s => s.w < 34 && s.h < 34 && s.w > 22 && s.fill === '#062A3C');
    if (numbered) cardPill(sl, 'flow', {d: 34, ic: 18}); else { spaceRows(sl, 36); cardPill(sl, 'top', {d: 36, ic: 18, bg: '#062A3C'}); } };
  return {cardPillAuto, spaceRows, cardPill, cards, inside, centerCards, toCorner, contentRect, C, S, box, shapes, texts, imgs, emojis, swap, svg, add, div, hide, restroke, unfilter, color, near, isEmoji};
})();
