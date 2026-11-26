import yaml
P='/home/claude/nmp-decks/decks/femtech/extras.yaml'
X=yaml.safe_load(open(P)) or []
X=[x for x in X if not str(x['slide'].get('id','')).startswith(('xs_p','xs_i','xs_m','xs_d','xs_s','xs_f','xc_'))] if False else [x for x in X if x['slide'].get('id') in ('pp_s06','ed048-2','xs_survivors')]
L='../../assets/logos/'
def src(c,u,d,q): return {'claim':c,'url':u,'date':d,'quote':q}
SIG=dict(pill='SIGNAL',section='Market opportunity')
S_PRO=[src('Record 1.3 million signed lives and near 100% retention','https://www.sec.gov/Archives/edgar/data/1551306/000155130626000163/exhibit991q32026.htm','2026-11-04','Selling Season Yields Record 1.3 Million New Covered Lives with Another Year of Near 100% Retention'),
 src('Over 85 new clients','https://investors.progyny.com/news-releases/news-release-details/progyny-inc-announces-third-quarter-2026-results','2026-11-04','and over 85 new clients')]
S_IVF=[src('IVF covered by 54% of large employers in 2026, 50% in 2025','https://www.mercer.com/en-us/insights/us-health-news/2026-survey-employers-doubled-down-on-health-benefit-cost-management/','2026-11','IVF, one of the most important family-forming benefits, is now covered by 54% of all large employers, up from 50% in 2025')]
S_MEN=[src('Employers offering menopause support, 2025 and 2026','https://www.shrm.org/topics-tools/news/benefits-compensation/menopause-benefits-see-big-jump-employer-offerings','2026-07-31','The percentage of employers offering menopause support or resources jumped to 27%, up substantially from 18% last year')]
S_MAV=[src('Lives supported','https://www.mavenclinic.com/','2026-11-26','supporting 28 million lives worldwide'),src('Employers','https://www.mavenclinic.com/','2026-11-26','Trusted by 2,300+ employers'),
 src('Countries','https://www.mavenclinic.com/','2026-11-26','Global care, coverage, and reimbursement across 175+ countries'),
 src('November 2022 comparison','https://www.prnewswire.com/news-releases/maven-clinic-announces-90-million-series-e-round-of-funding-amidst-seismic-changes-in-womens-and-family-health-301676406.html','2022-11-14','Reaching 15 million lives under management')]
S_DEAL=[src('Hologic and Reveal Genomics','https://www.hologic.com/about/press-release/hologic-signs-definitive-agreement-acquire-reveal-genomics','2026-10-19','signed a definitive agreement to acquire Reveal Genomics'),
 src('Labcorp and Myriad prenatal','https://ir.labcorp.com/news-releases/news-release-details/myriad-genetics-and-labcorp-announce-definitive-agreement-myriad','2026-10-20','sell its Prenatal Health testing business'),
 src('Ferring and Gameto','https://www.gametogen.com/news/ferring-pharmaceuticals-and-gameto-sign-agreement-for-proposed-acquisition/','2026-10-27','The proposed transaction has a deal value of up to $1.3825 billion, subject to development, regulatory and commercial milestones.'),
 src('Cinven and Theramex','https://www.cinven.com/news-insights/cinven-to-acquire-theramex/','2026-11-03','it has reached an agreement to acquire Theramex'),
 src('Fertifa and Tuune','https://www.fertifa.com/resources/blog/tuune-acquisition','2026-11-06','Fertifa has acquired Tuune.')]
S_AUS=[src('Screening HPV tests self-collected, 2018 to H1 2026','https://www.aihw.gov.au/reports/cancer-screening/ncsp-monitoring-report-2026/contents/performance-indicator-1-participation','2026-11','Screening HPV tests self-collected (%) 0.1 0.2 0.4 0.7 6.6 21.7 35.2 46.3 51.5')]
S_FAM=[src('Ages 26 to 35, 13% in 2024 and 23% in 2026','https://www.kff.org/womens-health-policy/womens-experiences-with-contraception-use-coverage-and-preferences/','2026-11-17','with the largest increase among women ages 26 to 35 (23% vs. 13%)')]
S_MAR=[src('Progyny Q3 2026 revenue (thousands)','https://www.sec.gov/Archives/edgar/data/1551306/000155130626000163/exhibit991q32026.htm','2026-11-04','Revenue 341,254'),
 src('Progyny Q3 2026 operating income (thousands)','https://www.sec.gov/Archives/edgar/data/1551306/000155130626000163/exhibit991q32026.htm','2026-11-04','Income from operations 35,182'),
 src('Femasys Q3 2026 sales','https://ir.femasys.com/news/news-details/2026/Femasys-Announces-Financial-Results-for-Quarter-Ended-September-30-2026-and-Provides-Corporate-Update/default.aspx','2026-11-13','Sales 404,597'),
 src('Femasys Q3 2026 operating loss','https://ir.femasys.com/news/news-details/2026/Femasys-Announces-Financial-Results-for-Quarter-Ended-September-30-2026-and-Provides-Corporate-Update/default.aspx','2026-11-13','Loss from operations (4,450,010)')]
