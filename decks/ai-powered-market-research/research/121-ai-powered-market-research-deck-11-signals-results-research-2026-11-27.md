# AI market research: Signals and Data Points

**Research cutoff:** 2026-11-27  
**Candidates retained:** 16  
**Market opportunity candidates:** 7  
**Formats with passing candidates:** key-trend, icon-grid, kpi-trio

## Scope and method

**Market definition used:** AI market research comprises independent technology vendors whose principal product uses AI to collect, simulate, interpret or analyze evidence about consumers, buyers, audiences and markets so organizations can make research-led product, brand, pricing and strategic decisions.

Included product types: AI-moderated interviews and focus groups; AI-guided surveys and panel studies; statistically calibrated synthetic respondents and behavioral simulations; AI-first coding and synthesis of research data; consumer/category signal intelligence; and AI-assisted concept and creative pretesting when research is the core product.

Excluded: generic LLM/search assistants, broad data infrastructure, agencies without proprietary scalable software, generic transcription without research positioning, marketing content generation/activation, ad buying/optimization, sales lead enrichment and standalone CRM/prospecting.

**Scoring:** surprise, importance, clarity in three seconds, and durability over six months are each scored 1-5. Candidates are ranked by total score, with ties ordered by importance and then surprise. Every candidate below passed its format's keep condition. The list deliberately does not force a candidate for every format.

**Freshness:** GRIT and Displayr survey data are Q1 2026. Company totals are dated to the latest disclosed snapshot. Case-study data are dated to the publication or recorded interview date. Forecasts and company-reported claims are labeled as such.

**Important limitations:**
- GRIT survey percentages are shares of individual research professionals in supplier or buyer-side subgroups, not market revenue shares or audited company adoption rates. Some subgroup bases are small.
- Displayr's AI Readiness Quiz is vendor-run and should be treated as directional, not as a representative probability sample.
- Conveo's 400+ figure is enterprise teams, not a verified count of paying customers. Its interview speed and AI-follow-up metrics are company-reported.
- Listen Labs' revenue and interview metrics were disclosed before its acquisition. Salesforce completed the acquisition on 2026-11-02, so Listen Labs is **NOT A STARTUP** at the research cutoff. It is included as evidence of product traction and strategic consolidation.
- Strella metrics are reported in an investor-authored Bessemer case study. The Duolingo and Aaru time-saving examples are single customer cases, not market-wide averages.
- Aaru's 92.4% benchmark is company-produced and should not be described as general model accuracy. It measures brand-pair ordering against actual card-purchase data.
- No funding rounds or financing-derived valuation ladders are included. The prompt directs funding-round formats to the internal database.

## Ranked candidates

### 1. Listen Labs reached enterprise scale before its Salesforce acquisition

```yaml
format: kpi-trio
title: "Listen Labs grew annualized revenue 15x and interviewed 1M people"
chapter: Market opportunity
why_it_matters: "Listen Labs reported 15x annualized revenue growth and more than 1M interviews within nine months, then became a Salesforce acquisition. Its 50M-person participant network points to enterprise-scale reach, although network size is not completed interview volume."
data:
  - label: "Annualized revenue growth since launch"
    value: 15
    unit: "x"
    date: "2026-01-14"
  - label: "People interviewed"
    value: 1000000
    unit: "people"
    date: "2026-01-14"
  - label: "Global participant network available to Listen Labs agents"
    value: 50000000
    unit: "participants"
    date: "2026-09-29"
note: "We use Listen Labs' January 14, 2026 company announcement for revenue growth and interviews, and Salesforce's September 29, 2026 release for network size. Salesforce completed the acquisition on November 2, 2026, so Listen Labs is NOT A STARTUP at the 2026-11-27 cutoff."
scores: {surprise: 5, importance: 5, clarity: 5, durability: 3, total: 18}
fresh: {period: total, end: "2026-09"}
sources:
  - claim: "15x annualized revenue growth and more than 1M interviews in nine months"
    url: "https://listenlabs.com/blog/announcing-listen-labs-series-b"
    date: "2026-01-14"
    quote: "Since launching nine months ago, Listen has grown its annualized revenue by 15x and interviewed more than one million people."
  - claim: "50M+ participant network and 120 languages"
    url: "https://www.salesforce.com/news/stories/salesforce-signs-definitive-agreement-to-acquire-listen-labs/"
    date: "2026-09-29"
    quote: "Agents can draw from a global network of more than 50 million participants and run interviews around the clock in more than 120 languages."
  - claim: "Salesforce completed the acquisition"
    url: "https://www.salesforce.com/news/stories/salesforce-signs-definitive-agreement-to-acquire-listen-labs/"
    date: "2026-11-02"
    quote: "Salesforce completed its acquisition of Listen Labs on November 2, 2026."
```

