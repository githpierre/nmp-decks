"""Atelier 5 (après la 2e revue de Pierre).
- B = ATELIER DU JUGE (décision qui revient sur chaque slide) : combien de lignes pour une note de bas de page.
  6 vraies notes ; A = 1 ligne, B = 2 lignes, C = 3 lignes ; même contenu ; lignes à moins de 12 % d'écart (audit NOTE_BALANCE).
  Mon choix change selon le cas, et je dis pourquoi j'hésite.
- C, D, E = PRÉSENTATIONS DE VARIANTES (un design qu'on choisit une fois) : beaucoup de variantes, une par ligne.
Écrit decks/atelier5/deck.yaml + manifest.json."""
import copy, json, pathlib, yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
S = yaml.safe_load((ROOT / 'decks/edtech/deck.yaml').read_text())['slides']
slides, sections = [], []

def add(slide):
    slides.append(slide); return len(slides)

# ---------------- B : atelier du juge ----------------
B = [
 (4, 'Maturité', 'B',
  'Deux idées (ce qu’est le score, et ses limites). Une seule ligne perd la limite, trois lignes coupent une idée en deux.',
  ['We rate market maturity with a simple internal score that is directional, not exact'],
  ['We rate market maturity with a simple internal score based on tech progress and disruptions',
   'The score is directional and not exact, but it stays clearer than vague labels like early'],
  ['We rate market maturity with a simple internal score of our own',
   'It is based on tech progress, disruptions, and yearly changes',
   'It is directional and not exact, but clearer than vague labels']),
 (5, 'Ce qui a changé', 'B',
  'Deux idées (pas de chronologie officielle, et notre critère de choix). En une ligne on ne dit plus pour qui on a choisi.',
  ['There is no official timeline, so we kept the changes that mattered most to investors and founders'],
  ['There is no official timeline, and some may pick other changes or slightly different dates',
   'We kept the moments that mattered most for investors and founders entering the market'],
  ['There is no official timeline for when this market changed',
   'Some may pick other changes or slightly different dates',
   'We kept the moments that mattered most to investors']),
 (8, 'Estimations', 'C',
  'Trois étapes distinctes (source, ajustement du périmètre, âge du chiffre). En 2 lignes, deux étapes se collent ; ici 3 lignes se lisent comme une méthode.',
  ['We take each estimate from the firm’s website and adjust it to our scope and to its age'],
  ['We take each estimate from the firm’s website and adjust it when its scope differs from ours',
   'When an estimate is more than six months old, we also take its age into account in our math'],
  ['We take each estimate directly from the firm’s own website',
   'We adjust it when the firm’s scope is different from ours',
   'We also take into account estimates older than six months']),
 (9, 'Comparaison', 'B',
  'La source suffit-elle (1 ligne) ? Non : « app spending » surprend le lecteur, il faut le dire. Deux lignes suffisent.',
  ['We used the latest 2025 estimates from Circana, SEMI, Sensor Tower, and Gartner'],
  ['We used the latest 2025 estimates from Circana, SEMI, Sensor Tower, and Gartner',
   'App spending is what people pay inside apps, and a small part goes to learning'],
  ['We used the latest 2025 estimates from four research firms',
   'They are Circana, SEMI, Sensor Tower, and also Gartner',
   'App spending includes a small part for learning apps']),
 (13, 'Priorités', 'B',
  'Trois idées possibles, mais « chaque client est différent » et « valide avec de vrais clients » vont ensemble. Deux lignes, plus fluide que trois.',
  ['This table is a simple starting point, so check its priorities with real customers first'],
  ['Every customer is different, and this table is a simplified view based on forums and reports',
   'It gives you a starting point, not a checklist, so check the priorities with real customers'],
  ['Every customer is different, so this table is a simplified view',
   'It is built from patterns seen in forums, reports, and feedback',
   'Use it as a starting point and check it with real customers']),
 (11, 'Carte du monde', 'A',
  'Une seule idée (trois sources combinées puis ajustées). La couper en deux lignes ajoute des mots pour rien : une ligne suffit.',
  ['We combined the regional shares of Grand View, Fortune Business Insights, and IMARC, adjusted to our definition'],
  ['We combined the regional shares of Grand View, Fortune Business Insights, and IMARC',
   'We then adjusted every share so it matches our own definition of the EdTech market'],
  ['We used regional shares from Grand View, Fortune, and IMARC',
   'We combined them into a single share for each of the regions',
   'We then adjusted every share to our own definition of EdTech']),
]
cases = []
for idx, name, mine, why, one, two, three in B:
    ns = {}
    for L, note in zip('ABC', [one, two, three]):
        s = copy.deepcopy(S[idx]); s['note'] = note; ns[L] = add(s)
    cases.append(dict(name=name, mine=mine, why=why, n=ns))
sections.append(dict(kind='juge', id='B', title='Notes de bas de page : 1, 2 ou 3 lignes ?', short='Notes',
    change='le nombre de lignes. Le contenu reste le même, et dans chaque version les lignes ont presque la même longueur (moins de 12 % d’écart, contrôlé à chaque build).',
    variants={'A': '1 ligne', 'B': '2 lignes', 'C': '3 lignes'},
    rule='Ma règle de départ : une ligne par idée. 1 idée = 1 ligne, 2 idées = 2 lignes, 3 étapes distinctes = 3 lignes. Jamais de point final quand chaque ligne est une phrase.',
    cases=cases, zoom='note'))

