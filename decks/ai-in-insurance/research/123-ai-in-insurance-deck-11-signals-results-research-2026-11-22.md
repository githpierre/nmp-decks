# AI in Insurance: Ranked Signals for NewMarketPitch

**Research cut-off:** November 22, 2026  
**Selected candidates:** 12  
**Market opportunity candidates:** 7  
**Format types with a candidate:** 9 of 31

## Scope and editorial guardrails

The startup universe is limited to independent AI-material insurance carriers, brokers, MGAs and vertical AI software businesses founded in or after 2000 (including later listed/acquired exceptions). Incumbent data, industry surveys and regulator statistics are used as **market signals**, not to add incumbents to the startup universe. The selection avoids funding-round research, undated pilot-as-production claims, and Google Trends. The `fresh` field for cross-sectional surveys/deals/price observations records the evidence vintage, not a monthly adoption time series. All sources were accessible or indexed by the research cut-off. Any percentage based on a company internal metric is labeled accordingly.

### Ranked index

| Rank | Score / 20 | Format | Chapter | Slide headline |
|---:|---:|---|---|---|
| 1 | 19 | key-trend | Market opportunity | Insurers using AI more than doubled to 62% |
| 2 | 19 | cost-threshold | Value creation | Lemonade cut its claims-handling cost ratio below the incumbent benchmark |
| 3 | 19 | kpi-trio | Market opportunity | Kalepa tripled revenue and customers as work volume quadrupled |
| 4 | 18 | deal-timeline | Market opportunity | Incumbents moved from pilots to buying insurance AI platforms |
| 5 | 18 | key-trend | Market opportunity | Lemonade automated 82% of customer service interactions |
| 6 | 18 | icon-grid | Market opportunity | Most companies say AI-attack risk is not insured |
| 7 | 17 | forecast-gap | Market size | Published AI-insurance market forecasts disagree by sevenfold |
| 8 | 17 | icon-grid | Market opportunity | More than one-third of consumers would bend a claims photo |
| 9 | 17 | kpi-trio | Market opportunity | Lemonade revenue grew 73% as premium volume rose 34% |
| 10 | 16 | profit-gap | Value creation | Root turns a profit while Lemonade still loses money |
| 11 | 16 | fallen-star | Startup killers | Lemonade closed at $35.46 versus a $183.26 peak |
| 12 | 14 | rules-wave | Market challenges | AI litigation has accelerated sharply in the US and abroad |

## Slide-ready YAML candidates

### 1. Insurers using AI more than doubled to 62% (19/20)

```yaml
format: key-trend
title: Insurers using AI more than doubled to 62%
chapter: Market opportunity
why_it_matters: AI is rapidly becoming mainstream among insurers, opening a larger buyer base for specialist AI vendors. The survey measures reported use
  of any AI, not purchases from AI-first startups.
data:
- label: 2024 insurance respondents currently using AI
  value: 29
  unit: '%'
  date: 2024-03
- label: 2025 insurance respondents currently using AI
  value: 48
  unit: '%'
  date: 2025-03
- label: 2026 insurance respondents currently using AI
  value: 62
  unit: '%'
  date: 2026-02
note: We use Goldman Sachs Asset Management Global Insurance Survey annual responses for 2024, 2025 and 2026, with identical AI-use question wording. We
  use the 2026 survey collected January 11 to February 3 from 434 respondents; the 2026-to-2024 ratio is 2.14x and composition can change between survey
  waves.
fresh:
  period: year
  end: 2026-02
scores:
  surprise: 5
  importance: 5
  clarity: 5
  durability: 4
total_score: 19
sources:
- claim: Comparable three-wave AI usage chart
  url: https://am.gs.com/cms-assets/gsam-app/documents/insights/en/2026/am-Insurance-survey-2026.pdf?view=true
  date: 2026-03
  quote: The number of respondents currently using AI increased by 14-percentage points year-over-year and 33-percentage points since 2024.
- claim: 2026 use and sample
  url: https://am.gs.com/en-no/advisors/news/press-release/2026/press-insurance-survey-2026
  date: 2026-03
  quote: Most insurers are either currently using (62%) or considering the use (34%) of Artificial Intelligence (AI).
```

