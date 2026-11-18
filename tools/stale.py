"""What has aged in a deck already built (update of an existing market, Pierre 18 Nov 2026).

    python3 tools/stale.py <handle> [--today YYYY-MM-DD]

Prints, chapter by chapter, what needs new research and what refreshes by itself:
- research chapters: date of the result file, age in days; dated chapters older than 60 days are TO REDO
  (evergreen chapters 01, 04, 06 are only re-read);
- SIGNAL slides past their `fresh` limit (same limits as the import: month 6, quarter 9, half 12, total 12 months);
- extra slides without `fresh` (check their figures in the signals prompt);
- relative time words in edits / extras / live (« so far », « this year », « today », « latest quarter »);
- database slides: they re-flow from the base at the next rebuild (no prompt), last base date shown;
- product-page twins: listed, to compare with the live page before the rebuild.
Then: send ONE zip with the TO REDO chapters + the signals prompt, import, rebuild, review page, PDF."""
import argparse, datetime as dt, re, csv, pathlib, yaml
ROOT = pathlib.Path(__file__).resolve().parent.parent
ap = argparse.ArgumentParser(); ap.add_argument('handle'); ap.add_argument('--today', default=str(dt.date.today())); a = ap.parse_args()
D = ROOT / 'decks' / a.handle; today = dt.date.fromisoformat(a.today)
if not D.exists(): raise SystemExit(f'no deck decks/{a.handle}: this market was never built, follow PROTOCOL.md from step 0')
EVER = {'01', '04', '06'}
print(f'== {a.handle}, {today}\n-- research chapters')
for f in sorted((D / 'research').glob('*.md')):
    m = re.search(r'-deck-(\d\d)-(.+?)-results-research-(\d{4}-\d\d-\d\d)', f.name)
    if not m: continue
    ch, name, d = m.group(1), m.group(2), dt.date.fromisoformat(m.group(3)); age = (today - d).days
    tag = 'evergreen, re-read' if ch in EVER else ('TO REDO' if age > 60 else 'ok')
    print(f'  {ch} {name:40} {d} ({age} d)  {tag}')
print('-- SIGNAL and extra slides')
lim = dict(month=6, quarter=9, half=12, total=12)
for e in yaml.safe_load((D / 'extras.yaml').read_text()) or []:
    s = e['slide']; fr = s.get('fresh')
    if not fr: print(f"  {s['id']:12} no fresh date: check its figures"); continue
    y, mo = map(int, str(fr['end']).split('-')); age = (today.year - y) * 12 + today.month - mo
    ok = (y >= today.year or (y == today.year - 1 and today.month <= 4)) if fr['period'] == 'year' else age <= lim[fr['period']]
    print(f"  {s['id']:12} {fr['period']} {fr['end']} ({age} months)  {'ok' if ok else 'STALE: redo or replace'}")
print('-- relative time words (rewrite them)')
for n in ('edits.yaml', 'extras.yaml', 'live.yaml', 'db_text.yaml'):
    p = D / n
    if not p.exists(): continue
    for i, l in enumerate(p.read_text().splitlines(), 1):
        if re.search(r'so far|this year|today|latest quarter|right now|this past year', l, re.I) and 'title' not in l: print(f'  {n}:{i}  {l.strip()[:110]}')
print('-- database slides: re-flow at the rebuild from nmp-seo data/startups (no prompt)')
cov = pathlib.Path('/home/claude/nmp-seo/data/startups/coverage.csv')
if cov.exists():
    rows = [r for r in csv.DictReader(open(cov)) if a.handle in (r.get('market') or r.get('market_handle') or '')]
    if rows: print('  base searched until', max(r.get('searched_until', '') for r in rows))
print('-- product-page twins: compare with https://newmarketpitch.com/pages/' + a.handle)
L = yaml.safe_load((D / 'live.yaml').read_text()) or {}
print('  ' + ', '.join(L))
