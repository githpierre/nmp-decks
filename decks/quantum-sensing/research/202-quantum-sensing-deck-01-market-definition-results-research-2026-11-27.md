# quantum sensing, chapter 01 Market definition (evergreen, written by Claude, 27 Nov 2026)

### ed006
```yaml
status: ok
title: What is quantum sensing, in simple terms?
text: It is the market for sensors, clocks and detectors that use atoms, light or diamond to measure time, motion and fields far more precisely than today's tools
note: We use a plain definition here because it makes the boundary with quantum computing and with classical sensors, which share parts and buyers, easier to see.
icon_tl: ⚛️
```

### ed008
```yaml
status: ok
title: What markets are often confused with quantum sensing?
t:
  12: QUANTUM COMPUTING
  13: QUANTUM SENSING
  14: CLASSICAL SENSORS
  7: Quantum sensing differs from both because it uses quantum effects to measure the real world, not to compute
  10: Quantum computers use atoms and lasers to run calculations, while quantum sensors use the same parts to measure
  11: Classical gyros, GPS chips and MRI scanners measure the same things, but without the precision of atoms or diamond
```

### ed009
```yaml
status: ok
title: What markets does quantum sensing sit between?
t:
  8: 'DEFENSE

    TECH'
  9: 'SCIENTIFIC

    INSTRUMENTS'
  10: 'MEDICAL

    IMAGING'
  13: 'Quantum sensing sits between three markets: it sells GPS-free clocks and navigators to armed forces, it builds precise lab instruments for scientists and chipmakers, and it makes wearable brain scanners for hospitals.'
```

### ed010
```yaml
status: ok
title: And what if we break it down in smaller markets?
t:
  21: QUANTUM SENSING
  5: 'QUANTUM

    TIMING'
  8: 'QUANTUM

    NAVIGATION'
  11: 'MAGNETIC

    SENSING'
  14: 'MEDICAL

    IMAGING'
  17: 'RF

    SENSING'
  7: It is in the market when an atomic clock keeps exact time after GPS is lost
  10: It is in the market when a ship or a plane finds its way by gravity, with no GPS
  13: It is in the market when a diamond or atom sensor maps the magnetic field
  16: It is in the market when a wearable helmet maps the brain without helium
  19: It is in the market when excited atoms pick up radio signals instead of antennas
```

### ed011
```yaml
status: ok
title: What are some common acronyms I should know?
note: We prioritized acronyms that appear often in vendor, defense and investor materials rather than very technical physics terms.
t:
  6: PNT
  15: CSAC
  23: GNSS
  8: 'Position, Navigation

    and Timing'
  16: 'Chip-Scale

    Atomic Clock'
  24: 'Global Navigation

    Satellite System'
  17: It is the motion sensors on a ship or plane that guess its position without GPS
  13: It is an atomic clock the size of a chip, made for drones, satellites and radios
  21: It is the family of satellite systems, from GPS to Galileo, that jamming disrupts
  11: NV
  19: INS
  27: DIU
  12: 'Nitrogen-Vacancy

    Center'
  20: 'Inertial

    Navigation System'
  28: 'Defense

    Innovation Unit'
  9: It is a flaw in diamond, a missing atom next to nitrogen, that senses magnetic fields
  4: It is the trio of services GPS gives, which quantum sensors aim to back up
  25: It is the Pentagon unit that funds field tests and early buys of quantum sensors
```

### ed012
```yaml
status: no_data
reason: products and their names change too often to group them reliably without fresh research
```

### ed013
```yaml
status: no_data
reason: prices depend on the platform, the volume and the contract and are rarely published
```