### 2. Strella reported first-year ARR and strong early retention

```yaml
format: kpi-trio
title: "Strella reached $1.6M ARR and 150%+ net dollar retention"
chapter: Market opportunity
why_it_matters: "Strella reported $1.6M ARR in its first monetization year and over 150% net dollar retention on its first renewal cohort. Its 8M-person panel gives the product reach beyond a boutique AI interview tool."
data:
  - label: "ARR in first year of monetization"
    value: "$1.6M"
    unit: "USD ARR"
    date: "2026-04-21"
  - label: "Net dollar retention on first renewal cohort"
    value: "150%+"
    unit: "NDR"
    date: "2026-04-21"
  - label: "Global participant panel access"
    value: 8000000
    unit: "participants"
    date: "2026-04-21"
note: "We use Bessemer's April 21, 2026 case study; ARR and NDR are company-reported, and the 8M figure is access to a global panel, not completed interviews. Bessemer is an investor in Strella."
scores: {surprise: 5, importance: 5, clarity: 5, durability: 3, total: 18}
fresh: {period: half, end: "2026-04"}
sources:
  - claim: "$1.6M first-year ARR and 150% NDR on the first renewal cohort"
    url: "https://www.bvp.com/atlas/strella-transforming-qualitative-research-from-a-bottleneck-into-an-ai-superpower"
    date: "2026-04-21"
    quote: "The company reached $1.6M ARR in its first year of monetization and 150% NDR on its first cohort of renewals."
  - claim: "Access to an 8M-person global panel"
    url: "https://www.bvp.com/atlas/strella-transforming-qualitative-research-from-a-bottleneck-into-an-ai-superpower"
    date: "2026-04-21"
    quote: "Strella's platform supports studies across 46+ languages with access to a panel of 8 million global participants."
```

### 3. Synthetic data use nearly doubled across large service-led suppliers

```yaml
format: key-trend
title: "Synthetic data use nearly doubled across large service-led suppliers"
chapter: Market opportunity
why_it_matters: "Synthetic data use nearly doubled in both service-led supplier bands with 101+ FTE. That is evidence of simulation moving into established research operations, not just early-stage experimentation."
data:
  - label: "500+ FTE service-led suppliers, 2025 wave"
    value: 26
    unit: "% reporting current use"
    date: "2025 wave"
  - label: "500+ FTE service-led suppliers, 2026 wave"
    value: 44
    unit: "% reporting current use"
    date: "2026 wave"
  - label: "101-500 FTE service-led suppliers, 2025 wave"
    value: 16
    unit: "% reporting current use"
    date: "2025 wave"
  - label: "101-500 FTE service-led suppliers, 2026 wave"
    value: 34
    unit: "% reporting current use"
    date: "2026 wave"
note: "We use the 2026 GRIT executive table for service-led suppliers with 101-500 and 500+ FTE; these are respondent shares reporting current use, not revenue shares. The 2026 survey was fielded January 11 to March 9, 2026."
scores: {surprise: 4, importance: 5, clarity: 5, durability: 4, total: 18}
fresh: {period: quarter, end: "2026-03"}
sources:
  - claim: "Synthetic data adoption rose sharply in the largest service-led supplier segment"
    url: "https://hs-6530786.f.hubspotemail.net/hubfs/6530786/2026%20GRIT%20Insights%20Practice%20Report/2026%20GRIT%20Insights%20Practice%20Report%20-%20Unabridged.pdf"
    date: "2026-06"
    quote: "Since last year, synthetic data adoption among the largest service-led suppliers nearly doubled."
```

