# Longevity market: researched slide signals

**Research date:** November 18, 2026  
**Scope:** independent startups founded in or after 2000 with a biological-aging, preventive-health, healthy-aging or age-related-decline thesis; corporate partner mentions do not imply that the incumbent is an in-scope startup.  
**Kept:** 12 ranked candidates across 8 formats, including **7 Market opportunity signals**.  
**Ranking:** surprise + importance + three-second clarity + six-month durability, each scored 1-5. Ties favor the market-opportunity chapter.

## Ranked candidates

### 1. Neko scan volume rose more than ninefold in 17 months (20/20)

```yaml
format: key-trend
title: Neko scan volume rose more than ninefold in 17 months
chapter: Market opportunity
why_it_matters: This shows the preventive-screening market is hot as a new clinic network scales actual appointments. Delivered
  scans grew far faster than the passage of time.
data:
- label: Neko cumulative completed scans
  value: 10000
  unit: scans
  date: '2025-01-23'
- label: Neko cumulative completed scans
  value: 92002
  unit: scans
  date: '2026-06-30'
note: We compare Neko Health's January 23, 2025 cumulative scans with its September 2026 data report covering January 31,
  2023 through June 30, 2026. The 9.20x ratio is computed as 92,002 / 10,000; the latter report uses an explicit scan denominator.
scores:
  surprise: 5
  importance: 5
  clarity: 5
  durability: 5
fresh:
  period: total
  end: 2026-09
sources:
- claim: 10,000 cumulative completed scans in January 2025
  url: https://www.nekohealth.com/gb/en/press/neko-health-raises-260m-series-b
  date: '2025-01-23'
  quote: 10,000 scans complete since launch, across London and Stockholm
- claim: 92,002 cumulative scans through June 2026
  url: https://www.nekohealth.com/us/en/press/neko-data-story-year-three
  date: '2026-09-14'
  quote: a total of 92,002 scans.
```

### 2. Prenuvo passed 200,000 scans after crossing 100,000 (19/20)

```yaml
format: key-trend
title: Prenuvo passed 200,000 scans after crossing 100,000
chapter: Market opportunity
why_it_matters: This shows the longevity imaging market is hot because a preventive MRI chain more than doubled its delivered
  exam base. Repeat scale also creates a growing research imaging dataset.
data:
- label: Prenuvo cumulative completed scans
  value: 100000
  unit: scans
  date: '2024-12-17'
- label: Prenuvo cumulative completed scans
  value: 200000
  unit: scans, lower bound
  date: '2026-09-29'
note: We compare Prenuvo's December 17, 2024 milestone with its September 29, 2026 company release. The later figure is over
  200,000, so 2.0x is a conservative lower-bound ratio rather than a precise count.
scores:
  surprise: 4
  importance: 5
  clarity: 5
  durability: 5
fresh:
  period: total
  end: 2026-09
sources:
- claim: 100,000 completed whole-body MRI scans
  url: https://prenuvo.com/announcements/100-000-prenuvo-scans-signal-a-historic-milestone-in-proactive-healthcare
  date: '2024-12-17'
  quote: 'Today, we proudly mark a monumental milestone: 100,000 MRI scans completed.'
- claim: Over 200,000 completed scans by September 2026
  url: https://www.prnewswire.com/news-releases/prenuvo-launches-research-network-to-track-disease-patterns-with-whole-body-mri-302892100.html
  date: '2026-09-29'
  quote: With over 200,000 whole-body MRI scans completed, the Biobank enables researchers to help study disease patterns
    years before symptoms may appear.
```

### 3. Neko logged 350,000 registrations and 100,000 scanned members (19/20)

