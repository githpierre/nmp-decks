# deepfake detection, chapter 04 Pain points (evergreen, written by Claude, 27 Nov 2026)

### ed054
```yaml
status: ok
title: What are the pain points of yesterday vs. today?
note: 'We grouped the market into phases: early face swaps, the first voice scams, cheap generative AI, and today''s fraud at scale. We used regulator alerts, fraud reports and studies.'
t:
  6: '2017 - 2019

    Face swap videos spread online, but they were crude and rare, and detection was mostly a research topic funded by DARPA'
  7: '2019 - 2022

    A cloned CEO voice tricked a UK energy firm into wiring €220,000, but most companies still saw deepfakes as a celebrity issue'
  8: '2023 - 2024

    Cheap AI tools made fake faces and voices easy, and a fake video call cost Arup about $25.6M, while few firms had any defense'
  9: 'TODAY

    Deepfake attacks hit banks, call centers and hiring every day, yet only a small share of firms use a detection tool built for it'
  10: '?

    Real-time fakes may become impossible to spot by eye, so checks must run inside every call, selfie and upload, at very low cost'
```

### ed055
```yaml
status: ok
title: Which old problems are now behind us?
note: We treat these as problems that new tools have removed for many buyers. They do not mean that every deepfake is now caught, or that detectors work in every condition.
t:
  5: Checking a suspicious video meant sending it to a lab and waiting days
  7: Forensic tools from Sensity, Reality Defender and GetReal now score a file in minutes, with a report
  8: Call centers had no way to tell a cloned voice from a real customer
  10: Pindrop and other voice tools now flag synthetic voices during the call, inside the systems agents use
  11: Selfie checks could be fooled by a photo, a mask or a replayed video
  13: Liveness checks from Incode, iProov and others now spot many fake faces in under a second at sign-up
  14: Video meetings had no check that each person on screen was real
  16: GetReal, Reality Defender and Resemble AI now run checks inside Zoom, Teams and Webex meetings
  17: Platforms had no shared way to show where a photo or a video came from
  19: Content Credentials from the C2PA now attach a signed record of origin to media from many cameras and apps
  20: Victims of fake intimate images had no US right to quick removal
  22: The TAKE IT DOWN Act now makes US platforms remove such images within 48 hours of a valid request
```

### ed056
```yaml
status: ok
title: What problems do all players face?
page: 1/2
note: We kept the problems that come back in detector tests, fraud reports and buyer surveys. We skipped generic startup issues and focused on spotting AI-made media.
t:
  25: 'New AI models

    beat old detectors'
  23: 'You need

    fresh data'
  8: 'Lab scores fall

    in real use'
  6: 'You need real-world

    tests'
  29: 'False alarms

    block real users'
  27: 'You need low

    error rates'
  12: 'Low quality

    hides clues'
  10: 'You need robust

    models'
  33: 'Live checks must

    be very fast'
  31: 'You need low

    latency'
  16: 'Watermarks only

    cover some tools'
  14: 'You need checks

    without marks'
  37: 'Verdicts must

    hold up in court'
  35: 'You need clear

    reasons'
  20: 'Attackers test

    every defense'
  18: 'You need constant

    updates'
```

### ed057
```yaml
status: ok
title: What problems do all players face?
page: 2/2
note: We separated the problems of detecting fakes from those of selling detection. The second set matters once a tool works, because budgets, platforms, rules and rivals still decide who wins.
t:
  25: 'Few firms buy

    a dedicated tool'
  23: 'You need a

    clear budget'
  8: 'Big platforms add

    detection for free'
  6: 'You need a

    clear edge'
  29: 'Buyers want it

    inside their tools'
  27: 'You need many

    plug-ins'
  12: 'Rules differ by

    country and state'
  10: 'You need legal

    clarity'
  33: 'Voice data raises

    privacy claims'
  31: 'You need clear

    consent'
  16: 'Losses are hard

    to prove upfront'
  14: 'You need ROI

    proof'
  37: 'Hype hurts trust

    in accuracy claims'
  35: 'You need open

    test results'
  20: 'Big security firms

    buy the leaders'
  18: 'You need partner

    channels'
```

