### ed132
```yaml
status: ok
section: Market challenges
title: What do newcomers often miss here?
t:
  '17': Fast transfers on a blockchain still need banks to get dollars in and out locally
  '25': A digital dollar can lose its peg if reserve banks fail, as USDC showed in 2023
  '28': Low network fees can hide costly local exchange, conversion and withdrawal steps
  '21': On-chain transfer totals are not sales. McKinsey counts only actual payments
  '23': Payment firms face money transfer rules even when no bank handles the coin
note: We drew on payment-flow analysis, banking disruptions, and licensing rules. Speed on a chain does not remove the steps needed to deliver spendable money.
sources:
- claim: BIS finds bank cash-out can delay recipient access
  url: https://www.bis.org/publications/working-paper-1385-competing-rails-crossborder-payments-banks-fintechs-and-stablecoins
  date: '2026-10-19'
  quote: Recipients may also have to wait for stablecoin conversion and bank processing before they can access the funds in their bank accounts.
- claim: BIS finds conversion and withdrawal costs complicate stablecoin payments
  url: https://www.bis.org/publications/working-paper-1385-competing-rails-crossborder-payments-banks-fintechs-and-stablecoins
  date: '2026-10-19'
  quote: These conversions still rely on crypto exchanges and other intermediaries, whose trading, conversion and withdrawal fees can substantially increase the total cost.
- claim: Circle disclosed $3.3B of USDC reserves at failed SVB
  url: https://www.circle.com/pressroom/3-3-billion-of-usdc-reserve-risk-removed-dollar-de-peg-closes
  date: '2023-03-13'
  quote: The $3.3B USDC reserve deposit held at Silicon Valley Bank, about 8% of the USDC total reserve
- claim: Most blockchain stablecoin volumes are not end-user payments
  url: https://www.mckinsey.com/industries/financial-services/our-insights/stablecoins-in-payments-what-the-raw-transaction-numbers-miss
  date: '2026-02-18'
  quote: most of this activity doesn’t represent true end-user payments, such as paying suppliers or sending remittances.
- claim: FinCEN treats certain custodial crypto transmitters as money services businesses
  url: https://www.fincen.gov/resources/statutes-regulations/guidance/application-fincens-regulations-persons-administering
  date: '2013-03-18'
  quote: an administrator or exchanger is an MSB under FinCEN’s regulations, specifically, a money transmitter
```

### ed133
```yaml
status: ok
section: Market challenges
title: What has held back market growth so far?
t:
  '6': '2017 - 2020


    Stablecoins first spread as digital dollars in crypto markets. Few payment firms connected them to local bank accounts.'
  '7': '2021 - 2023


    Visa tested USDC settlement with partners, but Circle''s 2023 bank exposure showed how fragile dollar access could be.'
  '8': '2024 - 2025


    New EU and US rules clarified issuer obligations. Stripe and Circle added payment products, but converting coins to local money remained hard.'
  '10': '2025 - 2026


    Business payments and cards grew quickly, yet cash-out costs and license checks still held back wider use.'
  '9': 'TODAY


    Real payment volume is rising, but thin local liquidity and mixed national rules keep expansion uneven.'
note: We separated the main phases using payment launches, banking events, regulatory changes, and measured use. The phase dates are approximate.
sources:
- claim: Visa ran real stablecoin settlements with acquirers in 2023
  url: https://investor.visa.com/news/news-details/2023/Visa-Expands-Stablecoin-Settlement-Capabilities-to-Merchant-Acquirers/
  date: '2023-09-05'
  quote: Through live pilots with issuers and acquirers, Visa has already moved millions of USDC between its partners
- claim: Circle disclosed $3.3B of USDC reserves at failed SVB
  url: https://www.circle.com/pressroom/3-3-billion-of-usdc-reserve-risk-removed-dollar-de-peg-closes
  date: '2023-03-13'
  quote: The $3.3B USDC reserve deposit held at Silicon Valley Bank, about 8% of the USDC total reserve
- claim: GENIUS Act became US law July 18, 2025
  url: https://occ.treas.gov/topics/charters-and-licensing/genius-act/index-genius-act.html
  date: '2025-07-18'
  quote: signed the Guiding and Establishing National Innovation for U.S. Stablecoins (GENIUS) Act into law on July 18, 2025
- claim: MiCA contains transition until July 1, 2026 for qualifying providers
  url: https://www.esma.europa.eu/publications-and-data/interactive-single-rulebook/mica/article-143-transitional-measures
  date: '2024-12-30'
  quote: may continue to do so until 1 July 2026 or until they are granted or refused an authorisation
- claim: Stripe added USDC merchant acceptance for Shopify in 34 countries
  url: https://stripe.com/newsroom/news/shopify-stripe-stablecoin-payments
  date: '2025-06-12'
  quote: Shopify merchants across 34 countries will be able to accept USDC, a dollar-backed stablecoin.
- claim: Measured stablecoin payments more than doubled from 2024 to 2025
  url: https://www.mckinsey.com/industries/financial-services/our-insights/stablecoins-in-payments-what-the-raw-transaction-numbers-miss
  date: '2026-02-18'
  quote: The true volume of stablecoin payments identified in our analysis, about $390 billion in 2025, has more than doubled from 2024 levels.
- claim: BIS highlights thin local-currency liquidity
  url: https://www.bis.org/publications/working-paper-1385-competing-rails-crossborder-payments-banks-fintechs-and-stablecoins
  date: '2026-10-19'
  quote: Moreover, liquidity between US dollar stablecoins and non-US currencies is generally very thin.
```

