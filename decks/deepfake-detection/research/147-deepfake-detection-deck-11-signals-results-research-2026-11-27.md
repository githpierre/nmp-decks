# Deepfake detection - Signal slides - research 2026-11-27

11 candidates kept, ranked by total score. 6 of them are Market opportunity candidates with fresh data (2026).

Formats tried and dropped (no candidate passed its "keep only if" test, or the data was not solid enough):
- rules-wave: Ballotpedia counts 58 deepfake bills enacted by late July 2026 against 64 at the same point of 2025, so the last bar does not jump, and no full-year counts are published. Kept the state count as a key-trend instead.
- forecast-gap: we found only 2 publishers sizing deepfake detection alone for the same year (LP Information, $1,886M in 2030, and one outlier range of $80B to $150B). The other forecasts cover deepfake generation too.
- earnings-mentions, lobbying-spend: no published series (Pindrop's 2025 federal lobbying of $460K has no earlier years to compare).
- kpi-trio: Pindrop has 3 strong numbers ($100M+ ARR, 385M calls authenticated in 2025, $283M of fraud avoided in 2025) but no published growth rate.
- single-customer: authID reports 3 clients making 72% of revenue, but no single client share.
- value-ladder: only one $1B+ player (Persona at $2B).
- A third and fourth key-trend (Entrust detection frequency, from one every 5 minutes in 2024 to one every 3 minutes in 2026, and the Deepfake-Eval-2024 accuracy drop) were cut to respect 2 candidates per format. The second is used on the "Why do deepfake detection startups fail?" slide.
- Funding-round formats are left to our own database, as asked.

### 1. key-trend (total 18)
```yaml
format: key-trend
title: AI-driven attacks seen by Pindrop rose 1,680% in recent quarters
chapter: Market opportunity
why_it_matters: AI-driven attacks on call centers grow faster than any other threat Pindrop tracks, so buyers need detection now. Pindrop says these attacks grow eight times faster than traditional ones.
data:
  - {label: Q4 2024, value: 100, unit: index of AI-driven attacks, date: 2024-12}
  - {label: June 2026, value: 1780, unit: index of AI-driven attacks, date: 2026-06}
  - {label: Increase, value: 1680, unit: '%', date: 2024-12 to 2026-06}
note: We index Pindrop's Q4 2024 level of AI-driven attacks to 100 and apply the 1,680% rise it reported through June 2026 in its 2026 Deepfake Readiness Index.
fresh: {period: month, end: 2026-06}
scores: {surprise: 4, importance: 5, clarity: 5, durability: 4}
sources:
  - {claim: AI-driven attacks up 1,680% from Q4 2024 through June 2026, url: 'https://www.biometricupdate.com/202609/deepfakes-are-overwhelming-businesses-unprepared-to-deal-with-ai-threat-pindrop', date: '2026-09-28', quote: 'AI-driven attacks increased 1,680 percent from Q4 2024 through June 2026'}
  - {claim: AI-driven attacks grow eight times faster than traditional ones, url: 'https://www.biometricupdate.com/202609/deepfakes-are-overwhelming-businesses-unprepared-to-deal-with-ai-threat-pindrop', date: '2026-09-28', quote: 'growing eight times faster than traditional attack types.'}
```

### 2. funnel (total 18)
```yaml
format: funnel
title: 93% of security leaders fear deepfakes, only 10% deploy detection
chapter: Market opportunity
why_it_matters: Almost every security leader worries about deepfakes but very few have bought a tool, so most of the market is still unserved. That gap is the room left for detection vendors.
data:
  - {label: Worried they are not prepared, value: 93, unit: '% of security leaders', date: 2026-09}
  - {label: Hit by or suspect a deepfake attack in the past year, value: 74, unit: '% of security leaders (nearly three-quarters, estimate)', date: 2026-09}
  - {label: Deploying deepfake detection tools, value: 10, unit: '% of security leaders', date: 2026-09}
note: We use Pindrop's 2026 Deepfake Readiness Index survey of security leaders, published in September 2026. We read "nearly three-quarters" as about 74%.
fresh: {period: total, end: 2026-09}
scores: {surprise: 4, importance: 5, clarity: 5, durability: 4}
sources:
  - {claim: 93% of leaders worry they are not prepared, url: 'https://www.biometricupdate.com/202609/deepfakes-are-overwhelming-businesses-unprepared-to-deal-with-ai-threat-pindrop', date: '2026-09-28', quote: '93 percent of leaders are concerned they aren''t prepared for a deepfake attack.'}
  - {claim: Nearly three-quarters encountered or suspect an attack, url: 'https://helpnetsecurity.com/2026/09/29/pindrop-enterprise-deepfake-attacks-report', date: '2026-09-29', quote: 'Nearly three-quarters of security leaders have encountered or suspect a deepfake attack in the past year'}
  - {claim: Only 10% deploy deepfake detection tools, url: 'https://www.biometricupdate.com/202609/deepfakes-are-overwhelming-businesses-unprepared-to-deal-with-ai-threat-pindrop', date: '2026-09-28', quote: 'only 10 percent are deploying deepfake detection tools to catch them.'}
```

### 3. icon-grid (total 18)
```yaml
format: icon-grid
title: Only 2 of 2,000 people spotted every deepfake in a test
chapter: Market opportunity
why_it_matters: People cannot tell real from fake by eye, so companies have to buy machines to check calls, faces and files. Participants were told to look for fakes and still failed.
data:
  - {label: Participants, value: 2000, unit: people in the UK and US, date: 2025-02}
  - {label: Got every item right, value: 2, unit: people, date: 2025-02}
  - {label: Share with a perfect score, value: 0.1, unit: '%', date: 2025-02}
note: We use iProov's test of 2,000 UK and US consumers shown real and deepfake images and videos, published in February 2025.
fresh: {period: total, end: 2025-02}
scores: {surprise: 4, importance: 4, clarity: 5, durability: 5}
sources:
  - {claim: Only 0.1% identified all real and fake stimuli, url: 'https://www.businesswire.com/news/home/20250211131029/en', date: '2025-02-12', quote: 'Just 0.1% of respondents correctly identified all deepfake and real stimuli (e.g., images and videos)'}
  - {claim: 0.1% means two of 2,000 participants, url: 'https://techradar.com/pro/in-a-test-2000-people-were-shown-deepfake-content-only-one-of-them-managed-to-get-a-perfect-score', date: '2025-02-13', quote: 'finding only 0.1% of participants - two whole people - correctly distinguished between real and deepfake stimuli.'}
```

### 4. deal-timeline (total 17)
```yaml
format: deal-timeline
title: HR, audit and identity giants keep buying into deepfake detection
chapter: Market opportunity
why_it_matters: Large buyers from identity, HR, telecom and audit are paying to own detection, which shows the market is hot right now. Each deal also gives startups a clear exit path.
data:
  - {label: Entrust closes Onfido purchase, value: $650M, unit: reported price, date: 2024-04}
  - {label: Hiya buys Loccus.ai, value: undisclosed, unit: '', date: 2024-07}
  - {label: Cheq buys Deduce, value: undisclosed, unit: '', date: 2025-01}
  - {label: LexisNexis Risk Solutions closes IDVerse purchase, value: undisclosed, unit: '', date: 2025-02}
  - {label: Deel buys Clarity, value: $45M, unit: 'estimate, midpoint of a reported $40M to $50M', date: 2026-08}
  - {label: KPMG takes a minority stake in Reality Defender, value: undisclosed, unit: '', date: 2026-09}
note: We list acquisitions and stakes announced from April 2024 to September 2026, from company releases and trade press. Prices are reported figures where disclosed.
fresh: {period: total, end: 2026-09}
scores: {surprise: 3, importance: 5, clarity: 4, durability: 5}
sources:
  - {claim: Entrust bought Onfido for a reported $650M, url: 'https://techcrunch.com/2024/02/06/confirmed-entrust-is-buying-ai-based-id-verification-startup-onfido-sources-say-for-more-than-400m', date: '2024-02-06', quote: 'Since we published this story, sources close to the deal have confirmed the price is $650 million.'}
  - {claim: Entrust completed the Onfido deal in April 2024, url: 'https://www.lse.co.uk/rns/portfolio-company-onfido-acquired-by-entrust-ji9aqq4uoobxrj1.html', date: '2024-04-09', quote: 'notes the announcement by Entrust that they have completed their acquisition of Onfido'}
  - {claim: Hiya acquired Loccus.ai, url: 'https://www.businesswire.com/news/home/20240725061586/en', date: '2024-07-25', quote: 'Hiya, the leader in global voice security services, has acquired Loccus.ai, the industry leader in deepfake detection solutions.'}
  - {claim: Cheq acquired Deduce (value undisclosed), url: 'https://www.biometricupdate.com/202501/deepfake-detection-platform-deduce-acquired-by-cheq', date: '2025-01-15', quote: 'The company did not disclose the value of the deal.'}
  - {claim: LexisNexis Risk Solutions completed the IDVerse acquisition, url: 'https://www.insurancebusinessmag.com/us/news/breaking-news/lexisnexis-risk-solutions-announces-acquisition-525451.aspx', date: '2025-02-20', quote: 'LexisNexis Risk Solutions, which supplies data insights to the insurance industry, has completed its acquisition of IDVerse'}
  - {claim: Deel acquired Clarity for an estimated $40M to $50M, url: 'https://calcalistech.com/ctechnews/article/bkeyex0sgl', date: '2026-08-03', quote: 'the deal is estimated to be worth approximately $40-50 million, paid in a combination of cash and shares of the acquiring company.'}
  - {claim: KPMG took a minority stake in Reality Defender, url: 'https://kpmg.com/us/en/media/news/kpmg-llp-takes-minority-stake-in-deepfake-detection-leader-reality-defender.html', date: '2026-09-10', quote: 'KPMG LLP Takes Minority Stake in Deepfake Detection Leader Reality Defender'}
```

### 5. incident-count (total 17)
```yaml
format: incident-count
title: AI-linked child abuse reports to NCMEC rose from 4,700 to 400,000+
chapter: Pain points
why_it_matters: Platforms now face a flood of AI-made abuse images that humans cannot review one by one. This is the core demand behind platform screening tools.
data:
  - {label: '2023', value: 4700, unit: CyberTipline reports linked to generative AI, date: 2023-12}
  - {label: '2024', value: 67000, unit: CyberTipline reports linked to generative AI, date: 2024-12}
  - {label: '2025', value: 400000, unit: 'CyberTipline reports linked to generative AI (more than, excluding 1.1M Amazon reports with no actionable information)', date: 2025-12}
note: We use the US National Center for Missing and Exploited Children (NCMEC) yearly counts for 2023 to 2025. NCMEC received 1.5M such reports in 2025, but 1.1M came from Amazon AI Services with no actionable information, so we show the remaining 400,000+.
fresh: {period: year, end: 2025-12}
scores: {surprise: 4, importance: 4, clarity: 4, durability: 5}
sources:
  - {claim: 4,700 reports in 2023, url: 'https://ncmec.org/GAI', date: '2026-03-31', quote: '4,700 CyberTipline reports of GAI from the public and ESPs'}
  - {claim: 67,000 reports in 2024, url: 'https://ncmec.org/GAI', date: '2026-03-31', quote: '67,000 CyberTipline reports of GAI from the public and ESPs'}
  - {claim: 1.5M in 2025, of which 1.1M from Amazon with no actionable information, url: 'https://ncmec.org/GAI', date: '2026-03-31', quote: 'Of this total, 1.1 million were submitted by Amazon AI Services and contained no actionable information.'}
  - {claim: More than 400,000 actionable reports in 2025, url: 'https://cf.missingkids.org/theissues/generative-ai', date: '2026-03-31', quote: 'More than 400,000 CyberTipline reports of GAI from the public and ESPs that can be separated into five categories'}
```

### 6. key-trend (total 17)
```yaml
format: key-trend
title: 48 states now have sexual deepfake laws, up from 29 in mid-2024
chapter: Market opportunity
why_it_matters: New laws force platforms to find and remove fake intimate images fast, which pushes them to buy screening tools now. The federal TAKE IT DOWN Act adds a 48-hour removal duty on top.
data:
  - {label: June 2024, value: 29, unit: states with laws on sexually explicit deepfakes, date: 2024-06}
  - {label: January 2026, value: 46, unit: states with laws on sexually explicit deepfakes, date: 2026-01}
  - {label: August 2026, value: 48, unit: states with laws on sexually explicit deepfakes, date: 2026-08}
note: We use Ballotpedia's AI Deepfake Legislation Tracker counts of US states with laws on sexually explicit (pornographic) deepfakes, from June 2024 to August 2026.
fresh: {period: total, end: 2026-08}
scores: {surprise: 3, importance: 4, clarity: 5, durability: 5}
sources:
  - {claim: 29 states in June 2024, url: 'https://news.ballotpedia.org/?p=37853', date: '2024-06-27', quote: 'As of June 21, 29 states had enacted laws related to pornographic deepfakes.'}
  - {claim: 46 states in January 2026, url: 'https://ballotpedia.org/Deepfake_policy_in_the_United_States,_2019_-_Present', date: '2026-01-09', quote: 'As of January 9, 2026, 46 states had enacted laws concerning the creation or distribution of deepfakes that depict explicit sexual acts'}
  - {claim: 48 states in August 2026, url: 'https://www.finanznachrichten.de/nachrichten-2026-08/69225276-ballotpedia-ballotpedia-reports-forty-eight-states-now-have-laws-addressing-sexually-explicit-deepfakes-296.htm', date: '2026-08-05', quote: '48 states have passed laws addressing sexually explicit deepfakes, up from 46 at the beginning of 2026'}
  - {claim: TAKE IT DOWN Act 48-hour removal duty, url: 'https://www.yahoo.com/news/ai-generated-porn-mr-deepfakes-001406528.html', date: '2025-05-06', quote: 'requires social media platforms and other websites to remove images and videos within 48 hours after a victim''s request.'}
```

### 7. profit-gap (total 16)
```yaml
format: profit-gap
title: authID lost $8.95 per $1 of 2025 sales, Mitek earned 5 cents
chapter: Value creation
why_it_matters: Small listed detection players spend far more than they sell, while the profitable incumbent earns a thin margin. Scale, not technology, decides who survives.
data:
  - {label: authID, value: -8.95, unit: net result in $ per $1 of revenue, date: 2025-12}
  - {label: Cyabra, value: -2.25, unit: net result in $ per $1 of revenue, date: 2025-12}
  - {label: Mitek, value: 0.05, unit: net result in $ per $1 of revenue, date: 2025-09}
note: We divide each company's 2025 net result by its 2025 revenue, from company releases and filings. authID lost $17.9M on $2M, Cyabra $12.82M on $5.71M, and Mitek earned $8.8M on $179.7M in its fiscal year ended September 2025.
fresh: {period: year, end: 2025-12}
scores: {surprise: 4, importance: 3, clarity: 5, durability: 4}
sources:
  - {claim: authID 2025 net loss $17.9M, url: 'https://www.barchart.com/story/news/1073766/authid-reports-financial-and-operating-results-for-the-fourth-quarter-2025', date: '2026-03-31', quote: 'Net loss was $17.9 million, or $1.38 per share, compared to a loss of $14.3 million, or $1.40 per share a year ago.'}
  - {claim: authID 2025 net revenue $2M, url: 'https://www.barchart.com/story/news/1073766/authid-reports-financial-and-operating-results-for-the-fourth-quarter-2025', date: '2026-03-31', quote: 'Total net revenue for the twelve months ended December 31, 2025 which reflects estimated concessions totaling $0.9 million, was $2.0 million'}
  - {claim: authID markets deepfake countermeasures, url: 'https://www.nasdaq.com/press-release/authid-publishes-new-whitepaper-next-generation-deepfake-detection-technology-2025-03', date: '2025-03-06', quote: 'authID Publishes New Whitepaper on Next-Generation Deepfake Detection Technology'}
  - {claim: Cyabra 2025 revenue $5.71M, url: 'https://www.macroaxis.com/financial-statements/CYAB', date: '2026-11-01', quote: 'Cyabra Common''s total revenue came in at $5.71 million for the fiscal year ended December 31, 2025'}
  - {claim: Cyabra 2025 net loss $12.82M, url: 'https://www.macroaxis.com/financial-statements/CYAB', date: '2026-11-01', quote: 'Cyabra Common reported a net loss of $12.82 million for fiscal 2025'}
  - {claim: Mitek fiscal 2025 revenue $179.7M, url: 'https://seekingalpha.com/pr/20337551', date: '2025-12-11', quote: 'Total revenue of $179.7 million was a 4% increase year-over-year'}
  - {claim: Mitek fiscal 2025 GAAP net income $8.8M, url: 'https://seekingalpha.com/pr/20337551', date: '2025-12-11', quote: 'GAAP net income of $8.8 million, compared to $3.3 million a year ago.'}
```

### 8. country-gap (total 15)
```yaml
format: country-gap
title: Deepfake attacks grew 2,200% in the Americas, 116% in Asia-Pacific
chapter: Market opportunity
why_it_matters: Deepfake attacks on identity checks are growing fastest in the Americas, the biggest buyer market, which shows demand is accelerating right now. Financial services drew 94% of all deepfakes Entrust detected.
data:
  - {label: Americas, value: 2200, unit: '% growth in deepfake attacks, year over year', date: 2026-09}
  - {label: World, value: 165, unit: '% growth in deepfake attacks, year over year', date: 2026-09}
  - {label: Asia-Pacific, value: 116, unit: '% growth in deepfake attacks, year over year', date: 2026-09}
note: We use Entrust's 2027 Identity Fraud Report, based on identity checks it processed from September 2025 to September 2026 across 195 countries. Entrust reports regions, not single countries.
fresh: {period: year, end: 2026-09}
scores: {surprise: 4, importance: 4, clarity: 4, durability: 3}
sources:
  - {claim: Americas deepfake attacks up 2,200%, url: 'https://www.entrust.com/company/newsroom/2027-identity-fraud-report', date: '2026-11-17', quote: 'Deepfake attacks increased 2,200%'}
  - {claim: Global deepfake attacks up 165%, url: 'https://www.entrust.com/company/newsroom/2027-identity-fraud-report', date: '2026-11-17', quote: 'Deepfake attacks increased 165% year over year'}
  - {claim: Asia-Pacific deepfake activity up 116%, url: 'https://technode.global/?p=997891', date: '2026-11-18', quote: 'Detected deepfake activity in Asia-Pacific increased 116 percent year over year'}
  - {claim: Financial services share 94%, url: 'https://www.entrust.com/company/newsroom/2027-identity-fraud-report', date: '2026-11-17', quote: 'Financial services accounted for 94% of all deepfakes detected globally'}
  - {claim: Data period September 2025 to September 2026, url: 'https://technode.global/?p=997891', date: '2026-11-18', quote: 'the report analyzed data from identity verifications processed between September 2025 and September 2026 across 195 countries.'}
```

### 9. fallen-star (total 14)
```yaml
format: fallen-star
title: Cyabra trades about 98% below its $6.20 peak after listing
chapter: Startup killers
why_it_matters: The only pure listed player near this market lost almost all its value within months of its 2026 debut. Investors punish tiny revenue and cash shortfalls fast.
data:
  - {label: Peak after listing, value: $6.20, unit: share price, date: 2026-03}
  - {label: April 7, value: $1.79, unit: share price, date: 2026-04}
  - {label: May 29, value: $0.63, unit: share price, date: 2026-05}
  - {label: August 17, value: $0.34, unit: share price, date: 2026-08}
  - {label: November 13, value: $0.09, unit: share price, date: 2026-11}
  - {label: Fall from peak, value: 98, unit: '%', date: 2026-11}
note: We use Cyabra share prices from March to November 2026, before its 30-for-1 reverse split of November 23, 2026 (the split does not change the percentage fall). Cyabra is a disinformation and impersonation investigation firm.
fresh: {period: total, end: 2026-11}
scores: {surprise: 3, importance: 3, clarity: 5, durability: 3}
sources:
  - {claim: All-time high $6.20, url: 'https://www.trade-ideas.com/stock-info/CYAB/', date: '2026-11-01', quote: 'The stock is 96.8% away from all-time highs of $6.2000'}
  - {claim: $1.79 on April 7, 2026, url: 'https://stockanalysis.com/stocks/cyab/financials/', date: '2026-04-07', quote: '1.790 +0.110 (6.55%) Apr 7, 2026, 3:22 PM EDT - Market open'}
  - {claim: $0.63 on May 29, 2026, url: 'https://stockanalysis.com/stocks/cyab/revenue/', date: '2026-05-29', quote: '0.6300 -0.0080 (-1.25%) May 29, 2026, 11:18 AM EDT - Market open'}
  - {claim: $0.34 on August 17, 2026, url: 'https://ng.investing.com/equities/cyabra', date: '2026-08-17', quote: 'The Cyabra stock price today is 0.34 USD.'}
  - {claim: $0.09 on November 13, 2026, url: 'https://marketchameleon.com/Overview/CYAB', date: '2026-11-13', quote: 'Cyabra (CYAB) closed at $0.09 on November 13, 2026, down 7.3% from the previous close'}
  - {claim: 30-for-1 reverse split on November 23, 2026, url: 'https://menafn.com/1111985929/Cyabra-Announces-30-To-1-Reverse-Stock-Split', date: '2026-11-18', quote: 'is expected to be implemented at the market open on November 23, 2026.'}
```

### 10. icon-grid (total 14)
```yaml
format: icon-grid
title: 62% of organizations faced a deepfake attack in a single year
chapter: Pain points
why_it_matters: Deepfake attacks are no longer rare events but a routine problem for most large organizations. Gartner found them in both social engineering and automated processes.
data:
  - {label: Organizations hit by a deepfake attack in the past 12 months, value: 62, unit: '% of 302 cybersecurity leaders', date: 2025-09}
note: We use Gartner's survey of 302 cybersecurity leaders in North America, EMEA and Asia-Pacific, run from March to May 2025 and published in September 2025.
fresh: {period: total, end: 2025-09}
scores: {surprise: 2, importance: 4, clarity: 5, durability: 3}
sources:
  - {claim: 62% experienced a deepfake attack, url: 'https://gartner.com/en/newsroom/press-releases/2025-09-22-gartner-survey-reveals-generative-artificial-intelligence-attacks-are-on-the-rise', date: '2025-09-22', quote: 'The survey found that 62% of organizations experienced a deepfake attack involving social engineering or exploiting automated processes'}
  - {claim: Survey of 302 leaders, March to May 2025, url: 'https://gartner.com/en/newsroom/press-releases/2025-09-22-gartner-survey-reveals-generative-artificial-intelligence-attacks-are-on-the-rise', date: '2025-09-22', quote: 'The survey was conducted from March-May 2025 among 302 cybersecurity leaders in North America, EMEA and Asia/Pacific.'}
```

### 11. country-gap (total 13)
```yaml
format: country-gap
title: Deepfake attempts rose 967% in Zambia but 94% in the UK in 2025
chapter: Tech and infra
why_it_matters: Deepfake fraud spreads fastest where digital onboarding grew faster than checking tools. Vendors can find new buyers in Africa and Asia, not only in the US and Europe.
data:
  - {label: Zambia, value: 967, unit: '% growth in deepfake attempts', date: 2025}
  - {label: DR Congo, value: 367, unit: '% growth in deepfake attempts', date: 2025}
  - {label: Singapore, value: 158, unit: '% growth in deepfake cases (more than)', date: 2025}
  - {label: United Kingdom, value: 94, unit: '% growth in deepfake attempts', date: 2025}
note: We use Sumsub's Identity Fraud Report 2025-2026, which compares its 2025 verification data with 2024, as quoted in business and tech press.
fresh: {period: year, end: 2025-12}
scores: {surprise: 3, importance: 3, clarity: 4, durability: 3}
sources:
  - {claim: Zambia +967% and DRC +367%, url: 'https://businessday.ng/technology/article/africa-enters-high-skill-fraud-era-as-deepfakes-surge-967-in-zambia-367-in-drc/', date: '2025-11-26', quote: 'Zambia witnessed an astonishing 967% surge in deepfake attempts, the highest on the continent'}
  - {claim: DRC +367%, url: 'https://businessday.ng/technology/article/africa-enters-high-skill-fraud-era-as-deepfakes-surge-967-in-zambia-367-in-drc/', date: '2025-11-26', quote: 'the Democratic Republic of Congo (DRC) followed closely with 367 percenr'}
  - {claim: Singapore deepfake cases up more than 158%, url: 'https://www.techedt.com/sumsub-reports-sharp-rise-in-synthetic-personal-data-fraud-in-apac', date: '2025-12-12', quote: 'Singapore experienced an overall decline in fraud of 12% but saw deepfake cases increase by more than 158%'}
  - {claim: UK deepfake attempts up 94%, url: 'https://sumsub.com/blog/fraud-trends/', date: '2026-04-15', quote: 'in the United Kingdom, according to the Sumsub Identity Fraud Report 2025, deepfake attempts increased by 94%'}
```
