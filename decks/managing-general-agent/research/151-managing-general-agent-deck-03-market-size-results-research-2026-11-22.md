### ed041
```yaml
status: ok
section: Market size
title: What counts as a Managing General Agent, and what does not?
note: We count firms that make insurance decisions under authority from a separate risk-bearing insurer, not firms that only sell policies.
t:
  7: We define an MGA as a specialist firm that designs, prices, selects or binds insurance on behalf of a licensed insurer that carries
    the risk.
  8: We include MGUs, program managers with binding powers, embedded insurance MGAs and technology-led firms that make risk decisions.
  9: We exclude brokers that only place policies, insurers carrying their own risk, software sellers, claims vendors and carrier-only
    partners.
sources:
- claim: Delegated underwriting role and licensed insurer relationship
  url: https://web.ambest.com/docs/default-source/events/2026/imb-apcia-2026-presentation-slides.pdf
  date: '2026-11-02'
  quote: The MGA has become responsible for many of the activities traditionally performed by an insurance company
- claim: Companies underwriting or binding risks on behalf of another insurer
  url: https://insuramore.com/downloads/globalvista_us/
  date: undated
  quote: entities with the authority to underwrite or bind insurance risks and that do this exclusively or mainly on behalf of unaffiliated
    underwriters.
```

### ed042
```yaml
status: ok
section: Market size
title: What are the market size estimates from different sources online?
rows:
- firm: Howden Re
  value: $160B
  comment: Global MGA premiums in 2025, including firms tied to insurers. It is a channel benchmark, not our independent-only number.
- firm: Insuramore
  value: '>$250B'
  comment: Global premiums across all insurance types in 2024. This wider count includes broker-owned underwriting groups and other
    channels.
- firm: Conning
  value: $128B
  comment: US premiums in 2025, including Lloyd's and unreported business. It also counts insurer-owned MGA operations.
- firm: AM Best
  value: $109B
  comment: US direct premiums in 2025 from statutory filings, rounded from USD 108.7 billion. Smaller programs may not be visible.
note:
- We compare written premiums, not MGA fees. Country scope, insurer ownership and reporting gaps explain much of the difference.
- We do not add these estimates together. Global figures cover more markets, while US sources use different reporting filters.
sources:
- claim: Howden Re estimates about $160B in 2025 global MGA premiums
  url: https://www.insurancebusinessmag.com/reinsurance/news/breaking-news/european-mga-market-swells-as-it-doubles-us-growth-pace--howden-re-574701.aspx
  date: '2026-05-11'
  quote: Global MGA premium reached about $160 billion (€142 billion) last year, up 10%
- claim: Insuramore estimates over $250B global MGA premiums for 2024
  url: https://www.insuramore.com/wp-content/uploads/press_release_global_insurance_mga-mgu.pdf
  date: '2025-07-10'
  quote: globally, over USD 250 billion in premiums across all classes are likely to have been written by MGAs in 2024.
- claim: Conning estimates $128B US MGA premium for 2025
  url: https://www.conning.com/about-us/news/ir-pr---mga-2026
  date: '2026-07-28'
  quote: with Conning estimating total premium reached approximately $128 billion.
- claim: AM Best calculates USD 108.7 billion direct US MGA premiums for 2025
  url: https://news.ambest.com/pr/PressContent.aspx?altsrc=2&refnum=37486
  date: '2026-06-30'
  quote: Total direct premiums written sourced from DUAEs reached $108.7 billion in 2025, up from $92.3 billion in 2024
```

