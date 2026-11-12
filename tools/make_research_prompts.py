"""Research prompts for a new market deck (Pierre, 12 Nov 2026: « donne un nom de marché, reçois les prompts puis le deck »).

    python3 tools/make_research_prompts.py decks/invivo-demo  --uuid 109 --handle in-vivo-car-t --name "in vivo CAR-T" \
        --definition-file /home/claude/nmp-seo/data/startups/market_definitions.csv  --out /home/claude/prompts_invivo

How it works: every slide of the new deck comes from a reference slide of the EdTech deck (same template).
For each slide the prompt shows the EdTech content as the model (same keys, same number of items, about the same length)
and asks the other LLM for the new market's version, sourced. The answer comes back as YAML blocks that go straight into deck.yaml.
Slides filled from our startups database (funding rounds, investors, grids) are not asked. Signal slides have their own prompt.
One TXT per chapter, all in one zip, no README (Pierre's rules for prompts)."""
import argparse, csv, json, re, zipfile, yaml
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
REF = yaml.safe_load((ROOT / 'decks/edtech-full/deck.yaml').read_text())['slides']
REFID = {s['id']: s for s in REF}

SKIP_TYPES = {'agenda', 'cover'}
SKIP_IDS = {'ed002', 'ed003'} | {f'ed{n:03d}' for n in range(215, 222)}
# filled from our startups database (data/startups in nmp-seo): rounds, funding totals, investors, top players by stage
DB_IDS = {'ed156', 'ed157', 'ed158', 'ed159', 'ed160', 'ed162', 'ed164', 'ed165p', 'ed166p', 'ed167', 'ed168p', 'ed169', 'ed171p', 'ed205'}
PAIN_BLOCK = ['ed062', 'ed063', 'ed064', 'ed065']      # divider, who pays, pains, priority: one block per pain segment
VALUE_BLOCK = ['ed106', 'ed107', 'ed108', 'ed109']     # divider, who needs it, maximum value, money flow: one block per value segment
CHAPTERS = [  # (file part, chapter title, sections)
    ('01-market-definition', 'Market definition', ['Market definition']),
    ('02-market-opportunity', 'Market opportunity', ['Market opportunity']),
    ('03-market-size', 'Market size', ['Market size']),
    ('04-pain-points', 'Pain points', ['Pain points']),
    ('05-tech-and-infra', 'Tech and infra', ['Tech and infra']),
    ('06-value-creation', 'Value creation', ['Value creation']),
    ('07-market-challenges', 'Market challenges', ['Market challenges']),
    ('08-growth-drivers', 'Growth drivers', ['Growth drivers']),
    ('09-investor-bets-and-top-players', 'Investor bets and top players', ['Investor bets', 'Top players']),
    ('10-killers-and-strategies', 'Startup killers and startup strategies', ['Startup killers', 'Startup strategies']),
]
DROP_KEYS = {'id', 'type', 'src', 'signal', 'tag', 'img', 'csv', 'handle', 'weight', 'srcs', 'label', 'variant', 'mode', 'pill'}


def key_pos(tpl):
    """box key -> (row, left) read from the template: rows are 30 px bands"""
    f = ROOT / 'templates/slides' / (tpl if tpl.endswith('.j2') else tpl + '.j2')
    if not f.exists(): return {}
    return {int(k): (round(float(t) / 30), float(l)) for k, l, t in re.findall(r'data-k="(\d+)" style="left:([\d.]+)px;top:([\d.]+)px', f.read_text())}

