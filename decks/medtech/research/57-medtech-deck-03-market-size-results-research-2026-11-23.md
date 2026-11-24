### ed041
```yaml
status: ok
section: Market size
title: What counts as MedTech, and what doesn't?
note: We count human medical devices and clinically purposed software, not drugs, wellness products or office administration.
t:
  7: We define MedTech as devices and clinical software that directly diagnose, monitor or treat human health conditions, from scans to implants and sensors
  8: We include test devices, medical scans, surgical robots, heart implants, pain stimulators and software that reads images or guides care
  9: We exclude drugs, fitness gadgets, appointment and billing apps, virtual care services, and research tools with no patient-facing use
sources:
- claim: The FDA device definition centers on diagnosis and treatment of disease.
  url: https://www.fda.gov/medical-devices/classify-your-medical-device/how-determine-if-your-product-medical-device
  date: undated
  quote: intended for use in the diagnosis of disease or other conditions, or in the cure, mitigation, treatment, or prevention of disease
- claim: Medical software can have an independent clinical purpose without dedicated hardware.
  url: https://www.fda.gov/medical-devices/digital-health-center-excellence/software-medical-device-samd
  date: '2026-11-18'
  quote: software intended to be used for one or more medical purposes that perform these purposes without being part of a hardware medical device.
- claim: The FDA identifies appointment reminders as non-device software.
  url: https://www.fda.gov/medical-devices/device-software-functions-including-mobile-medical-applications/examples-software-functions-are-not-medical-devices
  date: undated
  quote: Generate reminders for scheduled medical appointments or blood donation appointments
- claim: The FDA identifies patient bill payment software as a non-device function.
  url: https://www.fda.gov/medical-devices/device-software-functions-including-mobile-medical-applications/examples-software-functions-are-not-medical-devices
  date: undated
  quote: Help patients track, review and pay medical claims and bills online
- claim: FDA-authorized AI medical devices exist as a regulated clinical software category.
  url: https://www.fda.gov/medical-devices/digital-health-center-excellence/artificial-intelligence-enabled-medical-devices
  date: '2026-11-18'
  quote: The FDA reviews medical devices through an appropriate premarket pathway
```

### ed042
```yaml
status: ok
section: Market size
title: What are the market size estimates from different sources online?
rows:
- firm: 'Diligence

    Insights'
  value: $ 624 B
  comment: Their global device forecast covers hospital supplies, testing and treatment devices. It sits below our own sector-based estimate.
- firm: 'Fortune Business

    Insights'
  value: $ 605 B
  comment: They include tests, imaging, implants and many other device types. Their 2026 figure is below our base, but has clear scope.
- firm: 'Frost &

    Sullivan'
  value: $ 682 B
  comment: Their 2026 global total includes a $4.9B animal-care line. We remove that line and use their detailed sectors as our base.
- firm: 'Precedence

    Research'
  value: $ 720 B
  comment: Their broad global device estimate includes connected and home health technologies. We use it as a high-end cross-check.
note:
- We compare published 2026 device sales forecasts from four researchers and keep their differing definitions visible
- We remove veterinary sales from the detailed forecast and do not count funding or acquisitions as device revenue
sources:
- claim: Diligence Insights forecasts $624B of medical devices sales in 2026.
  url: https://www.marketresearch.com/Diligence-Insights-v4290/Medical-Devices-Size-Share-Trends-44442872/
  date: '2026-03-23'
  quote: $623.86 billion in 2026, and is projected to reach $910.30 billion by 2032
- claim: Fortune Business Insights forecasts $605B of global medical-device sales in 2026.
  url: https://www.fortunebusinessinsights.com/industry-reports/medical-devices-market-100085
  date: '2026-11-02'
  quote: from USD 604.99 billion in 2026 to USD 1032.66 billion by 2034
- claim: Frost & Sullivan forecasts $682B of global medical-device sales in 2026, including animal care.
  url: https://www1.hkexnews.hk/app/sehk/2026/108529/documents/sehk26051101259.pdf
  date: '2026-05-11'
  quote: '| 2026E | 682.3 |'
- claim: Animal care accounts for $4.9B in the Frost & Sullivan 2026 medical-device total.
  url: https://www1.hkexnews.hk/app/sehk/2026/108529/documents/sehk26051101259.pdf
  date: '2026-05-11'
  quote: '| Animal care | 3.6 | 3.8 | 4.0 | 4.2 | 4.4 | 4.6 | 4.9 |'
- claim: Precedence Research estimates the 2026 medical-device market at $720B.
  url: https://www.precedenceresearch.com/medical-devices-market
  date: '2026-09-09'
  quote: The global medical devices market was valued at USD 719.61 billion in 2026
```