### ed043
```yaml
status: ok
section: Market size
title: Our own first-principles, bottom-up calculation of the market size
page: 1/2
note: We use direct premium managed by independent MGA operators as our unit, then adjust published totals that include carrier-owned
  programs.
t:
  21: We estimate premium run by independent MGAs, not insurer sales
  16: We begin with the US, where insurer filings show delegated policy premiums
  15: We use Conning because it splits firms owned by insurers from other MGAs
  14: We count only MGA programs with real authority to price or bind policies
  9: We leave out pure brokers, the insurers taking the risk and software vendors
  8: We use 2025 reported data, then make one clear estimate for 2026
  7: We start from about $48B in US premiums reported by nonaffiliated MGAs
  6: We compare this with Conning's $103B total in filings
  3: We note Conning adds Lloyd's and smaller unreported US programs
  2: We use $128B as the wider US total, not as our target figure
  0: We also check Howden's global $160B to avoid double counting
sources:
- claim: US nonaffiliated MGA 2025 premiums USD 47.5 billion
  url: https://www.theinsurer.com/program-manager/news/conning-naic-data-shows-us-mga-premium-volume-hit-1028-billion-in-2025-2026-07-29/
  date: '2026-07-29'
  quote: with the former generating $46.6 billion of reported premium volume and the latter $47.5 billion.
- claim: Conning USD 102.6 billion statutory premium and $128B wider US total
  url: https://www.conning.com/about-us/news/ir-pr---mga-2026
  date: '2026-07-28'
  quote: Statutory filings reported $102.6 billion in MGA direct premium written, up 12% from 2024
- claim: Conning $128B wider US reported plus other streams
  url: https://www.conning.com/about-us/news/ir-pr---mga-2026
  date: '2026-07-28'
  quote: with Conning estimating total premium reached approximately $128 billion.
- claim: Howden global MGA premium $160B in 2025
  url: https://www.insurancebusinessmag.com/reinsurance/news/breaking-news/european-mga-market-swells-as-it-doubles-us-growth-pace--howden-re-574701.aspx
  date: '2026-05-11'
  quote: Global MGA premium reached about $160 billion (€142 billion) last year, up 10%
```

### ed044
```yaml
status: ok
section: Market size
title: Our own first-principles, bottom-up calculation of the market size
page: 2/2
note: We extend the US independent share to its missing premiums, use Howden for Europe, and assign a cautious share elsewhere before
  one-year growth.
t:
  21: We add $25B of US premium missing from Conning's filing total
  16: We apply the reported nonaffiliated share to the missing US volume
  15: We estimate $59B of independent MGA premium in the US
  14: We take Howden's $23B European total for the same year
  9: We use 77.5% for Europe, the midpoint of its major independent firms
  8: We estimate about $18B of European independent MGA premium
  7: We take $9B for other regions after the US and Europe are removed
  6: We assume 65% of that smaller pool meets our independent MGA definition
  3: We total about $83B globally in independent 2025 premiums
  2: We apply 10% growth for 2026, close to recent US and world gains
  0: We round our 2026 estimate to about $91B in managed premiums
comment: 'Analyst scenario, not a published statistic: 2025 US USD 47.5 billion + ($128B-USD 102.6 billion) x (USD 47.5 billion/USD
  102.6 billion) = USD 59.3 billion. Europe $23B x 77.5% = USD 17.8 billion. Rest ($160B-$128B-$23B) x 65% = $5.9B. The 2025 sum $83B.
  Apply 10% to get about $91B in 2026. The 65% rest-of-world and Europe midpoint assumptions are unverified. Nonaffiliated US firms
  can also be broker-owned, so the result is not a verified independent-only total.'
sources:
- claim: Conning US totals USD 102.6 billion and $128B in 2025
  url: https://www.conning.com/about-us/news/ir-pr---mga-2026
  date: '2026-07-28'
  quote: Statutory filings reported $102.6 billion in MGA direct premium written, up 12% from 2024
- claim: US wider Conning total $128B
  url: https://www.conning.com/about-us/news/ir-pr---mga-2026
  date: '2026-07-28'
  quote: with Conning estimating total premium reached approximately $128 billion.
- claim: US nonaffiliated reported premium USD 47.5 billion
  url: https://www.theinsurer.com/program-manager/news/conning-naic-data-shows-us-mga-premium-volume-hit-1028-billion-in-2025-2026-07-29/
  date: '2026-07-29'
  quote: with the former generating $46.6 billion of reported premium volume and the latter $47.5 billion.
- claim: Europe premiums $23B and 70%-85% of premiums at established independent firms
  url: https://www.howdenre.com/news-insights/howden-re-publishes-filtered-for-quality-a-refined-view-of-europes-mga-market
  date: '2026-05-08'
  quote: European MGA gross written premium reached approximately US$23 billion in 2025, up 15% year-on-year
- claim: Established independent Europe group generates 70%-85% of premium
  url: https://www.howdenre.com/news-insights/howden-re-publishes-filtered-for-quality-a-refined-view-of-europes-mga-market
  date: '2026-05-08'
  quote: represent around 30% of the European market by entity count but generate between 70% and 85% of total premium.
- claim: Global broad MGA premiums about $160B
  url: https://www.insurancebusinessmag.com/reinsurance/news/breaking-news/european-mga-market-swells-as-it-doubles-us-growth-pace--howden-re-574701.aspx
  date: '2026-05-11'
  quote: Global MGA premium reached about $160 billion (€142 billion) last year, up 10%
- claim: Gallagher Re observed about 10% US MGA growth in 2025
  url: https://www.ajg.com/gallagherre/news-and-insights/mgas-remain-at-the-growth-epicenter-of-insurance/
  date: '2026-05-19'
  quote: representing growth of approximately +10%.
```

