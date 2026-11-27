import yaml, re, glob
D='/home/claude/nmp-decks/decks/deepfake-detection/'
P=D+'extras.yaml'
X=[x for x in (yaml.safe_load(open(P)) or []) if x['slide'].get('id')=='pp_s06']
txt=open(glob.glob(D+'research/*11-signals*')[0]).read()
C={}
for m in re.finditer(r'### (\d+)\. .*?\n```yaml\n(.*?)```',txt,re.S): C[int(m.group(1))]=yaml.safe_load(m.group(2))
def S(n,keys=None): return [{k:str(v) for k,v in s.items()} for s in C[n]['sources'] if not keys or any(k in s['claim'] for k in keys)]
def src(c,u,d,q): return {'claim':c,'url':u,'date':d,'quote':q}
L='../../assets/logos/'
SIG=dict(pill='SIGNAL',section='Market opportunity')
new=[
 dict(after='ed032',link='ed032, signal 1 of the list',slide=dict(id='xs_pindrop',type='x/sig_key_trend',**SIG,fresh={'period':'month','end':'2026-06'},
  title='AI-driven attacks seen by Pindrop rose\n1,680% from late 2024 to mid-2026',
  t={9:'100',10:'Q4 2024',12:'1,780',13:'JUN 2026',15:'×17.8',16:'WHY IT IS HOT',17:'Attacks with AI voices and faces on companies grow faster than any other threat Pindrop tracks, so buyers need detection now, a sign of a hot market.\n\n\nThe index sets the end of 2024 at 100. It counts attacks Pindrop sees, not all attacks.'},
  vbars=[100,1780],note='We set Pindrop’s level of AI-driven attacks in Q4 2024 at 100 and applied the 1,680% rise it reported through June 2026'),sources=S(1)),
 dict(after='xs_pindrop',link='ed032, signal 2 of the list',slide=dict(id='xs_gap',type='kpis',**SIG,fresh={'period':'total','end':'2026-09'},
  title='93% of security leaders fear deepfakes,\nbut only 10% use a detection tool',
  items=[dict(value='93%',label='Security leaders who worry their company is not ready for deepfake attacks'),
         dict(value='~74%',label='Leaders who saw or suspect a deepfake attack on their company in the past year'),
         dict(value='10%',label='Leaders whose company already uses a tool built to detect deepfakes')],
  why='This is a sign of a hot market because almost every leader worries and very few have bought, so most of the demand is still unserved. Pindrop sells such tools.',
  note='We used Pindrop’s Deepfake Readiness Index of September 2026. “nearly three-quarters” is read as about 74%'),sources=S(2)),
 dict(after='xs_gap',link='ed032, signal 3 of the list',slide=dict(id='xs_deals',type='sx_league',**SIG,fresh={'period':'total','end':'2026-09'},big='4',h0='BUYER AND TARGET',h1='NO.',h2='WHEN',kicker='WHY IT IS HOT',
  title='Identity, telecom, HR and audit groups\nkeep buying into deepfake detection',
  rows=[dict(n=1,name='Entrust + Onfido',src=L+'entrust.png',v='Apr 2024',what='Selfie and ID checks, $650M'),
        dict(n=2,name='Hiya + Loccus.ai',src=L+'hiya.png',v='Jul 2024',what='Voice deepfake detection'),
        dict(n=3,name='Deel + Clarity',src=L+'deel.png',v='Aug 2026',what='Fake candidates, up to $50M'),
        dict(n=4,name='KPMG + Reality Defender',src=L+'reality-defender.png',v='Sep 2026',what='Minority stake')],
  story='Large groups now pay to own or back detection, from identity checks to hiring, a sign of a hot market. Prices are reported figures, and most deals were not priced.',
  note=['We listed four deals announced from April 2024 to September 2026, from releases and the press','The Onfido and Clarity prices are reported estimates, not official figures from the companies']),sources=S(4,['Entrust completed','Entrust bought','Hiya','Deel','KPMG'])),
 dict(after='xs_deals',link='ed032, signal 4 of the list',slide=dict(id='xs_laws',type='x/sig_key_trend',**SIG,fresh={'period':'total','end':'2026-08'},
  title='48 US states now have laws on sexual\ndeepfakes, up from 29 in mid-2024',
  t={9:'29',10:'JUN 2024',12:'48',13:'AUG 2026',15:'×1.7',16:'WHY IT IS HOT',17:'New laws push platforms to find and remove fake intimate images fast, so they buy screening tools now, a sign of a hot market.\n\n\nThe federal TAKE IT DOWN Act adds a 48-hour removal duty, enforced by the FTC since May 2026.'},
  vbars=[29,48],note='We used Ballotpedia’s counts of US states with laws on sexually explicit deepfakes, from June 2024 to August 2026'),sources=S(6)),
 dict(after='xs_laws',link='ed032, signal 5 of the list',slide=dict(id='xs_entrust',type='sx_stat_strip',**SIG,fresh={'period':'year','end':'2026-09'},
  title='Deepfake attacks on identity checks\ngrew 2,200% in the Americas in a year',headline='Yearly growth of deepfake attacks seen by Entrust in 2026',
  stats=[dict(v='+2,200%',l='Americas, the largest buyer market for identity tools'),dict(v='+165%',l='Worldwide, across the 195 countries Entrust covers'),dict(v='94%',l='Share of deepfakes seen that targeted finance firms')],
  story='Fraudsters aim fake faces at banks first, which is why banks are the main buyers of detection, a sign of a hot market. These are Entrust’s own checks, not all attacks.',
  note=['We used Entrust’s 2027 Identity Fraud Report, published in November 2026,','on identity checks it processed from September 2025 to September 2026']),sources=S(8)),
 dict(after='xs_entrust',link='ed032, signal 6 of the list',slide=dict(id='xs_doppel',type='x/sig_announced_vs_built',**SIG,fresh={'period':'total','end':'2025-11'},
  title='Doppel’s value rose from $205M to more\nthan $600M in about six months',
  t={8:'205',9:'$M valuation at\nSeries B, May 2025',11:'600',12:'$M+ valuation at\nSeries C, Nov 2025',15:'×2.9',16:'WHY IT IS HOT',17:'Investors paid about three times more for Doppel, which tracks fake profiles and impersonation across channels, within six months, a sign of a hot market.\n\n\nA valuation is a price paid by a few investors in one round, not revenue or a proven market value.'},
  vbars=[205,600],note='We used Doppel’s Series B release of May 2025 and Fortune’s report on its $70M Series C of November 2025'),
  sources=[src('$35M Series B at $205M valuation led by Bessemer','https://www.businesswire.com/news/home/20250502542037/en','2025-05-02','The Series B round of $35 million at $205 million valuation is led by Bessemer Venture Partners'),
           src('Doppel raised $70M at more than $600M valuation','https://fortune.com/2025/11/19/exclusive-doppel-raises-70-million-series-c-at-more-than-600-million-valuation-to-fight-ai-powered-social-engineering-attacks','2025-11-19','Exclusive: Doppel raises $70 million Series C at more than $600 million valuation to fight AI-powered social engineering attacks')]),
 dict(after='xs_doppel',link='ed032, signal 7 of the list',slide=dict(id='xs_modulate',type='kpis',**SIG,fresh={'period':'total','end':'2026-09'},
  title='Modulate checks more than 10M hours\nof audio a month for fake voices',
  items=[dict(value='10M+',label='Hours of audio Modulate analyzes each month for fake voices'),
         dict(value='600M+',label='Hours of audio it has analyzed in total since it was founded'),
         dict(value='$25M',label='New round raised in September 2026, for $60M raised in total')],
  why='This is a sign of a hot market because voice checks now run at the scale of whole platforms, and investors fund more of it. Hours analyzed are not hours of fakes found.',
  note='We used SecurityWeek and ID Tech Wire reports of September 28, 2026 on Modulate’s round and the volume of audio it analyzes'),
  sources=[src('Modulate analyzes 10 million hours of audio monthly','https://www.securityweek.com/modulate-raises-25-million-to-advance-deepfake-detection/','2026-09-28','The firm currently analyzes more than 10 million hours of audio each month, with over 600 million hours analyzed in total.'),
           src('Modulate raised $25M, total $60M','https://idtechwire.com/modulate-raises-25-million-to-expand-audio-ai-and-fraud-detection/','2026-09-28','Future Ventures led the financing, with participation from Hyperplane and Lakestar, bringing the company’s total funding to $60 million.')]),
 dict(after='pp_s06',link='pp_s06, the business models, and ed104 BUILT-IN PLACEMENT',slide=dict(id='xv_margins',type='sx_stat_strip',section='Value creation',
  title='authID lost $8.95 per dollar of sales\nwhile Mitek earned 5 cents',headline='Net profit or loss per $1 of revenue, full year 2025',
  stats=[dict(v='−$8.95',l='authID, a small listed seller of face checks with deepfake defense'),dict(v='−$2.25',l='Cyabra, a small listed firm that tracks fake profiles and false stories'),dict(v='+$0.05',l='Mitek, an older identity firm with $179.7M of revenue in its fiscal 2025')],
  story='Small detection sellers still spend far more than they sell, while a large identity firm earns a thin margin. Scale and a place in buyers’ tools decide who survives.',
  note=['We divided each company’s 2025 net result by its 2025 revenue, from filings and releases.','Mitek’s fiscal year ended in September 2025. None of the three is a startup today']),sources=S(7)),
 dict(after='ed064-s3',link='ed064-s3, AI images flooding child safety reports',slide=dict(id='xc_ncmec',type='kpis',section='Pain points',
  title='AI-linked child abuse reports to NCMEC\nrose from 4,700 to more than 400,000',
  items=[dict(value='4,700',label='Reports linked to generative AI received by NCMEC in all of 2023'),
         dict(value='67,000',label='Reports linked to generative AI received in 2024, 14 times more'),
         dict(value='400,000+',label='Reports in 2025 that NCMEC could act on, out of 1.5M in total')],
  why='Child safety teams now face a flood of AI-made images that people cannot review one by one, the core need behind platform screening tools.',
  note='We used NCMEC’s counts for 2023 to 2025. Of the 1.5M reports of 2025, 1.1M came from Amazon AI Services with no actionable information'),sources=S(5)),
]
yaml.safe_dump(X+new,open(P,'w'),allow_unicode=True,sort_keys=False,width=1000)
print(len(X+new))