### ed134
```yaml
status: ok
section: Market challenges
title: And more recently?
t:
  '12': 2025 (JUN)
  '13': EU officials flagged overlapping licenses for stablecoin payments under MiCA and PSD2 {1|EBA}
  '14': 2025 (JUL)
  '15': The US passed the GENIUS Act, setting federal reserve rules for payment coin issuers {1|OCC}
  '16': 2025 (DEC)
  '17': Visa began USDC settlement with Cross River Bank and Lead Bank, showing that regulated banks can settle onchain {1|Visa}
  '18': 2026 (MAR)
  '19': Visa and Bridge said stablecoin-linked cards were live in 18 countries, with further expansion planned {1|Visa}
  '20': 2026 (AUG)
  '21': Mastercard bought stablecoin payment firm BVNK, raising competition for new payment firms {1|Mastercard}
  '22': 2026 (OCT)
  '23': EU supervisors urged licensed providers to stop serving clients with stablecoins that fail to meet MiCA rules {1|ESMA}
sources:
- claim: EBA highlighted double-authorization problem for payments using euro stablecoins
  url: https://www.eba.europa.eu/publications-and-media/press-releases/eba-publishes-no-action-letter-interplay-between-payment-services-directive-psd23-and-markets-crypto
  date: '2025-06-10'
  quote: EU law needs to avoid a dual authorisation under two pieces of EU law for the activity of transacting electronic money tokens
- claim: GENIUS Act became US law July 18, 2025
  url: https://occ.treas.gov/topics/charters-and-licensing/genius-act/index-genius-act.html
  date: '2025-07-18'
  quote: signed the Guiding and Establishing National Innovation for U.S. Stablecoins (GENIUS) Act into law on July 18, 2025
- claim: GENIUS Act will require dollar-for-dollar permitted reserves for issuers
  url: https://www.everycrsreport.com/reports/IN12553.html
  date: '2026-08-20'
  quote: Issuers are required to hold at least one dollar of permitted reserves for every one dollar of stablecoins issued.
- claim: Visa began US bank settlement in USDC
  url: https://corporate.visa.com/en/sites/visa-perspectives/press-releases/visa-launches-stablecoin-settlement-in-the-united-states.html
  date: '2025-12-16'
  quote: Initial banking participants include Cross River Bank and Lead Bank, which have started settling with Visa in USDC over the Solana blockchain.
- claim: Bridge Visa stablecoin cards were live in 18 countries by March 2026
  url: https://corporate.visa.com/en/sites/visa-perspectives/press-releases/visa-bridge-stablecoin-linked-card-expansion.html
  date: '2026-03-03'
  quote: Bridge-enabled stablecoin-linked cards are now live in 18 countries, with planned expansion to over 100 countries
- claim: Mastercard completed acquisition of BVNK in August 2026
  url: https://www.mastercard.com/global/en/news-and-trends/press/2026/august/mastercard-completes-acquisition-of-bvnk-to-advance-global-stabl.html
  date: '2026-08-03'
  quote: 'Mastercard (NYSE: MA) today completed its acquisition of BVNK'
- claim: ESMA advises ending EU services for non-MiCA-compliant stablecoins
  url: https://www.esma.europa.eu/press-news/esma-news/esma-sets-out-supervisory-expectations-services-related-unauthorised
  date: '2026-10-08'
  quote: Crypto-asset service providers (CASPs) authorised under MiCA should cease providing services related to non-MiCA-compliant stablecoins to clients in the European Union.
```

