import yaml, re, glob
D='/home/claude/nmp-decks/decks/ai-powered-market-research/'
P=D+'extras.yaml'
X=[x for x in (yaml.safe_load(open(P)) or []) if x['slide'].get('id')=='pp_s06']
# sources of each candidate, read from the signals research file (claims, urls, dates and quotes as delivered)
txt=open(glob.glob(D+'research/*11-signals*')[0]).read()
C={}
for m in re.finditer(r'### (\d+)\. .*?\n```yaml\n(.*?)```',txt,re.S): C[int(m.group(1))]=yaml.safe_load(m.group(2))
def S(n): return [{k:str(v) for k,v in s.items()} for s in C[n]['sources']]
SIG=dict(pill='SIGNAL',section='Market opportunity')
new=[
 dict(after='ed032',link='ed032, signal 1 of the list',slide=dict(id='xs_listen',type='kpis',**SIG,fresh={'period':'total','end':'2026-09'},
  title='Listen Labs grew revenue 15x and\ninterviewed 1M people in nine months',
  items=[dict(value='15x',label='Growth of Listen Labs’ annualized revenue in the nine months after its launch'),
         dict(value='1M+',label='People interviewed by its AI moderator in those same nine months'),
         dict(value='50M+',label='People in the global panel its AI agents can draw on, in 120+ languages')],
  why='This is a sign of a hot market because an AI interview startup reached this scale in months, then Salesforce bought it. The panel counts people who can be asked, not interviews.',
  note='We used Listen Labs’ release of January 14, 2026 and Salesforce’s release of September 29, 2026. Salesforce closed the deal on November 2, 2026'),sources=S(1)),
 dict(after='xs_listen',link='ed032, signal 2 of the list',slide=dict(id='xs_strella',type='kpis',**SIG,fresh={'period':'half','end':'2026-04'},
  title='Strella reached $1.6M of recurring revenue\nin its first year, with 150% retention',
  items=[dict(value='$1.6M',label='Annual recurring revenue of Strella in its first year of selling'),
         dict(value='150%',label='Revenue kept and grown from its first clients when they renewed'),
         dict(value='8M',label='People in the global panel that Strella’s AI interviews can reach')],
  why='This is a sign of a hot market because clients spent half as much again when they renewed. These are company figures reported by Bessemer, an investor in Strella.',
  note='We used Bessemer’s case study of April 21, 2026. Retention of 150% means renewing clients spent 1.5 times what they spent the year before'),sources=S(2)),
 dict(after='xs_strella',link='ed032, signal 3 of the list',slide=dict(id='xs_synth',type='x/sig_key_trend',**SIG,fresh={'period':'quarter','end':'2026-03'},
  title='Synthetic data use at the largest research\nsuppliers jumped from 26% to 44% in a year',
  t={9:'26%',10:'2025',12:'44%',13:'2026',15:'×1.7',16:'WHY IT IS HOT',17:'The biggest research suppliers now use synthetic answers in their daily work, a market for synthetic respondent startups, a sign of a hot market.\n\n\nThe survey counts firms that use it, not the share of their revenue or of their studies.'},
  vbars=[26,44],note='We used Greenbook’s GRIT reports of 2025 and 2026 for service-led suppliers with more than 500 staff, surveyed in early 2026'),sources=S(3)),
 dict(after='xs_synth',link='ed032, signal 4 of the list',slide=dict(id='xs_aiqual',type='x/sig_key_trend',**SIG,fresh={'period':'quarter','end':'2026-03'},
  title='AI-moderated interviews at mid-sized firms\nrose from 25% to 45% in a year',
  t={9:'25%',10:'2025',12:'45%',13:'2026',15:'×1.8',16:'WHY IT IS HOT',17:'Nearly half of mid-sized research firms now let AI run their interviews, a sign of a hot market for AI interview startups.\n\n\nThe 2026 survey worded the question a little differently, so the jump is a direction, not an exact rate.'},
  vbars=[25,45],note='We used Greenbook’s GRIT reports of 2025 and 2026 for service-led research suppliers with 21 to 100 staff'),sources=S(9)),
 dict(after='xs_aiqual',link='ed032, signal 5 of the list',slide=dict(id='xs_conveo',type='x/sig_announced_vs_built',**SIG,fresh={'period':'total','end':'2026-11'},
  title='Conveo grew its team from about 20\nto 90 people during 2026',
  t={8:'20',9:'people at the\nstart of 2026',11:'90',12:'people in\nNovember 2026',15:'×4.5',16:'WHY IT IS HOT',17:'Conveo hired fast after its $50M Series A of September 2026 to serve more than 400 enterprise teams, including Fortune 500 brands, that use its AI interviews, a sign of a hot market.\n\n\nHeadcount is not revenue: it shows where the company bets, not what it already sells.'},
  vbars=[20,90],note='We used Conveo’s profile on Y Combinator, checked on November 27, 2026. The starting figure of about 20 people is approximate'),sources=S(10)),
 dict(after='xs_conveo',link='ed032, signal 6 of the list',slide=dict(id='xs_speed',type='sx_stat_strip',**SIG,fresh={'period':'total','end':'2026-07'},
  title='AI research cut a six-week study\nto two days at Duolingo',headline='Time to run a study, before and after AI research tools',
  stats=[dict(v='2 days',l='Duolingo’s video concept test with Strella, against 6+ weeks'),dict(v='8 weeks',l='A food brand’s product cycle with Aaru, against nine months before'),dict(v='3 days',l='Time Conveo says it needs to run 100 interviews with real buyers')],
  story='Studies that took weeks now take days, so brands can ask many more questions each year, a sign of a hot market. These are single client cases reported by the vendors.',
  note=['We used Bessemer’s Strella case study of April 21, 2026, an Aaru interview of July 2026','published by Goldman Sachs in November 2026, and Conveo’s media kit, checked in November']),sources=S(7)+S(6)+[s for s in S(11) if 'three days' in s['claim']]),
 dict(after='xs_speed',link='ed032, signal 7 of the list',slide=dict(id='xs_aaru',type='share_waffle',**SIG,fresh={'period':'total','end':'2026-09'},big='92%',kicker='WHY IT IS HOT',
  title='Aaru’s synthetic buyers matched real\npurchases in 92% of 340 brand pairs',
  **{'on':'Same order as real purchases','off':'Different order'},unit='brand pairs',years=[dict(k=92,n=100,p=92,x='2026')],
  story='A synthetic panel ranked brands almost like real card purchases did, the kind of proof buyers ask for, a sign of a hot market.\nAaru ran the test itself, and no one has repeated it yet.',
  note=['We used Aaru’s benchmark of September 24, 2026, on 340 pairs of brands compared','with a panel of real card purchases. One square is one pair out of 100, 92.4% rounded']),sources=S(5)),
 dict(after='iv_safety',link='iv_safety « BAD AI OUTPUT »',slide=dict(id='xc_check',type='share_waffle',section='Market challenges',big='67%',kicker='WHAT IT MEANS',
  title='Two thirds of researchers still\ndouble-check every AI output',
  **{'on':'Check every AI output','off':'Do not check every output'},unit='researchers',years=[dict(k=67,n=100,p=67,x='2026')],
  story='Researchers do not yet trust AI enough to skip a human check, so part of the time AI saves goes back into checking it.\nThe survey was run by a software vendor, so read it as a direction.',
  note=['We used Displayr’s survey of researchers of March 2026, where 135 of the','203 people answered this question. One square is one researcher out of 100']),sources=S(8)),
]
yaml.safe_dump(X+new,open(P,'w'),allow_unicode=True,sort_keys=False,width=1000)
print(len(X+new))
