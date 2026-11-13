"""Database slides of a market deck (Investor bets, top rounds, top investors), from the latest nmp-seo startups base.

    python3 tools/make_db_slides.py <handle> --name "humanoid robotics" [--today 2026-11-12]   -> decks/<handle>/db.yaml

Rules (RULES.md, Content): equity rounds only (no IPO, debt, grants), complete since January 2024, rounds with no public
amount count as zero and the notes say so. Keys and shapes follow the reference deck (decks/in-vivo-car-t/db.yaml).
Product-page twins (ed168p, ed171p) are not written here: they copy the live page (live.yaml).
Texts that need judgment (ed162 before/after) are written in edits.yaml after reading the printed figures."""
import sys as _s, pathlib as _p; _s.path.insert(0, str(_p.Path(__file__).resolve().parent))
import argparse, collections, re, statistics as st, sys, yaml
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, '/home/claude/nmp-seo/outils/startups'); sys.path.insert(0, str(ROOT / 'tools'))
import gen_lib as g
_src = (ROOT / 'tools/build_sources.py').read_text()          # publisher names (PUB, pub) without running build_sources
exec(_src[_src.index('PUB = {'):_src.index('def title(')])


def money(v):
    if v >= 1e9: return f'${v / 1e9:.1f}B'.replace('.0B', 'B')
    if v >= 1e7: return f'${v / 1e6:.0f}M'
    return f'${v / 1e6:.1f}M'.replace('.0M', 'M')


def poss(n): return n + ('’' if n.endswith('s') else '’s')      # « Isomorphic Labs’ $2.1B », « Sail’s $465M »