### 4. Only 8% say AI has completely transformed their research workflow

```yaml
format: icon-grid
title: "Only 8% of researchers say AI has completely transformed their workflow"
chapter: Market challenges
why_it_matters: "AI use is widespread among surveyed researchers, but only 8% say it has completely transformed how they work. The gap shows how far tool adoption remains from full workflow redesign."
data:
  - label: "Researchers saying AI has completely transformed how they work"
    value: 8
    unit: "% of respondents"
    date: "2026-03"
note: "We use Displayr's March 2026 AI market research survey of 203 researchers; this is self-reported workflow transformation, not a measure of AI tool adoption or productivity. The sample is vendor-run and directional."
scores: {surprise: 5, importance: 4, clarity: 5, durability: 4, total: 18}
fresh: {period: quarter, end: "2026-03"}
sources:
  - claim: "Only a small share say AI has fully transformed their work"
    url: "https://www.displayr.com/ai-market-research-adoption-is-near-universal-trust-is-not/"
    date: "2026-03"
    quote: "Only 8% say AI has completely transformed how they work."
```

### 5. Aaru matched real purchase-panel brand ordering in 92.4% of pairs

```yaml
format: icon-grid
title: "Aaru matched real purchase-panel brand ordering in 92.4% of 340 pairs"
chapter: Tech and infra
why_it_matters: "Aaru's synthetic population model reproduced actual card-panel brand ordering in 92.4% of 340 pairs. This is a concrete validation signal, but the benchmark is company-run and has not been independently replicated."
data:
  - label: "Brand-pair ordering agreement with actual card-purchase panel across 340 pairs"
    value: 92.4
    unit: "%"
    date: "2026-09-24"
note: "We use Aaru's September 24, 2026 benchmark across 340 brand pairs and 100 brand-period observations; the model's three-run average is compared with actual card-purchase ordering."
scores: {surprise: 5, importance: 4, clarity: 5, durability: 3, total: 17}
fresh: {period: total, end: "2026-09"}
sources:
  - claim: "Aaru's synthetic model matched real purchase-panel ordering across 340 brand pairs"
    url: "https://aaru.com/publications/population-simulation-at-the-replication-floor-research"
    date: "2026-09-24"
    quote: "Aaru gets the order correct in 92.4% of 340 brand pairs."
```

### 6. Aaru cut one CPG product innovation cycle from nine months to eight weeks

```yaml
format: key-trend
title: "Aaru cut a CPG product cycle from 9 months to 8 weeks"
chapter: Value creation
why_it_matters: "Aaru says one CPG client cut its product innovation cycle from nine months to eight weeks using behavioral simulations. The client is unnamed, so treat this as a single case study rather than a market-wide benchmark."
data:
  - label: "Traditional product innovation cycle for the client"
    value: 9
    unit: "months"
    date: "Client baseline"
  - label: "Aaru-assisted product innovation cycle"
    value: 8
    unit: "weeks"
    date: "2026-07"
note: "We use Aaru co-founder Youssef's July 22, 2026 Goldman Sachs interview, published November 5; the client is unnamed and the time reduction is company-reported."
scores: {surprise: 5, importance: 4, clarity: 5, durability: 3, total: 17}
fresh: {period: total, end: "2026-07"}
sources:
  - claim: "A CPG client's traditional product innovation cycle was nine months"
    url: "https://www.goldmansachs.com/insights/videos/ai-is-about-to-transform-market-research-heres-how"
    date: "2026-11-05"
    quote: "Their product innovation cycle traditionally was nine months long."
  - claim: "Aaru reduced the cycle to eight weeks"
    url: "https://www.goldmansachs.com/insights/videos/ai-is-about-to-transform-market-research-heres-how"
    date: "2026-11-05"
    quote: "We managed to squeeze it down into eight weeks."
```

### 7. Duolingo's Strella project fell from over six weeks to two days

