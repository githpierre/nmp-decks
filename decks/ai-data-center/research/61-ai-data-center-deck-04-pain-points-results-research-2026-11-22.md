# AI data center, chapter 04 Pain points (evergreen, written by Claude, 22 Nov 2026)

### ed054
```yaml
status: ok
title: What are the pain points of yesterday vs. today?
note: We grouped the market into phases, from cloud data centers sized by floor space to today's gigawatt AI campuses. We used company filings, lease news and utility reports.
t:
  6: "2015 - 2021\n\nCloud data centers grew fast near big cities, but each rack drew little power and air cooling was enough for every hall"
  7: "2022 - 2023\n\nChatGPT set off a rush for AI chips, but most halls could not power or cool the new racks, and good sites ran out fast"
  8: "2024 - 2025\n\nAI labs and big clouds signed huge leases for new campuses, but grid hookups, gas turbines and transformers became scarce"
  9: "TODAY\n\nGigawatt AI campuses are going live, but power, local opposition and a few huge tenants limit how fast the market can grow"
  10: "?\n\nOwn power plants and factory-built halls could speed things up, but only if AI demand holds for the 15 years of each lease"
```

### ed055
```yaml
status: ok
title: Which old problems are now behind us?
note: We treat these as problems that new builders, leases and financing have removed for tenants. They do not mean that AI capacity is now cheap or easy to find everywhere.
t:
  5: AI tenants could only find halls built for ordinary servers drawing little power
  7: New AI halls are now built for racks of over 100 kW, with water pipes running straight onto the chips
  8: A big data center meant a single building of a few megawatts
  10: Campuses of one gigawatt or more are now being built in Texas, Louisiana, Norway and the Gulf
  11: Building a data center took three to four years from land to first tenant
  13: Factory-built halls and ready powered land now cut the wait for some sites to well under two years
  14: Big tech had to build and own almost every large site itself
  16: Startups like Crusoe, Lancium and Fluidstack now build whole campuses that big tech and AI labs lease
  17: Lenders would not fund a campus without decades of track record
  20: Data centers had to wait for the grid in a few crowded hubs
  19: Banks and funds now lend billions against long leases signed by strong tenants before the first hall opens
  22: Sites with their own gas turbines or power plants now go live away from the crowded hubs
```

### ed056
```yaml
status: ok
title: What problems do all players face?
page: 1/2
note: We kept the problems that come back in company filings, utility reports and analyst notes. We skipped electrical design details and focused on what blocks AI data centers from growing.
t:
  6: "You need power\nbefore your rivals"
  8: "Grid hookups take\nyears to arrive"
  10: "You need a tenant\nbefore you build"
  12: "Few leases are\nsigned early"
  14: "You need heavy\npower equipment"
  16: "Gas turbines\narrive years late"
  18: "You must cool\nthe newest racks"
  20: "Old halls cannot\nhandle the heat"
  23: "You need signed\nleases to borrow"
  25: "Debt costs rise\nwith every delay"
  27: "You must win\nlocal support"
  29: "Towns block or\ndelay new sites"
  31: "You must build\nbefore chips change"
  33: "Each new chip\nneeds more power"
  35: "You need crews\nwho build fast"
  37: "Skilled crews\nare hard to hire"
```

### ed057
```yaml
status: ok
title: What problems do all players face?
page: 2/2
note: We separated the problems of building capacity from the problems of leasing it. Even a builder with power and land must still find tenants, prices and rules it can live with.
t:
  6: "You need more\nthan one tenant"
  8: "A few tenants take\nmost of the capacity"
  10: "You must secure\nwater for cooling"
  12: "Dry regions limit\nwater use"
  14: "You need fair\nlease prices"
  16: "Lease prices\nswing with demand"
  18: "You must keep\nsites running"
  20: "One outage hits\nevery tenant"
  23: "You need land\nwith fiber nearby"
  25: "Good sites are\ntaken years early"
  27: "You must follow\nlocal energy rules"
  29: "Rules differ in\neach state"
  31: "You need cheap\nmoney to grow"
  33: "Interest rates\nraise every cost"
  35: "You must plan\nfor tenants leaving"
  37: "Leases can be cut\nbefore they start"
```

### ed059
```yaml
status: ok
title: Which problems are startups going after?
t:
  16: "Grid\naccess"
  11: "Build\nspeed"
  14: "Power\nsupply"
  21: "Pain points change sharply by tenant and by size.\n\nBroad statements quickly mislead.\nSo we split AI labs, big tech, GPU clouds and governments before scoring priorities."
  13: "Liquid\ncooling"
  12: "Tenant\nspread"
  15: "Local\nsupport"
  18: "Sovereign\nsites"
  19: "Cheap\nfinancing"
```