### 2. Lemonade cut its claims-handling cost ratio below the incumbent benchmark (19/20)

```yaml
format: cost-threshold
title: Lemonade cut its claims-handling cost ratio below the incumbent benchmark
chapter: Value creation
why_it_matters: The AI-native carrier has reduced claim-adjustment overhead substantially while growing the premium base. If durable, the lower cost base
  is an underwriting and pricing advantage, although the incumbent comparison is company-reported.
data:
- label: Lemonade Q3 2022
  value: 13
  unit: LAE ratio %, excluding PPD
  date: '2022-09-30'
- label: Lemonade Q3 2023
  value: 11
  unit: LAE ratio %, excluding PPD
  date: '2023-09-30'
- label: Lemonade Q3 2024
  value: 9
  unit: LAE ratio %, excluding PPD
  date: '2024-09-30'
- label: Lemonade Q3 2025
  value: 7
  unit: LAE ratio %, excluding PPD
  date: '2025-09-30'
- label: Lemonade Q3 2026
  value: 5
  unit: LAE ratio %, excluding PPD
  date: '2026-09-30'
- label: Large-incumbent reference, company-reported
  value: 9
  unit: LAE ratio %, approximate reference
  date: '2025-09-30'
note: We use Lemonade Q3 shareholder letters for 2022-2025 historical LAE excluding prior-period development, and its Q3 2026 insurance supplement for the
  latest actual ratio. We compare against Lemonade's approximate 9% incumbent reference from November 2025, not an independently standardized industry average;
  no Q4/year-end values are substituted for Q3.
fresh:
  period: quarter
  end: 2026-09
scores:
  surprise: 5
  importance: 5
  clarity: 5
  durability: 4
total_score: 19
sources:
- claim: Q3 2022 to Q3 2025 series
  url: https://www.lemonade.com/investor-relations-bo/wp-content/uploads/2025/11/LMND-Shareholder-Letter_Q3_25.pdf
  date: '2025-11-05'
  quote: Over the past three years, we’ve almost halved our LAE ratio, from 13% to 7%
- claim: 2026 Q3 LAE ratio of 5%
  url: https://www.lemonade.com/investor-relations-bo/wp-content/uploads/docs/LMND-Shareholder-Letter-Q3-2026.pdf
  date: '2026-11-05'
  quote: LAE (excl. PPD) 7% 6% 6% 5% 5%
- claim: Company-reported large incumbent reference
  url: https://www.lemonade.com/investor-relations-bo/wp-content/uploads/2025/11/LMND-Shareholder-Letter_Q3_25.pdf
  date: '2025-11-05'
  quote: many leading incumbents report LAE ratios around 9%
```

### 3. Kalepa tripled revenue and customers as work volume quadrupled (19/20)

```yaml
format: kpi-trio
title: Kalepa tripled revenue and customers as work volume quadrupled
chapter: Market opportunity
why_it_matters: A specialist insurer AI platform reporting simultaneous growth in customers, revenue and workload suggests buyers are scaling production
  use, not merely pilots. These are company-disclosed multipliers, not audited revenue figures.
data:
- label: Revenue growth over preceding year
  value: 3
  unit: x prior-year level
  date: '2026-11-05'
- label: Customer count growth over preceding year
  value: 3
  unit: x prior-year level
  date: '2026-11-05'
- label: Volume of work running through platform
  value: 4
  unit: x prior-year level
  date: '2026-11-05'
note: We use Kalepa's November 5, 2026 company update for changes across the preceding approximately 12 months; absolute revenue and customer counts were
  not disclosed. We omit the financing information from the source, because funding rounds belong in NewMarketPitch's internal database.
fresh:
  period: year
  end: 2026-11
scores:
  surprise: 5
  importance: 5
  clarity: 5
  durability: 4
total_score: 19
sources:
- claim: Revenue and customer 3x growth
  url: https://kalepa.com/news-posts/kalepa-raises-75-million-series-b
  date: '2026-11-05'
  quote: Over the past year, the company has tripled revenue and its customer count.
- claim: Workload 4x growth
  url: https://kalepa.com/news-posts/kalepa-raises-75-million-series-b
  date: '2026-11-05'
  quote: The volume of work running through the platform grew 4x in the past year.
```

