### ed041
```yaml
status: ok
section: Market size
title: What counts as neocloud, and what does not?
note: We count revenue from customer access to actual accelerator compute, not chip sales, facility rent or model software alone.
t:
  7: 'We count specialist sellers of rented AI compute: GPU instances, reserved chip clusters and hosted endpoints that run models for paying customers.'
  8: We include GPU cloud compute, dedicated AI clusters, bare-metal AI cloud, managed training, paid inference and booked GPU marketplaces.
  9: We exclude general cloud firms, chip vendors, landlords, pure model apps, GPU schedulers and miners without customer-facing AI compute.
sources:
- claim: Gartner defines specialist neoclouds
  url: https://www.gartner.com/en/newsroom/press-releases/2026-06-23-gartner-predicts-neocloud-providers-will-capture-20-percent-of-the-267-billion-dollar-ai-cloud-market-by-2030
  date: '2026-06-23'
  quote: By 2030, neocloud providers will capture 20% of the $267 billion AI cloud market, according to Gartner, Inc.
- claim: GPU services include pods clusters and endpoints
  url: https://www.runpod.io/pricing
  date: '2026-11-12'
  quote: Serverless bills inference workers based on usage, and Clusters support multi-node workloads and reserved capacity.
- claim: Cloud inference services run customer models
  url: https://www.baseten.co/pricing/
  date: '2026'
  quote: You can deploy open source and custom models on Baseten.
```

### ed042
```yaml
status: ok
section: Market size
title: What are the market size estimates from different sources online?
rows:
- firm: 'Synergy

    Research'
  value: ≈ $40B
  comment: Their $25B-plus 2025 base times 1.58 suggests about $40B in 2026. This covers neocloud supply, but also some platform and site activity.
- firm: 'ABI

    Research'
  value: ≈ $60B
  comment: Their $42B 2025 GPU cloud base and 43% growth imply roughly $60B in 2026. Scope is specialist rented compute, but methods are not public.
- firm: 'Fortune

    Insights'
  value: $8.7B
  comment: Their 2026 GPU-as-a-service figure covers broad cloud rentals and major cloud firms. It is not a complete neocloud revenue count.
- firm: 'Grand View

    Research'
  value: $5.1B
  comment: Their 2026 GPU rental market includes other computing uses yet is well below named neocloud sales. We do not average it with Synergy.
note:
- We compare two neocloud forecasts with two GPU-rental studies, stating where their scopes are not alike.
- We derive 2026 figures for Synergy and ABI from their 2025 base and stated growth rate, not direct forecasts.
sources:
- claim: Synergy revenue exceeded $25B in 2025
  url: https://www.srgresearch.com/articles/neocloud-market-forecast-to-approach-400b-by-2031-driven-by-surging-ai-infrastructure-demand
  date: '2026-04-02'
  quote: exceeding $25 billion for full-year 2025.
- claim: Synergy forecasts 58% growth
  url: https://www.srgresearch.com/articles/neocloud-market-forecast-to-approach-400b-by-2031-driven-by-surging-ai-infrastructure-demand
  date: '2026-04-02'
  quote: Synergy forecasts the market will approach $400 billion by 2031, representing a sustained 58% compound annual growth rate.
- claim: ABI starts from $42B in 2025 and forecasts 43% CAGR
  url: https://www.abiresearch.com/news-resources/chart-data/gpu-as-a-service-revenue-for-neoclouds
  date: 2025-Q4
  quote: at a Compound Annual Growth Rate (CAGR) of 43% (from US$42 in 2025).
- claim: Fortune GPUaaS 2026 about $8.7B and 44.3%
  url: https://www.fortunebusinessinsights.com/gpu-as-a-service-market-107797
  date: '2026-11-02'
  quote: '2026 Market Size: USD 8.66 billion'
- claim: Grand View GPUaaS 2026 $5.1B and 16%
  url: https://www.grandviewresearch.com/industry-analysis/gpu-as-a-service-gpuaas-market-report
  date: '2026'
  quote: 'Estimated market size in 2026: USD 5.1 Billion'
comment: 2026 neocloud size is an indicative extrapolation of published market series, not a complete bottom-up sum. Synergy also includes some offerings outside our strict compute-only definition.
```

