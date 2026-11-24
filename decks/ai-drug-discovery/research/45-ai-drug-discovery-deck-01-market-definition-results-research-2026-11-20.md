# AI in drug discovery, chapter 01 Market definition (evergreen, written by Claude, 20 Nov 2026)

### ed006
```yaml
status: ok
title: What is AI in drug discovery, in simple terms?
text: AI in drug discovery is the market for companies that use AI to find disease targets and design new drug candidates, before the first tests in people
note: We use a conversational definition here because it makes the boundary with AI used later, in clinical trials or in hospitals, easier to understand.
icon_tl: 🧬
```

### ed007p
```yaml
status: no_data
reason: taken from the live product page
```

### ed008
```yaml
status: ok
title: What markets are often confused with AI in drug discovery?
t:
  12: CLINICAL AI
  13: AI DRUG DISCOVERY
  14: CRO SERVICES
  7: AI drug discovery sits before both, because it picks the target and designs the molecule long before any patient takes it
  10: Clinical AI helps run trials and care for patients, finding sites and patients or reading scans, after a drug exists
  11: Contract labs make and test molecules for a fee on request, without their own AI platform choosing what to make
```

### ed009
```yaml
status: ok
title: What markets does AI in drug discovery sit between?
t:
  8: "BIG\nPHARMA"
  9: "AI\nSOFTWARE"
  10: "LAB\nAUTOMATION"
  13: 'AI drug discovery sits between three markets: it sells or develops medicines like pharma, it builds AI models like software firms, and it runs robotic labs that test thousands of molecules a week.'
```

### ed010
```yaml
status: ok
title: And what if we break it down in smaller markets?
t:
  21: AI DRUG DISCOVERY
  5: "TARGET\nDISCOVERY"
  8: "MOLECULE\nDESIGN"
  11: "PROTEIN\nDESIGN"
  14: "SAFETY\nTESTING"
  17: "DRUG\nREPURPOSING"
  7: It is in the market when AI picks which protein or gene a new drug should act on
  10: It is in the market when AI draws and improves new small molecules before they are made
  13: It is in the market when AI designs antibodies or proteins to treat a disease
  16: It is in the market when AI predicts how toxic a molecule will be in people
  19: It is in the market when AI finds a new disease for a drug that already exists
```

### ed011
```yaml
status: ok
title: What are some common acronyms I should know?
note: We prioritized acronyms that appear often in company, investor and regulator materials rather than very technical chemistry terms.
t:
  6: ML
  15: ADMET
  23: MoA
  8: "Machine\nLearning"
  16: "Absorption to\nToxicity"
  24: "Mechanism\nof Action"
  4: It is software that learns patterns from data to predict or design molecules
  13: It sums up how a drug is absorbed, spread, broken down, removed and how toxic it is
  21: It is how a drug changes the disease biology, what a new target must explain
  11: DMTA
  19: SAR
  27: IPF
  12: "Design Make\nTest Analyze"
  20: "Structure\nActivity"
  28: "Pulmonary\nFibrosis"
  9: It is the loop in which chemists design, make, test and study molecules again
  17: It is how small changes to a molecule's shape change how well it works on a target
  25: It is the lung disease of Insilico's rentosertib, the most advanced AI drug today
```

### ed012
```yaml
status: no_data
reason: offers and their names are too varied to group into a reliable price map without fresh research
```

### ed013
```yaml
status: no_data
reason: deal terms and software prices are rarely public, left for the research chapters
```

### ed014
```yaml
status: ok
title: When and where is value created in the market?
items:
- e: 🎯
  t: When AI finds a new disease target that no drug acts on yet, backed by human data
- e: ⏱️
  t: When a drug candidate is chosen in months instead of the usual four to five years
- e: 🧪
  t: When fewer molecules have to be made and tested in the lab to find one that works
- e: 🛡️
  t: When AI flags a toxic molecule before it reaches costly animal and human tests
- e: 🧬
  t: When AI designs an antibody or protein that would be very hard to find by trial and error
- e: 🤝
  t: When a big pharma pays cash upfront to use a platform on its own disease targets
- e: 💊
  t: When an AI-found drug passes phase 2 in people and becomes worth billions to a buyer
- e: 🔁
  t: When each new lab result retrains the models, so the next design round improves
```