### ed043
```yaml
status: ok
section: Market size
title: Our own first-principles, bottom-up calculation of the market size
page: 1/2
note: We use Frost & Sullivan's 2026 manufacturer-price sales forecast by device sector and exclude its animal-care line.
t:
  21: We build from device sales rather than funding or valuations
  16: We use Frost & Sullivan's global device forecast by product line for 2026
  15: We count tests, scans, monitors, surgery, implants and clinical software
  14: We exclude animal care and services that do not supply medical technology
  9: We avoid adding hospital procedure fees to sales of the devices used
  8: We keep the 2026 forecast year so every estimate is compared fairly
  7: We start with Frost & Sullivan's $682B global device forecast for 2026
  6: We remove its $4.9B animal-care sector from the total
  3: We retain the $139B test-device line as the largest named sector
  2: We add $96B in imaging systems and $13B in bedside monitoring gear
  0: We add $65B in vessel procedures and $38B in surgical systems
sources:
- claim: Frost & Sullivan forecasts $682B of global medical-device sales in 2026, including animal care.
  url: https://www1.hkexnews.hk/app/sehk/2026/108529/documents/sehk26051101259.pdf
  date: '2026-05-11'
  quote: '| 2026E | 682.3 |'
- claim: Animal care accounts for $4.9B in the Frost & Sullivan 2026 medical-device total.
  url: https://www1.hkexnews.hk/app/sehk/2026/108529/documents/sehk26051101259.pdf
  date: '2026-05-11'
  quote: '| Animal care | 3.6 | 3.8 | 4.0 | 4.2 | 4.4 | 4.6 | 4.9 |'
- claim: Frost & Sullivan forecasts $139B in 2026 in-vitro diagnostics.
  url: https://www1.hkexnews.hk/app/sehk/2026/108529/documents/sehk26051101259.pdf
  date: '2026-05-11'
  quote: '| 2026E | 139.4 |'
- claim: Frost & Sullivan forecasts $96B in 2026 medical imaging.
  url: https://www1.hkexnews.hk/app/sehk/2026/108529/documents/sehk26051101259.pdf
  date: '2026-05-11'
  quote: '| MI | 63.8 | 70.4 | 73.8 | 83.3 | 87.2 | 91.5 | 96.2 |'
- claim: Frost & Sullivan forecasts $13B in 2026 monitoring and life-support systems.
  url: https://www1.hkexnews.hk/app/sehk/2026/108529/documents/sehk26051101259.pdf
  date: '2026-05-11'
  quote: '| PMLS | 9.7 | 9.9 | 10.4 | 11.2 | 11.9 | 12.3 | 12.8 |'
- claim: Frost & Sullivan forecasts $65B in 2026 minimally invasive intervention.
  url: https://www1.hkexnews.hk/app/sehk/2026/108529/documents/sehk26051101259.pdf
  date: '2026-05-11'
  quote: '| MII | 36.5 | 40.0 | 44.0 | 48.6 | 53.8 | 59.5 | 65.4 |'
- claim: Frost & Sullivan forecasts $38B in 2026 minimally invasive surgery.
  url: https://www1.hkexnews.hk/app/sehk/2026/108529/documents/sehk26051101259.pdf
  date: '2026-05-11'
  quote: '| MIS | 27.7 | 29.8 | 31.5 | 33.4 | 33.8 | 35.5 | 37.5 |'
- claim: Medical software can have an independent clinical purpose without dedicated hardware.
  url: https://www.fda.gov/medical-devices/digital-health-center-excellence/software-medical-device-samd
  date: '2026-11-18'
  quote: software intended to be used for one or more medical purposes that perform these purposes without being part of a hardware medical device.
```