```yaml
format: kpi-trio
title: Neko logged 350,000 registrations and 100,000 scanned members
chapter: Market opportunity
why_it_matters: This shows the longevity consumer market is hot, with substantial declared demand and completed visits in
  a single young network. Advance bookings add an early repeat-purchase signal.
data:
- label: People registered for / joined the scan waitlist
  value: 350000
  unit: people, lower bound
  date: '2026-07-15'
- label: Members who experienced a scan
  value: 100000
  unit: people, lower bound
  date: '2026-07-15'
- label: Members booking and prepaying next-year scan
  value: 75
  unit: percent
  date: '2026-07-15'
note: We use Neko's July 15, 2026 statement for all three figures. Registrations can include people who were already scanned,
  so 350,000 is not a distinct waiting list, and the firm does not report audited active membership.
scores:
  surprise: 4
  importance: 5
  clarity: 5
  durability: 5
fresh:
  period: total
  end: 2026-07
sources:
- claim: More than 350,000 registrations
  url: https://www.nekohealth.com/gb/en/press/neko-health-raises-usd700m-series-c-ahead-of-us-launch
  date: '2026-07-15'
  quote: Over 350,000 people have registered for a Neko Health Scan
- claim: More than 100,000 scanned members
  url: https://www.nekohealth.com/gb/en/press/neko-health-raises-usd700m-series-c-ahead-of-us-launch
  date: '2026-07-15'
  quote: more than 100,000 members have already experienced one.
- claim: 75% prepay next year
  url: https://www.nekohealth.com/gb/en/press/neko-health-raises-usd700m-series-c-ahead-of-us-launch
  date: '2026-07-15'
  quote: On average, 75% of members book and prepay a scan for the following year at the end of their appointment.
```

### 4. Function topped 500,000 members and 100 million tests (18/20)

```yaml
format: kpi-trio
title: Function topped 500,000 members and 100 million tests
chapter: Market opportunity
why_it_matters: This shows the preventive-testing market is hot because a subscription-led provider has reached mass-market
  scale. Its wide annual panel illustrates how longevity services can become a repeat health-data product.
data:
- label: People who have become Function members
  value: 500000
  unit: members, lower bound
  date: '2026-07-31'
- label: Cumulative lab tests reported
  value: 100000000
  unit: tests, lower bound
  date: '2026-07-31'
- label: Tests offered in annual membership
  value: 160
  unit: tests, lower bound
  date: '2026-11-18'
note: We use July 31, 2026 reporting for cumulative signups and tests and Function's pricing page checked on November 18,
  2026 for annual test count. The 500,000 figure is members to date, not verified active paying subscribers; the 100 million
  figure is cumulative tests, not unique people.
scores:
  surprise: 4
  importance: 5
  clarity: 5
  durability: 4
fresh:
  period: total
  end: 2026-11
sources:
- claim: 500,000 members and 100 million tests since 2023
  url: https://athletechnews.com/function-450-million-growth-financing-general-catalyst/
  date: '2026-07-31'
  quote: has grown to more than 500,000 members since its 2023 launch and logged over 100 million lab tests.
- claim: Annual membership offers 160 tests
  url: https://www.functionhealth.com/
  date: '2026-11-18'
  quote: 160+ lab tests
```

### 5. Three in four Neko visitors prepay for next year (18/20)

```yaml
format: icon-grid
title: Three in four Neko visitors prepay for next year
chapter: Market opportunity
why_it_matters: This shows the longevity market is hot because preventive screening is not only attracting first visits but
  also advance purchases. That may support more predictable use of future clinic capacity.
data:
- label: Book and prepay next-year scan
  value: 75
  unit: out of 100 members
  date: '2026-07-15'
- label: Do not book and prepay immediately, derived
  value: 25
  unit: out of 100 members
  date: '2026-07-15'
note: We convert Neko's July 15, 2026 average 75% next-year prepayment rate into a 100-icon grid; the 25 other icons are 100
  minus 75. This is a point-of-appointment booking rate, not independently verified 12-month customer retention.
scores:
  surprise: 4
  importance: 5
  clarity: 5
  durability: 4
fresh:
  period: total
  end: 2026-07
sources:
- claim: Average 75% of members book and prepay next-year scan
  url: https://www.nekohealth.com/gb/en/press/neko-health-raises-usd700m-series-c-ahead-of-us-launch
  date: '2026-07-15'
  quote: On average, 75% of members book and prepay a scan for the following year at the end of their appointment.
```

### 6. About one in 100 healthy Neko members had hidden severe disease (18/20)

