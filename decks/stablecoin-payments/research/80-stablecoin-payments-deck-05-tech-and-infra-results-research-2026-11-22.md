### ed087
```yaml
status: ok
section: Tech and infra
title: What are the tech and infra layers?
page: 1/2
t:
  7: CHAINS
  10: Blockchains record stablecoin transfers across borders, even on weekends.
  9: WALLETS
  11: Wallets hold and send digital dollars. Signing controls approve each payment.
  21: LAYERS
  12: FX RAMPS
  14: Partners turn bank cash into stablecoins and pay out local currency.
  13: PAYOUTS
  15: Banks and mobile money networks deliver final funds after settlement.
note: We map the stack from moving a token to delivering spendable money. Blockchain settlement alone is not a complete payment.
sources:
- claim: bridge
  url: https://bridge.xyz/product/orchestration
  date: undated
  quote: A single API enables you to move USDC, USDT, your own stablecoin, and more across 10+ blockchains.
- claim: circle26
  url: https://www.circle.com/pressroom/circle-launches-cpn-managed-payments-a-full-stack-platform-for-seamless-stablecoin-settlement
  date: '2026-04-08'
  quote: CPN Managed Payments abstracts digital asset complexity, enabling partners to interact solely in fiat while Circle manages the entire digital asset lifecycle
- claim: yellow
  url: https://yellowcard.io/api
  date: undated
  quote: Collect and pay out local currency across emerging markets through one API.
- claim: conduit
  url: https://conduitpay.com/send
  date: undated
  quote: Our global network uses stablecoins to power faster, cheaper international fiat to fiat transfers.
```

### ed088
```yaml
status: ok
section: Tech and infra
title: What are the tech and infra layers?
page: 2/2
t:
  7: LIQUIDITY
  10: Cash and token reserves let firms quote exchange rates and complete transfers reliably.
  9: CHECKS
  11: Wallet and identity checks decide who can send or receive money in each market.
  21: LAYERS
  12: CARD FUND
  14: Card programs need ready funds for settlement even when banks are closed.
  13: OPS
  15: Tracking, refunds, and payment records turn transfers into a reliable service.
note: We include the operating layers needed for a customer payment to clear, convert, reach its destination, and reconcile.
sources:
- claim: visaerror
  url: https://www.visa.com/en-us/thought-leadership/innovation/financing-stablecoin-linked-card-programs
  date: '2026-09-08'
  quote: Every card program has to fund its daily settlement obligation before it collects from cardholders
- claim: circle26
  url: https://www.circle.com/pressroom/circle-launches-cpn-managed-payments-a-full-stack-platform-for-seamless-stablecoin-settlement
  date: '2026-04-08'
  quote: CPN Managed Payments abstracts digital asset complexity, enabling partners to interact solely in fiat while Circle manages the entire digital asset lifecycle
- claim: bridge
  url: https://bridge.xyz/product/orchestration
  date: undated
  quote: A single API enables you to move USDC, USDT, your own stablecoin, and more across 10+ blockchains.
- claim: mastercard26
  url: https://www.mastercard.com/us/en/news-and-trends/press/2026/june/mastercard-expands-settlement-capabilities-to-include-stablecoin.html
  date: '2026-06-03'
  quote: Mastercard today announced plans to expand its settlement capabilities with additional intraday, weekend and holiday card settlement
```

