# Neocloud, chapter 06 Value creation (evergreen, written by Claude, 19 Nov 2026)

### ed101
```yaml
status: ok
title: What's commoditized today in the market?
note: We identified elements that are now widely available across neocloud offers. They remain necessary, but value is moving to power, the newest chips, uptime and signed contracts.
t:
  7: OLDER GPUS
  9: ON-DEMAND H100S
  11: OPEN MODELS
  13: STORAGE
  15: GPU DRIVERS
  17: HOURLY BILLING
  19: RACK SPACE
  21: MODEL APIS
  6: Nvidia A100 and older chips, rented by many hosts far below launch price
  8: Single H100 GPUs by the hour, now listed by dozens of providers online
  10: Free AI models like Llama, Mistral and DeepSeek that any cloud can host
  12: Disks and file storage next to the GPUs, sold by every provider at similar prices
  14: Nvidia drivers and CUDA tools, free for any cloud that buys its chips
  16: Billing by the hour or by the second, now offered by almost every GPU cloud
  18: Space, power and cooling for standard servers, sold by many data center owners
  20: Simple ways to call a model, copied from the OpenAI format by most clouds
```

### ed102
```yaml
status: ok
title: Why has it become commoditized?
note: We see commoditization where neoclouds rent the same chips, models and tools as everyone else. New value therefore comes from power, early access to new chips, uptime and long contracts.
t:
  7: OLDER GPUS
  9: ON-DEMAND H100S
  11: OPEN MODELS
  13: STORAGE
  15: GPU DRIVERS
  17: HOURLY BILLING
  19: RACK SPACE
  21: MODEL APIS
  6: Because each new Nvidia generation makes the last one far less wanted
  8: Because supply caught up with demand and dozens of hosts bought the same chip
  10: Because Meta, Mistral and DeepSeek publish their models for free
  12: Because storage makers sell the same systems to every cloud
  14: Because Nvidia gives its software away to sell more of its chips
  16: Because marketplaces made GPU prices easy to compare in seconds
  18: Because data center builders have added huge amounts of space
  20: Because developers want to switch models without rewriting code
```

### ed103
```yaml
status: ok
title: Where is value created today?
page: 1/2
note: We derived these elements from what slows neoclouds today and from what clients and lenders pay most for. The strongest value is in power, the newest chips and clusters that do not fail.
t:
  9: "POWER AND\nLAND"
  7: Sites with grid power already secured, since a new grid connection can take several years
  12: "NEWEST\nCHIPS"
  10: Early access to the newest Nvidia systems, which rent at top prices in their first months
  17: "CLUSTER\nUPTIME"
  15: Software and teams that keep thousands of GPUs running for weeks without a single crash
```

### ed104
```yaml
status: ok
title: Where is value created today?
page: 2/2
note: We derived these elements from the largest contracts, the fastest growing inference clouds and the sovereign deals so far. Value is moving to signed demand, steady usage and trust.
t:
  9: "SIGNED\nCONTRACTS"
  7: Multiyear take-or-pay deals with strong clients, which let lenders fund the chips at lower rates
  12: "INFERENCE\nVOLUME"
  10: Steady streams of requests from many apps, which keep the GPUs busy around the clock
  17: "LOCAL\nTRUST"
  15: Clouds that governments and banks trust with data that must stay inside the country
```

### ed106-s1
```yaml
status: ok
t:
  6: VALUE CREATION
  3: GPU CLOUDS
  5: Clouds that rent GPU servers by the hour or by the month
```

### ed107-s1
```yaml
status: ok
title: Who needs it the most?
note: We focus on five groups where GPU clouds create the clearest value today. These are priority use cases, not a full list of their clients.
t:
  21: GPU CLOUDS
  5: "AI\nSTARTUPS"
  8: "RESEARCH\nLABS"
  11: "AI MODEL\nLABS"
  14: "BIG\nCLOUDS"
  17: "SOLO\nDEVELOPERS"
  7: They are young companies that need a few hundred GPUs for months, with no time to wait for a big cloud sales team
  10: They are universities and public labs that rent GPU time for a project, since they cannot buy and run their own cluster
  13: They are the big AI labs that rent extra GPUs for experiments next to the giant clusters they reserve for years
  16: They are hyperscalers that rent capacity from GPU clouds when their own new data centers run late or sell out
  19: They are single engineers who start one GPU for an afternoon to test a model and stop paying the minute they finish
```

