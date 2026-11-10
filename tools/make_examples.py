"""Exemples hors EdTech pour tester les gabarits sur d'autres marchés (couverture, définition, carte).
Contenus de carte ILLUSTRATIFS (chiffres et textes fictifs, la note le dit) : seule la mise en page est testée."""
import copy, pathlib, yaml
ROOT = pathlib.Path(__file__).resolve().parent.parent
S = yaml.safe_load((ROOT / 'decks/edtech/deck.yaml').read_text())['slides']
DISC = S[0]['disclaimer']
M = [
 ('nuclear_fusion.jpg', 'Nuclear\nfusion', 'nuclear fusion', '⚛️',
  'The nuclear fusion market is the reactors, magnets, lasers, and fuel that governments, utilities, and investors fund to make clean power from fusing atoms',
  dict(na=(48, 'North America leads, with most private fusion startups, the largest rounds raised so far, and the first deals to sell fusion power to tech companies.'),
       eu=(24, 'Europe relies on public programs and a few startups, with ITER in France as its anchor and national labs in the UK and Germany behind most of the work.'),
       apac=(21, 'Asia-Pacific grows with China and Japan, where the state funds large test reactors and moves faster than most private projects in the West.'),
       latam=(2, 'Latin America has almost no fusion spending yet, outside of a few university research labs in Brazil and Argentina.'),
       mea=(5, 'The Middle East funds a few partnerships with Western startups, mostly to prepare the energy mix that comes after oil and gas.'))),
 ('biotechnology.jpg', 'Biotechnology', 'biotechnology', '🧬',
  'The biotechnology market is the drugs, tools, and lab services built from living cells that pharma groups, hospitals, and labs pay for to treat and test diseases',
  dict(na=(44, 'North America leads by far, with Boston and San Francisco as the two main hubs for biotech startups, investors, and big pharma buyers.'),
       eu=(25, 'Europe is strong in research, with hubs in the UK, Switzerland, and Germany, but its startups raise less money and often sell out early.'),
       apac=(23, 'Asia-Pacific grows fast, led by China and South Korea, which now run many of the world’s drug trials and make a growing share of new drugs.'),
       latam=(4, 'Latin America is small and mostly buys drugs and tests made elsewhere, with a few local makers in Brazil and Argentina.'),
       mea=(4, 'The Middle East invests in local production and research centers, while Africa remains a small market that mostly buys from abroad.'))),
 ('wearable_technology.jpg', 'Wearable\ntechnology', 'wearable tech', '⌚',
  'The wearable tech market is the watches, rings, bands, and glasses that consumers, insurers, and employers buy to track health, stay connected, and stay safe',
  dict(na=(33, 'North America is the largest market for smartwatches and rings, where people pay more for health tracking and a premium brand.'),
       eu=(26, 'Europe buys a lot of fitness trackers and smartwatches, with strong sales in Germany and the UK, and stricter rules on health data.'),
       apac=(30, 'Asia-Pacific has the most users, led by China and India, where cheap bands from local brands sell in very large volumes.'),
       latam=(5, 'Latin America buys mostly low-cost bands and older watch models, with Brazil and Mexico as the two largest markets.'),
       mea=(6, 'The Gulf countries buy premium watches and rings, while the rest of the region is still a small market for cheaper bands.'))),
 ('ai_voice_agents.jpg', 'AI voice\nagents', 'AI voice agents', '🎙️',
  'The AI voice agents market is the software that talks on the phone for you, which companies pay for to answer, sell, and book without a human agent',
  dict(na=(52, 'North America leads, since most voice agent startups and their first big customers are in the US, from call centers to clinics and car dealers.'),
       eu=(21, 'Europe follows, slowed by language diversity and strict privacy rules that make every rollout longer, even for large companies.'),
       apac=(17, 'Asia-Pacific grows with India and the Philippines, where outsourced call centers start to use AI agents for simple calls.'),
       latam=(5, 'Latin America tests voice agents in banks and telecom companies, mostly in Spanish and Portuguese, and often with local partners.'),
       mea=(5, 'The Middle East buys AI agents for government services and airlines, often in Arabic and English, with Gulf states as early buyers.'))),
 ('longevity.jpg', 'Longevity\nmarket', 'longevity', '⏳',
  'The longevity market is the tests, clinics, drugs, and supplements that people, clinics, and insurers pay for to stay healthy for longer',
  dict(na=(41, 'North America leads with clinics, tests, and supplements sold directly to people, and most of the venture money in the field.'),
       eu=(28, 'Europe follows, with high-end clinics in Switzerland and the UK, a large supplement market, and strong public research in aging biology.'),
       apac=(22, 'Asia-Pacific grows with Japan, an aging country that funds research, and Singapore, a hub for studies on healthy aging.'),
       latam=(3, 'Latin America is small, with a few clinics in Mexico and Brazil that mostly serve wealthy local and foreign patients.'),
       mea=(6, 'The Gulf countries invest in longevity research and premium clinics, often with large public budgets and foreign partners.'))),
]
slides = []
for img, big, mk, ico, text, regs in M:
    slides.append(dict(type='cover', image=f'media/{img}', big=big, disclaimer=DISC))
    lab = mk.upper() + (' market' if 'market' not in mk else '')
    d = copy.deepcopy(S[2]); d['label'] = lab; d['title'] = f'What is the {mk} market,\nin simple terms?'; d['text'] = text; d['icon_tl'] = ico; slides.append(d)
    w = copy.deepcopy(S[11]); w['label'] = lab; w['title'] = f'Where in the world is\n{mk} money spent?'; w.pop('widths', None)
    w['regions'] = {k: dict(pct=p, text=t) for k, (p, t) in regs.items()}
    w['note'] = ['Example layout: the shares and texts on this map are illustrative, not research results']
    slides.append(w)
deck = dict(keep_together=['nuclear fusion', 'wearable tech', 'AI voice agents'], market='Examples', label='Layout examples', quarter='Q3 2026', year=2026, slug='examples', chapters=[], slides=slides)
(ROOT / 'decks/examples/deck.yaml').write_text(yaml.dump(deck, allow_unicode=True, sort_keys=False, width=1000))
print(len(slides))
