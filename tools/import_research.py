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
import sys as _sys; _sys.path.insert(0, str(Path(__file__).resolve().parent))   # tools/ (run with -I)
ROOT = Path(__file__).resolve().parent.parent
REF = {s['id']: s for s in yaml.safe_load((ROOT / 'decks/edtech-full/deck.yaml').read_text())['slides']}



def tidy_numbers(v):
    """amounts and shares read at a glance (Pierre, 14 Nov 2026: « $56.01B » makes no sense, « $56B » does):
    $10B or more -> no decimal, under $10B -> one decimal at most, same for M and K; a share keeps one decimal at most"""
    def amt(m):
        x = float(m.group(1).replace(',', '')); u = m.group(2)
        r = f'{x:.0f}' if x >= 10 else f'{x:.1f}'.rstrip('0').rstrip('.')
        return '$' + r + u
    v = re.sub(r'\$(\d+\.\d+)(B|M|K)\b', amt, v)
    v = re.sub(r'\$(\d+)\.0(B|M|K)\b', r'$\1\2', v)   # « $1.0B » -> « $1B »
    v = re.sub(r'(?<![\d.])(\d+\.\d)\d+%', lambda m: m.group(1).rstrip('0').rstrip('.') + '%', v)
    return v
def tidy_all(x, k=None):
    if isinstance(x, dict): return {kk: tidy_all(vv, kk) for kk, vv in x.items()}
    if isinstance(x, list): return [tidy_all(vv, k) for vv in x]
    if isinstance(x, str) and k not in ('url', 'src', 'href', 'link', 'note'): return tidy_numbers(x)   # the note keeps the exact figures of the arithmetic
    return x

def use_model(deck):
    """the reference deck (In Vivo CAR-T, 12 Nov 2026) becomes the model; EdTech stays for the slides it does not have"""
    for s in yaml.safe_load((ROOT / deck / 'deck.yaml').read_text())['slides']:
        m = re.match(r'(ed\d{3})-s(\d)$', s['id'])
        if m and m.group(2) != '1': continue
        REF[m.group(1) if m else s['id']] = s
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


DOMAINS = {}          # company name (lower case) -> website domain, read from the answers (logos lists, rows)
_GLOBE = None


def fetch_logo(domain, slug):
    """square logo from the site's own favicon (Google favicon service, 256 px), the way the In Vivo logos were checked (12 Nov 2026).
    Only the domain name leaves the machine. The generic globe returned for unknown sites is refused."""
    import hashlib, subprocess, tempfile
    from PIL import Image
    global _GLOBE
    def get(d):
        f = tempfile.mktemp(suffix='.png')
        r = subprocess.run(['curl', '-sSL', '-m', '15', '-o', f, f'https://www.google.com/s2/favicons?domain={d}&sz=256'], capture_output=True)
        return f if r.returncode == 0 and Path(f).exists() else None
    if _GLOBE is None:
        g = get('no-such-site-nmp-xyz.invalid'); _GLOBE = hashlib.md5(Path(g).read_bytes()).hexdigest() if g else ''
    f = get(re.sub(r'^https?://|/.*$', '', domain))
    if not f: return False
    b = Path(f).read_bytes()
    if hashlib.md5(b).hexdigest() == _GLOBE: return False
    try: im = Image.open(f).convert('RGBA')
    except Exception: return False
    if im.width < 96: return False
    bg = Image.new('RGBA', im.size, 'white'); bg.alpha_composite(im)
    bg.convert('RGB').save(ROOT / 'assets/logos' / f'{slug}.png'); print('logo fetched from favicon:', slug, domain)
    return True


LIBS = [Path('/home/claude/nmp-pages/nmp-funding/logos'), Path('/home/claude/nmp-product-pages/w/logos_all')]
MARKET = ''


GENERIC_ICONS = set('🤒 🤥 🟢 💰 📈 🤝 🏦 📉 💎 🔒 ⛔ 💀 🏆 🚀 ✅ ❌ ⚖️ 😤 😖 ☠️ ⚠️ 💥 🎯 🔀 ♾️ ⏳ 🛡️ 🤩 🔍 📊 💡 🧩 🔁 🔄'.split())
_SITES = None


