# AI in drug discovery | 05 Tech and infra (researched by Claude, 20 Nov 2026)

### ed087
```yaml
status: ok
section: Tech and infra
title: What are the tech and infra layers?
page: 1/2
t:
  7: DATA
  10: Biology data from cells, patients and past lab tests that the AI models learn from
  9: MODELS
  11: Models predict how molecules bind to a disease protein and draw new candidates
  21: LAYERS
  12: COMPUTE
  14: GPU computing power trains the models and scores huge sets of molecules
  13: LAB ROBOTS
  15: Automated labs make and test AI designs, then feed the results back
sources:
- claim: AlphaFold Database gives over 200 million predicted protein structures
  url: https://www.ebi.ac.uk/about/news/updates-from-data-resources/new-alphafold-database-entry-pages/
  date: '2025-08-07'
  quote: Developed in collaboration with Google DeepMind, the AlphaFold Database serves over 200 million protein structure predictions
- claim: AlphaFold 3 predicts complexes of proteins with small molecules
  url: https://www.nature.com/articles/s41586-024-07487-w
  date: '2024-05-08'
  quote: predicting the joint structure of complexes including proteins, nucleic acids, small molecules, ions and modified residues.
- claim: AI models work with automated lab experiments
  url: https://ir.iambic.ai/news-releases/news-release-details/iambic-provides-business-updates-and-third-quarter-2026
  date: '2026-11-16'
  quote: integrating proprietary AI with automated, scalable chemistry and biology experimentation
```

### ed088
```yaml
status: ok
section: Tech and infra
title: What are the tech and infra layers?
page: 2/2
t:
  7: SAFETY
  10: Models predict absorption, side effects and toxicity before costly animal and human tests
  9: TARGETS
  11: Target maps link genes and cell changes to a disease to pick what a drug should hit
  21: LAYERS
  12: SOFTWARE
  14: Platforms package the models for chemists, sold as licenses or used in pharma deals
  13: TRIALS
  15: Human trials still decide if an AI-designed drug is safe and actually helps patients
sources:
- claim: FDA plan cites AI-based computational models of toxicity
  url: https://www.fda.gov/news-events/press-announcements/fda-announces-plan-phase-out-animal-testing-requirement-monoclonal-antibodies-and-other-drugs
  date: '2025-04-10'
  quote: including AI-based computational models of toxicity and cell lines and organoid toxicity testing in a laboratory setting
- claim: Insilico uses Pharma.AI from target finding to molecule design
  url: https://insilico.com/news/0x2bab4j81-insilico-medicine-earns-second-consecuti?amp=true
  date: '2026-08-26'
  quote: integrating target identification through PandaOmics, generative chemistry through Chemistry42
- claim: Trials go from Phase 1 to Phase 3
  url: https://www.fda.gov/patients/drug-development-process/step-3-clinical-research
  date: undated
  quote: Clinical trials follow a typical series from early, small-scale, Phase 1 studies to late-stage, large scale, Phase 3 studies.
```

### ed089
```yaml
status: ok
section: Tech and infra
title: Does every layer carry the same weight?
note: We ranked these layers directionally from recent reviews and company disclosures, not from a standardized industry score.
t:
  38: RANKING
  6: DATA
  14: Sets the ceiling of every model, since scarce, biased biology data limit what AI learns
  7: TARGETS
  24: Picking the right disease cause decides most of a drug's value, more than its design
  8: MODELS
  26: Draw and score molecules fast, but their value depends on the data and on lab checks
  9: LAB LOOP
  28: Robotic labs test designs fast and feed results back, so models improve each round
  10: SAFETY
  30: Flags toxic molecules early, but predictions still need lab and human confirmation
  11: COMPUTE
  32: Needed to train and run models, but GPU time is easy to rent today
  12: SOFTWARE
  34: Makes models usable by chemists, yet free open models now limit its pricing power
  13: TRIALS
  36: Prove whether a design helps patients, and no AI layer can skip this costly step
sources:
- claim: Biological data in drug discovery is highly conditional, which complicates AI
  url: https://www.nature.com/articles/s41573-026-01496-2
  date: '2026-08-07'
  quote: The highly conditional nature of so much of the available biological data in drug discovery also complicates the application of AI
- claim: Boltz-2 is open for academic and commercial use
  url: https://www.boltz.com/boltz2
  date: '2025-06-06'
  quote: Boltz-2 is open-sourced under an MIT license. The model, weights, and training pipeline are available for academic and commercial use.
- claim: Lab binding tests are a time and cost bottleneck
  url: https://www.boltz.com/boltz2
  date: '2025-06-06'
  quote: Running these experiments in the lab is a critical time and cost bottleneck for early stage drug discovery.
```

