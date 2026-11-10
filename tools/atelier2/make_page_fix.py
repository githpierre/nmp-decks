"""Page avant / après de l'audit visuel : python3 tools/atelier2/make_page_fix.py <dir with img/ + fixed.json>"""
import json, html, sys, pathlib, importlib.util
H = pathlib.Path(__file__).parent; D = pathlib.Path(sys.argv[1]); E = html.escape
s = importlib.util.spec_from_file_location('fixes', H / 'fixes.py'); M = importlib.util.module_from_spec(s); s.loader.exec_module(M)
FX = json.loads((D / 'fixed.json').read_text())
HOW = {'convertisseur': 'règle du convertisseur : tous les decks', 'règle générale': 'règle générale : toutes les slides converties, tous les decks',
       'type': 'tout ce type de slide', 'slide': 'cette slide', 'overrides': 'réécriture de cette slide'}
RULE = {'snapLines': 'traits prolongés jusqu’à leur cible', 'trimBus': 'lignes d’arbre recoupées', 'centerText': 'texte centré dans sa carte',
        'headers': 'en-têtes rendus lisibles', 'grid': 'cartes réalignées au pixel', 'gauges': 'mini-jauges', 'pillText': 'pastille + texte centrés', 'rail': 'rail des frises datées', 'arrowheads': 'pointes de flèches'}
