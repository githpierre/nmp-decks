### ed041
```yaml
status: ok
section: Market size
title: What counts as AI in drug discovery, and what doesn't?
note: We count AI systems that guide the choice or design of therapeutic targets and medicines before human testing, not general healthcare AI.
t:
  7: We define AI in drug discovery as tools using learned models to find disease targets, create or improve drugs and pick candidates before human trials.
  8: We include AI target finding, screening, molecule and protein design, repurposing, lead refinement, safety checks and automated labs.
  9: We exclude diagnosis-only tools, trial management, generic cloud services, factory software and businesses making only nonmedical proteins.
sources:
- claim: Therapeutic discovery work includes targets, screening, molecular design and lead optimization
  url: https://www.kenresearch.com/industry-reports/global-artificial-intelligence-in-drug-discovery-market
  date: 2026-08
  quote: across target identification, virtual screening, molecular generation and lead optimization.
- claim: Clinical trial design is a separate AI use
  url: https://www.futuremarketinsights.com/reports/ai-enabled-drug-discovery-market
  date: 2026 (day not stated)
  quote: AI target identification platforms, AI lead optimization platforms, AI clinical trial design tools
- claim: Preclinical work includes candidate assessment
  url: https://www.grandviewresearch.com/industry-analysis/artificial-intelligence-drug-discovery-market
  date: 2026-01 (updated 2026-06)
  quote: AI in the preclinical testing segment enhances the evaluation of drug candidates before human trials.
```

### ed042
```yaml
status: ok
section: Market size
title: What are the market size estimates from different sources online?
rows:
- firm: 'Grand View

    Research'
  value: $2.9B
  comment: Its 2026 estimate includes drug optimization and preclinical testing. We use it as a lower, direct market check.
- firm: 'Coherent Market

    Insights'
  value: $3.2B
  comment: Its process split covers targets, screening, lead work and preclinical development. It closely matches our scoped estimate.
- firm: 'Market Research

    Future'
  value: $3.5B
  comment: Its market also includes clinical-trial uses, which we exclude. We use the 2026 result as a broad comparison only.
- firm: 'Global Market

    Insights'
  value: $4B
  comment: Its estimate spans paid software and services. We keep it as an upper cross-check for our narrower discovery scope.
note:
- We take each 2026 figure from its publisher, then compare the included drug-discovery work with our scope.
- We exclude trial operations, generic AI compute and deal headline values from our own estimate.
sources:
- claim: 'Grand View Research: $2.9B for 2026'
  url: https://www.grandviewresearch.com/industry-analysis/artificial-intelligence-drug-discovery-market
  date: 2026-01 (updated 2026-06)
  quote: 'Estimated market size in 2026: USD 2.9 Billion'
- claim: 'Coherent Market Insights: about $3.2B for 2026'
  url: https://www.coherentmarketinsights.com/industry-reports/ai-in-drug-discovery-market
  date: '2026-09-23'
  quote: Revenue, 2026 USD 3,240.0 Mn
- claim: 'Market Research Future: about $3.5B for 2026'
  url: https://www.marketresearchfuture.com/reports/ai-drug-discovery-market-9393
  date: '2026-11-12'
  quote: projected to grow from USD 3.48 billion in 2026 to USD 23.95 billion by 2035
- claim: Market Research Future scope includes clinical trials
  url: https://www.marketresearchfuture.com/reports/ai-drug-discovery-market-9393
  date: '2026-11-12'
  quote: Target Identification, Lead Optimization, Drug Repurposing, Clinical Trials, Preclinical Testing
- claim: 'Global Market Insights: $4B for 2026'
  url: https://www.gminsights.com/industry-analysis/ai-in-drug-discovery-market
  date: 2026-09
  quote: is expected to reach USD 4 billion in 2026
```