def example(s):
    """the reference content shown to the other LLM: texts and data only, no file paths"""
    def clean(v):
        if isinstance(v, dict): return {k: clean(x) for k, x in v.items() if k not in DROP_KEYS and k != 'src' and k != 'logos'}
        if isinstance(v, list): return [clean(x) for x in v]
        if isinstance(v, str) and (v.endswith('.png') or v.endswith('.jpg')): return '<logo>'
        return v
    e = {k: clean(v) for k, v in s.items() if k not in DROP_KEYS}
    if isinstance(e.get('note'), str): e['note'] = e['note'].replace('DEMO DATA. ', '')
    if s.get('img'): e['logos_on_slide'] = len(s['img'])
    if isinstance(e.get('t'), dict) and str(s.get('type', '')).startswith('x/'):   # keys in reading order (top to bottom, left to right), 12 Nov: the other LLM paired a label with the wrong card
        P = key_pos(s['type'])
        e['t'] = dict(sorted(e['t'].items(), key=lambda kv: P.get(int(kv[0]), (999, 999))))
    if isinstance(e.get('t'), dict):
        e['t'] = {k: v for k, v in e['t'].items() if not re.fullmatch(r'\s*(\d{1,2}|[^\w\s]{1,3}|[✓✕×])\s*', v or '')}   # keep numbers like 1..8 and icons out
    return e


def ylen(e):
    """target length of every text, as a hint: ±15% of the EdTech text"""
    out = {}
    if isinstance(e.get('t'), dict):
        for k, v in e['t'].items(): out[k] = len(re.sub(r'\{\d\|([^}]*)\}', r'\1', v))
    return out


EXTRA = {
    'ed061': 'For {name}: the pain points are split into 3 segments ({pains}). Fill the first 3 items with them and leave the others empty (""); we switch the slide to a 3-item layout.',
    'ed018': 'For this market the categories of companies are the technical approaches: {vals}.',
}
COMMON = """You are a senior market analyst working for NewMarketPitch, which sells market reports to founders and investors.
We are building the {name} market report (a deck of about 180 slides). Every slide uses a fixed design template.
For each slide below we show you the content of the SAME slide in our EdTech report: it is the MODEL of the structure only.
Your job: research the {name} market and write the {name} version of each slide.

MARKET DEFINITION (it decides what is in or out):
{definition}
Categories used in our database: {categories}

HOW TO ANSWER, FOR EVERY SLIDE
1. Same structure as the model: same keys, same number of items, same order. Each text about the same length as the model (the target length in characters is given; stay within ±15%), because the text must fit a fixed box.
   Keep the formatting marks of the model: a line break inside a text is written \\n, and {{1|text}} marks a run in a second style (for example a bold company name followed by normal text). Keep them where the model has them.
2. Content is about {name} only, written for a smart reader who is not an expert: plain US English, short sentences, no jargon without a word of explanation, no em dash, no exclamation marks.
3. Every figure, date, name and claim must be true and sourced. Prefer primary sources: company releases and filings, FDA, ClinicalTrials.gov, peer-reviewed papers, reputable press (Reuters, STAT, Endpoints, Fierce Biotech, BioPharma Dive, Nature Biotechnology). A database such as Crunchbase or PitchBook alone is never a source. Never use newmarketpitch.com.
4. Recent facts first (2025-2026). If something is your own estimate, say "estimate" in the source note and explain how you got it.
5. If you cannot find solid facts for a slide, do NOT invent: return `status: no_data` with one line explaining what is missing, and if possible propose a close alternative angle that can be sourced.
6. The `note` of each slide (the small text at the bottom) says where the data comes from, starting with "We", in one or two plain sentences. Never put a date like "as of" in it.
7. Where the model shows <logo> or logos_on_slide, the slide shows company logos: give the company names and websites in the matching texts or in a `logos:` list, we add the logos ourselves.
8. Titles stay the same as the model, with the market name changed, unless the model title is a fact (then write the {name} fact).

OUTPUT
Deliver ONE downloadable Markdown file named exactly: {fname}
(not a message in the chat). Inside, for each slide, in the order given:

### <slide id>
```yaml
status: ok            # or no_data
title: ...
<same keys as the model>
note: ...
sources:
  - claim: <the figure or fact>
    url: <link>
    date: <publication date>
    quote: <the exact sentence that supports it, under 25 words>
```

Before delivering, check yourself, slide by slide: same number of items as the model, every number has a source with a quote, lengths within ±15%, no EdTech words left (students, schools, teachers, learning…), nothing outside the market definition. Fix what fails, then deliver the file. Do not ask questions; take the most reasonable reading and say it in a `comment:` line when needed.
"""


