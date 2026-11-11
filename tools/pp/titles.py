"""Title families per slide type, rotated market by market so the 225 pages do not all ask the same question (Pierre, 11 Nov 2026).
The family is picked by rotation, then the next family is taken if the title cannot sit on 2 balanced lines."""
import sys, csv
sys.path.insert(0, '/root/w/s10/rebal'); import rebal2 as R
ORDER = [r['handle'] for r in csv.DictReader(open('/root/w/nmp_slide_kit/markets_225.csv'))]
FAM = {
 'pp_tech': ['Which {m} company has the most complete tech today?', 'Who has the most complete {m} tech today?',
             'Which {m} players can already do the most today?', 'Who has built the full {m} stack so far?'],
 'pp_raises': ['Which {m} startups raised the most recently?', 'Who raised the biggest {m} rounds lately?',
               'Where did the big {m} money go recently?', 'Which {m} startups got the biggest checks lately?',
               'Who are investors backing most in {m} right now?', 'Which {m} startups have received the most funding?'],
 'pp_grid': ['Who are the top companies in {m}?', 'Who are the top players in {m} today?',
             'Who are the leading companies in {m}?', 'Which companies lead {m} right now?'],
}
def ratio(t):
    s = R.split2(t, 28, True, 8.6)
    if not s: return 0, t
    a, b = R.R.g.tw(s[1], 28, True), R.R.g.tw(s[2], 28, True); return min(a, b) / max(a, b), s[1] + '\n' + s[2]
def vary(slides, name):
    """name(h) gives the market name used in titles"""
    for s in slides:
        F = FAM.get(s['type']); h = s.get('_h')
        if not F or not h: continue
        k0 = (ORDER.index(h) if h in ORDER else 0) % len(F); best = None
        for j in range(len(F)):
            r, t = ratio(F[(k0 + j) % len(F)].format(m=name(h)))
            if name(h) not in t.replace('\n', '|').split('|')[0] and name(h) not in t.split('\n')[-1]: r = 0   # never cut the market name
            if r >= 0.85: best = t; break
            if not best or r > best[0]: best = (r, t)
        s['title'] = best if isinstance(best, str) else best[1]