### ed044
```yaml
status: ok
section: Market size
title: Our own first-principles, bottom-up calculation of the market size
page: 2/2
note: We add six human-device sectors, remove animal care and compare our rounded result with other forecasts and EY sales.
t:
  21: We add the $326B other-device sector to complete the market sum
  16: We total six human device sectors to reach about $677B in sales
  15: We confirm $682B less $5B in animal care is about $677B
  14: We compare Fortune's $605B forecast with our device sum
  9: We see Precedence's $720B as a higher view of global device sales
  8: We check Diligence Insights' lower forecast of $624B in 2026
  7: We use EY's reported $650B in 2025 MedTech sales as a reality check
  6: We note EY found $325B in first-half 2026 revenue, up 7.1% on last year
  3: We avoid counting software twice when it is sold with a device
  2: We round the $677B human-device sum to about $680B in 2026
  0: We conclude that MedTech is worth roughly $680B worldwide in 2026
sources:
- claim: Frost & Sullivan forecasts $682B of global medical-device sales in 2026, including animal care.
  url: https://www1.hkexnews.hk/app/sehk/2026/108529/documents/sehk26051101259.pdf
  date: '2026-05-11'
  quote: '| 2026E | 682.3 |'
- claim: Animal care accounts for $4.9B in the Frost & Sullivan 2026 medical-device total.
  url: https://www1.hkexnews.hk/app/sehk/2026/108529/documents/sehk26051101259.pdf
  date: '2026-05-11'
  quote: '| Animal care | 3.6 | 3.8 | 4.0 | 4.2 | 4.4 | 4.6 | 4.9 |'
- claim: Frost & Sullivan forecasts $139B in 2026 in-vitro diagnostics.
  url: https://www1.hkexnews.hk/app/sehk/2026/108529/documents/sehk26051101259.pdf
  date: '2026-05-11'
  quote: '| 2026E | 139.4 |'
- claim: Frost & Sullivan forecasts $96B in 2026 medical imaging.
  url: https://www1.hkexnews.hk/app/sehk/2026/108529/documents/sehk26051101259.pdf
  date: '2026-05-11'
  quote: '| MI | 63.8 | 70.4 | 73.8 | 83.3 | 87.2 | 91.5 | 96.2 |'
- claim: Frost & Sullivan forecasts $65B in 2026 minimally invasive intervention.
  url: https://www1.hkexnews.hk/app/sehk/2026/108529/documents/sehk26051101259.pdf
  date: '2026-05-11'
  quote: '| MII | 36.5 | 40.0 | 44.0 | 48.6 | 53.8 | 59.5 | 65.4 |'
- claim: Frost & Sullivan forecasts $38B in 2026 minimally invasive surgery.
  url: https://www1.hkexnews.hk/app/sehk/2026/108529/documents/sehk26051101259.pdf
  date: '2026-05-11'
  quote: '| MIS | 27.7 | 29.8 | 31.5 | 33.4 | 33.8 | 35.5 | 37.5 |'
- claim: Frost & Sullivan forecasts $13B in 2026 monitoring and life-support systems.
  url: https://www1.hkexnews.hk/app/sehk/2026/108529/documents/sehk26051101259.pdf
  date: '2026-05-11'
  quote: '| PMLS | 9.7 | 9.9 | 10.4 | 11.2 | 11.9 | 12.3 | 12.8 |'
- claim: Frost & Sullivan forecasts $326B in the 2026 other-device category.
  url: https://www1.hkexnews.hk/app/sehk/2026/108529/documents/sehk26051101259.pdf
  date: '2026-05-11'
  quote: '| Others | 208.0 | 252.3 | 263.3 | 304.5 | 305.2 | 313.5 | 326.0 |'
- claim: Fortune Business Insights forecasts $605B of global medical-device sales in 2026.
  url: https://www.fortunebusinessinsights.com/industry-reports/medical-devices-market-100085
  date: '2026-11-02'
  quote: from USD 604.99 billion in 2026 to USD 1032.66 billion by 2034
- claim: Precedence Research estimates the 2026 medical-device market at $720B.
  url: https://www.precedenceresearch.com/medical-devices-market
  date: '2026-09-09'
  quote: The global medical devices market was valued at USD 719.61 billion in 2026
- claim: Diligence Insights forecasts $624B of medical devices sales in 2026.
  url: https://www.marketresearch.com/Diligence-Insights-v4290/Medical-Devices-Size-Share-Trends-44442872/
  date: '2026-03-23'
  quote: $623.86 billion in 2026, and is projected to reach $910.30 billion by 2032
- claim: EY reports approximately $650B of medical technology revenue in 2025.
  url: https://www.ey.com/en_us/newsroom/2026/10/pulse-medtech-industry-report-2026
  date: '2026-10-19'
  quote: reaching approximately US$650 billion in revenue and representing growth of 11%
- claim: EY reports $325B for the first half of 2026, a 7.1% year-on-year increase.
  url: https://www.ey.com/en_us/newsroom/2026/10/pulse-medtech-industry-report-2026
  date: '2026-10-19'
  quote: generating $325 billion in revenue, a 7.1% increase compared with the same time period in 2025.
```

