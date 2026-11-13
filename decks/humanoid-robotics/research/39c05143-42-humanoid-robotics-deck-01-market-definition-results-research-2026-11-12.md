### ed006
```yaml
status: ok
section: Market definition
title: What is the humanoid robotics market, in simple terms?
text: Humanoid robotics is the market for complete robots with a human-like upper body that can move, handle objects and perform useful physical tasks in spaces built for people
note: We use a functional definition because humanoid robots can walk on legs, roll on wheels or use hybrid bases while still doing human-oriented work.
sources:
  - claim: Humanoid robots are defined here by human-oriented form and physical work, not by bipedal locomotion alone.
    url: https://www.bmwgroup.com/en/news/general/2026/humanoid-robot-in-leipzig.html
    date: 2026-10-01
    quote: "The centrepiece of AEON is its human-like torso, which can be equipped with a range of gripping tools."
```

### ed007p
```yaml
status: ok
section: Market definition
title: 'What is actually included

  in the humanoid robotics market?'
caption:
- Distance to the center reflects how closely each company fits a complete, task-performing humanoid platform
- The companies shown are a representative sample, not an exhaustive list, chosen to show where the market’s boundaries lie
inside:
- <logo>
- <logo>
- <logo>
- <logo>
- <logo>
- <logo>
- <logo>
- <logo>
inside_xy:
- x: 486.4
  y: 352.2
- x: 446.1
  y: 397.2
- x: 505.5
  y: 411.4
- x: 422.5
  y: 334.2
- x: 553.3
  y: 359.5
- x: 469.3
  y: 463.3
- x: 506.6
  y: 280.2
- x: 373.2
  y: 371.1
edge_xy:
  BL:
    x: 386.7
    y: 489.9
  BR:
    x: 588.7
    y: 483.9
  TL:
    x: 361.7
    y: 279.3
  TR:
    x: 647.6
    y: 277.6
TL:
  name: NVIDIA
  text: supplies computing and robot AI platforms, but does not independently sell a complete humanoid robot
TR:
  name: Schunk
  text: supplies robot hands and gripping systems, not a complete mobile humanoid platform
BL:
  name: Unitree Robotics
  text: sells quadrupeds too, but independently designs and sells complete humanoid robots such as G1 and R1
BR:
  name: Hexagon Robotics
  text: sits near the edge because AEON rolls on wheels, but its human-like torso and arms perform factory tasks
logos:
- name: Figure AI
  domain: figure.ai
- name: Apptronik
  domain: apptronik.com
- name: Agility Robotics
  domain: agilityrobotics.com
- name: Boston Dynamics
  domain: bostondynamics.com
- name: Unitree Robotics
  domain: unitree.com
- name: 1X
  domain: 1x.tech
- name: Sanctuary AI
  domain: sanctuary.ai
- name: NEURA Robotics
  domain: neura-robotics.com
note: We include complete task-performing humanoids and human-form mobile manipulators, while excluding component, compute and AI-only suppliers.
sources:
  - claim: Unitree sells complete humanoid robots including G1 and R1.
    url: https://shop.unitree.com/collections/humanoid-robot
    date: 2026-11-11
    quote: "Unitree R1 From $4,900.00 USD"
  - claim: AEON is a wheeled humanoid with a human-like torso.
    url: https://www.bmwgroup.com/en/news/general/2026/humanoid-robot-in-leipzig.html
    date: 2026-10-01
    quote: "The centrepiece of AEON is its human-like torso"
```

### ed008
```yaml
status: ok
section: Market definition
title: What markets are often confused with humanoid robotics?
t:
  12: INDUSTRIAL ARMS
  13: HUMANOID ROBOTS
  14: MOBILE ROBOTS
  7: Humanoids differ because one integrated robot combines mobility, perception and human-like arms to perform varied physical tasks
  10: Industrial arms are fixed machines optimized for repeatable motions, usually inside a defined workstation or guarded cell
  11: Mobile robots move goods through sites, while humanoids add arms and manipulation for tasks designed around human bodies
note: We separate humanoids from adjacent automation by requiring an integrated body that can physically manipulate its environment.
sources:
  - claim: Humanoids are positioned for flexible work in human spaces rather than only fixed automation.
    url: https://www.agilityrobotics.com/content/digit-deployed-at-gxo-in-historic-humanoid-raas-agreement
    date: 2024-06-05
    quote: "Digit is built to operate in human spaces and do many things."
```

