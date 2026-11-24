# AI data center | Tech and infra | research slides | 22 November 2026

### ed087
```yaml
status: ok
section: Tech and infra
title: What are the tech and infra layers?
page: 1/2
t:
  7: POWER
  10: A grid connection and firm electric supply turn a site into a usable AI campus.
  9: COOLING
  11: Liquid loops carry heat away from dense GPU racks that air alone cannot cool well.
  21: LAYERS
  12: NETWORK
  14: Fast fiber links AI halls to users and lets servers exchange data at speed.
  13: BUILDINGS
  15: Purpose-built halls fit heavy racks, coolant pipes and space for upgrades.
note: We group the physical systems that make rented AI capacity usable, from power and cooling to site design and fiber links.
sources:
- claim: Transmission line construction can take four to eight years
  url: https://www.iea.org/reports/energy-and-ai/executive-summary
  date: '2025-04-10'
  quote: Building new transmission lines can take four to eight years in advanced economies
- claim: GB200 NVL72 racks use direct liquid cooling for 120 kW heat loads
  url: https://developer.nvidia.com/blog/?p=90182
  date: '2024-10-15'
  quote: To efficiently manage the 120 KW cooling capacity required for the rack, we’ve implemented direct liquid cooling
    techniques.
- claim: Grid availability constrains global data center projects
  url: https://www.cbre.com/insights/reports/global-data-center-trends-2026
  date: '2026-06-17'
  quote: Global power availability and grid infrastructure constraints are impacting development timelines and site selection
```

### ed088
```yaml
status: ok
section: Tech and infra
title: What are the tech and infra layers?
page: 2/2
t:
  7: BACKUP
  10: Batteries smooth sudden load jumps and protect the racks during outages.
  9: POWER GEAR
  11: Substations and switches turn grid supply into safe power for each rack.
  21: LAYERS
  12: MODULES
  14: Factory-built halls cut site work, but still need power and fiber nearby.
  13: OPERATE
  15: Sensors and skilled teams keep power and cooling stable once halls open.
note: We separate equipment that delivers electricity from backup systems, factory builds and the daily work of keeping halls
  available.
sources:
- claim: AI workloads produce sudden swings in power demand
  url: https://www.iea.org/reports/key-questions-on-energy-and-ai/executive-summary
  date: '2026-04-16'
  quote: Unlike traditional data centre operations, AI training and model use induce large and rapid power swings
- claim: Transformer and cable wait times doubled over three years
  url: https://www.iea.org/reports/energy-and-ai/executive-summary
  date: '2025-04-10'
  quote: wait times for critical grid components such as transformers and cables have doubled in the past three years.
- claim: Crusoe introduced modular liquid-cooled units supporting 3.5 MW
  url: https://www.crusoe.ai/resources/newsroom/crusoe-introduces-crusoe-spark-liquid
  date: '2026-10-21'
  quote: Crusoe Spark Liquid delivers high-efficiency DLC closed-loop cooling to support up to 3.5MW of compute per unit.
- claim: Operators face power, staffing and equipment supply shortages
  url: https://uptimeinstitute.com/resources/research-and-reports/uptime-institute-global-data-center-survey-results-2026
  date: '2026-07-27'
  quote: operators must navigate challenges such as limited power availability, falling grid reliability, rising costs, supply
    chain limits and staffing shortages.
```

### ed089
```yaml
status: ok
section: Tech and infra
title: Does every layer carry the same weight?
t:
  38: RANKING
  6: POWER
  14: A signed power path decides whether a site opens, the first gate to useful capacity.
  7: POWER GEAR
  24: Long waits for substations and transformers can hold up even a fully leased campus.
  8: COOLING
  26: Liquid cooling decides which dense AI racks a new hall can safely accept and run.
  9: NETWORK
  28: Fast fiber makes powered sites practical for large AI jobs and remote clients.
  10: BUILDINGS
  30: Flexible hall layouts let a landlord adapt to new chips and higher power use.
  11: BACKUP
  32: Batteries guard uptime when large GPU clusters cause sharp power jumps.
  12: MODULES
  34: Prefabricated units can speed up delivery after land, permits and power are ready.
  13: OPERATE
  36: Staff and controls protect service quality after construction turns into daily use.
comment: The rank is qualitative and does not represent measured shares of economic value.
note: We rank the layers by their likely effect on whether AI capacity can be leased and put into use. This is a judgment,
  not an audited score.
sources:
- claim: Grid availability constrains global data center projects
  url: https://www.cbre.com/insights/reports/global-data-center-trends-2026
  date: '2026-06-17'
  quote: Global power availability and grid infrastructure constraints are impacting development timelines and site selection
- claim: Transformer and cable wait times doubled over three years
  url: https://www.iea.org/reports/energy-and-ai/executive-summary
  date: '2025-04-10'
  quote: wait times for critical grid components such as transformers and cables have doubled in the past three years.
- claim: GB200 NVL72 racks use direct liquid cooling for 120 kW heat loads
  url: https://developer.nvidia.com/blog/?p=90182
  date: '2024-10-15'
  quote: To efficiently manage the 120 KW cooling capacity required for the rack, we’ve implemented direct liquid cooling
    techniques.
- claim: AI workloads produce sudden swings in power demand
  url: https://www.iea.org/reports/key-questions-on-energy-and-ai/executive-summary
  date: '2026-04-16'
  quote: Unlike traditional data centre operations, AI training and model use induce large and rapid power swings
- claim: Crusoe introduced modular liquid-cooled units supporting 3.5 MW
  url: https://www.crusoe.ai/resources/newsroom/crusoe-introduces-crusoe-spark-liquid
  date: '2026-10-21'
  quote: Crusoe Spark Liquid delivers high-efficiency DLC closed-loop cooling to support up to 3.5MW of compute per unit.
- claim: Operators face power, staffing and equipment supply shortages
  url: https://uptimeinstitute.com/resources/research-and-reports/uptime-institute-global-data-center-survey-results-2026
  date: '2026-07-27'
  quote: operators must navigate challenges such as limited power availability, falling grid reliability, rising costs, supply
    chain limits and staffing shortages.
```

