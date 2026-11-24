# MedTech, chapter 01 Market definition (evergreen, written by Claude, 23 Nov 2026)

### ed006
```yaml
status: ok
title: What is the MedTech market, in simple terms?
text: MedTech is the market for medical devices and clinical software that find, track or treat a disease, from heart valves and surgery robots to glucose sensors
note: We use a conversational definition here because it makes the boundary with drugs, wellness gadgets and hospital admin software easier to understand.
icon_tl: 🩺
```

### ed007p
```yaml
status: no_data
reason: taken from the live product page
```

### ed008
```yaml
status: ok
title: What markets are often confused with MedTech?
t:
  12: DIGITAL HEALTH
  13: MEDTECH
  14: PHARMA
  7: MedTech differs from both because its products are devices or clinical software that find, track or treat a disease directly
  10: Digital health covers apps, video visits and admin software that help deliver care but do not diagnose or treat alone
  11: Pharma sells drugs that act on the body through chemistry, while MedTech acts through devices, energy or measurement
```

### ed009
```yaml
status: ok
title: What markets does MedTech sit between?
t:
  8: "HOSPITAL\nCARE"
  9: "PRECISION\nENGINEERING"
  10: "DATA\nSCIENCE"
  13: 'MedTech sits between three markets: it serves doctors and patients like hospitals do, it builds tiny, precise hardware like engineering firms, and it relies more and more on data science to read signals and scans.'
```

### ed010
```yaml
status: ok
title: And what if we break it down in smaller markets?
t:
  21: MEDTECH
  5: "HEART\nDEVICES"
  8: "JOINTS AND\nSPINE"
  11: "BRAIN AND\nNERVES"
  14: "DIABETES\nCARE"
  17: "CANCER\nCARE"
  7: It is in the market when valves, stents or catheters fix the heart and blood vessels
  10: It is in the market when implants or robots repair a hip, a knee or the spine
  13: It is in the market when implants or pulses treat pain, stroke or paralysis
  16: It is in the market when sensors and pumps track and dose blood sugar
  19: It is in the market when scanners, tests or energy find and destroy tumors
```

### ed011
```yaml
status: ok
title: What are some common acronyms I should know?
note: We prioritized acronyms that appear often in company, regulator and investor materials rather than very technical engineering terms.
t:
  6: PMA
  15: MDR
  23: CGM
  8: "Premarket\nApproval"
  16: "Medical Device\nRegulation"
  24: "Continuous Glucose\nMonitor"
  4: It is the strictest FDA review, with clinical trials, needed for most implants
  13: It is the EU law, applied since 2021, that made approving devices in Europe slower
  21: It is a small sensor worn on the skin that reads blood sugar every few minutes
  11: PFA
  19: BCI
  27: IVD
  12: "Pulsed Field\nAblation"
  20: "Brain-Computer\nInterface"
  28: "In Vitro\nDiagnostic"
  9: It is a way to treat an irregular heartbeat with short electric pulses instead of heat
  17: It is an implant that reads brain signals so a paralyzed person can use a computer
  25: It is a test run on blood, urine or tissue outside the body, in a lab or at the bedside
```

### ed012
```yaml
status: no_data
reason: MedTech products and prices are too varied to group into a reliable product map without fresh research
```

### ed013
```yaml
status: no_data
reason: device prices are mostly negotiated with hospitals and rarely public, left for the research chapters
```

### ed014
```yaml
status: ok
title: When and where is value created in the market?
items:
- e: 🎯
  t: When a device treats through a small cut or a vein instead of open surgery
- e: ⏱️
  t: When a test gives an answer in minutes at the bedside instead of days in a lab
- e: 🏠
  t: When patients are followed and treated at home instead of in a hospital bed
- e: 📊
  t: When a large trial proves that patients live longer or need less care afterwards
- e: 💳
  t: When insurers agree to pay for a new device with its own payment code
- e: 🔁
  t: When each use sells a sensor, an instrument or a refill, not just one machine
- e: 🧠
  t: When software reads scans and signals faster than doctors can on their own
- e: 🤝
  t: When a large group buys a startup to sell its device through its sales force
```