### ed009
```yaml
status: ok
section: Market definition
title: What markets does humanoid robotics sit between?
t:
  8: 'ROBOTICS

    HARDWARE'
  13: 'Humanoid robotics sits between three markets: robotics hardware provides the body, physical AI provides learned behavior, and industrial automation provides the workflows, safety and integration needed for useful work.'
  9: PHYSICAL<br>AI
  10: INDUSTRIAL<br>AUTOMATION
note: We use these three adjacent markets because commercial humanoids need capable hardware, learned control and integration into real operating environments.
sources:
  - claim: Physical AI links digital AI with physical machines in production.
    url: https://www.press.bmwgroup.com/global/article/detail/T0455864EN/bmw-group-to-deploy-humanoid-robots-in-production-in-germany-for
    date: 2026-02-27
    quote: "Physical AI combines digital artificial intelligence (AI) with real machines and robots."
```

### ed010
```yaml
status: ok
section: Market definition
title: And what if we break it down in smaller markets?
t:
  21: HUMANOID ROBOTS
  5: 'GENERAL-PURPOSE

    BIPEDS'
  8: 'WHEELED

    HUMANOIDS'
  11: 'DEVELOPER

    PLATFORMS'
  14: 'SOCIAL

    HUMANOIDS'
  17: 'INDUSTRIAL

    SUPERHUMANOIDS'
  7: It is in the market when a two-legged robot can move, manipulate objects and learn multiple useful tasks
  10: It is in the market when a human-like torso and arms ride on wheels to work flexibly around a site
  13: It is in the market when a complete physical humanoid is sold for embodied-AI research and development
  16: It is in the market when a complete human-form robot physically interacts with people and its surroundings
  19: It is in the market when a heavy-duty human-form machine is built to manipulate loads in industrial settings
note: We break the market into robot forms and use cases rather than components, because each segment still requires a complete embodied platform.
sources:
  - claim: Unitree sells humanoids with open control interfaces for development.
    url: https://www.unitree.com/mobile/R1/
    date: 2026-10-31
    quote: "Fully open control interfaces for joints and sensors"
  - claim: AEON uses a wheeled base with a human-like torso.
    url: https://www.bmwgroup.com/en/news/general/2026/humanoid-robot-in-leipzig.html
    date: 2026-10-01
    quote: "enables dynamic use on wheels"
```

### ed011
```yaml
status: ok
section: Market definition
title: What are some common acronyms I should know?
note: We prioritized acronyms that recur in humanoid product, AI, deployment and investor materials rather than narrow engineering abbreviations.
t:
  6: DoF
  15: VLA
  23: RaaS
  8: 'Degrees of

    Freedom'
  16: 'Vision-Language-

    Action'
  24: 'Robots as a

    Service'
  4: It counts the independent joint motions that determine how flexibly a robot can move
  13: It is an AI model that links camera input and language directly to physical robot actions
  21: It is a subscription-style model where customers pay to use robots rather than own them
  11: AMR
  19: HRI
  27: ODD
  12: 'Autonomous Mobile

    Robot'
  20: 'Human-Robot

    Interaction'
  28: 'Operational Design

    Domain'
  9: It is a wheeled robot that navigates a site autonomously, usually without human-like arms
  17: It describes how people and robots communicate, share space and work safely together
  25: It defines the conditions and environments in which an autonomous robot is designed to operate
sources:
  - claim: Unitree G1 is specified with 23 to 43 degrees of freedom.
    url: https://www.unitree.com/g1/
    date: 2026-11-10
    quote: "23~43 joint motors"
  - claim: Figure describes Helix as a vision-language-action model.
    url: https://www.figure.ai/news/helix
    date: 2025-02-20
    quote: "Vision-Language-Action (VLA) model"
  - claim: Agility and GXO announced a Robots-as-a-Service agreement.
    url: https://www.agilityrobotics.com/content/gxo-signs-industry-first-multi-year-agreement-with-agility-robotics
    date: 2024-06-27
    quote: "first Robots-as-a-Service (RaaS) deployment of humanoid robots"
```