### ed090
```yaml
status: ok
section: Tech and infra
title: Where does 80% of AI data center value sit?
t:
  9: "\U0001F4B0 \U0001F4B0 \U0001F4B0 \U0001F4B0 \U0001F4B0 \U0001F4B0 \U0001F4B0 \U0001F4B0 \U0001F4B0\n\U0001F4B0 \U0001F4B0\
    \ \U0001F4B0 \U0001F4B0 \U0001F4B0 \U0001F4B0 \U0001F4B0 \U0001F4B0 \U0001F4B0\n\U0001F4B0 \U0001F4B0 \U0001F4B0 \U0001F4B0\
    \ \U0001F4B0 \U0001F4B0 \U0001F4B0 \U0001F4B0 \U0001F4B0\n\U0001F4B0 \U0001F4B0 \U0001F4B0 \U0001F4B0 \U0001F4B0 \U0001F4B0\
    \ \U0001F4B0 \U0001F4B0 \U0001F4B0\n\U0001F4B0 \U0001F4B0 \U0001F4B0 \U0001F4B0 \U0001F4B0 \U0001F4B0 \U0001F4B0 \U0001F4B0\
    \ \U0001F4B0\n\U0001F4B0 \U0001F4B0 \U0001F4B0 \U0001F4B0 \U0001F4B0 \U0001F4B0 \U0001F4B0 \U0001F4B0 \U0001F4B0\n\U0001F4B0\
    \ \U0001F4B0 \U0001F4B0 \U0001F4B0 \U0001F4B0 \U0001F4B0 \U0001F4B0 \U0001F4B0 \U0001F4B0\n\U0001F4B0 \U0001F4B0 \U0001F4B0\
    \ \U0001F4B0 \U0001F4B0 \U0001F4B0 \U0001F4B0 \U0001F4B0 \U0001F4B0\n\U0001F4B0 \U0001F4B0 \U0001F4B0 \U0001F4B0 \U0001F4B0\
    \ \U0001F4B0 \U0001F4B0 \U0001F4B0 \U0001F4B0\n\U0001F4B0 \U0001F4B0 \U0001F4B0 \U0001F4B0 \U0001F4B0 \U0001F4B0 \U0001F4B0\
    \ \U0001F4B0 \U0001F4B0"
  8: "A large share of a campus’s practical value is locked in its power path and its ability to cool dense AI racks. Without\
    \ both, the hall may sit empty even after it is built.\n\nNext comes safe power delivery inside the site, then fast network\
    \ access and a layout that can change as new chips arrive.\n\nThis is a priority map, not a claim that any layer captures\
    \ a measured 80% of industry revenue."
comment: The 80% in the title is a visual heuristic, not an empirical economic-value calculation.
note: We use the 80% framing to show the hardest dependencies, led by power and high-density cooling. No published study measures
  this share.
sources:
- claim: Grid availability constrains global data center projects
  url: https://www.cbre.com/insights/reports/global-data-center-trends-2026
  date: '2026-06-17'
  quote: Global power availability and grid infrastructure constraints are impacting development timelines and site selection
- claim: Transmission line construction can take four to eight years
  url: https://www.iea.org/reports/energy-and-ai/executive-summary
  date: '2025-04-10'
  quote: Building new transmission lines can take four to eight years in advanced economies
- claim: GB200 NVL72 racks use direct liquid cooling for 120 kW heat loads
  url: https://developer.nvidia.com/blog/?p=90182
  date: '2024-10-15'
  quote: To efficiently manage the 120 KW cooling capacity required for the rack, we’ve implemented direct liquid cooling
    techniques.
- claim: AI server power density rose elevenfold between 2020 and 2025
  url: https://www.iea.org/reports/key-questions-on-energy-and-ai/executive-summary
  date: '2026-04-16'
  quote: between 2020 and 2025, the power density of AI servers increased by 11 times
```

