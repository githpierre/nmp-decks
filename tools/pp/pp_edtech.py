"""EdTech: the product-page slides (pp_* templates) replace their twin slide in decks/edtech-full (Pierre, 12 Nov 2026: « on remplace »).
Data comes from the twin slide itself (same question, same facts), so the deck stays consistent.

    python3 tools/pp/pp_edtech.py          # rewrites decks/edtech-full/deck.yaml (run once; it checks the twin is still there)
"""
import yaml, re
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
F = ROOT / 'decks/edtech-full/deck.yaml'
R = lambda h: f'media/raw/{h}.png'                 # logos already in the deck (from the PowerPoint)
L = lambda s: f'../../assets/logos/{s}.png'
PP = lambda s: f'../../assets/logos/pp/{s}.png'


def drivers_events():
    raw = [('1997', 'Blackboard moves college courses online', 13), ('2001', 'MIT puts its course materials online free', 13),
           ('2002', 'No Child Left Behind fuels testing software', 13), ('2006', 'Free Google Apps pulls schools online', 13),
           ('2008', 'Khan Academy shows video lessons can scale', 16), ('2010', 'iPad puts touch tablets in classrooms', 13),
           ('2010', 'Common Core forces schools to buy content', 13), ('2011', 'Stanford AI class draws 160,000 online', 16),
           ('2012', 'Coursera and edX spark the MOOC boom', 16), ('2012', 'Duolingo makes language lessons a free app', 10),
           ('2014', 'Free Google Classroom gets teachers online', 16), ('2014', 'FCC E-Rate overhaul brings Wi-Fi to schools', 13),
           ('2015', 'LinkedIn pays $1.5B for Lynda courses', 13), ('2016', "Jio's cheap data brings India online", 13),
           ('2017', 'Chromebooks win most US school laptops', 13), ('2019', 'Pearson goes digital first for textbooks', 10),
           ('2020', 'Covid shuts schools for 1.6 billion kids', 26), ('2020', 'Zoom becomes the default classroom', 16),
           ('2020', 'Google certificates rival college degrees', 10), ('2021', 'US relief funds give schools $190B', 23),
           ('2021', 'Coursera and Duolingo IPOs prove EdTech pays', 13), ('2022', 'ChatGPT gives every student an AI tutor', 26),
           ('2023', 'Khanmigo brings GPT-4 tutoring to schools', 13), ('2023', 'Chegg crash shows AI beats homework sites', 10),
           ('2025', 'White House order pushes AI into schools', 13), ('2025', 'Beijing makes AI classes required in schools', 13),
           ('2025', 'OpenAI and Google give students free AI', 16), ('2025', 'Microsoft pledges $4B for AI education', 13),
           ('2025', 'ChatGPT study mode turns chat into tutoring', 10), ('2026', 'India adds AI classes from grade 3', 13)]
    imp = {10: 1.0, 13: 1.5, 16: 2.0, 23: 2.5, 26: 3.0}        # dot size on the PowerPoint slide -> impact scale of the template
    return [dict(year=y, text=t, impact=imp[d]) for y, t, d in raw]


