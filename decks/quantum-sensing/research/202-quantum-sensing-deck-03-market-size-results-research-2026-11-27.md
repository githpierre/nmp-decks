# Quantum sensing, deck 03, Market size (research results, 27 November 2026)

### ed041
```yaml
status: ok
section: Market size
title: What counts as quantum sensing, and what doesn’t?
note: We count independent companies whose main product is a sensor, clock or detector built on quantum effects, and keep large diversified makers outside the core figure.
t:
  7: "We define quantum sensing as sensors, clocks and detectors that use atoms, light particles or diamond defects to measure the world far more precisely"
  8: "We include atomic clocks, cold-atom gravity and motion sensors, diamond and atom magnetometers, atom radio receivers and photon counters"
  9: "We exclude ordinary gyros and radar, quantum computers, quantum encryption, generic lasers or diamonds, and giants where sensing is small"
sources:
  - claim: Quantum sensing measures quantities such as gravity and electromagnetic fields with greater sensitivity than classical sensors
    url: https://www.mckinsey.com/capabilities/mckinsey-digital/our-insights/tech-forward/quantum-technology-investment-hits-a-magic-moment
    date: "2025-06"
    quote: "Finally, quantum sensing (QS) measures elements such as gravity and electromagnetic fields with greater sensitivity than classical versions."
  - claim: The quantum sensing technology base spans Rydberg atoms, photons, neutral atoms and solid-state spins
    url: https://quantumconsortium.org/publication/2026-market-forecast-quantum-sensing/
    date: "2026-04"
    quote: "Rydberg atoms are most prevalent, followed by photons, neutral atoms and solid-state spins."
```

### ed042
```yaml
status: ok
section: Market size
title: What are the market size estimates from different sources online?
rows:
- firm: "QED-C"
  value: "$ 625 M"
  comment: "Their 2026 figure comes from a survey of 47 quantum sensing companies, very close to our scope. We use it as our main anchor."
- firm: "Fortune Business\n\nInsights"
  value: "$ 502 M"
  comment: "Their scope mixes atomic clocks with farm light meters that are not quantum. It is the lowest figure, so we use it as the low case."
- firm: "Global Market\n\nInsights"
  value: "$ 796 M"
  comment: "Their figure covers all quantum sensors, with incumbent Microchip alone above 22%. We use it after removing that large incumbent."
- firm: "Mordor\n\nIntelligence"
  value: "$ 860 M"
  comment: "Their figure counts incumbents and every sensor type, so it is the highest. We use it only as an upper bound for 2026."
note:
- We take each 2026 estimate from the firm's own page and compare its scope with our definition
- We prefer survey-based counts of real sales and treat broad sensor reports as upper bounds
sources:
  - claim: QED-C estimates the quantum sensing market at $625M in 2026 (chart labels for 2025 to 2028)
    url: https://quantumconsortium.org/mp-files/quantum-sensing-market-forecast-2026_1.pdf/
    date: "2026-04"
    quote: "2025 2026 2027 2028 $470M $625M $831M $1,106M"
  - claim: QED-C's forecast is based on 58 participants from 47 companies
    url: https://quantumconsortium.org/publication/2026-market-forecast-quantum-sensing/
    date: "2026-04"
    quote: "Based on responses from 58 participants representing 47 distinct companies"
  - claim: Fortune Business Insights puts the 2026 quantum sensors market at $502.3M
    url: https://fortunebusinessinsights.com/quantum-sensors-market-110331
    date: "2026-01-19"
    quote: "is projected to grow from USD 502.3 million in 2026 to USD 1,543.60 million by 2034"
  - claim: Fortune's scope includes photosynthetically active radiation (PAR) sensors used in farming
    url: https://www.fortunebusinessinsights.com/segmentation/quantum-sensors-market-110331
    date: "2026-04-20"
    quote: "By Type (Atomic Clocks, Magnetic Sensors, Photosynthetically Active Radiation (PAR) Sensors, Gravity Sensors, and Others)"
  - claim: Global Market Insights puts the 2026 market at $796M
    url: https://www.gminsights.com/industry-analysis/quantum-sensors-market
    date: "2026-11"
    quote: "The quantum sensors market was valued at USD 705 million in 2025, is estimated to reach USD 796 million in 2026"
  - claim: Microchip Technology / Microsemi led GMI's market with over 22% share in 2025
    url: https://www.gminsights.com/industry-analysis/quantum-sensors-market
    date: "2026-11"
    quote: "Market Leader: Microchip Technology / Microsemi led with over 22% market share in 2025."
  - claim: Mordor Intelligence puts the 2026 market at $860M
    url: https://www.mordorintelligence.com/industry-reports/quantum-sensors-market
    date: "2026"
    quote: "expected to grow from USD 0.76 billion in 2025 to USD 0.86 billion in 2026."
```

