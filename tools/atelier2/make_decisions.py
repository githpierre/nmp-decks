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
for n in DEC.CARDS: out.append(f"__D.push([{n},'','A.cardPillAuto(sl)','cards']);")
out.append("""(function go(){ if(window.__rawfit!==true) return setTimeout(go,50);
  __D.forEach(([n,css,js,id])=>{ const sl=document.querySelector(`.slide[data-n="${n}"]`); if(!sl) return;
    if(css){const st=document.createElement('style');st.textContent=css;document.head.appendChild(st);}
    try{ (new Function('sl','A','C',js))(sl,window.A,window.A.C); }catch(e){ console.error('decision',id,n,e); } });
  window.__decided=true; })();""")
d = pathlib.Path(sys.argv[1]); (d / 'decisions.js').write_text('\n'.join(out)); print('decisions', len(DEC.D))
