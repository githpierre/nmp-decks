"""Rounds listed in skip_rounds.yaml never reach a deck slide (doubtful rounds kept in the base, Stablecoin payments, 22 Nov 2026).

    import skip_rounds; skip_rounds.patch(g)      # after « import gen_lib as g »: every g.rounds_for() drops them
    df = skip_rounds.drop(df)                     # a pandas table read straight from rounds.csv
"""
from pathlib import Path
import yaml

F = Path(__file__).resolve().parent.parent / 'skip_rounds.yaml'
SKIP = set((yaml.safe_load(F.read_text()) or {}).keys()) if F.exists() else set()


def patch(g):
    if getattr(g, '_skip_rounds', False): return
    f = g.rounds_for
    g.rounds_for = lambda *a, **k: [r for r in f(*a, **k) if r.get('round_id') not in SKIP]
    g._skip_rounds = True


def drop(df):
    return df[~df['round_id'].isin(SKIP)] if 'round_id' in df.columns else df
