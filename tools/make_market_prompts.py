"""Research prompts for a new market deck, with the REFERENCE deck (In Vivo CAR-T, validated by Pierre) as the model.

    python3 tools/make_market_prompts.py --spec plans/humanoid-robotics.yaml --out /home/claude/prompts_humanoid

Structure of the new deck = the reference deck (its final slide list), plus the slides the reference market had to drop for lack of
data (they may have data in the new market), minus:
  - slides Pierre removed on purpose (spec: pierre_dropped),
  - slides filled from our startups database (DB_IDS),
  - product-page twins the new market's live page already gives (spec: live_twins),
  - extra slides (xs_*: they come from the signals prompt), sources slides, dividers, agenda, cover.
Each slide shows the reference content as the MODEL (same keys, same lengths). Slides the reference had to drop show the EdTech model.
Reference-specific slides are re-targeted by the spec (`retarget`: new title and brief, same template).
Files: 10 chapters + 11 signals + 12 startup killers (setbacks), one zip, no README (Pierre's rules for prompts).
"""
import argparse, csv, re, zipfile, yaml
from pathlib import Path
import make_research_prompts as base   # example(), ylen(), SIGNALS screening text
ROOT = Path(__file__).resolve().parent.parent
EDT = {s['id']: s for s in yaml.safe_load((ROOT / 'decks/edtech-full/deck.yaml').read_text())['slides']}
DEMO = [s['id'] for s in yaml.safe_load((ROOT / 'decks/invivo-demo/deck.yaml').read_text())['slides']]
DB_IDS = base.DB_IDS
KILLERS = ['ed192', 'ed195', 'ed199p', 'ed200', 'ed201']
PAIN, VALUE = ['ed062', 'ed063', 'ed064', 'ed065'], ['ed106', 'ed107', 'ed108', 'ed109']


def structure(ref, spec):
    """ordered slide ids of the new deck (reference order, dropped-for-data slides put back at their demo place)"""
    ids = [s['id'] for s in ref]
    for sid in spec.get('reask', []):
        if sid in ids: continue
        i = DEMO.index(sid); prev = next((p for p in reversed(DEMO[:i]) if p in ids), None)
        ids.insert(ids.index(prev) + 1 if prev else 0, sid)
    return ids


EXKEYS = ['jargon_bad', 'jargon_good', 'jargon_why', 'proof_rule', 'proof_bad', 'proof_good', 'proof_why', 'fresh_bad', 'fresh_good', 'fresh_est', 'fresh_method', 'not_proof']


def examples(spec):
    """Bad / good examples of the prompts, written for THIS market in the spec (`examples:`). No default: a default would carry
    another market's words into every prompt (13 Nov 2026: robot examples left in the tool when Healthcare AI started)."""
    X = spec.get('examples') or {}; miss = [k for k in EXKEYS if not X.get(k)]
    if miss: raise SystemExit(f'spec: examples missing {miss} (write them for this market, see plans/humanoid-robotics.yaml)')
    return X


