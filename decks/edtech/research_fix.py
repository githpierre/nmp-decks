import re,yaml,glob
R='/home/claude/nmp-decks/decks/edtech/research/'
# round 1 (28 Nov 2026): ed173 came back transposed (company columns, one-word headers). Rebuilt in the reference shape:
# (INSTRUCTURE is 11 letters, cut in two in the row label: Docebo instead, from its annual filing)
# columns = 5 workflows on two lines, rows = 6 companies (Coursera added from its own filings: Coursera for Business 2016,
# verified mastery in the Udemy merger release); SELF-STUDY APP dropped to keep 5 columns.
ROWS=[('DUOLINGO',['YES','NO','NO','NO','YES']),('PREPLY',['YES','YES','NO','YES','NO']),('DOCEBO',['NO','NO','YES','YES','NO']),
      ('LEARNUPON',['NO','NO','YES','YES','NO']),('SPEAK',['YES','NO','NO','NO','NO']),('COURSERA',['NO','NO','NO','YES','YES'])]
HEAD={10:"LANGUAGE\n\nLEARNING",14:"LIVE\n\nTUTORING",28:"LEARNING\n\nPLATFORM",32:"STAFF\n\nTRAINING",40:"SKILL\n\nPROOF"}
RK=[6,7,8,19,20,46]; CELLS={6:[9,13,27,31,39],7:[11,15,29,33,41],8:[12,16,30,34,42],19:[21,23,35,37,43],20:[22,24,36,38,44],46:[47,48,49,50,51]}
for f in glob.glob(R+'*09-investor*'):
    t=open(f).read(); o=t
    def fix(m):
        if m.group(1)!='ed173': return m.group(0)
        d=yaml.safe_load(m.group(2))
        if 'LIVE\n\nTUTORING' in str(d['t']): return m.group(0)
        tt=dict(HEAD)
        for rk,(n,v) in zip(RK,ROWS):
            tt[rk]=n
            for ck,val in zip(CELLS[rk],v): tt[ck]=val
        d['t']=tt; d.pop('comment',None)
        d['note']="We compare six startup-origin businesses by their core offerings. NO means the workflow is not a core focus in the cited descriptions, not that no related feature exists."
        d['sources'].append({'claim':'Coursera enterprise platform','url':'https://www.sec.gov/Archives/edgar/data/1651562/000095017022014875/cour-20220630.htm','date':'2022-08','quote':'Coursera for Business, our Enterprise platform offering for businesses, in 2016'})
        d['sources'].append({'claim':'Coursera verified mastery','url':'https://investor.coursera.com/news/news-details/2026/Coursera-Completes-Combination-with-Udemy-to-Build-the-Worlds-Most-Comprehensive-Skills-Platform/default.aspx','date':'2026-05-11','quote':'connect skills discovery, development, and verified mastery'})
        d['sources'].append({'claim':'Docebo learning platform for companies','url':'https://www.sec.gov/Archives/edgar/data/1829959/000162828026012566/doceboaif2025finalv2.htm','date':'2026-02','quote':'94% of our revenue was generated from our recurring subscription-based plans for our learning management platform.'})
        return '### %s\n```yaml\n%s```'%('ed173',yaml.safe_dump(d,allow_unicode=True,sort_keys=False,width=1000))
    t=re.sub(r'### (\S+)\n```yaml\n(.*?)```',fix,t,flags=re.S)
    if t!=o: open(f,'w').write(t)

# round 2 (first build, 28 Nov 2026): line counts, labels that wrap, map text on 3 lines, balanced notes
REP=[("text: The Middle East and Africa account for about 3% of the published total, the smallest of the five regional groups.","text: The Middle East and Africa account for about 3% of the published total, the smallest of the five regional groups in the table."),
("'LEARNING PROOF\n\n\n    Over the pilot term","'RESULTS\n\n\n    Over the pilot term"),
("'AI DEPENDENCE\n\n\n\n    A high school","'AI RELIANCE\n\n\n\n    A high school"),
("'NO LEARNING GAIN\n\n\n\n    A 2026","'FLAT SCORES\n\n\n\n    A 2026"),
("'Teachers and learners must engage with tools\n\n    for them to work'","'Tools only work if teachers and\n\n    learners use them every week'"),
("'A useful tool still needs independent evidence\n\n    of learning gains'","'Tools still need independent proof\n\n    that students learn more'"),
("'Learners got little structured feedback\n\n    after live lessons'","'Learners got little feedback\n\n    after live lessons'"),
("- We used published product descriptions, business disclosures and company announcements for Duolingo.","- We used published product descriptions, filings and company announcements for Duolingo."),
("- We used published product descriptions, business disclosures and company announcements for Preply.","- We used published product descriptions, filings and company announcements for Preply."),
("- We used published product descriptions, business disclosures and company announcements for Brisk Teaching.","- We used product descriptions, filings and company announcements for Brisk Teaching."),
("- We used published product descriptions, business disclosures and company announcements for MagicSchool.","- We used product descriptions, filings and company announcements for MagicSchool."),
("- We used published product descriptions, business disclosures and company announcements for Yoodli.","- We used published product descriptions, filings and company announcements for Yoodli.")]
for f in glob.glob(R+'*.md'):
    t=open(f).read(); o=t
    for a,b in REP: t=t.replace(a,b)
    if t!=o: open(f,'w').write(t)

# round 3 (visual pass): the Australia text ran under its leader line
for f in glob.glob(R+'*09-investor*'):
    t=open(f).read(); o=t.replace("text: Australia is home to Mathspace, a school math platform that provides adaptive learning paths and step-by-step feedback.","text: Australia has Mathspace, a school math platform with adaptive learning paths and step-by-step feedback.")
    if t!=o: open(f,'w').write(o)
