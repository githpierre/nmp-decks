# Humanoid robotics market report — Market size

### ed041
```yaml
status: ok
section: Market size
title: What counts as humanoid robotics, and what doesn’t?
note: We count integrated humanoid platforms with a functional torso, task-capable arms and mobility, and exclude standalone components, AI software and nonhumanoid robots.
t:
  7: We define humanoid robotics as integrated human-oriented robots with a functional torso and articulated arms that perform physical tasks in human spaces
  8: We include bipedal, wheeled and hybrid humanoids for industrial, logistics, service, home, research and embodied-AI training use
  9: We exclude component-only, AI-only and nonhumanoid robots, including hands, arms, grippers, AMRs, robot dogs, exoskeletons and animatronics
sources:
  - claim: Humanoid robots have an anthropomorphic torso, upper-limb operating structures and mobility, and can execute tasks in human environments.
    url: https://www.frostchina.com/en/content/insight/detail/6ad199fb7f1bc6817386cd98
    date: 2026-09-30
    quote: "Humanoid robots are robot systems with anthropomorphic torso, upper limb operating structures, and mobility"
  - claim: Humanoid robots can move by two legs or wheels and perform actual tasks with dual arms or other end effectors.
    url: https://www.frostchina.com/en/content/insight/detail/6ad199fb7f1bc6817386cd98
    date: 2026-09-30
    quote: "humanoid robots can move via two legs or wheels and complete various actual tasks"
```

### ed042
```yaml
status: ok
section: Market size
title: What are the market size estimates from different sources online?
rows:
- firm: 'Grand View

    Research'
  value: $ 4.2 B
  comment: Their 2026 estimate includes hardware and software across biped and wheel-drive robots. We use it as the low end of broad published estimates.
- firm: 'Marketsand

    Markets'
  value: $ 5.41 B
  comment: Their scope includes hardware, software and services, plus stationary torso systems. It is broader than our integrated mobile-platform definition.
- firm: 'Fortune Business

    Insights'
  value: $ 6.24 B
  comment: Their ecosystem also includes component and software suppliers. We treat the 2026 figure as a broad market benchmark, not direct robot sales.
- firm: 'Global Market

    Insights'
  value: $ 10.9 B
  comment: Their 2026 estimate is the highest of these sources and starts from a very broad revenue base. We use it only as an upper cross-check.
note:
- We take each estimate from the firm's current website and compare its scope with our definition
- We keep complete humanoid-platform revenue apart from components, software, services, funding and orders
sources:
  - claim: Grand View Research estimates the humanoid robot market at $4.2B in 2026.
    url: https://www.grandviewresearch.com/industry-analysis/humanoid-robot-market-report
    date: 2026-06-05
    quote: "projected to grow from USD 4.2 billion in 2026 to USD 40.5 billion by 2033"
  - claim: MarketsandMarkets estimates the humanoid robot market at $5.41B in 2026.
    url: https://www.marketsandmarkets.com/Market-Reports/humanoid-robot-market-99567653.html
    date: 2026-07-06
    quote: "The humanoid robot market size is estimated to be USD 5.41 billion in 2026"
  - claim: Fortune Business Insights estimates the humanoid robot market at $6.24B in 2026.
    url: https://www.fortunebusinessinsights.com/humanoid-robots-market-110188
    date: 2026-10-26
    quote: "projected to grow from USD 6.24 billion in 2026"
  - claim: Global Market Insights estimates the humanoid robot market at $10.9B in 2026.
    url: https://www.gminsights.com/industry-analysis/humanoid-robot-market
    date: 2026-09-01
    quote: "estimated to increase from USD 10.9 billion in 2026 to USD 192.7 billion by 2035"
```