def common(spec, fname, chapter):
    m, ref = spec['name'], spec['model_name']; X = examples(spec)
    return f"""You are a senior market analyst working for NewMarketPitch, which sells market reports to founders and investors.
We are building the {m} market report (a deck of about 190 slides). Every slide uses a fixed design template.
For each slide below we show you the content of the SAME slide in our {ref} report: it is the MODEL of the structure and of the tone only.
Your job: research the {m} market and write the {m} version of each slide. Today is {spec['today']}.

MARKET DEFINITION (it decides what is in or out):
{spec['definition']}
Categories of companies used in our database: {spec['categories']}

HOW TO ANSWER, FOR EVERY SLIDE
1. Same structure as the model: same keys, same number of items, same order. Each text at most the length given in characters (and not much shorter), because it must fit a fixed box: a longer text breaks the slide. Count before you deliver.
   Keep the formatting marks of the model: a line break inside a text is written \\n, and {{1|text}} marks a run in a second style (for example a bold company name followed by normal text). Keep them where the model has them. Keys that hold a single emoji are icons: give one fitting emoji.
   The length rule is for sentences. A name (company, product, person, acronym) is written as it is, never padded or cut to reach a length.
   Bad: \"ABRIDGE AI NOTES\", \"Aidoc AI\" (words added to a company name). Good: \"ABRIDGE\", \"Aidoc\".
2. Content is about {m} only, written for a smart reader who is not an expert: plain US English, short sentences, no jargon without a word of explanation, no em dash, no exclamation marks.
   Bad: "{X['jargon_bad']}" Good: "{X['jargon_good']}" ({X['jargon_why']})
3. Every figure, date, name and claim must be true and sourced. Prefer primary sources: {spec['sources_hint']} A database such as Crunchbase or PitchBook alone is never a source. Never use newmarketpitch.com. The url is the exact page that carries the quote, never a homepage (« https://www.sec.gov » proves nothing), and the quote is copied word for word from it.
4. Recent facts first (2025-2026). {X['proof_rule']}
   Bad: "{X['proof_bad']}" Good: "{X['proof_good']}" ({X['proof_why']})
5. Money is written the way people say it: $285M, $4.2B, never $0.285B.
6. If you cannot find solid facts for a slide, do NOT invent: return `status: no_data` with one line explaining what is missing. A slide that cannot be filled completely is removed, so never leave half the items empty.
7. The `note` of each slide (the small text at the bottom) says where the data comes from, starting with "We", in one or two plain sentences. Never put a date like "as of" in it. The note speaks to the reader of the report: never mention this prompt, the model slide, the segments you were given or the length limits.
8. Where the model shows <logo> or logos_on_slide, the slide shows company logos: give the company names and their website domains in a `logos:` list, we add the logos ourselves. Company names are never shortened.
9. Titles stay the same as the model, with the market name changed, unless the model title is a fact (then write the {m} fact). Titles are questions people would ask, not analyst wording.

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

Before delivering, check yourself, slide by slide: same number of items as the model, every number has a source with a quote, every text between 80% and 100% of its length, no semicolon (two sentences instead), contrast slides ("How X…") with exactly 8 rows, no {ref} words left ({spec['model_words']}), nothing outside the market definition, the same category names everywhere. Fix what fails, then deliver the file. Do not ask questions; take the most reasonable reading and say it in a `comment:` line when needed.

CHAPTER: {chapter}

"""


LIMS = {}                      # slide id -> {key: length}, filled by block() and written into the self-check of each file


def selfcheck(fname):
    """The other LLM checks its own file before delivering (Pierre, 13 Nov 2026: the fit to the boxes is done by the research, not by
    Claude afterwards). A script, not a wish: it prints every text out of its range and the delivery waits for « 0 problems »."""
    import json
    t = (ROOT / 'tools/selfcheck_template.txt').read_text().replace('__LIMITS__', json.dumps({k: {str(a): b for a, b in v.items()} for k, v in LIMS.items() if v})).replace('__FNAME__', fname)
    LIMS.clear(); return t


