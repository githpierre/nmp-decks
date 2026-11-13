"""Sources chapter of a deck (12 Nov 2026): key sources in the validated 3-column design (edits on the divider_10 slides,
written by hand in decks/<slug>/sources_key.yaml) + the full list of every source in sources.yaml (sources_list slides).
Writes decks/<slug>/sources_slides.yaml (inserted by import_research.py after the last key-source slide).
Usage: python3 tools/build_sources.py <slug>"""
import sys, re, yaml, collections, datetime
from pathlib import Path
slug = sys.argv[1]; D = Path(__file__).resolve().parent.parent / 'decks' / slug
PUB = {'bjnews.com.cn': 'Beijing News', 'ithome.com': 'IT Home', 'chinastarmarket.cn': 'STAR Market Daily', 'cls.cn': 'Cailian Press', 'chinaventure.com.cn': 'ChinaVenture', '36kr.com': '36Kr', 'jiemian.com': 'Jiemian', 'pedaily.cn': 'PEdaily', 'xinhuanet.com': 'Xinhua', 'mk.co.kr': 'Maeil Business', 'caixinglobal.com': 'Caixin', 'caixin.com': 'Caixin', 'scmp.com': 'SCMP', 'techcrunch.com': 'TechCrunch', 'reuters.com': 'Reuters', 'bloomberg.com': 'Bloomberg', 'theinformation.com': 'The Information', 'therobotreport.com': 'The Robot Report', 'ieee.org': 'IEEE Spectrum', 'yicai.com': 'Yicai', 'sina.com.cn': 'Sina', '163.com': 'NetEase', 'qq.com': 'Tencent News', 'stcn.com': 'Securities Times', 'cnstock.com': 'China Securities Journal', 'eastmoney.com': 'East Money', 'thepaper.cn': 'The Paper', 'latepost.com': 'LatePost', 'nikkei.com': 'Nikkei', 'koreaherald.com': 'Korea Herald', 'businesswire.com': 'Business Wire', 'fda.gov': 'FDA', 'pmc.ncbi.nlm.nih.gov': 'PubMed Central', 'pubmed.ncbi.nlm.nih.gov': 'PubMed', 'nature.com': 'Nature', 'sec.gov': 'SEC filing',
       'fiercebiotech.com': 'Fierce Biotech', 'globenewswire.com': 'GlobeNewswire', 'prnewswire.com': 'PR Newswire', 'businesswire.com': 'Business Wire',
       'ashpublications.org': 'Blood (ASH)', 'nejm.org': 'NEJM', 'grandviewresearch.com': 'Grand View Research', 'precedenceresearch.com': 'Precedence Research',
       'futuremarketinsights.com': 'Future Market Insights', 'meticulousresearch.com': 'Meticulous Research', 'fortunebusinessinsights.com': 'Fortune Business Insights',
       'frontiersin.org': 'Frontiers', 'link.springer.com': 'Springer', 'sciencedirect.com': 'ScienceDirect', 'onlinelibrary.wiley.com': 'Wiley', 'cell.com': 'Cell Press',
       'investor.lilly.com': 'Eli Lilly', 'lilly.gcs-web.com': 'Eli Lilly', 'news.abbvie.com': 'AbbVie', 'investors.gilead.com': 'Gilead', 'astrazeneca.com': 'AstraZeneca',
       'investors.bms.com': 'Bristol Myers Squibb', 'news.bms.com': 'Bristol Myers Squibb', 'statnews.com': 'STAT', 'endpts.com': 'Endpoints News', 'biopharmadive.com': 'BioPharma Dive',
       'clinicaltrials.gov': 'ClinicalTrials.gov', 'jnj.com': 'Johnson & Johnson', 'investor.jnj.com': 'Johnson & Johnson', 'cgtlive.com': 'CGTLive', 'biospace.com': 'BioSpace', 'createmedicines.com': 'CREATE Medicines', 'carismatx.com': 'Carisma', 'capstantx.com': 'Capstan', 'doi.org': 'DOI',
       'bio.org': 'BIO', 'ascopubs.org': 'ASCO', 'abbvieclinicaltrials.com': 'AbbVie', 'umoja-biopharma.com': 'Umoja Biopharma', 'orbitaltx.com': 'Orbital',
       'keloniatx.com': 'Kelonia', 'sana.com': 'Sana', 'ensoma.com': 'Ensoma', 'magicrna.com': 'MagicRNA', 'starnatx.com': 'Starna', 'circio.com': 'Circio',
       'wedbush.com': 'Wedbush', 'businessinsider.com': 'Business Insider', 'reuters.com': 'Reuters', 'nih.gov': 'NIH', 'ema.europa.eu': 'EMA'}