### ed108-s1
```yaml
status: ok
title: What does "maximum customer value" look like in practice?
t:
  5: GPU CLOUDS
  10: EXCEPTIONAL CUSTOMER EXPERIENCE
  7: The team picks the newest Nvidia GPUs on a web page, starts a cluster in minutes, finds its data and tools ready, gets a clear price per hour with no surprise fees, and can grow from eight GPUs to a thousand when its model starts working.
  12: VS
  9: BAD CUSTOMER EXPERIENCE
  6: The team waits weeks for GPUs that were sold as available, finds slow storage and a broken network once the job starts, loses days of work when a server fails, and gets a bill full of fees it never saw on the price page.
```

### ed109-s1
```yaml
status: ok
title: How does the money flow in this case?
t:
  14: GPU CLOUDS
  9: "🏦\nThe cloud borrows to buy GPUs"
  7: "💻\nNvidia ships the servers"
  6: "🏢\nA data center hosts the racks"
  8: "🧑‍💻\nA team rents GPUs by the hour"
  13: "📈\nThe team grows to a bigger cluster"
  11: "📝\nIt signs a reserved contract"
  10: "💳\nThe client pays each month"
  12: "🔁\nThe cloud repays debt and buys more"
```

### ed106-s2
```yaml
status: ok
t:
  6: VALUE CREATION
  3: INFERENCE CLOUDS
  5: Clouds that run the AI models of their clients and bill by the token
```

### ed107-s2
```yaml
status: ok
title: Who needs it the most?
note: We focus on five groups where inference clouds create the clearest value today. These are priority use cases, not a full list of their clients.
t:
  21: INFERENCE CLOUDS
  5: "CODING\nAPPS"
  8: "SEARCH AND\nCHAT APPS"
  11: "IMAGE AND\nVIDEO APPS"
  14: "LARGE\nCOMPANIES"
  17: "AI AGENT\nBUILDERS"
  7: They are tools that write code for developers and call a model thousands of times a day, where every second of delay costs users
  10: They are apps that answer questions with AI, which need fast answers at a low price per request to make money on each user
  13: They are apps that create images and videos, which run heavy models for a few seconds per request and pay for each one
  16: They are firms that run open models on their own data, and want a private endpoint without running any GPUs themselves
  19: They are teams building agents that call models in long chains, where a slow or costly step breaks the whole task
```

### ed108-s2
```yaml
status: ok
title: What does "maximum customer value" look like in practice?
t:
  5: INFERENCE CLOUDS
  10: EXCEPTIONAL CUSTOMER EXPERIENCE
  7: The app switches to an open model in one line of code, gets answers in a fraction of a second, pays a clear price per million tokens, sees capacity grow on its own when traffic jumps, and can fine-tune the model on its own data in a day.
  12: VS
  9: BAD CUSTOMER EXPERIENCE
  6: The app gets slow answers at peak hours, sees requests fail during a launch, pays for capacity it does not use at night, learns that its private data was kept for training, and spends weeks moving to another provider.
```

### ed109-s2
```yaml
status: ok
title: How does the money flow in this case?
t:
  14: INFERENCE CLOUDS
  9: "🧠\nA lab publishes an open model"
  7: "⚙️\nThe cloud tunes it to run fast"
  6: "📱\nAn app calls the model by API"
  8: "🪙\nEach request is billed by token"
  13: "📈\nApp traffic grows every month"
  11: "🖥️\nThe cloud adds GPUs to keep up"
  10: "💳\nThe app pays its monthly bill"
  12: "🔁\nVolume lowers the cost per token"
```

### ed106-s3
```yaml
status: ok
t:
  6: VALUE CREATION
  3: COMPUTE MARKETPLACES
  5: Platforms that rent out spare GPUs of other hosts to their clients
```

