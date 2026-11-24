# Neocloud, chapter 09 Investor bets and top players (researched by Claude on 19 Nov 2026, at Pierre's request)

### iv_deals
```yaml
status: ok
section: Investor bets
title: Which corporate deals shaped the market?
note: We used contract values from company releases, filings and the press. Amounts marked "up to" include orders that the client may or may not place later.
t:
  13: 2026 (AUG)
  15: 2026 (MAY)
  17: 2026 (APR)
  19: 2026 (MAR)
  21: 2026 (JAN)
  23: 2025 (NOV)
  14: Anthropic agreed to rent about 460 MW from Nscale for six years, in a deal worth up to $45B from late 2027 {1|SEC}
  16: Nvidia signed a five-year $3.4B contract to rent GPU capacity from IREN, a former bitcoin miner turned AI cloud {1|IREN}
  18: Meta expanded its deal with CoreWeave to about $21B of AI cloud capacity, running through December 2032 {1|CoreWeave}
  20: Meta signed a five-year deal with Nebius for $12B of dedicated capacity, worth up to $27B with later orders {1|Nebius}
  22: Nvidia invested $2B in CoreWeave at $87.20 a share, to speed up the build of its AI factories {1|CoreWeave}
  24: Microsoft signed a five-year $9.7B contract with IREN for access to Nvidia GB300 GPUs in Texas {1|IREN}
sources:
- claim: Nscale Anthropic up to about $45B
  url: https://www.sec.gov/Archives/edgar/data/2110365/000119312526395475/ck0002110365-20260918.htm
  date: '2026-09-18'
  quote: The Anthropic Services Agreements provide for aggregate payments to us of up to approximately $44.6 billion.
- claim: 460 MW, six years, late 2027
  url: https://techcrunch.com/2026/08/26/anthropic-continues-compute-gobbling-streak-in-45-billion-deal-with-nscale
  date: '2026-08-26'
  quote: The compute capacity is expected to start powering the AI lab's services in late 2027, the source said.
- claim: IREN Nvidia $3.4B
  url: https://iren.gcs-web.com/news-releases/news-release-details/iren-secures-34bn-ai-cloud-contract-nvidia
  date: '2026-05-07'
  quote: The total value of the five-year contract is approximately $3.4 billion.
- claim: CoreWeave Meta $21B
  url: https://www.coreweave.com/news/coreweave-and-meta-announce-21-billion-expanded-ai-infrastructure-agreement
  date: '2026-04-09'
  quote: provide AI cloud capacity through December 2032 for approximately $21 billion.
- claim: Nebius Meta $12B and up to $27B
  url: https://nebius.com/newsroom/nebius-signs-new-ai-infrastructure-agreement-with-meta
  date: '2026-03-16'
  quote: Under the five-year agreement, Nebius will provide $12 billion of dedicated capacity across multiple locations
- claim: Nvidia $2B in CoreWeave
  url: https://coreweave.com/news/nvidia-and-coreweave-strengthen-collaboration-to-accelerate-buildout-of-ai-factories
  date: '2026-01-26'
  quote: NVIDIA has invested $2 billion in CoreWeave Class A common stock at a purchase price of $87.20 per share.
- claim: IREN Microsoft $9.7B
  url: https://iren.gcs-web.com/news-releases/news-release-details/iren-secures-97bn-ai-cloud-contract-microsoft
  date: '2025-11-03'
  quote: IREN will provide Microsoft with access to NVIDIA GB300 GPUs over a five-year term
```

### ed172
```yaml
status: ok
section: Top players
title: What are the different types of startup?
note: We grouped neocloud startups by what they sell and how they bill, using the categories of our company database and their own offers.
t:
  8: "💻\nStartups renting GPU servers by the hour or month"
  6: "⚡\nStartups serving AI models billed by the token"
  5: "🏭\nStartups building whole clusters for one big AI lab"
  7: "🔁\nStartups reselling spare GPUs on an open marketplace"
  12: "🌍\nStartups keeping AI chips and data in one country"
  10: "🧠\nStartups selling tools to train and tune AI models"
  9: "🔋\nFormer bitcoin miners turning power sites into AI clouds"
  11: "🔬\nChip makers renting out clouds built on their own chips"
```

