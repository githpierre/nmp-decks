"""In Vivo CAR-T demo deck (DEMO DATA) from the EdTech reference deck, following plans/in-vivo-car-t.md.

    python3 tools/make_invivo_demo.py      -> decks/invivo-demo/deck.yaml (+ media)

Purpose: show the structure and the look of an In Vivo CAR-T deck before the research. Every slide carries a yellow DEMO DATA tag.
Words are swapped automatically (companies, customers, segments); figures are EdTech's and mean nothing here.
The real content comes from the research prompts.
"""
import re, shutil, yaml, copy
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
SRC, OUT = ROOT / 'decks/edtech-full', ROOT / 'decks/invivo-demo'

# ---------- 1. words -------------------------------------------------------------------------------
COMPANIES = [  # EdTech name -> In Vivo name (demo pairing, no meaning)
    ('Khan Academy', 'Sana'), ('Duolingo', 'Capstan'), ('Coursera', 'Interius'), ('Udemy', 'Umoja'), ('edX', 'Kelonia'),
    ('Babbel', 'EsoBiotec'), ('Rosetta', 'Azalea'), ('Praktika', 'Vyriad'), ('Chegg', 'Exuma'), ('Byju’s', 'Carisma'), ("Byju's", 'Carisma'),
    ('Unacademy', 'Myeloid'), ('2U', 'Abintus'), ('Pearson', 'Novartis'), ('MasterClass', 'Moderna'), ('Zoom', 'Lonza'),
    ('OpenAI', 'BioNTech'), ('ChatGPT Edu', 'Kymriah'), ('ChatGPT', 'Kymriah'), ('Microsoft', 'AbbVie'), ('Google Classroom', 'Yescarta'),
    ('Google', 'Gilead'), ('Preply', 'Ensoma'), ('SpeakX', 'Genocury'), ('Speak', 'Orna'), ('LearnVector', 'Sail Bio'), ('Yoodli', 'Create Medicines'),
    ('Emversity', 'Immorna'), ('MagicSchool', 'Tessera'), ('Multiverse', 'MagicRNA'), ('PhysicsWallah', 'IASO Bio'), ('Gizmo', 'MVRIX'),
    ('Eruditus', 'Legend Biotech'), ('Emeritus', 'Legend Biotech'), ('Nerdy', 'Cellectis'), ('Instructure', 'Kite'), ('Canvas', 'Kite'),
    ('PowerSchool', 'Bristol Myers Squibb'), ('Blackboard', 'Juno'), ('Quizlet', 'ThunderBio'), ('GoStudent', 'Starna'),
    ('Knowunity', 'DeliNova'), ('Brisk', 'Stylus'), ('Amira', 'Vivo Bio'), ('ClassDojo', 'Orbital'), ('Newsela', 'Kyverna'),
    ('Guild', 'Cabaletta'), ('Degreed', 'Autolus'), ('Stepful', 'Arcellx'), ('Teachy', 'Mote'), ('Oboe', 'Ocugen'),
    ('Docebo', 'Allogene'), ('Khanmigo', 'CAP-1002'), ('Grand Canyon Education', 'Legend Biotech'), ('upGrad', 'Lilly'),
    ('LinkedIn', 'Roche'), ('Lynda', 'Poseida'), ('Stride', 'Beam'), ('Medly AI', 'Mote Bio'), ('Alpha School', 'Vivo Bio'),
    ('YouTube', 'PubMed'), ('Moodle', 'Lonza'), ('Workday', 'Thermo Fisher'), ('Turnitin', 'Catalent'), ('GPTZero', 'Charles River'),
]
SEGMENTS = [  # EdTech segments -> In Vivo approaches (categories of companies)
    ('School platforms', 'mRNA-LNP CAR-T'), ('SCHOOL PLATFORMS', 'MRNA-LNP CAR-T'), ('Online courses', 'Lentiviral CAR-T'), ('ONLINE COURSES', 'LENTIVIRAL CAR-T'),
    ('Digital tutoring', 'Gene-editing CAR-T'), ('DIGITAL TUTORING', 'GENE-EDITING CAR-T'), ('Workforce learning', 'Beyond T cells'),
    ('WORKFORCE LEARNING', 'BEYOND T CELLS'), ('Assessment tech', 'Other approaches'), ('ASSESSMENT TECH', 'OTHER APPROACHES'),
    ('Digital credentialing', 'Manufacturing tools'), ('DIGITAL CREDENTIALING', 'MANUFACTURING TOOLS'), ('Credentialing', 'Manufacturing tools'),
    ('CREDENTIALING', 'MANUFACTURING TOOLS'), ('Other spending', 'Other spending'),
]
WORDS = [  # generic words, longest first, case kept by the helper
    ('EdTech market', 'in vivo CAR-T market'), ('EdTech', 'in vivo CAR-T'), ('online learning', 'in vivo therapy'), ('school districts', 'payers'),
    ('learners', 'patients'), ('learner', 'patient'), ('students', 'patients'), ('student', 'patient'), ('teachers', 'oncologists'),
    ('teacher', 'oncologist'), ('schools', 'hospitals'), ('school', 'hospital'), ('classrooms', 'clinics'), ('classroom', 'clinic'),
    ('courses', 'therapies'), ('course', 'therapy'), ('tutoring', 'cell therapy'), ('tutors', 'therapies'), ('tutor', 'therapy'),
    ('education', 'healthcare'), ('districts', 'payers'), ('employers', 'insurers'), ('degrees', 'approvals'), ('homework', 'dosing'),
    ('learning', 'treatment'), ('lessons', 'doses'), ('lesson', 'dose'), ('parents', 'caregivers'), ('universities', 'cancer centers'),
    ('university', 'cancer center'), ('apps', 'platforms'), ('app', 'platform'),
]


