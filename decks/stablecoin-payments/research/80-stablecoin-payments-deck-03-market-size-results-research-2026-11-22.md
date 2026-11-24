### ed041
```yaml
status: ok
section: Market size
title: What counts as stablecoin payments, and what doesn’t?
note: We count stablecoin movement tied to a payment service, not the full volume transferred between blockchain wallets.
t:
  7: We count services that move, settle, convert, or spend stablecoins for customers, including cross-border payments, cards, checkout, and payouts
  8: We include stablecoin payment rails, merchant checkout, global transfers, card spending, payroll, treasury settlement, and payment APIs
  9: We exclude crypto trading, passive token issuance, investment wallets, and fiat-only transfers with no core stablecoin payment service
sources:
- claim: mck
  url: https://www.mckinsey.com/industries/financial-services/our-insights/stablecoins-in-payments-what-the-raw-transaction-numbers-miss
  date: '2026-02-18'
  quote: The true volume of stablecoin payments identified in our analysis, about $390 billion in 2025, has more than doubled from 2024 levels.
- claim: bridge
  url: https://bridge.xyz/product/orchestration
  date: '2026-11-22'
  quote: A single API enables you to move USDC, USDT, your own stablecoin, and more across 10+ blockchains.
- claim: circle26
  url: https://www.circle.com/pressroom/circle-launches-cpn-managed-payments-a-full-stack-platform-for-seamless-stablecoin-settlement
  date: '2026-04-08'
  quote: CPN Managed Payments abstracts digital asset complexity, enabling partners to interact solely in fiat while Circle manages the entire digital asset lifecycle
```

### ed042
```yaml
status: ok
section: Market size
title: What are the market size estimates from different sources online?
rows:
- firm: Allium
  value: $394B
  comment: Its 2025 measure labels payments by wallet and counterparty type, with exchange flows removed. We use it as the comparable full-year base.
- firm: McKinsey / Artemis
  value: $390B
  comment: Their December 2025 payment pace is annualized, not the sum of that year. It separates real payments from internal wallet transfers.
- firm: Stripe
  value: $400B
  comment: Stripe cites roughly $400 billion of 2025 stablecoin payment volume. Its rounded figure checks our baseline, not issuer revenue.
- firm: BCG / Allium
  value: $350-550B
  comment: Their 2025 range captures observed bilateral payments, with some off-chain and card activity missing. We use it as a method check.
note:
- We compare payment flow estimates, not token supply, trading transfers or fees earned by service providers.
- We treat annual totals, December run rates and ranges as distinct measures before selecting a baseline.
sources:
- claim: allium25
  url: https://www.allium.so/reports/stablecoin-payments-q1-2026
  date: '2026-01-31'
  quote: Labeled stablecoin payment volume grew 39% in 2025 to $393.5 billion across 540.7 million transactions.
- claim: mck
  url: https://www.mckinsey.com/industries/financial-services/our-insights/stablecoins-in-payments-what-the-raw-transaction-numbers-miss
  date: '2026-02-18'
  quote: The true volume of stablecoin payments identified in our analysis, about $390 billion in 2025, has more than doubled from 2024 levels.
- claim: stripe400
  url: https://stripe.com/en-sg/newsroom/news/stripe-2025-update
  date: '2026-02-24'
  quote: stablecoin payments volume doubled to around $400 billion
- claim: bcg
  url: https://bcg.allium.so/
  date: undated
  quote: and real-economy payments ($350-550B).
- claim: bcgmethod
  url: https://www.allium.so/reports/stablecoin-payments-the-truth-behind-the-numbers
  date: '2025-12-31'
  quote: We exclude large categories of offchain usage, including internal exchange settlements and stablecoin card-based payments.
```