### ed091
```yaml
status: ok
section: Tech and infra
title: How has tech and infra evolved over the years?
t:
  6: "2017 - 2020\n\nOperators built power-first sites for cloud and mining. Some hosted GPUs before high-density AI became\
    \ a separate facility business."
  7: "2021 - 2023\n\nBigger AI jobs needed connected GPU rooms. Rising server power began to strain older air-cooled sites."
  8: "2024 - 2025\n\nCore Scientific signed a big AI hosting deal. Crusoe built the Abilene Stargate site, with its first\
    \ buildings live in 2025."
  9: "TODAY\n\nOperators sell firm power and liquid cooling. Galaxy and Applied Digital have delivered leased AI halls, not\
    \ just plans."
  10: "?\n\nOperators may pair on-site power, factory-built halls and water-saving cooling loops to shorten the time from\
    \ lease to use."
note: We trace the shift from general powered sites to verified AI-first campuses, using early hosting contracts and later
  delivery milestones.
sources:
- claim: Core Scientific hosted CoreWeave GPUs from 2019 through 2022
  url: https://investors.corescientific.com/news-events/press-releases/detail/74/core-scientific-to-provide-approximately-200-mw-of-infrastructure-to-host-coreweaves-high-performance-computing-services-capturing-significant-ai-compute-opportunity
  date: '2024-06-04'
  quote: From 2019 to 2022, Core Scientific hosted thousands of CoreWeave’s GPUs in its data centers.
- claim: Core Scientific signed a 200 MW hosting deal with CoreWeave
  url: https://investors.corescientific.com/news-events/press-releases/detail/74/core-scientific-to-provide-approximately-200-mw-of-infrastructure-to-host-coreweaves-high-performance-computing-services-capturing-significant-ai-compute-opportunity
  date: '2024-06-04'
  quote: Core Scientific will deliver approximately 200 megawatts (“MW”) of infrastructure to host CoreWeave’s high-performance
    compute (“HPC”) operations.
- claim: Crusoe began its Abilene AI data center build in June 2024
  url: https://www.crusoe.ai/resources/newsroom/crusoe-announces-flagship-abilene-data-center-is-live
  date: '2025-09-30'
  quote: Construction of the multi-building campus began in June 2024.
- claim: Crusoe brought phase one of the Abilene Stargate campus online
  url: https://www.crusoe.ai/resources/newsroom/crusoe-announces-flagship-abilene-data-center-is-live
  date: '2025-09-30'
  quote: the first phase of Stargate’s flagship data center campus in Abilene, Texas, is now up and running on Oracle Cloud
    Infrastructure
- claim: Applied Digital reached 250 MW of operational IT load
  url: https://ir.applieddigital.com/news-events/press-releases/detail/161/applied-digital-brings-an-additional-75-mw-of-ai
  date: '2026-10-02'
  quote: brings fully operational critical IT load at Polaris Forge 1 to 250 MW.
- claim: Galaxy delivered 133 MW of AI IT load to CoreWeave at Helios
  url: https://www.galaxy.com/newsroom/galaxy-completes-phase-i-of-its-helios-data-center-campus
  date: '2026-07-06'
  quote: 133 MW of critical IT load
- claim: AI server power density rose elevenfold between 2020 and 2025
  url: https://www.iea.org/reports/key-questions-on-energy-and-ai/executive-summary
  date: '2026-04-16'
  quote: between 2020 and 2025, the power density of AI servers increased by 11 times
- claim: Crusoe introduced modular liquid-cooled units supporting 3.5 MW
  url: https://www.crusoe.ai/resources/newsroom/crusoe-introduces-crusoe-spark-liquid
  date: '2026-10-21'
  quote: Crusoe Spark Liquid delivers high-efficiency DLC closed-loop cooling to support up to 3.5MW of compute per unit.
```

### ed092
```yaml
status: ok
section: Tech and infra
title: What were the latest tech and infra developments?
page: 1/2
t:
  13: '2024'
  14: Core Scientific signed 12-year deals with CoreWeave for 200 MW of AI hosting, so mining sites could become AI facilities.
  15: '2025'
  16: Crusoe energized two Abilene buildings, bringing Stargate GPU systems online for Oracle Cloud Infrastructure.
  17: '2025'
  18: Applied Digital signed about 15-year leases for 250 MW at Ellendale with CoreWeave, giving its first AI campus a firm
    customer.
  19: '2025'
  20: Galaxy agreed to deliver an extra 260 MW to CoreWeave at Helios, raising the AI conversion beyond the first signed phase.
  21: '2025'
  22: Nscale and Microsoft committed to the Loughton AI campus near London, linking a purpose-built UK facility to a named
    user.
  23: '2025'
  24: IREN signed a Microsoft deal covering four Horizon halls at Childress, with about 200 MW of IT load planned for GPUs.
note: We selected signed capacity contracts and sites put into service rather than treating unleased land or announced power
  targets as delivery.
sources:
- claim: Core Scientific signed a 200 MW hosting deal with CoreWeave
  url: https://investors.corescientific.com/news-events/press-releases/detail/74/core-scientific-to-provide-approximately-200-mw-of-infrastructure-to-host-coreweaves-high-performance-computing-services-capturing-significant-ai-compute-opportunity
  date: '2024-06-04'
  quote: Core Scientific will deliver approximately 200 megawatts (“MW”) of infrastructure to host CoreWeave’s high-performance
    compute (“HPC”) operations.
- claim: Crusoe brought phase one of the Abilene Stargate campus online
  url: https://www.crusoe.ai/resources/newsroom/crusoe-announces-flagship-abilene-data-center-is-live
  date: '2025-09-30'
  quote: the first phase of Stargate’s flagship data center campus in Abilene, Texas, is now up and running on Oracle Cloud
    Infrastructure
- claim: Applied Digital signed CoreWeave leases for 250 MW
  url: https://ir.applieddigital.com/news-events/press-releases/detail/123/applied-digital-announces-250mw-ai-data-center-lease-with
  date: '2025-06-02'
  quote: Applied Digital will deliver 250 megawatts (MW) of critical IT load to host CoreWeave's artificial intelligence
- claim: Galaxy signed additional CoreWeave capacity at Helios
  url: https://www.galaxy.com/newsroom/galaxy-announces-commitment-with-coreweave
  date: '2025-04-23'
  quote: Galaxy has agreed to deliver approximately 260 MW of incremental critical IT load
- claim: Nscale and Microsoft committed to the Loughton AI campus
  url: https://www.nscale.com/press-releases/nscale-uk-ai-infrastructure-announcement
  date: '2025-09-16'
  quote: Nscale and Microsoft are today announcing they have entered a commitment on Nscale’s AI Campus in Loughton
- claim: IREN contracted four GPU data halls at Childress
  url: https://www.sec.gov/Archives/edgar/data/1878848/000187884825000081/iren-20250930.htm
  date: '2025-11-07'
  quote: The GPUs will be installed across four data center facilities at Childress known as “Horizon 1,” “Horizon 2,” “Horizon
    3,” and “Horizon 4”
```

