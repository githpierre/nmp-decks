# AI Data Center: one-data-point slide research

**Research cutoff:** November 22, 2026. **Output:** 13 vetted candidates, ranked by total score. **Market opportunity:** 7 candidates.

**Scope and measurement rules:** Companies must independently develop, own, deliver, or operate third-party AI-optimized physical capacity. Broader data center benchmarks are included only as labeled supply-and-demand proxies, not as AI-only operator statistics. Contracted capacity is not live capacity; planned or nonbinding announcements do not count as leases. Public companies remain market players but not startups. No funding round research is included.

## Ranked shortlist

| Rank | Total / 20 | Format | Chapter | Data point |
|---:|---:|---|---|---|
| 1 | 20 | key-trend | Market opportunity | Observed AI-factory capacity jumped tenfold to 17 GW |
| 2 | 20 | key-trend | Market opportunity | TeraWulf AI hosting revenue surged almost ninefold |
| 3 | 19 | announced-vs-built | Market challenges | Applied Digital has 1,410 MW leased but 250 MW live |
| 4 | 19 | kpi-trio | Market opportunity | CoreWeave hit $132.5B in backlog and 1.7 GW active |
| 5 | 18 | icon-grid | Market opportunity | Four in five future US data center MW are already preleased |
| 6 | 18 | kpi-trio | Market opportunity | TeraWulf signed $27B in leases on 839 MW |
| 7 | 18 | fallen-star | Startup killers | Fermi America fell from $32.53 to $1.95 per share |
| 8 | 17 | funnel | Market challenges | ERCOT shows just 5.9 GW energized against 445.8 GW requested |
| 9 | 17 | rules-wave | Market challenges | US data center bills rose from 54 to 375 in three years |
| 10 | 17 | single-customer | Startup killers | CoreWeave still gets 30% of sales from one customer |
| 11 | 17 | deal-timeline | Market opportunity | Four recent AI campus leases range from $5.2B to $19B |
| 12 | 17 | icon-grid | Market opportunity | Just 1.4% of major US data center capacity sat vacant |
| 13 | 16 | profit-gap | Value creation | TeraWulf loses $1.16 operating for each $1 in sales |

## Candidate records

### 1. Observed AI-factory capacity jumped tenfold to 17 GW (20/20)

```yaml
format: key-trend
title: Observed AI-factory capacity jumped tenfold to 17 GW
chapter: Market opportunity
why_it_matters: A tenfold jump in AI-first campus footprints shows that real-world construction is accelerating.
  This is physical infrastructure momentum, not a forecast of GPU demand.
data:
- label: 93-site AI-factory footprint, inferred potential
  value: 1.7
  unit: GW (estimated)
  date: 2024-09
- label: 93-site AI-factory footprint, inferred potential
  value: 17
  unit: GW (estimated)
  date: 2026-09
note: We use the IEA World Energy Outlook 2026 satellite-based tracking of the same set of 93 purpose-built AI facilities
  through September 2026. The 2024 1.7 GW point is calculated as 17 GW divided by the stated tenfold gain; both
  points are inferred potential capacity based on observed buildings, not energized IT power.
fresh:
  period: month
  end: 2026-09
scores:
  surprise: 5
  importance: 5
  clarity: 5
  durability: 5
sources:
- claim: IEA measures potential physical capacity of 93 AI factories and a tenfold two-year increase to 17 GW.
  url: https://www.iea.org/files/41082112-1153-4b16-b738-d44fb273dfd9/WorldEnergyOutlook2026.pdf
  date: '2026-11-19'
  quote: inferred potential capacity associated with such data centres growing 10-fold in just 24 months to reach
    17 GW
```

### 2. TeraWulf AI hosting revenue surged almost ninefold (20/20)

