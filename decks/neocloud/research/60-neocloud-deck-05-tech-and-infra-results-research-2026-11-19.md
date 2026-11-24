### ed087
```yaml
status: ok
title: What are the tech and infra layers?
section: Tech and infra
page: 1/2
t:
  7: GPUS
  10: Special AI chips do the math for model training and inference inside rented servers
  9: NETWORKS
  11: Very fast links let many GPUs work on one AI model without waiting on each other
  21: LAYERS
  12: STORAGE
  14: Shared storage feeds huge datasets and saves checkpoints when long jobs pause
  13: SCHEDULER
  15: Cloud software reserves GPUs, starts jobs and keeps customers from clashing
note: We use specialist cloud products and independent cluster tests to define the first four technology layers.
sources:
- claim: network and storage criteria
  url: https://clustermax.semianalysis.com/criteria
  date: undated
  quote: ClusterMAX evaluates GPU cloud providers across 10 critical dimensions.
- claim: GPU instance offering
  url: https://www.crusoe.ai/cloud/pricing
  date: undated
  quote: Flexible pricing for every workload
- claim: compute orchestration
  url: https://modal.com/products/inference
  date: undated
  quote: Deploy fully managed endpoints or take advantage of low-level primitives to build, serve, and scale inference however your workload demands.
```

### ed088
```yaml
status: ok
title: What are the tech and infra layers?
section: Tech and infra
page: 2/2
t:
  7: POWER
  10: Utility power, cooling and backup systems must keep dense GPU racks running all day
  9: HEALTH
  11: Health checks detect failed GPUs and weak network links before they spoil a run
  21: LAYERS
  12: CONTROL
  14: Cloud tools give users access, security rules and clear ways to scale each job
  13: BILLING
  15: Usage meters turn rented GPU hours or served model requests into customer bills
note: We separate physical site needs from operating software and commercial metering, using public cloud product and test criteria.
sources:
- claim: power and dense racks
  url: https://www.iea.org/reports/key-questions-on-energy-and-ai/executive-summary
  date: '2026-04-16'
  quote: Electricity consumption from AI-focused data centres grows much faster than overall data centre electricity consumption, tripling in this period.
- claim: monitoring and lifecycle testing
  url: https://clustermax.semianalysis.com/criteria
  date: undated
  quote: ClusterMAX evaluates GPU cloud providers across 10 critical dimensions.
- claim: hourly and token billing
  url: https://www.crusoe.ai/cloud/pricing
  date: undated
  quote: Flexible pricing for every workload
```

### ed089
```yaml
status: ok
title: Does every layer carry the same weight?
section: Tech and infra
t:
  38: RANKING
  6: POWER
  14: Sets the live compute ceiling. Without enough electricity, purchased GPUs sit idle
  7: GPU FLEET
  24: Sets what workloads the cloud can sell and how quickly its hardware becomes old
  8: NETWORKS
  26: Keeps large training jobs fast by moving data between thousands of linked chips
  9: UPTIME
  28: Finds broken nodes before they waste expensive model training time or lose clients
  10: SOFTWARE
  30: Lets customers start, scale and manage work instead of wiring every GPU by hand
  11: STORAGE
  32: Feeds jobs at high speed and protects saved model work during failures
  12: COOLING
  34: Keeps crowded racks in safe ranges as each new chip uses more electricity
  13: BILLING
  36: Turns capacity and token use into paid revenue, with clear prices and terms
note: We rank enabling layers by their effect on saleable compute, cluster uptime and deployment schedules. The order is analytical, not a measured score.
sources:
- claim: power constraints
  url: https://www.iea.org/news/data-centre-electricity-use-surged-in-2025-even-with-tightening-bottlenecks-driving-a-scramble-for-solutions
  date: '2026-04-16'
  quote: Electricity demand from data centres soared by 17% in 2025, and that of AI-focused data centres climbed even faster
- claim: GPU cloud test criteria
  url: https://clustermax.semianalysis.com/criteria
  date: undated
  quote: ClusterMAX evaluates GPU cloud providers across 10 critical dimensions.
- claim: hardware age
  url: https://s205.q4cdn.com/133937190/files/doc_financials/2025/q4/CoreWeave-Inc-FY25-10-K-7.pdf
  date: '2026-03-02'
  quote: Technology equipment | 6 years
- claim: billing mechanics
  url: https://www.crusoe.ai/cloud/pricing
  date: undated
  quote: Flexible pricing for every workload
```

