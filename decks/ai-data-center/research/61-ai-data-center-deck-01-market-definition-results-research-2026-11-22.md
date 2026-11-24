# AI data center, chapter 01 Market definition (evergreen, written by Claude, 22 Nov 2026)

### ed006
```yaml
status: ok
title: What is the AI data center market, in simple terms?
text: AI data centers are the companies that build and run the buildings where AI chips work, from giant campuses to small factory-made halls, and lease them to others
note: We use a conversational definition here because it makes the boundary with chip makers, GPU clouds and plain data centers easier to understand.
icon_tl: 🏢
```

### ed007p
```yaml
status: no_data
reason: taken from the live product page
```

### ed008
```yaml
status: ok
title: What markets are often confused with AI data centers?
t:
  12: NEOCLOUDS
  13: AI DATA CENTERS
  14: GENERAL COLO
  7: AI data centers sit in between because they build the halls, the power and the cooling made for AI chips, and lease them out
  10: Neoclouds rent AI chips by the hour or by the month, and most of them lease the buildings that hold the chips from others
  11: General colocation sites rent space, power and cooling to many tenants, for ordinary servers that need far less power
```

### ed009
```yaml
status: ok
title: What markets do AI data centers sit between?
t:
  8: "REAL\nESTATE"
  9: "POWER\nGENERATION"
  10: "CLOUD\nCOMPUTING"
  13: 'AI data centers sit between three markets: they buy land and build like property developers, they secure power like small utilities, and they lease capacity to AI labs and cloud companies.'
```

### ed010
```yaml
status: ok
title: And what if we break it down in smaller markets?
t:
  21: AI DATA CENTERS
  5: "AI\nCOLOCATION"
  8: "AI\nCAMPUSES"
  11: "POWERED\nCAMPUSES"
  14: "MODULAR AI\nCENTERS"
  17: "AI CLOUD\nOPERATORS"
  7: It is in the market when a company leases halls built for hot AI racks to several tenants
  10: It is in the market when a company builds a giant campus and leases it to one AI tenant
  13: It is in the market when a campus comes with its own power plant on the same land
  16: It is in the market when AI halls are built in a factory and shipped to a site
  19: It is in the market when a company runs its own AI campuses and rents the chips inside
```

### ed011
```yaml
status: ok
title: What are some common acronyms I should know?
note: We kept the acronyms that come back again and again in leases, utility filings and investor decks, rather than electrical engineering terms.
t:
  6: GPU
  15: PPA
  23: kW
  8: "Graphics\nProcessing Unit"
  16: "Power Purchase\nAgreement"
  24: "Kilowatt\nper rack"
  4: It is the chip that does the math of AI, and each new one needs more power to run
  13: It is a long contract to buy power from a plant, often signed before the site is built
  21: It measures how hot one rack runs, from about 10 kW in old halls to over 100 kW for AI
  11: MW
  19: HPC
  27: BTS
  12: "One million\nwatts"
  20: "High Performance\nComputing"
  28: "Build to\nSuit"
  9: It is how data centers are sized, and 1 MW is enough power for about 800 US homes
  17: It is heavy computing for science and AI, the word miners now use for their AI sites
  25: It is a site built for one tenant to its exact needs, then leased to it for 10 to 20 years
```

### ed012
```yaml
status: no_data
reason: lease and colocation offers are private and change too often to group them reliably without fresh research
```

### ed013
```yaml
status: no_data
reason: lease prices per megawatt move every quarter, left for the research chapters
```

### ed014
```yaml
status: ok
title: When and where is value created in the market?
items:
- e: ⚡
  t: When a company secures grid power years before its rivals can get any of it
- e: 🏗️
  t: When a campus is built fast enough to go live before the next chip generation
- e: 🤝
  t: When a big AI lab or cloud signs a lease of 10 to 20 years before the build starts
- e: 💧
  t: When halls are built for liquid cooling from day one, ready for the hottest AI racks
- e: 🏦
  t: When lenders fund the build against a lease of many years that is already signed
- e: 🔁
  t: When an old bitcoin mine and all its power are turned into a new AI data hall
- e: 🌍
  t: When a country pays to keep its AI computing and its data inside its borders
- e: 📦
  t: When halls are made in a factory, so a site goes live in months, not years
```

### ed015
```yaml
status: ok
title: What are some common myths about AI data centers?
page: 1/2
note: We focused on myths that come back often in investor, analyst and press debates. The counters describe what companies have shown so far in leases and filings.
t:
  9: AI data centers are just bigger data centers
  7: AI racks draw ten times more power than older ones and need water cooling, so most older halls cannot host them without a full rebuild
  12: Building the halls is the hardest part of the job
  10: Getting power is harder, as new sites wait years for a grid link in top US hubs, so many builders now bring their own gas turbines
  15: Only big tech firms can build AI campuses
  13: Startups like Crusoe, Lancium and Fluidstack build gigawatt campuses, and big tech and AI labs lease them instead of building alone
  0: Every AI data center drinks huge amounts of water
  16: Many new AI halls use closed water loops that are rarely refilled, but sites cooled by evaporation in hot places can still draw a lot
```