### ed090
```yaml
status: ok
section: Tech and infra
title: Where does 80% of AI in drug discovery value sit?
note: We treated data, target choice and lab loops as the main value drivers because recent reviews and company results keep pointing to them.
t:
  9: '💰 💰 💰 💰 💰 💰 💰 💰 💰

    💰 💰 💰 💰 💰 💰 💰 💰 💰

    💰 💰 💰 💰 💰 💰 💰 💰 💰

    💰 💰 💰 💰 💰 💰 💰 💰 💰

    💰 💰 💰 💰 💰 💰 💰 💰 💰

    💰 💰 💰 💰 💰 💰 💰 💰 💰

    💰 💰 💰 💰 💰 💰 💰 💰 💰

    💰 💰 💰 💰 💰 💰 💰 💰 💰


    💰 💰 💰 💰 💰 💰 💰 💰 💰

    💰 💰 💰 💰 💰 💰 💰 💰 💰'
  8: 'Most value today sits in unique data and in the choice of target, because a model is only as good as the biology it learns from and the disease cause it aims at.


    Lab loops come next: robots that make and test designs, then feed the results back, turn a model into a repeatable engine.


    Winners will own data others lack, run fast lab loops and take their own drugs into human trials.'
sources:
- claim: Clinical impact evidence of AI in drug discovery is so far limited
  url: https://www.nature.com/articles/s41573-026-01496-2
  date: '2026-08-07'
  quote: evidence of their clinically relevant impact is, so far, disappointingly limited.
- claim: Isomorphic Labs added MSD's proprietary data
  url: https://www.isomorphiclabs.com/articles/isomorphic-labs-enters-into-a-research-collaboration-with-msd
  date: '2026-11-19'
  quote: This collaboration brings together Isomorphic Labs’ AI approach to drug discovery with MSD’s rich proprietary data resources and deep discovery experience.
```

### ed091
```yaml
status: ok
section: Tech and infra
title: How has tech and infra evolved over the years?
note: We used dated model releases, lab results and first human trials because they show when each technology became usable.
t:
  6: '2017 - 2020


    Deep learning began to rank targets and draw molecules. In 2019, Insilico designed new drug leads in 21 days, tested in cells and mice'
  7: '2021 - 2023


    The AlphaFold database opened predicted protein shapes to every lab, and an AI-found lung drug reached Phase 2 in 2023'
  8: '2024 - 2025


    AlphaFold 3 predicted how drugs bind proteins, open models like Boltz-2 became free to use, and the FDA drafted rules on AI'
  9: 'TODAY


    Design engines now cover pills and antibodies, robot labs run with AI agents, and two AI-made drugs are in Phase 3 trials'
  10: '?


    Next tools may learn from pharma data they never see, test designs nonstop in robot labs and replace part of animal testing'
sources:
- claim: In 2019 Insilico identified DDR1 inhibitors in 21 days
  url: https://insilico.com/phase1
  date: '2022-02-24'
  quote: In 2019 we reached a significant proof-of-concept milestone where we predicted a molecule for a well-known target called DDR1 in just 21 days
- claim: The 2019 AI-designed lead was studied in mice
  url: https://www.nature.com/articles/s41587-019-0224-x
  date: '2019-09-02'
  quote: One lead candidate was tested and demonstrated favorable pharmacokinetics in mice.
- claim: AlphaFold Protein Database launched in 2021
  url: https://deepmind.google/blog/alphafold-five-years-of-impact/
  date: '2025-11-25'
  quote: In 2021, we launched the AlphaFold Protein Database in partnership with EMBL-EBI
- claim: Insilico dosed its AI-designed lung drug in Phase 2 in June 2023
  url: https://insilico.com/blog/first_phase2
  date: '2023-07-01'
  quote: bringing the first drug discovered and designed by generative AI into Phase II clinical trials with patients.
- claim: AlphaFold 3 predicts complexes with small molecules
  url: https://www.nature.com/articles/s41586-024-07487-w
  date: '2024-05-08'
  quote: predicting the joint structure of complexes including proteins, nucleic acids, small molecules, ions and modified residues.
- claim: Boltz-2 open for commercial use
  url: https://www.boltz.com/boltz2
  date: '2025-06-06'
  quote: Boltz-2 is open-sourced under an MIT license. The model, weights, and training pipeline are available for academic and commercial use.
- claim: FDA first guidance on AI in drug development, January 2025
  url: https://www.fda.gov/news-events/press-announcements/fda-proposes-framework-advance-credibility-ai-models-used-drug-and-biological-product-submissions
  date: '2025-01-06'
  quote: This is the first guidance the agency has issued on the use of AI for the development of drug and biological products.
- claim: Isomorphic Labs design engine covers small molecules and antibodies
  url: https://www.isomorphiclabs.com/articles/isomorphic-labs-enters-into-a-research-collaboration-with-johnson-johnson
  date: '2026-01-20'
  quote: small molecules, antibodies, peptides and molecular glues.
- claim: Xaira AI agents coordinate robotic lab work
  url: https://www.xaira.com/news/x-automate-brings-physical-and-agentic-ai-to-labs
  date: '2026-10-23'
  quote: X-Scientist uses a vision-language model (VLM) to interpret the scene, select operations, and coordinate workflows.
- claim: Rentosertib in Phase 3
  url: https://insilico.com/news/isn1009261-insilico-medicine-doses-first-patient-genesis-ipf-3
  date: '2026-09-10'
  quote: it has dosed the first patient with Rentosertib (known as ISM001-055 / INS018_055) in GENESIS-IPF-3, a Phase III clinical trial
- claim: GB-0895 in two Phase 3 asthma studies
  url: https://generatebiomedicines.com/news-releases/Generate-Biomedicines-Earnings-Release-Q3-2026
  date: '2026-11-12'
  quote: GB-0895 is being evaluated in two Phase 3 severe asthma studies for dosing twice a year
```

