# Managing General Agents: extra-slide signals

**Research cutoff:** November 22, 2026  
**Scope:** Independent and specialist delegated-underwriting MGAs/MGUs using insurer, reinsurer or Lloyd’s capacity. Publicly listed parents and fee-based MGA groups are eligible when their delegated businesses are substantive; risk-bearing carriers used only as comparators or capacity counterparties are explicitly identified.  
**Selection:** 13 ranked candidates. Seven qualify for **Market opportunity** and use current 2026 metrics, releases, contracts or a November 2026 Lloyd’s snapshot. Figures are not interchangeable: **GWP / written premium / bound premium are not MGA revenue or profit**.  
**Scoring:** Surprise, market importance, three-second clarity and six-month durability, each 1–5 (out of 20). Ties are editorially sequenced.  
**Date convention:** Point `date` is the period end or announcement date; `fresh.end` is the newest underlying metric or event, not necessarily the publishing date. For `deal-timeline`, values of 1 represent distinct dated announcements rather than money raised. Quotes are short, exact supporting excerpts; calculated figures appear in the notes.

## Ranked slide candidates

### 01. One carrier provides 47% of TFP’s bound premium | 20/20 | Startup killers

```yaml
format: icon-grid
title: One carrier provides 47% of TFP’s bound premium
chapter: Startup killers
why_it_matters: A delegated underwriting firm can have many carrier partners yet still depend heavily on one source of risk
  capacity. The exposure becomes material when renewal, price, or appetite changes threaten a concentrated share of program
  volume.
data:
- label: Pelagos share of TFP bound premium, trailing 12 months
  value: 47
  unit: '% of bound premium'
  date: 2026-09
note: We use the 12 months ended September 30, 2026, as disclosed in TFP’s November 19 F-1/A. We chart capacity-provider concentration
  in bound premium net of reinsurance, not single-customer revenue concentration or economic risk borne by TFP.
fresh:
  period: total
  end: 2026-09
scores:
  surprise: 5
  importance: 5
  clarity: 5
  durability: 5
sources:
- claim: Capacity provider identity, numerator share and period
  url: https://www.sec.gov/Archives/edgar/data/2128185/000162828026075089/tfpgrouplimited-fx1a1.htm
  date: '2026-11-19'
  quote: net of reinsurance, supported 47% of our Bound Premium in the twelve months ended September 30, 2026.
```

### 02. Ominimo’s premium run-rate jumped from €26.3M to €306.8M | 19/20 | Market opportunity

```yaml
format: key-trend
title: Ominimo’s premium run-rate jumped from €26.3M to €306.8M
chapter: Market opportunity
why_it_matters: This market is hot because a new motor MGA expanded premium volume nearly twelvefold within two years. Its
  delegated-risk model permits rapid expansion without carrying the full underwriting balance sheet.
data:
- label: 2024 annualized run-rate
  value: 26.3
  unit: EUR M gross written premium run-rate
  date: 2024-12
- label: 2025 annualized run-rate
  value: 157.8
  unit: EUR M gross written premium run-rate
  date: 2025-12
- label: July 2026 annualized run-rate
  value: 306.8
  unit: EUR M gross written premium run-rate
  date: 2026-07
note: We use company-reported annualized GWP run-rates as reproduced in July 27, 2026 coverage, not actual full-year earned
  premium or MGA revenue. We calculate 306.8 / 26.3 = 11.67x; Ominimo was an MGA backed by carrier partners at the measurement
  date.
fresh:
  period: month
  end: 2026-07
scores:
  surprise: 5
  importance: 5
  clarity: 5
  durability: 4
sources:
- claim: 2024 and July 2026 premium run-rates
  url: https://beinsure.com/news/insurtech-ominimo-reaches-1-6-bn-valuation/
  date: '2026-07-27'
  quote: Its annualised gross written premium run-rate has climbed from €26.3 mn in 2024 to about €307 mn today.
- claim: MGA structure and third-party risk bearers
  url: https://beinsure.com/news/insurtech-ominimo-reaches-1-6-bn-valuation/
  date: '2026-07-27'
  quote: It prices risk, manages customer relationships and handles claims, while partner carriers carry the underwriting
    risk.
- claim: All three annualized premium run-rate points
  url: https://dealroom.co/news/141203-ominimo-hits-1-6b-valuation-two-years-after-launch-with-20-1m-series-b/
  date: '2026-07-27'
  quote: from roughly €26.3 million in 2024 to €157.8 million in 2025, and now stands at about €306.8 million.
```

