### ed087
```yaml
status: ok
section: Tech and infra
title: 'What are the tech\n\n  and infra layers?'
page: 1/2
t:
  7: LNPs
  9: VIRUSES
  10: Targeted lipid particles carry CAR RNA into immune cells without genome integration
  11: Retargeted lentiviral vectors enter T cells and can make CAR expression durable
  12: TARGETING
  13: PAYLOADS
  14: Surface binders steer vectors toward T-cell markers such as CD3, CD7, or CD8
  15: CAR RNA or DNA encodes receptors that redirect immune cells to disease targets
  21: LAYERS
note: We grouped the stack from recent reviews of the leading viral and nonviral in vivo CAR delivery approaches.
sources:
  - claim: Leading in vivo CAR platforms include lentiviral vectors and targeted LNPs carrying RNA.
    url: https://pmc.ncbi.nlm.nih.gov/articles/PMC13127696/
    date: 2026-05-01
    quote: "We describe the major delivery platforms under clinical development, with a focus on lentiviral vectors (LVVs) and lipid nanoparticles (LNPs)."
  - claim: T-cell targeting commonly uses CD3, CD5, CD7, or related surface receptors.
    url: https://link.springer.com/article/10.1007/s44466-026-00050-4
    date: 2026-08-31
    quote: "Targeting is achieved either through conjugation of T-cell-specific ligands... recognizing CD3, CD5, CD7, or other surface receptors."
```

### ed088
```yaml
status: ok
section: Tech and infra
title: 'What are the tech\n\n  and infra layers?'
page: 2/2
t:
  7: DOSE
  9: ANALYTICS
  10: Dose, route, and formulation control how many immune cells are engineered in vivo
  11: Assays track vector identity, potency, biodistribution, and CAR kinetics
  12: SCALE
  13: CLINICS
  14: Scalable vector manufacturing must hold potency, purity, and batch consistency
  15: Clinics monitor cytokine release and other acute infusion toxicities
  21: LAYERS
note: We treated dosing, analytical control, manufacturing, and clinical monitoring as infrastructure because each is required for reproducible in vivo engineering.
sources:
  - claim: Robust CMC and quantitative biodistribution are core translational requirements.
    url: https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2026.1841160/full
    date: 2026-08-01
    quote: "We outline a practical roadmap—quantitative biodistribution and potency, cargo-tuned persistence, receptor-aware targeting, robust CMC, and indication-specific risk–benefit."
  - claim: Acute inflammatory toxicity requires clinical monitoring in early in vivo CAR trials.
    url: https://ashpublications.org/bloodict/article-split/2/1/100027/557440/In-vivo-generation-of-CAR-T-cells-biology-delivery
    date: 2026-02-01
    quote: "Acute inflammatory reactions and grade 3 CRS were observed in 3 patients within 2 days after infusion."
```

### ed089
```yaml
status: ok
section: Tech and infra
title: 'Does every layer\n\n  carry the same weight?'
t:
  6: TARGETING
  7: DELIVERY
  8: CARs
  9: ASSAYS
  10: DOSE
  11: CELL ENTRY
  12: SCALE
  13: SAFETY
  14: Determines which immune cells are engineered and limits harmful off-target delivery
  24: Controls whether cargo reaches T cells efficiently and lasts long enough to work
  26: Sets disease target and signaling, but still depends on effective delivery
  28: Makes potency and biodistribution measurable before programs can scale dosing
  30: Shapes expansion and toxicity, but cannot rescue poor cell specificity
  32: Governs uptake after binding, so precise targeting still needs cell entry
  34: Turns a lab vector into consistent batches once the core biology works
  36: Can halt development when cytokine, immune, or genome risks outweigh benefit
  38: RANKING
note: We ranked these layers directionally from recent translational reviews and the first human studies, not from a standardized industry score.
sources:
  - claim: Key barriers include targeting specificity, immunogenicity, persistence, and genomic integration safety.
    url: https://pubmed.ncbi.nlm.nih.gov/42979064/
    date: 2026-11-05
    quote: "This review provides a systematic examination of the critical barriers impeding the advancement of in vivo CAR-T therapy."
  - claim: CMC consistency and off-target biodistribution are major translational constraints.
    url: https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2026.1841160/full
    date: 2026-08-01
    quote: "Key translational challenges include: off-target transduction and murky biodistribution... repeat-dose immunity, CMC consistency, and regulatory fit."
```