### ed045
```yaml
status: ok
section: Market size
title: How much is the Managing General Agent market worth today?
t:
  6: $91B
  8: We estimate $91B of 2026 premiums managed by independent MGAs worldwide. This excludes insurer-owned programs and is not MGA revenue.
    Howden puts the wider global channel near $160B in 2025.
  4: '2026'
note: We estimate independent MGA-managed premiums from US ownership data and European market research. The published total for all
  MGAs is larger.
comment: Approximate 2026 analyst scenario, not an observed global total. Underlying 2025 independent-premium estimate is $83B with
  an assumed 10% rise.
sources:
- claim: Conning reports USD 47.5 billion US nonaffiliated MGA premium in 2025
  url: https://www.theinsurer.com/program-manager/news/conning-naic-data-shows-us-mga-premium-volume-hit-1028-billion-in-2025-2026-07-29/
  date: '2026-07-29'
  quote: with the former generating $46.6 billion of reported premium volume and the latter $47.5 billion.
- claim: Howden wider worldwide estimate $160B for 2025
  url: https://www.insurancebusinessmag.com/reinsurance/news/breaking-news/european-mga-market-swells-as-it-doubles-us-growth-pace--howden-re-574701.aspx
  date: '2026-05-11'
  quote: Global MGA premium reached about $160 billion (€142 billion) last year, up 10%
- claim: Howden Europe premiums $23B in 2025
  url: https://www.howdenre.com/news-insights/howden-re-publishes-filtered-for-quality-a-refined-view-of-europes-mga-market
  date: '2026-05-08'
  quote: European MGA gross written premium reached approximately US$23 billion in 2025, up 15% year-on-year
```

### ed048
```yaml
status: ok
section: Market size
title: What is behind these categories?
t:
  5: SPECIALTY RISK
  8: PERSONAL COVER
  10: PROGRAM MGAS
  11: 🛡️
  4: Cyber and technology, Commercial and specialty, Property and catastrophe, and Parametric and climate MGAs price risks.
  12: 🚗
  7: Motor and mobility, Consumer and travel, and Life and health MGAs make tailored policies with an insurer taking the risk.
  9: Embedded and program MGAs run cover in partner sales journeys, with real pricing or binding powers from insurers.
  15: ''
  17: ''
  18: ''
  19: ''
  14: ''
  16: ''
holes_ok: true
note: We group eight underwriting specialties into three visual families. The MGA must control some risk decisions, not just sell coverage.
sources:
- claim: MGAs take on product development and risk selection for insurers
  url: https://web.ambest.com/docs/default-source/events/2026/imb-apcia-2026-presentation-slides.pdf
  date: '2026-11-02'
  quote: The MGA has become responsible for many of the activities traditionally performed by an insurance company
- claim: MGA authority means underwriting or binding delegated risk
  url: https://insuramore.com/downloads/globalvista_us/
  date: undated
  quote: entities with the authority to underwrite or bind insurance risks and that do this exclusively or mainly on behalf of unaffiliated
    underwriters.
```

### ed049
```yaml
status: no_data
section: Market size
title: Where in the world is Managing General Agent money spent?
comment: No verified five-region MGA premium split is available. Howden publishes US, Europe and rest-of-world shares, but not separate
  Asia-Pacific, Latin America and Middle East/Africa figures for the defined independent-MGA scope.
```

