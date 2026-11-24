# Neocloud: sourced slide signals

Research cutoff: 2026-11-19. Ranked by surprise + importance + three-second clarity + durability. Contract values are not revenue.

## 01. CoreWeave quarterly revenue grew 2.7x in one year (19/20)

```yaml
format: key-trend
title: CoreWeave quarterly revenue grew 2.7x in one year
chapter: Market opportunity
why_it_matters: The market is hot because a specialist AI cloud is converting GPU demand into billions of quarterly sales.
  Revenue grew 168% even as the business continued to scale.
data:
- label: Q3 2025
  value: 1.365
  unit: USD billions
  date: 2025-09
- label: Q3 2026
  value: 3.661
  unit: USD billions
  date: 2026-09
note: We use CoreWeave's 10-Q for the three months ended September 30 in 2025 and 2026. Revenue is recognized sales, not contract
  value.
fresh:
  period: quarter
  end: 2026-09
scores:
  surprise: 5
  importance: 5
  clarity: 5
  durability: 4
sources:
- claim: Q3 revenue, 2025 and 2026
  url: https://www.sec.gov/Archives/edgar/data/1769628/000176962826000465/crwv-20260930.htm
  date: '2026-11-13'
  quote: Revenue for the three months ended September 30, 2026 increased by $2.3 billion, or 168%, compared to the three months
    ended September 30, 2025.
```

## 02. Nscale has $103.4B booked but only $2.6B active (19/20)

```yaml
format: announced-vs-built
title: Nscale has $103.4B booked but only $2.6B active
chapter: Market challenges
why_it_matters: An enormous signed order book can coexist with a tiny currently active contract base. Financing, site delivery
  and customer acceptance still determine how much becomes cash.
data:
- label: Active contracts
  value: 2.6
  unit: USD billions TCV
  date: 2026-08
- label: Active plus contracted
  value: 103.4
  unit: USD billions TCV
  date: 2026-08
note: We use Nscale's September 2026 SEC IPO filing reporting active and total contracted take-or-pay value on August 31.
  The difference is not a count of canceled or failed orders.
fresh:
  period: total
  end: 2026-08
scores:
  surprise: 5
  importance: 5
  clarity: 5
  durability: 4
sources:
- claim: Active and contracted value
  url: https://www.sec.gov/Archives/edgar/data/2110365/000119312526395475/ck0002110365-20260918.htm
  date: '2026-09-18'
  quote: These take-or-pay contracts, totaling $2.6 billion of active and $103.4 billion of active and contracted TCV as of
    August 31, 2026
```

## 03. Nebius AI cloud quarterly sales rose 7.4x (18/20)

```yaml
format: key-trend
title: Nebius AI cloud quarterly sales rose 7.4x
chapter: Market opportunity
why_it_matters: The market is hot because dedicated AI compute is generating far more revenue than a year ago. Part of the
  leap included a $325M one-time platform deployment fee, so it is not all recurring.
data:
- label: Q3 2025 AI cloud
  value: 131.1
  unit: USD millions
  date: 2025-09
- label: Q3 2026 AI cloud
  value: 973.8
  unit: USD millions
  date: 2026-09
note: We use the Nebius Q3 shareholder letter and SEC segment figures for July to September 2025 and 2026. The 2026 figure
  includes nonrecurring partner-deployment revenue.
fresh:
  period: quarter
  end: 2026-09
scores:
  surprise: 5
  importance: 5
  clarity: 5
  durability: 3
sources:
- claim: 2026 AI cloud growth
  url: https://www.sec.gov/Archives/edgar/data/1513845/000110465926126008/tm2629571d1_ex99-2.htm
  date: '2026-11-12'
  quote: Nebius AI cloud revenue was $973.8 million in Q3’26, a 643% increase year-over-year from Q3’25.
- claim: 2025 and 2026 AI cloud segment revenue
  url: https://www.sec.gov/Archives/edgar/data/1513845/000110465926126238/nbis-ex99d2.htm
  date: '2026-11-12'
  quote: Nebius AI cloud
```

## 04. Six AI cloud contracts ranged from $2.8B to $44.6B (18/20)