### ed043
```yaml
status: ok
section: Market size
title: Our own first-principles, bottom-up calculation of the market size
page: 1/2
note: We multiply modeled paying discovery engagements by their annual economic value. This is a demand model, not audited sales.
t:
  21: We count annual payments for AI that helps discover new medicines
  16: We start from paid discovery software and lab-backed research contracts
  15: We include earned research fees and paid molecule design programs
  14: We exclude trial services, diagnostics and generic cloud compute
  9: We leave out venture funding, acquisitions and unpaid deal milestones
  8: We use 2026 demand inputs from Ken Research's discovery study
  7: It models 1,380 active AI discovery customer deals for the year 2026
  6: It puts their average annual value near $2.5M
  3: We multiply 1,380 deals by about $2.5M each to size annual paid demand
  2: That gives about $3.4B in sales using unrounded model inputs
  0: We cross-check this demand figure against other 2026 reports
sources:
- claim: Ken Research counts discovery software, services and partnerships
  url: https://www.kenresearch.com/industry-reports/global-artificial-intelligence-in-drug-discovery-market
  date: 2026-08
  quote: The Global Artificial Intelligence in Drug Discovery Market monetizes software licenses, computational discovery services, integrated research collaborations and milestone-linked programs
- claim: 2026 estimated 1,380 active engagements and about $2.5M value each
  url: https://www.kenresearch.com/industry-reports/global-artificial-intelligence-in-drug-discovery-market
  date: 2026-08
  quote: 2026  | $3,440 Mn  | +26.0%  | 1,380  | 2.49  | $#%  | Forecast
- claim: Published demand model and method
  url: https://www.kenresearch.com/industry-reports/global-artificial-intelligence-in-drug-discovery-market
  date: 2026-08
  quote: The base-year model reconciles supply-side company activity, operational engagement economics and demand from pharmaceutical, biotechnology, CRO and academic adopters
- claim: Recognized up-front fees are distinct from large future milestones
  url: https://www.mckinsey.com/industries/life-sciences/our-insights/ai-drug-discovery-focusing-on-what-matters-most/
  date: '2026-09-21'
  quote: Up-front cash payments totaled only $0.60 billion, just 2 percent of deal value, in 2025
```

### ed044
```yaml
status: ok
section: Market size
title: Our own first-principles, bottom-up calculation of the market size
page: 2/2
note: We test our demand model against published forecasts and disclosed supplier revenue. We do not add mixed-business sales to it.
t:
  21: We derive about $3.4B by rounding the 2026 paid contract model
  16: Coherent Market Insights puts 2026 market sales at about $3.2B
  15: Market Research Future estimates about $3.5B in 2026
  14: Grand View Research reports a lower total of $2.9B for 2026
  9: Global Market Insights gives a higher 2026 value of $4B in revenue
  8: Coherent estimates software at 66.8% of the 2026 market
  7: That implies about $2.3B in software and $1.1B in paid services for us
  6: Schrödinger reported $256M of total 2025 sales, including non-drug work
  3: Recursion reported $74.7M of total revenue from 2025 programs
  2: We use vendor sales only as checks, not the entire market
  0: We conclude that AI in drug discovery is worth about $3.4B in 2026
sources:
- claim: 2026 modeled value about $3.4B
  url: https://www.kenresearch.com/industry-reports/global-artificial-intelligence-in-drug-discovery-market
  date: 2026-08
  quote: 2026  | $3,440 Mn  | +26.0%  | 1,380  | 2.49  | $#%  | Forecast
- claim: Coherent Market Insights estimate about $3.2B
  url: https://www.coherentmarketinsights.com/industry-reports/ai-in-drug-discovery-market
  date: '2026-09-23'
  quote: Revenue, 2026 USD 3,240.0 Mn
- claim: Market Research Future estimate about $3.5B
  url: https://www.marketresearchfuture.com/reports/ai-drug-discovery-market-9393
  date: '2026-11-12'
  quote: projected to grow from USD 3.48 billion in 2026
- claim: Grand View Research estimate $2.9B
  url: https://www.grandviewresearch.com/industry-analysis/artificial-intelligence-drug-discovery-market
  date: 2026-01 (updated 2026-06)
  quote: 'Estimated market size in 2026: USD 2.9 Billion'
- claim: Global Market Insights estimate $4B
  url: https://www.gminsights.com/industry-analysis/ai-in-drug-discovery-market
  date: 2026-09
  quote: is expected to reach USD 4 billion in 2026
- claim: Software share of 66.8% in 2026
  url: https://www.coherentmarketinsights.com/industry-reports/ai-in-drug-discovery-market
  date: '2026-09-23'
  quote: Software is projected to hold 66.8% of the global AI in drug discovery market share in 2026
- claim: Schrodinger 2025 about $256M total revenue
  url: https://ir.schrodinger.com/press-releases/news-details/2026/Schrdinger-Reports-Fourth-Quarter-and-Full-Year-2025-Financial-Results/default.aspx
  date: '2026-02-25'
  quote: Total revenue was $255.9 million, a 23.3% increase.
- claim: Recursion 2025 reported revenue $74.7M
  url: https://recursion.gcs-web.com/news-releases/news-release-details/recursion-reports-fourth-quarter-and-full-year-2025-financial
  date: '2026-02-25'
  quote: Total revenue, consisting primarily of revenue from collaboration agreements, was $74.7 million for the year ended December 31, 2025
```