### ed015
```yaml
status: ok
title: What are some common myths about MedTech?
page: 1/2
note: We focused on myths that come back often in investor, doctor and press debates. The counters describe what companies and regulators have shown so far in filings and official lists.
t:
  9: Robot surgery belongs to Intuitive alone
  7: Medtronic's Hugo won FDA clearance in December 2025 and J&J's Ottava in July 2026, the first big US rivals to da Vinci in over 20 years
  12: Medical AI is still only a research topic
  10: The FDA list counted 1,614 AI-enabled devices in September 2026, three in four for radiology, though none of them used generative AI yet
  15: Surgery robots are a niche for big hospitals
  13: About 3.15 million operations were done with da Vinci robots in 2025, up 18% in a year, on more than 11,100 systems around the world
  0: Big MedTech buyouts have dried up for good
  16: Boston Scientific agreed to pay about $15B for Penumbra in January 2026, and Abbott closed its $21B purchase of Exact Sciences in March
sources:
- claim: Hugo FDA clearance for urologic procedures, December 2025
  url: https://news.medtronic.com/2025-12-03-Medtronic-announces-FDA-clearance-of-Hugo-TM-robotic-assisted-surgery-system-for-urologic-surgical-procedures
  date: '2025-12-03'
  quote: today announced the U.S. Food and Drug Administration (FDA) has cleared the Hugo robotic-assisted surgery (RAS) system for use in urologic surgical procedures
- claim: Ottava De Novo authorization, July 2026
  url: https://www.jnj.com/media-center/press-releases/johnson-johnson-receives-fda-market-authorization-in-the-u-s-for-its-ottava-robotic-surgical-system
  date: '2026-07-22'
  quote: the U.S. Food and Drug Administration (FDA) has granted De Novo authorization for the OTTAVA Robotic Surgical System
- claim: 1,614 AI-enabled devices, no generative AI device as of September 2026
  url: https://medicalfuturist.com/the-current-state-of-fda-approved-ai-based-medical-devices
  date: '2026-09-15'
  quote: As of September, 2026, no device has been authorized that uses generative AI or is powered by large language models.
- claim: 3,153,000 da Vinci procedures in 2025, installed base 11,106
  url: https://investor.intuitivesurgical.com/news-releases/news-release-details/intuitive-announces-preliminary-fourth-quarter-and-full-year-5
  date: '2026-01-14'
  quote: approximately 3,153,000 surgical procedures were performed with da Vinci surgical systems, an increase of approximately 18%
- claim: Boston Scientific to acquire Penumbra for about 14.5 billion dollars
  url: https://news.bostonscientific.com/2026-01-15-Boston-Scientific-announces-agreement-to-acquire-Penumbra,-Inc
  date: '2026-01-15'
  quote: transaction that values Penumbra at $374 per share, reflecting an enterprise value of approximately $14.5 billion
- claim: Abbott closed its $21B Exact Sciences deal in March 2026
  url: https://hlth.com/insights/news/abbott-closes-21b-deal-for-exact-sciences-2026-03-24
  date: '2026-03-24'
  quote: Abbott Closes $21B Deal for Exact Sciences
```

### ed016
```yaml
status: ok
title: What are some common myths about MedTech?
page: 2/2
note: We focused on myths that come back often in investor, doctor and press debates. The counters describe what companies and regulators have shown so far in filings and official lists.
t:
  9: Brain implants are still science fiction
  7: Neuralink had implanted 21 people with paralysis by January 2026, who use it to move a cursor and type on a screen with their thoughts
  12: An FDA clearance means insurers will pay
  10: Clearance and payment are separate steps, and Medicare's fast lane for new devices, created in 2024, takes only about five devices a year
  15: MedTech grows as fast as software firms
  13: Forecasts put the market's growth near 6% a year, because each new device needs trials, approval and payment before it sells widely
  0: A smartwatch cannot be a medical device
  16: Apple won FDA clearance for sleep apnea alerts in 2024 and blood pressure alerts in 2025, while it still sells the watch as a gadget
sources:
- claim: Neuralink implanted 21 participants by January 2026
  url: https://www.roic.ai/news/neuralink-expands-brain-computer-interface-trial-to-21-participants-worldwide-01-28-2026
  date: '2026-01-28'
  quote: Neuralink expands brain computer interface trial to 21 participants worldwide
- claim: Medicare TCET pathway finalized in August 2024, up to five devices a year
  url: https://www.cms.gov/newsroom/fact-sheets/final-notice-transitional-coverage-emerging-technologies-cms-3421-fn
  date: '2024-08-07'
  quote: CMS anticipates accepting up to five TCET candidates per year
```