### ed014
```yaml
status: ok
title: When and where is value created in the market?
items:
- e: 🛰️
  t: When a plane keeps flying on course after its GPS signal is jammed or spoofed
- e: ⏱️
  t: When a telecom network keeps exact time after it loses satellite time signals
- e: 🧭
  t: When a ship navigates for days at sea using only gravity maps and no GPS
- e: 🧠
  t: When a hospital scans a child's brain while the child moves, with no helium
- e: 💎
  t: When a miner finds an ore body from a truck before paying for any drilling
- e: 🔬
  t: When a chipmaker sees current flowing inside a chip and finds a hidden fault
- e: 📡
  t: When an army hears radio signals across the whole spectrum with one small receiver
- e: 🏗️
  t: When a builder finds voids and old tunnels under a street before anyone digs
```

### ed015
```yaml
status: ok
title: What are some common myths about quantum sensing?
page: 1/2
note: We focused on myths that come back often in vendor, defense and investor debates. The counters describe what trials, sales and deals have shown so far.
t:
  9: Quantum tech is only about quantum computers
  7: Infleqtion expects about two thirds of its revenue to come from sensing, and QED-C counts 47 firms selling quantum sensors today
  12: Quantum sensors only work in quiet labs
  10: Q-CTRL guided a 29-meter vessel 83 km without GPS, within one nautical mile, and its Ironstone Opal navigator passed DO-160 tests
  15: Nobody really buys quantum sensors yet
  13: Cerca Magnetics has sold 19 wearable brain scanners in 12 countries, and IonQ bought Vector Atomic with $200M+ of contracts, in 2025
  0: GPS jamming only happens in war zones
  16: IATA counts GPS loss on about 57 of every 1,000 flights in 2025, almost twice the 2022 rate, on air routes all around the world
```

### ed016
```yaml
status: ok
title: What are some common myths about quantum sensing?
page: 2/2
note: We focused on myths that come back often in vendor, defense and investor debates. The counters describe what trials, sales and deals have shown so far.
t:
  9: Investors pour lots of money into sensing
  7: McKinsey found that only about 10% of 2025 quantum startup money went to sensing and communication, and the other 90% to quantum computing startups
  12: Quantum sensors must be kept near zero
  10: Diamond sensors work at room temperature, and Dirac Labs is building golf ball-sized units to guide craft by Earth's magnetism
  15: Atomic clocks will always fill a lab bench
  13: Infleqtion's Tiqker optical clock fits in a standard server rack, and Mesa Quantum is working to put such clocks on a single chip
  0: A listed quantum stock is a very safe bet
  16: Infleqtion's shares fell about 65% from their 2026 peak, and its revenue dropped from $12.6M to $9.1M from one quarter to the next
```

### ed017
```yaml
status: ok
title: How mature is quantum sensing as a market?
score: 35
text: The market is real because armed forces, hospitals and chipmakers pay for clocks, scanners and inspection tools today. The score stays low because sales are about $625M, more than a third of firms sold nothing in 2025, and most units are still trial or prototype systems.
note:
- We rate market maturity with an internal score of products on sale, paying clients, big buyers and funding.
- We set 35/100 because demand is real and growing, but most sensors are still leaving the trial stage.
```

### ed018
```yaml
status: ok
title: How can we categorize companies of the quantum sensing market?
page: 1/3
note: We use the solution groups of our company database, merged into six, from atomic clocks to sensors that count single particles of light.
t:
  25: Here, we categorize by type of solution
categories:
- label: 'QUANTUM

    TIMING'
  description: Atomic and optical clocks that keep exact time when GPS goes down
  e: ⏱️
- label: 'QUANTUM

    NAVIGATION'
  description: Atom sensors of motion and gravity that guide ships and planes
  e: 🧭
- label: 'MAGNETIC

    SENSING'
  description: Atom and diamond sensors that map magnetic fields with precision
  e: 🧲
- label: 'MEDICAL

    IMAGING'
  description: Wearable scanners that map the brain and the heart without helium
  e: 🧠
- label: 'RF

    SENSING'
  description: Receivers that use excited atoms to pick up radio and radar signals
  e: 📡
- label: 'OPTICAL

    SENSING'
  description: Detectors and cameras that count single particles of light, one by one
  e: 🔬
```