```yaml
format: icon-grid
title: About one in 100 healthy Neko members had hidden severe disease
chapter: Pain points
why_it_matters: Some people who feel well are living with serious conditions they do not know they have. A low but consequential
  discovery rate explains demand for proactive screening.
data:
- label: Severe or potentially life-threatening finding
  value: 1
  unit: per 100 Swedish members, approximate
  date: 2025-12
- label: No such documented finding, complement
  value: 99
  unit: per 100 Swedish members, approximate
  date: 2025-12
note: We use Neko's September 14, 2026 observational report of asymptomatic Swedish members aged 28 to 72 across 2023-2025;
  the 2025 reported rate is 1.0%. The other 99 icons are a mathematical complement, not a claim of perfect health; the self-selected
  cohort is not nationally representative.
scores:
  surprise: 4
  importance: 5
  clarity: 5
  durability: 4
fresh:
  period: total
  end: 2026-09
sources:
- claim: About 1% had a severe asymptomatic condition
  url: https://www.nekohealth.com/us/en/press/neko-data-story-year-three
  date: '2026-09-14'
  quote: This rate has remained stable even as scan volumes more than tripled, at 1.0% in 2023, 1.2% in 2024, and 1.0% in
    2025
- claim: Detects severe illness in asymptomatic members
  url: https://www.nekohealth.com/us/en/press/neko-data-story-year-three
  date: '2026-09-14'
  quote: around 1% of Swedish members aged 28 to 72 had a severe and potentially life-threatening condition detected through
    their Neko Scan
```

### 7. Four 2026 deals joined biology-of-aging startups and larger players (17/20)

```yaml
format: deal-timeline
title: Four 2026 deals joined biology-of-aging startups and larger players
chapter: Market opportunity
why_it_matters: This shows the longevity market is hot because outside partners are buying or testing access to aging-biology
  platforms. The deals span drug discovery, geroscience assets, pet medicine, and biological skin aging.
data:
- label: Gordian Bio / Pfizer research collaboration
  value: 1
  unit: announced strategic deal
  date: '2026-01-08'
- label: Pulmatrix / Eos SENOLYTIX proposed merger
  value: 1
  unit: announced strategic deal
  date: '2026-03-26'
- label: Rejuvenate Bio / Merck Animal Health R&D collaboration
  value: 1
  unit: announced strategic deal
  date: '2026-06-08'
- label: Junevity / Amorepacific collaboration and license
  value: 1
  unit: announced strategic deal
  date: '2026-09-29'
note: We compiled four independently announced transactions dated January 8 through September 29, 2026, using company statements
  and Longevity.Technology. The Eos merger remained pending as of November 17, 2026; a collaboration is not a completed acquisition,
  and none of these announcements establishes clinical efficacy.
scores:
  surprise: 5
  importance: 4
  clarity: 4
  durability: 4
fresh:
  period: year
  end: 2026-09
sources:
- claim: Pfizer and Gordian aging-disease platform research deal
  url: https://www.gordian.bio/media/1625/
  date: '2026-01-08'
  quote: Gordian Bio Announces Research Collaboration with Pfizer to Accelerate In Vivo Target Discovery in Obesity
- claim: Pulmatrix and Eos announced geroscience merger agreement
  url: https://www.prnewswire.com/news-releases/pulmatrix-and-eos-senolytix-announce-merger-agreement-to-advance-novel-mitochondrial-therapies-to-improve-healthspan-302726133.html
  date: '2026-03-26'
  quote: today jointly announced a definitive merger agreement under which Pulmatrix will acquire Eos
- claim: Merck Animal Health and Rejuvenate Bio entered research deal
  url: https://www.diamondbiofund.com/en/rejuvenate-bio-announces-6-million-financing-and-strategic-rd-collaboration-with-merck-animal-health/
  date: '2026-06-08'
  quote: In addition to the financing, Rejuvenate Bio and Merck Animal Health have entered into a strategic research and development
    collaboration
- claim: Junevity and Amorepacific collaborated on skin aging
  url: https://longevity.technology/news/junevity-takes-gene-network-reset-into-skincare/
  date: '2026-09-29'
  quote: "The partnership will use Junevity\u2019s RESET platform to identify transcription factors and pathways involved\
    \ in skin aging"
```

### 8. Four longevity platform acquisitions were announced in 2026 (17/20)

