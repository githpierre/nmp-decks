# Synthetic biology, chapter 06 Value creation (evergreen, written by Claude, 26 Nov 2026)

### ed101
```yaml
status: ok
title: What's commoditized today in the market?
note: We identified tools that are now broadly available and used by almost every team. They remain necessary, but value is shifting to strain yield, scale-up, design data and regulatory proof.
t:
  7: DNA PRINTING
  9: DNA READING
  11: CRISPR kits
  13: HOST CELLS
  15: LAB ROBOTS
  17: FOLD MODELS
  19: BULK ENZYMES
  21: SMALL TANKS
  6: Short DNA strands, now ordered online for cents per letter from many suppliers
  8: DNA sequencing to check a design, now cheap and fast in any lab
  10: Standard CRISPR tools for basic gene edits, sold as ready-made kits
  12: Common workhorse microbes such as E. coli and baker's yeast, used by every lab
  14: Liquid-handling robots for routine lab steps, sold by many equipment makers
  16: Protein structure prediction, now open to use through models like AlphaFold
  18: Bulk enzymes for detergents and starch, sold at low prices by a few big suppliers
  20: Small lab and pilot fermenters, now easy to buy or rent by the week
```

### ed102
```yaml
status: ok
title: Why has it become commoditized?
note: We see commoditization where the field can reuse cheap DNA, standard cells and open models. New value therefore comes from making engineered cells work at scale and at a price buyers accept.
t:
  7: DNA PRINTING
  9: DNA READING
  11: CRISPR kits
  13: HOST CELLS
  15: LAB ROBOTS
  17: FOLD MODELS
  19: BULK ENZYMES
  21: SMALL TANKS
  6: Because chip-based synthesis turned short DNA into a cheap mass product
  8: Because reading a human genome went from about $100M in 2001 to under $1,000
  10: Because CRISPR became the default editing tool in labs after 2012
  12: Because these microbes have been studied and used for many decades
  14: Because lab automation spread across pharma long before synthetic biology
  16: Because AlphaFold made predicted structures free for most known proteins
  18: Because these enzymes have sold in large volumes for many decades
  20: Because standard steel and glass tanks are made by many equipment firms
```

### ed103
```yaml
status: ok
title: Where is value created today?
page: 1/2
note: We derived these elements from the bottlenecks that sank or slowed flagship companies. The strongest value today sits in making engineered cells productive, scalable and cheap to purify.
t:
  9: 'STRAIN

    YIELD'
  7: Cells that make more product per liter and per hour, which sets the cost per kilo
  12: 'SCALE-UP

    KNOW-HOW'
  10: Teams and data that keep lab yields when a process moves from a flask to big tanks
  17: 'DOWNSTREAM

    PURIFICATION'
  15: Methods that recover a pure product from the broth at a low cost per kilo
```

### ed104
```yaml
status: ok
title: Where is value created today?
page: 2/2
note: We derived these elements from recent deals, funding rounds and approvals. Value is increasingly created by owning lab data, designing proteins with AI and holding the clearances buyers need.
t:
  9: 'DESIGN

    DATA'
  7: Large sets of measured lab results that make AI design models more accurate
  12: 'AI PROTEIN

    DESIGN'
  10: Models that propose working proteins, enzymes and editors in fewer rounds of lab testing
  17: 'REGULATORY

    CLEARANCES'
  15: Approvals from the FDA, EPA or EFSA that let an engineered product reach buyers
```

### ed106-s1
```yaml
status: ok
t:
  6: VALUE CREATION
  3: DESIGN TOOLS
  5: Software and AI that plan new DNA, proteins and cells
```

### ed107-s1
```yaml
status: ok
title: Who needs it the most?
note: We focus on five groups where design tools create the clearest value today. These are priority use cases, not a full list of clients.
t:
  21: DESIGN TOOLS
  5: 'BIOTECH

    STARTUPS'
  7: They are young drug and enzyme companies that want to design proteins in weeks without building a large wet lab first
  8: 'PHARMA R&D

    TEAMS'
  10: They are big drug makers that want AI to improve antibodies and enzymes faster than their own screening teams can
  11: 'ENZYME

    MAKERS'
  13: They are industrial enzyme suppliers that want enzymes that work hotter, faster or cheaper in customers' plants
  14: 'ACADEMIC

    LABS'
  16: They are university labs that want to plan gene circuits and proteins before spending scarce grant money on tests
  17: 'CELL LINE

    TEAMS'
  19: They are teams that build cells to make biologic drugs and want designs that raise yield and stay stable
```

### ed108-s1
```yaml
status: ok
title: What does "maximum customer value" look like in practice?
t:
  5: DESIGN TOOLS
  10: EXCEPTIONAL CUSTOMER EXPERIENCE
  7: The team uploads a target and gets a short list of protein designs that mostly work at the first lab test. The model learns from each round, the data stays private, and a drug or enzyme candidate is ready in weeks instead of the year it used to take.
  12: VS
  9: BAD CUSTOMER EXPERIENCE
  6: The team pays for a model that looks good on benchmarks, but few designs work in the lab. Data must be cleaned by hand, results cannot be explained, and after months of tests the project falls back to old screening methods.
```

