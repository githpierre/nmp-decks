# Neocloud, chapter 04 Pain points (evergreen, written by Claude, 19 Nov 2026)

### ed054
```yaml
status: ok
title: What are the pain points of yesterday vs. today?
note: We grouped the market into phases, from crypto miners renting spare GPUs to today's multiyear AI contracts. We used company filings, contract news and rental price history.
t:
  6: "2017 - 2021\n\nCrypto miners and small hosts rented spare GPUs, but AI teams still bought almost all their computing from the big clouds"
  7: "2022 - 2023\n\nChatGPT set off a rush for Nvidia H100 chips, but AI labs waited months for them and paid up to $8 an hour per GPU"
  8: "2024 - 2025\n\nNeoclouds raised billions and signed multiyear deals, but rental prices fell and debt piled up on every new cluster"
  9: "TODAY\n\nThe biggest labs and clouds rent from neoclouds, but power, chip supply and a few huge clients limit how fast they grow"
  10: "?\n\nInference billed by the token could spread demand across many clients, but only if prices hold as chips keep getting cheaper"
```

### ed055
```yaml
status: ok
title: Which old problems are now behind us?
note: We treat these as problems that new providers, contracts and financing have removed for buyers. They do not mean that computing is now cheap or easy to find everywhere.
t:
  5: AI teams waited months to get even a few top Nvidia GPUs from the big clouds
  7: Neoclouds now let a developer start an H100 in a few minutes and pay only for the seconds it runs, with no contract
  8: Renting a GPU meant a long contract signed with a sales team
  10: Self-serve consoles now rent GPUs with a credit card in a few clicks, from one chip up to a small cluster
  11: A big training cluster could only be built by the three big clouds
  13: CoreWeave, Crusoe and Nscale now build clusters of tens of thousands of GPUs for one single client
  14: Running an open AI model meant renting and managing your own servers
  16: Inference clouds like Fireworks AI and Together AI now serve them by the token, with no server to manage
  17: Lenders would not fund chips rented by the hour to unknown clients
  19: Banks now lend billions of dollars against GPUs, as long as a strong client has signed a multiyear contract
  20: Many countries had to send their AI data to US clouds abroad
  22: Sovereign clouds in Europe, India and the Gulf now keep the data and the chips inside the country
```

### ed056
```yaml
status: ok
title: What problems do all players face?
page: 1/2
note: We kept the problems that come back in company filings, analyst reports and client reviews. We skipped chip design details and focused on what blocks neoclouds from growing.
t:
  6: "You need chips\nbefore your rivals"
  8: "Nvidia rations\nits newest GPUs"
  10: "You must keep\nevery GPU busy"
  12: "Idle GPUs\nburn cash fast"
  14: "You need power\nand land"
  16: "Grid hookups take\nyears to arrive"
  18: "You must keep\nclusters running"
  20: "One failed node\nstops training"
  23: "You need signed\ncontracts to borrow"
  25: "Debt costs more\nthan for big clouds"
  27: "You must win\nclients from AWS"
  29: "Big clouds keep\ncutting prices"
  31: "You must replace\nchips often"
  33: "Chips lose value\nwithin a few years"
  35: "You need staff\nwho run clusters"
  37: "Skilled engineers\nare hard to hire"
```

### ed057
```yaml
status: ok
title: What problems do all players face?
page: 2/2
note: We separated the problems of building capacity from the problems of selling it. Even a provider with chips and power must still find clients, prices and rules it can live with.
t:
  6: "You need more\nthan one big client"
  8: "A few clients make\nmost of the revenue"
  10: "You must cool\nthe newest racks"
  12: "Old sites cannot\nhandle liquid cooling"
  14: "You need a fair\nprice per GPU-hour"
  16: "Rental prices\nswing month to month"
  18: "You must keep\nclient data safe"
  20: "Model weights\nare prime targets"
  23: "You need good\nsoftware on top"
  25: "Raw servers do\nnot win loyal clients"
  27: "You must follow\nlocal data rules"
  29: "Rules differ in\neach country"
  31: "You need cheap\nmoney to grow"
  33: "Interest rates\nraise every cost"
  35: "You must plan\nfor export rules"
  37: "US export limits\nblock some markets"
```

### ed059
```yaml
status: ok
title: Which problems are startups going after?
t:
  16: "Chip\naccess"
  11: "Idle\nGPUs"
  14: "Power\nsupply"
  21: "Pain points change sharply by buyer and by size.\n\nBroad statements quickly mislead.\nSo we split AI labs, big tech, app startups and enterprises before scoring priorities."
  13: "Cluster\nuptime"
  12: "Client\nspread"
  15: "Price\nswings"
  18: "Local\ndata"
  19: "Cheap\nfinancing"
```