### ed059
```yaml
status: ok
title: Which problems are startups going after?
t:
  16: 'Voice

    clones'
  11: 'Fake

    selfies'
  14: 'CEO

    fraud'
  21: 'Pain points change sharply by buyer.


    Broad statements quickly mislead.

    So we split banks and fintechs, contact centers, agencies, newsrooms and platforms and security teams before scoring.'
  13: 'Fake

    hires'
  12: 'False

    news'
  15: 'Slow

    checks'
  18: 'Fake

    nudes'
  19: 'False

    alarms'
```

### ed060
```yaml
status: ok
title: How will we proceed?
note: We break the market down before scoring because the same tool creates very different value and risk for a bank, a call center or a newsroom.
t:
  9: '😣

    PAIN POINTS


    We list each group''s main pains and score them to rank them.'
  6: '🎯

    GOAL


    Find the pains that matter most in deepfake detection, and who feels them.'
  7: '🏷️

    CATEGORIES


    We split the market by buyer, because who pays and what they need differ.'
  8: '👥

    SEGMENTS


    For each buyer, we list the people who decide, pay, use and check tools.'
```

### ed061
```yaml
status: ok
title: Which categories will we use?
note: We split the market into five types of buyer. They differ enough in who pays, what proof they need and how they buy to score their pain points separately.
t:
  7: 'BANKS AND

    FINTECHS'
  9: 'CONTACT

    CENTERS'
  11: 'GOVERNMENT

    AGENCIES'
  13: 'NEWSROOMS AND

    PLATFORMS'
  15: 'SECURITY

    TEAMS'
  6: Banks, payment apps and lenders that check new clients, logins and large transfers
  8: Call centers of banks, insurers and retailers that verify callers before account changes
  10: Defense, police, election and public agencies that check media, evidence and identities
  12: Media groups and social apps that check what people upload and share every day
  14: Company security teams that protect calls, meetings, payments and hiring from fakes
  17: ''
  16: ''
holes_ok: true
```

### ed062-s1
```yaml
status: ok
t:
  6: PAIN POINTS
  3: BANKS AND FINTECHS
  5: 'Banks, payment apps and lenders that check

    new clients, logins and large transfers'
```

### ed063-s1
```yaml
status: ok
title: Who needs deepfake detection?
note: We focus on the five groups inside these buyers that choose, pay for, use and check detection tools.
t:
  27: BANKS AND FINTECHS
  5: 'FRAUD

    TEAMS'
  20: 🛡️
  7: They need to stop fake faces and voices before money moves, without blocking real clients at each step
  8: 'ONBOARDING

    TEAMS'
  21: 💳
  10: They need selfie and ID checks that catch deepfakes in seconds, so new clients do not give up at sign-up
  11: 'COMPLIANCE

    OFFICERS'
  22: 📋
  13: They need records that show regulators how each check worked, and reports of fraud filed on time
  14: 'PAYMENT

    TEAMS'
  23: 💰
  16: They need to confirm that a request for a large transfer really comes from the client or the CFO
  17: 'RISK

    LEADERS'
  24: 📊
  19: They need proof that a tool cuts fraud losses by more than it costs, before it gets a yearly budget
```

### ed064-s1
```yaml
status: ok
title: What are these customers' strongest pain points?
note: We prioritized problems that recur in fraud reports, regulator alerts, detector tests and company releases on deepfakes.
t:
  13: BANKS AND FINTECHS
  14: They see deepfake attempts rise at account sign-up
  15: They lose new clients when checks feel too slow
  16: They face fake selfies that pass basic checks
  17: They see fraud losses rise with each new AI tool
  18: They must report deepfake fraud to regulators
  19: They find it hard to prove that a tool pays back
  20: They struggle to keep up with new attack methods
```

### ed065-s1
```yaml
status: ok
title: Which pains deserve attention first?
subtitle: Banks and fintechs
icons:
- 🛡️
- 💳
- 📋
- 💰
- 📊
rows:
- pain: Deepfake attempts at account sign-up keep rising each year
  s:
  - 3
  - 3
  - 2
  - 1
  - 3
  p: CRITICAL
- pain: Clients give up when identity checks feel too slow
  s:
  - 1
  - 3
  - 1
  - 1
  - 2
  p: MAJOR
- pain: Fake selfies get past basic liveness checks today
  s:
  - 3
  - 3
  - 2
  - 1
  - 2
  p: CRITICAL
- pain: Fraud losses rise with each new AI generation tool
  s:
  - 3
  - 1
  - 2
  - 3
  - 3
  p: CRITICAL
- pain: Deepfake fraud must be reported to regulators
  s:
  - 2
  - 1
  - 3
  - 1
  - 2
  p: HIGH
- pain: It is hard to prove a detection tool pays back
  s:
  - 2
  - 1
  - 1
  - 1
  - 3
  p: HIGH
- pain: New attack methods appear faster than updates
  s:
  - 3
  - 2
  - 1
  - 2
  - 2
  p: MAJOR
note:
- Every stakeholder is different, and this table is a simplified view based on reports and studies
- It gives a starting point, not a checklist, so priorities should be checked with real buyers
```

