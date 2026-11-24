# Managing General Agent: Tech and infra

Research completed: 2026-11-22. Company announcements and forecasts are identified as such.

### ed087
```yaml
status: ok
section: Tech and infra
title: What are the tech and infra layers?
page: 1/2
t:
  7: PAPER
  10: A licensed insurer supplies policy paper and defines delegated authority limits.
  9: RISK DATA
  11: Records and broker inputs reveal which property, cyber, and fleet risks to price.
  21: LAYERS
  12: RATING
  14: Rules turn risk data into prices, coverage limits, exclusions, and referrals.
  13: BINDING
  15: Quote and policy systems issue cover only within the insurer-approved rules.
note: We map the core operating layers that let an MGA assess and bind risks using third-party insurer capacity.
sources:
- claim: Lloyd’s registers delegated binding authority contracts.
  url: https://www.lloyds.com/market-resources/tools/delegated-contract-and-oversight-manager
  date: undated
  quote: It is a mandatory requirement that all binding authorities are registered online in DCOM.
- claim: Lloyd’s standardizes delegated risk, premium and claims data.
  url: https://www.lloyds.com/market-resources/tools/secure-applications
  date: undated
  quote: This online platform standardises the collection, validation, and processing of Delegated Authority data.
- claim: MGA infrastructure combines policy, capacity and regulatory tools.
  url: https://boostinsurance.com/platform/mga-infrastructure/
  date: undated
  quote: Boost’s full-stack infrastructure delivers everything you need to create and manage an insurance program.
- claim: Steadily uses an automated quotation and binding platform.
  url: https://investors.siriuspt.com/press-releases/news-details/2026/SiriusPoint-announces-new-partnership-with-property-MGA-Steadily/default.aspx
  date: '2026-03-25'
  quote: Steadily’s automated underwriting platform is purpose-built for landlord insurance and allows the MGA to offer underwriting, quoting, and binding within minutes.
```

### ed088
```yaml
status: ok
section: Tech and infra
title: What are the tech and infra layers?
page: 2/2
t:
  7: CLAIMS
  10: Claims systems feed early loss alerts and case costs back into pricing and renewals.
  9: CAPACITY
  11: Carrier and reinsurance partners provide the risk budget and review its use.
  21: LAYERS
  12: REPORTING
  14: Risk, premium, and claims files give insurers a clear view of the entire book.
  13: CONTROL
  15: Audit logs, checks, and approval rights keep the MGA inside its binding powers.
note: We separate loss feedback, available insurer capacity, recurring reporting, and authority controls from initial quoting.
sources:
- claim: Delegated data systems process risk, premium and claims files.
  url: https://www.lloyds.com/market-resources/tools/secure-applications
  date: undated
  quote: This online platform standardises the collection, validation, and processing of Delegated Authority data.
- claim: Lloyd’s has a market system to coordinate audits.
  url: https://www.lloyds.com/market-resources/delegated-authorities/systems-and-tools/delegated-audit-manager
  date: undated
  quote: Delegated Audit Manager is an online system that allows the market to manage and monitor the audit of Coverholder and Delegated Claims Administrators (DCAs).
- claim: Delegated underwriting retains insurer accountability.
  url: https://www.lloyds.com/market-resources/delegated-authorities/market-knowledge/delegated-underwriting-guidance/
  date: '2026'
  quote: Delegated underwriting remains a core and valuable part of the Lloyd’s market.
- claim: MGA infrastructure covers policy and claims management.
  url: https://boostinsurance.com/platform/mga-infrastructure/
  date: undated
  quote: Boost’s full-stack infrastructure delivers everything you need to create and manage an insurance program.
```