### ed043
```yaml
status: ok
section: Market size
title: Our own first-principles, bottom-up calculation of the market size
page: 1/2
note: We use labeled end-user payments as the unit of market size and keep volumes distinct from payment-provider revenue.
t:
  21: We start with labeled customer payments, not raw blockchain transfers
  16: We use Allium payment labels, checked against McKinsey and Stripe data
  15: We count business transfers, consumer pay, cards, payroll, and payouts
  14: We leave out exchange trading, internal wallet shuffles, and token supply
  9: We do not add network settlements twice when they reuse the same payment money
  8: We use Allium’s nine reported months through September 2026
  7: We take Allium’s $394B full-year 2025 payment total as the prior base
  6: We check Stripe’s roughly $400B for the same year
  3: We check McKinsey and Artemis at about $390B annualized in late 2025
  2: We keep BCG’s $350B to $550B estimate as a wider method cross-check
  0: We then use the $482B of payments identified by Allium in 2026
sources:
- claim: allium25
  url: https://www.allium.so/reports/stablecoin-payments-q1-2026
  date: '2026-01-31'
  quote: Labeled stablecoin payment volume grew 39% in 2025 to $393.5 billion across 540.7 million transactions.
- claim: allium26
  url: https://app.allium.so/analyze/research/state-of-stablecoins-and-payments-q3-2026
  date: '2026-10-15'
  quote: Supply grew 0.4% this year to $305B, while payments grew 45% to $482B as payment count rose 71% and the average payment fell.
- claim: mck
  url: https://www.mckinsey.com/industries/financial-services/our-insights/stablecoins-in-payments-what-the-raw-transaction-numbers-miss
  date: '2026-02-18'
  quote: The true volume of stablecoin payments identified in our analysis, about $390 billion in 2025, has more than doubled from 2024 levels.
- claim: stripe400
  url: https://stripe.com/en-sg/newsroom/news/stripe-2025-update
  date: '2026-02-24'
  quote: stablecoin payments volume doubled to around $400 billion
- claim: bcg
  url: https://bcg.allium.so/
  date: undated
  quote: and real-economy payments ($350-550B).
```

### ed044
```yaml
status: ok
section: Market size
title: Our own first-principles, bottom-up calculation of the market size
page: 2/2
note: We annualize Allium’s January to September 2026 payment volume. Future months may differ from this nine-month average.
t:
  21: We start with $482B of payments reported through September 2026
  16: We use the same monthly payment average over nine reported months
  15: We divide $482B by nine and multiply it by twelve
  14: We get about $643B in yearly payment flow at that pace
  9: We know Q4 can differ, so this is a run rate and not a closed-year total
  8: We compare that run rate with Allium’s $394B in 2025
  7: We see Allium reporting 45% payment growth year on year in 2026
  6: We do not add cards or cross-border payments twice if already included
  3: We use $643B as a simple annualized 2026 market proxy
  2: We label this as yearly payment flow, not the fees earned from it
  0: We conclude the 2026 payment-flow pace is about $643B a year
sources:
- claim: allium26
  url: https://app.allium.so/analyze/research/state-of-stablecoins-and-payments-q3-2026
  date: '2026-10-15'
  quote: Supply grew 0.4% this year to $305B, while payments grew 45% to $482B as payment count rose 71% and the average payment fell.
- claim: allium25
  url: https://www.allium.so/reports/stablecoin-payments-q1-2026
  date: '2026-01-31'
  quote: Labeled stablecoin payment volume grew 39% in 2025 to $393.5 billion across 540.7 million transactions.
- claim: fxc
  url: https://www.allium.so/reports/stablecoins-cross-border-payments-2026
  date: '2026-07-30'
  quote: Stablecoins moved $135bn of the $44.3tn retail cross-border payments market in 2025
- claim: visa2025card
  url: https://www.visa.com/en-us/thought-leadership/innovation/stablecoin-linked-cards-monetize-money-movement
  date: '2026-03-31'
  quote: In 2025 alone, these cards processed approximately ~$5.2 billion in volume, a 319% year-over-year increase.
```

### ed045
```yaml
status: ok
section: Market size
title: How much are stablecoin payments worth today?
t:
  6: $643B
  8: We estimate an annualized payment flow of $643 billion in 2026 from Allium’s $482 billion through September. That is money sent for payments, not industry revenue. The final 2026 total remains open.
  4: '2026'
note: We divide nine months of Allium’s identified 2026 payments by nine and multiply by twelve to estimate an annual pace.
comment: This is annualized 2026 payment throughput, not stablecoin supply, total on-chain volume, or provider revenue.
sources:
- claim: allium26
  url: https://app.allium.so/analyze/research/state-of-stablecoins-and-payments-q3-2026
  date: '2026-10-15'
  quote: Supply grew 0.4% this year to $305B, while payments grew 45% to $482B as payment count rose 71% and the average payment fell.
```