### ed012
```yaml
status: ok
section: Market definition
title: 'What products and services

  are sold in this market?'
note: We grouped the main commercial offers so you get a clear view of most of the market, from developer hardware to enterprise deployments and home robots.
t:
  7: Robot hardware
  35: Complete humanoids sold to developers
  37: Robots sold or leased to businesses
  16: Unitree G1
  19: Unitree R1
  10: Atlas
  13: Apollo
  17: Unitree H2
  20: Figure 03
  11: Phoenix
  14: Digit
  18: 4NE1
  21: AEON
  12: NEO
  15: GR-2
  8: Paid as hardware
  9: Paid per robot
  22: Digit RaaS
  25: Fleet software
  28: Robot support
  31: Site integration
  23: NEO subscription
  26: Skill updates
  29: Remote assist
  32: Maintenance
  24: Pilot programs
  27: Safety setup
  30: AI training
  33: Data capture
  38: Services that enterprises buy with robots
  39: Software and support bought around robots
  6: Deployment stack
sources:
  - claim: Unitree publicly sells G1 and R1 hardware.
    url: https://shop.unitree.com/collections/humanoid-robot
    date: 2026-11-11
    quote: "Unitree G1 From $13,500.00 USD"
  - claim: NEO is available through ownership and subscription.
    url: https://www.1x.tech/order
    date: 2026-10-01
    quote: "$499/mo Subscription"
  - claim: Digit has a commercial RaaS model.
    url: https://www.agilityrobotics.com/content/gxo-signs-industry-first-multi-year-agreement-with-agility-robotics
    date: 2024-06-27
    quote: "first Robots-as-a-Service (RaaS) deployment of humanoid robots"
```

### ed013
```yaml
status: ok
section: Market definition
title: 'What are the different

  price ranges?'
note: We show public hardware or subscription prices where manufacturers publish them. Enterprise humanoids are often sold through negotiated pilots or service contracts instead.
t:
  6: '$4.9K-$20K


    Entry humanoids and developer units sit here, such as Unitree R1 from $4,900, G1 from $13,500 and 1X NEO Early Access at $20,000'
  7: '$20K-$100K


    Larger research and performance robots sit here, including Unitree H2 at $29,900 and H1 listed at $90,000 before tax and shipping'
  8: '$100K+ / RaaS


    Enterprise systems often use negotiated contracts or service pricing; Agility commercializes Digit through multi-year Robots-as-a-Service deals'
sources:
  - claim: Unitree R1 starts at $4,900.
    url: https://www.unitree.com/mobile/R1/
    date: 2026-10-31
    quote: "Price from $4,900"
  - claim: Unitree G1 starts at $13,500.
    url: https://www.unitree.com/g1/
    date: 2026-11-10
    quote: "Price from $13.5K"
  - claim: NEO Early Access ownership costs $20,000.
    url: https://www.1x.tech/order
    date: 2026-10-01
    quote: "$20,000 Ownership"
  - claim: Unitree H2 is listed at $29,900 and H1 at $90,000.
    url: https://shop.unitree.com/
    date: 2026-11-11
    quote: "Unitree H2 $29,900.00 USD"
  - claim: Digit is sold through a multi-year RaaS agreement.
    url: https://www.agilityrobotics.com/content/gxo-signs-industry-first-multi-year-agreement-with-agility-robotics
    date: 2024-06-27
    quote: "multi-year agreement to begin deploying Digit"
```

### ed014
```yaml
status: ok
section: Market definition
title: When and where is value created in the market?
items:
- e: 🦾
  t: When one robot can learn several physical tasks instead of being built for only one motion
- e: ⏱️
  t: When automation can be added to an existing human workspace without rebuilding the whole line
- e: 👁️
  t: When perception lets the robot handle parts that arrive in changing positions and orientations
- e: 👐
  t: When two capable hands let one platform handle tools, bins and objects made for people
- e: 🚶
  t: When mobility lets the same robot move between workstations and manipulate at each one
- e: 🏭
  t: When reliable shift operation turns a prototype into useful labor inside a real facility
- e: 🛡️
  t: When safety systems let robots work around people without isolating every task behind cages
- e: 📈
  t: When fleet software and shared learning spread one new skill across many deployed robots
note: We focus on value created by flexibility, manipulation, safe integration and repeatable operation, not spectacle or human-like appearance alone.
sources:
  - claim: Figure 02 ran 10-hour shifts in BMW production.
    url: https://www.figure.ai/news/production-at-bmw
    date: 2025-11-19
    quote: "Ran 10-hour shift Monday-Friday"
  - claim: Figure 03 handles variable part positions in sequencing.
    url: https://www.figure.ai/news/f-03-at-bmw
    date: 2026-06-30
    quote: "parts may have shifted, rotated, partially occluded, or presented differently"
```

