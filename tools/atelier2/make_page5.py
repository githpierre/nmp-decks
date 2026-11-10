"""Page HTML de l'atelier « 100 améliorations » : python3 tools/atelier2/make_page.py <dir with img/ + items.json>
Une section par point : l'actuel en grand, puis A/B/C ; Oui/Non par variante ; mon choix encadré en vert ; bandeau jaune."""
import json, html, sys, pathlib
D = pathlib.Path(sys.argv[1]); IT = json.load(open(D / 'items.json')); E = html.escape
fams = []
for it in IT:
    if it['fam'] not in fams: fams.append(it['fam'])
body = []
for f in fams:
    items = [i for i in IT if i['fam'] == f]
    body.append(f'<h2 class="fam" id="f-{E(f)}">{E(f)} <span>{len(items)} points</span></h2>')
    for it in items:
        sc = it['scope']
        scope = 'toutes les slides' if sc and sc[0] == 'toutes les slides' else ('slide ' + str(sc[0]) if len(sc) == 1 else f'{len(sc)} slides : ' + ', '.join(map(str, sc)))
        vs = []
        for L in it.get('keys', list('ABC')):
            v = it[L]; mine = L == it['mine']
            vs.append(f'<div class="v{" rec" if mine else ""}" data-k="{it["id"]}{L}" data-label="{E(f"{it["id"]} · {it["title"]} · {L} = {v["name"]}")}">'
                      f'<div class="lab"><b class="lt">{L}</b><span>{E(v["name"])}</span>{"<em>mon choix</em>" if mine else ""}</div>'
                      f'<img class="sl" loading="lazy" src="img/{it["id"]}{L}.jpg" alt=""><p class="vd">{E(v["desc"])}</p>'
                      f'<div class="yn"><button class="y">Oui</button><button class="n">Non</button></div></div>')
        body.append(f'''<section class="it" id="i{it["id"]}"><div class="hd"><span class="num">{it["id"]}</span><h3>{E(it["title"])}</h3><span class="sc">s'applique à {E(scope)}</span></div>
<div class="band"><p><b>Ce qui ne va pas :</b> {E(it["what"])}</p><p><b>Mon choix : {it["mine"]} ({E(it[it["mine"]]["name"])}).</b> {E(it["why"])}</p></div>
<div class="grid"><div class="v cur"><div class="lab"><b class="lt now">0</b><span>Actuel</span></div><img class="sl" loading="lazy" src="img/{it["id"]}0.jpg" alt=""></div>{"".join(vs)}</div></section>''')
nav = ''.join(f'<a href="#f-{E(f)}">{E(f)}</a>' for f in fams)
page = f'''<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>EdTech · 100 améliorations visuelles</title><style>
:root{{--navy:#062A3C;--green:#1fa463;--yellow:#FFE45C}}*{{box-sizing:border-box}}
body{{margin:0;font:15px/1.5 -apple-system,Segoe UI,Roboto,sans-serif;background:#eef1f3;color:#14212b;padding-bottom:70px}}
header{{background:var(--navy);color:#fff;padding:22px 24px}}header h1{{margin:0 0 6px;font-size:22px}}header p{{margin:3px 0;opacity:.92;max-width:1000px}}
nav{{position:sticky;top:0;z-index:5;background:#fff;border-bottom:1px solid #d5dbe0;padding:9px 24px;display:flex;gap:18px;flex-wrap:wrap}}
nav a{{color:var(--navy);text-decoration:none;font-weight:600;font-size:14px}}
main{{max-width:1500px;margin:0 auto;padding:0 20px}}
h2.fam{{font-size:22px;margin:30px 0 6px;scroll-margin-top:50px}}h2.fam span{{font-size:14px;color:#6b7a85;font-weight:500}}
.it{{background:#fff;border-radius:10px;padding:14px 16px 16px;margin:14px 0;box-shadow:0 1px 3px #0001;scroll-margin-top:50px}}
.hd{{display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin-bottom:8px}}.hd h3{{margin:0;font-size:17px}}
.num{{background:var(--navy);color:#fff;border-radius:4px;padding:1px 9px;font-weight:700}}.sc{{font-size:13px;color:#6b7a85}}
.band{{background:var(--yellow);border-radius:8px;padding:9px 14px;margin-bottom:12px}}.band p{{margin:3px 0;font-size:14.5px}}
.grid{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px}}.lt{{width:auto!important;min-width:26px;padding:0 6px;border-radius:13px!important}}
.v{{border:3px solid transparent;border-radius:8px;padding:8px;background:#f6f8f9;display:flex;flex-direction:column;gap:7px}}
.v.rec{{border-color:var(--green);background:#eefaf3}}.v.cur{{background:#e9edf0}}
.v.ok{{box-shadow:0 0 0 2px var(--green) inset}}.v.ko{{opacity:.55}}
.lab{{display:flex;align-items:center;gap:8px;font-size:14px;font-weight:700}}.lab span{{flex:1}}
.lt{{display:inline-flex;align-items:center;justify-content:center;width:26px;height:26px;border-radius:50%;background:var(--navy);color:#fff;font-size:14px;flex:none}}.lt.now{{background:#8a99a3}}
em{{font-style:normal;background:var(--green);color:#fff;font-size:11.5px;font-weight:700;border-radius:3px;padding:1px 7px;white-space:nowrap}}
.sl{{width:100%;border-radius:4px;display:block;cursor:zoom-in;background:#0b2233}}.vd{{margin:0;font-size:13.5px;color:#3d4c56;flex:1}}
.yn{{display:flex;gap:8px}}.yn button{{flex:1;border:1.5px solid #b8c2c9;background:#fff;border-radius:6px;padding:8px 0;font-weight:700;font-size:14px;cursor:pointer}}
.yn .y.on{{background:var(--green);border-color:var(--green);color:#fff}}.yn .n.on{{background:#d7263d;border-color:#d7263d;color:#fff}}
#bar{{position:fixed;left:0;right:0;bottom:0;background:var(--navy);color:#fff;display:flex;gap:12px;align-items:center;padding:10px 18px;font-size:14px;z-index:6}}
#bar button{{background:var(--yellow);border:0;border-radius:6px;padding:8px 14px;font-weight:700;cursor:pointer}}
#lb{{display:none;position:fixed;inset:0;background:#000d;z-index:9;align-items:center;justify-content:center;cursor:zoom-out}}#lb img{{max-width:96vw;max-height:94vh}}
#out{{display:none;position:fixed;inset:8% 8%;background:#fff;z-index:8;border-radius:10px;padding:16px;flex-direction:column;gap:10px;box-shadow:0 10px 40px #0006}}#out textarea{{flex:1;font:13px/1.4 monospace}}
@media(max-width:760px){{.grid{{grid-template-columns:1fr}}main{{padding:0 8px}}nav{{flex-wrap:nowrap;overflow-x:auto;white-space:nowrap}}}}
</style></head><body>
<header><h1>Deck EdTech · prix : 30 mises en page</h1>
<p>Seulement les points que tu m'as demandé de remontrer, avec de vrais designs différents. Le rendu « actuel » (0) inclut déjà tes choix du 1er tour (ex. 4 lignes sur la slide 22). Chaque variante est faite sur la vraie slide, en vrai CSS. Quand un format se répète, la variante s'applique à toutes les slides qui le partagent (indiqué sous le titre).</p>
<p>Clique Oui ou Non sur chaque variante (plusieurs Oui possibles). Mon choix est encadré en vert. Clique une image pour l'agrandir. Tes réponses restent dans ce navigateur ; « Copier mes réponses » en bas si tu veux me les coller.</p></header>
<nav>{nav}</nav><main>{"".join(body)}</main>
<div id="bar"><span id="cnt"></span><button id="copy">Copier mes réponses</button></div>
<div id="lb"><img alt=""></div><div id="out"><b>Tes réponses</b><textarea id="txt" readonly></textarea><button id="cl">Fermer</button></div>
<script>
const K='nmp-atelier100e';let S={{}};try{{S=JSON.parse(localStorage.getItem(K)||'{{}}')}}catch(e){{}}
const V=[...document.querySelectorAll('.v[data-k]')];
function paint(){{let n=0;V.forEach(v=>{{const a=S[v.dataset.k];v.classList.toggle('ok',a==='y');v.classList.toggle('ko',a==='n');v.querySelector('.y').classList.toggle('on',a==='y');v.querySelector('.n').classList.toggle('on',a==='n');if(a)n++}});
document.getElementById('cnt').textContent=n+' / '+V.length+' variantes jugées';try{{localStorage.setItem(K,JSON.stringify(S))}}catch(e){{}}}}
V.forEach(v=>{{v.querySelector('.y').onclick=()=>{{S[v.dataset.k]=S[v.dataset.k]==='y'?undefined:'y';paint()}};v.querySelector('.n').onclick=()=>{{S[v.dataset.k]=S[v.dataset.k]==='n'?undefined:'n';paint()}}}});paint();
document.querySelectorAll('.sl').forEach(i=>i.onclick=()=>{{const l=document.getElementById('lb');l.querySelector('img').src=i.src;l.style.display='flex'}});
document.getElementById('lb').onclick=e=>e.currentTarget.style.display='none';
document.getElementById('copy').onclick=async()=>{{const L=['Atelier 100, 2e tour : réponses'];V.forEach(v=>{{if(S[v.dataset.k])L.push((S[v.dataset.k]==='y'?'OUI ':'NON ')+v.dataset.label)}});const x=L.join('\\n');document.getElementById('txt').value=x;try{{await navigator.clipboard.writeText(x)}}catch(e){{}}document.getElementById('out').style.display='flex'}};
document.getElementById('cl').onclick=()=>document.getElementById('out').style.display='none';
</script></body></html>'''
(D / 'index.html').write_text(page); print(len(page), len(IT))