### ed045
```yaml
status: ok
section: Market size
title: How much is MedTech worth today?
t:
  6: $680B
  8: We estimate $680B in 2026 from Frost & Sullivan's $682B global forecast, less $5B in animal care. Fortune puts the market at $605B and Precedence at $720B, which brackets our result.
  4: '2026'
note: We round the detailed 2026 human-device sector total after removing veterinary sales and check against two other estimates.
sources:
- claim: Frost & Sullivan forecasts $682B of global medical-device sales in 2026, including animal care.
  url: https://www1.hkexnews.hk/app/sehk/2026/108529/documents/sehk26051101259.pdf
  date: '2026-05-11'
  quote: '| 2026E | 682.3 |'
- claim: Animal care accounts for $4.9B in the Frost & Sullivan 2026 medical-device total.
  url: https://www1.hkexnews.hk/app/sehk/2026/108529/documents/sehk26051101259.pdf
  date: '2026-05-11'
  quote: '| Animal care | 3.6 | 3.8 | 4.0 | 4.2 | 4.4 | 4.6 | 4.9 |'
- claim: Fortune Business Insights forecasts $605B of global medical-device sales in 2026.
  url: https://www.fortunebusinessinsights.com/industry-reports/medical-devices-market-100085
  date: '2026-11-02'
  quote: from USD 604.99 billion in 2026 to USD 1032.66 billion by 2034
- claim: Precedence Research estimates the 2026 medical-device market at $720B.
  url: https://www.precedenceresearch.com/medical-devices-market
  date: '2026-09-09'
  quote: The global medical devices market was valued at USD 719.61 billion in 2026
```

### ed047p
```yaml
status: no_data
reason: no category donut on the live product page and these three revenue buckets are not our database categories (ed048 follows a donut only)
```

### ed048
```yaml
status: no_data
reason: no category donut on the live product page and these three revenue buckets are not our database categories (ed048 follows a donut only)
```

### ed049
```yaml
status: ok
section: Market size
title: Where in the world is MedTech money spent?
regions:
  na:
    pct: 38.1
    text: North America leads with $231B in 2026 device sales. Fortune links its scale to access to care and fast use of new tools.
  eu:
    pct: 25.6
    text: Europe is second with $155B in 2026 sales, helped by hospitals and more spending on advanced tests and treatment devices.
  apac:
    pct: 25.4
    text: Asia-Pacific has $154B in 2026 and is forecast to grow quickly as hospitals add new medical equipment.
  latam:
    pct: 6.6
    text: Latin America has about $40B in 2026. Fortune points to rising chronic disease and greater use of medical equipment in the region.
  mea:
    pct: 4.3
    text: We derive about $26B in 2026 for the Middle East and Africa after removing four other regions from Fortune's global total.
note:
- We calculate regional shares from Fortune Business Insights' 2026 global and four published regional sales figures
- We derive Middle East and Africa as the remainder and round the five percentages to one decimal place
sources:
- claim: Fortune Business Insights forecasts $605B of global medical-device sales in 2026.
  url: https://www.fortunebusinessinsights.com/industry-reports/medical-devices-market-100085
  date: '2026-11-02'
  quote: from USD 604.99 billion in 2026 to USD 1032.66 billion by 2034
- claim: North America reaches $231B in 2026 medical-device sales.
  url: https://www.fortunebusinessinsights.com/industry-reports/medical-devices-market-100085
  date: '2026-11-02'
  quote: USD 230.62 billion in 2026, led by advanced healthcare infrastructure.
- claim: Europe reaches $155B in 2026 medical-device sales.
  url: https://www.fortunebusinessinsights.com/industry-reports/medical-devices-market-100085
  date: '2026-11-02'
  quote: USD 154.82 billion in 2026, driven by rising healthcare spending.
- claim: Asia-Pacific reaches $154B in 2026 medical-device sales.
  url: https://www.fortunebusinessinsights.com/industry-reports/medical-devices-market-100085
  date: '2026-11-02'
  quote: USD 153.58 billion in 2026, with the fastest growth.
- claim: Latin America reaches $40B in 2026 medical-device sales.
  url: https://www.fortunebusinessinsights.com/industry-reports/medical-devices-market-100085
  date: '2026-11-02'
  quote: The region is likely to hit USD 39.87 billion in 2026, as the fourth-largest market.
```