### ed043
```yaml
status: ok
section: Market size
title: Our own first-principles, bottom-up calculation of the market size
page: 1/2
note: We anchor the estimate to current shipment and industry-revenue data, then remove the broader component, software and service layers included in many market reports.
t:
  21: We estimate platform revenue using shipments and realized market sales
  16: We start from 2026 shipment data because commercial volumes are now measurable
  15: We count complete humanoid platforms sold to external customers worldwide
  14: We exclude standalone components, AI software, services and adjacent robots
  9: We exclude funding, orders and factory capacity because they are not realized sales
  8: We use 2026, the latest year with shipment and revenue estimates
  7: SAG expects about 54,000 humanoid robots to ship worldwide during 2026
  6: SAG estimates 2026 humanoid revenue at $1.9 billion
  3: That implies roughly $35,000 in recognized revenue for each robot shipped
  2: Frost reported 36,000 humanoid sales and $540 million in H1 2026
  0: Frost reported $320 million for full-size embodied humanoids in H1 2026
sources:
  - claim: SAG forecasts 54,000 global humanoid shipments in 2026.
    url: https://smartanalyticsglobal.com/global-humanoid-robot-shipments-q3-2026-agibot-ubtech-unitree/
    date: 2026-11-09
    quote: "SAG forecasts global shipments to reach 54K units in 2026"
  - claim: SAG forecasts $1.9B of humanoid industry revenue in 2026.
    url: https://smartanalyticsglobal.com/global-humanoid-robot-shipments-q3-2026-agibot-ubtech-unitree/
    date: 2026-11-09
    quote: "with industry revenue reaching US$1.9 billion and US$2.8 billion, respectively"
  - claim: Frost & Sullivan reports 36,000 humanoid sales and $540M revenue in H1 2026.
    url: https://www.frostchina.com/en/content/insight/detail/6ad199fb7f1bc6817386cd98
    date: 2026-09-30
    quote: "in the first half of 2026, it reached 36,000 units"
  - claim: Frost & Sullivan reports $320M revenue for full-size embodied intelligent humanoids in H1 2026.
    url: https://www.frostchina.com/en/content/insight/detail/6ad199fb7f1bc6817386cd98
    date: 2026-09-30
    quote: "the first half of 2026, it reached 6,000 units"
```

### ed044
```yaml
status: ok
section: Market size
title: Our own first-principles, bottom-up calculation of the market size
page: 2/2
note: We use SAG's shipment-linked 2026 revenue estimate as the cleanest current proxy for complete robot sales, and use Frost as an independent commercial cross-check.
t:
  21: We use $1.9 billion because SAG reports both 2026 shipments and revenue
  16: The estimate equals about 54,000 robots times roughly $35,000 per unit
  15: That unit value fits today’s mix of low and high-end robots
  14: Frost reported $540 million of humanoid revenue in H1 2026
  9: SAG reported 16,500 units shipped globally in Q3 2026, up 347% year over year
  8: Those H1 figures support a low single-digit billion market
  7: Published 2026 market reports range from $4.2 billion to $10.9 billion
  6: Most broad reports also count software, components or services around the robot
  3: We keep complete-platform revenue and use $1.9 billion for 2026
  2: We use one number traceable to shipments and recognized market sales
  0: We conclude humanoid robot platform revenue is about $1.9 billion today
sources:
  - claim: SAG forecasts 54,000 shipments and $1.9B industry revenue in 2026.
    url: https://smartanalyticsglobal.com/global-humanoid-robot-shipments-q3-2026-agibot-ubtech-unitree/
    date: 2026-11-09
    quote: "SAG forecasts global shipments to reach 54K units in 2026"
  - claim: SAG reports 16,500 global humanoid shipments in Q3 2026, up 347% YoY.
    url: https://smartanalyticsglobal.com/global-humanoid-robot-shipments-q3-2026-agibot-ubtech-unitree/
    date: 2026-11-09
    quote: "global humanoid robot shipments surged 347% year over year (YoY) to 16,500 units in Q3 2026"
  - claim: Frost & Sullivan reports $540M of global humanoid revenue in H1 2026.
    url: https://www.frostchina.com/en/content/insight/detail/6ad199fb7f1bc6817386cd98
    date: 2026-09-30
    quote: "the global humanoid robot market size was $500 million for the whole of 2025 and $540 million"
  - claim: Published 2026 estimates span $4.2B to $10.9B.
    url: https://www.grandviewresearch.com/industry-analysis/humanoid-robot-market-report
    date: 2026-06-05
    quote: "Market Estimate, 2026 $4.2B"
  - claim: Published 2026 estimates span $4.2B to $10.9B.
    url: https://www.gminsights.com/industry-analysis/humanoid-robot-market
    date: 2026-09-01
    quote: "2026 Market Size $ 10.9 Billion"
```

### ed045
```yaml
status: ok
section: Market size
title: How much is humanoid robotics worth today?
t:
  6: $1.9B
  8: We estimate $1.9 billion in 2026 from 54,000 shipments and SAG revenue data. Broader reports span $4.2B to $10.9B because many include software, components and services.
  4: '2026'
note: We use direct industry revenue tied to current humanoid shipments, rather than the wider ecosystem definitions used by many market-research reports.
sources:
  - claim: SAG forecasts 54,000 shipments and $1.9B industry revenue in 2026.
    url: https://smartanalyticsglobal.com/global-humanoid-robot-shipments-q3-2026-agibot-ubtech-unitree/
    date: 2026-11-09
    quote: "with industry revenue reaching US$1.9 billion and US$2.8 billion, respectively"
  - claim: Broad published 2026 market estimates reach $10.9B.
    url: https://www.gminsights.com/industry-analysis/humanoid-robot-market
    date: 2026-09-01
    quote: "2026 Market Size $ 10.9 Billion"
```