### ed089
```yaml
status: ok
section: Tech and infra
title: Does every layer carry the same weight?
note: We rank layers by how directly they limit a reliable customer payment. This is an editorial ranking, not a measured fee share.
t:
  38: RANKING
  6: CASH OUT
  14: Turns token balances into money recipients can use at local banks, wallets, or stores.
  7: CHECKS
  24: Makes sender and receiver checks work across laws, partners, and jurisdictions.
  8: LIQUIDITY
  26: Ensures enough dollars and local currency are available for each conversion.
  9: ROUTING
  28: Selects working chains and payout partners to avoid delays, retries, and fees.
  10: WALLETS
  30: Secures the balance and approvals that start or accept an actual payment.
  11: CARD FUND
  32: Keeps stablecoin-backed card programs funded for daily network settlement.
  12: APIS
  34: Lets merchants and fintechs add payment flows without rebuilding each local rail.
  13: AUDIT
  36: Tracks receipts, screening results, and exceptions after funds have moved.
sources:
- claim: bridge
  url: https://bridge.xyz/product/orchestration
  date: undated
  quote: A single API enables you to move USDC, USDT, your own stablecoin, and more across 10+ blockchains.
- claim: yellow
  url: https://yellowcard.io/api
  date: undated
  quote: Collect and pay out local currency across emerging markets through one API.
- claim: visaerror
  url: https://www.visa.com/en-us/thought-leadership/innovation/financing-stablecoin-linked-card-programs
  date: '2026-09-08'
  quote: Every card program has to fund its daily settlement obligation before it collects from cardholders
- claim: circle26
  url: https://www.circle.com/pressroom/circle-launches-cpn-managed-payments-a-full-stack-platform-for-seamless-stablecoin-settlement
  date: '2026-04-08'
  quote: CPN Managed Payments abstracts digital asset complexity, enabling partners to interact solely in fiat while Circle manages the entire digital asset lifecycle
```

### ed090
```yaml
status: ok
section: Tech and infra
title: Where does 80% of stablecoin payments value sit?
note: We use an 80/20 value-chain hypothesis, not a measured distribution of stablecoin payment company revenue.
t:
  9: 💰 💰 💰 💰 💰 💰 💰 💰 💰 💰 💰 💰 💰 💰 💰 💰 💰 💰 💰 💰 💰 💰 💰 💰 💰 💰 💰 💰 💰 💰 💰 💰 💰 💰 💰 💰 💰 💰 💰 💰 💰 💰 💰 💰 💰 💰 💰 💰 💰 💰 💰 💰 💰 💰 💰 💰 💰 💰 💰 💰 💰 💰 💰 💰 💰 💰 💰 💰 💰 💰 💰 💰 💰 💰 💰 💰 💰 💰 💰 💰 💰 💰 💰 💰 💰 💰 💰
  8: "The highest-value problems sit where stablecoins become usable money: local cash-out, bank access, and reliable currency conversion. These steps decide whether recipients actually get paid.\n\nCompliance\
    \ and liquidity come next. Wallet checks, regulated partners, and funding matter across every country and customer type.\n\nBlockchains are necessary, but speed alone is not the moat. Payment winners\
    \ will combine routes, trust, and steady settlement in one service."
comment: No verified source assigns 80% of industry revenue to particular infrastructure layers. This slide shows an explicit qualitative hypothesis.
sources:
- claim: yellow
  url: https://yellowcard.io/api
  date: undated
  quote: Collect and pay out local currency across emerging markets through one API.
- claim: conduit
  url: https://conduitpay.com/send
  date: undated
  quote: Our global network uses stablecoins to power faster, cheaper international fiat to fiat transfers.
- claim: bridge
  url: https://bridge.xyz/product/orchestration
  date: undated
  quote: A single API enables you to move USDC, USDT, your own stablecoin, and more across 10+ blockchains.
- claim: circle26
  url: https://www.circle.com/pressroom/circle-launches-cpn-managed-payments-a-full-stack-platform-for-seamless-stablecoin-settlement
  date: '2026-04-08'
  quote: CPN Managed Payments abstracts digital asset complexity, enabling partners to interact solely in fiat while Circle manages the entire digital asset lifecycle
```

