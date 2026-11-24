# AI in Insurance | Tech and infra | Research results | 2026-11-22

### ed087
```yaml
status: ok
section: Tech and infra
title: What are the tech and infra layers?
page: 1/2
t:
  7: DATA
  10: Policy, claims, and broker records give models a view of each risk before action
  9: MODELS
  11: Prediction engines estimate loss, fraud, or repair cost from policy and claim data
  21: LAYERS
  12: DOCUMENTS
  14: Vision and language tools turn scans, emails, and photos into usable fields
  13: RULES
  15: Coverage, price, and claim rules bound what automated tools may safely decide
sources:
- claim: AI covers insurance pricing, claims and fraud work
  url: https://content.naic.org/insurance-topics/artificial-intelligence
  date: '2026-04-03'
  quote: In the insurance industry, AI is used in areas such as underwriting, pricing, customer service, claims handling, marketing, and fraud detection.
- claim: Insurance-focused AI extracts structured data from risk files
  url: https://www.cytora.com/risk-flow-center/blog/introducing-cytora-platform-3-0
  date: '2025'
  quote: Multi agent LLMs collaborate to digitize - in a fully explainable way - the most complex risk submissions
- claim: Insurers link pricing models with claims feedback
  url: https://www.hyperexponential.com/newsroom/hyperexponential-and-akur8-partnership
  date: '2023-11-20'
  quote: The pricing decision data can then be pulled from hx Renew, integrated with claims data, and sent back to Akur8
note: We separate the intake, prediction, and decision layers used by insurance-specific AI. The boundaries are functional rather than vendor-specific.
```

### ed088
```yaml
status: ok
section: Tech and infra
title: What are the tech and infra layers?
page: 2/2
t:
  7: AGENTS
  10: Insurance AI agents move cases between steps, while human staff review sensitive decisions
  9: LINKS
  11: Links to policy and claims systems let AI act on live records instead of demos
  21: LAYERS
  12: CONTROLS
  14: Audit logs, bias tests, and approval gates show who made each decision and why
  13: FEEDBACK
  15: Paid claims and renewals teach models which risk signals work and where they fail
sources:
- claim: Insurance agents can execute multistep workflows
  url: https://withpace.com/news/product-launch
  date: '2026-06-22'
  quote: Today, we’re launching one multimodal agent that runs every step, end to end.
- claim: Insurance AI needs human oversight
  url: https://content.naic.org/insurance-topics/artificial-intelligence
  date: '2026-04-03'
  quote: Human oversight remains an important part of insurance decision-making.
- claim: Claims feedback can recalibrate risk pricing
  url: https://www.hyperexponential.com/newsroom/hyperexponential-and-akur8-partnership
  date: '2023-11-20'
  quote: The pricing decision data can then be pulled from hx Renew, integrated with claims data, and sent back to Akur8
note: We distinguish live workflow connections and human controls from the underlying models. Feedback comes from real claim and policy outcomes.
```

### ed089
```yaml
status: ok
section: Tech and infra
title: Does every layer carry the same weight?
t:
  38: RANKING
  6: DATA
  14: Bad policy and claim records can weaken every later pricing, fraud, or coverage decision
  7: WORKFLOWS
  24: Links to live claims and quote systems decide whether good models produce real savings
  8: MODELS
  26: Risk and fraud models can improve selection, but need verified losses to show value
  9: CHECKS
  28: Bias tests and audit trails make AI-assisted decisions usable under insurance rules
  10: DOCUMENTS
  30: Reading forms and photos cuts manual entry across risk reviews and claims
  11: INFERENCE
  32: Fast, secure model responses matter when a live quote or claim cannot wait
  12: FEEDBACK
  34: Paid claims and renewals expose drift as weather, repairs, and risks change
  13: SECURITY
  36: A data leak or unsafe agent action can block rollout despite high model accuracy
note: We rank layers by their effect on decisions, production use, and regulatory exposure. This is a directional view, not an industry score.
sources:
- claim: Regulators can require explanations of algorithmic decisions
  url: https://content.naic.org/insurance-topics/artificial-intelligence
  date: '2026-04-03'
  quote: State insurance regulators oversee insurers’ use of AI and may require companies to explain how these tools are used in underwriting, pricing
- claim: Documented production results remain limited
  url: https://evidentinsights.com/insights/insurance-ai-index-2026-report/
  date: '2026'
  quote: 20 of 30 insurers now report at least one AI use case with outcomes (+8 YoY)
- claim: Insurance agent systems require secure integrations
  url: https://withpace.com/news/product-launch
  date: '2026-06-22'
  quote: Today, we’re launching one multimodal agent that runs every step, end to end.
```

