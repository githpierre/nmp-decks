# Stablecoin payments | Extra data-driven signals | November 22, 2026

Research candidates ranked by total of surprise, importance, three-second clarity and six-month durability (maximum 20).

### Signal 01 | 19/20
```yaml
format: key-trend
title: Circle's payment network volume rose fivefold in six months
chapter: Market opportunity
why_it_matters: Live payment-specific volume is multiplying in 2026. The Circle Payments Network rose from an $8.3B to
  a $41.3B annualized pace in two quarters.
data:
- label: Q1 2026
  value: $8.3B
  unit: annualized payment volume
  date: 2026-03
- label: Q2 2026
  value: $14.7B
  unit: annualized payment volume
  date: 2026-06
- label: Q3 2026
  value: $41.3B
  unit: annualized payment volume
  date: 2026-09
note: We use Circle Payments Network annualized payment transaction volume derived from each quarter-end trailing 30
  days. This is payment network volume, not all USDC transfers.
fresh:
  period: quarter
  end: 2026-09
scores:
  surprise: 5
  importance: 5
  clarity: 5
  durability: 4
sources:
- claim: CPN annualized volume Q1 2026 $8.3B
  url: https://www.circle.com/pressroom/circle-reports-first-quarter-2026-results
  date: '2026-05-11'
  quote: with $8.3 billion in annualized transaction volume
- claim: CPN annualized volume Q2 2026 $14.7B
  url: https://www.circle.com/pressroom/circle-reports-second-quarter-2026-results
  date: '2026-08-05'
  quote: CPN reached $14.7 billion in annualized transaction volume for the trailing 30 days
- claim: CPN annualized volume Q3 2026 $41.3B
  url: https://www.sec.gov/Archives/edgar/data/1876042/000187604226000309/finalq3epr-110326.htm
  date: '2026-11-04'
  quote: CPN hit $41.3B in annualized TPV this quarter
```

### Signal 02 | 19/20
```yaml
format: key-trend
title: Visa's stablecoin settlement pace passed $20B
chapter: Market opportunity
why_it_matters: A mainstream card network is settling more money through stablecoins. Its annualized pace has grown from
  $3.5B to more than $20B in under a year.
data:
- label: Nov 2025
  value: $3.5B
  unit: annualized stablecoin settlement
  date: 2025-11
- label: Apr 2026
  value: $7B
  unit: annualized stablecoin settlement
  date: 2026-04
- label: Sep 2026
  value: '>$20B'
  unit: annualized stablecoin settlement
  date: 2026-09
note: We use Visa disclosures of annualized settlement pace, not annual completed payments. The September figure is a
  lower bound and the April figure describes a pilot.
fresh:
  period: month
  end: 2026-09
scores:
  surprise: 5
  importance: 5
  clarity: 5
  durability: 4
sources:
- claim: Visa November 2025 $3.5B pace
  url: https://corporate.visa.com/en/sites/visa-perspectives/press-releases/visa-launches-stablecoin-settlement-in-the-united-states.html
  date: '2025-12-16'
  quote: Visa’s monthly stablecoin settlement volume passed a $3.5 billion annualized run rate
- claim: Visa April 2026 $7B pace
  url: https://corporate.visa.com/en/sites/visa-perspectives/press-releases/visa-expands-stablecoin-settlement-adds-five-blockchains.html
  date: '2026-04-29'
  quote: has reached a $7 billion annualized stablecoin settlement run rate
- claim: Visa September 2026 exceeded $20B pace
  url: https://www.visa.com/en-us/thought-leadership/innovation/financing-stablecoin-linked-card-programs
  date: '2026-09-08'
  quote: stablecoin settlement volume recently surpassed a $20 billion annualized run rate
```

