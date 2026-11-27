import yaml, re, glob
D='/home/claude/nmp-decks/decks/quantum-sensing/'
P=D+'extras.yaml'
X=[x for x in (yaml.safe_load(open(P)) or []) if x['slide'].get('id')=='pp_s06']
for x in X: x['link']='ed104 SAFETY APPROVALS, records that win defense orders, and how each model gets paid'
txt=open(glob.glob(D+'research/*11-signals*')[0]).read()
C={}
for m in re.finditer(r'## (\d+)\. .*?\n```yaml\n(.*?)```',txt,re.S): C[int(m.group(1))]=yaml.safe_load(m.group(2))
def S(n,keys=None): return [{k:str(v) for k,v in s.items()} for s in C[n]['sources'] if not keys or any(k in s['claim'] for k in keys)]
def src(c,u,d,q): return {'claim':c,'url':u,'date':d,'quote':q}
L='../../assets/logos/'
SIG=dict(pill='SIGNAL',section='Market opportunity')
QC=[src('Q-CTRL raised a $290M Series C led by Salesforce Ventures and became a unicorn','https://thequantuminsider.com/2026/11/12/q-ctrl-secures-us290-million-series-c-funding-led-by-salesforce-ventures/','2026-11-12','Q-CTRL raised US$290 million in a Series C round led by Salesforce Ventures, achieving unicorn status'),
    src('Q-CTRL is valued at over $1B','https://siliconangle.com/2026/11/12/quantum-sensor-and-software-maker-q-ctrl-raises-290m-in-funding/','2026-11-12','The Australian company is now valued at over $1 billion.'),
    src('Q-CTRL raised a record $113M Series B in October 2024','https://thequantuminsider.com/2024/10/08/q-ctrl-sets-global-quantum-technology-fundraising-record-increasing-series-b-to-usd-113m-led-by-gp-bullhound/','2024-10-08','Q-CTRL Sets Global Quantum Technology Fundraising Record, Increasing Series B to USD $113M, Led by GP Bullhound')]
CQ=[src('CIQTEK market value passed 45 billion yuan on its STAR Market debut','https://eu.36kr.com/de/p/3934499685793159','2026-08-11','der Marktwert überschritt 45 Milliarden Yuan'),
    src('CIQTEK revenue of 400, 501 and 666 million yuan in 2023 to 2025','https://eu.36kr.com/en/p/3937325292174466','2026-08-13','the company achieved operating revenues of 400 million yuan, 501 million yuan and 666 million yuan respectively.')]
