# AI in drug discovery, chapter 06 Value creation (evergreen, written by Claude, 20 Nov 2026)

### ed101
```yaml
status: ok
title: What's commoditized today in the market?
note: We identified elements that are now free, open or widely sold across AI drug discovery. They remain necessary, but the edge is moving to own lab data, new targets and results in people.
t:
  7: PROTEIN SHAPES
  9: OPEN MODELS
  11: PUBLIC DATA
  13: DOCKING
  15: VIRTUAL SCREENS
  17: TOX SCORES
  19: CLOUD COMPUTE
  21: CHEMICAL SPACE
  6: Protein shape prediction, now free for most proteins with AlphaFold
  8: Open design models such as Boltz and OpenFold that anyone can run and adapt
  10: Public data on proteins, genes and molecules that every team trains on
  12: Classic docking software that estimates how a molecule fits a protein pocket
  14: Screening millions of virtual molecules, now a standard step sold by many vendors
  16: Basic toxicity and absorption predictions now built into most chemistry tools
  18: GPU computing rented by the hour, which any startup can now buy from many clouds
  20: Huge libraries of buyable virtual molecules that every company can search
```

### ed102
```yaml
status: ok
title: Why has it become commoditized?
note: We see commoditization where models, data and computing are shared or sold by many players. New value therefore comes from own lab data, new disease biology and drugs that work in people.
t:
  7: PROTEIN SHAPES
  9: OPEN MODELS
  11: PUBLIC DATA
  13: DOCKING
  15: VIRTUAL SCREENS
  17: TOX SCORES
  19: CLOUD COMPUTE
  21: CHEMICAL SPACE
  6: Because AlphaFold and its database made protein shapes free for researchers
  8: Because labs publish model code so others can check and build on their work
  10: Because public databases were built with public money and are open to all
  12: Because docking has been taught and used in drug labs for decades
  14: Because cheap GPUs and open models let any vendor screen billions of molecules
  16: Because the same public toxicity data trains most of these models
  18: Because GPU clouds compete on price and rent chips by the hour
  20: Because chemical suppliers list billions of molecules made on demand
```

### ed103
```yaml
status: ok
title: Where is value created today?
page: 1/2
note: We derived these elements from the open problems of AI drug discovery and from what the best funded companies are building. The strongest value today is in human proof, own data and new targets.
t:
  9: "HUMAN\nPROOF"
  7: Drugs found with AI that show a real effect in phase 2 trials, the step where most drugs fail
  12: "OWN LAB\nDATA"
  10: Large datasets from robotic labs that no rival can download, used to train better models
  17: "NEW\nTARGETS"
  15: Disease targets backed by human genetic or patient data that no drug acts on yet
```

### ed104
```yaml
status: ok
title: Where is value created today?
page: 2/2
note: We derived these elements from recent deals and funding rounds. Value is increasingly created by designing drugs for hard targets, closing the loop with fast labs and owning the molecules.
t:
  9: "HARD\nTARGETS"
  7: AI designs for proteins once seen as undruggable, which pharma pays the most for
  12: "CLOSED\nLOOPS"
  10: Labs where each AI design is made and tested in days, and the result retrains the model
  17: "OWN\nDRUGS"
  15: Keeping the rights to AI-made molecules instead of selling the work for a fee
```

### ed106-s1
```yaml
status: ok
t:
  6: VALUE CREATION
  3: TARGET DISCOVERY
  5: AI that finds which protein or gene a new drug should act on
```

### ed107-s1
```yaml
status: ok
title: Who needs it the most?
note: We focus on five groups where target discovery creates the clearest value today. These are priority use cases, not a full list of clients.
t:
  21: TARGET DISCOVERY
  5: "BIG\nPHARMA"
  8: "BIOTECH\nFOUNDERS"
  11: "RARE DISEASE\nPATIENTS"
  14: "ACADEMIC\nLABS"
  17: "DEAL\nTEAMS"
  7: They are drug groups that need new targets backed by human data, since most drugs fail in phase 2 for lack of effect
  10: They are scientists who start a company around one new target and need proof that it drives the disease in people
  13: They are people with diseases whose cause is poorly known, for whom a first good target is the start of any drug
  16: They are university teams with patient data and biology insight that AI firms can turn into targets worth a drug
  19: They are pharma licensing teams that compare dozens of target offers and want the ones with the strongest evidence
```