### ed091
```yaml
status: ok
section: Tech and infra
title: How has tech and infra evolved over the years?
note: We track launches of real payment services and network integrations rather than the date a token first traded.
t:
  6: "2018 - 2022\n\nStablecoins gained practical wallet uses, but merchants still needed banks, cash-out partners, and separate crypto tools to get paid."
  7: "2023\n\nPayPal introduced PYUSD for payments, while Visa expanded live USDC settlement pilots to Solana and merchant acquirers."
  8: "2024 - 2025\n\nStripe bought Bridge, Circle launched CPN, Mastercard added merchant settlement options, and Visa grew card services."
  9: "2026\n\nCircle added managed settlement, Visa expanded its supported chains, and payment firms shipped bank-funded bills and local-currency payouts."
  10: "NEXT\n\nServices may hide blockchain steps from payers, offer cards at scale, and route cash-outs and compliance in more markets."
sources:
- claim: circle2018
  url: https://www.circle.com/blog/usd-coin-launches-with-wide-ecosystem-support
  date: '2018-09-26'
  quote: Circle and the CENTRE open source consortium today introduced a service to tokenize US dollars, called USD//Coin (USDC)
- claim: paypal23
  url: https://developer.paypal.com/community/blog/pyusd-stablecoin/
  date: '2024-01-25'
  quote: In August 2023, PayPal announced the launch of PayPal USD (PYUSD), a U.S. dollar denominated stablecoin designed for payments.
- claim: visapilot
  url: https://usa.visa.com/about-visa/newsroom/press-releases.releaseId.19881.html
  date: '2023-09-05'
  quote: Through live pilots with issuers and acquirers, Visa has already moved millions of USDC between its partners over the Solana and Ethereum blockchain networks
- claim: bridge25
  url: https://stripe.com/newsroom/news/stripe-completes-bridge-acquisition
  date: '2025-02-04'
  quote: Stripe, a financial infrastructure platform for businesses, today announced that it has completed its acquisition of Bridge.
- claim: circle25
  url: https://www.circle.com/blog/circle-payments-network-cpn-mainnet-is-here-advancing-mainstream-stablecoin-payments-globally
  date: '2025-05-21'
  quote: the Circle Payments Network (CPN) mainnet is officially live, with a growing roster of financial institutions now moving value globally
- claim: mastercard25
  url: https://investor.mastercard.com/investor-news/investor-news-details/2025/Mastercard-Unveils-End-to-End-Capabilities-to-Power-Stablecoin-Transactions--From-Wallets-to-Checkouts/default.aspx
  date: '2025-04-28'
  quote: Mastercard is teaming up with Nuvei and Circle to give merchants the option to receive their payments in stablecoins
- claim: circle26
  url: https://www.circle.com/pressroom/circle-launches-cpn-managed-payments-a-full-stack-platform-for-seamless-stablecoin-settlement
  date: '2026-04-08'
  quote: CPN Managed Payments abstracts digital asset complexity, enabling partners to interact solely in fiat while Circle manages the entire digital asset lifecycle
- claim: visa2026
  url: https://corporate.visa.com/en/sites/visa-perspectives/press-releases/visa-expands-stablecoin-settlement-adds-five-blockchains.html
  date: '2026-04-29'
  quote: Visa’s stablecoin settlement pilot now supports nine blockchains and has reached a $7 billion annualized stablecoin settlement run rate
- claim: rampstripe
  url: https://stripe.com/en-fi/newsroom/news/ramp-and-stripe
  date: '2026-07-21'
  quote: Ramp customers can now pay bills with stablecoin payments funded from an external bank account
```

### ed092
```yaml
status: ok
section: Tech and infra
title: What were the latest tech and infra developments?
page: 1/2
note: We use company announcements and distinguish commercial services from early pilots that still have limited customer access.
t:
  13: '2023'
  14: PayPal introduced PYUSD for payments, making a major wallet provider a stablecoin issuer focused on everyday commerce.
  15: '2023'
  16: Visa used USDC over Solana and Ethereum in live pilots, linking blockchain transfer with card network settlement.
  17: '2025'
  18: Stripe completed its acquisition of Bridge, bringing stablecoin transfer and conversion APIs into a major payment platform.
  19: '2025'
  20: Circle launched its Payments Network, giving financial firms a way to route cross-border settlements using regulated stablecoins.
  21: '2025'
  22: Mastercard and Nuvei outlined merchant settlement in USDC, letting sellers receive stablecoins even when buyers pay another way.
  23: '2025'
  24: Visa began testing Visa Direct payouts to stablecoin wallets for platforms paying freelancers across borders.
sources:
- claim: paypal23
  url: https://developer.paypal.com/community/blog/pyusd-stablecoin/
  date: '2024-01-25'
  quote: In August 2023, PayPal announced the launch of PayPal USD (PYUSD), a U.S. dollar denominated stablecoin designed for payments.
- claim: visapilot
  url: https://usa.visa.com/about-visa/newsroom/press-releases.releaseId.19881.html
  date: '2023-09-05'
  quote: Through live pilots with issuers and acquirers, Visa has already moved millions of USDC between its partners over the Solana and Ethereum blockchain networks
- claim: bridge25
  url: https://stripe.com/newsroom/news/stripe-completes-bridge-acquisition
  date: '2025-02-04'
  quote: Stripe, a financial infrastructure platform for businesses, today announced that it has completed its acquisition of Bridge.
- claim: circle25
  url: https://www.circle.com/blog/circle-payments-network-cpn-mainnet-is-here-advancing-mainstream-stablecoin-payments-globally
  date: '2025-05-21'
  quote: the Circle Payments Network (CPN) mainnet is officially live, with a growing roster of financial institutions now moving value globally
- claim: mastercard25
  url: https://investor.mastercard.com/investor-news/investor-news-details/2025/Mastercard-Unveils-End-to-End-Capabilities-to-Power-Stablecoin-Transactions--From-Wallets-to-Checkouts/default.aspx
  date: '2025-04-28'
  quote: Mastercard is teaming up with Nuvei and Circle to give merchants the option to receive their payments in stablecoins
- claim: visa25payout
  url: https://corporate.visa.com/en/sites/visa-perspectives/newsroom/visa-direct-stablecoin-payouts.html
  date: '2025-11-12'
  quote: Visa Inc. (V) announced a breakthrough pilot allowing businesses and platforms to send payouts directly to recipients’ stablecoin wallets.
```