### 03. Neptune Flood’s quarterly written premium reached $132.7M | 19/20 | Market opportunity

```yaml
format: key-trend
title: Neptune Flood’s quarterly written premium reached $132.7M
chapter: Market opportunity
why_it_matters: This market is hot because a publicly traded parent of an AI-native MGA recorded successive premium gains.
  The momentum reflects actual program volume rather than a financing announcement.
data:
- label: Q3 2024
  value: 77.7
  unit: USD M written premium
  date: 2024-09
- label: Q3 2025
  value: 101.6
  unit: USD M written premium
  date: 2025-09
- label: Q3 2026
  value: 132.7
  unit: USD M written premium
  date: 2026-09
note: We compare the same third quarter across three years using Neptune releases dated November 12, 2025 and October 20,
  2026. We calculate (132.7 / 77.7 - 1) x 100 = 70.8%; written premium belongs to carrier capacity and is not MGA revenue
  or profit.
fresh:
  period: quarter
  end: 2026-09
scores:
  surprise: 4
  importance: 5
  clarity: 5
  durability: 5
sources:
- claim: Q3 2024 and Q3 2025 written premiums
  url: https://investors.neptuneflood.com/news/news-details/2025/Neptune-Insurance-Holdings-Inc--Reports-Third-Quarter-2025-Results/default.aspx
  date: '2025-11-12'
  quote: written premiums increased 30.7% to $101.6 million compared to $77.7 million in the third quarter of 2024.
- claim: Q3 2026 written premiums
  url: https://investors.neptuneflood.com/news/news-details/2026/Neptune-Insurance-Holdings-Inc--Reports-Third-Quarter-2026-Results/default.aspx
  date: '2026-10-20'
  quote: Written Premium* growth of 31% to a record $132.7 million
- claim: Neptune is an MGA, not a full-stack risk carrier
  url: https://investors.neptuneflood.com/news/news-details/2026/Neptune-Insurance-Holdings-Inc--Reports-Third-Quarter-2026-Results/default.aspx
  date: '2026-10-20'
  quote: Neptune is a leading, AI-native managing general agent
```

### 04. Delegated underwriting handles 45% of Lloyd’s premium | 19/20 | Market opportunity

```yaml
format: icon-grid
title: Delegated underwriting handles 45% of Lloyd’s premium
chapter: Market opportunity
why_it_matters: This market is hot because delegated underwriting already commands nearly half of a major global specialty
  insurance marketplace. It gives specialist underwriting businesses a scaled distribution channel rather than a niche experiment.
data:
- label: Delegated share of Lloyd’s premium income
  value: 45
  unit: '% Lloyd’s premium income'
  date: 2026-11
note: We use Lloyd’s delegated-authority market page, whose figures are marked November 9, 2026. We do not equate all Lloyd’s
  delegated underwriting with independent MGAs; the channel also includes coverholders and service companies.
fresh:
  period: total
  end: 2026-11
scores:
  surprise: 4
  importance: 5
  clarity: 5
  durability: 5
sources:
- claim: Premium share delegated through Lloyd’s
  url: https://www.lloyds.com/market-resources/delegated-authorities
  date: '2026-11-09'
  quote: Delegated underwriting is a key distribution channel for Lloyd’s, accounting for approximately 45% of the market’s
    premium income.
- claim: Lloyd’s data timestamp
  url: https://www.lloyds.com/market-resources/delegated-authorities
  date: '2026-11-09'
  quote: Figures as of 09/11/2026
```

### 05. Five major MGA transactions punctuated 2026 | 19/20 | Market opportunity