### ed015
```yaml
status: ok
section: Market definition
title: What are some common myths about humanoid robotics?
page: 1/2
note: We focused on myths that recur in company, investor and specialist discussions. These counters distinguish demonstrated operation from broader claims about future scale.
t:
  9: Humanoids are still only staged demos and lab prototypes
  7: Digit has worked commercially at GXO since 2024, and its fleet has logged more than 65,000 real-world operating hours
  12: Humanoids need factories rebuilt around the robot
  10: Figure 02 worked on BMW’s existing line, loading 90,000+ parts and supporting production of more than 30,000 vehicles
  15: Useful humanoids must always walk on two legs
  13: BMW is piloting Hexagon’s wheeled AEON because a human-like torso and arms can still perform flexible factory work
  0: Humanoids cannot yet perform a full production shift
  16: Figure 02 ran ten-hour weekday shifts at BMW, while Digit operates in live logistics under a commercial agreement
sources:
  - claim: Digit has more than 65,000 hours of real-world operation.
    url: https://www.agilityrobotics.com/content/gxo-and-agility-robotics-expand-partnership-to-accelerate-deployment-of-humanoids-in-u-s-operations
    date: 2026-10-26
    quote: "Digit has accumulated more than 65,000 hours of real-world operation."
  - claim: Figure 02 moved more than 90,000 parts and supported 30,000 vehicles.
    url: https://www.figure.ai/news/production-at-bmw
    date: 2025-11-19
    quote: "90,000+ parts loaded"
  - claim: AEON is designed for dynamic use on wheels.
    url: https://www.press.bmwgroup.com/global/article/detail/T0455864EN/bmw-group-to-deploy-humanoid-robots-in-production-in-germany-for
    date: 2026-02-27
    quote: "enables dynamic use on wheels"
```

### ed016
```yaml
status: ok
section: Market definition
title: What are some common myths about humanoid robotics?
page: 2/2
note: We focused on myths that recur in company, investor and specialist discussions. The counters show real progress while avoiding claims that broad autonomy is already solved.
t:
  9: Humanoids are only for car factories
  7: Digit is deployed in logistics, while NEO targets homes and Figure is testing both factory and household-style manipulation
  12: Every useful humanoid costs hundreds of thousands
  10: Unitree lists R1 from $4,900 and G1 from $13,500, while 1X lists NEO Early Access ownership at $20,000
  15: General-purpose autonomy is already solved
  13: Current deployments still focus on bounded tasks such as tote handling, sheet-metal loading and parts sequencing
  0: No serious buyer has moved beyond small experiments
  16: Agility reports $300M+ in committed multi-year Digit 5 orders, subject to contractual milestones
sources:
  - claim: Unitree R1 starts at $4,900 and G1 at $13,500.
    url: https://shop.unitree.com/collections/humanoid-robot
    date: 2026-11-11
    quote: "Unitree R1 From $4,900.00 USD"
  - claim: Agility has more than $300M in committed multi-year Digit 5 orders.
    url: https://investors.agilityrobotics.com/news-releases/news-release-details/agility-robotics-and-churchill-capital-corp-xi-complete-business
    date: 2026-11-04
    quote: "more than $300 million in committed multi-year orders for Digit 5"
```