### ed093
```yaml
status: ok
section: Tech and infra
title: What were the latest tech and infra developments?
page: 2/2
note: We select 2026 company announcements that change how payments can be accepted, settled, converted, or spent.
t:
  13: '2026'
  14: Circle launched CPN Managed Payments, letting firms pay through stablecoin settlement while Circle handles wallets and compliance work.
  15: '2026'
  16: Visa expanded its stablecoin settlement pilot to nine chains and reported a $7B annualized run rate, giving partners more routes.
  17: '2026'
  18: Mastercard outlined card settlement in USDC and other regulated stablecoins, with early deployments and more bank support planned.
  19: '2026'
  20: MoonPay joined WalletConnect and Ingenico to connect stablecoin checkout at store terminals with fiat settlement for merchants.
  21: '2026'
  22: Stripe enabled Ramp Bill Pay customers to send bank-funded stablecoin bill payments through Bridge, without holding coins first.
  23: '2026'
  24: Western Union and Rain launched Stablecard, combining a wallet for USDPT with a Visa card designed for everyday spending.
sources:
- claim: circle26
  url: https://www.circle.com/pressroom/circle-launches-cpn-managed-payments-a-full-stack-platform-for-seamless-stablecoin-settlement
  date: '2026-04-08'
  quote: CPN Managed Payments abstracts digital asset complexity, enabling partners to interact solely in fiat while Circle manages the entire digital asset lifecycle
- claim: visa2026
  url: https://corporate.visa.com/en/sites/visa-perspectives/press-releases/visa-expands-stablecoin-settlement-adds-five-blockchains.html
  date: '2026-04-29'
  quote: Visa’s stablecoin settlement pilot now supports nine blockchains and has reached a $7 billion annualized stablecoin settlement run rate
- claim: mastercard26
  url: https://www.mastercard.com/us/en/news-and-trends/press/2026/june/mastercard-expands-settlement-capabilities-to-include-stablecoin.html
  date: '2026-06-03'
  quote: Mastercard today announced plans to expand its settlement capabilities with additional intraday, weekend and holiday card settlement
- claim: moonpos
  url: https://www.moonpay.com/newsroom/moonpay-iron-walletconnect
  date: '2026-04-09'
  quote: When a customer pays in stablecoins at an Ingenico terminal, Iron will handle the off-ramp
- claim: rampstripe
  url: https://stripe.com/en-fi/newsroom/news/ramp-and-stripe
  date: '2026-07-21'
  quote: Ramp customers can now pay bills with stablecoin payments funded from an external bank account
- claim: westerncard
  url: https://ir.westernunion.com/news/archived-press-releases/press-release-details/2026/Western-Union-Launches-Stablecard-in-Partnership-with-Rain/default.aspx
  date: '2026-08-04'
  quote: Stablecard offers a consumer-friendly way to receive funds and store value in USDPT
```

