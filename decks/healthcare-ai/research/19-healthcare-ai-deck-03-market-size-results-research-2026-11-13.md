### ed041
```yaml
status: ok
section: Market size
title: What counts as healthcare AI, and what doesn't?
t:
  7: We define healthcare AI as purpose-built software and diagnostics used by providers, insurers and drug developers to improve care or automate work.
  8: We include clinical AI, imaging and diagnostic AI, scribes, monitoring, workflows, billing, payer automation and AI-first drug research.
  9: We exclude AI cloud tools, hospital software, fitness apps and healthcare businesses that do not rely on AI for their core offering.
note: We include healthcare-first AI products, using our market inclusion rules rather than broad technology spending definitions.
sources:
- claim: Grand View Research reports a 46% software share in its broad healthcare AI market estimate.
  url: https://www.grandviewresearch.com/industry-analysis/artificial-intelligence-ai-healthcare-market
  date: 2026-06
  quote: "By component: Software solution segment held the largest market share of 46% in 2025."
- claim: MarketsandMarkets estimates broad healthcare AI at $36.67B in 2026.
  url: https://www.marketsandmarkets.com/Market-Reports/artificial-intelligence-healthcare-market-54679303.html
  date: 2026-06
  quote: "Market Size (2026): USD 36.67 Billion"
```

### ed042
```yaml
status: ok
section: Market size
title: What are the market size estimates from different sources online?
rows:
- firm: MarketsandMarkets
  value: $36.67B
  comment: Their 2026 forecast includes clinical software, robots and cybersecurity. It is a broad market low case, not our exact scope.
- firm: "Grand View\nResearch"
  value: $50.7B
  comment: Their 2026 total covers hardware, services, consumer tools and software. We use it only as a wide cross-check.
- firm: "Precedence\nResearch"
  value: $51.20B
  comment: Their 2026 estimate includes major platform suppliers and medical hardware. We treat it as a broad reference case.
- firm: "Fortune Business\nInsights"
  value: $56.01B
  comment: Their 2026 figure spans robotic surgery, platforms and virtual care. We regard it as the upper end of the published range.
note:
- We copy published 2026 broad-market estimates without presenting them as revenue from our narrower company universe.
- We do not count financing as sales or assume that hardware and general-purpose AI spend meet our definition.
sources:
- claim: MarketsandMarkets estimates broad healthcare AI at $36.67B in 2026.
  url: https://www.marketsandmarkets.com/Market-Reports/artificial-intelligence-healthcare-market-54679303.html
  date: 2026-06
  quote: "Market Size (2026): USD 36.67 Billion"
- claim: Grand View Research reports a $50.7B estimate for 2026.
  url: https://www.grandviewresearch.com/industry-analysis/artificial-intelligence-ai-healthcare-market
  date: 2026-06
  quote: "Estimated market size in 2026: USD 50.7 Billion"
- claim: Precedence Research estimates broad healthcare AI at $51.20B in 2026.
  url: https://www.precedenceresearch.com/artificial-intelligence-in-healthcare-market
  date: '2026-09-16'
  quote: "Market Size in 2026: USD 51.20 Billion"
- claim: Fortune Business Insights estimates $56.01B in 2026.
  url: https://www.fortunebusinessinsights.com/industry-reports/artificial-intelligence-in-healthcare-market-100534
  date: '2026-10-26'
  quote: "2026 Market Size: USD 56.01 Billion"
```

### ed043
```yaml
status: no_data
title: Our own first-principles, bottom-up calculation of the market size
comment: No audited category-level 2026 revenues are disclosed for all six healthcare-first AI segments. Published totals include excluded hardware and horizontal providers, so a bottom-up sum is not defensible.
sources: []
```

### ed044
```yaml
status: no_data
title: Our own first-principles, bottom-up calculation of the market size
comment: No verified company-level AI-only revenue census or non-overlapping six-category subtotal supports a second bottom-up calculation.
sources: []
```

### ed045
```yaml
status: no_data
title: How much is healthcare AI worth today?
comment: The $36.67B to $56.01B published range covers broader scopes. A single 2026 valuation for the strict healthcare-first AI company definition is not verifiable.
sources: []
```

### ed047p
```yaml
status: no_data
title: How is the healthcare AI market split between its categories?
comment: No reliable revenue split across Clinical AI Tools, Diagnostic AI Software, Care Workflow AI, Revenue Cycle AI, Payer AI Platforms and Life Science AI is available.
sources: []
```