### ed089
```yaml
status: ok
section: Tech and infra
title: Does every layer carry the same weight?
t:
  38: RANKING
  6: LOSS DATA
  14: Shows which risks actually lose money and tells the MGA when prices must change.
  7: RISK MODEL
  24: Selects and prices risks before bind, shaping claims costs and the value of each book.
  8: CAPACITY
  26: Determines how much cover can be sold and whether the insurer will keep backing it.
  9: CONTROLS
  28: Proves every policy was bound within granted limits and meets insurer rules.
  10: CLAIMS
  30: Turns incidents and case reserves into insight, but often too late for new quotes.
  11: DISASTERS
  32: Maps shared exposures so one storm or outage does not hit too many policies.
  12: ISSUANCE
  34: Converts approved quotes into policies fast, lowering friction once terms are sound.
  13: APIS
  36: Connects brokers and carriers, but cleaner pipes cannot repair weak risk pricing.
note: We rank layers by their effect on underwriting profit, carrier confidence, and speed. This is a directional assessment.
sources:
- claim: Carrier oversight and performance data are core delegated underwriting duties.
  url: https://www.lloyds.com/market-resources/delegated-authorities/market-knowledge/delegated-underwriting-guidance/
  date: '2026'
  quote: Delegated underwriting remains a core and valuable part of the Lloyd’s market.
- claim: Accelerant combines exposure and claims data for risk analysis.
  url: https://www.sec.gov/Archives/edgar/data/1997350/000199735026000003/arx-20251231.htm
  date: '2026'
  quote: We continue to make significant investments in the development of our data, analytics, and AI.
- claim: Lloyd’s processes delegated risk, premium and claims reporting.
  url: https://www.lloyds.com/market-resources/tools/secure-applications
  date: undated
  quote: This online platform standardises the collection, validation, and processing of Delegated Authority data.
```

### ed090
```yaml
status: ok
section: Tech and infra
title: Where does 80% of MGA tech value sit?
comment: The 80% in the title is a qualitative prioritization prompt, not a measured industry value share.
t:
  9: '💰 💰 💰 💰 💰 💰 💰 💰 💰

    💰 💰 💰 💰 💰 💰 💰 💰 💰

    💰 💰 💰 💰 💰 💰 💰 💰 💰

    💰 💰 💰 💰 💰 💰 💰 💰 💰

    💰 💰 💰 💰 💰 💰 💰 💰 💰

    💰 💰 💰 💰 💰 💰 💰 💰 💰

    💰 💰 💰 💰 💰 💰 💰 💰 💰

    💰 💰 💰 💰 💰 💰 💰 💰 💰

    💰 💰 💰 💰 💰 💰 💰 💰 💰

    💰 💰 💰 💰 💰 💰 💰 💰 💰'
  8: 'The highest value sits in risk selection and pricing. Better loss data helps an MGA decide what to insure, what to decline, and how much to charge.


    Next comes portfolio monitoring: carriers need to see clusters of risk, fresh claims, and whether the program stays within its limits.


    Digital quotes, policy issuance, and clean reporting matter too. Yet speed alone cannot rescue a book that is priced below the true cost of claims.'
note: We use a qualitative value map, not a verified 80% revenue split. Risk economics and carrier trust drive the ranking.
sources:
- claim: Accelerant ties its data platform to underwriting intelligence and portfolio monitoring.
  url: https://www.sec.gov/Archives/edgar/data/1997350/000199735026000003/arx-20251231.htm
  date: '2026'
  quote: We continue to make significant investments in the development of our data, analytics, and AI.
- claim: Lloyd’s stresses performance, exposure and ongoing delegated oversight.
  url: https://www.lloyds.com/market-resources/delegated-authorities/market-knowledge/delegated-underwriting-guidance/
  date: '2026'
  quote: Delegated underwriting remains a core and valuable part of the Lloyd’s market.
- claim: Coalition will price, develop products and manage claims for a carrier portfolio.
  url: https://www.coalitioninc.com/en-gb/announcements/coalition-and-allianz-commercial-expand-strategic-global-cyber-insurance-partnership
  date: '2026-05-06'
  quote: Allianz will transition its commercial cyber insurance business to Coalition.
```

