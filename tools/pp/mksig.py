"""S02 public-signal curves (markets 131-225), Claude's own pilot research of 11 Nov 2026. usage: python3 mksig.py <slug>"""
import os, re, sys, csv, yaml
sys.path.insert(0, os.path.dirname(__file__))
from mkpp import SRC, ROOT, two, balance_note
MK = {r['handle']: r for r in csv.DictReader(open('/root/w/nmp_slide_kit/markets_225.csv'))}
def label(h): return ' '.join(''.join(w.split()) for w in re.split(r'\s{2,}', MK[h]['market_name_for_slide'].strip()))
# handle, title, note, points, xs (time position), label format, last-point lines, big multiple, unit, 3 facts, forecast points
CUR = [
 ('optical-interconnect', "Innolight now sells four times more optical modules than two years ago",
  "We used the quarterly revenue that Innolight reports in its stock market filings. We converted it at 7.1 yuan per US dollar.",
  [['Q3 24', 0.92], ['Q4 24', 0.92], ['Q1 25', 0.94], ['Q2 25', 1.14], ['Q3 25', 1.44], ['Q4 25', 1.86], ['Q1 26', 2.75], ['Q2 26', 3.14], ['Q3 26', 3.91]], None, '$%.1fB',
  ['sold by Innolight', 'in Q3 2026'], '4.3x', ' in 2 years',
  ['Innolight sold $3.9B of optical modules in the third quarter of 2026, up 172% in a year.', 'It holds about a fifth of the world market for optical modules.', 'Its order book already ran through the end of 2026 in April.'], 0),
 ('ev-charging-infrastructure', "China's EV chargers doubled in less than two years",
  "We used the total number of EV charging points in China, public and private, at the end of each period. We took it from the National Energy Administration.",
  [['Dec 22', 5.21], ['Dec 23', 8.60], ['Dec 24', 12.82], ['Sep 25', 18.06], ['Mar 26', 21.48], ['Sep 26', 24.78]], [0, 12, 24, 33, 39, 45], '%.1fM',
  ['charging points', 'in China, Sep 2026'], '4.8x', ' since 2022',
  ['China had 24.8 million EV charging points at the end of September 2026, up 37% in a year.', 'Home chargers grow fastest, up 44% in a year.', 'Beijing targets 28 million charging points by the end of 2027.'], 0),
 ('sustainable-aviation-fuel', "Sustainable jet fuel output has grown almost ten times since 2022",
  "We used the yearly sustainable aviation fuel production estimated by IATA. The 2026 point is its own estimate.",
  [['2021', 0.08], ['2022', 0.25], ['2023', 0.5], ['2024', 1.0], ['2025', 1.9], ['2026', 2.4]], None, '%.1fMt',
  ['of sustainable jet fuel', 'expected in 2026'], '9.6x', ' since 2022',
  ['IATA expects 2.4 million tonnes of sustainable jet fuel in 2026.', 'Output almost doubled in 2025 alone.', 'It still covers only 0.8% of the jet fuel airlines burn.'], 1),
 ('autonomous-trucking', ["Half a million miles, and nobody", "at the wheel of Aurora's trucks"],
  "We used the total driverless miles Aurora reports since its launch in spring 2025. We took them from its quarterly letters.",
  [['Apr 25', 0], ['Oct 25', 100], ['Jan 26', 250], ['Apr 26', 370], ['Sep 26', 500]], [0, 6, 9, 12, 17], '%dK',
  ['driverless miles', 'by Sep 2026'], '5x', ' in a year',
  ['Aurora passed 500,000 driverless miles in September 2026, with no crash caused by its system.', 'Its driverless customers rose from 7 to 10 during 2026.', 'It now plans 200 driverless trucks by February 2027.'], 0),
 ('maritime-decarbonization', "Ships running on LNG have more than doubled since 2022",
  "We used the number of ships running on LNG around the world, not counting the LNG carriers themselves. We took it from the DNV Alternative Fuels Insight platform.",
  [['Dec 22', 355], ['Dec 23', 469], ['Dec 24', 641], ['Jun 26', 914]], [0, 12, 24, 42], '%d',
  ['ships running on LNG', 'in June 2026'], '2.6x', ' since 2022',
  ['914 ships ran on LNG in June 2026, against 355 at the end of 2022.', '61 more joined the fleet in the first half of 2026.', 'Another 654 LNG-fuelled ships are on order.'], 0),
]
def N2(note):
    """Workshop rule: 2 lines, one idea per line, no dots. Second sentence (if any) joins the sources line."""
    p = [x.strip().rstrip('.') for x in note.split('. ') if x.strip()]
    if len(p) == 1: return [p[0], 'We checked each point against its source, and all the sources are included at the end of the report']
    return [p[0], p[1][0].upper() + p[1][1:] + ', and all the sources are included at the end of the report']

LABS = {'sustainable-aviation-fuel': ['0.08Mt', '0.25Mt', '0.5Mt', '1.0Mt', '1.9Mt', '2.4Mt'], 'autonomous-trucking': ['0', '100K', '250K', '370K', '500K']}
out = []
for h, title, note, pts, xs, fmt, ll, big, unit, paras, fc in CUR:
    s = dict(label=label(h), type='pp_curve', section='Market opportunity', title=two(title), note=N2(note), points=pts, labs=LABS.get(h) or [fmt % v for _, v in pts], forecast=fc, zero=True,
             lastlines=ll, big=big, unit=unit, paras=paras)
    if xs: s['xs'] = [x / xs[-1] for x in xs]
    out.append(s)
for s in out: s['note'] = balance_note(s['note'])
slug = sys.argv[1]; os.makedirs(f'{ROOT}/decks/{slug}', exist_ok=True)
yaml.safe_dump(dict(market='Product page slides', quarter='signals pilot', label='', slides=out), open(f'{ROOT}/decks/{slug}/deck.yaml', 'w'), sort_keys=False, allow_unicode=True, width=200)
print(len(out), 'slides')