### ed015
```yaml
status: ok
title: What are some common myths about AI in drug discovery?
page: 1/2
note: We focused on myths that come back often in investor, scientist and press debates. The counters describe what companies have shown so far in trials, filings and deals.
t:
  9: AI drugs are still only a computer idea
  7: Insilico's rentosertib, with an AI-found target and an AI-made molecule, started a phase 3 trial in July 2026 after a 71-patient phase 2a
  12: AI has already brought new drugs to market
  10: As of October 2026, no drug discovered or designed with AI had been approved by the FDA or any major regulator, so approval is still years away
  15: AI drugs fail in people as often as others
  13: In a 2024 analysis, the first AI-found molecules had an 80 to 90% success rate in phase 1, against 40 to 65% usually for other drugs
  0: Only small startups bet on AI discovery
  16: Lilly, Novartis, Pfizer, Sanofi and Bristol Myers Squibb all signed AI discovery deals with startups in 2025 and 2026, Lilly with $115M up front
sources:
- claim: Rentosertib Phase IIa enrolled 71 patients, Phase III initiated July 2026
  url: https://insilico.com/news/xmjsn4l091-insilico-initiates-phase-iii-clinical-tr
  date: '2026-07-07'
  quote: The GENESIS-IPF trial was a multicenter, double-blind, randomized, placebo-controlled Phase IIa study in 71 patients
- claim: Lilly upfront payment of $115M to Insilico
  url: https://insilico.com/news/uiy12zcjg1-insilico-medicine-announces-global-rampd?amp=true
  date: '2026-03-29'
  quote: Insilico is eligible to receive an $115 million upfront payment
```

### ed016
```yaml
status: ok
title: What are some common myths about AI in drug discovery?
page: 2/2
note: We focused on myths that come back often in investor, scientist and press debates. The counters describe what companies have shown so far in trials, filings and deals.
t:
  9: AI makes most of the drug cost go away
  7: AI mostly speeds up the early years, while trials in people still take most of the time and money of a new drug, often 3 to 8 years
  12: A good AI model is enough to win the race
  10: Free models such as Boltz-2 are open to any company, so the leaders also need their own lab data, robots and drugs to stand out
  15: Big pharma deals bring big cash to AI firms
  13: Most deal values are paid only if drugs hit later goals, and upfront cash was just 2% of total deal value in 2025, McKinsey found
  0: Investors have given up on AI drug discovery
  16: Isomorphic Labs raised $5B in November 2026, six months after a $2.1B round, the largest rounds this market has seen, co-led by Sequoia
sources:
- claim: Upfront cash was 2% of deal value in 2025
  url: https://www.mckinsey.com/industries/life-sciences/our-insights/ai-drug-discovery-focusing-on-what-matters-most/
  date: '2026-09-21'
  quote: Up-front cash payments totaled only $0.60 billion, just 2 percent of deal value, in 2025
- claim: Boltz-2 open for academic and commercial use
  url: https://www.boltz.com/boltz2
  date: '2025-06-06'
  quote: Boltz-2 is open-sourced under an MIT license. The model, weights, and training pipeline are available for academic and commercial use.
- claim: Isomorphic Series C co-led by Greenoaks and Sequoia
  url: https://www.isomorphiclabs.com/articles/isomorphic-labs-announces-series-c-investment-round
  date: '2026-11-17'
  quote: The round was co-led by Greenoaks and Sequoia Capital, alongside Andreessen Horowitz (a16z)
```

### ed017
```yaml
status: ok
title: How mature is AI in drug discovery as a market?
score: 40
text: The market is real because AI-found drugs now reach phase 2 and phase 3, big pharma signs deals every month and leaders are listed. The score stays below the middle because no AI-found drug is approved yet, most revenue still comes from partner fees, and few molecules have finished phase 2.
note:
- We rate market maturity with an internal score of clinical proof, approved products, partner revenue and funding.
- We set 40/100 because trials and deals are proven, but no approval has shown that AI drugs work better.
```