### ed092
```yaml
status: ok
section: Tech and infra
title: What were the latest tech and infra developments?
page: 1/2
note: We kept the model releases, rules and lab results that changed what AI drug discovery teams can do, from company releases, journals and the FDA.
t:
  13: '2024'
  14: Xaira launched with more than $1B to build its own AI models and labs to design drugs, one of the largest starts ever
  15: '2024'
  16: AlphaFold 3 was published in Nature, predicting how proteins bind small drug molecules, DNA and RNA in one model
  17: '2025'
  18: The FDA issued its first draft guidance on AI used to support drug submissions, asking sponsors to prove model credibility
  19: '2025'
  20: The FDA set a plan to phase out some animal tests for antibodies, using AI toxicity models and human lab organoids instead
  21: '2025'
  22: Boltz-2 came out free for commercial use, predicting both the shape and the binding strength of a drug on its target
  23: '2025'
  24: Chai-2 designed full-length antibodies against six hard targets, and 3D images confirmed how five of them bind
sources:
- claim: Xaira launched with more than $1B
  url: https://www.bioworld.com/articles/707977-xaira-launches-with-1b-for-ai-drug-development?v=preview
  date: '2024-04-24'
  quote: In one of the biggest startups ever, Xaira Therapeutics has launched with more than $1 billion from investors.
- claim: AlphaFold 3 published in Nature in May 2024
  url: https://www.nature.com/articles/s41586-024-07487-w
  date: '2024-05-08'
  quote: predicting the joint structure of complexes including proteins, nucleic acids, small molecules, ions and modified residues.
- claim: FDA first AI guidance for drug development
  url: https://www.fda.gov/news-events/press-announcements/fda-proposes-framework-advance-credibility-ai-models-used-drug-and-biological-product-submissions
  date: '2025-01-06'
  quote: This is the first guidance the agency has issued on the use of AI for the development of drug and biological products.
- claim: FDA plan to phase out animal testing for antibodies
  url: https://www.fda.gov/news-events/press-announcements/fda-announces-plan-phase-out-animal-testing-requirement-monoclonal-antibodies-and-other-drugs
  date: '2025-04-10'
  quote: including AI-based computational models of toxicity and cell lines and organoid toxicity testing in a laboratory setting
- claim: Boltz-2 open under MIT license
  url: https://www.boltz.com/boltz2
  date: '2025-06-06'
  quote: Boltz-2 is open-sourced under an MIT license. The model, weights, and training pipeline are available for academic and commercial use.
- claim: Chai-2 designed full-length antibodies against six GPCRs
  url: https://www.chaidiscovery.com/news/chai-2-mab
  date: '2025-11-19'
  quote: We challenged Chai-2 to design both mAbs and VHH antibodies binding to a panel of six GPCRs.
- claim: Chai-2 designs checked by cryo-EM
  url: https://www.chaidiscovery.com/news/chai-2-mab
  date: '2025-11-19'
  quote: We used Cryo-EM to examine five designed antibody-antigen complexes.
```