### ed109-s1
```yaml
status: ok
title: How does the money flow in this case?
t:
  14: DESIGN TOOLS
  9: '🔍

    A lab compares design platforms'
  7: '🧪

    It tests the first designs in the lab'
  6: '📊

    Results feed back into the model'
  8: '💳

    The lab pays a yearly license'
  13: '🔁

    New targets and uses are added'
  11: '👥

    More teams in the firm use the tool'
  10: '📈

    The model improves with each project'
  12: '💊

    A better protein enters development'
```

### ed106-s2
```yaml
status: ok
t:
  6: VALUE CREATION
  3: ROBOTIC BIOFOUNDRIES
  5: Robot labs that build and test thousands of designs for clients
```

### ed107-s2
```yaml
status: ok
title: Who needs it the most?
note: We focus on five groups where robotic biofoundries create the clearest value today. These are priority use cases, not a full list of clients.
t:
  21: ROBOTIC BIOFOUNDRIES
  5: 'FOOD

    STARTUPS'
  7: They are young food and ingredient companies that need an engineered strain fast but cannot afford their own robot lab
  8: 'CHEMICAL

    GROUPS'
  10: They are chemical and materials makers that want to test bio-based routes without hiring a full biology team
  11: 'PHARMA

    PARTNERS'
  13: They are drug makers that outsource cell line and enzyme work to cut cost and keep internal teams on core programs
  14: 'DEFENSE

    AGENCIES'
  16: They are defense and public agencies that fund biomanufacturing for local supply of critical chemicals and materials
  17: 'UNIVERSITY

    LABS'
  19: They are academic labs that rent automated build and test runs instead of doing hundreds of steps by hand
```

### ed108-s2
```yaml
status: ok
title: What does "maximum customer value" look like in practice?
t:
  5: ROBOTIC BIOFOUNDRIES
  10: EXCEPTIONAL CUSTOMER EXPERIENCE
  7: The client sends a target molecule and gets a strain that meets the agreed yield, with full data on every design tested. Timelines and fees are fixed, results transfer smoothly to the client's pilot plant, and the client keeps the rights to the strain.
  12: VS
  9: BAD CUSTOMER EXPERIENCE
  6: The client pays for many months of runs, but the strain only works in the foundry's small plates. Yields fall in the first pilot tank, the data is hard to reuse, and disputes over who owns the strain delay the launch.
```

### ed109-s2
```yaml
status: ok
title: How does the money flow in this case?
t:
  14: ROBOTIC BIOFOUNDRIES
  9: '🔍

    A client sets a target molecule'
  7: '🤖

    Robots build thousands of strains'
  6: '📊

    Tests pick the best performers'
  8: '💳

    The client pays fees and milestones'
  13: '🔁

    Royalties flow if the product sells'
  11: '👥

    The client orders new projects'
  10: '📈

    Foundry data improves each design'
  12: '🏭

    The strain moves to a pilot plant'
```

### ed106-s3
```yaml
status: ok
t:
  6: VALUE CREATION
  3: BIO-MANUFACTURING
  5: Engineered microbes and enzymes that make chemicals, foods and fibers
```

### ed107-s3
```yaml
status: ok
title: Who needs it the most?
note: We focus on five groups where bio-manufacturing creates the clearest value today. These are priority use cases, not a full list of clients.
t:
  21: BIO-MANUFACTURING
  5: 'FOOD

    BRANDS'
  7: They are food and drink makers that want dairy, egg and sweet proteins without animals or sugar, at a stable price
  8: 'CHEMICAL

    MAKERS'
  10: They are chemical groups that want lower-carbon versions of molecules they already buy from oil-based plants
  11: 'BEAUTY

    BRANDS'
  13: They are cosmetics makers that want rare natural ingredients like squalane made without sharks or olive harvests
  14: 'FASHION

    BRANDS'
  16: They are clothing and textile brands that want fibers made by fermentation instead of oil-based nylon
  17: 'FEED

    MAKERS'
  19: They are animal feed producers that want enzymes and proteins that raise nutrition and cut waste
```

### ed108-s3
```yaml
status: ok
title: What does "maximum customer value" look like in practice?
t:
  5: BIO-MANUFACTURING
  10: EXCEPTIONAL CUSTOMER EXPERIENCE
  7: The buyer gets an ingredient that works like the old one in its recipes and lines, at a price within a few percent. Supply comes from several plants under long contracts, quality is the same in every batch, and the label passes every regulator.
  12: VS
  9: BAD CUSTOMER EXPERIENCE
  6: The buyer reformulates around a new ingredient, then supply stalls when the startup's plant misses its yield. The price stays several times higher than the old input, batches vary, and the brand drops the product after one season.
```