### ed018
```yaml
status: ok
title: How can we categorize companies of the AI in drug discovery market?
page: 1/3
note: We use the six solution groups of our company database, from finding the disease target to testing the safety of a molecule before trials.
t:
  25: Here, we categorize by type of solution
categories:
- label: "TARGET\nDISCOVERY"
  description: Using patient and cell data to find which gene a drug should hit
  e: 🎯
- label: "MOLECULE\nDESIGN"
  description: Drawing and improving new small-molecule drugs before chemists make them
  e: 🧪
- label: "HIT\nFINDING"
  description: Screening billions of molecules to find the first ones that hit a target
  e: 🔍
- label: "PROTEIN\nDESIGN"
  description: Designing antibodies, peptides and proteins that treat a disease
  e: 🧬
- label: "SAFETY\nTESTING"
  description: Predicting toxicity and running robot labs that test molecules early
  e: 🛡️
- label: "DRUG\nREPURPOSING"
  description: Finding new diseases for drugs that already exist or were dropped
  e: 🔁
```

### ed019
```yaml
status: ok
title: How can we categorize companies of the AI in drug discovery market?
page: 2/3
note: We also categorize by buyer because big pharma, smaller biotechs and patients need very different deals, prices and proof.
t:
  25: Here, we categorize by the type of buyer
categories:
- label: "BIG\nPHARMA"
  description: Selling discovery deals to Lilly or Novartis for cash and milestones
  e: 🏢
- label: "MID-SIZE\nBIOTECHS"
  description: Licensing software or discovery work to biotechs with small teams
  e: 🏥
- label: "EARLY-STAGE\nBIOTECHS"
  description: Giving young biotechs cloud access to models to design with few staff
  e: 🚀
- label: "PATIENTS\nIN NEED"
  description: Developing their own drugs for diseases with no good treatment yet
  e: 💊
- label: "ACADEMIC\nLABS"
  description: Offering cheap model access to university labs that later pay for it
  e: 🔬
- label: "BIG\nTECH"
  description: Partnering with Nvidia, Google or OpenAI for computing and joint models
  e: 💻
```

### ed020
```yaml
status: ok
title: How can we categorize companies of the AI in drug discovery market?
page: 3/3
note: A third useful lens is the business model, because selling software, selling discovery work and owning drugs bring in money very differently.
t:
  25: Here, we categorize by business model
categories:
- label: "SOFTWARE\nLICENSES"
  description: Selling yearly licenses or cloud access to models, like Schrödinger
  e: 💻
- label: "PARTNER\nDEALS"
  description: Paid upfront and by milestones to design drugs on a partner's targets
  e: 🤝
- label: "OWN\nPIPELINE"
  description: Keeping their AI-made drugs to test them and sell or license them later
  e: 💊
- label: "HYBRID\nMODELS"
  description: Mixing partner deals that pay the bills with a few drugs of their own
  e: 🔀
- label: "DISCOVERY\nSERVICES"
  description: Selling AI screening or design work for a fee, with no rights to drugs
  e: 🧪
- label: "DATA\nPLATFORMS"
  description: Building large cell or patient datasets that pharma pays to use
  e: 📊
```

### ed021
```yaml
status: ok
title: What do top companies do in this market?
note: Other companies could also make the top eight. We chose the players with the most funding, clinical progress or pharma deals to show the range of the market.
t:
  8: XAIRA
  16: INSILICO
  7: They launched in 2024 with $1B to design antibodies and proteins with AI from day one
  15: They took rentosertib, with an AI-found target and molecule, into a phase 3 trial in 2026
  10: ISOMORPHIC
  18: CHAI
  9: They are the DeepMind spinout behind AlphaFold 3 and raised $7.7B to reach trials
  17: They design antibodies with Chai models used by Lilly and Pfizer, and raised $400M
  12: GENERATE
  20: RECURSION
  11: They took an AI-designed antibody into phase 3 for asthma and listed in 2026
  19: They merged with Exscientia in 2024 and test drugs found by imaging billions of cells
  14: IAMBIC
  22: EIKON
  13: They pair AI with robotic chemistry labs and listed on Nasdaq in October 2026
  21: They track single proteins in living cells and raised $381M in a 2026 IPO
```

