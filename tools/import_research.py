"""Import the research results (Markdown files with one YAML block per slide) into a new market deck.

    python3 tools/import_research.py <results dir> --demo decks/invivo-demo --out decks/in-vivo-car-t --name "in vivo CAR-T" \
        --pain "Blood cancers;Autoimmune diseases;Solid tumors" --value "mRNA-LNP CAR-T;Lentiviral CAR-T;Gene-editing CAR-T;Beyond T cells"

- parses every "### <slide id>" + ```yaml block (lenient on unquoted colons);
- checks each answer against its EdTech model: same keys, same number of items, lengths within ±25%, sources present,
  no EdTech words left; writes the report to <out>/research_report.md;
- builds the deck: the demo structure, segment blocks rebuilt from their model (one copy per segment), texts replaced,
  sources kept in <out>/sources.yaml. Slides still without real content keep a yellow tag saying why (DEMO DATA, DATABASE, NO DATA)."""
import argparse, copy, glob, json, re, yaml
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
REF = {s['id']: s for s in yaml.safe_load((ROOT / 'decks/edtech-full/deck.yaml').read_text())['slides']}
DB_IDS = {'ed156', 'ed157', 'ed158', 'ed159', 'ed160', 'ed162', 'ed164', 'ed165p', 'ed166p', 'ed167', 'ed168p', 'ed169', 'ed171p', 'ed205'}
EDWORDS = re.compile(r'\b(edtech|students?|teachers?|schools?|classrooms?|learners?|tutor(s|ing)?|homework|duolingo|coursera|chegg)\b', re.I)


def lenient_yaml(y):
    try: return yaml.safe_load(y)
    except Exception:
        out = []
        for l in y.split('\n'):
            m = re.match(r'^(\s*(?:-\s+)?[\w{}|-]+:\s+)(.*)$', l)
            if m and ': ' in m.group(2) and not m.group(2).lstrip().startswith(('"', "'", '[', '{', '|', '>')):
                l = m.group(1) + json.dumps(m.group(2))
            out.append(l)
        return yaml.safe_load('\n'.join(out))


def parse(d):
    R, errs = {}, []
    for f in sorted(glob.glob(str(Path(d) / '*.md'))):
        txt = Path(f).read_text()
        for m in re.finditer(r'^###\s+(\S+)[^\n]*\n(.*?)```ya?ml\n(.*?)```', txt, re.S | re.M):
            try: R[m.group(1)] = lenient_yaml(m.group(3)) or {}
            except Exception as e: errs.append((m.group(1), str(e)[:100]))
    return R, errs


def like_model(v, mv):
    """same paragraph structure as the model: its separators (blank paragraphs give each part its own style) between the answer's parts"""
    if isinstance(v, str) and isinstance(mv, str) and mv.startswith('\n'):   # leading blank lines of the model are kept (ed221); idempotent
        return re.match(r'\n+', mv).group(0) + like_model(v.lstrip('\n'), mv.lstrip('\n'))
    if isinstance(v, str) and isinstance(mv, str) and '\n' not in mv and '\n' in v and len(v) <= 40:
        return ' '.join(v.split())   # a short label never carries the LLM's own line break: rawfit breaks every label of a grid the same way (12 Nov 2026)
    if not isinstance(v, str) or not isinstance(mv, str) or '\n' not in mv: return v
    mseg, msep = re.split(r'\n+', mv), re.findall(r'\n+', mv)
    aseg = [x.strip() for x in re.split(r'\n+', v) if x.strip()]
    if len(aseg) < len(mseg): return '\n'.join(aseg) if all(len(x) == 1 for x in msep) else (msep[0].join(aseg) if aseg else v)
    if len(aseg) > len(mseg): aseg = aseg[:len(mseg) - 1] + [' '.join(aseg[len(mseg) - 1:])]
    out = aseg[0]
    for sep, part in zip(msep, aseg[1:]): out += sep + part
    return out


def clean_title(t):
    return re.sub(r'\s+', ' ', str(t).replace('\\n', ' ')).strip() if t else t


