# In vivo CAR-T market definition research

### ed006
```yaml
status: ok
section: Market definition
title: 'What is the in vivo CAR-T market,\n\n  in simple terms?'
text: In vivo CAR-T is the market for medicines that deliver genetic instructions into a patient so their own immune cells become CAR cells inside the body
note: We use a conversational definition here because it makes the boundary with conventional ex vivo CAR-T easier to understand.
sources:
  - claim: In vivo CAR-T generates engineered CAR immune cells directly inside the patient instead of manufacturing them outside the body.
    url: https://pmc.ncbi.nlm.nih.gov/articles/PMC12857126/
    date: 2026-02-01
    quote: "in vivo CAR-T cell therapies"
  - claim: In vivo generation can bypass ex vivo manufacturing and lymphodepletion.
    url: https://pubmed.ncbi.nlm.nih.gov/41882404/
    date: 2026-04-01
    quote: "can bypass ex vivo manufacturing and lymphodepletion"
```

### ed007p
```yaml
status: ok
section: Market definition
title: 'Who is in in vivo CAR-T,\n\n  and who stays outside?'
caption:
  - Distance to the center reflects how directly a platform creates CAR-engineered immune cells inside the patient, not whether it simply supports cell therapy
  - The companies shown are a representative sample, not an exhaustive list, chosen to make the market boundary easy to see
inside:
  - <logo>
  - <logo>
  - <logo>
  - <logo>
  - <logo>
  - <logo>
  - <logo>
  - <logo>
TL:
  name: Legend Biotech
  text: develops CAR-T, but its established products are manufactured ex vivo; only its newer LVIVO program sits inside this market
TR:
  name: Moderna
  text: leads mRNA-LNP drug delivery, but generic RNA delivery alone is outside unless it is used to generate CAR immune cells in vivo
BL:
  name: AstraZeneca
  text: is a diversified pharma, yet its 2025 EsoBiotec acquisition gives it a direct in vivo CAR platform and clinical program
BR:
  name: Umoja
  text: is centered on VivoVec, a targeted lentiviral platform designed to generate CAR-T cells directly inside patients
logos:
  - Capstan Therapeutics — https://www.capstantx.com
  - Umoja Biopharma — https://www.umoja-biopharma.com
  - Kelonia Therapeutics — https://www.keloniatx.com
  - Interius BioTherapeutics — https://www.interiusbio.com
  - EsoBiotec — https://www.esobiotec.com
  - Orna Therapeutics — https://www.ornatx.com
  - Orbital Therapeutics — https://www.orbitaltx.com
  - CREATE Medicines — https://createmedicines.com
note: We keep companies inside only when in vivo CAR generation is central to the platform or a documented specialist-source exception applies.
sources:
  - claim: Current commercial pipelines include Capstan, EsoBiotec, Interius, Kelonia and other direct in vivo CAR developers.
    url: https://pmc.ncbi.nlm.nih.gov/articles/PMC12857126/
    date: 2026-02-01
    quote: "Commercial pipeline of in vivo CAR-T cell therapies"
  - claim: AstraZeneca completed its acquisition of EsoBiotec in May 2025.
    url: https://www.astrazeneca.com/media-centre/press-releases/2025/acquisition-of-esobiotec-completed.html
    date: 2025-05-20
    quote: "successful completion of the acquisition of EsoBiotec"
  - claim: Umoja's UB-VV111 is designed to generate CD19 CAR T cells in vivo.
    url: https://www.umoja-biopharma.com/news/umoja-biopharma-announces-fda-clearance-of-ind-application-for-ub-vv111-a-cd19-directed-in-situ-car-t-for-hematologic-malignancies/
    date: 2024-07-31
    quote: "generates CD19 CAR T-cells in situ"
```

### ed008
```yaml
status: ok
section: Market definition
title: 'What markets are often\n\n  confused with in vivo CAR-T?'
t:
  7: In vivo CAR-T differs from both because the drug reprograms immune cells inside the patient, rather than shipping finished cells
  10: Ex vivo CAR-T removes immune cells, engineers them outside the body, then reinfuses the manufactured cells into the patient
  11: Gene delivery moves DNA or RNA into cells, while in vivo CAR-T uses that delivery specifically to create CAR immune cells
  12: EX VIVO CAR-T
  13: IN VIVO CAR-T
  14: GENE DELIVERY
note: "We separate the market by where CAR engineering happens: outside the patient for ex vivo CAR-T and inside the patient for in vivo CAR-T."
sources:
  - claim: Interius contrasts in vivo therapy with traditional CAR-T cell harvesting, engineering and reinfusion.
    url: https://investors.gilead.com/news/news-details/2025/Kite-to-Acquire-Interius-BioTherapeutics-to-Advance-In-Vivo-Platform/default.aspx
    date: 2025-08-21
    quote: "Unlike traditional CAR T therapies that require cell harvesting, engineering and reinfusion"
  - claim: In vivo approaches use vectors or nanoparticles to deliver CAR-encoding material directly to immune cells.
    url: https://pmc.ncbi.nlm.nih.gov/articles/PMC12857126/
    date: 2026-02-01
    quote: "delivery platform"
```