### ed017
```yaml
status: ok
title: How mature is MedTech as a market?
score: 75
text: The market is mature because devices are used in every hospital, the largest groups sell tens of billions of dollars a year and the FDA paths are well known. The score is not higher because brain implants, medical AI and care at home are still young, and insurers are slow to pay for them.
note:
- We rate market maturity with an internal score of products in use, sales, regulatory clarity and payment by insurers.
- We set 75/100 because core devices are proven and paid, while the newest device areas are still early and small.
```

### ed018
```yaml
status: ok
title: How can we categorize companies of the MedTech market?
page: 1/3
note: We use the six solution groups of our company database, from implants and surgery robots to sensors worn at home and software that reads scans.
t:
  25: Here, we categorize by type of solution
categories:
- label: "IMPLANTABLE\nDEVICES"
  description: Implants that fix the heart, joints, spine or brain from inside
  e: 🦴
- label: "THERAPEUTIC\nDEVICES"
  description: Machines that treat disease with pulses, energy, fluids or doses
  e: ⚡
- label: "DIAGNOSTIC\nDEVICES"
  description: Tests, scanners and probes that find a disease early and fast
  e: 🔬
- label: "SURGICAL\nSYSTEMS"
  description: Robots and tools that help surgeons operate through small cuts
  e: 🤖
- label: "MEDICAL\nSOFTWARE"
  description: AI and software that read scans and lab tests to guide doctors
  e: 💻
- label: "PATIENT\nMONITORING"
  description: Sensors worn at home that track the heart, sugar or breathing
  e: 📱
```

### ed019
```yaml
status: ok
title: How can we categorize companies of the MedTech market?
page: 2/3
note: We also categorize by buyer because a hospital, a surgeon, a lab and a patient at home need very different prices, proof and support.
t:
  25: Here, we categorize by the type of buyer
categories:
- label: "HOSPITALS AND\nHEALTH SYSTEMS"
  description: Selling robots, scanners and monitors to hospital buying teams
  e: 🏥
- label: "SURGEONS AND\nSPECIALISTS"
  description: Winning the doctors who choose which implant or tool they use
  e: 🩺
- label: "LABS AND\nCLINICS"
  description: Placing test machines in labs and clinics that then pay per test
  e: 🧪
- label: "PATIENTS\nAT HOME"
  description: Prescribing sensors and pumps that patients use in daily life
  e: 🏠
- label: "HEALTH\nINSURERS"
  description: Proving to insurers that a device cuts later costs, to get paid
  e: 💳
- label: "LARGE MEDTECH\nGROUPS"
  description: Selling the device or the company to a giant with a sales force
  e: 🤝
```

### ed020
```yaml
status: ok
title: How can we categorize companies of the MedTech market?
page: 3/3
note: A third useful lens is the business model, because selling a machine once and selling each use or refill bring in money very differently.
t:
  25: Here, we categorize by business model
categories:
- label: "MACHINE\nSALES"
  description: Selling scanners or robots once, often with a service contract
  e: 🏭
- label: "PAID PER\nPROCEDURE"
  description: Selling an implant or a single-use kit each time a patient is treated
  e: 🩺
- label: "RAZOR AND\nBLADES"
  description: Placing a machine, then selling the instruments used each time
  e: 🔁
- label: "SENSOR\nREFILLS"
  description: Selling sensors that patients replace every week or two weeks
  e: 📦
- label: "SOFTWARE\nLICENSES"
  description: Charging hospitals a yearly fee or a fee per scan for software
  e: 💻
- label: "REMOTE\nMONITORING"
  description: Billing insurers each month for following patients from home
  e: 📈
```

### ed021
```yaml
status: ok
title: What do top companies do in this market?
note: Other companies could also make the top eight. We chose startups with the most funding, the furthest clinical progress or the most use to show the range of the market.
t:
  8: NEURALINK
  16: MIRUS
  7: They build a wireless brain implant that 21 paralyzed people used by early 2026 to type
  15: They make a valve put in through an artery and spine implants from a strong rhenium alloy
  10: CMR SURGICAL
  18: AIDOC
  9: They make Versius, a modular robot for keyhole surgery, authorized by the FDA in 2024
  17: They sell AI that reads CT scans and alerts doctors to bleeds and clots in minutes
  12: KARDIUM
  20: SALUDA MEDICAL
  11: They make Globe, which maps and treats atrial fibrillation with electric pulses
  19: They make a spinal cord stimulator for pain that reads nerve responses and adjusts itself
  14: NEKO HEALTH
  22: SYNCHRON
  13: They run clinics that check skin, heart and blood with a full-body scan
  21: They place a brain implant through a neck vein, with no open-brain surgery
```