### ed062-s2
```yaml
status: ok
t:
  6: PAIN POINTS
  3: CONTACT CENTERS
  5: 'Call centers of banks, insurers and retailers that

    verify callers before account changes'
```

### ed063-s2
```yaml
status: ok
title: Who needs deepfake detection?
note: We focus on the five groups inside these buyers that choose, pay for, use and check detection tools.
t:
  27: CONTACT CENTERS
  5: 'CALL CENTER

    AGENTS'
  20: 📞
  7: They need a clear alert when a caller's voice is synthetic, so they do not change an account for a fraudster
  8: 'CENTER

    MANAGERS'
  21: 🏢
  10: They need checks that do not slow each call, since each extra second costs money across millions of calls
  11: 'FRAUD

    ANALYSTS'
  22: 🔍
  13: They need to see which calls were flagged and why, to find fraud rings that call again and again
  14: 'IT

    TEAMS'
  23: 🔌
  16: They need tools that plug into their phone systems and call platforms without a long and costly project
  17: 'PRIVACY

    TEAMS'
  24: 🔒
  19: They need consent and data rules for recorded voices, since voice analysis has led to lawsuits
```

### ed064-s2
```yaml
status: ok
title: What are these customers' strongest pain points?
note: We prioritized problems that recur in fraud reports, regulator alerts, detector tests and company releases on deepfakes.
t:
  13: CONTACT CENTERS
  14: They hear cloned voices that sound like real clients
  15: They cannot slow down millions of calls with checks
  16: They miss fraud rings that call again and again
  17: They face lawsuits over recording and voice data
  18: They find it hard to connect old phone systems
  19: They see agents fooled by calm and urgent fakes
  20: They lack proof of losses avoided each year
```

### ed065-s2
```yaml
status: ok
title: Which pains deserve attention first?
subtitle: Contact centers
icons:
- 📞
- 🏢
- 🔍
- 🔌
- 🔒
rows:
- pain: Cloned voices sound just like real clients on calls
  s:
  - 3
  - 2
  - 3
  - 1
  - 1
  p: CRITICAL
- pain: Checks cannot slow down millions of calls a year
  s:
  - 2
  - 3
  - 1
  - 3
  - 1
  p: MAJOR
- pain: Fraud rings call again and again with new voices
  s:
  - 2
  - 2
  - 3
  - 1
  - 1
  p: MAJOR
- pain: Recording and voice analysis can lead to lawsuits
  s:
  - 1
  - 2
  - 1
  - 2
  - 3
  p: HIGH
- pain: Old phone systems are hard to connect to new tools
  s:
  - 1
  - 2
  - 1
  - 3
  - 1
  p: HIGH
- pain: Calm or urgent fake callers fool trained agents
  s:
  - 3
  - 2
  - 2
  - 1
  - 1
  p: CRITICAL
- pain: Losses avoided are hard to prove to the board each year
  s:
  - 1
  - 3
  - 2
  - 1
  - 1
  p: HIGH
note:
- Every stakeholder is different, and this table is a simplified view based on reports and studies
- It gives a starting point, not a checklist, so priorities should be checked with real buyers
```

### ed062-s3
```yaml
status: ok
t:
  6: PAIN POINTS
  3: GOVERNMENT AGENCIES
  5: 'Defense, police, election and public agencies that

    check media, evidence and identities'
```