```yaml
format: deal-timeline
title: Five major MGA transactions punctuated 2026
chapter: Market opportunity
why_it_matters: This market is hot because strategic and private-equity acquirers announced or completed multiple specialty
  MGA deals within months. Transaction activity spans property, M&A liability, cyber, platform infrastructure, and agribusiness.
data:
- label: Acrisure closes Vave acquisition
  value: 1
  unit: qualifying MGA transaction
  date: '2026-04-01'
- label: Arrow buys Fusion majority stake
  value: 1
  unit: qualifying MGA transaction
  date: '2026-06-04'
- label: Thoma Bravo agrees to buy Accelerant
  value: 1
  unit: qualifying MGA transaction
  date: '2026-08-13'
- label: Munich Re agrees to buy At-Bay
  value: 1
  unit: qualifying MGA transaction
  date: '2026-08-19'
- label: Amynta closes Southern States deal
  value: 1
  unit: qualifying MGA transaction
  date: '2026-10-22'
note: We assemble an illustrative five-deal timeline from the transaction parties’ 2026 releases, not a complete M&A census.
  We distinguish completed purchases from the still-pending Accelerant and At-Bay deals; Accelerant operates a risk exchange
  that includes a substantive MGA Operations segment.
fresh:
  period: month
  end: 2026-10
scores:
  surprise: 5
  importance: 5
  clarity: 5
  durability: 4
sources:
- claim: Vave acquisition completed
  url: https://www.acrisure.com/news/acrisure-completes-acquisition-of-vave-mga-from-canopius
  date: '2026-04-01'
  quote: today announces it has completed the acquisition of Vave, a technology-driven property MGA, from Canopius Group.
- claim: Fusion control transaction
  url: https://fusionspecialty.com/arrow-global-insurance-acquires-majority-stake-in-fusion-specialty-group/
  date: '2026-06-04'
  quote: has acquired a majority stake in the business, marking a significant milestone in Fusion’s growth as a leading global
    specialty MGA.
- claim: Accelerant signed, not closed
  url: https://www.thomabravo.com/press-releases/accelerant-enters-into-definitive-agreement-to-be-acquired-by-thoma-bravo
  date: '2026-08-13'
  quote: entered into a definitive agreement with Thoma Bravo to become a privately held company
- claim: At-Bay transaction agreed
  url: https://www.munichre.com/en/company/media-relations/media-information-and-corporate-news/media-information/2026/media-release-2026-08-19.item-1c676c1dd2d2cf609457c5f0db4ad7a2efbbf862e3185df492b83c53d4d74fb4.html
  date: '2026-08-19'
  quote: Munich Re Group today announced that it has agreed to acquire At-Bay, Inc.
- claim: Southern States Underwriters acquisition completed
  url: https://www.prnewswire.com/news-releases/amynta-group-completes-acquisition-of-southern-states-underwriters-302917382.html
  date: '2026-10-22'
  quote: has completed its acquisition of Southern States Underwriters and SSC Insurance Agency
```

### 06. Pine Walk’s MGAs bound $1,117.7M of premium in nine months | 19/20 | Market opportunity