### Signal 03 | 18/20
```yaml
format: deal-timeline
title: Four payments acquisitions show the giants buying stablecoin rails
chapter: Market opportunity
why_it_matters: The biggest payment firms are acquiring rather than merely testing stablecoin infrastructure. The deals
  link digital dollars to card acceptance, payouts and local bank rails.
data:
- label: Stripe buys Bridge (closed)
  value: 1
  unit: acquisition
  date: 2025-02
- label: Nium buys Cypher (closed)
  value: 1
  unit: acquisition
  date: 2026-07
- label: Mastercard buys BVNK (closed)
  value: 1
  unit: acquisition
  date: 2026-08
- label: Circle agrees to buy Tazapay (pending)
  value: 1
  unit: announced deal
  date: 2026-09
note: We use dated buyer releases. The first three acquisitions closed, while Circle announced a signed deal for Tazapay
  that is expected to close in 2027.
fresh:
  period: total
  end: 2026-09
scores:
  surprise: 5
  importance: 5
  clarity: 5
  durability: 3
sources:
- claim: Stripe Bridge close
  url: https://stripe.com/newsroom/news/stripe-completes-bridge-acquisition
  date: '2025-02-04'
  quote: today announced that it has completed its acquisition of Bridge.
- claim: Nium Cypher acquisition
  url: https://www.nium.com/newsroom/nium-acquires-cypher
  date: '2026-07-08'
  quote: today announced the acquisition of Cypher, a crypto-native non-custodial wallet and issuing company.
- claim: Mastercard BVNK close
  url: https://www.mastercard.com/global/en/news-and-trends/press/2026/august/mastercard-completes-acquisition-of-bvnk-to-advance-global-stabl.html
  date: '2026-08-03'
  quote: 'Mastercard (NYSE: MA) today completed its acquisition of BVNK'
- claim: Circle Tazapay signed agreement
  url: https://investor.circle.com/news/news-details/2026/Circle-Expands-Global-Payments-Infrastructure-with-Agreement-to-Acquire-Singapore-Based-Cross-Border-Payments-Platform-Tazapay/default.aspx
  date: '2026-09-08'
  quote: has signed a definitive agreement to acquire Tazapay
```

### Signal 04 | 18/20
```yaml
format: kpi-trio
title: Visa has more than 160 live stablecoin card programs
chapter: Market opportunity
why_it_matters: Stablecoin spending cards have become a large active network. Visa reports rapid annual spending growth
  alongside a much larger stablecoin settlement operation.
data:
- label: Live card programs
  value: '>160'
  unit: programs
  date: 2026-09
- label: Year-over-year card payment volume growth
  value: ~200%
  unit: percent growth
  date: 2026-09
- label: Settlement run rate
  value: '>$20B'
  unit: annualized dollars
  date: 2026-09
note: We use Visa figures for live stablecoin-linked cards and its reported year-on-year payment volume growth. The settlement
  pace covers all Visa stablecoin settlement, not cards alone.
fresh:
  period: month
  end: 2026-09
scores:
  surprise: 4
  importance: 5
  clarity: 5
  durability: 4
sources:
- claim: Visa more than 160 live card programs
  url: https://www.visa.com/en-us/thought-leadership/innovation/financing-stablecoin-linked-card-programs
  date: '2026-09-08'
  quote: more than 160 stablecoin-linked card programs were live around the world
- claim: Visa nearly 200% yoy payment volume rise
  url: https://www.visa.com/en-us/thought-leadership/innovation/financing-stablecoin-linked-card-programs
  date: '2026-09-08'
  quote: payment volume on those programs grew nearly 200% year over year
- claim: Visa stablecoin settlement $20B+ annualized
  url: https://www.visa.com/en-us/thought-leadership/innovation/financing-stablecoin-linked-card-programs
  date: '2026-09-08'
  quote: stablecoin settlement volume recently surpassed a $20 billion annualized run rate
```