### ed108-s1
```yaml
status: ok
title: What does "maximum customer value" look like in practice?
t:
  5: TARGET DISCOVERY
  10: EXCEPTIONAL CUSTOMER EXPERIENCE
  7: The pharma team gets a short list of new targets, each backed by human genetic and patient data, with a clear reason why it drives the disease. Lab tests confirm the top one in weeks, and a drug against it later works in phase 2.
  12: VS
  9: BAD CUSTOMER EXPERIENCE
  6: The team gets a long list of targets found only in mouse or cell data, half of them already known, with no clear reason why they matter. Years later, the drug made against the top target fails in phase 2.
```

### ed109-s1
```yaml
status: ok
title: How does the money flow in this case?
t:
  14: TARGET DISCOVERY
  9: "🧬\nThe firm gathers patient and cell data"
  7: "🤖\nAI ranks thousands of possible targets"
  6: "🔬\nThe lab confirms the best ones"
  8: "🤝\nA pharma licenses one target"
  13: "🔁\nNew data improves the next ranking"
  11: "💊\nA drug against it enters trials"
  10: "💳\nThe pharma pays upfront and milestones"
  12: "📈\nRoyalties come in if the drug sells"
```

### ed106-s2
```yaml
status: ok
t:
  6: VALUE CREATION
  3: MOLECULE DESIGN
  5: AI that draws and improves new small-molecule drugs
```

### ed107-s2
```yaml
status: ok
title: Who needs it the most?
note: We focus on five groups where molecule design creates the clearest value today. These are priority use cases, not a full list of clients.
t:
  21: MOLECULE DESIGN
  5: "MEDICINAL\nCHEMISTS"
  8: "BIG PHARMA\nPROGRAMS"
  11: "MID-SIZE\nBIOTECHS"
  14: "AI-FIRST\nBIOTECHS"
  17: "LUNG FIBROSIS\nPATIENTS"
  7: They are drug chemists who want fewer molecules to make and test before finding one with the right potency and safety
  10: They are pharma programs stuck on a hard target, where years of classic chemistry failed to find a good molecule
  13: They are biotechs with a known target but no large chemistry team, that pay for AI design work to reach a candidate
  16: They are companies like Insilico and Iambic that design their own molecules with AI and take them into trials
  19: They are patients with lung fibrosis, where Insilico's AI-designed rentosertib is now in a phase 3 trial
```

### ed108-s2
```yaml
status: ok
title: What does "maximum customer value" look like in practice?
t:
  5: MOLECULE DESIGN
  10: EXCEPTIONAL CUSTOMER EXPERIENCE
  7: The chemists get a few dozen AI designs that are easy to make, potent on the target and clean on toxicity. The lab makes the best ones in weeks, each result retrains the model, and a candidate is picked in months instead of years.
  12: VS
  9: BAD CUSTOMER EXPERIENCE
  6: The chemists get thousands of designs that look good on screen but cannot be made, or fall apart in the lab. They go back to classic methods, and the AI deal ends with no candidate after two years of fees.
```

### ed109-s2
```yaml
status: ok
title: How does the money flow in this case?
t:
  14: MOLECULE DESIGN
  9: "🤝\nA pharma brings a hard target"
  7: "🤖\nAI designs new molecules for it"
  6: "🧪\nThe lab makes and tests the best"
  8: "🔁\nResults retrain the model each week"
  13: "💊\nThe candidate enters phase 1"
  11: "🎯\nA drug candidate is picked"
  10: "💳\nThe pharma pays fees and milestones"
  12: "📈\nRoyalties come in if the drug sells"
```

### ed106-s3
```yaml
status: ok
t:
  6: VALUE CREATION
  3: HIT FINDING
  5: AI that finds the first molecules that act on a target
```