### ed060
```yaml
status: ok
title: How will we proceed?
note: We break the market down before scoring because the same campus creates very different value and risk for an AI lab, a big cloud, a GPU cloud or a government.
t:
  9: "😣\nPAIN POINTS\n\nWe list each group's main pains and score them to rank them."
  6: "🎯\nGOAL\n\nFind the pain points that matter most in AI data centers, and who feels them."
  7: "🏷️\nCATEGORIES\n\nWe split the market by tenant, because needs and budgets differ a lot."
  8: "🧑‍🤝‍🧑\nSEGMENTS\n\nFor each tenant, we list the people who decide, pay, use and approve."
```

### ed061
```yaml
status: ok
title: Which categories will we use?
note: We split the market into four tenant groups. They differ enough in lease size, technical needs and decision steps to score their pain points separately.
t:
  7: "AI MODEL\nLABS"
  9: "HYPERSCALERS\nAND BIG TECH"
  11: "GPU\nCLOUDS"
  13: "ENTERPRISES AND\nGOVERNMENTS"
  6: Labs like OpenAI and Anthropic that need gigawatt campuses to train and run models
  8: Big clouds and tech groups that lease whole campuses when their own builds run late
  10: AI clouds like CoreWeave and Lambda that lease powered halls to fill with rented chips
  12: Banks, factories and states that want AI computing kept inside their own country
  15: ''
  17: ''
  14: ''
  16: ''
holes_ok: true
```

### ed062-s1
```yaml
status: ok
t:
  6: PAIN POINTS
  3: AI MODEL LABS
  5: "Labs that train the biggest AI models\nand lease whole campuses for many years"
```

### ed063-s1
```yaml
status: ok
title: Who needs AI data center capacity?
note: We focus on the five groups inside AI labs that plan, approve, fund and use the campuses they lease from builders.
t:
  27: AI MODEL LABS
  5: "COMPUTE\nLEADS"
  8: "RESEARCH\nTEAMS"
  11: "FINANCE\nCHIEFS"
  14: "SITE\nTEAMS"
  17: "SECURITY\nTEAMS"
  20: 🧑‍💻
  21: 🧠
  22: 💰
  23: 🏗️
  24: 🔒
  7: They need gigawatts of capacity on a fixed date, since a late campus delays the next model by months
  10: They need halls that never lose power, because one outage can stop a training run for hours
  13: They need to fund billions of building without being stuck with sites the next chips outgrow
  16: They need sites with power, water and fiber ready, in places where towns will not block them
  19: They need to keep model weights and data safe in buildings that the lab does not run itself
```

### ed064-s1
```yaml
status: ok
title: What are these customers' strongest pain points?
note: We prioritized problems that recur in lab statements, lease news and analyst reports on the largest AI campuses.
t:
  13: AI MODEL LABS
  14: They get their new campuses later than the date promised
  15: They run out of power before they run out of money
  16: They sign leases of 15 years for chips that age in two
  17: They depend on a few builders for most of their capacity
  18: They face local anger over power bills and water use
  19: They see training runs stop when a site loses power
  20: They must protect model weights in sites they do not run
```

### ed065-s1
```yaml
status: ok
title: Which pains deserve attention first?
subtitle: AI model labs
icons:
- 🧑‍💻
- 🧠
- 💰
- 🏗️
- 🔒
rows:
- pain: New campuses arrive later than the date in the lease
  s: [3, 3, 2, 3, 1]
  p: CRITICAL
- pain: Power runs out before money does on new sites
  s: [3, 2, 2, 3, 1]
  p: CRITICAL
- pain: Leases of 15 years outlive chips that age in two
  s: [2, 1, 3, 2, 1]
  p: MAJOR
- pain: Most of their capacity depends on a few builders
  s: [3, 2, 3, 2, 2]
  p: MAJOR
- pain: Local anger over power bills and water use grows
  s: [1, 1, 2, 3, 1]
  p: HIGH
- pain: Training runs stop for hours when a site loses its power
  s: [2, 3, 1, 2, 1]
  p: HIGH
- pain: Model weights sit in buildings that the lab does not run
  s: [1, 2, 1, 1, 3]
  p: HIGH
note:
- Every stakeholder is different, and this table is a simplified view based on lab statements and analyst reports
- It gives a starting point, not a checklist, so priorities should be validated with labs, builders and lenders
```