### ed048
```yaml
status: ok
section: Market size
title: What is behind these categories?
t:
  5: CROSS-BORDER
  8: MERCHANT PAY
  10: CARDS AND PAYOUTS
  11: 🌍
  4: Business transfers and remittances use stablecoins to settle value, then deliver dollars or local currency to recipients
  12: 💳
  7: Checkout tools let buyers pay stablecoins while sellers receive tokens or a converted balance in local currency
  9: Cards make stablecoins spendable at shops, while payment APIs send wages, creator earnings, and supplier payouts
  15: ''
  17: ''
  18: ''
  19: ''
  14: ''
  16: ''
holes_ok: true
note: We group payment uses by what end customers do. Each route needs a working send, receive, spend, or payout function.
sources:
- claim: fxc
  url: https://www.allium.so/reports/stablecoins-cross-border-payments-2026
  date: '2026-07-30'
  quote: Stablecoins moved $135bn of the $44.3tn retail cross-border payments market in 2025
- claim: mastercard25
  url: https://investor.mastercard.com/investor-news/investor-news-details/2025/Mastercard-Unveils-End-to-End-Capabilities-to-Power-Stablecoin-Transactions--From-Wallets-to-Checkouts/default.aspx
  date: '2025-04-28'
  quote: Mastercard is teaming up with Nuvei and Circle to give merchants the option to receive their payments in stablecoins
- claim: visa2025card
  url: https://www.visa.com/en-us/thought-leadership/innovation/stablecoin-linked-cards-monetize-money-movement
  date: '2026-03-31'
  quote: In 2025 alone, these cards processed approximately ~$5.2 billion in volume, a 319% year-over-year increase.
- claim: toku
  url: https://www.toku.com/stablecoin-payroll/usdt
  date: '2026-11-12'
  quote: Toku runs payroll and pays employees and contractors in USDT on Ethereum, Polygon, Base, Avalanche, Tron, BNB Chain
```

### ed049
```yaml
status: ok
section: Market size
title: Where in the world are stablecoin payments made?
regions:
  na:
    pct: 24
    text: North America originates about $95B of annual payment flow in the McKinsey and Artemis study, roughly one-quarter of its total.
  eu:
    pct: 13
    text: Europe originates about $50B of yearly payments, less than North America and Asia in the McKinsey and Artemis study.
  apac:
    pct: 63
    text: Asia leads identified origin volume at about $245B, driven largely by Singapore, Hong Kong, and Japan.
  latam:
    pct: 0
    text: Latin America is below $1B in this study, rounding to 0% at whole-percent precision. That reflects measurement scope, not no use.
  mea:
    pct: 0
    text: Africa is also below $1B and rounds to 0%. The report groups its flows separately, but cannot support a precise regional split.
note:
- We use the payment-origin estimates from McKinsey and Artemis, not wallet holdings or raw exchange flows.
- We round to whole shares. Regions below $1B round to zero and may be undercounted by payment labels.
sources:
- claim: mckregion
  url: https://www.mckinsey.com/industries/financial-services/our-insights/stablecoins-in-payments-what-the-raw-transaction-numbers-miss
  date: '2026-02-18'
  quote: Stablecoin payments sent from Asia represent the largest source of volume, accounting for about $245 billion in payments, or 60 percent of the total.
- claim: mckregion2
  url: https://www.mckinsey.com/industries/financial-services/our-insights/stablecoins-in-payments-what-the-raw-transaction-numbers-miss
  date: '2026-02-18'
  quote: North America is next, accounting for $95 billion, followed by Europe at $50 billion.
- claim: mckregion3
  url: https://www.mckinsey.com/industries/financial-services/our-insights/stablecoins-in-payments-what-the-raw-transaction-numbers-miss
  date: '2026-02-18'
  quote: Latin America and Africa each accounts for less than $1 billion.
```