### ed094
```yaml
status: ok
section: Tech and infra
title: What are the solvable bottlenecks?
note: We focus on problems visible in live payment products, card settlement, bank connections, and compliance workflows.
t:
  39: BOTTLENECK
  38: EXPLANATION
  41: BOTTLENECK
  40: EXPLANATION
  7: "FX\\nLIQUIDITY"
  5: Currency conversions need enough cash and stablecoins on both sides, including nights and weekends.
  24: "RULES\\nBY MARKET"
  22: Providers must check identities, sanctions, and local rules in every corridor.
  11: "LOCAL\\nCASH OUT"
  9: Recipients may need a bank transfer or mobile money, not a token balance in a wallet.
  28: "CARD\\nFUNDING"
  26: Card programs must fund daily network settlement before user balances clear.
  15: "BANK\\nACCESS"
  13: Fiat accounts still depend on licensed banks and local transfer rules.
  32: "REFUND\\nROUTES"
  30: Refunds must return value even when a blockchain transfer cannot be undone.
  19: "WALLET\\nSAFETY"
  17: A wrong address or stolen signing key can make a payment hard to recover.
  36: "CHAIN\\nSPLITS"
  34: Tokens exist on many networks, and moving value between them adds steps and risk.
sources:
- claim: visaerror
  url: https://www.visa.com/en-us/thought-leadership/innovation/financing-stablecoin-linked-card-programs
  date: '2026-09-08'
  quote: Every card program has to fund its daily settlement obligation before it collects from cardholders
- claim: yellow
  url: https://yellowcard.io/api
  date: undated
  quote: Collect and pay out local currency across emerging markets through one API.
- claim: bridge
  url: https://bridge.xyz/product/orchestration
  date: undated
  quote: A single API enables you to move USDC, USDT, your own stablecoin, and more across 10+ blockchains.
- claim: circle26
  url: https://www.circle.com/pressroom/circle-launches-cpn-managed-payments-a-full-stack-platform-for-seamless-stablecoin-settlement
  date: '2026-04-08'
  quote: CPN Managed Payments abstracts digital asset complexity, enabling partners to interact solely in fiat while Circle manages the entire digital asset lifecycle
- claim: paypal26
  url: https://developer.paypal.com/crypto/
  date: '2026-08-11'
  quote: accept cryptocurrency (crypto) payments from global buyers and receive automatic settlement in local currency.
```

### ed095
```yaml
status: ok
section: Tech and infra
title: Why can’t we solve them yet?
note: We explain each obstacle as an operational dependency, not as a failure of blockchain speed alone.
t:
  39: BOTTLENECK
  38: REASON WHY
  41: BOTTLENECK
  40: REASON WHY
  7: "FX\\nLIQUIDITY"
  5: Conversion rates depend on partners, local currency demand, and inventory held across time zones.
  24: "RULES\\nBY MARKET"
  22: Licenses and customer checks differ by country, asset, company, and recipient.
  11: "LOCAL\\nCASH OUT"
  9: Local banks, wallet partners, and holidays vary by country and can delay the last mile.
  28: "CARD\\nFUNDING"
  26: Issuers may owe card networks cash before stablecoins can be sold or funds collected.
  15: "BANK\\nACCESS"
  13: A chain can stay open while the bank that accepts or sends fiat money is closed.
  32: "REFUND\\nROUTES"
  30: Token transfers are final, but mistaken payments and disputes still occur.
  19: "WALLET\\nSAFETY"
  17: Open wallet transfers are hard to recover, so signing and identity checks matter.
  36: "CHAIN\\nSPLITS"
  34: Chains have different fees, wallets, and token versions that routers must handle.
sources:
- claim: bridge
  url: https://bridge.xyz/product/orchestration
  date: undated
  quote: A single API enables you to move USDC, USDT, your own stablecoin, and more across 10+ blockchains.
- claim: visa24h
  url: https://www.visa.com/en-us/thought-leadership/innovation/onchain-settlement-financing
  date: '2026-09-08'
  quote: Traditional financing was not designed for digital-native, 24/7 card programs.
- claim: mastercard26
  url: https://www.mastercard.com/us/en/news-and-trends/press/2026/june/mastercard-expands-settlement-capabilities-to-include-stablecoin.html
  date: '2026-06-03'
  quote: Mastercard today announced plans to expand its settlement capabilities with additional intraday, weekend and holiday card settlement
- claim: circle26
  url: https://www.circle.com/pressroom/circle-launches-cpn-managed-payments-a-full-stack-platform-for-seamless-stablecoin-settlement
  date: '2026-04-08'
  quote: CPN Managed Payments abstracts digital asset complexity, enabling partners to interact solely in fiat while Circle manages the entire digital asset lifecycle
- claim: paypal26
  url: https://developer.paypal.com/crypto/
  date: '2026-08-11'
  quote: accept cryptocurrency (crypto) payments from global buyers and receive automatic settlement in local currency.
- claim: eba
  url: https://www.eba.europa.eu/regulation-and-policy/asset-referenced-and-e-money-tokens-mica
  date: undated
  quote: Issuers of asset-referenced tokens (ARTs) and electronic money tokens (EMTs) are required to hold the relevant authorisation
```