### ed136
```yaml
status: ok
section: Market challenges
title: What slows stablecoin payment adoption down?
t:
  '6': '🏦


    Bank partners still control the dollar entry and exit points'
  '7': '⚖️


    Payment licenses differ by country and service'
  '8': '💵


    Local currency exchange can erase fee savings'
  '9': '🔐


    Fraud and sanctions screening cannot be skipped'
  '10': '🛒


    Merchants want familiar pricing, refunds and bank payouts'
  '11': '🔗


    Different coins and networks make transfers harder to route'
  '12': '💳


    Card programs need sponsor banks and network approval'
  '13': '📊


    Most reported coin transfers are not real payments'
note: We compared the main obstacles described by payment networks, regulators, and transaction researchers. Many arise at the points where coins meet ordinary money.
sources:
- claim: BIS finds conversion and withdrawal costs complicate stablecoin payments
  url: https://www.bis.org/publications/working-paper-1385-competing-rails-crossborder-payments-banks-fintechs-and-stablecoins
  date: '2026-10-19'
  quote: These conversions still rely on crypto exchanges and other intermediaries, whose trading, conversion and withdrawal fees can substantially increase the total cost.
- claim: BIS highlights thin local-currency liquidity
  url: https://www.bis.org/publications/working-paper-1385-competing-rails-crossborder-payments-banks-fintechs-and-stablecoins
  date: '2026-10-19'
  quote: Moreover, liquidity between US dollar stablecoins and non-US currencies is generally very thin.
- claim: FinCEN treats certain custodial crypto transmitters as money services businesses
  url: https://www.fincen.gov/resources/statutes-regulations/guidance/application-fincens-regulations-persons-administering
  date: '2013-03-18'
  quote: an administrator or exchanger is an MSB under FinCEN’s regulations, specifically, a money transmitter
- claim: EBA highlighted double-authorization problem for payments using euro stablecoins
  url: https://www.eba.europa.eu/publications-and-media/press-releases/eba-publishes-no-action-letter-interplay-between-payment-services-directive-psd23-and-markets-crypto
  date: '2025-06-10'
  quote: EU law needs to avoid a dual authorisation under two pieces of EU law for the activity of transacting electronic money tokens
- claim: Bridge Visa stablecoin cards were live in 18 countries by March 2026
  url: https://corporate.visa.com/en/sites/visa-perspectives/press-releases/visa-bridge-stablecoin-linked-card-expansion.html
  date: '2026-03-03'
  quote: Bridge-enabled stablecoin-linked cards are now live in 18 countries, with planned expansion to over 100 countries
- claim: Most blockchain stablecoin volumes are not end-user payments
  url: https://www.mckinsey.com/industries/financial-services/our-insights/stablecoins-in-payments-what-the-raw-transaction-numbers-miss
  date: '2026-02-18'
  quote: most of this activity doesn’t represent true end-user payments, such as paying suppliers or sending remittances.
- claim: Stripe added USDC merchant acceptance for Shopify in 34 countries
  url: https://stripe.com/newsroom/news/shopify-stripe-stablecoin-payments
  date: '2025-06-12'
  quote: Shopify merchants across 34 countries will be able to accept USDC, a dollar-backed stablecoin.
```

### ed138
```yaml
status: ok
section: Market challenges
title: How is regulation evolving?
t:
  '7': '2017 - 2023


    US money transfer rules covered many coin firms, while issuers faced uneven oversight.'
  '8': '2024 - 2025


    EU MiCA set rules, and the US GENIUS Act outlined future reserve duties for coin issuers.'
  '9': '2026


    EU providers faced a MiCA cutoff and new limits on unapproved coins used for payments.'
  '10': 'TODAY


    A payment firm must still meet local money transfer, anti-crime and banking partner requirements.'
  '11': '?


    US and Asian rules may evolve. Issuer permission alone cannot approve every payment app.'
note: We used EU supervisory guidance, US law and financial crime rules, plus recent Asian regulatory actions. Issuer permission and payment service permission remain distinct.
sources:
- claim: FinCEN treats certain custodial crypto transmitters as money services businesses
  url: https://www.fincen.gov/resources/statutes-regulations/guidance/application-fincens-regulations-persons-administering
  date: '2013-03-18'
  quote: an administrator or exchanger is an MSB under FinCEN’s regulations, specifically, a money transmitter
- claim: MiCA contains transition until July 1, 2026 for qualifying providers
  url: https://www.esma.europa.eu/publications-and-data/interactive-single-rulebook/mica/article-143-transitional-measures
  date: '2024-12-30'
  quote: may continue to do so until 1 July 2026 or until they are granted or refused an authorisation
- claim: GENIUS Act became US law July 18, 2025
  url: https://occ.treas.gov/topics/charters-and-licensing/genius-act/index-genius-act.html
  date: '2025-07-18'
  quote: signed the Guiding and Establishing National Innovation for U.S. Stablecoins (GENIUS) Act into law on July 18, 2025
- claim: GENIUS Act will require dollar-for-dollar permitted reserves for issuers
  url: https://www.everycrsreport.com/reports/IN12553.html
  date: '2026-08-20'
  quote: Issuers are required to hold at least one dollar of permitted reserves for every one dollar of stablecoins issued.
- claim: OCC final GENIUS Act issuer rule takes effect January 18, 2027
  url: https://occ.gov/news-issuances/bulletins/2026/bulletin-2026-50.html
  date: '2026-10-21'
  quote: The final rule will be effective on January 18, 2027.
- claim: ESMA advises ending EU services for non-MiCA-compliant stablecoins
  url: https://www.esma.europa.eu/press-news/esma-news/esma-sets-out-supervisory-expectations-services-related-unauthorised
  date: '2026-10-08'
  quote: Crypto-asset service providers (CASPs) authorised under MiCA should cease providing services related to non-MiCA-compliant stablecoins to clients in the European Union.
- claim: EBA updated treatment of euro stablecoin payment services in 2026
  url: https://www.eba.europa.eu/publications-and-media/press-releases/eba-advises-national-authorities-actions-take-end-transition-period-under-its-no-action-letter
  date: '2026-02-12'
  quote: The transition period allows crypto asset service providers (CASPs) nine months to continue transacting electronic money tokens that qualify as payment services
- claim: HKMA granted first two stablecoin issuance licenses in April 2026
  url: https://www.hkma.gov.hk/eng/news-and-media/insight/2026/04/20260410/
  date: '2026-04-10'
  quote: The HKMA announced today the granting of stablecoin issuer licences to two entities by the Monetary Authority under the Stablecoins Ordinance
- claim: Singapore MAS proposed 2026 stablecoin licensing amendments
  url: https://www.mas.gov.sg/publications/consultations/2026/consultation-on-proposed-amendments-to-the-payment-services-act-for-stablecoin-regulation
  date: '2026-09-01'
  quote: This paper sets out proposed legislative amendments to the Payment Services Act 2019 to introduce the regulatory framework for stablecoins in Singapore
```

