import json, html, sys, pathlib
man = json.load(open(sys.argv[1] + '/manifest.json'))
AT = {
 'A': ('Couverture : où mettre le petit texte légal du bas',
       "Même gabarit, 6 photos différentes. Ce qui change entre les 3 variantes : seulement la place et la largeur du disclaimer. "
       "Nouveau dans les 3 : la taille du titre se règle seule d’après la photo (il rapetisse s’il allait toucher l’objet, et « NEW MARKET PITCH » suit).",
       "Mon choix : <b>en bas, aligné sur le bouton, largeur auto</b> (encadré vert). C’est ton A3 validé : il reste toujours sur la partie sombre. "
       "Le bloc large finit sur la photo dès que l’objet descend bas (fusion, bracelets). Sous le titre, ça charge le bloc titre et casse le vide qui met la photo en valeur.",
       'cases', ['EdTech', 'Nuclear fusion', 'Biotechnology', 'Wearable technology', 'AI voice agents', 'Longevity']),
 'B': ('Notes de bas de page : 2 lignes, 3 lignes ou paragraphe',
       "6 notes réelles, chacune sur sa vraie slide. Sous chaque slide, un zoom ×2 de la note pour juger la forme.",
       "Mon choix : <b>2 lignes de même longueur, sans point</b> pour les 4 premières. Pour Priorités, <b>3 lignes</b> car il y a 3 idées. "
       "Pour la carte, <b>2 lignes</b> plutôt qu’une longue phrase coupée au hasard.",
       'cases', ['Maturité', 'Ce qui a changé', 'Estimations', 'Comparaison', 'Priorités', 'Carte']),
 'C': ('Liste datée : les ronds sur la barre rose',
       "La même slide « What has changed (very) recently? » avec 4, 5 ou 6 dates. À gauche, toujours le style actuel (C1). Les 2 autres changent à chaque cas, pour montrer les 6 autres styles deux fois. Zoom ×2 sous chaque slide.",
       "Mon choix : <b>C1, ronds creux roses</b> (style actuel). C’est le plus discret, les dates restent l’info principale. Les ronds pleins (C2) et les cibles (C6) attirent l’œil sur la barre au lieu du texte.",
       'cases', ['Page 1, 6 dates', 'Page 2, 6 dates', 'Page 1, 4 dates', 'Page 2, 4 dates', 'Page 1, 5 dates', 'Page 2, 5 dates']),
 'D': ('« What is the X market, in simple terms? »',
       "6 marchés, 3 designs. Les définitions des 5 nouveaux marchés sont écrites pour l’atelier (à refaire avec la recherche dans un vrai deck).",
       "Mon choix : <b>D4, la phrase puis 3 cartes WHAT / WHO PAYS / WHAT FOR</b>. Le lecteur comprend le marché en 3 secondes, même sans lire la phrase. "
       "D1 (l’ancien cadre) ne met rien en valeur. D3 est élégant mais reste une seule phrase.",
       'cases', ['EdTech', 'Nuclear fusion', 'Biotechnology', 'Wearable tech', 'AI voice agents', 'Longevity']),
 'E': ('Carte du monde : la forme des lignes pointillées',
       "6 cartes avec des parts et des textes différents (les 5 nouvelles sont fictives : seule la forme des lignes compte). Clique sur une slide pour l’agrandir.",
       "Mon choix : <b>E2, courbe en S</b>. Elle part dans le sens naturel du texte et arrive en douceur sur le point. Le coude fait schéma technique ; l’arc part parfois à contresens.",
       'cases', ['EdTech', 'Nuclear fusion', 'Biotechnology', 'Wearable tech', 'AI voice agents', 'Longevity']),
}
out = []
for at, (title, what, mine, _, cases) in AT.items():
    out.append(f'<section class="at" id="atelier-{at}"><h2><span class="al">Atelier {at}</span>{html.escape(title)}</h2>'
               f'<div class="band"><p>{what}</p><p>{mine}</p></div>')
    for c in range(1, 7):
        L = sorted([m for m in man if m['at'] == at and m['case'] == c], key=lambda m: m['var'])
        out.append(f'<div class="case{" wide" if at=="B" else ""}"><h3>Cas {c} · {html.escape(cases[c-1])}</h3><div class="row">')
        for m in L:
            k = f"{at}{c}{m['var']}"
            z = f'<img class="zoom" loading="lazy" src="img/{k}z.jpg" alt="">' if at in 'BC' else ''
            rec = ' rec' if m['rec'] else ''
            badge = '<span class="mine">Mon choix</span>' if m['rec'] else ''
            out.append(f'<div class="v{rec}" data-k="{k}" data-label="{html.escape(at+" · cas "+str(c)+" ("+cases[c-1]+") · "+m["label"])}">'
                       f'<div class="lab">{badge}{html.escape(m["label"].split(" — ")[0 if at=="C" else -1])}</div>'
                       f'<div class="pics"><img class="sl" loading="lazy" src="img/{k}.jpg" alt="">{z}</div>'
                       f'<div class="yn"><button class="y">Oui</button><button class="n">Non</button></div></div>')
        out.append('</div></div>')
    out.append('</section>')
page = open(pathlib.Path(__file__).parent / 'page_tpl.html').read().replace('<!--BODY-->', '\n'.join(out))
open(sys.argv[2] + '/index.html', 'w').write(page)
print(len(page))
