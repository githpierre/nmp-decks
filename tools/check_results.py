"""Check research result files (the other LLM's, or the evergreen chapters Claude writes) against specs/slides.yaml before importing.

    python3 tools/check_results.py <model deck> <result.md> [...]      e.g. decks/in-vivo-car-t decks/x/research/*.md

Same checks as the self-check given to the research LLM: lengths, words, em dash, semicolon, amount format. Prints « N problems »."""
import re, sys, yaml
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent)); import spec
ROOT = Path(__file__).resolve().parent.parent
model = {s['id']: s for s in yaml.safe_load((ROOT / sys.argv[1] / 'deck.yaml').read_text())['slides']}
F = chr(96) * 3; n = 0; nr = 0
# titles copied from the model that few other full decks share are often about the model's market (Neocloud, 19 Nov 2026:
# ed140 kept « Where do developers, doctors and regulators clash? » from In Vivo CAR-T and no check saw it)
_others = {}
for _p in ROOT.glob('decks/*/deck.yaml'):
    if _p.parent.name == Path(sys.argv[1]).name or 'demo' in _p.parent.name: continue
    try:
        for _t in {x.get('title') for x in yaml.safe_load(_p.read_text())['slides'] if isinstance(x, dict)}: _others[_t] = _others.get(_t, 0) + 1
    except Exception: pass
for f in sys.argv[2:]:
    for sid, body in re.findall(r'### (\S+)\s+' + F + r'yaml\n(.*?)' + F, Path(f).read_text(), re.S):
        d = yaml.safe_load(body) or {}
        if d.get('status') != 'ok': continue
        m = model.get(sid) or model.get(re.sub(r'-s\d+$', '-s1', sid)) or {}
        d['type'] = d.get('type') or m.get('type')
        P = [p for p in spec.problems(d, sid) if 'capitals' not in p]
        flat = yaml.dump(d, allow_unicode=True)
        P += [f'{sid} | {w}' for c, w in ((chr(8212), 'em dash'), (chr(8211), 'en dash'), ('; ', 'semicolon')) if c in flat]
        # the slides are in US English (Natural hydrogen, 21 Nov 2026: « modelled » on ed093); quotes stay as the source wrote them
        _brit = re.compile(r'\b(model|label|travel|cancel|fuel|signal|channel)l(ed|ing|er|ers)\b|\b\w*(organi|reali|recogni|speciali|prioriti|optimi|commerciali|industriali|utili|capitali|moneti|minimi|maximi|standardi|digiti|categori|summari|stabili|mobili|centrali|decentrali|normali|moderni|globali|subsidi|incentivi|scrutini|synthesi|characteri|emphasi|customi|localis|financiali)s(e|ed|es|ing|ation|ations)\b|\banalys(e|ed|es|ing)\b|\b(colour|favour|behaviour|centre|metre|litre|programme|labour|defence|licence|catalogue)s?\b')   # lower case only: a proper name keeps its spelling (« Petroleum Exploration Licence », South Australia)
        def _noq(x):   # quotes stay as the source wrote them, at any depth (FemTech survivors, 26 Nov 2026: a nested source quote said « cancelled »)
            if isinstance(x, dict): return {k: _noq(v) for k, v in x.items() if k not in ('sources', 'source', 'quote')}
            if isinstance(x, list): return [_noq(v) for v in x]
            return x
        P += [f'{sid} | British spelling, write US English | {w.group(0)}' for w in _brit.finditer(yaml.dump(_noq(d), allow_unicode=True))]
        # an estimates value is the amount alone: « $39M 2024 » looked ugly, the year goes in the comment (Pierre, Natural hydrogen, 21 Nov 2026)
        P += [f'{sid} | estimates value with a year, put the year in the comment | {r.get("value")}' for r in (d.get('rows') or []) if isinstance(r, dict) and re.search(r'\b(19|20)\d\d\b', str(r.get('value', '')))]
        # quotes are copied word for word from the source: $2.57B there is right (AI drug discovery, 20 Nov 2026)
        flat_nq = yaml.dump({**d, 'sources': [{k: v for k, v in so.items() if k != 'quote'} for so in d.get('sources') or [] if isinstance(so, dict)]}, allow_unicode=True)
        P += [f'{sid} | amount format {a}' for a in re.findall(r'\$\d+\.\d{2,}[BMK]|\$\d{2,}\.\d[B]|\$\d+\.0[BMK]|\d+\.\d{2,}%', flat_nq)]
        # a label the model writes on two lines needs two words (RULES « a one-word label gets a second word »): the build only
        # saw it as LABEL_LINES after a 4-min run (Neocloud, 19 Nov 2026: FOUNDERS, COMPANIES, NVIDIA, HYPERSCALERS…)
        mt, dt = m.get('t') or {}, d.get('t') or {}
        P += [f'{sid} {k} | one-word label where the model has two lines: add a second word | {v}' for k, v in dt.items()
              if isinstance(v, str) and '\n' in str(mt.get(k, mt.get(str(k), ''))) and len(v.split()) == 1 and v.strip() and v == v.upper() and v.strip().isalpha()]
        # the reference market's name left in a text (MedTech, 23 Nov 2026: « Which bold bets could reshape in vivo CAR-T? »): the import
        # already stops it (MODEL MARKET LEFT), but it must fail here, before the import, not show as a REVIEW line
        flat_nsrc = yaml.dump({k: v for k, v in d.items() if k not in ('sources', 'comment')}, allow_unicode=True)
        P += [f'{sid} | reference market name left: {w}' for w in ('in vivo CAR-T', 'CAR-T') if w.lower() in flat_nsrc.lower()][:1]
        R = []
        if d.get('title') and d.get('title') == m.get('title') and _others.get(d['title'], 0) <= 3:
            R.append(f"REVIEW {sid} | title kept from the model, is it about this market? | {d['title']}")
        # a capital-letters header sits above the text of the key just before it (x/startups_stand_out: 19 over 18, 23 over 22):
        # print each pair so a swapped pair shows (Neocloud ed175: COREWEAVE sat over Fireworks' $1B run rate)
        for k, v in (dt.items() if d['type'] in ('x/startups_stand_out',) else ()):
            mv = str(mt.get(k, '')); prev = mt.get(k - 1) if isinstance(k, int) else None
            if isinstance(v, str) and v.isupper() and mv.isupper() and isinstance(prev, str) and not prev.isupper() and (k - 1) in dt \
                    and not re.search(r'\d', v) and v.split()[0].lower() not in str(dt[k - 1]).lower():
                R.append(f"REVIEW {sid} pair | {v} over: {dt[k - 1]}")
        # stronger: the source whose claim/quote shares a code or figure with the text (REC-4881, IAM1363, $40M) names a company
        # in its link; if that company is another header of the slide, the pair is swapped (AI drug discovery ed175, 20 Nov 2026)
        if d['type'] in ('x/startups_stand_out',):
            heads = {k: re.sub(r'[^a-z0-9]', '', str(v).lower()) for k, v in dt.items() if isinstance(v, str) and v.isupper() and (k - 1) in dt}
            for k, h in heads.items():
                toks = set(re.findall(r'[A-Z]{2,}-?\d+|\$[\d.,]+[MBK]?', str(dt[k - 1])))
                for so in d.get('sources') or []:
                    if toks & set(re.findall(r'[A-Z]{2,}-?\d+|\$[\d.,]+[MBK]?', f"{so.get('claim', '')} {so.get('quote', '')}")):
                        url = re.sub(r'[^a-z0-9]', '', str(so.get('url', '')).lower())
                        other = [heads[o] for o in heads if o != k and heads[o] and heads[o] in url]
                        if h in url: R = [r for r in R if not r.startswith(f"REVIEW {sid} pair | {dt[k]} over")]
                        if other and h not in url:
                            P.append(f"{sid} {k} | header {dt[k]} sits over a text whose source is about {other[0].upper()}: swap the headers | {dt[k - 1]}")
                        break
        for p in P + R: print(p)
        n += len(P); nr += len(R)
