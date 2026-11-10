/* A one-line label is never stretched to the group count.
   Raw slides: parallel boxes get the same number of lines, and every multi-line text is balanced
   (Pierre's rules, 10 Nov 2026). Groups = text boxes of the same width and font size, on one row or one column.
   For each paragraph we pick the line breaks (dynamic programming) that make the lines as equal as possible
   for the target line count: the group's largest natural count, or data-lines when set in overrides.yaml. */
(() => {
  const words = p => {                       // wrap words in spans once; return [{a, b, sp}] segments (sp = space node before)
    if (!p._segs) {
      const tw = document.createTreeWalker(p, NodeFilter.SHOW_TEXT), nodes = []; let nd;
      while ((nd = tw.nextNode())) nodes.push(nd);
      nodes.forEach(t => { const f = document.createDocumentFragment();
        t.textContent.replace(/(\$?£?€?[\d.,]+\+?) (billion|million|trillion|thousand|percent|hours?|years?|days?|weeks?|months?|minutes?)\b/gi, '$1\u00a0$2').split(/( +)/).forEach(s => { if (!s) return; if (/^ +$/.test(s)) f.appendChild(document.createTextNode(' '));
          else { const w = document.createElement('span'); w.className = 'fw'; w.textContent = s; f.appendChild(w); } });
        t.replaceWith(f); });
      const segs = []; let cur = null, sp = null;
      const walk = n => n.childNodes.forEach(c => {
        if (c.nodeType === 3) { if (c.textContent === ' ') { sp = c; cur = null; } }
        else if (c.classList && c.classList.contains('fw')) { if (!cur) { cur = {spans: [], sp}; segs.push(cur); sp = null; } cur.spans.push(c); }
        else walk(c); });
      walk(p); p._segs = segs;
    }
    return p._segs;
  };
  const rows = p => { words(p); const r = new Set(); p.querySelectorAll('.fw').forEach(s => [...s.getClientRects()].forEach(x => r.add(Math.round(x.top / 3)))); return r.size; };
  const fit = (p, N) => {
    const segs = words(p); if (segs.length < 2 || N < 2) return;
    const maxW = p.getBoundingClientRect().width - 1;
    p.style.whiteSpace = 'nowrap'; p.style.textWrap = 'nowrap';
    const L = segs.map(s => s.spans[0].getBoundingClientRect().left), R = segs.map(s => s.spans[s.spans.length - 1].getBoundingClientRect().right);
    p.style.whiteSpace = ''; p.style.textWrap = '';
    const n = segs.length, W = (i, j) => R[j] - L[i], tgt = (W(0, n - 1)) / N;
    if (N > n) return;
    const dp = [...Array(N + 1)].map(() => Array(n + 1).fill(Infinity)), bk = [...Array(N + 1)].map(() => Array(n + 1).fill(-1));
    dp[0][0] = 0;
    for (let k = 1; k <= N; k++) for (let j = k; j <= n; j++) for (let i = k - 1; i < j; i++) {
      if (dp[k - 1][i] === Infinity) continue; const w = W(i, j - 1); if (w > maxW) continue;
      const c = dp[k - 1][i] + (w - tgt) ** 2; if (c < dp[k][j]) { dp[k][j] = c; bk[k][j] = i; } }
    if (dp[N][n] === Infinity) return false;
    const cuts = []; for (let k = N, j = n; k > 0; k--) { const i = bk[k][j]; if (i > 0) cuts.push(i); j = i; }
    cuts.forEach(i => { const s = segs[i].sp; if (s && s.parentNode) { const br = document.createElement('br'); br.className = 'fb'; s.replaceWith(br); segs[i].sp = br; } });
    p.style.textWrap = 'wrap';
    return true;
  };
  const main = el => { const ps = [...el.querySelectorAll('p')].filter(p => /[a-z]/i.test(p.textContent)); return ps[ps.length - 1]; };
  const run = () => {
    document.querySelectorAll('.slide').forEach(sl => {
      const S = sl.getBoundingClientRect();
      const T = [...sl.querySelectorAll('.raw .rx-t')].filter(el => el.style.whiteSpace !== 'nowrap' && !el.dataset.nofit).map(el => {
        const p = main(el); if (!p || p.querySelector('br') || p.textContent.trim().length < 13) return null;
        const b = el.getBoundingClientRect();
        return {el, p, x: b.left - S.left, y: b.top - S.top, w: b.width, fs: getComputedStyle(p).fontSize, col: getComputedStyle(p.querySelector('span') || p).color, n: rows(p)};
      }).filter(Boolean);
      const used = new Set();
      T.forEach((a, i) => { if (used.has(i)) return;
        const g = T.filter((b, j) => !used.has(j) && Math.abs(b.w - a.w) <= 3 && b.fs === a.fs && b.col === a.col && (Math.abs(b.y - a.y) <= 4 || Math.abs(b.x - a.x) <= 4));
        g.forEach(b => used.add(T.indexOf(b)));
        const want = Math.max(...g.map(b => +b.el.dataset.lines || b.n));
        g.forEach(b => { const N = +b.el.dataset.lines || (g.length > 1 && b.n > 1 ? want : b.n); if (N >= 2 || b.n >= 2) fit(b.p, Math.max(N, 1)); });
      });
      // other multi-line paragraphs of these boxes: balanced at their natural count
      sl.querySelectorAll('.raw .rx-t p').forEach(p => { if (p._segs || p.querySelector('br') || !/[a-z]/i.test(p.textContent)) return;
        if (p.closest('.rx-t').style.whiteSpace === 'nowrap') return; const n = rows(p); if (n >= 2) fit(p, n); });
    });
    window.__rawfit = true;
  };
  window.__fitapi = {fit, rows, main, words};
  document.fonts.ready.then(run);
})();