### ed050
```yaml
status: ok
section: Market size
title: What are the growth rate estimates from different sources online?
note: We compare observed payment-volume growth. None of these firms publishes a directly comparable ten-year market forecast.
t:
  24: FIRM
  25: GROWTH
  26: COMMENTS
  6: Allium
  5: "45%\\n2026 YTD"
  7: Allium finds payment volume rose 45% year on year through September 2026. We use this as the latest broad growth signal.
  10: Stripe
  9: "~100%\\nin 2025"
  11: Stripe says stablecoin payments roughly doubled in 2025. It is a directional cross-check, not a separate forecast.
  14: FXC / Allium
  13: "64%\\nin 2025"
  15: Their measured cross-border stablecoin payment flow rose 64% in 2025. That is a narrower use case, not total-market growth.
  18: Allium Q1
  17: "39%\\nin 2025"
  19: Allium finds labeled stablecoin payment volume rose 39% in 2025. The slower full-year rate supports a base case below the newest pace.
sources:
- claim: allium26
  url: https://app.allium.so/analyze/research/state-of-stablecoins-and-payments-q3-2026
  date: '2026-10-15'
  quote: Supply grew 0.4% this year to $305B, while payments grew 45% to $482B as payment count rose 71% and the average payment fell.
- claim: stripe400
  url: https://stripe.com/en-sg/newsroom/news/stripe-2025-update
  date: '2026-02-24'
  quote: stablecoin payments volume doubled to around $400 billion
- claim: fxcgrowth
  url: https://www.allium.so/reports/stablecoins-cross-border-payments-2026
  date: '2026-07-30'
  quote: Stablecoin cross-border volume grew 64% year on year against 9% for fiat.
- claim: allium25
  url: https://www.allium.so/reports/stablecoin-payments-q1-2026
  date: '2026-01-31'
  quote: Labeled stablecoin payment volume grew 39% in 2025 to $393.5 billion across 540.7 million transactions.
```

### ed051
```yaml
status: ok
section: Market size
title: What is a realistic CAGR for the stablecoin payments market?
note: We set a 30% analyst base-case growth scenario, with 15% and 45% bounds. These are not published consensus forecasts.
t:
  15: BEST CASE ~ 45%
  17: "~30%\\nthrough 2036"
  19: Labeled payments grew 39% in 2025 and 45% through September 2026. We use a slower 30% long-run scenario as wider use meets banking, compliance, and payout limits.
  16: WORST CASE ~ 15%
comment: Scenario rates are our assumptions, not third-party forecasts.
sources:
- claim: allium25
  url: https://www.allium.so/reports/stablecoin-payments-q1-2026
  date: '2026-01-31'
  quote: Labeled stablecoin payment volume grew 39% in 2025 to $393.5 billion across 540.7 million transactions.
- claim: allium26
  url: https://app.allium.so/analyze/research/state-of-stablecoins-and-payments-q3-2026
  date: '2026-10-15'
  quote: Supply grew 0.4% this year to $305B, while payments grew 45% to $482B as payment count rose 71% and the average payment fell.
- claim: fxcgrowth
  url: https://www.allium.so/reports/stablecoins-cross-border-payments-2026
  date: '2026-07-30'
  quote: Stablecoin cross-border volume grew 64% year on year against 9% for fiat.
```

### ed052p
```yaml
status: ok
section: Market size
title: How much bigger can stablecoin payments get?
size: 0.643
cagr: 30
y0: 2026
lead: 'To get that big, '
condition: merchant checkout and business payouts must move beyond early adopters, while bank access, local cash-out routes, reliable card funding, and clear rules expand with real customer demand.
note:
- We apply a 30% scenario CAGR to the $643B annualized payment-flow proxy, reaching about $8.9T by 2036.
- We do not treat total wallet transfers or token supply as payments. The path depends on broader actual use.
comment: The projection is our analyst scenario based on a nine-month annualization, not a cited independent forecast.
sources:
- claim: allium26
  url: https://app.allium.so/analyze/research/state-of-stablecoins-and-payments-q3-2026
  date: '2026-10-15'
  quote: Supply grew 0.4% this year to $305B, while payments grew 45% to $482B as payment count rose 71% and the average payment fell.
- claim: allium25
  url: https://www.allium.so/reports/stablecoin-payments-q1-2026
  date: '2026-01-31'
  quote: Labeled stablecoin payment volume grew 39% in 2025 to $393.5 billion across 540.7 million transactions.
- claim: circle26
  url: https://www.circle.com/pressroom/circle-launches-cpn-managed-payments-a-full-stack-platform-for-seamless-stablecoin-settlement
  date: '2026-04-08'
  quote: CPN Managed Payments abstracts digital asset complexity, enabling partners to interact solely in fiat while Circle manages the entire digital asset lifecycle
- claim: fxc
  url: https://www.allium.so/reports/stablecoins-cross-border-payments-2026
  date: '2026-07-30'
  quote: Stablecoins moved $135bn of the $44.3tn retail cross-border payments market in 2025
```

