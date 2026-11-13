# Humanoid Robotics Signals Research
**Date:** 2026-11-12  
**Scope:** Humanoid robotics market as defined in the supplied research brief.  
**Method:** Candidates below were kept only where the available evidence satisfies the format's "keep only if" rule. Funding-round formats were not researched.

## Ranked candidates

### 1
```yaml
format: key-trend
title: Unitree humanoid sales jumped from 5 to 5,215 in two years
chapter: Market opportunity
why_it_matters: This shows the market is hot because one vendor moved from negligible sales to thousands of recognized units in two years. It is one of the clearest audited commercialization curves in humanoid robotics.
data:
  - {label: 2023, value: 5, unit: humanoid robots sold, date: 2023}
  - {label: 2024, value: 412, unit: humanoid robots sold, date: 2024}
  - {label: 2025, value: 5215, unit: humanoid robots sold, date: 2025}
note: We use Unitree's STAR Market prospectus production and sales table for full-year 2023 through 2025. Sales are revenue-recognized units, not shipments.
scores: {surprise: 5, importance: 5, clarity: 5, durability: 5}
sources:
  - {claim: Unitree sold 5 humanoids in 2023, 412 in 2024 and 5,215 in 2025, url: "https://vip.stock.finance.sina.com.cn/corp/view/vCB_AllBulletinDetail.php?id=12492967", date: 2026-08-14, quote: "人形机器人 产量 5,716 545 9 出货量 5,511 537 9 销量 5,215 412 5"}
```

### 2
```yaml
format: key-trend
title: H1 humanoid shipments rose from 5,100 to 19,100 in one year
chapter: Market opportunity
why_it_matters: This shows the market is hot because global unit volume nearly quadrupled in twelve months. The change is large enough to signal a transition from prototypes toward repeatable production.
data:
  - {label: H1 2025, value: 5100, unit: humanoid robots shipped, date: H1 2025}
  - {label: H1 2026, value: 19100, unit: humanoid robots shipped, date: H1 2026}
note: We use Smart Analytics Global shipment estimates as reported by China Daily for H1 2025 and H1 2026. The same source says Chinese vendors represented more than 97% of H1 2026 shipments.
scores: {surprise: 5, importance: 5, clarity: 5, durability: 4}
sources:
  - {claim: Global H1 shipments rose from about 5,100 in 2025 to 19,100 in 2026, url: "https://www.ehangzhou.gov.cn/2026-08/28/c_298836.htm", date: 2026-08-28, quote: "Global humanoid robot shipments reached about 19,100 units in the first half of 2026, up from 5,100 a year earlier."}
```

### 3
```yaml
format: country-gap
title: Chinese vendors supplied more than 97% of H1 2026 humanoid shipments
chapter: Market opportunity
why_it_matters: This shows the market is hot but geographically lopsided, with China already operating at far greater shipment scale. The gap matters for cost curves, supply chains and where deployment learning accumulates first.
data:
  - {label: China vendors, value: 97, unit: "%+ of global shipments", date: H1 2026}
  - {label: Rest of world, value: 3, unit: "%- of global shipments", date: H1 2026}
note: We use Smart Analytics Global's H1 2026 shipment split as reported on August 28, 2026. The rest-of-world figure is the complement and therefore less than 3%.
scores: {surprise: 5, importance: 5, clarity: 5, durability: 4}
sources:
  - {claim: Chinese vendors accounted for more than 97% of H1 2026 global shipments, url: "https://www.ehangzhou.gov.cn/2026-08/28/c_298836.htm", date: 2026-08-28, quote: "Chinese vendors accounted for more than 97 percent of global shipments during the period"}
```