### ed096
```yaml
status: ok
section: Tech and infra
title: When can we realistically expect to solve them?
note: We set directional analyst milestones for workable improvements, not dates when all customer risk disappears.
t:
  39: BOTTLENECK
  38: WHY THIS TIMELINE
  41: BOTTLENECK
  40: WHY THIS TIMELINE
  7: "FX\\nLIQUIDITY"
  5: Better automated quotes can help soon, but deep liquidity in thin corridors takes longer to build.
  24: "RULES\\nBY MARKET"
  22: Clearer rules help product teams, while cross-border legal alignment remains slow and uneven.
  42: '2029'
  46: '2032'
  11: "LOCAL\\nCASH OUT"
  9: New payout partners can add coverage, though bank hours and local laws still shape delivery.
  28: "CARD\\nFUNDING"
  26: On-chain credit can ease card funding, but underwriting and network rules take time to mature.
  43: '2029'
  47: '2029'
  15: "BANK\\nACCESS"
  13: More banks may join, but access still needs reviews, licenses, and local partners.
  32: "REFUND\\nROUTES"
  30: Payment firms can build refund reserves and workflows, but transfers will not undo themselves.
  44: '2030'
  48: '2030'
  19: "WALLET\\nSAFETY"
  17: Safer approvals and wallet checks can improve quickly, but loss recovery stays difficult.
  36: "CHAIN\\nSPLITS"
  34: Routing APIs can hide chain choice, although assets and liquidity remain split across networks.
  45: '2028'
  49: '2028'
comment: The years shown are analyst expectations, not promised rollout dates or independently published forecasts.
sources:
- claim: visaerror
  url: https://www.visa.com/en-us/thought-leadership/innovation/financing-stablecoin-linked-card-programs
  date: '2026-09-08'
  quote: Every card program has to fund its daily settlement obligation before it collects from cardholders
- claim: circle26
  url: https://www.circle.com/pressroom/circle-launches-cpn-managed-payments-a-full-stack-platform-for-seamless-stablecoin-settlement
  date: '2026-04-08'
  quote: CPN Managed Payments abstracts digital asset complexity, enabling partners to interact solely in fiat while Circle manages the entire digital asset lifecycle
- claim: bridge
  url: https://bridge.xyz/product/orchestration
  date: undated
  quote: A single API enables you to move USDC, USDT, your own stablecoin, and more across 10+ blockchains.
- claim: meshapr
  url: https://www.meshpay.com/blog/what-were-building-april-2026
  date: '2026-04-18'
  quote: Users can fund with the assets they hold across Tempo, TON, and MegaETH, while SmartFunding handles all bridging behind the scenes.
- claim: mastercard26
  url: https://www.mastercard.com/us/en/news-and-trends/press/2026/june/mastercard-expands-settlement-capabilities-to-include-stablecoin.html
  date: '2026-06-03'
  quote: Mastercard today announced plans to expand its settlement capabilities with additional intraday, weekend and holiday card settlement
- claim: eba
  url: https://www.eba.europa.eu/regulation-and-policy/asset-referenced-and-e-money-tokens-mica
  date: undated
  quote: Issuers of asset-referenced tokens (ARTs) and electronic money tokens (EMTs) are required to hold the relevant authorisation
```

