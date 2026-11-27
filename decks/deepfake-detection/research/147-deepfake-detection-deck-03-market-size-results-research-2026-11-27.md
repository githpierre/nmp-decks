# Deepfake detection: Market size (deck 03)

### ed041
```yaml
status: ok
section: Market size
title: What counts as deepfake detection, and what doesn’t?
note: We count paid tools that tell whether audio, images, video or live calls are fake or altered, and exclude AI generators and generic fraud tools.
t:
  7: "We define deepfake detection as paid technology that tells whether audio, images, video or live calls were faked or altered by AI to deceive"
  8: "We include voice and video detectors, live call screening, deepfake checks in ID onboarding, screening APIs and provenance checks"
  9: "We exclude AI generators, generic fraud or spam filters, pure watermark projects, photo editing and consulting firms with no product"
sources:
  - claim: Gartner defines deepfake detection as a cybersecurity discipline that identifies, analyzes and performs forensics on AI-generated or manipulated media
    url: https://www.gartner.com/en/articles/deepfake-detection-emerging-market
    date: '2026-07'
    quote: "Gartner defines deepfake detection as a cybersecurity discipline that identifies, analyzes and performs forensics on AI-generated or manipulated"
  - claim: Market reports cover detection software, APIs and services
    url: https://www.astuteanalytica.com/industry-report/deepfake-detection-market
    date: '2026-07-15'
    quote: "The market covers detection software, APIs and services."
```

### ed042
```yaml
status: ok
section: Market size
title: What are the market size estimates from different sources online?
rows:
- firm: "SNS\n\nInsider"
  value: $ 1.2 B
  comment: Their 2025 base of $918.6M grows 29.5% a year, which gives about $1.2B in 2026. We treat it as the high end of our range.
- firm: "Astute\n\nAnalytica"
  value: $ 904 M
  comment: Their 2025 figure of $700.5M with 29.1% yearly growth gives about $904M in 2026. We use it as the low case.
- firm: "Meticulous\n\nResearch"
  value: $ 990 M
  comment: Their October 2026 report puts 2026 at $990M for detection platforms, APIs and services. We use it as our anchor.
- firm: "Next Move\n\nStrategy"
  value: $ 1.7 B
  comment: Their detector-tool market reaches $1.7B in 2026 under a wider scope. We use it only as an upper bound.
note:
- We take each estimate from the firm's website and adjust it when its definition is broader or narrower than ours
- When a firm gives only 2025, we grow it by that firm's own growth rate to get a comparable 2026 figure
sources:
  - claim: SNS Insider values the market at $918.6M in 2025, growing 29.5% a year to 2035
    url: https://www.snsinsider.com/reports/deepfake-detection-market-11090
    date: '2026'
    quote: "The Deepfake Detection Market was valued at USD 918.6 Million in 2025"
  - claim: SNS Insider growth rate of 29.5% from 2026 to 2035
    url: https://www.snsinsider.com/reports/deepfake-detection-market-11090
    date: '2026'
    quote: "growing at a CAGR of 29.5% from 2026 to 2035"
  - claim: Astute Analytica estimates $700.5M in 2025 with 29.1% yearly growth
    url: https://www.astuteanalytica.com/industry-report/deepfake-detection-market
    date: '2026-07-15'
    quote: "The deepfake detection market is estimated at USD 700.5 million in 2025"
  - claim: Meticulous Research estimates about $990M for 2026
    url: https://www.meticulousresearch.com/product/deepfake-detection-market-6944
    date: '2026-10'
    quote: "This market is expected to reach USD 9.44 billion by 2036 from an estimated USD 0.99 billion in 2026"
  - claim: Next Move Strategy Consulting puts the AI deepfake detector tool market at $1.7B in 2026
    url: https://www.nextmsc.com/report/ai-deepfake-detector-tool-market-ic5131
    date: '2026'
    quote: "valued at USD 1.24 Billion in 2025 and is estimated at USD 1.72 Billion in 2026"
comment: The SNS Insider and Astute Analytica 2026 values are our own calculation (2025 value x 1.295 and x 1.291). Next Move Strategy Consulting is written on two lines to fit the label.
```