### ed090
```yaml
status: ok
title: Where does 80% of neocloud value sit?
section: Tech and infra
t:
  9: "💰 💰 💰 💰 💰 💰 💰 💰 💰\n💰 💰 💰 💰 💰 💰 💰 💰 💰\n💰 💰 💰 💰 💰 💰 💰 💰 💰\n💰 💰 💰 💰 💰 💰 💰 💰 💰\n💰 💰 💰 💰 💰 💰 💰 💰 💰\n💰 💰 💰 💰 💰 💰 💰 💰 💰\n💰 💰 💰 💰 💰 💰 💰 💰 💰\n💰 💰 💰 💰 💰 💰 💰 💰 💰\n\n💰 💰 💰 💰 💰 💰 💰 💰 💰\n💰 💰 💰 💰 💰 💰 💰 💰 💰"
  8: 'Most value sits where scarce power, usable GPUs and a stable cloud platform meet. An idle chip earns no rent, even when it is the newest model.


    Fast links and health checks matter next. A slow or broken part can waste time across a large training job, not just one server.


    Inference adds a different prize: software that routes each user request to an available chip and bills for actual use. This is an illustrative ranking, not a measured value split.'
note: We place the most weight on delivered, billable compute and operating quality. The 80% framing is illustrative, not an audited value split.
sources:
- claim: power bottlenecks
  url: https://www.iea.org/news/data-centre-electricity-use-surged-in-2025-even-with-tightening-bottlenecks-driving-a-scramble-for-solutions
  date: '2026-04-16'
  quote: Electricity demand from data centres soared by 17% in 2025, and that of AI-focused data centres climbed even faster
- claim: reliability criteria
  url: https://clustermax.semianalysis.com/criteria
  date: undated
  quote: ClusterMAX evaluates GPU cloud providers across 10 critical dimensions.
- claim: compute and inference pricing
  url: https://www.crusoe.ai/cloud/pricing
  date: undated
  quote: Flexible pricing for every workload
- claim: contract-backed assets
  url: https://lambda.com/blog/lambda-closes-1-billion-senior-secured-fixed-rate-financing
  date: '2026-10-01'
  quote: The financing is backed by contracted cash flows from two hyperscale customers
```

### ed091
```yaml
status: ok
title: How has tech and infra evolved over the years?
section: Tech and infra
t:
  6: '2017 - 2020


    Special GPU clouds began by pooling graphics cards and basic servers. CoreWeave launched a cloud platform in 2020.'
  7: '2021 - 2023


    Bigger models needed linked GPUs. Cloud firms added H100 clusters, storage and tools to book whole fleets.'
  8: '2024 - 2025


    H200 and Blackwell reached cloud customers. Specialist operators began pairing hardware with stronger service layers.'
  9: 'TODAY


    Vera Rubin now runs production cloud jobs, while more GPU purchases are funded by the cash flows of signed deals.'
  10: '?


    Next, clouds may pair faster inference chips, smarter job routing and local power solutions, while sites grow denser.'
note: We trace commercial cloud launches and production hardware, rather than chip announcements that have not reached paying customers.
sources:
- claim: 2020 platform
  url: https://d18rn0p25nwr6d.cloudfront.net/CIK-0001769628/6aa70dc1-592c-44f2-aeae-a78d51a52fe7.pdf
  date: 2025-03
  quote: Launched CoreWeave Cloud Platform, delivered as a Serverless Kubernetes Service
- claim: Blackwell availability
  url: https://investors.coreweave.com/news/news-details/2025/CoreWeave-Launches-NVIDIA-GB200-Grace-Blackwell-Systems-at-Scale/default.aspx
  date: '2025-04-15'
  quote: Cohere, IBM and Mistral AI are the first customers to gain access to NVIDIA GB200 NVL72 rack-scale systems
- claim: Rubin production
  url: https://coreweave.com/news/coreweave-delivers-nvidia-vera-rubin-nvl72-performance-at-production-scale-starting-with-cognition
  date: '2026-09-30'
  quote: with Cognition as the first customer anywhere running production workloads on the system.
- claim: GPU financing
  url: https://lambda.com/blog/lambda-closes-1-billion-senior-secured-fixed-rate-financing
  date: '2026-10-01'
  quote: The financing is backed by contracted cash flows from two hyperscale customers
- claim: density increase
  url: https://www.iea.org/reports/key-questions-on-energy-and-ai/executive-summary
  date: '2026-04-16'
  quote: Electricity consumption from AI-focused data centres grows much faster than overall data centre electricity consumption, tripling in this period.
```