```yaml
format: key-trend
title: "Duolingo's Strella project fell from over 6 weeks to 2 days"
chapter: Value creation
why_it_matters: "Duolingo completed a video concept-testing project in two days instead of more than six weeks using Strella. The case shows AI interviews can change project cadence, not just reduce moderator time."
data:
  - label: "Video concept-testing project before Strella"
    value: "6+"
    unit: "weeks"
    date: "Pre-Strella baseline"
  - label: "Video concept-testing project using Strella"
    value: 2
    unit: "days"
    date: "2026-04"
note: "We use Bessemer's April 21, 2026 case study; it is a single Duolingo project and the source is an investor case study, not a controlled time-motion study."
scores: {surprise: 5, importance: 4, clarity: 5, durability: 3, total: 17}
fresh: {period: total, end: "2026-04"}
sources:
  - claim: "Duolingo's latest video concept-testing project took two days rather than over six weeks"
    url: "https://www.bvp.com/atlas/strella-transforming-qualitative-research-from-a-bottleneck-into-an-ai-superpower"
    date: "2026-04-21"
    quote: "Their last project with us took two days to complete (versus over six weeks before Strella)."
```

### 8. Two-thirds of researchers still double-check every AI output

```yaml
format: icon-grid
title: "67% of researchers double-check every AI output"
chapter: Market challenges
why_it_matters: "Two-thirds of surveyed researchers routinely double-check every AI output. This shows verification remains a real workflow cost as AI tools move from experimentation into research production."
data:
  - label: "Respondents who double-check every AI output as a matter of routine"
    value: 67
    unit: "% of respondents to this question"
    date: "2026-03"
note: "We use Displayr's March 2026 AI market research survey; 203 researchers answered the overall survey and 135 answered this item. The sample is vendor-run and should be treated as directional."
scores: {surprise: 4, importance: 4, clarity: 5, durability: 4, total: 17}
fresh: {period: quarter, end: "2026-03"}
sources:
  - claim: "Most researchers routinely verify AI output"
    url: "https://www.displayr.com/ai-market-research-adoption-is-near-universal-trust-is-not/"
    date: "2026-03"
    quote: "67% double-check every AI output as a matter of routine."
```

### 9. AI-moderated qualitative use rose from 25% to 45% in one year

```yaml
format: key-trend
title: "AI-moderated qualitative use rose from 25% to 45% in one year"
chapter: Market opportunity
why_it_matters: "AI-moderated qualitative use rose 1.8x among mid-sized service-led suppliers in one year. The result suggests AI interviewing is moving into established supplier workflows, though the segment sample is modest."
data:
  - label: "Service-led suppliers with 21-100 FTE, 2025 wave"
    value: 25
    unit: "% reporting use of AI-/chatbot-moderated qual"
    date: "2025 wave"
  - label: "Service-led suppliers with 21-100 FTE, 2026 wave"
    value: 45
    unit: "% reporting use of AI-/chatbot-moderated qual"
    date: "2026 wave"
note: "We use GRIT's 2025 and 2026 waves for service-led suppliers with 21-100 FTE; the 2026 category clarifies the earlier automated-interviewing item, so read the 25% to 45% comparison as directional."
scores: {surprise: 4, importance: 4, clarity: 5, durability: 3, total: 16}
fresh: {period: quarter, end: "2026-03"}
sources:
  - claim: "AI-/chatbot-moderated qualitative use rose to 45% among mid-sized service-led suppliers"
    url: "https://hs-6530786.f.hubspotemail.net/hubfs/6530786/2026%20GRIT%20Insights%20Practice%20Report/2026%20GRIT%20Insights%20Practice%20Report%20-%20Unabridged.pdf"
    date: "2026-06"
    quote: "AI-/chatbot-moderated qual jumped +20% to 45%."
```

### 10. Conveo's team grew from about 20 to 90 people in 2026