### ed173
```yaml
status: ok
section: Top players
title: Who owns what?
note: We compare six of the largest players from company filings and releases. The table is simplified and shows what each one had in place by November 2026.
t:
  10: "NVIDIA\nBACKED"
  14: "MICROSOFT\nCLIENT"
  28: "FORMER\nMINER"
  32: "STOCK\nLISTED"
  40: "PER\nTOKEN"
  6: COREWEAVE
  9: 'YES'
  13: 'YES'
  27: 'YES'
  31: 'YES'
  39: 'YES'
  7: NEBIUS
  11: 'YES'
  15: 'YES'
  29: 'NO'
  33: 'YES'
  41: 'YES'
  8: NSCALE
  12: 'YES'
  16: 'YES'
  30: 'YES'
  34: 'NO'
  42: 'YES'
  19: LAMBDA
  21: 'YES'
  23: 'YES'
  35: 'NO'
  37: 'NO'
  43: 'NO'
  20: CRUSOE
  22: 'YES'
  24: 'YES'
  36: 'YES'
  38: 'NO'
  44: 'YES'
  46: IREN
  47: 'NO'
  48: 'YES'
  49: 'YES'
  50: 'YES'
  51: 'NO'
sources:
- claim: Nvidia invested in CoreWeave and Nebius
  url: https://nebius.com/newsroom/nvidia-and-nebius-partner-to-scale-full-stack-ai-cloud
  date: '2026-03-11'
  quote: NVIDIA will invest $2 billion in Nebius
- claim: Nvidia among Lambda investors
  url: https://lambda.ai/blog/lambda-raises-480m-to-expand-ai-cloud-platform
  date: '2025-02-19'
  quote: participation from new investors Andrej Karpathy, ARK Invest, Fincadia Advisors, G Squared, In-Q-Tel (IQT), KHK & Partners, NVIDIA, and others.
- claim: Nvidia in Crusoe Series E
  url: https://www.thestar.com.my/tech/tech-news/2025/10/24/ai-data-centre-startup-crusoe-raising-138-billion-in-latest-funding-round
  date: '2025-10-24'
  quote: co-led by Valor Equity Partners and Mubadala Capital and includes Nvidia, Fidelity Management and Founders Fund
- claim: Nvidia backs Nscale, spun out of a bitcoin miner
  url: https://www.theenergymag.com/news/2026-03-09/nscale-ai-2-billion
  date: '2026-03-09'
  quote: the AI infrastructure firm spun out of Bitcoin mining company Arkon Energy.
- claim: Nscale not yet listed, filed for NYSE
  url: https://w.media/?p=43614
  date: '2026-09-21'
  quote: the number of shares to be offered and the expected price range have not yet been disclosed.
- claim: Lambda shut its token-priced inference API
  url: https://docs.runpod.io/migrate/lambda
  date: '2026'
  quote: Lambda sunset its hosted Inference API (the shutdown date was September 25, 2025)
- claim: CoreWeave sells inference per token
  url: https://wandb.ai/wandb_fc/product-announcements-fc/reports/Introducing-W-B-Inference-powered-by-CoreWeave--VmlldzoxMzI1NjU0MQ
  date: '2025'
  quote: usage-based pricing per million input and output tokens.
- claim: Nebius Token Factory per token
  url: https://nebius.com/services/token-factory
  date: '2026'
  quote: Deploy your own checkpoints directly on Token Factory endpoints with guaranteed performance and transparent per-token pricing.
- claim: Microsoft deals with Lambda, IREN, Nscale, Nebius
  url: https://lambda.com/blog/lambda-announces-multibillion-dollar-agreement-with-microsoft-to-deploy-ai-infrastructure-powered-by-tens-of-thousands-of-nvidia-gpus
  date: '2025-11-03'
  quote: announced a multibillion-dollar agreement with Microsoft to deploy AI infrastructure
- claim: Crusoe campus for Microsoft
  url: https://www.crusoe.ai/resources/newsroom/crusoe-announces-new-900-mw-ai-factory-campus-in-abilene-texas-to-support-microsoft-ai-infrastructure
  date: '2026-03-27'
  quote: Land clearing and site preparation for the new campus are already underway
- claim: Crusoe started with stranded gas flares
  url: https://techgistafrica.com/world-regional-news/north-america/denver%E2%80%91based-data-centre-startup-crusoe-secures-us1-38-billion-in-series-e-funding/amp
  date: '2025-10'
  quote: Crusoe originally built its business around converting stranded natural-gas flares into power for computing workloads
comment: IREN and Nebius are listed companies (IREN BORDERLINE, Nebius NOT A STARTUP), shown for comparison. Crusoe's early computing on gas flares was bitcoin mining (sold to NYDIG in 2025).
```