def check(sid, model, ans):
    """list of problems of one answer against its model"""
    P = []
    if ans.get('status') != 'ok': return [f"status {ans.get('status')}: {ans.get('comment') or ans.get('reason') or ans.get('note') or ''}"[:160]]
    if isinstance(model.get('t'), dict):
        mt, at = model['t'], ans.get('t') or {}
        at = {int(k) if str(k).isdigit() else k: v for k, v in at.items()}
        miss = [k for k, v in mt.items() if k not in at and not re.fullmatch(r'\s*(\d{1,2}|[^\w\s]{1,3}|[✓✕×])\s*', v or '')]
        if miss: P.append(f'missing keys {miss}')
        for k, v in at.items():
            if k in mt and mt[k] and v:
                a, b = len(re.sub(r'\{\d\|([^}]*)\}', r'\1', str(v))), len(re.sub(r'\{\d\|([^}]*)\}', r'\1', mt[k]))
                if b >= 20 and not (0.75 * b <= a <= 1.25 * b): P.append(f'length {k}: {a} vs {b}')
    for k in ('rows', 'items', 'events', 'cats', 'pains', 'criteria', 'companies', 'features', 'signs', 'bars'):
        if isinstance(model.get(k), list) and isinstance(ans.get(k), list) and len(model[k]) != len(ans[k]):
            P.append(f'{k}: {len(ans[k])} items vs {len(model[k])}')
    if not ans.get('sources'): P.append('no sources')
    blob = yaml.dump({k: v for k, v in ans.items() if k not in ('sources', 'logos')}, allow_unicode=True)
    w = sorted({m.group(0).lower() for m in EDWORDS.finditer(blob)})
    if w: P.append('EdTech words: ' + ', '.join(w))
    return P


OUTDIR = None
MISSING = set()


def slugify(n):
    return re.sub(r'[^a-z0-9]+', '-', str(n).lower()).strip('-')


def logo(name, deck_rel=True):
    """company name -> logo path seen from deck.html: assets/logos (and pp/), else a generated initials tile (listed as missing)"""
    if isinstance(name, dict): name = next(iter(name), '')
    name = re.split(r'\s+[—-]\s+https?://', str(name))[0].split(' / ')[-1].strip()
    base = slugify(name); cands = [base]
    short = re.sub(r'-(therapeutics|biotherapeutics|biopharma|biotechnology|biotech|medicines|bio|inc|sciences|pharmaceuticals?)$', '', base)
    cands += [short, short + '-therapeutics', short + '-bio', short + '-biopharma']
    for c in cands:
        for d in ('assets/logos', 'assets/logos/pp'):
            if (ROOT / d / f'{c}.png').exists(): return f'../../{d}/{c}.png'
    MISSING.add(name)
    from PIL import Image, ImageDraw, ImageFont
    ini = ''.join(w[0] for w in re.findall(r'[A-Za-z0-9]+', name)[:2]).upper() or '?'
    f = OUTDIR / 'media/ini' / f'{base}.png'; f.parent.mkdir(parents=True, exist_ok=True)
    if not f.exists():
        im = Image.new('RGB', (200, 200), 'white'); d = ImageDraw.Draw(im)
        ft = ImageFont.truetype(str(ROOT / 'assets/fonts/Lexend-SemiBold.ttf'), 84)
        w = d.textlength(ini, font=ft); d.text(((200 - w) / 2, 48), ini, font=ft, fill='#062A3C'); im.save(f)
    return f'media/ini/{base}.png'


def fill_list(model_list, ans_list):
    """answer items keep the logo fields of the model shape, filled from the company names"""
    out = []
    for i, it in enumerate(ans_list):
        if not isinstance(it, dict): out.append(it); continue
        m = model_list[min(i, len(model_list) - 1)] if model_list else {}
        it = dict(it)
        nm = it.get('name') or it.get('short')
        if isinstance(m, dict):
            if 'src' in m and 'src' not in it and nm: it['src'] = logo(nm)
            if 'logos' in m and 'logos' not in it: it['logos'] = []
            if 'logos' in it and it['logos'] and isinstance(it['logos'][0], str) and not it['logos'][0].endswith('.png'):
                it['logos'] = [logo(x) for x in it['logos']] if not isinstance(m.get('logos', [None])[0] if m.get('logos') else None, dict) else [{'src': logo(x)} for x in it['logos']]
            for k in ('ini', 'slug', 'domain'):
                if k in m and k not in it and nm: it[k] = {'ini': ''.join(w[0] for w in str(nm).split()[:2]).upper(), 'slug': slugify(nm), 'domain': ''}[k]
        out.append(it)
    return out


