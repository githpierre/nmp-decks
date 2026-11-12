### ed041
```yaml
status: ok
section: Market size
title: 'What counts as in vivo CAR-T,\n\n  and what doesn’t?'
note: We count therapeutic vectors and nanocarriers that create CAR-engineered immune cells inside the patient, and exclude ex vivo cell manufacturing and generic suppliers.
t:
  7: We define in vivo CAR-T as therapies that deliver CAR instructions or editing machinery into the body so immune cells are engineered inside the patient
  8: We include targeted lentiviral, LNP-RNA, circular-RNA, DNA, hybrid, and in vivo editing platforms that directly generate CAR immune cells
  9: We exclude ex vivo CAR-T products, generic vector suppliers, CDMOs, research-only tools, and programs where in vivo CAR is only peripheral
sources:
  - claim: In vivo CAR-T generates CAR-T cells directly inside the patient rather than through ex vivo manufacturing
    url: https://www.nature.com/articles/s41573-025-01291-5
    date: 2025-09-30
    quote: "In vivo chimeric antigen receptor (CAR)-T cell therapy"
  - claim: Viral and non-viral vectors are the two main delivery approaches
    url: https://pmc.ncbi.nlm.nih.gov/articles/PMC13729517/
    date: 2026-08-31
    quote: "There are now two dominating platforms: viral vectors and non-viral systems"
```

### ed042
```yaml
status: ok
section: Market size
title: 'What are the market size estimates\n\n  from different sources online?'
rows:
- firm: 'Precedence\nResearch'
  value: $ 861 M
  comment: Their 2026 figure uses a broad in vivo CAR-T market definition across development stages. We treat it as the high end of our range.
- firm: 'Future Market\nInsights'
  value: $ 180 M
  comment: Their scope is narrow and revenue-based, centered on administered vectors, nanocarriers, and clinical supply. We use it as the low case.
- firm: 'Grand View\nResearch'
  value: $ 341 M
  comment: Their figure covers the broader in vivo cell-therapy market, not only CAR-T. We use it as a cross-check, then adjust for T-cell share.
- firm: 'Metic.\nNext'
  value: $ 500–800 M
  comment: Their 2026 range includes development spending, acquisitions, partnerships, manufacturing, and clinical supply. We use it only as an upper bound.
note:
- We take each estimate from the firm’s website and adjust when its definition is broader or narrower than ours
- We prioritize current 2026 estimates and separate therapy revenue from financing, acquisitions, and other non-market transactions
sources:
  - claim: Precedence Research estimates the 2026 in vivo CAR-T market at $861.25 million
    url: https://www.precedenceresearch.com/in-vivo-car-t-therapy-market
    date: 2026-09-09
    quote: "The global in vivo CAR-T therapy market size accounted for USD 650.00 million in 2025"
  - claim: Future Market Insights estimates the 2026 market at $180.0 million
    url: https://www.futuremarketinsights.com/reports/in-vivo-car-t-cell-therapy-market
    date: 2026-10
    quote: "FMI values the in vivo CAR-T cell therapy market at USD 180.0 million in 2026"
  - claim: Grand View Research estimates the broader 2026 in vivo cell-therapy market at $340.7 million
    url: https://www.grandviewresearch.com/industry-analysis/in-vivo-cell-therapy-market-report
    date: 2026-08
    quote: "Market Estimate, 2026 $340.7M"
  - claim: Meticulous Next gives a $0.5-$0.8 billion 2026 range under a broader spending definition
    url: https://www.meticulousresearch.com/meticulous-next/meticulous-next-in-vivo-car-t-market-outlook-2026-2036
    date: 2026
    quote: "USD 0.5–0.8 billion in 2026"
```