### ed093
```yaml
status: ok
section: Tech and infra
title: What were the latest tech and infra developments?
page: 2/2
note: We used company releases and FDA announcements to capture the most consequential 2026 technology milestones.
t:
  13: '2026'
  14: Isomorphic Labs and Johnson & Johnson agreed to design small molecules, antibodies and peptides with one AI engine
  15: '2026'
  16: Recursion and Genentech found and validated their first brain disease target from an AI map of human nerve cells grown in the lab
  17: '2026'
  18: Insilico dosed the first patient in a 52-week Phase 3 trial of rentosertib, its AI-found and AI-designed lung fibrosis pill
  19: '2026'
  20: The FDA changed its rules so that validated computer and lab models can replace some animal tests for drug safety
  21: '2026'
  22: Xaira showed X-Automate, a robot lab run by AI agents that plan and coordinate experiments with little human help
  23: '2026'
  24: Isomorphic Labs signed with MSD to train its drug design engine on MSD's private discovery data, after a $5B round
sources:
- claim: Isomorphic Labs and J&J cross-modality collaboration
  url: https://www.isomorphiclabs.com/articles/isomorphic-labs-enters-into-a-research-collaboration-with-johnson-johnson
  date: '2026-01-20'
  quote: Isomorphic Labs announces a cross-modality, multi-target research collaboration with Johnson & Johnson.
- claim: Recursion and Genentech validated a neuroscience target
  url: https://recursion.com/news/unlocking-the-first-neuroscience-target-for-the-recursion-and-genentech-collaboration
  date: '2026-08-05'
  quote: A joint team from Recursion and Genentech has identified and validated its first target from an AI-driven, neuroscience-specific map of biology.
- claim: Rentosertib Phase 3 first patient dosed
  url: https://insilico.com/news/isn1009261-insilico-medicine-doses-first-patient-genesis-ipf-3
  date: '2026-09-10'
  quote: today announced that it has dosed the first patient with Rentosertib
- claim: FDA rule removes animal-only language
  url: https://www.fda.gov/news-events/press-announcements/fda-updates-regulations-advance-innovative-alternatives-animal-testing
  date: '2026-09-21'
  quote: The rule removes language that could suggest that animal testing is the only acceptable way to generate safety information
- claim: Xaira X-Automate robot lab with AI agents
  url: https://www.xaira.com/news/x-automate-brings-physical-and-agentic-ai-to-labs
  date: '2026-10-23'
  quote: X-Scientist uses a vision-language model (VLM) to interpret the scene, select operations, and coordinate workflows.
- claim: Isomorphic Labs and MSD collaboration with MSD's proprietary data
  url: https://www.isomorphiclabs.com/articles/isomorphic-labs-enters-into-a-research-collaboration-with-msd
  date: '2026-11-19'
  quote: This collaboration brings together Isomorphic Labs’ AI approach to drug discovery with MSD’s rich proprietary data resources and deep discovery experience.
```