### ed019
```yaml
status: ok
title: How can we categorize companies of the quantum sensing market?
page: 2/3
note: We also categorize by buyer because armies, telecom operators, miners and hospitals need very different proof, prices and ways to pay.
t:
  25: Here, we categorize by the type of buyer
categories:
- label: 'DEFENSE

    FORCES'
  description: Navies, air forces and armies that need navigation and time without GPS
  e: 🛡️
- label: 'TELECOM AND

    GRID OPERATORS'
  description: Networks and power grids that need exact time if satellite time fails
  e: 📡
- label: 'MINING AND

    ENERGY FIRMS'
  description: Miners and energy firms that map what lies underground before drilling
  e: 🌍
- label: 'HOSPITALS AND

    RESEARCH LABS'
  description: Hospitals and labs that scan brains and study cells and new materials
  e: 🏥
- label: 'CHIP

    MAKERS'
  description: Chip factories that look for hidden faults inside their newest chips
  e: 💻
- label: 'SPACE

    AGENCIES'
  description: Space agencies that map gravity and magnetism of the Earth from orbit
  e: 🛰️
```

### ed020
```yaml
status: ok
title: How can we categorize companies of the quantum sensing market?
page: 3/3
note: A third useful lens is the business model, because a defense grant, a device sale or a software license earns money very differently.
t:
  25: Here, we categorize by business model
categories:
- label: 'DEFENSE

    CONTRACTS'
  description: Paid trials and programs from DARPA, DIU and allied defense ministries
  e: 🏛️
- label: 'DEVICE

    SALES'
  description: Selling each clock, scanner or gravimeter as a unit with a warranty
  e: 📦
- label: 'SOFTWARE

    LICENSES'
  description: Charging for the software that cleans noise and matches readings to maps
  e: 💻
- label: 'SURVEY

    SERVICES'
  description: Running gravity or magnetic surveys for miners and builders as a service
  e: 🧭
- label: 'PARTS AND

    COMPONENTS'
  description: Selling vapor cells, lasers and diamonds to other sensor makers
  e: 🧩
- label: 'OEM

    PARTNERSHIPS'
  description: Building sensors into the products of firms like Safran and Airbus
  e: 🤝
```

### ed021
```yaml
status: ok
title: What do top companies do in this market?
note: Other companies could also make the top eight. We chose startups with the most clients, funding, contracts or field trials to show the range of the market.
t:
  8: CERCA
  16: SANDBOXAQ
  7: It has sold 19 wearable brain scanners to neuroscience centers in 12 countries
  15: Its AQNav guides aircraft by Earth's magnetic field, with 450+ hours flown
  10: INFLEQTION
  18: Q-CTRL
  9: It sells Tiqker clocks and atom radio receivers, and listed on the NYSE in 2026
  17: Its navigator passed DO-160 flight tests, and it raised $290M in 2026
  12: DELTA.G
  20: VECTOR ATOMIC
  11: Its quantum gravity sensors find voids, tunnels and buried structures
  19: It makes sea-tested gravimeters and airborne clocks, and IonQ bought it in 2025
  14: CIQTEK
  22: SBQUANTUM
  13: It makes quantum instruments in Hefei and listed in Shanghai in 2026
  21: Its diamond magnetometer was launched into orbit in 2026 to map Earth's field
```

### ed022
```yaml
status: ok
title: What is rare and that people happily pay for in this market?
note: We looked at funding rounds, deals, contracts and field trials to find the capabilities that look truly scarce and valuable.
t:
  6: '🧭

    Proof on moving platforms, because most sensors lose accuracy on ships and planes'
  7: '🛡️

    Defense track records, because armed forces buy only from proven suppliers'
  8: '📏

    Small size and low power, because drones and racks have very little room'
  9: '🌍

    Good gravity and magnetic maps, because navigators are useless without them'
  10: '✅

    Safety approvals like DO-160, because aircraft need them before any sale'
  11: '🏭

    Volume production, because most sensors are still built one by one by hand'
  12: '🧠

    Software that cancels noise, so sensors work without heavy shielding'
  13: '🧪

    Rare parts like stable lasers and pure diamond, made by very few suppliers'
```

