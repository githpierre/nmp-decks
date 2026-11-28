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
import gen_lib as g, skip_rounds; skip_rounds.patch(g)   # doubtful rounds kept in the base never reach a slide
_src = (ROOT / 'tools/build_sources.py').read_text()          # publisher names (PUB, pub) without running build_sources
exec(_src[_src.index('PUB = {'):_src.index('def title(')])


def money(v):
    if v >= 1e9: return f'${v / 1e9:.1f}B'.replace('.0B', 'B')
    if v >= 1e7: return f'${v / 1e6:.0f}M'
    return f'${v / 1e6:.1f}M'.replace('.0M', 'M')


def poss(n): return n + ('’' if n.endswith('s') else '’s')      # « Isomorphic Labs’ $2.1B », « Sail’s $465M »


INV_TAIL = re.compile(r'(\s*,?\s+(Management(\s*&\s*Research)?(\s+Company)?|Private Capital|Private Equity|Venture Partners|Venture Capital|Ventures|Capital Partners|Capital Management|Partners|Capital|LLC|L\.?P\.?|Inc\.?))+$', re.I)
def inv_short(x):   # « Fidelity Management & Research Company » -> « Fidelity », « Lightspeed Venture Partners » -> « Lightspeed »: the name people use (Longevity, 18 Nov 2026: names too long for the investor slide)
    if x.strip() in INV_ALIAS: return INV_ALIAS[x.strip()]
    y = INV_TAIL.sub('', x).strip(); return y if len(y) >= 3 and y.lower() not in GENERIC_INV else x
INV_ALIAS = {'QDNL Participations': 'QDNL', 'U.S. Venture Partners': 'USVP', 'RA Capital Management': 'RA Capital', 'Johnson & Johnson Innovation – JJDC': 'J&J Innovation', 'Johnson & Johnson Innovation': 'J&J Innovation', 'Elevage Medical Technologies': 'Elevage'}   # labels on 2 lines (in vivo CAR-T S09, MedTech, 28 Nov 2026)   # « U.S. Venture Partners » became « U.S. » (MedTech, 24 Nov 2026)
GENERIC_INV = {'u.s.', 'us', 'blockchain', 'crypto', 'digital', 'global', 'general', 'growth', 'venture', 'first', 'new', 'tech', 'future'}   # « Blockchain Capital » stays whole: « led by Blockchain » reads as a technology (Stablecoin payments, 22 Nov 2026)
CO_TAIL = re.compile(r'\s+(Biosciences|Pharmaceuticals|Therapeutics|Technologies|Biotechnology|Biotechnologies)$', re.I)
def co_short(n): return re.sub(r'\s+Biosciences$', ' Bio', n) if ' ' not in n.rsplit(' ', 1)[0] and n.endswith('Biosciences') else (CO_TAIL.sub('', n) or n)   # « Aeovian Pharmaceuticals » -> « Aeovian » on the narrow investor slide