### iv_fda
```yaml
status: ok
section: Market challenges
title: What does it take to launch a stablecoin payment service?
comment: Planning times are illustrative estimates, not published industry averages. GENIUS governs issuers, not a universal payment-service license.
t:
  '7': 'LICENSE & SCOPE


    Regulators decide which licenses apply. Plan months. EU MiCA and US state rules both matter.'
  '8': 'BANK & CASH OUT


    Banks approve dollar deposits and withdrawals. Plan weeks or months to agree on local money routes.'
  '9': 'COIN & RESERVES


    Choose a permitted issuer and test redemption. Plan weeks. GENIUS reserve rules begin later.'
  '11': 'CHECKS & CONTROLS


    Your team must screen customers and transfers for fraud and sanctions on each route.'
  '10': 'CARDS & PAYOUTS


    Card networks or payout partners approve routes. Pilot for months before scaling.'
note: We mapped five practical approval and integration steps from regulatory and provider materials. Time windows are indicative planning estimates, not mandated deadlines.
sources:
- claim: FinCEN treats certain custodial crypto transmitters as money services businesses
  url: https://www.fincen.gov/resources/statutes-regulations/guidance/application-fincens-regulations-persons-administering
  date: '2013-03-18'
  quote: an administrator or exchanger is an MSB under FinCEN’s regulations, specifically, a money transmitter
- claim: EBA updated treatment of euro stablecoin payment services in 2026
  url: https://www.eba.europa.eu/publications-and-media/press-releases/eba-advises-national-authorities-actions-take-end-transition-period-under-its-no-action-letter
  date: '2026-02-12'
  quote: The transition period allows crypto asset service providers (CASPs) nine months to continue transacting electronic money tokens that qualify as payment services
- claim: MiCA contains transition until July 1, 2026 for qualifying providers
  url: https://www.esma.europa.eu/publications-and-data/interactive-single-rulebook/mica/article-143-transitional-measures
  date: '2024-12-30'
  quote: may continue to do so until 1 July 2026 or until they are granted or refused an authorisation
- claim: GENIUS Act became US law July 18, 2025
  url: https://occ.treas.gov/topics/charters-and-licensing/genius-act/index-genius-act.html
  date: '2025-07-18'
  quote: signed the Guiding and Establishing National Innovation for U.S. Stablecoins (GENIUS) Act into law on July 18, 2025
- claim: GENIUS Act will require dollar-for-dollar permitted reserves for issuers
  url: https://www.everycrsreport.com/reports/IN12553.html
  date: '2026-08-20'
  quote: Issuers are required to hold at least one dollar of permitted reserves for every one dollar of stablecoins issued.
- claim: OCC final GENIUS Act issuer rule takes effect January 18, 2027
  url: https://occ.gov/news-issuances/bulletins/2026/bulletin-2026-50.html
  date: '2026-10-21'
  quote: The final rule will be effective on January 18, 2027.
- claim: BIS finds bank cash-out can delay recipient access
  url: https://www.bis.org/publications/working-paper-1385-competing-rails-crossborder-payments-banks-fintechs-and-stablecoins
  date: '2026-10-19'
  quote: Recipients may also have to wait for stablecoin conversion and bank processing before they can access the funds in their bank accounts.
- claim: Bridge Visa stablecoin cards were live in 18 countries by March 2026
  url: https://corporate.visa.com/en/sites/visa-perspectives/press-releases/visa-bridge-stablecoin-linked-card-expansion.html
  date: '2026-03-03'
  quote: Bridge-enabled stablecoin-linked cards are now live in 18 countries, with planned expansion to over 100 countries
- claim: Visa Direct stablecoin prefunding went into commercial production
  url: https://corporate.visa.com/en/sites/visa-perspectives/newsroom/visa-direct-moves-stablecoin-pilots-production.html
  date: '2026-10-15'
  quote: Inyo Global is the first enabler to bring Visa Direct's stablecoin prefunding capability into commercial production.
```