# ---------------- C : présentation de variantes (liste datée) ----------------
K = [('k1', 'Classique', 'barre 8 px, ronds creux 14 px, centrés sur l’axe'),
     ('k2', 'Barre fine', 'barre 4 px, ronds creux 14 px détachés par un liseré'),
     ('k3', 'Gros anneaux', 'barre 8 px, anneaux 18 px plus épais'),
     ('k4', 'Fil + repère', 'barre 2 px, petits ronds, petit trait vers la date'),
     ('k5', 'Lumineux', 'barre 6 px arrondie, léger halo rose'),
     ('k6', 'Anneaux pleins', 'anneaux 16 px remplis d’un bleu un peu plus clair')]
vs = []
for k, name, desc in K:
    s = copy.deepcopy(S[5]); s['variant'] = k
    vs.append(dict(key=k, name=name, desc=desc, n=[add(s)]))
sections.append(dict(kind='variantes', id='C', title='Liste datée : ronds creux roses, centrés sur l’axe', short='Liste datée', zoom='rail',
    what='Tu as gardé les ronds creux roses. Tous sont maintenant centrés sur l’axe de la barre (et à la hauteur exacte de la date). Voici 6 finitions, une par ligne. Le même gabarit sert pour les 2 pages (toujours 6 dates, c’est maintenant vérifié à chaque build).',
    mine='k1', why='Le plus net : la barre et les anneaux ont le même poids, rien ne vole la vedette aux textes. B (barre fine) est élégant, mais la barre devient un fil.',
    variants=vs))

# ---------------- D : présentation de variantes (définition) ----------------
defs = {
 'EdTech': ('EdTech', 'The EdTech market is the **software, apps, and online services** that **schools, companies, and learners** pay for to **teach, learn, test, and certify** new skills',
   [('💻', 'Software, apps, and online services for learning'), ('🏫', 'Schools, companies, and learners themselves'), ('🎯', 'To teach, learn, test, and certify new skills')]),
 'biotechnology': ('Biotechnology', 'The biotechnology market is the **drugs, tools, and lab services** built from living cells that **pharma groups, hospitals, and labs** pay for to **treat and test** diseases',
   [('🧬', 'Drugs, tools, and lab services built from cells'), ('🏥', 'Pharma groups, hospitals, and labs'), ('💊', 'To treat, prevent, and test diseases')]),
}
E = [('e1', 'Phrase + 3 cartes', 'l’actuel, avec un liseré rose en haut des cartes'),
     ('e2', 'Équation', 'WHAT + WHO PAYS + WHAT FOR = le marché'),
     ('e3', 'Phrase à gauche, pile à droite', 'la phrase en grand, les 3 parties empilées'),
     ('e4', 'Le marché au centre', 'un rond au centre, les 3 parties autour'),
     ('e5', 'Le parcours', 'qui paie → quoi → pour quoi faire, avec des flèches'),
     ('e6', 'Citation + pastilles', 'grande phrase avec barre rose, 3 pastilles dessous'),
     ('e7', '3 colonnes numérotées', '01 / 02 / 03, sans cadres'),
     ('e8', 'Une seule grande carte', 'phrase en haut, 3 parties en bas'),
     ('e9', 'Entrée de dictionnaire', '« EdTech market, noun » puis la définition')]
vs = []
for k, name, desc in E:
    ns = []
    for mk, (lab, text, parts) in defs.items():
        s = copy.deepcopy(S[2]); s['variant'] = k; s['market_label'] = lab
        if mk != 'EdTech': s['title'] = f'What is the {mk} market,\nin simple terms?'
        s['text'] = text
        s['parts'] = [dict(e=e, k=kk, v=t) for (e, t), kk in zip(parts, ['WHAT', 'WHO PAYS', 'WHAT FOR'])]
        ns.append(add(s))
    vs.append(dict(key=k, name=name, desc=desc, n=ns))
sections.append(dict(kind='variantes', id='D', title='« What is the X market, in simple terms? » : 9 designs', short='Définition',
    what='9 designs différents. Chacun est montré sur EdTech et sur Biotechnology (nom long), pour vérifier qu’il tient avec un autre marché.',
    mine='e3', why='La phrase est l’info principale : en grand à gauche, elle se lit d’abord ; les 3 parties à droite la résument d’un coup d’œil. Plus aéré que les cartes en ligne.',
    variants=vs))

# ---------------- E : présentation de variantes (carte) ----------------
C6 = [('s', 'Courbe en S', 'part dans le sens du texte, arrive en douceur'),
      ('soft', 'Arc léger', 'presque droite, juste un peu courbée'),
      ('arc', 'Arc marqué', 'courbe plus prononcée'),
      ('elbow', 'Coude arrondi', 'un seul virage'),
      ('s-dot', 'S + point de départ', 'courbe en S avec un petit point sous le texte'),
      ('s-solid', 'S en trait plein', 'courbe en S, trait fin continu au lieu de pointillés')]
vs = []
for k, name, desc in C6:
    s = copy.deepcopy(S[11]); s['curve'] = k
    vs.append(dict(key=k, name=name, desc=desc, n=[add(s)]))
sections.append(dict(kind='variantes', id='E', title='Carte du monde : la forme des lignes', short='Carte',
    what='6 formes de lignes, chacune sur toute la largeur pour bien voir les flèches. Points, textes et positions ne bougent pas.',
    mine='s-dot', why='La courbe en S est la plus naturelle, et le petit point dit clairement de quel texte part la ligne.',
    variants=vs))

deck = dict(market='Workshop 5', label='EdTech market', quarter='judge', year=2026, slug='atelier5', chapters=[], slides=slides)
(ROOT / 'decks/atelier5').mkdir(exist_ok=True)
(ROOT / 'decks/atelier5/deck.yaml').write_text(yaml.dump(deck, allow_unicode=True, sort_keys=False, width=1000))
(ROOT / 'decks/atelier5/manifest.json').write_text(json.dumps(dict(sections=sections), ensure_ascii=False, indent=1))
print(len(slides), 'slides')