### ed090
```yaml
status: ok
section: Tech and infra
title: Where might 80% of AI in insurance value sit?
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
  8: 'Most value is likely in the decisions that shape real policy and claim economics: risk selection, pricing, fraud checks, and settlement. These determine losses, not just staff time.


    Document intake and agents matter because they help those decisions work in daily operations.


    The missing proof is sustained loss-ratio improvement, fair treatment, and audited results at scale.'
note: We treat the 80% framing as a directional hypothesis rather than a measured allocation of value. We prioritize where AI affects insured losses and claims.
sources:
- claim: Most disclosed insurer AI projects still focus on narrow efficiency tasks
  url: https://evidentinsights.com/insights/insurance-ai-index-2026-report/
  date: '2026'
  quote: 49% of disclosed use cases remain narrow in scope, focused on speed, cost reduction, and process efficiency.
- claim: Lemonade reports material automated claim volume
  url: https://marketing-edge-assets.lemonade.com/investor/reports/LMND%202025%20Annual%20Report%20Final%204.22.26.pdf
  date: '2026-04-22'
  quote: As of December 31, 2025, roughly 55% of our claims were automated
- claim: Underwriting AI can cut quote cycle time
  url: https://www.federato.ai/articles/video-how-velocity-reinvented-submission-intake-with-federato
  date: '2024-10-22'
  quote: the average time from a submission being modeling-complete to issuance of a quote dropped from 21 days and 11 hours
```

### ed091
```yaml
status: ok
section: Tech and infra
title: How has tech and infra evolved over the years?
t:
  6: '2017 - 2020


    Early vision AI reached real car damage claims. By 2020, Tokio Marine had adopted Tractable AI for motor damage assessment in Japan'
  7: '2021 - 2023


    Pricing models became live insurer tools. Aviva used hx to build 20 models in nine months as states drafted AI oversight rules'
  8: '2024 - 2025


    Zurich worked with Sixfold. Insurers then added AI submission triage and multi-agent claims handling, including Allianz Nemo'
  9: 'TODAY


    Live deployments now span quote tools, claim calls, photo estimates, and fraud reviews. Guidewire has agreed to buy hyperexponential'
  10: '?


    Next platforms may link risk scores to claim outcomes, trace agents, and prove fairer prices and lower losses across whole books'
note: We use dated insurer deployments and product releases rather than research concepts. Future changes are possibilities, not announced commitments.
sources:
- claim: Tokio Marine announced AI damage assessment in Japan in 2020
  url: https://tractable.ai/ja/tokio-marine-to-use-tractables-ai-to-analyse-auto-damage-across-japan/
  date: '2020-05-07'
  quote: it’s the first time that a major Japanese insurer has deployed an AI auto damage assessment solution into the claims process
- claim: Aviva used new models for writing insurance policies in 2023
  url: https://www.hyperexponential.com/newsroom/aviva-fast-tracks-pricing
  date: '2023-10-17'
  quote: The hx platform cuts build time by 75% to help create 20 new models in just 9 months
- claim: Zurich chose Sixfold for underwriting in 2024
  url: https://www.zurich.com/en/media/news-releases/2024/2024-0529-01
  date: '2024-05-29'
  quote: Sixfold will work with Zurich North America to improve underwriting efficiency by leveraging its purpose-built AI.
- claim: Allianz introduced agentic claims in 2025
  url: https://www.allianz.com/en/mediacenter/news/articles/251103-when-the-storm-clears-so-should-the-claim-queue.html
  date: '2025-11-03'
  quote: Allianz has launched its first agentic AI solution to automate food spoilage claims and drastically cut processing times from days to hours.
- claim: Guidewire announced an agreement to acquire hyperexponential in 2026
  url: https://ir.guidewire.com/news-releases/news-release-details/guidewire-signs-definitive-agreement-acquire-hyperexponential
  date: '2026-10-27'
  quote: for a base purchase price of $1.7 billion in cash, subject to adjustments
```