### ed140
```yaml
status: ok
section: Market challenges
title: Where do payment firms, banks and regulators clash?
t:
  '7': Regulators want traceable payments and clear licenses
  '0': Startups want to launch globally through one simple API
  '19': Banks ask where dollars came from before paying out
  '18': Payment apps want deposits and cash-outs around the clock
  '10': Merchants want local currency and simple refunds
  '9': Wallet firms want customers to spend coins directly
  '22': Card networks decide where linked coins can be spent
  '21': Fintechs want fewer limits on countries and card use
  '13': Compliance teams need to flag risky transfers
  '12': Users want money to arrive with almost no checks
  '25': Analysts separate real payments from trading flows
  '24': Investors want fast growth from big chain totals
sources:
- claim: FinCEN treats certain custodial crypto transmitters as money services businesses
  url: https://www.fincen.gov/resources/statutes-regulations/guidance/application-fincens-regulations-persons-administering
  date: '2013-03-18'
  quote: an administrator or exchanger is an MSB under FinCEN’s regulations, specifically, a money transmitter
- claim: ESMA advises ending EU services for non-MiCA-compliant stablecoins
  url: https://www.esma.europa.eu/press-news/esma-news/esma-sets-out-supervisory-expectations-services-related-unauthorised
  date: '2026-10-08'
  quote: Crypto-asset service providers (CASPs) authorised under MiCA should cease providing services related to non-MiCA-compliant stablecoins to clients in the European Union.
- claim: BIS finds bank cash-out can delay recipient access
  url: https://www.bis.org/publications/working-paper-1385-competing-rails-crossborder-payments-banks-fintechs-and-stablecoins
  date: '2026-10-19'
  quote: Recipients may also have to wait for stablecoin conversion and bank processing before they can access the funds in their bank accounts.
- claim: Stripe added USDC merchant acceptance for Shopify in 34 countries
  url: https://stripe.com/newsroom/news/shopify-stripe-stablecoin-payments
  date: '2025-06-12'
  quote: Shopify merchants across 34 countries will be able to accept USDC, a dollar-backed stablecoin.
- claim: Bridge Visa stablecoin cards were live in 18 countries by March 2026
  url: https://corporate.visa.com/en/sites/visa-perspectives/press-releases/visa-bridge-stablecoin-linked-card-expansion.html
  date: '2026-03-03'
  quote: Bridge-enabled stablecoin-linked cards are now live in 18 countries, with planned expansion to over 100 countries
- claim: Most blockchain stablecoin volumes are not end-user payments
  url: https://www.mckinsey.com/industries/financial-services/our-insights/stablecoins-in-payments-what-the-raw-transaction-numbers-miss
  date: '2026-02-18'
  quote: most of this activity doesn’t represent true end-user payments, such as paying suppliers or sending remittances.
- claim: Chainalysis estimates 84% of 2025 illicit crypto flows involved stablecoins
  url: https://www.chainalysis.com/blog/2026-crypto-crime-report-introduction/
  date: '2026-01-08'
  quote: Stablecoins currently dominate the illicit crypto ecosystem, accounting for 84% of all illicit transaction volume in 2025.
```

### iv_safety
```yaml
status: ok
section: Market challenges
title: What could go wrong for stablecoin payments?
t:
  '6': 'PEG BREAK


    USDC lost its dollar peg in March 2023 after Circle disclosed $3.3B at Silicon Valley Bank, putting payment trust at risk.'
  '7': 'BANK CUT OFF


    Circle cleared a backlog of USDC minting and redemption after the 2023 bank failures, exposing the risk of blocked cash-out.'
  '8': 'LICENSE SHOCK


    In October 2026, ESMA said EU providers should stop offering services with stablecoins that do not comply with MiCA rules.'
  '9': 'FRAUD COSTS


    Paxos accepted a $26.5M New York penalty in 2025 over old compliance issues with Binance, showing the cost of weak checks.'
  '10': 'GIANT RIVALS


    Mastercard bought BVNK in August 2026, bringing stablecoin payments inside a major card network and raising the bar.'
note: We selected documented reserve, banking, licensing, compliance and competition events. These are scenarios, not predictions of how often a provider will fail.
sources:
- claim: Circle disclosed $3.3B of USDC reserves at failed SVB
  url: https://www.circle.com/pressroom/3-3-billion-of-usdc-reserve-risk-removed-dollar-de-peg-closes
  date: '2023-03-13'
  quote: The $3.3B USDC reserve deposit held at Silicon Valley Bank, about 8% of the USDC total reserve
- claim: Circle USDC redemptions faced a backlog after bank failure
  url: https://www.circle.com/blog/march-15-update-on-usdc-operations
  date: '2023-03-16'
  quote: we have cleared substantially all of the backlog of minting and redemption requests for USDC.
- claim: ESMA advises ending EU services for non-MiCA-compliant stablecoins
  url: https://www.esma.europa.eu/press-news/esma-news/esma-sets-out-supervisory-expectations-services-related-unauthorised
  date: '2026-10-08'
  quote: Crypto-asset service providers (CASPs) authorised under MiCA should cease providing services related to non-MiCA-compliant stablecoins to clients in the European Union.
- claim: Paxos paid $26.5M for historical compliance failures with Binance
  url: https://www.paxos.com/newsroom/statement-from-paxos-in-response-to-nydfs
  date: '2025-08-07'
  quote: This agreement includes a $26.5M monetary penalty.
- claim: Mastercard completed acquisition of BVNK in August 2026
  url: https://www.mastercard.com/global/en/news-and-trends/press/2026/august/mastercard-completes-acquisition-of-bvnk-to-advance-global-stabl.html
  date: '2026-08-03'
  quote: 'Mastercard (NYSE: MA) today completed its acquisition of BVNK'
```