### ed094
```yaml
status: ok
section: Tech and infra
title: What are the solvable bottlenecks?
note: We selected bottlenecks named again and again in 2026 reviews and company results as technically addressable but not yet solved.
t:
  39: BOTTLENECK
  38: EXPLANATION
  41: BOTTLENECK
  40: EXPLANATION
  7: 'BIASED

    DATA'
  5: Public biology data cover well-studied targets, so models judge new targets poorly
  24: 'MODEL

    TESTING'
  22: Many models are scored on past data, not on new molecules made in a real lab
  11: 'MISSING

    FAILURES'
  9: Failed experiments are rarely published, so models learn mostly from successes
  28: 'TOXICITY

    CALLS'
  26: Safety models still miss liver and heart risks that show up later in people
  15: 'LAB

    SPEED'
  13: Making and testing each design still takes weeks, which slows every model update
  32: 'HARD

    TARGETS'
  30: Some disease proteins move or lack pockets, so even good models struggle
  19: 'DATA

    SHARING'
  17: Pharma data sit in separate companies, so no model learns from the full industry record
  36: 'HUMAN

    PROOF'
  34: Few AI-made drugs have finished late trials, so their real success rate is unknown
sources:
- claim: Very often no prospective validations are performed in publications
  url: https://www.nature.com/articles/s41573-026-01496-2
  date: '2026-08-07'
  quote: In publications, very often no prospective validations are performed
- claim: Biological data in drug discovery is highly conditional
  url: https://www.nature.com/articles/s41573-026-01496-2
  date: '2026-08-07'
  quote: The highly conditional nature of so much of the available biological data in drug discovery also complicates the application of AI
- claim: Lab binding tests are a time and cost bottleneck
  url: https://www.boltz.com/boltz2
  date: '2025-06-06'
  quote: Running these experiments in the lab is a critical time and cost bottleneck for early stage drug discovery.
- claim: Phase 2a trial of an AI-discovered drug, where safety was a main endpoint
  url: https://www.nature.com/articles/s41591-025-03743-2
  date: '2025-06-03'
  quote: 'A generative AI-discovered TNIK inhibitor for idiopathic pulmonary fibrosis: a randomized phase 2a trial'
- claim: Only five of 129 AI-linked clinical assets entered or completed Phase 3
  url: https://pubmed.ncbi.nlm.nih.gov/42874241/
  date: '2026-10-08'
  quote: only five had entered or completed Phase 3.
```

### ed095
```yaml
status: ok
section: Tech and infra
title: Why can’t we solve them yet?
note: We tied each reason to how biology data and lab work are produced today, rather than assuming a better model alone can fix it.
t:
  39: BOTTLENECK
  38: REASON WHY
  41: BOTTLENECK
  40: REASON WHY
  7: 'BIASED

    DATA'
  5: New targets have little data by definition, and making that data takes years of lab work
  24: 'MODEL

    TESTING'
  22: A real test means making new molecules and measuring them, which is slow and costly
  11: 'MISSING

    FAILURES'
  9: Journals and companies have little reason to share what did not work in the lab
  28: 'TOXICITY

    CALLS'
  26: Side effects come from the whole body over months, which cell tests only partly show
  15: 'LAB

    SPEED'
  13: Chemists still make many molecules by hand, and cell tests need days to run
  32: 'HARD

    TARGETS'
  30: Shapes that change or hide make it hard to predict where a drug can stick
  19: 'DATA

    SHARING'
  17: Each drugmaker guards its data as a key asset, so pooling it needs trust and new tools
  36: 'HUMAN

    PROOF'
  34: Late trials take years and hundreds of patients, so proof arrives slowly
sources:
- claim: Discovery data is highly conditional
  url: https://www.nature.com/articles/s41573-026-01496-2
  date: '2026-08-07'
  quote: The highly conditional nature of so much of the available biological data in drug discovery also complicates the application of AI
- claim: Insilico needed 60 to 200 molecules per program
  url: https://insilico.com/news/xmjsn4l091-insilico-initiates-phase-iii-clinical-tr
  date: '2026-07-07'
  quote: with only 60 to 200 molecules synthesized and tested per program.
- claim: Phase 3 rentosertib study runs over 52 weeks
  url: https://insilico.com/news/isn1009261-insilico-medicine-doses-first-patient-genesis-ipf-3
  date: '2026-09-10'
  quote: systematically evaluate the efficacy and safety of once-daily Rentosertib administered over 52 weeks.
- claim: REC-4881 Phase 3 to enroll about 200 adults
  url: https://ir.recursion.com/news-releases/news-release-details/recursion-announces-alignment-fda-registrational-phase-3-trial
  date: '2026-11-18'
  quote: The trial is expected to enroll approximately 200 adults with FAP following colectomy or proctocolectomy
```