### ed009
```yaml
status: ok
section: Market definition
title: 'What markets does in vivo CAR-T\n\n  sit between?'
t:
  8: 'GENE\n\n    DELIVERY'
  9: CELL<br>THERAPY
  10: IMMUNO-ONCOLOGY
  13: In vivo CAR-T sits between three markets because it combines a genetic payload, targeted delivery, and living immune-cell function. Gene therapy supplies the vectors, cell therapy supplies the CAR biology, and immunology supplies the disease targets and immune-reset logic.
note: We use these three adjacent markets because most in vivo CAR programs borrow technology, talent, and regulatory thinking from all three.
sources:
  - claim: In vivo CAR-T combines targeted genetic delivery with CAR immune-cell generation.
    url: https://pubmed.ncbi.nlm.nih.gov/40581818/
    date: 2025-06-27
    quote: "targeted delivery of stably integrating genetic medicines"
  - claim: Orna pairs circular RNA with lipid nanoparticles to generate cell therapies inside the body.
    url: https://investor.lilly.com/news-releases/news-release-details/lilly-acquire-orna-therapeutics-advance-cell-therapies
    date: 2026-02-09
    quote: "engineered circular RNA paired with novel lipid nanoparticles"
```

### ed010
```yaml
status: ok
section: Market definition
title: 'And what if we break it down\n\n  in smaller markets?'
t:
  5: 'TARGETED\n\n    LENTIVIRUS'
  7: It is in the market because lentiviral particles can place durable CAR genes directly into T cells
  8: 'TARGETED\n\n    RNA-LNP'
  10: It is in the market because targeted LNPs deliver temporary CAR mRNA into selected T cells
  11: 'CIRCULAR\n\n    RNA CAR-T'
  13: It is in the market because circular RNA can extend CAR expression without integrating a CAR gene
  14: 'IN VIVO\n\n    GENE EDITING'
  16: It is in the market when editing or integration creates a CAR program directly inside immune cells
  17: 'OTHER CAR\n\n    IMMUNE CELLS'
  19: It is in the market when platforms generate CAR-NK, CAR-myeloid, or other CAR cells in vivo
  21: IN VIVO CAR-T
note: We group the market by the delivery and engineering mechanism because that choice drives persistence, repeat dosing, safety, and manufacturing.
sources:
  - claim: Current clinical programs use both lentiviral vectors and lipid nanoparticles.
    url: https://onlinelibrary.wiley.com/doi/full/10.1002/mco2.71030
    date: 2026-10-01
    quote: "Advancements in in vivo CAR-T clinical trials"
  - claim: Orna uses circular RNA paired with lipid nanoparticles for in vivo CAR-T.
    url: https://investor.lilly.com/news-releases/news-release-details/lilly-acquire-orna-therapeutics-advance-cell-therapies
    date: 2026-02-09
    quote: "engineered circular RNA paired with novel lipid nanoparticles"
  - claim: Interius can generate both CAR T and CAR NK cells in vivo.
    url: https://pubmed.ncbi.nlm.nih.gov/40581818/
    date: 2025-06-27
    quote: "results in both CAR T cells"
```

### ed011
```yaml
status: ok
section: Market definition
title: 'What are some common\n\n  acronyms I should know?'
note: We prioritized acronyms that appear repeatedly in company, clinical-trial, and investor materials rather than very technical vector-engineering terms.
t:
  4: It is the engineered receptor that lets immune cells recognize a target
  6: CAR
  8: 'Chimeric Antigen\n\n    Receptor'
  9: It is the lipid carrier used to deliver RNA payloads into selected cells in vivo
  11: LNP
  12: 'Lipid\n\n    Nanoparticle'
  13: It is an integrating viral delivery system used by several in vivo CAR programs
  15: LVV
  16: 'Lentiviral\n\n    Vector'
  17: It is the chemotherapy step often used before CAR-T to clear immune cells
  19: LD
  20: 'Lympho-\n\n    depletion'
  21: It is the inflammatory immune reaction monitored closely after CAR-T treatment
  23: CRS
  24: 'Cytokine Release\n\n    Syndrome'
  25: It is a deep-response test showing no detectable cancer at the assay threshold
  27: MRD
  28: 'Minimal Residual\n\n    Disease'
sources:
  - claim: CAR means chimeric antigen receptor.
    url: https://pubmed.ncbi.nlm.nih.gov/40581818/
    date: 2025-06-27
    quote: "chimeric antigen receptor"
  - claim: LNP means lipid nanoparticle and is used for RNA delivery.
    url: https://news.abbvie.com/2025-06-30-AbbVie-to-Acquire-Capstan-Therapeutics%2C-Further-Strengthening-Commitment-to-Transforming-Patient-Care-in-Immunology
    date: 2025-06-30
    quote: "targeted lipid nanoparticle"
  - claim: CRS is a key toxicity monitored in early in vivo CAR-T trials.
    url: https://www.nature.com/articles/s41591-026-04244-6
    date: 2026-04-01
    quote: "Cytokine release syndrome occurred in four patients"
  - claim: MRD negativity is reported in KLN-1010 clinical results.
    url: https://ashpublications.org/blood/article/146/Supplement%202/LBA-1/556929
    date: 2025-12-01
    quote: "All patients experienced an MRD-negative response"
```