```yaml
format: key-trend
title: TeraWulf AI hosting revenue surged almost ninefold
chapter: Market opportunity
why_it_matters: Actual AI/HPC facility rent grew far faster than a typical real-estate revenue line. It indicates
  that converted mining infrastructure is moving into paid third-party AI hosting.
data:
- label: Q3 2025 HPC lease revenue
  value: 7.203
  unit: $M
  date: 2025-09
- label: Q3 2026 HPC lease revenue
  value: 62.986
  unit: $M
  date: 2026-09
note: We use TeraWulf GAAP HPC lease revenue for the three months ending September 30 in each year, divided from
  the reported thousands into millions. Growth equals 62.986 / 7.203 = 8.74x; this is recognized lease revenue,
  not prospective bookings.
fresh:
  period: quarter
  end: 2026-09
scores:
  surprise: 5
  importance: 5
  clarity: 5
  durability: 5
sources:
- claim: SEC-filed income statement reports $7.203M and $62.986M in third-quarter HPC lease revenue.
  url: https://www.sec.gov/Archives/edgar/data/1083301/000162828026071306/a_wulfearningsreleaseq32026.htm
  date: '2026-11-06'
  quote: HPC lease revenue | 62,986 | 7,203
```

### 3. Applied Digital has 1,410 MW leased but 250 MW live (19/20)

```yaml
format: announced-vs-built
title: Applied Digital has 1,410 MW leased but 250 MW live
chapter: Market challenges
why_it_matters: Lease demand is materially ahead of ready-to-use AI capacity. The gap is a phased construction obligation,
  not proof that Applied Digital has missed a contracted deadline.
data:
- label: Signed AI-factory critical IT load
  value: 1410
  unit: MW
  date: 2026-08
- label: Live critical IT load at Polaris Forge 1
  value: 250
  unit: MW
  date: 2026-10
note: We compare 1,410 MW of signed AI-factory critical IT leases as of August 31, 2026 with the 250 MW declared
  live on October 1, 2026. This is a 5.64x leased-to-live ratio across the company portfolio and one currently operating
  campus; contracted capacity is not yet all due for delivery.
fresh:
  period: total
  end: 2026-10
scores:
  surprise: 5
  importance: 5
  clarity: 5
  durability: 4
sources:
- claim: Signed AI critical IT leases total about 1.41GW across five campuses.
  url: https://ir.applieddigital.com/news-events/press-releases/detail/163/applied-digital-reports-fiscal-first-quarter-2027-results
  date: '2026-10-07'
  quote: leases for approximately 1.41 GW of critical IT load across five campuses
- claim: 250MW of critical IT had reached ready-for-service in Polaris Forge 1.
  url: https://ir.applieddigital.com/news-events/press-releases/detail/163/applied-digital-reports-fiscal-first-quarter-2027-results
  date: '2026-10-07'
  quote: bringing fully operational critical IT load at the campus to 250 MW
```

### 4. CoreWeave hit $132.5B in backlog and 1.7 GW active (19/20)

```yaml
format: kpi-trio
title: CoreWeave hit $132.5B in backlog and 1.7 GW active
chapter: Market opportunity
why_it_matters: An enormous committed revenue base now accompanies an operating power footprint at gigawatt scale.
  CoreWeave qualifies here through directly operated physical AI infrastructure, not its GPU cloud offering alone.
data:
- label: Q3 2026 revenue
  value: 3.661
  unit: $B
  date: 2026-09
- label: Committed revenue backlog
  value: 132.5
  unit: $B
  date: 2026-09
- label: Active power footprint, lower bound
  value: 1.7
  unit: GW
  date: 2026-09
note: We take all figures from CoreWeave third-quarter 2026 results published November 10, with quarterly revenue
  converted from $3,661M and active power stated as over 1.7 GW. Backlog is management-defined future contracted
  revenue and is not revenue already earned; the 1.7 GW point is a reported lower bound.
fresh:
  period: quarter
  end: 2026-09
scores:
  surprise: 5
  importance: 5
  clarity: 5
  durability: 4
sources:
- claim: Quarterly revenue of $3,661M.
  url: https://www.sec.gov/Archives/edgar/data/1769628/000176962826000465/crwv-20260930.htm
  date: '2026-11-10'
  quote: Revenue | | $ | 3,661
- claim: Committed revenue backlog of $132.5B.
  url: https://investors.coreweave.com/news/news-details/2026/CoreWeave-Reports-Strong-Third-Quarter-2026-Results/
  date: '2026-11-10'
  quote: Revenue backlog was approximately $132.5 billion as of September 30, 2026.
- claim: More than 1.7 GW active power, distinct from contracted power.
  url: https://investors.coreweave.com/news/news-details/2026/CoreWeave-Reports-Strong-Third-Quarter-2026-Results/
  date: '2026-11-10'
  quote: active power to reach over 1.7 GW
```