### ed096
```yaml
status: ok
section: Tech and infra
title: When can we realistically expect to solve them?
note: We based these estimates on today's trial calendars, rule changes and lab automation progress. They are directional, not consensus forecasts.
t:
  39: BOTTLENECK
  38: WHY THIS TIMELINE
  41: BOTTLENECK
  40: WHY THIS TIMELINE
  7: 'BIASED

    DATA'
  5: Large cell and patient maps are growing fast, but new targets need years of fresh data
  24: 'MODEL

    TESTING'
  22: Robot labs make real tests cheaper, so most new models can be checked in the lab soon
  42: '2030'
  46: '2028'
  11: 'MISSING

    FAILURES'
  9: Robot labs record every failed test, but it takes years to build enough of that data
  28: 'TOXICITY

    CALLS'
  26: The FDA now accepts validated computer models, but each one needs years of proof
  43: '2029'
  47: '2030'
  15: 'LAB

    SPEED'
  13: Robot labs run day and night already and are spreading to more companies
  32: 'HARD

    TARGETS'
  30: Antibody and protein design models improve fast, but each hard target still needs trials
  44: '2028'
  48: '2031'
  19: 'DATA

    SHARING'
  17: Pharma now trains partners' models on its private data, but wider pooling needs trust
  36: 'HUMAN

    PROOF'
  34: The first Phase 3 results of AI-made drugs come in the next years, but one result is not enough
  45: '2029'
  49: '2030'
sources:
- claim: FDA lets developers use validated nonanimal methods
  url: https://www.fda.gov/news-events/press-announcements/fda-updates-regulations-advance-innovative-alternatives-animal-testing
  date: '2026-09-21'
  quote: Developers may use NAMs to generate safety information when the methods are adequately validated and appropriate for the product and regulatory question.
- claim: Xaira robotic lab with AI agents
  url: https://www.xaira.com/news/x-automate-brings-physical-and-agentic-ai-to-labs
  date: '2026-10-23'
  quote: Our X-Suite connects AI models, scientific agents and experimental capabilities to accelerate that work.
- claim: MSD brings proprietary data to Isomorphic Labs
  url: https://www.isomorphiclabs.com/articles/isomorphic-labs-enters-into-a-research-collaboration-with-msd
  date: '2026-11-19'
  quote: This collaboration brings together Isomorphic Labs’ AI approach to drug discovery with MSD’s rich proprietary data resources and deep discovery experience.
- claim: Rentosertib Phase 3 runs 52 weeks
  url: https://insilico.com/news/isn1009261-insilico-medicine-doses-first-patient-genesis-ipf-3
  date: '2026-09-10'
  quote: systematically evaluate the efficacy and safety of once-daily Rentosertib administered over 52 weeks.
```

### ed097
```yaml
status: ok
section: Tech and infra
title: Which bold bets could reshape AI in drug discovery?
note: We grounded the bets in current directions such as robot labs, AI antibody design, pharma data deals and the FDA's openness to computer safety models.
t:
  9: SELF-DRIVING LABS
  12: FEWER ANIMAL TESTS
  15: DESIGNED ANTIBODIES
  18: POOLED PHARMA DATA
  33: 'NEAR-TERM HORIZON

    (0-5 YEARS)'
  7: It is a lab where AI picks, makes and tests molecules day and night with little human work
  10: It is validated computer and organoid safety tests that replace part of animal studies before trials
  13: It is antibodies designed by AI from scratch on a computer, with no animal immunization needed
  16: It is models trained on many drugmakers' private data without anyone handing over raw files
  21: VIRTUAL CELLS
  24: HIGHER SUCCESS RATES
  27: UNDRUGGABLE TARGETS
  30: CANDIDATE IN MONTHS
  34: 'LONG-TERM HORIZON

    (5-10 YEARS)'
  19: It is a model of a human cell that predicts how a drug changes it before any lab test
  22: It is AI-chosen targets and drugs that fail far less often in Phase 2 trials than drugs do today
  25: It is drugs designed for disease proteins that no medicine can reach today
  28: It is a drug candidate picked in a few months, against four to five years in usual discovery
sources:
- claim: Xaira robot lab with AI agents
  url: https://www.xaira.com/news/x-automate-brings-physical-and-agentic-ai-to-labs
  date: '2026-10-23'
  quote: X-Scientist uses a vision-language model (VLM) to interpret the scene, select operations, and coordinate workflows.
- claim: FDA accepts validated nonanimal methods
  url: https://www.fda.gov/news-events/press-announcements/fda-updates-regulations-advance-innovative-alternatives-animal-testing
  date: '2026-09-21'
  quote: The rule removes language that could suggest that animal testing is the only acceptable way to generate safety information
- claim: Chai-2 designs full-length antibodies
  url: https://www.chaidiscovery.com/news/chai-2-mab
  date: '2025-11-19'
  quote: the model can design full-length, drug-like mAbs, while maintaining the high hit rates we previously reported
- claim: Insilico reached candidates in 12 to 18 months on average
  url: https://insilico.com/news/xmjsn4l091-insilico-initiates-phase-iii-clinical-tr
  date: '2026-07-07'
  quote: Insilico has consistently reached preclinical candidate (PCC) nomination in an average of just 12 to 18 months
```