### ed043
```yaml
status: ok
section: Market size
title: Our own first-principles, bottom-up calculation of the market size
page: 1/2
note: We triangulate current market reports, grow 2025 figures by each firm's own growth rate, and use wider tool markets only as a cross-check.
t:
  21: We build our estimate only from market data we can reconcile
  16: We begin from analyst revenue estimates because vendors rarely publish sales
  15: We count detection software, APIs and related services sold to buyers
  14: We exclude AI generators, generic fraud tools and pure watermarking
  9: We exclude acquisitions and funding rounds because those are financing, not sales
  8: We keep 2026, the current year with fresh estimates from each source
  7: We start with Meticulous at $990 million in 2026, the newest report
  6: We compare SNS Insider, which implies $1.2 billion
  3: We treat Next Move's $1.7 billion tool market as a broad upper bound
  2: We check Astute Analytica, whose 2025 base implies $904 million
  0: We check that software and APIs lead spending in every direct report
sources:
  - claim: Meticulous Research estimates about $990M for 2026, report published October 2026
    url: https://www.meticulousresearch.com/product/deepfake-detection-market-6944
    date: '2026-10'
    quote: "from an estimated USD 0.99 billion in 2026, registering a CAGR of 25.3% during the forecast period (2026-2036)"
  - claim: SNS Insider 2025 base of $918.6M
    url: https://www.snsinsider.com/reports/deepfake-detection-market-11090
    date: '2026'
    quote: "The Deepfake Detection Market was valued at USD 918.6 Million in 2025"
  - claim: Next Move Strategy Consulting detector-tool market of $1.7B in 2026
    url: https://www.nextmsc.com/report/ai-deepfake-detector-tool-market-ic5131
    date: '2026'
    quote: "estimated at USD 1.72 Billion in 2026"
  - claim: Astute Analytica 2025 base of $700.5M growing 29.1% a year
    url: https://www.astuteanalytica.com/speak-analyst/deepfake-detection-market
    date: '2026-07-15'
    quote: "projected to reach USD 9,008.9 million by 2035, growing at a CAGR of 29.1%"
  - claim: Software and APIs hold the largest share (Astute Analytica), and solutions lead (Meticulous Research)
    url: https://www.astuteanalytica.com/industry-report/deepfake-detection-market
    date: '2026-07-15'
    quote: "software/APIs segment accounted for the largest share of the market."
comment: Key 16 is a method choice. The leading specialists (Reality Defender, GetReal Security, Pindrop, Resemble AI) are private and do not publish detection revenue, so analyst estimates are the only comparable starting point.
```

### ed044
```yaml
status: ok
section: Market size
title: Our own first-principles, bottom-up calculation of the market size
page: 2/2
note: We land near Meticulous Research's direct figure, while keeping Astute Analytica as the narrow case and Next Move as the high case.
t:
  21: We average the three direct estimates of $904M, $990M and $1.2B
  16: We cross-check with Market Intelo at $1.3 billion for 2025 under a wider scope
  15: We see the three direct estimates sit within $290 million of each other
  14: We note that identity checks and KYC are the top use in every report
  9: We note public estimates diverge because the market's borders are still unsettled
  8: We keep Astute Analytica's implied $904 million as the narrow case
  7: We keep Next Move's $1.7 billion as the high case, under a wider scope
  6: We note most vendors are private and share no sales
  3: We take the scope-adjusted midpoint, about $1 billion for 2026
  2: We round to one simple number that stays easy to check and defend
  0: We conclude that deepfake detection is worth about $1 billion today
sources:
  - claim: Market Intelo values deepfake detection and synthetic media authentication at $1.3B in 2025
    url: https://marketintelo.com/report/deepfake-detection-and-synthetic-media-authentication-market
    date: '2026'
    quote: "was valued at $1.3 billion in 2025"
  - claim: Identity verification and KYC is the leading application (Astute Analytica)
    url: https://www.astuteanalytica.com/industry-report/deepfake-detection-market
    date: '2026-07-15'
    quote: "identity verification & KYC emerged as the leading segment."
  - claim: Identity verification and KYC was the leading application in 2025 (SNS Insider)
    url: https://www.snsinsider.com/reports/deepfake-detection-market-11090
    date: '2026'
    quote: "Identity Verification & KYC dominated the Deepfake Detection Market"
  - claim: Next Move Strategy Consulting detector-tool market of $1.7B in 2026
    url: https://www.nextmsc.com/report/ai-deepfake-detector-tool-market-ic5131
    date: '2026'
    quote: "estimated at USD 1.72 Billion in 2026"
comment: Average of $904M, $990M and $1,190M is $1,028M, rounded to $1B. The spread between $904M and $1,190M is $286M.
```

