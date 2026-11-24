### ed041
```yaml
status: ok
section: Market size
title: What counts as an AI data center, and what doesn't?
note: We count independently marketed AI-ready facility space and contracted power delivered to outside customers, not the chips or cloud services inside.
t:
  7: We define AI data centers as third-party facilities that rent out power, cooling and secure space built for dense AI computing loads.
  8: We include AI colocation, large leased AI campuses, powered buildings, and modular or edge facilities with real tenants.
  9: We exclude chip makers, power and cooling vendors, GPU rental alone, ordinary server rooms and internal-only AI sites.
sources:
- claim: Core Scientific sells site space power and cooling to third-party AI clients
  url: https://investors.corescientific.com/sec-filings/all-sec-filings/content/0001839341-26-000030/core-20260930.htm
  date: '2026-11-05'
  quote: The Company’s Colocation segment provides space, power, cooling, facilities operations, security and other services to third-party colocation customers
- claim: Colocation is the largest Fortune data center type in 2026
  url: https://www.fortunebusinessinsights.com/ai-data-center-market-110845
  date: '2026-11-02'
  quote: The colocation data center segment captured the largest market share in 2026.
- claim: Crusoe developing a 900 MW AI factory campus supporting Microsoft
  url: https://www.crusoe.ai/resources/newsroom/crusoe-announces-new-900-mw-ai-factory-campus-in-abilene-texas-to-support-microsoft-ai-infrastructure
  date: '2026-03-27'
  quote: Crusoe Announces New 900 MW AI Factory Campus in Abilene, Texas to Support Microsoft AI Infrastructure
```

### ed042
```yaml
status: ok
section: Market size
title: What are the market size estimates from different sources online?
rows:
- firm: 'Fortune

    Business Insights'
  value: $21B
  comment: Their estimate counts hardware, software and services at AI facilities. It is close to our proxy, but not a clean total for third-party site rent.
- firm: 'Ameco

    Research'
  value: $23B
  comment: Their market covers purpose-built AI facilities with GPU and power equipment. This is a useful nearby check, not a rental-only total.
- firm: 'OG

    Analysis'
  value: $47B
  comment: Their estimate spans cloud providers, colocated sites, and equipment. We treat its wider scope as an upper check, not rent earned by sites.
- firm: 'Grand View

    Research'
  value: $181B
  comment: Their much larger figure includes hardware and software. It is not comparable to what independent facility operators bill tenants.
note:
- We use the firms' published global 2026 estimates and round the figures to whole billions for display.
- We show their wider AI infrastructure markets separately from the rent-only estimate we build below.
sources:
- claim: Fortune estimates AI data center market of USD 21.27 billion in 2026
  url: https://www.fortunebusinessinsights.com/ai-data-center-market-110845
  date: '2026-11-02'
  quote: '2026 Market Size: USD 21.27 billion'
- claim: Hardware dominates the Fortune market definition
  url: https://www.fortunebusinessinsights.com/ai-data-center-market-110845
  date: '2026-11-02'
  quote: The hardware segment is projected to dominate the market
- claim: Ameco estimates the AI data center market at USD 22.85 billion in 2026
  url: https://www.amecoresearch.com/market-report/ai-data-center-market-277159
  date: '2026-10-17'
  quote: The market is estimated at USD 22.85 billion in 2026, with North America holding the largest share
- claim: OG Analysis estimates an AI data center market of USD 46.5 billion in 2026
  url: https://www.researchandmarkets.com/reports/6241937/artificial-intelligence-data-center-market
  date: 2026-11
  quote: The Artificial Intelligence (AI) Data Center Market is estimated at USD 46.5 billion in 2026
- claim: Grand View Research forecasts USD 180.6 billion in 2026
  url: https://www.grandviewresearch.com/industry-analysis/ai-data-center-market-report
  date: 2026-06
  quote: 'Estimated market size in 2026: USD 180.6 Billion'
- claim: Grand View counts hardware as 53.7% of its 2025 AI market
  url: https://www.grandviewresearch.com/industry-analysis/ai-data-center-market-report
  date: 2026-06
  quote: Hardware segment held the largest revenue share of 53.7% in 2025.
```