### ed017
```yaml
status: ok
section: Market definition
title: How mature is humanoid robotics as a market?
score: 45
text: The market is commercially real because humanoids now work in live factories and warehouses, some fleets have tens of thousands of operating hours, and production hardware is shipping. The score stays below halfway because deployments remain small, task scope is narrow, and broad general-purpose autonomy is not yet proven at scale.
note:
- We rate market maturity with a simple internal score based on real deployments, product availability, customer commitments and repeatable commercial operation.
- We set 45/100 because commercial proof exists, but the market is still early in fleet scale, safety certification and general-purpose capability.
sources:
  - claim: Digit has more than 65,000 hours of real-world operation.
    url: https://www.agilityrobotics.com/content/gxo-and-agility-robotics-expand-partnership-to-accelerate-deployment-of-humanoids-in-u-s-operations
    date: 2026-10-26
    quote: "Digit has accumulated more than 65,000 hours of real-world operation."
  - claim: Boston Dynamics began manufacturing production Atlas in 2026.
    url: https://bostondynamics.com/blog/boston-dynamics-unveils-new-atlas-robot-to-revolutionize-industry/
    date: 2026-01-05
    quote: "The company will begin production of the new Atlas robots at its Boston headquarters immediately."
```

### ed018
```yaml
status: ok
section: Market definition
title: How can we categorize companies of the humanoid robotics market?
page: 1/3
note: There are many ways to categorize the field, but these five robot types capture most current company strategies and make the competitive map easier to read.
categories:
- label: 'BIPEDAL

    GENERAL-PURPOSE'
  description: Companies building two-legged humanoids designed to learn and perform many physical tasks
  emoji: 🚶
- label: 'WHEELED + HYBRID

    HUMANOIDS'
  description: Companies using human-like torsos and arms on wheels or mixed locomotion for practical work
  emoji: 🛞
- label: 'LOW-COST + OPEN

    DEVELOPER PLATFORMS'
  description: Companies selling accessible complete humanoids for robotics research, training and software development
  emoji: 🧑‍💻
- label: 'SOCIAL + EXPRESSIVE

    HUMANOIDS'
  description: Companies building human-form robots for interaction, hospitality, guidance or social settings
  emoji: 🗣️
- label: 'HEAVY-DUTY INDUSTRIAL

    SUPERHUMANOIDS'
  description: Companies building stronger human-form machines for demanding industrial manipulation and factory work
  emoji: 🏭
categorization: Here, we categorize by type of robot
sources:
  - claim: Unitree R1 is an open humanoid development platform.
    url: https://www.unitree.com/mobile/R1/
    date: 2026-10-31
    quote: "Fully open control interfaces for joints and sensors"
  - claim: AEON combines a human-like upper body with wheeled mobility.
    url: https://www.bmwgroup.com/en/news/general/2026/humanoid-robot-in-leipzig.html
    date: 2026-10-01
    quote: "enables dynamic use on wheels"
```

### ed019
```yaml
status: ok
section: Market definition
title: How can we categorize companies of the humanoid robotics market?
page: 2/3
note: We also categorize by place of use because factory, warehouse, home and service environments create very different requirements for safety, mobility, dexterity and economics.
t:
  10: 'CAR + ELECTRONICS

    FACTORIES'
  8: Companies automating repetitive handling, sequencing, machine tending and assembly work on production floors
  13: 'WAREHOUSES +

    LOGISTICS'
  11: Companies moving totes, handling goods and automating repetitive material workflows in distribution sites
  25: Here, we categorize by the place where the robot works
  18: 'HOMES +

    ELDER CARE'
  16: Companies building safe, quiet humanoids for chores, assistance and everyday interaction around people
  7: 'RETAIL +

    SERVICES'
  19: Companies using humanoid form for customer-facing assistance, hospitality, guidance and practical service tasks
sources:
  - claim: Figure worked in BMW automotive production.
    url: https://www.figure.ai/news/production-at-bmw
    date: 2025-11-19
    quote: "Contributed to the production of 30,000+ X3 vehicles"
  - claim: Digit is commercially deployed in logistics at GXO.
    url: https://www.agilityrobotics.com/content/gxo-signs-industry-first-multi-year-agreement-with-agility-robotics
    date: 2024-06-27
    quote: "deploying fully operational Digit humanoids into a live warehouse environment"
  - claim: 1X NEO is designed for the home.
    url: https://www.1x.tech/discover/neo-home-robot
    date: 2025-10-28
    quote: "NEO is able to adapt to the world’s most diverse environment: the home."
```

