"""Atelier du juge n°3 : 5 ateliers (A-E) x 6 cas x 3 variantes, construits avec les vrais gabarits.
Écrit decks/atelier3/deck.yaml et decks/atelier3/manifest.json (atelier, cas, variante, recommandée, légende)."""
import copy, json, pathlib, yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
ed = yaml.safe_load((ROOT / 'decks/edtech/deck.yaml').read_text())
S = ed['slides']
DISC = S[0]['disclaimer']
slides, man = [], []

def add(slide, at, case, var, rec, label):
    slides.append(slide); man.append(dict(n=len(slides), at=at, case=case, var=var, rec=rec, label=label))

# ---------- A. Couverture : où va le texte du bas (disclaimer) ----------
covers = [('edtech.jpg', 'EdTech\nmarket'), ('nuclear_fusion.jpg', 'Nuclear\nfusion'), ('biotechnology.jpg', 'Biotechnology'),
          ('wearable_technology.jpg', 'Wearable\ntechnology'), ('ai_voice_agents.jpg', 'AI voice\nagents'), ('longevity.jpg', 'Longevity\nmarket')]
for i, (img, big) in enumerate(covers, 1):
    base = dict(type='cover', image=f'media/{img}', big=big, disclaimer=DISC)
    add(dict(base), 'A', i, 1, True, 'En bas, aligné sur le bouton, largeur auto (300 → 200 px) pour rester sur le sombre')
    add(dict(base, disc_style='width:430px'), 'A', i, 2, False, 'En bas, bloc large (430 px), moins de lignes')
    add(dict(base, disc_pos='under'), 'A', i, 3, False, 'Juste sous le titre, il suit le bloc titre')

# ---------- B. Notes de bas de page, sur leur vraie slide ----------
notes = [
    (4, 'Maturité', [['We compare market maturity with a simple internal score, based on tech progress and disruptions',
                      'The score is directional, not exact to the point, but it stays clearer than vague labels'],
                     ['We use a simple internal score to compare the maturity of the markets we follow',
                      'It is based on tech progress, disruptions, and yearly changes, and it stays directional'],
                     'We use a simple internal scoring tool to compare the maturity of markets we analyze regularly. It is based on observed tech progress, disruptions, and year-over-year changes. The score is mainly directional, not 100% exact, but still clearer than vague labels.'], 1),
    (5, 'Ce qui a changé', [['There is no official timeline, and some may pick other changes or slightly different dates',
                             'We kept the moments that mattered most for investors and founders entering the market'],
                            ['There is no official timeline, and others may choose different changes or dates',
                             'We kept the moments that felt most relevant for investors and entrepreneurs entering this market'],
                            'Obviously, there is no official timeline. Some may argue that other changes were more significant or happened at slightly different moments. We selected the periods that felt most relevant for investors and entrepreneurs entering the market.'], 1),
    (8, 'Estimations', [['We take estimates directly from firms’ websites and adjust them when their scope differs from ours',
                         'When an estimate is more than six months old, we account for it when we update our figures'],
                        ['Market size estimates come directly from firms’ websites',
                         'Their definitions sometimes differ from ours, so we document the gaps and adjust our math',
                         'When an estimate is more than six months old, we account for it in our updates'],
                        'Market size estimates are taken directly from firms’ websites. Because their market definitions sometimes differ from ours, we document those differences and adjust our calculations accordingly. If an estimate is more than six months old, we account for that when updating our figures.'], 1),
    (9, 'Comparaison', [['We used the latest 2025 estimates from Circana, SEMI, Sensor Tower, and Gartner',
                         'App spending is what consumers pay inside apps, and a small part of it goes to learning'],
                        ['We used the latest 2025 estimates from Circana, SEMI, Sensor Tower, and Gartner',
                         'App spending counts in-app payments, partly for learning'],
                        'We used the latest 2025 estimates from Circana, SEMI, Sensor Tower, and Gartner. App spending counts what consumers pay inside apps, and a small part of it goes to learning apps.'], 1),
    (13, 'Priorités', [['Every customer is different, and this table is a simplified view based on forums, reports, and feedback',
                        'It gives you a starting point, not a checklist, so validate the priorities with real customers first'],
                       ['Every customer is different, and this table is intentionally high-level and simplified',
                        'It is based on patterns seen across forums, reports, and feedback, as a starting point',
                        'If you build something, real priorities should come from talking to actual customers'],
                       'Every customer is different and this table is intentionally high-level and simplified. It is based on patterns seen across forums, reports, and feedback, and is meant to give you a starting point, not a checklist. If you are building something, the real priorities should come from talking to actual customers.'], 2),
    (11, 'Carte', ['We combined the regional shares of Grand View for 2024 and 2025 with Fortune Business Insights and IMARC, then adjusted everything to our market definition',
                   ['We combined the regional shares of Grand View, Fortune Business Insights, and IMARC',
                    'We then adjusted every share to our own definition of the EdTech market'],
                   'We combined the regional shares of Grand View, Fortune Business Insights, and IMARC. We then adjusted every share to our own definition of the EdTech market.'], 2),
]
VLAB = {'B': ['a : 2 lignes de même longueur, sans point', 'b : autre réécriture (2 courtes ou 3 lignes)', 'c : paragraphe avec points']}
for i, (idx, name, vs, rec) in enumerate(notes, 1):
    for v, note in enumerate(vs, 1):
        s = copy.deepcopy(S[idx]); s['note'] = note
        lab = VLAB['B'][v - 1]
        if name == 'Carte' and v == 1: lab = 'a : une seule longue phrase (2 lignes, sans point)'
        if name == 'Carte' and v == 2: lab = 'b : 2 lignes de même longueur, sans point'
        add(s, 'B', i, v, v == rec, f'{name} — {lab}')