### ed098
```yaml
status: ok
section: Tech and infra
title: Which companies are working on groundbreaking tech today?
t:
  8: INSILICO
  6: They use one AI suite from target to molecule design, and took a lung drug to Phase 3
  24: CHAI DISCOVERY
  22: They built Chai-2, which designs full-length antibodies from scratch, checked by 3D images
  11: RECURSION
  9: They map how drugs change human cells, using over 1 trillion nerve cells made in their labs
  27: BOLTZ
  25: They release open models that predict drug binding, free for companies to use
  14: XAIRA
  12: They run a robot lab where AI agents plan experiments and coordinate the machines
  30: ENVEDA
  28: They use AI to find drug molecules that already exist in plants, microbes and the body
  17: GENERATE
  15: They design new protein drugs with AI and took an asthma antibody into two Phase 3 trials
  33: IAMBIC
  31: They pair AI with automated chemistry and brought a cancer drug to the clinic in two years
logos:
- name: Insilico Medicine
  domain: insilico.com
- name: Chai Discovery
  domain: chaidiscovery.com
- name: Recursion
  domain: recursion.com
- name: Boltz
  domain: boltz.com
- name: Xaira Therapeutics
  domain: xaira.com
- name: Enveda
  domain: enveda.com
- name: Generate:Biomedicines
  domain: generatebiomedicines.com
- name: Iambic
  domain: iambic.ai
sources:
- claim: Insilico Pharma.AI integrates target identification and generative chemistry
  url: https://insilico.com/news/0x2bab4j81-insilico-medicine-earns-second-consecuti?amp=true
  date: '2026-08-26'
  quote: integrating target identification through PandaOmics, generative chemistry through Chemistry42
- claim: Chai-2 designs full-length antibodies, checked by cryo-EM
  url: https://www.chaidiscovery.com/news/chai-2-mab
  date: '2025-11-19'
  quote: the model can design full-length, drug-like mAbs, while maintaining the high hit rates we previously reported
- claim: Recursion map from over 1 trillion iPSC-derived nerve cells
  url: https://ir.recursion.com/news-releases/news-release-details/recursion-reports-third-quarter-2026-financial-results-and
  date: '2026-11-02'
  quote: from a subset of over 1 trillion internally manufactured iPSC-derived neuronal cells
- claim: Boltz-2 open for commercial use
  url: https://www.boltz.com/boltz2
  date: '2025-06-06'
  quote: Boltz-2 is open-sourced under an MIT license. The model, weights, and training pipeline are available for academic and commercial use.
- claim: Xaira AI agents coordinate robotic lab work
  url: https://www.xaira.com/news/x-automate-brings-physical-and-agentic-ai-to-labs
  date: '2026-10-23'
  quote: X-Scientist uses a vision-language model (VLM) to interpret the scene, select operations, and coordinate workflows.
- claim: Enveda PRISM finds existing natural molecules
  url: https://enveda.com/news/enveda-raises-311-million/
  date: '2026-09-23'
  quote: PRISM identifies molecules that already exist in plants, microbes, and the human body, predicts their structures from mass spectrometry data
- claim: Generate designs therapeutic proteins with AI, GB-0895 in two Phase 3 trials
  url: https://generatebiomedicines.com/news-releases/Generate-Biomedicines-Earnings-Release-Q3-2026
  date: '2026-11-12'
  quote: GB-0895 is being evaluated in two Phase 3 severe asthma studies for dosing twice a year
- claim: Iambic brought IAM1363 to the clinic in about two years
  url: https://ir.iambic.ai/news-releases/news-release-details/iambic-presents-updated-iam1363-clinical-data-esmo-2026-showing
  date: '2026-10-26'
  quote: IAM1363, now in a Phase 1/1b study, was designed using Iambic’s molecular superintelligence platform and brought to clinical development in approximately two years
```