PUB.update({'fiercehealthcare.com': 'Fierce Healthcare', 'mobihealthnews.com': 'MobiHealthNews', 'beckershospitalreview.com': 'Becker’s Hospital Review', 'tech.eu': 'Tech.eu', 'axios.com': 'Axios',
       'eu-startups.com': 'EU-Startups', 'finance.yahoo.com': 'Yahoo Finance', 'streetinsider.com': 'StreetInsider', 'geekwire.com': 'GeekWire', 'siliconangle.com': 'SiliconANGLE',
       'einpresswire.com': 'EIN Presswire', 'accessnewswire.com': 'ACCESS Newswire', 'prweb.com': 'PRWeb', 'finsmes.com': 'FinSMEs', 'calcalistech.com': 'CTech', 'forbes.com': 'Forbes',
       'nasdaq.com': 'Nasdaq', 'techfundingnews.com': 'Tech Funding News', 'vcnewsdaily.com': 'VC News Daily', 'digitalhealth.net': 'Digital Health', 'teleborsa.it': 'Teleborsa', 'ucl.ac.uk': 'UCL',
       'dealroom.co': 'Dealroom', 'cbinsights.com': 'CB Insights', 'linkedin.com': 'LinkedIn', 'endpoints.news': 'Endpoints News', 'endpts.com': 'Endpoints News', 'statnews.com': 'STAT',
       'healthcaredive.com': 'Healthcare Dive', 'modernhealthcare.com': 'Modern Healthcare', 'medcitynews.com': 'MedCity News', 'hitconsultant.net': 'HIT Consultant', 'biospace.com': 'BioSpace',
       'sifted.eu': 'Sifted', 'wamda.com': 'Wamda', 'brutkasten.com': 'Brutkasten', 'indiatimes.com': 'The Economic Times', 'healthcareitnews.com': 'Healthcare IT News', 'webwire.com': 'WebWire',
       'thesaasnews.com': 'The SaaS News', 'forgeglobal.com': 'Forge Global', 'bydrug.pharmcube.com': 'PharmCube', 'zhangtongshe.com': 'Zhangtongshe', 'klasresearch.com': 'KLAS', 'jamanetwork.com': 'JAMA',
       'ama-assn.org': 'AMA', 'fda.gov': 'FDA', 'cms.gov': 'CMS', 'hhs.gov': 'HHS', 'nature.com': 'Nature', 'rockhealth.com': 'Rock Health', 'menlovc.com': 'Menlo Ventures', 'bvp.com': 'Bessemer', 'investegate.eu': 'Investegate', 'parkwalk.vc': 'Parkwalk', 'investegate.co.uk': 'Investegate'})
def site_label(u):
    """main label of the host: blog.newlimit.com -> newlimit, ucl.ac.uk -> ucl (a sub-domain is never a publisher name: « Blog », 13 Nov 2026)"""
    h = re.sub(r'^https?://(www\.)?', '', u).split('/')[0].lower(); p = h.split('.')
    if len(p) >= 3 and p[-2] in ('co', 'com', 'ac', 'org', 'net', 'gov', 'edu') and len(p[-1]) == 2: return p[-3]
    if len(p) >= 3 and p[-2] in ('substack', 'medium', 'notion', 'webflow'): return p[-3]      # a company's page on a blog host: the company, not the host
    return p[-2] if len(p) >= 2 else h
def pub(u):
    h = re.sub(r'^https?://(www\.)?', '', u).split('/')[0]
    if h in PUB: return PUB[h]
    for k, v in PUB.items():
        if h.endswith('.' + k): return v
    b = site_label(u)
    return b.replace('-', ' ').title().replace('Biopharma', 'Biopharma')