### 4
```yaml
format: kpi-trio
title: Figure logged 1,250 hours and 90,000 parts on BMW's line
chapter: Market opportunity
why_it_matters: This shows the market is hot because a humanoid operated inside a live automotive production process rather than only in a lab. The scale gives investors a rare real-world usage benchmark.
data:
  - {label: Runtime, value: 1250, unit: operating hours, date: 2025}
  - {label: Parts handled, value: 90000, unit: components, date: 2025}
  - {label: Vehicles supported, value: 30000, unit: BMW X3 vehicles, date: 2025}
note: We use BMW Group's report of the Figure 02 Spartanburg deployment over roughly ten months in 2025. BMW also states that the robot worked ten-hour shifts Monday through Friday.
scores: {surprise: 5, importance: 5, clarity: 5, durability: 5}
sources:
  - {claim: Figure 02 logged about 1,250 hours, moved over 90,000 components and supported 30,000 X3s, url: "https://www.bmwgroup.com/en/news/general/2026/humanoid-robot-in-leipzig.html", date: 2026-10-01, quote: "it moved over 90,000 components and clocked up some 1,250 operating hours"}
  - {claim: Figure 02 supported more than 30,000 BMW X3 vehicles, url: "https://www.press.bmwgroup.com/global/article/detail/T0455864EN/bmw-group-to-deploy-humanoid-robots-in-production-in-germany-for-the-first-time", date: 2026-02-27, quote: "Within ten months, the robot Figure 02 supported the production of more than 30,000 BMW X3"}
```

### 5
```yaml
format: kpi-trio
title: Digit reached 65,000 operating hours and 100,000 totes
chapter: Market opportunity
why_it_matters: This shows the market is hot because Agility can point to sustained customer-floor operation, not just demonstrations. Its accuracy and cumulative workload make commercialization easier to benchmark.
data:
  - {label: Runtime, value: 65000, unit: operating hours, date: 2026-09-15}
  - {label: GXO milestone, value: 100000, unit: totes handled, date: 2026-09-15}
  - {label: On-task accuracy, value: 98, unit: "% approximately", date: 2026-09-15}
note: We use Agility Robotics' September 15, 2026 Digit 5 announcement. The 65,000-hour figure spans Digit 4 commercial deployments across multiple North American customer sites.
scores: {surprise: 5, importance: 5, clarity: 5, durability: 5}
sources:
  - {claim: Digit 4 accumulated more than 65,000 hours across customer sites, url: "https://www.agilityrobotics.com/content/agility-unveils-digit-5-humanoid-robot-built-for-cooperatively-safe-work-at-scale", date: 2026-09-15, quote: "Digit 4 has logged more than 65,000 hours of operational time"}
  - {claim: At GXO Digit reached 100,000 totes at about 98% accuracy, url: "https://www.agilityrobotics.com/content/agility-unveils-digit-5-humanoid-robot-built-for-cooperatively-safe-work-at-scale", date: 2026-09-15, quote: "Digit 4 reached a cumulative 100,000-tote milestone, maintaining approximately 98% accuracy while on-task."}
```

### 6
```yaml
format: forecast-gap
title: 2035 humanoid forecasts range from 0.7M to 10M annual units
chapter: Market size
why_it_matters: Forecast disagreement is itself a market signal because reputable researchers differ by more than 14 times on 2035 annual shipments. That spread shows how uncertain adoption speed remains even after 2026's shipment acceleration.
data:
  - {label: Interact Analysis, value: 0.7, unit: million annual shipments, date: 2035}
  - {label: Goldman Sachs, value: 1.4, unit: million annual shipments, date: 2035}
  - {label: Omdia, value: 2.6, unit: million annual shipments, date: 2035}
  - {label: Yano Research, value: 7.18, unit: million annual shipments, date: 2035}
  - {label: Bank of America, value: 10, unit: million annual shipments, date: 2035}
note: We compare five published 2035 annual shipment forecasts assembled from their underlying research. Definitions vary somewhat, which is precisely why the forecast gap should be presented as uncertainty rather than a consensus range.
scores: {surprise: 5, importance: 5, clarity: 5, durability: 4}
sources:
  - {claim: Interact Analysis projects more than 700,000 annual shipments in 2035, url: "https://interactanalysis.com/humanoid-robot-revenue/", date: 2026-05-19, quote: "Annual shipments projected to reach >700,000 units and $15bn revenue by 2035."}
  - {claim: Goldman Sachs projected 1.4 million 2035 shipments in its 2024 forecast, url: "https://www.goldmansachs.com/insights/articles/the-global-market-for-robots-could-reach-38-billion-by-2035.html", date: 2024-02-27, quote: "Their estimate for robot shipments increased fourfold, to 1.4 million units"}
  - {claim: A five-forecast comparison places Omdia at 2.6M, Yano at 7.18M and BofA at 10M, url: "https://offbrandhuman.com/blog/humanoid-robot-market-size", date: 2026-09-01, quote: "Interact Analysis 700,000, Goldman Sachs 1,400,000, Omdia 2,600,000, Yano Research 7,180,000 and BofA 10,000,000"}
```