### 5. Four in five future US data center MW are already preleased (18/20)

```yaml
format: icon-grid
title: Four in five future US data center MW are already preleased
chapter: Market opportunity
why_it_matters: AI and hyperscale buyers are locking up facilities before delivery, signaling exceptional demand.
  New entrants with credible power and build schedules may find customers long before completion.
data:
- label: Preleased share of under-construction MW
  value: 80.4
  unit: '%'
  date: 2026-06
- label: Not preleased, derived complement
  value: 19.6
  unit: '%'
  date: 2026-06
note: We use CBRE primary-market under-construction capacity weighted by MW in the first half of 2026. The available
  19.6% is calculated as 100 minus 80.4; these eight wholesale markets include both AI and non-AI occupants, so
  this is an AI demand proxy rather than an AI-only denominator.
fresh:
  period: half
  end: 2026-06
scores:
  surprise: 4
  importance: 5
  clarity: 5
  durability: 4
sources:
- claim: 80.4% of construction had tenant commitments; complement is 19.6%.
  url: https://www.cbre.com/insights/books/north-america-data-center-trends-h1-2026
  date: '2026-08-27'
  quote: Preleasing activity accelerated with commitments made on 80.4% of all under-construction capacity, compared
    with 74.3% a year ago.
```

### 6. TeraWulf signed $27B in leases on 839 MW (18/20)

```yaml
format: kpi-trio
title: TeraWulf signed $27B in leases on 839 MW
chapter: Market opportunity
why_it_matters: Long-dated AI infrastructure customers have contracted multibillion-dollar physical campus capacity.
  The operating footprint is still much smaller, showing how much rent-bearing delivery remains ahead.
data:
- label: Contracted critical IT power
  value: 839
  unit: MW
  date: 2026-09
- label: Base-term contracted gross lease revenue
  value: 27
  unit: $B (approximately)
  date: 2026-09
- label: Delivered and operating critical IT power
  value: 102
  unit: MW
  date: 2026-09
note: We use the November 6, 2026 investor deck for the September 30 contracted portfolio; the $27B total is approximate
  over 10-to-20-year lease terms and is not current revenue. The reported 102 MW is operating capacity, while the
  other 737 MW is under construction.
fresh:
  period: quarter
  end: 2026-09
scores:
  surprise: 4
  importance: 5
  clarity: 5
  durability: 4
sources:
- claim: 839MW signed and about $27B contracted revenue.
  url: https://investors.terawulf.com/sec-filings/all-sec-filings/content/0001628280-26-071306/terawulfq32026investorpr.htm
  date: '2026-11-06'
  quote: 839 MW CONTRACTED CRITICAL IT ~$27B CONTRACTED REVENUE
- claim: 102MW already operating.
  url: https://www.sec.gov/Archives/edgar/data/1083301/000162828026071306/a_wulfearningsreleaseq32026.htm
  date: '2026-11-06'
  quote: 102 MW of critical IT capacity online at Lake Mariner
```

### 7. Fermi America fell from $32.53 to $1.95 per share (18/20)