### ed016
```yaml
status: ok
title: What are some common myths about AI data centers?
page: 2/2
note: We focused on myths that come back often in investor, analyst and press debates. The counters describe what companies have shown so far in leases and filings.
t:
  9: Demand for AI data centers can only keep rising
  7: Microsoft slowed or paused some early projects in 2025, and a tenant can cut back plans for a campus long before its lease is signed
  12: A planned tenant means the money is safe
  10: Fermi America lost its first planned tenant in 2025 before a lease was signed, and its shares fell far below the price of its IPO
  15: Bitcoin miners cannot run AI data centers
  13: Galaxy, IREN, Core Scientific and Cipher turned mining sites into AI halls leased to CoreWeave, Microsoft or Amazon Web Services
  0: An AI data hall stays up to date for decades
  16: The building can last, but chips change every year or two, and each new rack needs more power and cooling than the hall was built for
```

### ed017
```yaml
status: ok
title: How mature is the AI data center market?
score: 50
text: The market is real because AI labs and big clouds sign leases of 10 to 20 years and gigawatt campuses are going live in Texas, Europe and Asia. The score stays in the middle because a few tenants take most of the capacity, grid power is scarce and most campuses are built with heavy debt.
note:
- We rate market maturity with an internal score of signed leases, live capacity, tenant spread, power access and debt risk.
- We set 50/100 because demand and leases are proven, but tenant concentration, power and debt keep the risk high.
```

### ed018
```yaml
status: ok
title: How can we categorize companies of the AI data center market?
page: 1/3
note: We use the six solution groups of our company database, from giant campuses leased to one tenant to halls built in a factory.
t:
  25: Here, we categorize by type of solution
categories:
- label: "AI\nCAMPUSES"
  description: Companies building giant campuses leased for years to one big AI tenant
  e: 🏗️
- label: "AI CLOUD\nOPERATORS"
  description: Companies running their own AI campuses and renting out the chips inside
  e: 🖥️
- label: "MODULAR AI\nCENTERS"
  description: Companies building AI data halls in factories and shipping them to sites
  e: 📦
- label: "AI\nCOLOCATION"
  description: Companies leasing halls ready for hot AI racks to many tenants at once
  e: 🏢
- label: "AI COMPUTE\nCENTERS"
  description: Companies building AI sites in new places, from Nordic towns to orbit
  e: 🛰️
- label: "POWERED\nCAMPUSES"
  description: Companies building AI campuses with their own power plant on the land
  e: ⚡
```

### ed019
```yaml
status: ok
title: How can we categorize companies of the AI data center market?
page: 2/3
note: We also categorize by buyer because AI labs, big tech, GPU clouds and governments need very different sizes, leases and power.
t:
  25: Here, we categorize by the type of buyer
categories:
- label: "AI MODEL\nLABS"
  description: Companies building gigawatt campuses for labs like OpenAI and Anthropic
  e: 🧠
- label: "BIG\nTECH"
  description: Companies leasing whole campuses to Microsoft, Meta, Google and Amazon
  e: 🏢
- label: "GPU\nCLOUDS"
  description: Companies leasing powered halls to CoreWeave and other GPU rental firms
  e: 💻
- label: "COMPANIES AND\nGOVERNMENT"
  description: Companies hosting the AI chips of banks, factories and states in-country
  e: 🏛️
- label: "AI APP\nSTARTUPS"
  description: Companies renting racks or small cages to young AI firms by the month
  e: 🚀
- label: "RESEARCH\nLABS"
  description: Companies hosting the AI computers of universities and national labs
  e: 🔬
```

### ed020
```yaml
status: ok
title: How can we categorize companies of the AI data center market?
page: 3/3
note: A third useful lens is the business model, because a 15-year lease, a monthly rack rental and a module sale bring in money very differently.
t:
  25: Here, we categorize by business model
categories:
- label: "LONG\nLEASES"
  description: Companies leasing whole halls for 10 to 20 years at a fixed price per MW
  e: 📝
- label: "POWERED\nLAND"
  description: Companies selling or leasing land that already has power, before a hall
  e: 📍
- label: "RACK\nRENTAL"
  description: Companies renting racks or cages by the month, with power billed on top
  e: 🗂️
- label: "GPU\nRENTAL"
  description: Companies putting chips in their own halls and renting them by the hour
  e: ⏱️
- label: "MODULE\nSALES"
  description: Companies selling factory-built data halls, often with service contracts
  e: 📦
- label: "JOINT\nVENTURES"
  description: Companies building campuses with funds, utilities or states for a share
  e: 🤝
```