### ed043
```yaml
status: ok
section: Market size
title: Our own first-principles, bottom-up calculation of the market size
page: 1/2
note: We triangulate current market reports, then strip out M&A and other financing and use broader in vivo cell-therapy data only as a cross-check.
t:
  0: We exclude M&A and licensing because those are financing, not therapy revenue
  2: We start with FMI at $180 million in 2026, the narrowest direct estimate
  3: We check Grand View’s broader $341 million in vivo cell-therapy estimate
  6: We take the scope-adjusted midpoint, about $285 million for 2026
  7: We derive $284 million by taking 83.2% of Grand View’s $341 million
  8: We compare Precedence, which puts 2026 at $861 million
  9: We treat Meticulous Next’s $0.5–0.8 billion as a broad upper range
  14: We begin from trial-supply revenue because no in vivo CAR-T has an approved label
  15: We exclude ex vivo CAR-T, CDMOs, generic vectors, and downstream care
  16: We count administered vector or nanocarrier products and clinical supply
  21: We explain our estimate using only market data we can reconcile
sources:
  - claim: Future Market Insights estimates $180.0 million in 2026 and says no in vivo product has an approved label
    url: https://www.futuremarketinsights.com/reports/in-vivo-car-t-cell-therapy-market
    date: 2026-10
    quote: "no in vivo product has yet reached an approved label"
  - claim: Grand View Research estimates $340.7 million for the broader in vivo cell-therapy market in 2026
    url: https://www.grandviewresearch.com/industry-analysis/in-vivo-cell-therapy-market-report
    date: 2026-08
    quote: "Estimated market size in 2026: USD 340.7 Million"
  - claim: T cells represented 83.2% of the broader in vivo cell-therapy market in 2025
    url: https://www.grandviewresearch.com/industry-analysis/in-vivo-cell-therapy-market-report
    date: 2026-08
    quote: "The T cell segment held the highest market share of 83.2% in 2025"
  - claim: Precedence Research estimates $861.25 million for 2026
    url: https://www.precedenceresearch.com/in-vivo-car-t-therapy-market
    date: 2026-09-09
    quote: "Market Size in 2026 | USD 861.25 Million"
  - claim: Meticulous Next estimates $0.5-$0.8 billion in 2026 under a broad spending definition
    url: https://www.meticulousresearch.com/meticulous-next/meticulous-next-in-vivo-car-t-market-outlook-2026-2036
    date: 2026
    quote: "USD 0.5–0.8 billion in 2026"
```

### ed044
```yaml
status: ok
section: Market size
title: Our own first-principles, bottom-up calculation of the market size
page: 2/2
note: We land near the T-cell share of Grand View’s broader market, while keeping FMI as the narrow case and Precedence as the high case.
t:
  0: We conclude that in vivo CAR-T is worth about $285 million today
  2: We round to one simple number that stays easy to check and defend
  3: We check that T cells are 83.2% of broader in vivo cell therapy
  6: We note hematologic malignancies were 60% of 2025 market value
  7: We keep 2026, the current year with fresh estimates from each source
  8: We check FMI’s 2026 figure of $180 million as the narrow case
  9: We note there are no approved products yet, so trial supply drives revenue
  14: We check Precedence, which gives $861 million under a broader scope
  15: We note public estimates diverge because definitions are still unsettled
  16: We add Grand View’s $341 million broader in vivo cell-therapy estimate
  21: We add SNS Insider at $283 million for the broader in vivo cell market
sources:
  - claim: Our rounded estimate is based on 83.2% of Grand View's $340.7 million 2026 market, or about $284 million
    url: https://www.grandviewresearch.com/industry-analysis/in-vivo-cell-therapy-market-report
    date: 2026-08
    quote: "Market Estimate, 2026 $340.7M"
  - claim: Hematologic malignancies held 60% of the in vivo CAR-T market in 2025
    url: https://www.precedenceresearch.com/in-vivo-car-t-therapy-market
    date: 2026-09-09
    quote: "the hematologic malignancies segment led the global market in 2025 with a 60% share"
  - claim: Future Market Insights estimates $180.0 million in 2026
    url: https://www.futuremarketinsights.com/reports/in-vivo-car-t-cell-therapy-market
    date: 2026-10
    quote: "Estimated Market Size in 2026 | USD 180.0 million"
  - claim: No in vivo CAR-T product has an approved label yet
    url: https://www.futuremarketinsights.com/reports/in-vivo-car-t-cell-therapy-market
    date: 2026-10
    quote: "no in vivo product has yet reached an approved label"
  - claim: SNS Insider estimates the broader in vivo cell-therapy market at $282.92 million in 2026
    url: https://www.snsinsider.com/reports/in-vivo-cell-therapy-market-11688
    date: 2026-11-11
    quote: "2026 MARKET SIZE USD 282.92 Million"
```

### ed045
```yaml
status: ok
section: Market size
title: 'How much is in vivo CAR-T\n\n  worth today?'
t:
  4: '2026'
  6: $285M
  8: We estimate $285 million in 2026. FMI gives $180 million and Grand View $341 million for broader in vivo cell therapy, while Precedence gives $861 million. We use the T-cell-adjusted Grand View figure because its scope is closest to ours.
note: We use a scope-adjusted estimate rather than a simple average because public sources count very different things in this pre-commercial market.
sources:
  - claim: Future Market Insights estimates $180.0 million in 2026
    url: https://www.futuremarketinsights.com/reports/in-vivo-car-t-cell-therapy-market
    date: 2026-10
    quote: "FMI values the in vivo CAR-T cell therapy market at USD 180.0 million in 2026"
  - claim: Grand View Research estimates $340.7 million for the broader in vivo cell-therapy market in 2026
    url: https://www.grandviewresearch.com/industry-analysis/in-vivo-cell-therapy-market-report
    date: 2026-08
    quote: "Estimated market size in 2026: USD 340.7 Million"
  - claim: Precedence Research estimates $861.25 million in 2026
    url: https://www.precedenceresearch.com/in-vivo-car-t-therapy-market
    date: 2026-09-09
    quote: "Market Size in 2026 | USD 861.25 Million"
```