```yaml
format: key-trend
title: "Conveo's team grew from about 20 to 90 people in 2026"
chapter: Market opportunity
why_it_matters: "Conveo's team expanded from roughly 20 to 90 people in 2026, a 4.5x increase. That hiring pace signals capacity-building around enterprise research demand, although headcount is not revenue or customer growth."
data:
  - label: "Conveo team at the start of 2026, approximate"
    value: 20
    unit: "people"
    date: "2026-01"
  - label: "Conveo team size in current Y Combinator profile"
    value: 90
    unit: "people"
    date: "2026-11"
note: "We compare Conveo's stated team size at the start of 2026 with the current Y Combinator profile's team-size field, checked November 27; the starting figure is approximate and the current field is not audited."
scores: {surprise: 4, importance: 4, clarity: 5, durability: 3, total: 16}
fresh: {period: total, end: "2026-11"}
sources:
  - claim: "Conveo began 2026 with approximately 20 people"
    url: "https://www.ycombinator.com/companies/conveo"
    date: "2026-11-27"
    quote: "We entered 2026 as a team of ~20."
  - claim: "Current listed team size is 90"
    url: "https://www.ycombinator.com/companies/conveo"
    date: "2026-11-27"
    quote: "Team Size: 90."
```

### 11. Conveo reports 400+ enterprise teams and AI-driven follow-ups

```yaml
format: kpi-trio
title: "Conveo reports 400+ enterprise teams and 70%+ AI-driven follow-ups"
chapter: Market opportunity
why_it_matters: "Conveo reports 400+ enterprise teams and says AI-driven follow-ups generate over 70% of surfaced insights. Its 100-interview, three-day fielding claim points to a scalable research workflow, not just automated transcription."
data:
  - label: "Enterprise teams globally"
    value: "400+"
    unit: "teams"
    date: "2026-11-27"
  - label: "Insights surfaced from AI-driven follow-up questions"
    value: "70%+"
    unit: "share of surfaced insights"
    date: "2026-11-27"
  - label: "Reported interview fielding speed"
    value: 100
    unit: "interviews in 3 days"
    date: "2026-11-27"
note: "We use Conveo's current Y Combinator profile and official media kit, checked November 27, 2026; the 400+ figure refers to enterprise teams, not a verified count of paying customers, and the other metrics are company-reported."
scores: {surprise: 4, importance: 4, clarity: 5, durability: 3, total: 16}
fresh: {period: total, end: "2026-11"}
sources:
  - claim: "Conveo reports a footprint of 400+ enterprise teams"
    url: "https://www.ycombinator.com/companies/conveo"
    date: "2026-11-27"
    quote: "400+ enterprise teams globally."
  - claim: "AI-driven follow-up questions account for over 70% of surfaced insights"
    url: "https://www.ycombinator.com/companies/conveo"
    date: "2026-11-27"
    quote: "Over 70% of the insights we surface come from AI-driven follow-up questions."
  - claim: "Conveo says it can field 100 interviews in three days"
    url: "https://conveo.ai/mediakit"
    date: "2026-11-27"
    quote: "Fielding speed: 100 interviews in 3 days."
```

### 12. 66% expect agents to mediate research purchases

```yaml
format: icon-grid
title: "66% of brand-side analytics leaders expect agents to mediate research purchases"
chapter: Growth drivers
why_it_matters: "Two-thirds of analytics-oriented brand-side professionals expect automated or agentic systems to mediate most research purchases within a few years. This is a demand signal, not current procurement behavior."
data:
  - label: "Analytics-oriented brand-side professionals expecting agents to mediate most research purchases"
    value: 66
    unit: "%"
    date: "2026-03"
note: "We use Greenbook's October 1, 2026 analysis of the 2026 GRIT survey; the 66% is a future expectation, not evidence that agents already control procurement."
scores: {surprise: 4, importance: 4, clarity: 5, durability: 3, total: 16}
fresh: {period: quarter, end: "2026-03"}
sources:
  - claim: "Two-thirds of analytics-oriented brand-side professionals expect agentic systems to mediate research purchases"
    url: "https://www.greenbook.org/insights/market-research-trends/agentic-ai-is-coming-to-market-research-but-are-insights-teams-ready"
    date: "2026-10-01"
    quote: "66% of analytics-oriented insights professionals on the brand-side completely or mostly agree."
```

### 13. Text-based qualitative research use fell from 46% to 30%