### ed063-s3
```yaml
status: ok
title: Who needs deepfake detection?
note: We focus on the five groups inside these buyers that choose, pay for, use and check detection tools.
t:
  27: GOVERNMENT AGENCIES
  5: 'DEFENSE

    ANALYSTS'
  20: 🛰️
  7: They need to check fake images and videos fast in a crisis, when a false clip can shape public reactions
  8: 'POLICE

    DETECTIVES'
  21: 🔍
  10: They need reports that show how a file was faked, written so that a court can accept the evidence
  11: 'ELECTION

    OFFICIALS'
  22: 🏛️
  13: They need to spot fake videos of candidates before a vote and to warn the public in a clear way
  14: 'PROCUREMENT

    OFFICERS'
  23: 📋
  16: They need approved vendors with security clearances, sold through contracts their agency can use
  17: 'CHILD SAFETY

    UNITS'
  24: 🛡️
  19: They need to sort real abuse images from AI-made ones, since reports of AI images are rising fast
```

### ed064-s3
```yaml
status: ok
title: What are these customers' strongest pain points?
note: We prioritized problems that recur in fraud reports, regulator alerts, detector tests and company releases on deepfakes.
t:
  13: GOVERNMENT AGENCIES
  14: They must judge viral fakes fast during a crisis
  15: They need evidence that a judge and court accept
  16: They face fake videos of candidates before votes
  17: They buy slowly through long public contracts
  18: They see AI images flood child safety reports
  19: They need vendors with a federal security approval
  20: They struggle to train their staff on new fakes
```

### ed065-s3
```yaml
status: ok
title: Which pains deserve attention first?
subtitle: Government agencies
icons:
- 🛰️
- 🔍
- 🏛️
- 📋
- 🛡️
rows:
- pain: Viral fakes must be judged fast during a crisis
  s:
  - 3
  - 1
  - 3
  - 1
  - 2
  p: CRITICAL
- pain: Evidence must be accepted by a court or a tribunal
  s:
  - 2
  - 3
  - 1
  - 1
  - 3
  p: MAJOR
- pain: Fake videos of candidates appear before votes
  s:
  - 2
  - 1
  - 3
  - 1
  - 1
  p: CRITICAL
- pain: Long contracts slow the purchase of new tools
  s:
  - 1
  - 1
  - 1
  - 3
  - 1
  p: HIGH
- pain: AI-made images flood child safety reports each year
  s:
  - 1
  - 3
  - 1
  - 1
  - 3
  p: CRITICAL
- pain: Vendors need security approval to work with agencies
  s:
  - 2
  - 1
  - 1
  - 3
  - 2
  p: HIGH
- pain: Staff struggle to keep up with new kinds of fakes
  s:
  - 2
  - 2
  - 2
  - 1
  - 2
  p: HIGH
note:
- Every stakeholder is different, and this table is a simplified view based on reports and studies
- It gives a starting point, not a checklist, so priorities should be checked with real buyers
```

### ed062-s4
```yaml
status: ok
t:
  6: PAIN POINTS
  3: NEWSROOMS AND PLATFORMS
  5: 'Media groups and social apps that check

    what people upload and share every day'
```

### ed063-s4
```yaml
status: ok
title: Who needs deepfake detection?
note: We focus on the five groups inside these buyers that choose, pay for, use and check detection tools.
t:
  27: NEWSROOMS AND PLATFORMS
  5: 'FACT

    CHECKERS'
  20: 📰
  7: They need to prove a viral video is fake within hours, before it spreads further than any correction
  8: 'TRUST AND

    SAFETY TEAMS'
  21: 🛡️
  10: They need to scan millions of uploads a day for fake media, at a cost that fits their budget
  11: EDITORS
  22: ✍️
  13: They need to know a photo or a clip is real before they publish it, since one mistake hurts trust
  14: 'LEGAL

    TEAMS'
  23: ⚖️
  16: They need to meet takedown rules, like the 48-hour limit for fake intimate images in the US
  17: 'PRODUCT

    TEAMS'
  24: 📱
  19: They need to label AI media and show where content came from, without slowing down users' posts
```

### ed064-s4
```yaml
status: ok
title: What are these customers' strongest pain points?
note: We prioritized problems that recur in fraud reports, regulator alerts, detector tests and company releases on deepfakes.
t:
  13: NEWSROOMS AND PLATFORMS
  14: They have only hours to stop a fake from spreading
  15: They scan many millions of new uploads every day
  16: They face strict legal limits on takedown times
  17: They see watermarks missing on most AI content
  18: They risk publishing a fake clip by mistake
  19: They pay a lot for each item that gets checked
  20: They face false alarms on real photos and clips
```