### ed093
```yaml
status: ok
section: Tech and infra
title: What were the latest tech and infra developments?
page: 2/2
t:
  13: '2026'
  14: Galaxy delivered 133 MW of critical IT power at Helios to CoreWeave, turning the former mining campus into a rent-paying
    AI facility.
  15: '2026'
  16: Core Scientific signed leases for about 530 MW with AMD and a neocloud across five sites, adding a second anchor to
    CoreWeave.
  17: '2026'
  18: IREN delivered Horizon 1 to Microsoft in August, showing that the new liquid-cooled AI halls at Childress were more
    than a power plan.
  19: '2026'
  20: Crusoe confirmed that it is building Google’s Armstrong County AI campus, using a closed-loop cooling design.
  21: '2026'
  22: Applied Digital lifted live critical IT load at Polaris Forge 1 to 250 MW, with a further 150 MW contracted to CoreWeave.
  23: '2026'
  24: Polar said its 12 MW Tørdal hall was live for Crusoe Cloud and announced a further 40 MW liquid-cooled phase for 2027.
note: We prioritize site delivery, documented tenant leases and deployed cooling, rather than confusing proposed gigawatts
  with live capacity.
sources:
- claim: Galaxy delivered 133 MW of AI IT load to CoreWeave at Helios
  url: https://www.galaxy.com/newsroom/galaxy-completes-phase-i-of-its-helios-data-center-campus
  date: '2026-07-06'
  quote: 133 MW of critical IT load
- claim: Core Scientific signed about 530 MW of new 2026 AI site leases
  url: https://investors.corescientific.com/sec-filings/all-sec-filings/content/0001839341-26-000030/core-20260930.htm
  date: '2026-11-05'
  quote: for an aggregate of approximately 530 MW of critical IT capacity across five of the Company's sites.
- claim: Microsoft accepted IREN Horizon 1 in August 2026
  url: https://www.sec.gov/Archives/edgar/data/1878848/000187884826000052/iren-20260630.htm
  date: '2026-08-28'
  quote: Horizon 1 was delivered to, and accepted by, Microsoft in August 2026.
- claim: Crusoe is developing a Google campus under construction in Texas
  url: https://www.crusoe.ai/resources/newsroom/crusoe-developing-data-center-campus-in-armstrong-county-texas
  date: '2026-09-28'
  quote: Crusoe, the AI factory company, today announced it is the developer of Google’s data center campus under construction
    in Armstrong County
- claim: Applied Digital reached 250 MW of operational IT load
  url: https://ir.applieddigital.com/news-events/press-releases/detail/161/applied-digital-brings-an-additional-75-mw-of-ai
  date: '2026-10-02'
  quote: brings fully operational critical IT load at Polaris Forge 1 to 250 MW.
- claim: Polar operates a 12 MW site for Crusoe in Tørdal, Norway
  url: https://www.crusoe.ai/resources/newsroom/polar-crusoe-partnership-expansion
  date: '2026-10-21'
  quote: DRA01 is now live, providing 12MW of IT capacity, powered by 100% hydroelectric energy.
```