### ed012
```yaml
status: ok
section: Market definition
title: 'What products and services\n\n  are sold in this market?'
note: We show representative clinical and preclinical drug programs rather than generic vectors or contract manufacturing, which sit outside our market boundary.
t:
  6: Cancer programs
  7: Autoimmune programs
  8: Viral delivery
  9: RNA delivery
  10: UB-VV111
  11: ESO-T01
  12: INT2104
  13: KLN-1010
  14: JY-231
  15: LVIVO-TaVec100
  16: UB-V400/410
  17: KL-1010
  18: CPTX2309
  19: HN2301
  20: JCXH-213
  21: GT801
  22: ORN-252
  23: OTX-201
  24: MT-302
  25: MT-303
  26: VivoVec
  27: ENaBL
  28: iGPS
  29: Interius LVV
  30: tLNP platform
  31: circular RNA
  32: myeloid CAR
  33: CAR-NK programs
  35: Lentiviral drugs that create durable CAR cells in vivo
  37: RNA drugs that create transient CAR expression in vivo
  38: Cancer programs aimed at blood tumors and solid tumors
  39: Immune-reset programs aimed at B-cell autoimmune disease
sources:
  - claim: A 2026 review lists UB-VV111, ESO-T01, INT2104, KLN-1010, CPTX2309 and other clinical in vivo CAR programs.
    url: https://onlinelibrary.wiley.com/doi/full/10.1002/mco2.71030
    date: 2026-10-01
    quote: "Advancements in in vivo CAR-T clinical trials"
  - claim: ORN-252 is a CD19 in vivo CAR-T program for B-cell-driven autoimmune disease.
    url: https://investor.lilly.com/news-releases/news-release-details/lilly-acquire-orna-therapeutics-advance-cell-therapies
    date: 2026-02-09
    quote: "ORN-252"
  - claim: OTX-201 uses circular RNA encoding a CD19 CAR delivered by targeted LNPs.
    url: https://news.bms.com/news/corporate-financial/2025/Bristol-Myers-Squibb-Strengthens-and-Diversifies-Cell-Therapy-Portfolio-with-Acquisition-of-Orbital-Therapeutics/default.aspx
    date: 2025-10-10
    quote: "OTX-201"
  - claim: MT-302 is an mRNA-LNP in vivo CAR therapy for solid tumors.
    url: https://createmedicines.com/news/create-medicines-announces-positive-first-in-human-results-for-mt-302
    date: 2025-11-07
    quote: "mRNA-LNP-encoded TROP2-targeted in vivo CAR therapy"
```

### ed013
```yaml
status: no_data
section: Market definition
title: 'What are the different\n\n  price ranges?'
reason: No in vivo CAR-T product has a public commercial treatment price yet because the field is still in early clinical development.
alternative: A later slide can compare deal values, manufacturing steps, or expected cost drivers instead of unsupported patient prices.
note: We do not infer treatment prices from ex vivo CAR-T list prices because the in vivo products, dosing, and care pathways are materially different.
sources:
  - claim: Current in vivo CAR-T programs are early-stage clinical or preclinical rather than approved commercial products.
    url: https://pmc.ncbi.nlm.nih.gov/articles/PMC13198039/
    date: 2026-06-01
    quote: "Clinical translation remains at a very early stage"
```

### ed014
```yaml
status: ok
section: Market definition
title: 'When and where is value\n\n  created in the market?'
items:
  - e: 🎯
    t: When one IV drug turns a patient’s own T cells into targeted CAR cells
  - e: ⏱️
    t: When treatment avoids weeks of personalized cell manufacturing
  - e: 🧪
    t: When a vector reaches the intended immune cell and limits off-target delivery
  - e: 🔁
    t: When RNA dosing can be repeated to tune CAR exposure over time
  - e: 🧬
    t: When integrating delivery creates longer CAR expression from one treatment
  - e: 🏥
    t: When patients can avoid leukapheresis and complex centralized logistics
  - e: 🛡️
    t: When immune reset is achieved without lymphodepleting chemotherapy
  - e: 🌍
    t: When an off-the-shelf drug can expand access beyond specialist CAR-T centers
note: We define value around simplification, targeting, persistence, repeatability, and access because these are the core problems current developers are trying to solve.
sources:
  - claim: In vivo CAR-T can avoid leukapheresis, ex vivo manufacturing and lymphodepletion.
    url: https://pubmed.ncbi.nlm.nih.gov/41882404/
    date: 2026-04-01
    quote: "without leukapheresis, ex vivo manufacturing or lymphodepleting chemotherapy"
  - claim: Interius describes a single IV infusion without preconditioning chemotherapy or complex cell processing.
    url: https://investors.gilead.com/news/news-details/2025/Kite-to-Acquire-Interius-BioTherapeutics-to-Advance-In-Vivo-Platform/default.aspx
    date: 2025-08-21
    quote: "single intravenous infusion"
```