### ed022
```yaml
status: ok
title: What is rare and that people happily pay for in this market?
note: We looked at deal terms, funding rounds, clinical results and specialist reviews to find the capabilities that look truly scarce and valuable.
t:
  6: "🧬\nHuman proof, because a drug that works in phase 2 is worth far more than any model"
  7: "📊\nOwn lab data, because public data is used by everyone and gives no edge to any model"
  8: "🎯\nNew targets, because a protein no rival works on can lead to a first-in-class drug"
  9: "🔁\nClosed loops, because fast lab tests of each design make the models learn quicker"
  10: "🧪\nHard targets, because pharma pays most to drug proteins once seen as undruggable"
  11: "🤝\nPharma trust, because repeat deals with big groups prove the time saved"
  12: "💻\nComputing power, because training large models of biology needs thousands of chips"
  13: "🧠\nRare talent, because few teams mix top AI research with drug chemists"
```

### ed023
```yaml
status: ok
title: Which AI in drug discovery truths have flipped?
note: These are market shifts we see in recent trial results, company releases and deals. They are not formal industry rules, but they come back across the evidence.
t:
  6: AI-designed drugs used to be only computer predictions
  8: Now Insilico's rentosertib is in phase 3, and dozens more are in trials
  10: Predicting protein shapes used to take years in the lab
  12: Now AlphaFold won a Nobel Prize and free models do it in hours
  14: AI used to help mostly with small-molecule drugs
  16: Now Chai, Generate and Xaira design antibodies and proteins with AI too
  18: Animal tests used to be required for almost every new drug
  20: Now the FDA plans to phase them out with AI models and lab organoids
  22: AI startups used to raise tens of millions of dollars
  24: Now Isomorphic raised $5B in one round, and Chai $400M in another
  26: Pharma used to treat AI firms mainly as small service providers
  28: Now Lilly, Novartis and Pfizer sign platform deals and build their own AI labs
```

### ed024
```yaml
status: ok
title: What has changed (very) recently?
page: 1/2
items:
- d: SINCE 2024
  t: Google DeepMind and Isomorphic Labs released AlphaFold 3, which predicts how proteins bind to drugs and other molecules, not only protein shapes alone.
- d: SINCE 2024
  t: Xaira Therapeutics launched with $1B of funding to design drugs with AI from day one, one of the largest first rounds ever raised by a biotech.
- d: SINCE 2024
  t: The Nobel Prize in Chemistry went to David Baker for protein design and to Demis Hassabis and John Jumper of Google DeepMind for AlphaFold.
- d: SINCE 2024
  t: Recursion merged with Exscientia to build a larger AI drug discovery group, and then cut several programs and a fifth of its staff in 2025.
- d: SINCE 2025
  t: The FDA announced a plan to phase out animal testing for antibodies and other drugs, using AI models of toxicity and human lab organoids instead.
- d: SINCE 2025
  t: Insilico published phase 2a results of rentosertib in Nature Medicine, the first AI-found drug to show a lung function signal in a randomized trial.
note:
- We kept the milestones that most changed clinical proof, funding or the way pharma works with AI
- firms. There is no official timeline, and another analyst could pick a few different milestones here
```

### ed025
```yaml
status: ok
title: What has changed (very) recently?
page: 2/2
items:
- d: SINCE 2026
  t: Generate:Biomedicines raised $400M in a Nasdaq IPO in February, with an AI-designed antibody already in phase 3 trials for severe asthma.
- d: SINCE 2026
  t: Isomorphic Labs raised $2.1B in May and then $5B in November, the largest private rounds ever raised by an AI drug discovery company.
- d: SINCE 2026
  t: Insilico dosed the first patient in a phase 3 trial of rentosertib for lung fibrosis, the furthest an AI-found drug has gone in people so far.
- d: SINCE 2026
  t: Chai Discovery raised $400M at a $3.8B value after signing deals with Lilly, Pfizer and Novartis to design antibodies with its AI models.
- d: SINCE 2026
  t: Iambic listed on Nasdaq in October with $172.5M of IPO proceeds, joining Generate, Recursion and Schrödinger among AI drug firms on the market.
- d: SINCE 2026
  t: A study at the ASCO cancer meeting counted 117 AI-enabled drugs that had entered human trials, of which only eight had completed phase 2.
note:
- We kept the milestones that most changed clinical proof, funding or the way pharma works with AI
- firms. There is no official timeline, and another analyst could pick a few different milestones here
```