### ed062-s2
```yaml
status: ok
t:
  6: PAIN POINTS
  3: HYPERSCALERS AND BIG TECH
  5: "Big clouds and tech groups that lease\nwhole campuses when their own run late"
```

### ed063-s2
```yaml
status: ok
title: Who needs AI data center capacity?
note: We focus on the five groups inside big clouds and tech groups that decide when to lease campuses from builders and how much.
t:
  27: HYPERSCALERS AND BIG TECH
  5: "CAPACITY\nPLANNERS"
  8: "SITE\nSELECTION TEAMS"
  11: "LEASING\nTEAMS"
  14: "FINANCE\nCHIEFS"
  17: "ENERGY\nTEAMS"
  20: 📊
  21: 📍
  22: 📝
  23: 💰
  24: ⚡
  7: They need new halls within months when their own new data centers are late or already full
  10: They need sites with power and land ready, far from the crowded hubs where the grid is full
  13: They need leases they can grow or cut, since demand for AI may change within two or three years
  16: They need to lease rather than build, to keep billions of spending off their own balance sheet
  19: They need clean or firm power for each site, to meet their climate goals and keep uptime high
```

### ed064-s2
```yaml
status: ok
title: What are these customers' strongest pain points?
note: We prioritized problems that recur in earnings calls of the big clouds, their lease announcements and analyst reports on AI spending.
t:
  13: HYPERSCALERS AND BIG TECH
  14: They have more AI demand than their own sites can serve
  15: They wait years for power at their own new data centers
  16: They face investors worried about record AI spending
  17: They miss climate goals as new sites burn more gas
  18: They risk paying for capacity if AI demand slows
  19: They rely on young builders carrying heavy debt
  20: They face towns that block or delay their new campuses
```

### ed065-s2
```yaml
status: ok
title: Which pains deserve attention first?
subtitle: Hyperscalers and big tech
icons:
- 📊
- 📍
- 📝
- 💰
- ⚡
rows:
- pain: AI demand is larger than their own sites can serve
  s: [3, 2, 2, 2, 1]
  p: CRITICAL
- pain: Power for their own new data centers takes years
  s: [3, 3, 1, 2, 3]
  p: CRITICAL
- pain: Investors worry about their record spending on AI
  s: [1, 1, 2, 3, 1]
  p: MAJOR
- pain: New sites burn more gas and push climate goals away
  s: [1, 2, 1, 1, 3]
  p: HIGH
- pain: Long leases must still be paid if demand slows
  s: [2, 1, 3, 3, 1]
  p: HIGH
- pain: Their builders carry heavy debt on every campus
  s: [1, 1, 3, 3, 1]
  p: HIGH
- pain: Towns block or delay their new campuses for years
  s: [2, 3, 1, 1, 2]
  p: MAJOR
note:
- Every stakeholder is different, and this table is a simplified view based on earnings calls and lease news
- It gives a starting point, not a checklist, so priorities should be validated with clouds, builders and analysts
```

### ed062-s3
```yaml
status: ok
t:
  6: PAIN POINTS
  3: GPU CLOUDS
  5: "AI clouds that rent out chips by the hour\nand lease powered halls to put them in"
```

### ed063-s3
```yaml
status: ok
title: Who needs AI data center capacity?
note: We focus on the five groups inside GPU clouds that choose, pay for and run the halls behind the chips they rent out.
t:
  27: GPU CLOUDS
  5: "STARTUP\nFOUNDERS"
  8: "DATA CENTER\nTEAMS"
  11: "CAPACITY\nPLANNERS"
  14: "FINANCE\nLEADS"
  17: "OPERATIONS\nTEAMS"
  20: 🚀
  21: 🏢
  22: 📊
  23: 💵
  24: ⚙️
  7: They need powered halls in months, since a signed client will not wait for a new building
  10: They need halls built for liquid cooling, ready for the hottest racks Nvidia ships each year
  13: They need capacity that grows in steps with their client contracts, not one giant site at once
  16: They need leases that lenders accept, so they can borrow against the GPUs they put inside
  19: They need sites that rarely fail, because clients pay only for hours when the chips are running
```

### ed064-s3
```yaml
status: ok
title: What are these customers' strongest pain points?
note: We prioritized problems that recur in GPU cloud filings, founder interviews and lease news from former bitcoin mining sites.
t:
  13: GPU CLOUDS
  14: They find few powered halls ready for the newest racks
  15: They sign long leases before clients have signed theirs
  16: They pay rent on halls while chips are still on the way
  17: They depend on landlords that carry heavy debt too
  18: They lose clients when a site goes down for hours
  19: They see lease prices rise in every crowded hub
  20: They wait for builders who promise more than they deliver
```

