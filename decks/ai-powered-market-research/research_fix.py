import re,yaml,glob,sys
R='/home/claude/nmp-decks/decks/ai-powered-market-research/research/'
drop={'ed136':range(14,22),'ed153':range(14,22),'ed172':range(13,21),'ed186':range(15,23)}
new={
 'ed032':{15:'Listen Labs ran one million AI-led customer talks'},
 'ed041':{7:'We define the market as independent vendors using AI to collect, simulate or analyze evidence about buyers and markets for business decisions.',
          8:'We include AI-moderated interviews, AI surveys, synthetic respondents, research coding, consumer intelligence and concept tests.',
          9:'We exclude generic assistants, broad data infrastructure, agency services, transcription, content generation and ad buying.'},
 'ed029':{12:'Funding, launches and customer use accelerated across synthetic audiences, AI interviews and evidence-linked research tools for enterprises.'},
 'ed048':{4:'AI-moderated interviews and focus groups plus AI-powered surveys and quantitative studies collect real buyer evidence.'},
 'ed050':{18:'ESOMAR GUIDANCE'},
 'ed088':{14:'Privacy, consent and human review control how research data enters AI tools.',
          15:'APIs and repositories move findings into product, brand and strategy calls.'},
 'ed091':{7:'2024\nToluna launched HarmonAIze, a synthetic data suite for quantitative and qualitative research, focused on hard-to-reach audiences.'},
 'ed092':{24:"quantilope launched Category Twins, synthetic consumers built on each brand's tracking data for early concept tests."},
 'ed093':{16:'Conveo launched StoryLines, a continuous research product that keeps interviews running on strategic topics for brands.'},
 'ed094':{5:'Online panels face bots and fake respondents, so studies need checks beyond basic attention tests.',
          22:'AI respondents can match broad averages yet miss individual views and small groups.',
          13:'Panels may miss rare buyers, offline groups and people with little web access.',
          30:'Research data holds personal facts, so consent, access and retention rules count.'},
 'ed095':{5:'Coherent fake answers evade simple filters, so screening needs identity, behavior and data checks.',
          13:'Opt-in samples do not always represent rare buyers, nonusers or offline groups.',
          34:'ESOMAR asks for validity and reliability proof, but has no shared cross-vendor score.'},
 'ed098':{25:'Simile creates synthetic users to test product, price, campaign and service choices.',
          30:'POGO',
          28:'Pogo runs AI interviews with a panel of 3M US consumers and verified purchases.'},
 'ed173':{40:'AD TESTS'},
 'ed174':{7:'2023 - 2024\n\nGenerative AI made it easier to build AI moderators and synthetic users. New platforms like Conveo and Aaru emerged beside older specialists.'},
 'ed182':{14:'MODELING'},
}
n=0
for f in glob.glob(R+'*.md'):
    t=open(f).read(); o=t
    def fix(m):
        global n
        i=m.group(1); y=m.group(2)
        if i not in drop and i not in new and '$3.0M' not in y: return m.group(0)
        d=yaml.safe_load(y)
        for k in drop.get(i,[]): d['t'].pop(k,None)
        for k,v in new.get(i,{}).items(): d['t'][k]=v
        if i=='ed098':
            d['logos']=[('Pogo | joinpogo.com' if 'Electric Twin' in x else x) for x in d['logos']]
            d['sources']=[x for x in d['sources'] if 'Electric Twin' not in x['claim']]+[{'claim':'Pogo launched an AI research platform on its consumer panel.','url':'https://www.joinpogo.com/articles/announcing-32m-in-funding','date':'2026-06-01','quote':'Pogo has raised $32 million to date and launched the first product in its research platform.'}]
        s=yaml.safe_dump(d,allow_unicode=True,sort_keys=False,width=1000).replace('$3.0M','$3M')
        n+=1
        return '### %s\n```yaml\n%s```'%(i,s)
    t=re.sub(r'### (\S+)\n```yaml\n(.*?)```',fix,t,flags=re.S)
    if t!=o: open(f,'w').write(t)
print('blocks fixed',n)

# --- round 2 (first build, 27 Nov 2026): YES/NO read as booleans, layout fixes on research texts
import yaml as _y
LIT={
 '200M':None,
}
REP=[
 ("What counts as AI-powered market research, and what does not?","What counts as AI market research, and what does not?"),
 ("Which bold bets could reshape AI-powered market research?","Which bold bets could reshape AI market research?"),
 ("MIXED-MEDIA TESTING","MULTIMEDIA TESTS"),
 ("They combine study design, fieldwork and synthesis in one tool","They combine study design, fieldwork and synthesis"),
 ("They reported interviewing over one million people by January","They interviewed over one million people by January"),
 ("Salesforce completed its acquisition of Listen Labs in November","Salesforce bought Listen Labs in early November 2026"),
 ("They support research interviews natively in over 40 languages","They run interviews natively in over 40 languages"),
 ("They support custom guides and AI-generated interview guides","They support custom and AI-generated interview guides"),
 ("They reported tenfold revenue growth and raised a $14M round","They grew revenue tenfold and raised a $14M round"),
 ("They compare each new wave with earlier waves to spot shifts","They compare each wave with earlier ones to spot shifts"),
 ("They show tracked measures in live charts with video evidence","They show tracked measures in live charts with video"),
 ("They combine language models with real consumer survey data","They combine language models with real survey data"),
 ("They hold back evaluation questions when building the audience","They hold back test questions when building the audience"),
 ("They compare predicted distributions with actual survey answers","They compare predicted answers with real survey answers"),
 ("Each interview adds evidence that improves the next study and follow-up questions","Each interview adds evidence that improves the next study"),
 ("Ideally's team spans Auckland, Sydney and Melbourne and serves more than 300 brands across global markets.","Ideally's team spans Auckland, Sydney and Melbourne and serves more than 300 brands."),
]
for f in glob.glob(R+'*.md'):
    t=open(f).read(); o=t
    for a,b in REP: t=t.replace(a,b)
    def yn(m):
        if m.group(1)!='ed173': return m.group(0)
        d=_y.safe_load(m.group(2))
        for k,v in list(d['t'].items()):
            if isinstance(v,bool): d['t'][k]='YES' if v else 'NO'
        return '### %s\n```yaml\n%s```'%(m.group(1),_y.safe_dump(d,allow_unicode=True,sort_keys=False,width=1000))
    t=re.sub(r'### (\S+)\n```yaml\n(.*?)```',yn,t,flags=re.S)
    if t!=o: open(f,'w').write(t)