def _case(src, dst):
    if src.isupper() and len(src) > 1: return dst.upper()
    if dst.startswith('in vivo'): return dst        # a market name stays lower case inside a sentence
    if src[0].isupper(): return dst[0].upper() + dst[1:]
    return dst


def swap(t):
    if not isinstance(t, str): return t
    for a, b in COMPANIES + SEGMENTS:
        t = re.sub(r'(?<![\w-])' + re.escape(a).replace('\\ ', r'\s+') + r'(?![\w])', b, t)
        if a.upper() != a and len(a) > 3: t = re.sub(r'(?<![\w-])' + re.escape(a.upper()).replace('\\ ', r'\s+') + r'(?![\w])', b.upper(), t)
    for a, b in WORDS:
        t = re.sub(r'(?<![\w-])(' + re.escape(a) + r')(?![\w])', lambda m: _case(m.group(1), b), t, flags=re.I)
    t = re.sub(r'What has already been fixed\s+in in vivo CAR-T, and what is left to solve\?', 'What has already been fixed,\nand what is left to solve?', t)
    t = re.sub(r'\bin in vivo CAR-T market\b', 'in the in vivo CAR-T market', t)
    t = re.sub(r'\bin in vivo CAR-T\b', 'in the in vivo CAR-T space', t)
    t = re.sub(r'(^|[.!?]\s+)in vivo', lambda m: m.group(1) + 'In vivo', t)      # sentence start only
    t = re.sub(r'\b[Aa] in vivo', lambda m: m.group(0)[0] + 'n in vivo', t)
    return t


# ---------- 2. logos ------------------------------------------------------------------------------
POOL = [f'../../assets/logos/{x}.png' for x in ('sail-biomedicines', 'immorna', 'magicrna', 'create-medicines', 'azalea-therapeutics', 'tessera-therapeutics',
                                                 'vyriad', 'umoja-biopharma', 'iaso-biotherapeutics', 'mvrix', 'ensoma', 'thunderbiotech')] + \
       [f'../../assets/logos/pp/{x}.png' for x in ('interius', 'sana', 'abbvie', 'astrazeneca', 'gilead-kite', 'bristol-myers-squibb', 'novartis', 'kite',
                                                    'legend-biotech', 'autolus', 'arcellx', 'allogene', 'cellectis', 'crispr-therapeutics', 'beam', 'moderna',
                                                    'biontech', 'lilly', 'regeneron', 'pfizer')]
LOGO = {}


def logo(p):
    if p not in LOGO: LOGO[p] = POOL[len(LOGO) % len(POOL)]
    return LOGO[p]


def walk(v, key=''):
    if isinstance(v, str):
        if key in ('src',) or (v.endswith('.png') and ('media/raw/' in v or 'assets/logos' in v)):
            return logo(v) if ('media/raw/' in v or 'assets/logos' in v) and 'b8681302' not in v else v
        if key in ('type', 'id', 'csv', 'variant', 'mode', 'handle', 'l', 'slug', 'domain'): return v
        return swap(v)
    if isinstance(v, dict): return {k: walk(x, k) for k, x in v.items()}
    if isinstance(v, list): return [walk(x, key) for x in v]
    return v