### ed090
```yaml
status: ok
section: Tech and infra
title: 'Where does 80% of\n\n  in vivo CAR-T value sit?'
comment: The 80% framing is a directional value-concentration view, not a measured market-share statistic.
t:
  8: 'Most value today sits in targeted delivery and cell entry, because vectors must reach the right immune cells while avoiding liver and other tissues.\n\n    Payload design comes next, since RNA is transient while integrating vectors can add durability but also genome risk.\n\n    Winners will pair precise targeting with controllable persistence, scalable CMC, and safety that supports repeatable dosing.'
  9: '💰 💰 💰 💰 💰 💰 💰 💰 💰\n\n    💰 💰 💰 💰 💰 💰 💰 💰 💰\n\n    💰 💰 💰 💰 💰 💰 💰 💰 💰\n\n    💰 💰 💰 💰 💰 💰 💰 💰 💰\n\n    💰 💰 💰 💰 💰 💰 💰 💰 💰\n\n    💰 💰 💰 💰 💰 💰 💰 💰 💰\n\n    💰 💰 💰 💰 💰 💰 💰 💰 💰\n\n    💰 💰 💰 💰 💰 💰 💰 💰 💰\n\n\n    💰 💰 💰 💰 💰 💰 💰 💰 💰\n\n    💰 💰 💰 💰 💰 💰 💰 💰 💰'
note: We treated delivery specificity and persistence control as the main value bottlenecks because recent reviews repeatedly identify them as the core translational constraints.
sources:
  - claim: Specificity, persistence, immunogenicity, and integration risk are central optimization problems.
    url: https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2026.1927594/full
    date: 2026-09-04
    quote: "Key translational challenges... improve T-cell targeting specificity... reduce vector immunogenicity, enhance CAR expression persistence, mitigate safety concerns associated with... genomic integration."
  - claim: Nonviral systems face liver-skewed exposure and viral systems face integration and repeat-dose immunity tradeoffs.
    url: https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2026.1841160/full
    date: 2026-08-01
    quote: "Key translational challenges include... liver-skewed exposure for non-viral systems, integration risk for durable vectors, repeat-dose immunity."
```

### ed091
```yaml
status: ok
section: Tech and infra
title: 'How has tech and infra\n\n  evolved over the years?'
t:
  6: '2017 - 2020\n\n\n    Academic teams showed that targeted viral particles could program CAR T cells directly in animals, establishing the core in vivo concept'
  7: '2021 - 2023\n\n\n    Startups refined lentiviral, LNP, and fusosome delivery, while MT-302 reached patients as an RNA CAR for myeloid cells'
  8: '2024 - 2025\n\n\n    Interius dosed INT2104, Umoja entered Phase 1, Capstan started CPTX2309, and large pharma began acquiring leading platforms'
  9: 'TODAY\n\n\n    Multiple Phase 1 programs span cancer and autoimmunity, with early human responses reported for ESO-T01, KLN-1010, and HN2301'
  10: '?\n\n\n    Next platforms may combine precise cell targeting, redosable RNA, durable gene placement, dual-antigen CARs, safer integration, and outpatient dosing without bespoke cell manufacturing'
note: We used clinical milestones rather than discovery dates because they show when the enabling technology became usable in people.
sources:
  - claim: MT-302 dosed its first patient in 2023.
    url: https://createmedicines.com/news/myeloid-therapeutics-initiates-patient-dosing-with-mt-302-a-novel-trop2
    date: 2023-09-12
    quote: "Myeloid... has dosed the first patient with MT-302 in a Phase 1 study."
  - claim: INT2104 first patient dosing occurred in 2024.
    url: https://www.globenewswire.com/news-release/2024/10/23/2967445/0/en/Interius-BioTherapeutics-Doses-First-Patient-with-in-vivo-Chimeric-Antigen-Receptor-CAR-Gene-Therapy-in-Phase-1-Clinical-Trial.html
    date: 2024-10-23
    quote: "the first study participant has been dosed in INVISE, its first-in-human Phase 1 clinical trial of INT2104"
  - claim: By 2026 multiple lentiviral and LNP programs were in Phase 1.
    url: https://pmc.ncbi.nlm.nih.gov/articles/PMC12857126/
    date: 2026-02-01
    quote: "Commercial pipeline of in vivo CAR-T cell therapies"
```