def block(sid, model, src, extra=''):
    e = base.example(model); L = base.ylen(e); LIMS[sid] = L
    t = f"### {sid}\n{src} model (structure only):\n```yaml\n{yaml.dump(e, allow_unicode=True, sort_keys=False, width=200)}```\n"
    if L: t += 'Length in characters per key, between 80% and 100% of: ' + ', '.join(f'{k}: {v}' for k, v in L.items()) + ' (a text much shorter leaves its box half empty: add one concrete fact rather than filler words)\n'
    if extra: t += extra.strip() + '\n'
    return t + '\n'


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--spec'); ap.add_argument('--out'); a = ap.parse_args()
    spec = yaml.safe_load((ROOT / a.spec).read_text())
    ref = yaml.safe_load((ROOT / spec['model_deck'] / 'deck.yaml').read_text())['slides']; R = {s['id']: s for s in ref}
    dfn = [r for r in csv.DictReader(open(spec['definition_file'])) if r['market_handle'] == spec['handle']][-1]
    spec['definition'] = dfn['definition'] + '\nIncluded: ' + dfn['include'] + '\nExcluded: ' + dfn['exclude'] + '\nRule: ' + dfn['decision_rule']
    spec['categories'] = '; '.join(r['category'] for r in csv.DictReader(open(spec['categories_file'])) if r['market_handle'] == spec['handle'])
    ids = structure(ref, spec)
    skip = set(spec.get('pierre_dropped', [])) | set(spec.get('live_twins', [])) | DB_IDS
    pains, vals = spec['pain_segments'], spec['value_segments']
    out = Path(a.out); out.mkdir(parents=True, exist_ok=True); files, asked = [], []
    RT = spec.get('retarget', {}); EX = {k: v.format(pains='; '.join(pains), vals='; '.join(vals), np=len(pains), nv=len(vals)) for k, v in spec.get('extra', {}).items()}

    def model_of(sid):
        if sid in R: return R[sid], spec['model_name']
        return EDT[sid], 'EdTech'

    for part, chap, secs in base.CHAPTERS + [('12-startup-killers', 'Startup killers (setbacks)', [])]:
        fname = f"{spec['uuid']}-{spec['handle']}-deck-{part}-results-research-{spec['date']}.md"
        body = common(spec, fname, chap); n = 0
        if part == '12-startup-killers':
            body += spec['killers_brief'].strip() + '\n\n'
        done_blk = set()
        for sid in ids:
            s = R.get(sid) or EDT.get(sid)
            if s is None: continue
            root = sid.split('-s')[0] if re.match(r'ed\d{3}-s\d', sid) else sid
            sec = s.get('section') or ''
            in_ch = (sid in KILLERS) if part == '12-startup-killers' else (sec in secs and sid not in KILLERS)
            if root in PAIN: in_ch = chap == 'Pain points'
            if root in VALUE: in_ch = chap == 'Value creation'
            if not in_ch: continue
            if sid.startswith(('xs_', 'src_', 'sig_')) or s['type'] in base.SKIP_TYPES or root in skip or sid in skip: continue
            if s['type'].startswith('x/divider') and root not in PAIN + VALUE: continue
            if root in PAIN + VALUE:
                blk, segs = (PAIN, pains) if root in PAIN else (VALUE, vals)
                if tuple(blk) in done_blk: continue
                done_blk.add(tuple(blk))
                body += (f"\nREPEATED BLOCK: the next {len(blk)} slides form one block that we repeat for EACH of these {len(segs)} segments: "
                         + '; '.join(f'{i}. {x}' for i, x in enumerate(segs, 1)) + f". Answer the whole block once per segment, with slide ids suffixed by the segment number ({blk[1]}-s1 … {blk[1]}-s{len(segs)}). The segment name is written exactly the same way everywhere.\n\n")
                for b in blk:
                    m_, src = model_of(b + '-s1'); body += block(b, m_, src, EX.get(b, '')); n += 1; asked.append(b)
                continue
            m_, src = model_of(sid)
            extra = EX.get(sid, '')
            if sid in RT:
                m_ = dict(m_, title=RT[sid]['title']); extra = ('THIS SLIDE IS RE-TARGETED for this market (same template, new subject): ' + RT[sid]['brief'] + '\n' + extra)
            body += block(sid, m_, src, extra); n += 1; asked.append(sid)
        body += selfcheck(fname)
        p = out / f"{spec['uuid']}-{spec['handle']}-deck-{part}.txt"; p.write_text(body); files.append(p)
        print(f'{p.name}: {n} slides, {len(body)} chars')
    # signals: same screening as the reference market, market text swapped
    files.insert(10, write_signals(spec, out))
    z = out / f"{spec['uuid']}-{spec['handle']}-deck-research-prompts-{spec['date']}.zip"
    with zipfile.ZipFile(z, 'w', zipfile.ZIP_DEFLATED) as zf:
        for f in files: zf.write(f, f.name)
    print(z, len(files), 'files;', len(asked), 'slides asked')


