"""S02 public-signal curves (markets 131-225), Claude's own pilot research of 11 Nov 2026. usage: python3 mksig.py <slug>"""
import os, re, sys, csv, yaml
sys.path.insert(0, os.path.dirname(__file__))
from mkpp import SRC, ROOT, two
MK = {r['handle']: r for r in csv.DictReader(open('/root/w/nmp_slide_kit/markets_225.csv'))}
def label(h): return ' '.join(''.join(w.split()) for w in re.split(r'\s{2,}', MK[h]['market_name_for_slide'].strip()))
# handle, title, note, points, xs (time position), label format, last-point lines, big multiple, unit, 3 facts, forecast points
CUR = [
 ('optical-interconnect', "Innolight now sells four times more optical modules than two years ago",
  "We used the quarterly revenue that Innolight, the largest maker of optical modules for AI data centers, reports in its filings, converted at 7.1 yuan per US dollar.",
  [['Q3 24', 0.92], ['Q4 24', 0.92], ['Q1 25', 0.94], ['Q2 25', 1.14], ['Q3 25', 1.44], ['Q4 25', 1.86], ['Q1 26', 2.75], ['Q2 26', 3.14], ['Q3 26', 3.91]], None, '$%.1fB',
  ['sold by Innolight', 'in Q3 2026'], '4.3x', ' in 2 years',
  ['Innolight sold $3.9B of optical modules in the third quarter of 2026, up 172% in a year.', 'It holds about a fifth of the world market for optical modules.', 'Its order book already ran through the end of 2026 in April.'], 0),
 ('ev-charging-infrastructure', "China's EV chargers doubled in less than two years",
  "We used the number of EV charging points in China published by the National Energy Administration and the charging alliance EVCIPA, at the end of each period.",
  [['Dec 22', 5.21], ['Dec 23', 8.60], ['Dec 24', 12.82], ['Sep 25', 18.06], ['Mar 26', 21.48], ['Sep 26', 24.78]], [0, 12, 24, 33, 39, 45], '%.1fM',
  ['charging points', 'in China, Sep 2026'], '4.8x', ' since 2022',
  ['China had 24.8 million EV charging points at the end of September 2026, up 37% in a year.', 'Home chargers grow fastest, up 44% in a year.', 'Beijing targets 28 million charging points by the end of 2027.'], 0),
 ('sustainable-aviation-fuel', "Sustainable jet fuel output has grown almost ten times since 2022",
  "We used the yearly sustainable aviation fuel production estimated by IATA, the global airline association. The 2026 point is its own estimate for the year.",
  [['2021', 0.08], ['2022', 0.25], ['2023', 0.5], ['2024', 1.0], ['2025', 1.9], ['2026', 2.4]], None, '%.1fMt',
  ['of sustainable jet fuel', 'expected in 2026'], '9.6x', ' since 2022',
  ['IATA expects 2.4 million tonnes of sustainable jet fuel in 2026.', 'Output almost doubled in 2025 alone.', 'It still covers only 0.8% of the jet fuel airlines burn.'], 1),
 ('autonomous-trucking', ["Half a million miles, and nobody", "at the wheel of Aurora's trucks"],
  "We used the total driverless miles Aurora reports in its quarterly letters and announcements, counted since its commercial launch in Texas in spring 2025.",
  [['Apr 25', 0], ['Oct 25', 100], ['Jan 26', 250], ['Apr 26', 370], ['Sep 26', 500]], [0, 6, 9, 12, 17], '%dK',
  ['driverless miles', 'by Sep 2026'], '5x', ' in a year',
  ['Aurora passed 500,000 driverless miles in September 2026, with no crash caused by its system.', 'Its driverless customers rose from 7 to 10 during 2026.', 'It now plans 200 driverless trucks by February 2027.'], 0),
]
LABS = {'sustainable-aviation-fuel': ['0.08Mt', '0.25Mt', '0.5Mt', '1.0Mt', '1.9Mt', '2.4Mt'], 'autonomous-trucking': ['0', '100K', '250K', '370K', '500K']}
out = []
for h, title, note, pts, xs, fmt, ll, big, unit, paras, fc in CUR:
    s = dict(label=label(h), type='pp_curve', section='Market opportunity', title=two(title), note=note + SRC, points=pts, labs=LABS.get(h) or [fmt % v for _, v in pts], forecast=fc, zero=True,
             lastlines=ll, big=big, unit=unit, paras=paras)
    if xs: s['xs'] = [x / xs[-1] for x in xs]
    out.append(s)
slug = sys.argv[1]; os.makedirs(f'{ROOT}/decks/{slug}', exist_ok=True)
yaml.safe_dump(dict(market='Product page slides', quarter='signals pilot', label='', slides=out), open(f'{ROOT}/decks/{slug}/deck.yaml', 'w'), sort_keys=False, allow_unicode=True, width=200)
print(len(out), 'slides')