def stage(r):
    t = r['round_type'] or ''
    return '' if t in ('Unknown', 'Other', '') else t.replace('Series D+', 'late-stage')


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('handle'); ap.add_argument('--name'); ap.add_argument('--today', default='2026-11-12')
    a = ap.parse_args(); H, N, today = a.handle, a.name, a.today
    b = g.Base(); M = {m['company_id']: m for m in b.markets[H]}
    R = []
    for cid, m in M.items():
        for r in g.rounds_for(b, cid, 'deals'):
            if (r['round_type'] or '').upper() == 'IPO' or 'IPO' in (r['round_label'] or ''): continue   # equity rounds only, never a listing
            R.append(dict(r, name=b.companies[cid]['name'], what=m.get('what_they_do') or '', cat=m.get('category') or '', country=b.companies[cid]['hq_country'], amt=float(r['amount_usd'] or 0)))
    R.sort(key=lambda r: r['date'])
    tot = sum(r['amt'] for r in R); D = {}
    year_ago = f'{int(today[:4]) - 1}{today[4:]}'
    print(f'{len(R)} equity rounds since 2024, {money(tot)}; base covers to', max(r['date'] for r in R))

    def sentence(r):
        """« Tutor Intelligence raised a $75M Series B led by Andreessen Horowitz for its industrial and factory humanoids {1|Business Wire} »"""
        lead = (r['lead_investors'] or '').split(';')[0].strip(); st_ = stage(r)
        if st_ and not st_.startswith('Series'): st_ = st_.lower() + ' round'          # « a $787M growth equity round », never « a $787M Growth Equity » (13 Nov 2026)
        if r['amt']: s = f"{r['name']} raised {'a ' + money(r['amt']) + ' ' + st_ if st_ else money(r['amt'])}"
        else: s = f"{r['name']} raised an undisclosed {st_ or 'round'}"
        if lead: s += f' led by {lead}'
        w_ = (r.get('what') or '').strip().rstrip('.')   # what the company does (markets.csv), so the reader learns something (Pierre, 14 Nov 2026: rows 30-40% too short)
        lw = lambda x: ' '.join(t if (t.isupper() or any(c.isupper() for c in t[1:])) else t.lower() for t in x.split())
        verb = bool(re.match(r'^(Builds|Develops|Combines|Uses|Makes|Designs|Provides|Offers|Creates|Runs|Helps|Turns|Applies)\b', w_))
        lim = 140 - len(pub(r['source_url']))   # two lines at most, source label included
        while w_ and len(s) + len(w_) >= lim:                     # too long: cut at the last « and », « for », « to », comma
            cut = max(w_.rfind(x) for x in (' and ', ' for ', ' to ', ', ', ' with '))
            w_ = w_[:cut] if cut > 15 else ''
        if w_ and verb: s += '. It ' + lw(w_)
        elif w_: s += ' for its ' + lw(w_)
        elif r['cat'] and len(s) + len(r['cat']) < 100: s += ' for its ' + ' '.join(w if w.isupper() else w.lower() for w in r['cat'].split())   # « life science AI », not « life Science AI »
        p_ = pub(r['source_url']); key = re.sub(r'[^a-z0-9]', '', r['name'].lower())
        lab = re.sub(r'[^a-z0-9]', '', site_label(r['source_url']))
        if p_.lower()[:5] == key[:5] or (len(lab) >= 4 and (key.startswith(lab) or lab.startswith(key))) or 'pr.co' in r['source_url']: p_ = r['name'].split()[0]   # a company's own site, blog or press page: name the company
        elif p_ not in PUB.values() and p_.lower() not in (r['lead_investors'] or '').lower(): print('PUBLISHER UNKNOWN', r['source_url'][:70], '->', p_)   # shown on a slide: add its name to PUB (tools/build_sources.py)
        return s + f" {{1|{p_}}}"
    def dl(d): return f"{d[:4]} ({['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC'][int(d[5:7]) - 1]})"

    last = sorted(R, key=lambda r: r['date'], reverse=True)[:12]; floor = ''
    if sum(1 for r in last if 0 < r['amt'] < 1e7) > 6:      # a busy market: most of the 12 latest rounds are small rounds of unknown startups (Healthcare AI, 13 Nov 2026).
        last = sorted([r for r in R if r['amt'] >= 1e7], key=lambda r: r['date'], reverse=True)[:12]; floor = ' of $10M or more'   # Pierre: the 12 latest of $10M or more, and the note says so
    D['ed156'] = {k: v for i, r in enumerate(last[:6]) for k, v in ((13 + 2 * i, dl(r['date'])), (14 + 2 * i, sentence(r)))}
    D['ed156']['note'] = f'We list the latest equity rounds{floor} of {N} startups in our tracker, from company releases and the press.' + ('' if floor else ' Undisclosed means no amount was made public')
    D['ed157'] = {k: v for i, r in enumerate(last[6:12]) for k, v in ((14 + 2 * i, dl(r['date'])), (15 + 2 * i, sentence(r)))}
    D['ed157']['note'] = D['ed156']['note']

    def ann(rs):
        rs = sorted(rs, key=lambda r: -r['amt']); s = sum(r['amt'] for r in rs)
        if not rs or not s: return ''
        t = rs[0]
        if t['amt'] > .5 * s: return f"{poss(t['name'])} {money(t['amt'])} made up most of it"
        return f"{t['name']} {money(t['amt'])}, {rs[1]['name']} {money(rs[1]['amt'])}" if len(rs) > 1 else f"{t['name']} {money(t['amt'])}"
    halves = [('2025', 'H1'), ('2025', 'H2'), ('2026', 'H1'), ('2026', 'H2')]
    bars = []
    for y, h in halves:
        rs = [r for r in R if r['date'][:4] == y and ((r['date'][5:7] <= '06') == (h == 'H1'))]
        bars.append(dict(x=f'{y} {h}', v=round(sum(r['amt'] for r in rs) / 1e6), ann=ann(rs) + f', in {len(rs)} rounds'))
    D['ed158'] = dict(bars=bars, note=[f'We add up the disclosed equity rounds of {N} startups in our tracker, by half-year',
                                       f'{today[:4]} H2 runs to mid-{["January","February","March","April","May","June","July","August","September","October","November","December"][int(today[5:7]) - 1]} only, and rounds with no public amount count as zero'])
    yb = []
    for y in ('2024', '2025', '2026'):
        rs = [r for r in R if r['date'][:4] == y]; yb.append(dict(x=y, v=round(sum(r['amt'] for r in rs) / 1e6), ann=ann(rs)))
    D['ed159'] = dict(type='fundbars', t=None, bars=yb, note=[f'We add up the disclosed equity rounds of {N} startups in our database, which is complete from January 2024',
                                                             'IPOs, debt and grants are left out, 2026 runs to mid-November, and rounds with no public amount count as zero'])
    pb = []
    for y in ('2024', '2025', '2026'):
        rs = sorted([r for r in R if r['date'][:4] == y], key=lambda r: -r['amt']); s = sum(r['amt'] for r in rs)
        if s: pb.append(dict(x=y if y != today[:4] else f'{y} (YTD)', v=round(100 * rs[0]['amt'] / s), ann=f"{poss(rs[0]['name'])} {money(rs[0]['amt'])}, out of {len(rs)} rounds"))
    D['ed164'] = dict(type='fundbars', unit='pct', t=None, bars=pb, note=['We divide, for each year, the largest round by all the disclosed capital in our tracker',
                                                                           'IPOs, debt and grants are left out, and 2026 only runs to mid-November for now'])
    # biggest rounds: last twelve months / before
    def raises(rs, n=4):
        out = []
        for r in sorted(rs, key=lambda r: -r['amt'])[:n]:
            q = (int(r['date'][5:7]) - 1) // 3 + 1
            out.append(dict(name=r['name'], amt=int(r['amt']), date=f"Q{q} {r['date'][:4]}", stage=stage(r) or 'Equity'))
        return out
    D['ed165p'] = dict(rounds=raises([r for r in R if r['date'] >= year_ago]), note=[f'We listed the biggest equity rounds raised by {N} startups over the last twelve months',
                       'We used company announcements and the press, and all our sources are at the end of the report'])
    old = []
    for cid, m in M.items():
        for r in g.rounds_for(b, cid, 'ranking'):
            if r['date'] < year_ago and (r['round_type'] or '').upper() != 'IPO': old.append(dict(r, name=b.companies[cid]['name'], what=m.get('what_they_do') or '', cat=m.get('category') or '', amt=float(r['amount_usd'] or 0)))
    D['ed166p'] = dict(rounds=[dict(x, date=x['date'][-4:]) for x in raises(old)], note=[f'We listed the biggest equity rounds raised by {N} startups before the last twelve months',
                       'We used our tracker of rounds, company announcements and the press, with sources at the end'])
    def names_fit(ex, k):                        # as many names as the box holds (specs/slides.yaml), so it never looks half empty (14 Nov 2026)
        import spec as sp
        cap = ((sp.SPEC.get('where_did_most_capital_go') or {}).get(str(k)) or {}).get('max', 60); out = []
        for n_ in ex:
            if len(', '.join(out + [n_])) > cap: break
            out.append(n_)
        return ', '.join(out or ex[:1])
    # categories
    cat = collections.defaultdict(list)
    for r in R: cat[r['cat'] or 'Other'].append(r)
    top = sorted(cat.items(), key=lambda kv: -sum(r['amt'] for r in kv[1]))[:3]
    t167 = {}
    for i, (c, rs) in enumerate(top):
        ex = []; [ex.append(r['name']) for r in sorted(rs, key=lambda r: -r['amt']) if r['name'] not in ex]
        t167[6 + i] = c.upper(); t167[[9, 11, 12][i]] = str(len(rs)); t167[[13, 15, 16][i]] = money(sum(r['amt'] for r in rs)); t167[[17, 19, 20][i]] = names_fit(ex, [17, 19, 20][i])
    t167['note'] = f'We used our tracker of {len(R)} {N} equity rounds announced since January 2024, worth about {money(tot)}. IPOs, debt and grants are left out'
    D['ed167'] = t167
    # investors (leads)
    inv = collections.defaultdict(list)
    for r in R:
        for x in [y.strip() for y in (r['lead_investors'] or '').split(';') if y.strip()]: inv[x].append(r)
    ti = sorted(inv.items(), key=lambda kv: (-len(kv[1]), -sum(r['amt'] for r in kv[1])))[:5]
    t169 = {}
    K = [(7, 10, 14, 18), (8, 12, 16, 20), (9, 13, 17, 21), (26, 28, 30, 32), (27, 29, 31, 33)]
    for (kn, kc, kf, ke), (x, rs) in zip(K, ti):
        s = sum(r['amt'] for r in rs); names = collections.Counter(r['name'] for r in rs)
        t169[kn] = x.upper(); t169[kc] = str(len(rs)); t169[kf] = money(s) if s else 'Undisclosed'
        t169[ke] = ', '.join(f'{n} (twice)' if c == 2 else n for n, c in names.most_common(2))
    t169['note'] = f'We count rounds each investor led or co-led in our tracker since 2024, with full round sizes, not individual checks. Leads are known for only part of the {len(R)} rounds'
    D['ed169'] = t169
    big = sorted(sorted(R, key=lambda r: -r['amt'])[:6], key=lambda r: r['date'])
    D['ed205'] = {k: v for i, r in enumerate(big) for k, v in ((14 + 2 * i, dl(r['date'])), (15 + 2 * i, sentence(r)))}
    D['ed205']['note'] = f'We picked the biggest disclosed rounds of {N} startups since 2024, from our tracker of rounds'
    # figures for the insight slides (ed160, ed162): printed, the sentences are written by Claude in edits.yaml
    dis = [r['amt'] for r in R if r['amt']]
    byc = collections.Counter(); amc = collections.Counter()
    for r in R: byc[r['country']] += 1; amc[r['country']] += r['amt']
    print('categories:', [(c, len(rs), money(sum(r['amt'] for r in rs))) for c, rs in sorted(cat.items(), key=lambda kv: -sum(r['amt'] for r in kv[1]))])
    print('disclosed', len(dis), 'of', len(R), 'median', money(st.median(dis)))
    print('countries rounds', byc.most_common(4), 'money', [(k, money(v)) for k, v in amc.most_common(4)])
    big100 = [r for r in R if r['amt'] >= 1e8]; print('rounds >= $100M', len(big100), money(sum(r['amt'] for r in big100)), f'{100 * sum(r["amt"] for r in big100) / tot:.0f}%')
    print('biggest', [(r['name'], money(r['amt']), r['date']) for r in sorted(R, key=lambda r: -r['amt'])[:5]])
    print('stages', collections.Counter(stage(r) or 'undisclosed stage' for r in R).most_common(5))
    # facts every hand-written sentence quotes as {db.key} (db_text.yaml, extras.yaml, edits.yaml): a base update can never leave a stale figure (12 Nov 2026)
    stg = collections.Counter(stage(r) for r in R); cn = [r for r in R if r['country'] == 'China']; us = [r for r in R if r['country'] == 'United States']
    F = dict(n=len(R), total=money(tot), cn_n=len(cn), cn_rounds_pct=round(100 * len(cn) / len(R)), cn_money_pct=round(100 * sum(r['amt'] for r in cn) / tot),
             us_money=money(amc['United States']), big_n=len(big100), big_pct=round(100 * sum(r['amt'] for r in big100) / tot), disclosed=len(dis), median=money(st.median(dis)),
             seed=stg['Seed'], series_a=stg['Series A'], series_b=stg['Series B'], until=max(r['date'] for r in R))
    F['row_rounds_pct'] = 100 - F['cn_rounds_pct']; F['row_money_pct'] = 100 - F['cn_money_pct']
    F.update(us_n=len(us), us_rounds_pct=round(100 * len(us) / len(R)), us_money_pct=round(100 * amc['United States'] / tot))
    for i, (c, rs) in enumerate(sorted(cat.items(), key=lambda kv: -sum(r['amt'] for r in kv[1]))[:3], 1):      # top categories by money
        F[f'cat{i}'] = c; F[f'cat{i}_n'] = len(rs); F[f'cat{i}_total'] = money(sum(r['amt'] for r in rs)); F[f'cat{i}_pct'] = round(100 * sum(r['amt'] for r in rs) / tot)
    for i, (c, v) in enumerate(amc.most_common(2), 1): F[f'ctry{i}'] = {'United States': 'the United States', 'United Kingdom': 'the United Kingdom'}.get(c, c); F[f'ctry{i}_money'] = money(v); F[f'ctry{i}_n'] = byc[c]
    for i, r in enumerate(sorted(R, key=lambda r: -r['amt'])[:2], 1): F[f'big{i}_name'] = r['name']; F[f'big{i}_amt'] = money(r['amt']); F[f'big{i}_stage'] = stage(r); F[f'big{i}_year'] = r['date'][:4]
    for y in sorted({r['date'][:4] for r in R}):
        ry = [r for r in R if r['date'][:4] == y]; by = [r for r in ry if r['amt'] >= 1e8]
        F[f'n_{y}'] = len(ry); F[f'total_{y}'] = money(sum(r['amt'] for r in ry)); F[f'big_{y}'] = len(by)
    (ROOT / 'decks' / H / 'db_facts.yaml').write_text(yaml.dump(F, allow_unicode=True, sort_keys=False)); print('facts', F)
    def fill(v):
        if isinstance(v, str): return re.sub(r'\{db\.(\w+)\}', lambda m: str(F[m.group(1)]), v)
        if isinstance(v, dict): return {k: fill(x) for k, x in v.items()}
        if isinstance(v, list): return [fill(x) for x in v]
        return v
    tx = ROOT / 'decks' / H / 'db_text.yaml'          # sentences that need judgment (ed160, ed162), written from the figures above
    if tx.exists():
        for k, v in (yaml.safe_load(tx.read_text()) or {}).items(): D.setdefault(k, {}).update(fill(v))
    out = ROOT / 'decks' / H / 'db.yaml'
    out.write_text(yaml.dump(D, allow_unicode=True, sort_keys=False, width=1000)); print(out)


if __name__ == '__main__':
    main()