```yaml
format: kpi-trio
title: Pine Walk’s MGAs bound $1,117.7M of premium in nine months
chapter: Market opportunity
why_it_matters: This market is hot because a specialist MGA incubation platform materially scaled underwriting and fee generation
  in 2026. A newly filed IPO prospectus makes its economics and number of operating specialist teams observable.
data:
- label: Pine Walk bound premium, 9M 2026
  value: 1117.7
  unit: USD M bound premium
  date: 2026-09
- label: Pine Walk placement commissions, 9M 2026
  value: 144.2
  unit: USD M placement commission
  date: 2026-09
- label: Pine Walk operating specialist MGAs
  value: 18
  unit: MGA entities
  date: 2026-11
note: We take nine-month bound premium and placement commissions through September 30, 2026, and live-entity count as of the
  November 19 prospectus from TFP’s SEC F-1/A. We do not treat bound premium as TFP revenue; the separate commissions are
  a revenue component, and the group itself is a fee-based underwriter rather than a risk-bearing carrier.
fresh:
  period: quarter
  end: 2026-09
scores:
  surprise: 5
  importance: 5
  clarity: 4
  durability: 5
sources:
- claim: Pine Walk premiums and 61% year-on-year increase
  url: https://www.sec.gov/Archives/edgar/data/2128185/000162828026075089/tfpgrouplimited-fx1a1.htm
  date: '2026-11-19'
  quote: Bound Premium originated by the Pine Walk segment was $1,117.7 million for the nine months ended September 30, 2026
- claim: Placement commissions and their year-on-year increase
  url: https://www.sec.gov/Archives/edgar/data/2128185/000162828026075089/tfpgrouplimited-fx1a1.htm
  date: '2026-11-19'
  quote: Placement commission in the Pine Walk segment for the nine months ended September 30, 2026 was $144.2 million
- claim: Operating MGA count
  url: https://www.sec.gov/Archives/edgar/data/2128185/000162828026075089/tfpgrouplimited-fx1a1.htm
  date: '2026-11-19'
  quote: with 18 entities as of the date of this prospectus.
```

### 07. Accelerant’s exchange margin dwarfs its risk-carrier margin | 19/20 | Value creation

```yaml
format: profit-gap
title: Accelerant’s exchange margin dwarfs its risk-carrier margin
chapter: Value creation
why_it_matters: The data illustrate how capital-light risk exchange services can earn a different economic return from underwriting
  held on a carrier balance sheet. The comparison is within one company and one quarter.
data:
- label: Exchange Services Q2 2026
  value: 66.2
  unit: '% adjusted EBITDA / operating revenue'
  date: 2026-06
- label: MGA Operations Q2 2026
  value: 43.2
  unit: '% adjusted EBITDA / operating revenue'
  date: 2026-06
- label: Underwriting segment Q2 2026
  value: 1.4
  unit: '% adjusted EBITDA / operating revenue'
  date: 2026-06
note: We divide Accelerant’s Q2 2026 segment adjusted EBITDA of $74.0M, $30.3M and $1.9M by respective segment operating revenue
  of $111.8M, $70.1M and $133.9M, rounding to one decimal. We use comparable non-GAAP segment ratios before corporate costs
  and eliminations; its carrier underwriting segment is a comparator, not classified here as an independent MGA.
fresh:
  period: quarter
  end: 2026-06
scores:
  surprise: 5
  importance: 5
  clarity: 5
  durability: 4
sources:
- claim: Segment operating revenue inputs, Exchange / MGA / Underwriting
  url: https://www.sec.gov/Archives/edgar/data/1997350/000199735026000015/arx-20260630.htm
  date: '2026-08-13'
  quote: Operating revenues (3)  | 111.8
- claim: Additional operating revenue inputs
  url: https://www.sec.gov/Archives/edgar/data/1997350/000199735026000015/arx-20260630.htm
  date: '2026-08-13'
  quote: '70.1'
- claim: Additional operating revenue inputs
  url: https://www.sec.gov/Archives/edgar/data/1997350/000199735026000015/arx-20260630.htm
  date: '2026-08-13'
  quote: '133.9'
- claim: Segment adjusted EBITDA inputs, Exchange / MGA / Underwriting
  url: https://www.sec.gov/Archives/edgar/data/1997350/000199735026000015/arx-20260630.htm
  date: '2026-08-13'
  quote: Adjusted EBITDA  | $  | 74.0
- claim: Additional adjusted EBITDA inputs
  url: https://www.sec.gov/Archives/edgar/data/1997350/000199735026000015/arx-20260630.htm
  date: '2026-08-13'
  quote: '30.3'
- claim: Additional adjusted EBITDA inputs
  url: https://www.sec.gov/Archives/edgar/data/1997350/000199735026000015/arx-20260630.htm
  date: '2026-08-13'
  quote: '1.9'
```

### 08. Neptune pairs $59.6M quarterly revenue with $17.3M profit | 18/20 | Market opportunity