### ed015
```yaml
status: ok
section: Market definition
title: 'What are some common myths\n\n  about in vivo CAR-T?'
page: 1/2
note: We focused on myths that recur in company, investor, and specialist discussions. The evidence is still early, so these counters describe what has been demonstrated, not what is clinically proven at scale.
t:
  0: In vivo CAR-T is still only a preclinical idea
  7: Multiple Phase 1 programs now treat patients with viral or targeted RNA approaches in cancer and autoimmunity
  9: CAR-T cells cannot be made well inside patients
  10: KLN-1010 produced CAR-positive cells at 22% to 85% of circulating CD3 T cells around day 15 in its first four patients
  12: In vivo CAR-T always needs lymphodepletion
  13: ESO-T01, KLN-1010 and several other programs have generated CAR cells without preparative lymphodepleting chemotherapy
  15: RNA in vivo CAR-T cannot show clinical activity
  16: Early HN2301 autoimmune data showed B-cell depletion and lower disease activity after CD19 CAR mRNA-LNP dosing
sources:
  - claim: Multiple in vivo CAR-T Phase 1 trials are active.
    url: https://onlinelibrary.wiley.com/doi/full/10.1002/mco2.71030
    date: 2026-10-01
    quote: "Phase 1"
  - claim: KLN-1010 generated CAR-positive T cells equal to 22% to 85% of CD3-positive cells on day 15.
    url: https://ascopost.com/issues/february-25-2026-supplement-ash-meeting-highlights-2025/early-findings-from-first-human-study-of-in-vivo-car-t-in-myeloma/
    date: 2026-02-25
    quote: "22% to 85% of CD3-positive T cells"
  - claim: ESO-T01 was administered without lymphodepleting chemotherapy.
    url: https://pubmed.ncbi.nlm.nih.gov/41882404/
    date: 2026-04-01
    quote: "without leukapheresis, ex vivo manufacturing or lymphodepleting chemotherapy"
  - claim: HN2301 produced B-cell depletion and reduced disease activity in early lupus patients.
    url: https://ashpublications.org/bloodict/article-split/2/1/100027/557440/In-vivo-generation-of-CAR-T-cells-biology-delivery
    date: 2026-02-01
    quote: "B-cell depletion was achieved within 7 to 10 days"
```

### ed016
```yaml
status: ok
section: Market definition
title: 'What are some common myths\n\n  about in vivo CAR-T?'
page: 2/2
note: We focused on myths that recur in company, investor, and specialist discussions. The evidence is still early, so these counters describe what has been demonstrated, not what is clinically proven at scale.
t:
  0: Big pharma is waiting for the science to mature
  7: AbbVie paid up to $2.1B for Capstan in 2025, while BMS agreed to pay $1.5B for Orbital later that year
  9: The market is only about blood cancer
  10: Programs now target autoimmune disease and solid tumors, including CPTX2309, ORN-252, HN2301 and MT-302
  12: Only lentiviral vectors are serious
  13: Clinical pipelines include targeted RNA-LNP programs, while circular-RNA assets have drawn major acquisitions
  15: Early responses prove durable cures
  16: ESO-T01 showed responses, but 2026 follow-up found limited persistence and still-scarce clinical data
sources:
  - claim: AbbVie agreed to pay up to $2.1 billion for Capstan.
    url: https://news.abbvie.com/2025-06-30-AbbVie-to-Acquire-Capstan-Therapeutics%2C-Further-Strengthening-Commitment-to-Transforming-Patient-Care-in-Immunology
    date: 2025-06-30
    quote: "pay up to $2.1 billion"
  - claim: BMS agreed to pay $1.5 billion for Orbital.
    url: https://news.bms.com/news/corporate-financial/2025/Bristol-Myers-Squibb-Strengthens-and-Diversifies-Cell-Therapy-Portfolio-with-Acquisition-of-Orbital-Therapeutics/default.aspx
    date: 2025-10-10
    quote: "pay $1.5 billion in cash"
  - claim: MT-302 is being studied as an in vivo CAR therapy in solid tumors.
    url: https://createmedicines.com/news/create-medicines-announces-positive-first-in-human-results-for-mt-302
    date: 2025-11-07
    quote: "in vivo CAR therapy in solid tumors"
  - claim: Long-term ESO-T01 follow-up found limited persistence and scarce clinical data.
    url: https://www.nature.com/articles/s41591-026-04704-z
    date: 2026-10-01
    quote: "clinical data still remain very scarce"
```