### ed046
```yaml
status: ok
section: Market size
title: 'How does it compare\n\n  to other markets?'
rows:
- name: In vivo CAR-T
  v: 0.285
  hl: true
- name: NK cell therapy
  v: 0.320
- name: In vivo cell therapy
  v: 0.341
- name: Gene therapy
  v: 4.22
- name: mRNA therapeutics
  v: 6.85
- name: CAR-T therapy
  v: 6.9
- name: T-cell therapy
  v: 9.7
note:
- We compare 2026 global market estimates in USD billions, using the latest public estimate available for each category
- In vivo CAR-T remains tiny beside established CAR-T and gene therapy because its revenue is still mainly trial and clinical supply
sources:
  - claim: NK cell therapy is estimated at $320 million in 2026
    url: https://www.meticulousresearch.com/product/nk-cell-therapy-market-7108
    date: 2026-11
    quote: "estimated USD 320.0 million in 2026"
  - claim: In vivo cell therapy is estimated at $340.7 million in 2026
    url: https://www.grandviewresearch.com/industry-analysis/in-vivo-cell-therapy-market-report
    date: 2026-08
    quote: "Market Estimate, 2026 $340.7M"
  - claim: Gene therapy is estimated at $4.22 billion in 2026
    url: https://www.fortunebusinessinsights.com/industry-reports/gene-therapy-market-100243
    date: 2026-10-19
    quote: "projected to grow from USD 4.22 billion in 2026"
  - claim: mRNA therapeutics is estimated at $6.85 billion in 2026
    url: https://www.fortunebusinessinsights.com/mrna-therapeutics-market-113411
    date: 2026-09-28
    quote: "projected to be worth USD 6.85 billion in 2026"
  - claim: CAR-T therapy is estimated at $6.9 billion in 2026
    url: https://www.grandviewresearch.com/industry-analysis/car-t-cell-therapy-market-report
    date: 2026-06
    quote: "Market Estimate, 2026 $6.9B"
  - claim: T-cell therapy is estimated at $9.7 billion in 2026
    url: https://www.grandviewresearch.com/industry-analysis/t-cell-therapy-market
    date: 2026-07
    quote: "Market Estimate, 2026 $9.7B"
```

### ed047p
```yaml
status: ok
section: Market size
title: How is the in vivo CAR-T market split between its categories?
cats:
- name: Targeted viral vectors
  p: 53
- name: Targeted LNPs
  p: 29
- name: Extracellular vesicles
  p: 2
- name: Undisclosed delivery
  p: 16
- name: Other disclosed routes
  p: 0
note:
- We use the global clinical-pipeline delivery mix as a proxy because there are still no approved in vivo CAR-T product sales to split
- The source counts 45 clinical-stage pipelines: 24 viral, 13 LNP, one extracellular-vesicle program, and seven undisclosed
sources:
  - claim: Clinical-stage in vivo CAR-T pipelines were 53.3% viral, 28.9% LNP, 2.2% EV, and 15.6% undisclosed
    url: https://www.scribd.com/document/1057635228/Cytiva-Invivo-CAR-T%E8%A1%8C%E4%B8%9A%E8%93%9D%E7%9A%AE%E4%B9%A6
    date: 2026
    quote: "病毒载体占 53.3%，脂质纳米颗粒占 28.9%，细胞外囊泡占 2.2%，另有 15.6% 尚未披露"
  - claim: No in vivo CAR-T product has reached an approved label
    url: https://www.futuremarketinsights.com/reports/in-vivo-car-t-cell-therapy-market
    date: 2026-10
    quote: "no in vivo product has yet reached an approved label"
```