### ed092
```yaml
status: ok
title: What were the latest tech and infra developments?
section: Tech and infra
page: 1/2
t:
  13: '2023'
  14: CoreWeave deployed H100 cloud clusters and raised $2.3B in private debt, showing that fast GPU access could draw major credit
  15: '2024'
  16: CoreWeave brought H200 GPUs into commercial cloud use, offering a faster generation for large model workloads
  17: '2025'
  18: CoreWeave launched GB200 cloud systems for IBM, Cohere and Mistral, opening a new class of large connected racks to users
  19: '2025'
  20: Cerebras announced six inference data centers, including owned sites in Oklahoma City and Montreal, to scale its hosted cloud
  21: '2025'
  22: Nscale and Microsoft committed to an AI campus in Loughton, UK, showing sovereign capacity can be booked before opening
  23: '2025'
  24: Fireworks AI raised $250M for production inference, as hosted model execution became its own cloud product
note: We selected hardware firsts, commercially backed AI clusters and inference infrastructure announcements with clear named operators.
sources:
- claim: 2023 H100 and debt
  url: https://d18rn0p25nwr6d.cloudfront.net/CIK-0001769628/6aa70dc1-592c-44f2-aeae-a78d51a52fe7.pdf
  date: 2025-03
  quote: Launched CoreWeave Cloud Platform, delivered as a Serverless Kubernetes Service
- claim: 2025 GB200 customers
  url: https://investors.coreweave.com/news/news-details/2025/CoreWeave-Launches-NVIDIA-GB200-Grace-Blackwell-Systems-at-Scale/default.aspx
  date: '2025-04-15'
  quote: Cohere, IBM and Mistral AI are the first customers to gain access to NVIDIA GB200 NVL72 rack-scale systems
- claim: inference cloud expansion
  url: https://www.cerebras.ai/press-release/cerebras-announces-six-new-ai-datacenters-across-north-america-and-europe-to-deliver-industry-s
  date: '2025-03-11'
  quote: The Oklahoma City and Montreal datacenters house AI hardware exclusively owned and operated by Cerebras.
- claim: Microsoft campus
  url: https://www.nscale.com/press-releases/nscale-uk-ai-infrastructure-announcement
  date: '2025-09-16'
  quote: Nscale and Microsoft are today announcing they have entered a commitment on Nscale’s AI Campus in Loughton
- claim: inference funding
  url: https://fireworks.ai/news/fireworks-ai-raises-250m-series-c
  date: '2025-10-28'
  quote: Fireworks AI, the AI inference cloud powering production AI applications for companies like Uber, Genspark, and Shopify
```