### ed092
```yaml
status: ok
section: Tech and infra
title: What were the latest tech and infra developments?
page: 1/2
t:
  13: '2023'
  14: Aviva put 20 hx price models into use in nine months, cutting policy quote creation from over an hour to minutes
  15: '2024'
  16: Zurich selected Sixfold to parse broker files and help North America underwriters assess risks and speed up reviews
  17: '2025'
  18: Federato released Submission Triage and Orchestrate, adding agents that prioritize insurer broker submissions and automate work
  19: '2025'
  20: hyperexponential launched Triage, linking AI risk intake, carrier appetite, and quote pricing in one commercial insurance workflow
  21: '2025'
  22: Allianz launched Nemo, using seven focused AI agents to screen food spoilage claims while a human handler confirms the payout
  23: '2025'
  24: Armilla AI launched standalone cover for AI system failures, moving technical model assessment into a live insurance product
note: We selected dated releases that show a real insurer workflow or a newly available insurance product. A launch alone is not proof of lower loss costs.
sources:
- claim: Aviva built 20 insurance pricing models in nine months
  url: https://www.hyperexponential.com/newsroom/aviva-fast-tracks-pricing
  date: '2023-10-17'
  quote: The hx platform cuts build time by 75% to help create 20 new models in just 9 months
- claim: Zurich selected Sixfold to support underwriters
  url: https://www.zurich.com/en/media/news-releases/2024/2024-0529-01
  date: '2024-05-29'
  quote: Sixfold will work with Zurich North America to improve underwriting efficiency by leveraging its purpose-built AI.
- claim: Federato made two agentic underwriting tools generally available
  url: https://www.federato.ai/articles/submission-triage-orchestrate-agentic-ai-launch
  date: '2025-04-29'
  quote: 'Today, Federato is announcing the general availability of two new offerings: Submission Triage'
- claim: hyperexponential launched AI-powered submission triage
  url: https://www.hyperexponential.com/newsroom/hyperexponential-announces-triage-expanding-its-ai-powered-platform-across-the-full-commercial-p-c-underwriting-journey
  date: '2025-09-17'
  quote: Triage uses AI to ingest complex submissions and intelligently prioritise opportunities based on each carrier’s appetite, not just order of arrival.
- claim: Allianz deployed agentic handling of small catastrophe claims
  url: https://www.allianz.com/en/mediacenter/news/articles/251103-when-the-storm-clears-so-should-the-claim-queue.html
  date: '2025-11-03'
  quote: Allianz has launched its first agentic AI solution to automate food spoilage claims and drastically cut processing times from days to hours.
- claim: Armilla launched standalone AI liability insurance in 2025
  url: https://www.armilla.ai/company
  date: not stated
  quote: In April 2025 we launched a standalone, affirmative AI liability policy.
```

