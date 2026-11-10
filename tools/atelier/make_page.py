"""Page HTML d'un atelier : python3 make_page.py <deck dir> <page dir> [bandeau d'en-tête HTML]
manifest.json = {sections: [...]} ; kind 'juge' (cas x variantes A/B/C, mon choix par cas) ou 'variantes' (un design, beaucoup de variantes, une par ligne)."""
import json, html, sys, pathlib
M = json.load(open(sys.argv[1] + '/manifest.json')); head = sys.argv[3] if len(sys.argv) > 3 else ''
E = html.escape; out = []; nav = []
LET = 'ABCDEFGHIJKL'
def yn(): return '<div class="yn"><button class="y">Oui</button><button class="n">Non</button></div>'
for sec in M['sections']:
    sid = sec['id']; kind = sec['kind']
    nav.append(f'<a href="#s-{sid}">{sid} · {E(sec["short"])}<span class="pr" data-at="{sid}"></span></a>')
    tag = 'Atelier du juge' if kind == 'juge' else 'Choix de design'
    out.append(f'<section class="at" id="s-{sid}"><h2><span class="al">{sid}</span><span class="kd {kind}">{tag}</span>{E(sec["title"])}</h2>')
    if kind == 'juge':
        legend = ''.join(f'<li><b class="lt">{L}</b>{E(n)}</li>' for L, n in sec['variants'].items())
        out.append(f'<div class="band"><p><b>Ce qui change entre A, B et C :</b> {E(sec["change"])}</p><ul class="leg">{legend}</ul><p>{E(sec["rule"])} Mon choix peut donc changer selon le cas : je l’explique à chaque fois.</p></div>')
        for c, case in enumerate(sec['cases'], 1):
            cls = 'tri' if sec.get('zoom') == 'region' else 'wide'
            out.append(f'<div class="case {cls}"><h3>Cas {c} · {E(case["name"])}</h3><p class="why"><b>Je prends {case["mine"]}.</b> {E(case["why"])}</p><div class="row">')
            for L, n in case['n'].items():
                mine = L == case['mine']
                out.append(f'<div class="v{" rec" if mine else ""}" data-s="{sid}" data-k="{sid}{c}{L}" data-label="{E(f"{sid} · cas {c} ({case["name"]}) · {L} = {sec["variants"][L]}")}">'
                           f'<div class="lab"><b class="lt">{L}</b><span>{E(sec["variants"][L])}</span>{"<em>mon choix</em>" if mine else ""}</div>'
                           + (f'<div class="pics"><img class="zoom" loading="lazy" src="img/s{n}z.jpg" alt="zoom"><img class="sl mini" loading="lazy" src="img/s{n}.jpg" alt=""></div>{yn()}</div>' if cls == 'tri' else f'<div class="pics"><img class="sl" loading="lazy" src="img/s{n}.jpg" alt=""><img class="zoom" loading="lazy" src="img/s{n}z.jpg" alt="zoom"></div>{yn()}</div>'))
            out.append('</div></div>')
    else:
        mineL = LET[[v['key'] for v in sec['variants']].index(sec['mine'])]
        out.append(f'<div class="band"><p>{E(sec["what"])}</p><p><b>Mon choix : {mineL} ({E(next(v["name"] for v in sec["variants"] if v["key"] == sec["mine"]))}).</b> {E(sec["why"])}</p></div>')
        for i, v in enumerate(sec['variants']):
            L = LET[i]; mine = v['key'] == sec['mine']
            pics = ''.join(f'<img class="sl" loading="lazy" src="img/s{n}.jpg" alt="">' for n in v['n'])
            if sec.get('zoom') == 'rail': pics += ''.join(f'<img class="zoom" loading="lazy" src="img/s{n}z.jpg" alt="zoom">' for n in v['n'])
            if sec.get('zoom') == 'button': pics += '<div class="zrow">' + ''.join(f'<img class="zoom" loading="lazy" src="img/s{n}z.jpg" alt="zoom">' for n in v['n']) + '</div>'
            cols = 'c1' if len(v['n']) == 1 and not sec.get('zoom') else 'c2'
            out.append(f'<div class="case var{" rec" if mine else ""} v" data-s="{sid}" data-k="{sid}{L}" data-label="{E(f"{sid} · {L} = {v["name"]} ({v["desc"]})")}">'
                       f'<div class="vh"><b class="lt">{L}</b><div><div class="vn">{E(v["name"])}{" <em>mon choix</em>" if mine else ""}</div><div class="vd">{E(v["desc"])}</div></div>{yn()}</div>'
                       f'<div class="pics {cols}">{pics}</div></div>')
    out.append('</section>')
tpl = (pathlib.Path(__file__).parent / 'page_tpl.html').read_text()
page = tpl.replace('<!--NAV-->', ''.join(nav)).replace('<!--HEAD-->', head).replace('<!--BODY-->', '\n'.join(out))
open(sys.argv[2] + '/index.html', 'w').write(page); print(len(page))