### ed174
```yaml
status: ok
section: Top players
title: What have been the different waves of 'hot' startups over time?
note: We grouped companies by when they became visible through contracts, listings or large rounds. It is a directional history, not a formal taxonomy.
t:
  6: "2017 - 2021\n\n\nCoreWeave and Crusoe started close to crypto mining while Lambda sold AI servers. GPU rental was a niche next to the big clouds."
  7: "2022 - 2023\n\n\nChatGPT set off a rush for Nvidia chips. CoreWeave won Microsoft as a client and borrowed $2.3B against contracts it had signed."
  8: "2024 - 2025\n\n\nCoreWeave listed in 2025 as inference clouds took off. Fireworks AI, Baseten, Modal and fal all passed $1B in value."
  9: "TODAY\n\n\nNscale signed $45B with Anthropic, Crusoe is worth $31B and Fireworks AI $18B. Giant contracts now drive the market."
  10: "?\n\n\nThe next winners may be those that serve many apps at a profit, not those with the most GPUs. Power, debt costs and chip prices will decide."
sources:
- claim: CoreWeave 2023 debt
  url: https://www.coreweave.com/blog/coreweave-secures-2-3-billion-debt-financing-magnetar-capital-blackstone
  date: '2023-08-03'
  quote: we secured a $2.3 billion debt facility
- claim: Microsoft and CoreWeave 2023
  url: https://www.investing.com/news/stock-market-news/microsoft-inks-computing-infra-deal-with-coreweave--cnbc-3096521
  date: '2023-06-01'
  quote: Microsoft Corp (NASDAQ:MSFT) may spend billions of dollars over multiple years on computing infrastructure from start-up CoreWeave
- claim: Crusoe about $31B
  url: https://www.crusoe.ai/resources/newsroom/crusoe-announces-series-f-funding
  date: '2026-09-17'
  quote: initial closing of its anticipated $3.9 billion Series F funding round, at a $30.9 billion post-money valuation.
- claim: Fireworks about $18B
  url: https://fireworks.ai/news/fireworks-raises-1-5-billion-series-d
  date: '2026-07-16'
  quote: announced a $1.505 billion Series D round at a $17.5 billion valuation.
- claim: Lambda sold AI infrastructure since 2017
  url: https://lambda.com/blog/lambda-raises-320m-to-build-a-gpu-cloud-for-ai
  date: '2024-02-15'
  quote: When we started selling AI infrastructure in 2017, the transformer architecture had just been published
```

### ed175
```yaml
status: ok
section: Top players
title: Which neocloud startups stand out?
note: We selected companies that recur in recent contracts, funding rounds and results. This is a curated view, not an objective ranking.
t:
  19: FIREWORKS AI
  18: It passed $1B in yearly revenue pace and raised $1.5B in 2026
  23: COREWEAVE
  22: It reported $3.7B of quarterly sales and a $133B order backlog
  27: MODAL
  26: It raised $750M at a $16B value after passing a $1B run rate
  25: BASETEN
  24: It raised $1.5B at $13B as its inference volume grew 40x
  21: NSCALE
  20: It signed a $45B deal with Anthropic and filed for a US listing
sources:
- claim: Fireworks $1B run rate
  url: https://fireworks.ai/blog/fireworks-series-d-funding
  date: '2026-07-15'
  quote: Fireworks surpasses $1 billion in annualized revenue run rate and serves more than 40 trillion tokens every day.
- claim: CoreWeave Q3 revenue and backlog
  url: https://investors.coreweave.com/news/news-details/2026/CoreWeave-Reports-Strong-Third-Quarter-2026-Results/
  date: '2026-11-10'
  quote: Revenue backlog was approximately $132.5 billion as of September 30, 2026.
- claim: Modal Series D
  url: https://www.axios.com/pro/enterprise-software-deals/2026/10/14/modal-accel-ai-infrastructure
  date: '2026-10-14'
  quote: raised a $750 million Series D at a $15.75 billion post-money valuation
- claim: Baseten Series F
  url: https://www.baseten.co/blog/announcing-our-series-f/
  date: '2026-06-22'
  quote: Over the last year, our revenue has grown 20x, and inference volume has grown 40x.
- claim: Nscale IPO filing
  url: https://pulse2.com/nscale-files-for-ipo/
  date: '2026-09-19'
  quote: The London-based company has applied to list its ordinary shares on the New York Stock Exchange under the ticker symbol NSCL.
```