### ed093
```yaml
status: ok
section: Tech and infra
title: What were the latest tech and infra developments?
page: 2/2
t:
  13: '2026'
  14: Corgi raised $108M after winning approval for an AI-native startup insurer handling underwriting, claims, and policy operations
  15: '2026'
  16: Travelers launched an agentic voice assistant for customers calling to report auto damage claims, with staff available for handoffs
  17: '2026'
  18: Allianz Commercial deployed 13 hyperexponential pricing tools in 13 weeks across core business lines, moving beyond trial use
  19: '2026'
  20: AXA put the first version of its global AI Hub into use at five group entities for controlled agent deployment and governance
  21: '2026'
  22: Guidewire agreed to buy hyperexponential for $1.7B plus up to $400M contingent, to build AI-native insurance pricing tools
  23: '2026'
  24: Gradient AI launched Sentinel to find signs of costly group health conditions in lab records before they appear in paid claims
note: We rely on dated company disclosures and distinguish live deployments from product launches and announced acquisitions.
sources:
- claim: Corgi announced $108M in financing and carrier approval
  url: https://www.prnewswire.com/news-releases/corgi-insurance-raises-108-million-receives-regulatory-approval-to-launch-the-first-full-stack-insurance-carrier-for-startups-302657727.html
  date: '2026-01-09'
  quote: Corgi announced today that it has raised $108 million in funding
- claim: Travelers launched an AI voice agent for auto loss reporting
  url: https://investor.travelers.com/newsroom/press-releases/news-details/2026/Travelers-Launches-Industry-Leading-Agentic-AI-Claim-Assistant-Developed-with-OpenAI/default.aspx
  date: '2026-02-18'
  quote: This capability is initially being used with customers who are calling to file an auto damage claim
- claim: Allianz Commercial deployed 13 pricing tools in 13 weeks
  url: https://www.hyperexponential.com/newsroom/hyperexponential-powers-allianz-commercial-pricing-transformation
  date: '2026-06-25'
  quote: Working with Allianz Commercial, hx has already delivered 13 pricing tools in just 13 weeks
- claim: AXA deployed its AI Hub to five entities
  url: https://www.axa.com/press/press-releases/axa-and-publicis-sapient-collaborate-to-deploy-global-ai-hub-at-scale
  date: '2026-09-08'
  quote: whose first platform version was delivered in July and is in use across five AXA entities.
- claim: Guidewire agreed to buy hyperexponential for $1.7B base
  url: https://ir.guidewire.com/news-releases/news-release-details/guidewire-signs-definitive-agreement-acquire-hyperexponential
  date: '2026-10-27'
  quote: for a base purchase price of $1.7 billion in cash, subject to adjustments
- claim: Gradient AI launched its early group health claim-risk tool
  url: https://www.gradientai.com/press-gradient-ai-launches-sentinel-group-health-solution/
  date: '2026-11-18'
  quote: Gradient AI, a prominent enterprise software provider of artificial intelligence solutions for the insurance industry, has launched Sentinel
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
  7: 'SUBMIT

    DATA'
  11: 'LOSS

    LABELS'
  15: 'FRAUD

    NOISE'
  19: 'MODEL

    DRIFT'
  24: 'FAIR

    PRICES'
  28: 'CORE

    SYSTEMS'
  32: 'AI

    ERRORS'
  36: 'AUDIT

    TRAILS'
  5: Broker emails, scans, and loss runs arrive in different formats, with gaps and errors
  9: Claims develop over months or years, so the true loss outcome can arrive late
  13: Fraud flags can catch honest claims and flood investigators with weak alerts
  17: Pricing and fraud models can go stale as repair costs, weather, and behavior shift
  22: Risk scores may use hidden proxies for protected traits and create unfair prices
  26: Older policy and claim systems make safe two-way data flows difficult to build
  30: Language models can invent policy terms or misread coverage in complex claims
  34: Insurers need records of training data, model changes, approvals, and decisions
note: We focus on problems that insurance-specific AI teams can address in software, data operations, and governance, not on risks they can eliminate completely.
sources:
- claim: Insurance submissions often need language-based digitization
  url: https://www.cytora.com/risk-flow-center/blog/introducing-cytora-platform-3-0
  date: '2025'
  quote: Multi agent LLMs collaborate to digitize - in a fully explainable way - the most complex risk submissions
- claim: Accurate pricing depends on feedback from paid claims
  url: https://www.hyperexponential.com/newsroom/hyperexponential-and-akur8-partnership
  date: '2023-11-20'
  quote: The pricing decision data can then be pulled from hx Renew, integrated with claims data, and sent back to Akur8
- claim: Insurers must explain AI decisions and avoid unfair discrimination
  url: https://content.naic.org/insurance-topics/artificial-intelligence
  date: '2026-04-03'
  quote: State insurance regulators oversee insurers’ use of AI and may require companies to explain how these tools are used in underwriting, pricing
- claim: Insurance agents must work across policy systems and keep audit trails
  url: https://withpace.com/news/product-launch
  date: '2026-06-22'
  quote: Today, we’re launching one multimodal agent that runs every step, end to end.
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
  7: 'SUBMIT

    DATA'
  11: 'LOSS

    LABELS'
  15: 'FRAUD

    NOISE'
  19: 'MODEL

    DRIFT'
  24: 'FAIR

    PRICES'
  28: 'CORE

    SYSTEMS'
  32: 'AI

    ERRORS'
  36: 'AUDIT

    TRAILS'
  5: One broker sends spreadsheets, another PDFs, and each account uses different terms
  9: A policy sold today may not reveal its true claim cost until years later
  13: Fraud is rare and changing, while a false alert costs staff time and trust
  17: A model trained on old claims may misprice new risks or fail in new conditions
  22: Even lawful data can track protected traits, and fairness rules vary by place
  26: Critical data still lives in old portals, manual queues, and incompatible records
  30: AI can sound certain when its source is missing or a coverage clause is unclear
  34: Multiple vendors, changing models, and humans sharing work make clear logs hard
note: We connect each bottleneck to delayed insurance feedback, fragmented records, and the need to explain customer-facing decisions.
sources:
- claim: Insurance AI must comply with laws and avoid unfair decisions
  url: https://content.naic.org/insurance-topics/artificial-intelligence
  date: '2026-04-03'
  quote: State insurance regulators oversee insurers’ use of AI and may require companies to explain how these tools are used in underwriting, pricing
- claim: Brokers send mixed documents requiring digitization
  url: https://www.cytora.com/risk-flow-center/blog/introducing-cytora-platform-3-0
  date: '2025'
  quote: Multi agent LLMs collaborate to digitize - in a fully explainable way - the most complex risk submissions
- claim: Pricing needs continuous feedback from claims outcomes
  url: https://www.hyperexponential.com/newsroom/hyperexponential-and-akur8-partnership
  date: '2023-11-20'
  quote: The pricing decision data can then be pulled from hx Renew, integrated with claims data, and sent back to Akur8
- claim: Insurance agents need full workflow audit lineage
  url: https://withpace.com/news/product-launch
  date: '2026-06-22'
  quote: Today, we’re launching one multimodal agent that runs every step, end to end.
```