### ed091
```yaml
status: ok
section: Tech and infra
title: How has tech and infra evolved over the years?
t:
  6: '2017 - 2020


    Specialist MGAs paired online quotes with insurer paper, while Lloyd’s began central data checks for delegated policies.'
  7: '2021 - 2023


    Cyber scanning, fleet sensors, and API-based program tools gave new MGAs more live risk data before bind.'
  8: '2024 - 2025


    Cloud-outage models supported a new bond, fleet data drew new insurer support, and AI reached more underwriting steps.'
  9: 'TODAY


    MGAs use AI to read submissions, score unusual risks, and monitor books. Carriers demand deeper data and loss proof.'
  10: '?


    Next tools may join real-time claims, shared risk profiles, instant approvals, and adaptive prices within carrier-set limits.'
note: We trace the shift from digital distribution to continuous underwriting, using reported product and market infrastructure milestones.
sources:
- claim: Lloyd’s introduced delegated data processing tools.
  url: https://www.lloyds.com/market-resources/tools/secure-applications
  date: undated
  quote: This online platform standardises the collection, validation, and processing of Delegated Authority data.
- claim: Coalition used security scanning tools to expand cyber risk services.
  url: https://www.coalitioninc.com/announcements/msad-insurance-group-partnership
  date: '2023-10-04'
  quote: MS&AD Cyber Risk Finder is currently available to the entire Japanese SMB market.
- claim: Parametrix supplied modeling for a cloud-outage catastrophe bond.
  url: https://www.parametrixinsurance.com/in-the-news/first-ever-cloud-outage-ils
  date: '2024-04-15'
  quote: Parametrix acts as modeling and calculation agent on the annual bonds.
- claim: Nirvana used vehicle data and gained reinsurance support.
  url: https://www.nirvanatech.com/blog/nirvana-insurance-announces-new-top-tier-reinsurers-and-doubling-of-capacity
  date: '2024-10-15'
  quote: As we secure top-tier reinsurers and expand our capabilities, we’re looking forward to further opportunities to transform the commercial insurance landscape.
- claim: Cowbell released an AI-native specialty underwriting system.
  url: https://cowbell.insure/news-events/pr/cowbell-launches-omni-an-ai-native-decision-intelligence-system/
  date: '2026-07-28'
  quote: OMNI accelerates Cowbell’s new product deployment cycle to six weeks, expediting expansion to Europe and Asia
```

### ed092
```yaml
status: ok
section: Tech and infra
title: What were the latest tech and infra developments?
page: 1/2
t:
  13: '2023'
  14: Coalition and MS&AD brought a cyber risk scanner to Japan, giving small firms security checks before purchase.
  15: '2024'
  16: Parametrix modeled the first cloud-outage catastrophe bond for Hannover Re, adding a new source of risk capacity.
  17: '2024'
  18: Nirvana added top reinsurers and doubled its insurance capacity, using truck driving data and AI to assess fleet risks.
  19: '2025'
  20: Coalition launched a new US Active Cyber Policy that rewards stronger security with more tailored cover and policy terms.
  21: '2025'
  22: HDI Global and Descartes launched parametric earthquake cover in Japan, linking payouts to measured seismic events.
  23: '2025'
  24: Accelerant described a Risk Exchange that joins policy and claims records, letting partners monitor risks on shared data.
note: We select dated changes that show technology moving into a live MGA program, capacity decision, or measurable risk workflow.
sources:
- claim: Coalition and MS&AD launched a cyber risk assessment service in Japan.
  url: https://www.coalitioninc.com/announcements/msad-insurance-group-partnership
  date: '2023-10-04'
  quote: MS&AD Cyber Risk Finder is currently available to the entire Japanese SMB market.
- claim: Parametrix modeled the first cloud-outage catastrophe bond.
  url: https://www.parametrixinsurance.com/in-the-news/first-ever-cloud-outage-ils
  date: '2024-04-15'
  quote: Parametrix acts as modeling and calculation agent on the annual bonds.
- claim: Nirvana announced new reinsurance partners and doubled capacity.
  url: https://www.nirvanatech.com/blog/nirvana-insurance-announces-new-top-tier-reinsurers-and-doubling-of-capacity
  date: '2024-10-15'
  quote: As we secure top-tier reinsurers and expand our capabilities, we’re looking forward to further opportunities to transform the commercial insurance landscape.
- claim: Coalition introduced its new US Active Cyber Policy.
  url: https://www.coalitioninc.com/de/announcements/coalition-launches-new-active-cyber-policy
  date: '2025-04-09'
  quote: Beginning April 15, 2025, all non-admitted new business and renewal quotes in the US will be issued on this new form.
- claim: HDI Global and Descartes developed earthquake cover in Japan.
  url: https://descartesunderwriting.com/newsroom/hdi-global-se-collaboration-descartes-obtains-approval-launch-new-parametric-earthquake
  date: '2025-07-14'
  quote: HDI Global collaborated with Descartes Underwriting SA (Head Office, Paris, France), a world leader in corporate parametric insurance solutions for natural catastrophic risks.
- claim: Accelerant disclosed its shared technology and underwriting data platform.
  url: https://www.sec.gov/Archives/edgar/data/1997350/000199735025000004/arx-20250630.htm
  date: '2025'
  quote: Exchange Services and MGA Operations are both fee-based businesses.
```