### ed043
```yaml
status: ok
section: Market size
title: Our own first-principles, bottom-up calculation of the market size
page: 1/2
note: We triangulate current estimates, strip out funding and buyouts, and use broad sensor reports that include large incumbents only as a cross-check.
t:
  21: "We explain our estimate using only figures we can trace and check"
  16: "We begin from 2026 sales of companies whose main product is a quantum sensor"
  15: "We count clocks, navigation, magnetic, gravity, RF and photon sensors"
  14: "We exclude quantum computers, encryption links and generic components"
  9: "We exclude funding rounds and buyouts because they are investment, not sales"
  8: "We keep 2026, the current year with fresh figures from each source"
  7: "We start with Fortune at $502 million, the narrowest direct estimate"
  6: "We compare QED-C, which puts 2026 at $625 million"
  3: "We treat Mordor's $860 million as a broad upper bound for 2026"
  2: "We check GMI's $796 million, which includes large incumbent makers"
  0: "We check that Microchip alone holds over 22% of GMI's whole market"
sources:
  - claim: Fortune Business Insights 2026 estimate is $502.3M
    url: https://fortunebusinessinsights.com/quantum-sensors-market-110331
    date: "2026-01-19"
    quote: "is projected to grow from USD 502.3 million in 2026 to USD 1,543.60 million by 2034"
  - claim: QED-C 2026 estimate is $625M
    url: https://quantumconsortium.org/mp-files/quantum-sensing-market-forecast-2026_1.pdf/
    date: "2026-04"
    quote: "2025 2026 2027 2028 $470M $625M $831M $1,106M"
  - claim: Mordor Intelligence 2026 estimate is $860M
    url: https://www.mordorintelligence.com/industry-reports/quantum-sensors-market
    date: "2026"
    quote: "expected to grow from USD 0.76 billion in 2025 to USD 0.86 billion in 2026."
  - claim: GMI 2026 estimate is $796M
    url: https://www.gminsights.com/industry-analysis/quantum-sensors-market
    date: "2026-11"
    quote: "The quantum sensors market was valued at USD 705 million in 2025, is estimated to reach USD 796 million in 2026"
  - claim: Microchip holds over 22% of GMI's market
    url: https://www.gminsights.com/industry-analysis/quantum-sensors-market
    date: "2026-11"
    quote: "Market Leader: Microchip Technology / Microsemi led with over 22% market share in 2025."
```