### ed094
```yaml
status: ok
section: Tech and infra
title: What are the solvable bottlenecks?
t:
  39: BOTTLENECK
  38: EXPLANATION
  41: BOTTLENECK
  40: EXPLANATION
  7: "GRID\nACCESS"
  11: "POWER\nGEAR"
  15: "LIQUID\nCOOL"
  19: "RACK\nPOWER"
  24: "FIBER\nLINKS"
  28: "BUILD\nSPEED"
  32: "SITE\nPERMITS"
  36: "SITE\nUPTIME"
  5: A campus may have land and tenants but no firm date for the grid to supply full power.
  9: Transformers and large switches take time to source, build, test and connect.
  13: Dense GPU racks need coolant pipes, pumps and dry connections that do not leak.
  17: New rack designs draw much more power, forcing upgrades to cables and breakers.
  22: Remote sites need enough fiber routes to keep large AI clusters linked to users.
  26: Concrete, electrical gear and specialist crews must all arrive in the right order.
  30: Local rules and public concerns can delay large sites even when land is secured.
  34: Power dips and coolant failures can interrupt the very AI jobs a tenant pays to run.
note: We focus on bottlenecks that facility developers can partly address through location choices, engineering, procurement
  and site operations.
sources:
- claim: Grid availability constrains global data center projects
  url: https://www.cbre.com/insights/reports/global-data-center-trends-2026
  date: '2026-06-17'
  quote: Global power availability and grid infrastructure constraints are impacting development timelines and site selection
- claim: Transformer and cable wait times doubled over three years
  url: https://www.iea.org/reports/energy-and-ai/executive-summary
  date: '2025-04-10'
  quote: wait times for critical grid components such as transformers and cables have doubled in the past three years.
- claim: GB200 NVL72 racks use direct liquid cooling for 120 kW heat loads
  url: https://developer.nvidia.com/blog/?p=90182
  date: '2024-10-15'
  quote: To efficiently manage the 120 KW cooling capacity required for the rack, we’ve implemented direct liquid cooling
    techniques.
- claim: AI server power density rose elevenfold between 2020 and 2025
  url: https://www.iea.org/reports/key-questions-on-energy-and-ai/executive-summary
  date: '2026-04-16'
  quote: between 2020 and 2025, the power density of AI servers increased by 11 times
- claim: Operators face power, staffing and equipment supply shortages
  url: https://uptimeinstitute.com/resources/research-and-reports/uptime-institute-global-data-center-survey-results-2026
  date: '2026-07-27'
  quote: operators must navigate challenges such as limited power availability, falling grid reliability, rising costs, supply
    chain limits and staffing shortages.
- claim: GPU training load ramps sharply and needs power smoothing
  url: https://www.crusoe.ai/resources/newsroom/crusoe-and-on-energy-to-deploy-5-gw-of-ai-ups-tm-at-multiple-hyperscale-campuses
  date: '2026-07-21'
  quote: During training, many thousands of GPUs ramp up and down in synchronized bursts, creating fluctuations in power demand.
```

### ed095
```yaml
status: ok
section: Tech and infra
title: Why can’t we solve them yet?
t:
  39: BOTTLENECK
  38: REASON WHY
  41: BOTTLENECK
  40: REASON WHY
  7: "GRID\nACCESS"
  11: "POWER\nGEAR"
  15: "LIQUID\nCOOL"
  19: "RACK\nPOWER"
  24: "FIBER\nLINKS"
  28: "BUILD\nSPEED"
  32: "SITE\nPERMITS"
  36: "SITE\nUPTIME"
  5: Grid plans serve many users, and the lines needed for huge new loads take years.
  9: Utilities and builders all need the same scarce transformers and switchgear.
  13: Cooling must work across changing chip types, with no leaks in crowded racks.
  17: Each GPU generation changes heat and power needs faster than halls can be rebuilt.
  22: Fiber paths and local rights of way may not be ready where cheap power exists.
  26: Major halls depend on skilled crews and gear from several long supply chains.
  30: Water use, power bills and land impacts can trigger protests and long reviews.
  34: AI training causes fast load swings, while every outage risks costly downtime.
note: We link each delay to the physical build process and grid constraints. Better chips alone do not deliver a working data
  center.
sources:
- claim: Transmission line construction can take four to eight years
  url: https://www.iea.org/reports/energy-and-ai/executive-summary
  date: '2025-04-10'
  quote: Building new transmission lines can take four to eight years in advanced economies
- claim: Transformer and cable wait times doubled over three years
  url: https://www.iea.org/reports/energy-and-ai/executive-summary
  date: '2025-04-10'
  quote: wait times for critical grid components such as transformers and cables have doubled in the past three years.
- claim: Operators face power, staffing and equipment supply shortages
  url: https://uptimeinstitute.com/resources/research-and-reports/uptime-institute-global-data-center-survey-results-2026
  date: '2026-07-27'
  quote: operators must navigate challenges such as limited power availability, falling grid reliability, rising costs, supply
    chain limits and staffing shortages.
- claim: AI server power density rose elevenfold between 2020 and 2025
  url: https://www.iea.org/reports/key-questions-on-energy-and-ai/executive-summary
  date: '2026-04-16'
  quote: between 2020 and 2025, the power density of AI servers increased by 11 times
- claim: Grid availability constrains global data center projects
  url: https://www.cbre.com/insights/reports/global-data-center-trends-2026
  date: '2026-06-17'
  quote: Global power availability and grid infrastructure constraints are impacting development timelines and site selection
- claim: AI workloads produce sudden swings in power demand
  url: https://www.iea.org/reports/key-questions-on-energy-and-ai/executive-summary
  date: '2026-04-16'
  quote: Unlike traditional data centre operations, AI training and model use induce large and rapid power swings
```