### ed092
```yaml
status: ok
section: Tech and infra
title: 'What were the latest tech\n\n  and infra developments?'
page: 1/2
t:
  13: '2023'
  14: MT-302 dosed its first patient, taking an mRNA-LNP CAR that programs myeloid cells into a Phase 1 solid-tumor study
  15: '2024'
  16: Interius dosed INT2104, a targeted lentiviral therapy that generates CD20 CAR-T and CAR-NK cells inside patients
  17: '2024'
  18: Umoja received FDA clearance for UB-VV111, moving its CD19 VivoVec in situ CAR-T platform into a Phase 1 trial
  19: '2025'
  20: Capstan started Phase 1 testing of CPTX2309, a CD8-targeted LNP carrying mRNA for a CD19 CAR in autoimmunity
  21: '2025'
  22: AstraZeneca acquired EsoBiotec for up to $1 billion, adding its targeted ENaBL lentiviral in vivo cell platform
  23: '2025'
  24: Kite agreed to buy Interius for $350 million, adding its integrating single-infusion in vivo CAR platform
note: We prioritized milestones with direct clinical or platform consequences, using company releases and trial records where available.
sources:
  - claim: MT-302 first patient dosing in Phase 1.
    url: https://createmedicines.com/news/myeloid-therapeutics-initiates-patient-dosing-with-mt-302-a-novel-trop2
    date: 2023-09-12
    quote: "Myeloid... has dosed the first patient with MT-302 in a Phase 1 study."
  - claim: INT2104 first patient dosing and CAR-T/CAR-NK generation.
    url: https://www.globenewswire.com/news-release/2024/10/23/2967445/0/en/Interius-BioTherapeutics-Doses-First-Patient-with-in-vivo-Chimeric-Antigen-Receptor-CAR-Gene-Therapy-in-Phase-1-Clinical-Trial.html
    date: 2024-10-23
    quote: "INT2104... designed to generate CAR-T and CAR-NK cells in the patient’s body"
  - claim: UB-VV111 FDA IND clearance.
    url: https://www.umoja-biopharma.com/news/umoja-biopharma-announces-fda-clearance-of-ind-application-for-ub-vv111-a-cd19-directed-in-situ-car-t-for-hematologic-malignancies/
    date: 2024-07-31
    quote: "the clearance of its Investigational New Drug (IND) application... for UB-VV111"
  - claim: CPTX2309 is a targeted LNP anti-CD19 CAR-T therapy in Phase 1.
    url: https://news.abbvie.com/2025-06-30-AbbVie-to-Acquire-Capstan-Therapeutics%2C-Further-Strengthening-Commitment-to-Transforming-Patient-Care-in-Immunology
    date: 2025-06-30
    quote: "CPTX2309... is a targeted lipid nanoparticle (tLNP) that delivers an mRNA encoding an anti-CD19 chimeric antigen receptor"
  - claim: AstraZeneca completed the EsoBiotec acquisition for up to $1 billion.
    url: https://www.astrazeneca.com/media-centre/press-releases/2025/acquisition-of-esobiotec-completed.html
    date: 2025-05-20
    quote: "AstraZeneca has acquired all outstanding equity of EsoBiotec for a total consideration of up to $1bn"
  - claim: Kite agreed to acquire Interius for $350 million.
    url: https://investors.gilead.com/news/news-details/2025/Kite-to-Acquire-Interius-BioTherapeutics-to-Advance-In-Vivo-Platform/default.aspx
    date: 2025-08-21
    quote: "acquire Interius BioTherapeutics... for $350 million"
```