### ed048
```yaml
status: ok
section: Market size
title: 'What is behind\n\n  these categories?'
t:
  4: Lentiviral particles target immune cells and insert CAR instructions, usually creating durable CAR expression inside patients
  5: VIRAL CAR VECTORS
  7: Lipid nanoparticles that deliver CAR mRNA or circular RNA into immune cells for transient, repeatable CAR expression in vivo
  8: LNP-RNA DELIVERY
  9: Bioinspired vesicles carry CAR-encoding nucleic acids into immune cells and offer an early nonviral delivery route
  10: EV PLATFORMS
  14: Clinical programs that disclose an in vivo CAR candidate but have not publicly identified the exact delivery technology yet
  15: UNNAMED DELIVERY
  16: The cited pipeline reports no other disclosed delivery class beyond viral vectors, LNPs, and vesicles
  17: OTHER ROUTES
note: We describe the same delivery buckets used in the clinical-pipeline proxy on the previous slide, not a sales split.
sources:
  - claim: Viral and LNP systems dominate current in vivo CAR-T delivery
    url: https://pmc.ncbi.nlm.nih.gov/articles/PMC13729517/
    date: 2026-08-31
    quote: "Currently, two main platforms dominate the field: viral vectors, primarily lentiviral vectors, and non-viral systems based on LNPs-mRNA"
  - claim: Clinical-stage pipeline mix includes viral, LNP, EV, and undisclosed delivery routes
    url: https://www.scribd.com/document/1057635228/Cytiva-Invivo-CAR-T%E8%A1%8C%E4%B8%9A%E8%93%9D%E7%9A%AE%E4%B9%A6
    date: 2026
    quote: "病毒载体占 53.3%，脂质纳米颗粒占 28.9%，细胞外囊泡占 2.2%"
```

### ed049
```yaml
status: ok
section: Market size
title: 'Where in the world is\n\n  in vivo CAR-T money spent?'
regions:
  na:
    pct: 50
    text: North America leads because the US concentrates major developers, trial sites, acquisitions, and specialist cell-therapy infrastructure. Precedence puts the region at 50% of 2025 value.
  eu:
    pct: 25
    text: Europe is the second-largest region, with strong biotech research, specialist hospitals, and active platform development. Precedence estimates about 25% of 2025 value.
  apac:
    pct: 15
    text: Asia-Pacific holds about 15% today but is the fastest-growing region. China has an expanding in vivo CAR-T trial base and a large domestic cell-therapy ecosystem.
  latam:
    pct: 7
    text: We estimate Latin America at about 7% by allocating the residual share using the broader 2025 CAR-T regional mix, where Latin America is much larger than MEA.
  mea:
    pct: 3
    text: We estimate Middle East and Africa at about 3% using the same residual method. Advanced cell-therapy infrastructure remains concentrated in a small number of Gulf and Israeli centers.
note:
- We use Precedence’s direct in vivo shares for North America, Europe, and Asia-Pacific, then split the remaining 10% using the broader CAR-T ratio for Latin America versus MEA
sources:
  - claim: North America had 50% of the in vivo CAR-T market in 2025
    url: https://www.precedenceresearch.com/in-vivo-car-t-therapy-market
    date: 2026-09-09
    quote: "North America led the in vivo CAR-T therapy market in 2025 with a 50% share"
  - claim: Europe had about 25% of the in vivo CAR-T market in 2025
    url: https://www.precedenceresearch.com/in-vivo-car-t-therapy-market
    date: 2026-09-09
    quote: "Europe held about 25% share of the in vivo CAR-T therapy market in 2025"
  - claim: Asia Pacific had about 15% of the in vivo CAR-T market in 2025
    url: https://www.precedenceresearch.com/in-vivo-car-t-therapy-market
    date: 2026-09-09
    quote: "In 2025, Asia Pacific held approximately 15% share of the in vivo CAR-T therapy market"
  - claim: Broader CAR-T revenue in 2025 was $405.01 million in Latin America and $148.50 million in MEA
    url: https://www.globenewswire.com/news-release/2025/10/30/3177604/0/en/car-t-cell-therapy-market-size-to-surpass-usd-146-55-billion-by-2034-fueled-by-innovations-in-cancer-treatment-and-growing-demand-for-personalized-therapies.html
    date: 2025-10-30
    quote: "Latin America | 169.33 | 226.63 | 303.12 | 405.01 | 540.51"
```