def write_signals(spec, out):
    rows = [l for l in (ROOT / 'SIGNALS.md').read_text().splitlines() if l.startswith('| ') and not l.startswith('| format') and not l.startswith('|---')]
    DBF = {'funding-by-region', 'funding-by-segment', 'funding-by-stage', 'funding-share', 'mega-rounds', 'corporate-backers', 'repeat-raisers', 'round-size', 'searches-vs-funding', 'google-trends'}
    fmts = []
    for l in rows:
        c = [x.strip() for x in l.strip('|').split('|')]
        if c[0] not in DBF: fmts.append(f'- **{c[0]}**: {c[1]}. Data: {c[2]}. Usual chapters: {c[3]}. Keep only if: {c[4]}.')
    m = spec['name']; fname = f"{spec['uuid']}-{spec['handle']}-deck-11-signals-results-research-{spec['date']}.md"; X = examples(spec)
    txt = f"""You are a senior market analyst working for NewMarketPitch, which sells market reports to founders and investors.
We are building the {m} market report. Today is {spec['today']}. Besides its fixed slides, a report gets 5 to 15 extra slides: each one shows ONE striking, sourced data point that tells something important about the market (it is hot, it is stuck, a leader is winning, money is moving…). Each one uses one of the visual formats below.

MARKET DEFINITION (it decides what is in or out):
{spec['definition']}

YOUR TASK
1. Explore the {m} market widely and try EVERY format below. Work like an investigator: for each format, ask "is there a real, sourced, striking case in this market?". Angles worth checking in this market: {spec['signal_angles']}
2. Keep only the candidates that pass the "keep only if" condition of their format. Never force a format: no candidate is better than a weak one. A format can give 0, 1 or 2 candidates.
3. For each kept candidate, research it fully in the same pass (all the data points the chart needs, each with its source), so that we can build the slide without any other research.
4. Score each candidate from 1 to 5 on: surprise (would an informed investor learn something?), importance for the market, clarity in 3 seconds, durability (still true in 6 months). Rank them by total score. Aim for 12 to 20 candidates; we keep 6 to 15. Market opportunity needs 6 to 8 of them that show why the market is hot right now.
5. Freshness of the "hot right now" candidates (today is {spec['date']}). A figure that shows momentum must be recent: a monthly figure at most 6 months old, a quarterly figure at most 3 quarters old, a half-year figure at most 12 months old, a yearly figure for the current year only (last year is accepted until April).
   Bad: "{X['fresh_bad']}" written in {spec['today'].split(' ', 1)[1]} (a year old, the reader wonders what happened since).
   Good: "{X['fresh_good']}" (latest published period, same period a year before).
   Good: "{X['fresh_est']}" with the method in the note ({X['fresh_method']}). When only last year's figure exists as a total, look for the latest quarterly or half-year filing and derive the current-year estimate yourself; say "should" and give the arithmetic.
   Add to each candidate `fresh: {{period: month|quarter|half|year|total, end: YYYY-MM}}` (total = a cumulative proof at a date, at most 12 months old).

THE FORMATS
""" + '\n'.join(fmts) + f"""

(Funding-round formats are computed by us from our own database: do not research funding rounds.)

FOR EACH CANDIDATE, RETURN
```yaml
format: <format name>
title: <the striking fact in under 75 characters, a statement, no question; say "recent" rather than "since 2024">
chapter: <Market opportunity, Market size, Pain points, Tech and infra, Value creation, Market challenges, Growth drivers, Investor bets, Top players, Startup killers or Startup strategies>
why_it_matters: <2 plain sentences, under 45 words; for Market opportunity, the first sentence says why it shows the market is hot>
data:            # every point of the chart: label, value, unit, date
  - {{label: ..., value: ..., unit: ..., date: ...}}
note: <one or two sentences starting with "We" that say where the data comes from and the exact period>
scores: {{surprise: 1-5, importance: 1-5, clarity: 1-5, durability: 1-5}}
sources:
  - {{claim: ..., url: ..., date: ..., quote: <exact supporting sentence, under 25 words>}}
```

RULES: plain US English, no em dash; primary sources first ({spec['sources_hint']}); a database such as Crunchbase or PitchBook alone is never a source; never use newmarketpitch.com; {X['not_proof']}; one measure per chart; every number of the title must appear in the data; money written $285M, $4.2B; mark estimates as estimates.
Before delivering, check every candidate against its "keep only if" condition and every number against its quote; drop what fails.

OUTPUT: ONE downloadable Markdown file named exactly {fname} (not a chat message), candidates ranked by total score. Do not ask questions.
"""
    p = out / f"{spec['uuid']}-{spec['handle']}-deck-11-signals.txt"; p.write_text(txt); print(p.name, len(fmts), 'formats', len(txt), 'chars'); return p


if __name__ == '__main__':
    main()