```yaml
format: fallen-star
title: Fermi America fell from $32.53 to $1.95 per share
chapter: Startup killers
why_it_matters: Even an enormous proposed AI campus can lose nearly all public-market credibility before delivering
  capacity. The cancellation of its first AI tenant lease underlines the execution risk behind powered-land announcements.
data:
- label: All-time highest daily close, split-adjusted
  value: 32.53
  unit: USD/share
  date: '2025-10-01'
- label: Latest daily close before research cutoff
  value: 1.95
  unit: USD/share
  date: '2026-11-20'
note: We compare the highest historical daily close on October 1, 2025 with the November 20, 2026 close; (32.53
  - 1.95) / 32.53 = 94.0%. The company disclosed termination of the TensorWave lease on November 10; its separate
  600 MW hyperscaler letter of intent is explicitly nonbinding and is not treated as a lease.
fresh:
  period: month
  end: 2026-11
scores:
  surprise: 5
  importance: 4
  clarity: 5
  durability: 4
sources:
- claim: First-day share close of $32.53.
  url: https://ca.finance.yahoo.com/quote/FRMI/history/
  date: '2025-10-01'
  quote: Oct 1, 2025 | 25.1300 | 33.4600 | 24.5000 | 32.5300
- claim: Nov 20 share close $1.95, adjusted close identical.
  url: https://stockanalysis.com/stocks/frmi/history/
  date: '2026-11-20'
  quote: Nov 20, 2026 | 2.03 | 2.09 | 1.80 | 1.95 | 1.95
- claim: TensorWave lease was terminated November 10 rather than delivering $6.5B of anticipated rent.
  url: https://www.sec.gov/Archives/edgar/data/2071778/000207177826000058/frmi-20260930.htm
  date: '2026-11-12'
  quote: on November 10, 2026, the TensorWave Lease was terminated in accordance with its terms.
```

### 8. ERCOT shows just 5.9 GW energized against 445.8 GW requested (17/20)

```yaml
format: funnel
title: ERCOT shows just 5.9 GW energized against 445.8 GW requested
chapter: Market challenges
why_it_matters: Grid applications vastly exceed the power that has reached live operations. Many applications are
  speculative and future-dated, so this measures the current screening bottleneck, not the probability a given AI
  campus will fail.
data:
- label: All large-load applications, cumulative through 2033
  value: 445.8
  unit: GW
  date: 2026-04
- label: Applications with studies submitted or later, derived
  value: 124.8
  unit: GW
  date: 2026-04
- label: Section 9.5 met or further, derived
  value: 31.1
  unit: GW
  date: 2026-04
- label: Approved to energize or already energized, derived
  value: 9.1
  unit: GW
  date: 2026-04
- label: Observed energized large loads
  value: 5.9
  unit: GW
  date: 2026-04
note: 'We derive cumulative funnel bars from ERCOT April 2026 status buckets: 321.0 GW no studies, 93.7 GW under
  review, 22.0 GW Section 9.5 met, 3.2 GW approved but not operational, and 5.9 GW energized; they sum to 445.8
  GW. Applications extend to 2033 and include non-AI large loads, and the stages are a cross-sectional queue snapshot,
  not one application cohort.'
fresh:
  period: month
  end: 2026-04
scores:
  surprise: 5
  importance: 5
  clarity: 4
  durability: 3
sources:
- claim: Current large-load application volume 445.8GW and no studies 321GW.
  url: https://www.ercot.com/files/docs/2026/05/13/ERCOT-Monthly-April-2026-FINAL.pdf
  date: '2026-05-13'
  quote: applications of large loads now totaling 445.8 gigawatts (GW) by 2033
- claim: ERCOT advanced stages total 93.7GW, 22GW, 3.2GW and 5.9GW.
  url: https://www.ercot.com/files/docs/2026/05/13/ERCOT-Monthly-April-2026-FINAL.pdf
  date: '2026-05-13'
  quote: ERCOT has 5.9 GW of Observed Energized Large Loads
```

### 9. US data center bills rose from 54 to 375 in three years (17/20)