### ed043
```yaml
status: ok
section: Market size
title: Our own first-principles, bottom-up calculation of the market size
page: 1/2
note: We use global third-party facility revenue as the base, then make an explicit AI workload allocation instead of counting server sales.
t:
  21: We build a facility rent proxy, not a total for all AI hardware
  16: We start with what global operators earn from renting data center space
  15: We use Grand View's $99B 2026 global colocation market forecast
  14: We count rented halls, leased campus space and powered buildings
  9: We exclude server purchases, GPU hours, software and internal-only sites
  8: We use JLL's finding that AI took a quarter of workloads in 2025
  7: We apply that 25% AI mix to the $99B global site rental market
  6: We get about $25B in annual AI facility rent
  3: We compare Fortune's wider $21B AI data center market estimate
  2: We also compare Ameco's wider $23B industry estimate for 2026
  0: We do not treat those mixed hardware markets as facility sales
sources:
- claim: Grand View estimates USD 99.2 billion global colocation revenue in 2026
  url: https://www.grandviewresearch.com/industry-analysis/data-center-colocation-market
  date: 2026-06
  quote: 'Estimated market size in 2026: USD 99.2 Billion'
- claim: JLL says AI was a quarter of global data center workloads in 2025
  url: https://www.jll.com/en-us/insights/market-outlook/data-center-outlook
  date: '2026-01-05'
  quote: AI only represented about a quarter of all data center workloads in 2025, with training driving most of the demand.
- claim: Fortune estimates AI data center market of USD 21.27 billion in 2026
  url: https://www.fortunebusinessinsights.com/ai-data-center-market-110845
  date: '2026-11-02'
  quote: '2026 Market Size: USD 21.27 billion'
- claim: Ameco estimates the AI data center market at USD 22.85 billion in 2026
  url: https://www.amecoresearch.com/market-report/ai-data-center-market-277159
  date: '2026-10-17'
  quote: The market is estimated at USD 22.85 billion in 2026, with North America holding the largest share
- claim: Hardware dominates the Fortune market definition
  url: https://www.fortunebusinessinsights.com/ai-data-center-market-110845
  date: '2026-11-02'
  quote: The hardware segment is projected to dominate the market
```

### ed044
```yaml
status: ok
section: Market size
title: Our own first-principles, bottom-up calculation of the market size
page: 2/2
note: We round a workload-based rental proxy and check it against operator contracts. It is an estimate, not verified global site revenue.
t:
  21: We round the rental proxy to about $25B for 2026 facility sales
  16: We do not add new buildings or server purchases to annual site rent
  15: We keep future lease totals apart from current sales
  14: We test this against Applied Digital's $36B in future leases
  9: We do not count those long-term lease values as 2026 site sales
  8: We test JLL's forecast of half of AI workloads by 2030
  7: We note Fortune's $21B and Ameco's $23B wider market estimates
  6: We set aside Grand View's $181B figure because it includes hardware
  3: We call $25B a modeled 2026 proxy, not an audited market total
  2: We warn that AI workload share may not equal its share of rent
  0: We estimate annual AI facility revenue near $25B worldwide
sources:
- claim: Grand View estimates USD 99.2 billion global colocation revenue in 2026
  url: https://www.grandviewresearch.com/industry-analysis/data-center-colocation-market
  date: 2026-06
  quote: 'Estimated market size in 2026: USD 99.2 Billion'
- claim: JLL says AI was a quarter of global data center workloads in 2025
  url: https://www.jll.com/en-us/insights/market-outlook/data-center-outlook
  date: '2026-01-05'
  quote: AI only represented about a quarter of all data center workloads in 2025, with training driving most of the demand.
- claim: JLL forecasts AI may reach half of global data center workloads by 2030
  url: https://www.jll.com/en-us/insights/market-outlook/data-center-outlook
  date: '2026-01-05'
  quote: By 2030, AI could represent half of all workloads with inference becoming the primary driver.
- claim: Applied Digital has approximately USD 36 billion in contracted lease revenue over base terms
  url: https://www.sec.gov/Archives/edgar/data/1144879/000114487926000057/apldq127earningsrelease.htm
  date: '2026-10-07'
  quote: Those leases represent approximately $36 billion of contracted revenue over their initial base terms
- claim: Fortune estimates AI data center market of USD 21.27 billion in 2026
  url: https://www.fortunebusinessinsights.com/ai-data-center-market-110845
  date: '2026-11-02'
  quote: '2026 Market Size: USD 21.27 billion'
- claim: Ameco estimates the AI data center market at USD 22.85 billion in 2026
  url: https://www.amecoresearch.com/market-report/ai-data-center-market-277159
  date: '2026-10-17'
  quote: The market is estimated at USD 22.85 billion in 2026, with North America holding the largest share
- claim: Grand View Research forecasts USD 180.6 billion in 2026
  url: https://www.grandviewresearch.com/industry-analysis/ai-data-center-market-report
  date: 2026-06
  quote: 'Estimated market size in 2026: USD 180.6 Billion'
- claim: Grand View counts hardware as 53.7% of its 2025 AI market
  url: https://www.grandviewresearch.com/industry-analysis/ai-data-center-market-report
  date: 2026-06
  quote: Hardware segment held the largest revenue share of 53.7% in 2025.
```