### ed093
```yaml
status: ok
title: What were the latest tech and infra developments?
section: Tech and infra
page: 2/2
t:
  13: '2026'
  14: CoreWeave announced its first operational Vera Rubin rack in June after system-level tests of the new cloud architecture
  15: '2026'
  16: Nscale expanded its Narvik plan with Microsoft to add more than 30,000 Rubin GPUs on a 230 MW AI campus in Norway
  17: '2026'
  18: IREN delivered a 50 MW liquid-cooled GPU site to Microsoft at Childress, the first tranche in a much larger agreement
  19: '2026'
  20: CoreWeave said Cognition was using Vera Rubin in production in September, moving a new chip generation beyond lab checks
  21: '2026'
  22: Nebius said the shift from temporary to permanent power in New Jersey delayed delivery of some Microsoft capacity
  23: '2026'
  24: Lambda closed $1B of fixed-rate debt tied to three customer-backed GPU deployments, extending the financing model
note: We favored physically delivered hardware, signed customer deployments and reported site constraints over announcements without execution.
sources:
- claim: Rubin system validation
  url: https://www.coreweave.com/news/coreweave-completes-industry-first-bring-up-of-nvidia-vera-rubin-nvl72
  date: '2026-06-01'
  quote: The milestone achievement includes the completion of rigorous system-level validation for the entire rack scale architecture.
- claim: Narvik campus expansion
  url: https://www.nscale.com/press-releases/nscale-microsoft-norway
  date: '2026-04-14'
  quote: the 230 MW Nscale Narvik campus will add more than 30,000 NVIDIA Rubin GPUs in deployment
- claim: Horizon 1 live
  url: https://iren.gcs-web.com/news-releases/news-release-details/iren-reports-fy26-results
  date: '2026-08-27'
  quote: Horizon 1 delivered to Microsoft
- claim: September production
  url: https://coreweave.com/news/coreweave-delivers-nvidia-vera-rubin-nvl72-performance-at-production-scale-starting-with-cognition
  date: '2026-09-30'
  quote: with Cognition as the first customer anywhere running production workloads on the system.
- claim: power delays
  url: https://assets.nebius.com/assets/721c566e-9ba5-4935-ad24-b1209116a4cc/Nebius-SHL-2026-Q3.pdf?cache-buster=2026-11-12T13%3A19%3A39.055Z
  date: '2026-11-12'
  quote: In New Jersey, we now expect to have delivered more than half of the capacity contracted with Microsoft by the end of the year
- claim: financing
  url: https://lambda.com/blog/lambda-closes-1-billion-senior-secured-fixed-rate-financing
  date: '2026-10-01'
  quote: The financing is backed by contracted cash flows from two hyperscale customers
```

### ed094
```yaml
status: ok
title: What are the solvable bottlenecks?
section: Tech and infra
t:
  39: BOTTLENECK
  38: EXPLANATION
  41: BOTTLENECK
  40: EXPLANATION
  7: GRID POWER
  5: Cloud operators can book GPUs long before power is ready to run them at a site
  24: FAST LINKS
  22: Slow links between GPU racks make large model jobs wait instead of doing useful work
  11: GPU SUPPLY
  9: Advanced chips and server parts are scarce when the same generation launches
  28: GPU FINANCE
  26: Buying GPU fleets before billing clients ties up vast amounts of cash
  15: RACK HEAT
  13: Dense new racks need better liquid cooling and electrical designs to stay safe
  32: CHIP AGING
  30: Each chip generation can lower the value of older hourly rental fleets
  19: CHIP FAULTS
  17: A failed chip can stall a large model run, so faults must be found and fixed fast
  36: DATA RULES
  34: A client may need local data handling rules before buying remote cloud compute
note: We selected technical constraints seen in operator deployments and cloud benchmark criteria, rather than unsolved chip design alone.
sources:
- claim: grid and equipment
  url: https://www.iea.org/news/data-centre-electricity-use-surged-in-2025-even-with-tightening-bottlenecks-driving-a-scramble-for-solutions
  date: '2026-04-16'
  quote: Electricity demand from data centres soared by 17% in 2025, and that of AI-focused data centres climbed even faster
- claim: network and reliability
  url: https://clustermax.semianalysis.com/criteria
  date: undated
  quote: ClusterMAX evaluates GPU cloud providers across 10 critical dimensions.
- claim: GPU financing
  url: https://lambda.com/blog/lambda-closes-1-billion-senior-secured-fixed-rate-financing
  date: '2026-10-01'
  quote: The financing is backed by contracted cash flows from two hyperscale customers
- claim: hardware life
  url: https://s205.q4cdn.com/133937190/files/doc_financials/2025/q4/CoreWeave-Inc-FY25-10-K-7.pdf
  date: '2026-03-02'
  quote: Technology equipment | 6 years
- claim: remote access
  url: https://www.bis.gov/press-release/bis-issues-rule-addressing-remote-access-american-super-intelligence-technology
  date: '2026-11-16'
  quote: to address remote access to advanced super intelligence (SI) chips and servers.
- claim: power commissioning
  url: https://assets.nebius.com/assets/721c566e-9ba5-4935-ad24-b1209116a4cc/Nebius-SHL-2026-Q3.pdf?cache-buster=2026-11-12T13%3A19%3A39.055Z
  date: '2026-11-12'
  quote: In New Jersey, we now expect to have delivered more than half of the capacity contracted with Microsoft by the end of the year
```