```yaml
format: rules-wave
title: US data center bills rose from 54 to 375 in three years
chapter: Market challenges
why_it_matters: Policy and community opposition are now a major variable in campus timelines. This is an unusually
  rapid rise in legislative attention even though many proposals never pass.
data:
- label: '2023: mostly incentives'
  value: 54
  unit: state bills introduced
  date: 2023-12
  story: Predominantly tax benefits and faster approvals
- label: '2024: early scrutiny'
  value: 75
  unit: state bills introduced
  date: 2024-12
  story: Bill volume continued to rise
- label: '2025: regulation wave'
  value: 243
  unit: state bills introduced
  date: 2025-12
  story: More restrictions appeared
- label: '2026 partial: through July 15'
  value: 375
  unit: state bills introduced
  date: 2026-07
  story: Roughly three quarters sought restrictions; partial year
note: We use Washington Post analysis of LegiScan state-level bills mentioning data centers, with consistent exclusions
  for incidental, government-only, and non-AI references. The 2026 bar is only through July 15, not a full-year
  estimate; bill introduction is not passage.
fresh:
  period: year
  end: 2026-07
scores:
  surprise: 5
  importance: 5
  clarity: 4
  durability: 3
sources:
- claim: '2023 state bills: 54.'
  url: https://www.washingtonpost.com/nation/2026/09/03/how-data-center-backlash-is-growing-us-statehouses/
  date: '2026-09-03'
  quote: '2023

    54'
- claim: '2024 state bills: 75.'
  url: https://www.washingtonpost.com/nation/2026/09/03/how-data-center-backlash-is-growing-us-statehouses/
  date: '2026-09-03'
  quote: '2024

    75'
- claim: '2025 state bills: 243.'
  url: https://www.washingtonpost.com/nation/2026/09/03/how-data-center-backlash-is-growing-us-statehouses/
  date: '2026-09-03'
  quote: '2025

    243'
- claim: '2026 state bills through July 15: 375.'
  url: https://www.washingtonpost.com/nation/2026/09/03/how-data-center-backlash-is-growing-us-statehouses/
  date: '2026-09-03'
  quote: '2026*

    375 total'
```

### 10. CoreWeave still gets 30% of sales from one customer (17/20)

```yaml
format: single-customer
title: CoreWeave still gets 30% of sales from one customer
chapter: Startup killers
why_it_matters: Its dependence on a single buyer has fallen sharply but remains material. A change in one AI lab
  or hyperscaler relationship could still reshape facility demand and financing.
data:
- label: Top customer, Q3 2025 revenue share
  value: 67
  unit: '%'
  date: 2025-09
- label: Top customer, Q3 2026 revenue share
  value: 30
  unit: '%'
  date: 2026-09
note: We take the top-customer contribution directly from CoreWeave Form 10-Q for the three months ended September
  30 in 2025 and 2026. The next-largest 2026 customer represented 24%, but the plotted measure is largest-customer
  share only.
fresh:
  period: quarter
  end: 2026-09
scores:
  surprise: 4
  importance: 5
  clarity: 4
  durability: 4
sources:
- claim: Largest buyer represented about 67% in Q3 2025.
  url: https://www.sec.gov/Archives/edgar/data/1769628/000176962826000465/crwv-20260930.htm
  date: '2026-11-10'
  quote: approximately 67% of our revenue from our top customer
- claim: Largest buyer represented about 30% in Q3 2026.
  url: https://www.sec.gov/Archives/edgar/data/1769628/000176962826000465/crwv-20260930.htm
  date: '2026-11-10'
  quote: approximately 30% and 24% of our revenue from our top two customers
```

### 11. Four recent AI campus leases range from $5.2B to $19B (17/20)