### ed096
```yaml
status: ok
section: Tech and infra
title: When can we realistically expect to solve them?
t:
  39: BOTTLENECK
  38: WHY THIS TIMELINE
  41: BOTTLENECK
  40: WHY THIS TIMELINE
  7: "GRID\nACCESS"
  11: "POWER\nGEAR"
  15: "LIQUID\nCOOL"
  19: "RACK\nPOWER"
  24: "FIBER\nLINKS"
  28: "BUILD\nSPEED"
  32: "SITE\nPERMITS"
  36: "SITE\nUPTIME"
  5: More grid capacity takes years to permit and build, so relief is gradual even at top sites.
  9: New factory output may help, but high-voltage gear needs long lead times and testing.
  13: Liquid designs work, yet broader use needs more trained fitters and repeatable parts.
  17: Higher-power layouts can spread by the decade end, but each new GPU resets the demands.
  22: New routes can be laid faster than power lines, although distant sites need more paths.
  26: Modules cut field work, but campus roads, power and local labor still shape delivery.
  30: Permitting can speed up in favored regions, while local pushback may delay other sites.
  34: Better controls and batteries may smooth power dips, but full uptime is never guaranteed.
  42: '2032'
  43: '2030'
  44: '2029'
  45: '2030'
  46: '2029'
  47: '2029'
  48: '2032'
  49: '2031'
comment: Years are analyst estimates for material easing at scale, not industry consensus or guaranteed resolution.
note: We estimate when each constraint might ease at scale, not disappear. These are analyst scenarios based on build times
  and current progress.
sources:
- claim: Transmission line construction can take four to eight years
  url: https://www.iea.org/reports/energy-and-ai/executive-summary
  date: '2025-04-10'
  quote: Building new transmission lines can take four to eight years in advanced economies
- claim: Transformer and cable wait times doubled over three years
  url: https://www.iea.org/reports/energy-and-ai/executive-summary
  date: '2025-04-10'
  quote: wait times for critical grid components such as transformers and cables have doubled in the past three years.
- claim: Operators face power, staffing and equipment supply shortages
  url: https://uptimeinstitute.com/resources/research-and-reports/uptime-institute-global-data-center-survey-results-2026
  date: '2026-07-27'
  quote: operators must navigate challenges such as limited power availability, falling grid reliability, rising costs, supply
    chain limits and staffing shortages.
- claim: AI server power density rose elevenfold between 2020 and 2025
  url: https://www.iea.org/reports/key-questions-on-energy-and-ai/executive-summary
  date: '2026-04-16'
  quote: between 2020 and 2025, the power density of AI servers increased by 11 times
- claim: Crusoe introduced modular liquid-cooled units supporting 3.5 MW
  url: https://www.crusoe.ai/resources/newsroom/crusoe-introduces-crusoe-spark-liquid
  date: '2026-10-21'
  quote: Crusoe Spark Liquid delivers high-efficiency DLC closed-loop cooling to support up to 3.5MW of compute per unit.
- claim: AI workloads produce sudden swings in power demand
  url: https://www.iea.org/reports/key-questions-on-energy-and-ai/executive-summary
  date: '2026-04-16'
  quote: Unlike traditional data centre operations, AI training and model use induce large and rapid power swings
- claim: Grid availability constrains global data center projects
  url: https://www.cbre.com/insights/reports/global-data-center-trends-2026
  date: '2026-06-17'
  quote: Global power availability and grid infrastructure constraints are impacting development timelines and site selection
```