### ed096
```yaml
status: ok
section: Tech and infra
title: When can we realistically expect to solve them?
t:
  39: BOTTLENECK
  38: WHY THIS TIMELINE
  41: BOTTLENECK
  40: WHY THIS TIMELINE
  7: 'SUBMIT

    DATA'
  11: 'LOSS

    LABELS'
  15: 'FRAUD

    NOISE'
  19: 'MODEL

    DRIFT'
  24: 'FAIR

    PRICES'
  28: 'CORE

    SYSTEMS'
  32: 'AI

    ERRORS'
  36: 'AUDIT

    TRAILS'
  5: Intake tools already read forms well, but wider data standards need insurer and broker adoption
  9: Claims feedback can improve model tests, but slow loss development takes several years
  13: Better claim graphs and human review can cut noise, but fraud patterns keep changing
  17: Monitoring can flag drift soon, but stable results need multi-year claim comparisons
  22: Better testing can reveal proxy bias, while approved pricing still depends on local rules
  26: Agent connectors are advancing, but replacing decades of core software takes longer
  30: Source checks and human review reduce errors, but full automated coverage decisions remain risky
  34: Logging can be deployed quickly, though regulator-ready audits need years of real use
  42: '2028'
  43: '2031'
  44: '2029'
  45: '2029'
  46: '2032'
  47: '2032'
  48: '2030'
  49: '2028'
note: We estimate when materially better tools could be common, not when risks vanish. These dates are analyst forecasts and have no consensus benchmark.
sources:
- claim: Intake automation tools already exist
  url: https://www.cytora.com/risk-flow-center/blog/introducing-cytora-platform-3-0
  date: '2025'
  quote: Multi agent LLMs collaborate to digitize - in a fully explainable way - the most complex risk submissions
- claim: Human review remains important in insurance AI
  url: https://content.naic.org/insurance-topics/artificial-intelligence
  date: '2026-04-03'
  quote: Human oversight remains an important part of insurance decision-making.
- claim: Regulation requires governance and explainable decisions
  url: https://content.naic.org/insurance-topics/artificial-intelligence
  date: '2026-04-03'
  quote: State insurance regulators oversee insurers’ use of AI and may require companies to explain how these tools are used in underwriting, pricing
- claim: Current deployments mostly target narrow tasks
  url: https://evidentinsights.com/insights/insurance-ai-index-2026-report/
  date: '2026'
  quote: 49% of disclosed use cases remain narrow in scope, focused on speed, cost reduction, and process efficiency.
```