def stage(r):
    t = r['round_type'] or ''
    return '' if t in ('Unknown', 'Other', '') else t.replace('Series D+', 'late-stage')


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('handle'); ap.add_argument('--name'); ap.add_argument('--today', default=__import__('datetime').date.today().isoformat())   # was a fixed 2026-11-12: rebuild.sh passes no date, so the « last twelve months » window went stale (Quantum sensing, 27 Nov 2026)
    a = ap.parse_args(); H, N, today = a.handle, a.name, a.today
    b = g.Base(); import startup_status as _ss   # startups only: the base keeps non-startups as history (Lanserhof on Longevity, 18 Nov 2026)
    M = {m['company_id']: m for m in b.markets[H] if _ss.table_startup_base(b, m['company_id'])[0]}
    R = []
    for cid, m in M.items():
        for r in g.rounds_for(b, cid, 'deals'):
            if (r['round_type'] or '').upper() == 'IPO' or 'IPO' in (r['round_label'] or ''): continue   # equity rounds only, never a listing
            R.append(dict(r, name=b.companies[cid]['name'], what=m.get('what_they_do') or '', cat=m.get('category') or '', country=b.companies[cid]['hq_country'], amt=float(r['amount_usd'] or 0)))
    R.sort(key=lambda r: r['date'])
    # doubtful rounds (Stablecoin payments, 22 Nov 2026: MoonPay « $100M Series B » sourced only by Forge Global, and a 2022
    # « investor participation » extension shown as a second round): listed, then left out with skip_rounds.yaml if confirmed
    SECONDARY = ('forgeglobal.com', 'equityzen.com', 'hiive.com', 'caplight.com', 'notice.co')   # secondary-market sites: their « rounds » are estimates, not announcements
    CHECKED = yaml.safe_load((ROOT / 'checked_rounds.yaml').read_text()) or {}   # rounds already ruled on (24 Nov 2026): no warning again
    for cid in M:
        for r in g.rounds_for(b, cid, 'ranking'):
            if r['round_id'] in CHECKED: continue
            if r.get('amount_usd') and any(s in (r.get('source_url') or '') for s in SECONDARY) and (float(r['amount_usd']) >= 1e8 or (r.get('date') or '') >= '2024'):   # RULES 131 of the base keeps the rest at low confidence: only a big or recent one moves a slide (24 Nov 2026)
                print(f"WEAK ROUND SOURCE: {r['round_id']} {money(float(r['amount_usd']))} only from {r['source_url']}: check, or add it to skip_rounds.yaml")
            if re.search(r'participation', r.get('round_label') or '', re.I):   # « Series A investor participation »: the same round again (an « extension » is new money, kept)
                print(f"ROUND EXTENSION: {r['round_id']} « {r['round_label']} » is likely the same round as an earlier one: check, or add it to skip_rounds.yaml")
    tot = sum(r['amt'] for r in R); D = {}
    year_ago = f'{int(today[:4]) - 1}{today[4:]}'
    print(f'{len(R)} equity rounds since 2024, {money(tot)}; base covers to', max(r['date'] for r in R))

    _csf = ROOT / 'decks' / H / 'cat_short.yaml'; CS = yaml.safe_load(_csf.read_text()) if _csf.exists() else {}
    _cpf = ROOT / 'decks' / H / 'cat_phrase.yaml'; CP = yaml.safe_load(_cpf.read_text()) if _cpf.exists() else {}   # what the category sells, for sentences
    def sentence(r, _lead=True):
        out_ = _sentence(r, _lead)   # the joining words can still push a row past 118 (Eden GeoPower on ed157, 119, 21 Nov 2026): drop the lead then
        return out_ if not _lead or len(re.sub(r'\{1\|([^}]*)\}', r'\1', out_)) <= 118 else _sentence(r, False)
    def _sentence(r, _lead=True):
        """« Tutor Intelligence raised a $75M Series B led by Andreessen Horowitz for its industrial and factory humanoids {1|Business Wire} »"""
        lead = inv_short((r['lead_investors'] or '').split(';')[0].strip()) if _lead else ''; st_ = stage(r)
        if st_ and not st_.startswith('Series'): st_ = st_.lower() + ' round'          # « a $787M growth equity round », never « a $787M Growth Equity » (13 Nov 2026)
        # « an $80M Series C », « an $18M round » (MGA, 22 Nov 2026: « a $80M Series C » on the latest rounds slide)
        art = lambda m: 'an' if re.match(r'\$(8|11(?![\d])|18(?![\d]))', m) else 'a'
        if r['amt']: s = f"{r['name']} raised {art(money(r['amt'])) + ' ' + money(r['amt']) + ' ' + st_ if st_ else money(r['amt'])}"
        else: s = f"{r['name']} raised an undisclosed {st_ or 'round'}"
        if lead and len(s) + len(lead) + len(pub(r['source_url'])) + 14 <= 118: s += f' led by {lead}'   # a long lead name alone pushed ed157 to 125 characters (AI drug discovery, 20 Nov 2026): drop the lead before the slide breaks
        w_ = (r.get('what') or '').strip().rstrip('.')   # what the company does (markets.csv), so the reader learns something (Pierre, 14 Nov 2026: rows 30-40% too short)
        PROPER = {'India', 'China', 'Japan', 'Europe', 'Asia', 'Africa', 'America', 'American', 'European', 'Chinese', 'Indian', 'Japanese', 'US', 'UK', 'FDA', 'Korea', 'Korean', 'Singapore', 'Australia', 'Canada', 'Germany', 'France', 'Sweden', 'Swiss'}
        lw = lambda x: ' '.join(t if (t.isupper() or any(c.isupper() for c in t[1:]) or t.strip(',.') in PROPER) else t.lower() for t in x.split())   # « in India », never « in india » (Longevity, 18 Nov 2026)
        verb = bool(re.match(r'^(Builds|Develops|Combines|Uses|Makes|Designs|Provides|Offers|Creates|Runs|Helps|Turns|Applies)\b', w_))
        _w0 = next((x for x in w_.split() if not x.lower().endswith('ly')), '')   # « Electrically stimulates » is a verb too, never « for its electrically stimulates » (Natural hydrogen, 21 Nov 2026)   # any verb in the 3rd person (« Operates », « Automates »), never « for its operates » (Healthcare AI, 18 Nov 2026)
        verb = verb or bool(re.match(r'^[A-Za-z][a-z]+s$', _w0) and not re.search(r'(ics|ions|ors|ems|ots|ools|ents|ances|ings|orms|ices|ss|us|is|as|os|ys)$', _w0.lower()))   # « Thymus » is not a verb (« It thymus regeneration », Longevity, 18 Nov 2026)
        # plural nouns of people that end like a verb: « It homeowners insurance with… » (MGA, 22 Nov 2026, Stand)
        if re.search(r'(owners|holders|workers|drivers|customers|users|brokers|farmers|carriers|insurers|travelers|renters|landlords|employers|consumers|retailers|members|partners|truckers|builders|contractors|lenders|sellers|buyers)$', _w0.lower()): verb = False
        lim = 118 - len(pub(r['source_url'])) - 10   # the joining words « for its » / « . It » and the space before the source count too (MedTech, 23 Nov 2026: Sirona row at 126 for max 118)   # ed157 allows 120 (AI drug discovery, 20 Nov 2026)   # two lines at most, source label included (spec max 128 with the joining words)
        while w_ and len(s) + len(w_) >= lim:                     # too long: cut at the last « for », « to », « with », comma
            cut = max(w_.rfind(x) for x in (' for ', ' to ', ', ', ' with '))   # never at « and »: it splits a noun phrase (« an AI-powered patient data », Healthcare AI, 18 Nov 2026)
            w_ = w_[:cut] if cut > 15 else ''
            while w_ and re.search(r'\b(one|two|three|four|five|six|seven|eight|nine|ten|\d+|a|an|the|of|and|or|its|their|both|with)$', w_, re.I):   # never end on a dangling word (« robots with two », Humanoid Robotics, 18 Nov 2026)
                cut = max(w_.rfind(x) for x in (' for ', ' to ', ', ', ' with ')); w_ = w_[:cut] if cut > 15 else ''
        if w_ and re.search(r'(-enabled|-powered|-based|-driven|-derived|-specific|-grade|ed)$', w_.split()[-1]): w_ = ''   # a cut that ends on an adjective: use the category instead
        if w_ and verb: s += '. It ' + lw(w_)
        elif w_: s += ' for its ' + lw(w_)
        elif r['cat'] and (r['cat'] in CP or CS.get(r['cat']) in CP) and len(s) + len(CP.get(r['cat']) or CP[CS.get(r['cat'])]) < 100: s += ' for its ' + (CP.get(r['cat']) or CP[CS.get(r['cat'])])   # decks/<h>/cat_phrase.yaml: « for its specialty business insurance », never « for its specialty commercial » (MGA, 22 Nov 2026)
        elif r['cat'] and len(s) + len(CS.get(r['cat'], r['cat'])) < 100: s += ' for its ' + ' '.join(w if (w.isupper() or any(c.isupper() for c in w[1:])) else w.lower() for w in CS.get(r['cat'], r['cat']).split())   # « payment APIs », never « payment apis » (Stablecoin payments, 22 Nov 2026)   # the short slide name (« aging-biology drugs »), never the base label « longevity therapeutics developers » (Longevity, 18 Nov 2026)   # « life science AI », not « life Science AI »
        p_ = pub(r['source_url']); key = re.sub(r'[^a-z0-9]', '', r['name'].lower())
        lab = re.sub(r'[^a-z0-9]', '', site_label(r['source_url']))
        if p_.lower()[:5] == key[:5] or (len(lab) >= 4 and (key.startswith(lab) or lab.startswith(key))) or 'pr.co' in r['source_url']: p_ = r['name'] if len(r['name']) <= 14 else r['name'].split()[0]   # « Project Omega », never « Project » (18 Nov 2026)   # a company's own site, blog or press page: name the company
        elif p_ not in PUB.values() and p_.lower() not in (r['lead_investors'] or '').lower(): print('PUBLISHER UNKNOWN', r['source_url'][:70], '->', p_)   # shown on a slide: add its name to PUB (tools/build_sources.py)
        return s + f" {{1|{p_}}}"
    def dl(d): return f"{d[:4]} ({['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC'][int(d[5:7]) - 1]})" if d[5:7].isdigit() else d[:4]   # a year-only date in the base (In vivo CAR-T, 24 Nov 2026)

    last = sorted(R, key=lambda r: r['date'], reverse=True)[:12]; floor = ''
    if sum(1 for r in last if 0 < r['amt'] < 1e7) > 6:      # a busy market: most of the 12 latest rounds are small rounds of unknown startups (Healthcare AI, 13 Nov 2026).
        last = sorted([r for r in R if r['amt'] >= 1e7], key=lambda r: r['date'], reverse=True)[:12]; floor = ' of $10M or more'   # Pierre: the 12 latest of $10M or more, and the note says so
    if len(last) < 12:   # a young market with fewer than 12 rounds since 2024: the template's own rows stayed on ed157 (an in vivo CAR-T round on Natural hydrogen, 21 Nov 2026)
        _older = []        # complete the list with the latest older rounds of the same startups, so the 12 rows are still the 12 latest rounds
        for cid, m in M.items():
            for r in g.rounds_for(b, cid, 'ranking'):
                if (r['round_type'] or '').upper() == 'IPO' or r['date'] >= min(x['date'] for x in R): continue
                if floor and float(r['amount_usd'] or 0) < 1e7: continue
                _older.append(dict(r, name=b.companies[cid]['name'], what=m.get('what_they_do') or '', cat=m.get('category') or '', country=b.companies[cid]['hq_country'], amt=float(r['amount_usd'] or 0)))
        last = last + sorted(_older, key=lambda r: r['date'], reverse=True)[:12 - len(last)]
    if len(last) < 12:
        raise SystemExit(f'ed156/ed157 need 12 rounds, the base has {len(last)}: add rounds to the base or drop ed157 in edits.yaml (never leave the template rows)')
    D['ed156'] = {k: v for i, r in enumerate(last[:6]) for k, v in ((13 + 2 * i, dl(r['date'])), (14 + 2 * i, sentence(r)))}
    D['ed156']['note'] = f'We list the latest equity rounds{floor} of {N} startups in our tracker, from company releases and the press.' + ('' if floor else ' Undisclosed means no amount was made public')
    D['ed157'] = {k: v for i, r in enumerate(last[6:12]) for k, v in ((14 + 2 * i, dl(r['date'])), (15 + 2 * i, sentence(r)))}
    D['ed157']['note'] = D['ed156']['note']

    def ann(rs, tail=''):
        """Three short lines over each bar, always the same shape so sibling notes have the same number of lines (audit CARD_LINES):
        « Isomorphic Labs, $600M top round, in 40 rounds ». Two names and « X’s $Y made up most of it » ran on 4 to 7 lines and
        overlapped the next bar (AI drug discovery, 20 Nov 2026). The template puts each « , » part on its own line."""
        rs = sorted(rs, key=lambda r: -r['amt']); s = sum(r['amt'] for r in rs)
        if not rs: return ''
        t = rs[0]; nm = co_short(t['name']); nm = nm if len(nm) <= 16 else nm.split()[0]
        if not s: return f"{nm}, undisclosed amount" + (f", {tail}" if tail else '')   # a $0M bar with an arrow and no words (Natural hydrogen 2026 H2, 21 Nov 2026)
        return f"{nm}, {money(t['amt'])} top round" + (f", {tail}" if tail else '')
    halves = [('2025', 'H1'), ('2025', 'H2'), ('2026', 'H1'), ('2026', 'H2')]
    bars = []
    for y, h in halves:
        rs = [r for r in R if r['date'][:4] == y and ((r['date'][5:7] <= '06') == (h == 'H1'))]
        bars.append(dict(x=f'{y} {h}', v=round(sum(r['amt'] for r in rs) / 1e6), ann=ann(rs, f"in {len(rs)} round{'s' if len(rs) != 1 else ''}")))
    for b_ in bars:                              # a half-year with rounds but no public amount reads « Undisclosed », never « $0M » (Natural hydrogen, 24 Nov 2026)
        if b_['v'] == 0 and 'in 0 rounds' not in b_['ann']: b_['lab'] = 'Undisclosed'
    D['ed158'] = dict(bars=bars, note=[f'We add up the disclosed equity rounds of {N} startups in our tracker, by half-year',
                                       f'{today[:4]} H2 runs to mid-{["January","February","March","April","May","June","July","August","September","October","November","December"][int(today[5:7]) - 1]} only, and rounds with no public amount count as zero'])
    yb = []
    for y in ('2024', '2025', '2026'):
        rs = [r for r in R if r['date'][:4] == y]; yb.append(dict(x=y, v=round(sum(r['amt'] for r in rs) / 1e6), ann=ann(rs, f"in {len(rs)} round{'s' if len(rs) != 1 else ''}")))
    for b_ in yb:
        if b_['v'] == 0 and 'in 0 rounds' not in b_['ann']: b_['lab'] = 'Undisclosed'
    D['ed159'] = dict(type='fundbars', t=None, bars=yb, note=[f'We add up the disclosed equity rounds of {N} startups in our database, which is complete from January 2024',
                                                             'IPOs, debt and grants are left out, 2026 runs to mid-November, and rounds with no public amount count as zero'])
    pb = []
    for y in ('2024', '2025', '2026'):
        rs = sorted([r for r in R if r['date'][:4] == y], key=lambda r: -r['amt']); s = sum(r['amt'] for r in rs)
        if s: pb.append(dict(x=y if y != today[:4] else f'{y} (YTD)', v=round(100 * rs[0]['amt'] / s), ann=ann(rs, f"out of {len(rs)} round{'s' if len(rs) != 1 else ''}")))
    D['ed164'] = dict(type='fundbars', unit='pct', t=None, bars=pb, note=['We divide, for each year, the largest round by all the disclosed capital in our tracker',
                                                                           'IPOs, debt and grants are left out, and 2026 only runs to mid-November for now'])
    # biggest rounds: last twelve months / before
    def raises(rs, n=4):
        out = []
        for r in sorted([r for r in rs if r['amt'] > 0], key=lambda r: -r['amt'])[:n]:   # an undisclosed round is not a « biggest round »: it drew a $0M bar (Koloma, Natural hydrogen, 21 Nov 2026)
            # a date known only to the year (« 2022 ») shows the year alone, no quarter (Infleqtion, Quantum sensing, 27 Nov 2026)
            d = f"Q{(int(r['date'][5:7]) - 1) // 3 + 1} {r['date'][:4]}" if len(r['date']) >= 7 else r['date'][:4]
            out.append(dict(name=r['name'], amt=int(r['amt']), date=d, stage=stage(r) or 'Equity'))
        return out
    D['ed165p'] = dict(rounds=raises([r for r in R if r['date'] >= year_ago]), note=[f'We listed the biggest equity rounds raised by {N} startups over the last twelve months',
                       'We used company announcements and the press, and all our sources are at the end of the report'])
    old = []
    for cid, m in M.items():
        for r in g.rounds_for(b, cid, 'ranking'):
            if r['date'] < year_ago and (r['round_type'] or '').upper() != 'IPO': old.append(dict(r, name=b.companies[cid]['name'], what=m.get('what_they_do') or '', cat=m.get('category') or '', amt=float(r['amount_usd'] or 0)))
    D['ed166p'] = dict(rounds=[dict(x, date=x['date'][-4:]) for x in raises(old)], note=[f'We listed the biggest equity rounds raised by {N} startups before the last twelve months',
                       'We used our tracker of rounds, company announcements and the press, with sources at the end'])
    def names_fit(ex, k, cap=None):              # as many names as the box holds (specs/slides.yaml), so it never looks half empty (14 Nov 2026)
        import spec as sp
        cap = cap or ((sp.SPEC.get('where_did_most_capital_go') or {}).get(str(k)) or {}).get('max', 60); out = []
        for n_ in ex:
            n_ = co_short(n_)                    # short names fill the box evenly: rows on 1 and 2 lines side by side (BODY_LINES, AI drug discovery, 20 Nov 2026)
            if len(', '.join(out + [n_])) > cap: continue
            if n_ in out: continue
            out.append(n_)
        return ', '.join(out or ex[:1])
    # categories
    cat = collections.defaultdict(list)
    for r in R: cat[CS.get(r['cat'], r['cat']) or 'Other'].append(r)      # by SHORT name: merged base categories count as one (AI drug discovery, 20 Nov 2026: Molecule design = 2 base categories)
    top = sorted(cat.items(), key=lambda kv: -sum(r['amt'] for r in kv[1]))[:3]
    t167 = {}; _sf = ROOT / 'decks' / H / 'cat_short.yaml'          # short category names, as on the live S09 slide (Advanced Nuclear, 18 Nov 2026)
    SHORT = yaml.safe_load(_sf.read_text()) if _sf.exists() else {}
    for i, (c, rs) in enumerate(top):
        ex = []; [ex.append(r['name']) for r in sorted(rs, key=lambda r: -r['amt']) if r['name'] not in ex]
        t167[6 + i] = SHORT.get(c, c).upper(); t167[[9, 11, 12][i]] = str(len(rs)); t167[[13, 15, 16][i]] = money(sum(r['amt'] for r in rs)); t167[[17, 19, 20][i]] = names_fit(ex, [17, 19, 20][i])
    _ex = {k: v for k, v in t167.items() if k in (17, 19, 20)}   # a category with few startups fills one line: the other rows keep one line too (BOX_LINES, Neocloud, 24 Nov 2026)
    if len(_ex) == 3 and min(len(v) for v in _ex.values()) <= 36:
        for i, (c, rs) in enumerate(top):
            ex = []; [ex.append(r['name']) for r in sorted(rs, key=lambda r: -r['amt']) if r['name'] not in ex]
            t167[[17, 19, 20][i]] = names_fit(ex, [17, 19, 20][i], cap=36)
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
        t169[kn] = inv_short(x).upper(); t169[kc] = str(len(rs)); t169[kf] = money(s) if s else 'Undisclosed'
        t169[ke] = ', '.join(f'{co_short(n)} (twice)' if c == 2 else co_short(n) for n, c in names.most_common(2))
        if len(t169[ke]) > 35: t169[ke] = ', '.join(f'{co_short(n)} (twice)' if c == 2 else co_short(n) for n, c in names.most_common(1))   # « Isomorphic Labs (twice), Chai Discovery » broke the box (35 max)
    t169['note'] = f'We count rounds each investor led or co-led in our tracker since 2024, with full round sizes, not individual checks. Leads are known for only part of the {len(R)} rounds'
    if not ti or len(ti[0][1]) < 2: t169['drop'] = True   # « most active investors » with one deal each says nothing: the slide goes (Natural hydrogen, 24 Nov 2026)
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