### ed093
```yaml
status: ok
section: Tech and infra
title: 'What were the latest tech\n\n  and infra developments?'
page: 2/2
t:
  13: '2026'
  14: Nature Medicine reported ESO-T01 human data, showing four responses among five treated multiple-myeloma patients
  15: '2026'
  16: Kelonia reported six early KLN-1010 patients all responded and were MRD-negative in marrow at month one
  17: '2026'
  18: Lilly agreed to acquire Orna, adding circular-RNA LNPs and a clinical-ready CD19 in vivo CAR-T for autoimmunity
  19: '2026'
  20: Sana showed SG293 produced CAR-T cells and deep B-cell depletion in primates without lymphodepleting chemotherapy
  21: '2026'
  22: Umoja received FDA clearance for UB-VV400, adding a CD22-directed program to its clinical in vivo CAR-T pipeline
  23: '2026'
  24: Lilly agreed to acquire Kelonia, adding its targeted integrating lentiviral platform and Phase 1 KLN-1010 program
note: We used peer-reviewed clinical reports and company releases to capture the most consequential 2026 technology milestones.
sources:
  - claim: ESO-T01 produced objective responses in four of five treated patients.
    url: https://www.nature.com/articles/s41591-026-04244-6
    date: 2026-04-01
    quote: "four of five patients achieved objective responses, including three stringent complete remissions"
  - claim: All six early KLN-1010 patients achieved a response and MRD negativity at month one.
    url: https://ascopubs.org/doi/10.1200/JCO.2026.44.16_suppl.7509
    date: 2026-05-27
    quote: "All 6 pts achieved minimal residual disease (MRD) negativity... at M1 in the BM."
  - claim: Orna's lead ORN-252 uses circular RNA and LNPs for CD19 in vivo CAR-T.
    url: https://investor.lilly.com/news-releases/news-release-details/lilly-acquire-orna-therapeutics-advance-cell-therapies
    date: 2026-02-09
    quote: "Orna's lead program is ORN-252, a clinical trial-ready, CD19 targeting in vivo... CAR-T therapy"
  - claim: SG293 showed cell-specific delivery and deep B-cell depletion without lymphodepletion in primates.
    url: https://ir.sana.com/news-releases/news-release-details/sana-biotechnology-presents-preclinical-data-vivo-car-t-cell
    date: 2026-05-12
    quote: "achieved cell-specific delivery... and deep B cell depletion in non-human primates... without... lymphodepleting chemotherapy"
  - claim: FDA cleared the UB-VV400 IND in July 2026.
    url: https://www.globenewswire.com/news-release/2026/07/16/3328378/0/en/Umoja-Biopharma-Announces-FDA-Clearance-of-IND-Application-for-UB-VV400-the-Industry-s-First-Known-CD22-Directed-In-Vivo-CAR-T-Cell-Therapy-for-Relapsed-Refractory-B-Cell-Malignanc.html
    date: 2026-07-16
    quote: "FDA recently cleared its Investigational New Drug (IND) application for UB-VV400"
  - claim: Lilly agreed to acquire Kelonia and its iGPS platform.
    url: https://investor.lilly.com/node/54136
    date: 2026-04-20
    quote: "Lilly... and Kelonia Therapeutics... announced a definitive agreement for Lilly to acquire Kelonia."
```

### ed094
```yaml
status: ok
section: Tech and infra
title: 'What are the\n\n  solvable bottlenecks?'
t:
  5: Vectors can still reach the wrong tissues, so the field needs tighter immune-cell targeting
  7: 'CELL\n\n    TARGETING'
  9: Nonviral particles often favor liver uptake instead of the immune cells developers want
  11: 'LIVER\n\n    UPTAKE'
  13: Viral particles can trigger immune responses that reduce usable exposure
  15: 'VIRAL\n\n    IMMUNE'
  17: Short-lived RNA may fade too quickly, while durable vectors raise other safety tradeoffs
  19: 'CAR\n\n    PERSISTENCE'
  22: Integrating vectors can create durable CAR cells but raise genome-safety risks
  24: 'INTEGRATION\n\n    RISK'
  26: Vector products must keep identity, potency, purity, and batch consistency
  28: 'BATCH\n\n    CONSISTENCY'
  30: Solid tumors block immune-cell access and suppress engineered cells after arrival
  32: 'SOLID\n\n    TUMORS'
  34: Neutralizing immunity can limit later doses, especially with viral platforms
  36: 'DOSE\n\n    AGAIN'
  38: EXPLANATION
  39: BOTTLENECK
  40: EXPLANATION
  41: BOTTLENECK
note: We selected bottlenecks repeatedly identified in 2026 delivery reviews and early human studies as technically addressable but not yet broadly solved.
sources:
  - claim: Off-target delivery, liver exposure, integration risk, repeat-dose immunity, and CMC consistency are key constraints.
    url: https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2026.1841160/full
    date: 2026-08-01
    quote: "Key translational challenges include: off-target transduction... liver-skewed exposure... integration risk... repeat-dose immunity, CMC consistency."
  - claim: Poor persistence and vector immunogenicity remain active research problems.
    url: https://pubmed.ncbi.nlm.nih.gov/42979064/
    date: 2026-11-05
    quote: "we discuss the determinants of poor CAR-T cell persistence, including unstable mRNA payloads and exhaustion-associated signaling pathways"
```

