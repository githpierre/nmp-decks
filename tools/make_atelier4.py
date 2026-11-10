"""Atelier du juge n°4 (refait après la revue de Pierre) : ateliers B à E.
Règles : 6 cas x 3 variantes A/B/C, les MÊMES variantes à chaque cas, UNE seule chose change entre A, B et C.
Écrit decks/atelier4/deck.yaml et decks/atelier4/manifest.json (méta des ateliers + liste des slides)."""
import copy, json, pathlib, yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
S = yaml.safe_load((ROOT / 'decks/edtech/deck.yaml').read_text())['slides']
slides, items, ateliers = [], [], []

def add(slide, at, case, letter):
    slides.append(slide); items.append(dict(n=len(slides), at=at, case=case, var=letter))

# ---------- B. Notes de bas de page : seule la mise en forme change (mêmes idées, presque mêmes mots) ----------
B = [
 (4, 'Maturité',
  ['We compare market maturity with a simple internal score based on tech progress and disruptions',
   'The score is directional, not exact, but it stays clearer than vague labels'],
  ['We compare market maturity with a simple internal score',
   'It is based on tech progress and disruptions',
   'The score is directional, not exact, but it stays clearer than vague labels']),
 (5, 'Ce qui a changé',
  ['There is no official timeline, and some may pick other changes or slightly different dates',
   'We kept the moments that mattered most for investors and founders entering the market'],
  ['There is no official timeline',
   'Some may pick other changes or slightly different dates',
   'We kept the moments that mattered most for investors and founders entering the market']),
 (8, 'Estimations',
  ['We take estimates directly from firms’ websites and adjust them when their scope differs from ours',
   'When an estimate is more than six months old, we account for it when we update our figures'],
  ['We take estimates directly from firms’ websites',
   'We adjust them when their scope differs from ours',
   'When an estimate is more than six months old, we account for it when we update our figures']),
 (9, 'Comparaison',
  ['We used the latest 2025 estimates from Circana, SEMI, Sensor Tower, and Gartner',
   'App spending is what consumers pay inside apps, and a small part of it goes to learning'],
  ['We used the latest 2025 estimates from Circana, SEMI, Sensor Tower, and Gartner',
   'App spending is what consumers pay inside apps',
   'A small part of it goes to learning']),
 (13, 'Priorités',
  ['Every customer is different, and this table is a simplified view based on forums, reports, and feedback',
   'It gives you a starting point, not a checklist, so validate the priorities with real customers first'],
  ['Every customer is different, and this table is a simplified view',
   'It is based on forums, reports, and feedback, and gives you a starting point, not a checklist',
   'Validate the priorities with real customers first']),
 (11, 'Carte du monde',
  ['We combined the regional shares of Grand View, Fortune Business Insights, and IMARC',
   'We then adjusted every share to our own definition of the EdTech market'],
  ['We combined the regional shares of Grand View, Fortune Business Insights, and IMARC',
   'We then adjusted every share',
   'to our own definition of the EdTech market']),
]
B[5] = (11, 'Carte du monde', B[5][2],
        ['We used the regional shares of Grand View, Fortune Business Insights, and IMARC',
         'We combined them into one figure per region',
         'We then adjusted every share to our own definition of the EdTech market'])
ateliers.append(dict(id='B', title='Notes de bas de page', short='Notes',
    change='la mise en forme de la note. Les idées et presque tous les mots restent les mêmes.',
    variants={'A': '2 lignes de même longueur, sans point', 'B': '3 lignes plus courtes, sans point', 'C': 'un paragraphe avec des points'},
    mine='A', why='C’est ta règle actuelle : 2 lignes équilibrées se lisent d’un coup d’œil. 3 lignes prennent plus de hauteur pour rien, et le paragraphe se lit moins vite.',
    cases=[b[1] for b in B], zoom=True))
for i, (idx, name, two, three) in enumerate(B, 1):
    para = '. '.join(two) + '.'
    for L, note in zip('ABC', [two, three, para]):
        s = copy.deepcopy(S[idx]); s['note'] = note; add(s, 'B', i, L)

# ---------- C. Liste datée : seule la forme des ronds change ----------
cases_c = [(5, None, 'Page 1, 6 dates'), (6, None, 'Page 2, 6 dates'), (5, 4, 'Page 1, 4 dates'),
           (6, 4, 'Page 2, 4 dates'), (5, 5, 'Page 1, 5 dates'), (6, 5, 'Page 2, 5 dates')]