def merge(slide, ans):
    s = copy.deepcopy(slide)
    for k, v in ans.items():
        if k in ('status', 'sources', 'comment', 'section', 'logos'): continue
        if k == 't' and isinstance(v, dict):
            t = dict(s.get('t') or {})
            for kk, vv in v.items():
                kk = int(kk) if str(kk).isdigit() else kk
                if kk not in t: continue
                vv = str(vv).replace('\\n', '\n').strip()                  # a literal backslash-n written by the other LLM is a line break
                if '\n\n' not in t[kk]: vv = re.sub(r'\n\s*\n+', '\n', vv)   # no blank paragraph unless the model has one
                t[kk] = vv
            s['t'] = t
        elif k == 'title': s['title'] = clean_title(v)
        elif k == 'note':
            fx = lambda x: ' '.join(f'{a}: {b}' for a, b in x.items()) if isinstance(x, dict) else str(x)
            s['note'] = [fx(x) for x in v] if isinstance(v, list) else fx(v)
        elif k in ('inside',) or (isinstance(v, list) and v and v[0] == '<logo>'): continue
        elif k in ('TL', 'TR', 'BL', 'BR') and isinstance(v, dict) and isinstance(s.get(k), dict):
            s[k] = {**s[k], **{kk: vv for kk, vv in v.items() if kk != 'src'}, 'src': logo(v.get('name', ''))}
        elif isinstance(v, list) and isinstance(s.get(k), list): s[k] = fill_list(s[k], v)
        else: s[k] = v
    names = ans.get('logos') or []
    if s.get('type') == 'pp_radar' and names: s['inside'] = [logo(x) for x in names][:len(s.get('inside') or names)]
    elif s.get('img') and any('/deco/' in x for x in s['img']): pass     # decoration (grey emoji of 'bad customer experience'...) is never a logo slot (12 Nov 2026)
    elif s.get('img') and names:
        s['img'] = [logo(names[i]) if i < len(names) else s['img'][i] for i in range(len(s['img']))]
    elif s.get('img') and str(s.get('type', '')).startswith('x/') and not s['id'].startswith('sig_'):
        s['img'] = [logo('?' + str(i)) for i in range(len(s['img']))]      # EdTech logos never stay on another market's slide
    s.pop('tag', None)
    return s


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('results'); ap.add_argument('--demo'); ap.add_argument('--out'); ap.add_argument('--name')
    ap.add_argument('--pain'); ap.add_argument('--value'); ap.add_argument('--drop-no-data', action='store_true')
    a = ap.parse_args()
    R, errs = parse(a.results)
    global OUTDIR
    out = ROOT / a.out; out.mkdir(parents=True, exist_ok=True); OUTDIR = out
    demo = yaml.safe_load((ROOT / a.demo / 'deck.yaml').read_text())
    pains, vals = a.pain.split(';'), a.value.split(';')
    S, rep, sources = [], [], {}
    blocks = {62: (['ed062', 'ed063', 'ed064', 'ed065'], pains, range(62, 74)), 106: (['ed106', 'ed107', 'ed108', 'ed109'], vals, range(106, 123))}
    done = set()
    for s in demo['slides']:
        sid = s['id']; n0 = int(sid[2:5]) if re.match(r'ed\d{3}', sid) else 0
        blk = next((b for b in blocks.values() if n0 in b[2]), None)
        if blk:
            if id(blk) in done: continue
            done.add(id(blk))
            ids, segs, _ = blk
            for i, seg in enumerate(segs, 1):
                for b in ids:
                    base = next(x for x in demo['slides'] if x['id'] == b)
                    ans = R.get(f'{b}-s{i}')
                    if ans is None: x = copy.deepcopy(base); x['id'] = f'{b}-s{i}'; x['tag'] = 'NO ANSWER'; S.append(x); rep.append((f'{b}-s{i}', ['no answer'])); continue
                    rep.append((f'{b}-s{i}', check(f'{b}-s{i}', REF[b], ans)))
                    x = merge(base, ans); x['id'] = f'{b}-s{i}'
                    if b in ('ed062', 'ed106'):
                        ks = list(x['t']); x['t'][ks[0]] = seg.upper()
                    else:                        # the segment label under the title is the segment name, the same everywhere (Pierre, 12 Nov)
                        lab = str(next(iter(REF[ids[0]]['t'].values()))).strip().upper()   # EdTech label of the segment (AI TUTORS)
                        for k, v in (REF[b].get('t') or {}).items():
                            if isinstance(v, str) and v.strip().upper() == lab and k in x['t']: x['t'][k] = seg.upper()
                    if x.get('subtitle') is not None or b in ('ed065',): x['subtitle'] = seg
                    if ans.get('status') != 'ok': x['tag'] = 'NO DATA'
                    sources[x['id']] = ans.get('sources') or []
                    S.append(x)
            continue
        ans = R.get(sid)
        if ans is None:
            x = copy.deepcopy(s)
            if not x.get('tag'): pass
            elif sid.startswith('sig_'): pass
            S.append(x); continue
        model = REF.get(sid) or s
        rep.append((sid, check(sid, model, ans)))
        if ans.get('status') != 'ok' and a.drop_no_data: rep.append((sid, ['dropped: no data'])); continue   # Pierre, 12 Nov: slides without solid data are removed
        x = merge(s, ans) if ans.get('status') == 'ok' else dict(copy.deepcopy(s), tag='NO DATA')
        sources[sid] = ans.get('sources') or []
        S.append(x)
    ed = out / 'edits.yaml'                      # Claude's fit rewrites (texts too long for their box), kept across re-imports
    dbf = out / 'db.yaml'                        # slides built from our startups database (nmp-seo), applied first, then the edits
    E = {}
    for f in (dbf, ed):
        if f.exists():
            for k, v in (yaml.safe_load(f.read_text()) or {}).items(): E.setdefault(k, {}).update(v)
    DB_DONE = set(yaml.safe_load(dbf.read_text()) or {}) if dbf.exists() else set()
    if E:
        for x in S:
            for k, v in (E.get(x['id']) or {}).items():
                if v is None: x.pop(k, None); continue   # null in edits.yaml removes the field (a demo tag…)
                if k == '__replace__':
                    y = yaml.dump(x, allow_unicode=True, width=10000)
                    for a_, b_ in v.items(): y = y.replace(a_, b_)
                    x.clear(); x.update(yaml.safe_load(y)); continue
                if isinstance(x.get('t'), dict) and str(k).isdigit(): x['t'][int(k)] = v
                elif k in ('title', 'note'): x[k] = v
                else:                     # any other field (cats, groups, events…): replaced; company names in logos become logo paths
                    m = REF.get(re.sub(r'-s\d$', '', x['id'])) or {}
                    x[k] = fill_list(m.get(k) or [], v) if isinstance(v, list) and v and isinstance(v[0], dict) else v
    def nl(v):                                   # a literal backslash-n anywhere (firm names of ed042…) is a line break
        if isinstance(v, str): return v.replace('\\n', '\n')
        if isinstance(v, list): return [nl(y) for y in v]
        if isinstance(v, dict): return {k: nl(y) for k, y in v.items()}
        return v
    S = [nl(x) for x in S]
    # a slide that cannot be filled completely is removed, never shown with holes (Pierre, 12 Nov 2026: products grid of a market
    # with few products). `drop: true` in edits.yaml removes a slide by hand; the products grid is dropped as soon as one cell is empty.
    def holes(x): return x.get('type') == 'x/products_services_sold_market' and any(str(v).strip() == '' for v in (x.get('t') or {}).values())
    for x in S:
        if x.get('drop') or holes(x): print('slide dropped (incomplete or drop: true):', x['id'], x.get('type'))
    S = [x for x in S if not (x.get('drop') or holes(x))]
    for x in S:                                  # a field the model does not have is dropped (pp_radar: the caption is the note, 12 Nov)
        m = REF.get(re.sub(r'-s\d$', '', x['id']))
        if m and 'note' in x and 'note' not in m: x.pop('note')
    for x in S:                                  # every text keeps the paragraph structure of its model (Pierre, 12 Nov: slide 120 lost its styles)
        m = REF.get(re.sub(r'-s\d$', '', x['id']))
        if m and isinstance(x.get('t'), dict) and isinstance(m.get('t'), dict):
            for k in x['t']: x['t'][k] = like_model(x['t'][k], m['t'].get(k))
    for x in S:                                  # titles: no doubled words left by the market-name swap
        if x.get('title'): x['title'] = re.sub(r'\b(\w+) \1\b', r'\1', re.sub(r'\bWho is in in vivo', 'Who is in the in vivo', x['title']), flags=re.I) if 'in in vivo' not in x['title'] else x['title'].replace('in in vivo CAR-T,', 'in the in vivo CAR-T market,')
    for x in S:                                  # what the yellow tag says now
        b = re.sub(r'-s\d$', '', x['id'])
        if x['type'] in ('agenda', 'cover') or b in ('ed002', 'ed003', 'ed221'): x.pop('tag', None)
        elif b in DB_IDS and x['id'] not in DB_DONE: x['tag'] = 'FROM OUR DATABASE: TO BUILD'
        elif x['id'] in DB_DONE: x.pop('tag', None)
        elif b in {f'ed{n}' for n in range(215, 221)} and not (out / 'sources_key.yaml').exists(): x['tag'] = 'SOURCES: TO BUILD'
    for x in S:                                  # pp_grid cells written as company names: slugs + logo paths
        if x.get('type') == 'pp_grid' and not x.get('tiles') and any(' ' in n or n[:1].isupper() for row in x['cells'] for cell in row for n in cell):
            srcs = {}
            x['cells'] = [[[slugify(n) for n in cell] for cell in row] for row in x['cells']]
            for row, rown in zip(x['cells'], (yaml.safe_load(dbf.read_text()) or {}).get(x['id'], {}).get('cells', [])):
                for cell, celln in zip(row, rown):
                    for sl, n in zip(cell, celln): srcs[sl] = logo(n)
            x['srcs'] = srcs
    lf = out / 'live.yaml'                       # product-page twins: the slide of the live product page, copied as is (Pierre, 12 Nov 2026:
    if lf.exists():                              # "pour les 12 pages qui illustrent la page produit tu aurais dû reprendre exactement ça")
        LV = yaml.safe_load(lf.read_text()) or {}
        for j, y in enumerate(S):
            if y['id'] in LV: S[j] = {**{k: y[k] for k in ('id', 'type', 'section') if k in y}, **LV[y['id']]}
        for k in LV:
            if not any(y['id'] == k for y in S): print('live.yaml: slide not in deck', k)
    sf = out / 'sources_slides.yaml'             # full list of sources (tools/build_sources.py), after the key-source slides
    if sf.exists():
        for e in yaml.safe_load(sf.read_text()) or []:
            i = next((j for j, y in enumerate(S) if y['id'] == e['after']), None)
            if i is not None: S.insert(i + 1, e['slide'])
    xf = out / 'extras.yaml'                     # validated extra slides (slides complémentaires), each after a given slide id
    if xf.exists():
        for e in yaml.safe_load(xf.read_text()) or []:
            i = next((j for j, y in enumerate(S) if y['id'] == e['after']), None)
            if i is None: print('extra slide: anchor not found', e['after']); continue
            if not e.get('link'):                  # RULES.md « liant » : the slide before must announce the extra slide
                print('extra slide: no link written for', e['slide'].get('id'), '(say which phrase of', e['after'], 'leads to it)')
            S.insert(i + 1, e['slide'])
    D = {k: v for k, v in demo.items() if k != 'slides'}; D['slug'] = Path(a.out).name; D['slides'] = S
    (out / 'deck.yaml').write_text(yaml.dump(D, allow_unicode=True, sort_keys=False, width=1000))
    (out / 'sources.yaml').write_text(yaml.dump(sources, allow_unicode=True, sort_keys=False, width=1000))
    bad = [(k, p) for k, p in rep if p]
    md = [f'# Research import report\n\n{len(R)} answers parsed, {len(errs)} YAML errors, {len(bad)} slides with remarks.\n']
    for e in errs: md.append(f'- YAML error {e[0]}: {e[1]}')
    for k, p in bad: md.append(f'- **{k}**: ' + '; '.join(p))
    (out / 'research_report.md').write_text('\n'.join(md) + '\n')
    (out / 'logos_missing.txt').write_text('\n'.join(sorted(n for n in MISSING if not n.startswith('?'))) + '\n')
    print(len(MISSING), 'logos missing;', len(S), 'slides;', len(R), 'answers;', len(errs), 'yaml errors;', len(bad), 'with remarks ->', out / 'research_report.md')


if __name__ == '__main__':
    main()