def base_site(name):
    """website of a company in the nmp-seo startups base, when the research gave no domain"""
    global _SITES
    if _SITES is None:
        _SITES = {}
        try:
            import sys; sys.path.insert(0, '/home/claude/nmp-seo/outils/startups'); import gen_lib as g
            for c in g.Base().companies.values():
                w = (c.get('website') or '').lower()
                if w: _SITES[c['name'].lower()] = re.sub(r'^https?://(www\.)?', '', w).split('/')[0]
        except Exception as e: print('base_site:', e)
    return _SITES.get(name.lower(), '')


def lib_logo(cands):
    """Pierre's logo libraries (repos nmp-pages and nmp-product-pages): square tiles first, wide wordmarks refused"""
    import shutil
    from PIL import Image
    for c in cands:
        if not c: continue
        keys = [c, c.replace('-', '')]
        for lib in LIBS:
            if not lib.exists(): continue
            pats = [f'*/tile/{k}.png' for k in keys] + [f'*/fav/{k}.png' for k in keys] if 'funding' in str(lib) else [f'{MARKET}__{k}.png' for k in keys] + [f'{k}.png' for k in keys] + [f'*__{k}.png' for k in keys]
            for pat in pats:
                for f in sorted(lib.glob(pat)):
                    w, h = Image.open(f).size
                    im = Image.open(f).convert('RGBA'); bg = Image.new('RGBA', im.size, (255, 255, 255, 255)); bg.alpha_composite(im)
                    from PIL import ImageChops
                    bb = ImageChops.difference(bg.convert('RGB'), Image.new('RGB', im.size, (255, 255, 255))).getbbox() or (0, 0, w, h)
                    bw, bh = bb[2] - bb[0], bb[3] - bb[1]
                    if w < 64 or max(w, h) > 2.5 * min(w, h) or bw > 2.5 * bh: continue   # wordmark: unreadable in a square tile
                    out = ROOT / 'assets/logos/lib' / f'{c}.png'; out.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy(f, out); return f'../../assets/logos/lib/{c}.png'
    return None