### ed097
```yaml
status: ok
section: Tech and infra
title: Which bold bets could reshape AI in insurance?
t:
  9: AUTONOMOUS CLAIMS
  12: LIVE RISK PRICES
  15: BROKER AI AGENTS
  18: AI RISK COVER
  33: 'NEAR-TERM HORIZON

    (0-5 YEARS)'
  7: It is an agent that checks coverage, spots fraud, and pays simple claims under clear limits
  10: It is a risk price that adjusts as new loss data and verified exposure signals arrive
  13: It is an AI broker assistant that reads client needs and completes multi-carrier quotes
  16: It is an insurance product that pays when certified AI agents fail in defined ways
  21: LOSS LOOP PRICING
  24: VERIFIED FAIRNESS
  27: CLAIM PROOF GRAPH
  30: AGENT TO AGENT COVER
  34: 'LONG-TERM HORIZON

    (5-10 YEARS)'
  19: It is a pricing model that learns reliably from each settled loss and new exposure
  22: It is proof that each automated risk price is fair, traceable, and legal in each market
  25: It is a shared map of evidence that can verify claim events without repeat data entry
  28: It is policy buying and claims between customer and insurer agents, with consent and checks
note: We frame these as possible product bets, grounded in live claims AI, pricing platforms, AI agents, and emerging AI liability coverage.
sources:
- claim: Allianz used AI agents to automate claim tasks
  url: https://www.allianz.com/en/mediacenter/news/articles/251103-when-the-storm-clears-so-should-the-claim-queue.html
  date: '2025-11-03'
  quote: Allianz has launched its first agentic AI solution to automate food spoilage claims and drastically cut processing times from days to hours.
- claim: Claims data can recalibrate insurance pricing
  url: https://www.hyperexponential.com/newsroom/hyperexponential-and-akur8-partnership
  date: '2023-11-20'
  quote: The pricing decision data can then be pulled from hx Renew, integrated with claims data, and sent back to Akur8
- claim: AI agents can run insurance operations end to end
  url: https://withpace.com/news/product-launch
  date: '2026-06-22'
  quote: Today, we’re launching one multimodal agent that runs every step, end to end.
- claim: AI agent liability policies exist
  url: https://www.aiuc.com/research/announcements/elevenlabs-secures-first-of-its-kind-ai-agent-insurance
  date: '2026-02-12'
  quote: ElevenLabs, the leading AI audio research and product company, has rolled-out a first-of-its-kind AI insurance policy
- claim: Zurich already works with insurance-specific AI underwriting
  url: https://www.zurich.com/en/media/news-releases/2024/2024-0529-01
  date: '2024-05-29'
  quote: Sixfold will work with Zurich North America to improve underwriting efficiency by leveraging its purpose-built AI.
```