### ed045
```yaml
status: ok
section: Market size
title: How much is the AI data center market worth today?
t:
  6: $25B
  8: 'We estimate $25B of AI site rent in 2026 using a 25% AI workload proxy and a $99B global colocation market. This is uncertain: market reports often include chips and software, which we exclude.'
  4: '2026'
sources:
- claim: Grand View estimates USD 99.2 billion global colocation revenue in 2026
  url: https://www.grandviewresearch.com/industry-analysis/data-center-colocation-market
  date: 2026-06
  quote: 'Estimated market size in 2026: USD 99.2 Billion'
- claim: JLL says AI was a quarter of global data center workloads in 2025
  url: https://www.jll.com/en-us/insights/market-outlook/data-center-outlook
  date: '2026-01-05'
  quote: AI only represented about a quarter of all data center workloads in 2025, with training driving most of the demand.
- claim: Hardware dominates the Fortune market definition
  url: https://www.fortunebusinessinsights.com/ai-data-center-market-110845
  date: '2026-11-02'
  quote: The hardware segment is projected to dominate the market
```

### ed047p
```yaml
status: no_data
section: Market size
title: How is the AI data center market split between its categories?
comment: No verified 2026 revenue split exists across the seven specified company categories. Operator revenue is private or blends facility rent with GPUs, equipment and construction. Assigning percentage shares would be speculative.
sources:
- claim: Colocation is the largest Fortune data center type in 2026
  url: https://www.fortunebusinessinsights.com/ai-data-center-market-110845
  date: '2026-11-02'
  quote: The colocation data center segment captured the largest market share in 2026.
- claim: Grand View counts hardware as 53.7% of its 2025 AI market
  url: https://www.grandviewresearch.com/industry-analysis/ai-data-center-market-report
  date: 2026-06
  quote: Hardware segment held the largest revenue share of 53.7% in 2025.
```

### ed048
```yaml
status: ok
section: Market size
title: What is behind these categories?
t:
  5: 'AI COLOCA

    TION FACILI

    TIES'
  8: HYPERSCALE AI CAMPUSES
  10: POWERED AI CAMPUS DEVELOPERS
  11: 🏢
  4: Operators rent secure halls with power and cooling to AI tenants, usually on long contracts for space and support.
  12: 🏗️
  7: Huge purpose-built sites house dense AI server clusters for a major tenant, with space delivered in stages as power arrives.
  9: Developers secure land, grid power and a ready building shell, then lease the site for customers to equip and run.
  15: ''
  17: ''
  18: ''
  19: ''
  14: ''
  16: ''
holes_ok: true
sources:
- claim: Core Scientific sells site space power and cooling to third-party AI clients
  url: https://investors.corescientific.com/sec-filings/all-sec-filings/content/0001839341-26-000030/core-20260930.htm
  date: '2026-11-05'
  quote: The Company’s Colocation segment provides space, power, cooling, facilities operations, security and other services to third-party colocation customers
- claim: Crusoe developing a 900 MW AI factory campus supporting Microsoft
  url: https://www.crusoe.ai/resources/newsroom/crusoe-announces-new-900-mw-ai-factory-campus-in-abilene-texas-to-support-microsoft-ai-infrastructure
  date: '2026-03-27'
  quote: Crusoe Announces New 900 MW AI Factory Campus in Abilene, Texas to Support Microsoft AI Infrastructure
- claim: Applied Digital has approximately USD 36 billion in contracted lease revenue over base terms
  url: https://www.sec.gov/Archives/edgar/data/1144879/000114487926000057/apldq127earningsrelease.htm
  date: '2026-10-07'
  quote: Those leases represent approximately $36 billion of contracted revenue over their initial base terms
- claim: Core Scientific signed approximately 530 MW with AMD and a neocloud in 2026
  url: https://investors.corescientific.com/sec-filings/all-sec-filings/content/0001839341-26-000030/core-20260930.htm
  date: '2026-11-05'
  quote: In July 2026, we announced our second HDC contract with AMD and a Neocloud counterparty
```