def logo(name, deck_rel=True):
    """company name -> logo path seen from deck.html: assets/logos (and pp/), else a generated initials tile (listed as missing)"""
    domain = ''
    if isinstance(name, dict): domain = name.get('domain') or ''; name = name.get('name') or next(iter(name.values()), '')
    name = re.split(r'\s+[—-]\s+https?://', str(name))[0].split(' / ')[-1].strip()
    domain = domain or DOMAINS.get(name.lower(), '') or base_site(name)
    base = slugify(name.replace('²', '2').replace('³', '3')); cands = [base]
    short = re.sub(r'-(therapeutics|biotherapeutics|biopharma|biotechnology|biotech|medicines|bio|inc|sciences|pharmaceuticals?|robotics|robot|ai|labs|technologies|technology|dynamics)$', '', base)
    cands += [short, short + '-therapeutics', short + '-bio', short + '-biopharma', short + '-robotics', short + '-ai']
    for c in cands:
        if (ROOT / 'assets/logos' / f'{c}.png').exists(): return f'../../assets/logos/{c}.png'
    hit = lib_logo(cands)
    if hit: return hit
    for c in cands:
        if (ROOT / 'assets/logos/pp' / f'{c}.png').exists(): return f'../../assets/logos/pp/{c}.png'
    if domain and fetch_logo(domain, base): return f'../../assets/logos/{base}.png'
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
        elif k in ('inside', 'inside_xy', 'edge_xy') or (isinstance(v, list) and v and v[0] == '<logo>'): continue
        elif k in ('TL', 'TR', 'BL', 'BR') and isinstance(v, dict) and isinstance(s.get(k), dict):
            s[k] = {**s[k], **{kk: vv for kk, vv in v.items() if kk != 'src'}, 'src': logo(v.get('name', ''))}
        elif isinstance(v, list) and isinstance(s.get(k), list): s[k] = fill_list(s[k], v)
        else: s[k] = v
    names = ans.get('logos') or []
    if s.get('type') == 'pp_radar': s.pop('inside_xy', None); s.pop('edge_xy', None)   # exact tiles belong to the model's live page only
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
    ap.add_argument('--model', help='reference deck used as model (decks/in-vivo-car-t)'); ap.add_argument('--model-words', default=''); ap.add_argument('--model-name', default='')
    a = ap.parse_args()
    global EDWORDS
    if a.model:
        use_model(a.model)
        if a.model_words: EDWORDS = re.compile(r'\b(' + '|'.join(re.escape(w.strip()) for w in a.model_words.split(',')) + r')\b', re.I)
    R, errs = parse(a.results)
    def walk(v):
        if isinstance(v, dict):
            if v.get('name') and v.get('domain'): DOMAINS[str(v['name']).lower()] = v['domain']
            for x in v.values(): walk(x)
        elif isinstance(v, list):
            for x in v: walk(x)
    walk(R)
    global OUTDIR, MARKET
    out = ROOT / a.out; out.mkdir(parents=True, exist_ok=True); OUTDIR = out; MARKET = out.name
    demo = yaml.safe_load((ROOT / a.demo / 'deck.yaml').read_text())
    pains, vals = a.pain.split(';'), a.value.split(';')
    S, rep, sources = [], [], {}
    NOANS = []
    KEEP = set()                                 # slides whose content comes from live.yaml (twin of the live page) or edits.yaml (`keep: true`, our own estimate): never dropped as no_data
    for f_ in ('live.yaml', 'edits.yaml'):
        if (out / f_).exists(): KEEP |= {k for k, v in (yaml.safe_load((out / f_).read_text()) or {}).items() if f_ == 'live.yaml' or (isinstance(v, dict) and v.get('keep'))}
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
            if not str(s.get('type', '')).startswith(('x/divider', 'agenda', 'cover', 'sources', 'intro')) and not sid.startswith('src_') and sid not in ('ed001', 'ed002', 'ed003', 'ed004', 'ed005'): NOANS.append(sid)   # the research did not answer it: it still holds the reference market's content
            if not x.get('tag'): pass
            elif sid.startswith('sig_'): pass
            S.append(x); continue
        model = REF.get(sid) or s
        rep.append((sid, check(sid, model, ans)))
        if ans.get('status') != 'ok' and a.drop_no_data and sid not in KEEP: rep.append((sid, ['dropped: no data'])); continue   # Pierre, 12 Nov: slides without solid data are removed
        x = merge(s, ans) if ans.get('status') == 'ok' else dict(copy.deepcopy(s), **({} if sid in KEEP else {'tag': 'NO DATA'}))   # kept without data only when live.yaml or edits.yaml (`keep: true`) gives the content
        sources[sid] = ans.get('sources') or []
        S.append(x)
    for x in S:                                  # a market with N categories answers ed018 with a `categories:` list: the slide takes the N-item template at once,
        if x.get('categories') and x.get('type') == 'x/categorize_companies_market':      # so the 4 model slots (and their words) never stay under it (13 Nov 2026)
            x['categorization'] = (x.get('t') or {}).get(25) or (x.get('t') or {}).get('25') or ''; x['type'] = 'sx_categories_n'; x.pop('t', None)
            x['categories'] = [dict(label=c.get('label'), description=c.get('description'), emoji=c.get('emoji') or c.get('e')) for c in x['categories']]
    ed = out / 'edits.yaml'                      # Claude's fit rewrites (texts too long for their box), kept across re-imports
    def _talk():                                 # a note that talks about the prompt (« the four specified groups », « original short-card label limits ») is not for the reader (13 Nov 2026)
        for x in S:
            n = ' '.join(x['note']) if isinstance(x.get('note'), list) else str(x.get('note') or '')
            m = re.search(r'\b(template|specified|short-card|label limits?|the model (has|slide)|slots?|verbatim|placeholder)\b', n, re.I)
            if m: print('PROMPT TALK', x['id'], '«', m.group(0), '»', n[:90])
    dbf = out / 'db.yaml'                        # slides built from our startups database (nmp-seo), applied first, then the edits
    for f in (out / 'edits.yaml', out / 'live.yaml', out / 'db_text.yaml', out / 'lengths.yaml'):      # a key written twice silently drops the first block (12 Nov 2026: ed018 lost its categories)
        if f.exists():
            ks = re.findall(r'(?m)^([A-Za-z0-9_-]+):', f.read_text()); d = {k for k in ks if ks.count(k) > 1}
            if d: raise SystemExit(f'DUPLICATE KEY in {f.name}: {sorted(d)}')
    E = {}
    for f in (dbf, ed, out / 'lengths.yaml'):   # lengths.yaml: texts brought into their spec range (method v2), applied last; its replacements are `__replace2__`
        if f.exists():
            for k, v in (yaml.safe_load(f.read_text()) or {}).items(): E.setdefault(k, {}).update(v)
    DB_DONE = set(yaml.safe_load(dbf.read_text()) or {}) if dbf.exists() else set()
    if E:
        for x in S:
            for k, v in (E.get(x['id']) or {}).items():
                if v is None: x.pop(k, None); continue   # null in edits.yaml removes the field (a demo tag…)
                if k in ('__replace__', '__replace2__'):
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
        elif x.get("tag") == "PRODUCT PAGE: TO COPY" and (out / "live.yaml").exists() and x["id"] in (yaml.safe_load((out / "live.yaml").read_text()) or {}): x.pop("tag", None)
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
            if str(e['slide'].get('type', '')).startswith('x/sig_') and not any(e['slide'].get(k) for k in ('vbars', 'hbars', 'dots', 'curves', 'split')): print('FIXED CHART', e['slide'].get('id'), e['slide']['type'], ': a converted chart keeps the bar sizes of its original data, give `vbars`, `hbars`… or use a data template (13 Nov 2026: Humanoid slide 51 showed the bars of another market)')
            if not e.get('link') or str(e['link']).startswith('TO WRITE'):                  # RULES.md « liant » : the slide before must announce the extra slide
                print('extra slide: no link written for', e['slide'].get('id'), '(say which phrase of', e['after'], 'leads to it)')
            S.insert(i + 1, e['slide'])
    # SIGNAL slides show momentum NOW (Pierre, 12 Nov 2026): each one states the period of its newest figure in `fresh: {period, end: YYYY-MM}`
    #   month: at most 6 months old ; quarter: 9 months ; half: 12 months ; total (cumulative proof at a date): 12 months ;
    #   year: the current year (an estimate « should sell… » derived from the published months, explained in the note) or last year until April 30.
    import datetime as _dt
    _today = _dt.date.today(); _lim = dict(month=6, quarter=9, half=12, total=12)
    for x in S:
        if x.get('pill') != 'SIGNAL' or str(x.get('type', '')).startswith('pp_'): continue
        fr = x.get('fresh')
        if not fr: print('SIGNAL NO DATE', x['id'], '(add fresh: {period, end})'); continue
        y, m = map(int, str(fr['end']).split('-')); age = (_today.year - y) * 12 + _today.month - m
        ok = (y >= _today.year or (y == _today.year - 1 and _today.month <= 4)) if fr['period'] == 'year' else age <= _lim[fr['period']]
        if not ok: print('SIGNAL STALE', x['id'], fr, f'{age} months old')
    def _semi(v, k=None):                         # no semicolon in slide texts (same rule as the product pages): two sentences instead
        if isinstance(v, str): return v if k in ('url', 'image', 'src', 'logo_src', 'csv') or v.startswith('http') else re.sub(r';\s+(\w)', lambda m: '. ' + m.group(1).upper(), v)
        if isinstance(v, dict): return {a: (b if a in ('sources', 'links') else _semi(b, a)) for a, b in v.items()}
        if isinstance(v, list): return [_semi(b, k) for b in v]
        return v
    S = [_semi(x) for x in S]
    _talk()
    _given = set()                               # content given by live.yaml, db.yaml, edits.yaml or extras.yaml
    for f_ in ('live.yaml', 'db.yaml', 'edits.yaml'):
        if (out / f_).exists(): _given |= set(yaml.safe_load((out / f_).read_text()) or {})
    _left = [i for i in NOANS if i not in _given and any(x['id'] == i for x in S)]
    if _left and R: print('NO ANSWER (the slide still shows the reference market, give it in live.yaml or edits.yaml, or drop it):', ' '.join(_left))
    _rad = next((x for x in S if x.get('id') == 'ed007p'), None)   # the eye decides (a corner can be an edge case that is in the market, or an incumbent named as context): the list only makes sure it is looked at (14 Nov 2026: Tempus AI outside the radar and leader on three slides)
    for c in ('TL', 'TR', 'BL', 'BR'):
        nm = ((_rad or {}).get(c) or {}).get('name')
        if not nm: continue
        w = nm.split()[0]
        ids = [x.get('id') for x in S if x.get('id') != 'ed007p' and not str(x.get('id')).startswith('src_') and re.search(r'\b' + re.escape(w) + r'\b', json.dumps(x, ensure_ascii=False), re.I)]
        if ids: print(f'radar corner {nm} is named on:', ' '.join(map(str, ids)))
    cv = out / 'cover.yaml'                      # cover layout copied from Pierre's cover slide (tools/cover_from_slides.py)
    if cv.exists() and S and S[0].get('type') == 'cover':
        import shutil
        S[0].update(yaml.safe_load(cv.read_text())); (out / 'media').mkdir(exist_ok=True); shutil.copy(ROOT / 'assets/covers' / f'{out.name}.jpg', out / 'media/cover.jpg')
    elif S and S[0].get('type') == 'cover': print('COVER NOT COPIED: run tools/cover_from_slides.py (the cover follows Pierre\'s cover slide, never a general layout)')
    ff = out / 'db_facts.yaml'                   # {db.key} in any text = a figure from the latest startups base (make_db_slides.py), never typed by hand
    if ff.exists():
        F = yaml.safe_load(ff.read_text()) or {}
        def dbf(v):
            if isinstance(v, str):
                m = re.fullmatch(r'\{db\.(\w+)\}', v.strip())
                if m and m.group(1) in F: return F[m.group(1)]          # a lone figure keeps its type (bar values)
                return re.sub(r'\{db\.(\w+)\}', lambda m: str(F.get(m.group(1), m.group(0))), v)
            if isinstance(v, dict): return {k: dbf(x) for k, x in v.items()}
            if isinstance(v, list): return [dbf(x) for x in v]
            return v
        S = [dbf(x) for x in S]
    for x in S:                                  # contrast slides: 8 rows (Pierre, 12 Nov 2026: 10 rows took too much room). `rows_drop: [i, j]` in edits.yaml removes the two weakest
        if x.get('type') == 'contrast':
            drop = x.pop('rows_drop', None) or []; x['rows'] = [r for i, r in enumerate(x.get('rows') or []) if i not in drop]
            if len(x.get('rows') or []) != 8: print('CONTRAST ROWS', x['id'], len(x.get('rows') or []), '(8 expected)')
    for x in S:                                  # contrast slides: the logo of the company on the right, found like every other logo (12 Nov 2026)
        if x.get('type') == 'contrast' and x.get('right'):
            nm = {'FIGURE': 'Figure AI', 'AGILITY ROBOTICS': 'Agility Robotics', 'UNITREE': 'Unitree Robotics', '1X': '1X Technologies'}.get(x['right'].upper(), x['right'].title())
            x['logo_src'] = logo(nm)
    for x in S:                  # segment dividers carry no slide title (Pierre, 14 Nov 2026: « Pain points: Hospitals… » sat over the arrows)
        if x.get('type') == 'x/divider_3': x.pop('title', None)
    for x in S:                  # a converted chart with fixed geometry needs its data (14 Nov 2026: the valuation lines of the original PowerPoint were shown in two decks)
        if x.get('type') == 'x/fast_startups_growing' and not x.get('growth'): print('FIXED CHART', x.get('id'), x['type'], ': give `growth: {36: {pts: [[years since founding, value], …]}, 37: …}` in edits.yaml, or drop the slide')
    if a.model:                  # icons copied from the reference market and still identical: a leftover when they belong to its domain (12 Nov 2026: 🧬 🦠 💉 in Humanoid Robotics)
        _M = {y.get('id'): y for y in yaml.safe_load((ROOT / a.model / 'deck.yaml').read_text())['slides']}
        _EDITS = (yaml.safe_load((out / 'edits.yaml').read_text()) or {}) if (out / 'edits.yaml').exists() else {}
        for x in S:
            _id = x.get('id') or ''   # a page of a series is compared with the same page of the model, then its first page (14 Nov 2026: the lookup dropped '-s1' and no series page was ever checked)
            m = _M.get(re.sub(r'-s\d+$', '-s1', _id)) or _M.get(_id) or _M.get(re.sub(r'-s\d+$', '', _id))   # every page of a series is built from the model's first page
            if not m: continue
            _ed = (_EDITS.get(_id) or {})   # an icon written in edits.yaml is a choice, even when it equals the model's
            pairs = [(k, v) for k, v in (x.get('t') or {}).items() if isinstance(v, str) and len(v) <= 3 and v == (m.get('t') or {}).get(k) and k not in _ed]
            pairs += [(k, x[k]) for k in ('icon_tl', 'icon') if x.get(k) and x.get(k) == m.get(k)]
            for k, v in pairs:
                if re.search('[\U0001F300-\U0001FAFF\u2600-\u27BF]', v) and v.strip() not in GENERIC_ICONS: print('MODEL ICON LEFT', x['id'], k, v)
    if a.model_name:             # the reference market's name left in slides nobody rewrote (agenda kicker, sources divider…) becomes the new name
        mn, nn = a.model_name, a.name
        def sw(v):
            if isinstance(v, str):
                v = re.sub(re.escape(mn.upper()), nn.upper(), v); v = re.sub(re.escape(mn[0].upper() + mn[1:]), nn[0].upper() + nn[1:], v)
                return re.sub(re.escape(mn), nn, v, flags=re.I)
            if isinstance(v, list): return [sw(y) for y in v]
            if isinstance(v, dict): return {k: sw(y) for k, y in v.items()}
            return v
        S = [sw(x) for x in S]
        left = [x['id'] for x in S if re.search(re.escape(mn), yaml.dump(x, allow_unicode=True), re.I)]
        if left: print('MODEL MARKET LEFT in', left); rep.append(('model market', ['name left in ' + ', '.join(left)]))
    D = {k: v for k, v in demo.items() if k != 'slides'}; D['slug'] = Path(a.out).name; D['slides'] = S
    for x in S:                  # fixed shapes of some slides (Pierre, 14 Nov 2026)
        t = x.get('t') if isinstance(x.get('t'), dict) else {}
        if x.get('type') == 'x/markets_sit_between':      # the three circles: always two words, one per line
            for k in (8, 9, 10):
                w = re.sub(r'<br>|\n', ' ', str(t.get(k, ''))).split()
                if len(w) == 2: t[k] = '\n'.join(w)
                elif t.get(k): print('VENN WORDS', x.get('id'), k, repr(t[k]), ': two words, one per line')
        if x.get('type') in ('x/top_companies_market', 'x/top_companies_market_2'):   # company names in capitals
            for k in range(8, 24, 2):
                if isinstance(t.get(k), str) and len(t[k]) < 30: t[k] = t[k].upper()
    S[:] = [tidy_all(x) for x in S]
    _DBIDS = set(yaml.safe_load((out / 'db.yaml').read_text()) or {}) if (out / 'db.yaml').exists() else set()
    import spec as _spec          # method v2 (14 Nov 2026): every text against its range in specs/slides.yaml. Capitals are applied, lengths are reported
    for x in S:
        E = _spec.SPEC.get(_spec.tpl(x)) or {}
        if isinstance(x.get('t'), dict):
            for k, v in list(x['t'].items()):
                if (E.get(str(k)) or {}).get('caps') and isinstance(v, str): x['t'][k] = re.sub(r'(?<!\{)\b([a-z])', lambda m: m.group(1).upper(), v) if '{' in v else v.upper()
        if isinstance(x.get('t'), dict):           # an icon on its own line in the sibling boxes stays on its own line (14 Nov 2026: « ⚖️ FDA… » overflowed slide 123)
            EM = r'^([\U0001F300-\U0001FAFF\u2600-\u27BF]\ufe0f?)'
            if sum(1 for v in x['t'].values() if isinstance(v, str) and re.match(EM + r'\n', v)) >= 2:
                for k, v in list(x['t'].items()):
                    if isinstance(v, str) and re.match(EM + r' ', v): x['t'][k] = re.sub(EM + r' +', r'\1\n', v)
        for p_ in _spec.problems(x):              # a sentence built from the base (db.yaml) cannot take a fact we do not have: only its maximum counts
            if 'capitals' not in p_ and not (x.get('id') in _DBIDS and 'too short' in p_): print('TEXT LENGTH', p_)
    _PLC = set('INDIA CHINA JAPAN TAIWAN ISRAEL UK US FRANCE GERMANY SWITZERLAND NORDICS CANADA BRAZIL MEXICO UAE AFRICA AUSTRALIA SINGAPORE'.split()) | {'JAPAN AND KOREA', 'SOUTH KOREA', 'UNITED KINGDOM', 'UNITED STATES', 'SAUDI ARABIA', 'SOUTHEAST ASIA', 'NEW ZEALAND',
            'NORTH AMERICA', 'EUROPE', 'ASIA-PACIFIC', 'MIDDLE EAST & AFRICA', 'LATIN AMERICA'}
    for x in S:                  # a renamed map region must be a place the map knows, so its dot moves with it (14 Nov 2026)
        for k, r in ((x.get('regions') or {}).items() if x.get('type') == 'worldmap' else []):
            nm = str(r.get('name') or '').upper().split(' - ')[0].strip()
            if nm and nm not in _PLC and not r.get('at'): print('MAP PLACE', x.get('id'), k, nm, ': name a known place or give `at: [x, y]`')
    for i, x in enumerate(S):    # the pages of a series (1/3, 2/3, 3/3) share one design and one number of items (Pierre, 14 Nov 2026: 6 rows on 1/3, 4 on 2/3 and 3/3)
        m = re.fullmatch(r'1/(\d)', str(x.get('page') or ''))
        if not m: continue
        G = S[i:i + int(m.group(1))]
        cnt = lambda y: len(y.get('rows') or y.get('items') or y.get('categories') or []) or sum(1 for v in (y.get('t') or {}).values() if isinstance(v, str) and v.strip())
        DATED = {'startups_news_lately', 'rounds_were_announced_last', 'startups_stumbled_lately', 'were_latest_tech_infra_developments'}   # one look: the dated timeline
        fam = lambda y: (lambda b: 'dated' if b in DATED else b)(re.sub(r'^x/|_\d$', '', str(y.get('type'))))
        if len({fam(y) for y in G}) > 1 or len({cnt(y) for y in G}) > 1:
            print('SERIES MIXED', ' '.join(f"{y.get('id')}={y.get('type')}:{cnt(y)}" for y in G), ': one design and one count on every page, or take the odd page out of the series (`page: null`)')
    (out / 'deck.yaml').write_text(yaml.dump(D, allow_unicode=True, sort_keys=False, width=1000))
    (out / 'sources.yaml').write_text(yaml.dump(sources, allow_unicode=True, sort_keys=False, width=1000))
    bad = [(k, p) for k, p in rep if p]
    md = [f'# Research import re, jsonport\n\n{len(R)} answers parsed, {len(errs)} YAML errors, {len(bad)} slides with remarks.\n']
    for e in errs: md.append(f'- YAML error {e[0]}: {e[1]}')
    for k, p in bad: md.append(f'- **{k}**: ' + '; '.join(p))
    (out / 'research_report.md').write_text('\n'.join(md) + '\n')
    (out / 'logos_missing.txt').write_text('\n'.join(sorted(n for n in MISSING if not n.startswith('?'))) + '\n')
    print(len(MISSING), 'logos missing;', len(S), 'slides;', len(R), 'answers;', len(errs), 'yaml errors;', len(bad), 'with remarks ->', out / 'research_report.md')


if __name__ == '__main__':
    main()
