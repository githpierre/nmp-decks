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
    const I = (window.ICONS || {})[e] || (window.ICONS || {})[e + '️'] || (window.ICONS || {})[e.replace('️', '')];
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
    sp.innerHTML = parts.join(''); sp.style.display = 'inline-flex'; sp.style.gap = (o.gap || Math.round(size * .25)) + 'px'; sp.style.verticalAlign = 'middle';
    const p = sp.closest('p'); if (p) { p.style.lineHeight = '1'; p.style.display = 'flex'; p.style.justifyContent = p.style.textAlign === 'left' ? 'flex-start' : 'center'; }
  });
  const add = (sl, html) => { const d = document.createElement('div'); d.innerHTML = html; const r = sl.querySelector('.raw') || sl; [...d.children].forEach(c => r.appendChild(c)); return r.lastChild; };
  const div = (sl, x, y, w, h, css, inner = '') => add(sl, `<div style="position:absolute;left:${x}px;top:${y}px;width:${w}px;height:${h}px;${css}">${inner}</div>`);
  const hide = arr => arr.forEach(o => (o.el || o).style.visibility = 'hidden');
  const restroke = (arr, st) => arr.forEach(o => { if (!o.p) return; Object.entries(st).forEach(([k, v]) => v === null ? o.p.removeAttribute(k) : o.p.setAttribute(k, v)); });
  const unfilter = arr => arr.forEach(o => o.el.style.filter = 'none');
  const color = (el, c) => (el.el || el).querySelectorAll('span').forEach(s => s.style.color = c);
  const near = (a, b, d = 6) => Math.abs(a - b) <= d;
  return {C, S, box, shapes, texts, imgs, emojis, swap, svg, add, div, hide, restroke, unfilter, color, near, isEmoji};
})();