```yaml
format: deal-timeline
title: Four recent AI campus leases range from $5.2B to $19B
chapter: Market opportunity
why_it_matters: The largest AI infrastructure customers are signing long physical facility leases worth billions
  each. This converts theoretical data center demand into durable commitments to identifiable operators.
data:
- label: Applied Digital, Delta Forge 1, signed Apr 23
  value: 7.5
  unit: $B base-term rent
  date: '2026-04-23'
- label: Applied Digital, Polaris Forge 3, signed May 20
  value: 7.5
  unit: $B base-term rent
  date: '2026-05-20'
- label: Applied Digital, Delta Forge 2, signed Jun 8
  value: 5.2
  unit: $B base-term rent
  date: '2026-06-08'
- label: TeraWulf, Anthropic at Justified, signed Jul 6
  value: 19
  unit: $B base-term rent
  date: '2026-07-06'
note: We count four publicly signed third-party physical-facility leases in April through July 2026, totaling approximately
  $39.2B over initial base terms, without optional renewals. The TeraWulf Anthropic lease was disclosed in July
  and reconfirmed in November; all four amounts are future contractual rent, not capacity already operating.
fresh:
  period: total
  end: 2026-11
scores:
  surprise: 4
  importance: 5
  clarity: 5
  durability: 3
sources:
- claim: Delta Forge 1 signed lease for $7.5B.
  url: https://ir.applieddigital.com/sec-filings/all-sec-filings/content/0001144879-26-000036/apld_deltaforgexprxfinal.htm
  date: '2026-04-23'
  quote: This lease represents approximately $7.5 billion in total contracted value over an estimated 15-year lease
    term
- claim: Polaris Forge 3 signed lease for $7.5B.
  url: https://ir.applieddigital.com/news-events/press-releases/detail/152/applied-digital-reaches-significant-milestone-surpassing-1
  date: '2026-05-20'
  quote: valued at approximately $7.5 billion in base-term contracted revenue
- claim: Delta Forge 2 signed lease for $5.2B.
  url: https://ir.applieddigital.com/sec-filings/all-sec-filings/content/0001493152-26-027984/ex99-1.htm
  date: '2026-06-08'
  quote: representing approximately $5.2 billion in base-term contracted revenue
- claim: Anthropic Justified 20-year lease for $19B.
  url: https://investors.terawulf.com/sec-filings/all-sec-filings/content/0001104659-26-080583/tm2619468d1_ex99-1.htm
  date: '2026-07-06'
  quote: The lease is expected to generate approximately $19 billion of contracted revenue over the initial lease
    term.
```

### 12. Just 1.4% of major US data center capacity sat vacant (17/20)

```yaml
format: icon-grid
title: Just 1.4% of major US data center capacity sat vacant
chapter: Market opportunity
why_it_matters: Customers have almost no immediately available space in major US wholesale markets. This scarcity
  supports the strategic value of powered and permitted AI-first sites.
data:
- label: Occupied share of live inventory, derived
  value: 98.6
  unit: '%'
  date: 2026-06
- label: Vacant share of live inventory
  value: 1.4
  unit: '%'
  date: 2026-06
note: We use the CBRE H1 2026 vacancy survey of eight primary North American wholesale data center markets and derive
  occupied share as 100 minus 1.4. This includes general wholesale capacity alongside AI facilities and must be
  labeled as the broader supply backdrop.
fresh:
  period: half
  end: 2026-06
scores:
  surprise: 4
  importance: 5
  clarity: 5
  durability: 3
sources:
- claim: 1.4% primary market vacancy, 1.6% a year earlier.
  url: https://www.cbre.com/insights/books/north-america-data-center-trends-h1-2026
  date: '2026-08-27'
  quote: primary market vacancy fell to a record low of 1.4% in H1 from 1.6% in H1 2025
```

### 13. TeraWulf loses $1.16 operating for each $1 in sales (16/20)

```yaml
format: profit-gap
title: TeraWulf loses $1.16 operating for each $1 in sales
chapter: Value creation
why_it_matters: Converting mining sites into AI campuses can create revenue long before it creates GAAP operating
  profits. This loss per sales dollar worsened despite a sharp increase in AI lease revenue.
data:
- label: Q3 2025 GAAP operating income per $1 revenue
  value: -0.49
  unit: USD per $1 sales
  date: 2025-09
- label: Q3 2026 GAAP operating income per $1 revenue
  value: -1.16
  unit: USD per $1 sales
  date: 2026-09
note: 'We calculate GAAP operating result divided by consolidated GAAP revenue from TeraWulf third-quarter filings:
  -$24.672M / $50.578M in 2025 and -$88.225M / $76.230M in 2026. Results include Bitcoin and AI/HPC activities and
  are not an AI-only segment margin; chart values are rounded to two decimals.'
fresh:
  period: quarter
  end: 2026-09
scores:
  surprise: 5
  importance: 4
  clarity: 4
  durability: 3
sources:
- claim: Comparative consolidated total revenue in the third quarter.
  url: https://www.sec.gov/Archives/edgar/data/1083301/000162828026071306/a_wulfearningsreleaseq32026.htm
  date: '2026-11-06'
  quote: Total revenue | 76,230 | 50,578
- claim: Comparative GAAP operating losses in the third quarter.
  url: https://www.sec.gov/Archives/edgar/data/1083301/000162828026071306/a_wulfearningsreleaseq32026.htm
  date: '2026-11-06'
  quote: Operating loss | (88,225) | (24,672)
```