def title(u, claim):
    path = re.sub(r'^https?://[^/]+', '', u).split('?')[0].rstrip('/')
    seg = [s for s in path.split('/') if s and not re.fullmatch(r'(default\.aspx|index\.html?|download|node|\d+|news|news-releases?|news-details?|press-releases?|articles?|media|media-centre|reports?|industry-analysis|en)', s, re.I)]
    w = re.sub(r'\.(html?|aspx|pdf)$', '', seg[-1]) if seg else ''
    words = [x for x in re.split(r'[-_]+', w) if x and not re.fullmatch(r'[0-9a-f]{6,}|s?\d{4,}.*', x, re.I)]
    if False:   # 12 Nov: URL slugs read badly (lower case, cut words); the claim the source supports is always used
        t = ' '.join(words); t = t[0].upper() + t[1:]
    else:
        t = re.sub(r'\.$', '', claim.strip())
    t = t[0].upper() + t[1:]
    t = re.sub(r'\bcar t\b', 'CAR-T', t, flags=re.I).replace(' Car ', ' CAR ').replace('Fda ', 'FDA ').replace(' fda ', ' FDA ')
    return t if len(t) <= 62 else t[:60].rsplit(' ', 1)[0] + '…'
S = yaml.safe_load((D / 'sources.yaml').read_text())
U = collections.OrderedDict()
for sid, v in S.items():
    for x in v or []:
        u = x['url'].rstrip('/')
        if u not in U: U[u] = x
key = {s['url'].rstrip('/') for s in yaml.safe_load((D / 'sources_key.yaml').read_text())['rows'] if s.get('url')}
items = []
HOME = [u for u in U if not re.search(r'https?://[^/]+/.+', u)]   # a bare homepage proves nothing: never listed as a source (12 Nov 2026)
if HOME: print('homepage-only sources left out (check the claims they carry):', ', '.join(HOME))
for u, x in U.items():
    if u in HOME: continue
    d = x.get('date'); d = d.strftime('%b %Y') if isinstance(d, (datetime.date,)) else (str(d) if d else '')
    if re.fullmatch(r'\d{4}-\d{2}', d or ''): d = datetime.date(int(d[:4]), int(d[5:]), 1).strftime('%b %Y')
    items.append(dict(t=title(u, x['claim']), pub=pub(u), d=d, url=u, key=u in key))
items.sort(key=lambda i: (i['pub'].lower(), i['t'].lower()))
import math; k = math.ceil(len(items) / 34); PER = math.ceil(len(items) / k); slides = []   # balanced pages
chunks = [items[i:i + PER] for i in range(0, len(items), PER)]
for n, c in enumerate(chunks, 1):
    h = (len(c) + 1) // 2
    slides.append(dict(after=None, slide=dict(id=f'src_all_{n}', type='sources_list', section='Sources', cols=[c[:h], c[h:]])))
prev = 'ed219'
for s in slides: s['after'] = prev; prev = s['slide']['id']
(D / 'sources_slides.yaml').write_text(yaml.safe_dump(slides, allow_unicode=True, sort_keys=False, width=1000))
print(len(items), 'sources,', len(slides), 'list slides')

# key-source slides ed216-ed219 (5 rows each) written into edits.yaml from sources_key.yaml (12 Nov 2026: no more hand copy)
KR = yaml.safe_load((D / 'sources_key.yaml').read_text())['rows']
E = yaml.safe_load((D / 'edits.yaml').read_text()) if (D / 'edits.yaml').exists() else {}
E['ed215'] = {**(E.get('ed215') or {}), 'tag': None}
for i, sid in enumerate(['ed216', 'ed217', 'ed218', 'ed219']):
    rows = KR[5 * i:5 * i + 5]
    if not rows: E[sid] = {'drop': True}; continue
    e = {0: 'SOURCE', 1: 'WHY WE TRUST IT', 2: 'HOW WE USED IT', 'section': 'Sources', 'tag': None, 'links': {}}
    for j, r in enumerate(rows):
        k = [3, 7, 10, 13, 16][j]; e[k] = r['name']; e[k + 1] = r['why']; e[k + 2] = r['how']
        if r.get('url'): e['links'][k] = r['url']
    E[sid] = e
(D / 'edits.yaml').write_text(yaml.dump(E, allow_unicode=True, sort_keys=False, width=1000))
print('key sources ->', len(KR), 'rows in ed216-ed219 (edits.yaml)')