### Signal 05 | 17/20
```yaml
format: kpi-trio
title: Tazapay brings $25B of payments into Circle deal
chapter: Market opportunity
why_it_matters: The proposed acquisition gives Circle access to a large working business payments platform. Stablecoins
  already touch most of Tazapay volume, and its local payout network spans more than 100 markets.
data:
- label: All-method annualized payment volume
  value: '>$25B'
  unit: annualized dollars
  date: 2026-07
- label: Volume that includes stablecoins
  value: ~60%
  unit: percent
  date: 2026-07
- label: Local payout coverage
  value: '>100'
  unit: markets
  date: 2026-07
note: We use Circle figures for Tazapay measured at July 31 and announced in September. The $25B includes fiat activity,
  so it is not the same as $25B of stablecoin-only payments.
fresh:
  period: month
  end: 2026-07
scores:
  surprise: 5
  importance: 5
  clarity: 4
  durability: 3
sources:
- claim: Tazapay >$25B all-method annualized volume
  url: https://investor.circle.com/news/news-details/2026/Circle-Expands-Global-Payments-Infrastructure-with-Agreement-to-Acquire-Singapore-Based-Cross-Border-Payments-Platform-Tazapay/default.aspx
  date: '2026-09-08'
  quote: Tazapay brings over $25 billion of annualized payment volume
- claim: Tazapay 60% includes stablecoins
  url: https://investor.circle.com/news/news-details/2026/Circle-Expands-Global-Payments-Infrastructure-with-Agreement-to-Acquire-Singapore-Based-Cross-Border-Payments-Platform-Tazapay/default.aspx
  date: '2026-09-08'
  quote: Approximately 60% of Tazapay's transaction volume already includes stablecoins
- claim: Tazapay >100 payout markets
  url: https://investor.circle.com/news/news-details/2026/Circle-Expands-Global-Payments-Infrastructure-with-Agreement-to-Acquire-Singapore-Based-Cross-Border-Payments-Platform-Tazapay/default.aspx
  date: '2026-09-08'
  quote: local payout rails covering over 100 markets
```

### Signal 06 | 17/20
```yaml
format: key-trend
title: Measured stablecoin payment counts jumped 71%
chapter: Market opportunity
why_it_matters: The number of identified payment transactions is rising far faster than supply. This is measured payment
  activity after removing routine blockchain movement and trading.
data:
- label: Prior comparable period (indexed)
  value: 100
  unit: payment count index
  date: 2025-09
- label: Jan to Sep 2026 (indexed)
  value: 171
  unit: payment count index
  date: 2026-09
note: We normalize Allium reported payment count growth of 71% in its September 2026 study to a prior-period index of
  100. The 171 value is our arithmetic, not a raw transaction count.
fresh:
  period: quarter
  end: 2026-09
scores:
  surprise: 4
  importance: 5
  clarity: 5
  durability: 3
sources:
- claim: Allium payments grew 71% by count through Q3
  url: https://app.allium.so/analyze/research/state-of-stablecoins-and-payments-q3-2026
  date: '2026-10-15'
  quote: payments grew 45% to $482B as payment count rose 71%
comment: Indexed comparison assumes the prior-period baseline implied by Allium is comparable to the September 2026 payment-count
  series.
```

### Signal 07 | 17/20
```yaml
format: icon-grid
title: Businesses receive at least 58% of stablecoin payments
chapter: Market opportunity
why_it_matters: This is no longer mainly about consumers sending money to friends. Businesses account for the majority
  of stablecoin payment receipts in the measured sample.
data:
- label: Business recipients (lower bound)
  value: 58
  unit: percent of payment value
  date: 2026-08
- label: All other recipients (upper bound)
  value: 42
  unit: percent of payment value
  date: 2026-08
note: We take the lower end of Allium estimated business receipt share for January through August 2026. The residual
  is a conservative upper bound for other recipients.
fresh:
  period: month
  end: 2026-08
scores:
  surprise: 4
  importance: 5
  clarity: 5
  durability: 3
sources:
- claim: Business recipients receive between 58% and 64%
  url: https://www.allium.so/reports/state-of-stablecoins-and-payments-september-2026
  date: '2026-09-15'
  quote: Businesses receive 58% to 64% of all payments
```