```yaml
format: key-trend
title: "Text-based qualitative research use fell from 46% to 30%"
chapter: Market challenges
why_it_matters: "Use of text- or SMS-based qualitative research fell by 16 percentage points among mid-sized service-led suppliers. GRIT suggests AI-moderated formats may be displacing it, but the survey does not establish causation."
data:
  - label: "Service-led suppliers with 21-100 FTE, 2025 wave"
    value: 46
    unit: "% reporting use of text-based online qual"
    date: "2025 wave"
  - label: "Service-led suppliers with 21-100 FTE, 2026 wave"
    value: 30
    unit: "% reporting use of online text- or SMS-based qual"
    date: "2026 wave"
note: "We use GRIT's 2025 and 2026 supplier-method waves for service-led suppliers with 21-100 FTE; the text/SMS label was refined between waves, so the comparison is directional rather than a perfect wording match. These are respondent shares, not market revenue."
scores: {surprise: 4, importance: 3, clarity: 5, durability: 3, total: 15}
fresh: {period: quarter, end: "2026-03"}
sources:
  - claim: "Text-based asynchronous qualitative research may be losing ground to AI-moderated formats"
    url: "https://hs-6530786.f.hubspotemail.net/hubfs/6530786/2026%20GRIT%20Insights%20Practice%20Report/2026%20GRIT%20Insights%20Practice%20Report%20-%20Unabridged.pdf"
    date: "2026-06"
    quote: "Text-based asynchronous qual may be getting displaced by AI-moderated formats that accomplish similar goals with more analytical capability attached."
```

### 14. Field services became a less significant revenue source for large suppliers

```yaml
format: key-trend
title: "Fewer large suppliers call field services a significant revenue source"
chapter: Market challenges
why_it_matters: "The share of large service-led suppliers calling field services a significant revenue source fell from 30% to 16%. This signals pressure on traditional delivery models, but does not prove AI caused the decline."
data:
  - label: "Service-led suppliers with 500+ FTE, 2025 wave"
    value: 30
    unit: "% saying field services are a significant revenue source"
    date: "2025 wave"
  - label: "Service-led suppliers with 500+ FTE, 2026 wave"
    value: 16
    unit: "% saying field services are a significant revenue source"
    date: "2026 wave"
note: "We use GRIT's 2025 and 2026 waves for service-led suppliers with 500+ FTE; this is the share of respondents who call field services a significant revenue source, not field services' share of actual company revenue."
scores: {surprise: 4, importance: 3, clarity: 5, durability: 3, total: 15}
fresh: {period: quarter, end: "2026-03"}
sources:
  - claim: "The share of large service-led suppliers calling field services a significant revenue source nearly halved"
    url: "https://hs-6530786.f.hubspotemail.net/hubfs/6530786/2026%20GRIT%20Insights%20Practice%20Report/2026%20GRIT%20Insights%20Practice%20Report%20-%20Unabridged.pdf"
    date: "2026-06"
    quote: "The percentage claiming field services as a significant source of revenue nearly halved."
```

### 15. 62% of brand-side analytics AI-moderation users use it regularly

```yaml
format: icon-grid
title: "62% of brand-side analytics AI-moderation users use it regularly"
chapter: Market opportunity
why_it_matters: "Regular use is a stronger signal than trial: 62% of brand-side analytics professionals already using AI-moderated qualitative research use it regularly. This points to repeat workflow adoption, not just experimentation."
data:
  - label: "Current AI-/chatbot-moderated qualitative users who use it regularly"
    value: 62
    unit: "% of current users in brand-side analytics"
    date: "2026-03"
note: "We use GRIT's 2026 brand-side analytics data; the denominator is only professionals who already use AI-/chatbot-moderated qual, not all brand-side analytics professionals."
scores: {surprise: 3, importance: 4, clarity: 5, durability: 3, total: 15}
fresh: {period: quarter, end: "2026-03"}
sources:
  - claim: "Most brand-side analytics professionals already using AI-moderated qual use it regularly"
    url: "https://hs-6530786.f.hubspotemail.net/hubfs/6530786/2026%20GRIT%20Insights%20Practice%20Report/2026%20GRIT%20Insights%20Practice%20Report%20-%20Unabridged.pdf"
    date: "2026-06"
    quote: "Most brand-side analytics professionals who use AI-/chatbot-moderated qual use it regularly (62%)."
```

### 16. 61% of the largest service-led suppliers use AI-moderated qualitative research