### ed095
```yaml
status: ok
title: Why can’t we solve them yet?
section: Tech and infra
t:
  39: BOTTLENECK
  38: EXPLANATION
  41: BOTTLENECK
  40: EXPLANATION
  7: GRID POWER
  5: Grid queues, new substations and large transformers all have long lead times
  24: FAST LINKS
  22: Network switches, fiber layout and software must all work at once across racks
  11: GPU SUPPLY
  9: Large labs and clouds compete for the same top chips and system supply chains
  28: GPU FINANCE
  26: GPU debt needs bankable buyers, useful collateral and firm delivery dates
  15: RACK HEAT
  13: Heat rises sharply when dense racks draw more power from each small floor area
  32: CHIP AGING
  30: A newer chip may run more work per dollar while the old chip still has book value
  19: CHIP FAULTS
  17: One bad link or GPU can break a large job, and shared clusters have many parts
  36: DATA RULES
  34: Exports and data rules differ, so one global fleet cannot serve all buyers
note: We tie each persistent bottleneck to equipment lead times, cluster interdependence, financing and cross-border requirements.
sources:
- claim: grid and equipment
  url: https://www.iea.org/news/data-centre-electricity-use-surged-in-2025-even-with-tightening-bottlenecks-driving-a-scramble-for-solutions
  date: '2026-04-16'
  quote: Electricity demand from data centres soared by 17% in 2025, and that of AI-focused data centres climbed even faster
- claim: network and reliability
  url: https://clustermax.semianalysis.com/criteria
  date: undated
  quote: ClusterMAX evaluates GPU cloud providers across 10 critical dimensions.
- claim: GPU financing
  url: https://lambda.com/blog/lambda-closes-1-billion-senior-secured-fixed-rate-financing
  date: '2026-10-01'
  quote: The financing is backed by contracted cash flows from two hyperscale customers
- claim: hardware life
  url: https://s205.q4cdn.com/133937190/files/doc_financials/2025/q4/CoreWeave-Inc-FY25-10-K-7.pdf
  date: '2026-03-02'
  quote: Technology equipment | 6 years
- claim: remote access
  url: https://www.bis.gov/press-release/bis-issues-rule-addressing-remote-access-american-super-intelligence-technology
  date: '2026-11-16'
  quote: to address remote access to advanced super intelligence (SI) chips and servers.
- claim: power commissioning
  url: https://assets.nebius.com/assets/721c566e-9ba5-4935-ad24-b1209116a4cc/Nebius-SHL-2026-Q3.pdf?cache-buster=2026-11-12T13%3A19%3A39.055Z
  date: '2026-11-12'
  quote: In New Jersey, we now expect to have delivered more than half of the capacity contracted with Microsoft by the end of the year
```