```yaml
format: kpi-trio
title: Neptune pairs $59.6M quarterly revenue with $17.3M profit
chapter: Market opportunity
why_it_matters: This market is hot because a specialist automated flood MGA has recently grown both fee revenue and earnings.
  Its policy book shows that scaled algorithmic underwriting can coexist with positive reported net income.
data:
- label: Q3 2026 revenue
  value: 59.6
  unit: USD M revenue
  date: 2026-09
- label: Q3 2026 GAAP net income
  value: 17.3
  unit: USD M net income
  date: 2026-09
- label: Policies in force, Q3 2026 end
  value: 336000
  unit: policies
  date: 2026-09
note: We use Neptune’s October 20, 2026 earnings release for the three months ended September 30 and its SEC-filed earnings
  presentation for quarter-end policies in force. We show GAAP net income separately from revenue and do not confuse either
  with the $132.7M premium it underwrites on third-party carrier capacity.
fresh:
  period: quarter
  end: 2026-09
scores:
  surprise: 4
  importance: 5
  clarity: 4
  durability: 5
sources:
- claim: Revenue for third quarter 2026
  url: https://investors.neptuneflood.com/news/news-details/2026/Neptune-Insurance-Holdings-Inc--Reports-Third-Quarter-2026-Results/default.aspx
  date: '2026-10-20'
  quote: Revenue growth of 34% to a record $59.6 million
- claim: GAAP net income for third quarter 2026
  url: https://investors.neptuneflood.com/news/news-details/2026/Neptune-Insurance-Holdings-Inc--Reports-Third-Quarter-2026-Results/default.aspx
  date: '2026-10-20'
  quote: Net income increase of 50% to a record $17.3 million
- claim: Policies in force at September 30, 2026
  url: https://www.sec.gov/Archives/edgar/data/2067129/000162828026066494/q32026-earningspresentat.htm
  date: '2026-10-20'
  quote: policies in force reached approximately 336,000
```

### 09. TFP reports a 59% margin against a 32% sector median | 18/20 | Value creation

```yaml
format: profit-gap
title: TFP reports a 59% margin against a 32% sector median
chapter: Value creation
why_it_matters: The prospectus suggests delegated specialist underwriting can operate with much higher fee-business margins
  than traditional insurance-service peers. However, this is management’s non-GAAP peer comparison, not a matched independent
  audit.
data:
- label: TFP group adjusted EBITDA margin, 9M 2026
  value: 59
  unit: '% adjusted EBITDA margin'
  date: 2026-09
- label: Listed insurance services sector median, TFP benchmark
  value: 32
  unit: '% adjusted EBITDA margin'
  date: 2026-09
note: We take the two adjusted EBITDA margins for the nine months ended September 30, 2026 from TFP’s November 19 SEC F-1/A.
  We retain the company-defined benchmark and do not substitute a GAAP operating margin or imply the margin is solely from
  Pine Walk MGAs.
fresh:
  period: quarter
  end: 2026-09
scores:
  surprise: 4
  importance: 5
  clarity: 5
  durability: 4
sources:
- claim: TFP nine-month adjusted EBITDA margin
  url: https://www.sec.gov/Archives/edgar/data/2128185/000162828026075089/tfpgrouplimited-fx1a1.htm
  date: '2026-11-19'
  quote: our Adjusted EBITDA Margin of 59%
- claim: TFP selected listed services sector median
  url: https://www.sec.gov/Archives/edgar/data/2128185/000162828026075089/tfpgrouplimited-fx1a1.htm
  date: '2026-11-19'
  quote: median Adjusted EBITDA Margin of the Listed Insurance Services Sector of 5% and 32%, respectively.
```

### 10. Pine Walk reviewed 850-plus teams but runs only 18 MGAs | 18/20 | Market challenges