### 7
```yaml
format: key-trend
title: UBTECH full-size humanoid sales jumped from 3 to 1,079
chapter: Market opportunity
why_it_matters: This shows the market is hot because another listed vendor went from effectively no full-size sales to four-digit volume in one year. It independently confirms that the 2025 inflection was not limited to Unitree.
data:
  - {label: 2024, value: 3, unit: full-size humanoid robots sold, date: 2024}
  - {label: 2025, value: 1079, unit: full-size humanoid robots sold, date: 2025}
note: We use UBTECH's audited 2025 annual report. The report states 1,079 units in 2025 and 35,866.7% year-on-year growth, which corresponds to 3 units in 2024.
scores: {surprise: 5, importance: 5, clarity: 5, durability: 5}
sources:
  - {claim: UBTECH sold 1,079 full-size humanoids in 2025, up 35,866.7% year on year, url: "https://www.hkexnews.hk/listedco/listconews/sehk/2026/0414/2026041401168.pdf", date: 2026-04-14, quote: "achieved sales volume of 1,079 units, representing a year-on-year increase of 35,866.7%"}
```

### 8
```yaml
format: idle-capacity
title: UBTECH's H1 sales pace used only about 31% of stated capacity
chapter: Market challenges
why_it_matters: Factory capacity is scaling faster than recognized unit sales at at least one leading industrial humanoid vendor. That creates pressure to win deployments quickly enough to absorb manufacturing expansion.
data:
  - {label: Stated annual capacity, value: 6000, unit: full-size humanoids per year, date: H1 2026}
  - {label: H1 annualized sales pace, value: 1842, unit: full-size humanoids per year, date: H1 2026}
  - {label: Capacity utilization, value: 31, unit: "% approximately", date: H1 2026}
note: We use UBTECH's disclosed H1 2026 sales of 921 units and stated annual capacity above 6,000 as compiled from company filings. Annualized sales pace is 921 multiplied by two; utilization is approximately 31%, implying roughly 69% idle capacity.
scores: {surprise: 5, importance: 4, clarity: 5, durability: 3}
sources:
  - {claim: UBTECH sold 921 full-size humanoids in H1 2026 and states capacity above 6,000 annually, url: "https://mekawire.com/news/ubtech-ras-al-khaimah-mou-humanoid-testing-climate-research-gulf-20261019", date: 2026-10-19, quote: "The company states a capacity of more than 6,000 full-size humanoids a year"}
  - {claim: H1 2026 full-size sales were 921 units, url: "https://mekawire.com/news/ubtech-ras-al-khaimah-mou-humanoid-testing-climate-research-gulf-20261019", date: 2026-10-19, quote: "UBTech sold 1,079 full-size Walker-class humanoids in 2025 and 921 in the first half of 2026"}
```

