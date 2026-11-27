import re,yaml,glob
R='/home/claude/nmp-decks/decks/quantum-sensing/research/'
# round 1 (27 Nov 2026): warning-signs grid in the shape of the reference (rows with name, slug, ini; two-line headers), US spelling
SIGNS={'INSOLVENCY':'Went|insolvent','SALES FELL':'Sales|fell','SHARES FELL':'Shares|fell','DEBT STRESS':'Debt|stress','LEGAL FIGHT':'Legal|fight'}
for f in glob.glob(R+'*.md'):
    t=open(f).read(); o=t
    def fix(m):
        i=m.group(1)
        if i!='ed199p': return m.group(0)
        d=yaml.safe_load(m.group(2))
        if 'companies' in d:
            d['signs']=[SIGNS.get(s,s) for s in d['signs']]
            rows=[]
            for c in d.pop('companies'):
                n=c['name']; rows.append({'name':n,'slug':re.sub(r'[^a-z0-9]+','-',n.lower()).strip('-'),'domain':c['domain'],'ini':n[0].upper(),'cells':c['cells']})
            d['rows']=rows; d.pop('comment',None)
        return '### %s\n```yaml\n%s```'%(i,yaml.safe_dump(d,allow_unicode=True,sort_keys=False,width=1000))
    t=re.sub(r'### (\S+)\n```yaml\n(.*?)```',fix,t,flags=re.S)
    t=t.replace('booked realised losses','booked realized losses')
    if t!=o: open(f,'w').write(t)

# round 2: the signals file has plain YAML values with ': ' inside (note of candidate 5), which do not parse: quote them
import json
f=glob.glob(R+'*11-signals*')[0]; t=open(f).read(); o=t
def q(m):
    k,v=m.group(1),m.group(2)
    if v[:1] in '"\'{[' or ': ' not in v: return m.group(0)
    return k+': '+json.dumps(v,ensure_ascii=False)
t=re.sub(r'(?m)^(note|why_it_matters|title): (.*)$',q,t)
if t!=o: open(f,'w').write(t)

# round 3 (first build): fill, line counts and split words
REP=[("23: Classical sensors and AI navigation keep getting better and cheaper too","23: Classical sensors and AI-based navigation keep getting better too"),
("23: Classical sensors and AI-based navigation keep getting better\n","23: Classical sensors and AI-based navigation keep getting better too\n"),
("They test their sensors only on quiet lab benches","They only ever test their sensors on quiet lab benches"),
("They build computers, clocks and radio sensors on one platform","They build computers, clocks and RF sensors on one base"),
("They wait years for a first government customer","They wait many years for a first government customer"),
("Their systems are used by the US Department of War and NASA","Their systems serve the US Department of War and NASA"),
("They burn cash and borrow to keep the lights on","They burn cash and borrow money to keep the lights on"),
("They use AI software to keep quantum sensors steady in motion","Their AI software keeps quantum sensors steady in motion"),
("They wait years for their first defense contract","They wait many years for their first defense contract"),
("They build a sensor first and look for a use later","They build a sensor first and look for a use only later"),
("They take years to land a first paying customer","They take many years to land a first paying customer"),
("Capital is flowing. Q-CTRL raised $290M, CIQTEK listed and QuantumDiamonds won €91M.","Capital is flowing. Q-CTRL raised $290M at a $1B+ value, CIQTEK listed and Thales bid $4.5B for Exail."),
("21: Big, heavy units fixed to one room","21: Big, heavy units fixed to one lab room for good"),
("SandboxAQ spun out of Alphabet and QuantumDiamonds launched. DIU started field tests, and Infleqtion flew a quantum clock on a jet.","SandboxAQ spun out of Alphabet, DIU started field tests of quantum sensors, and Infleqtion flew a quantum clock on a jet."),
('"QUALIFICATION\\n\\n\\nTesters','"SAFETY TESTS\\n\\n\\nTesters'),
('"PRODUCTION DEAL\\n\\n\\nThe buyer','"BIG ORDERS\\n\\n\\nThe buyer')]
for f in glob.glob(R+'*.md'):
    t=open(f).read(); o=t
    for a,b in REP: t=t.replace(a,b)
    if t!=o: open(f,'w').write(t)

# round 4: no 2-decimal amounts on slides (check_results « amount format »)
for f in glob.glob(R+'*08-growth*'):
    t=open(f).read(); o=t.replace("Thales bid $4.45B for Exail.","Thales bid $4.5B for Exail.")
    if t!=o: open(f,'w').write(o)

# round 5 (visual pass): one date per deal across the deck (Qnami: June 2026 everywhere), no NVision amount that contradicts
# the base ($38M in the base, $55M in NVision's release: signaled to Pierre), Vector Atomic price is known (6.3M IonQ shares)
REP5=[('  18: 2026 (MAY)\n  19: "Quantum Design bought Qnami','  18: 2026 (JUN)\n  19: "Quantum Design bought Qnami'),
('"Abbott anchored a $55M Series B in NVision, a German startup using quantum physics to boost MRI signals, for $120M raised {1|Abbott}"','"Abbott anchored the Series B of NVision, a German startup that uses quantum physics to boost the signals of MRI scanners {1|Abbott}"'),
('NVision got Abbott to anchor a $55M round for its quantum-boosted MRI','NVision got Abbott to anchor its Series B for quantum-boosted MRI'),
("Some deals, such as IonQ's purchase of Vector Atomic, did not disclose a price.","Some deals, such as Quantum Design's purchase of Qnami, did not disclose a price.")]
for f in glob.glob(R+'*.md'):
    t=open(f).read(); o=t
    for a,b in REP5: t=t.replace(a,b)
    if t!=o: open(f,'w').write(t)

# round 6: the newcomers curve label still reached x=54 at 66 characters
for f in glob.glob(R+'*07-market*'):
    t=open(f).read(); o=t.replace("23: Classical sensors and AI-based navigation keep getting better too\n","23: Classical sensors and AI navigation keep getting better\n")
    if t!=o: open(f,'w').write(o)