### 4. Incumbents moved from pilots to buying insurance AI platforms (18/20)

```yaml
format: deal-timeline
title: Incumbents moved from pilots to buying insurance AI platforms
chapter: Market opportunity
why_it_matters: Buyers are committing to acquire specialist AI-native insurance platforms, showing strategic demand beyond experimentation. Four different
  2026 deals span fleet risk, underwriting, benefits brokerage and agentic pricing.
data:
- label: Admiral Group agreement to acquire Flock
  value: 1
  unit: announced acquisition
  date: '2026-02-12'
- label: Duck Creek acquisition of Send
  value: 1
  unit: completed acquisition
  date: '2026-07-07'
- label: Alliant agreement to acquire Nava Benefits
  value: 1
  unit: announced acquisition
  date: '2026-08-18'
- label: Guidewire agreement to acquire hyperexponential
  value: 1
  unit: announced acquisition
  date: '2026-10-27'
note: We use dated buyer announcements from February 12, July 7, August 18 and October 27, 2026, counting distinct specialist targets once each. We distinguish
  announced agreements from completed transactions; Guidewire's $1.7B base plus up to $400M earnout is a pending deal, not a closed exit.
fresh:
  period: total
  end: 2026-10
scores:
  surprise: 4
  importance: 5
  clarity: 5
  durability: 4
total_score: 18
sources:
- claim: Flock transaction and risk AI
  url: https://admiralgroupplc.gcs-web.com/news-releases/news-release-details/admiral-group-acquires-flock-drive-innovation-commercial-motor
  date: '2026-02-12'
  quote: Admiral Group today announces that it has reached an agreement to acquire Flock, a digital commercial fleet insurance provider with an innovative
    telemetry-based proposition.
- claim: Send AI-native underwriting acquisition
  url: https://www.duckcreek.com/resource/press-releases/duck-creek-acquires-send-creating-the-industrys-only-agentic-underwriting-to-core-platform/
  date: '2026-07-07'
  quote: Duck Creek Technologies, the intelligent core of insurance, today announced it has acquired Send Technology Solutions Ltd, a leading AI-native
    underwriting orchestration engine
- claim: Nava AI-native platform agreement
  url: https://alliant.com/news-resources/alliant-insurance-services-to-acquire-nava-creating-an-ai-native-model-for-the-future-of-employee-benefits/
  date: '2026-08-18'
  quote: Alliant Insurance Services today announced that it has entered into an agreement to acquire Nava Benefits
- claim: Hyperexponential acquisition terms
  url: https://ir.guidewire.com/news-releases/news-release-details/guidewire-signs-definitive-agreement-acquire-hyperexponential
  date: '2026-10-27'
  quote: 'Guidewire (NYSE: GWRE) announced today that it entered into a definitive agreement to acquire Hyperexponential Ltd'
deal_status: Flock, Nava and hyperexponential were agreement announcements; Send was completed as of the cited date. No undisclosed purchase amounts are
  inferred.
```

### 5. Lemonade automated 82% of customer service interactions (18/20)

```yaml
format: key-trend
title: Lemonade automated 82% of customer service interactions
chapter: Market opportunity
why_it_matters: An AI-native carrier is now automating most routine servicing in production, demonstrating credible unit-cost leverage. The accelerating
  series creates an attainable competitive benchmark for insurance AI workflow startups.
data:
- label: 2024 service automation
  value: 51
  unit: '% of customer-service interactions'
  date: 2024-12
- label: 2025 service automation
  value: 67
  unit: '% of customer-service interactions'
  date: 2025-12
- label: November 2026 service automation
  value: 82
  unit: '% of customer-service interactions'
  date: '2026-11-17'
note: We use page 38 of Lemonade's November 17, 2026 Investor Day presentation, which labels the final point "Today" and reports the sequence 51%, 67%,
  82%. We interpret the earlier 2024 and 2025 points as years, without inventing specific quarter-end measurement dates; this is internal company measurement.
fresh:
  period: month
  end: 2026-11
scores:
  surprise: 4
  importance: 5
  clarity: 5
  durability: 4
total_score: 18
sources:
- claim: All three service automation percentages
  url: https://www.lemonade.com/investor-relations-bo/wp-content/uploads/docs/LMND-Investor-Day-Presentation-2026.pdf
  date: '2026-11-17'
  quote: Service Automation % 2024 51% 2025 67% Today 82%
- claim: Operational validation in investor-day commentary
  url: https://stockanalysis.com/stocks/lmnd/transcripts/678984-investor-day-2026/
  date: '2026-11-17'
  quote: 80% of our customer service interactions are fully automated.
```