### ed045
```yaml
status: ok
section: Market size
title: How much is deepfake detection worth today?
t:
  6: $1B
  8: "We estimate $1B in 2026. Astute Analytica implies $904M, Meticulous Research $990M and SNS Insider $1.2B, while Next Move sees $1.7B for a wider tool market. Meticulous is closest to ours."
  4: '2026'
sources:
  - claim: Meticulous Research estimates about $990M for 2026
    url: https://www.meticulousresearch.com/product/deepfake-detection-market-6944
    date: '2026-10'
    quote: "from an estimated USD 0.99 billion in 2026"
  - claim: Next Move Strategy Consulting detector-tool market of $1.7B in 2026
    url: https://www.nextmsc.com/report/ai-deepfake-detector-tool-market-ic5131
    date: '2026'
    quote: "estimated at USD 1.72 Billion in 2026"
  - claim: SNS Insider 2025 base of $918.6M growing 29.5% a year
    url: https://www.snsinsider.com/reports/deepfake-detection-market-11090
    date: '2026'
    quote: "growing at a CAGR of 29.5% from 2026 to 2035"
  - claim: Astute Analytica 2025 base of $700.5M growing 29.1% a year
    url: https://www.astuteanalytica.com/speak-analyst/deepfake-detection-market
    date: '2026-07-15'
    quote: "The deepfake detection market is estimated at USD 700.5 million in 2025"
```

### ed048
```yaml
status: ok
section: Market size
title: What is behind these categories?
t:
  5: VIDEO DEEPFAKE CHECKS
  8: VOICE DEEPFAKE CHECKS
  10: IMAGE AND MULTIMODAL
  11: 🎥
  4: Tools that spot face swaps and fake video in files and live calls. Video is the largest type in every direct report
  12: 🎙️
  7: Tools that tell a cloned voice from a real caller in call centers and meetings. Voice is the fastest-growing type
  9: Checks on photos and ID images, plus platforms that score voice, face and video together in one verdict
  15: ''
  17: ''
  18: ''
  19: ''
  14: ''
  16: ''
holes_ok: true
sources:
  - claim: Video is the largest media type
    url: https://www.meticulousresearch.com/product/deepfake-detection-market-6944
    date: '2026-10'
    quote: "By media type, Video is expected to account for the largest market share."
  - claim: Audio and voice is the fastest-growing modality
    url: https://www.snsinsider.com/reports/deepfake-detection-market-11090
    date: '2026'
    quote: "while Audio/Voice is the fastest-growing modality segment"
  - claim: Market reports split modality into video, audio or voice, image, and text or multimodal
    url: https://www.astuteanalytica.com/request-toc/deepfake-detection-market
    date: '2026-07-15'
    quote: "Modality (Video, Audio/Voice, Image, Text/ Multimodal)"
comment: We read the categories as the modality split used by the market reports (video, voice, image and multimodal), since the category slide itself is not in this chapter.
```