### ed096
```yaml
status: ok
title: When can we realistically expect to solve them?
section: Tech and infra
t:
  39: BOTTLENECK
  38: WHY THIS DATE
  41: BOTTLENECK
  40: WHY THIS DATE
  7: GRID POWER
  5: Grid upgrades need local approvals and heavy gear, so many projects will slip into the next decade
  24: FAST LINKS
  22: Faster links and better network tools help, yet large shared jobs still face bottlenecks
  42: '2030'
  46: '2028'
  11: GPU SUPPLY
  9: New chip supply expands with each launch, but top models will keep early scarcity
  28: GPU FINANCE
  26: Signed deals bring cheaper credit, but smaller buyers remain harder for lenders to rate
  43: '2028'
  47: '2028'
  15: RACK HEAT
  13: Liquid cooling can meet dense racks, but retrofits need trained crews and safe site tests
  32: CHIP AGING
  30: Long deals protect current cash flow, though each GPU generation resets its price risk
  44: '2028'
  48: '2029'
  19: CHIP FAULTS
  17: Fault checks improve every year, but near-perfect uptime across huge clusters is hard
  36: DATA RULES
  34: Clouds can add local zones and audits, but changing trade rules still need legal review
  45: '2029'
  49: '2030'
note: We give directional dates for meaningful improvement, not for complete removal. Hardware and local approval cycles vary widely.
sources:
- claim: grid and equipment
  url: https://www.iea.org/news/data-centre-electricity-use-surged-in-2025-even-with-tightening-bottlenecks-driving-a-scramble-for-solutions
  date: '2026-04-16'
  quote: Electricity demand from data centres soared by 17% in 2025, and that of AI-focused data centres climbed even faster
- claim: network and reliability
  url: https://clustermax.semianalysis.com/criteria
  date: undated
  quote: ClusterMAX evaluates GPU cloud providers across 10 critical dimensions.
- claim: GPU financing
  url: https://lambda.com/blog/lambda-closes-1-billion-senior-secured-fixed-rate-financing
  date: '2026-10-01'
  quote: The financing is backed by contracted cash flows from two hyperscale customers
- claim: hardware life
  url: https://s205.q4cdn.com/133937190/files/doc_financials/2025/q4/CoreWeave-Inc-FY25-10-K-7.pdf
  date: '2026-03-02'
  quote: Technology equipment | 6 years
- claim: remote access
  url: https://www.bis.gov/press-release/bis-issues-rule-addressing-remote-access-american-super-intelligence-technology
  date: '2026-11-16'
  quote: to address remote access to advanced super intelligence (SI) chips and servers.
- claim: power commissioning
  url: https://assets.nebius.com/assets/721c566e-9ba5-4935-ad24-b1209116a4cc/Nebius-SHL-2026-Q3.pdf?cache-buster=2026-11-12T13%3A19%3A39.055Z
  date: '2026-11-12'
  quote: In New Jersey, we now expect to have delivered more than half of the capacity contracted with Microsoft by the end of the year
```