### ed065-s4
```yaml
status: ok
title: Which pains deserve attention first?
subtitle: Newsrooms and platforms
icons:
- 📰
- 🛡️
- ✍️
- ⚖️
- 📱
rows:
- pain: A fake must be stopped within hours, before it spreads
  s:
  - 3
  - 3
  - 3
  - 2
  - 2
  p: CRITICAL
- pain: Millions of uploads must be scanned every day
  s:
  - 1
  - 3
  - 1
  - 1
  - 3
  p: MAJOR
- pain: Laws set short limits on takedown times for platforms
  s:
  - 1
  - 3
  - 1
  - 3
  - 2
  p: MAJOR
- pain: Most AI content carries no watermark to read
  s:
  - 3
  - 3
  - 2
  - 1
  - 3
  p: HIGH
- pain: A fake can be published by mistake and hurt trust
  s:
  - 3
  - 1
  - 3
  - 2
  - 1
  p: CRITICAL
- pain: Each item checked adds to a large yearly bill
  s:
  - 1
  - 3
  - 1
  - 1
  - 2
  p: HIGH
- pain: False alarms flag real photos and real clips
  s:
  - 3
  - 2
  - 3
  - 1
  - 2
  p: MAJOR
note:
- Every stakeholder is different, and this table is a simplified view based on reports and studies
- It gives a starting point, not a checklist, so priorities should be checked with real buyers
```

### ed062-s5
```yaml
status: ok
t:
  6: PAIN POINTS
  3: SECURITY TEAMS
  5: 'Company security teams that protect calls,

    meetings, payments and hiring from fakes'
```

### ed063-s5
```yaml
status: ok
title: Who needs deepfake detection?
note: We focus on the five groups inside these buyers that choose, pay for, use and check detection tools.
t:
  27: SECURITY TEAMS
  5: 'SECURITY

    LEADERS'
  20: 🛡️
  7: They need to protect executives, meetings and payments from impersonation without adding friction
  8: 'FINANCE

    TEAMS'
  21: 💰
  10: They need to confirm that a payment request on a call or a video really comes from their CFO
  11: 'HR AND

    RECRUITERS'
  22: 💼
  13: They need to check that remote job candidates are real people and not deepfakes before hiring
  14: 'IT AND HELP

    DESKS'
  23: 💻
  16: They need to confirm that a caller asking for a password reset is really the employee they claim
  17: EXECUTIVES
  24: 👔
  19: They need to stop fake copies of their face and voice from being used to trick staff and partners
```

### ed064-s5
```yaml
status: ok
title: What are these customers' strongest pain points?
note: We prioritized problems that recur in fraud reports, regulator alerts, detector tests and company releases on deepfakes.
t:
  13: SECURITY TEAMS
  14: They see fake CFOs order urgent large payments
  15: They face fake candidates in remote job interviews
  16: They see help desks tricked into password resets
  17: They lack a budget line for deepfake defense
  18: They need checks inside Zoom, Teams and Webex
  19: They see their executives cloned for phone scams
  20: They find it hard to train every single employee
```

### ed065-s5
```yaml
status: ok
title: Which pains deserve attention first?
subtitle: Corporate security teams
icons:
- 🛡️
- 💰
- 💼
- 💻
- 👔
rows:
- pain: Fake CFOs on calls order urgent large payments
  s:
  - 3
  - 3
  - 1
  - 1
  - 3
  p: CRITICAL
- pain: Fake candidates slip into remote hiring processes
  s:
  - 2
  - 1
  - 3
  - 2
  - 1
  p: CRITICAL
- pain: Help desks are tricked into giving password resets
  s:
  - 3
  - 1
  - 1
  - 3
  - 1
  p: MAJOR
- pain: No budget line exists yet for deepfake defense
  s:
  - 3
  - 2
  - 1
  - 1
  - 2
  p: HIGH
- pain: Checks must run inside Zoom, Teams and Webex
  s:
  - 2
  - 1
  - 2
  - 3
  - 2
  p: MAJOR
- pain: Executives are cloned to scam staff and partners
  s:
  - 3
  - 2
  - 1
  - 1
  - 3
  p: MAJOR
- pain: Training every employee is slow and very costly
  s:
  - 2
  - 1
  - 2
  - 2
  - 1
  p: HIGH
note:
- Every stakeholder is different, and this table is a simplified view based on reports and studies
- It gives a starting point, not a checklist, so priorities should be checked with real buyers
```