### ed065-s3
```yaml
status: ok
title: Which pains deserve attention first?
subtitle: GPU clouds
icons:
- 🚀
- 🏢
- 📊
- 💵
- ⚙️
rows:
- pain: Few powered halls are ready for the newest racks
  s: [3, 3, 3, 1, 2]
  p: CRITICAL
- pain: Long leases are signed before client contracts are
  s: [3, 1, 2, 3, 1]
  p: CRITICAL
- pain: Rent is paid on halls while chips are still on the way
  s: [2, 1, 2, 3, 1]
  p: MAJOR
- pain: Their landlords carry heavy debt on every site
  s: [2, 1, 1, 3, 1]
  p: HIGH
- pain: Clients leave when a site goes down for hours at a time
  s: [3, 2, 1, 1, 3]
  p: MAJOR
- pain: Lease prices rise in every crowded data center hub
  s: [2, 1, 2, 3, 1]
  p: HIGH
- pain: Builders promise more capacity than they deliver
  s: [3, 3, 3, 2, 2]
  p: HIGH
note:
- Every stakeholder is different, and this table is a simplified view based on GPU cloud filings and lease news
- It gives a starting point, not a checklist, so priorities should be validated with founders, landlords and lenders
```

### ed062-s4
```yaml
status: ok
t:
  6: PAIN POINTS
  3: ENTERPRISES AND GOVERNMENTS
  5: "Large firms and states that want AI\ncomputing kept inside their own country"
```

### ed063-s4
```yaml
status: ok
title: Who needs AI data center capacity?
note: We focus on the five groups inside large firms and public bodies that decide, approve and pay for AI capacity at home.
t:
  27: ENTERPRISES AND GOVERNMENTS
  5: "IT\nCHIEFS"
  8: "DATA\nTEAMS"
  11: "COMPLIANCE\nOFFICERS"
  14: "PUBLIC\nAGENCIES"
  17: "BUYING\nTEAMS"
  20: 🏢
  21: 📊
  22: ⚖️
  23: 🏛️
  24: 📋
  7: They need AI capacity that fits their security rules, without building an AI data center themselves
  10: They need to train and run models on their own data, which often cannot leave the country
  13: They need proof of where data sits and who can enter the site, to satisfy regulators and auditors
  16: They need national AI campuses for local firms and researchers, run under local law and power
  19: They need clear leases and prices they can compare, in a market that changes every quarter
```

### ed064-s4
```yaml
status: ok
title: What are these customers' strongest pain points?
note: We prioritized problems that recur in enterprise AI surveys, public sovereign AI plans and the offers of local AI data centers.
t:
  13: ENTERPRISES AND GOVERNMENTS
  14: They cannot send sensitive data to sites abroad
  15: They lack the staff to run AI halls on their own
  16: They find few local sites ready for the newest racks
  17: They must prove where their data sits to regulators
  18: They struggle to compare offers that change each quarter
  19: They fear paying for capacity that their teams barely use
  20: They face slow public buying rules in a fast market
```

### ed065-s4
```yaml
status: ok
title: Which pains deserve attention first?
subtitle: Enterprises and governments
icons:
- 🏢
- 📊
- ⚖️
- 🏛️
- 📋
rows:
- pain: Sensitive data cannot be sent to sites in other countries
  s: [3, 3, 3, 3, 1]
  p: CRITICAL
- pain: Too few of their staff know how to run AI halls
  s: [3, 2, 1, 2, 1]
  p: MAJOR
- pain: Few local sites are ready for the newest AI racks
  s: [2, 3, 1, 3, 2]
  p: MAJOR
- pain: Regulators ask where data sits and who sees it
  s: [2, 1, 3, 3, 1]
  p: CRITICAL
- pain: Offers and prices of builders change each quarter
  s: [1, 1, 1, 1, 3]
  p: HIGH
- pain: Capacity leased may sit barely used for months
  s: [3, 2, 1, 2, 3]
  p: HIGH
- pain: Public buying rules are too slow for such a fast market
  s: [1, 1, 1, 3, 3]
  p: HIGH
note:
- Every stakeholder is different, and this table is a simplified view based on enterprise surveys and public AI plans
- It gives a starting point, not a checklist, so priorities should be validated with IT chiefs, agencies and builders
```
