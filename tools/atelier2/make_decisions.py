"""python3 tools/atelier2/make_decisions.py decks/<slug> -> <deck>/decisions.js (lib + icons + chosen variants, per slide)."""
import json, pathlib, sys, importlib.util
H = pathlib.Path(__file__).parent
def load(n):
    s = importlib.util.spec_from_file_location(n, H / f'{n}.py'); m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
IT = {i['id']: i for i in load('items').ITEMS}; DEC = load('decisions')
out = ["window.__decided=false;", "window.ICONS=" + (H / 'icons.json').read_text() + ";", (H / 'lib.js').read_text(), "const __D=[];"]
E = []      # (slide n in the reference deck, css with 'S ' = this slide, js, decision id)
for iid, (v, extra, css, scope) in DEC.D.items():
    it = IT[iid]; V = it[v]; js = V.get('js') or ''
    if iid in DEC.SIZE: js = js.replace(*DEC.SIZE[iid])
    for n in (scope or it['scope']):
        if isinstance(n, int): E.append((n, (V.get('css') or '') + css, js + ';' + extra, str(iid)))
for mod, iid, key, sc in DEC.EXTRA:
    it = {i['id']: i for i in load(mod).ITEMS}[iid]
    for n in sc: E.append((n, '', it[key]['js'], f'{iid}{key}'))
for n in DEC.CARDS: E.append((n, '', 'A.cardPillAuto(sl)', 'cards'))
FX = load('fixes'); out.insert(4, (H / 'fixlib.js').read_text())   # visual-audit fixes (11 Nov): per-type JS, then the generic rules on every raw slide
for f in FX.FIXES:
    if f.get('js'):
        for n in f['slides']: E.append((n, '', f['js'], f"fix{f['id']}"))
# Slide numbers in decisions.py / fixes.py are those of the reference deck (decks/edtech-full on 12 Nov 2026, frozen in ref_slides.json).
# Each one becomes a selector that survives inserted slides and other decks (12 Nov):
#   a raw-derived template -> every slide built from it, in any deck ([data-tpl]);
#   a typed slide -> its type ([data-type]) when the decision covers every slide of that type in the reference deck, else its id (ed005…).
import re as _re, yaml as _yaml
REF = json.loads((H / 'ref_slides.json').read_text())          # n -> {"id", "title", "tpl" | "type"}
_ser = {}
for n, r in REF.items():
    if r['title'] and ('tpl' in r): _ser.setdefault(r['title'], []).append(int(n))
# series harmony (Pierre, 11 Nov): pages of one series (same title) get the same decisions (not the fix* ones)
_sib = {n: [m for m in g if m != n] for g in _ser.values() if len(g) > 1 for n in g}
have = {}
for n, *_r, did in E: have.setdefault(did, set()).add(n)
for n, css, js, did in list(E):
    if did.startswith('fix'): continue
    for m in _sib.get(n, []):
        if m not in have[did]: E.append((m, css, js, did)); have[did].add(m); print('series: decision', did, 'copied', n, '->', m)
bytype = {}
for n, r in REF.items():
    if 'type' in r: bytype.setdefault(r['type'], set()).add(int(n))
def sel(n, did):
    r = REF[str(n)]
    if 'tpl' in r: return f'.slide[data-tpl="{r["tpl"]}"]'
    if bytype[r['type']] <= have[did]: return f'.slide[data-type="{r["type"]}"]'
    return f'.slide[data-id="{r["id"]}"]'
seen = set()
for n, css, js, did in E:
    s_ = sel(n, did)
    if (s_, did) in seen: continue
    seen.add((s_, did)); out.append(f"__D.push([{json.dumps(s_)},{json.dumps(css.replace('S ', s_ + ' '))},{json.dumps(js)},{json.dumps(did)}]);")
out.append("""(function go(){ if(window.__rawfit!==true) return setTimeout(go,50);
  __D.forEach(([q,css,js,id])=>{ if(css){const st=document.createElement('style');st.textContent=css;document.head.appendChild(st);}
    document.querySelectorAll(q).forEach(sl=>{ try{ (new Function('sl','A','C',js))(sl,window.A,window.A.C); }catch(e){ console.error('decision',id,q,e); } }); });
  document.querySelectorAll('.slide').forEach(sl=>{ try{ window.F.all(sl); }catch(e){ console.error('fixall',sl.dataset.n,e); } });
  try{ window.F.deck(); }catch(e){ console.error('deck',e); }
  window.__decided=true; })();""")
d = pathlib.Path(sys.argv[1]); (d / 'decisions.js').write_text('\n'.join(out)); print('decisions', len(DEC.D))