### ed017
```yaml
status: ok
section: Market definition
title: 'How mature is in vivo CAR-T\n\n  as a market?'
score: 28
text: The market is real because several programs are in Phase 1 and early patients have generated CAR cells and clinical responses. The score stays low because cohorts are tiny, durability is uncertain, and no in vivo CAR-T product is commercially approved yet.
note:
  - We rate market maturity with a simple internal score based on clinical proof, platform breadth, strategic investment, and commercial readiness.
  - We set 28/100 because human proof exists, but the field remains early Phase 1 with sparse long-term data and no commercial product.
sources:
  - claim: Multiple in vivo CAR-T products are in Phase 1.
    url: https://onlinelibrary.wiley.com/doi/full/10.1002/mco2.71030
    date: 2026-10-01
    quote: "Phase 1"
  - claim: Clinical translation remains very early and evidence is limited to small cohorts.
    url: https://pmc.ncbi.nlm.nih.gov/articles/PMC13198039/
    date: 2026-06-01
    quote: "Clinical translation remains at a very early stage"
  - claim: ESO-T01 follow-up says long-term clinical data remain scarce.
    url: https://www.nature.com/articles/s41591-026-04704-z
    date: 2026-10-01
    quote: "clinical data still remain very scarce"
```

### ed018
```yaml
status: ok
section: Market definition
title: 'How can we categorize companies\n\n  of the in vivo CAR-T market?'
page: 1/3
note: There are many ways to categorize the field, but these four technical approaches capture most current company strategies and make the competitive map easier to read.
t:
  7: 'TARGETED\n\n    LNP-mRNA'
  8: Companies delivering CAR mRNA to immune cells with targeted lipid nanoparticles
  10: 'TARGETED\n\n    LENTIVIRUS'
  11: Companies using engineered lentiviral particles to place CAR genes directly into immune cells
  13: 'GENE EDITING +\n\n    INTEGRATION'
  16: Companies pursuing durable CAR programs through genome integration or direct editing
  18: 'BEYOND\n\n    T CELLS'
  19: Companies programming NK, myeloid, or multiple immune-cell lineages beyond T cells
  25: Here, we categorize by the technical approach used
sources:
  - claim: Commercial pipelines include both LNP-RNA and lentiviral-vector approaches.
    url: https://pmc.ncbi.nlm.nih.gov/articles/PMC12857126/
    date: 2026-02-01
    quote: "Commercial pipeline of in vivo CAR-T cell therapies"
  - claim: Interius can generate CAR T and NK cells with targeted lentiviral delivery.
    url: https://pubmed.ncbi.nlm.nih.gov/40581818/
    date: 2025-06-27
    quote: "CAR T and NK cell generation"
```

### ed019
```yaml
status: ok
section: Market definition
title: 'How can we categorize companies\n\n  of the in vivo CAR-T market?'
page: 2/3
note: We also categorize by disease because oncology and immune reset impose different requirements for dosing, persistence, safety, and acceptable toxicity.
t:
  7: 'BLOOD\n\n    CANCERS'
  8: Companies targeting CD19, CD20, BCMA, or CD22 in blood cancers such as myeloma
  10: 'AUTOIMMUNE\n\n    DISEASE'
  11: Companies using in vivo CAR-T to deplete B cells and reset immunity in lupus
  13: 'SOLID\n\n    TUMORS'
  16: Companies programming CAR immune cells against targets such as TROP2 in solid tumors
  18: 'MULTI-\n\n    DISEASE'
  19: Companies building delivery platforms for several payloads, targets, and disease areas
  25: Here, we categorize by the disease being targeted
sources:
  - claim: Current in vivo CAR-T trials include B-cell malignancies, multiple myeloma and autoimmune diseases.
    url: https://onlinelibrary.wiley.com/doi/full/10.1002/mco2.71030
    date: 2026-10-01
    quote: "B-cell tumors"
  - claim: MT-302 targets TROP2 in advanced solid tumors.
    url: https://createmedicines.com/news/create-medicines-announces-positive-first-in-human-results-for-mt-302
    date: 2025-11-07
    quote: "TROP2-targeted in vivo CAR therapy"
```