# ---------- C. Ronds sur la barre rose de la liste datée ----------
STY = {'c1': 'C1 ronds creux roses (actuel)', 'c2': 'C2 ronds pleins roses', 'c3': 'C3 barre fine + ronds creux sable',
       'c4': 'C4 petits ronds pleins sable', 'c5': 'C5 ronds creux + petit trait vers la date', 'c6': 'C6 cible (rond + point)',
       'c7': 'C7 ronds roses cerclés de blanc'}
pairs = [('c2', 'c6'), ('c3', 'c4'), ('c5', 'c7'), ('c6', 'c2'), ('c4', 'c5'), ('c7', 'c3')]
cases = [(5, None), (6, None), (5, 4), (6, 4), (5, 5), (6, 5)]
for i, ((idx, k), (o1, o2)) in enumerate(zip(cases, pairs), 1):
    for v, sty in enumerate(['c1', o1, o2], 1):
        s = copy.deepcopy(S[idx]); s['variant'] = sty
        if k: s['items'] = s['items'][:k]
        add(s, 'C', i, v, sty == 'c1', f"{STY[sty]} — {len(s['items'])} dates")

# ---------- D. « What is the X market, in simple terms? » ----------
defs = [
    ('EdTech', 'The EdTech market is the **software, apps, and online services** that **schools, companies, and learners** pay for to **teach, learn, test, and certify** new skills',
     [('💻', 'Software, apps, and online services for learning'), ('🏫', 'Schools, companies, and learners themselves'), ('🎯', 'To teach, learn, test, and certify new skills')], '🎓'),
    ('nuclear fusion', 'The nuclear fusion market is the **reactors, magnets, lasers, and fuel** that **governments, utilities, and investors** fund to **make clean power** from fusing atoms',
     [('⚛️', 'Reactors, magnets, lasers, and fuel systems'), ('🏛️', 'Governments, utilities, and private investors'), ('⚡', 'To make clean power from fusing atoms')], '⚛️'),
    ('biotechnology', 'The biotechnology market is the **drugs, tools, and lab services** built from living cells that **pharma groups, hospitals, and labs** pay for to **treat and test** diseases',
     [('🧬', 'Drugs, tools, and lab services built from cells'), ('🏥', 'Pharma groups, hospitals, and labs'), ('💊', 'To treat, prevent, and test diseases')], '🧬'),
    ('wearable tech', 'The wearable tech market is the **watches, rings, bands, and glasses** that **consumers, insurers, and employers** buy to **track health, stay connected, and stay safe**',
     [('⌚', 'Watches, rings, bands, and smart glasses'), ('👤', 'Consumers, insurers, and employers'), ('❤️', 'To track health, stay connected, and stay safe')], '⌚'),
    ('AI voice agents', 'The AI voice agents market is the **software that talks on the phone** for you, which **companies** pay for to **answer, sell, and book** without a human agent',
     [('🎙️', 'Software that answers and makes phone calls'), ('🏢', 'Companies, from call centers to small shops'), ('📞', 'To answer, sell, and book without a human')], '🎙️'),
    ('longevity', 'The longevity market is the **tests, clinics, drugs, and supplements** that **people, clinics, and insurers** pay for to **stay healthy for longer**',
     [('🧪', 'Tests, clinics, drugs, and supplements'), ('👥', 'People, clinics, and insurers'), ('⏳', 'To stay healthy for longer')], '⏳'),
]
DLAB = {'d4': 'D4 phrase + 3 cartes WHAT / WHO PAYS / WHAT FOR', 'd1': 'D1 cadre avec icônes (ancien design)', 'd3': 'D3 étiquette à gauche + phrase'}
for i, (mk, text, parts, ico) in enumerate(defs, 1):
    for v, var in enumerate(['d4', 'd1', 'd3'], 1):
        s = copy.deepcopy(S[2]); s['variant'] = var
        s['title'] = f'What is the {mk} market,\nin simple terms?' if mk != 'EdTech' else s['title']
        s['text'] = text if var != 'd1' else text.replace('**', '')
        s['parts'] = [dict(e=e, k=k, v=t) for (e, t), k in zip(parts, ['WHAT', 'WHO PAYS', 'WHAT FOR'])]
        s['icon_tl'] = ico
        s['market_label'] = mk if mk[0].isupper() else mk.capitalize()
        add(s, 'D', i, v, var == 'd4', DLAB[var])

# ---------- E. Courbes de la carte (textes et chiffres fictifs, seule la forme compte) ----------
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
CLAB = {'s': 'E2 courbe en S', 'elbow': 'E1 coude', 'arc': 'E3 arc'}
for i, (mk, regs) in enumerate(maps, 1):
    for v, cv in enumerate(['s', 'elbow', 'arc'], 1):
        s = copy.deepcopy(S[11]); s['curve'] = cv
        if regs:
            s['regions'] = {k: dict(pct=p, text=t) for k, (p, t) in regs.items()}
            s['title'] = f'Where in the world is\n{mk} money spent?'
            s['note'] = 'Workshop case: the shares and texts are illustrative, only the shape of the lines matters here'
            s.pop('widths', None)
        add(s, 'E', i, v, cv == 's', CLAB[cv])

deck = dict(market='Workshop 3', label='Workshop', quarter='judge', year=2026, slug='atelier3', chapters=[], slides=slides)
(ROOT / 'decks/atelier3/deck.yaml').write_text(yaml.dump(deck, allow_unicode=True, sort_keys=False, width=1000))
(ROOT / 'decks/atelier3/manifest.json').write_text(json.dumps(man, ensure_ascii=False, indent=1))
print(len(slides), 'slides')
