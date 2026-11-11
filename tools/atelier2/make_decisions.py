"""python3 tools/atelier2/make_decisions.py decks/<slug> -> <deck>/decisions.js (lib + icons + chosen variants, per slide)."""
import json, pathlib, sys, importlib.util
H = pathlib.Path(__file__).parent
def load(n):
    s = importlib.util.spec_from_file_location(n, H / f'{n}.py'); m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
IT = {i['id']: i for i in load('items').ITEMS}; DEC = load('decisions')
out = ["window.__decided=false;", "window.ICONS=" + (H / 'icons.json').read_text() + ";", (H / 'lib.js').read_text(), "const __D=[];"]
for iid, (v, extra, css, scope) in DEC.D.items():
    it = IT[iid]; V = it[v]; js = V.get('js') or ''
    if iid in DEC.SIZE: js = js.replace(*DEC.SIZE[iid])
    for n in (scope or it['scope']):
        if not isinstance(n, int): continue
        c = ((V.get('css') or '') + css).replace('S ', f'.slide[data-n="{n}"] ')
        out.append(f"__D.push([{n},{json.dumps(c)},{json.dumps(js + ';' + extra)},{iid}]);")
for mod, iid, key, sc in DEC.EXTRA:
    it = {i['id']: i for i in load(mod).ITEMS}[iid]
    for n in sc: out.append(f"__D.push([{n},'',{json.dumps(it[key]['js'])},'{iid}{key}']);")
for n in DEC.CARDS: out.append(f"__D.push([{n},'','A.cardPillAuto(sl)','cards']);")
FX = load('fixes'); out.insert(4, (H / 'fixlib.js').read_text())   # visual-audit fixes (11 Nov): per-type JS, then the generic rules on every raw slide
for f in FX.FIXES:
    if f.get('js'):
        for n in f['slides']: out.append(f"__D.push([{n},'',{json.dumps(f['js'])},'fix{f['id']}']);")
# series harmony (Pierre, 11 Nov): slides of one series (same title: 1/2, 2/2…) always get the same decisions.
# Any decision on one page of a series is copied to the pages that lack it (that is how 208 had kept its emojis while 207 had icons).
import re as _re, yaml as _yaml
_Y = _yaml.safe_load((pathlib.Path(sys.argv[1]) / 'deck.yaml').read_text()); _ser = {}
for _i, _s in enumerate(_Y['slides'], 1):
    _t = _re.sub(r'\s+', ' ', str(_s.get('title') or '')).strip()
    if _t and _s.get('type') == 'raw': _ser.setdefault(_t, []).append(_i)
_sib = {n: [m for m in g if m != n] for g in _ser.values() if len(g) > 1 for n in g}
_have = {}
for _l in out:
    _m = _re.match(r"__D\.push\(\[(\d+),.*,'?([^,']+)'?\]\);$", _l, _re.S)
    if _m: _have.setdefault(_m.group(2), set()).add(int(_m.group(1)))
_add = []
for _l in out:
    _m = _re.match(r"__D\.push\(\[(\d+),.*,'?([^,']+)'?\]\);$", _l, _re.S)
    if not _m or _m.group(2).startswith('fix'): continue
    n, did = int(_m.group(1)), _m.group(2)
    for m in _sib.get(n, []):
        if m not in _have[did]:
            _add.append(_l.replace(f'[{n},', f'[{m},', 1).replace(f'data-n=\\"{n}\\"', f'data-n=\\"{m}\\"')); _have[did].add(m); print('series: decision', did, 'copied', n, '->', m)
out += _add
out.append("""(function go(){ if(window.__rawfit!==true) return setTimeout(go,50);
  __D.forEach(([n,css,js,id])=>{ const sl=document.querySelector(`.slide[data-n="${n}"]`); if(!sl) return;
    if(css){const st=document.createElement('style');st.textContent=css;document.head.appendChild(st);}
    try{ (new Function('sl','A','C',js))(sl,window.A,window.A.C); }catch(e){ console.error('decision',id,n,e); } });
  document.querySelectorAll('.slide').forEach(sl=>{ try{ window.F.all(sl); }catch(e){ console.error('fixall',sl.dataset.n,e); } });
  window.__decided=true; })();""")
d = pathlib.Path(sys.argv[1]); (d / 'decisions.js').write_text('\n'.join(out)); print('decisions', len(DEC.D))