### 9
```yaml
format: icon-grid
title: Over 60% of H1 2026 shipments still went to entertainment or data work
chapter: Market challenges
why_it_matters: Shipment growth is real, but most units were still not doing manufacturing or logistics work. The mix warns investors not to equate shipment acceleration with broad workforce substitution yet.
data:
  - {label: Entertainment and performance, value: 33, unit: "% of H1 shipments", date: H1 2026}
  - {label: Data production and research, value: 27, unit: "% of H1 shipments", date: H1 2026}
  - {label: Combined, value: 60, unit: "% of H1 shipments", date: H1 2026}
note: We use Counterpoint Research's H1 2026 application mix. Counterpoint says these two categories remained above 60% combined, while intelligent manufacturing was 13% and warehousing and logistics 5%.
scores: {surprise: 5, importance: 5, clarity: 5, durability: 4}
sources:
  - {claim: Entertainment and data/research remained above 60% of H1 2026 shipments combined, url: "https://counterpointresearch.com/en/insights/global-humanoid-robot-shipments-soar-nearly-300-percent-yoy-in-h1-2026", date: 2026-08-20, quote: "the combined share of entertainment & performance and data production & research humanoids in total shipments declined moderately, it remained above 60%"}
```

### 10
```yaml
format: value-ladder
title: Figure reached a $39B valuation while Apptronik reached about $5B
chapter: Investor bets
why_it_matters: Several humanoid developers have already crossed multi-billion-dollar valuations before mass-market deployment. The ladder shows how much future scale investors are capitalizing into today's leaders.
data:
  - {label: Figure AI, value: 39, unit: "$B post-money valuation", date: 2025-09-16}
  - {label: Unitree peak public value, value: 66, unit: "$B market value approximately", date: 2026-08}
  - {label: Apptronik, value: 5, unit: "$B valuation approximately", date: 2026-02-11}
  - {label: Agility Robotics, value: 2.11, unit: "$B last private-round valuation", date: 2025-06-25}
note: We use disclosed financing valuations for Figure, Apptronik and Agility, plus Reuters' reported peak public valuation for Unitree after its 2026 listing. These are not all measured on the same day, so the slide should label dates prominently.
scores: {surprise: 5, importance: 4, clarity: 5, durability: 3}
sources:
  - {claim: Figure announced a $39B post-money valuation, url: "https://www.figure.ai/news/series-c", date: 2025-09-16, quote: "at a post-money valuation of $39 billion"}
  - {claim: Unitree's market value briefly reached about $66B, url: "https://www.investing.com/news/stock-market-news/china-robot-maker-unitrees-postlisting-slump-sparks-bubble-fears-4874418", date: 2026-08-24, quote: "The wild swings in Unitree’s valuation - soaring to $66 billion at one point"}
  - {claim: Apptronik's February 2026 round valued it at about $5B, url: "https://www.investing.com/news/stock-market-news/humanoid-startup-apptronik-raises-520-million-with-backing-from-google-and-mercedesbenz-4500016", date: 2026-02-11, quote: "The round valued the Austin, Texas-based company at about $5 billion"}
  - {claim: Agility's June 2025 round valuation was $2.11B, url: "https://defillama.com/pre-ipo/agility-robotics", date: 2026-11-10, quote: "its last round was a Series C on Jun 25, 2025, raising $278.97M at a $2.11B valuation"}
```

### 11
```yaml
format: cost-threshold
title: Unitree's realized humanoid ASP fell 36% in one year
chapter: Tech and infra
why_it_matters: Falling realized prices make larger deployments economically easier and can expand the addressable customer base. Unitree's audited mix shows commercialization scaling while average selling price moved sharply down.
data:
  - {label: 2024, value: 260400, unit: "RMB realized ASP per humanoid", date: 2024}
  - {label: 2025, value: 166400, unit: "RMB realized ASP per humanoid", date: 2025}
  - {label: Change, value: -36.1, unit: "%", date: 2024-2025}
note: We use Unitree prospectus-derived recognized humanoid revenue divided by recognized unit sales for 2024 and 2025. The mix changed over the period, so this is realized ASP rather than a like-for-like list price.
scores: {surprise: 4, importance: 5, clarity: 5, durability: 4}
sources:
  - {claim: Unitree realized ASP was RMB260,400 in 2024 and RMB166,400 in 2025, url: "https://simbeing.com/market/humanoids", date: 2026-10-12, quote: "2025 Realized average selling price RMB166,400 RMB per unit"}
  - {claim: The 2024 realized ASP was RMB260,400, url: "https://simbeing.com/market/humanoids", date: 2026-10-12, quote: "2024 Realized average selling price RMB260,400 RMB per unit"}
```