### ed049
```yaml
status: ok
section: Market size
title: Where in the world is AI data center money spent?
regions:
  na:
    pct: 32.5
    text: North America leads this broad AI infrastructure spending mix at 32.5%. The US has large cloud tenants and leased AI campuses.
  eu:
    pct: 29.9
    text: Europe accounts for 29.9% in Fortune's estimate. London, Frankfurt and Paris attract AI space despite tight power supply.
  apac:
    pct: 26.8
    text: Asia-Pacific holds 26.8%. AI data center demand spans China, Japan, India and Southeast Asia.
  latam:
    pct: 6.2
    text: Latin America represents 6.2% of Fortune's broad market. New data center capacity is growing in Brazil and Mexico.
  mea:
    pct: 4.7
    text: The Middle East and Africa make up 4.7%. The UAE and Saudi Arabia are pushing several large new AI facility plans.
note:
- We use Fortune Business Insights' 2025 regional mix for the wider AI data center market as a proxy.
- We do not claim these percentages measure rental-only revenue. Published shares total 100.1% from rounding.
sources:
- claim: Fortune global AI data center market valued at USD 17.73 billion in 2025
  url: https://www.fortunebusinessinsights.com/ai-data-center-market-110845
  date: '2026-11-02'
  quote: '2025 Market Size: USD 17.73 billion'
- claim: Fortune North America market was USD 5.76 billion in 2025
  url: https://www.fortunebusinessinsights.com/ai-data-center-market-110845
  date: '2026-11-02'
  quote: North America maintained a strong presence in the global market, reaching USD 5.76 billion in 2025
- claim: Fortune Europe market was USD 5.3 billion in 2025
  url: https://www.fortunebusinessinsights.com/ai-data-center-market-110845
  date: '2026-11-02'
  quote: In 2025, Europe generated USD 5.3 billion
- claim: Fortune Asia Pacific market was USD 4.75 billion in 2025
  url: https://www.fortunebusinessinsights.com/ai-data-center-market-110845
  date: '2026-11-02'
  quote: The Asia Pacific market accounted for USD 4.75 billion in 2025
- claim: Fortune Latin America market was USD 1.09 billion in 2025
  url: https://www.fortunebusinessinsights.com/ai-data-center-market-110845
  date: '2026-11-02'
  quote: with a valuation of USD 1.09 billion
- claim: Fortune Middle East and Africa market was USD 0.83 billion in 2025
  url: https://www.fortunebusinessinsights.com/ai-data-center-market-110845
  date: '2026-11-02'
  quote: In 2025, Middle East & Africa represented USD 0.83 billion
```