### ed020
```yaml
status: ok
section: Market definition
title: 'How can we categorize companies\n\n  of the in vivo CAR-T market?'
page: 3/3
note: A third useful lens is expression strategy because persistent integrated CAR expression and transient RNA expression create very different risk-benefit and redosing profiles.
t:
  7: 'DURABLE\n\n    EXPRESSION'
  8: Companies using integrating vectors to create CAR cells that may persist after one dose
  10: 'TRANSIENT\n\n    EXPRESSION'
  11: Companies using mRNA so CAR expression fades and repeat dosing stays controllable
  13: 'EXTENDED RNA\n\n    EXPRESSION'
  16: Companies using circular RNA to extend expression without integrating a CAR gene
  18: 'HYBRID\n\n    PLATFORMS'
  19: Companies combining delivery or editing tools to tune persistence and cell specificity
  25: Here, we categorize by how long CAR expression lasts
sources:
  - claim: Interius uses an integrating in vivo platform intended for durable CAR generation.
    url: https://investors.gilead.com/news/news-details/2025/Kite-to-Acquire-Interius-BioTherapeutics-to-Advance-In-Vivo-Platform/default.aspx
    date: 2025-08-21
    quote: "integrating in vivo platform"
  - claim: Orna says circular RNA may deliver more durable protein expression than traditional RNA approaches.
    url: https://investor.lilly.com/news-releases/news-release-details/lilly-acquire-orna-therapeutics-advance-cell-therapies
    date: 2026-02-09
    quote: "more durable expression of therapeutic proteins"
```

### ed021
```yaml
status: ok
section: Market definition
title: 'What do top companies\n\n  do in this market?'
note: Other companies could also make the top eight. We chose clinical leaders and strategically important platforms to show the range of approaches shaping the market.
t:
  7: They lead targeted RNA CAR-T with CPTX2309, now in Phase 1 for autoimmune disease
  8: CAPSTAN
  9: They lead BCMA in vivo CAR-T with KLN-1010 and early MRD-negative responses
  10: KELONIA
  11: They run VivoVec, with UB-VV111 in Phase 1 and FDA Fast Track in B-cell cancers
  12: UMOJA
  13: They built INT2104, an integrating vector creating both CAR-T and CAR-NK cells
  14: INTERIUS
  15: They built ENaBL and ESO-T01, one of the first human in vivo CAR-T programs
  16: ESOBIOTEC
  17: They built ORN-252, combining circular RNA and LNPs for autoimmune in vivo CAR-T
  18: ORNA
  19: They built OTX-201, a circular-RNA CD19 CAR program acquired by BMS for $1.5B
  20: ORBITAL
  21: They reported first-in-human MT-302 data for an mRNA-LNP CAR in solid tumors
  22: CREATE
sources:
  - claim: CPTX2309 is in Phase 1 for B-cell-mediated autoimmune diseases.
    url: https://news.abbvie.com/2025-08-19-AbbVie-Completes-Acquisition-of-Capstan-Therapeutics
    date: 2025-08-19
    quote: "currently in Phase 1"
  - claim: KLN-1010 patients achieved early MRD-negative responses.
    url: https://ashpublications.org/blood/article/146/Supplement%202/LBA-1/556929
    date: 2025-12-01
    quote: "All patients experienced an MRD-negative response"
  - claim: UB-VV111 received FDA Fast Track designation in 2025.
    url: https://www.umoja-biopharma.com/news/umoja-biopharma-announces-that-ub-vv111-receives-fda-fast-track-designation-for-relapsed-refractory-b-cell-malignancies/
    date: 2025-09-30
    quote: "FDA has granted Fast Track designation"
  - claim: INT2104 generates both CAR T and CAR NK cells.
    url: https://pubmed.ncbi.nlm.nih.gov/40581818/
    date: 2025-06-27
    quote: "results in both CAR T cells"
  - claim: OTX-201 was included in BMS's $1.5 billion Orbital acquisition.
    url: https://news.bms.com/news/corporate-financial/2025/Bristol-Myers-Squibb-Strengthens-and-Diversifies-Cell-Therapy-Portfolio-with-Acquisition-of-Orbital-Therapeutics/default.aspx
    date: 2025-10-10
    quote: "pay $1.5 billion in cash"
  - claim: MT-302 produced positive first-in-human results in solid tumors.
    url: https://createmedicines.com/news/create-medicines-announces-positive-first-in-human-results-for-mt-302
    date: 2025-11-07
    quote: "Positive First-in-Human Results for MT-302"
```