### ed023
```yaml
status: ok
title: Which quantum sensing truths have flipped?
note: These are market shifts we see in recent trials, deals and company releases. They are not formal industry rules, but they come back across the evidence.
t:
  6: Quantum sensors used to work only on quiet lab benches
  8: Now Q-CTRL navigates ships and planes with them, with no GPS at all
  10: Atomic clocks used to fill a whole laboratory table
  12: Now Infleqtion's Tiqker clock fits inside a standard server rack
  14: GPS loss used to be a rare problem for airlines
  16: Now IATA counts it on about 57 of every 1,000 flights each year
  18: Sensing startups used to live on research grants
  20: Now Q-CTRL raised $290M, and Infleqtion listed on the NYSE in 2026
  22: Brain scans used to need magnets cooled by liquid helium
  24: Now Cerca's wearable helmets scan brains at normal room temperature
  26: Quantum sensing used to be a side show next to computing
  28: Now IonQ, Thales and Quantum Design buy quantum sensing firms
```

### ed024
```yaml
status: ok
title: What has changed (very) recently?
page: 1/2
items:
- d: SINCE 2024
  t: Infleqtion flew its Tiqker optical clock and a cold-atom system on a UK test jet in May 2024, the first such flights made public anywhere in the world.
- d: SINCE 2024
  t: The Pentagon gave Infleqtion an $11M APFIT contract in December 2024 to field its Tiqker clocks faster, one of the first production steps for quantum timing.
- d: SINCE 2025
  t: Q-CTRL's Ironstone Opal navigated aircraft without GPS in April 2025, with up to 50 times less error than a high-end conventional backup system.
- d: SINCE 2025
  t: DARPA launched its Robust Quantum Sensors program in August 2025 and gave Q-CTRL $24.4M to make sensors that keep working on military vehicles.
- d: SINCE 2025
  t: IonQ completed its purchase of Vector Atomic in October 2025, adding field-tested clocks, gravimeters and motion sensors backed by $200M+ of contracts.
- d: SINCE 2026
  t: Infleqtion began trading on the NYSE in February 2026 after its SPAC merger, with over $550M of new money for its sensors, clocks and computers.
note:
- We kept the milestones that most changed the products, the money and the big players of the market
- There is no official timeline, and another analyst could reasonably pick a few different milestones here
```

### ed025
```yaml
status: ok
title: What has changed (very) recently?
page: 2/2
items:
- d: SINCE 2026
  t: A US executive order of June 2026 told the Pentagon to field at least three quantum sensor projects by 2028, and DIU set aside up to $200M for Farseer.
- d: SINCE 2026
  t: Q-CTRL's Ironstone Opal became the first quantum navigation system to pass the DO-160 flight safety tests in July 2026, a key step toward use on aircraft.
- d: SINCE 2026
  t: Thales agreed in July 2026 to buy Exail, maker of cold-atom gravimeters, at a €3.9B enterprise value, and named quantum sensors as one reason for the deal.
- d: SINCE 2026
  t: QuantumDiamonds closed €91M in July 2026, including €76M of EU Chips Act aid, to build a factory for diamond-based chip inspection tools in Munich.
- d: SINCE 2026
  t: CIQTEK, a Hefei maker of quantum measuring instruments, listed on Shanghai's STAR Market in August 2026, with a value above 45 billion yuan on day one.
- d: SINCE 2026
  t: Q-CTRL raised a $290M Series C led by Salesforce Ventures in November 2026, at a value above $1B, to scale its GPS-free Ironstone Opal navigator.
note:
- We kept the milestones that most changed the products, the money and the big players of the market
- There is no official timeline, and another analyst could reasonably pick a few different milestones here
```