### ed095
```yaml
status: ok
section: Tech and infra
title: 'Why can’t we solve\n\n  them yet?'
t:
  5: Cell markers overlap, and binding alone does not ensure selective entry
  7: 'CELL\n\n    TARGETING'
  9: LNP chemistry shapes organ tropism, and shifting exposure from liver is hard
  11: 'LIVER\n\n    UPTAKE'
  13: Patients can recognize vector proteins, making repeat exposure less predictable
  15: 'VIRAL\n\n    IMMUNE'
  17: Transient cargo can stop, while durable integration is harder to reverse or tune
  19: 'CAR\n\n    PERSISTENCE'
  22: Integration is stochastic, so teams must track insertion sites and clonal expansion
  24: 'INTEGRATION\n\n    RISK'
  26: Process changes can alter vector potency, tropism, particle quality, and dose
  28: 'BATCH\n\n    CONSISTENCY'
  30: Tumors combine poor trafficking, antigen diversity, and local immune suppression
  32: 'SOLID\n\n    TUMORS'
  34: Adaptive immunity can neutralize later doses before vectors reach target cells
  36: 'DOSE\n\n    AGAIN'
  38: REASON WHY
  39: BOTTLENECK
  40: REASON WHY
  41: BOTTLENECK
note: We tied each reason to known vector biology rather than assuming a single engineering change can solve the full problem.
sources:
  - claim: Current reviews cite specificity, persistence, immunogenicity, integration, and solid-tumor barriers.
    url: https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2026.1927594/full
    date: 2026-09-04
    quote: "major delivery platforms... and corresponding optimization strategies, including approaches to improve T-cell targeting specificity and delivery controllability"
  - claim: LNP composition can shift tropism and unstable mRNA can limit persistence.
    url: https://pubmed.ncbi.nlm.nih.gov/42979064/
    date: 2026-11-05
    quote: "the composition and physicochemical properties of LNPs shift their tropism from the liver to the spleen"
```

### ed096
```yaml
status: ok
section: Tech and infra
title: 'When can we realistically\n\n  expect to solve them?'
comment: Years are directional estimates based on current clinical maturity, not published forecasts.
t:
  5: Human biodistribution can refine targeting, but broad specificity proof needs trials
  7: 'CELL\n\n    TARGETING'
  9: Better ionizable lipids can redirect exposure, but human tropism data remain limited
  11: 'LIVER\n\n    UPTAKE'
  13: Shielding can reduce immunity, but repeat dosing still needs human proof
  15: 'VIRAL\n\n    IMMUNE'
  17: Cargo can tune duration, but durable control must balance efficacy and reversibility
  19: 'CAR\n\n    PERSISTENCE'
  22: Safer integration designs and long follow-up help, but rare events require years to exclude
  24: 'INTEGRATION\n\n    RISK'
  26: Analytics can standardize batches, but scale-up must preserve potency and tropism
  28: 'BATCH\n\n    CONSISTENCY'
  30: Combination designs may help trafficking, but solid tumors need more than delivery
  32: 'SOLID\n\n    TUMORS'
  34: Redosable particles look feasible, but repeated human exposure must prove safety
  36: 'DOSE\n\n    AGAIN'
  38: WHY THIS TIMELINE
  39: BOTTLENECK
  40: WHY THIS TIMELINE
  41: BOTTLENECK
  42: '2029'
  43: '2029'
  44: '2030'
  45: '2029'
  46: '2032'
  47: '2029'
  48: '2032'
  49: '2030'
note: We base these estimates on the field's current Phase 1 status and known safety follow-up needs; they are directional rather than consensus forecasts.
sources:
  - claim: Multiple in vivo CAR programs were already in Phase 1 by 2026.
    url: https://pmc.ncbi.nlm.nih.gov/articles/PMC12857126/
    date: 2026-02-01
    quote: "Commercial pipeline of in vivo CAR-T cell therapies"
  - claim: Long-term safety data remain scarce.
    url: https://www.nature.com/articles/s41591-026-04704-z
    date: 2026-10-06
    quote: "Data on long-term outcomes of in vivo chimeric antigen receptor T cell (CAR-T) therapy remain scarce."
```

