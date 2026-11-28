import yaml, re, glob
D='/home/claude/nmp-decks/decks/edtech/'
P=D+'extras.yaml'
X=[x for x in (yaml.safe_load(open(P)) or []) if x['slide'].get('id')=='pp_s06']
for x in X: x['link']='ed104 DAILY HABITS, products that turn free use into paid subscriptions, and how each model gets paid'
txt=open(glob.glob(D+'research/*11-signals*')[0]).read()
C={}
for m in re.finditer(r'## (\d+)\. .*?\n```yaml\n(.*?)```',txt,re.S): C[int(m.group(1))]=yaml.safe_load(m.group(2))
def S(n,keys=None): return [{k:str(v) for k,v in s.items()} for s in C[n]['sources'] if not keys or any(k in s['claim'] for k in keys)]
def src(c,u,d,q): return {'claim':c,'url':u,'date':d,'quote':q}
SIG=dict(pill='SIGNAL',section='Market opportunity')
PR=[src('Preply Series D and valuation','https://preply.com/en/blog/preply-raises-150-million-to-shape-the-future-of-education-through-human-led-ai-enhanced-learning/','2026-01-21','Led by WestCap, the Series D Round Values the Company at $1.2 Billion'),
    src('Preply became EBITDA positive','https://preply.com/en/blog/preply-raises-150-million-to-shape-the-future-of-education-through-human-led-ai-enhanced-learning/','2026-01-21','In the last twelve months the company continued improving EBITDA and became EBITDA positive.'),
    src('Preply tutors and countries','https://www.techstars.com/blog/startup-spotlight/preply-redefines-learning-and-becomes-a-unicorn','2026-01-23',"Preply's platform connects more than 100,000 tutors with learners in 180 countries")]
LO=[src('Loora raised $22M','https://www.loora.com/news/company-news/loora-raises-22m-funding','2026-09-16','Loora Raises $22M to Advance AI-Powered English Learning'),
    src('Loora recurring revenue','https://www.calcalistech.com/ctechnews/article/byr9ag00yze','2026-09-16','its annual recurring revenue reached tens of millions of dollars.'),
    src('Loora B2B users','https://www.loora.com/news/company-news/loora-raises-22m-funding','2026-09-16','More than 100 corporations, governments and universities are also now using the B2B product we built over the last year.')]