### ed022
```yaml
status: ok
section: Market definition
title: 'What is rare and that people\n\n  happily pay for in this market?'
note: We looked at clinical proof, acquisition values, specialist reviews, and company disclosures to identify capabilities that appear genuinely scarce and strategically valuable.
t:
  6: '🎯\n\n    Precise targeting, because delivery must reach the intended immune cells'
  7: '🛡️\n\n    Immune shielding, because vectors must survive circulation and keep activity'
  8: '🧬\n\n    Controlled persistence, because too little expression fails and too much can add risk'
  9: '🔁\n\n    Repeat dosing, because nonintegrating RNA programs may need redosing'
  10: '🏥\n\n    No lymphodepletion, because simpler conditioning can widen patient access'
  11: '📈\n\n    Human proof, because early cohorts now separate clinical platforms from concepts'
  12: '🌍\n\n    Scalable supply, because off-the-shelf dosing avoids custom cell manufacturing'
  13: '🧩\n\n    Platform breadth, because buyers value delivery systems that carry many payloads'
sources:
  - claim: AbbVie paid up to $2.1 billion for Capstan and its targeted LNP platform.
    url: https://news.abbvie.com/2025-06-30-AbbVie-to-Acquire-Capstan-Therapeutics%2C-Further-Strengthening-Commitment-to-Transforming-Patient-Care-in-Immunology
    date: 2025-06-30
    quote: "pay up to $2.1 billion"
  - claim: AstraZeneca acquired EsoBiotec and its targeted in vivo delivery platform for up to $1 billion.
    url: https://www.astrazeneca.com/media-centre/press-releases/2025/acquisition-of-esobiotec-completed.html
    date: 2025-05-20
    quote: "total consideration of up to $1bn"
  - claim: The field's major technical challenges include targeting precision and scalable manufacturing.
    url: https://ashpublications.org/bloodict/article-split/2/1/100027/557440/In-vivo-generation-of-CAR-T-cells-biology-delivery
    date: 2026-02-01
    quote: "enhance targeting precision, and achieve scalable manufacturing"
```

### ed023
```yaml
status: ok
section: Market definition
title: 'Which in vivo CAR-T truths\n\n  have flipped?'
note: These are directional market shifts identified from recent clinical reports, company disclosures, and transactions. They are not formal industry rules, but they recur across the evidence.
t:
  6: In vivo CAR-T used to be mostly a preclinical delivery concept
  8: Now several Phase 1 programs have generated CAR cells directly inside human patients
  10: Viral vectors used to dominate serious in vivo CAR discussions
  12: Now targeted mRNA-LNP and circular-RNA programs have reached trials and major acquisitions
  14: CAR-T used to be framed mainly as a cancer treatment
  16: Now autoimmune immune reset is a major focus for Capstan, Orna, Orbital and others
  18: Cell therapy used to require custom manufacturing for each patient
  20: Now in vivo developers aim to turn CAR-T into an off-the-shelf injectable drug
  22: Early value used to sit in preclinical platform claims
  24: Now human data can move strategy fast, with acquisitions following early clinical validation
  26: The market used to be led mainly by small independent biotechs
  28: Now major pharma companies own or partner with leading in vivo CAR platforms
sources:
  - claim: Multiple Phase 1 in vivo CAR-T programs now exist.
    url: https://onlinelibrary.wiley.com/doi/full/10.1002/mco2.71030
    date: 2026-10-01
    quote: "Phase 1"
  - claim: AbbVie acquired Capstan and its targeted LNP platform in 2025.
    url: https://news.abbvie.com/2025-08-19-AbbVie-Completes-Acquisition-of-Capstan-Therapeutics
    date: 2025-08-19
    quote: "completed its acquisition of Capstan Therapeutics"
  - claim: Lilly agreed to acquire Orna and its circular-RNA in vivo CAR-T platform in 2026.
    url: https://investor.lilly.com/news-releases/news-release-details/lilly-acquire-orna-therapeutics-advance-cell-therapies
    date: 2026-02-09
    quote: "Lilly to acquire Orna Therapeutics"
```