### ed176
```yaml
status: ok
section: Top players
title: Which startups are in the news lately?
page: 1/2
note: We focused on companies whose main business is renting AI computing, and kept only events reported by the company, a filing or the press.
t:
  12: 2026 (NOV)
  13: fal raised $1.3B in a round led by Bessemer, doubling its value to $16B as demand for image and video AI kept rising {1|TechCrunch}
  14: 2026 (NOV)
  15: Nscale said in a filing that it had not yet secured binding funding for the GPUs behind its $45B Anthropic deal {1|SEC}
  16: 2026 (OCT)
  17: Modal raised $750M at a $16B valuation, led by Accel, after passing a $1B yearly revenue run rate five months after its last round {1|Modal}
  18: 2026 (OCT)
  19: Microsoft pulled out of Nscale's flagship UK data center after grid delays pushed its power supply into the 2030s {1|Reuters}
  20: 2026 (OCT)
  21: Lambda closed $1B of fixed-rate debt backed by contracts with two hyperscale clients, to fund three GPU sites {1|Lambda}
  22: 2026 (SEP)
  23: Crusoe raised $3.9B in a Series F at a $31B valuation, to build more AI factories and grow its own cloud {1|Crusoe}
sources:
- claim: fal $1.3B, $16B
  url: https://techcrunch.com/2026/11/03/ai-inference-startup-fal-doubles-its-valuation-to-16b-as-demand-surges/
  date: '2026-11-03'
  quote: has raised $1.3 billion in its latest funding round led by Bessemer Venture Partners
- claim: Nscale funding not secured
  url: https://www.sec.gov/Archives/edgar/data/2110365/000119312526458722/ck0002110365-20261112.htm
  date: '2026-11-12'
  quote: we have not obtained binding commitments for any of the financings required to fund performance under the Anthropic Services Agreements
- claim: Modal Series D
  url: https://modal.com/blog/1-billion-annualized-run-rate-series-d
  date: '2026-10-14'
  quote: We recently crossed $1B in annualized run rate
- claim: Microsoft exits Nscale UK site
  url: https://www.investing.com/news/stock-market-news/microsoft-pulls-out-of-uk-nscale-data-centre-deal-over-power-delay-4960690
  date: '2026-10-19'
  quote: power connection delays pushed its expected supply date into the 2030s
- claim: Lambda $1B debt
  url: https://lambda.com/blog/lambda-closes-1-billion-senior-secured-fixed-rate-financing
  date: '2026-10-01'
  quote: backed by contracted cash flows from two hyperscale customers
- claim: Crusoe Series F
  url: https://www.crusoe.ai/resources/newsroom/crusoe-announces-series-f-funding
  date: '2026-09-17'
  quote: initial closing of its anticipated $3.9 billion Series F funding round, at a $30.9 billion post-money valuation.
```

### ed177
```yaml
status: ok
section: Top players
title: Which startups are in the news lately?
page: 2/2
note: We focused on companies whose main business is renting AI computing, and kept only events reported by the company, a filing or the press.
t:
  13: 2026 (SEP)
  14: Fluidstack raised $1.5B in a round led by Jane Street that valued the cloud behind Anthropic's new sites at $18B {1|Forbes}
  15: 2026 (AUG)
  16: Anthropic agreed to rent about 460 MW from Nscale for six years in a deal worth $45B, with service starting in late 2027 {1|TechCrunch}
  17: 2026 (JUL)
  18: Fireworks AI raised $1.5B at an $18B valuation after passing a $1B revenue run rate and 40 trillion tokens a day {1|Fireworks}
  19: 2026 (JUL)
  20: Together AI raised $800M in a round led by Aramco Ventures to grow its cloud for training and serving open models {1|Reuters}
  21: 2026 (JUN)
  22: Baseten raised $1.5B at a $13B valuation after its revenue grew 20 times and its inference volume 40 times {1|Baseten}
  23: 2026 (JUN)
  24: TensorWave raised $350M at a $1.6B valuation, co-led by AMD, to grow its cloud built only on AMD chips {1|Magnetar}
sources:
- claim: Fluidstack $1.5B at $18B
  url: https://www.forbes.com.au/news/innovation/fluidstack-is-now-worth-18-billion/
  date: '2026-09-03'
  quote: A tiny startup helping Google take on Nvidia is now worth $18 billion.
- claim: Anthropic Nscale $45B
  url: https://techcrunch.com/2026/08/26/anthropic-continues-compute-gobbling-streak-in-45-billion-deal-with-nscale
  date: '2026-08-26'
  quote: The compute capacity is expected to start powering the AI lab's services in late 2027, the source said.
- claim: Fireworks Series D
  url: https://fireworks.ai/blog/fireworks-series-d-funding
  date: '2026-07-15'
  quote: Fireworks surpasses $1 billion in annualized revenue run rate and serves more than 40 trillion tokens every day.
- claim: Together AI $800M
  url: https://www.investing.com/news/stock-market-news/together-ai-raises-800-million-at-83-billion-valuation-4771027
  date: '2026-07-01'
  quote: raised $800 million in a funding round led by Aramco Ventures
- claim: Baseten Series F
  url: https://www.baseten.co/blog/announcing-our-series-f/
  date: '2026-06-22'
  quote: Over the last year, our revenue has grown 20x, and inference volume has grown 40x.
- claim: TensorWave Series B
  url: https://www.magnetar.com/insights/tensorwave-raises-350-million-series-b-at-155b-valuation
  date: '2026-06-10'
  quote: TensorWave, the all-AMD AI cloud specializing in high-performance, memory-intensive workloads, today announced it has raised $350 million in Series B funding.
```