### ed093
```yaml
status: ok
section: Tech and infra
title: What were the latest tech and infra developments?
page: 2/2
t:
  13: '2026'
  14: Descartes added parametric protection for data centers against weather disasters, using measurable triggers for faster losses.
  15: '2026'
  16: Shepherd set out an AI workflow to read submissions, enrich data and price construction risks, with underwriters on exceptions.
  17: '2026'
  18: Coalition and Allianz agreed to combine cyber risk tools with insurer reach, giving Coalition pricing and claims responsibility.
  19: '2026'
  20: Cowbell launched OMNI to unify risk data and underwriting rules, and said it can launch new specialty products in six weeks.
  21: '2026'
  22: AIG and Parametrix added an outage-based cyber feature, with a preset formula to pay covered cloud disruption losses.
  23: '2026'
  24: Cowbell announced a standalone AI liability policy using signals on AI autonomy and control, but sales begin in January 2027.
note: We report announced technology changes and mark products not yet on sale. Company statements do not establish loss profitability.
sources:
- claim: Descartes launched disaster-triggered protection for data centers.
  url: https://descartesunderwriting.com/newsroom/descartes-launches-parametric-insurance-protection-140m-data-centers
  date: '2026-01-22'
  quote: Flexible capacity of up to $140 million per policy for earthquake and hurricane risks is available for projects and operational data centers
- claim: Shepherd published its AI-assisted underwriting roadmap.
  url: https://www.withshepherd.com/blog/behind-our-42m-series-b
  date: '2026-03-24'
  quote: We've mapped underwriting to an autonomy framework, similar to self-driving vehicles.
- claim: Coalition and Allianz announced global cyber portfolio delegation.
  url: https://www.coalitioninc.com/en-gb/announcements/coalition-and-allianz-commercial-expand-strategic-global-cyber-insurance-partnership
  date: '2026-05-06'
  quote: Allianz will transition its commercial cyber insurance business to Coalition.
- claim: Cowbell launched its OMNI underwriting intelligence system.
  url: https://cowbell.insure/news-events/pr/cowbell-launches-omni-an-ai-native-decision-intelligence-system/
  date: '2026-07-28'
  quote: OMNI accelerates Cowbell’s new product deployment cycle to six weeks, expediting expansion to Europe and Asia
- claim: AIG launched outage-triggered cyber protection using Parametrix.
  url: https://aig.gcs-web.com/news-releases/news-release-details/aig-expands-cyber-insurance-offering-help-businesses-manage
  date: '2026-08-13'
  quote: AIG’s new Parametric Cloud Outage Solution triggers are based on a predefined formula that considers cloud service downtime and the associated potential financial impact.
- claim: Cowbell announced specialized AI liability risk factors.
  url: https://cowbell.insure/news-events/pr/cowbell-launches-standalone-ai-liability-insurance-for-u-s-smes/?trk=public_post_comment-text
  date: '2026-11-10'
  quote: Underwriting incorporates three AI-specific Cowbell Factors™ assessing AI observability, autonomy, and governance, alongside other risk signals.
- claim: Cowbell states the AI liability product is not available until January 2027.
  url: https://cowbell.insure/news-events/pr/cowbell-launches-standalone-ai-liability-insurance-for-u-s-smes/?trk=public_post_comment-text
  date: '2026-11-10'
  quote: Cowbell AI Liability Insurance will be available exclusively through wholesale brokers on a non-admitted basis beginning January 1, 2027.
```