### ed050
```yaml
status: ok
section: Market size
title: What are the growth rate estimates from different sources online?
note: We compare the latest published growth evidence. Howden gives a historical global CAGR, while the other figures are US year-on-year
  gains, not forward forecasts.
t:
  24: FIRM
  25: CAGR
  26: COMMENTS
  6: Howden Re
  5: ≈ 16%\n2019-2024
  7: Howden measures broad global MGA premium growth over five years. This is a historical CAGR, not an outlook for independent firms.
  10: Conning
  9: ≈ 12%\nin 2025
  11: Conning shows a US statutory premium rise in 2025. It is a one-year gain, not a forecast, and includes insurer-owned units.
  14: Gallagher Re
  13: ≈ 10%\nin 2025
  15: Gallagher tracks a wider US program market including premiums outside filings. It is the lower recent pace we use for context.
  18: AM Best
  17: ≈ 17.8%\nin 2025
  19: AM Best finds faster US MGA premium growth than Conning using its own filings review. These one-year growth rates should not be
    averaged.
sources:
- claim: Howden global MGA premiums grew at a 16% historical CAGR from 2019 to 2024
  url: https://www.howdengroupholdings.com/sites/default/files/2025-12/howden-re-balancing-2026-FINAL.pdf
  date: '2026-01-02'
  quote: rising from US$70 billion to US$150 billion and registering a compound annual growth rate (CAGR) of 16%
- claim: Conning reports 12% statutory growth in US 2025
  url: https://www.conning.com/about-us/news/ir-pr---mga-2026
  date: '2026-07-28'
  quote: Statutory filings reported $102.6 billion in MGA direct premium written, up 12% from 2024
- claim: Gallagher Re reports around 10% growth in 2025
  url: https://www.ajg.com/gallagherre/news-and-insights/mgas-remain-at-the-growth-epicenter-of-insurance/
  date: '2026-05-19'
  quote: representing growth of approximately +10%.
- claim: AM Best chart shows 17.8% growth in US MGA direct premiums in 2025
  url: https://riskandinsurance.com/mga-premiums-hit-108-7-billion-in-2025-as-capacity-scrutiny-tightens/
  date: '2026-07-03'
  quote: Managing general agents and other delegated underwriting authority enterprises wrote $108.7 billion in direct premiums in 2025,
    up 17.8% from $92.3 billion in 2024
```

### ed051
```yaml
status: ok
section: Market size
title: What is a realistic CAGR for the Managing General Agent market?
note: We use a projected 11% annual rise in independent MGA-managed premiums, below past global growth and near current US premium growth.
t:
  15: BEST CASE ≈ 15%
  17: ≈11%\nto 2030
  19: MGA premiums can grow as insurers hand off niche risks, but softer pricing and tougher checks on loss results could slow expansion.
    We choose 11% near recent US gains.
  16: WORST CASE ≈ 6%
comment: The 6%, 11% and 15% rates are NewMarketPitch scenarios, not quoted publisher forecasts. The base case refers to independent
  MGA-managed gross premiums for 2026-2030.
sources:
- claim: Conning reported 12% 2025 MGA statutory premium growth
  url: https://www.conning.com/about-us/news/ir-pr---mga-2026
  date: '2026-07-28'
  quote: Statutory filings reported $102.6 billion in MGA direct premium written, up 12% from 2024
- claim: Gallagher Re reported around 10% 2025 US MGA premium growth
  url: https://www.ajg.com/gallagherre/news-and-insights/mgas-remain-at-the-growth-epicenter-of-insurance/
  date: '2026-05-19'
  quote: representing growth of approximately +10%.
- claim: Howden reports 16% 2019-2024 global MGA premium CAGR
  url: https://www.howdengroupholdings.com/sites/default/files/2025-12/howden-re-balancing-2026-FINAL.pdf
  date: '2026-01-02'
  quote: rising from US$70 billion to US$150 billion and registering a compound annual growth rate (CAGR) of 16%
- claim: Capacity providers are more selective about underwriting quality
  url: https://news.ambest.com/pr/PressContent.aspx?altsrc=2&refnum=37486
  date: '2026-06-30'
  quote: the capacity being afforded this sector is becoming more selective and more dialed-in on long-term underwriting quality
```