ateliers.append(dict(id='C', title='Liste datée : les ronds sur la barre rose', short='Liste datée',
    change='la forme des ronds. Barre, dates, textes et espacements sont identiques.',
    variants={'A': 'ronds creux roses (actuel)', 'B': 'ronds pleins roses', 'C': 'petits ronds pleins sable'},
    mine='A', why='Les ronds creux marquent chaque date sans voler la vedette au texte. Les ronds pleins font une barre très chargée, et le sable se perd sur le fond.',
    cases=[c[2] for c in cases_c], zoom=True))
for i, (idx, k, _) in enumerate(cases_c, 1):
    for L, sty in zip('ABC', ['c1', 'c2', 'c4']):
        s = copy.deepcopy(S[idx]); s['variant'] = sty
        if k: s['items'] = s['items'][:k]
        add(s, 'C', i, L)

# ---------- D. Définition : seule la mise en page change ----------
defs = [
 ('EdTech', 'EdTech', 'The EdTech market is the **software, apps, and online services** that **schools, companies, and learners** pay for to **teach, learn, test, and certify** new skills',
  [('💻', 'Software, apps, and online services for learning'), ('🏫', 'Schools, companies, and learners themselves'), ('🎯', 'To teach, learn, test, and certify new skills')], '🎓'),
 ('nuclear fusion', 'Nuclear fusion', 'The nuclear fusion market is the **reactors, magnets, lasers, and fuel** that **governments, utilities, and investors** fund to **make clean power** from fusing atoms',
  [('⚛️', 'Reactors, magnets, lasers, and fuel systems'), ('🏛️', 'Governments, utilities, and private investors'), ('⚡', 'To make clean power from fusing atoms')], '⚛️'),
 ('biotechnology', 'Biotechnology', 'The biotechnology market is the **drugs, tools, and lab services** built from living cells that **pharma groups, hospitals, and labs** pay for to **treat and test** diseases',
  [('🧬', 'Drugs, tools, and lab services built from cells'), ('🏥', 'Pharma groups, hospitals, and labs'), ('💊', 'To treat, prevent, and test diseases')], '🧬'),
 ('wearable tech', 'Wearable tech', 'The wearable tech market is the **watches, rings, bands, and glasses** that **consumers, insurers, and employers** buy to **track health, stay connected, and stay safe**',
  [('⌚', 'Watches, rings, bands, and smart glasses'), ('👤', 'Consumers, insurers, and employers'), ('❤️', 'To track health, stay connected, and stay safe')], '⌚'),
 ('AI voice agents', 'AI voice agents', 'The AI voice agents market is the **software that talks on the phone** for you, which **companies** pay for to **answer, sell, and book** without a human agent',
  [('🎙️', 'Software that answers and makes phone calls'), ('🏢', 'Companies, from call centers to small shops'), ('📞', 'To answer, sell, and book without a human')], '🎙️'),
 ('longevity', 'Longevity', 'The longevity market is the **tests, clinics, drugs, and supplements** that **people, clinics, and insurers** pay for to **stay healthy for longer**',
  [('🧪', 'Tests, clinics, drugs, and supplements'), ('👥', 'People, clinics, and insurers'), ('⏳', 'To stay healthy for longer')], '⏳'),
]
ateliers.append(dict(id='D', title='« What is the X market, in simple terms? »', short='Définition',
    change='la mise en page. La phrase de définition est la même dans les 3 (seuls les mots en gras disparaissent dans B, l’ancien cadre).',
    variants={'A': 'phrase + 3 cartes WHAT / WHO PAYS / WHAT FOR', 'B': 'phrase dans un cadre avec icônes (ancien design)', 'C': 'nom du marché à gauche + phrase'},
    mine='A', why='Les 3 cartes font comprendre le marché en 3 secondes, même sans lire la phrase. B ne met rien en valeur ; C est propre mais reste une seule phrase.',
    cases=[d[1] for d in defs], zoom=False, note='Définitions des 5 nouveaux marchés écrites pour l’atelier (à refaire avec la recherche dans un vrai deck).'))
for i, (mk, lab, text, parts, ico) in enumerate(defs, 1):
    for L, var in zip('ABC', ['d4', 'd1', 'd3']):
        s = copy.deepcopy(S[2]); s['variant'] = var
        if mk != 'EdTech': s['title'] = f'What is the {mk} market,\nin simple terms?'
        s['text'] = text if var != 'd1' else text.replace('**', '')
        s['parts'] = [dict(e=e, k=k, v=t) for (e, t), k in zip(parts, ['WHAT', 'WHO PAYS', 'WHAT FOR'])]
        s['icon_tl'] = ico; s['market_label'] = lab
        add(s, 'D', i, L)