### ed020
```yaml
status: ok
section: Market definition
title: How can we categorize companies of the humanoid robotics market?
page: 3/3
note: A third useful lens is commercial maturity because a robot sold as a developer platform, used in a paid pilot or operating commercially represents a very different business stage.
t:
  10: 'DEVELOPER

    HARDWARE'
  8: Companies shipping complete humanoids mainly for research, software development and embodied-AI training
  13: 'PAID

    PILOTS'
  11: Companies placing robots with enterprises to validate tasks, economics, safety and integration before scale
  25: Here, we categorize by commercial maturity
  18: 'LIVE COMMERCIAL

    DEPLOYMENTS'
  16: Companies with robots performing recurring work under commercial customer agreements in operating facilities
  7: 'CONSUMER

    PREORDERS'
  19: Companies taking orders for home humanoids before broad consumer delivery and fully autonomous capability
sources:
  - claim: Digit is commercially deployed in live operations.
    url: https://www.agilityrobotics.com/content/gxo-and-agility-robotics-expand-partnership-to-accelerate-deployment-of-humanoids-in-u-s-operations
    date: 2026-10-26
    quote: "industry’s first formal commercial deployment of humanoid robots in live operations"
  - claim: NEO has consumer ordering with U.S. deliveries starting in 2026.
    url: https://www.1x.tech/order
    date: 2026-10-01
    quote: "US Deliveries start 2026"
```

### ed021
```yaml
status: ok
section: Market definition
title: What do top companies do in this market?
note: Other companies could also make the top eight. We chose deployment leaders and strategically important platforms to show the range of approaches shaping the market.
t:
  8: FIGURE
  16: APPTRONIK
  7: They deploy Figure 03 at BMW and train Helix for factory and household-style manipulation
  15: They build Apollo and work with Mercedes-Benz and GXO on industrial humanoid applications
  10: AGILITY
  18: 1X
  9: They commercially deploy Digit in logistics and report more than 65,000 operating hours
  17: They build NEO for homes, with $20,000 Early Access ownership and a $499 monthly plan
  12: UNITREE
  20: BOSTON DYNAMICS
  11: They sell lower-cost humanoids including R1 from $4,900 and G1 from $13,500
  19: They manufacture Atlas for industrial work, with 2026 deployments to Hyundai and Google DeepMind
  14: NEURA
  22: HEXAGON
  13: They build 4NE1 Gen 4, a German humanoid being prepared for series production
  21: They build wheeled AEON for industrial work and pilot it at BMW’s Leipzig factory
sources:
  - claim: Figure 03 is operating at BMW.
    url: https://www.figure.ai/news/f-03-at-bmw
    date: 2026-06-30
    quote: "Figure 03 - arrived in Hall 52"
  - claim: Apptronik has a Mercedes-Benz commercial agreement.
    url: https://apptronik.com/news-collection/apptronik-and-mercedes-benz-enter-commercial-agreement
    date: 2024-03-15
    quote: "Apptronik and Mercedes-Benz Enter Commercial Agreement"
  - claim: Digit has more than 65,000 operating hours.
    url: https://www.agilityrobotics.com/content/gxo-and-agility-robotics-expand-partnership-to-accelerate-deployment-of-humanoids-in-u-s-operations
    date: 2026-10-26
    quote: "more than 65,000 hours of real-world operation"
  - claim: 4NE1 Gen 4 is being prepared for series production.
    url: https://neura-robotics.com/products/4ne1/
    date: 2026-10-28
    quote: "being prepared for series production"
  - claim: Atlas deployments are scheduled at Hyundai and Google DeepMind.
    url: https://bostondynamics.com/blog/boston-dynamics-unveils-new-atlas-robot-to-revolutionize-industry/
    date: 2026-01-05
    quote: "fleets scheduled to ship to Hyundai’s Robotics Metaplant Application Center (RMAC) and Google DeepMind"
```