### ed178
```yaml
status: ok
section: Top players
title: Who are the current market leaders?
note: We use contracts, revenue and funding reported by the companies. This is directional, because no official leaderboard of neocloud companies exists.
t:
  9: "GPU\nCLOUDS"
  7: CoreWeave and Lambda lead, both counting Microsoft among their big clients
  21: "COMPUTE\nMARKETPLACES"
  19: Vast.ai and SF Compute lead, letting teams rent or resell GPUs at live prices
  12: "INFERENCE\nCLOUDS"
  10: Fireworks AI and Baseten lead, each now valued at $13B or more
  24: "TRAINING\nPLATFORMS"
  22: Together AI leads, after raising $800M to train and serve open models
  15: "DEDICATED\nCLUSTERS"
  13: Nscale and Fluidstack lead, building whole sites for Anthropic and Microsoft
  27: BIGGEST BACKLOG
  25: CoreWeave leads, with about $133B of signed future revenue
sources:
- claim: Vast.ai live prices
  url: https://vast.ai/
  date: '2026'
  quote: Prices set by supply and demand across 20,000+ GPUs.
- claim: SF Compute resale marketplace
  url: https://www.eweek.com/news/sf-compute-ai-funding/
  date: '2025-11'
  quote: By enabling buyers to resell unused capacity in a flexible marketplace
- claim: CoreWeave backlog
  url: https://investors.coreweave.com/news/news-details/2026/CoreWeave-Reports-Strong-Third-Quarter-2026-Results/
  date: '2026-11-10'
  quote: Revenue backlog was approximately $132.5 billion as of September 30, 2026.
- claim: Anthropic data centers with Fluidstack
  url: https://www.forbes.com.au/news/innovation/fluidstack-is-now-worth-18-billion/
  date: '2026-09-03'
  quote: A tiny startup helping Google take on Nvidia is now worth $18 billion.
```

### ed182
```yaml
status: ok
section: Top players
title: Who leads each neocloud link, from power to clients?
note: We selected leaders by contracts, sites and funding they have announced. The value chain is simplified for clarity.
t:
  11: POWER
  12: GPU SUPPLY
  13: CLUSTERS
  14: SOFTWARE
  15: CAPITAL
  16: Crusoe, IREN and Nscale lead on power, with their own energy sites from Abilene in Texas to Narvik in Norway
  17: CoreWeave and Nebius lead on chip access, each backed by a $2B Nvidia stake, and CoreWeave ran Vera Rubin first
  18: Nscale, Fluidstack and CoreWeave lead on giant clusters, building whole sites for Anthropic, Meta and Microsoft
  19: Fireworks AI and Modal lead the software that runs client models, each past a $1B yearly revenue pace
  20: Lambda and Nebius lead on funding, with loans and prepayments backed by contracts signed with big clients
sources:
- claim: CoreWeave first Vera Rubin in production
  url: https://coreweave.com/news/coreweave-delivers-nvidia-vera-rubin-nvl72-performance-at-production-scale-starting-with-cognition
  date: '2026-09-30'
  quote: with Cognition as the first customer anywhere running production workloads on the system.
- claim: Narvik campus
  url: https://www.nscale.com/press-releases/nscale-microsoft-norway
  date: '2026-04-14'
  quote: the 230 MW Nscale Narvik campus will add more than 30,000 NVIDIA Rubin GPUs in deployment
- claim: Abilene
  url: https://www.crusoe.ai/resources/newsroom/crusoe-announces-flagship-abilene-data-center-is-live
  date: '2025-09-30'
  quote: the first phase of Stargate's flagship data center campus in Abilene, Texas, is now up and running on Oracle Cloud Infrastructure
- claim: Nebius prepayments
  url: https://www.sec.gov/Archives/edgar/data/1513845/000110465926126008/tm2629571d1_ex99-2.htm
  date: '2026-11-12'
  quote: More than 90% of contract value signed in the third quarter carried a prepayment
- claim: Modal run rate
  url: https://modal.com/blog/1-billion-annualized-run-rate-series-d
  date: '2026-10-14'
  quote: We recently crossed $1B in annualized run rate
```