### ed141
```yaml
status: ok
section: Market challenges
title: Which constraints are structural?
t:
  '5': 'Getting digital dollars in or out


    still requires a bank or cash partner'
  '10': 'A coin moves all day, but local banks


    and payment systems may not'
  '15': 'Fraud, sanctions and identity checks


    are required on regulated routes'
  '20': 'Thin local-currency liquidity can


    wipe out savings on small transfers'
  '25': 'Merchants need clear prices,


    refunds and easy checkout'
sources:
- claim: BIS highlights thin local-currency liquidity
  url: https://www.bis.org/publications/working-paper-1385-competing-rails-crossborder-payments-banks-fintechs-and-stablecoins
  date: '2026-10-19'
  quote: Moreover, liquidity between US dollar stablecoins and non-US currencies is generally very thin.
- claim: BIS finds bank cash-out can delay recipient access
  url: https://www.bis.org/publications/working-paper-1385-competing-rails-crossborder-payments-banks-fintechs-and-stablecoins
  date: '2026-10-19'
  quote: Recipients may also have to wait for stablecoin conversion and bank processing before they can access the funds in their bank accounts.
- claim: FinCEN treats certain custodial crypto transmitters as money services businesses
  url: https://www.fincen.gov/resources/statutes-regulations/guidance/application-fincens-regulations-persons-administering
  date: '2013-03-18'
  quote: an administrator or exchanger is an MSB under FinCEN’s regulations, specifically, a money transmitter
- claim: Stripe added USDC merchant acceptance for Shopify in 34 countries
  url: https://stripe.com/newsroom/news/shopify-stripe-stablecoin-payments
  date: '2025-06-12'
  quote: Shopify merchants across 34 countries will be able to accept USDC, a dollar-backed stablecoin.
- claim: Stablecoin cards give direct spending access at merchants
  url: https://www.mckinsey.com/industries/financial-services/our-insights/stablecoins-in-payments-what-the-raw-transaction-numbers-miss
  date: '2026-02-18'
  quote: stablecoin-linked cards are expanding practical usability by enabling holders to spend stablecoins directly with merchants globally
```

### ed143
```yaml
status: ok
section: Market challenges
title: How likely is each stablecoin payment risk?
comment: The eight probabilities are analyst estimates over five years, not directly observed event rates. Evidence sources support risk mechanisms, not the quoted percentages.
t:
  '38': ≈80%
  '37': VOLUME HYPE
  '34': Many transfers reflect trading or internal wallet movements
  '27': ≈75%
  '26': LOW ADOPTION
  '24': McKinsey found real payments were only 0.02 percent of payment value
  '23': ≈45%
  '22': CARD GATEKEEPERS
  '20': Visa and Mastercard now link stablecoins to vast card networks
  '19': ≈70%
  '18': FX EXIT COST
  '16': BIS found local coin swaps add fees and slow cash-outs
  '15': ≈65%
  '14': FRAUD & SANCTIONS
  '12': Chainalysis says stablecoins made up 84% of illicit crypto flows
  '11': ≈55%
  '10': LICENSE DELAY
  '8': EU MiCA and PSD2 overlap has forced extra payment reviews
  '7': ≈35%
  '6': BANK RAIL LOSS
  '4': Circle needed new banking routes after its 2023 redemption backlog
  '3': ≈20%
  '2': PEG LOSS
  '0': USDC broke its peg when $3.3B of reserves sat at failed SVB
note: We estimate the chance each issue materially disrupts payment market growth within five years. Percentages are scenario judgments anchored in the documented incidents, not measured frequencies.
sources:
- claim: Most blockchain stablecoin volumes are not end-user payments
  url: https://www.mckinsey.com/industries/financial-services/our-insights/stablecoins-in-payments-what-the-raw-transaction-numbers-miss
  date: '2026-02-18'
  quote: most of this activity doesn’t represent true end-user payments, such as paying suppliers or sending remittances.
- claim: Real stablecoin payments account for about 0.02 percent of global payment value
  url: https://www.mckinsey.com/industries/financial-services/our-insights/stablecoins-in-payments-what-the-raw-transaction-numbers-miss
  date: '2026-02-18'
  quote: representing roughly 0.02 percent of global payments volumes
- claim: Stablecoin-linked card spending was $4.5B in 2025, up 673%
  url: https://www.mckinsey.com/industries/financial-services/our-insights/stablecoins-in-payments-what-the-raw-transaction-numbers-miss
  date: '2026-02-18'
  quote: We estimate that stablecoin-linked card spending has grown to $4.5 billion in 2025, up 673 percent from 2024.
- claim: BIS finds conversion and withdrawal costs complicate stablecoin payments
  url: https://www.bis.org/publications/working-paper-1385-competing-rails-crossborder-payments-banks-fintechs-and-stablecoins
  date: '2026-10-19'
  quote: These conversions still rely on crypto exchanges and other intermediaries, whose trading, conversion and withdrawal fees can substantially increase the total cost.
- claim: Chainalysis estimates 84% of 2025 illicit crypto flows involved stablecoins
  url: https://www.chainalysis.com/blog/2026-crypto-crime-report-introduction/
  date: '2026-01-08'
  quote: Stablecoins currently dominate the illicit crypto ecosystem, accounting for 84% of all illicit transaction volume in 2025.
- claim: EBA highlighted double-authorization problem for payments using euro stablecoins
  url: https://www.eba.europa.eu/publications-and-media/press-releases/eba-publishes-no-action-letter-interplay-between-payment-services-directive-psd23-and-markets-crypto
  date: '2025-06-10'
  quote: EU law needs to avoid a dual authorisation under two pieces of EU law for the activity of transacting electronic money tokens
- claim: Circle disclosed $3.3B of USDC reserves at failed SVB
  url: https://www.circle.com/pressroom/3-3-billion-of-usdc-reserve-risk-removed-dollar-de-peg-closes
  date: '2023-03-13'
  quote: The $3.3B USDC reserve deposit held at Silicon Valley Bank, about 8% of the USDC total reserve
- claim: Circle USDC redemptions faced a backlog after bank failure
  url: https://www.circle.com/blog/march-15-update-on-usdc-operations
  date: '2023-03-16'
  quote: we have cleared substantially all of the backlog of minting and redemption requests for USDC.
- claim: Bridge Visa stablecoin cards were live in 18 countries by March 2026
  url: https://corporate.visa.com/en/sites/visa-perspectives/press-releases/visa-bridge-stablecoin-linked-card-expansion.html
  date: '2026-03-03'
  quote: Bridge-enabled stablecoin-linked cards are now live in 18 countries, with planned expansion to over 100 countries
```