### ed097
```yaml
status: ok
section: Tech and infra
title: Which bold bets could reshape AI data centers?
t:
  9: ON-SITE POWER
  7: It is an AI campus with firm local generation that can open before a full grid upgrade.
  12: DRY LIQUID COOL
  10: It is dense liquid cooling that keeps GPU racks cold without heavy water loss.
  15: MODULAR AI HALLS
  13: It is factory-built high-density capacity delivered in repeatable units near ready power.
  18: BATTERY BUFFER
  16: It is storage that absorbs sudden GPU power jumps before they strain the utility grid.
  33: "NEAR-TERM HORIZON\n(0-5 YEARS)"
  21: FLEXIBLE AI LOAD
  19: It is a campus that shifts less urgent compute jobs to hours when power is plentiful.
  24: WASTE HEAT SALES
  22: It is an AI hall that sells its recovered heat to nearby buildings or industry.
  27: FIBER-FIRST SITES
  25: It is a network of remote AI sites built around ready fiber and cheaper firm power.
  30: SELF-RUNNING HALLS
  28: It is a site where sensors catch cooling and power faults before tenants lose uptime.
  34: "LONG-TERM HORIZON\n(5-10 YEARS)"
comment: These are technology bets, not validated forecasts or claims that each solution is already proven at scale.
note: We picked plausible infrastructure shifts already visible in live projects or announced designs. Timing and commercial
  success remain uncertain.
sources:
- claim: Crusoe announced a Microsoft AI campus with 900 MW of power
  url: https://www.crusoe.ai/resources/newsroom/crusoe-announces-new-900-mw-ai-factory-campus-in-abilene-texas-to-support-microsoft-ai-infrastructure
  date: '2026-03-27'
  quote: Supporting large scale AI workloads for Microsoft, the 900 MW site includes two new buildings and an onsite power
    plant
- claim: Crusoe is developing a Google campus under construction in Texas
  url: https://www.crusoe.ai/resources/newsroom/crusoe-developing-data-center-campus-in-armstrong-county-texas
  date: '2026-09-28'
  quote: Crusoe, the AI factory company, today announced it is the developer of Google’s data center campus under construction
    in Armstrong County
- claim: Crusoe introduced modular liquid-cooled units supporting 3.5 MW
  url: https://www.crusoe.ai/resources/newsroom/crusoe-introduces-crusoe-spark-liquid
  date: '2026-10-21'
  quote: Crusoe Spark Liquid delivers high-efficiency DLC closed-loop cooling to support up to 3.5MW of compute per unit.
- claim: GPU training load ramps sharply and needs power smoothing
  url: https://www.crusoe.ai/resources/newsroom/crusoe-and-on-energy-to-deploy-5-gw-of-ai-ups-tm-at-multiple-hyperscale-campuses
  date: '2026-07-21'
  quote: During training, many thousands of GPUs ramp up and down in synchronized bursts, creating fluctuations in power demand.
- claim: AI workloads produce sudden swings in power demand
  url: https://www.iea.org/reports/key-questions-on-energy-and-ai/executive-summary
  date: '2026-04-16'
  quote: Unlike traditional data centre operations, AI training and model use induce large and rapid power swings
- claim: Operators face power, staffing and equipment supply shortages
  url: https://uptimeinstitute.com/resources/research-and-reports/uptime-institute-global-data-center-survey-results-2026
  date: '2026-07-27'
  quote: operators must navigate challenges such as limited power availability, falling grid reliability, rising costs, supply
    chain limits and staffing shortages.
- claim: Transmission line construction can take four to eight years
  url: https://www.iea.org/reports/energy-and-ai/executive-summary
  date: '2025-04-10'
  quote: Building new transmission lines can take four to eight years in advanced economies
```

### ed098
```yaml
status: ok
section: Tech and infra
title: Which companies are working on groundbreaking tech today?
t:
  8: FLUIDSTACK
  6: They develop custom AI halls for Anthropic and have started a huge Texas site.
  24: APPLIED DIGITAL
  22: They turn large signed leases into live high-density AI halls in North Dakota.
  11: CRUSOE
  9: They build huge AI campuses and liquid-cooled modular units for rapid use.
  27: GALAXY
  25: They are converting the Helios mining site into a leased AI campus for CoreWeave.
  14: NSCALE
  12: They plan dense AI campus capacity in Norway and the UK for Microsoft.
  30: IREN
  28: They are building liquid-cooled Horizon halls to serve Microsoft at Childress.
  17: POLAR
  15: They run a hydro-powered AI hall in Norway and plan more liquid-cooled space.
  33: ARMADA
  31: They build modular AI data centers that can be placed close to available power.
note: We select firms whose marketed products include physical AI capacity, campus development or modular data centers rather
  than software alone.
sources:
- claim: Crusoe introduced modular liquid-cooled units supporting 3.5 MW
  url: https://www.crusoe.ai/resources/newsroom/crusoe-introduces-crusoe-spark-liquid
  date: '2026-10-21'
  quote: Crusoe Spark Liquid delivers high-efficiency DLC closed-loop cooling to support up to 3.5MW of compute per unit.
- claim: Applied Digital reached 250 MW of operational IT load
  url: https://ir.applieddigital.com/news-events/press-releases/detail/161/applied-digital-brings-an-additional-75-mw-of-ai
  date: '2026-10-02'
  quote: brings fully operational critical IT load at Polaris Forge 1 to 250 MW.
- claim: Fluidstack will develop custom Texas and New York AI sites for Anthropic
  url: https://fluidstack.com/news/fluidstack-selected-by-anthropic-to-deliver-custom-data-centers-in-the-us
  date: '2025-11-12'
  quote: Fluidstack is announcing a $50 billion American computing infrastructure deal with Anthropic, building data centers
    in New York and Texas
- claim: Fluidstack began construction in Cameron County, Texas
  url: https://fluidstack.com/community/building-compute-in-cameron-county
  date: '2026-09-21'
  quote: We’ve begun construction on the $4 billion first phase of our AI data center campus in Cameron County, Texas.
- claim: Core Scientific had begun billing on 485 MW of contracted load
  url: https://investors.corescientific.com/sec-filings/all-sec-filings/content/0001839341-26-000030/core-20260930.htm
  date: '2026-11-05'
  quote: As of September 30, 2026, approximately 485 MW has commenced billing.
- claim: Galaxy delivered 133 MW of AI IT load to CoreWeave at Helios
  url: https://www.galaxy.com/newsroom/galaxy-completes-phase-i-of-its-helios-data-center-campus
  date: '2026-07-06'
  quote: 133 MW of critical IT load
- claim: Nscale has a Microsoft deal for its 230 MW Narvik campus
  url: https://www.nscale.com/press-releases/nscale-microsoft-norway
  date: '2026-04-14'
  quote: the 230 MW Nscale Narvik campus will add more than 30,000 NVIDIA Rubin GPUs in deployment
- claim: Microsoft accepted IREN Horizon 1 in August 2026
  url: https://www.sec.gov/Archives/edgar/data/1878848/000187884826000052/iren-20260630.htm
  date: '2026-08-28'
  quote: Horizon 1 was delivered to, and accepted by, Microsoft in August 2026.
- claim: Polar operates a 12 MW site for Crusoe in Tørdal, Norway
  url: https://www.crusoe.ai/resources/newsroom/polar-crusoe-partnership-expansion
  date: '2026-10-21'
  quote: DRA01 is now live, providing 12MW of IT capacity, powered by 100% hydroelectric energy.
- claim: Armada launched a modular AI data center with 10 MW capacity
  url: https://www.armada.ai/blog/armada-orion-10mw-galleon-sovereign-ai-grid
  date: '2026-08-26'
  quote: Armada today launched Orion, the 10-megawatt Galleon and the most powerful member of its Galleon family of modular
    data centers.
```