### ed107-s3
```yaml
status: ok
title: Who needs it the most?
note: We focus on five groups where compute marketplaces create the clearest value today. These are priority use cases, not a full list of their users.
t:
  21: COMPUTE MARKETPLACES
  5: "PRICE\nHUNTERS"
  8: "SHORT-TERM\nRENTERS"
  11: "GPU\nOWNERS"
  14: "YOUNG\nSTARTUPS"
  17: "STUDENTS AND\nHOBBYISTS"
  7: They are teams that compare offers from many providers in one place and always book the cheapest GPU that fits the job
  10: They are teams that need a big cluster for a few days or weeks only, a deal most providers refuse to sign
  13: They are data centers and former crypto miners with idle GPUs, who earn money by renting them out to strangers
  16: They are young companies that cannot sign a long contract yet, but need real GPUs on short notice
  19: They are learners and hobbyists who rent a cheap GPU for a few hours to train or test small models
```

### ed108-s3
```yaml
status: ok
title: What does "maximum customer value" look like in practice?
t:
  5: COMPUTE MARKETPLACES
  10: EXCEPTIONAL CUSTOMER EXPERIENCE
  7: The team sees live prices from dozens of providers, books a tested cluster for exactly two weeks, gets the same tools and support whatever host runs it, pays one bill, and can sell back the hours it does not use to another team.
  12: VS
  9: BAD CUSTOMER EXPERIENCE
  6: The team books the cheapest GPU on the list, finds it shared with others and far slower than promised, loses its data when the host goes offline, and cannot get anyone to answer because the platform only matches buyers and sellers.
```

### ed109-s3
```yaml
status: ok
title: How does the money flow in this case?
t:
  14: COMPUTE MARKETPLACES
  9: "🏭\nA host lists its spare GPUs"
  7: "🔍\nThe platform tests and rates them"
  6: "📊\nBuyers compare live prices"
  8: "📅\nA team books hours or weeks"
  13: "🔁\nThe team books again next month"
  11: "💳\nThe buyer pays the platform"
  10: "💵\nThe host gets most of the price"
  12: "💰\nThe platform keeps its fee"
```

### ed106-s4
```yaml
status: ok
t:
  6: VALUE CREATION
  3: DEDICATED CLUSTERS
  5: Whole clusters built and reserved for one big client for years
```

### ed107-s4
```yaml
status: ok
title: Who needs it the most?
note: We focus on five groups where dedicated clusters create the clearest value today. These are priority use cases, not a full list of their clients.
t:
  21: DEDICATED CLUSTERS
  5: "FRONTIER\nLABS"
  8: "BIG\nCLOUDS"
  11: "BIG TECH\nGROUPS"
  14: "CHIP\nMAKERS"
  17: "BANKS AND\nFUNDS"
  7: They are labs like OpenAI and Anthropic that need tens of thousands of GPUs in one place to train their next model on time
  10: They are big clouds like Microsoft that rent whole clusters from neoclouds to serve their own clients when they lack sites
  13: They are groups like Meta that want huge capacity fast, without waiting years to build and power their own data centers
  16: They are chip makers that want their newest systems live at scale fast, and back neoclouds that buy them in bulk
  19: They are banks and funds that lend billions against GPUs, as long as a strong client has signed for years of use
```

### ed108-s4
```yaml
status: ok
title: What does "maximum customer value" look like in practice?
t:
  5: DEDICATED CLUSTERS
  10: EXCEPTIONAL CUSTOMER EXPERIENCE
  7: The lab signs for a cluster of the newest chips, gets it on the promised date, finds every server tested at full load, runs a training of several months with almost no crash, and extends the contract to a second site already powered.
  12: VS
  9: BAD CUSTOMER EXPERIENCE
  6: The cluster arrives months late because power or chips are missing, fails often once training starts at full scale, and leaves the lab paying for years of capacity while the next chip generation is already on sale.
```

### ed109-s4
```yaml
status: ok
title: How does the money flow in this case?
t:
  14: DEDICATED CLUSTERS
  9: "📝\nA lab signs a multiyear contract"
  7: "🏦\nLenders fund the GPUs against it"
  6: "⚡\nThe neocloud secures power and land"
  8: "🏗️\nThe site and cluster are built"
  13: "🔁\nThe client renews or expands"
  11: "🧪\nEvery server is tested at full load"
  10: "💳\nThe lab pays a fixed monthly fee"
  12: "💰\nThe fees repay the debt over time"
```

### ed106-s5
```yaml
status: ok
t:
  6: VALUE CREATION
  3: SOVEREIGN AI CLOUDS
  5: Clouds that keep AI chips and data inside one country or region
```