# ---------- E. Carte : seule la forme des lignes pointillées change ----------
maps = [
 ('EdTech', None),
 ('nuclear fusion', dict(na=(48, 'North America leads, with most private fusion startups and the largest rounds raised so far.'),
     eu=(24, 'Europe relies on public programs and a few startups, with ITER in France as its anchor.'),
     apac=(21, 'Asia-Pacific grows with China and Japan, where the state funds large test reactors.'),
     latam=(2, 'Latin America has almost no fusion spending yet, outside of research labs.'),
     mea=(5, 'The Middle East funds a few partnerships, mostly to diversify away from oil.'))),
 ('biotechnology', dict(na=(44, 'North America leads by far, with Boston and San Francisco as the two main hubs for biotech startups and big pharma buyers.'),
     eu=(25, 'Europe is strong in research, with hubs in the UK, Switzerland, and Germany, but its startups raise less money.'),
     apac=(23, 'Asia-Pacific grows fast, led by China and South Korea, which now run many of the world’s drug trials.'),
     latam=(4, 'Latin America is small and mostly buys drugs and tests made elsewhere.'),
     mea=(4, 'The Middle East invests in local production, while Africa remains a small market.'))),
 ('wearable tech', dict(na=(33, 'North America is the largest market for smartwatches and rings.'),
     eu=(26, 'Europe buys a lot of fitness trackers and smartwatches.'),
     apac=(30, 'Asia-Pacific has the most users, led by China and India, with cheap bands.'),
     latam=(5, 'Latin America buys mostly low-cost bands.'),
     mea=(6, 'The Gulf countries buy premium watches.'))),
 ('AI voice agents', dict(na=(52, 'North America leads, since most voice agent startups and their first big customers are in the US, from call centers to clinics and car dealers.'),
     eu=(21, 'Europe follows, slowed by language diversity and strict privacy rules that make every rollout longer.'),
     apac=(17, 'Asia-Pacific grows with India and the Philippines, where outsourced call centers start to use AI agents.'),
     latam=(5, 'Latin America tests voice agents in banks and telecom companies, mostly in Spanish and Portuguese.'),
     mea=(5, 'The Middle East buys AI agents for government services and airlines, often in Arabic and English.'))),
 ('longevity', dict(na=(41, 'North America leads with clinics, tests, and supplements sold directly to people.'),
     eu=(28, 'Europe follows, with clinics in Switzerland and the UK and a large supplement market.'),
     apac=(22, 'Asia-Pacific grows with Japan, an aging country, and Singapore, a research hub.'),
     latam=(3, 'Latin America is small, with a few clinics in Mexico and Brazil.'),
     mea=(6, 'The Gulf countries invest in longevity research and premium clinics.'))),
]
ateliers.append(dict(id='E', title='Carte du monde : la forme des lignes pointillées', short='Carte',
    change='la forme des lignes qui relient chaque texte à son point. Points, textes et positions sont identiques.',
    variants={'A': 'courbe en S', 'B': 'coude (angle arrondi)', 'C': 'arc'},
    mine='A', why='La courbe en S part dans le sens du texte et arrive en douceur sur le point. Le coude fait schéma technique ; l’arc part parfois à contresens.',
    cases=['EdTech', 'Nuclear fusion', 'Biotechnology', 'Wearable tech', 'AI voice agents', 'Longevity'], zoom=False,
    note='Sur les 5 nouvelles cartes, les parts et les textes sont inventés : seule la forme des lignes compte.'))
for i, (mk, regs) in enumerate(maps, 1):
    for L, cv in zip('ABC', ['s', 'elbow', 'arc']):
        s = copy.deepcopy(S[11]); s['curve'] = cv
        if regs:
            s['regions'] = {k: dict(pct=p, text=t) for k, (p, t) in regs.items()}
            s['title'] = f'Where in the world is\n{mk} money spent?'
            s['note'] = 'Workshop case: the shares and texts are illustrative, only the shape of the lines matters here'
            s.pop('widths', None)
        add(s, 'E', i, L)

deck = dict(market='Workshop 4', label='EdTech market', quarter='judge', year=2026, slug='atelier4', chapters=[], slides=slides)
(ROOT / 'decks/atelier4').mkdir(exist_ok=True)
(ROOT / 'decks/atelier4/deck.yaml').write_text(yaml.dump(deck, allow_unicode=True, sort_keys=False, width=1000))
(ROOT / 'decks/atelier4/manifest.json').write_text(json.dumps(dict(ateliers=ateliers, items=items), ensure_ascii=False, indent=1))
print(len(slides), 'slides')