CH=S(4)+[src('Chegg academic revenue fell on fewer subscribers','https://www.sec.gov/Archives/edgar/data/1364954/000143774926034534/chgg20260930c_10q.htm','2026-11','The decrease was primarily due to a decrease in subscription revenue, primarily related to reduced traffic which led to fewer subscribers.')]
new=[
 dict(after='ed032',link='ed032, signal 1 of the list',slide=dict(id='xe_genai',type='x/sig_key_trend',**SIG,fresh={'period':'year','end':'2026-09'},
  title='GenAI course enrollments passed\n45 a minute on Coursera and Udemy',
  t={9:'25',10:'2025',12:'45+',13:'2026',15:'×1.8',16:'WHY IT IS HOT',17:'People sign up for AI courses almost twice as fast as a year ago, a sign of a hot market for practical skills training.\n\n\nThe figures count enrollments per minute, not unique learners or purchases.'},
  vbars=[25,45],note='We used the Coursera Global Skills Report of September 28, 2026, for Coursera and Udemy combined. The 2026 rate is a lower bound'),sources=S(1)),
 dict(after='xe_genai',link='ed032, signal 2 of the list',slide=dict(id='xe_dau',type='x/sig_key_trend',**SIG,fresh={'period':'quarter','end':'2026-09'},
  title='Duolingo reached 64.9M daily learners,\nnearly three times its 2023 level',
  t={9:'24.2',10:'Q3 2023',12:'64.9',13:'Q3 2026',15:'×2.7',16:'WHY IT IS HOT',17:'A learning app now draws a daily crowd the size of a big consumer app, and it still grew 29% in the last year, a sign of a hot market.\n\n\nThe bars show average daily active users in millions, for the same quarter of each year.'},
  vbars=[24.2,64.9],note='We used Duolingo shareholder letters and its 10-Q for the third quarters of 2023 and 2026, filed with the SEC'),sources=S(2)),
 dict(after='xe_dau',link='ed032, signal 3 of the list',slide=dict(id='xe_preply',type='kpis',**SIG,fresh={'period':'total','end':'2026-01'},
  title='Preply raised $150M at a $1.2B value\nafter it turned a profit',
  items=[dict(value='$150M',label='Series D led by WestCap in January 2026, for human tutoring with AI'),
         dict(value='$1.2B',label='Value of Preply after the round, which made it a new EdTech unicorn'),
         dict(value='100K+',label='Tutors on its marketplace, who teach learners in 180 different countries')],
  why='This is a sign of a hot market because investors paid a unicorn price for a tutoring firm that was already EBITDA positive, far from the cash burn of 2021.',
  note='We used the Preply release of January 21, 2026, and a Techstars profile of January 23, 2026'),sources=PR),
 dict(after='xe_preply',link='ed032, signal 4 of the list',slide=dict(id='xe_deals',type='sx_stat_strip',**SIG,fresh={'period':'total','end':'2026-10'},
  title='EdTech deals passed a ten-year record\nby August 2026',headline='Mergers and acquisitions in EdTech, January to October 2026',
  stats=[dict(v='149',l='EdTech deals through August 2026, above the ten-year yearly record'),dict(v='$674M',l='Value Coursera paid for Udemy when the merger closed in May'),dict(v='4',l='AI teaching tools bought by McGraw Hill, Pearson and IXL in 2 months')],
  story='Big education groups now pay for AI tools and platforms, a sign of a hot market. Teachally, TeachFX, Workera and NoRedInk were all bought from September to October 2026.',
  note=['We used the Corum Group report of October 2026, Coursera’s 10-Q, and the releases','of McGraw Hill, Pearson and IXL. Pearson had agreed to buy Workera, not yet closed']),sources=S(5)),
 dict(after='xe_deals',link='ed032, signal 5 of the list',slide=dict(id='xe_pw',type='kpis',**SIG,fresh={'period':'half','end':'2026-09'},
  title='PhysicsWallah grew far beyond\nexam prep in the last six months',
  items=[dict(value='+130%',label='Enrollments in school board and CUET courses, April to September 2026'),
         dict(value='+77%',label='Enrollments in courses taught in Indian languages other than English'),
         dict(value='+75%',label='Revenue growth of its online courses for school students, year on year')],
  why='This is a sign of a hot market because India’s biggest test prep player now finds fast demand in school courses and in local languages too.',
  note='We used the PhysicsWallah earnings release of November 4, 2026, to India’s stock exchange. The three figures are not additive'),sources=S(6)),
 dict(after='xe_pw',link='ed032, signal 6 of the list',slide=dict(id='xe_noredink',type='share_waffle',**SIG,fresh={'period':'total','end':'2026-10'},
  title='NoRedInk was used by 9 in 10\nUS school districts before IXL bought it',
  on='Districts reached',off='Not reached',unit='districts',years=[dict(x='OCTOBER 2026',k=90,n=100,p=90)],big='90%',kicker='WHY IT IS HOT',
  story='A small writing app reached almost every US school district, and a larger group bought it for that reach, a sign of a hot market.\nThe share counts districts that used it since its launch, not paid ones.',
  note=['We used the IXL Learning release of October 19, 2026, on its purchase of NoRedInk','The figure counts districts reached since inception, not current paid subscriptions']),sources=S(9)),
 dict(after='xe_noredink',link='ed032, signal 7 of the list',slide=dict(id='xe_loora',type='sx_stat_strip',**SIG,fresh={'period':'total','end':'2026-09'},
  title='Loora raised $22M as its AI English\ntutor passed tens of millions in sales',headline='Loora, an AI English tutor, as of September 2026',
  stats=[dict(v='$22M',l='New funding raised in September 2026 to grow its AI tutor'),dict(v='$10M+',l='Recurring revenue a year, reported in the tens of millions'),dict(v='100+',l='Companies, governments and universities using its B2B product')],
  story='People and employers now pay for AI language tutors at scale, a sign of a hot market. Loora built its business product only over the last year.',
  note=['We used the Loora release and the Calcalist article of September 16, 2026','The $10M+ is a floor for “tens of millions of dollars” of recurring revenue']),sources=LO),
 dict(after='ed136',link='ed136, high sign-up counts can hide low classroom engagement',slide=dict(id='xe_khanmigo',type='share_waffle',section='Market challenges',
  title='Students asked Khanmigo for help in\nonly 17% of sessions with a mistake',
  on='Asked the tutor',off='Did not ask',unit='sessions',years=[dict(x='2026 STUDY',k=17,n=100,p=17)],big='17%',kicker='WHAT IS GOING ON',
  story='Even with an AI tutor one click away, students who got stuck rarely asked it for help.\nA tutor that waits for questions leaves most of its value unused, so products must step in on their own.',
  note=['We used the NBER working paper of August 2026 on a two-year trial in 18 Tennessee','middle schools. The share counts exercise sessions with a mistake, not students']),sources=S(3)),
 dict(after='ed200',link='ed200 AI RIVALS, they fail when free AI tools replace paid study help',slide=dict(id='xe_chegg',type='sx_faceoff',section='Startup killers',
  title='Chegg fell from $113.51 a share\nto $0.52 as students turned to AI',
  cards=[dict(name='Nov 2026',hl=True,stats=[dict(v='$0.52',l='closing price on November 27, 2026'),dict(v='−99.5%',l='fall from its all-time closing high')]),
         dict(name='Feb 2021',stats=[dict(v='$113.51',l='all-time closing high, February 12, 2021'),dict(v='Peak',l='at the height of pandemic homework help')])],
  story='Paid homework help lost almost all its value once free AI tools could answer the same questions. Chegg’s academic revenue keeps falling with its subscribers.',
  note=['We compared the adjusted closing prices from Macrotrends and Stock Analysis','The fall is 1 minus 0.52 divided by 113.51, which is our own arithmetic here']),sources=CH),
 dict(after='pp_s06',link='pp_s06, monthly subscriptions and degrees, the two ends of the money map',slide=dict(id='xe_multiple',type='sx_faceoff',section='Value creation',
  title='Investors value $1 of Duolingo sales\nat seven times $1 of Coursera sales',
  cards=[dict(name='Duolingo',hl=True,stats=[dict(v='6.1x',l='market value to trailing sales, November 2026'),dict(v='$7.2B',l='market value, for about $1.2B of sales')]),
         dict(name='Coursera',stats=[dict(v='0.9x',l='market value to trailing sales, November 2026'),dict(v='$914M',l='market value, for about $1.1B of sales')])],
  story='Two firms with similar sales get very different prices. Investors pay for daily habits and paid subscriptions far more than for course catalogs that must win each learner again.',
  note=['We used Stock Analysis snapshots of November 24 and 25, 2026. Coursera’s sales','include Udemy only from May 2026, and the 7 times is our own arithmetic']),sources=S(8)),
]
yaml.safe_dump(X+new,open(P,'w'),allow_unicode=True,sort_keys=False,width=1000)
print(len(X+new))