### ed097
```yaml
status: ok
section: Tech and infra
title: 'Which bold bets could\n\n  reshape in vivo CAR-T?'
t:
  7: It is one infusion that resets pathogenic B cells in autoimmunity without cell manufacturing
  9: ONE-SHOT RESET
  10: It is durable in vivo CAR-T given without lymphodepletion or bespoke cell processing
  12: NO-CHEMO CAR-T
  13: It programs T, NK, or myeloid cells in vivo to attack disease in complementary ways
  15: MULTILINEAGE CAR
  16: It is in vivo CAR that works in solid tumors despite trafficking and immune suppression
  18: SOLID-TUMOR CAR
  19: It is redosable RNA delivery that can tune the depth and duration of immune reset
  21: REDOSABLE RNA CAR
  22: It is gene editing inside the body that places a CAR only in the intended immune-cell population
  24: GENE EDITING
  25: It is one in vivo product that attacks two antigens to reduce target escape
  27: DUAL-TARGET CAR
  28: It is a standardized infusion with predictable toxicity that can move into outpatient care
  30: OUTPATIENT CAR-T
  33: 'NEAR-TERM HORIZON\n\n    (0-5 YEARS)'
  34: 'LONG-TERM HORIZON\n\n    (5-10 YEARS)'
note: We grounded the bets in current platform directions such as autoimmune immune reset, multilayer targeting, dual-antigen CARs, and delivery without lymphodepletion.
sources:
  - claim: CPTX2309 is designed for B-cell autoimmune disease without lymphodepleting chemotherapy.
    url: https://news.abbvie.com/2025-08-19-AbbVie-Completes-Acquisition-of-Capstan-Therapeutics
    date: 2025-08-19
    quote: "This can be accomplished without the need for lymphodepleting chemotherapy"
  - claim: Umoja has a dual-target BCMA x GPRC5D in vivo CAR-T program.
    url: https://www.umoja-biopharma.com/violator_item/selected-news/
    date: 2026-04-27
    quote: "Industry’s First Combination BCMA x GPRC5D In Vivo CAR T Cell Therapy"
  - claim: Solid tumors remain a major barrier for in vivo CAR approaches.
    url: https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2026.1927594/full
    date: 2026-09-04
    quote: "overcome the physical, antigenic, and immunosuppressive barriers encountered in solid tumors"
```