new=[
 dict(after='ed032',link='ed032, signal 1 of the list',slide=dict(id='xs_progyny',type='kpis',**SIG,fresh={'period':'total','end':'2026-11'},
  title='Progyny signed a record 1.3M new\ncovered lives for its fertility benefit',
  items=[dict(value='1.3M',label='New covered lives Progyny signed in its 2026 selling season, a record for the company'),
         dict(value='85+',label='New employer clients signed in the same season, most of them starting in 2027'),
         dict(value='~100%',label='Share of existing clients that renewed for 2027, as Progyny describes it')],
  why='This is a sign of a hot market because employers keep buying fertility benefits in volume. Covered lives are people who can use the benefit, not patients treated.',
  note='We used Progyny’s third quarter results of November 4, 2026. Near 100% is the company’s own description, not an exact rate'),sources=S_PRO),
 dict(after='xs_progyny',link='ed032, signal 2 of the list',slide=dict(id='xs_ivf',type='share_waffle',**SIG,fresh={'period':'year','end':'2026-11'},big='54%',kicker='WHY IT IS HOT',
  title='54% of large US employers now\ncover IVF, up from 50% in 2025',
  **{'on':'Cover IVF','off':'Do not cover IVF'},unit='large employers',years=[dict(k=54,n=100,p=54,x='2026')],
  story='IVF is now a standard benefit at most large US employers, which gives fertility startups a payer to sell to, a sign of a hot market.\nCoverage is not use: it says nothing of how many cycles are paid.',
  note=['We used Mercer’s 2026 national survey of employer health plans, published in November 2026,','where large employers have 500 employees or more. One square is one employer out of 100']),sources=S_IVF),
 dict(after='xs_ivf',link='ed032, signal 3 of the list',slide=dict(id='xs_menopause',type='x/sig_key_trend',**SIG,fresh={'period':'year','end':'2026-07'},
  title='The share of employers offering menopause\nsupport jumped from 18% to 27% in a year',
  t={9:'18%',10:'2025',12:'27%',13:'2026',15:'×1.5',16:'WHY IT IS HOT',17:'Employers now pay for menopause support, a new way for midlife care startups to reach women, a sign of a hot market.\n\n\nThe survey counts support and resources, not only clinical care or paid apps, so the paying market is smaller.'},
  vbars=[18,27],note='We used the SHRM Employee Benefits Study of 2025 and 2026, as reported by SHRM on July 31, 2026'),sources=S_MEN),
 dict(after='xs_menopause',link='ed032, signal 4 of the list',slide=dict(id='xs_maven',type='kpis',**SIG,fresh={'period':'total','end':'2026-11'},
  title='Maven’s virtual care now reaches 28M\npeople, up from 15M in late 2022',
  items=[dict(value='28M',label='People who can use Maven’s care, up from 15 million in 2022'),
         dict(value='2,300+',label='Employers that pay for Maven as a benefit for their staff and families'),
         dict(value='175+',label='Countries where Maven offers care, coverage and reimbursement')],
  why='This is a sign of a hot market because employers buy women’s care on one virtual platform for staff worldwide. These are eligible people, not active patients.',
  note='We used Maven’s website in November 2026 and its Series E release of November 2022 for the 15M figure'),sources=S_MAV),
 dict(after='xs_maven',link='ed032, signal 5 of the list',slide=dict(id='xs_deals',type='sx_league',**SIG,fresh={'period':'month','end':'2026-11'},big='5',h0='BUYER AND TARGET',h1='NO.',h2='WHEN',kicker='WHY IT IS HOT',
  title='Five women’s health takeovers were\nannounced in just 18 days this fall',
  rows=[dict(n=1,name='Hologic + Reveal Genomics',src=L+'hologic.png',v='Oct 19',what='Breast cancer test data'),
        dict(n=2,name='Labcorp + Myriad prenatal',src=L+'myriad.png',v='Oct 20',what='Prenatal testing business'),
        dict(n=3,name='Ferring + Gameto',src=L+'gameto.png',v='Oct 27',what='IVF egg maturation, up to $1.4B'),
        dict(n=4,name='Cinven + Theramex',src=L+'theramex.png',v='Nov 3',what='Women’s health medicines'),
        dict(n=5,name='Fertifa + Tuune',src=L+'tuune.png',v='Nov 6',what='Hormone health app')],
  story='Big groups now compete to buy women’s health companies, from tests to IVF tools, a sign of a hot market. Four of the five deals were still to close.',
  note=['We listed five takeovers announced from October 19 to November 6, 2026, from company releases,','with the Gameto amount including milestones. It is not a count of every deal in the sector']),sources=S_DEAL),
 dict(after='xs_deals',link='ed032, signal 6 of the list',slide=dict(id='xs_selftest',type='x/sig_key_trend',**SIG,fresh={'period':'half','end':'2026-06'},
  title='Half of Australia’s cervical screening\ntests are now collected by women themselves',
  t={9:'6.6%',10:'2022',12:'51.5%',13:'H1 2026',15:'×7.8',16:'WHY IT IS HOT',17:'When a whole country lets women take their own sample, most choose it within four years, a sign of a hot market for home screening tests.\n\n\nSelf-collected does not always mean at home: many women take the sample at the clinic.'},
  vbars=[6.6,51.5],note='We used the Australian Institute of Health and Welfare report of November 2026, screening HPV tests for women aged 25 to 74'),sources=S_AUS),
 dict(after='xs_selftest',link='ed032, signal 7 of the list',slide=dict(id='xs_fam',type='share_waffle',**SIG,fresh={'period':'year','end':'2026-04'},big='23%',kicker='WHY IT IS HOT',
  title='23% of US women aged 26 to 35 on birth\ncontrol now track their fertile days',
  **{'on':'Track fertile days','off':'Other methods only'},unit='women',years=[dict(k=23,n=100,p=23,x='2026')],
  story='More young women want birth control without hormones, a large audience for cycle tracking apps, a sign of a hot market.\nIt was 13% in 2024. Some use it with another method, and not all with an app.',
  note=['We used KFF’s 2026 Women’s Health Survey, published on November 17, 2026,','covering women aged 26 to 35 who use birth control. One square is one woman in 100']),sources=S_FAM),
 dict(after='pp_s06',link='pp_s06, the business models, and ed103 « PAYER CONTRACTS »',slide=dict(id='xv_margins',type='sx_stat_strip',section='Value creation',
  title='Progyny earned 10 cents per dollar of sales\nwhile Femasys lost $11 per dollar',headline='Operating result per $1 of revenue, third quarter of 2026',
  stats=[dict(v='+$0.10',l='Progyny, which sells fertility benefits paid by employers'),dict(v='−$11',l='Femasys, which builds and sells its own fertility devices'),dict(v='$341M',l='Progyny’s revenue in the quarter, against $0.4M for Femasys')],
  story='Payer contracts turn into revenue at scale, while a device maker still pays to build and sell its product. These are two firms at different stages, not averages.',
  note=['We divided operating income or loss by revenue for the three months to September 30,','2026, from the quarterly results of Progyny and Femasys. Progyny is listed, not a startup']),sources=S_MAR),
 dict(after='ed141',link='ed141 « Remote clinical care still needs access to qualified specialists »',slide=dict(id='xc_backlog',type='x/sig_announced_vs_built',section='Market challenges',
  title='England’s gynecology waiting list is\nnearly five times what it sees each month',
  t={8:'585',9:'thousand on the\nwaiting list',11:'126',12:'thousand seen\neach month',15:'×4.7',16:'WHAT IS GOING ON',17:'In August 2026, 585,378 gynecology referrals were waiting in England, a list that grew for a fifth month in a row.\n\n\nIn 2026 the NHS saw about 125,594 referrals a month, almost five months of visits. Specialists are the bottleneck, which virtual care can ease but not remove.'},
  vbars=[585378,125594],note='We used the Royal College of Obstetricians and Gynaecologists update of October 16, 2026, on NHS England data'),sources=[src('Waiting list','https://www.rcog.org.uk/news/gynaecology-waiting-list-increases-for-a-fifth-month-in-a-row/','2026-10-16','the gynaecology waiting list now stands at 585,378.'),src('Seen per month','https://www.rcog.org.uk/news/gynaecology-waiting-list-increases-for-a-fifth-month-in-a-row/','2026-10-16','on average 125,594 seen this year.')]),
]
yaml.safe_dump(X+new,open(P,'w'),allow_unicode=True,sort_keys=False,width=1000)
print(len(X+new))