### ed050
```yaml
status: ok
section: Market size
title: What are the growth rate estimates from different sources online?
note: We compare annual global medical-device sales growth, not drug sales, hospital procedure charges or deal values.
t:
  24: FIRM
  25: CAGR
  26: COMMENTS
  6: 'Frost &

    Sullivan'
  5: '≈ 6.0%

    through 2030'
  7: Their forecast uses device sales at factory prices. It projects steady growth in tests, scans and tools used for treatment.
  10: "Technavio\nResearch"
  9: '≈ 6.3%

    through 2030'
  11: Their report sees global growth as medical gear improves and hospitals replace it. We use it near our middle case.
  14: 'Diligence

    Insights'
  13: '≈ 6.5%

    through 2032'
  15: They include diagnostics, hospital supplies and surgical equipment. Their 6.5% growth rate sits right at our base case.
  18: 'Coherent Market

    Insights'
  17: '≈ 7.3%

    through 2033'
  19: Their broader device forecast is the fastest of these four. It includes tests, monitors, implants and newer tools used at home.
sources:
- claim: Frost & Sullivan projects 6.0% global device market growth for 2025 to 2030.
  url: https://www1.hkexnews.hk/app/sehk/2026/108529/documents/sehk26051101259.pdf
  date: '2026-05-11'
  quote: '| 2025-2030E | 6.9% | 5.7% | 8.8% | 8.2% | 4.4% | 8.7% | 4.9% | 6.0% |'
- claim: Technavio forecasts a 6.3% annual growth rate during 2025 to 2030.
  url: https://www.researchandmarkets.com/reports/4994813/medical-devices-market-2026-2030
  date: '2026-06-01'
  quote: accelerating at a CAGR of 6.3% during the forecast period.
- claim: Diligence Insights forecasts a 6.5% annual growth rate through 2032.
  url: https://www.marketresearch.com/Diligence-Insights-v4290/Medical-Devices-Size-Share-Trends-44442872/
  date: '2026-03-23'
  quote: growing at a CAGR of 6.5% during the forecast period.
- claim: Coherent Market Insights forecasts a 7.3% annual growth rate from 2026 to 2033.
  url: https://www.coherentmarketinsights.com/industry-reports/medical-devices-market
  date: '2026-03-17'
  quote: exhibiting a compound annual growth rate (CAGR) of 7.3% from 2026 to 2033.
```

### ed051
```yaml
status: ok
section: Market size
title: What is a realistic CAGR for the MedTech market?
note: We use 6.5% as the base case, between published growth forecasts near 6% and 7%. The 5% and 8% cases are our scenarios.
t:
  15: BEST CASE ≈ 8%
  17: '≈6.5%

    through 2035'
  19: Most major forecasts sit near 6% to 7% annual growth. We choose 6.5% for 2026 to 2035, with a 5% downside for price pressure and an 8% upside if adoption speeds up.
  16: WORST CASE ≈ 5%
sources:
- claim: Frost & Sullivan projects 6.0% global device market growth for 2025 to 2030.
  url: https://www1.hkexnews.hk/app/sehk/2026/108529/documents/sehk26051101259.pdf
  date: '2026-05-11'
  quote: '| 2025-2030E | 6.9% | 5.7% | 8.8% | 8.2% | 4.4% | 8.7% | 4.9% | 6.0% |'
- claim: Technavio forecasts a 6.3% annual growth rate during 2025 to 2030.
  url: https://www.researchandmarkets.com/reports/4994813/medical-devices-market-2026-2030
  date: '2026-06-01'
  quote: accelerating at a CAGR of 6.3% during the forecast period.
- claim: Diligence Insights forecasts a 6.5% annual growth rate through 2032.
  url: https://www.marketresearch.com/Diligence-Insights-v4290/Medical-Devices-Size-Share-Trends-44442872/
  date: '2026-03-23'
  quote: growing at a CAGR of 6.5% during the forecast period.
- claim: Coherent Market Insights forecasts a 7.3% annual growth rate from 2026 to 2033.
  url: https://www.coherentmarketinsights.com/industry-reports/medical-devices-market
  date: '2026-03-17'
  quote: exhibiting a compound annual growth rate (CAGR) of 7.3% from 2026 to 2033.
```