### ed044
```yaml
status: ok
section: Market size
title: Our own first-principles, bottom-up calculation of the market size
page: 2/2
note: We land where the incumbent-adjusted GMI figure meets QED-C's company survey, keeping Fortune as the narrow case and Mordor as the high case.
t:
  21: "We remove incumbent Microchip's 22% share from GMI's $796 million"
  16: "We get about $621 million left for startups and other focused sensor makers"
  15: "We see QED-C's survey figure of $625 million land within $4 million"
  14: "We see The Business Research Company at $630 million, close to both"
  9: "We note estimates differ because some count incumbents and farm light meters"
  8: "We keep Fortune's 2026 figure of $502 million as the narrow case"
  7: "We keep Mordor's $860 million as the high case, under a wider scope"
  6: "We note over a third of firms had no sales in 2025"
  3: "We take the scope-adjusted midpoint, about $625 million for 2026"
  2: "We round to one simple number that stays easy to check and defend"
  0: "We conclude that quantum sensing is worth about $625 million today"
comment: "GMI's 22% for Microchip is a 2025 share applied to its 2026 total. 796 x 0.78 = $621 million."
sources:
  - claim: Microchip holds over 22% of GMI's market and GMI puts 2026 at $796M
    url: https://www.gminsights.com/industry-analysis/quantum-sensors-market
    date: "2026-11"
    quote: "Market Leader: Microchip Technology / Microsemi led with over 22% market share in 2025."
  - claim: QED-C 2026 estimate is $625M
    url: https://quantumconsortium.org/mp-files/quantum-sensing-market-forecast-2026_1.pdf/
    date: "2026-04"
    quote: "2025 2026 2027 2028 $470M $625M $831M $1,106M"
  - claim: The Business Research Company puts quantum sensing and metrology at $630M in 2026
    url: https://www.researchandmarkets.com/reports/6244767/quantum-sensing-metrology-market-report
    date: "2026-06"
    quote: "It will grow from $0.53 billion in 2025 to $0.63 billion in 2026 at a compound annual growth rate (CAGR) of 19%."
  - claim: Some broad reports count PAR light sensors used in farming
    url: https://www.imarcgroup.com/quantum-sensors-market
    date: "2025"
    quote: "Quantum Sensors Market Report by Product (Atomic Clocks, Magnetic Sensors, PAR Quantum Sensors, Gravity Sensors)"
  - claim: More than a third of surveyed firms reported no quantum sensing sales in 2025
    url: https://quantumconsortium.org/publication/2026-market-forecast-quantum-sensing/
    date: "2026-04"
    quote: "The market nevertheless remains early stage, with more than one-third of respondents reporting no quantum sensing sales in 2025."
  - claim: Mordor's 2026 estimate is $860M
    url: https://www.mordorintelligence.com/industry-reports/quantum-sensors-market
    date: "2026"
    quote: "expected to grow from USD 0.76 billion in 2025 to USD 0.86 billion in 2026."
```

### ed045
```yaml
status: ok
section: Market size
title: How much is quantum sensing worth today?
t:
  6: "$625M"
  8: "We estimate $625 million in 2026. Fortune says $502 million, GMI $796 million and Mordor $860 million for wider scopes. QED-C's company survey, at $625 million, is closest to ours."
  4: "2026"
sources:
  - claim: QED-C 2026 estimate is $625M
    url: https://quantumconsortium.org/mp-files/quantum-sensing-market-forecast-2026_1.pdf/
    date: "2026-04"
    quote: "2025 2026 2027 2028 $470M $625M $831M $1,106M"
  - claim: Fortune 2026 estimate is $502.3M
    url: https://fortunebusinessinsights.com/quantum-sensors-market-110331
    date: "2026-01-19"
    quote: "is projected to grow from USD 502.3 million in 2026 to USD 1,543.60 million by 2034"
  - claim: GMI 2026 estimate is $796M
    url: https://www.gminsights.com/industry-analysis/quantum-sensors-market
    date: "2026-11"
    quote: "The quantum sensors market was valued at USD 705 million in 2025, is estimated to reach USD 796 million in 2026"
  - claim: Mordor 2026 estimate is $860M
    url: https://www.mordorintelligence.com/industry-reports/quantum-sensors-market
    date: "2026"
    quote: "expected to grow from USD 0.76 billion in 2025 to USD 0.86 billion in 2026."
```