### ed049
```yaml
status: ok
section: Market size
title: Where in the world is deepfake detection money spent?
regions:
  na:
    pct: 39
    text: "North America leads: 23 of the 59 known detection vendors are based in the US. Market Intelo puts the region at 39.2% of 2025."
  eu:
    pct: 28
    text: "Europe comes second, pushed by the EU AI Act's deepfake labeling rules since August 2026. Market Intelo estimates 27.6% of 2025."
  apac:
    pct: 22
    text: "Asia-Pacific holds about 22% and grows the fastest. Sumsub saw its deepfake cases jump 1,530% in 2023."
  latam:
    pct: 6
    text: "Latin America holds about 6%, per Market Intelo. iProov saw virtual camera attacks first tested in Asia move there next."
  mea:
    pct: 5
    text: "The Middle East and Africa hold about 5%, the smallest share. Sumsub still counted a 450% rise in deepfake cases there in 2023."
note:
- We use Market Intelo's 2025 regional shares and round them so that the five regions add up to 100%
- We cross-check the ranking with Meticulous Research, which also puts North America first and Asia-Pacific fastest
sources:
  - claim: Regional shares of 39.2% North America, 27.6% Europe, 22.4% Asia-Pacific, 5.9% Latin America and 4.9% Middle East and Africa
    url: https://marketintelo.com/report/deepfake-detection-and-synthetic-media-authentication-market
    date: '2026'
    quote: "North America: 39.2%, Europe: 27.6%, Asia Pacific: 22.4%, Latin America: 5.9%, Middle East & Africa: 4.9%"
  - claim: Most identified deepfake detection providers are headquartered in the US
    url: https://gov.uk/government/publications/deepfake-detection-technology/deepfake-detection-technology
    date: '2026-03-26'
    quote: "led by 23 US-headquartered providers out of 59 identified third-party firms as of 2025"
  - claim: EU AI Act Article 50 transparency duties apply from August 2, 2026
    url: https://www.morganlewis.com/blogs/sourcingatmorganlewis/2026/08/eu-ai-acts-transparency-rules-what-went-into-effect-on-2-august
    date: '2026-08'
    quote: "On 2 August 2026, the transparency obligations in Article 50 of the EU AI Act began to apply."
  - claim: North America largest and Asia-Pacific fastest-growing
    url: https://www.meticulousresearch.com/product/deepfake-detection-market-6944
    date: '2026-10'
    quote: "North America is expected to account for the largest market share in 2026, while Asia-Pacific is projected to register the fastest growth"
  - claim: Sumsub counted a 1,530% rise in APAC deepfake cases from 2022 to 2023
    url: https://aapnews.aap.com.au/news/cision20231128AE78899
    date: '2023-11-28'
    quote: "the APAC region has experienced a 1530% surge in deepfake cases from 2022 to 2023"
  - claim: Attack methods tested in Southeast Asia later spread to Latin America
    url: https://itbrief.co.uk/story/iproov-report-warns-of-soaring-ios-injection-attacks
    date: '2026-04-09'
    quote: "with those methods later adopted in other regions, particularly Latin America"
  - claim: Sumsub counted a 450% rise in MEA deepfake cases in 2023
    url: https://businesstech.co.za/news/?p=735165
    date: '2023-12'
    quote: "a 1740% deepfake surge in North America, 780% in Europe and 450% in MEA"
comment: Rounded shares are 39, 28, 22, 6 and 5 percent, which add up to 100.
```