### ed094
```yaml
status: ok
section: Tech and infra
title: What are the solvable bottlenecks?
t:
  39: BOTTLENECK
  38: EXPLANATION
  41: BOTTLENECK
  40: EXPLANATION
  7: DATA GAPS
  5: Broker forms and claims files arrive in mixed formats, leaving too many risk fields missing.
  11: LOSS DELAY
  9: Claims are reported and settled after a delay, so weak prices may look sound for months.
  15: RISK CLUMPS
  13: Many policies can face the same storm or cloud outage across distant clients.
  19: MODEL DRIFT
  17: Models can miss loss patterns as customer behavior, threats, and weather change.
  24: CAPACITY FIT
  22: A sound program still needs a carrier willing to support its risks and limits.
  28: BINDING APIS
  26: MGA and insurer systems need custom links to quote, bind, and share changes.
  32: AUDIT PROOF
  30: Delegated decisions need an audit record of the limits, checks, and approval used.
  36: CLAIM LINKS
  34: Loss updates need to reach pricing teams before renewal prices are set.
note: We focus on engineering gaps that can be improved with shared data, controls, automation, and better loss feedback.
sources:
- claim: Lloyd’s delegates risk, premium and claims data processing.
  url: https://www.lloyds.com/market-resources/tools/secure-applications
  date: undated
  quote: This online platform standardises the collection, validation, and processing of Delegated Authority data.
- claim: Lloyd’s coordinates delegated audits.
  url: https://www.lloyds.com/market-resources/delegated-authorities/systems-and-tools/delegated-audit-manager
  date: undated
  quote: Delegated Audit Manager is an online system that allows the market to manage and monitor the audit of Coverholder and Delegated Claims Administrators (DCAs).
- claim: Lloyd’s calls for high-quality data, exposure monitoring and ongoing oversight.
  url: https://www.lloyds.com/market-resources/delegated-authorities/market-knowledge/delegated-underwriting-guidance/
  date: '2026'
  quote: Delegated underwriting remains a core and valuable part of the Lloyd’s market.
- claim: Accelerant collects exposure and claims information from fragmented systems.
  url: https://www.sec.gov/Archives/edgar/data/1997350/000199735026000003/arx-20251231.htm
  date: '2026'
  quote: We continue to make significant investments in the development of our data, analytics, and AI.
- claim: Cloud-outage products show accumulated common-event exposure.
  url: https://www.parametrixinsurance.com/in-the-news/cumulus-re-cat-bond-renews-75-larger
  date: '2026-04-08'
  quote: Cumulus Re was not triggered during its first two years.
```

### ed095
```yaml
status: ok
section: Tech and infra
title: Why can’t we solve them yet?
t:
  39: BOTTLENECK
  38: REASON WHY
  41: BOTTLENECK
  40: REASON WHY
  7: DATA GAPS
  5: Insurers, brokers, and MGAs use different fields, documents, and definitions for the same risk.
  11: LOSS DELAY
  9: Large losses can take years to settle, so the newest data may still understate costs.
  15: RISK CLUMPS
  13: Events can hit regions or shared vendors beyond what a policy file reveals.
  19: MODEL DRIFT
  17: Past loss models may miss shifts in rates, weather, cyber threats, and claims.
  24: CAPACITY FIT
  22: Carriers differ in risk appetite, limits, required data, and return goals.
  28: BINDING APIS
  26: Older systems lack common APIs, so teams map policy fields and rules by hand.
  32: AUDIT PROOF
  30: Rules differ by carrier, while human overrides can escape system logs.
  36: CLAIM LINKS
  34: Adjusters, vendors, and carriers store loss details apart from the MGA price model.
note: We treat these as data, process, and incentive problems, not failures that a single AI feature can solve.
sources:
- claim: Delegated data needs collection, validation and processing.
  url: https://www.lloyds.com/market-resources/tools/secure-applications
  date: undated
  quote: This online platform standardises the collection, validation, and processing of Delegated Authority data.
- claim: Lloyd’s guidance stresses carrier-specific controls and accumulation monitoring.
  url: https://www.lloyds.com/market-resources/delegated-authorities/market-knowledge/delegated-underwriting-guidance/
  date: '2026'
  quote: Delegated underwriting remains a core and valuable part of the Lloyd’s market.
- claim: Accelerant describes structured and unstructured risk and claims information.
  url: https://www.sec.gov/Archives/edgar/data/1997350/000199735026000003/arx-20251231.htm
  date: '2026'
  quote: We continue to make significant investments in the development of our data, analytics, and AI.
- claim: Delegated coverholder audits require coordination.
  url: https://www.lloyds.com/market-resources/delegated-authorities/systems-and-tools/delegated-audit-manager
  date: undated
  quote: Delegated Audit Manager is an online system that allows the market to manage and monitor the audit of Coverholder and Delegated Claims Administrators (DCAs).
```