### ed097
```yaml
status: ok
title: Which bold bets could reshape neocloud?
section: Tech and infra
t:
  9: GRID READY CLOUD
  12: SELF HEAL FLEETS
  15: LOCAL AI ZONES
  18: LOW COST INF
  33: 'NEAR TERM


    (0-5 YEARS)'
  7: It is reserved GPU capacity built only where grid power and cooling are already secured
  10: It is a cluster that spots slow chips and moves work before a long model run fails
  13: It is cloud compute sold in a region that meets buyer rules for data location
  16: It is hosted inference that routes each request to a chip at the lowest usable cost
  21: POWER FLEX CLOUD
  24: MULTI CHIP RUN
  27: AUTO GPU CREDIT
  30: NO IDLE GPU
  34: 'LONG TERM


    (5-10 YEARS)'
  19: It is an AI cloud that can shift jobs in time to match power supply and lower grid cost
  22: It is one service that picks different chip types for training and live inference jobs
  25: It is credit priced from each fleet real use and booked cash, not just its hardware
  28: It is a shared GPU market that fills spare slots without hurting big reserved jobs
note: We treat these as plausible technical and business bets inferred from cloud quality, pricing, chip and power trends, not promised outcomes.
sources:
- claim: power availability
  url: https://www.iea.org/news/data-centre-electricity-use-surged-in-2025-even-with-tightening-bottlenecks-driving-a-scramble-for-solutions
  date: '2026-04-16'
  quote: Electricity demand from data centres soared by 17% in 2025, and that of AI-focused data centres climbed even faster
- claim: fault detection
  url: https://clustermax.semianalysis.com/criteria
  date: undated
  quote: ClusterMAX evaluates GPU cloud providers across 10 critical dimensions.
- claim: regional rules
  url: https://www.bis.gov/press-release/bis-issues-rule-addressing-remote-access-american-super-intelligence-technology
  date: '2026-11-16'
  quote: to address remote access to advanced super intelligence (SI) chips and servers.
- claim: inference pricing
  url: https://www.crusoe.ai/cloud/pricing
  date: undated
  quote: Flexible pricing for every workload
- claim: financing mechanisms
  url: https://lambda.com/blog/lambda-closes-1-billion-senior-secured-fixed-rate-financing
  date: '2026-10-01'
  quote: The financing is backed by contracted cash flows from two hyperscale customers
- claim: special inference
  url: https://groq.com/newsroom/groq-raises-usd650m-to-scale-its-ai-inference-cloud-business
  date: '2026-06-22'
  quote: Groq today announced $650 million in new growth capital to accelerate the expansion of its AI inference cloud.
```

### ed098
```yaml
status: ok
title: Which companies are working on groundbreaking tech today?
section: Tech and infra
t:
  8: COREWEAVE
  6: They run large Nvidia GPU clusters with tools built to keep AI training stable
  24: NEBIUS
  22: They sell full AI cloud capacity and reserve huge multi-year fleets for Meta
  11: IREN
  9: They turn powered sites into paid AI cloud services, with Microsoft as a buyer
  27: LAMBDA
  25: They finance and rent GPU clusters backed by committed cloud customers
  14: CRUSOE
  12: They combine rented GPU instances with managed model inference services
  30: GROQ
  28: They run fast cloud inference on their own LPU chips instead of only GPUs
  17: CEREBRAS
  15: They sell hosted inference using wafer-scale chips in operated cloud sites
  33: FIREWORKS AI
  31: They host production inference endpoints so apps run models on remote chips
note: We include only providers offering customer-facing accelerated compute or model execution, including proprietary-chip clouds.
sources:
- claim: CoreWeave cloud
  url: https://investors.coreweave.com/news/news-details/2026/CoreWeave-Reports-Strong-Third-Quarter-2026-Results/
  date: '2026-11-10'
  quote: Revenue backlog was approximately $132.5 billion as of September 30, 2026.
- claim: Nebius dedicated clusters
  url: https://nebius.com/newsroom/nebius-signs-new-ai-infrastructure-agreement-with-meta
  date: '2026-03-16'
  quote: Under the five-year agreement, Nebius will provide $12 billion of dedicated capacity across multiple locations
- claim: IREN GPU service
  url: https://www.sec.gov/Archives/edgar/data/1878848/000187884826000052/iren-20260630.htm
  date: '2026-08-27'
  quote: The total contract value is approximately $9.7 billion through 2031
- claim: Lambda debt backed cloud
  url: https://lambda.com/blog/lambda-closes-1-billion-senior-secured-fixed-rate-financing
  date: '2026-10-01'
  quote: The financing is backed by contracted cash flows from two hyperscale customers
- claim: Crusoe services
  url: https://www.crusoe.ai/cloud/pricing
  date: undated
  quote: Flexible pricing for every workload
- claim: Groq inference cloud
  url: https://groq.com/newsroom/groq-raises-usd650m-to-scale-its-ai-inference-cloud-business
  date: '2026-06-22'
  quote: Groq today announced $650 million in new growth capital to accelerate the expansion of its AI inference cloud.
- claim: Cerebras inference
  url: https://www.cerebras.ai/press-release/cerebras-launches-the-worlds-fastest-ai-inference
  date: '2024-08-27'
  quote: Today, Cerebras Systems, the pioneer in high performance AI compute, announced Cerebras Inference
- claim: Fireworks inference
  url: https://fireworks.ai/news/fireworks-ai-raises-250m-series-c
  date: '2025-10-28'
  quote: Fireworks AI, the AI inference cloud powering production AI applications for companies like Uber, Genspark, and Shopify
logos:
- name: CoreWeave
  domain: coreweave.com
- name: Nebius
  domain: nebius.com
- name: IREN
  domain: iren.com
- name: Lambda
  domain: lambda.com
- name: Crusoe
  domain: crusoe.ai
- name: Groq
  domain: groq.com
- name: Cerebras
  domain: cerebras.ai
- name: Fireworks AI
  domain: fireworks.ai
comment: IREN is a publicly listed legacy mining operator transitioning toward customer-facing AI cloud services. It is included as BORDERLINE, not treated as an independent startup.
```