body = []
for f in M.FIXES:
    i = f['id']; sl = ', '.join(map(str, f['slides']))
    body.append(f'''<section class="it" data-k="{i}" data-label="{E(f"{i} · {f['title']}")}"><div class="hd"><span class="num">{i}</span><h3>{E(f["title"])}</h3>
<span class="sc">{E(HOW[f["how"]])} · slide{"s" if len(f["slides"]) > 1 else ""} {E(sl)}</span></div>
<div class="band">{E(f["why"])}</div>
<div class="grid"><figure><figcaption>Avant</figcaption><img class="sl" loading="lazy" src="img/f{i:02d}_before.jpg" alt=""></figure>
<figure class="aft"><figcaption>Après</figcaption><img class="sl" loading="lazy" src="img/f{i:02d}_after.jpg" alt=""></figure></div>
<div class="yn"><button class="y">Oui</button><button class="n">Non</button></div></section>''')
rules = ''.join(f'<li><b>{E(RULE.get(k, k))}</b> : slides {", ".join(map(str, v))}</li>' for k, v in FX.items())
page = f'''<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>EdTech · audit visuel : 25 corrections</title><style>
:root{{--navy:#062A3C;--green:#1fa463;--yellow:#FFE45C}}*{{box-sizing:border-box}}
body{{margin:0;font:15px/1.5 -apple-system,Segoe UI,Roboto,sans-serif;background:#eef1f3;color:#14212b;padding-bottom:70px}}
header{{background:var(--navy);color:#fff;padding:22px 24px}}header h1{{margin:0 0 6px;font-size:22px}}header p{{margin:4px 0;opacity:.92;max-width:1050px}}
header ul{{margin:6px 0;padding-left:20px;font-size:13.5px;opacity:.9}}
main{{max-width:1500px;margin:0 auto;padding:0 20px}}
.it{{background:#fff;border-radius:10px;padding:14px 16px 16px;margin:14px 0;box-shadow:0 1px 3px #0001}}
.it.ok{{box-shadow:0 0 0 3px var(--green)}}.it.ko{{opacity:.55}}
.hd{{display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin-bottom:8px}}.hd h3{{margin:0;font-size:17px}}
.num{{background:var(--navy);color:#fff;border-radius:4px;padding:1px 9px;font-weight:700}}.sc{{font-size:13px;color:#6b7a85}}
.band{{background:var(--yellow);border-radius:8px;padding:8px 14px;margin-bottom:12px;font-size:14.5px}}
.grid{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px}}figure{{margin:0;background:#e9edf0;border-radius:8px;padding:8px}}figure.aft{{background:#eefaf3;outline:3px solid var(--green)}}
figcaption{{font-weight:700;font-size:14px;margin-bottom:6px}}.sl{{width:100%;border-radius:4px;display:block;cursor:zoom-in;background:#0b2233}}
.yn{{display:flex;gap:8px;margin-top:10px;max-width:420px}}.yn button{{flex:1;border:1.5px solid #b8c2c9;background:#fff;border-radius:6px;padding:8px 0;font-weight:700;font-size:14px;cursor:pointer}}
.yn .y.on{{background:var(--green);border-color:var(--green);color:#fff}}.yn .n.on{{background:#d7263d;border-color:#d7263d;color:#fff}}
#bar{{position:fixed;left:0;right:0;bottom:0;background:var(--navy);color:#fff;display:flex;gap:12px;align-items:center;padding:10px 18px;font-size:14px;z-index:6}}
#bar button{{background:var(--yellow);border:0;border-radius:6px;padding:8px 14px;font-weight:700;cursor:pointer}}
#lb{{display:none;position:fixed;inset:0;background:#000d;z-index:9;align-items:center;justify-content:center;cursor:zoom-out}}#lb img{{max-width:96vw;max-height:94vh}}
#out{{display:none;position:fixed;inset:8% 8%;background:#fff;z-index:8;border-radius:10px;padding:16px;flex-direction:column;gap:10px;box-shadow:0 10px 40px #0006}}#out textarea{{flex:1;font:13px/1.4 monospace}}
@media(max-width:760px){{.grid{{grid-template-columns:1fr}}main{{padding:0 8px}}}}
</style></head><body>
<header><h1>Deck EdTech · audit visuel : 25 corrections, avant / après</h1>
<p>J'ai passé les 221 slides au détecteur (texte qui déborde ou chevauche, traits qui n'arrivent sur rien, éléments décalés de 1 à 6 px), puis regardé chaque slide signalée. Voici les 25 défauts évidents corrigés. Quand c'est une règle, elle s'applique à toutes les slides du même type et aux autres decks (indiqué sous chaque titre).</p>
<p>Ce que les règles générales ont touché dans le deck :</p><ul>{rules}</ul>
<p>Oui = je garde, Non = je reviens en arrière. Clique une image pour l'agrandir.</p></header>
<main>{"".join(body)}</main>
<div id="bar"><span id="cnt"></span><button id="copy">Copier mes réponses</button></div>
<div id="lb"><img alt=""></div><div id="out"><b>Tes réponses</b><textarea id="txt" readonly></textarea><button id="cl">Fermer</button></div>
<script>
const K='nmp-audit25';let S={{}};try{{S=JSON.parse(localStorage.getItem(K)||'{{}}')}}catch(e){{}}
const V=[...document.querySelectorAll('.it[data-k]')];
function paint(){{let n=0;V.forEach(v=>{{const a=S[v.dataset.k];v.classList.toggle('ok',a==='y');v.classList.toggle('ko',a==='n');v.querySelector('.y').classList.toggle('on',a==='y');v.querySelector('.n').classList.toggle('on',a==='n');if(a)n++}});
document.getElementById('cnt').textContent=n+' / '+V.length+' corrections jugées';try{{localStorage.setItem(K,JSON.stringify(S))}}catch(e){{}}}}
V.forEach(v=>{{v.querySelector('.y').onclick=()=>{{S[v.dataset.k]=S[v.dataset.k]==='y'?undefined:'y';paint()}};v.querySelector('.n').onclick=()=>{{S[v.dataset.k]=S[v.dataset.k]==='n'?undefined:'n';paint()}}}});paint();
document.querySelectorAll('.sl').forEach(i=>i.onclick=()=>{{const l=document.getElementById('lb');l.querySelector('img').src=i.src;l.style.display='flex'}});
document.getElementById('lb').onclick=e=>e.currentTarget.style.display='none';
document.getElementById('copy').onclick=async()=>{{const L=['Audit visuel : réponses'];V.forEach(v=>{{if(S[v.dataset.k])L.push((S[v.dataset.k]==='y'?'OUI ':'NON ')+v.dataset.label)}});const x=L.join('\\n');document.getElementById('txt').value=x;try{{await navigator.clipboard.writeText(x)}}catch(e){{}}document.getElementById('out').style.display='flex'}};
document.getElementById('cl').onclick=()=>document.getElementById('out').style.display='none';
</script></body></html>'''
(D / 'index.html').write_text(page); print(len(page))