```yaml
format: deal-timeline
title: Six AI cloud contracts ranged from $2.8B to $44.6B
chapter: Market opportunity
why_it_matters: The market is hot because the biggest AI buyers are signing multi-year compute commitments with specialist
  providers. Contract ceilings are not collected revenue, and delivery conditions still apply.
data:
- label: IREN / Microsoft
  value: 9.7
  unit: USD billions, contract value
  date: 2025-11
- label: Nebius / Meta
  value: 27
  unit: USD billions, up to
  date: 2026-03
- label: CoreWeave / Meta
  value: 21
  unit: USD billions, approximately
  date: 2026-04
- label: IREN / NVIDIA
  value: 3.4
  unit: USD billions, contract value
  date: 2026-05
- label: IREN / AI developers
  value: 2.8
  unit: USD billions, combined
  date: 2026-07
- label: Nscale / Anthropic
  value: 44.6
  unit: USD billions, up to
  date: 2026-08
note: We use signed customer agreements or provider filings dated November 2025 through August 2026. The $108.5B sum is nominal
  maximum contract value across different durations, not expected 2026 revenue.
fresh:
  period: total
  end: 2026-08
scores:
  surprise: 5
  importance: 5
  clarity: 4
  durability: 4
sources:
- claim: IREN and Microsoft
  url: https://iren.gcs-web.com/news-releases/news-release-details/iren-secures-97bn-ai-cloud-contract-microsoft
  date: '2025-11-03'
  quote: with a total contract value of approximately $9.7 billion
- claim: Nebius and Meta
  url: https://www.sec.gov/Archives/edgar/data/1513845/000110465926027886/tm268879d1_6k.htm
  date: '2026-03-16'
  quote: The Agreement and the initial Orders thereunder have a total contract value of up to approximately $27 billion.
- claim: CoreWeave and Meta
  url: https://www.sec.gov/Archives/edgar/data/1769628/000176962826000154/ex991.htm
  date: '2026-04-09'
  quote: to provide AI cloud capacity through December 2032 for approximately $21 billion.
- claim: IREN and NVIDIA
  url: https://iren.gcs-web.com/news-releases/news-release-details/iren-secures-34bn-ai-cloud-contract-nvidia
  date: '2026-05-07'
  quote: The total value of the five-year contract is approximately $3.4 billion.
- claim: IREN developer customers
  url: https://www.sec.gov/Archives/edgar/data/1878848/000187884826000052/iren-20260630.htm
  date: '2026-08-30'
  quote: representing approximately $2.8 billion in aggregate total contract value.
- claim: Nscale and Anthropic
  url: https://www.sec.gov/Archives/edgar/data/2110365/000119312526395475/ck0002110365-20260918.htm
  date: '2026-09-18'
  quote: The Anthropic Services Agreements provide for aggregate payments to us of up to approximately $44.6 billion.
```

## 05. Nscale H1 operating loss reached 350% of revenue (18/20)

```yaml
format: profit-gap
title: Nscale H1 operating loss reached 350% of revenue
chapter: Value creation
why_it_matters: An early cloud can book huge deals yet lose more than three dollars at the operating level per dollar sold.
  Its margins remain far worse than those of an established specialist.
data:
- label: Nscale H1 operating profit / revenue
  value: -350
  unit: percent, reported
  date: 2026-06
- label: CoreWeave H1 operating profit / revenue
  value: -4.1
  unit: percent, derived
  date: 2026-06
note: 'We take Nscale''s six-month 2026 net margin from its IPO filing. We derive CoreWeave H1 by subtracting the September
  quarter from its nine-month SEC 10-Q totals: -$1.366B / $4.653B.'
fresh:
  period: half
  end: 2026-06
scores:
  surprise: 5
  importance: 5
  clarity: 4
  durability: 4
sources:
- claim: Nscale H1 operating loss and revenue
  url: https://www.sec.gov/Archives/edgar/data/2110365/000119312526458722/ck0002110365-20261112.htm
  date: '2026-11-12'
  quote: Operating loss margin
- claim: CoreWeave Q3 and YTD operating result
  url: https://www.sec.gov/Archives/edgar/data/1769628/000176962826000465/crwv-20260930.htm
  date: '2026-11-13'
  quote: CONDENSED CONSOLIDATED STATEMENTS OF OPERATIONS AND COMPREHENSIVE INCOME (LOSS)
```

## 06. CoreWeave has $132.5B of orders behind its cloud (18/20)

```yaml
format: kpi-trio
title: CoreWeave has $132.5B of orders behind its cloud
chapter: Market opportunity
why_it_matters: The market is hot because a leading pure-play cloud has a large contracted work pipeline alongside fast sales
  growth. The backlog remains subject to installation and service delivery.
data:
- label: Q3 revenue
  value: 3.661
  unit: USD billions
  date: 2026-09
- label: Contracted revenue backlog
  value: 132.5
  unit: USD billions
  date: 2026-09
- label: Active power
  value: 1.7
  unit: gigawatts, over
  date: 2026-09
note: We combine CoreWeave's September 2026 quarter results and operating capacity disclosure. Backlog, quarterly revenue
  and active power are different metrics intentionally shown as a KPI trio.
fresh:
  period: quarter
  end: 2026-09
scores:
  surprise: 4
  importance: 5
  clarity: 5
  durability: 4
sources:
- claim: Q3 2026 revenue
  url: https://investors.coreweave.com/news/news-details/2026/CoreWeave-Reports-Strong-Third-Quarter-2026-Results/default.aspx
  date: '2026-11-10'
  quote: Third Quarter 2026 Financial Highlights
- claim: Backlog
  url: https://investors.coreweave.com/news/news-details/2026/CoreWeave-Reports-Strong-Third-Quarter-2026-Results/default.aspx
  date: '2026-11-10'
  quote: Revenue backlog was approximately $132.5 billion as of September 30, 2026.
- claim: Active power
  url: https://investors.coreweave.com/news/news-details/2026/CoreWeave-Reports-Strong-Third-Quarter-2026-Results/default.aspx
  date: '2026-11-10'
  quote: Added more than 200 MWs of active power to reach over 1.7 GW, doubling our active footprint since the start of the
    year
```