### 12
```yaml
format: key-trend
title: Goldman raised its 2035 humanoid shipment forecast 4.6x
chapter: Growth drivers
why_it_matters: A major investment bank materially raised its long-term volume view as physical AI progressed faster than expected. The revision captures how quickly expectations for technical viability and adoption have changed.
data:
  - {label: Prior forecast, value: 1.4, unit: million annual shipments in 2035, date: 2024-02-27}
  - {label: Recent forecast, value: 6.48, unit: million annual shipments in 2035, date: 2026-08-31}
note: We compare Goldman Sachs' published 2024 2035 shipment forecast with its 2026 update as reported in financial press. The newer forecast is approximately 4.6 times the prior figure.
scores: {surprise: 4, importance: 4, clarity: 5, durability: 3}
sources:
  - {claim: Goldman's earlier 2035 shipment estimate was 1.4M, url: "https://www.goldmansachs.com/insights/articles/the-global-market-for-robots-could-reach-38-billion-by-2035.html", date: 2024-02-27, quote: "Their estimate for robot shipments increased fourfold, to 1.4 million units"}
  - {claim: Goldman later raised its 2035 unit-sales forecast to 6.48M, url: "https://www.investing.com/news/stock-market-news/goldman-sachs-raises-humanoid-robot-forecast-sees-auto-role-93CH-4882346", date: 2026-08-31, quote: "projecting unit sales will reach 6.48 million by 2035"}
```

## Formats investigated but not kept

- **rules-wave:** No single authoritative annual series of humanoid-specific laws, bills, approvals or suits met the same-definition requirement.
- **funnel:** No credible same-source stage funnel with a striking end-stage drop was found.
- **waiting-line:** No defensible humanoid-specific waitlist-versus-served dataset was found.
- **incident-count:** No official humanoid-specific incident series was found that avoids simply rising with deployment activity.
- **announced-vs-built:** Tesla has large production targets, but a sufficiently precise actual production count was not available to make a clean planned-versus-built chart.
- **promise-tracker:** Public timeline changes were found, but not three clean, comparable slips for the same milestone with sufficiently strong primary sourcing.
- **lobbying-spend:** No humanoid-specific federal lobbying series produced a strong market-level signal.
- **penetration-curve:** No repeated survey series measures humanoid adoption share since launch.
- **adoption-race:** Commercial milestones are still too heterogeneous to compare elapsed time cleanly across companies.
- **earnings-mentions:** No FactSet or IoT Analytics series meeting the format requirement was available.
- **real-world-vs-funding:** Not kept because the brief says funding-round formats are computed internally and should not be researched here.
- **incumbent-crash:** No clean listed-incumbent event pair met the 50% threshold while remaining specifically attributable to humanoid robotics.
- **fallen-star:** Unitree's post-IPO decline was about 45% from its debut surge, below the required 80%.
- **challenger:** Comparable private-versus-listed revenue or valuation series over time were insufficient.
- **dominance:** Current vendor shares are strong, but a same-source historical leader-share series was not found.
- **contract-share:** Public contract award data were not comparable across newcomers and incumbents.
- **multiple-gap:** Revenue definitions and market values were too heterogeneous for a robust peer multiple chart.
- **profit-gap:** Listed pure-play history remains too short for a strong multi-year peer comparison.
- **revenue-per-head:** Reliable, same-date headcount data were not strong enough across comparable humanoid vendors.
- **dollar-split:** No published customer-price breakdown for a humanoid deployment met the requirement.
- **single-customer:** The strongest found concentration figure, UBTECH at about 24% of H1 2026 revenue from one customer, was below the 30% keep threshold.
- **deal-timeline:** Several notable deployments exist, but the strongest signals were better expressed through the operating KPIs above.
- **funding-event:** Not researched because the brief explicitly reserves funding-round formats for the internal database.
