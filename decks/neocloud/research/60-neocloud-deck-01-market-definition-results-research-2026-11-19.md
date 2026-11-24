# Neocloud, chapter 01 Market definition (evergreen, written by Claude, 19 Nov 2026)

### ed006
```yaml
status: ok
title: What is the neocloud market, in simple terms?
text: Neocloud is the market for specialist companies that rent out AI computing power, from one GPU by the hour to whole clusters and hosted AI models
note: We use a conversational definition here because it makes the boundary with the big general clouds and with plain data centers easier to understand.
icon_tl: 🖥️
```

### ed007p
```yaml
status: no_data
reason: taken from the live product page
```

### ed008
```yaml
status: ok
title: What markets are often confused with neocloud?
t:
  12: BIG CLOUDS
  13: NEOCLOUD
  14: DATA CENTERS
  7: Neoclouds sit between them because they run the chips and the building, and sell only AI computing time to their clients
  10: Big clouds like AWS, Azure and Google Cloud rent hundreds of services, and AI chips are only one line among many
  11: Data centers rent space, power and cooling to tenants, who then bring and run their own servers inside
```

### ed009
```yaml
status: ok
title: What markets does neocloud sit between?
t:
  8: "CLOUD\nCOMPUTING"
  9: "AI\nCHIPS"
  10: "DATA\nCENTERS"
  13: 'Neocloud sits between three markets: it rents computing like the big clouds, it buys the newest AI chips before most others, and it builds or leases data centers full of them. It sells only AI work.'
```

### ed010
```yaml
status: ok
title: And what if we break it down in smaller markets?
t:
  21: NEOCLOUD
  5: "GPU\nCLOUDS"
  8: "INFERENCE\nCLOUDS"
  11: "DEDICATED\nCLUSTERS"
  14: "SOVEREIGN\nAI CLOUDS"
  17: "COMPUTE\nMARKETPLACES"
  7: It is in the market when a company rents GPUs by the hour or by the month to anyone
  10: It is in the market when a company runs its clients' AI models and bills by the token
  13: It is in the market when a whole cluster is built and reserved for one big AI client
  16: It is in the market when a local cloud keeps AI chips and data inside one country
  19: It is in the market when a platform rents out spare GPUs of other hosts to its clients
```

### ed011
```yaml
status: ok
title: What are some common acronyms I should know?
note: We kept the acronyms that come back again and again in company filings, contract news and investor decks, rather than chip design terms.
t:
  6: GPU
  15: SLA
  23: HBM
  8: "Graphics\nProcessing Unit"
  16: "Service Level\nAgreement"
  24: "High Bandwidth\nMemory"
  4: It is the chip that does the math of AI, made mostly by Nvidia and also by AMD
  13: It is the uptime a cloud promises in its contract, with money back when it fails
  21: It is the fast memory stacked next to each AI chip, and it is now in short supply
  11: LLM
  19: TCO
  27: TPU
  12: "Large Language\nModel"
  20: "Total Cost of\nOwnership"
  28: "Tensor\nProcessing Unit"
  9: It is the type of AI model behind ChatGPT, which neoclouds train and run for clients
  17: It is the full cost of a chip over its life, with power, staff and debt included
  25: It is Google's own AI chip, an alternative to Nvidia GPUs that Anthropic rents at scale
```

### ed012
```yaml
status: no_data
reason: offers and their names change too often to group them reliably without fresh research
```

### ed013
```yaml
status: no_data
reason: rental prices per GPU-hour move every month, left for the research chapters
```

### ed014
```yaml
status: ok
title: When and where is value created in the market?
items:
- e: ⚡
  t: When a company secures power and a site years before its rivals can
- e: 🤝
  t: When a big AI lab signs a take-or-pay contract that books years of capacity
- e: 💻
  t: When the newest Nvidia chips go live before they reach the big clouds
- e: 🔁
  t: When spare GPUs are rented out by the hour, so that no costly chip sits idle
- e: ⚙️
  t: When software turns raw servers into clusters that rarely fail in training
- e: 💸
  t: When AI models are served by the token at a lower price than the big clouds
- e: 🌍
  t: When a country pays to keep its AI chips and all its data inside its borders
- e: 🏦
  t: When lenders fund GPU fleets against contracts already signed by clients
```

### ed015
```yaml
status: ok
title: What are some common myths about neocloud?
page: 1/2
note: We focused on myths that come back often in investor, analyst and press debates. The counters describe what companies have shown so far in filings and contracts.
t:
  9: Neoclouds just resell the GPUs of the big clouds
  7: Most of them own or lease their own chips and sites, and the big clouds now rent capacity from them instead
  12: Renting out GPUs is a simple commodity business
  10: Training runs crash when one server fails, so buyers pay more for clouds that keep thousands of GPUs running
  15: Only Nvidia chips matter in this market
  13: Cerebras, Groq and SambaNova run inference clouds on their own chips, and AMD backs clouds such as TensorWave
  0: Neoclouds only serve small AI startups
  16: Microsoft, Meta and OpenAI have signed multibillion contracts with CoreWeave, Nebius, Nscale, IREN and Lambda
```