### ed050
```yaml
status: ok
section: Market size
title: 'What are the growth rate estimates\n\n  from different sources online?'
note: We use direct in vivo CAR-T forecasts first, then broader in vivo cell-therapy forecasts only as an upside check because their definitions are wider than ours.
t:
  5: '≈ 32.2%\nthrough 2036'
  6: 'Future Market\nInsights'
  7: They forecast growth as trial supply turns into approved-product revenue. We use this as the cautious end of our realistic range.
  9: '≈ 32.5%\nthrough 2035'
  10: 'Precedence\nResearch'
  11: Their direct in vivo CAR-T forecast is almost identical to FMI. We use it to anchor our base case through the next decade.
  13: '≈ 38–42%\nthrough 2036'
  14: 'Metic.\nNext'
  15: Their range includes broader development spending and deal value. We treat it as an optimistic signal, not our core revenue CAGR.
  17: '≈ 49.6%\nthrough 2033'
  18: 'Grand View\nResearch'
  19: Their forecast covers the wider in vivo cell-therapy market. We use it only to test how fast the category could grow if adoption broadens.
  24: FIRM
  25: CAGR
  26: COMMENTS
sources:
  - claim: Future Market Insights forecasts 32.2% CAGR from 2026 to 2036
    url: https://www.futuremarketinsights.com/reports/in-vivo-car-t-cell-therapy-market
    date: 2026-10
    quote: "CAGR, 2026 to 2036 | 32.2%"
  - claim: Precedence Research forecasts 32.5% CAGR from 2026 to 2035
    url: https://www.precedenceresearch.com/in-vivo-car-t-therapy-market
    date: 2026-09-09
    quote: "CAGR, 2026 - 2035 32.50%"
  - claim: Meticulous Next forecasts an indicative 38%-42% CAGR from 2026 to 2036
    url: https://www.meticulousresearch.com/meticulous-next/meticulous-next-in-vivo-car-t-market-outlook-2026-2036
    date: 2026
    quote: "indicative CAGR 38–42% over 2026–2036"
  - claim: Grand View Research forecasts 49.6% CAGR for the broader in vivo cell-therapy market
    url: https://www.grandviewresearch.com/industry-analysis/in-vivo-cell-therapy-market-report
    date: 2026-08
    quote: "CAGR, 2026–2033 49.6%"
```

### ed051
```yaml
status: ok
section: Market size
title: 'What is a realistic CAGR for the\n\n  in vivo CAR-T market?'
note: Direct in vivo CAR-T forecasts cluster near 32%, while broader market forecasts run higher. We use 35% as a base case, with 25% and 45% as downside and upside scenarios.
t:
  15: BEST CASE ≈ 45%
  16: WORST CASE ≈ 25%
  17: '≈ 35%\nthrough 2036'
  19: Early clinical supply is tiny, so approvals can lift revenue quickly. But safety, manufacturing, and trial risk remain high. We use 35%, slightly above the two direct 32% forecasts and below broader 38–50% forecasts.
sources:
  - claim: Future Market Insights forecasts 32.2% CAGR through 2036
    url: https://www.futuremarketinsights.com/reports/in-vivo-car-t-cell-therapy-market
    date: 2026-10
    quote: "CAGR, 2026 to 2036 | 32.2%"
  - claim: Precedence Research forecasts 32.5% CAGR through 2035
    url: https://www.precedenceresearch.com/in-vivo-car-t-therapy-market
    date: 2026-09-09
    quote: "CAGR, 2026 - 2035 32.50%"
  - claim: Meticulous Next forecasts 38%-42% CAGR under its broader definition
    url: https://www.meticulousresearch.com/meticulous-next/meticulous-next-in-vivo-car-t-market-outlook-2026-2036
    date: 2026
    quote: "indicative CAGR 38–42% over 2026–2036"
  - claim: Grand View Research forecasts 49.6% CAGR for broader in vivo cell therapy
    url: https://www.grandviewresearch.com/industry-analysis/in-vivo-cell-therapy-market-report
    date: 2026-08
    quote: "CAGR, 2026–2033 49.6%"
```

### ed052p
```yaml
status: ok
section: Market size
title: 'How much bigger can\n\n  in vivo CAR-T get?'
size: 285
cagr: 35
y0: 2026
lead: 'To get that big, '
condition: the first products must win approvals around 2029–2030, while safer outpatient dosing and autoimmune expansion move in vivo CAR-T beyond a small group of specialist trial centers.
note:
- We start from our $285 million 2026 estimate and apply a 35% base-case CAGR, which implies roughly $5.7 billion by 2036
- We anchor the timing to public forecasts that expect first approvals around 2029–2030 and broader adoption after early safety and efficacy readouts
sources:
  - claim: Meticulous Next expects first in vivo CAR-T approvals around 2029 to 2030
    url: https://www.meticulousresearch.com/meticulous-next/meticulous-next-in-vivo-car-t-market-outlook-2026-2036
    date: 2026
    quote: "first approvals in relapsed multiple myeloma and B-cell malignancies around 2029 to 2030"
  - claim: Future Market Insights expects trial supply to give way to approved use
    url: https://www.futuremarketinsights.com/reports/in-vivo-car-t-cell-therapy-market
    date: 2026-10
    quote: "as trial supply gives way to approved use"
```
