"""Page HTML d'un atelier du juge : python3 make_page.py <deck dir> <page dir> [ligne d'en-tête en HTML]
Lit manifest.json ({ateliers, items}) ; les images doivent être dans <page dir>/img (shoot.py)."""
import json, html, sys, pathlib
M = json.load(open(sys.argv[1] + '/manifest.json')); head = sys.argv[3] if len(sys.argv) > 3 else ''
E = html.escape; out = []; nav = []
for a in M['ateliers']:
    at = a['id']; nav.append(f'<a href="#atelier-{at}">{at} · {E(a.get("short") or a["title"].split(":")[0])}<span class="pr" data-at="{at}"></span></a>')
    legend = ''.join(f'<li class="{"mine" if L == a["mine"] else ""}"><b class="lt">{L}</b>{E(n)}{" <em>mon choix</em>" if L == a["mine"] else ""}</li>' for L, n in a['variants'].items())
    out.append(f'<section class="at" id="atelier-{at}"><h2><span class="al">Atelier {at}</span>{E(a["title"])}</h2>'
               f'<div class="band"><p><b>Une seule chose change entre A, B et C :</b> {E(a["change"])}</p><ul class="leg">{legend}</ul>'
               f'<p><b>Mon choix : {a["mine"]}.</b> {E(a["why"])}</p>' + (f'<p class="small">{E(a["note"])}</p>' if a.get('note') else '') + '</div>')
    for c, cname in enumerate(a['cases'], 1):
        out.append(f'<div class="case{" wide" if at == "B" else ""}"><h3>Cas {c} · {E(cname)}</h3><div class="row">')
        for L, vname in a['variants'].items():
            k = f'{at}{c}{L}'; mine = L == a['mine']
            z = f'<img class="zoom" loading="lazy" src="img/{k}z.jpg" alt="zoom">' if a.get('zoom') else ''
            out.append(f'<div class="v{" rec" if mine else ""}" data-k="{k}" data-label="{E(f"{at} · cas {c} ({cname}) · {L} = {vname}")}">'
                       f'<div class="lab"><b class="lt">{L}</b><span>{E(vname)}</span>{"<em>mon choix</em>" if mine else ""}</div>'
                       f'<div class="pics"><img class="sl" loading="lazy" src="img/{k}.jpg" alt="">{z}</div>'
                       f'<div class="yn"><button class="y">Oui</button><button class="n">Non</button></div></div>')
        out.append('</div></div>')
    out.append('</section>')
tpl = (pathlib.Path(__file__).parent / 'page_tpl.html').read_text()
page = tpl.replace('<!--NAV-->', ''.join(nav)).replace('<!--HEAD-->', head).replace('<!--BODY-->', '\n'.join(out))
open(sys.argv[2] + '/index.html', 'w').write(page); print(len(page))