```yaml
format: deal-timeline
title: Four longevity platform acquisitions were announced in 2026
chapter: Market opportunity
why_it_matters: This shows the longevity market is hot because operators are acquiring distribution, testing and clinical
  capabilities rather than building everything from scratch. Deals connect labs, supplements, biological-age tests and clinics.
data:
- label: Function acquires mobile phlebotomy company Getlabs
  value: 1
  unit: acquisition announced
  date: '2026-04-08'
- label: Infinite Epigenetics acquires Tally Health
  value: 1
  unit: acquisition announced
  date: '2026-04-29'
- label: Function acquires supplement platform SuppCo
  value: 1
  unit: acquisition announced
  date: '2026-05-12'
- label: Temple acquires longevity clinic Longevous
  value: 1
  unit: acquisition announced
  date: '2026-08-27'
note: We assembled four named longevity-adjacent acquisitions with dates from April 8 through August 27, 2026. Two have the
  same acquirer, Function; this chart counts transactions, not distinct buyers, transaction values or completed post-merger
  integrations.
scores:
  surprise: 4
  importance: 5
  clarity: 4
  durability: 4
fresh:
  period: year
  end: 2026-08
sources:
- claim: Function acquired Getlabs
  url: https://www.prnewswire.com/news-releases/function-acquires-getlabs-bringing-healthcare-directly-to-you-302737483.html
  date: '2026-04-08'
  quote: Function today announced it has acquired Getlabs, a leading mobile healthcare platform
- claim: Infinite Epigenetics acquired Tally Health
  url: https://www.prnewswire.com/news-releases/infinite-epigenetics-acquires-tally-health-to-accelerate-the-future-of-epigenetics-driven-health-and-longevity-302756729.html
  date: '2026-04-29'
  quote: "today announced the acquisition of Tally Health\xAE"
- claim: Function acquired SuppCo
  url: https://www.functionhealth.com/article/function-acquires-suppco-to-bring-trust-and-clarity-to-supplements
  date: '2026-05-12'
  quote: Function today announced it has acquired SuppCo
- claim: Temple acquired Longevous
  url: https://yourstory.com/2026/08/deepinder-goyal-wearable-startup-temple-acquires-longevous
  date: '2026-08-27'
  quote: Temple has acquired evidence-based Longevous as it builds its clinical and scientific capabilities ahead of its launch
```

### 9. Only 10 of 600-plus XPRIZE teams won a second milestone award (17/20)

```yaml
format: funnel
title: Only 10 of 600-plus XPRIZE teams won a second milestone award
chapter: Market challenges
why_it_matters: The scientific funnel remains steep despite broad global enthusiasm for healthspan therapies. Selecting teams
  for further clinical testing is not the same as proving that the treatments extend human healthspan.
data:
- label: Teams registered
  value: 600
  unit: teams, lower bound
  date: '2025-05-12'
- label: Top 40 semifinalists
  value: 40
  unit: teams
  date: '2025-05-12'
- label: Finalist teams
  value: 20
  unit: teams
  date: '2026-08-11'
- label: Second milestone awardees
  value: 10
  unit: teams
  date: '2026-08-11'
note: We chart successive stages reported by XPRIZE on May 12, 2025 and August 11, 2026. More than 600 registered, making
  the displayed 600 the conservative base; these are competing teams including universities, not all independent startups
  or approved products.
scores:
  surprise: 4
  importance: 4
  clarity: 5
  durability: 4
fresh:
  period: total
  end: 2026-08
sources:
- claim: Over 600 teams registered
  url: https://www.xprize.org/news/xprize-healthspan-awards-ceremony-2025
  date: '2025-05-12'
  quote: Over 600 teams across 58 countries registered to compete
- claim: 40 semifinalists
  url: https://www.xprize.org/news/xprize-healthspan-awards-ceremony-2025
  date: '2025-05-12'
  quote: On May 12, 2025, we are announcing the Top 40 XPRIZE Healthspan Semifinalists
- claim: 20 finalists and 10 milestone 2 awardees
  url: https://www.xprize.org/news/20-healthspan-finalist-teams-advance-in-the-race-to-extend-healthy-aging
  date: '2026-08-11'
  quote: Today, XPRIZE announced the 20 Finalist teams advancing to the next stage of the competition
- claim: Ten teams granted milestone 2 awards
  url: https://www.xprize.org/news/20-healthspan-finalist-teams-advance-in-the-race-to-extend-healthy-aging
  date: '2026-08-11'
  quote: Among the finalists, 10 teams from the United States, South Korea, Japan, and China were selected as Milestone 2
    awardees
```

### 10. BioAge stock closed at $5.10, down from a $25.83 peak (17/20)

