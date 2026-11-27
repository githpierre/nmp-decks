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