### ed048
```yaml
status: ok
section: Market size
title: What is behind these categories?
holes_ok: true
t:
  5: CLINICAL AI TOOLS
  8: CARE WORKFLOW AI
  10: LIFE SCIENCE AI
  4: Clinical tools support decisions, review patient facts and interpret scans. This group also includes Diagnostic AI Software.
  7: AI drafts notes, billing codes and payer reviews. This group also covers Revenue Cycle AI and Payer AI Platforms.
  9: AI tools find targets, design molecules and support trials. The model must drive discovery, not assist research.
  15: ""
  17: ""
  18: ""
  19: ""
  14: ""
  16: ""
note: We explain three illustrative groups and map all six database categories into them. These groups are not a measured revenue split.
sources:
- claim: FDA says it had authorized over 1,600 AI-enabled medical devices by September 2026.
  url: https://www.fda.gov/medical-devices/digital-health-center-excellence/artificial-intelligence-enabled-medical-devices
  date: 2026-10
  quote: The FDA has authorized over 1,600 AI-enabled medical devices for marketing in the United States as of September 2026.
- claim: KFF finds AI insurance decisions pose risks if no individualized clinical review is applied.
  url: https://www.kff.org/patient-consumer-protections/regulation-of-ai-in-prior-authorization-and-claims-review-a-look-at-federal-and-state-consumer-protections/
  date: '2026-05-06'
  quote: Risks to consumers include the potential for inaccurate or biased outcomes and privacy breaches.
- claim: Nature Reviews Drug Discovery highlights the difficulty of proving AI improves drug-development outcomes.
  url: https://www.nature.com/articles/s41573-026-01496-2
  date: 2026-08
  quote: This further confounds the analysis of whether AI is translating to improved clinical outcomes across the industry, or at least a subset of it.
```

### ed049
```yaml
status: ok
section: Market size
title: Where in the world is healthcare AI money spent?
regions:
  na:
    pct: 45
    text: North America leads with 44.5% of the broad market in 2025, per Fortune Business Insights. The US drives adoption.
  eu:
    pct: 28
    text: Europe accounts for 28.1% in Fortune Business Insights data. Hospital AI and drug research help build demand.
  apac:
    pct: 21
    text: Asia Pacific holds 21.05%, led by China, Japan and India. The report expects rapid further growth.
  latam:
    pct: 4
    text: Latin America holds 4.08% of 2025 broad-market revenue. Brazil and Mexico are major markets.
  mea:
    pct: 2
    text: Middle East and Africa account for 2.26% of 2025 broad-market revenue. Gulf investments support interest.
note:
- We use Fortune Business Insights regional 2025 shares as a broad-market proxy, not a direct split of our strict company universe.
- We round its five published shares to whole percentages and do not infer precision beyond the source.
sources:
- claim: Fortune Business Insights forecasts $56.01B in 2026 and 43.96% CAGR to 2034.
  url: https://www.fortunebusinessinsights.com/industry-reports/artificial-intelligence-in-healthcare-market-100534
  date: '2026-10-26'
  quote: North America dominated the artificial intelligence in healthcare market with a market share of 44.50% in 2025.
- claim: Fortune Business Insights reports Europe represented 28.10% of broader healthcare AI spending in 2025.
  url: https://www.fortunebusinessinsights.com/industry-reports/artificial-intelligence-in-healthcare-market-100534
  date: '2026-10-26'
  quote: representing 28.10% of global demand, and is projected to grow to USD 15.73 billion in 2026.
- claim: Fortune Business Insights estimates Asia Pacific represented 21.05% in 2025.
  url: https://www.fortunebusinessinsights.com/industry-reports/artificial-intelligence-in-healthcare-market-100534
  date: '2026-10-26'
  quote: The Asia Pacific region captured 21.05% of the global market in 2025
- claim: Fortune Business Insights estimates Latin America represented 4.08% of the broad 2025 market.
  url: https://www.fortunebusinessinsights.com/industry-reports/artificial-intelligence-in-healthcare-market-100534
  date: '2026-10-26'
  quote: Latin America recorded a market size of USD 1.6 billion in 2025, capturing 4.08% of the global market share
- claim: Fortune Business Insights estimates MEA represented 2.26% in 2025.
  url: https://www.fortunebusinessinsights.com/industry-reports/artificial-intelligence-in-healthcare-market-100534
  date: '2026-10-26'
  quote: contributing 2.26% to global market revenue
```