## Format audit: tested but not forced

The shortlist contains 13 slides using 10 distinct formats. Other requested formats were tested against the published evidence and their explicit acceptance thresholds. Rejections below mean there was no defensible, source-complete slide, not that the phenomenon does not exist.

- **country-gap:** JLL compared 2026 grid waits in city hubs, not whole-country averages. Labeling Tokyo or Mumbai as a national country figure would be misleading.
- **waiting-line:** The ERCOT request queue is not a verified waitlist of serious AI projects with matched served counts, so its request-to-live ratio was not reused as waiting time.
- **incident-count:** No consistent official yearly series of AI data center incidents or losses with a material confirmed rise.
- **idle-capacity:** CBRE inventory and leases cannot establish at least 30% physically built AI-specific capacity idle. Preleasing is not utilization.
- **promise-tracker:** Projects had future delivery targets and revisions, but no one milestone with three independently dated missed deadlines.
- **lobbying-spend:** No robust LD-2 apples-to-apples company lobbying jump specific enough to physical AI campuses.
- **cost-threshold:** High-density build costs and power prices are reported, but no verified 4-10 point time series crossing a single comparable benchmark.
- **penetration-curve:** No consistent survey series tracking physical AI data center adoption by years since launch versus earlier technology.
- **adoption-race:** New campus lease milestones are real, but historical leaders lack a comparable company inception-to-milestone timeline.
- **earnings-mentions:** No verifiable FactSet or IoT Analytics quarterly cited-company series increased at least threefold under one methodology.
- **real-world-vs-funding:** The requested internal quarterly funding database was not provided. Funding round reconstruction from external databases was excluded.
- **incumbent-crash:** Fermi is a newly listed developer, not an established incumbent, so its collapse belongs in fallen-star only.
- **challenger:** No clean, dated private-versus-public valuation or revenue series establishing rapid catch-up with common entity definitions.
- **dominance:** No credible multi-period market share series for AI-first physical capacity developers with stable coverage.
- **contract-share:** Commercial hyperscaler leases do not constitute public-sector contract awards; no valid new-vs-incumbent public-award series.
- **multiple-gap:** Sector valuations mix developers, GPU clouds, mining and pre-revenue shells. A threefold comparable enterprise-value-to-sales gap was not verified.
- **revenue-per-head:** Current employee counts for private facility developers are not sufficiently harmonized with booked revenue.
- **dollar-split:** Published leases give price and term, but no audited breakdown of customer spending into landlord cost, power, depreciation and margin.
- **forecast-gap:** Forecasts for 2030 differ on AI-only campuses, all data centers, and total equipment spend, so five like-for-like publishers could not be established.
- **value-ladder:** A 4-6 player private AI-campus valuation ladder cannot be sourced without private funding-derived values, explicitly excluded from this task.
- **funding-event:** Funding round formats must be computed from the internal funding database, not researched externally.

**Important exclusions:** Fermi America's terminated $6.5B TensorWave lease is not a live deal; its 600 MW November 10 letter of intent is nonbinding. CoreWeave backlog is not recognized revenue. The IEA satellite inferred potential MW is not energized IT load. ERCOT large-load applications are not an AI-only cohort. Grid and wholesale market proxies include non-AI workloads.

**Scoring:** surprise + market importance + three-second clarity + six-month durability, each 1 to 5. Higher combined score comes first; ties favor market importance, then surprise.