### ed022
```yaml
status: ok
title: What is rare and that people happily pay for in this market?
note: We looked at deal prices, funding rounds, trial results and payment decisions to find the capabilities that look truly scarce and valuable in MedTech.
t:
  6: "📊\nHard proof, because a large trial that shows longer lives opens every door"
  7: "💳\nA payment code, because hospitals rarely buy what insurers will not pay for"
  8: "🎯\nLess invasive care, because a fix through a vein beats opening the chest every time"
  9: "🏥\nSurgeon trust, because doctors stick with the tools they learned and trust"
  10: "🔁\nRecurring revenue, because sensors and instruments sell again with every patient"
  11: "🛡️\nA clean safety record, because one recall can wipe out years of sales"
  12: "🏭\nScale manufacturing, because tiny implants must be made perfectly by the million"
  13: "🧠\nRare talent, because few teams mix engineering, medicine and FDA know-how"
```

### ed023
```yaml
status: ok
title: Which MedTech truths have flipped?
note: These are market shifts we see in recent company results, FDA decisions and deals. They are not formal industry rules, but they come back across the evidence.
t:
  6: Replacing a heart valve used to mean open-heart surgery
  8: Now most new valves go in through an artery in the leg, with no open chest
  10: Intuitive used to be alone in US soft-tissue surgery robots
  12: Now Medtronic's Hugo and J&J's Ottava robots compete with it
  14: Glucose sensors used to need a doctor's prescription
  16: Now Dexcom Stelo and Abbott Lingo are sold over the counter in the US
  18: Brain implants used to be only for research labs
  20: Now Neuralink, Synchron and Precision implant patients in trials
  22: Atrial fibrillation used to be treated mostly with heat or cold
  24: Now pulsed field ablation with short electric pulses grows fastest
  26: Medical AI used to be a research topic for universities
  28: Now the FDA lists over 1,600 AI-enabled devices, most of them for scans
```

### ed024
```yaml
status: ok
title: What has changed (very) recently?
page: 1/2
items:
- d: SINCE 2024
  t: The FDA approved Boston Scientific's Farapulse in January, and pulsed field ablation quickly became the fastest-growing way to treat atrial fibrillation in the US.
- d: SINCE 2024
  t: Dexcom's Stelo became the first glucose sensor cleared by the FDA for sale without a prescription, followed by Abbott's Lingo a few months later in the same year.
- d: SINCE 2024
  t: Neuralink placed its first brain implant in a paralyzed patient in January, who then used it to move a cursor and play chess with his thoughts.
- d: SINCE 2024
  t: Johnson & Johnson closed its $13B purchase of Shockwave Medical, whose catheters break up hard calcium inside blocked heart and leg arteries with sound waves.
- d: SINCE 2024
  t: Medicare created TCET, a faster path to pay for new breakthrough devices, so patients can get them while more evidence is collected after the FDA decision.
- d: SINCE 2025
  t: Stryker closed its $4.9B purchase of Inari Medical, which removes blood clots from veins and lungs, one of the largest buyouts of a young device maker.
note:
- We kept the milestones that most changed what devices can do, who sells them and how they get paid
- There is no official timeline, and another analyst could pick a few different milestones here
```

### ed025
```yaml
status: ok
title: What has changed (very) recently?
page: 2/2
items:
- d: SINCE 2025
  t: Medtronic won FDA clearance for its Hugo surgical robot for urology in December, the first big US rival in soft-tissue surgery for Intuitive's da Vinci.
- d: SINCE 2026
  t: Boston Scientific agreed to buy Penumbra for about $15B in January, its largest deal in 20 years, to enter the fast-growing market for removing blood clots.
- d: SINCE 2026
  t: Abbott closed its purchase of Exact Sciences, the maker of the Cologuard cancer test, for about $21B in March, its largest deal in nearly a decade.
- d: SINCE 2026
  t: Neuralink reached 21 implanted patients in January and opened trials in the UK, Canada and the UAE, as brain implants moved from single cases to small series.
- d: SINCE 2026
  t: Johnson & Johnson won FDA authorization for its Ottava robot in July, the first surgery robot built into the operating table, for ten stomach and bowel operations.
- d: SINCE 2026
  t: The FDA list of AI-enabled devices passed 1,600 in September, with about 30 new ones a month, but none of them uses generative AI to diagnose patients yet.
note:
- We kept the milestones that most changed what devices can do, who sells them and how they get paid
- There is no official timeline, and another analyst could pick a few different milestones here
```