### ed183
```yaml
status: ok
section: Top players
title: And at different regions of the world?
note: We mapped leaders by company headquarters and announced sites. Most of them serve clients worldwide, so regions show where companies are based.
regions:
  apac:
    name: ASIA
    text: Asia is led by India's Yotta, which planned 20,736 Nvidia GPUs and a $1B cloud deal with Nvidia in 2026.
    at:
    - 572
    - 405
  au:
    name: AUSTRALIA
    text: Australia produced IREN, now a $9.7B supplier to Microsoft, and Firmus, which pulled its stock market listing in October 2026.
  eu:
    name: EUROPE
    text: 'Europe is led by Nscale and Nebius: Nscale signed $45B with Anthropic, and Nebius signed up to $27B with Meta in 2026.'
  na:
    name: NORTH AMERICA
    text: 'North America is the deepest cluster: CoreWeave, Lambda, Crusoe, Fireworks AI, Baseten, Modal and fal are all based in the US.'
sources:
- claim: Yotta 20,736 GPUs and $1B Nvidia DGX Cloud deal
  url: https://www.itnews.asia/news/yotta-to-build-us2-billion-ai-hub-in-india-with-nvidia-chips-623718
  date: '2026-02-18'
  quote: The four-year engagement, valued at over US$1 billion, builds on an existing relationship
- claim: Firmus IPO withdrawn
  url: https://www.abc.net.au/news/2026-10-09/firmus-float-gets-pulled-following-lacklustre-investor-demand/107246230
  date: '2026-10-09'
  quote: AI data centre company Firmus has withdrawn its application to list on the ASX
- claim: IREN Microsoft
  url: https://iren.gcs-web.com/news-releases/news-release-details/iren-secures-97bn-ai-cloud-contract-microsoft
  date: '2025-11-03'
  quote: over a five-year term, with a total contract value of approximately $9.7 billion
- claim: Nebius Meta
  url: https://nebius.com/newsroom/nebius-signs-new-ai-infrastructure-agreement-with-meta
  date: '2026-03-16'
  quote: The agreement has a contract value of up to approximately $27 billion.
comment: IREN was founded in Sydney (our base lists it in Australia). Yotta belongs to a larger Indian group.
```

### ed184
```yaml
status: ok
section: Top players
title: Any new disruptive startups emerging recently?
note: We selected younger companies with recent rounds or milestones that change how AI computing is sold, from AMD-only clouds to GPU marketplaces.
t:
  12: 2026 (JUL)
  13: Prime Intellect raised a $130M Series A led by Radical Ventures, with Nvidia, for its open AI training stack {1|Prime Intellect}
  14: 2026 (JUN)
  15: TensorWave raised $350M, co-led by AMD, for a cloud with 8,192 AMD GPUs online and no Nvidia chips {1|TensorWave}
  16: 2026 (JUN)
  17: Runpod raised $100M from Summit Partners after passing one million developers renting its GPUs {1|Runpod}
  18: 2025 (NOV)
  19: SF Compute raised $40M at a $300M valuation for a market where teams resell the GPU hours they do not use {1|WSJ}
  20: 2025 (SEP)
  21: Modal became a unicorn with an $87M Series B at $1.1B, renting GPUs by the second to run AI code in the cloud {1|Modal}
  22: 2025 (JUL)
  23: fal raised $125M at a $1.5B valuation to run image, video and audio AI models through one API {1|Reuters}
sources:
- claim: Prime Intellect Series A
  url: https://www.primeintellect.ai/blog/series-a
  date: '2026-07-08'
  quote: Prime Intellect closed a $130M Series A led by Radical Ventures, lifting its total funding above $150M.
- claim: TensorWave 8,192 MI325X online
  url: https://pulse2.com/tensorwave-raises-350-million-series-b-at-1-55-billion-valuation-to-expand-amd-powered-ai-infrastructure/
  date: '2026-06-10'
  quote: now operates one of North America's largest AMD-based AI training clusters, with 8,192 AMD Instinct MI325X GPUs online.
- claim: Runpod one million developers and $100M
  url: https://www.runpod.io/blog/one-million-developers
  date: '2026-06'
  quote: we've crossed more than one million developers building on the platform.
- claim: SF Compute $40M at $300M
  url: https://www.startupresearcher.com/news/sf-compute-raises-usd40-million-to-build-ai-compute-marketplace
  date: '2025-11-28'
  quote: The Series A round values the company at $300 million
- claim: Modal Series B
  url: https://modal.com/blog/announcing-our-series-b
  date: '2025-09-29'
  quote: Our post-money valuation is $1.1B. This brings our total money raised to $111M.
- claim: fal Series C
  url: https://www.itiger.com/hans/news/2555856218
  date: '2025-07-31'
  quote: fal raised a $125 million Series C round valuing the company at $1.5 billion, the company said Thursday.
```