```yaml
format: fallen-star
title: BioAge stock closed at $5.10, down from a $25.83 peak
chapter: Startup killers
why_it_matters: BioAge illustrates how quickly capital markets can reassess a public longevity platform. Its share-price collapse
  contrasts with enthusiasm around funding and preventive-care demand.
data:
- label: BioAge historical highest closing share price
  value: 25.83
  unit: USD per share, adjusted
  date: '2024-10-21'
- label: BioAge latest completed session close
  value: 5.1
  unit: USD per share, adjusted
  date: '2026-11-17'
note: We compare the historical split-adjusted peak close on October 21, 2024 with the latest full Nasdaq session available
  on November 17, 2026. The decline is 1 - 5.10/25.83 = 80.26%; this is price performance, not company revenue or longevity-treatment
  outcomes.
scores:
  surprise: 4
  importance: 4
  clarity: 5
  durability: 4
fresh:
  period: month
  end: 2026-11
sources:
- claim: All-time high closing price $25.83 on October 21, 2024
  url: https://companiesmarketcap.com/bioage-labs/stock-price-history/
  date: '2026-11-18'
  quote: 'Highest end of day price: $25.83 USD (United States Dollar) on 2024-10-21'
- claim: November 17, 2026 full-session close $5.10
  url: https://finance.yahoo.com/quote/BIOA/history/
  date: '2026-11-17'
  quote: Nov 17, 2026 | 5.30 | 5.30 | 4.98 | 5.10 | 5.10
```

### 11. One partner supplied 100% of BioAge collaboration revenue (17/20)

```yaml
format: single-customer
title: One partner supplied 100% of BioAge collaboration revenue
chapter: Startup killers
why_it_matters: Dependence on one licensing or research partner can make a biotech reported revenue line fragile. BioAge has
  yet to record product sales, so collaboration concentration is especially important.
data:
- label: Collaboration revenue from largest customer
  value: 100
  unit: percent of revenue
  date: '2025-09-30'
- label: Collaboration revenue from largest customer
  value: 100
  unit: percent of revenue
  date: '2026-09-30'
note: We use BioAge's November 5, 2026 Form 10-Q, which explicitly covers the nine months ended September 30 in both 2025
  and 2026. These are research-collaboration revenues from one customer, not commercial drug sales or necessarily BioAge's
  total financial support.
scores:
  surprise: 4
  importance: 4
  clarity: 5
  durability: 4
fresh:
  period: total
  end: 2026-09
sources:
- claim: 100% concentration for both nine-month periods
  url: https://www.sec.gov/Archives/edgar/data/1709941/000119312526450023/bioa-20260930.htm
  date: '2026-11-05'
  quote: "For the nine months ended September 30, 2026 and 2025, the same customer accounted for 100% of the Company\u2019\
    s revenue."
- claim: No product revenue to date
  url: https://www.sec.gov/Archives/edgar/data/1709941/000119312526450023/bioa-20260930.htm
  date: '2026-11-05'
  quote: The Company has not generated any product revenue to date.
```

### 12. BioAge lost $125.54 per $1 of collaboration revenue in Q3 (15/20)

```yaml
format: profit-gap
title: BioAge lost $125.54 per $1 of collaboration revenue in Q3
chapter: Value creation
why_it_matters: BioAge demonstrates the extreme commercialization gap at a clinical-stage longevity company. The ratio is
  distorted by the timing of collaboration accounting and must not be confused with product-unit economics.
data:
- label: Q3 2025 operating loss per $1 collaboration revenue
  value: -11.27
  unit: USD operating profit per $1 collaboration revenue
  date: '2025-09-30'
- label: Q3 2026 operating loss per $1 collaboration revenue
  value: -125.54
  unit: USD operating profit per $1 collaboration revenue
  date: '2026-09-30'
note: 'We divide BioAge''s reported quarterly operating loss by quarterly collaboration revenue in the November 5, 2026 comparative
  results: -$23.140M / $2.054M = -$11.27 and -$37.411M / $0.298M = -$125.54. The September 2026 Novartis contract amendment
  reduced that quarter''s recognized revenue by $1.7M; there are no product sales.'
scores:
  surprise: 4
  importance: 3
  clarity: 5
  durability: 3
fresh:
  period: quarter
  end: 2026-09
sources:
- claim: Quarterly collaboration revenue in 2026 and 2025
  url: https://bioagelabs.gcs-web.com/news-releases/news-release-details/bioage-labs-reports-third-quarter-2026-financial-results-and
  date: '2026-11-05'
  quote: Collaboration revenue was $0.3 million for the quarter ended September 30, 2026, compared to $2.1 million for the
    same period in 2025.
- claim: Operating losses of $37.411M and $23.140M
  url: https://bioagelabs.gcs-web.com/news-releases/news-release-details/bioage-labs-reports-third-quarter-2026-financial-results-and
  date: '2026-11-05'
  quote: Loss from operations
- claim: Accounting adjustment reduced Q3 recognized revenue
  url: https://bioagelabs.gcs-web.com/news-releases/news-release-details/bioage-labs-reports-third-quarter-2026-financial-results-and
  date: '2026-11-05'
  quote: The $1.8 million decrease was primarily due to a $1.7 million cumulative catch-up adjustment
```

