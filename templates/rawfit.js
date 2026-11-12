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
        t.textContent.replace(/(\$?£?€?[\d.,]+\+?) (billion|million|trillion|thousand|percent|hours?|years?|days?|weeks?|months?|minutes?)\b/gi, '$1\u00a0$2').split(/( +)/).forEach(s => { if (!s) return; if (/^ +$/.test(s)) f.appendChild(document.createTextNode(s));
          else { const w = document.createElement('span'); w.className = 'fw'; w.textContent = s; f.appendChild(w); } });
        t.replaceWith(f); });
      const segs = []; let cur = null, sp = null;
      const walk = n => n.childNodes.forEach(c => {
        if (c.nodeType === 3) { if (/^ +$/.test(c.textContent)) { sp = c; cur = null; } }
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
  const unfit = p => { (p._segs || []).forEach(g => { if (g.sp && g.sp.nodeName === 'BR' && g.sp.parentNode) { const t = document.createTextNode(' '); g.sp.replaceWith(t); g.sp = t; } }); p.style.textWrap = ''; };
  // one slide. Called once at load, then again at the end of the design fixes (fixlib.all), because they move and resize boxes:
  // the line counts must be equal on the FINAL geometry (12 Nov 2026, slide 116: 3 and 4 lines in one grid)
  const slideFit = sl => {
    {
      sl.querySelectorAll('.raw .rx-t p').forEach(p => { if (p._segs) unfit(p); });
      const S = sl.getBoundingClientRect();
      const T = [...sl.querySelectorAll('.raw .rx-t')].filter(el => el.style.whiteSpace !== 'nowrap' && !el.dataset.nofit).map(el => {
        const p = main(el); if (!p || p.querySelector('br:not(.fb)') || p.textContent.trim().length < 13) return null;
        const b = el.getBoundingClientRect();
        return {el, p, x: b.left - S.left, y: b.top - S.top, w: b.width, fs: getComputedStyle(p).fontSize, col: getComputedStyle(p.querySelector('span') || p).color, n: rows(p)};
      }).filter(Boolean);
      const used = new Set();
      T.forEach((a, i) => { if (used.has(i)) return;
        // a grid of boxes is ONE group: every box that shares a row or a column with a member joins it (12 Nov 2026: slide 116 had 3 and 4 lines
        // in the same grid because a group was only the row + the column of its first box)
        const g = [a]; used.add(i);
        for (let q = 0; q < g.length; q++) T.forEach((b, j) => { if (used.has(j)) return; const c = g[q];
          if (Math.abs(b.w - c.w) <= 3 && b.fs === c.fs && b.col === c.col && (Math.abs(b.y - c.y) <= 4 || Math.abs(b.x - c.x) <= 4)) { used.add(j); g.push(b); } });
        const want = Math.max(...g.map(b => +b.el.dataset.lines || b.n));
        g.forEach(b => { const N = +b.el.dataset.lines || (g.length > 1 && (b.n > 1 || b.p.textContent.trim().length >= 40) ? want : b.n);   // a real sentence follows its group (slide 161), a short label stays on one line if (!(N >= 2 || b.n >= 2)) return;
          let ok = fit(b.p, Math.max(N, 1));
          // a fixed line count (data-lines) wins over the font size: the text shrinks a little (down to 85%) until it fits (Pierre, 12 Nov 2026)
          if (ok === false && b.el.dataset.lines) { const f0 = parseFloat(getComputedStyle(b.p).fontSize);
            for (let k = 0.97; k >= 0.85 && ok === false; k -= 0.03) { b.p.style.fontSize = f0 * k + 'px'; b.p.querySelectorAll('span').forEach(x => x.style.fontSize = f0 * k + 'px'); ok = fit(b.p, N); } } });
      });
      // other multi-line paragraphs of these boxes: balanced at their natural count
      const done = new Set(T.map(t => t.p)); sl.querySelectorAll('.raw .rx-t p').forEach(p => { if (done.has(p) || p.querySelector('br') || !/[a-z]/i.test(p.textContent)) return;
        if (p.closest('.rx-t').style.whiteSpace === 'nowrap') return; const n = rows(p); if (n >= 2) fit(p, n); });
      // labels of one grid (short upper-case headers): all on one line or all on two lines, never mixed (Pierre, 12 Nov 2026)
      // a label = the only paragraph of a box, or the first paragraph of a card (TITLE + text) ; mostly upper-case ("GENERIC LNPs" counts)
      const LB = [...sl.querySelectorAll('.raw .rx-t')].map(el => { const ps = [...el.querySelectorAll('p')].filter(p => /[a-z]/i.test(p.textContent));
        if (!ps.length) return null; const p = ps[0]; let t = p.innerText.replace(/\s+/g, ' ').trim(); if (p.querySelector('br:not(.fb)')) return null;
        let fixed = 0;   // a label written on two paragraphs (hard break) is a member of the group with its 2 lines, it is not re-broken
        if (ps.length > 1 && ps.map(x => x.textContent.trim()).join(' ').length <= 34) { t = ps.map(x => x.textContent.trim()).join(' '); fixed = ps.reduce((a, x) => a + rows(x), 0); }
        else if (ps.length > 1 && ps.slice(1).map(x => x.textContent).join(' ').length < 40) return null;
        const up = (t.match(/[A-Z]/g) || []).length, lo = (t.match(/[a-z]/g) || []).length;
        if (t.length > 32 || up < 3 * lo || t.split(/\s+/).length > 4) return null;
        const b = el.getBoundingClientRect(); return {el, p, t, fixed, w: b.width, fs: getComputedStyle(p).fontSize, col: getComputedStyle(p.querySelector('span') || p).color, n: fixed || rows(p)}; }).filter(Boolean);
      const lu = new Set();
      LB.forEach((a, i) => { if (lu.has(i)) return;
        const g = LB.filter((b, j) => !lu.has(j) && Math.abs(b.w - a.w) <= 3 && b.fs === a.fs && b.col === a.col); g.forEach(b => lu.add(LB.indexOf(b)));
        if (g.length < 3 || g.some(b => !b.n) || new Set(g.map(b => b.n)).size < 2) return;
        if (g.every(b => b.t.split(/\s+/).length >= 2)) { g.forEach(b => { if (b.n < 2 && !b.fixed) fit(b.p, 2); }); return; }
        if (g.some(b => b.fixed)) return;
        g.forEach(b => b.p.querySelectorAll('br.fb').forEach(br => br.replaceWith(document.createTextNode(' '))));   // one word cannot break: the whole group goes on one line
        for (let k = 1; k >= 0.8 && g.some(b => rows(b.p) > 1); k -= 0.03) g.forEach(b => { b.p.style.fontSize = (parseFloat(b.fs) * k) + 'px'; b.p.querySelectorAll('span').forEach(x => x.style.fontSize = (parseFloat(b.fs) * k) + 'px'); });
      });
    }
  };
  const run = () => { document.querySelectorAll('.slide').forEach(slideFit); window.__rawfit = true; };
  window.__fitapi = {fit, rows, main, words, slideFit};
  document.fonts.ready.then(run);
})();