### ed045
```yaml
status: ok
section: Market size
title: How much is AI in drug discovery worth today?
t:
  6: $3.4B
  8: We estimate $3.4B for 2026 from 1,380 modeled discovery deals worth about $2.5M each. Coherent estimates $3.2B and Market Research Future $3.5B. We exclude funding and unpaid deal milestones.
  4: '2026'
note: We estimate annual revenue from paid discovery workflows rather than future drug sales or announced deal ceilings.
sources:
- claim: 'Our modeled 2026 value: $3.4B from 1,380 deals near $2.5M'
  url: https://www.kenresearch.com/industry-reports/global-artificial-intelligence-in-drug-discovery-market
  date: 2026-08
  quote: 2026  | $3,440 Mn  | +26.0%  | 1,380  | 2.49  | $#%  | Forecast
- claim: 'Coherent: 2026 about $3.2B'
  url: https://www.coherentmarketinsights.com/industry-reports/ai-in-drug-discovery-market
  date: '2026-09-23'
  quote: Revenue, 2026 USD 3,240.0 Mn
- claim: 'Market Research Future: 2026 about $3.5B'
  url: https://www.marketresearchfuture.com/reports/ai-drug-discovery-market-9393
  date: '2026-11-12'
  quote: projected to grow from USD 3.48 billion in 2026
- claim: Large partnership values are not cash revenue
  url: https://www.mckinsey.com/industries/life-sciences/our-insights/ai-drug-discovery-focusing-on-what-matters-most/
  date: '2026-09-21'
  quote: Up-front cash payments totaled only $0.60 billion, just 2 percent of deal value, in 2025
```

### ed047p
```yaml
status: no_data
section: Market size
title: How is the AI in drug discovery market split between its categories?
comment: No source gives a complete, mutually exclusive revenue split for all eight discovery categories. Published stage shares overlap or omit workflows.
```

### ed048
```yaml
status: ok
section: Market size
title: What is behind these categories?
t:
  5: TARGET & SCREENING
  8: MOLECULE DESIGN
  10: EARLY SAFETY CHECKS
  11: 🧬
  4: AI links gene and cell data to diseases, then ranks targets and screens compounds to find promising early drug candidates.
  12: 🧪
  7: AI draws and improves small molecules, therapeutic proteins and RNA treatments before labs make and test top candidates.
  9: AI predicts absorption and safety before human trials, while robotic labs feed new test results back into models.
  15: ''
  17: ''
  18: ''
  19: ''
  14: ''
  16: ''
holes_ok: true
comment: These three workflow groups explain the eight database categories but do not imply a measured revenue split.
sources:
- claim: Target identification and screening
  url: https://www.coherentmarketinsights.com/industry-reports/ai-in-drug-discovery-market
  date: '2026-09-23'
  quote: By Drug Discovery Process Target Identification and Validation · Hit Identification and Screening · Lead Identification and Optimization · Preclinical Development
- claim: Molecular design spans multiple treatment types
  url: https://www.futuremarketinsights.com/reports/ai-enabled-drug-discovery-market
  date: 2026 (day not stated)
  quote: By application, small-molecule drug discovery represents the largest use case
- claim: AI preclinical testing includes toxicity and pharmacokinetics
  url: https://www.grandviewresearch.com/industry-analysis/artificial-intelligence-drug-discovery-market
  date: 2026-01 (updated 2026-06)
  quote: Machine learning models predict toxicity, efficacy, and pharmacokinetics from molecular and biological data.
- claim: Experimental feedback guides iterative drug design
  url: https://www.mckinsey.com/industries/life-sciences/our-insights/ai-drug-discovery-focusing-on-what-matters-most/
  date: '2026-09-21'
  quote: The priority is now shifting from predicting binding affinity to generating standardized readouts for developability and closing design-make-test-learn loops.
```