### 6. Most companies say AI-attack risk is not insured (18/20)

```yaml
format: icon-grid
title: Most companies say AI-attack risk is not insured
chapter: Market opportunity
why_it_matters: An explicit gap in AI-risk insurance coverage creates room for AI liability underwriting, model audits and specialty MGAs. Surveyed risk
  professionals are reporting perceived coverage, not a legal review of policy wording.
data:
- label: Respondents saying AI-generated attacks are not covered
  value: 63
  unit: '% of survey respondents'
  date: 2026-05
- label: Respondents unsure if AI-generated attacks are covered
  value: 15
  unit: '% of survey respondents'
  date: 2026-05
note: We use the independently conducted Ponemon Institute 2026 global study sponsored by Aon, published in May, based on 2,487 respondents from multiple
  industries. We use 63% as the icon-grid headline rate and show 15% unsure as a note only; the reported gap concerns AI-generated attack risks, not every
  type of AI liability.
fresh:
  period: total
  end: 2026-05
scores:
  surprise: 5
  importance: 5
  clarity: 4
  durability: 4
total_score: 18
sources:
- claim: AI-attack cover and uncertainty
  url: https://assets.aon.com/-/media/files/aon/reports/2026/intangible-versus-tangible-risks-2026.pdf
  date: 2026-05
  quote: Sixty-three percent of respondents say their companies existing insurance policies or a separate standalone AI liability policy do not cover
- claim: Study respondents and scope
  url: https://assets.aon.com/-/media/files/aon/reports/2026/intangible-versus-tangible-risks-2026.pdf
  date: 2026-05
  quote: Drawing on survey responses from 2,487 professionals involved in digital and enterprise risk management across multiple global regions and industries
```

### 7. Published AI-insurance market forecasts disagree by sevenfold (17/20)