### ed016
```yaml
status: ok
title: What are some common myths about neocloud?
page: 2/2
note: We focused on myths that come back often in investor, analyst and press debates. The counters describe what companies have shown so far in filings and contracts.
t:
  9: GPU demand will only keep going up
  7: The rental price of an Nvidia H100 fell from about $8 an hour in 2023 to near $2 in 2025 as supply caught up
  12: A bigger cluster always brings a bigger profit
  10: Clusters are bought with billions of debt, and an idle or outdated chip still has to be paid off every month
  15: Owning the chips is enough to win clients
  13: Clients choose on uptime, software and support, which is why analysts rate clouds on much more than price
  0: Neoclouds are only for training AI models
  16: Inference now grows fast, with Fireworks AI, Baseten and Together AI serving client models and billing by the token
```

### ed017
```yaml
status: ok
title: How mature is neocloud as a market?
score: 55
text: The market is real because leaders are listed, revenue passed $25B in 2025 and the biggest AI labs and clouds sign multiyear contracts. The score stays in the middle because a few clients make most of the revenue, fleets are funded with heavy debt and chips lose value in a few years.
note:
- We rate market maturity with an internal score of revenue, listed leaders, signed contracts, client spread and funding risk.
- We set 55/100 because demand and contracts are proven, but client concentration and debt-funded chips keep the risk high.
```

### ed018
```yaml
status: ok
title: How can we categorize companies of the neocloud market?
page: 1/3
note: We use the six solution groups of our company database, from clouds that rent GPUs by the hour to clusters built for one client.
t:
  25: Here, we categorize by type of solution
categories:
- label: "GPU\nCLOUDS"
  description: Companies renting GPU servers by the hour or by the month to AI teams of any size
  e: 💻
- label: "INFERENCE\nCLOUDS"
  description: Companies running their clients' AI models and billing by the token or by the second
  e: ⚡
- label: "COMPUTE\nMARKETPLACES"
  description: Companies renting out spare GPUs of partner data centers and taking a share of each hour
  e: 🔀
- label: "DEDICATED\nCLUSTERS"
  description: Companies building whole clusters reserved for one big AI lab under a multiyear contract
  e: 🏭
- label: "SOVEREIGN\nAI CLOUDS"
  description: Companies keeping AI chips and data inside one country or spread across many small hosts
  e: 🌍
- label: "TRAINING\nPLATFORMS"
  description: Companies selling tools and computing power to train and fine-tune AI models in one place
  e: 🧠
```

### ed019
```yaml
status: ok
title: How can we categorize companies of the neocloud market?
page: 2/3
note: We also categorize by buyer because AI labs, big tech, startups and governments need very different contract sizes, prices and service levels.
t:
  25: Here, we categorize by the type of buyer
categories:
- label: "AI MODEL\nLABS"
  description: Companies building clusters of tens of thousands of GPUs for labs like OpenAI and Anthropic
  e: 🧠
- label: "BIG\nTECH"
  description: Companies renting extra capacity to hyperscalers like Microsoft and Meta when theirs runs out
  e: 🏢
- label: "AI APP\nSTARTUPS"
  description: Companies serving the models behind coding, search and image apps, billed by each request
  e: 🚀
- label: "COMPANIES AND\nGOVERNMENT"
  description: Companies giving banks, factories and states private AI computing inside their own country
  e: 🏛️
- label: "RESEARCH\nLABS"
  description: Companies renting GPU time to universities and public labs that cannot afford their own
  e: 🔬
- label: "SOLO\nDEVELOPERS"
  description: Companies letting one person start a GPU in a minute and pay only for the seconds used
  e: 🧑‍💻
```

### ed020
```yaml
status: ok
title: How can we categorize companies of the neocloud market?
page: 3/3
note: A third useful lens is the business model, because an hourly rental, a five-year contract and a fee per token bring in money very differently.
t:
  25: Here, we categorize by business model
categories:
- label: "HOURLY\nRENTAL"
  description: Companies billing each GPU by the hour or the second, with no commitment from the client
  e: ⏱️
- label: "RESERVED\nCONTRACTS"
  description: Companies signing take-or-pay contracts of several years before building the cluster
  e: 📝
- label: "PER-TOKEN\nPRICING"
  description: Companies charging for each word an AI model reads or writes, not for the chips behind it
  e: 🪙
- label: "BROKER\nFEES"
  description: Companies keeping a share of every GPU hour they sell on behalf of partner data centers
  e: 🔗
- label: "MANAGED\nPLATFORMS"
  description: Companies selling a yearly plan that bundles computing, software and support for AI teams
  e: 🧰
- label: "PUBLIC\nPROGRAMS"
  description: Companies paid by governments to run national AI computing for local firms and researchers
  e: 🏛️
```