```yaml
format: funnel
title: Pine Walk reviewed 850-plus teams but runs only 18 MGAs
chapter: Market challenges
why_it_matters: Most prospective MGA teams never appear as running entities on a top underwriting incubation platform. Strong
  delegated authority, talent, capacity and economics appear to create a narrow scale-ready pipeline.
data:
- label: Prospective Pine Walk MGA opportunities reviewed, cumulative minimum
  value: 850
  unit: prospective opportunities, lower bound
  date: 2026-11
- label: Pine Walk MGAs operating at filing date
  value: 18
  unit: active MGA entities
  date: 2026-11
note: 'We use TFP’s November 19, 2026 F-1/A: more than 850 opportunities reviewed since the platform began in 2017 and 18
  entities live at filing. We show a minimum reviewed-volume versus present entity-stock funnel, NOT a formally reported cohort
  conversion rate; unlaunched pipeline, historical attrition and review timing are not disclosed.'
fresh:
  period: total
  end: 2026-11
scores:
  surprise: 5
  importance: 4
  clarity: 4
  durability: 5
sources:
- claim: Cumulative MGA opportunities reviewed
  url: https://www.sec.gov/Archives/edgar/data/2128185/000162828026075089/tfpgrouplimited-fx1a1.htm
  date: '2026-11-19'
  quote: have reviewed more than 850 prospective opportunities since Pine Walk’s inception.
- claim: Current active MGA count
  url: https://www.sec.gov/Archives/edgar/data/2128185/000162828026075089/tfpgrouplimited-fx1a1.htm
  date: '2026-11-19'
  quote: with 18 entities as of the date of this prospectus.
```

### 11. UK MGA premium is over seven times Germany’s | 18/20 | Tech and infra

```yaml
format: country-gap
title: UK MGA premium is over seven times Germany’s
chapter: Tech and infra
why_it_matters: Underwriting delegation has not reached the same scale across major European markets. The contrast suggests
  that distribution structures and carrier appetite matter as much as insurance spending.
data:
- label: United Kingdom, 2025
  value: 8350
  unit: EUR M estimated MGA GWP
  date: 2025-12
- label: France, 2025
  value: 1310
  unit: EUR M estimated MGA GWP
  date: 2025-12
- label: Germany, 2025
  value: 1130
  unit: EUR M estimated MGA GWP
  date: 2025-12
note: We use a single Howden Re May 2026 study, Figure 2 on PDF page 9, estimating full-year 2025 independent-branded MGA
  gross written premium across comparable country markets. We calculate UK / Germany = 7.39x; Howden estimates include Lloyd’s
  coverholders, are not audited national statistical totals, and are a structural comparison rather than a fresh 2026 momentum
  claim.
fresh:
  period: year
  end: 2025-12
scores:
  surprise: 4
  importance: 4
  clarity: 5
  durability: 5
sources:
- claim: UK 2025 MGA premium in EUR millions
  url: https://www.howdenre.com/sites/howdenre.howdenprod.com/files/2026-05/howden-re-mga_eu-report-filtered-for-quality.pdf
  date: 2026-05
  quote: UK 7,260 8,350
- claim: France 2025 MGA premium in EUR millions
  url: https://www.howdenre.com/sites/howdenre.howdenprod.com/files/2026-05/howden-re-mga_eu-report-filtered-for-quality.pdf
  date: 2026-05
  quote: France 1,200 1,310
- claim: Germany 2025 MGA premium in EUR millions
  url: https://www.howdenre.com/sites/howdenre.howdenprod.com/files/2026-05/howden-re-mga_eu-report-filtered-for-quality.pdf
  date: 2026-05
  quote: Germany 1,060 1,130
- claim: Study’s independent MGA scope
  url: https://www.howdenre.com/sites/howdenre.howdenprod.com/files/2026-05/howden-re-mga_eu-report-filtered-for-quality.pdf
  date: 2026-05
  quote: For the purposes of this analysis, Howden Re focusses on independently branded MGAs
```

### 12. New capacity partnerships are opening doors for specialist MGAs | 17/20 | Market opportunity