```yaml
format: forecast-gap
title: Published AI-insurance market forecasts disagree by sevenfold
chapter: Market size
why_it_matters: Market size reports cannot yet establish one credible denominator for AI-insurance spending. Even excluding either extreme, the same-year
  published and derived forecasts disagree by more than threefold, warning against false TAM precision.
data:
- label: KBV Research, published 2030 value
  value: 12.173
  unit: estimated 2030 USD billions
  date: 2030-12
- label: The Insight Partners, 2030 modeled from 2025 base and CAGR
  value: 23.097
  unit: estimated 2030 USD billions
  date: 2030-12
- label: TrendX Insights, published 2030 value
  value: 32.8
  unit: estimated 2030 USD billions
  date: 2030-12
- label: Precedence Research, 2030 modeled from 2026 base and CAGR
  value: 43.966
  unit: estimated 2030 USD billions
  date: 2030-12
- label: The Business Research Company, published 2030 value
  value: 49.13
  unit: estimated 2030 USD billions
  date: 2030-12
- label: Mordor Intelligence, 2030 modeled from 2026 base and CAGR
  value: 85.303
  unit: estimated 2030 USD billions
  date: 2030-12
note: We compare six publisher models available by November 22, 2026, all expressed as USD billions for the global AI-in-insurance market in calendar 2030.
  We calculate the three marked modeled values as Insight 5.13*(1.3511^5), Precedence 14.39*(1.3221^4) and Mordor 26.3*(1.342^4); publishers apply different
  market definitions, so this is a forecast disagreement, not six equivalent observations.
fresh:
  period: total
  end: 2026-11
scores:
  surprise: 5
  importance: 4
  clarity: 4
  durability: 4
total_score: 17
sources:
- claim: KBV 2030 table, USD million
  url: https://www.kbvresearch.com/datapro/global/ai-in-insurance-market
  date: 2026-05
  quote: Global 1,527.34 1,943.34 2,447.73 3,114.70 4,005.00 5,204.90 6,838.03 9,077.59 12,172.84
- claim: Insight 2025 base and 2034 endpoint
  url: https://www.theinsightpartners.com/reports/artificial-intelligence-in-insurance-market
  date: '2026-09-01'
  quote: The artificial intelligence in insurance market was valued at US$ 5.13 Billion in 2025
- claim: Insight CAGR
  url: https://www.theinsightpartners.com/reports/artificial-intelligence-in-insurance-market
  date: '2026-09-01'
  quote: CAGR 2026-2034 35.11 %
- claim: TrendX published 2030
  url: https://trendxinsights.com/syndicated-market-research-reports/ai-in-insurance-market/
  date: 2026-09
  quote: 2030 (F) 32.80 28.6%
- claim: Precedence 2026 base
  url: https://www.precedenceresearch.com/artificial-intelligence-in-insurance-market
  date: '2026-09-16'
  quote: Revenue, 2026 USD 14.39 Bn
- claim: Precedence forecast CAGR
  url: https://www.precedenceresearch.com/artificial-intelligence-in-insurance-market
  date: '2026-09-16'
  quote: CAGR, 2026 - 2035 32.21%
- claim: TBRC published 2030
  url: https://www.thebusinessresearchcompany.com/report/artificial-intelligence-ai-for-insurance-global-market-report
  date: 2026-11
  quote: It will grow to $49.13 billion in 2030 at a compound annual growth rate (CAGR) of 37.0%.
- claim: Mordor 2026 baseline
  url: https://www.mordorintelligence.com/industry-reports/ai-in-insurance-market
  date: '2026-05-07'
  quote: The AI in insurance market size is expected to grow from USD 19.60 billion in 2025 to USD 26.3 billion in 2026
- claim: Mordor forecast CAGR
  url: https://www.mordorintelligence.com/industry-reports/ai-in-insurance-market
  date: '2026-05-07'
  quote: Growth Rate (2026 - 2031) 34.20 %
calculations:
  max_min_ratio: 7.01x
  without_smallest_ratio: 3.69x
  without_largest_ratio: 4.03x
scope_caution: These are modeled broader technology markets including incumbent procurement and sometimes hardware/services, not summed startup revenue.
  KBV values are shown on a public page marked locked; seek confirmation before publication.
```

### 8. More than one-third of consumers would bend a claims photo (17/20)

```yaml
format: icon-grid
title: More than one-third of consumers would bend a claims photo
chapter: Market opportunity
why_it_matters: Digital-media manipulation creates new demand for claims authenticity and insurance-specific fraud detection. The result is stated willingness
  to edit, not a measured fraud incidence rate.
data:
- label: Consumers willing to make a rule-breaking claim edit
  value: 36
  unit: '% of surveyed consumers'
  date: 2026-03
note: We use Verisk's March 2026 State of Insurance Fraud Study; the 36% refers to respondents at least somewhat likely to make a small edit strengthening
  a claim even if against insurer rules. We do not equate consumer intentions with observed paid fraudulent claims.
fresh:
  period: total
  end: 2026-03
scores:
  surprise: 4
  importance: 4
  clarity: 5
  durability: 4
total_score: 17
sources:
- claim: Willingness to edit
  url: https://www.verisk.com/49411b/siteassets/media/campaigns/gated/claims/verisk-state-of-insurance-fraud-study.pdf
  date: 2026-03
  quote: But 36% say they’d still be at least somewhat likely to make a small edit to strengthen a claim, even if it breaks insurer rules.
```

### 9. Lemonade revenue grew 73% as premium volume rose 34% (17/20)