### ed060
```yaml
status: ok
title: How will we proceed?
note: We break the market down before scoring because the same GPU cluster creates very different value and risk for an AI lab, a big cloud, a startup or a government.
t:
  9: "😣\nPAIN POINTS\n\nWe list each group's main pains and score them to rank them."
  6: "🎯\nGOAL\n\nFind the pain points that matter most in neocloud, and who feels them."
  7: "🏷️\nCATEGORIES\n\nWe split the market by buyer, because needs and budgets differ a lot."
  8: "🧑‍🤝‍🧑\nSEGMENTS\n\nFor each buyer, we list the people who decide, pay, use and approve."
```

### ed061
```yaml
status: ok
title: Which categories will we use?
note: We split the market into four buyer groups. They differ enough in contract size, technical needs and decision steps to score their pain points separately.
t:
  7: "AI MODEL\nLABS"
  9: "HYPERSCALERS\nAND BIG TECH"
  11: "AI APP\nSTARTUPS"
  13: "ENTERPRISES AND\nGOVERNMENTS"
  6: Labs like OpenAI and Anthropic training the biggest models on clusters rented for years
  8: Big clouds and tech groups that rent extra GPU capacity when their own sites run out
  10: Young companies whose coding, search or image apps pay for every AI request they serve
  12: Banks, factories and states that want private AI computing under their own data rules
  15: ''
  17: ''
  14: ''
  16: ''
holes_ok: true
```

### ed062-s1
```yaml
status: ok
t:
  6: PAIN POINTS
  3: AI MODEL LABS
  5: "Labs that train the biggest AI models\nand rent whole clusters for several years"
```

### ed063-s1
```yaml
status: ok
title: Who needs neocloud capacity?
note: We focus on the five groups inside AI labs that plan, buy, use and secure the clusters they rent from neoclouds.
t:
  27: AI MODEL LABS
  5: "COMPUTE\nLEADS"
  8: "RESEARCH\nTEAMS"
  11: "FINANCE\nCHIEFS"
  14: "INFERENCE\nTEAMS"
  17: "SECURITY\nTEAMS"
  20: 🧑‍💻
  21: 🧠
  22: 💰
  23: ⚡
  24: 🔒
  7: They need tens of thousands of GPUs on a fixed date, since a late cluster delays the next model by months
  10: They need clusters that rarely crash, because one failed server can stop a training run for hours
  13: They need to fund billions of computing without being stuck paying for chips that age fast
  16: They need cheap and fast capacity to serve millions of users once a new model is launched
  19: They need to keep model weights and data safe in sites that the lab does not run itself
```

### ed064-s1
```yaml
status: ok
title: What are these customers' strongest pain points?
note: We prioritized problems that recur in lab statements, contract news and analyst reports on the largest AI training clusters.
t:
  13: AI MODEL LABS
  14: They get their new clusters later than the date promised
  15: They see training runs crash when one server fails
  16: They sign contracts of years on chips that age fast
  17: They depend on a few providers for most of their capacity
  18: They run out of power before they run out of money
  19: They pay more and more to serve each new model to users
  20: They must protect model weights in sites they do not run
```

### ed065-s1
```yaml
status: ok
title: Which pains deserve attention first?
subtitle: AI model labs
icons:
- 🧑‍💻
- 🧠
- 💰
- ⚡
- 🔒
rows:
- pain: New clusters arrive later than the date in the contract
  s: [3, 3, 2, 2, 1]
  p: CRITICAL
- pain: Training runs crash when a single server fails
  s: [2, 3, 1, 1, 1]
  p: MAJOR
- pain: Multiyear contracts lock them into chips that age fast
  s: [2, 1, 3, 2, 1]
  p: MAJOR
- pain: Most of their capacity depends on a few providers
  s: [3, 2, 3, 2, 2]
  p: CRITICAL
- pain: Power runs out before money does on new sites
  s: [3, 2, 2, 2, 1]
  p: HIGH
- pain: Serving each new model to users costs more and more
  s: [2, 1, 3, 3, 1]
  p: HIGH
- pain: Model weights sit in data centers they do not run
  s: [1, 2, 1, 1, 3]
  p: HIGH
note:
- Every stakeholder is different, and this table is a simplified view based on lab statements and analyst reports
- It gives a starting point, not a checklist, so priorities should be validated with labs, providers and lenders
```