### ed098
```yaml
status: ok
section: Tech and infra
title: Which companies are working on groundbreaking tech today?
t:
  6: They target CD8 T cells with CAR mRNA LNPs for autoimmune immune reset
  8: CAPSTAN TX
  9: They use VivoVec lentiviral particles to generate CAR-T cells directly in vivo
  11: UMOJA BIOPH
  12: They use CD7-targeted vectors to generate CAR-T and CAR-NK cells in patients
  14: IBIO
  15: They use iGPS lentiviral particles to place durable CAR programs into T cells in vivo
  17: KELONI
  22: They built immune-shielded ENaBL vectors that generated BCMA CAR-T cells in patients
  24: ESOBI
  25: They pair circular RNA with immunotropic LNPs to build in vivo CAR-T programs
  27: ORNA THER
  28: They develop CD8-targeted fusosomes for in vivo CD19 and BCMA CAR-T
  30: SANA.
  31: They program immune cells in vivo with mRNA-LNP CARs for solid tumors
  33: CREATE TX
note: We selected companies with differentiated delivery systems and current clinical or advanced preclinical programs inside the market definition.
sources:
  - claim: Capstan uses a targeted LNP to deliver anti-CD19 CAR mRNA to CD8 T cells.
    url: https://news.abbvie.com/2025-06-30-AbbVie-to-Acquire-Capstan-Therapeutics%2C-Further-Strengthening-Commitment-to-Transforming-Patient-Care-in-Immunology
    date: 2025-06-30
    quote: "delivers an mRNA encoding an anti-CD19 chimeric antigen receptor (CAR) to CD8-expressing cytotoxic T cells in vivo"
  - claim: Interius INT2104 generates CAR-T and CAR-NK cells in vivo.
    url: https://www.globenewswire.com/news-release/2024/10/23/2967445/0/en/Interius-BioTherapeutics-Doses-First-Patient-with-in-vivo-Chimeric-Antigen-Receptor-CAR-Gene-Therapy-in-Phase-1-Clinical-Trial.html
    date: 2024-10-23
    quote: "generate effector CAR-T and CAR-NK cells in vivo"
  - claim: Kelonia iGPS uses engineered lentiviral particles to enter T cells in the body.
    url: https://investor.lilly.com/node/54136
    date: 2026-04-20
    quote: "specially engineered lentiviral-based particles designed to efficiently and selectively enter T-cells inside the body"
  - claim: Orna pairs circular RNA with novel lipid nanoparticles for in vivo cell engineering.
    url: https://investor.lilly.com/news-releases/news-release-details/lilly-acquire-orna-therapeutics-advance-cell-therapies
    date: 2026-02-09
    quote: "engineered circular RNA paired with novel lipid nanoparticles to allow the patient's own body to generate cell therapies"
  - claim: Sana SG293 is a CD8-targeted fusosome delivering a CD19 CAR program.
    url: https://ir.sana.com/news-releases/news-release-details/sana-biotechnology-reports-third-quarter-2026-financial-results
    date: 2026-11-05
    quote: "SG293 is a CD8-targeted fusosome that delivers the genetic material to make CD19-directed CAR T cells."
  - claim: CREATE reported human in vivo RNA-CAR data in solid tumors.
    url: https://createmedicines.com/news/create-medicines-announces-positive-first-in-human-results-for-mt-302
    date: 2025-11-07
    quote: "Data demonstrates proof-of-mechanism for In Vivo CAR therapy in solid tumors"
```

### iv_pipeline
```yaml
status: ok
section: Tech and infra
title: 'Where are in vivo CAR-T\n\n  programs in the clinic?'
comment: We use the fixed eight-row layout for representative public Phase 1 programs; it is not an exhaustive registry of every global in vivo CAR-cell trial.
t:
  0: CD19 CAR mRNA in targeted LNPs for rheumatoid arthritis and lupus
  2: CAPSTAN · CPTX2309
  3: PH 1
  4: CD20 CAR-T and CAR-NK generated in vivo for relapsed B-cell cancers
  6: INTERIUS · INT2104
  7: PH 1
  8: BCMA CAR-T generated by targeted lentivirus for relapsed multiple myeloma
  10: KELONIA · KLN-1010
  11: PH 1
  12: CD19 in vivo CAR-T for lymphoma and CLL
  14: UMOJA · UB-VV111
  15: PH 1
  16: TROP2 RNA CAR programs myeloid cells for advanced solid tumors
  18: CREATE MED · MT302
  19: PH 1
  20: GPC3 RNA CAR programs myeloid cells for liver cancer
  22: CRTE · MT303
  23: PH 1
  24: CD19 CAR mRNA in LNPs for lupus and RA
  26: MAGIC · HN2301
  27: PH 1
  34: CD19 CAR RNA in vivo for B-cell malignancies
  37: IMMORNA · J213
  38: PH 1
note: We list eight representative Phase 1 programs because the slide has eight fixed rows; additional registered programs exist outside this layout.
sources:
  - claim: CPTX2309 is recruiting in Phase 1 for RA and SLE.
    url: https://www.abbvieclinicaltrials.com/study/CPTX2309-01-01
    date: 2026-11-12
    quote: "Phase 1"
  - claim: INT2104 is a Phase 1 in vivo CAR-T/CAR-NK program.
    url: https://www.globenewswire.com/news-release/2024/10/23/2967445/0/en/Interius-BioTherapeutics-Doses-First-Patient-with-in-vivo-Chimeric-Antigen-Receptor-CAR-Gene-Therapy-in-Phase-1-Clinical-Trial.html
    date: 2024-10-23
    quote: "first-in-human Phase 1 clinical trial of INT2104"
  - claim: KLN-1010 is an active Phase 1 program in multiple myeloma.
    url: https://keloniatx.com/pipeline/
    date: 2026-07-01
    quote: "inMMyCAR is our Phase 1 clinical trial for KLN-1010 and is open and enrolling patients."
  - claim: UB-VV111 remains in an ongoing Phase 1 trial.
    url: https://www.umoja-biopharma.com/news/umoja-biopharma-announces-that-ub-vv111-receives-fda-fast-track-designation-for-relapsed-refractory-b-cell-malignancies/
    date: 2025-09-30
    quote: "An ongoing Phase 1 clinical trial is evaluating the safety and antitumor activity of UB-VV111"
  - claim: MT-302 and MT-303 are Phase 1 in vivo CAR programs for solid tumors.
    url: https://pmc.ncbi.nlm.nih.gov/articles/PMC12857126/
    date: 2026-02-01
    quote: "MT-302... Phase I... MT-303... Phase I"
  - claim: HN2301 and JCKH-213 are Phase 1 LNP-RNA in vivo CAR programs.
    url: https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2026.1927594/full
    date: 2026-09-04
    quote: "NCT06618313... JCKH-213... Phase I... NCT06801119... HN2301... Phase I"
```