### ed107-s3
```yaml
status: ok
title: Who needs it the most?
note: We focus on five groups where hit finding creates the clearest value today. These are priority use cases, not a full list of clients.
t:
  21: HIT FINDING
  5: "SCREENING\nTEAMS"
  8: "EARLY-STAGE\nBIOTECHS"
  11: "ACADEMIC\nDRUG LABS"
  14: "BIG PHARMA\nPROGRAMS"
  17: "NATURE DRUG\nHUNTERS"
  7: They are pharma teams that used to test millions of real molecules by robot and now want virtual screens that cost far less
  10: They are young biotechs with a new target and little cash, that need a first set of active molecules in a few months
  13: They are university labs studying a disease protein that need starting molecules to test their idea in cells
  16: They are pharma programs where classic screens found nothing, and that try AI on billions of virtual molecules
  19: They are firms like Enveda and LifeMine that use AI to find drugs in plants and fungi that labs never tested
```

### ed108-s3
```yaml
status: ok
title: What does "maximum customer value" look like in practice?
t:
  5: HIT FINDING
  10: EXCEPTIONAL CUSTOMER EXPERIENCE
  7: The team sends a target and gets back a few hundred molecules ranked by AI out of billions, most of them buyable. A good share of them are active when tested in the lab, and several open new chemical families no rival owns.
  12: VS
  9: BAD CUSTOMER EXPERIENCE
  6: The team gets molecules that look active on screen but do nothing in the lab, or that are already in rivals' patents. It pays for the screen, finds no real hit, and falls back on a costly robot screen.
```

### ed109-s3
```yaml
status: ok
title: How does the money flow in this case?
t:
  14: HIT FINDING
  9: "🎯\nA client brings a target"
  7: "🤖\nAI screens billions of molecules"
  6: "🛒\nThe best ones are bought or made"
  8: "🔬\nThe lab tests which ones are active"
  13: "🔁\nResults retrain the screening model"
  11: "🧪\nChemists improve the best hits"
  10: "💳\nThe client pays per screen or project"
  12: "🤝\nGood hits lead to a bigger deal"
```

### ed106-s4
```yaml
status: ok
t:
  6: VALUE CREATION
  3: PROTEIN DESIGN
  5: AI that designs antibodies and proteins to treat a disease
```

### ed107-s4
```yaml
status: ok
title: Who needs it the most?
note: We focus on five groups where protein design creates the clearest value today. These are priority use cases, not a full list of clients.
t:
  21: PROTEIN DESIGN
  5: "ANTIBODY\nTEAMS"
  8: "BIG PHARMA\nPROGRAMS"
  11: "ASTHMA\nPATIENTS"
  14: "AI-FIRST\nBIOTECHS"
  17: "GENE THERAPY\nTEAMS"
  7: They are pharma antibody groups that want binders designed on a computer instead of months of animal immunization
  10: They are pharma programs that sign deals with Chai, Generate or Absci to design antibodies on hard targets
  13: They are people with severe asthma, for whom Generate's AI-designed antibody is now in phase 3 trials
  16: They are companies like Xaira and Generate that design their own antibodies and take them into trials
  19: They are teams that need new proteins and gene editors designed for treatments, a field Profluent works on
```

### ed108-s4
```yaml
status: ok
title: What does "maximum customer value" look like in practice?
t:
  5: PROTEIN DESIGN
  10: EXCEPTIONAL CUSTOMER EXPERIENCE
  7: The team picks the exact spot on the target it wants to hit, and the AI designs antibodies that bind it tightly on the first round. They are stable, easy to make and safe in tests, and one of them reaches the clinic in record time.
  12: VS
  9: BAD CUSTOMER EXPERIENCE
  6: The AI designs binders that look perfect on screen, but most do not bind in the lab, and the few that do clump or trigger the immune system. The team falls back on animal immunization after a year of work.
```

### ed109-s4
```yaml
status: ok
title: How does the money flow in this case?
t:
  14: PROTEIN DESIGN
  9: "🎯\nA pharma names a target and a spot"
  7: "🤖\nAI designs hundreds of antibodies"
  6: "🧫\nThe lab tests which ones bind"
  8: "🔁\nResults train the next designs"
  13: "💊\nThe antibody enters trials"
  11: "🧪\nThe best one is made at scale"
  10: "💳\nThe pharma pays upfront and milestones"
  12: "📈\nRoyalties come in if the drug sells"
```

### ed106-s5
```yaml
status: ok
t:
  6: VALUE CREATION
  3: SAFETY TESTING
  5: AI and robotic labs that test molecules before any trial
```