### ed048
```yaml
status: ok
section: Market size
title: What is behind these categories?
comment: "The first label is our database category Atomic clocks and timing. The second is the short form of Quantum inertial and gravity sensing. The third groups magnetometry and diamond sensing, biomedical, RF and electric-field, optical and photon-counting, and metrology instruments."
t:
  5: "ATOMIC CLOCKS AND TIMING"
  8: "INERTIAL AND GRAVITY"
  10: "MAGNETIC AND OTHERS"
  11: "⏱️"
  4: "Atomic and optical clocks that keep exact time when GPS fails. Together with magnetometers, they anchor sales today"
  12: "🧭"
  7: "Cold-atom sensors that measure motion and gravity, so ships can navigate and miners can see underground"
  9: "Magnetometers for brains, mines and chips, plus Rydberg radio receivers and single-photon detectors"
  15: ""
  17: ""
  18: ""
  19: ""
  14: ""
  16: ""
holes_ok: true
sources:
  - claim: Atomic clocks and magnetometers anchor the application mix
    url: https://quantumconsortium.org/publication/2026-market-forecast-quantum-sensing/
    date: "2026-04"
    quote: "Atomic clocks and magnetometers continue to anchor the application mix"
  - claim: Imaging, photon detectors, inertial sensors and gravimeters add breadth
    url: https://quantumconsortium.org/publication/2026-market-forecast-quantum-sensing/
    date: "2026-04"
    quote: "with quantum imaging, photon detectors, inertial sensors, and gravimeters providing additional breadth."
  - claim: Q-CTRL navigated a ship with a quantum gravimeter
    url: https://www.defenceconnect.com.au/naval/18808-q-ctrl-completes-milestone-maritime-vessel-navigation-without-gps-using-quantum-gravimeter
    date: "2026-08"
    quote: "Q-CTRL performed autonomous gravity mapping and GPS-free quantum-gravimetric navigation, achieving the key metric of one nautical mile positioning accuracy."
  - claim: Atomionics' quantum gravimeter maps underground deposits for miners
    url: https://www.mining-technology.com/?p=718766
    date: "2026-10"
    quote: "Quantum sensing company Atomionics has announced that its exploration technology matched a drilled resource estimate at an active iron ore mine in India"
```

### ed049
```yaml
status: ok
section: Market size
title: Where in the world is quantum sensing money spent?
regions:
  na:
    pct: 45
    text: "North America leads: the US hosts most quantum sensing startups and funds most defense trials. MRFR puts it near 45%."
  eu:
    pct: 30
    text: "Europe comes second, with strong national programs in the UK, France and Germany. MRFR puts it at about 30% of the market."
  apac:
    pct: 20
    text: "Asia-Pacific holds about 20% but grows fastest, led by China, Japan, South Korea and India."
  latam:
    pct: 2
    text: "We estimate Latin America at about 2% of the market, by splitting the remaining 5% with the Middle East and Africa."
  mea:
    pct: 3
    text: "We estimate the Middle East and Africa at about 3%, the same way. Almost no firm in QED-C's sensing survey is based there."
note:
- We use MRFR's shares for North America, Europe and Asia-Pacific, the three largest regions
- We then split the remaining 5% between Latin America and the Middle East and Africa
sources:
  - claim: MRFR puts North America at about 45% and Europe at about 30% of the quantum sensors market
    url: https://www.einpresswire.com/article/929625722?promo=4400
    date: "2026-07-30"
    quote: "North America leads all regions with roughly 45% of global share, Europe follows at approximately 30%"
  - claim: MRFR puts Asia-Pacific at about 20%
    url: https://www.einpresswire.com/article/929625722?promo=4400
    date: "2026-07-30"
    quote: "Asia-Pacific accounts for approximately 20% of global share"
  - claim: 53% of surveyed quantum sensing companies are headquartered in North America, and almost all others in Europe and Asia-Pacific
    url: https://quantumconsortium.org/mp-files/quantum-sensing-market-forecast-2026_1.pdf/
    date: "2026-04"
    quote: "Of the 47 quantum sensing companies surveyed, 53% are headquartered in North America, 26% in Europe,"
  - claim: Asia-Pacific shows the highest growth, led by China, Japan, South Korea and India
    url: https://www.giiresearch.com/report/fbs1954617-quantum-sensors-market-size-share-growth-global.html
    date: "2026"
    quote: "highest CAGR through 2034, driven by rapid industrialization and government-backed quantum initiatives in China, Japan, South Korea, and India."
  - claim: MRFR puts the Middle East and Africa at about 5%
    url: https://www.einpresswire.com/article/929625722?promo=4400
    date: "2026-07-30"
    quote: "currently holding about 5% of the global share"
```

