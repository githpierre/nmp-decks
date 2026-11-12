"""Structure deck of a new market, built from the REFERENCE deck (In Vivo CAR-T) for tools/import_research.py --demo.

    python3 tools/make_market_demo.py --spec plans/humanoid-robotics.yaml        -> decks/<handle>-demo/deck.yaml

- slide list = the reference deck's final slides; segment blocks folded back to one model copy (ed062..ed065, ed106..ed109,
  from the first segment) that the import repeats for each segment of the new market;
- slides the reference market dropped for lack of data (spec `reask`) come back from the In Vivo demo at their place;
- extra slides (xs_*, pp_s06) and the full sources list (src_all_*) are removed: the new market gets its own;
- product-page twins keep the reference content with a yellow tag until the new market's live.yaml replaces them.
"""
import argparse, copy, re, yaml
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--spec'); a = ap.parse_args()
    spec = yaml.safe_load((ROOT / a.spec).read_text())
    ref = yaml.safe_load((ROOT / spec['model_deck'] / 'deck.yaml').read_text())
    demo = {s['id']: s for s in yaml.safe_load((ROOT / 'decks/invivo-demo/deck.yaml').read_text())['slides']}
    demo_ids = list(demo)
    S, seen = [], set()
    for s in ref['slides']:
        sid = s['id']
        if sid.startswith(('xs_', 'src_')) or sid == 'pp_s06': continue
        m = re.match(r'(ed\d{3})-s(\d)$', sid)
        if m:
            if m.group(2) != '1' or m.group(1) in seen: continue
            seen.add(m.group(1)); s = dict(copy.deepcopy(s), id=m.group(1))
        else: s = copy.deepcopy(s)
        if sid in spec.get('live_twins', []): s['tag'] = 'PRODUCT PAGE: TO COPY'
        S.append(s)
    ids = [s['id'] for s in S]
    for sid in spec.get('reask', []):
        if sid in ids: continue
        i = demo_ids.index(sid); prev = next((p for p in reversed(demo_ids[:i]) if p in ids), None)
        j = ids.index(prev) + 1 if prev else 0
        S.insert(j, copy.deepcopy(demo[sid])); ids.insert(j, sid)
    D = {k: v for k, v in ref.items() if k != 'slides'}
    D.update(market=spec['market_title'], label=spec['label'], slug=spec['handle'] + '-demo', keep_together=spec.get('keep_together', []))
    D['slides'] = S
    out = ROOT / 'decks' / (spec['handle'] + '-demo'); (out / 'media').mkdir(parents=True, exist_ok=True)
    (out / 'deck.yaml').write_text(yaml.dump(D, allow_unicode=True, sort_keys=False, width=1000))
    print(out / 'deck.yaml', len(S), 'slides')


if __name__ == '__main__':
    main()