# ---------- 3. the 4 biotech slides (DEMO texts on existing templates) ----------------------------
def biotech(E):
    pipe = copy.deepcopy(E[143 - 1]); pipe['id'] = 'iv_pipeline'; pipe['section'] = 'Tech and infra'
    pipe['title'] = 'Where are in vivo CAR-T\nprograms in the clinic?'
    rows = [('CAPSTAN · CPTX2309', 'PH 1', 'mRNA-LNP CAR-T for lupus and other B-cell autoimmune diseases'),
            ('INTERIUS · INT2104', 'PH 1', 'Lentiviral in vivo CAR for B-cell cancers, first patients dosed'),
            ('ESOBIOTEC · ESO-T01', 'PH 1', 'Lentiviral BCMA CAR for multiple myeloma, early responses reported'),
            ('UMOJA · UB-VV111', 'PH 1', 'In vivo CD19 CAR-T for lymphoma and leukemia'),
            ('KELONIA · KLN-1010', 'PH 1', 'BCMA in vivo CAR-T given as one infusion, no chemo before'),
            ('SANA · SG299', 'PRE', 'Fusosome delivery of a CD19 CAR straight to T cells'),
            ('ORNA · ORN-101', 'PRE', 'Circular RNA CAR for autoimmune diseases'),
            ('AZALEA · AZ-01', 'PRE', 'Gene-editing CAR-T made inside the body')]
    keys = [(2, 3, 0), (6, 7, 4), (10, 11, 8), (14, 15, 12), (18, 19, 16), (22, 23, 20), (26, 27, 24), (37, 38, 34)]
    for (kl, kv, kd), (l, v, d) in zip(keys, rows):
        pipe['t'][kl] = l; pipe['t'][kv] = v; pipe['t'][kd] = d
    pipe['note'] = 'DEMO DATA. We will list every in vivo CAR-T program with a public trial, from trial registries and company news.'
    deals = copy.deepcopy(E[156 - 1]); deals['id'] = 'iv_deals'; deals['title'] = 'Which pharma deals\nshaped the market?'
    D = [('2025 (OCT)', 'Bristol Myers Squibb bought Orbital Therapeutics for $1.5B to add its circular RNA in vivo CAR-T', 'Company news'),
         ('2025 (AUG)', 'Gilead and Kite bought Interius for $350M in cash to own its lentiviral in vivo CAR-T platform', 'Company news'),
         ('2025 (JUN)', 'AbbVie bought Capstan for up to $2.1B, its first big bet on mRNA in vivo CAR-T for autoimmunity', 'Company news'),
         ('2025 (MAR)', 'AstraZeneca bought EsoBiotec for up to $1B to add its lentiviral in vivo cell therapy platform', 'Company news'),
         ('2025 (JAN)', 'A top-10 pharma licensed a demo mRNA CAR program for $40M upfront and up to $600M in milestones', 'Demo source'),
         ('2024 (DEC)', 'A demo biotech licensed its T-cell targeted LNP to a big pharma for $25M upfront and royalties', 'Demo source')]
    for (kd, kt), (d, t, src) in zip([(13, 14), (15, 16), (17, 18), (19, 20), (21, 22), (23, 24)], D):
        deals['t'][kd] = d; deals['t'][kt] = t + ' {1|' + src + '}'
    deals.pop('page', None); deals.pop('subtitle', None)
    deals['note'] = 'DEMO DATA. Deal amounts to confirm by the research. We will list acquisitions and licensing deals, with the amount paid upfront and the total.'
    fda = copy.deepcopy(E[147 - 1]); fda['id'] = 'iv_fda'; fda['section'] = 'Market challenges'
    fda['title'] = 'What does the road\nto FDA approval look like?'
    for k, t in {7: 'IND\n\nThe company files a request to start trials in people. The FDA has 30 days to say no.',
                 8: 'PHASE 1\n\nA few dozen patients get the drug. The goal is safety and the right dose, not proof it works.',
                 9: 'PHASE 2\n\nA larger group tests whether the drug works. Strong results can earn faster review.',
                 11: 'PHASE 3 AND BLA\n\nHundreds of patients compare the drug with standard care, then the company files for approval.',
                 10: 'FAST LANES\n\nRMAT and Breakthrough labels shorten reviews. Most in vivo programs are still in phase 1.'}.items():
        fda['t'][k] = t
    fda['note'] = 'DEMO DATA. We will describe each step from FDA guidance, with the usual time per step for cell and gene therapies.'
    safe = copy.deepcopy(E[54 - 1]); safe['id'] = 'iv_safety'; safe['section'] = 'Market challenges'
    safe['title'] = 'Which safety risks worry\ndoctors the most?'
    for k, t in {6: 'CYTOKINE STORM\n\nCAR-T cells can trigger a strong immune reaction with fever and low blood pressure, which needs hospital care',
                 7: 'NERVE EFFECTS\n\nSome patients get confusion or seizures in the days after treatment, so they stay near the hospital',
                 8: 'SECOND CANCERS\n\nThe FDA added a warning about rare T-cell cancers after CAR-T, which every new program must watch',
                 9: 'TODAY\n\nIn vivo CAR-T must also prove that only T cells get the CAR, and that the gene does not reach other cells',
                 10: '?\n\nIf in vivo programs keep side effects low, CAR-T could move from big cancer centers to everyday clinics'}.items():
        safe['t'][k] = t
    safe['note'] = 'DEMO DATA. We will gather the known risks from FDA labels, trial results and medical reviews.'
    return pipe, deals, fda, safe