### iv_pipeline
```yaml
status: ok
title: Which big AI clusters are neoclouds building right now?
section: Tech and infra
t:
  38: LIVE
  34: Childress, United States. Microsoft accepted a 50 MW GPU hall.
  37: IREN · MICROSOFT
  27: LIVE
  26: IREN · GPU CLOUD
  24: Prince George, Canada. Its GPUs are live or in final setup.
  23: BUILD
  22: IREN · GPU CLOUD
  20: Mackenzie, Canada. The 80 MW site was readied for GPU installs in 2026.
  19: BUILD
  18: NSCALE · MICROSOFT
  16: Narvik, Norway. The 230 MW campus will serve Microsoft.
  15: PLAN
  12: Loughton, United Kingdom. Microsoft booked an AI cloud site.
  14: NSCALE · MICROSOFT
  11: LIVE
  10: CRUSOE · ORACLE
  8: Abilene, United States. The first AI campus phase went live for Oracle.
  7: LIVE
  6: CEREBRAS · INFERENCE
  4: Oklahoma City, United States. Cerebras runs inference here.
  3: LIVE
  2: CEREBRAS · INFERENCE
  0: Montreal, Canada. Cerebras runs an owned inference site.
note: We list eight named facilities with signed buyers, reported construction or operating compute. Planned megawatts are not described as live.
sources:
- claim: Childress Microsoft handoff
  url: https://iren.gcs-web.com/news-releases/news-release-details/iren-reports-fy26-results
  date: '2026-08-27'
  quote: Horizon 1 delivered to Microsoft
- claim: Prince George and Mackenzie
  url: https://www.sec.gov/Archives/edgar/data/1878848/000187884826000028/irentranscript.htm
  date: 2026-05
  quote: At Prince George, all air-cooled GPUs have now been delivered and are either operating or undergoing commissioning
- claim: Narvik Microsoft campus
  url: https://www.nscale.com/press-releases/nscale-microsoft-norway
  date: '2026-04-14'
  quote: the 230 MW Nscale Narvik campus will add more than 30,000 NVIDIA Rubin GPUs in deployment
- claim: Loughton commitment
  url: https://www.nscale.com/press-releases/nscale-uk-ai-infrastructure-announcement
  date: '2025-09-16'
  quote: Nscale and Microsoft are today announcing they have entered a commitment on Nscale’s AI Campus in Loughton
- claim: live Abilene campus
  url: https://www.crusoe.ai/resources/newsroom/crusoe-announces-flagship-abilene-data-center-is-live
  date: '2025-09-30'
  quote: the first phase of Stargate’s flagship data center campus in Abilene, Texas, is now up and running on Oracle Cloud Infrastructure
- claim: Oklahoma City and Montreal inference sites
  url: https://www.cerebras.ai/press-release/cerebras-announces-six-new-ai-datacenters-across-north-america-and-europe-to-deliver-industry-s
  date: '2025-03-11'
  quote: The Oklahoma City and Montreal datacenters house AI hardware exclusively owned and operated by Cerebras.
```