### ed048
```yaml
status: ok
section: Market size
title: What is behind these categories?
t:
  5: BIPEDAL HUMANOIDS
  8: WHEELED HUMANOIDS
  10: HYBRID LOCOMOTION
  4: Two-legged robots use a human-like torso and arms while walking through stairs, factory aisles and other spaces designed around people
  7: Wheeled humanoids keep a task-capable torso and two arms but trade stairs for greater stability, efficiency and runtime on flat floors
  9: Hybrid platforms combine legs, wheels or transformable bases to preserve manipulation while adapting locomotion to different work settings
  15: ''
  17: ''
  18: ''
  19: ''
  14: ''
  16: ''
holes_ok: true
note: We group platforms by locomotion while requiring the same core feature: an integrated humanoid upper body that can physically manipulate its environment.
sources:
  - claim: Frost & Sullivan divides humanoids into two-legged and wheeled robots and explains their different mobility advantages.
    url: https://www.frostchina.com/en/content/insight/detail/6ad199fb7f1bc6817386cd98
    date: 2026-09-30
    quote: "humanoid robots can be divided into two-legged humanoid robots and wheeled humanoid robots"
  - claim: Grand View Research says biped robots held 71.6% of humanoid revenue in 2025.
    url: https://www.grandviewresearch.com/industry-analysis/humanoid-robot-market-report
    date: 2026-06-05
    quote: "Biped segment dominated the market with a revenue share of 71.6% in 2025"
```

### ed049
```yaml
status: ok
section: Market size
title: Where in the world is humanoid robotics money spent?
regions:
  na:
    pct: 43.4
    text: 'North America leads this broad revenue view at 43.4%, helped by US developers, research spending and early industrial deployments.'
  eu:
    pct: 11.1
    text: Europe holds 11.1%, with manufacturing the largest application and Germany expected to post the region’s fastest growth.
  apac:
    pct: 41.3
    text: Asia-Pacific is close behind at 41.3% and is the fastest-growing region, led by China, Japan and South Korea.
  latam:
    pct: 3.0
    text: Latin America accounts for 3.0% of 2025 revenue. Brazil is expected to register the region’s highest growth through 2033.
  mea:
    pct: 1.2
    text: The Middle East and Africa account for 1.2%. Commercial activity remains small compared with North America and Asia-Pacific.
note:
- We use Grand View Research's 2025 regional revenue shares because they provide a complete five-region split
- These shares use a broader hardware-and-software scope than our $1.9 billion complete-platform estimate
sources:
  - claim: North America held 43.4% of global humanoid robot revenue in 2025.
    url: https://www.grandviewresearch.com/industry-analysis/humanoid-robot-market-report
    date: 2026-06-05
    quote: "North America dominated the global market, accounting for the largest revenue share of 43.4% in 2025"
  - claim: Asia-Pacific held 41.3% of global humanoid robot revenue in 2025.
    url: https://www.grandviewresearch.com/horizon/outlook/humanoid-robot-market/asia-pacific
    date: 2026-07-30
    quote: "Asia Pacific region accounted for 41.3% of the global humanoid robot market in 2025"
  - claim: Europe held 11.1% of global humanoid robot revenue in 2025.
    url: https://www.grandviewresearch.com/horizon/outlook/humanoid-robot-market/europe
    date: 2026-07-30
    quote: "Europe region accounted for 11.1% of the global humanoid robot market in 2025"
  - claim: Latin America held 3.0% of global humanoid robot revenue in 2025.
    url: https://www.grandviewresearch.com/horizon/outlook/humanoid-robot-market/latin-america
    date: 2026-08-01
    quote: "Latin America region accounted for 3.0% of the global humanoid robot market in 2025"
  - claim: Middle East and Africa held 1.2% of global humanoid robot revenue in 2025.
    url: https://www.grandviewresearch.com/horizon/outlook/humanoid-robot-market/mea
    date: 2026-08-01
    quote: "MEA region accounted for 1.2% of the global humanoid robot market in 2025"
```