### ed096
```yaml
status: ok
section: Tech and infra
title: When can we realistically expect to solve them?
comment: Dates are analyst scenario milestones for broadly practical improvements, not announced completion dates or industry consensus forecasts.
t:
  39: BOTTLENECK
  38: WHY THIS TIMELINE
  41: BOTTLENECK
  40: WHY THIS TIMELINE
  7: DATA GAPS
  5: Common intake fields and AI extraction can help soon, but partner systems still need matching rules.
  42: '2028'
  11: LOSS DELAY
  9: Better early loss estimates can improve decisions, but some large claims still take years to resolve.
  43: '2031'
  15: RISK CLUMPS
  13: Event maps can improve fast, but hidden links between risks need more complete data.
  44: '2029'
  19: MODEL DRIFT
  17: Ongoing tests can catch weaker prices, yet fast-changing risk types will still surprise models.
  45: '2030'
  24: CAPACITY FIT
  22: Shared book metrics can speed carrier review, but risk appetite and financial cycles remain human.
  46: '2030'
  28: BINDING APIS
  26: Standard APIs can spread, but older policy and finance systems take years to replace.
  47: '2029'
  32: AUDIT PROOF
  30: Digital approval logs can mature quickly, while each carrier still needs tailored checks.
  48: '2028'
  36: CLAIM LINKS
  34: Claims feeds can become near real time, but matching reserve changes to policy data takes work.
  49: '2029'
note: We give directional timelines for usable tools, not a date when risk vanishes. Capital decisions and late claims still need judgment.
sources:
- claim: Lloyd’s guidance supports standardized reporting, oversight, and risk concentration checks.
  url: https://www.lloyds.com/market-resources/delegated-authorities/market-knowledge/delegated-underwriting-guidance/
  date: '2026'
  quote: Delegated underwriting remains a core and valuable part of the Lloyd’s market.
- claim: Lloyd’s operates shared delegated data processing infrastructure.
  url: https://www.lloyds.com/market-resources/tools/secure-applications
  date: undated
  quote: This online platform standardises the collection, validation, and processing of Delegated Authority data.
- claim: Accelerant illustrates the work needed to combine and govern multiple data sources.
  url: https://www.sec.gov/Archives/edgar/data/1997350/000199735026000003/arx-20251231.htm
  date: '2026'
  quote: We continue to make significant investments in the development of our data, analytics, and AI.
```

### ed097
```yaml
status: ok
section: Tech and infra
title: Which bold bets could reshape MGA tech?
t:
  9: LIVE LOSS FEED
  7: It is a claims signal that flags rising loss costs before an MGA quotes or renews cover.
  12: DYNAMIC PRICE
  10: It is a price model that adapts to new fleet, cyber, or property data within insurer-set limits.
  15: AUTO BIND RULES
  13: It is quote-to-policy software that checks limits and issues cover with few manual steps.
  18: STORM RISK MAP
  16: It is a live view of storm, flood, and cloud exposure across every policy in a shared book.
  33: 'NEAR-TERM HORIZON

    (0-5 YEARS)'
  21: ALWAYS ON COVER
  19: It is continuous risk review that suggests safer actions and better renewal terms all year.
  24: RISK DATA PORTAL
  22: It is a risk profile shared across brokers, MGAs, and carriers with consent.
  27: CAPACITY ROUTER
  25: It is a rules engine that directs each risk to an insurer with the right appetite.
  30: FAST CLAIM PAYOUT
  28: It is fast payment for clear events, while complex losses still get human review.
  34: 'LONG-TERM HORIZON

    (5-10 YEARS)'
note: We frame these as potential applications of tools already visible in specialist MGAs, not guaranteed future products.
sources:
- claim: Lloyd’s provides guidance for data quality and ongoing delegated oversight.
  url: https://www.lloyds.com/market-resources/delegated-authorities/market-knowledge/delegated-underwriting-guidance/
  date: '2026'
  quote: Delegated underwriting remains a core and valuable part of the Lloyd’s market.
- claim: API infrastructure supports program administration.
  url: https://boostinsurance.com/
  date: undated
  quote: Our platform packages the necessary compliance, capital, and technology needed to power an insurance program, into a single API-based solution.
- claim: Parametric cover depends on measurable independent triggers.
  url: https://descartesunderwriting.com/faq
  date: undated
  quote: Parametric insurance does not cover events that cannot be measured by an objective, independent index.
- claim: Cowbell is building AI-assisted underwriting workflows.
  url: https://cowbell.insure/news-events/pr/cowbell-launches-omni-an-ai-native-decision-intelligence-system/
  date: '2026-07-28'
  quote: OMNI accelerates Cowbell’s new product deployment cycle to six weeks, expediting expansion to Europe and Asia
- claim: Cover Whale connects ongoing vehicle data to risk management.
  url: https://help.coverwhale.com/knowledge/how-does-the-cover-whale-driver-safety-program-work
  date: '2026-08-04'
  quote: Cover Whale's Driver Safety Program uses telematics data, coaching, and coverage to promote safer driving and lower insurance costs for truck drivers.
```

