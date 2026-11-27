# Quantum sensing: extra-slide signals (research of 2026-11-27)

12 candidates kept, ranked by total score (surprise + importance + clarity + durability, max 20).
Every candidate passed its format's "keep only if" check, and every number was checked against its quote.

| # | Format | Title | Chapter | Score | Fresh |
|---|---|---|---|---|---|
| 1 | incident-count | Poland logged 13,043 GNSS interference events in 2025, up from 64 in 2023 | Pain points | 18 | year 2025-12 |
| 2 | key-trend | Russian GPS spoofing antennas in Kaliningrad jumped from 3 to 36 | Market opportunity | 18 | total 2026-05 |
| 3 | icon-grid | Only 10% of 2025 quantum startup money went to sensing and comms | Investor bets | 16 | year 2025-12 |
| 4 | single-customer | The US government paid for about 80% of Infleqtion's recent revenue | Startup killers | 16 | quarter 2026-06 |
| 5 | key-trend | Infleqtion's backlog jumped from $22.5M to $51.2M in a single quarter | Market opportunity | 15 | quarter 2026-09 |
| 6 | profit-gap | Infleqtion lost $3.79 per $1 of sales last quarter, up from $0.92 | Value creation | 15 | quarter 2026-09 |
| 7 | deal-timeline | Thales bids $4.45B for Exail as quantum sensing deals pile up | Market opportunity | 15 | total 2026-07 |
| 8 | key-trend | Airliners now lose GPS 57.1 times per 1,000 flights, up from 30.9 | Pain points | 15 | year 2025-12 |
| 9 | icon-grid | GNSS interference hit 27.4% of flights over the Baltic region in one month | Pain points | 14 | month 2025-04 |
| 10 | multiple-gap | Infleqtion is valued at 43.9x sales; Thales pays 4.8x for Exail | Value creation | 13 | total 2026-11 |
| 11 | kpi-trio | Infleqtion: revenue up 57%, backlog $51.2M, 2026 sales of at least $45.1M | Market opportunity | 13 | quarter 2026-09 |
| 12 | deal-timeline | The Pentagon put up to $200M behind quantum sensing in one program | Market opportunity | 13 | total 2026-11 |