```yaml
format: kpi-trio
title: Lemonade revenue grew 73% as premium volume rose 34%
chapter: Market opportunity
why_it_matters: Strong current-quarter growth in an AI-native carrier is concrete evidence that digitally operated insurance models can scale. The figures
  are business growth, not a causal estimate of AI's contribution.
data:
- label: In-force premium year-over-year growth
  value: 34
  unit: '% YoY'
  date: '2026-09-30'
- label: Total revenue year-over-year growth
  value: 73
  unit: '% YoY'
  date: '2026-09-30'
- label: Gross profit year-over-year growth
  value: 48
  unit: '% YoY'
  date: '2026-09-30'
note: We use Lemonade's November 5, 2026 Q3 disclosure comparing the three months ended September 30, 2026 with the prior-year quarter. We cross-check revenue
  $336.1M versus $194.5M and gross profit $118.1M versus $79.9M against the SEC quarterly filing; in-force premium is an end-quarter annualized stock.
fresh:
  period: quarter
  end: 2026-09
scores:
  surprise: 4
  importance: 5
  clarity: 5
  durability: 3
total_score: 17
sources:
- claim: Company financial highlights
  url: https://api.lemonade.com/investor
  date: '2026-11-05'
  quote: IFP reached $1.55 Billion (+34%)
- claim: Revenue 73%
  url: https://api.lemonade.com/investor
  date: '2026-11-05'
  quote: Revenue grew 73% to $336M
- claim: Gross profit 48%
  url: https://api.lemonade.com/investor
  date: '2026-11-05'
  quote: Record Gross Profit of $118M (+48%)
- claim: SEC quarter revenues
  url: https://www.sec.gov/Archives/edgar/data/1691421/000169142126000068/lmnd-20260930.htm
  date: '2026-11-05'
  quote: Total revenue 336.1 194.5 888.5 509.8
```

### 10. Root turns a profit while Lemonade still loses money (16/20)

```yaml
format: profit-gap
title: Root turns a profit while Lemonade still loses money
chapter: Value creation
why_it_matters: AI-native insurers have diverging economics at similar quarterly revenue scale. Root earned positive GAAP net income while Lemonade still
  reported losses, reminding investors that automation does not guarantee profitability.
data:
- label: Root Q3 2026 GAAP net income per $1 total revenue
  value: 3.78
  unit: cents per $1 revenue
  date: '2026-09-30'
- label: Lemonade Q3 2026 GAAP net income per $1 total revenue
  value: -13.0
  unit: cents per $1 revenue
  date: '2026-09-30'
note: 'We calculate comparable GAAP net-income margin from SEC-reported Q3 2026 net income and total revenue: Root $14.4M/$381.3M = +3.78 cents per revenue
  dollar, Lemonade -$43.7M/$336.1M = -13.00 cents. We label this an after-tax net-result proxy, not EBIT or operating margin, because the firms classify
  financing costs differently.'
fresh:
  period: quarter
  end: 2026-09
scores:
  surprise: 4
  importance: 4
  clarity: 5
  durability: 3
total_score: 16
sources:
- claim: Root GAAP revenues and net income
  url: https://www.sec.gov/Archives/edgar/data/1788882/000178888226000082/root-20260930.htm
  date: '2026-11-04'
  quote: Net income (loss) 14.4 (5.4) 75.7 35.0
- claim: Root revenue base
  url: https://www.sec.gov/Archives/edgar/data/1788882/000178888226000082/root-20260930.htm
  date: '2026-11-04'
  quote: Total revenues 381.3 387.8 1,164.0 1,120.1
- claim: Lemonade net result
  url: https://www.sec.gov/Archives/edgar/data/1691421/000169142126000068/lmnd-20260930.htm
  date: '2026-11-05'
  quote: Net loss (43.7) (37.5) (122.9) (143.8)
- claim: Lemonade revenue base
  url: https://www.sec.gov/Archives/edgar/data/1691421/000169142126000068/lmnd-20260930.htm
  date: '2026-11-05'
  quote: Total revenue 336.1 194.5 888.5 509.8
methodological_exception: 'The format calls for operating result per sales dollar; net income is used for comparable GAAP presentation, and this is explicitly
  disclosed. Optional stricter alternative: drop if operating-only is mandatory.'
```

### 11. Lemonade closed at $35.46 versus a $183.26 peak (16/20)