### ed185
```yaml
status: ok
section: Top players
title: Which ones are disrupting the value chain?
t:
  11: POWER
  12: GPU SUPPLY
  13: CLUSTERS
  14: SOFTWARE
  15: CAPITAL
  16: Former bitcoin miners like IREN and Crusoe turned their power sites into AI clouds, skipping the long wait for a new grid link
  17: TensorWave runs a cloud on AMD chips alone, while Cerebras and Groq rent out their own chips, giving buyers options beyond Nvidia
  18: SF Compute lets teams book a cluster for a few days and resell the hours they do not use, instead of signing a contract for years
  19: Baseten pools GPUs from more than ten clouds behind one service, so apps never see which data center runs their model
  20: Nebius asks clients to pay part of the price up front, and over 90% of the contract value it signed in the third quarter came with a prepayment
sources:
- claim: Baseten pools GPUs from 10+ clouds
  url: https://www.nvidia.com/en-eu/case-studies/baseten-cloud-scaling-ai-inference/
  date: undated
  quote: Baseten brings together GPUs from more than 10 cloud providers across dozens of global regions
- claim: SF Compute resale
  url: https://www.eweek.com/news/sf-compute-ai-funding/
  date: '2025-11'
  quote: By enabling buyers to resell unused capacity in a flexible marketplace
- claim: Nebius prepayments
  url: https://www.sec.gov/Archives/edgar/data/1513845/000110465926126008/tm2629571d1_ex99-2.htm
  date: '2026-11-12'
  quote: More than 90% of contract value signed in the third quarter carried a prepayment
- claim: TensorWave AMD only
  url: https://www.magnetar.com/insights/tensorwave-raises-350-million-series-b-at-155b-valuation
  date: '2026-06-10'
  quote: TensorWave, the all-AMD AI cloud specializing in high-performance, memory-intensive workloads
```

### ed186
```yaml
status: ok
section: Top players
title: Which ones are working on moonshots?
note: A moonshot is a highly ambitious goal with major uncertainty, even for companies that already sell computing today.
t:
  10: "🌍\nPrime Intellect aims to build an open stack to train frontier AI models"
  8: "⚡\nCerebras aims to make AI answers far faster with chips as big as a wafer"
  7: "🔋\nNscale aims to grow its West Virginia campus past 8 GW, on its own power"
  9: "🔁\nSF Compute wants GPU hours to trade like a commodity, bought and resold"
  14: "🏭\nCrusoe aims to build AI factories where cheap energy already exists"
  12: "🎯\nTensorWave wants to prove a large AI cloud can run on AMD chips alone"
  11: "💻\nModal aims to let any developer run AI code on GPUs with no servers"
  13: "🧠\nFluidstack is building whole data centers for Anthropic, in a $50B plan"
sources:
- claim: Nscale 8 GW path
  url: https://aiweekly.co/alerts/nscale-files-nyse-ipo-behind-446b-anthropic-compute-deal
  date: '2026-09'
  quote: with what the company describes as a "clear expansion path to 8GW+" of capacity.
- claim: Prime Intellect open stack
  url: https://www.primeintellect.ai/blog/series-a
  date: '2026-07-08'
  quote: It describes an "open superintelligence stack" for training, deploying, and continuously improving models.
- claim: Crusoe energy-first
  url: https://www.crusoe.ai/about/company
  date: undated
  quote: Crusoe is founded with an energy-first approach
```

