"""Exemples des autres gabarits sur un autre marché (AI voice agents). Contenu INDICATIF pour juger la mise en page :
chiffres illustratifs, cabinets anonymes (Firm A-D), aucun fait chiffré attribué à une vraie société. Chaque note le dit."""
import pathlib, yaml
ROOT = pathlib.Path(__file__).resolve().parent.parent
N = ['Example layout: the figures on this slide are illustrative, not research results']
slides = [
 dict(type='agenda', section='AI voice agents market', current=0),
 dict(type='cards', section='Market definition', title='When and where is value\ncreated in the market?', items=[
   dict(e='📞', t='When a clinic answers every call, even at night and on weekends'),
   dict(e='⏱️', t='When a customer gets an answer in seconds instead of waiting on hold'),
   dict(e='🗓️', t='When a car dealer books test drives while the team sleeps'),
   dict(e='🌍', t='When a hotel answers guests in their own language'),
   dict(e='💸', t='When a call costs a few cents instead of several dollars'),
   dict(e='📈', t='When a sales team calls back every lead within one minute'),
   dict(e='🧾', t='When a bank checks a payment issue without a human agent'),
   dict(e='🧑‍💼', t='When human agents keep only the hard and sensitive calls')]),
 dict(type='maturity', section='Market definition', title='How mature are AI voice agents\nas a market?', score=38,
   text='The market is real because many companies already let AI answer simple calls, and the cost per call drops every year. The score is not higher because most deployments are still pilots, voices still make mistakes, and buyers worry about trust and privacy.',
   note=['We rate market maturity with a simple internal score based on tech progress and disruptions',
         'The score is directional and not exact, but it stays clearer than vague labels like early']),
 dict(type='dated', section='Market definition', title='What has changed\n(very) recently?', page='1/1', items=[
   dict(d='SINCE 2022', t='Large language models made it possible to hold a natural conversation on the phone, not just follow a fixed menu of options.'),
   dict(d='SINCE 2023', t='Synthetic voices became hard to tell apart from human ones, and the delay before each answer fell below one second.'),
   dict(d='SINCE 2024', t='Startups began to sell ready-made voice agents that a small business can set up in an afternoon, without any developers.'),
   dict(d='SINCE 2024', t='Large call center firms started to test AI agents on their simplest calls, like booking, tracking, and password resets.'),
   dict(d='SINCE 2025', t='Regulators began to ask that callers be told when they speak to an AI, and some states banned AI voices in robocalls.'),
   dict(d='SINCE 2026', t='Buyers now compare voice agents on the share of calls they fully solve, not on how human the voice sounds to the caller.')],
   note=['This is an example layout: the dates and changes are broad trends, not a researched timeline',
         'A real deck would date each change from sources and keep the moments that matter most']),
 dict(type='kpis', section='Market opportunity', pill='SIGNAL', title='AI agents now answer one call\nin five at early adopters',
   why='This is a strong signal because voice was long seen as too hard for AI. Early adopters now trust it with real customers.',
   items=[dict(value='20%', label='Of calls are fully handled by AI at early adopter call centers'),
          dict(value='-60%', label='Is how much the cost of one call can fall when AI answers it'),
          dict(value='<1 s', down=True, label='Is the delay before an AI agent answers, close to a human')],
   note=N),
 dict(type='estimates', section='Market size', title='What are the market size estimates\nfrom different sources online?', rows=[
   dict(firm='Research\nfirm A', value='$ 2.4 B', comment='Their figure covers voice agents sold to companies, without the phone systems around them. We use it as our base.'),
   dict(firm='Research\nfirm B', value='$ 3.1 B', comment='Their scope adds voice tools for developers. We use it to confirm the upper end of our range.'),
   dict(firm='Research\nfirm C', value='$ 4.0 B', comment='Their figure includes chatbots that only write. We keep only the share that speaks on the phone.'),
   dict(firm='Research\nfirm D', value='$ 9.5 B', comment='Their definition is much wider and counts all conversational AI. We treat it as an upper bound only.')],
   note=['Example layout: the firms are anonymous and their figures are illustrative, not research results']),
 dict(type='compare', section='Market size', title='How does it compare\nto other markets?', rows=[
   dict(name='Podcasts', v=2), dict(name='Speech to text', v=2), dict(name='AI voice agents', v=3, hl=True),
   dict(name='Voice cloning', v=4), dict(name='Contact center software', v=6), dict(name='Chatbots', v=8), dict(name='Call center outsourcing', v=12)],
   unit='$ B', note=N),
 dict(type='catbars', section='Market size', title='What are the categories\nand how much do they generate?', cats=[
   dict(name='Customer\nservice', v=1.2), dict(name='Sales and\nbooking', v=0.7), dict(name='Healthcare\ncalls', v=0.5), dict(name='Banks and\ninsurers', v=0.4), dict(name='Other\nuses', v=0.2)],
   note=N),
 dict(type='projection', section='Market size', title='What is the projected growth\nfor the AI voice agents market?', cagr='34% CAGR',
   bars=[dict(x=y, v=v) for y, v in zip(range(2026, 2037), [3, 4, 5, 7, 9, 12, 16, 22, 29, 39, 53])],
   intro='To reach this value, voice agents must move from pilots to the main line of call centers, and solve most calls without passing them to a human.\nThey must also keep voices safe from fraud, follow new rules on disclosure, and stay cheaper than outsourced agents in low-cost countries.',
   note=N),
 dict(type='priority', section='Pain points', subtitle='Call centers', title='Which pains deserve\nattention first?', icons=['🏢', '🏥', '🏦', '🛒', '🚗'], rows=[
   dict(pain='They lose customers who hang up after long waits on hold', p='CRITICAL', s=[3, 3, 2, 3, 2]),
   dict(pain='They cannot find and keep enough trained human agents', p='HIGH', s=[3, 2, 2, 2, 1]),
   dict(pain='They pay too much for simple calls like booking and tracking', p='HIGH', s=[3, 2, 1, 3, 2]),
   dict(pain='They fear that AI says something wrong to a real customer', p='MAJOR', s=[2, 3, 3, 1, 1]),
   dict(pain='They must follow strict rules on recording and consent', p='MAJOR', s=[2, 3, 3, 1, 1]),
   dict(pain='They struggle to connect AI to their old phone systems', p='HIGH', s=[3, 2, 2, 2, 2]),
   dict(pain='They cannot answer calls at night or in other languages', p='HIGH', s=[2, 3, 1, 2, 3])],
   note=['Every customer is different, and this table is a simplified example of the layout',
         'A real deck builds it from forums, reports, and feedback, then checks it with customers']),
 dict(type='fundbars', section='Investor bets', title='How has fundraising activity\nevolved recently?', bars=[
   dict(x='Q3 2025', v=410, ann='Two late-stage rounds made up most of the quarter'),
   dict(x='Q4 2025', v=520, ann='A record quarter, led by tools for call centers'),
   dict(x='Q1 2026', v=780, ann='One large round took almost half of all capital'),
   dict(x='Q2 2026', v=350, ann='Many small seed rounds, but few large ones'),
   dict(x='Q3 2026', v=610, ann='Healthcare voice agents raised the most money')],
   note=['Example layout: the amounts and comments are illustrative, not from our tracker']),
]
ED = yaml.safe_load((ROOT / 'decks/edtech/deck.yaml').read_text())
deck = dict(market='AI voice agents', label='AI voice agents market', quarter='Q3 2026', year=2026, slug='examples2', chapters=ED['chapters'], slides=slides)
(ROOT / 'decks/examples2').mkdir(exist_ok=True)
(ROOT / 'decks/examples2/deck.yaml').write_text(yaml.dump(deck, allow_unicode=True, sort_keys=False, width=1000))
print(len(slides))