### ed109-s3
```yaml
status: ok
title: How does the money flow in this case?
t:
  14: BIO-MANUFACTURING
  9: '🔍

    A buyer tests samples in its recipes'
  7: '🧬

    The strain is tuned for higher yield'
  6: '🏭

    A pilot plant makes the first tons'
  8: '💳

    The buyer signs a supply contract'
  13: '🔁

    New products reuse the same plant'
  11: '👥

    More brands adopt the ingredient'
  10: '📈

    Volume lowers the cost per kilo'
  12: '📦

    Product ships at commercial scale'
```

### ed106-s4
```yaml
status: ok
t:
  6: VALUE CREATION
  3: ENGINEERED MEDICINES
  5: Programmed cells, gene circuits and edits that treat diseases
```

### ed107-s4
```yaml
status: ok
title: Who needs it the most?
note: We focus on five groups where engineered medicines create the clearest value today. These are priority use cases, not a full list of clients.
t:
  21: ENGINEERED MEDICINES
  5: 'BIG

    PHARMA'
  7: They are large drug makers that want gene editors and programmed cells to treat diseases that pills and antibodies cannot reach
  8: 'BIOTECH

    STARTUPS'
  10: They are young drug developers that license editing or cell-design tools instead of building them from scratch
  11: 'HOSPITALS AND

    CLINICS'
  13: They are care centers that want one-time treatments for genetic diseases such as sickle cell, given safely
  14: 'HEALTH

    INSURERS'
  16: They are health insurers that want proof that a one-time gene treatment saves more than years of usual care
  17: 'DRUG

    REGULATORS'
  19: They are agencies such as the FDA that want clear data on how an edited cell was made and how long it stays safe
```

### ed108-s4
```yaml
status: ok
title: What does "maximum customer value" look like in practice?
t:
  5: ENGINEERED MEDICINES
  10: EXCEPTIONAL CUSTOMER EXPERIENCE
  7: The drug maker licenses an editor or cell program that hits only the intended genes, works in one dose and keeps working for years. Making it is repeatable at scale, safety follow-up is clean, and the price is backed by savings on long-term care.
  12: VS
  9: BAD CUSTOMER EXPERIENCE
  6: The editor also changes genes it should not touch, or the programmed cells stop working after months. Each dose is costly to make, safety checks drag on for years, and insurers refuse to pay the high one-time price.
```

### ed109-s4
```yaml
status: ok
title: How does the money flow in this case?
t:
  14: ENGINEERED MEDICINES
  9: '🔍

    A drug maker screens editing platforms'
  7: '🧪

    The program enters early human trials'
  6: '📊

    Data confirm the edit and its safety'
  8: '💳

    A partner pays upfront and milestones'
  13: '🔁

    The platform moves to new diseases'
  11: '🏥

    More centers learn to give it'
  10: '📈

    Long follow-up builds trust'
  12: '💉

    Treated people get a one-time dose'
```

### ed106-s5
```yaml
status: ok
t:
  6: VALUE CREATION
  3: CROP ENGINEERING
  5: Edited crops and engineered microbes that feed and protect plants
```

### ed107-s5
```yaml
status: ok
title: Who needs it the most?
note: We focus on five groups where crop engineering creates the clearest value today. These are priority use cases, not a full list of clients.
t:
  21: CROP ENGINEERING
  5: 'CORN

    GROWERS'
  7: They are large corn and wheat farms that want to cut synthetic fertilizer costs without losing yield
  8: 'SEED

    COMPANIES'
  10: They are seed groups that want edited traits for yield, disease or shelf life faster than classic breeding allows
  11: 'INPUT

    RETAILERS'
  13: They are farm stores and distributors that want new products with good margins that fit their delivery season
  14: 'FRUIT

    GROWERS'
  16: They are banana, fruit and vegetable growers that want crops that resist disease and last longer after harvest
  17: 'FOOD

    COMPANIES'
  19: They are food buyers that want steady crop supply with less waste, under labels their markets accept
```

### ed108-s5
```yaml
status: ok
title: What does "maximum customer value" look like in practice?
t:
  5: CROP ENGINEERING
  10: EXCEPTIONAL CUSTOMER EXPERIENCE
  7: The farmer applies an engineered microbe at planting and gets the same or better yield with less fertilizer, field after field. The price is locked for several seasons, results are measured on their own farm, and export buyers accept the crop.
  12: VS
  9: BAD CUSTOMER EXPERIENCE
  6: The microbe works in trials but fades in cold or dry soil, so yields drop on some fields. The farmer pays for both the product and extra fertilizer, cannot see a clear gain, and an export buyer questions the edited crop.
```

### ed109-s5
```yaml
status: ok
title: How does the money flow in this case?
t:
  14: CROP ENGINEERING
  9: '🔍

    Agronomists run trials on local farms'
  7: '🌱

    Growers apply the product at planting'
  6: '📊

    Yields are measured at harvest'
  8: '💳

    The grower pays per acre treated'
  13: '🔁

    New crops and traits are added'
  11: '👥

    More growers adopt it nearby'
  10: '📈

    Field data improve the next version'
  12: '📦

    The crop is sold to food buyers'
```