### ed022
```yaml
status: ok
section: Market definition
title: What is rare and that people happily pay for in this market?
note: We looked at operating deployments, customer programs, product disclosures and safety work to identify capabilities that appear genuinely scarce and strategically valuable.
t:
  6: '👐

    Dexterous hands, because useful robots must reliably grasp objects made for people'
  7: '🛡️

    Proven safety, because enterprises need robots that can work near people and equipment'
  8: '🧠

    Generalizable skills, because buyers want one platform to learn more than one fixed task'
  9: '🔁

    Shift reliability, because demos matter less than hours of repeatable daily operation'
  10: '🏭

    Easy integration, because customers want automation without rebuilding every workstation'
  11: '📈

    Real deployment data, because operating fleets create training data that lab demos cannot'
  12: '⚙️

    Scalable production, because customers need repeatable hardware, service and spare parts'
  13: '🧩

    Full-stack control, because hardware, AI, safety and fleet software must work as one system'
sources:
  - claim: Agility reports 65,000+ hours of real-world operation.
    url: https://www.agilityrobotics.com/content/gxo-and-agility-robotics-expand-partnership-to-accelerate-deployment-of-humanoids-in-u-s-operations
    date: 2026-10-26
    quote: "more than 65,000 hours of real-world operation"
  - claim: Figure 02 worked 1,250+ hours at BMW.
    url: https://www.figure.ai/news/production-at-bmw
    date: 2025-11-19
    quote: "1,250+ hours of runtime"
```

### ed023
```yaml
status: ok
section: Market definition
title: Which humanoid robotics truths have flipped?
note: These are directional market shifts identified from recent deployments, product launches and customer agreements. They are not formal industry rules, but they recur across the evidence.
t:
  6: Humanoids used to be mainly impressive research demonstrations
  8: Now some robots work recurring shifts in factories and warehouses
  10: Serious humanoids used to imply very high six-figure hardware
  12: Now complete developer humanoids start below $5,000 from Unitree
  14: Two legs used to define the commercial humanoid idea
  16: Now wheeled human-form robots such as AEON are entering factories
  18: Robot intelligence once meant many separately programmed behaviors
  20: Now one learned model can control walking, hands and whole-body tasks
  22: Early value used to sit in prototypes and technical demonstrations
  24: Now operating hours, paid orders and repeat deployments drive credibility
  26: Humanoids used to look like a distant consumer and factory concept
  28: Now firms are building factories, taking home orders and shipping production hardware
sources:
  - claim: Unitree R1 starts below $5,000.
    url: https://www.unitree.com/mobile/R1/
    date: 2026-10-31
    quote: "Price from $4,900"
  - claim: Figure Helix 02 controls full-body autonomy.
    url: https://www.figure.ai/news/helix-02
    date: 2026-01-27
    quote: "extends that control to the entire robot"
  - claim: Agility has commercial operations and more than 65,000 hours.
    url: https://www.agilityrobotics.com/content/gxo-and-agility-robotics-expand-partnership-to-accelerate-deployment-of-humanoids-in-u-s-operations
    date: 2026-10-26
    quote: "more than 65,000 hours of real-world operation"
```

### ed024
```yaml
status: ok
section: Market definition
title: What has changed (very) recently?
page: 1/2
items:
- d: SINCE 2024
  t: GXO and Agility signed the first formal commercial humanoid deployment and first humanoid Robots-as-a-Service agreement, putting Digit into regular warehouse operations.
- d: SINCE 2025
  t: Figure 02 ran ten-hour weekday shifts at BMW, loaded more than 90,000 parts and contributed to production of more than 30,000 X3 vehicles.
- d: SINCE 2025
  t: Figure raised more than $1B in a Series C at a $39B post-money valuation, showing how much investor capital was moving toward general-purpose humanoids.
- d: SINCE 2025
  t: Hexagon launched AEON, a wheeled industrial humanoid, with Schaeffler and Pilatus named as pilot customers across industrial use cases.
- d: SINCE 2025
  t: 1X opened NEO home-robot orders at $20,000 for Early Access ownership, with a $499 monthly subscription planned for later delivery.
- d: SINCE 2026
  t: Boston Dynamics unveiled the production Atlas and began manufacturing, with 2026 fleets committed to Hyundai and Google DeepMind.
note:
- We kept milestones that most changed commercial credibility, customer adoption, pricing or the set of serious competitors
- There is no official timeline, and another analyst could reasonably pick a few different milestones here
sources:
  - claim: GXO and Agility signed the first formal commercial humanoid deployment.
    url: https://www.agilityrobotics.com/content/gxo-signs-industry-first-multi-year-agreement-with-agility-robotics
    date: 2024-06-27
    quote: "industry’s first formal commercial deployment of humanoid robots"
  - claim: Figure 02 supported more than 30,000 BMW vehicles.
    url: https://www.figure.ai/news/production-at-bmw
    date: 2025-11-19
    quote: "Contributed to the production of 30,000+ X3 vehicles"
  - claim: Figure raised more than $1B at a $39B post-money valuation.
    url: https://www.figure.ai/news
    date: 2025-09-16
    quote: "Figure Exceeds $1B in Series C Funding at $39B Post-Money Valuation"
  - claim: Hexagon launched AEON with Schaeffler and Pilatus pilots.
    url: https://hexagon.com/about/news-media/press-releases/2340225/hexagon-launches-aeon-a-humanoid-built-for-industry
    date: 2025-06-17
    quote: "Schaeffler and Pilatus will pilot the humanoid"
  - claim: NEO Early Access costs $20,000.
    url: https://www.1x.tech/order
    date: 2026-10-01
    quote: "$20,000 Ownership"
  - claim: Boston Dynamics began Atlas production in 2026.
    url: https://bostondynamics.com/blog/boston-dynamics-unveils-new-atlas-robot-to-revolutionize-industry/
    date: 2026-01-05
    quote: "The company will begin production of the new Atlas robots"
```