### ed021
```yaml
status: ok
title: What do top companies do in this market?
note: Other companies could also make the top eight. We chose the players with the most capacity, contracts or funding to show the range of the market.
t:
  8: COREWEAVE
  16: CRUSOE
  7: They are the largest neocloud, listed in 2025, with OpenAI, Meta and Microsoft as clients
  15: They build AI campuses with their own power, like the Stargate site in Abilene, Texas
  10: LAMBDA
  18: NSCALE
  9: They rent Nvidia GPU clusters to AI teams and signed a multibillion deal with Microsoft
  17: They build AI clusters in Europe and the US, with Microsoft as their anchor client
  12: TOGETHER AI
  20: FIREWORKS AI
  11: They run open-source AI models for developers and rent out training clusters
  19: They serve open AI models at high speed for coding and search apps, billed by the token
  14: BASETEN
  22: CEREBRAS
  13: They host and scale their clients' AI models, billed by the second of GPU use
  21: They run one of the fastest inference clouds on their own giant wafer-sized chips
```

### ed022
```yaml
status: ok
title: What is rare and that people happily pay for in this market?
note: We looked at contract terms, rental prices, analyst ratings and company filings to find the capabilities that are scarce and that buyers pay for.
t:
  6: "⚡\nPower, because a new AI site can wait years for its grid connection"
  7: "💻\nNew chips early, because the newest Nvidia GPUs rent at the highest prices"
  8: "🛡️\nUptime, because one failed server can stop a training run of thousands of GPUs"
  9: "🤝\nLong contracts, because lenders fund GPUs only against signed client deals"
  10: "🔌\nFast networks, because GPUs must share data all the time to train one model"
  11: "⚙️\nGood software, because clients want clusters that work on the very first day"
  12: "🌍\nLocal data, because many governments want AI to run inside their own borders"
  13: "🔥\nLiquid cooling, because the newest racks run too hot for most older data centers"
```

### ed023
```yaml
status: ok
title: Which neocloud truths have flipped?
note: These are market shifts we see in contracts, funding and filings in recent years. They are not formal industry rules, but they recur across the evidence.
t:
  6: GPU clouds used to be side businesses of crypto miners
  8: Now they are listed companies with contracts worth tens of billions
  10: AI chips used to go mainly to the three big clouds
  12: Now Nvidia ships huge volumes straight to neoclouds too
  14: Renting a top GPU used to mean weeks of waiting
  16: Now a developer can start one in a minute and pay by the second
  18: The big clouds used to see neoclouds as small rivals
  20: Now Microsoft and Meta rent billions of dollars of their capacity
  22: Training used to be the main reason to rent GPUs
  24: Now inference grows faster, and some clouds bill only per token
  26: Data centers used to be built for general cloud use
  28: Now new sites are built for AI first, with liquid cooling and their own power
```

### ed024
```yaml
status: ok
title: What has changed (very) recently?
page: 1/2
items:
- d: SINCE 2023
  t: Nvidia invested in CoreWeave and gave it early access to its newest chips, turning a former crypto miner into the leading AI cloud provider.
- d: SINCE 2024
  t: Analysts started to call GPU-first clouds neoclouds, as dozens of new providers raised money to buy Nvidia chips and rent them to AI teams.
- d: SINCE 2024
  t: Rental prices for an Nvidia H100 started to fall fast as supply caught up, pushing neoclouds from hourly rentals toward long contracts.
- d: SINCE 2025
  t: CoreWeave listed on Nasdaq in March, the first big neocloud IPO, and then signed contracts with OpenAI worth more than $22B in total.
- d: SINCE 2025
  t: Nvidia bought Lepton AI and launched DGX Cloud Lepton, a marketplace that sends developers to the GPU capacity of many partner clouds.
- d: SINCE 2025
  t: Microsoft signed a contract worth up to $19B with Nebius for GPU capacity in New Jersey, a sign that even the biggest clouds rent.
note:
- We kept the milestones that most changed contracts, funding or the way AI teams buy computing
- There is no official timeline, and another analyst could pick a few different milestones here
```

### ed025
```yaml
status: ok
title: What has changed (very) recently?
page: 2/2
items:
- d: SINCE 2025
  t: Meta signed a $14B deal with CoreWeave and a $3B deal with Nebius, joining Microsoft and OpenAI among the big buyers of neocloud capacity.
- d: SINCE 2025
  t: Microsoft signed a $9.7B five-year contract with IREN, a former bitcoin miner, showing how miners with power sites turn into AI clouds.
- d: SINCE 2025
  t: Anthropic announced a $50B plan to build its own data centers in Texas and New York with Fluidstack, a neocloud founded in 2017.
- d: SINCE 2025
  t: Nvidia signed a deal of about $20B for the chip technology and team of Groq, while GroqCloud kept running its inference service.
- d: SINCE 2026
  t: OpenAI agreed to buy 750 MW of inference computing from the Cerebras cloud through 2028, a deal reported to be worth more than $10B in total.
- d: SINCE 2026
  t: Gartner predicted that neoclouds will take 20% of an AI cloud market worth $267B by 2030, a sign that the label is now mainstream.
note:
- We kept the milestones that most changed contracts, funding or the way AI teams buy computing
- There is no official timeline, and another analyst could pick a few different milestones here
```
