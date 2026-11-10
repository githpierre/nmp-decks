"""Atelier 6 : lignes pointillées de la carte. 3 ateliers du juge, 6 cas réels x A/B/C, UNE chose change par atelier.
Chaque cas = une région d'une carte ; seule la ligne de cette région change, le zoom montre cette région."""
import copy, json, pathlib, yaml
ROOT = pathlib.Path(__file__).resolve().parent.parent
S = yaml.safe_load((ROOT / 'decks/edtech/deck.yaml').read_text())['slides']
VOICE = dict(na=(52, 'North America leads, since most voice agent startups and their first big customers are in the US, from call centers to clinics and car dealers.'),
     eu=(21, 'Europe follows, slowed by language diversity and strict privacy rules that make every rollout longer.'),
     apac=(17, 'Asia-Pacific grows with India and the Philippines, where outsourced call centers start to use AI agents.'),
     latam=(5, 'Latin America tests voice agents in banks and telecom companies, mostly in Spanish and Portuguese.'),
     mea=(5, 'The Middle East buys AI agents for government services and airlines, often in Arabic and English.'))
CASES = [('EdTech', 'na', 'North America : le point est sous le texte, à droite'),
         ('EdTech', 'eu', 'Europe : le point est sous le texte, côté gauche'),
         ('EdTech', 'apac', 'Asia-Pacific : le point est en bas à gauche du texte'),
         ('EdTech', 'latam', 'Latin America : le point est à droite du texte, un peu plus haut'),
         ('EdTech', 'mea', 'Middle East & Africa : le point est au-dessus du titre'),
         ('AI voice agents', 'na', 'North America, texte long : le point est loin sous le texte')]
ATS = [('M1', 'Départ sur le texte', 'start', {'A': 'corner', 'B': 'middle', 'C': 'side'},
        {'A': 'au coin du texte le plus proche du point', 'B': 'au milieu du bord tourné vers le point', 'C': 'sur le côté, à la ligne du milieu'},
        'l’endroit où la ligne quitte le texte. L’arrivée sur le point et la forme du virage restent les mêmes.'),
       ('M2', 'Arrivée sur le point', 'end', {'A': 'h', 'B': 'v', 'C': 'radial'},
        {'A': 'arrive à l’horizontale, sur le côté du point', 'B': 'arrive à la verticale, par le haut ou le bas', 'C': 'arrive tout droit vers le centre'},
        'la façon dont la ligne touche le point. Le départ (milieu du bord, ton choix M1) et la forme du virage restent les mêmes.'),
       ('M3', 'Forme du virage', 'bend', {'A': 0.9, 'B': 0.67, 'C': 0.35},
        {'A': 'coude serré', 'B': 'coude arrondi (actuel)', 'C': 'courbe douce'},
        'la forme du virage. Départ (milieu du bord) et arrivée (à angle droit) restent les mêmes.')]
PICK = {
 'M1': [('A', 'Le coin le plus proche donne la ligne la plus courte, elle part juste sous « based there. » et descend vers le point.'),
        ('B', 'Ici le point est presque sous le milieu du texte : partir du milieu donne une ligne courte et droite. Le coin gauche fait un détour.'),
        ('A', 'Le coin gauche du texte est juste au-dessus du point : ligne courte. Partir du milieu ou du côté allonge la ligne pour rien.'),
        ('B', 'Le point est à côté du texte : partir du côté, à la ligne du milieu, se lit naturellement. Partir du titre (A, C) fait croire que la ligne prolonge le titre.'),
        ('A', 'Le coin gauche du titre est le plus près du point : la ligne monte puis entre dans le point. Depuis le milieu, elle repart en arrière.'),
        ('A', 'Texte long, point loin dessous : le coin reste le plus court. Depuis le milieu, la ligne traverse la moitié de la carte.')],
 'M2': [('A', 'La ligne descend du milieu du texte puis entre dans le point à l’horizontale : un vrai coude, élégant. Par le haut, elle fait un S.'),
        ('A', 'Elle descend puis tourne vers le point et l’attaque par le côté. Les deux autres font un S ou une diagonale.'),
        ('A', 'Elle descend un peu puis file à l’horizontale vers le point : propre. C (vers le centre) est correct mais plus mou.'),
        ('B', 'Ici la ligne part sur le côté du texte : elle doit donc arriver par le bas, à la verticale, pour faire un coude. À l’horizontale, elle ferait un S.'),
        ('A', 'La ligne monte du milieu du titre puis entre dans le point par le côté. Par le bas, elle ferait un S serré.'),
        ('A', 'Comme le cas 1 : longue descente puis entrée horizontale dans le point.')],
 'M3': [('B', 'Le coude arrondi est net sans être cassant. Le serré fait presque un angle droit, le doux devient une diagonale.'),
        ('B', 'Même chose : « je descends, puis je vais au point ».'),
        ('B', 'Le coude arrondi suit le bas du texte puis va au point ; la courbe douce coupe en diagonale.'),
        ('C', 'Ici la ligne est longue et presque horizontale : la courbe douce glisse jusqu’au point, le coude fait une petite marche.'),
        ('B', 'Ligne courte : le coude arrondi suffit ; le serré fait un angle.'),
        ('B', 'Longue ligne : le coude arrondi reste lisible ; le doux part en biais trop tôt.')]}
RULE = {'M1': 'Ma règle de départ : partir du coin du texte le plus proche du point ; du milieu quand le point est en face du milieu ; du côté quand le point est à côté du texte.',
        'M2': 'Ma règle de départ : arriver à angle droit par rapport au départ (un vrai coude). La ligne part vers le bas ou le haut : elle arrive à l’horizontale. Elle part sur le côté : elle arrive à la verticale.',
        'M3': 'Ma règle de départ : coude arrondi ; courbe douce quand la ligne est longue et presque horizontale.'}
slides, sections = [], []
for at, title, key, vals, names, change in ATS[1:]:   # M1 settled: start = middle of the edge facing the dot
    cases = []
    for mk, rk, label in CASES:
        ns = {}
        for L, v in vals.items():
            s = copy.deepcopy(S[11])
            if mk != 'EdTech':
                s['regions'] = {k: dict(pct=p, text=t) for k, (p, t) in VOICE.items()}; s['title'] = f'Where in the world is\n{mk} money spent?'; s.pop('widths', None)
                s['note'] = ['Workshop case: the shares and texts are illustrative, only the lines matter here']
            s['regions'][rk][key] = v; s['hl'] = rk
            slides.append(s); ns[L] = len(slides)
        cases.append(dict(name=label, mine=PICK[at][len(cases)][0], why=PICK[at][len(cases)][1], n=ns))
    sections.append(dict(kind='juge', id=at, title=f'Carte : {title}', short=title, change=change, variants=names, rule=RULE[at], cases=cases, zoom='region'))
deck = dict(market='Workshop 6', label='EdTech market', quarter='judge', year=2026, slug='atelier6', chapters=[], slides=slides)
(ROOT / 'decks/atelier6').mkdir(exist_ok=True)
(ROOT / 'decks/atelier6/deck.yaml').write_text(yaml.dump(deck, allow_unicode=True, sort_keys=False, width=1000))
(ROOT / 'decks/atelier6/manifest.json').write_text(json.dumps(dict(sections=sections), ensure_ascii=False, indent=1))
print(len(slides))