### ed099p
```yaml
status: ok
section: Tech and infra
title: 'Which in vivo CAR-T players\n\n  can already do the most today?'
companies:
- name: Umoja Biopharma
- name: Kelonia Therapeutics
- name: Capstan Therapeutics
- name: Interius BioTherapeutics
- name: CREATE Medicines
- name: Sana Biotechnology
features:
- header: Clinical|program
  values:
  - 1
  - 1
  - 1
  - 1
  - 1
  - 0
- header: Cancer|focus
  values:
  - 1
  - 1
  - 0
  - 1
  - 1
  - 1
- header: Autoimmune|focus
  values:
  - 1
  - 1
  - 1
  - 1
  - 1
  - 1
- header: Human|efficacy
  values:
  - 0
  - 1
  - 0
  - 0
  - 1
  - 0
- header: Multi|lineage
  values:
  - 0
  - 0
  - 0
  - 1
  - 1
  - 0
- header: Dual|target
  values:
  - 1
  - 1
  - 0
  - 0
  - 0
  - 0
- header: No-chemo|design
  values:
  - 1
  - 1
  - 1
  - 1
  - 0
  - 1
note:
- We checked current company pipelines, trial records, peer-reviewed reports, and recent corporate releases feature by feature
- A pink mark means the capability is publicly documented, with the supporting sources listed below
sources:
  - claim: Umoja has clinical CD19/CD22 programs, a BCMA x GPRC5D dual-target program, and autoimmune development.
    url: https://www.umoja-biopharma.com/our-pipeline/
    date: 2026-11-12
    quote: "UB-VV500 Multiple Myeloma... Target BCMA x GPRC5D"
  - claim: Kelonia has a Phase 1 BCMA program, an oncology/autoimmune pipeline, and a CD19/BCMA biCAR.
    url: https://keloniatx.com/pipeline/
    date: 2026-07-01
    quote: "CD19/BCMA biCAR"
  - claim: Capstan CPTX2309 is Phase 1 in autoimmunity and designed without lymphodepletion.
    url: https://news.abbvie.com/2025-08-19-AbbVie-Completes-Acquisition-of-Capstan-Therapeutics
    date: 2025-08-19
    quote: "CPTX2309, currently in Phase 1 for the treatment of B cell-mediated autoimmune diseases"
  - claim: Interius generates CAR-T and CAR-NK cells and its platform is designed without preconditioning chemotherapy.
    url: https://investors.gilead.com/news/news-details/2025/Kite-to-Acquire-Interius-BioTherapeutics-to-Advance-In-Vivo-Platform/default.aspx
    date: 2025-08-21
    quote: "delivered via a single intravenous infusion, eliminating the need for preconditioning chemotherapy and complex cell processing"
  - claim: CREATE has human efficacy signals with MT-302 and multi-lineage in vivo CAR development.
    url: https://createmedicines.com/news/create-medicines-announces-positive-first-in-human-results-for-mt-302
    date: 2025-11-07
    quote: "first-in-human results from its Phase 1 MYE Symphony trial"
  - claim: Sana has cancer and autoimmune plans for SG293 and designs it without lymphodepletion.
    url: https://ir.sana.com/news-releases/news-release-details/sana-biotechnology-presents-preclinical-data-vivo-car-t-cell
    date: 2026-05-12
    quote: "deep B cell depletion in non-human primates... without the use of lymphodepleting chemotherapy"
```