### ed144
```yaml
status: ok
section: Market challenges
title: How severe is the impact of each one?
t:
  '38': MEDIUM
  '37': VOLUME HYPE
  '34': Misreading activity can waste capital on demand that is not truly there.
  '27': MEDIUM
  '26': LOW ADOPTION
  '24': Weak store demand slows scale even if business settlement grows.
  '23': MEDIUM
  '22': CARD GATEKEEPERS
  '20': Card limits can curb reach while bank and wallet payouts remain open.
  '19': MEDIUM
  '18': FX EXIT COST
  '16': Cash-out costs can erase savings without breaking payment service.
  '15': HIGH
  '14': FRAUD & SANCTIONS
  '12': Weak screening can prompt fines, lost partners and blocked payment corridors.
  '11': MEDIUM
  '10': LICENSE DELAY
  '8': Late approvals slow launches, but firms can still enter later.
  '7': HIGH
  '6': BANK RAIL LOSS
  '4': Losing a bank can halt cash-in and cash-out while the chain keeps running.
  '3': HIGH
  '2': PEG LOSS
  '0': A trust shock could freeze cash-outs and stop merchants taking a coin.
note: We rate impact on a typical stablecoin payment business if each risk materializes. Severity reflects our judgment, informed by observed failures, regulation and payment costs.
sources:
- claim: Circle disclosed $3.3B of USDC reserves at failed SVB
  url: https://www.circle.com/pressroom/3-3-billion-of-usdc-reserve-risk-removed-dollar-de-peg-closes
  date: '2023-03-13'
  quote: The $3.3B USDC reserve deposit held at Silicon Valley Bank, about 8% of the USDC total reserve
- claim: Circle USDC redemptions faced a backlog after bank failure
  url: https://www.circle.com/blog/march-15-update-on-usdc-operations
  date: '2023-03-16'
  quote: we have cleared substantially all of the backlog of minting and redemption requests for USDC.
- claim: EBA highlighted double-authorization problem for payments using euro stablecoins
  url: https://www.eba.europa.eu/publications-and-media/press-releases/eba-publishes-no-action-letter-interplay-between-payment-services-directive-psd23-and-markets-crypto
  date: '2025-06-10'
  quote: EU law needs to avoid a dual authorisation under two pieces of EU law for the activity of transacting electronic money tokens
- claim: ESMA advises ending EU services for non-MiCA-compliant stablecoins
  url: https://www.esma.europa.eu/press-news/esma-news/esma-sets-out-supervisory-expectations-services-related-unauthorised
  date: '2026-10-08'
  quote: Crypto-asset service providers (CASPs) authorised under MiCA should cease providing services related to non-MiCA-compliant stablecoins to clients in the European Union.
- claim: Chainalysis estimates 84% of 2025 illicit crypto flows involved stablecoins
  url: https://www.chainalysis.com/blog/2026-crypto-crime-report-introduction/
  date: '2026-01-08'
  quote: Stablecoins currently dominate the illicit crypto ecosystem, accounting for 84% of all illicit transaction volume in 2025.
- claim: BIS finds conversion and withdrawal costs complicate stablecoin payments
  url: https://www.bis.org/publications/working-paper-1385-competing-rails-crossborder-payments-banks-fintechs-and-stablecoins
  date: '2026-10-19'
  quote: These conversions still rely on crypto exchanges and other intermediaries, whose trading, conversion and withdrawal fees can substantially increase the total cost.
- claim: Bridge Visa stablecoin cards were live in 18 countries by March 2026
  url: https://corporate.visa.com/en/sites/visa-perspectives/press-releases/visa-bridge-stablecoin-linked-card-expansion.html
  date: '2026-03-03'
  quote: Bridge-enabled stablecoin-linked cards are now live in 18 countries, with planned expansion to over 100 countries
- claim: Real stablecoin payments account for about 0.02 percent of global payment value
  url: https://www.mckinsey.com/industries/financial-services/our-insights/stablecoins-in-payments-what-the-raw-transaction-numbers-miss
  date: '2026-02-18'
  quote: representing roughly 0.02 percent of global payments volumes
- claim: Most blockchain stablecoin volumes are not end-user payments
  url: https://www.mckinsey.com/industries/financial-services/our-insights/stablecoins-in-payments-what-the-raw-transaction-numbers-miss
  date: '2026-02-18'
  quote: most of this activity doesn’t represent true end-user payments, such as paying suppliers or sending remittances.
```