### ed043
```yaml
status: ok
section: Market size
title: Our own first-principles, bottom-up calculation of the market size
page: 1/2
note: We begin with specialist-provider revenue research and test the scale against published operating results.
t:
  21: We size only paid AI cloud compute, not the chips or buildings
  16: We use neocloud vendor sales as the main anchor, then test other totals
  15: We count live GPU rentals, reserved clusters and paid model runs
  14: We omit chip sales, pure facility rent and general cloud services
  9: We count revenue when cloud capacity is delivered, not when a deal is signed
  8: We use 2026 to match the newest public company revenue figures
  7: We start with Synergy at over $25B of neocloud revenue in 2025
  6: Its 58% growth path implies nearly $40B in 2026
  3: ABI reports $42B in 2025 from specialist neocloud GPU rental services
  2: Its 43% rate points toward roughly $60B in 2026, a wider view
  0: We do not blend smaller GPU-rental reports with neocloud totals
sources:
- claim: Synergy $25B revenue in 2025 and 58% CAGR
  url: https://www.srgresearch.com/articles/neocloud-market-forecast-to-approach-400b-by-2031-driven-by-surging-ai-infrastructure-demand
  date: '2026-04-02'
  quote: Synergy forecasts the market will approach $400 billion by 2031, representing a sustained 58% compound annual growth rate.
- claim: ABI $42B 2025 and 43% CAGR
  url: https://www.abiresearch.com/news-resources/chart-data/gpu-as-a-service-revenue-for-neoclouds
  date: 2025-Q4
  quote: global revenue from GPUaaS offerings by neocloud providers are projected to reach nearly US$250 billion
- claim: General GPU rental reports include hyperscalers
  url: https://www.fortunebusinessinsights.com/gpu-as-a-service-market-107797
  date: '2026-11-02'
  quote: '2026 Market Size: USD 8.66 billion'
- claim: Grand View narrower $5.1B 2026 comparison
  url: https://www.grandviewresearch.com/industry-analysis/gpu-as-a-service-gpuaas-market-report
  date: '2026'
  quote: 'Estimated market size in 2026: USD 5.1 Billion'
comment: 2026 neocloud size is an indicative extrapolation of published market series, not a complete bottom-up sum. Synergy also includes some offerings outside our strict compute-only definition.
```

### ed044
```yaml
status: ok
section: Market size
title: Our own first-principles, bottom-up calculation of the market size
page: 2/2
note: We use audited and quarterly company revenue only to check the market estimate, not as a complete vendor census.
t:
  21: We verify the scale against actual operator sales and filings
  16: CoreWeave guides to about $13B in full-year 2026 cloud sales
  15: Nebius AI cloud earned $1.9B in the first nine months
  14: IREN had $200M of AI cloud sales in the third quarter
  9: We leave out IREN mining sales and Nebius one-time fees in repeat runs
  8: We see at least three large cloud sellers with real revenue
  7: We use a $40B base that follows the Synergy neocloud growth path
  6: We use ABI near $60B as an upper check, not extra revenue piled on top
  3: We do not add signed backlogs to annual market revenue
  2: We round to $40B, with wider scope and timing as key risks
  0: We estimate neocloud sales at about $40B worldwide in 2026
sources:
- claim: CoreWeave 2026 guide about $13B
  url: https://investors.coreweave.com/news/news-details/2026/CoreWeave-Reports-Strong-Third-Quarter-2026-Results/
  date: '2026-11-10'
  quote: We are raising our full year 2026 revenue guidance to a range of $13.0 billion to $13.3 billion.
- claim: Nebius AI cloud booked about $1.9B in nine months of 2026
  url: https://www.sec.gov/Archives/edgar/data/1513845/000110465926126238/nbis-ex99d1.htm
  date: '2026-11-12'
  quote: to $1,938.4 million in the same period in 2026.
- claim: Nebius recognized $325M in one-time enablement revenue
  url: https://www.sec.gov/Archives/edgar/data/1513845/000110465926126008/tm2629571d1_ex99-2.htm
  date: '2026-11-12'
  quote: In Q3, we recognized approximately $325 million of non-recurring revenue as part of our asset-light model.
- claim: IREN Q3 2026 AI cloud sales $200M
  url: https://iren.gcs-web.com/news-releases/news-release-details/iren-reports-q1-fy27-results
  date: '2026-11-05'
  quote: AI Cloud quarterly revenue increased 182% sequentially to $200 million
- claim: Synergy over $25B 2025 and 58% growth
  url: https://www.srgresearch.com/articles/neocloud-market-forecast-to-approach-400b-by-2031-driven-by-surging-ai-infrastructure-demand
  date: '2026-04-02'
  quote: New data from Synergy Research Group reveals that neocloud revenues are scaling at an unprecedented pace
- claim: ABI 2025 $42B and 43% growth
  url: https://www.abiresearch.com/news-resources/chart-data/gpu-as-a-service-revenue-for-neoclouds
  date: 2025-Q4
  quote: Inferencing revenue for neoclouds will grow 88% annually, compared to 15% for training workloads.
comment: 2026 neocloud size is an indicative extrapolation of published market series, not a complete bottom-up sum. Synergy also includes some offerings outside our strict compute-only definition.
```