### ed188
```yaml
status: ok
section: Top players
title: Which neocloud startups passed $1B?
note: We use the valuation of each company's latest priced round, as announced by the company or reported by the press. Private values can change fast.
t:
  7: FIREWORKS AI
  17: MODAL
  6: Fireworks AI serves open AI models for apps, passed a $1B revenue run rate and raised $1.5B at an $18B valuation in July 2026
  9: Modal rents GPUs by the second to run AI code and raised $750M at a $16B valuation in October 2026
  12: BASETEN
  15: FAL
  11: Baseten runs the AI models of fast-growing apps and raised $1.5B at a $13B valuation in June 2026
  14: fal runs image, video and audio AI models through one API and raised $1.3B at a $16B valuation in November 2026
sources:
- claim: Fireworks about $18B
  url: https://fireworks.ai/news/fireworks-raises-1-5-billion-series-d
  date: '2026-07-16'
  quote: announced a $1.505 billion Series D round at a $17.5 billion valuation.
- claim: Modal about $16B
  url: https://www.axios.com/pro/enterprise-software-deals/2026/10/14/modal-accel-ai-infrastructure
  date: '2026-10-14'
  quote: raised a $750 million Series D at a $15.75 billion post-money valuation
- claim: Baseten $13B
  url: https://www.baseten.co/blog/announcing-our-series-f/
  date: '2026-06-22'
  quote: Baseten raised a $1.5B Series F and achieved a $13B valuation
- claim: fal $16B
  url: https://bloomberg.com/news/articles/2026-11-03/ai-inference-startup-fal-raises-capital-at-16-billion-valuation
  date: '2026-11-03'
  quote: has doubled its valuation to $16 billion in a new round of funding.
logos:
- name: Fireworks AI
  domain: fireworks.ai
- name: Modal
  domain: modal.com
- name: Baseten
  domain: baseten.co
- name: fal
  domain: fal.ai
```

### ed189
```yaml
status: ok
section: Top players
title: How long did it take them to pass $1B?
note: We count from the founding year in our database to the first round priced above $1B. This is a private-round timeline, not a stock market value.
t:
  19: '2019'
  8: '2026'
  20: Fireworks AI needed about 3 years (2022 - 2025)
  21: It took about 4 years for Modal (2021 - 2025)
  22: fal did it in 4 years (2021 - 2025)
  23: Baseten needed 6 years (2019 - 2025)
sources:
- claim: Fireworks Series B at $552M, then Series C at $4B
  url: https://news.bloomberglaw.com/private-equity/sequoia-nvidia-back-fireworks-ai-at-552-million-valuation
  date: '2024-07-11'
  quote: Startup Fireworks AI notched a valuation of $552 million in a funding round led by Sequoia Capital
- claim: Fireworks $4B in October 2025
  url: https://fireworks.ai/news/fireworks-ai-raises-250m-series-c
  date: '2025-10-28'
  quote: announced a $250 million Series C funding round at a $4 billion valuation.
- claim: Modal $1.1B in September 2025
  url: https://modal.com/blog/announcing-our-series-b
  date: '2025-09-29'
  quote: Our post-money valuation is $1.1B.
- claim: fal $1.5B in July 2025
  url: https://www.itiger.com/hans/news/2555856218
  date: '2025-07-31'
  quote: fal raised a $125 million Series C round valuing the company at $1.5 billion
- claim: Baseten passed $2B in September 2025
  url: https://fortune.com/2025/09/05/exclusive-baseten-ai-inference-unicorn-raises-150-million-at-2-15-billion-valuation/
  date: '2025-09-05'
  quote: The deal, which almost triples Baseten's valuation to $2.15 billion, was led by Bond
```

### ed190
```yaml
status: ok
section: Top players
title: 'How fast are neocloud

  startups growing?'
note: Each point shows the latest announced valuation against the years since founding. Modal and fal are both five years old and worth about $16B
t:
  12: $30B
  41: 'Why inference wins. {1|Four inference clouds passed $13B within eight years. Fireworks AI got there in four, as apps paid for every token.}'
  37: "FIREWORKS AI\n$18B"
  38: "FAL\n$16B"
  10: $15B
  36: "MODAL\n$16B"
  39: "BASETEN\n$13B"
  8: $0
  13: Founding
  14: Year 2
  15: Year 4
  16: Year 6
  17: Year 8
  18: Year 10
  19: Year 12
  20: Year 14
  21: Year 16
  22: YEARS SINCE FOUNDING
sources:
- claim: Fireworks about $18B (founded 2022)
  url: https://fireworks.ai/news/fireworks-raises-1-5-billion-series-d
  date: '2026-07-16'
  quote: announced a $1.505 billion Series D round at a $17.5 billion valuation.
- claim: Modal about $16B (founded 2021)
  url: https://www.axios.com/pro/enterprise-software-deals/2026/10/14/modal-accel-ai-infrastructure
  date: '2026-10-14'
  quote: raised a $750 million Series D at a $15.75 billion post-money valuation
- claim: fal $16B (founded 2021)
  url: https://bloomberg.com/news/articles/2026-11-03/ai-inference-startup-fal-raises-capital-at-16-billion-valuation
  date: '2026-11-03'
  quote: has doubled its valuation to $16 billion in a new round of funding.
- claim: Baseten $13B (founded 2019)
  url: https://www.baseten.co/blog/announcing-our-series-f/
  date: '2026-06-22'
  quote: Baseten raised a $1.5B Series F and achieved a $13B valuation
```
