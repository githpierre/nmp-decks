import re,yaml,glob
R='/home/claude/nmp-decks/decks/deepfake-detection/research/'
new={'ed173':{14:'PINDROP\n\nSECURITY',32:'HIVE\n\nAI',40:'SENSITY\n\nAI'}}
for f in glob.glob(R+'*.md'):
    t=open(f).read(); o=t
    def fix(m):
        i=m.group(1)
        if i not in new: return m.group(0)
        d=yaml.safe_load(m.group(2))
        for k,v in new[i].items(): d['t'][k]=v
        return '### %s\n```yaml\n%s```'%(i,yaml.safe_dump(d,allow_unicode=True,sort_keys=False,width=1000))
    t=re.sub(r'### (\S+)\n```yaml\n(.*?)```',fix,t,flags=re.S)
    if t!=o: open(f,'w').write(t)

# round 2 (first build, 27 Nov 2026): warning-signs grid in the shape of the reference (name, slug, ini; two-line headers),
# growth chart without data dropped
SIGNS={'BIG LAYOFFS':'Big|layoffs','LEGAL OR DATA TROUBLE':'Legal or|data trouble','SALES FELL':'Sales|fell','VALUE FELL':'Value|fell','SOLD OR SHUT':'Sold or|shut'}
for f in glob.glob(R+'*.md'):
    t=open(f).read(); o=t
    def fix2(m):
        i=m.group(1)
        if i not in ('ed199p','ed190'): return m.group(0)
        d=yaml.safe_load(m.group(2))
        if i=='ed190':
            if d.get('status')=='no_data': return m.group(0)
            d={'status':'no_data','reason':'no comparable growth curves of startups by years since founding were found'}
        else:
            d['signs']=[SIGNS.get(s,s) for s in d['signs']]
            for r in d['rows']:
                if 'company' in r:
                    n=r.pop('company'); r['name']=n; r['slug']=re.sub(r'[^a-z0-9]+','-',n.lower()).strip('-'); r['ini']=n[0].upper()
            d.pop('comment',None)
        return '### %s\n```yaml\n%s```'%(i,yaml.safe_dump(d,allow_unicode=True,sort_keys=False,width=1000))
    t=re.sub(r'### (\S+)\n```yaml\n(.*?)```',fix2,t,flags=re.S)
    if t!=o: open(f,'w').write(t)

# round 3: fill and line fixes after the first build
REP=[("They ask clients to install a separate new system","They ask clients to install a separate new system first"),
("They report pilots instead of recurring revenue","They report pilots instead of real recurring revenue"),
("They focus on a single format such as video only","They focus on a single format such as video files only"),
("They make clients leave their usual video tools","They make clients leave their usual video meeting tools"),
("They stay small and wait for buyers to find them","They stay small and wait for big buyers to find them"),
("Gartner named them a Market Shaper and KPMG took a stake","Gartner named them a Market Shaper, KPMG invested"),
("They hire a big team before finding their market","They hire a big team before they find their market"),
("They catch deepfakes live during job interviews","They catch deepfakes live during remote job interviews"),
("They treat each fake account as a separate case","They treat each fake account as a separate new case"),
("They train staff with slides and old phishing tests","They train their staff with slides and old phishing tests"),
("They grow their value slowly, round after round","They grow their value slowly, one round after another"),
("No analyst framework helped buyers\n\n    compare deepfake vendors","No analyst framework\n\n    helped buyers compare vendors"),
("Detection built into every meeting, phone and ID tool by default, as Teams allows","Detection built into every meeting, phone and ID tool, as Teams now allows"),
("Proof that detection cuts losses, like HealthEquity's 90% drop in voice fraud with Pindrop","Proof that detection cuts losses, like HealthEquity's 90% drop in voice fraud")]
for f in glob.glob(R+'*.md'):
    t=open(f).read(); o=t
    for a,b in REP: t=t.replace(a,b)
    if t!=o: open(f,'w').write(t)

# round 4: firm names on one line in the estimates table (the research wrote 'SNS\n\nInsider')
for f in glob.glob(R+'*.md'):
    t=open(f).read(); o=t
    def fix4(m):
        if m.group(1)!='ed042': return m.group(0)
        d=yaml.safe_load(m.group(2))
        for r in d.get('rows',[]): r['firm']=' '.join(str(r['firm']).split())
        return '### %s\n```yaml\n%s```'%(m.group(1),yaml.safe_dump(d,allow_unicode=True,sort_keys=False,width=1000))
    t=re.sub(r'### (\S+)\n```yaml\n(.*?)```',fix4,t,flags=re.S)
    if t!=o: open(f,'w').write(t)
