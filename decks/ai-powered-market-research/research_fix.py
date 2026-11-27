import re,yaml,glob,sys
R='/home/claude/nmp-decks/decks/ai-powered-market-research/research/'
drop={'ed136':range(14,22),'ed153':range(14,22),'ed172':range(13,21),'ed186':range(15,23)}
new={
 'ed032':{15:'Listen Labs passed one million interviews in under two years'},
 'ed041':{7:'We define the market as independent vendors using AI to collect, simulate or analyze evidence about buyers and markets for business decisions.',
          8:'We include AI-moderated interviews, AI surveys, synthetic respondents, research coding, consumer intelligence and concept tests.',
          9:'We exclude generic assistants, broad data infrastructure, agency services, transcription, content generation and ad buying.'},
 'ed048':{4:'AI-moderated interviews and focus groups plus AI-powered surveys and quantitative studies collect real buyer evidence.'},
 'ed050':{18:'ESOMAR GUIDANCE'},
 'ed088':{14:'Privacy, consent and human review control how research data enters AI tools.',
          15:'APIs and repositories move findings into product, brand and strategy calls.'},
 'ed091':{7:'2024\nToluna launched HarmonAIze, a synthetic data suite for quantitative and qualitative research, focused on hard-to-reach audiences.'},
 'ed092':{24:"quantilope launched Category Twins, synthetic consumers built on each brand's tracking data for early research and concept tests."},
 'ed093':{16:'Conveo launched StoryLines, a continuous research product that keeps interviews running on strategic topics for brands.'},
 'ed094':{5:'Online panels face bots and fake respondents, so studies need checks beyond basic attention tests.',
          22:'AI respondents can match broad averages yet miss individual views and small groups.',
          13:'Panels may miss rare buyers, offline groups and people with little digital access.',
          30:'Research data exposes personal details, so consent, access and retention rules count.'},
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