```yaml
format: icon-grid
title: "61% of the largest service-led suppliers use AI-moderated qual"
chapter: Growth drivers
why_it_matters: "More than half of the largest service-led suppliers report using AI-moderated qualitative research. This shows the method has reached established providers, though the 500+ FTE subgroup is small."
data:
  - label: "Service-led suppliers with 500+ FTE reporting use of AI-/chatbot-moderated qual"
    value: 61
    unit: "%"
    date: "2026-03"
note: "We use GRIT's 2026 wave for suppliers with 500+ FTE; the report says this rose 14 percentage points from 47% in 2025, and the subgroup base is small (roughly n=30-45)."
scores: {surprise: 3, importance: 3, clarity: 5, durability: 3, total: 14}
fresh: {period: quarter, end: "2026-03"}
sources:
  - claim: "AI-moderated qualitative use among the largest service-led suppliers"
    url: "https://hs-6530786.f.hubspotemail.net/hubfs/6530786/2026%20GRIT%20Insights%20Practice%20Report/2026%20GRIT%20Insights%20Practice%20Report%20-%20Unabridged.pdf"
    date: "2026-06"
    quote: "AI-/chatbot-moderated qual jumped +14% to 61%."
```

## Format screening: all formats tested

| Format | Result | Reason |
|---|---|---|
| key-trend | PASS: 7 candidates | Comparable before/after measures with at least a 1.5x change or a clear break. |
| rules-wave | NO | No same-source annual series of laws, bills, approvals or suits specific to AI market research. |
| funnel | NO | Available adoption tiers are mutually exclusive survey categories, not a nested sequence of counts. The 95% use, 11% embedded and 8% transformed figures are separate questions, so a funnel would imply unsupported conversion. |
| country-gap | NO | No fresh, same-year, same-measure country series with a 2x contrast. |
| waiting-line | NO | No credible paired waitlist/backlog and served-capacity figures for an in-scope vendor. |
| incident-count | NO | No official yearly incident or loss series that measures research-specific AI failures independently of market activity. |
| announced-vs-built | NO | No comparable count of announced AI research products versus products actually launched or delivered. |
| idle-capacity | NO | No source reports built research capacity and actual utilization for the same vendors. |
| promise-tracker | NO | No three dated slips for the same company milestone. |
| lobbying-spend | NO | No meaningful category-company LD-2 series with a recent jump or striking amount. |
| cost-threshold | NO | Public per-interview and per-study prices exclude different items (recruitment, incentives, platform fees and moderation), so there is no comparable 4-10 point price series against one reference. |
| penetration-curve | NO | Available surveys do not provide a consistent adoption series by years since launch; the GRIT waves are not a launch-cohort penetration curve. |
| adoption-race | NO | No comparable, dated time-to-milestone data for two or more vendors using the same milestone. |
| earnings-mentions | NO | No accessible FactSet or equivalent quarterly earnings-call series for the defined market. |
| real-world-vs-funding | NOT RESEARCHED | Funding data are handled by the internal database per instruction; no matching public real-world price/use series was identified. |
| incumbent-crash | NO | No listed pure-play incumbent showed a verified 50%+ fall since a defined market event. |
| fallen-star | NO | The category is mostly private; no relevant listed pure-play company was verified at 80%+ below its split-adjusted peak. |
| challenger | NO | No reliable current valuation/revenue series shows a private AI research challenger rapidly closing the gap with a listed giant. |
| dominance | NO | No single-source market-share series demonstrates a rising or crushing share for one vendor. |
| contract-share | NO | No comparable public-contract award dataset separates AI research newcomers from incumbents. |
| multiple-gap | NO | Comparable market value/sales data are unavailable; private valuations would rely on financing-round data, which were not researched. |
| profit-gap | NO | Private AI research vendors do not publish comparable operating-profit filings. |
| revenue-per-head | NO | No comparable current revenue and headcount data for both AI-native vendors and legacy research players. |
| dollar-split | NO | No published customer price breakdown allocates each dollar across software, recruitment, incentives and services. |
| single-customer | NO | No public filing discloses a qualifying AI research vendor's largest-customer revenue share over time. |
| forecast-gap | NO | Fewer than five credible publishers use the same definition and target year; broad AI market research forecasts are not comparable. |
| kpi-trio | PASS: 3 candidates | Listen Labs, Strella and Conveo have three current, sourced scale/growth metrics each. |
| deal-timeline | NO | Only one clearly in-scope acquisition was found in the current 12-month window: Salesforce/Listen Labs. The AI Palette, Gastrograph AI and Black Swan Data deals cluster in 2025 and are too old to support a fresh 2026 deal wave. |
| value-ladder | NOT RESEARCHED | Four to six comparable current valuations could not be built without using financing-round data, which were not researched. |
| icon-grid | PASS: 6 candidates | Six simple, well-sourced rates are easy to picture and materially informative. |
| funding-event | NOT RESEARCHED | Funding-round charts are computed from the internal database per instruction. |