### ed050
```yaml
status: ok
section: Market size
title: What are the growth rate estimates from different sources online?
t:
  24: FIRM
  25: CAGR
  26: COMMENTS
  6: MarketsandMarkets
  5: "39.7%\nthrough 2031"
  7: This forecast spans hospital software, imaging, robots and cybersecurity. We use its 2026 to 2031 growth as a demand signal.
  10: "Grand View\nResearch"
  9: "38.9%\nthrough 2033"
  11: The forecast includes hardware, services and patient-facing tools. It tests the pace, not the precise scope of our market.
  14: "Precedence\nResearch"
  13: "35.02%\nthrough 2035"
  15: The longer forecast includes AI platforms, devices and care tools. It offers a growth proxy, not a narrow industry forecast.
  18: "Fortune Business\nInsights"
  17: "43.96%\nthrough 2034"
  19: The higher forecast includes robotic surgery and virtual care. We use it as optimistic case, not a verified CAGR for AI-first companies.
note: We use four published 2026 estimates for the broad healthcare AI market and retain each firm's distinct forecast horizon.
sources:
- claim: MarketsandMarkets estimates broad healthcare AI at $36.67B in 2026.
  url: https://www.marketsandmarkets.com/Market-Reports/artificial-intelligence-healthcare-market-54679303.html
  date: 2026-06
  quote: "Market Size (2026): USD 36.67 Billion"
- claim: Grand View Research forecasts 38.9% growth from 2026 to 2033.
  url: https://www.grandviewresearch.com/industry-analysis/artificial-intelligence-ai-healthcare-market
  date: 2026-06
  quote: "CAGR (2026-2033): 38.9%"
- claim: Precedence Research estimates broad healthcare AI at $51.20B in 2026.
  url: https://www.precedenceresearch.com/artificial-intelligence-in-healthcare-market
  date: '2026-09-16'
  quote: "Market Size in 2026: USD 51.20 Billion"
- claim: Fortune Business Insights estimates a 43.96% CAGR from 2026 to 2034.
  url: https://www.fortunebusinessinsights.com/industry-reports/artificial-intelligence-in-healthcare-market-100534
  date: '2026-10-26'
  quote: "CAGR: 43.96% from 2026–2034"
- claim: MarketsandMarkets forecasts 39.7% annual growth in healthcare AI through 2031.
  url: https://www.marketsandmarkets.com/Market-Reports/artificial-intelligence-healthcare-market-54679303.html
  date: 2026-06
  quote: "CAGR (2026–2031): 39.7%"
- claim: Precedence Research forecasts 35.02% healthcare AI growth from 2026 to 2035.
  url: https://www.precedenceresearch.com/artificial-intelligence-in-healthcare-market
  date: '2026-09-16'
  quote: "CAGR (2026-2035): 35.02%"
```

### ed051
```yaml
status: ok
section: Market size
title: What is a realistic CAGR for the healthcare AI market?
t:
  15: BEST CASE ≈ 45%
  17: "≈39%\nthrough 2031"
  19: Published forecasts range from 35% to 44%. We use 39% as a planning proxy. It is not a verified forecast for our narrower set of AI-first companies.
  16: WORST CASE ≈ 30%
note: We center an illustrative scenario on published market forecasts. The downside and upside are analyst assumptions, not independent industry predictions.
sources:
- claim: MarketsandMarkets estimates broad healthcare AI at $36.67B in 2026.
  url: https://www.marketsandmarkets.com/Market-Reports/artificial-intelligence-healthcare-market-54679303.html
  date: 2026-06
  quote: "Market Size (2026): USD 36.67 Billion"
- claim: Grand View Research forecasts 38.9% growth from 2026 to 2033.
  url: https://www.grandviewresearch.com/industry-analysis/artificial-intelligence-ai-healthcare-market
  date: 2026-06
  quote: "CAGR (2026-2033): 38.9%"
- claim: Precedence Research estimates broad healthcare AI at $51.20B in 2026.
  url: https://www.precedenceresearch.com/artificial-intelligence-in-healthcare-market
  date: '2026-09-16'
  quote: "Market Size in 2026: USD 51.20 Billion"
- claim: Fortune Business Insights estimates a 43.96% CAGR from 2026 to 2034.
  url: https://www.fortunebusinessinsights.com/industry-reports/artificial-intelligence-in-healthcare-market-100534
  date: '2026-10-26'
  quote: "CAGR: 43.96% from 2026–2034"
- claim: MarketsandMarkets forecasts 39.7% annual growth in healthcare AI through 2031.
  url: https://www.marketsandmarkets.com/Market-Reports/artificial-intelligence-healthcare-market-54679303.html
  date: 2026-06
  quote: "CAGR (2026–2031): 39.7%"
- claim: Precedence Research forecasts 35.02% healthcare AI growth from 2026 to 2035.
  url: https://www.precedenceresearch.com/artificial-intelligence-in-healthcare-market
  date: '2026-09-16'
  quote: "CAGR (2026-2035): 35.02%"
```

### ed052p
```yaml
status: no_data
title: How much bigger can healthcare AI get?
comment: A forecast cannot be computed responsibly without an evidenced 2026 base revenue for the strict healthcare-first AI scope and a matching forward CAGR.
sources: []
```