```yaml
format: deal-timeline
title: New capacity partnerships are opening doors for specialist MGAs
chapter: Market opportunity
why_it_matters: This market is hot because established carriers and reinsurers signed or announced multiple routes to specialty
  MGA capacity in recent months. These agreements are infrastructure commitments, not MGA funding-round announcements.
data:
- label: Canopius multi-year Vave backing disclosed
  value: 1
  unit: MGA capacity agreement
  date: '2026-04-01'
- label: Arkel extends AmTrust binder
  value: 1
  unit: MGA capacity agreement
  date: '2026-09-30'
- label: Allianz Re agrees Ledgebrook reinsurance
  value: 1
  unit: MGA capacity agreement
  date: '2026-10-07'
- label: Aviva and Q Underwriting renew motor
  value: 1
  unit: MGA capacity agreement
  date: '2026-10-09'
- label: Hippo and Greenlight Re announce emerging-MGA support
  value: 1
  unit: MGA capacity partnership
  date: '2026-10-28'
note: We compile five dated announcements about existing or prospective MGA carrier and reinsurance support, using publication
  dates rather than claiming each policy commenced that day. We count Canopius, AmTrust, Allianz Re, Aviva and Hippo/Greenlight
  as capacity providers, not independent MGA companies; the Hippo partnership is conditional on qualifying future programs.
fresh:
  period: month
  end: 2026-10
scores:
  surprise: 4
  importance: 5
  clarity: 4
  durability: 4
sources:
- claim: Canopius multi-year support
  url: https://www.acrisure.com/news/acrisure-completes-acquisition-of-vave-mga-from-canopius
  date: '2026-04-01'
  quote: Canopius Group continues to be one of Vave’s capacity providers under a multi-year agreement.
- claim: Arkel AmTrust binder
  url: https://www.insuranceage.co.uk/topics/capacity
  date: '2026-09-30'
  quote: Specialist non-standard managing general agent Arkel has secured £380m in delegated authority capacity from AmTrust,
    extending the binder to 2031.
- claim: Allianz Re new agreement
  url: https://www.ledgebrook.com/press-release/ledgebrook-raises-usd-200-million
  date: '2026-10-07'
  quote: Allianz Re has agreed to enter a multi-year reinsurance agreement with Ledgebrook.
- claim: Aviva Q Underwriting renewal
  url: https://www.insuranceage.co.uk/topics/capacity
  date: '2026-10-09'
  quote: Aviva and managing general agent Q Underwriting have renewed their more than two decade long commercial motor partnership
    for a further five years.
- claim: Hippo Greenlight Re support partnership
  url: https://www.nasdaq.com/press-release/hippo-partners-greenlight-re-link-early-stage-insurance-investment-spinnaker-carrier
  date: '2026-10-28'
  quote: that connects opportunities to invest in emerging managing general agents (MGAs) with carrier and reinsurance support
    for their programs.
```

### 13. Hippo reviewed 200-plus programs but added just 27 | 17/20 | Market challenges

```yaml
format: funnel
title: Hippo reviewed 200-plus programs but added just 27
chapter: Market challenges
why_it_matters: Even large program carriers are selective about underwriting teams. A scarce capacity approval pipeline can
  slow MGA launches despite ample entrepreneur interest.
data:
- label: Hippo program opportunities reviewed since 2024, minimum
  value: 200
  unit: program opportunities, lower bound
  date: 2026-06
- label: Hippo programs added since 2024
  value: 27
  unit: programs added
  date: 2026-06
note: We compare Hippo’s reported 200-plus program reviews with its 27 additions over the same broad 2024-to-June-2026 window
  in the July 2026 quarter-two deck. We do not label the 13.5% stock-to-flow ratio as a true acceptance rate because some
  additions came from existing partners and individual submitted cohorts are not reconciled; Hippo is a carrier-capacity provider,
  not counted as an MGA.
fresh:
  period: half
  end: 2026-06
scores:
  surprise: 4
  importance: 4
  clarity: 5
  durability: 4
sources:
- claim: Both stage counts and common broad lookback
  url: https://www.sec.gov/Archives/edgar/data/1828105/000182810526000041/q226quarterlyinvestorupd.htm
  date: '2026-07-30'
  quote: 27 Programs added since 2024 with most from existing partners; staying very selective (reviewed +200 opportunities
    over that horizon)
```