### ed045
```yaml
status: ok
section: Market size
title: How much is neocloud worth today?
t:
  6: $40B
  8: We estimate $40B in 2026 from Synergy’s $25B-plus 2025 base and its 58% growth path. ABI implies near $60B under another GPU rental definition. Public sales confirm the scale, not the total.
  4: '2026'
note: We favor the more cautious neocloud revenue series, while showing why other research gives a different answer.
sources:
- claim: 2025 neocloud revenue over $25B, 58% CAGR
  url: https://www.srgresearch.com/articles/neocloud-market-forecast-to-approach-400b-by-2031-driven-by-surging-ai-infrastructure-demand
  date: '2026-04-02'
  quote: New data from Synergy Research Group reveals that neocloud revenues are scaling at an unprecedented pace
- claim: 2025 ABI base $42B, 43% growth
  url: https://www.abiresearch.com/news-resources/chart-data/gpu-as-a-service-revenue-for-neoclouds
  date: 2025-Q4
  quote: Inferencing revenue for neoclouds will grow 88% annually, compared to 15% for training workloads.
- claim: CoreWeave 2026 sales guide
  url: https://investors.coreweave.com/news/news-details/2026/CoreWeave-Reports-Strong-Third-Quarter-2026-Results/
  date: '2026-11-10'
  quote: Revenue backlog1 was approximately $132.5 billion as of September 30, 2026.
comment: 2026 neocloud size is an indicative extrapolation of published market series, not a complete bottom-up sum. Synergy also includes some offerings outside our strict compute-only definition.
```

### ed048
```yaml
status: ok
section: Market size
title: What is behind these categories?
page: 1/2
t:
  5: "DEDICATED\nCLUSTERS"
  8: "GPU\nCLOUDS"
  10: "INFERENCE\nCLOUDS"
  11: 🔗
  4: Long-term rental of linked AI servers lets one customer train or run a large model using many chips working as one group.
  12: 💻
  7: On-demand AI chip instances let a customer rent one or more GPUs by the hour, with cloud access and no server purchase.
  13: 🧠
  9: Hosted model endpoints run customer models and charge for GPU work or requests, without the buyer managing servers.
  15: ''
  17: ''
  18: ''
  19: ''
  14: ''
  16: ''
holes_ok: true
note: We explain the six categories of the market, in the order of their share, with representative paid products from Nscale, CoreWeave, Lambda and Baseten.
sources:
- claim: Hourly GPU instance price models
  url: https://lambda.com/pricing
  date: 2026-11
  quote: Deploy NVIDIA B200, H100, A100, or GH200 instances in minutes with self-serve, first-come access.
- claim: Dedicated GPU cluster contracts
  url: https://www.sec.gov/Archives/edgar/data/1513845/000110465925110025/tm2530771-1_424b5.htm
  date: 2025-11
  quote: Subject to the satisfaction of deployment and availability of the GPU clusters, the total contract value is about $17.4 billion through 2031.
- claim: Customer model serverless GPU endpoints
  url: https://www.runpod.io/product/serverless
  date: '2026-11-02'
  quote: Serverless GPU endpoints run containerized inference workloads behind an API and scale workers based on demand.
- claim: Hosted custom model inference
  url: https://www.baseten.co/pricing/
  date: '2026'
  quote: You can deploy open source and custom models on Baseten.
```

### ed049
```yaml
status: no_data
section: Market size
title: Where in the world is neocloud money spent?
sources:
- claim: Operator counts by home geography are not revenue
  url: https://www.amcompute.com/blog/state-of-the-neoclouds-2026
  date: '2026-10-15'
  quote: As of October 2026, 536 companies sell GPU capacity outside the hyperscalers, in 45 home countries.
- claim: GPUaaS North American share covers a different market
  url: https://www.grandviewresearch.com/industry-analysis/gpu-as-a-service-gpuaas-market-report
  date: '2026'
  quote: 'Estimated market size in 2026: USD 5.1 Billion'
comment: Verified 2026 neocloud revenue shares for all five regions are not public. Provider headquarters counts and broad GPUaaS studies cannot establish regional spending.
```