### ed098
```yaml
status: ok
section: Tech and infra
title: Which companies are working on groundbreaking tech today?
t:
  8: PARAMETRIX
  6: They measure cloud uptime and use that data to price outages and automate payouts.
  24: COVER WHALE
  22: They use truck sensor data and driver coaching to adjust fleet risk before renewal.
  11: SHEPHERD
  9: They connect jobsite software usage to building risk models and contractor pricing.
  27: ARBOL
  25: They price weather risks with parametric data and models under delegated reinsurance power.
  14: COALITION
  12: They scan cyber exposures and pair live security tools with delegated underwriting.
  30: COWBELL
  28: They use AI risk scores and policy data to assess cyber and emerging AI incidents.
  17: STEADILY
  15: They run automated landlord quotes and binding with live property risk oversight.
  33: NIRVANA
  31: They turn truck driving data into faster fleet risk scores, quotes, and safety tips.
logos:
- name: Parametrix
  domain: parametrixinsurance.com
- name: Cover Whale
  domain: coverwhale.com
- name: Shepherd
  domain: withshepherd.com
- name: Arbol Underwriters
  domain: arbolunderwriters.com
- name: Coalition
  domain: coalitioninc.com
- name: Cowbell
  domain: cowbell.insure
- name: Steadily
  domain: steadily.com
- name: Nirvana Insurance
  domain: nirvanatech.com
note: We select specialist underwriting businesses with documented risk technology. Features are company-reported, not proof of profit.
sources:
- claim: Parametrix operates as a monitoring-led MGA and coverholder.
  url: https://www.parametrixinsurance.com/in-the-news/critical-cloud-outage-events-down-in-2025-but-outage-risk-remains-significant
  date: '2026-03-30'
  quote: The company is a Managing General Agent and Lloyd’s Coverholder, with policies backed by major A-rated global insurers, and is headquartered in New York.
- claim: Cover Whale uses connected vehicle data and coaching.
  url: https://help.coverwhale.com/knowledge/how-does-the-cover-whale-driver-safety-program-work
  date: '2026-08-04'
  quote: Cover Whale's Driver Safety Program uses telematics data, coaching, and coverage to promote safer driving and lower insurance costs for truck drivers.
- claim: Shepherd uses real construction-technology activity in underwriting.
  url: https://www.withshepherd.com/savings
  date: undated
  quote: By incorporating verified activity and usage data into our underwriting process, Shepherd can offer insurance proposals with premium savings of up to 25%.
- claim: Arbol Underwriters has delegated parametric reinsurance authority.
  url: https://www.arbolunderwriters.com/
  date: undated
  quote: AUL is authorized by SIG Re, a class 3A insurer in Bermuda, to underwrite general parametric reinsurance on a fully collateralized basis.
- claim: Coalition is responsible for cyber risk pricing and management under carrier delegation.
  url: https://www.coalitioninc.com/en-gb/announcements/coalition-and-allianz-commercial-expand-strategic-global-cyber-insurance-partnership
  date: '2026-05-06'
  quote: Allianz will transition its commercial cyber insurance business to Coalition.
- claim: Cowbell uses specialized AI risk factors to underwrite emerging exposures.
  url: https://cowbell.insure/news-events/pr/cowbell-launches-standalone-ai-liability-insurance-for-u-s-smes/?trk=public_post_comment-text
  date: '2026-11-10'
  quote: Underwriting incorporates three AI-specific Cowbell Factors™ assessing AI observability, autonomy, and governance, alongside other risk signals.
- claim: Steadily uses automated quote and bind technology.
  url: https://investors.siriuspt.com/press-releases/news-details/2026/SiriusPoint-announces-new-partnership-with-property-MGA-Steadily/default.aspx
  date: '2026-03-25'
  quote: Steadily’s automated underwriting platform is purpose-built for landlord insurance and allows the MGA to offer underwriting, quoting, and binding within minutes.
- claim: Nirvana deploys AI against fleet and driver data.
  url: https://www.nirvanatech.com/blog/nirvanas-ai-first-approach-recognized-in-cb-insights-insurtech-50-for-2025
  date: '2025'
  quote: Our AI driver summary also analyzes and flags key characteristics in driver pools, accelerating review.
```