```yaml
format: fallen-star
title: Lemonade closed at $35.46 versus a $183.26 peak
chapter: Startup killers
why_it_matters: Even well-known AI-native insurers can destroy shareholder value despite operational advances. The price drawdown illustrates valuation
  and execution risk in insurance underwriting.
data:
- label: Lemonade all-time high adjusted daily close
  value: 183.26
  unit: USD per share
  date: '2021-01-11'
- label: Lemonade latest completed daily close
  value: 35.46
  unit: USD per share
  date: '2026-11-20'
note: 'We use adjusted closing prices, not the intraday record: $183.26 on January 11, 2021 and $35.46 on November 20, 2026, the latest completed US trading
  session before this report. We compute the drawdown as (35.46/183.26-1)*100 = -80.65%; share-price histories from CompaniesMarketCap and S&P Global Market
  Intelligence agree on the peak.'
fresh:
  period: total
  end: 2026-11
scores:
  surprise: 4
  importance: 4
  clarity: 5
  durability: 3
total_score: 16
sources:
- claim: Historical record close
  url: https://companiesmarketcap.com/lemonade/stock-price-history/
  date: '2026-11-20'
  quote: 'Highest end of day price: $183.26 USD (United States Dollar) on 2021-01-11'
- claim: Latest November 20 close
  url: https://stockanalysis.com/stocks/lmnd/history/
  date: '2026-11-20'
  quote: 'At close: Nov 20, 2026, 4:00 PM EST'
- claim: Nov 20 close price
  url: https://www.quotelinks.com/chart/lmnd.html
  date: '2026-11-20'
  quote: The highest closing price for LMND was $183.26 on January 11, 2021 (adjusted for stock splits).
```

### 12. AI litigation has accelerated sharply in the US and abroad (14/20)

```yaml
format: rules-wave
title: AI litigation has accelerated sharply in the US and abroad
chapter: Market challenges
why_it_matters: The spread of AI lawsuits expands legal uncertainty and creates a potential market for AI-specific risk coverage. The tracker counts broad
  AI cases, not only insurance claims denials or suits against insurers.
data:
- label: 2023 tracked AI lawsuits
  value: 30
  unit: cases filed
  date: '2023-12-31'
- label: 2024 tracked AI lawsuits
  value: 48
  unit: cases filed
  date: '2024-12-31'
- label: 2025 tracked AI lawsuits
  value: 110
  unit: cases filed
  date: '2025-12-31'
- label: 2026 tracked AI lawsuits, partial year
  value: 179
  unit: cases filed, year to date
  date: '2026-11-22'
note: We use AI Lawsuit Tracker's cases-by-year table as observed on November 22, 2026, with 2026 explicitly incomplete; counts were 30, 48, 110, then 179.
  We treat this as a broad adjacent liability indicator, not an insurance-litigation count; registry expansion and case discovery may affect comparability.
fresh:
  period: year
  end: 2026-11
scores:
  surprise: 3
  importance: 4
  clarity: 4
  durability: 3
total_score: 14
sources:
- claim: Yearly case count from one tracker
  url: https://ailawsuittracker.com/trends/
  date: '2026-11-22'
  quote: All types 30 48 110 179
- claim: Tracker methodology date
  url: https://ailawsuittracker.com/trends/
  date: '2026-11-15'
  quote: Every case here checked since September 27, 2026
definition_caution: Broad lawsuits against AI companies, not lawsuits challenging insurers' AI claim denials; use only if the chapter covers emerging AI
  liability insurance.
```

## Format investigation log

All prescribed formats were assessed. Rejected formats are not recommendations or fill-in slide ideas.