### ed049
```yaml
status: ok
section: Market size
title: Where in the world is AI in drug discovery money spent?
regions:
  na:
    pct: 52.8
    text: North America takes 52.8% of the 2025 benchmark. US drug developers and pharma buyers fund much of the paid AI discovery work.
  eu:
    pct: 25.6
    text: Europe holds 25.6% in the same 2025 benchmark. UK and EU drugmakers buy target research, molecule design and preclinical software.
  apac:
    pct: 18.8
    text: Asia-Pacific holds 18.8% in the 2025 benchmark, with China, Japan and India scaling AI discovery programs.
  latam:
    pct: 1.9
    text: Latin America holds 1.9% in the 2025 benchmark, a small market for paid discovery platforms. The share measures sales, not labs.
  mea:
    pct: 0.9
    text: The Middle East and Africa hold 0.9% of the 2025 benchmark. AI discovery is growing, but direct platform sales remain small.
note:
- We use Ken Research's five-region 2025 revenue split as a complete public proxy for discovery spending.
- We hold those shares fixed in 2026 because no consistent, scope-matched regional breakdown is disclosed.
sources:
- claim: 2025 shares 25.6% Europe, 18.8% Asia Pacific, 1.9% Latin America, 0.9% MEA
  url: https://www.kenresearch.com/industry-reports/global-artificial-intelligence-in-drug-discovery-market
  date: 2026-08
  quote: 25.6%  | 18.8%  | 1.9%  | 0.9%
- claim: GVR North America share validates first regional anchor
  url: https://www.grandviewresearch.com/industry-analysis/artificial-intelligence-drug-discovery-market
  date: 2026-01 (updated 2026-06)
  quote: North America held the largest market share of 52.8% in 2025.
```

### ed050
```yaml
status: ok
section: Market size
title: What are the growth rate estimates from different sources online?
note: We compare published AI-discovery revenue forecasts. We treat forecasts that also cover trial tools as broader than our own scope.
t:
  24: FIRM
  25: CAGR
  26: COMMENTS
  6: 'Future Market

    Insights'
  5: '≈15.3%

    through 2036'
  7: Its 15.3% forecast includes clinical trial design tools alongside discovery AI. We treat it as a slower case, not our base.
  10: 'Grand View

    Research'
  9: '≈24.8%

    through 2033'
  11: Its 24.8% forecast tracks paid AI discovery tools through 2033. We use it near the cautious end of our core growth range.
  14: 'Coherent Market

    Insights'
  13: '≈25.1%

    through 2033'
  15: Its 25.1% forecast covers target finding, screening, design and preclinical work. We use it to confirm a mid-20s base case.
  18: 'Global Market

    Insights'
  17: '≈30.5%

    through 2035'
  19: Its 30.5% forecast sees rapid software adoption and deeper service contracts. We keep it near our upside, not a guarantee of better drugs.
sources:
- claim: FMI CAGR 15.3% 2026-2036
  url: https://www.futuremarketinsights.com/reports/ai-enabled-drug-discovery-market
  date: 2026 (day not stated)
  quote: USD 33,951.6 million by 2036, at a CAGR of 15.3%.
- claim: FMI also includes clinical trial design tools
  url: https://www.futuremarketinsights.com/reports/ai-enabled-drug-discovery-market
  date: 2026 (day not stated)
  quote: Platforms  | AI Target Identification Platforms, AI Lead Optimization Platforms, AI Clinical Trial Design Tools
- claim: Grand View Research CAGR 24.8% 2026-2033
  url: https://www.grandviewresearch.com/industry-analysis/artificial-intelligence-drug-discovery-market
  date: 2026-01 (updated 2026-06)
  quote: 'CAGR (2026-2033): 24.8%'
- claim: Coherent CAGR 25.1% 2026-2033
  url: https://www.coherentmarketinsights.com/industry-reports/ai-in-drug-discovery-market
  date: '2026-09-23'
  quote: a compound annual growth rate (CAGR) of 25.1% from 2026 to 2033.
- claim: Global Market Insights CAGR 30.5% 2026-2035
  url: https://www.gminsights.com/industry-analysis/ai-in-drug-discovery-market
  date: 2026-09
  quote: at a CAGR of 30.5% during 2026-2035.
```