### ed050
```yaml
status: ok
section: Market size
title: What are the growth rate estimates from different sources online?
note: We use direct deepfake detection forecasts first, then a wider detector-tool forecast only as an upside check because its scope is broader than ours.
t:
  24: FIRM
  25: CAGR
  26: COMMENTS
  6: "Meticulous\n\nResearch"
  5: "≈ 25.3%\n\nthrough 2036"
  7: They forecast a direct detection market growing from $990M in 2026 to $9.4B. We use it as the cautious end of our range.
  10: "SNS\n\nInsider"
  9: "≈ 29.5%\n\nthrough 2035"
  11: Their direct forecast reaches $12B by 2035, from $918.6M in 2025. We use it with Astute Analytica to anchor our base case.
  14: "Astute\n\nAnalytica"
  13: "≈ 29.1%\n\nthrough 2035"
  15: Their forecast is almost identical to SNS Insider, reaching $9B by 2035. It confirms growth close to 29% a year.
  18: "Next Move\n\nStrategy"
  17: "≈ 36.5%\n\nthrough 2035"
  19: Their forecast covers a wider detector-tool market. We use it only to test how fast the category could grow if adoption broadens.
sources:
  - claim: Meticulous Research forecasts 25.3% a year from 2026 to 2036, reaching about $9.4B
    url: https://www.meticulousresearch.com/product/deepfake-detection-market-6944
    date: '2026-10'
    quote: "This market is expected to reach USD 9.44 billion by 2036 from an estimated USD 0.99 billion in 2026, registering a CAGR of 25.3%"
  - claim: SNS Insider forecasts 29.5% a year to $12,140.7M in 2035
    url: https://www.snsinsider.com/reports/deepfake-detection-market-11090
    date: '2026'
    quote: "is expected to reach USD 12,140.7 Million by 2035, growing at a CAGR of 29.5% from 2026 to 2035"
  - claim: Astute Analytica forecasts 29.1% a year to $9,008.9M in 2035
    url: https://www.astuteanalytica.com/speak-analyst/deepfake-detection-market
    date: '2026-07-15'
    quote: "projected to reach USD 9,008.9 million by 2035, growing at a CAGR of 29.1%"
  - claim: Next Move Strategy Consulting forecasts 36.5% a year for detector tools to 2035
    url: https://www.nextmsc.com/report/ai-deepfake-detector-tool-market-ic5131
    date: '2026'
    quote: "forecast to reach USD 28.30 Billion by 2035, expanding at a 36.5% CAGR between 2026 and 2035"
```

### ed051
```yaml
status: ok
section: Market size
title: What is a realistic CAGR for the deepfake detection market?
note: Direct deepfake detection forecasts cluster between 25% and 30%, while a wider tool forecast runs higher. We use 28% as a base case, with 20% and 37% as downside and upside scenarios.
t:
  15: BEST CASE ≈ 37%
  17: "≈28%\n\nthrough 2035"
  19: Detection is young, so platform hooks like Microsoft Teams can lift sales fast, but bundling into suites keeps prices down. We use 28%, inside the 25-30% forecasts.
  16: WORST CASE ≈ 20%
sources:
  - claim: Microsoft Teams will let certified third-party detectors flag deepfakes in meetings
    url: https://bleepingcomputer.com/news/security/microsoft-teams-to-add-third-party-deepfake-detection-impersonation-protection
    date: '2026-10-08'
    quote: "Microsoft will soon introduce support for third-party deepfake detection solutions and impersonation protection in Teams meetings."
  - claim: Deepfake detection is expected to be embedded into broader platforms rather than stay standalone
    url: https://varindia.com/news/gartner-maps-emerging-deepfake-detection-market-names-startups-driving-enterprise-adoption
    date: '2026-07-17'
    quote: "deepfake detection capabilities are expected to be embedded into identity verification, fraud prevention and cybersecurity platforms rather than remaining standalone products"
  - claim: Direct forecasts are 25.3%, 29.1% and 29.5%, and the wider tool forecast is 36.5%
    url: https://www.nextmsc.com/report/ai-deepfake-detector-tool-market-ic5131
    date: '2026'
    quote: "expanding at a 36.5% CAGR between 2026 and 2035"
comment: The 20% downside is our own scenario, set about five points under the lowest direct forecast. The 37% upside rounds the wider Next Move forecast.
```