## Format audit: tested and rejected

All requested visual formats were tested against publicly available material. The following were **not** kept because their precise threshold, required matched-series data, or market-perimeter tests were not met. Not including a format is intentional, not missing research.

| Rejected format | Why it did not pass the keep-only-if test |
|---|---|
| `rules-wave` | No comparable four-year MGA-specific counts of laws, enforcement actions or delegated-authority approvals from one authority showing a clear late jump. |
| `waiting-line` | No independently published waitlist-plus-served count for MGA underwriting or carrier capacity. |
| `incident-count` | Cyber claims and catastrophe losses have changing exposure and reporting bases; no clean official MGA-specific rise independent of policy growth. |
| `announced-vs-built` | Announced carrier platforms or MGA launches lack a matched delivered-versus-announced cohort with a quantified gap. |
| `idle-capacity` | Quoted treaty limits, binders and carrier capital are not measured utilization; no defensible 30%-plus idle calculation. |
| `promise-tracker` | No single, well-documented MGA product or regulatory target with three public dated slips. |
| `lobbying-spend` | No verified MGA-sector federal LD-2 time series with an exceptional change attributable to an eligible operating company. |
| `cost-threshold` | MGA operating costs and premiums were not published as one standardized time-series crossing a fixed comparison line. |
| `penetration-curve` | GWP market share is not a cohort survey of adoption by years since launch versus an earlier technology. |
| `adoption-race` | Dramatic new-company growth was found, but two eligible MGAs lack sufficiently comparable dated origin-to-milestone evidence. |
| `earnings-mentions` | No single FactSet/IoT-Analytics-style quarterly earnings-call series with at least threefold growth verified. |
| `real-world-vs-funding` | Funding database is reserved for the client; public real-world adoption and quarterly financing do not form a matched diverging series. |
| `incumbent-crash` | Public insurers are mainly capacity providers, not eligible displaced MGA incumbents; no verified event-linked drop of 50% or more. |
| `fallen-star` | No presently predominant, qualifying public MGA with verified split-adjusted drawdown of 80% or more from peak. |
| `challenger` | Private MGA valuations and listed operating-company revenue were too different in perimeter and dates for a credible closing-gap chart. |
| `dominance` | A single capacity partner’s 47% bound-premium share is concentration, not a historical share series or crushing market-leader dominance. |
| `contract-share` | Carrier capacity agreements are private insurance arrangements, not publicly awarded government contracts with newcomer/incumbent totals. |
| `multiple-gap` | Enterprise values for risk exchanges, fee-underwriters and insurers cannot be divided by inconsistent premium/revenue figures as if like-for-like sales. |
| `revenue-per-head` | The available MGA disclosures generally report written premium per employee, not comparable earned revenue and actual payroll headcount. |
| `dollar-split` | MGA placement fees, claims payments, fronting fees and reinsurer retention were not disclosed in one defensible premium-dollar waterfall. |
| `single-customer` | TFP’s 47% dependency refers to **bound premium from one capacity provider**, not 47% of revenue from a customer. |
| `forecast-gap` | No five independent same-year MGA-market forecasts with a non-outlier threefold spread and identical market definitions. |
| `value-ladder` | A four-to-six-company current verified valuation set with multiple $1B-plus pure MGA enterprises was not available on like-for-like terms. |
| `funding-event` | Deliberately excluded: funding-round formats are computed from the client’s private database. |

**Editorial warnings.** The deal timelines are selected examples, not exhaustively counted market transactions. The two funnel slides use published screening volumes and operating/added program counts, but neither is an audited individual applicant conversion cohort. Howden Re 2025 geographic estimates and TFP’s company-selected peer margin benchmark are explicitly labeled. Do not treat insurer subsidiaries, fronting insurers, or underwriting risk-bearing units as independent MGAs. Do not infer an acquisition closed when the definitive agreement is still pending.