### iv_pipeline
```yaml
status: ok
section: Tech and infra
title: Which AI-designed drugs are being tested in people today?
note: We list eight AI-found or AI-designed drugs in human trials, from company releases. Many more early programs exist outside this layout.
t:
  38: PH 3
  34: Rentosertib, a pill for lung fibrosis found and designed by AI
  37: INSILICO · ISM001-055
  27: PH 3
  26: GENERATE · GB-0895
  24: AI-engineered antibody given twice a year for severe asthma
  23: PH 2
  22: RECURSION · REC-4881
  20: Pill that shrank polyps by 47% in a rare inherited colon disease
  19: PH 1/2
  18: IAMBIC · IAM1363
  16: Pill for HER2 cancers, with responses in 19 of 53 patients
  15: PH 1/2
  12: Antibody designed with AI to treat pattern hair loss
  14: ABSCI · ABS-201
  11: PH 1B
  10: ENVEDA · ENV-294
  8: Pill from a natural molecule for eczema, 68% less skin disease
  7: PH 1
  6: RECURSION · REC-1245
  4: Cancer drug that gave 3 early partial responses in patients
  3: PH 1
  2: BIGHAT · BHB810
  0: AI-designed antibody carrying a drug to stomach cancer cells
sources:
- claim: Rentosertib Phase 3, AI-discovered TNIK inhibitor for IPF
  url: https://insilico.com/news/isn1009261-insilico-medicine-doses-first-patient-genesis-ipf-3
  date: '2026-09-10'
  quote: it has dosed the first patient with Rentosertib (known as ISM001-055 / INS018_055) in GENESIS-IPF-3, a Phase III clinical trial
- claim: GB-0895 in two Phase 3 severe asthma studies
  url: https://generatebiomedicines.com/news-releases/Generate-Biomedicines-Earnings-Release-Q3-2026
  date: '2026-11-12'
  quote: GB-0895 is being evaluated in two Phase 3 severe asthma studies for dosing twice a year
- claim: REC-4881 Phase 2 median 47% polyp burden reduction
  url: https://ir.recursion.com/news-releases/news-release-details/recursion-announces-alignment-fda-registrational-phase-3-trial
  date: '2026-11-18'
  quote: patients had a 47% median reduction in total polyp burden after 12 weeks of treatment
- claim: IAM1363 partial responses in 19 of 53 patients, Phase 1/2
  url: https://ir.iambic.ai/news-releases/news-release-details/iambic-presents-updated-iam1363-clinical-data-esmo-2026-showing
  date: '2026-10-26'
  quote: 'Systemic activity: Best overall response by RECIST v1.1 was partial response (PR) in 36% (19/53)'
- claim: ABS-201 in Phase 1/2a for pattern hair loss
  url: https://investors.absci.com/news-releases/news-release-details/absci-reports-business-updates-and-third-quarter-2026-financial
  date: '2026-11-12'
  quote: ABS-201, currently undergoing Phase 1/2a studies, is being developed for pattern hair loss (PHL).
- claim: ENV-294 Phase 1b, 68% mean EASI reduction
  url: https://enveda.com/news/enveda-reports-positive-results-for-env-294-in-a-phase-1b-clinical-trial-of-patients-with-moderate-to-severe-atopic-dermatitis/
  date: '2026-03-31'
  quote: Patients achieved a mean 68% reduction in Eczema Area and Severity Index (EASI)
- claim: REC-1245 three early partial responses
  url: https://ir.recursion.com/news-releases/news-release-details/recursion-reports-third-quarter-2026-financial-results-and
  date: '2026-11-02'
  quote: Three partial responses per RECIST 1.1 criteria (2 confirmed, 1 unconfirmed)
- claim: BHB810 Phase 1, AI-engineered CDH17 antibody-drug conjugate for gastric cancer
  url: https://www.bighatbio.com/news/bighat-biosciences-announces-first-patient-dosed-in-phase-1-trial-evaluating-bhb810
  date: '2026-09-01'
  quote: today announced that the first patient has been dosed in its Phase 1 clinical trial evaluating BHB810
```