### ed025
```yaml
status: ok
section: Market definition
title: What has changed (very) recently?
page: 2/2
items:
- d: SINCE 2026
  t: Figure returned to BMW with Figure 03 and moved from sheet-metal loading toward parts sequencing, a workflow requiring perception, dexterity and movement together.
- d: SINCE 2026
  t: Apptronik expanded its Series A to more than $935M, backed by Google, Mercedes-Benz, John Deere and others to scale Apollo production and deployment.
- d: SINCE 2026
  t: BMW advanced Hexagon’s AEON at Leipzig from testing toward production tasks in battery assembly and component manufacturing.
- d: SINCE 2026
  t: Agility reported more than 65,000 real-world operating hours and expanded GXO deployments to two additional U.S. facilities planned for 2027.
- d: SINCE 2026
  t: Agility completed its public-market transaction and reported more than $300M in committed multi-year Digit 5 orders, subject to contractual milestones.
- d: SINCE 2026
  t: China published a national general technical standard for humanoid robots and continued government programs aimed at real-world deployment and scale.
note:
- We kept milestones that most changed commercial credibility, customer adoption, financing or the institutional structure around the market
- There is no official timeline, and another analyst could reasonably pick a few different milestones here
sources:
  - claim: Figure 03 returned to BMW for sequencing.
    url: https://www.figure.ai/news/f-03-at-bmw
    date: 2026-06-30
    quote: "Figure has transitioned from classic pick-and-place sheet metal loading to an entirely new tier of complexity"
  - claim: Apptronik raised more than $935M in its Series A.
    url: https://apptronik.com/news-collection/apptronik-closes-over-935-million-series-a
    date: 2026-02-11
    quote: "bringing Apptronik’s total Series A to more than $935 million"
  - claim: Digit has more than 65,000 operating hours.
    url: https://www.agilityrobotics.com/content/gxo-and-agility-robotics-expand-partnership-to-accelerate-deployment-of-humanoids-in-u-s-operations
    date: 2026-10-26
    quote: "more than 65,000 hours of real-world operation"
  - claim: Agility reported more than $300M in committed multi-year Digit 5 orders.
    url: https://investors.agilityrobotics.com/news-releases/news-release-details/agility-robotics-and-churchill-capital-corp-xi-complete-business
    date: 2026-11-04
    quote: "more than $300 million in committed multi-year orders for Digit 5"
  - claim: China published a general technical requirements standard for humanoid robots.
    url: https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=32AB881AF970A02B4DE3DFC4984EFD52
    date: 2026-09-28
    quote: "Technical requirements for humanoid robots—Part 1：General"
  - claim: China launched a 2026 real-world training initiative for humanoid robots and embodied intelligence.
    url: https://www.miit.gov.cn/jgsj/kjs/wjfb/art/2026/art_cd666691abf8471fb8553d463aa416e3.html
    date: 2026-06-08
    quote: "推动人形机器人与具身智能产品在真实生产生活环境中常态化部署应用"
```