## 07. CoreWeave active power trails its contracted power by far (18/20)

```yaml
format: announced-vs-built
title: CoreWeave active power trails its contracted power by far
chapter: Market challenges
why_it_matters: Its sold future infrastructure footprint is far larger than the powered fleet operating today. Delayed delivery
  can postpone the conversion of contract backlog into revenue.
data:
- label: Total contracted
  value: 4.6
  unit: gigawatts, more than
  date: 2026-09
- label: Currently active
  value: 1.7
  unit: gigawatts, more than
  date: 2026-09
note: We compare power contracted and power active in CoreWeave's Q3 2026 release. The 37% is an illustrative ratio of reported
  floor values, not a precise utilization or default rate.
fresh:
  period: quarter
  end: 2026-09
scores:
  surprise: 4
  importance: 5
  clarity: 5
  durability: 4
sources:
- claim: Power capacity at September 2026
  url: https://investors.coreweave.com/news/news-details/2026/CoreWeave-Reports-Strong-Third-Quarter-2026-Results/default.aspx
  date: '2026-11-10'
  quote: Grew total contracted power more than 900 MW to over 4.6 GW
- claim: Operating capacity at September 2026
  url: https://investors.coreweave.com/news/news-details/2026/CoreWeave-Reports-Strong-Third-Quarter-2026-Results/default.aspx
  date: '2026-11-10'
  quote: Added more than 200 MWs of active power to reach over 1.7 GW
```

## 08. Over 90% of Nebius new deal value carried prepayments (18/20)

```yaml
format: icon-grid
title: Over 90% of Nebius new deal value carried prepayments
chapter: Market opportunity
why_it_matters: The market is hot because customers are willing to advance cash to secure AI computing capacity. Up-front
  payments can reduce the provider financing burden before GPUs go live.
data:
- label: Q3 2026 signed contract value with prepayment
  value: 90
  unit: percent, lower bound
  date: 2026-09
note: We use Nebius's November 2026 shareholder letter for contracts signed in July through September 2026. The 90% icon grid
  is a floor, not the fraction of total contract value paid up front.
fresh:
  period: quarter
  end: 2026-09
scores:
  surprise: 4
  importance: 5
  clarity: 5
  durability: 4
sources:
- claim: Q3 Nebius deals carrying prepayment terms
  url: https://www.sec.gov/Archives/edgar/data/1513845/000110465926126008/tm2629571d1_ex99-2.htm
  date: '2026-11-12'
  quote: More than 90% of contract value signed in the third quarter carried a prepayment
```

## 09. One Cerebras buyer still accounts for 38% of sales (18/20)

```yaml
format: single-customer
title: One Cerebras buyer still accounts for 38% of sales
chapter: Startup killers
why_it_matters: Customer concentration is easing but remains material at a cloud and accelerator supplier. A change in one
  buyer's deployment plan could swing total revenue.
data:
- label: MBZUAI, Q3 2025
  value: 70
  unit: percent of sales
  date: 2025-09
- label: MBZUAI, Q3 2026
  value: 38
  unit: percent of sales
  date: 2026-09
note: We use Cerebras's November 2026 10-Q for the corresponding July to September quarters. Cerebras qualifies here through
  its separately marketed Cerebras Cloud inference offering.
fresh:
  period: quarter
  end: 2026-09
scores:
  surprise: 5
  importance: 4
  clarity: 5
  durability: 4
sources:
- claim: Customer concentration
  url: https://www.sec.gov/Archives/edgar/data/2021728/000162828026073494/cbrs-20260930.htm
  date: '2026-11-12'
  quote: accounted for 38% and 70% of our total revenue for the three months ended September 30, 2026 and 2025, respectively
```

## 10. IREN has $20.3B booked against $200M quarterly cloud sales (17/20)