### ed050
```yaml
status: ok
section: Market size
title: What are the growth rate estimates from different sources online?
note: We compare four forecasts for the wider AI data center ecosystem. Their hardware and cloud scope makes them directional, not pure rent growth.
t:
  24: FIRM
  25: CAGR
  26: COMMENTS
  6: 'Fortune

    Business Insights'
  5: '≈25.8%

    through 2034'
  7: Their forecast includes AI servers, software and services. It sets a reference pace but does not isolate leased facilities.
  10: 'Ameco

    Research'
  9: '≈28.1%

    through 2035'
  11: They expect fast demand growth for purpose-built AI sites. Their estimate still blends buildings and the machines inside.
  14: 'OG

    Analysis'
  13: '≈28.6%

    through 2034'
  15: Their wider market includes cloud providers and equipment. We use the forecast as an upside check for site rent growth.
  18: 'Grand View

    Research'
  17: '≈23.9%

    through 2033'
  19: Their large market includes chips and software. We use the slower forecast to check how growth might ease as capacity expands.
sources:
- claim: Fortune forecasts 25.8% CAGR through 2034
  url: https://www.fortunebusinessinsights.com/ai-data-center-market-110845
  date: '2026-11-02'
  quote: from USD 21.27 billion in 2026 to USD 133.51 billion by 2034
- claim: Ameco forecasts 28.1% CAGR from 2026 to 2035
  url: https://www.amecoresearch.com/market-report/ai-data-center-market-277159
  date: '2026-10-17'
  quote: growing at a CAGR of 28.1% from 2026 to 2035.
- claim: OG Analysis forecasts 28.6% CAGR for 2026 to 2034
  url: https://www.researchandmarkets.com/reports/6241937/artificial-intelligence-data-center-market
  date: 2026-11
  quote: growing at a CAGR of 28.6% during 2026-2034.
- claim: Grand View Research forecasts 23.9% CAGR from 2026 to 2033
  url: https://www.grandviewresearch.com/industry-analysis/ai-data-center-market-report
  date: 2026-06
  quote: 'CAGR (2026-2033): 23.9%'
- claim: Grand View counts hardware as 53.7% of its 2025 AI market
  url: https://www.grandviewresearch.com/industry-analysis/ai-data-center-market-report
  date: 2026-06
  quote: Hardware segment held the largest revenue share of 53.7% in 2025.
```

### ed051
```yaml
status: ok
section: Market size
title: What is a realistic CAGR for the AI data center market?
note: We use 26% facility-revenue growth through 2030 as a scenario, bracketed by 18% and 32%. It is not a published landlord forecast.
t:
  15: BEST CASE ≈ 32%
  17: '≈26%

    through 2030'
  19: AI still takes a small share of site workloads, but demand is moving fast. We choose 26% below the fastest reports, with grid access and delays holding back growth.
  16: WORST CASE ≈ 18%
sources:
- claim: JLL says AI was a quarter of global data center workloads in 2025
  url: https://www.jll.com/en-us/insights/market-outlook/data-center-outlook
  date: '2026-01-05'
  quote: AI only represented about a quarter of all data center workloads in 2025, with training driving most of the demand.
- claim: JLL forecasts AI may reach half of global data center workloads by 2030
  url: https://www.jll.com/en-us/insights/market-outlook/data-center-outlook
  date: '2026-01-05'
  quote: By 2030, AI could represent half of all workloads with inference becoming the primary driver.
- claim: JLL projects 14% data center growth through 2030
  url: https://www.jll.com/en-us/insights/market-outlook/data-center-outlook
  date: '2026-01-05'
  quote: The global data center sector will likely expand at a 14% CAGR through 2030
- claim: Fortune forecasts 25.8% CAGR through 2034
  url: https://www.fortunebusinessinsights.com/ai-data-center-market-110845
  date: '2026-11-02'
  quote: from USD 21.27 billion in 2026 to USD 133.51 billion by 2034
- claim: Ameco forecasts 28.1% CAGR from 2026 to 2035
  url: https://www.amecoresearch.com/market-report/ai-data-center-market-277159
  date: '2026-10-17'
  quote: growing at a CAGR of 28.1% from 2026 to 2035.
- claim: OG Analysis forecasts 28.6% CAGR for 2026 to 2034
  url: https://www.researchandmarkets.com/reports/6241937/artificial-intelligence-data-center-market
  date: 2026-11
  quote: growing at a CAGR of 28.6% during 2026-2034.
- claim: Grand View Research forecasts 23.9% CAGR from 2026 to 2033
  url: https://www.grandviewresearch.com/industry-analysis/ai-data-center-market-report
  date: 2026-06
  quote: 'CAGR (2026-2033): 23.9%'
```