### ed062-s2
```yaml
status: ok
t:
  6: PAIN POINTS
  3: HYPERSCALERS AND BIG TECH
  5: "Big clouds and tech groups that rent\nextra capacity when their own runs out"
```

### ed063-s2
```yaml
status: ok
title: Who needs neocloud capacity?
note: We focus on the five groups inside big clouds and tech groups that decide when to rent capacity from neoclouds and how much.
t:
  27: HYPERSCALERS AND BIG TECH
  5: "CAPACITY\nPLANNERS"
  8: "CLOUD\nPRODUCT TEAMS"
  11: "PROCUREMENT\nTEAMS"
  14: "FINANCE\nCHIEFS"
  17: "SECURITY\nTEAMS"
  20: 📊
  21: 🖥️
  22: 📝
  23: 💰
  24: 🛡️
  7: They need extra GPUs within months when their own new data centers are late or already sold out
  10: They need capacity they can resell to their own cloud clients under their brand and their prices
  13: They need contracts they can grow or cut, since demand for AI may change within two years
  16: They need to rent rather than build, to keep billions of spending off their own balance sheet
  19: They need neocloud sites to meet the same security and uptime rules as their own data centers
```

### ed064-s2
```yaml
status: ok
title: What are these customers' strongest pain points?
note: We prioritized problems that recur in earnings calls of the big clouds, their capacity contracts and analyst reports on AI spending.
t:
  13: HYPERSCALERS AND BIG TECH
  14: They have more AI demand than their own sites can serve
  15: They wait years for power at their own new data centers
  16: They face investors worried about record AI spending
  17: They must hit their own uptime rules in sites they do not run
  18: They risk paying for capacity if AI demand slows
  19: They rely on small providers carrying heavy debt
  20: They want the newest chips as soon as Nvidia ships them
```

### ed065-s2
```yaml
status: ok
title: Which pains deserve attention first?
subtitle: Hyperscalers and big tech
icons:
- 📊
- 🖥️
- 📝
- 💰
- 🛡️
rows:
- pain: AI demand is larger than their own sites can serve
  s: [3, 3, 2, 2, 1]
  p: CRITICAL
- pain: Power for their own new data centers takes years
  s: [3, 2, 2, 2, 1]
  p: CRITICAL
- pain: Investors worry about their record spending on AI
  s: [1, 1, 2, 3, 1]
  p: MAJOR
- pain: Uptime rules must hold in sites they do not run
  s: [2, 3, 2, 1, 3]
  p: MAJOR
- pain: Long contracts must still be paid if demand slows
  s: [2, 1, 3, 3, 1]
  p: HIGH
- pain: Their providers carry heavy debt on every cluster
  s: [1, 1, 3, 3, 2]
  p: HIGH
- pain: They want the newest chips as soon as they ship
  s: [3, 3, 2, 1, 1]
  p: MAJOR
note:
- Every stakeholder is different, and this table is a simplified view based on earnings calls and capacity contracts
- It gives a starting point, not a checklist, so priorities should be validated with clouds, providers and analysts
```

### ed062-s3
```yaml
status: ok
t:
  6: PAIN POINTS
  3: AI APP STARTUPS
  5: "Young companies whose apps run on AI\nmodels and pay for every request they serve"
```

### ed063-s3
```yaml
status: ok
title: Who needs neocloud capacity?
note: We focus on the five groups inside AI app startups that choose, pay for and run the models behind their product.
t:
  27: AI APP STARTUPS
  5: "STARTUP\nFOUNDERS"
  8: "ML\nENGINEERS"
  11: "PLATFORM\nTEAMS"
  14: "FINANCE\nLEADS"
  17: "PRODUCT\nTEAMS"
  20: 🚀
  21: 🧑‍💻
  22: ⚙️
  23: 💵
  24: 📱
  7: They need computing costs that grow slower than revenue, since AI bills can eat most of their margin
  10: They need to fine-tune and serve open models fast, without managing servers or GPU drivers
  13: They need capacity that scales in seconds when traffic jumps, and that shuts down when it falls
  16: They need a clear and stable price per request, so they can price their own plans with confidence
  19: They need answers in a fraction of a second, because users leave an app that feels slow
```

### ed064-s3
```yaml
status: ok
title: What are these customers' strongest pain points?
note: We prioritized problems that recur in developer forums, startup founder interviews and the pricing pages of inference clouds.
t:
  13: AI APP STARTUPS
  14: They see AI bills eat most of their gross margin
  15: They cannot get GPUs fast when their traffic suddenly jumps
  16: They pay for idle GPUs between peaks of traffic
  17: They lose users when the model answers too slowly
  18: They struggle to switch from one provider to another
  19: They see prices per token change from month to month
  20: They lack the engineers to run models on their own GPUs
```