### ed050
```yaml
status: ok
section: Market size
title: What are the growth rate estimates from different sources online?
note: We favor specialist cloud forecasts and keep broader GPU-rental studies separate because their vendor scope differs.
t:
  24: FIRM
  25: CAGR
  26: COMMENTS
  6: 'Synergy

    Research'
  5: '≈ 58%

    through 2031'
  7: Their neocloud revenue forecast is the fastest relevant guide. It covers a wide range of specialist cloud firms and services.
  10: 'ABI

    Research'
  9: '≈ 43%

    through 2030'
  11: Their GPU rental forecast is for neoclouds, with model execution growing faster than large training jobs.
  14: 'Fortune

    Insights'
  13: '≈ 44.3%

    through 2034'
  15: Their GPU-rental forecast includes general cloud firms and non-AI work. It is a growth check, not a like-for-like total.
  18: 'Grand View

    Research'
  17: '≈ 16%

    through 2033'
  19: Their much lower growth rate comes from a broad GPU-as-a-service study with gaming and other uses. We treat it as a low-growth warning.
sources:
- claim: Synergy 58% CAGR until 2031
  url: https://www.srgresearch.com/articles/neocloud-market-forecast-to-approach-400b-by-2031-driven-by-surging-ai-infrastructure-demand
  date: '2026-04-02'
  quote: Synergy forecasts the market will approach $400 billion by 2031, representing a sustained 58% compound annual growth rate.
- claim: ABI 43% CAGR through 2030
  url: https://www.abiresearch.com/news-resources/chart-data/gpu-as-a-service-revenue-for-neoclouds
  date: 2025-Q4
  quote: global revenue from GPUaaS offerings by neocloud providers are projected to reach nearly US$250 billion
- claim: Fortune 44.3% growth through 2034
  url: https://www.fortunebusinessinsights.com/gpu-as-a-service-market-107797
  date: '2026-11-02'
  quote: exhibiting a CAGR of 44.3% during the forecast period.
- claim: Grand View 16% growth through 2033
  url: https://www.grandviewresearch.com/industry-analysis/gpu-as-a-service-gpuaas-market-report
  date: '2026'
  quote: 'CAGR (2026-2033): 16.0%'
```

### ed051
```yaml
status: ok
section: Market size
title: What is a realistic CAGR for the neocloud market?
note: We moderate near-term industry forecasts for a longer horizon, with 20% and 58% as downside and upside cases.
t:
  15: BEST CASE ≈ 58%
  17: '≈30%

    through 2036'
  19: Synergy sees 58% and ABI sees 43% for shorter periods. We use 30% for a decade because supply, prices and demand can mature, even as more AI models use rented clouds.
  16: WORST CASE ≈ 20%
sources:
- claim: Synergy 58% through 2031
  url: https://www.srgresearch.com/articles/neocloud-market-forecast-to-approach-400b-by-2031-driven-by-surging-ai-infrastructure-demand
  date: '2026-04-02'
  quote: New data from Synergy Research Group reveals that neocloud revenues are scaling at an unprecedented pace
- claim: ABI 43% through 2030
  url: https://www.abiresearch.com/news-resources/chart-data/gpu-as-a-service-revenue-for-neoclouds
  date: 2025-Q4
  quote: Inferencing revenue for neoclouds will grow 88% annually, compared to 15% for training workloads.
- claim: Grand View 16% broader GPU rental forecast
  url: https://www.grandviewresearch.com/industry-analysis/gpu-as-a-service-gpuaas-market-report
  date: '2026'
  quote: 'Estimated market size in 2026: USD 5.1 Billion'
```

### ed052p
```yaml
status: ok
section: Market size
title: How much bigger can neocloud get?
size: 40
cagr: 30
y0: 2026
lead: 'To get that big, '
condition: providers must bring booked GPU capacity online, keep chips busy as prices change, and win growing demand for paid model execution beyond a few large AI buyers.
note:
- We start at roughly $40B of 2026 neocloud revenue and apply our 30% long-term base rate, about $550B by 2036.
- We treat that decade view as a scenario, not booked sales, and test it against shorter Synergy and ABI forecasts.
sources:
- claim: Synergy growth 58% through 2031
  url: https://www.srgresearch.com/articles/neocloud-market-forecast-to-approach-400b-by-2031-driven-by-surging-ai-infrastructure-demand
  date: '2026-04-02'
  quote: New data from Synergy Research Group reveals that neocloud revenues are scaling at an unprecedented pace
- claim: ABI growth 43% through 2030
  url: https://www.abiresearch.com/news-resources/chart-data/gpu-as-a-service-revenue-for-neoclouds
  date: 2025-Q4
  quote: Inferencing revenue for neoclouds will grow 88% annually, compared to 15% for training workloads.
comment: 2026 neocloud size is an indicative extrapolation of published market series, not a complete bottom-up sum. Synergy also includes some offerings outside our strict compute-only definition.
```