### ed107-s5
```yaml
status: ok
title: Who needs it the most?
note: We focus on five groups where safety testing creates the clearest value today. These are priority use cases, not a full list of clients.
t:
  21: SAFETY TESTING
  5: "TOXICOLOGY\nTEAMS"
  8: "MEDICINAL\nCHEMISTS"
  11: "DRUG\nREGULATORS"
  14: "MID-SIZE\nBIOTECHS"
  17: "ANIMAL LAB\nMANAGERS"
  7: They are pharma safety teams that want to spot a toxic molecule before months of costly animal and human tests
  10: They are chemists who want to know early if a molecule will be absorbed, stable and safe, before making it
  13: They are FDA and EMA teams that since 2025 accept more data from AI models and human lab organoids
  16: They are biotechs that cannot afford to drop a candidate late, after paying for years of preclinical work
  19: They are managers of animal test programs under pressure to reduce animal use, as the FDA asked in 2025
```

### ed108-s5
```yaml
status: ok
title: What does "maximum customer value" look like in practice?
t:
  5: SAFETY TESTING
  10: EXCEPTIONAL CUSTOMER EXPERIENCE
  7: Before any molecule is made, the model flags the ones likely to harm the liver or the heart. Robotic labs test the best ones on human cells in days, and the candidate that reaches people has far fewer surprises.
  12: VS
  9: BAD CUSTOMER EXPERIENCE
  6: The model scores a molecule as safe, the team spends a year and millions on it, and the toxicity shows up only in animal tests or in phase 1. The program stops, and the model is trusted less on the next one.
```

### ed109-s5
```yaml
status: ok
title: How does the money flow in this case?
t:
  14: SAFETY TESTING
  9: "🤖\nAI predicts toxicity of each design"
  7: "🧫\nRobotic labs test on human cells"
  6: "📊\nResults rank the safest molecules"
  8: "🛡️\nRisky ones are dropped early"
  13: "🔁\nNew data improves the next predictions"
  11: "🏛️\nRegulators review the safety file"
  10: "💳\nClients pay per test or per year"
  12: "💊\nThe candidate enters phase 1"
```

### ed106-s6
```yaml
status: ok
t:
  6: VALUE CREATION
  3: DRUG REPURPOSING
  5: AI that finds new diseases for drugs that already exist
```

### ed107-s6
```yaml
status: ok
title: Who needs it the most?
note: We focus on five groups where drug repurposing creates the clearest value today. These are priority use cases, not a full list of clients.
t:
  21: DRUG REPURPOSING
  5: "RARE DISEASE\nPATIENTS"
  8: "PHARMA\nOWNERS"
  11: "SMALL\nBIOTECHS"
  14: "PATIENT\nGROUPS"
  17: "SPECIALIST\nDOCTORS"
  7: They are people with rare diseases that no company targets, for whom an existing drug could be the fastest option
  10: They are pharma groups holding drugs dropped for lack of effect, which could work in another disease
  13: They are small firms like Biossil that license abandoned drugs cheaply and test them on a new disease
  16: They are patient groups that fund research and push for trials of old drugs on their disease
  19: They are doctors who see a drug help a few patients and want data to know if it works for many more
```

### ed108-s6
```yaml
status: ok
title: What does "maximum customer value" look like in practice?
t:
  5: DRUG REPURPOSING
  10: EXCEPTIONAL CUSTOMER EXPERIENCE
  7: The AI matches a drug already shown to be safe in people with a new disease, backed by patient data. The team skips years of early work, starts a phase 2 trial quickly, and patients get a treatment years earlier.
  12: VS
  9: BAD CUSTOMER EXPERIENCE
  6: The AI suggests a match based on weak links in old papers. The trial on the new disease shows no effect, the patent on the old drug is too short to pay back the work, and no partner wants the program.
```

### ed109-s6
```yaml
status: ok
title: How does the money flow in this case?
t:
  14: DRUG REPURPOSING
  9: "📚\nAI reads data on thousands of drugs"
  7: "🎯\nIt matches one with a new disease"
  6: "🤝\nThe firm licenses the dropped drug"
  8: "🔬\nLab tests confirm the new effect"
  13: "🔁\nOther diseases are tested next"
  11: "💊\nA phase 2 trial starts quickly"
  10: "💳\nA buyer pays for the new use"
  12: "📈\nSales come from the new disease"
```