### ed145
```yaml
status: ok
section: Market challenges
title: Which constraints have largely disappeared today?
t:
  '32': CONSTRAINT
  '31': WHY IT HAS EASED
  '5': 'Businesses had few ways to


    accept coins during checkout'
  '7': 'Stripe now brings USDC checkout


    to Shopify sellers in 34 countries'
  '8': 'Coin users had few paths to


    spend at regular card stores'
  '10': 'Visa and Bridge now support


    stablecoin cards in 18 countries'
  '11': 'Banks had little real-world


    proof of using coins to settle'
  '13': 'Visa now settles USDC with two


    US banks over a live network'
  '14': 'Firms had to build more of


    the stablecoin payment stack'
  '16': 'Circle now runs managed


    settlement for payment firms'
  '17': 'US coin issuers lacked


    a national reserve law'
  '19': 'GENIUS Act sets future


    reserve rules for coin issuers'
  '20': 'Nobody had clean estimates


    of real stablecoin payments'
  '22': 'McKinsey and Artemis now track


    $390B in annualized payments'
note: We show constraints that eased through working products, a new US statute and better data. The US reserve rules take effect later, while banking and licensing gaps remain.
sources:
- claim: Stripe added USDC merchant acceptance for Shopify in 34 countries
  url: https://stripe.com/newsroom/news/shopify-stripe-stablecoin-payments
  date: '2025-06-12'
  quote: Shopify merchants across 34 countries will be able to accept USDC, a dollar-backed stablecoin.
- claim: Bridge Visa stablecoin cards were live in 18 countries by March 2026
  url: https://corporate.visa.com/en/sites/visa-perspectives/press-releases/visa-bridge-stablecoin-linked-card-expansion.html
  date: '2026-03-03'
  quote: Bridge-enabled stablecoin-linked cards are now live in 18 countries, with planned expansion to over 100 countries
- claim: Visa began US bank settlement in USDC
  url: https://corporate.visa.com/en/sites/visa-perspectives/press-releases/visa-launches-stablecoin-settlement-in-the-united-states.html
  date: '2025-12-16'
  quote: Initial banking participants include Cross River Bank and Lead Bank, which have started settling with Visa in USDC over the Solana blockchain.
- claim: Circle launched CPN Managed Payments in April 2026
  url: https://www.circle.com/pressroom/circle-launches-cpn-managed-payments-a-full-stack-platform-for-seamless-stablecoin-settlement
  date: '2026-04-08'
  quote: CPN Managed Payments abstracts digital asset complexity, enabling partners to interact solely in fiat while Circle manages the entire digital asset lifecycle
- claim: GENIUS Act became US law July 18, 2025
  url: https://occ.treas.gov/topics/charters-and-licensing/genius-act/index-genius-act.html
  date: '2025-07-18'
  quote: signed the Guiding and Establishing National Innovation for U.S. Stablecoins (GENIUS) Act into law on July 18, 2025
- claim: GENIUS Act will require dollar-for-dollar permitted reserves for issuers
  url: https://www.everycrsreport.com/reports/IN12553.html
  date: '2026-08-20'
  quote: Issuers are required to hold at least one dollar of permitted reserves for every one dollar of stablecoins issued.
- claim: OCC final GENIUS Act issuer rule takes effect January 18, 2027
  url: https://occ.gov/news-issuances/bulletins/2026/bulletin-2026-50.html
  date: '2026-10-21'
  quote: The final rule will be effective on January 18, 2027.
- claim: McKinsey and Artemis estimate $390B in annualized stablecoin payment volume
  url: https://www.mckinsey.com/industries/financial-services/our-insights/stablecoins-in-payments-what-the-raw-transaction-numbers-miss
  date: '2026-02-18'
  quote: the volume of actual stablecoin payments made annually is about $390 billion
```