### ed097
```yaml
status: ok
section: Tech and infra
title: Which bold bets could reshape stablecoin payments?
note: We frame bets as conditional product possibilities drawn from current payment APIs, card funding experiments, and pilot services.
t:
  9: GLOBAL CASH OUT
  12: BANKLESS FX PAY
  15: ANY TOKEN CARD
  18: ONE PAY API
  33: "NEAR-TERM HORIZON\n(0-5 YEARS)"
  7: It is one transfer that ends as local money in a bank or mobile wallet in most countries.
  10: It lets customers pay from banks while stablecoins settle the transfer behind the scenes.
  13: It lets cardholders spend stablecoins at checkout without manually selling tokens.
  16: It gives merchants one API for local pay-ins, stablecoin moves, and payouts worldwide.
  21: ALWAYS-ON FX
  24: SAFE AUTO PAY
  27: PRIVATE PAY RAILS
  30: REAL-TIME CARD FUND
  34: "LONG-TERM HORIZON\n(5-10 YEARS)"
  19: It makes local currency conversion available daily with liquid markets and clear prices.
  22: It lets software agents pay small invoices with strict limits, approvals, and clear records.
  25: It hides business details while giving banks the records needed for checks.
  28: It funds card spending continuously without large idle balances at issuer banks.
sources:
- claim: circle26
  url: https://www.circle.com/pressroom/circle-launches-cpn-managed-payments-a-full-stack-platform-for-seamless-stablecoin-settlement
  date: '2026-04-08'
  quote: CPN Managed Payments abstracts digital asset complexity, enabling partners to interact solely in fiat while Circle manages the entire digital asset lifecycle
- claim: rampstripe
  url: https://stripe.com/en-fi/newsroom/news/ramp-and-stripe
  date: '2026-07-21'
  quote: Ramp customers can now pay bills with stablecoin payments funded from an external bank account
- claim: visaerror
  url: https://www.visa.com/en-us/thought-leadership/innovation/financing-stablecoin-linked-card-programs
  date: '2026-09-08'
  quote: Every card program has to fund its daily settlement obligation before it collects from cardholders
- claim: visacards
  url: https://www.visa.com/en-us/thought-leadership/innovation/financing-stablecoin-linked-card-programs
  date: '2026-09-08'
  quote: more than 160 stablecoin-linked card programs were live around the world, payment volume on those programs grew nearly 200% year over year
- claim: meshtempo
  url: https://www.meshpay.com/press-releases/mesh-and-tempo-formalize-partnership-to-advance-stablecoin-payments-at-scale
  date: '2026-05-12'
  quote: The partnership establishes Tempo’s role as a settlement network within the Mesh ecosystem
```

### ed098
```yaml
status: ok
section: Tech and infra
title: Which companies are working on groundbreaking tech today?
t:
  8: BRIDGE
  6: Bridge offers APIs to receive, convert, send, and cash out stablecoins via fiat rails.
  24: YELLOW CARD
  22: Yellow Card uses stablecoins to settle cross-border transfers into local bank and mobile payouts.
  11: MOONPAY
  9: MoonPay Enterprise uses Iron for bank money, stablecoin payouts, and merchant settlement.
  27: BVNK
  25: BVNK provides embedded wallets and stablecoin settlement for Corpay and other global firms.
  14: ZEROHASH
  12: zerohash lets platforms send compliant stablecoin payouts through a single API call.
  30: TOKU
  28: Toku runs payroll checks and sends employee and contractor pay in stablecoins.
  17: MESH
  15: Mesh links wallets, stablecoins, local ramps, and merchant checkout in one network.
  33: CONDUIT
  31: Conduit routes stablecoins into local currency and supplier payouts through one API.
note: We select payment-first businesses with a documented working way to send, receive, convert, settle, or spend stablecoins.
sources:
- claim: bridge
  url: https://bridge.xyz/product/orchestration
  date: undated
  quote: A single API enables you to move USDC, USDT, your own stablecoin, and more across 10+ blockchains.
- claim: bvnk
  url: https://www.bvnk.com/press/corpay-partners-with-bvnk-to-add-stablecoin-wallets-for-global-customers
  date: '2026-05-11'
  quote: The integration will enable Corpay’s customers to see a stablecoin balance alongside their fiat balances
- claim: moonpay
  url: https://www.moonpay.com/nl/newsroom/moonpayenterprise
  date: '2026-08-06'
  quote: MoonPay Enterprise is built on Iron, the API-first stablecoin infrastructure platform MoonPay acquired in March 2025.
- claim: yellow
  url: https://yellowcard.io/api
  date: undated
  quote: Collect and pay out local currency across emerging markets through one API.
- claim: zerohash
  url: https://docs.zerohash.com/docs/eu-single-api-call-payouts-api
  date: undated
  quote: The Single API Call Payouts API lets platforms initiate a compliant stablecoin (or crypto) payout in a single API call.
- claim: toku
  url: https://www.toku.com/stablecoin-payroll/usdt
  date: '2026-11-12'
  quote: Toku runs payroll and pays employees and contractors in USDT on Ethereum, Polygon, Base, Avalanche, Tron, BNB Chain
- claim: mesh
  url: https://www.meshpay.com/
  date: undated
  quote: Businesses use one integration for crypto and stablecoin payments, deposits, payouts, on- and off-ramps and wallet verification.
- claim: conduit
  url: https://conduitpay.com/send
  date: undated
  quote: Our global network uses stablecoins to power faster, cheaper international fiat to fiat transfers.
```