## Company and boundary notes

- **Listen Labs:** AI-first customer research and human simulation. Salesforce completed its acquisition on 2026-11-02. Its pre-acquisition traction is useful, but it is classified as **NOT A STARTUP** at the cutoff.
- **Strella:** AI-moderated qualitative research. The Bessemer case study reports first-year ARR, first-cohort retention and a Duolingo concept-testing use case. Bessemer is an investor, so the company metrics are not independent audited figures.
- **Conveo:** AI-moderated interviews with AI-driven follow-up questions. The current 400+ enterprise-team figure is a company/profile claim and should not be presented as 400+ paying customers.
- **Aaru:** Synthetic populations and behavioral simulation for consumer research. Its 92.4% result is specifically brand-pair ordering against actual card-purchase data, not a universal accuracy score.
- **Outset:** In-scope AI-moderated research. Its current website reports 500K+ interview hours and 10K+ studies, but these are undated cumulative totals with no comparable prior point. They do not pass the KPI-trio strong-growth condition or a key-trend time-series condition.
- **M&A scan:** The 2025 acquisition cluster included AI Palette (GlobalData), Gastrograph AI (NIQ) and Black Swan Data (Mintel). Those deals are outside the current 12-month freshness window. Salesforce/Listen Labs is the clearly in-scope 2026 acquisition, but one current deal does not make a 4-6 event deal wave.
- **Incumbents:** Qualtrics, Ipsos, Kantar, NielsenIQ, Dynata, Toluna and YouGov were treated as incumbent research/insight platforms, not as AI-native startups merely because they offer AI features. Acquired assets were assessed on the acquired product's core purpose, not the acquirer's general AI roadmap.

## Non-candidate evidence checked

- Outset's current homepage reports "500K+ Hours of interviews conducted" and "10K+ Studies run". This is useful scale context, but without dated comparison points it is not a growth candidate. Source: [Outset](https://www.outset.ai/), checked 2026-11-27.
- The 2025 M&A cluster was checked as context, not promoted to a hot-now slide: [GlobalData and AI Palette](https://www.globaldata.com/media/press-release/globaldata-acquires-ai-palette-to-strengthen-its-innovation-solution-with-ai-powered-consumer-insights/), [NIQ and Gastrograph AI](https://nielseniq.com/global/en/news-center/2025/niq-to-acquire-gastrograph-ai/), and [Mintel and Black Swan Data](https://www.mintel.com/press-centre/mintel-acquires-black-swan-data-revolutionizing-predictive-intelligence-and-reshaping-the-future-of-insight/).
- The 2026 GRIT report's fieldwork ran from January 11 to March 9, 2026, with 735 completed surveys overall. Supplier and buyer-side subgroup bases vary, so subgroup percentages should be labeled with their segment and not generalized to the entire market.

## Recommendation for slide selection

The strongest market-opportunity story is the combination of: (1) AI-moderated qualitative use rising from 25% to 45% among mid-sized service-led suppliers; (2) synthetic data use nearly doubling across two large supplier bands; (3) the scale and monetization metrics from Listen Labs, Strella and Conveo; and (4) 62% regular use among brand-side analytics professionals already using AI moderation. For market challenges, use the 8% workflow-transformation rate, 67% routine double-check rate, and the decline in traditional text-based qual and field-services significance. For proof of value and technical credibility, use the Aaru and Strella customer cases and Aaru's 92.4% brand-pair benchmark.