### ed050
```yaml
status: ok
section: Market size
title: What are the growth rate estimates from different sources online?
note: We use current humanoid-robot forecasts with explicit 2026 starting years. Their scopes differ, so we treat the spread as scenarios rather than one precise answer.
t:
  24: FIRM
  25: CAGR
  26: COMMENTS
  6: 'Marketsand

    Markets'
  5: '≈ 28.1%

    through 2035'
  7: Their forecast is broad, but its 28.1% CAGR gives us a conservative long-term benchmark for humanoid robot revenue growth.
  10: 'Grand View

    Research'
  9: '≈ 38.2%

    through 2033'
  11: Their 38.2% forecast sits near the middle of current estimates and provides a useful base case for a broad humanoid market.
  14: 'Global Market

    Insights'
  13: '≈ 37.6%

    through 2035'
  15: Their 37.6% forecast is close to Grand View, despite a much larger starting market size. We use it as a second mid-range check.
  18: 'Fortune Business

    Insights'
  17: '≈ 50.6%

    through 2034'
  19: Their 50.6% forecast is the highest of the major current estimates. We treat it as an upside case because its ecosystem scope is broad.
sources:
  - claim: MarketsandMarkets forecasts a 28.1% CAGR from 2026 to 2035.
    url: https://www.marketsandmarkets.com/Market-Reports/humanoid-robot-market-99567653.html
    date: 2026-07-06
    quote: "growing at a CAGR of 28.1% from 2026 to 2035"
  - claim: Grand View Research forecasts a 38.2% CAGR from 2026 to 2033.
    url: https://www.grandviewresearch.com/industry-analysis/humanoid-robot-market-report
    date: 2026-06-05
    quote: "at a CAGR of 38.2% from 2026 to 2033"
  - claim: Global Market Insights forecasts a 37.6% CAGR from 2026 to 2035.
    url: https://www.gminsights.com/industry-analysis/humanoid-robot-market
    date: 2026-09-01
    quote: "at a CAGR of 37.6% from 2026 to 2035"
  - claim: Fortune Business Insights forecasts a 50.60% CAGR from 2026 to 2034.
    url: https://www.fortunebusinessinsights.com/humanoid-robots-market-110188
    date: 2026-10-26
    quote: "exhibiting a CAGR of 50.60% during the forecast period"
```

### ed051
```yaml
status: ok
section: Market size
title: What is a realistic CAGR for the humanoid robotics market?
note: Current forecasts range from 28.1% to 50.6%. We use 40% as a rounded base case, with 30% and 50% as downside and upside scenarios.
t:
  15: BEST CASE ≈ 50%
  17: '≈40%

    through 2036'
  19: Shipment growth is still extreme, but market forecasts cluster from 28% to 51%. We use 40% as a base case, with 30% downside and 50% upside.
  16: WORST CASE ≈ 30%
sources:
  - claim: Current published CAGR estimates include 28.1%.
    url: https://www.marketsandmarkets.com/Market-Reports/humanoid-robot-market-99567653.html
    date: 2026-07-06
    quote: "CAGR of 28.1% from 2026 to 2035"
  - claim: Current published CAGR estimates include 38.2%.
    url: https://www.grandviewresearch.com/industry-analysis/humanoid-robot-market-report
    date: 2026-06-05
    quote: "CAGR, 2026–2033 38.2%"
  - claim: Current published CAGR estimates include 50.60%.
    url: https://www.fortunebusinessinsights.com/humanoid-robots-market-110188
    date: 2026-10-26
    quote: "CAGR: 50.60% from 2026–2034"
  - claim: SAG forecasts 2026 shipments up 277% YoY and 2027 shipments up 59%.
    url: https://smartanalyticsglobal.com/global-humanoid-robot-shipments-q3-2026-agibot-ubtech-unitree/
    date: 2026-11-09
    quote: "54K units in 2026 (+277% YoY) and 86K in 2027 (+59%)"
```

### ed052p
```yaml
status: ok
section: Market size
title: How much bigger can humanoid robotics get?
size: 1.9
cagr: 40
y0: 2026
lead: 'To get that big, '
condition: commercial shipments must keep scaling beyond China, while factories, warehouses and service buyers turn pilots into repeat orders at sustainable prices.
note:
- We start from our $1.9 billion 2026 platform-revenue estimate and apply a 40% base-case CAGR, roughly $55 billion by 2036
- We anchor the growth rate to current forecasts of 28.1% to 50.6%, while requiring commercialization to broaden beyond today's China-heavy shipment base
sources:
  - claim: SAG forecasts $1.9B humanoid industry revenue in 2026.
    url: https://smartanalyticsglobal.com/global-humanoid-robot-shipments-q3-2026-agibot-ubtech-unitree/
    date: 2026-11-09
    quote: "industry revenue reaching US$1.9 billion and US$2.8 billion, respectively"
  - claim: China represented 87% of global humanoid robot consumption in Q3 2026.
    url: https://smartanalyticsglobal.com/global-humanoid-robot-shipments-q3-2026-agibot-ubtech-unitree/
    date: 2026-11-09
    quote: "China representing 87% of worldwide humanoid robot consumption"
  - claim: Published long-term CAGR estimates range from 28.1% to 50.60%.
    url: https://www.marketsandmarkets.com/Market-Reports/humanoid-robot-market-99567653.html
    date: 2026-07-06
    quote: "CAGR of 28.1% from 2026 to 2035"
  - claim: Published long-term CAGR estimates reach 50.60%.
    url: https://www.fortunebusinessinsights.com/humanoid-robots-market-110188
    date: 2026-10-26
    quote: "CAGR: 50.60% from 2026–2034"
```