NEW = {
 7: dict(type='pp_radar', section='Market definition', pill='MARKET MAP', title='Who is in EdTech,\nand who stays outside?',
         caption=['Distance to the center reflects how directly a product is built to teach, assess or certify, not just used by learners',
                  "The companies shown are a representative sample, not an exhaustive list, chosen to show where the market's boundaries lie"],
         inside=[R(h) for h in ('8738717e586a', '27d0aaec1319', '2c0170a34c83', '9b5d0692664d', '2010980f56b1', 'aded70e5d0bc', '42a3e9032be5', '4b576af154b9')],
         TL=dict(src=R('3bf56f6c'), name='MasterClass', text='sells celebrity video lessons by subscription, which feels like learning but works more like a streaming service'),
         TR=dict(src=R('36d491c1'), name='Zoom', text='hosted millions of classes during the pandemic, but it remains generic video software built for business meetings'),
         BL=dict(src=R('ffbc37cf'), name='Pearson', text='is seen as a textbook publisher, yet testing and online schools bring in about 60% of its sales, so it sits on the line'),
         BR=dict(src=R('d90aa2c4'), name='OpenAI', text='added a study mode for students and sells ChatGPT Edu to universities, yet ChatGPT remains a general assistant')),
 39: dict(type='pp_trends', section='Market opportunity', pill='SIGNAL', title='Online learning searches\nhave suddenly taken off',
          csv='decks/edtech-full/media/trends/online-learning.csv', term='online learning', date='Lately.',
          expl='After the Covid rush, interest in online learning slowly faded for years. Then free AI tutors got good enough for everyday homework help, and millions of parents and students went looking for new ways to learn online.',
          note=['We tracked how often people around the world googled this term over the last five years', "We also corrected the curve for a jump in Google's counts that happened in August 2025"]),
 47: dict(type='pp_donutv', variant='B', section='Market size', title='How is the EdTech market split between its categories?',
          cats=[dict(name='School platforms', p=35, logos=[L('magicschool'), PP('instructure')]),
                dict(name='Workforce learning', p=22, logos=[L('multiverse'), L('degreed')]),
                dict(name='Online courses', p=20, logos=[PP('coursera'), R('f4e85095')]),
                dict(name='Digital tutoring', p=14, logos=[L('preply'), PP('duolingo')]),
                dict(name='Other spending', p=9, logos=[R('4e4e7e87'), R('279d84b5')])],
          note=['We split the total using the end-user shares of Grand View and Fortune Business Insights',
                'We then rounded every category so that all of them still add up to the same $192 billion']),
 52: dict(type='pp_cagr', section='Market size', title='How much bigger can\nEdTech get?', size=213, cagr=11, y0=2026, lead='To get that big, ',
          condition='the market must turn AI tutors and teacher tools into paid products, while schools and companies keep budgets for learning every year.',
          note=['We compared the forecasts of Grand View, Fortune Business Insights, MarketsandMarkets, and IMARC',
                'We adjusted each one to our definition and aligned their timelines to build a realistic range']),
 99: dict(type='pp_tech', section='Tech and infra', title='Which EdTech players\ncan already do the most today?',
          companies=[dict(name='Duolingo', src=R('51c1caba')), dict(name='Khan Academy', src=R('56255c1e')), dict(name='Babbel', src=R('d071da06')),
                     dict(name='Coursera', src=R('d109e24b')), dict(name='Udemy', src=R('4214f8c6')), dict(name='edX', src=R('f4e85095'))],
          features=[dict(header='AI|tutor', values=[1, 1, 1, 1, 1, 1]), dict(header='Online|degrees', values=[0, 0, 0, 1, 0, 1]),
                    dict(header='Speech|scoring', values=[1, 0, 1, 0, 0, 0]), dict(header='K-12|teachers', values=[1, 1, 0, 0, 0, 0]),
                    dict(header='Open|marketplace', values=[0, 0, 0, 0, 1, 0]), dict(header='Kids|app', values=[1, 1, 0, 0, 0, 0]),
                    dict(header='In-house|courses', values=[1, 1, 1, 0, 0, 0])],
          note=['We went through each company’s website, filings and press releases, feature by feature',
                'A pink mark means the feature is there, with all the sources at the end of the report']),
 105: dict(type='pp_value', section='Value creation', title='How does money really\nflow in EdTech?',
           axes=['Pays once', 'Pays every month', 'Paid by', 'learners', 'Paid by', 'institutions'],
           groups=[dict(name='Degrees and certificates', x=0.23, y=0.69, logos=[dict(src=R('d109e24b')), dict(src=R('f4e85095'))]),
                   dict(name='Paid by school districts', x=0.77, y=0.9, logos=[dict(src=R('56255c1e'))]),
                   dict(name='Paid tutoring lessons', x=0.46, y=0.35, logos=[dict(src=R('73ab3e7b'))]),
                   dict(name='Monthly subscription', x=0.77, y=0.32, logos=[dict(src=R('51c1caba')), dict(src=R('d071da06'))])],
           note=['We placed each company by how its business model works, from pricing pages, company reports and filings',
                 'Positions are our own reading of each model, and all the sources are included at the end of the report']),
 142: dict(type='pp_risks', section='Market challenges', title='What could go wrong for EdTech?',
           events=[dict(text='Free study modes from OpenAI and Google get good enough for most learners, pulling customers away from paid apps and homework help', odds=25, impact=3),
                   dict(text='School budgets shrink as COVID relief ends and enrollment keeps falling, so K-12 vendors face deep cuts at renewal time', odds=20, impact=2),
                   dict(text='A long recession pushes employers to cut training first, as in 2009 and 2020, shrinking workforce learning for a year or two', odds=15, impact=2),
                   dict(text='Google, Microsoft and Coursera bundle every feature into their platforms, leaving little room for point tools from smaller startups', odds=15, impact=2),
                   dict(text='Studies show that AI tutors do not improve learning, so schools pull their budgets and parents lose trust in AI learning for years', odds=12, impact=3),
                   dict(text='Strict AI rules for schools, like the EU high-risk rules due in December 2027, make it too costly for small startups to sell', odds=10, impact=2),
                   dict(text='More governments limit screens in schools, beyond the 35 US states that limit phones, so K-12 apps lose their class time', odds=8, impact=2),
                   dict(text='A major breach of student data leads to bans on many learning tools at once, hurting every vendor that sells to schools', odds=5, impact=3)],
           note=['We listed the events that could slow EdTech down, from company news, regulators and analysts',
                 'Odds and impact are our own estimates, and you will find all the sources we used at the end of the report']),
 148: dict(type='pp_drivers', section='Growth drivers', title='What pushed the EdTech market forward, year after year?', events=drivers_events(),
           note=['Many events shaped EdTech, and these are the ones we believe had the biggest impact on the market',
                 'Ratings are our own, from company news, filings and analyst reports, with all the sources at the end']),
 165: dict(type='pp_raises', section='Investor bets', title='Who are investors backing most\nin EdTech right now?',
           rounds=[dict(name='Preply', amt=150e6, src=L('preply'), stage='Series D', date='Q1 2026'),
                   dict(name='LearnVector', amt=100e6, src=L('learnvector'), stage='Series A', date='Q3 2026'),
                   dict(name='Yoodli', amt=40e6, src=L('yoodli'), stage='Series B', date='Q4 2025'),
                   dict(name='Emversity', amt=30e6, src=L('emversity'), stage='Series A', date='Q1 2026')],
           note=['We listed the biggest equity rounds raised by EdTech startups over the last twelve months',
                 'We used company announcements and the press, and all our sources are at the end of the report']),
 168: dict(type='invbets', handle='edtech', section='Investor bets', title='Where did EdTech investors put their money this past year?',
           note='We added up every funding round we tracked in EdTech over the last twelve months, from company announcements, funding databases and the press. All the sources are included at the end of the report.',
           rows=[dict(name='Workforce learning', names=['LearnVector', 'Yoodli'], v='$278M', pct='37% of total', w=100.0, logos=[dict(src=R(h)) for h in ('b81e7571', '10993771', '94a7653b')]),
                 dict(name='Digital tutoring', names=['Preply', 'SpeakX'], v='$243M', pct='32% of total', w=87.4, logos=[dict(src=R(h)) for h in ('7cafbc9c', '4ad795ef', '5e02a6af')]),
                 dict(name='School platforms', names=['Subject', 'Gizmo'], v='$164M', pct='22% of total', w=59.0, logos=[dict(src=R(h)) for h in ('1148d4f5', 'e736cd32', 'c275461b')]),
                 dict(name='Online courses', names=['Oboe', 'Skillwill'], v='$39M', pct='5% of total', w=14.0, logos=[dict(src=R(h)) for h in ('ce15e973', 'c2eb9c18', '5f00df52')]),
                 dict(name='Assessment tech', names=['Ed.ai', 'DeweyLearn'], v='$21M', pct='3% of total', w=7.6, logos=[dict(src=R(h)) for h in ('4e4e7e87', '279d84b5')]),
                 dict(name='Digital credentialing', names=['BRUM Patenti', 'AICertified'], v='$7M', pct='under 1% of total', w=2.5, logos=[])]),
 171: dict(type='pp_grid', section='Top players', title='Who are the top players\nin EdTech today?', handle='edtech', cols=['Leaders', 'Challengers', 'Newcomers'],
           rows=['Schools', 'Consumers', 'Workforce'],
           cells=[[['classdojo', 'newsela'], ['magicschool', 'amira'], ['teachy', 'brisk']],
                  [['preply', 'gostudent'], ['knowunity', 'speakx'], ['sigiq', 'oboe']],
                  [['multiverse', 'guild'], ['yoodli', 'stepful'], ['fullyramped', 'secondnature']]],
           note=['We placed private players by their main customer and their stage, from funding news, revenue and reach',
                 'We left out big tech, listed firms like Duolingo and buyouts like PowerSchool, with sources at the end of the report']),
 199: dict(type='pp_killers', mode='warning', section='Startup killers', title='Which EdTech companies have shown warning signs lately?',
           signs=['Big|layoffs', 'Lost|independence', 'Lawsuit or|court case', 'Value|fell', 'Missed|deadlines'],
           rows=[dict(name='Chegg', slug='chegg', domain='chegg.com', src=R('3b6d140a'), ini='C', cells=['45% of|staff 2025', '', 'Sued Google|in 2025', 'Down 99%|from peak', '']),
                 dict(name="Byju's", slug='byjus', domain='byjus.com', src=R('a911bdf4'), ini='B', cells=['', 'Creditors|in control', 'US lender|suits 2023', 'Down from|$22B peak', 'Results|filed late']),
                 dict(name='Unacademy', slug='unacademy', domain='unacademy.com', src=R('7bd86be7'), ini='U', cells=['', 'Sold to|upGrad 2026', '', '94% below|peak value', '']),
                 dict(name='Udemy', slug='udemy', domain='udemy.com', src=R('4214f8c6'), ini='U', cells=['', 'Merged into|Coursera', '', 'Down 46%|in 2024', '']),
                 dict(name='Coursera', slug='coursera', domain='coursera.org', src=R('d109e24b'), ini='C', cells=['Job cuts|after merger', '', '', 'Down 91%|from peak', '']),
                 dict(name='2U', slug='2u', domain='2u.com', src=R('f91ee0de'), ini='2U', cells=['', 'Lenders|took over', 'Chapter 11|in 2024', 'Shares|wiped out', ''])],
           note=['We looked for warning signs among well-known EdTech companies, from layoffs and lawsuits to falling valuations',
                 'We used company filings, court records and the press, and all the sources are included at the end of the report']),
 209: dict(type='pp_winner', section='Startup strategies', title='Why might Duolingo be winning\nthe language app market?',
           companies=[dict(short='Duolingo', src=R('4b885a55')), dict(short='Babbel', src=R('fbee7802')), dict(short='Rosetta', src=R('ce5308d6')),
                      dict(short='Speak', src=R('2e37338a')), dict(short='Praktika', src=R('7abc8982'))],
           criteria=[dict(name='140M+ monthly learners', why='Biggest free learner funnel', ticks=[1, 0, 0, 0, 0]),
                     dict(name='12.7M paid subscribers', why='Strong paid conversion', ticks=[1, 0, 0, 0, 0]),
                     dict(name='AI speaking practice', why='Talk anytime, no tutor', ticks=[1, 1, 0, 1, 1]),
                     dict(name='Own English test', why='Revenue beyond app plans', ticks=[1, 0, 0, 0, 0]),
                     dict(name='Math, music and chess', why='More reasons to open the app', ticks=[1, 0, 0, 0, 0]),
                     dict(name='Profitable and listed', why='Cash to keep investing', ticks=[1, 0, 0, 0, 0]),
                     dict(name='Live tutor classes', why='Human help when needed', ticks=[0, 1, 1, 0, 0])],
           note=['We compared companies with the same business model on what matters most to customers',
                 'We used company reports, websites and the press, with all the sources at the end of the report']),
}


def fix_raw(v):
    """short hashes -> the real file names in media/raw"""
    names = [p.name for p in (ROOT / 'decks/edtech-full/media/raw').glob('*.png')]
    if isinstance(v, str) and v.startswith('media/raw/'):
        h = v[10:-4]; m = [n for n in names if n.startswith(h)]; assert len(m) == 1, v; return 'media/raw/' + m[0]
    if isinstance(v, dict): return {k: fix_raw(x) for k, x in v.items()}
    if isinstance(v, list): return [fix_raw(x) for x in v]
    return v


def main():
    D = yaml.safe_load(F.read_text())
    S = D['slides']
    for n, new in NEW.items():
        old = S[n - 1]
        assert old['id'] == f'ed{n:03d}', (n, old['id'])
        new = fix_raw(new)
        if new['type'] == 'pp_grid':
            new['srcs'] = {s: L(s) if (ROOT / f'assets/logos/{s}.png').exists() else '' for row in new['cells'] for c in row for s in c}
            new['weight'] = {}
        S[n - 1] = {'id': f'ed{n:03d}p', **new}
    F.write_text(yaml.dump(D, allow_unicode=True, sort_keys=False, width=1000))
    print('replaced', sorted(NEW))


if __name__ == '__main__':
    main()