### iv_pipeline
```yaml
status: ok
section: Tech and infra
title: Which big AI data center campuses are being built right now?
t:
  38: LIVE
  37: CRUSOE · ORACLE
  34: 'Abilene, Texas, USA: flagship Stargate campus operating'
  27: LIVE
  26: APPLIED DIGITAL · 250 MW
  24: 'Ellendale, North Dakota, USA: 250 MW of IT load running'
  23: LIVE
  22: GALAXY · COREWEAVE
  20: 'Helios, West Texas, USA: first 133 MW now in service'
  19: LIVE
  18: CORE SCIENTIFIC · COREWEAVE
  16: 'Denton, Texas, USA: large leased AI halls now in service'
  15: LIVE
  14: IREN · MICROSOFT
  12: 'Childress, Texas, USA: first Horizon phase was accepted'
  11: BUILD
  10: NSCALE · MICROSOFT
  8: 'Narvik, Norway: a 230 MW campus with a signed GPU deal'
  7: LIVE
  6: POLAR · CRUSOE
  4: 'Tørdal, Norway: 12 MW facility live, with added space planned'
  3: BUILD
  2: FLUIDSTACK · 1.5 GW
  0: 'Cameron County, Texas, USA: first site works began in 2026'
comment: Rows show eight distinct active campuses. The phase label describes verified current status, not ultimate site capacity.
note: We count a campus only if a tenant, live delivery or site construction is documented. LIVE means a portion operates,
  not the whole plan.
sources:
- claim: Crusoe brought phase one of the Abilene Stargate campus online
  url: https://www.crusoe.ai/resources/newsroom/crusoe-announces-flagship-abilene-data-center-is-live
  date: '2025-09-30'
  quote: the first phase of Stargate’s flagship data center campus in Abilene, Texas, is now up and running on Oracle Cloud
    Infrastructure
- claim: Applied Digital reached 250 MW of operational IT load
  url: https://ir.applieddigital.com/news-events/press-releases/detail/161/applied-digital-brings-an-additional-75-mw-of-ai
  date: '2026-10-02'
  quote: brings fully operational critical IT load at Polaris Forge 1 to 250 MW.
- claim: Galaxy delivered 133 MW of AI IT load to CoreWeave at Helios
  url: https://www.galaxy.com/newsroom/galaxy-completes-phase-i-of-its-helios-data-center-campus
  date: '2026-07-06'
  quote: 133 MW of critical IT load
- claim: Core Scientific expanded the Denton AI site to about 260 MW
  url: https://investors.corescientific.com/news-events/press-releases/detail/110/core-scientific-and-coreweave-announce-1-2-billion-expansion-at-denton-tx-site
  date: '2025-02-26'
  quote: The 70 MW of additional contracted power at the Denton site increases the full critical IT load to approximately
    260 MW.
- claim: Core Scientific disclosed its Denton capacity in a 2026 deck
  url: https://investors.corescientific.com/sec-filings/all-sec-filings/content/0001839341-26-000028/q3fy26earningsdeckvfinal.htm
  date: '2026-11-05'
  quote: Denton, TX 260 MW Dalton, GA 175 MW Muskogee, OK 70 MW Marble, NC 65 MW Austin, TX 20 MW
- claim: Microsoft accepted IREN Horizon 1 in August 2026
  url: https://www.sec.gov/Archives/edgar/data/1878848/000187884826000052/iren-20260630.htm
  date: '2026-08-28'
  quote: Horizon 1 was delivered to, and accepted by, Microsoft in August 2026.
- claim: Nscale has a Microsoft deal for its 230 MW Narvik campus
  url: https://www.nscale.com/press-releases/nscale-microsoft-norway
  date: '2026-04-14'
  quote: the 230 MW Nscale Narvik campus will add more than 30,000 NVIDIA Rubin GPUs in deployment
- claim: Polar operates a 12 MW site for Crusoe in Tørdal, Norway
  url: https://www.crusoe.ai/resources/newsroom/polar-crusoe-partnership-expansion
  date: '2026-10-21'
  quote: DRA01 is now live, providing 12MW of IT capacity, powered by 100% hydroelectric energy.
- claim: Fluidstack began construction in Cameron County, Texas
  url: https://fluidstack.com/community/building-compute-in-cameron-county
  date: '2026-09-21'
  quote: We’ve begun construction on the $4 billion first phase of our AI data center campus in Cameron County, Texas.
```