### ed021
```yaml
status: ok
title: What do top companies do in this market?
note: Other companies could also make the top eight. We chose the players with the most capacity, leases or funding to show the range of the market.
t:
  8: CRUSOE
  16: COREWEAVE
  7: They built the first Stargate campus for OpenAI in Abilene, Texas, with power on the site
  15: They are the largest listed AI cloud, with about 1.7 GW of active power in 2026
  10: FLUIDSTACK
  18: ARMADA
  9: They build the data centers of the $50B Anthropic plan in Texas and New York
  17: They ship rugged modular data centers to remote sites, from oil fields to bases
  12: NSCALE
  20: FERMI AMERICA
  11: They build AI campuses in Norway, the UK and Texas, with Microsoft as tenant
  19: They plan an 11 GW campus near Amarillo, Texas, with its own gas and nuclear power
  14: LANCIUM
  22: STARCLOUD
  13: They own the powered land of the Abilene Stargate site and plan more campuses
  21: They put an Nvidia H100 chip in orbit in 2025 to test data centers in space
```

### ed022
```yaml
status: ok
title: What is rare and that people happily pay for in this market?
note: We looked at leases, utility filings, analyst reports and company disclosures to find the capabilities that are scarce and that tenants pay for.
t:
  6: "⚡\nGrid power, because new AI sites wait years for a connection in top hubs"
  7: "📍\nPowered land, because few sites have both the space and the power ready to use"
  8: "🤝\nAnchor tenants, because lenders fund a campus only against a signed long lease"
  9: "💧\nLiquid cooling, because the newest AI racks run far too hot for air alone"
  10: "⏱️\nSpeed, because a hall that goes live a year late misses a chip generation"
  11: "👷\nSkilled crews, because electricians are short in every big data center hub"
  12: "🏛️\nLocal support, because towns now block or delay many new data centers"
  13: "🔌\nTransformers, because heavy power gear can take years to be delivered"
```

### ed023
```yaml
status: ok
title: Which AI data center truths have flipped?
note: These are market shifts we see in leases, funding and filings in recent years. They are not formal industry rules, but they recur across the evidence.
t:
  6: Data centers used to be sized by their floor space in feet
  8: Now they are sized by power, in megawatts and more and more in gigawatts
  10: Most halls used to be cooled by air blown under the floor
  12: Now new AI halls pipe cool water straight onto each of the chips
  14: Big tech used to build all of its own data centers
  16: Now it also leases whole campuses from startups such as Crusoe
  18: Bitcoin mines used to be the main users of cheap power
  20: Now many of them have turned into AI data centers for GPU clouds
  22: Sites used to be picked near big cities and fiber
  24: Now they are picked where the power is, from West Texas to Norway
  26: Data centers used to plug into the grid like any building
  28: Now many bring their own gas turbines or sign deals for nuclear power
```

### ed024
```yaml
status: ok
title: What has changed (very) recently?
page: 1/2
items:
- d: SINCE 2024
  t: Blackstone agreed to buy AirTrunk for about A$24B, the biggest data center deal in Asia-Pacific, a sign that investors now see AI campuses as core infrastructure.
- d: SINCE 2024
  t: xAI built its Colossus AI cluster in Memphis in about four months, showing how fast a site can go live when power, chips and money are ready at the same time.
- d: SINCE 2025
  t: OpenAI, SoftBank and Oracle launched Stargate, a plan of up to $500B for AI data centers in the US, starting with a campus built by Crusoe in Abilene, Texas.
- d: SINCE 2025
  t: CoreWeave agreed to buy Core Scientific for about $9B to own its power sites, but Core Scientific shareholders voted the deal down in October.
- d: SINCE 2025
  t: A group led by BlackRock, Nvidia, Microsoft and MGX agreed to buy Aligned Data Centers for $40B, the largest data center deal on record so far.
- d: SINCE 2025
  t: Anthropic announced a $50B plan to build its own data centers in Texas and New York with Fluidstack, a company founded in 2017 to rent out GPUs.
note:
- We kept the milestones that most changed leases, funding or the way AI campuses get built
- There is no official timeline, and another analyst could pick a few different milestones here
```

### ed025
```yaml
status: ok
title: What has changed (very) recently?
page: 2/2
items:
- d: SINCE 2025
  t: Meta raised about $27B with Blue Owl to fund Hyperion, its AI campus in Louisiana, keeping most of the debt off its own balance sheet.
- d: SINCE 2025
  t: Cipher Mining, a former bitcoin miner, signed a $5.5B lease of 15 years with Amazon Web Services, showing how miners with power turn into AI landlords.
- d: SINCE 2025
  t: Fermi America listed in New York and London to build an 11 GW campus near Amarillo, then lost its first planned tenant before a lease was signed.
- d: SINCE 2025
  t: Starcloud launched a satellite with an Nvidia H100 chip on board, the first step of its plan to run AI data centers in space on solar power.
- d: SINCE 2026
  t: CoreWeave reported $3.7B of revenue for the third quarter of 2026, 2.7 times more than a year earlier, with a revenue backlog of about $133B.
- d: SINCE 2026
  t: The CEO of Fermi America left in April and its shares fell about 78% below their IPO price, a warning that powered land alone is not yet a business.
note:
- We kept the milestones that most changed leases, funding or the way AI campuses get built
- There is no official timeline, and another analyst could pick a few different milestones here
```