### iv_pipeline
```yaml
status: ok
section: Tech and infra
title: Which new MGA programs got insurer backing lately?
comment: The row sequence follows the fixed 8-row template rather than chronological order. LIVE means the underlying line was operating or had capacity backing, not verified underwriting profit.
t:
  38: LAUNCH
  34: Accident and health cover for global specialty accounts
  37: CORSIAM · LLOYDS 3123
  27: LIVE
  26: VIKCO · FORTEGRA
  24: Builder risk cover for residential projects across the US
  23: LAUNCH
  22: BANYAN RISK · ACCREDITED
  20: Inland marine and property cover for US transit and logistics
  19: LAUNCH
  18: KYNTRA · ALLIED WORLD
  16: Property risk cover for buildings and operating sites
  15: LIVE
  12: General liability cover for smaller US trade contractors
  14: ISC · SIRIUSPOINT
  11: LAUNCH
  10: SHEPHERD · CORE SPECIALTY
  8: Workers compensation for construction and energy firms
  7: LIVE
  6: STEADILY · SIRIUSPOINT
  4: Landlord property insurance with fast automated policy binding
  3: LAUNCH
  2: ATA · ARCH
  0: Large AI data center projects across property, cargo, and cyber
note: We include dated 2025 and 2026 programs with a named insurer or Lloyd’s backer. Launches alone do not prove loss performance.
sources:
- claim: Corsiam launched A&H underwriting backed by Lloyd’s Syndicate 3123.
  url: https://www.insurancejournal.com/news/international/2025/09/30/841095.htm
  date: '2025-09-30'
  quote: Backed by The Fidelis Partnership Syndicate 3123 at Lloyd’s, Corsiam will underwrite a broad portfolio of global A&H insurance and reinsurance business.
- claim: Vikco launched a builder’s risk program on Fortegra paper.
  url: https://www.theinsurer.com/bdbb44589559/program-manager/news/k2s-vikco-launches-new-fortegra-capacity-backed-builders-risk-program-2025-01-14/
  date: '2025-01-14'
  quote: The new program is written on the paper of Rick Kahlbaugh-led Fortegra Group
- claim: Banyan launched inland marine cover backed by Accredited.
  url: https://www.theinsurer.com/program-manager/news/banyan-risk-launches-us-inland-marine-product-backed-by-accredited-2026-08-19/
  date: '2026-08-19'
  quote: Banyan Risk has launched a U.S. inland marine and marine property product, backed by capacity from Accredited Insurance Limited, the specialty MGA said on Wednesday.
- claim: Kyntra launched property business with Allied World capacity.
  url: https://www.theinsurer.com/ti/news/allied-world-provides-capacity-for-kyntra-launch-2026-10-07/
  date: '2026-10-07'
  quote: Allied World is providing capacity for property MGA Kyntra, which will offer a maximum line size of $35 million, the company told The Insurer.
- claim: SiriusPoint supplied capacity to ISC for its contractor liability program.
  url: https://investors.siriuspt.com/press-releases/news-details/2026/SiriusPoint-announces-new-partnership-with-ISC/default.aspx
  date: '2026-01-15'
  quote: The partnership predominantly focuses on ISC’s flagship general liability program, which is designed to provide cost-effective insurance solutions for small contractors.
- claim: Shepherd launched workers compensation through Core Specialty insurer paper.
  url: https://www.withshepherd.com/blog/introducing-new-workers-compensation-program
  date: '2026-09-30'
  quote: Today, Shepherd is announcing a new Workers’ Compensation offering.
- claim: SiriusPoint supplied capacity to landlord MGA Steadily.
  url: https://investors.siriuspt.com/press-releases/news-details/2026/SiriusPoint-announces-new-partnership-with-property-MGA-Steadily/default.aspx
  date: '2026-03-25'
  quote: Steadily’s automated underwriting platform is purpose-built for landlord insurance and allows the MGA to offer underwriting, quoting, and binding within minutes.
- claim: ATA launched AI infrastructure cover backed by Arch and other carriers.
  url: https://www.theinsurer.com/ti/news/ata-launches-750-million-facility-for-global-ai-infrastructure-2026-01-13/
  date: '2026-01-13'
  quote: Arch Insurance International, Munich Re Specialty and Scor are among backers
```