## Format audit: tested, not kept

Only cases meeting the format-specific acceptance rule appear above. Missing formats were examined and rejected rather than populated with weak examples.

- **rules-wave:** No consistent four-year official series of longevity-specific legislation or approvals with a recent jump.
- **country-gap:** No like-for-like recent metric across 3-6 national longevity-startup markets; aging demographics alone are too broad.
- **waiting-line:** A 2025 Neko waitlist exceeded cumulative scans by 10x, but it is stale; July 2026 registrations include served people and cannot establish a net waiting count.
- **incident-count:** No official comparable yearly harm/loss series specific to this market.
- **announced-vs-built:** Regulatory and clinic announcements did not yield a verifiable, comparable number delivered.
- **idle-capacity:** No substantiated built-versus-used capacity measure with at least 30% idle.
- **promise-tracker:** TAME, FDA longevity-dog-drug and merger milestones lack three distinct, sourced slips of one target.
- **lobbying-spend:** No sourced LD-2 series with a material jump for an in-scope longevity startup.
- **cost-threshold:** Ezra changed coverage and product tiers; comparing its $1,950/$1,350 legacy scan with later $499/$999 offerings would imply false like-for-like prices.
- **penetration-curve:** No multi-year, representative longevity-product penetration survey or valid historic technology comparison.
- **adoption-race:** Neko launch-to-100k and Prenuvo founding-to-100k dates do not use a comparable commercial launch start.
- **earnings-mentions:** No FactSet or equivalent consistent multi-quarter earnings-call series with a 3x rise.
- **real-world-vs-funding:** Requires proprietary quarterly funding data; funding-round research was excluded by the brief.
- **incumbent-crash:** No valid listed incumbent with an event-linked fall of at least 50% that is distinct from the BioAge fallen-star case.
- **challenger:** No dated private/public pair with compatible revenue or valuation and a clearly closing gap.
- **dominance:** No common-source market share time series for a clearly dominant longevity firm.
- **contract-share:** No meaningful public award series split between startups and incumbents.
- **multiple-gap:** No in-scope listed longevity group and peers with comparable audited current sales and a 3x multiple gap.
- **revenue-per-head:** Private startup revenue and reliable dated employee counts were not both available.
- **dollar-split:** No published allocation of each dollar paid by a longevity customer.
- **forecast-gap:** Published market estimates use incompatible boundaries; five truly comparable same-year figures and a robust 3x difference were not found.
- **value-ladder:** Comparable, independently verified valuations of 4-6 players were not established without funding-round research.
- **funding-event:** Requires yearly funding totals and a funding story, excluded by the instruction not to research funding rounds.

## Interpretation and reliability constraints

- **Company disclosures:** Scan, waitlist and test figures are company-reported, generally unaudited. Cumulative scans are not unique people, and registrations are not automatically customers waiting to be served.
- **Clinical evidence:** Screening detection rates are observational and subject to referral follow-up, self-selection and missing outcomes. They do not prove a scan causes improved longevity or that a severe condition would have been missed by conventional care.
- **Deals:** Timeline marks announcement dates, not closing dates unless the announcement states an acquisition is complete. The March 2026 Eos SENOLYTIX merger was still pending in November 2026.
- **Scope:** Pfizer, Merck Animal Health and Amorepacific appear as strategic partners to in-scope longevity startups, not as longevity startups themselves. BioAge qualifies through its expressly stated aging-biology platform despite initial clinical indications involving metabolic disease.
- **Funding:** Funding rounds and valuation ladders were excluded, as the internal NewMarketPitch funding database is responsible for those formats.
- **Hot right now:** Each Market opportunity candidate uses an announcement or cumulative operational proof dated in 2026. They are not inferred from stale yearly 2025 totals.
- **Quotations:** Source quote fields reproduce short verbatim text fragments/sentences, each under 25 words. One stock-price row and the BioAge operating-loss row are published data tables rather than narrative sentences; these excerpts identify the source rows.