# the same round written two ways in two chapters (Natural hydrogen, 21 Nov 2026: Koloma « $245M » on 3 slides, « $246M » on 6):
# amounts of one company within 3% of each other are one round rounded differently. Quotes and claims are left out.
_amt = {}
for f in sys.argv[2:]:
    for sid, body in re.findall(r'### (\S+)\s+' + F + r'yaml\n(.*?)' + F, Path(f).read_text(), re.S):
        d = yaml.safe_load(body) or {}
        txt = yaml.dump({k: v for k, v in d.items() if k != 'sources'}, allow_unicode=True)
        for co, v, u in re.findall(r'\b([A-Z][A-Za-z0-9]+)\b[^.$]{0,40}?\braised (?:a |an |about |over |nearly )?[$€]([\d.]+)([MB])', txt):
            _amt.setdefault(co, {}).setdefault(float(v) * (1000 if u == 'B' else 1), set()).add(sid)
for co, vs in _amt.items():
    ks = sorted(vs)
    for a_, b_ in zip(ks, ks[1:]):
        if a_ != b_ and (b_ - a_) / b_ <= 0.03:
            print(f"{co} | one round written two ways: ${a_:g}M ({', '.join(sorted(vs[a_]))}) and ${b_:g}M ({', '.join(sorted(vs[b_]))}): use one figure"); n += 1
print(n, 'problems,', nr, 'to review by eye (REVIEW lines)')