### ed024
```yaml
status: ok
section: Market definition
title: 'What has changed\n\n  (very) recently?'
page: 1/2
items:
  - d: SINCE 2024
    t: Umoja won FDA clearance for UB-VV111, a CD19 in situ CAR-T, moving its VivoVec platform from preclinical development into a human Phase 1 program.
  - d: SINCE 2024
    t: The first clinical evidence of lentiviral in vivo CAR-T antitumor activity appeared, showing that direct CAR generation inside patients was no longer only a lab concept.
  - d: SINCE 2025
    t: AstraZeneca bought EsoBiotec for up to $1 billion after early clinical activity from its targeted lentiviral ENaBL platform put in vivo CAR-T on big pharma radar screens.
  - d: SINCE 2025
    t: AbbVie agreed to buy Capstan for up to $2.1 billion, validating targeted RNA-LNP delivery as a strategic route for autoimmune in vivo CAR-T.
  - d: SINCE 2025
    t: Kite agreed to buy Interius for $350 million, adding an integrating platform that creates CAR-T cells directly inside patients with one IV infusion.
  - d: SINCE 2025
    t: BMS agreed to buy Orbital for $1.5 billion, bringing circular RNA and targeted LNP delivery into the center of the in vivo CAR-T race.
note:
  - We kept the milestones that most changed clinical credibility, platform competition, or strategic ownership in the market.
  - There is no official timeline, and another analyst could reasonably choose a few different milestones.
sources:
  - claim: FDA cleared Umoja's UB-VV111 IND in July 2024.
    url: https://www.umoja-biopharma.com/news/umoja-biopharma-announces-fda-clearance-of-ind-application-for-ub-vv111-a-cd19-directed-in-situ-car-t-for-hematologic-malignancies/
    date: 2024-07-31
    quote: "clearance of its Investigational New Drug"
  - claim: AstraZeneca acquired EsoBiotec for up to $1 billion.
    url: https://www.astrazeneca.com/media-centre/press-releases/2025/acquisition-of-esobiotec-completed.html
    date: 2025-05-20
    quote: "total consideration of up to $1bn"
  - claim: AbbVie agreed to pay up to $2.1 billion for Capstan.
    url: https://news.abbvie.com/2025-06-30-AbbVie-to-Acquire-Capstan-Therapeutics%2C-Further-Strengthening-Commitment-to-Transforming-Patient-Care-in-Immunology
    date: 2025-06-30
    quote: "pay up to $2.1 billion"
  - claim: Kite agreed to acquire Interius for $350 million.
    url: https://investors.gilead.com/news/news-details/2025/Kite-to-Acquire-Interius-BioTherapeutics-to-Advance-In-Vivo-Platform/default.aspx
    date: 2025-08-21
    quote: "for $350 million"
  - claim: BMS agreed to pay $1.5 billion for Orbital.
    url: https://news.bms.com/news/corporate-financial/2025/Bristol-Myers-Squibb-Strengthens-and-Diversifies-Cell-Therapy-Portfolio-with-Acquisition-of-Orbital-Therapeutics/default.aspx
    date: 2025-10-10
    quote: "pay $1.5 billion in cash"
```

### ed025
```yaml
status: ok
section: Market definition
title: 'What has changed\n\n  (very) recently?'
page: 2/2
items:
  - d: SINCE 2025
    t: Early KLN-1010 data showed MRD-negative responses in multiple myeloma while generating CAR-T cells in vivo without preparative chemotherapy, strengthening the case for durable viral delivery.
  - d: SINCE 2025
    t: HN2301 early lupus data showed rapid CAR-T generation, B-cell depletion, and lower disease activity, giving targeted RNA-LNP in vivo CAR-T its first autoimmune human proof point.
  - d: SINCE 2025
    t: CREATE Medicines reported first-in-human MT-302 data in solid tumors, extending in vivo CAR engineering beyond conventional T-cell blood-cancer programs.
  - d: SINCE 2026
    t: Lilly agreed to acquire Orna, bringing circular RNA plus LNP delivery and the ORN-252 autoimmune CAR-T program into a major pharmaceutical company.
  - d: SINCE 2026
    t: Lilly also agreed to acquire Kelonia after early KLN-1010 clinical data, adding an integrating lentiviral in vivo CAR platform to its genetic-medicine strategy.
  - d: SINCE 2026
    t: "Longer ESO-T01 follow-up showed both the promise and the limits of the first wave: responses occurred, but persistence was limited and clinical data remain scarce."
note:
  - We kept the milestones that most changed clinical credibility, platform competition, or strategic ownership in the market.
  - There is no official timeline, and another analyst could reasonably choose a few different milestones.
sources:
  - claim: KLN-1010 produced MRD-negative responses without preparative chemotherapy.
    url: https://ashpublications.org/blood/article/146/Supplement%202/LBA-1/556929
    date: 2025-12-01
    quote: "Lymphodepletion was not required"
  - claim: HN2301 produced B-cell depletion in early lupus patients.
    url: https://ashpublications.org/bloodict/article-split/2/1/100027/557440/In-vivo-generation-of-CAR-T-cells-biology-delivery
    date: 2026-02-01
    quote: "B-cell depletion was achieved within 7 to 10 days"
  - claim: CREATE reported positive first-in-human MT-302 results in November 2025.
    url: https://createmedicines.com/news/create-medicines-announces-positive-first-in-human-results-for-mt-302
    date: 2025-11-07
    quote: "Positive First-in-Human Results for MT-302"
  - claim: Lilly agreed to acquire Orna in February 2026.
    url: https://investor.lilly.com/news-releases/news-release-details/lilly-acquire-orna-therapeutics-advance-cell-therapies
    date: 2026-02-09
    quote: "Lilly to acquire Orna Therapeutics"
  - claim: Lilly agreed to acquire Kelonia in April 2026.
    url: https://lilly.gcs-web.com/news-releases/news-release-details/lilly-acquire-kelonia-therapeutics-advance-vivo-car-t-cell
    date: 2026-04-20
    quote: "Lilly to acquire Kelonia Therapeutics"
  - claim: ESO-T01 follow-up reported limited persistence and scarce clinical data.
    url: https://www.nature.com/articles/s41591-026-04704-z
    date: 2026-10-01
    quote: "The limited persistence observed necessitates"
```
