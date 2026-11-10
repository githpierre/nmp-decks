"""pilot.json -> nmp-decks/decks/<slug>/deck.yaml (one investor-bets slide per market), logos copied into assets/logos."""
import json, sys, os, shutil, yaml, re, pandas as pd
slug=sys.argv[1]; src=sys.argv[2] if len(sys.argv)>2 else '/home/claude/s09/pilot.json'
D=json.load(open(src)); ROOT='/home/claude/nmp-decks'; LG=f'{ROOT}/assets/logos'
mk=pd.read_csv('/home/claude/nmp-product-pages/w/nmp_slide_kit/markets_225.csv').set_index('handle')
def money(v): return f'${v/1e9:.1f}B' if v>=1e9 else f'${v/1e6:.0f}M'
TNAME={'rwa-tokenization':'real-world asset tokenization','ai-powered-market-research':'AI market research','anti-obesity-drugs':'obesity drug','ai-toys':'AI toy','radiopharmaceuticals':'radiopharmaceutical','b2b-payments':'B2B payment','cross-border-b2b-payments':'cross-border B2B payment','ai-personal-assistant':'AI assistant'}
def mname(h): return TNAME.get(h) or re.sub(r' market$','',mk.loc[h,'nom_market'])
def nname(h): return re.sub(r' (industry )?market$','',mk.loc[h,'nom_market']).replace('AI-powered market research industry','AI market research')
NOTE='We added up every funding round we tracked in {} over the last twelve months, from company announcements, funding databases and the press. All the sources are included at the end of the report.'
slides=[];keep=[]
for h,d in D.items():
    mx=max(r['v'] for r in d['rows']); rows=[]
    for r in d['rows']:
        lg=[]
        for l in r['logos']:
            if len(lg)==3: break
            if l['path']:
                dst=f"{LG}/{l['id']}.png"
                if not os.path.exists(dst): shutil.copy(l['path'],dst)
                lg.append(dict(src=f"../../assets/logos/{l['id']}.png",name=l['name']))
        lg=lg[:3]   # no name tile ever (Pierre, 11 Nov 2026): a missing logo is asked to Pierre
        p=r['pct']; rows.append(dict(name=r['short'],names=r['names'],v=money(r['v']),pct=f'{p*100:.0f}% of total' if p>=0.01 else 'under 1% of total',w=round(max(2,100*r['v']/mx),1),logos=lg))
    nm=mname(h); keep.append(nm)
    slides.append(dict(type='invbets',handle=h,section='Investor bets',title=f'Where did {nm} investors put their money this past year?',label=re.sub(r'\s{2,}','\u00a0',mk.loc[h,'market_name_for_slide'].strip()).replace(' ','').replace('\u00a0',' '),note=NOTE.format(nname(h)),rows=rows))
os.makedirs(f'{ROOT}/decks/{slug}',exist_ok=True)
yaml.safe_dump(dict(market='',quarter='S09',label='',keep_together=keep,slides=slides),open(f'{ROOT}/decks/{slug}/deck.yaml','w'),allow_unicode=True,sort_keys=False,width=200)
print(len(slides),'slides')