| Format | Verdict and strict-filter reason |
|---|---|
| `key-trend` | KEEP: insurer AI-use share and Lemonade service automation each exceed 1.5x. |
| `rules-wave` | KEEP WITH SCOPE WARNING: broad AI lawsuit tracker rises in 2025 and 2026; not insurance-only. |
| `funnel` | DROP: no single-method survey with striking stage-by-stage counts found. |
| `country-gap` | DROP: country comparisons found did not supply a robust same-year, identical question with a 2x gap. |
| `waiting-line` | DROP: no credible insurance AI waitlist paired with service capacity. |
| `incident-count` | DROP: no official comparable insurance-AI incident or deepfake-fraud count series insulated from reporting growth. |
| `announced-vs-built` | DROP: pilot survey rates are not launch counts against specific promises. |
| `idle-capacity` | DROP: no sourced AI-insurance platform capacity/usage series documenting >=30% idle. |
| `promise-tracker` | DROP: no single insurance-AI milestone with three dated slips. |
| `lobbying-spend` | DROP: no verified insurance-AI-specific LD-2 outlier series. |
| `cost-threshold` | KEEP: five comparable quarterly LAE ratios cross the company-reported incumbent benchmark. |
| `penetration-curve` | DROP: no comparable insurance-AI uptake series against an older technology since launch. |
| `adoption-race` | DROP: insufficient dated identical milestones for two competing vendors. |
| `earnings-mentions` | DROP: no FactSet or similarly consistent insurer earnings-call mention series with >=3x. |
| `real-world-vs-funding` | DROP: funding bars require the client database and no comparable independent usage series. |
| `incumbent-crash` | DROP: no verified incumbent insurance stock decline >=50% attributable to a specified AI event. |
| `fallen-star` | KEEP: Lemonade 2026 close is more than 80% below its adjusted 2021 all-time close. |
| `challenger` | DROP: no synchronized private-versus-listed valuations and revenues documenting a fast narrowing gap. |
| `dominance` | DROP: no consistent market-share series supporting a rising or crushing leader share. |
| `contract-share` | DROP: no verifiable public insurance AI contract spend split between startups and incumbents. |
| `multiple-gap` | DROP: no properly matched trailing-revenue and market-value set with a confirmed 3x multiple gap. |
| `profit-gap` | KEEP WITH METRIC CAUTION: same-quarter GAAP net result / revenue, not operating income. |
| `revenue-per-head` | DROP: no independent comparable current staffing and insurance-AI revenue values with 2x gap. |
| `dollar-split` | DROP: no published transparent dollar allocation for a single AI-native insurance product. |
| `single-customer` | DROP: no startup primary filings showing a customer concentration >=30%. |
| `forecast-gap` | KEEP WITH MODELED VALUES: six publisher estimates of 2030 revenue; >=3x gap remains after deleting either extreme. |
| `kpi-trio` | KEEP: Kalepa and Lemonade disclose recent product/business growth metrics. |
| `deal-timeline` | KEEP: four dated transactions, with agreements distinguished from completions. |
| `value-ladder` | DROP: no 4-6 consistently fresh, verified AI-first startup valuations; historical funding values are stale. |
| `icon-grid` | KEEP: Verisk 36% and Aon/Ponemon 63% are directly reported rates. |
| `funding-event` | NOT RESEARCHED: explicitly reserved for NewMarketPitch internal round database. |

## QA checklist and editorial limitations

- **Freshness:** all seven Market opportunity slides use data published or measured in 2026; annual Goldman and Kalepa data, the current Lemonade quarterly figures, the 2026 acquisitions, and two cross-sectional surveys are distinguished from cumulative evidence.
- **Thresholds:** AI usage 62/29 = 2.14x; service automation 82/51 = 1.61x; five LAE points cross the 9% reference; 2026 broad AI lawsuits 179 versus 2024 48 = 3.73x; Lemonade price decline is 80.65%; six 2030 publisher projections diverge by 7.01x, 3.69x without the smallest, and 4.03x without the largest.
- **Boundaries:** insurance adoption survey includes incidental incumbent AI usage and is a buyer-side market signal, not a startup penetration measure. The litigation indicator covers AI cases generally, not insurer claim denials. The market-size comparison covers broader insurance AI spending, not startup-only revenue.
- **Company-reported versus independent:** Kalepa growth, Lemonade automation and Lemonade's incumbent LAE reference come from the companies; the claims-photo statistic comes from Verisk's consumer survey; Aon's statistics are from Ponemon research sponsored by Aon.
- **M&A precision:** Flock, Nava and hyperexponential deal entries are announcement/agreement dates; Send was described by its buyer as acquired. The $1.7B Guidewire hyperexponential base consideration plus $400M potential contingent consideration is not a completed cash payment.
- **Metric exception:** Profit-gap uses after-tax GAAP net result per revenue dollar for comparability, not strict EBIT. Remove if the slide library requires accounting-definition-pure operating margin; the remaining 11 retain their format threshold.
- **Forecast caveat:** KBV’s public preview is marked locked even though its table values are visible. Reconfirm its quoted 2030 number with the vendor before production; if removed, the remaining five-source set fails the >=3x condition after dropping the low extreme. Do not publish the forecast-gap slide without this check.
- **Source quotes:** short exact supporting source excerpts are supplied. Some primary sources are tables or chart labels rather than prose; those appear as exact row/graphic transcriptions.