Market opportunity count: 5 candidates pass the freshness rule (#2, #5, #7, #11, #12), short of the 6 to 8 target. The strongest fresh funding fact we found, Q-CTRL's $290M Series C of November 2026 (valued above $1B), belongs to your own funding database, so we did not turn it into a slide here.

---

## 1. incident-count

```yaml
format: incident-count
title: Poland logged 13,043 GNSS interference events in 2025, up from 64 in 2023
chapter: Pain points
why_it_matters: Polish air traffic control went from a few dozen GPS interference events a year to thousands, about 200 times more in two years. That is the daily pain quantum navigation sells against, aircraft that cannot trust satellite positioning.
fresh: {period: year, end: 2025-12}
data:
  - {label: "2022", value: 20, unit: "GNSS interference events, FIR Warszawa", date: 2022}
  - {label: "2023", value: 64, unit: "GNSS interference events, FIR Warszawa", date: 2023}
  - {label: "2024", value: 6652, unit: "GNSS interference events, FIR Warszawa", date: 2024}
  - {label: "2025 (see note)", value: 13043, unit: "GNSS interference events, FIR Warszawa", date: 2025}
note: We use the yearly count of GNSS interference events in the Warsaw flight information region recorded by the Polish air navigation agency (PAZP), as given by Poland's Ministry of Infrastructure in its reply to parliamentary question no. 12112 (filed 10 September 2025). The reply is undated, so the 2025 bar may be a year-to-date figure; mark it as partial on the slide if in doubt. Latvia and Sweden logged slightly fewer reports in early 2026 than a year before, but both regulators say levels stay high.
scores: {surprise: 5, importance: 4, clarity: 5, durability: 4}
sources:
  - {claim: "Yearly GNSS interference events in FIR Warszawa: 20 (2022), 64 (2023), 6,652 (2024), 13,043 (2025)", url: "https://api.sejm.gov.pl/sejm/term10/interpellations/attachment/ATTDPLJUU/i12112-o1.pdf", date: "reply to interpellation of 2025-09-10 (undated)", quote: "liczba zdarzeń związanych z zakłóceniami GNSS w przestrzeni powietrznej FIR Warszawa przedstawia się następująco"}
```

## 2. key-trend

```yaml
format: key-trend
title: Russian GPS spoofing antennas in Kaliningrad jumped from 3 to 36
chapter: Market opportunity
why_it_matters: The threat that GPS-free quantum navigation answers is scaling fast, with Russia's spoofing antennas multiplied by 12 in about 16 months. Each antenna can feed fake positions to planes, ships and drones far into Europe.
fresh: {period: total, end: 2026-05}
data:
  - {label: "Early 2025", value: 3, unit: "GPS spoofing antennas on the Kaliningrad border", date: 2025-01}
  - {label: "May 2026", value: 36, unit: "GPS spoofing antennas on the Kaliningrad border", date: 2026-05}
note: We use the count given by Darius Kuliesius, deputy head of Lithuania's communications regulator, to Reuters on 26 May 2026. A separate EU Council document counts "interference sources" in Kaliningrad (5 in March 2025, 31 in October 2025), a different measure that we keep off the chart.
scores: {surprise: 5, importance: 4, clarity: 5, durability: 4}
sources:
  - {claim: "Spoofing antennas rose from 3 in early 2025 to 36 (Reuters interview with Lithuania's regulator)", url: "https://www.thestar.com.my/news/world/2026/05/26/russia-can-falsify-gps-signals-deep-into-europe-lithuania-says", date: 2026-05-26, quote: "from three in early 2025 to 36 now."}
  - {claim: "The antennas sit on the border of the Kaliningrad exclave", url: "https://theins.press/en/news/293080", date: 2026-05, quote: "only three antennas on the border of the Russian exclave"}
```

## 3. icon-grid

```yaml
format: icon-grid
title: Only 10% of 2025 quantum startup money went to sensing and comms
chapter: Investor bets
why_it_matters: Quantum sensing is the poor cousin of the quantum boom, as computing took 9 of every 10 startup dollars in 2025. Sensing founders compete for a thin slice of capital even though their products already sell.
fresh: {period: year, end: 2025-12}
data:
  - {label: "Quantum computing startups", value: 90, unit: "% of 2025 quantum startup investment", date: 2025}
  - {label: "Quantum sensing and quantum communication startups", value: 10, unit: "% of 2025 quantum startup investment", date: 2025}
note: We use McKinsey's Quantum Technology Monitor 2026 (published April 2026, data to March 2026), which splits 2025 investment in quantum technology startups by subsector. Sensing and communication are reported together, so the 10% is an upper bound for sensing alone. Grid of 100 icons, 10 colored.
scores: {surprise: 4, importance: 4, clarity: 5, durability: 3}
sources:
  - {claim: "90% of 2025 quantum startup investment went to computing, 10% to sensing and communication", url: "https://www.mckinsey.com/capabilities/mckinsey-technology/our-insights/mckinsey-quantum-technology-monitor-2026-a-commercial-tipping-point", date: 2026-04-28, quote: "the remaining 10 percent flowing to the two other quantum technology subsectors"}
```

## 4. single-customer

```yaml
format: single-customer
title: The US government paid for about 80% of Infleqtion's recent revenue
chapter: Startup killers
why_it_matters: Infleqtion, the first listed quantum sensing leader, depends on one customer for most of its sales. A budget delay or a lost US program would hit its revenue far harder than at a diversified sensor maker.
fresh: {period: quarter, end: 2026-06}
data:
  - {label: "Full year 2025", value: 60, unit: "% of revenue from the US government", date: 2025}
  - {label: "Q2 2026", value: 80, unit: "% of revenue from the US government and agencies", date: 2026-06}
note: We use Infleqtion's 10-K for fiscal 2025 (US government as prime or subcontractor, about 60%, plus about 12% from the UK government) and the share given with Q2 2026 results (about 80%). Sensing is about two thirds of Infleqtion's revenue; the US government counts as one customer across agencies, as in the filing.
scores: {surprise: 3, importance: 4, clarity: 5, durability: 4}
sources:
  - {claim: "US government about 60% of fiscal 2025 revenue (10-K excerpt)", url: "https://policyrisk.com/world/company/INFQ", date: 2026-03, quote: "represented approximately 60% of our revenue"}
  - {claim: "About 80% of Q2 2026 revenue came from the US government and agencies", url: "https://www.zacks.com/stock/news/2974198/", date: 2026-08, quote: "Around 80% of revenues came from the U.S. government and agencies"}
```

## 5. key-trend

```yaml
format: key-trend
title: Infleqtion's backlog jumped from $22.5M to $51.2M in a single quarter
chapter: Market opportunity
why_it_matters: Signed orders are arriving faster than revenue, as Infleqtion's contracted backlog more than doubled in three months. About $36.1M of it is due for delivery in 2027, which locks in next year's growth.
fresh: {period: quarter, end: 2026-09}
data:
  - {label: "30 June 2026", value: "$22.5M", unit: "USD, remaining performance obligations", date: 2026-06-30}
  - {label: "30 September 2026", value: "$51.2M", unit: "USD, remaining performance obligations", date: 2026-09-30}
note: "We use remaining performance obligations (signed, non-cancelable contracts not yet delivered): the June figure is the sum of the four delivery buckets in Infleqtion's Q2 2026 10-Q ($8.9M + $12.5M + $0.2M + $0.9M); the September figure is from the Q3 2026 results (17 November 2026 week). Press coverage of Q2 quoted $21M, close to our sum."
scores: {surprise: 4, importance: 3, clarity: 5, durability: 3}
sources:
  - {claim: "RPO buckets at 30 June 2026 summing to $22.5M", url: "https://www.sec.gov/Archives/edgar/data/0002007825/000162828026057508/infq-20260630.htm", date: 2026-08-17, quote: "$ 8.9million , $ 12.5 million, $ 0.2million, and $ 0.9 million from remaining performance obligations"}
  - {claim: "RPO of $51.2M at end of Q3 2026, $36.1M due next year", url: "https://finimize.com/content/wedbush-sees-infleqtion-rebounding-after-a-q3-miss", date: 2026-11, quote: "$51.2 million, with $36.1 million slated for delivery next year."}
```

## 6. profit-gap

```yaml
format: profit-gap
title: Infleqtion lost $3.79 per $1 of sales last quarter, up from $0.92
chapter: Value creation
why_it_matters: Quantum sensing still costs far more to deliver than it earns, and Infleqtion's quarterly loss now runs at almost four times its sales. Its gross margin even turned negative in the quarter, so new contracts add cost before profit.
fresh: {period: quarter, end: 2026-09}
data:
  - {label: "Q3 2025", value: -0.92, unit: "USD of GAAP operating result per $1 of revenue", date: 2025-09}
  - {label: "Q3 2026", value: -3.79, unit: "USD of GAAP operating result per $1 of revenue", date: 2026-09}
note: "We divide GAAP operating loss by revenue: Q3 2026, $34.5M loss on $9.1M; Q3 2025, $6.7M loss on about $7.3M (derived from the reported 25.1% growth). For the full year 2025 the ratio was -$1.09 ($35.3M loss on $32.5M). Q3 2026 gross margin was about -12%."
scores: {surprise: 4, importance: 4, clarity: 4, durability: 3}
sources:
  - {claim: "Q3 2026 GAAP operating loss $34.5M vs $6.7M a year earlier", url: "https://www.dailypolitical.com/?p=10586796", date: 2026-11, quote: "operating loss of $34.5 million for the third quarter, compared with $6.7 million"}
  - {claim: "Q3 2026 revenue $9.1M, up 25.1% year on year", url: "https://finsee.ai/earnings/infq/2026/q3/en/", date: 2026-11, quote: "Infleqtion reported $9.1 million in third-quarter sales, up 25.1% from a year ago"}
```

## 7. deal-timeline

```yaml
format: deal-timeline
title: Thales bids $4.45B for Exail as quantum sensing deals pile up
chapter: Market opportunity
why_it_matters: Big buyers are paying up for quantum sensing assets, with four deals in nine months. Thales outbid Safran for Exail, maker of cold-atom gravimeters and navigation systems, and named quantum sensors as one reason for the deal.
fresh: {period: total, end: 2026-07}
data:
  - {label: "IonQ completes all-stock purchase of Vector Atomic (atomic clocks, quantum inertial sensors)", value: "undisclosed", unit: "USD", date: 2025-10-07}
  - {label: "Infleqtion lists on the NYSE via SPAC, gross proceeds", value: "$550M", unit: "USD", date: 2026-02-17}
  - {label: "Quantum Design acquires Qnami (NV-diamond quantum sensing)", value: "undisclosed", unit: "USD", date: 2026-06-04}
  - {label: "Thales agrees to buy Exail, enterprise value (EUR 3.9B)", value: "$4.45B", unit: "USD", date: 2026-07-06}
note: We list completed or signed deals involving companies whose core offer is quantum sensing, from company releases and Reuters, October 2025 to July 2026. Exail is a diversified incumbent (NOT A STARTUP; drones and navigation are most of its sales); the Thales offer is EUR 134 per share and closing is expected in 2027.
scores: {surprise: 3, importance: 4, clarity: 4, durability: 4}
sources:
  - {claim: "IonQ completed the Vector Atomic acquisition (7 October 2025)", url: "https://www.hpcwire.com/off-the-wire/ionq-completes-acquisition-of-vector-atomic/", date: 2025-10-07, quote: "IonQ today announced the successful completion of its acquisition of Vector Atomic"}
  - {claim: "Infleqtion began NYSE trading on 17 February 2026", url: "https://infleqtion.com/?p=4025", date: 2026-02-17, quote: "began trading on February 17, 2026, following a business combination with Churchill Capital Corp X"}
  - {claim: "Listing brought over $550M of gross proceeds", url: "https://infleqtion.com/?p=3460", date: 2026-02-17, quote: "Infleqtion receiving over $550 million of gross proceeds"}
  - {claim: "Quantum Design acquired Qnami", url: "https://thequantuminsider.com/2026/06/04/quantum-design-acquires-quantum-sensing-company-qnami/", date: 2026-06-04, quote: "Quantum Design has acquired quantum sensing company Qnami"}
  - {claim: "Thales deal gives Exail an EV of EUR 3.9B ($4.45B)", url: "https://live.euronext.com/en/financial-news/thales-expands-fast-growing-sea-drone-warfare-market-exail-deal", date: 2026-07-06, quote: "gives Exail an enterprise value of €3.9 billion ($4.45 billion)."}
  - {claim: "Thales cites quantum sensors as a deal rationale", url: "https://optics.org/news/exail-poised-for-thales-takeover", date: 2026-07-13, quote: "accelerate their development in the field of quantum sensors"}
```

## 8. key-trend

```yaml
format: key-trend
title: Airliners now lose GPS 57.1 times per 1,000 flights, up from 30.9
chapter: Pain points
why_it_matters: GPS loss is now routine for airlines worldwide, not a war-zone oddity, with the rate per flight almost doubled since 2022. Because it is counted per 1,000 flights, the rise is not just more traffic.
fresh: {period: year, end: 2025-12}
data:
  - {label: "2022", value: 30.9, unit: "GPS loss events per 1,000 flights", date: 2022}
  - {label: "2023", value: 39.9, unit: "GPS loss events per 1,000 flights", date: 2023}
  - {label: "2024", value: 56.1, unit: "GPS loss events per 1,000 flights", date: 2024}
  - {label: "2025 (provisional)", value: 57.1, unit: "GPS loss events per 1,000 flights", date: 2025}
note: We use IATA's GNSS interference safety risk assessment (version 6, February 2026), based on aircraft-recorded data from about 30.7 million flights in its Flight Data eXchange; the 2025 figure is provisional. The year mapping matches IATA's public statements of 31 in 2022 and 56 in 2024.
scores: {surprise: 3, importance: 4, clarity: 4, durability: 4}
sources:
  - {claim: "IATA GPS loss rate series 28.1, 30.9, 39.9, 56.1, 57.1; 2025 slightly above 2024", url: "https://ic.iata.org/sites/default/files/iata_sih_document_attachment/IATA%20Safety%20Risk%20Assessment%20-%20GNSS%20Interference%20V6.pdf", date: 2026-02, quote: "GPS signal losses per 1000 flights have slightly increased compared to 2024"}
```

## 9. icon-grid

```yaml
format: icon-grid
title: GNSS interference hit 27.4% of flights over the Baltic region in one month
chapter: Pain points
why_it_matters: More than one flight in four over the Baltic region lost reliable satellite signals in a single month. For airlines and armies there, a GPS backup is no longer a nice-to-have.
fresh: {period: month, end: 2025-04}
data:
  - {label: "Flights affected by GNSS interference, Baltic region", value: 27.4, unit: "% of flights", date: 2025-04}
note: We use the joint submission of Sweden, Finland, Estonia, Latvia, Lithuania and Poland to ICAO (reported by SVT in September 2025) for April 2025; some areas exceeded 40%. Grid of 100 planes, 27 colored. The figure is a single month, so it works as a pain point, not as a fresh momentum signal.
scores: {surprise: 4, importance: 3, clarity: 5, durability: 2}
sources:
  - {claim: "27.4% of flights in the region affected in April 2025", url: "https://traveltomorrow.com/russian-gps-interference-disrupts-nearly-123000-flights-in-four-months/", date: 2025-09, quote: "Interference spiked in April alone, affecting 27.4% of flights in the region."}
  - {claim: "Some areas above 40%", url: "https://www.gpsworld.com/?p=111647", date: 2025-09, quote: "some areas experiencing rates above 40%"}
```

## 10. multiple-gap

```yaml
format: multiple-gap
title: Infleqtion is valued at 43.9x sales; Thales pays 4.8x for Exail
chapter: Value creation
why_it_matters: Public investors price quantum pure plays like hyper-growth software, about nine times the multiple Thales agreed to pay for an established navigation maker. That leaves little room for a missed quarter, as Infleqtion's mid-November drop showed.
fresh: {period: total, end: 2026-11}
data:
  - {label: "Infleqtion", value: 43.9, unit: "market value per $1 of trailing 12-month sales", date: 2026-10-27}
  - {label: "IonQ (quantum peer, computing-led)", value: 33.3, unit: "market value per $1 of trailing 12-month sales", date: 2026-11-05}
  - {label: "Exail (Thales offer, navigation incumbent)", value: 4.8, unit: "equity value per 1 of 2025 sales", date: 2026-07-06}
note: "We compute Infleqtion's value as $8.63 (27 Oct 2026) x 225.36M shares = $1.94B, over $44.3M trailing sales (9M 2026 $32.6M + Q4 2025 about $11.7M, derived from 2025 revenue of $32.5M and 57% nine-month growth); after the Q3 miss the stock fell to about $7.38, roughly 37.5x. IonQ: $12.68B market value over $380.4M (9M 2026 $318.55M + Q4 2025 $61.9M), with foundry revenue from SkyWater included. Exail: EUR 2.3B equity value in the Thales deal over EUR 479M 2025 revenue."
scores: {surprise: 4, importance: 3, clarity: 4, durability: 2}
sources:
  - {claim: "Infleqtion share price $8.63 on 27 Oct 2026", url: "https://upstox.com/us-stocks/infq-share-price/", date: 2026-10-27, quote: "As of 27 October 2026, Infleqtion, Inc.'s share price is $8.63."}
  - {claim: "Infleqtion shares outstanding 225.36M", url: "https://stockanalysis.com/stocks/INFQ", date: 2026-11, quote: "Shares Out | 225.36M"}
  - {claim: "Infleqtion 9M 2026 revenue $32.6M, up 57%", url: "https://www.earningswhispers.com/article/INFQ/2611163109", date: 2026-11, quote: "nine-month revenue $32.6 million, up 57% year over year"}
  - {claim: "Infleqtion 2025 revenue $32.5M", url: "https://www.businesswire.com/news/home/20260408711212/en/", date: 2026-04-08, quote: "Revenue of $32.5 million."}
  - {claim: "IonQ market value $12.68B at Q3 results", url: "https://stockstory.org/us/stocks/nyse/ionq/news/earnings/ionq-nyseionq-beats-expectations-in-strong-q3-2026-guides-for-strong-full-year-sales", date: 2026-11-05, quote: "Market capitalization $12.68 billion"}
  - {claim: "IonQ 9M 2026 revenue $318.55M vs $68.13M in 9M 2025", url: "https://quantumcomputingreport.com/ionq-announces-record-q3-2026-revenues-of-173-8m-and-raises-fy-2026-guidance-to-over-505m-as-backlog-reaches-1-2b/amp/", date: 2026-11-05, quote: "| Revenue | $173.83 | $39.87 | +336.0% | $318.55 | $68.13 | +367.6% |"}
  - {claim: "IonQ 2025 revenue $130M", url: "https://sqmagazine.co.uk/quantum-computing-statistics/", date: 2026, quote: "reaching $130 million in 2025"}
  - {claim: "Thales deal: Exail equity value EUR 2.3B", url: "https://quartr.com/events/thales-s-a-ho-m-a-announcement_3sfPA3SM", date: 2026-07-06, quote: "Enterprise value of €3.9 billion, equity value of €2.3 billion"}
  - {claim: "Exail 2025 revenue EUR 479M", url: "https://live.euronext.com/en/products/equities/company-news/2026-02-18-activity-4th-quarter-2025-revenue-growth-26", date: 2026-02-18, quote: "| Consolidated revenue | 153 | 122 | +32 | +26% | 479 | 373 | +105 | +28% |"}
```

## 11. kpi-trio

```yaml
format: kpi-trio
title: "Infleqtion: revenue up 57%, backlog $51.2M, 2026 sales of at least $45.1M"
chapter: Market opportunity
why_it_matters: The first listed quantum sensing leader is still growing fast, with nine-month revenue up 57% and a backlog that doubled in a quarter. If it meets guidance, 2026 sales should land about 39% above 2025.
fresh: {period: quarter, end: 2026-09}
data:
  - {label: "Revenue, first nine months of 2026 (up 57% year on year)", value: "$32.6M", unit: "USD", date: 2026-09-30}
  - {label: "Contracted backlog (remaining performance obligations)", value: "$51.2M", unit: "USD", date: 2026-09-30}
  - {label: "2026 revenue guidance, at least (2025: $32.5M)", value: "$45.1M", unit: "USD", date: 2026-11}
note: "We use Infleqtion's Q3 2026 results (November 2026); about two thirds of its revenue is quantum sensing and timing. The 39% is our arithmetic: $45.1M guidance over $32.5M 2025 revenue. Overlaps with candidate 5: keep one of the two."
scores: {surprise: 3, importance: 3, clarity: 4, durability: 3}
sources:
  - {claim: "9M 2026 revenue $32.6M, up 57%", url: "https://www.earningswhispers.com/article/INFQ/2611163109", date: 2026-11, quote: "nine-month revenue $32.6 million, up 57% year over year"}
  - {claim: "RPO $51.2M at end of Q3 2026", url: "https://finimize.com/content/wedbush-sees-infleqtion-rebounding-after-a-q3-miss", date: 2026-11, quote: "$51.2 million, with $36.1 million slated for delivery next year."}
  - {claim: "2026 guidance at least $45.1M maintained", url: "https://www.webull.com/news/15935490803090432", date: 2026-11, quote: "revenue outlook of at least $45.1 million."}
  - {claim: "2025 revenue $32.5M", url: "https://www.businesswire.com/news/home/20260408711212/en/", date: 2026-04-08, quote: "Revenue of $32.5 million."}
```

## 12. deal-timeline

```yaml
format: deal-timeline
title: The Pentagon put up to $200M behind quantum sensing in one program
chapter: Market opportunity
why_it_matters: Defense buyers have moved from studies to money, with a program worth up to $200M and a GPS-free test flight of over four hours. Startups now have funded paths from prototype to fielded product.
fresh: {period: total, end: 2026-11}
data:
  - {label: "DARPA RoQS awards to Q-CTRL for quantum navigation sensors", value: "$24.4M", unit: "USD", date: 2025-08-27}
  - {label: "DIU launches Farseer quantum sensing and timing program (up to)", value: "$200M", unit: "USD", date: 2026-06-23}
  - {label: "DIU and Honeywell fly an Embraer 170 on quantum magnetic navigation, no GPS", value: 263, unit: "minutes of flight", date: 2026-09}
  - {label: "NASA expands Infleqtion's quantum gravity sensing contract", value: "$20M", unit: "USD", date: 2026-11}
note: We list dated US government awards and tests from DARPA, the Defense Innovation Unit, Honeywell and Infleqtion releases, August 2025 to November 2026. Farseer followed Executive Order 14411 of 22 June 2026; the 263 minutes are the 4 h 23 min flight. Weakest of the 12 on clarity, since the items are of different kinds.
scores: {surprise: 3, importance: 4, clarity: 3, durability: 3}
sources:
  - {claim: "DARPA RoQS awards to Q-CTRL worth $24.4M", url: "https://insidehpc.com/2025/08/darpa-selects-q-ctrl-for-quantum-sensors/", date: 2025-08-27, quote: "won two awards under DARPA’s Robust Quantum Sensors (RoQS) program valued at A$38M (US$24.4M)"}
  - {claim: "DIU Farseer to invest up to $200M within a year", url: "https://www.quantum.gov/?p=6944", date: 2026-06-23, quote: "expected to invest up to $200M within the next year"}
  - {claim: "GPS-free quantum navigation flight of 4 h 23 min", url: "https://leehamnews.com/2026/09/09/honeywell-tests-magnetic-navigation-in-gps-free-flight/", date: 2026-09-09, quote: "flew over the Pacific Ocean for 4 hours 23 minutes without GPS."}
  - {claim: "NASA $20M expansion contract to Infleqtion", url: "https://quantumzeitgeist.com/?p=370953", date: 2026-11, quote: "a $20 million expansion contract with NASA"}
```

---

## Formats tried and dropped

- **forecast-gap**: ten 2030 forecasts found (BCC $726.7M, Global Industry Analysts $728.9M, P&S $889.4M, Polaris $894.1M, McKinsey about $1B, The Business Research Company $1.28B, GMI $1.37B, Mordor $1.39B, 360iResearch $1.73B, BCG $3B to $5B). Without the BCG extreme the spread is 2.4x, under the 3x bar.
- **fallen-star**: Infleqtion (the only listed pure play) peaked at $21.28 in 2026 and trades near $7.4, about 65% below peak, under the 80% bar.
- **incident-count via Sweden**: dropped; press figures for 2025 conflict (733 reports by August vs "roughly 336" for the year).
- **incumbent-crash, challenger, dominance**: no listed incumbent fell 50% on a quantum event; no share series exists.
- **value-ladder**: only three verified $1B+ values (Exail EUR 3.9B EV, Infleqtion about $1.7B to $1.9B, Q-CTRL above $1B); SandboxAQ's last verifiable valuation ($5.75B) is from April 2025 and its reported 2026 round could not be confirmed from a primary source.
- **lobbying-spend**: Infleqtion disclosed $110k for Q2 2026; no full LD-2 series retrieved and the amount is not striking.
- **earnings-mentions**: no FactSet or IoT Analytics series for quantum sensing.
- **country-gap**: no same-measure, same-year sensing data across countries (national GNSS counts use different reporting rules).
- **contract-share**: DIU TQS and DARPA RoQS award amounts are mostly undisclosed.
- **revenue-per-head**: Infleqtion headcount sources disagree (about 205 in data feeds vs 251 to 1,000 in SAM).
- **waiting-line, idle-capacity, announced-vs-built, promise-tracker, cost-threshold, penetration-curve, adoption-race, dollar-split, rules-wave**: no sourced case found that meets the bar (OPM-MEG brain scanners: no published install or waitlist counts).
- **real-world-vs-funding, funding-event**: need your funding database; the GNSS series above (candidates 1 and 8) can serve as the real-world line.