# ---------- 4. assemble ---------------------------------------------------------------------------
def main():
    E = yaml.safe_load((SRC / 'deck.yaml').read_text())
    S = E['slides']
    by = lambda n: copy.deepcopy(S[n - 1])
    pipe, deals, fda, safe = biotech(S)
    order = []
    for n in range(1, len(S) + 1):
        if 74 <= n <= 85: continue            # pain points: 3 disease blocks only (62-73)
        if 123 <= n <= 130: continue          # value creation: 4 approach blocks only (106-122)
        order.append(by(n))
        if n == 98: order.append(pipe)
        if n == 138: order.append(fda)
        if n == 140: order.append(safe)
        if n == 157: order.append(deals)
    PAIN = {62: 'Blood cancers', 66: 'Autoimmune diseases', 70: 'Solid tumors'}
    out = []
    cur = None
    for s in order:
        n0 = int(s['id'][2:5]) if re.match(r'ed\d{3}$', s['id']) else 0
        if n0 in PAIN: cur = PAIN[n0]
        if n0 > 73 or n0 < 62: cur = None
        s2 = walk(s)
        if cur and s2.get('subtitle'): s2['subtitle'] = cur
        if cur and isinstance(s2.get('t'), dict):
            for k, v in s2['t'].items():
                for a, b in SEGMENTS:
                    if b.upper() == v.strip().upper() and n0 not in PAIN: s2['t'][k] = cur.upper() if v.isupper() else cur
        s2['tag'] = 'DEMO DATA'
        out.append(s2)
    # the 3 pain-point dividers are diseases, the 4 value dividers are approaches (plans/in-vivo-car-t.md)
    dis = iter([('BLOOD CANCERS', 'Patients with lymphoma, leukemia or myeloma who failed other treatments'),
                ('AUTOIMMUNE DISEASES', 'Patients with lupus, myasthenia or multiple sclerosis whose immune system attacks the body'),
                ('SOLID TUMORS', 'Patients with lung, liver or brain tumors, where CAR-T still struggles to get in')])
    app = iter([('MRNA-LNP CAR-T', 'Lipid particles carry CAR mRNA to T cells, for a short effect that can be repeated'),
                ('LENTIVIRAL CAR-T', 'A virus delivers the CAR gene for good, so one dose can last for years'),
                ('GENE-EDITING CAR-T', 'Editors write the CAR into a precise spot of the T cell genome'),
                ('BEYOND T CELLS', 'The same idea applied to NK cells and macrophages, which reach solid tumors better')])
    for s in out:
        n0 = int(s['id'][2:5]) if re.match(r'ed\d{3}$', s['id']) else 0
        if n0 in (62, 66, 70, 106, 110, 115, 119):
            name, sub = next(dis) if n0 < 100 else next(app)
            ks = list(s['t'])
            s['t'][ks[0]] = name
            if s['t'][ks[1]].strip().upper() != 'PAIN POINTS': s['t'][ks[1]] = sub
    D = {k: v for k, v in E.items() if k != 'slides'}
    D.update(market='In Vivo CAR-T', label='In vivo CAR-T market', slug='invivo-demo', keep_together=['in vivo CAR-T', 'CAR-T'])
    out[0]['big'] = 'In vivo\nCAR-T'
    D['slides'] = out
    OUT.mkdir(parents=True, exist_ok=True)
    if (OUT / 'media').exists(): shutil.rmtree(OUT / 'media')
    shutil.copytree(SRC / 'media', OUT / 'media')
    shutil.copy(ROOT / 'assets/covers/in-vivo-car-t.jpg', OUT / 'media/cover.jpg')     # Pierre's cover (Google Slides, slide nmpcov109)
    (OUT / 'deck.yaml').write_text(yaml.dump(D, allow_unicode=True, sort_keys=False, width=1000))
    print(len(out), 'slides ->', OUT / 'deck.yaml')


if __name__ == '__main__':
    main()
