"""Text specification of the slides (specs/slides.yaml, made by tools/make_spec.py): shared by the research prompts, the
self-check given to the research LLM and the import. One place, so a rule written once applies everywhere (method v2)."""
import re, yaml
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
SPEC = yaml.safe_load((ROOT / 'specs/slides.yaml').read_text()) if (ROOT / 'specs/slides.yaml').exists() else {}
FORMAT = """FORMAT RULES (every text, no exception):
- Amounts read at a glance: $10B or more without decimal ($56B, never $56.01B), under $10B one decimal at most ($2.1B, $787M, $1B never $1.0B).
  A share keeps one decimal at most (39.7%, never 39.72%).
- US English, plain words, short sentences. No em dash, no semicolon, no exclamation mark.
- A key marked CAPS is written in capitals. A key marked WORDS n has exactly n words.
- Every text stays between its MIN and MAX characters (the source label in {1|...} counts). Too short leaves the box half empty: add one concrete fact.
  Too long breaks the slide: tighten the wording, never drop the fact that matters."""


def tpl(slide):
    t = str(slide.get('type') or '')
    return t[2:] if t.startswith('x/') else t


def leaves(x, path=''):
    if isinstance(x, dict):
        for k, v in x.items():
            if k in ('id', 'type', 'section', 'title', 'note', 'src', 'logo', 'logo_src', 'url', 'page', 'handle', 'sources', 'logos', 'status', 'comment'): continue
            yield from leaves(v, f'{path}.{k}' if path else str(k))
    elif isinstance(x, list):
        for v in x: yield from leaves(v, path + '.*')
    elif isinstance(x, str): yield path, x


def limits(slide):
    """{key or field path: {min, max, lines, caps, words}} for this slide's template ({} when the template has no spec)"""
    S = SPEC.get(tpl(slide)) or {}
    out = {}
    for p, v in leaves(slide):
        k = p[2:] if p.startswith('t.') else p
        if k in S: out[k] = S[k]
    return out


def plain(v): return re.sub(r'\s+', ' ', re.sub(r'\{\d\|([^}]*)\}', r'\1', v.replace('<br>', ' '))).strip()


def problems(slide, sid=None):
    """every text out of its spec, as readable lines"""
    S = SPEC.get(tpl(slide)) or {}; sid = sid or slide.get('id'); out = []
    for p, v in leaves(slide):
        k = p[2:] if p.startswith('t.') else p
        e = S.get(k)
        if not e or not v.strip() or re.fullmatch(r'\s*[^\w\s]{1,4}\s*', v): continue   # an empty box is a choice (holes_ok)
        L = len(plain(v))
        if L > e['max']: out.append(f'{sid} {k} | too long: {L} for max {e["max"]} | {plain(v)[:60]}')
        elif e.get('min') and L < e['min']: out.append(f'{sid} {k} | too short: {L} for min {e["min"]} (add one concrete fact) | {plain(v)[:60]}')
        if e.get('caps') and plain(v) != plain(v).upper(): out.append(f'{sid} {k} | must be in capitals | {plain(v)[:40]}')
        if e.get('words') and len(plain(v).split()) != e['words']: out.append(f'{sid} {k} | must have exactly {e["words"]} words | {plain(v)[:40]}')
    return out


def describe(slide):
    """the lines given to the research LLM under each slide model"""
    L = limits(slide)
    if not L: return ''
    f = lambda e: f"{e.get('min', 1)}-{e['max']}" + (' CAPS' if e.get('caps') else '') + (f" WORDS {e['words']}" if e.get('words') else '')
    return 'Characters per key (MIN-MAX), measured on the slide: ' + ', '.join(f'{k}: {f(e)}' for k, e in L.items()) + '\n'