### ed098
```yaml
status: ok
section: Tech and infra
title: Which companies are working on groundbreaking tech today?
t:
  8: SIXFOLD
  6: They read broker files and build risk summaries and next steps for underwriters
  24: AKUR8
  22: They use transparent machine learning to improve insurance price and reserve models
  11: FEDERATO
  9: They use AI to triage insurance submissions and match new risks to portfolio goals
  27: PACE
  25: They deploy agents that read forms, update core systems, and process insurance work
  14: TRACTABLE
  12: They assess car damage from photos to shorten claims and support quick payouts
  30: AIUC
  28: They test AI agents against failure risks and back that testing with liability cover
  17: CYTORA
  15: They use language AI to digitize complex broker and reinsurer risk submissions
  33: ARMILLA AI
  31: They insure AI model failures with technical risk reviews and dedicated cover
logos:
- name: Sixfold
  domain: sixfold.ai
- name: Akur8
  domain: akur8.com
- name: Federato
  domain: federato.ai
- name: Pace
  domain: withpace.com
- name: Tractable
  domain: tractable.ai
- name: AIUC
  domain: aiuc.com
- name: Cytora
  domain: cytora.com
- name: Armilla AI
  domain: armilla.ai
note: We chose independent companies whose central products apply AI to insurance decisions, workflows, claims, or model-linked insurance risk.
sources:
- claim: Sixfold supports large volumes of insurance submissions
  url: https://www.sixfold.ai/content/category/feature-release
  date: not stated
  quote: We learned this by processing more than 1.5 million submissions across more than 50 lines of business
- claim: Akur8 offers transparent ML for insurer pricing
  url: https://www.akur8.com/news/akur8-acquires-matrisk-bringing-powerful-filings-search-and-market-intelligence-to-its-pricing-platform
  date: '2026-01-06'
  quote: Akur8, the next-generation insurance pricing and reserving solution built on transparent machine learning
- claim: Federato launched underwriting submission triage
  url: https://www.federato.ai/articles/submission-triage-orchestrate-agentic-ai-launch
  date: '2025-04-29'
  quote: 'Today, Federato is announcing the general availability of two new offerings: Submission Triage'
- claim: Pace uses AI agents for end-to-end insurance work
  url: https://withpace.com/news/product-launch
  date: '2026-06-22'
  quote: Today, we’re launching one multimodal agent that runs every step, end to end.
- claim: Tractable assesses motor damage photos for claims
  url: https://tractable.ai/case-studies/admiral-seguros/
  date: not stated
  quote: In 2021, Admiral Seguros processed 12,000 touchless claims using Tractable AI.
- claim: AIUC combines risk assessments with AI agent cover
  url: https://www.aiuc.com/research/announcements/elevenlabs-secures-first-of-its-kind-ai-agent-insurance
  date: '2026-02-12'
  quote: ElevenLabs, the leading AI audio research and product company, has rolled-out a first-of-its-kind AI insurance policy
- claim: Cytora digitizes commercial insurance risk files
  url: https://www.cytora.com/risk-flow-center/blog/introducing-cytora-platform-3-0
  date: '2025'
  quote: Multi agent LLMs collaborate to digitize - in a fully explainable way - the most complex risk submissions
- claim: Armilla specializes in model-driven AI insurance
  url: https://www.armilla.ai/company
  date: not stated
  quote: In April 2025 we launched a standalone, affirmative AI liability policy.
```