### Signal 08 | 17/20
```yaml
format: key-trend
title: Stablecoin cross-border payments rose from $82B to $135B
chapter: Market challenges
why_it_matters: Adoption is growing even in international transfers that have traditional alternatives. Yet stablecoins
  remain a small part of the entire cross-border payments business.
data:
- label: '2024'
  value: $82B
  unit: annual cross-border stablecoin payments
  date: 2024-12
- label: '2025'
  value: $135B
  unit: annual cross-border stablecoin payments
  date: 2025-12
note: We use the Allium and FXC Intelligence estimate of real retail cross-border payment volume in 2024 and 2025. We
  exclude raw exchange and treasury transfers and do not treat this older full-year series as a 2026 momentum signal.
fresh:
  period: total
  end: 2026-07
scores:
  surprise: 4
  importance: 5
  clarity: 5
  durability: 3
sources:
- claim: Retail cross-border payment stablecoin volume $82B 2024 and $135B 2025
  url: https://www.allium.so/reports/stablecoins-cross-border-payments-2026
  date: '2026-07-30'
  quote: Stablecoins accounted for an estimated $135bn of $44.3tn in 2025, 0.31%, against $82bn of $40.5tn in 2024.
```

### Signal 09 | 17/20
```yaml
format: dollar-split
title: Only 7 cents of each USDC revenue dollar became profit
chapter: Value creation
why_it_matters: The issuer spends most of its income sharing fees with partners and keeping the system running. Issuing
  digital dollars and supporting payment rails does not mean keeping all the interest earned.
data:
- label: Distribution and partners
  value: 59
  unit: cents per $1 revenue
  date: 2026-06
- label: Infrastructure and operations
  value: 34
  unit: cents per $1 revenue
  date: 2026-06
- label: Net profit
  value: 7
  unit: cents per $1 revenue
  date: 2026-06
note: We use Circle management breakdown for the first half of 2026, across its whole USDC business. It is not a price
  breakdown charged to payment customers and should not be presented as such.
fresh:
  period: half
  end: 2026-06
scores:
  surprise: 5
  importance: 4
  clarity: 5
  durability: 3
sources:
- claim: Circle distribution partners 59 cents
  url: https://www.circle.com/blog/the-economics-of-usdc-and-why-our-partners-win
  date: '2026-10-16'
  quote: Approximately 59 cents of every dollar of revenue went to the global partners
- claim: Circle infrastructure reinvestment 34 cents
  url: https://www.circle.com/blog/the-economics-of-usdc-and-why-our-partners-win
  date: '2026-10-16'
  quote: Circle spent about $473 million, roughly 34 cents of every dollar
- claim: Circle net profit 7 cents
  url: https://www.circle.com/blog/the-economics-of-usdc-and-why-our-partners-win
  date: '2026-10-16'
  quote: Circle made 7 cents of net profit from every dollar of revenue earned.
```

### Signal 10 | 17/20
```yaml
format: icon-grid
title: Most mapped stablecoin payments do not cross borders
chapter: Market challenges
why_it_matters: International payments get most of the publicity, but domestic use is larger in geographically identified
  activity. Stablecoins also compete with local payment systems, not only international wires.
data:
- label: Domestic
  value: 61
  unit: percent of geolocated payment value
  date: 2026-08
- label: Cross-border
  value: 39
  unit: percent of geolocated payment value
  date: 2026-08
note: We use Allium geolocated payment flows for January through August 2026. The 39% cross-border share is the arithmetic
  complement of its 61% domestic rate.
fresh:
  period: month
  end: 2026-08
scores:
  surprise: 4
  importance: 4
  clarity: 5
  durability: 4
sources:
- claim: Geolocated stablecoin payment flows 61% domestic
  url: https://www.allium.so/reports/state-of-stablecoins-and-payments-september-2026
  date: '2026-09-15'
  quote: 61% of geographically attributed payment volume was domestic
```