def block(sid, s, extra=''):
    e = example(s)
    L = ylen(e)
    t = f"### {sid}\n" + ("EdTech model" if sid.startswith("ed") else "Model") + f" (structure only):\n```yaml\n{yaml.dump(e, allow_unicode=True, sort_keys=False, width=200)}```\n"
    if L: t += 'Target lengths in characters per key: ' + ', '.join(f'{k}: ~{v}' for k, v in L.items()) + '\n'
    if extra: t += extra + '\n'
    return t + '\n'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('deck'); ap.add_argument('--uuid'); ap.add_argument('--handle'); ap.add_argument('--name')
    ap.add_argument('--definition-file'); ap.add_argument('--categories-file'); ap.add_argument('--out'); ap.add_argument('--date', default='2026-11-12')
    ap.add_argument('--pain-segments', default=''); ap.add_argument('--value-segments', default='')
    a = ap.parse_args()
    D = yaml.safe_load((ROOT / a.deck / 'deck.yaml').read_text())['slides']
    dfn = [r for r in csv.DictReader(open(a.definition_file)) if r['market_handle'] == a.handle][-1]
    definition = dfn['definition'] + '\nIncluded: ' + dfn['include'] + '\nExcluded: ' + dfn['exclude'] + '\nRule: ' + dfn['decision_rule']
    cats = [r['category'] for r in csv.DictReader(open(a.categories_file)) if r['market_handle'] == a.handle]
    out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
    files = []
    pains = [x.strip() for x in a.pain_segments.split(';') if x.strip()]; vals = [x.strip() for x in a.value_segments.split(';') if x.strip()]
    for part, chap, secs in CHAPTERS:
        fname = f'{a.uuid}-{a.handle}-deck-{part}-results-research-{a.date}.md'
        body = COMMON.format(name=a.name, definition=definition, categories='; '.join(cats), fname=fname)
        body += f'\nCHAPTER: {chap}\n\n'
        seen_block = set(); n = 0
        for s in D:
            sid = s['id']
            if sid in PAIN_BLOCK and chap != 'Pain points': continue
            if sid in VALUE_BLOCK and chap != 'Value creation': continue
            if (s.get('section') or '') not in secs and sid not in PAIN_BLOCK + VALUE_BLOCK: continue
            if sid.startswith('sig_') or s['type'] in SKIP_TYPES or sid in SKIP_IDS or sid in DB_IDS: continue
            if s.get('signal'): continue
            refs = REFID.get(sid) or s                    # iv_* slides: their own demo content is the model
            if sid in PAIN_BLOCK or sid in VALUE_BLOCK:
                blk, segs = (PAIN_BLOCK, pains) if sid in PAIN_BLOCK else (VALUE_BLOCK, vals)
                if tuple(blk) in seen_block: continue
                seen_block.add(tuple(blk))
                body += (f"\nREPEATED BLOCK: the next {len(blk)} slides form one block that we repeat for EACH of these segments: "
                         + '; '.join(segs) + f". Answer the whole block once per segment, with slide ids suffixed by the segment number (e.g. {blk[1]}-s1).\n\n")
                for b in blk: body += block(b, REFID[b]); n += 1
                continue
            if any(sid in (PAIN_BLOCK + VALUE_BLOCK) for _ in [0]): continue
            n0 = int(sid[2:5]) if re.match(r'ed\d{3}', sid) else 0
            if (66 <= n0 <= 73) or (110 <= n0 <= 122): continue    # other copies of the segment blocks
            extra = EXTRA.get(sid, '').format(name=a.name, pains='; '.join(pains), vals='; '.join(vals))
            body += block(sid, refs, extra); n += 1
        p = out / f'{a.uuid}-{a.handle}-deck-{part}.txt'; p.write_text(body); files.append(p)
        print(p.name, n, 'slides', len(body), 'chars')
    # signals: the other LLM screens every format of SIGNALS.md (except the ones computed from our funding database)
    rows = [l for l in (ROOT / 'SIGNALS.md').read_text().splitlines() if l.startswith('| ') and not l.startswith('| format') and not l.startswith('|---')]
    DBF = {'funding-by-region', 'funding-by-segment', 'funding-by-stage', 'funding-share', 'mega-rounds', 'corporate-backers', 'repeat-raisers', 'round-size', 'searches-vs-funding', 'google-trends'}
    fmts = []
    for l in rows:
        c = [x.strip() for x in l.strip('|').split('|')]
        if c[0] not in DBF: fmts.append(f'- **{c[0]}**: {c[1]}. Data: {c[2]}. Usual chapters: {c[3]}. Keep only if: {c[4]}.')
    fname = f'{a.uuid}-{a.handle}-deck-11-signals-results-research-{a.date}.md'
    sig = f"""You are a senior market analyst working for NewMarketPitch, which sells market reports to founders and investors.
We are building the {a.name} market report. Besides its fixed slides, a report gets 5 to 15 "signal" slides: each one shows ONE striking, sourced data point that tells something important about the market (it is hot, it is stuck, a leader is winning, money is moving…). Each signal uses one of the visual formats below.

MARKET DEFINITION (it decides what is in or out):
{definition}

YOUR TASK
1. Explore the {a.name} market widely (trials, approvals, deals, prices, company results, rules, adoption, costs, delays, lobbying, forecasts…) and try EVERY format below. Work like an investigator: for each format, ask "is there a real, sourced, striking case in this market?".
2. Keep only the candidates that pass the "keep only if" condition of their format. Never force a format: no candidate is better than a weak one. A format can give 0, 1 or 2 candidates.
3. For each kept candidate, research it fully in the same pass (all the data points the chart needs, each with its source), so that we can build the slide without any other research.
4. Score each candidate from 1 to 5 on: surprise (would an informed investor learn something?), importance for the market, clarity in 3 seconds, durability (still true in 6 months). Rank them by total score. Aim for 10 to 20 candidates in total; we will keep 5 to 15.

THE FORMATS
""" + '\n'.join(fmts) + f"""

(Funding-round formats are computed by us from our own database: do not research rounds.)

FOR EACH CANDIDATE, RETURN
```yaml
format: <format name>
title: <the striking fact in under 75 characters, a statement, no question, no date words like "lately">
chapter: <where it belongs: Market opportunity, Market size, Pain points, Tech and infra, Value creation, Market challenges, Growth drivers, Investor bets, Top players, Startup killers or Startup strategies>
why_it_matters: <2 plain sentences for the side panel, under 45 words>
data:            # every point of the chart: label, value, unit, date
  - {{label: ..., value: ..., unit: ..., date: ...}}
note: <one or two sentences starting with "We" that say where the data comes from>
scores: {{surprise: 1-5, importance: 1-5, clarity: 1-5, durability: 1-5}}
sources:
  - {{claim: ..., url: ..., date: ..., quote: <exact supporting sentence, under 25 words>}}
```

RULES: plain US English, no em dash; primary sources first (company releases and filings, FDA, ClinicalTrials.gov, papers, reputable press); a database such as Crunchbase or PitchBook alone is never a source; never use newmarketpitch.com; one measure per chart; every number of the title must appear in the data; mark estimates as estimates.
Before delivering, check every candidate against its "keep only if" condition and every number against its quote; drop what fails.

OUTPUT: ONE downloadable Markdown file named exactly {fname} (not a chat message), candidates ranked by total score. Do not ask questions.
"""
    p = out / f'{a.uuid}-{a.handle}-deck-11-signals.txt'; p.write_text(sig); files.append(p); print(p.name, len(fmts), 'formats', len(sig), 'chars')
    z = out / f'{a.uuid}-{a.handle}-deck-research-prompts-{a.date}.zip'
    with zipfile.ZipFile(z, 'w', zipfile.ZIP_DEFLATED) as zf:
        for f in files: zf.write(f, f.name)
    print(z)
    return files


if __name__ == '__main__':
    main()