```yaml
format: kpi-trio
title: IREN has $20.3B booked against $200M quarterly cloud sales
chapter: Market opportunity
why_it_matters: The market is hot because a miner-turned-cloud operator now has booked demand far larger than its current
  revenue. Most future contracts still depend on GPUs going live.
data:
- label: Q3 AI cloud sales
  value: 200
  unit: USD millions
  date: 2026-09
- label: Revenue backlog
  value: 20.3
  unit: USD billions
  date: 2026-09
- label: Contracted ARR target
  value: 4
  unit: USD billions, more than
  date: 2026-09
note: We use IREN's November 5 earnings for July to September 2026. The $4B figure is a funded contracted annual-run-rate
  target, not operating revenue already earned.
fresh:
  period: quarter
  end: 2026-09
scores:
  surprise: 4
  importance: 5
  clarity: 4
  durability: 4
sources:
- claim: Quarterly AI Cloud revenue
  url: https://iren.gcs-web.com/news-releases/news-release-details/iren-reports-q1-fy27-results
  date: '2026-11-05'
  quote: AI Cloud quarterly revenue increased 182% sequentially to $200 million
- claim: Backlog
  url: https://iren.gcs-web.com/news-releases/news-release-details/iren-reports-q1-fy27-results
  date: '2026-11-05'
  quote: Revenue backlog increased 22% sequentially to $20.3 billion
- claim: ARR contracting
  url: https://iren.gcs-web.com/news-releases/news-release-details/iren-reports-q1-fy27-results
  date: '2026-11-05'
  quote: More than $4 billion ARR
- claim: Target status
  url: https://iren.gcs-web.com/news-releases/news-release-details/iren-reports-q1-fy27-results
  date: '2026-11-05'
  quote: target is fully contracted and fully funded
```

## 11. One Nscale customer represented 52% of first-half sales (17/20)

```yaml
format: single-customer
title: One Nscale customer represented 52% of first-half sales
chapter: Startup killers
why_it_matters: Major cloud contracts create a concentrated business well before the broad customer base matures. The largest
  customer still provided over half of Nscale revenue in early 2026.
data:
- label: Largest customer, FY2025
  value: 73
  unit: percent of sales
  date: 2025-12
- label: Largest customer, H1 2026
  value: 52
  unit: percent of sales
  date: 2026-06
note: We use Nscale's September IPO filing for full-year 2025 and the first six months of 2026. The periods differ in duration
  and should not be interpreted as a same-quarter comparison.
fresh:
  period: half
  end: 2026-06
scores:
  surprise: 4
  importance: 4
  clarity: 5
  durability: 4
sources:
- claim: First-half 2026 concentration
  url: https://www.sec.gov/Archives/edgar/data/2110365/000119312526395475/ck0002110365-20260918.htm
  date: '2026-09-18'
  quote: For the six months ended June 30, 2026, our largest customer accounted for 52% of our revenue.
- claim: Full-year 2025 concentration
  url: https://www.sec.gov/Archives/edgar/data/2110365/000119312526395475/ck0002110365-20260918.htm
  date: '2026-09-18'
  quote: For the year ended December 31, 2025, our largest customer accounted for 73% of our revenue.
```

## 12. Only one of four Microsoft AI halls was accepted (16/20)

```yaml
format: funnel
title: Only one of four Microsoft AI halls was accepted
chapter: Market challenges
why_it_matters: Even a signed $9.7B contract can take months to turn into delivered computing capacity. Most of IREN's four
  Microsoft halls were still pending at the September reporting date.
data:
- label: Horizon halls in Microsoft contract
  value: 4
  unit: halls
  date: 2026-09
- label: Accepted by Microsoft
  value: 1
  unit: halls
  date: 2026-09
note: We count the four Horizon tranches described in IREN's annual filing and the single one accepted by August 2026. This
  is a two-stage delivery funnel, not a claim that the other halls failed.
fresh:
  period: total
  end: 2026-08
scores:
  surprise: 4
  importance: 4
  clarity: 5
  durability: 3
sources:
- claim: Horizon 1 accepted
  url: https://www.sec.gov/Archives/edgar/data/1878848/000187884826000052/iren-20260630.htm
  date: '2026-09-01'
  quote: Horizon 1 was delivered to, and accepted by, Microsoft in August 2026.
- claim: Remaining halls pending
  url: https://www.sec.gov/Archives/edgar/data/1878848/000187884826000052/iren-20260630.htm
  date: '2026-09-01'
  quote: Horizon 2-4 is targeted for delivery in phases in calendar Q4 2026
```

## Screened formats with no qualifying candidate

No verified candidate was retained for rules-wave, country-gap, waiting-line, incident-count, idle-capacity, promise-tracker, lobbying-spend, penetration-curve, adoption-race, earnings-mentions, real-world-vs-funding, incumbent-crash, fallen-star, challenger, dominance, contract-share, multiple-gap, revenue-per-head, dollar-split, forecast-gap, value-ladder or funding-event. Several require comparable denominators, primary annual series, lending records or funding-round data not defensible from the available public evidence.