CE=[src('Cerca Magnetics sold 19 systems in 12 countries with over 100% annual sales growth for three years','https://thequantuminsider.com/2026/04/21/cerca-magnetics-secures-38m-series-a-funding-scale-quantum-brain-scanner/','2026-04-21','Cerca Magnetics has sold 19 systems to neuroscience centres in 12 countries with over 100 percent annual sales growth over the past three years')]
new=[
 dict(after='ed032',link='ed032, signal 1 of the list',slide=dict(id='xq_qctrl',type='kpis',**SIG,fresh={'period':'total','end':'2026-11'},
  title='Q-CTRL raised $290M in November 2026,\nat a value above $1B',
  items=[dict(value='$290M',label='Series C led by Salesforce Ventures in November 2026, for its GPS-free navigator'),
         dict(value='$1B+',label='Value of Q-CTRL after the round, the first quantum navigation unicorn'),
         dict(value='$113M',label='Its previous round, a Series B of October 2024, then a record in quantum tech')],
  why='This is a sign of a hot market because the round is more than 2.5 times the last one, two years later, and it funds sales of a product already on aircraft.',
  note='We used The Quantum Insider and SiliconANGLE of November 12, 2026, and Q-CTRL’s Series B release of October 2024'),sources=QC),
 dict(after='xq_qctrl',link='ed032, signal 2 of the list',slide=dict(id='xq_deals',type='sx_league',**SIG,fresh={'period':'total','end':'2026-07'},big='4',h0='BUYER AND TARGET',h1='NO.',h2='WHEN',kicker='WHY IT IS HOT',
  title='Thales bid $4.45B for Exail as deals\nin quantum sensing piled up',
  rows=[dict(n=1,name='IonQ + Vector Atomic',src=L+'vector-atomic.png',v='Oct 2025',what='Clocks and gravity sensors, stock deal'),
        dict(n=2,name='Infleqtion on the NYSE',src=L+'infleqtion.png',v='Feb 2026',what='SPAC listing, $550M raised'),
        dict(n=3,name='Quantum Design + Qnami',src=L+'qnami.png',v='Jun 2026',what='Diamond microscopes, price not disclosed'),
        dict(n=4,name='Thales + Exail',src=L+'exail-technologies.png',v='Jul 2026',what='Cold-atom gravimeters, $4.45B value')],
  story='Big buyers now pay for quantum sensing assets, a sign of a hot market. Exail mostly sells drones and navigation, but Thales named quantum sensors as one reason for the deal.',
  note=['We listed four deals signed or closed from October 2025 to July 2026, from releases','and Reuters. The Exail value is an enterprise value of €3.9B, closing expected in 2027']),sources=S(7)),
 dict(after='xq_deals',link='ed032, signal 3 of the list',slide=dict(id='xq_backlog',type='x/sig_key_trend',**SIG,fresh={'period':'quarter','end':'2026-09'},
  title='Infleqtion’s backlog more than doubled\nto $51M in a single quarter',
  t={9:'22.5',10:'JUN 2026',12:'51.2',13:'SEP 2026',15:'×2.3',16:'WHY IT IS HOT',17:'Signed orders for quantum sensors and clocks now arrive faster than sales, a sign of a hot market. About $36.1M of it is due in 2027.\n\n\nThe backlog counts signed contracts not yet delivered, in millions of dollars, not revenue.'},
  vbars=[22.5,51.2],note='We summed the four delivery buckets of Infleqtion’s 10-Q of June 2026 and used its Q3 2026 results for September'),sources=S(5)),
 dict(after='xq_backlog',link='ed032, signal 4 of the list',slide=dict(id='xq_spoof',type='x/sig_key_trend',**SIG,fresh={'period':'total','end':'2026-05'},
  title='Russian GPS spoofing antennas near\nKaliningrad grew from 3 to 36',
  t={9:'3',10:'EARLY 2025',12:'36',13:'MAY 2026',15:'×12',16:'WHY IT IS HOT',17:'Each antenna can feed fake positions to planes, ships and drones far into Europe, so buyers need GPS-free navigation now, a sign of a hot market.\n\n\nThe count comes from Lithuania’s telecom regulator, speaking to Reuters.'},
  vbars=[3,36],note='We used the count given by Lithuania’s communications regulator to Reuters on May 26, 2026, from early 2025 to May 2026'),sources=S(2)),
 dict(after='xq_spoof',link='ed032, signal 5 of the list',slide=dict(id='xq_pentagon',type='sx_stat_strip',**SIG,fresh={'period':'total','end':'2026-11'},
  title='The Pentagon put up to $200M behind\nquantum sensing in one program',headline='US defense money and tests for quantum sensing, 2025 to 2026',
  stats=[dict(v='$24.4M',l='DARPA awards to Q-CTRL to harden navigation sensors, August 2025'),dict(v='$200M',l='Most DIU’s Farseer program could invest in sensors and clocks, June 2026'),dict(v='4h23',l='Flight of an Embraer 170 on quantum magnetic navigation, with no GPS')],
  story='Defense buyers have moved from studies to money and real flights, a sign of a hot market. Farseer funds prototypes in 3 to 9 months, then a path to use in 2 to 3 years.',
  note=['We used DARPA, DIU, Honeywell and The Quantum Insider releases, August 2025 to November 2026','Farseer followed a June 2026 executive order on fielding new quantum sensors by the year 2028']),sources=S(12,['DARPA','Farseer','GPS-free'])),
 dict(after='xq_pentagon',link='ed032, signal 6 of the list',slide=dict(id='xq_ciqtek',type='kpis',**SIG,fresh={'period':'total','end':'2026-08'},
  title='CIQTEK passed 45 billion yuan in value\non its first day in Shanghai',
  items=[dict(value='¥45B',label='Value of CIQTEK on its first day in Shanghai, in August 2026'),
         dict(value='¥666M',label='Revenue in 2025 of this Hefei maker of quantum measuring tools'),
         dict(value='+33%',label='Growth of its revenue in 2025, from 501 million yuan in 2024')],
  why='This is a sign of a hot market because public investors in China valued a quantum sensing maker at about 68 times its sales on its first trading day.',
  note='We used 36Kr reports of August 11 and 13, 2026. The 68 times is our arithmetic, 45 billion over 666 million yuan'),sources=CQ),
 dict(after='xq_ciqtek',link='ed032, signal 7 of the list',slide=dict(id='xq_cerca',type='sx_stat_strip',**SIG,fresh={'period':'total','end':'2026-04'},
  title='Cerca Magnetics has sold 19 wearable\nbrain scanners in 12 countries',headline='Sales of Cerca’s quantum brain scanner, as of April 2026',
  stats=[dict(v='19',l='Wearable brain scanners sold to neuroscience centers'),dict(v='12',l='Countries, across North America, Europe, Asia and Australia'),dict(v='100%+',l='Yearly growth of its sales over each of the last three years')],
  story='Hospitals and labs now buy quantum brain scanners, not only test them, a sign of a hot market. The figures are Cerca’s own, given with its Series A of April 2026.',
  note=['We used The Quantum Insider of April 21, 2026, on Cerca’s £3.8M Series A','The sales growth is the company’s own figure and was not checked by an auditor']),sources=CE),
 dict(after='ed064-s1',link='ed064-s1, GPS jammed and spoofed near every conflict',slide=dict(id='xq_baltic',type='share_waffle',section='Pain points',
  title='GPS interference hit 27.4% of flights\nover the Baltic region in one month',
  on='Flights hit',off='Flights not hit',unit='flights',years=[dict(x='APRIL 2025',k=27,n=100,p=27)],big='27.4%',kicker='WHAT IS GOING ON',
  story='More than one flight in four over the Baltic region lost reliable satellite signals in a single month, and some areas passed 40%.\nFor air forces and airlines there, a GPS backup is no longer a nice-to-have.',
  note=['We used the report of Sweden, Finland, Estonia, Latvia, Lithuania and Poland','to ICAO, as reported in September 2025. The grid shows 27 of 100 flights']),sources=S(9)),
 dict(after='pp_s06',link='pp_s06, development contracts and instrument sales',slide=dict(id='xq_profit',type='sx_faceoff',section='Value creation',
  title='Infleqtion lost $3.79 per $1 of sales\nlast quarter, up from $0.92',
  cards=[dict(name='Q3 2026',hl=True,stats=[dict(v='−$3.79',l='operating loss per $1 of revenue, on $9.1M of sales'),dict(v='−12%',l='gross margin in the quarter')]),
         dict(name='Q3 2025',stats=[dict(v='−$0.92',l='operating loss per $1 of revenue, on about $7.3M'),dict(v='−$1.09',l='per $1 over the full year 2025')])],
  story='Quantum sensors still cost far more to build and deliver than they earn, even at the first listed leader. New contracts add cost before they add profit.',
  note=['We divided the GAAP operating loss by revenue, $34.5M on $9.1M in Q3 2026','and $6.7M on about $7.3M in Q3 2025, derived from the reported 25.1% growth']),sources=S(6)),
 dict(after='iv_safety',link='iv_safety FEW BUYERS, 60% of Infleqtion revenue from the US government',slide=dict(id='xq_customer',type='share_waffle',section='Market challenges',
  title='The US government paid for about 80%\nof Infleqtion’s revenue in one quarter',
  on='US government',off='Other buyers',unit='of revenue',years=[dict(x='2025',k=60,n=100,p=60),dict(x='Q2 2026',k=80,n=100,p=80)],big='80%',kicker='WHAT IS GOING ON',
  story='The first listed quantum sensing leader depends on one customer for most of its sales.\nA budget delay or a lost US program would hit its revenue far harder than at a diversified sensor maker.',
  note=['We used Infleqtion’s 10-K for 2025, about 60% plus 12% from the UK','government, and the share it gave with its Q2 2026 results, about 80%']),sources=S(4)),
]
yaml.safe_dump(X+new,open(P,'w'),allow_unicode=True,sort_keys=False,width=1000)
print(len(X+new))