### Signal 11 | 17/20
```yaml
format: icon-grid
title: Business cards make up 17% of Visa stablecoin card spend
chapter: Growth drivers
why_it_matters: Stablecoin cards increasingly serve company spending, not only consumer purchases. Business use already
  makes up a meaningful share of the growing Visa program network.
data:
- label: Business and commercial
  value: 17
  unit: percent of card payment value
  date: 2026-09
- label: Consumer and other
  value: 83
  unit: percent of card payment value
  date: 2026-09
note: We use Visa data for its fiscal 2026 year-to-date stablecoin-linked card volume, disclosed October 2026. The 83%
  residual is calculated, not directly stated by Visa.
fresh:
  period: month
  end: 2026-09
scores:
  surprise: 4
  importance: 4
  clarity: 5
  durability: 4
sources:
- claim: 17% of Visa card payment value in business and commercial programs
  url: https://corporate.visa.com/en/sites/visa-perspectives/newsroom/stablecoins-gain-traction-business-payments.html
  date: '2026-10-01'
  quote: Approximately 17% of stablecoin-linked card volume in FY26 year-to-date occurred across business and commercial
    card programs.
```

### Signal 12 | 16/20
```yaml
format: kpi-trio
title: AI agents made 29M tiny stablecoin payments in a month
chapter: Market opportunity
why_it_matters: Machine-to-machine purchasing is emerging as a real payment use case. Most x402 transfers bought small
  infrastructure and data services rather than being speculative transfers.
data:
- label: August x402 transfers
  value: 29000000
  unit: payments
  date: 2026-08
- label: Average payment
  value: $0.06
  unit: dollars per payment
  date: 2026-08
- label: Share buying data and infrastructure
  value: 89
  unit: percent since Oct 2025
  date: 2026-08
note: We use Allium classification of payments made on the x402 protocol in August 2026, with purchase-purpose share
  measured since October 2025. These microtransactions are distinct from trading volume.
fresh:
  period: month
  end: 2026-08
scores:
  surprise: 5
  importance: 4
  clarity: 4
  durability: 3
sources:
- claim: x402 August count and mean payment
  url: https://www.allium.so/reports/state-of-stablecoins-and-payments-september-2026
  date: '2026-09-15'
  quote: Agentic payments on the x402 protocol reached 29 million monthly transfers in August 2026, averaging 6 cents
    per payment.
- claim: x402 since October 2025 infrastructure payments share
  url: https://www.allium.so/reports/state-of-stablecoins-and-payments-september-2026
  date: '2026-09-15'
  quote: Since October 2025, 89% of agentic transfers purchased infrastructure, analytics, and data queries.
```

### Signal 13 | 16/20
```yaml
format: icon-grid
title: Cross-border accounts for 43% of mapped business transfers
chapter: Market challenges
why_it_matters: Even among company-to-company stablecoin payments, most mapped activity stays within countries. Stablecoin
  payment startups still need a domestic value proposition.
data:
- label: Cross-border B2B
  value: 43
  unit: percent of geolocated B2B payments
  date: 2026-08
- label: Domestic B2B
  value: 57
  unit: percent of geolocated B2B payments
  date: 2026-08
note: We use Allium geographic classification of business-to-business payments from January through August 2026. The
  reported cross-border share is 43%, with the domestic residual calculated.
fresh:
  period: month
  end: 2026-08
scores:
  surprise: 3
  importance: 4
  clarity: 5
  durability: 4
sources:
- claim: B2B payments 43% cross-border
  url: https://www.allium.so/reports/state-of-stablecoins-and-payments-september-2026
  date: '2026-09-15'
  quote: business-to-business transfers showed the highest cross-border share at 43%
```