### ed065-s3
```yaml
status: ok
title: Which pains deserve attention first?
subtitle: AI app startups
icons:
- 🚀
- 🧑‍💻
- ⚙️
- 💵
- 📱
rows:
- pain: AI bills eat most of the gross margin of the app
  s: [3, 1, 2, 3, 2]
  p: CRITICAL
- pain: GPUs are hard to get fast when traffic suddenly jumps
  s: [2, 2, 3, 1, 3]
  p: MAJOR
- pain: Idle GPUs are still paid for between traffic peaks
  s: [2, 1, 3, 3, 1]
  p: MAJOR
- pain: Slow model answers make users leave the app fast
  s: [3, 2, 2, 1, 3]
  p: CRITICAL
- pain: Moving from one provider to another takes weeks
  s: [1, 3, 3, 1, 1]
  p: HIGH
- pain: Prices per token change from one month to the next
  s: [2, 1, 1, 3, 2]
  p: HIGH
- pain: Too few engineers to run models on their own GPUs
  s: [3, 3, 2, 1, 1]
  p: HIGH
note:
- Every stakeholder is different, and this table is a simplified view based on developer forums and founder interviews
- It gives a starting point, not a checklist, so priorities should be validated with founders, engineers and providers
```

### ed062-s4
```yaml
status: ok
t:
  6: PAIN POINTS
  3: ENTERPRISES AND GOVERNMENTS
  5: "Large firms and states that want private\nAI computing under their own data rules"
```

### ed063-s4
```yaml
status: ok
title: Who needs neocloud capacity?
note: We focus on the five groups inside large firms and public bodies that decide, approve and pay for private AI computing.
t:
  27: ENTERPRISES AND GOVERNMENTS
  5: "IT\nCHIEFS"
  8: "DATA\nTEAMS"
  11: "COMPLIANCE\nOFFICERS"
  14: "PUBLIC\nAGENCIES"
  17: "BUYING\nTEAMS"
  20: 🏢
  21: 📊
  22: ⚖️
  23: 🏛️
  24: 📋
  7: They need AI computing that fits their security rules, without building a GPU data center themselves
  10: They need to train and run models on their own data, which often cannot leave the company
  13: They need proof of where data sits and who can see it, to satisfy regulators and auditors
  16: They need national AI capacity for local firms and researchers, run under local law
  19: They need clear contracts and prices they can compare, in a market that changes every month
```

### ed064-s4
```yaml
status: ok
title: What are these customers' strongest pain points?
note: We prioritized problems that recur in enterprise AI surveys, public sovereign AI plans and the offers of sovereign cloud providers.
t:
  13: ENTERPRISES AND GOVERNMENTS
  14: They cannot send sensitive data to clouds abroad
  15: They lack the staff to run GPU clusters on their own
  16: They find few local providers with the newest chips
  17: They must prove where their data sits to regulators
  18: They struggle to compare offers that change every month
  19: They fear paying for GPUs that their teams barely use
  20: They face slow public buying rules in a fast market
```

### ed065-s4
```yaml
status: ok
title: Which pains deserve attention first?
subtitle: Enterprises and governments
icons:
- 🏢
- 📊
- ⚖️
- 🏛️
- 📋
rows:
- pain: Sensitive data cannot be sent to clouds abroad
  s: [3, 3, 3, 3, 1]
  p: CRITICAL
- pain: Too few of their staff know how to run GPU clusters
  s: [3, 2, 1, 2, 1]
  p: MAJOR
- pain: Few local providers offer the newest Nvidia chips
  s: [2, 3, 1, 3, 2]
  p: MAJOR
- pain: Regulators ask where data sits and who sees it
  s: [2, 1, 3, 3, 1]
  p: CRITICAL
- pain: Offers and prices of providers change every month
  s: [1, 1, 1, 1, 3]
  p: HIGH
- pain: GPUs bought or rented may sit barely used for months
  s: [3, 2, 1, 2, 3]
  p: HIGH
- pain: Public buying rules are slow for a fast market
  s: [1, 1, 1, 3, 3]
  p: HIGH
note:
- Every stakeholder is different, and this table is a simplified view based on enterprise surveys and public AI plans
- It gives a starting point, not a checklist, so priorities should be validated with IT chiefs, agencies and providers
```