### ed051
```yaml
status: ok
section: Market size
title: What is a realistic CAGR for the AI in drug discovery market?
note: We use 26% annual growth near the narrow discovery forecasts. We set 15% and 31% as scenarios, not promises.
t:
  15: BEST CASE ≈ 31%
  17: '≈26%

    through 2036'
  19: Pharma buys repeat discovery work, but AI drugs still face hard human tests. We use 26%, close to peer forecasts, with 15% for slow adoption and 31% for faster uptake.
  16: WORST CASE ≈ 15%
sources:
- claim: Ken Research 26% 2025-2032 forecast
  url: https://www.kenresearch.com/industry-reports/global-artificial-intelligence-in-drug-discovery-market
  date: 2026-08
  quote: representing a 26.0% forecast CAGR.
- claim: FMI downside 15.3% 2026-2036
  url: https://www.futuremarketinsights.com/reports/ai-enabled-drug-discovery-market
  date: 2026 (day not stated)
  quote: at a CAGR of 15.3%.
- claim: Grand View Research forecast 24.8%
  url: https://www.grandviewresearch.com/industry-analysis/artificial-intelligence-drug-discovery-market
  date: 2026-01 (updated 2026-06)
  quote: 'CAGR (2026-2033): 24.8%'
- claim: Coherent forecast 25.1%
  url: https://www.coherentmarketinsights.com/industry-reports/ai-in-drug-discovery-market
  date: '2026-09-23'
  quote: a compound annual growth rate (CAGR) of 25.1% from 2026 to 2033.
- claim: Global Market Insights upside 30.5%
  url: https://www.gminsights.com/industry-analysis/ai-in-drug-discovery-market
  date: 2026-09
  quote: at a CAGR of 30.5% during 2026-2035.
- claim: Majority of AI native clinical assets still need human trial validation
  url: https://www.mckinsey.com/industries/life-sciences/our-insights/ai-drug-discovery-focusing-on-what-matters-most/
  date: '2026-09-21'
  quote: most AI-native clinical assets remain in Phase I or Phase II safety and dose-ranging trials.
```

### ed052p
```yaml
status: ok
section: Market size
title: How much bigger can AI in drug discovery get?
size: 3.4
cagr: 26
y0: 2026
lead: 'To get that big, '
condition: drugmakers must renew discovery contracts at scale, expand paid AI design and preclinical testing, and show that better early choices can withstand human trials without relying on speculative
  deals.
note:
- We start with $3.4B in 2026 and apply 26% annual growth, yielding about $34B by 2036.
- We anchor the rate in published forecasts, not assumed drug approvals or unpaid milestone deals.
sources:
- claim: 2026 starting market size about $3.4B modeled demand
  url: https://www.kenresearch.com/industry-reports/global-artificial-intelligence-in-drug-discovery-market
  date: 2026-08
  quote: 2026  | $3,440 Mn  | +26.0%  | 1,380  | 2.49  | $#%  | Forecast
- claim: 26% CAGR assumption 2025-2032
  url: https://www.kenresearch.com/industry-reports/global-artificial-intelligence-in-drug-discovery-market
  date: 2026-08
  quote: representing a 26.0% forecast CAGR.
- claim: Molecular design contracts dominated by contingent milestones
  url: https://www.mckinsey.com/industries/life-sciences/our-insights/ai-drug-discovery-focusing-on-what-matters-most/
  date: '2026-09-21'
  quote: with 60 to 90 percent of contract value contingent on downstream clinical and commercial milestones.
- claim: Rentosertib entered a Phase III trial in 2026, outcome not yet reported
  url: https://insilico.com/news/isn1009261-insilico-medicine-doses-first-patient-genesis-ipf-3
  date: '2026-09-10'
  quote: The Phase III clinical trial is a prospective, multi-center, randomized, double-blind, placebo-controlled, parallel-group study
```