### ed050
```yaml
status: ok
section: Market size
title: What are the growth rate estimates from different sources online?
note: We use survey-based quantum sensing forecasts first, then broader sensor forecasts as a cautious check, because their scope includes mature clock makers.
t:
  24: "FIRM"
  25: "CAGR"
  26: "COMMENTS"
  6: "QED-C"
  5: "≈ 32%\n\nthrough 2028"
  7: "Their survey of company sales sees fast early growth as products reach buyers. We use it as the optimistic end of our range."
  10: "The Business\n\nResearch Company"
  9: "≈ 19%\n\nthrough 2030"
  11: "Their path from $630 million in 2026 to $1.28 billion by 2030 means about 19% a year. We use it to anchor our base case."
  14: "Fortune Business\n\nInsights"
  13: "≈ 15%\n\nthrough 2034"
  15: "Their path from $502 million to $1.5 billion by 2034 means about 15% a year. We treat it as the cautious end of our range."
  18: "Global Market\n\nInsights"
  17: "≈ 13.4%\n\nthrough 2035"
  19: "Their broad forecast covers mature clock makers led by Microchip, above 22% share. We use it only as a floor for slow growth."
sources:
  - claim: QED-C projects 32% average annual growth to $1.1B in 2028
    url: https://quantumconsortium.org/publication/2026-market-forecast-quantum-sensing/
    date: "2026-04"
    quote: "representing average annual growth of 32%."
  - claim: The Business Research Company projects $1.28 billion by 2030 from $630M in 2026
    url: https://quantumzeitgeist.com/business-research-quantum-1-28-billion/
    date: "2026"
    quote: "The global quantum sensing and metrology market is projected to reach $1.28 billion by 2030"
  - claim: Fortune projects $502.3M in 2026 rising to $1,543.6M by 2034
    url: https://fortunebusinessinsights.com/quantum-sensors-market-110331
    date: "2026-01-19"
    quote: "is projected to grow from USD 502.3 million in 2026 to USD 1,543.60 million by 2034"
  - claim: GMI projects a 13.4% CAGR from 2026 to 2035 and names Microchip as leader with over 22%
    url: https://www.gminsights.com/industry-analysis/quantum-sensors-market
    date: "2026-11"
    quote: "is expected to expand at a 13.4% CAGR"
```

### ed051
```yaml
status: ok
section: Market size
title: What is a realistic CAGR for the quantum sensing market?
note: Survey-based forecasts run near 32%, while broad sensor forecasts sit between 13% and 19%. We use 22% as a base case, with 13% and 32% as downside and upside scenarios.
t:
  15: "BEST CASE ≈ 32%"
  17: "≈22%\n\nthrough 2030"
  19: "Startups grow faster than mature clock makers, but defense budgets set the pace. We use 22%, between the 32% survey path and the 13% to 19% broad forecasts."
  16: "WORST CASE ≈ 13%"
sources:
  - claim: QED-C survey path is 32% a year to 2028
    url: https://quantumconsortium.org/publication/2026-market-forecast-quantum-sensing/
    date: "2026-04"
    quote: "representing average annual growth of 32%."
  - claim: Government buyers, led by defense, are projected to be 47% of revenue in 2028
    url: https://quantumconsortium.org/publication/2026-market-forecast-quantum-sensing/
    date: "2026-04"
    quote: "combined government segments (defense and civil) are projected to represent 47% of the quantum sensing market in 2028"
  - claim: GMI's broad forecast is 13.4% a year
    url: https://www.gminsights.com/industry-analysis/quantum-sensors-market
    date: "2026-11"
    quote: "is expected to expand at a 13.4% CAGR"
  - claim: The Business Research Company reports 19% growth from 2025 to 2026
    url: https://www.researchandmarkets.com/reports/6244767/quantum-sensing-metrology-market-report
    date: "2026-06"
    quote: "It will grow from $0.53 billion in 2025 to $0.63 billion in 2026 at a compound annual growth rate (CAGR) of 19%."
```