### iv_pipeline
```yaml
status: ok
section: Tech and infra
title: Which banks and payment giants are launching stablecoin services?
note: We list announced stablecoin payment services and label a plan or pilot distinctly from a service in use.
t:
  38: LIVE
  34: Visa lets banks settle their card network dues in USDC onchain.
  37: VISA · USDC SETTLE
  27: PILOT
  26: MASTERCARD · USDC
  24: Mastercard adds regulated stablecoin settlement for card partners.
  23: LIVE
  22: PAYPAL · PAY WITH CRYPTO
  20: Merchants can accept crypto, then get local fiat settlement.
  19: LIVE
  18: CIRCLE · CPN
  16: CPN Managed Payments settles transfers using stablecoins.
  15: LIVE
  12: Stripe lets firms send and receive stablecoins in accounts.
  14: STRIPE · TREASURY
  11: LIVE
  10: WESTERN UNION · STABLECARD
  8: Stablecard lets customers store USDPT and spend with Visa.
  7: LIVE
  6: RAMP · BILL PAY
  4: Ramp bills can be funded by banks and sent as stablecoins.
  3: LIVE
  2: MOONPAY · ENTERPRISE
  0: MoonPay Enterprise lets firms convert and pay in stablecoins.
sources:
- claim: visaus
  url: https://corporate.visa.com/en/sites/visa-perspectives/press-releases/visa-launches-stablecoin-settlement-in-the-united-states.html
  date: '2025-12-16'
  quote: Initial banking participants include Cross River Bank and Lead Bank, which have started settling with Visa in USDC over the Solana blockchain.
- claim: mastercard26
  url: https://www.mastercard.com/us/en/news-and-trends/press/2026/june/mastercard-expands-settlement-capabilities-to-include-stablecoin.html
  date: '2026-06-03'
  quote: Mastercard today announced plans to expand its settlement capabilities with additional intraday, weekend and holiday card settlement
- claim: paypal26
  url: https://developer.paypal.com/crypto/
  date: '2026-08-11'
  quote: accept cryptocurrency (crypto) payments from global buyers and receive automatic settlement in local currency.
- claim: circle26
  url: https://www.circle.com/pressroom/circle-launches-cpn-managed-payments-a-full-stack-platform-for-seamless-stablecoin-settlement
  date: '2026-04-08'
  quote: CPN Managed Payments abstracts digital asset complexity, enabling partners to interact solely in fiat while Circle manages the entire digital asset lifecycle
- claim: stripetreas
  url: https://stripe.com/blog/introducing-stablecoins-for-treasury
  date: '2025-05-20'
  quote: Send and receive stablecoins globally across eight blockchain networks
- claim: westerncard
  url: https://ir.westernunion.com/news/archived-press-releases/press-release-details/2026/Western-Union-Launches-Stablecard-in-Partnership-with-Rain/default.aspx
  date: '2026-08-04'
  quote: Stablecard offers a consumer-friendly way to receive funds and store value in USDPT
- claim: rampstripe
  url: https://stripe.com/en-fi/newsroom/news/ramp-and-stripe
  date: '2026-07-21'
  quote: Ramp customers can now pay bills with stablecoin payments funded from an external bank account
- claim: moonpay
  url: https://www.moonpay.com/nl/newsroom/moonpayenterprise
  date: '2026-08-06'
  quote: MoonPay Enterprise is built on Iron, the API-first stablecoin infrastructure platform MoonPay acquired in March 2025.
```