### ed107-s5
```yaml
status: ok
title: Who needs it the most?
note: We focus on five groups where sovereign AI clouds create the clearest value today. These are priority use cases, not a full list of their clients.
t:
  21: SOVEREIGN AI CLOUDS
  5: "NATIONAL\nAGENCIES"
  8: "BANKS AND\nINSURERS"
  11: "HEALTH\nSYSTEMS"
  14: "DEFENSE\nAGENCIES"
  17: "LOCAL AI\nSTARTUPS"
  7: They are ministries and public bodies that want national AI computing run under local law, not by a foreign cloud
  10: They are financial firms that must keep client data in the country and prove to regulators where it is processed
  13: They are hospitals and health systems whose patient records cannot leave the country, even to train a model
  16: They are armed forces and security services that need AI computing in sites they can inspect and control
  19: They are young local AI companies that want GPUs close to home, often paid in part by public programs
```

### ed108-s5
```yaml
status: ok
title: What does "maximum customer value" look like in practice?
t:
  5: SOVEREIGN AI CLOUDS
  10: EXCEPTIONAL CUSTOMER EXPERIENCE
  7: The agency rents the newest GPUs in a local site run under local law, gets proof of where every file sits and who can see it, pays prices close to the big clouds, and lets local firms and researchers use the same capacity.
  12: VS
  9: BAD CUSTOMER EXPERIENCE
  6: The country pays for a national AI cloud built on older chips, finds that a foreign group still controls the software, sees few local firms use it, and ends up paying a high price for GPUs that sit idle most of the day.
```

### ed109-s5
```yaml
status: ok
title: How does the money flow in this case?
t:
  14: SOVEREIGN AI CLOUDS
  9: "🏛️\nA state launches an AI plan"
  7: "📝\nIt picks a local cloud partner"
  6: "🏦\nPublic and private funds pay for chips"
  8: "🏢\nThe cloud builds a local site"
  13: "🔁\nThe state renews its program"
  11: "🧑‍💻\nLocal firms rent the GPUs"
  10: "💳\nAgencies pay for their usage"
  12: "📈\nThe cloud adds capacity over time"
```

### ed106-s6
```yaml
status: ok
t:
  6: VALUE CREATION
  3: TRAINING PLATFORMS
  5: Platforms that bundle computing and tools to train AI models
```

### ed107-s6
```yaml
status: ok
title: Who needs it the most?
note: We focus on five groups where training platforms create the clearest value today. These are priority use cases, not a full list of their clients.
t:
  21: TRAINING PLATFORMS
  5: "ML\nENGINEERS"
  8: "COMPANY\nDATA TEAMS"
  11: "AI\nSTARTUPS"
  14: "RESEARCH\nGROUPS"
  17: "TEACHERS AND\nSTUDENTS"
  7: They are engineers who want to fine-tune a model on their data in one place, without setting up servers, drivers and storage
  10: They are teams inside large firms that want to adapt open models to their own work, with tools their IT team can approve
  13: They are young companies that train their own small models and need GPUs, tracking and tools for a few months at a time
  16: They are scientists who run many experiments and want to compare results and share them, with GPUs one click away
  19: They are schools and courses that need a simple place where many learners can train models on real GPUs
```

### ed108-s6
```yaml
status: ok
title: What does "maximum customer value" look like in practice?
t:
  5: TRAINING PLATFORMS
  10: EXCEPTIONAL CUSTOMER EXPERIENCE
  7: The engineer uploads data, picks an open model, starts a fine-tuning run on GPUs that appear in a minute, follows the results live, and sends the new model to production on the same platform with one click and a clear bill.
  12: VS
  9: BAD CUSTOMER EXPERIENCE
  6: The engineer spends days setting up drivers and storage, waits for GPUs that are never free, loses a run when a server stops, and finds the trained model cannot be moved out of the platform without starting again.
```

### ed109-s6
```yaml
status: ok
title: How does the money flow in this case?
t:
  14: TRAINING PLATFORMS
  9: "🧑‍💻\nAn engineer opens a free account"
  7: "📦\nThe team uploads its own data"
  6: "🧠\nIt picks an open model to adapt"
  8: "⚙️\nA run starts on rented GPUs"
  13: "🔁\nThe team retrains each month"
  11: "🚀\nThe model goes live from there"
  10: "💳\nThe team pays a plan and usage"
  12: "📈\nIt moves to a bigger yearly plan"
```