### iv_pipeline
```yaml
status: ok
section: Tech and infra
title: Which AI tools are big insurers already using for real?
t:
  38: SCALE
  34: Pricing models used to write commercial insurance policies
  37: AVIVA · HX
  27: SCALE
  26: ALLIANZ · HX
  24: 13 pricing tools deployed across Allianz Commercial lines
  23: SCALE
  22: ZURICH · SIXFOLD
  20: AI risk summaries used by 200+ underwriters in 22 offices
  19: SCALE
  18: AXA · SHIFT
  16: Fraud screening has checked over 1M Swiss claims
  15: SCALE
  12: 12,000 touchless car claims processed in a year
  14: ADMIRAL · TRACTABLE
  11: LIVE
  10: TRAVELERS · IN HOUSE
  8: Voice AI takes customer calls to start auto damage claims
  7: SCALE
  6: LEMONADE · IN HOUSE
  4: Lemonade AI Jim automated about 55% of all claims filed in 2025
  3: SCALE
  2: ALLIANZ · IN HOUSE
  0: German pet claims automated in nearly half of all cases in 2025
comment: HX is the product brand used by hyperexponential. SHIFT is the vendor brand Shift Technology uses on its products. These labels fit fixed widths.
note: We include only insurer-named live uses, not proposed partnerships. Scale means use across a business line or network. Figures are reported by insurers or named vendors.
sources:
- claim: Aviva used 20 pricing models for real policies
  url: https://www.hyperexponential.com/newsroom/aviva-fast-tracks-pricing
  date: '2023-10-17'
  quote: The hx platform cuts build time by 75% to help create 20 new models in just 9 months
- claim: Allianz Commercial deployed 13 tools
  url: https://www.hyperexponential.com/newsroom/hyperexponential-powers-allianz-commercial-pricing-transformation
  date: '2026-06-25'
  quote: Working with Allianz Commercial, hx has already delivered 13 pricing tools in just 13 weeks
- claim: Zurich used Sixfold across 22 offices
  url: https://www.sixfold.ai/events/scaling-ai-in-practice
  date: '2026-02-25'
  quote: Zurich North America expanded from a single team to more than 200 underwriters across 22 offices.
- claim: AXA Switzerland screened over one million claims
  url: https://www.shift-technology.com/resources/case-studies/axa-switzerland-insurance-fraud-detection-success
  date: not stated
  quote: AXA has now analyzed more than 1 million claims with Shift, and stopped over €12M in fraud
- claim: Admiral Seguros processed 12,000 touchless motor claims in 2021
  url: https://tractable.ai/case-studies/admiral-seguros/
  date: not stated
  quote: In 2021, Admiral Seguros processed 12,000 touchless claims using Tractable AI.
- claim: Travelers is using voice AI for real auto claim calls
  url: https://investor.travelers.com/newsroom/press-releases/news-details/2026/Travelers-Launches-Industry-Leading-Agentic-AI-Claim-Assistant-Developed-with-OpenAI/default.aspx
  date: '2026-02-18'
  quote: This capability is initially being used with customers who are calling to file an auto damage claim
- claim: Lemonade automated roughly 55% of its 2025 claims
  url: https://marketing-edge-assets.lemonade.com/investor/reports/LMND%202025%20Annual%20Report%20Final%204.22.26.pdf
  date: '2026-04-22'
  quote: As of December 31, 2025, roughly 55% of our claims were automated
- claim: Allianz automated 49.7% of German pet claims in 2025
  url: https://www.allianz.com/en/mediacenter/news/articles/260318-responsible-use-of-ai-at-allianz.html
  date: '2026-03-18'
  quote: In Allianz pet insurance in Germany, fully automated processing accounted for 49.7% of claims in 2025
```
