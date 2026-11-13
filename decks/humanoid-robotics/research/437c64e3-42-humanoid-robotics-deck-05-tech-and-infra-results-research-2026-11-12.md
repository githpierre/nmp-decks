### ed087
```yaml
status: ok
section: Tech and infra
title: What are the tech and infra layers?
page: 1/2
t:
  7: BODY
  10: Frames, joints and actuators turn motor commands into stable whole-body movement
  9: SENSORS
  11: Cameras, touch and joint sensors tell the robot what surrounds it and how it is moving
  21: LAYERS
  12: COMPUTE
  14: Onboard computers run perception, planning and control with low enough delay for motion
  13: HANDS
  15: Dexterous hands and grippers determine how reliably robots can grasp and manipulate objects
note: We group the stack from physical hardware through sensing and onboard compute, using current product architectures from leading humanoid platforms.
sources:
  - claim: Humanoid platforms combine body hardware, sensing, onboard compute and dexterous manipulation.
    url: https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-NVIDIA-Isaac-GR00T-Reference-Humanoid-Robot-for-Academic-Research/
    date: 2026-06-01
    quote: "The reference design features a Unitree H2 humanoid chassis, Sharpa five-fingered hands and NVIDIA Jetson AGX Thor onboard compute."
  - claim: Figure 03 adds tactile sensing and palm cameras for manipulation.
    url: https://www.figure.ai/news/helix-02
    date: 2026-01-27
    quote: "Figure 03’s embedded tactile sensing and palm cameras enable manipulation that was previously out of reach."
```

### ed088
```yaml
status: ok
section: Tech and infra
title: What are the tech and infra layers?
page: 2/2
t:
  7: DATA
  10: Human demonstrations, robot logs and synthetic scenes teach models how tasks should unfold
  9: ROBOT AI
  11: Vision-language-action models turn instructions and sensor inputs into robot actions
  21: LAYERS
  12: SIM
  14: Simulation creates training data and tests policies before expensive real-world runs
  13: FLEETS
  15: Fleet software connects robots to workflows, monitors performance and ships learned skills
note: We treat data, robot models, simulation and fleet software as the software infrastructure that turns hardware into a deployable system.
sources:
  - claim: GR00T uses human video, real robot teleoperation and synthetic data.
    url: https://developer.nvidia.com/blog/accelerate-generalist-humanoid-robot-development-with-nvidia-isaac-gr00t-n1/
    date: 2025-03-18
    quote: "The training data forms a pyramid of web data, synthetic data and real robot teleoperation data."
  - claim: GR00T spans simulation, training, evaluation and deployment.
    url: https://developer.nvidia.com/isaac/gr00t
    date: n.d.
    quote: "It comprises open data and data pipelines, an open robot foundation model, simulation frameworks, middleware and NVIDIA Jetson Thor."
  - claim: Atlas fleet software connects to enterprise systems and distributes skills.
    url: https://bostondynamics.com/products/atlas
    date: n.d.
    quote: "Orbit is your single source of truth to connect Atlas to MES, WMS, and other systems of record."
```

### ed089
```yaml
status: ok
section: Tech and infra
title: Does every layer carry the same weight?
note: We ranked the layers directionally from current deployment evidence and product roadmaps, not from a standardized industry score.
t:
  38: RANKING
  6: ROBOT AI
  14: Determines whether one robot can understand tasks, recover from variation and generalize
  7: HANDS
  24: Reliable grasping still decides whether useful work survives contact with messy objects
  8: DATA
  26: More diverse demonstrations improve task coverage, but data still needs capable hardware
  9: BODY
  28: Actuators and mechanics set speed, payload, uptime and the physical envelope of work
  10: SENSORS
  30: Vision and touch reduce uncertainty, especially when hands hide objects from cameras
  11: COMPUTE
  32: Low-latency onboard inference keeps perception and motion control responsive
  12: SIM
  34: Simulation scales training and testing, but real environments still expose the final gaps
  13: FLEETS
  36: Fleet tools matter most after robots can perform useful tasks reliably enough to scale
note: We ranked the layers directionally from current deployment evidence and product roadmaps, not from a standardized industry score.
sources:
  - claim: Figure unified full-body AI across vision, touch and proprioception in Helix 02.
    url: https://www.figure.ai/news/helix-02
    date: 2026-01-27
    quote: "Helix 02 connects every onboard sensor directly to every actuator through a single unified visuomotor neural network."
  - claim: GR00T 2 improves adaptation by scaling human, teleoperation and robot data.
    url: https://research.nvidia.com/labs/gear/gr00t-2/
    date: 2026-11
    quote: "GR00T 2 is pretrained on one mixture of three kinds of data."
  - claim: Figure reported hardware failures and reliability lessons from 1,250 hours at BMW.
    url: https://www.figure.ai/news/production-at-bmw
    date: 2025-11-19
    quote: "Six months of daily runtime yielded invaluable insights for our mechanical and reliability teams."
```

### ed090
```yaml
status: ok
section: Tech and infra
title: Where does 80% of humanoid robotics value sit?
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
  8: 'Most value today sits in robot intelligence, dexterous manipulation and reliable whole-body hardware, because useful work requires all three to hold up together.

    Data and simulation come next, since broader demonstrations and synthetic worlds can expand skills faster than collecting every task on real robots.

    Winners will combine generalizable models with dependable hands, safe motion, long uptime and fleet software that turns one learned task into repeatable operations.'
note: We treat robot intelligence, manipulation and reliable hardware as the main bottlenecks because current factory deployments still expose failures in those layers.
sources:
  - claim: Figure 02 deployment exposed mechanical and reliability failure points.
    url: https://www.figure.ai/news/production-at-bmw
    date: 2025-11-19
    quote: "Figure 02 recorded minimal hardware failures while generating critical data that informed the mechanical design of Figure 03."
  - claim: GR00T 2 showed broad skill transfer from human and robot data.
    url: https://research.nvidia.com/labs/gear/gr00t-2/
    date: 2026-11
    quote: "A skill shown on one embodiment, or only in human video, carries over to a robot that has never practiced it."
```

### ed091
```yaml
status: ok
section: Tech and infra
title: How has tech and infra evolved over the years?
t:
  6: '2013 - 2020

    Humanoids proved dynamic balance, walking and whole-body control in research, but remained expensive machines built mainly for laboratories'
  7: '2021 - 2023

    New startups shifted toward general-purpose workers, combining electric actuation, cameras, AI compute and human-scale designs'
  8: '2024 - 2025

    Figure and Agility put humanoids into live BMW and GXO workflows, while robot foundation models and simulation stacks matured'
  9: 'TODAY

    Production-ready Atlas, Figure 03, Walker S2 and Optimus move the field toward fleets, stronger hands, self-charging and factory-scale builds'
  10: '?

    Next platforms may learn from human video, transfer skills across robot bodies and operate longer with less task-specific programming'
note: We use product and deployment milestones rather than invention dates because they show when enabling technology became usable in real operations.
sources:
  - claim: Boston Dynamics moved Atlas from research toward a production-ready industrial humanoid.
    url: https://bostondynamics.com/blog/atlas-evolution-from-research-robot-to-industrial-humanoid/
    date: 2026
    quote: "In January 2026, Boston Dynamics and Hyundai Motor Group unveiled the production-ready Atlas."
  - claim: Figure 02 ran on BMW's assembly line in 2025.
    url: https://www.figure.ai/news/production-at-bmw
    date: 2025-11-19
    quote: "We launched full deployment on an active assembly line at the plant, running every single working day."
  - claim: Agility and GXO signed a multi-year commercial Digit deployment agreement in 2024.
    url: https://www.agilityrobotics.com/content/gxo-signs-industry-first-multi-year-agreement-with-agility-robotics
    date: 2024-06-27
    quote: "They have signed a multi-year agreement to begin deploying Digit in GXO’s logistics operations."
  - claim: GR00T 2 transfers skills from human video and other robot embodiments.
    url: https://research.nvidia.com/labs/gear/gr00t-2/
    date: 2026-11
    quote: "Skills shown only by humans, or with handheld and wearable devices, carry over to robots that never practiced them."
```

### ed092
```yaml
status: ok
section: Tech and infra
title: What were the latest tech and infra developments?
page: 1/2
t:
  13: '2025'
  14: NVIDIA released GR00T N1, combining web, synthetic and teleoperation data in an open humanoid foundation model
  15: '2025'
  16: Figure 03 added tactile fingertips, palm cameras and wireless charging while redesigning hardware for mass manufacturing
  17: '2025'
  18: Figure 02 completed daily BMW production work, moving 90,000+ parts across more than 1,250 operating hours
  19: '2025'
  20: UBTECH launched Walker S2 with autonomous three-minute battery swaps for near-continuous industrial operation
  21: '2026'
  22: Boston Dynamics launched production-ready Atlas with self-swapping batteries and enterprise workflow integration
  23: '2026'
  24: Figure Helix 02 unified walking, manipulation and balance under one neural system using vision, touch and proprioception
note: We prioritized technology milestones with clear consequences for autonomy, dexterity, uptime, manufacturing or real production use.
sources:
  - claim: NVIDIA released Isaac GR00T N1 in March 2025.
    url: https://nvidianews.nvidia.com/news/nvidia-isaac-gr00t-n1-open-humanoid-robot-foundation-model-simulation-frameworks
    date: 2025-03-18
    quote: "NVIDIA today announced NVIDIA Isaac GR00T N1, the world’s first open, fully customizable foundation model."
  - claim: Figure 03 was redesigned for tactile sensing, charging and high-volume manufacturing.
    url: https://www.figure.ai/news/introducing-figure-03
    date: 2025-10-09
    quote: "Figure 03 features a completely redesigned sensory suite and hand system."
  - claim: Figure 02 moved more than 90,000 parts over 1,250+ runtime hours at BMW.
    url: https://www.figure.ai/news/production-at-bmw
    date: 2025-11-19
    quote: "90,000+ parts loaded; 1,250+ hours of runtime."
  - claim: Walker S2 can autonomously swap a battery within three minutes.
    url: https://www.ubtrobot.com/en/humanoid/products/walker-s2
    date: 2025
    quote: "Walker S2 is able to swap battery autonomously within 3 minutes."
  - claim: Product Atlas has self-swapping batteries and enterprise workflow integration.
    url: https://bostondynamics.com/products/atlas
    date: 2026
    quote: "Atlas autonomously navigates to a charging station and swaps out its own battery."
  - claim: Helix 02 controls walking, manipulation and balance as one continuous system.
    url: https://www.figure.ai/news/helix-02
    date: 2026-01-27
    quote: "Helix 02 extends that control to the entire robot: walking, manipulating, and balancing as one continuous system."
```

### ed093
```yaml
status: ok
section: Tech and infra
title: What were the latest tech and infra developments?
page: 2/2
t:
  13: '2026'
  14: NVIDIA shipped Jetson Thor-based reference hardware pairing a Unitree humanoid with tactile five-finger hands and open software
  15: '2026'
  16: BMW began a Leipzig pilot of Agile Robots' wheeled AEON for battery assembly and component manufacturing
  17: '2026'
  18: Boston Dynamics opened Hyundai's RMAC with Atlas training on real automotive parts sequencing workflows
  19: '2026'
  20: Figure 03 returned to BMW for a harder sequencing workflow that combines cart pulling, walking and part manipulation
  21: '2026'
  22: Tesla reported Optimus production had begun on high-volume Fremont lines, moving the program into an early manufacturing ramp
  23: '2026'
  24: NVIDIA introduced GR00T 2, using 402,730 hours of human video plus robot data to transfer skills across embodiments
note: We used primary company and customer releases to capture the most consequential 2026 hardware, deployment and robot-AI milestones.
sources:
  - claim: NVIDIA announced a Jetson Thor humanoid reference robot with Unitree H2 and Sharpa hands.
    url: https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-NVIDIA-Isaac-GR00T-Reference-Humanoid-Robot-for-Academic-Research/
    date: 2026-06-01
    quote: "The reference design combines a Unitree H2 Plus humanoid robot, Sharpa five-fingered hands and NVIDIA Jetson Thor."
  - claim: BMW's Leipzig AEON deployment covers high-voltage battery assembly and component manufacturing.
    url: https://newsroom.bmwgroup.com/global/bmw-group-to-deploy-humanoid-robots-in-production-in-germany-for-the-first-time/
    date: 2026-02-27
    quote: "The robot will be used in the assembly of high-voltage batteries and in component manufacturing."
  - claim: Atlas robots are training at Hyundai's RMAC on parts sequencing.
    url: https://bostondynamics.com/news/boston-dynamics-opens-robotics-metaplant-application-center-to-train-humanoid-robots-for-manufacturing-tasks/
    date: 2026-09-21
    quote: "The robots are being trained in real-world environments, such as preparing the logistics and sequencing of automotive parts."
  - claim: Figure 03 returned to BMW for a sequencing workflow.
    url: https://www.figure.ai/news/f-03-at-bmw
    date: 2026-06-30
    quote: "Figure has transitioned from classic pick-and-place sheet metal loading to an entirely new tier of complexity: the sequencing use case."
  - claim: Tesla reported Optimus production began in Fremont on high-volume lines.
    url: https://assets-ir.tesla.com/tesla-contents/IR/TSLA-Q3-2026-Update.pdf
    date: 2026-10-21
    quote: "Optimus production began in Fremont on our high-volume lines."
  - claim: GR00T 2 uses 402,730 hours of egocentric human video.
    url: https://research.nvidia.com/labs/gear/gr00t-2/
    date: 2026-11
    quote: "GR00T 2 is pretrained on 402,730 hours of egocentric video of people at work."
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
  7: 'HAND

    DEXTERITY'
  5: Hands still miss small, slippery or occluded objects, so manipulation needs better touch and control
  24: 'HARDWARE

    UPTIME'
  22: Motors, cables and joints must survive long shifts without frequent resets or repair
  11: 'TASK

    DATA'
  9: Robots need far more varied demonstrations to cover the long tail of real workplace tasks
  28: 'BATTERY

    UPTIME'
  26: Short runtimes interrupt work unless charging or battery swaps fit the operating cycle
  15: 'GENERAL

    SKILLS'
  13: Policies still fail when objects, layouts or task sequences differ from training
  32: 'SAFE

    MOTION'
  30: Humanoids must detect people, limit forces and recover safely from errors or falls
  19: 'CYCLE

    SPEED'
  17: Robots must match production takt time while keeping grasping and placement reliable
  36: 'FLEET

    SCALE'
  34: Skills, maintenance and monitoring must work across many robots, sites and workflows
note: We selected bottlenecks that are repeatedly visible in current deployments and product designs and are technically addressable rather than fundamental limits.
sources:
  - claim: Figure added tactile sensing and palm cameras to address difficult manipulation.
    url: https://www.figure.ai/news/helix-02
    date: 2026-01-27
    quote: "Palm cameras provide in-hand visual feedback when objects are occluded from the head camera."
  - claim: Figure identified forearm hardware as its top failure point at BMW.
    url: https://www.figure.ai/news/production-at-bmw
    date: 2025-11-19
    quote: "One learning that informed Figure 03 design was the robot’s forearm, our top hardware failure point at BMW."
  - claim: Atlas battery life is four hours and it can autonomously swap batteries.
    url: https://bostondynamics.com/products/atlas
    date: 2026
    quote: "Battery Life 4 hours."
  - claim: GR00T 2 reports execution precision as a major remaining source of misses.
    url: https://research.nvidia.com/labs/gear/gr00t-2/
    date: 2026-11
    quote: "Most misses come from execution, not intent: GR00T 2 does the right steps in the right order."
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
  7: 'HAND

    DEXTERITY'
  5: Fine contact combines vision, touch, force control and mechanics at tight tolerances
  24: 'HARDWARE

    UPTIME'
  22: Humanoids pack many moving joints, cables and electronics into a compact body
  11: 'TASK

    DATA'
  9: Real robot data is slow and costly, while simulation still differs from the physical world
  28: 'BATTERY

    UPTIME'
  26: Higher energy capacity adds mass, while charging downtime cuts useful working time
  15: 'GENERAL

    SKILLS'
  13: Small physical changes can break policies that looked robust in familiar settings
  32: 'SAFE

    MOTION'
  30: Fast, powerful robots share space with people, so failures must remain bounded
  19: 'CYCLE

    SPEED'
  17: Faster motion leaves less time for perception, correction and stable manipulation
  36: 'FLEET

    SCALE'
  34: Sites differ in layout, IT, safety rules and maintenance, limiting simple replication
note: We tied each reason to current robot architectures and deployment evidence rather than assuming one software or hardware upgrade solves the full problem.
sources:
  - claim: NVIDIA describes a remaining simulation-to-reality gap.
    url: https://developer.nvidia.com/blog/accelerate-generalist-humanoid-robot-development-with-nvidia-isaac-gr00t-n1/
    date: 2025-03-18
    quote: "Simulation data fills this gap with infinite, real-time data, though it faces a simulation-to-reality gap."
  - claim: Figure's BMW work showed tight mechanical packaging, dexterity and thermal constraints in the forearm.
    url: https://www.figure.ai/news/production-at-bmw
    date: 2025-11-19
    quote: "The forearm is a challenging subsystem due to its tight packaging, dexterity requirements and thermal constraints."
  - claim: BMW needed revised safety concepts and improved 5G coverage for deployment.
    url: https://www.bmwgroup.com/en/news/general/2026/humanoid-robot-in-leipzig.html
    date: 2026-10
    quote: "The pilot project also delivered important insights including revised safety concepts and improved 5G coverage in the hall."
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
  7: 'HAND

    DEXTERITY'
  5: Touch, palm vision and five-finger control are improving fast, but reliability needs years of field data
  24: 'HARDWARE

    UPTIME'
  22: Factory pilots already expose weak components, but proving multi-shift durability takes larger fleets
  42: '2029'
  46: '2030'
  11: 'TASK

    DATA'
  9: Human video and simulation scale coverage quickly, but hard physical tasks still need robot demonstrations
  28: 'BATTERY

    UPTIME'
  26: Self-swapping batteries already work, so infrastructure can solve uptime before chemistry changes
  43: '2029'
  47: '2028'
  15: 'GENERAL

    SKILLS'
  13: Foundation models are generalizing faster, but robust transfer across sites remains unproven
  32: 'SAFE

    MOTION'
  30: Safety hardware is shipping now, but standards and operating evidence must mature with deployments
  44: '2031'
  48: '2030'
  19: 'CYCLE

    SPEED'
  17: BMW-scale work proves useful pace is possible, but broader tasks still trade speed for reliability
  36: 'FLEET

    SCALE'
  34: Multi-site fleet expansion has started, but repeatable integration and service need more operating history
  45: '2029'
  49: '2030'
note: These are directional estimates based on current field progress, not consensus forecasts; some bottlenecks will improve gradually rather than disappear in one year.
sources:
  - claim: Figure 03 uses tactile sensing and palm cameras for dexterity.
    url: https://www.figure.ai/news/helix-02
    date: 2026-01-27
    quote: "Tactile sensors embedded in each fingertip detect forces as small as three grams."
  - claim: Walker S2 already performs autonomous three-minute battery swaps.
    url: https://www.ubtrobot.com/en/humanoid/products/walker-s2
    date: 2025
    quote: "Walker S2 is able to swap battery autonomously within 3 minutes."
  - claim: GXO and Agility announced expansion to additional sites for 2027.
    url: https://www.agilityrobotics.com/content/gxo-and-agility-robotics-expand-partnership-to-accelerate-deployment-of-humanoids-in-u-s-operations
    date: 2026-10-26
    quote: "Digit humanoid robots to expand to additional GXO sites in 2027."
```

### ed097
```yaml
status: ok
section: Tech and infra
title: Which bold bets could reshape humanoid robotics?
t:
  9: GENERALIST BRAIN
  12: HUMAN-VIDEO LEARNING
  15: SELF-CHARGING FLEET
  18: TACTILE HANDS
  33: 'NEAR-TERM HORIZON

    (0-5 YEARS)'
  7: It is one policy that learns many factory and home tasks instead of one program per workflow
  10: It is robots learning physical skills from ordinary human video without collecting every task on robots
  13: It is fleets that recharge or swap batteries automatically and keep working across long shifts
  16: It is touch-aware five-finger hands that handle small, soft and partly hidden objects reliably
  21: CROSS-ROBOT SKILLS
  24: LIGHTER ACTUATION
  27: AUTONOMOUS HOMES
  30: ROBOT FACTORIES
  34: 'LONG-TERM HORIZON

    (5-10 YEARS)'
  19: It is one learned skill transferring across different humanoid bodies with little retraining
  22: It is quieter, safer actuation that cuts weight and power while preserving human-level force
  25: It is one home humanoid that handles changing chores without remote help for routine tasks
  28: It is highly automated production where humanoids help build, test and maintain other humanoids
note: We grounded the bets in current directions already visible in GR00T 2, Helix 02, autonomous charging, consumer humanoids and robot manufacturing pilots.
sources:
  - claim: GR00T 2 transfers skills from human video and across robot embodiments.
    url: https://research.nvidia.com/labs/gear/gr00t-2/
    date: 2026-11
    quote: "Skills shown only by humans carry over to robots that never practiced them."
  - claim: Helix 02 combines full-body autonomy with tactile manipulation.
    url: https://www.figure.ai/news/helix-02
    date: 2026-01-27
    quote: "Helix 02 extends that control to the entire robot: walking, manipulating, and balancing as one continuous system."
  - claim: Atlas can autonomously swap batteries and resume work.
    url: https://bostondynamics.com/products/atlas
    date: 2026
    quote: "Atlas autonomously navigates to a charging station and swaps out its own battery."
  - claim: Jabil and Apptronik are testing Apollo in the factories that will build Apollo.
    url: https://www.jabil.com/news/apptronik-jabil-collaborate.html
    date: 2025-02-25
    quote: "This includes the production lines that will build Apollo humanoid robots."
```

### ed098
```yaml
status: ok
section: Tech and infra
title: Which companies are working on groundbreaking tech today?
t:
  8: FIGURE
  6: They unify walking and dexterous manipulation with Helix 02 and tactile Figure 03 hands
  24: BOSTON DYNAMICS
  22: They built Atlas for industrial fleets with 360° sensing, tactile hands and self-swapping batteries
  11: 1X
  9: They use tendon-driven actuation, a soft body and 22-DoF hands for a consumer home humanoid
  27: UBTECH
  25: They built Walker S2 to autonomously swap batteries and coordinate factory tasks across fleets
  14: AGILITY
  12: They operate Digit in live logistics workflows and use field data to improve the platform
  30: UNITREE
  28: They offer full-size H2 hardware with 31 DoF, high joint torque and onboard AI compute
  17: APPTRONIK
  15: They designed Apollo for manufacturability and are validating robots inside Jabil factories
  33: TESLA
  31: They started Optimus production on high-volume lines while developing vision-based autonomy
note: We selected companies with distinct technical approaches and concrete 2025-2026 product, deployment or manufacturing evidence.
sources:
  - claim: Figure Helix 02 controls the full body and uses tactile hands.
    url: https://www.figure.ai/news/helix-02
    date: 2026-01-27
    quote: "Helix 02 connects every onboard sensor directly to every actuator."
  - claim: Atlas includes tactile sensing and self-swapping batteries.
    url: https://bostondynamics.com/products/atlas
    date: 2026
    quote: "Sensing Tactile and 360° camera view."
  - claim: 1X NEO uses tendon drive and 22-DoF hands.
    url: https://www.1x.tech/discover/neo-home-robot
    date: 2025-10-28
    quote: "NEO is built with 1X’s patented Tendon Drive."
  - claim: Walker S2 supports autonomous battery swapping.
    url: https://www.ubtrobot.com/en/humanoid/products/walker-s2
    date: 2025
    quote: "The World's First Humanoid Robot Capable of Autonomous Battery Swapping."
  - claim: Digit operates in live GXO workflows.
    url: https://www.agilityrobotics.com/content/gxo-and-agility-robotics-expand-partnership-to-accelerate-deployment-of-humanoids-in-u-s-operations
    date: 2026-10-26
    quote: "Digit has worked alongside existing automation to move totes and place them onto conveyors."
  - claim: Unitree H2 has 31 DoF and 360 N.m joint torque.
    url: https://shop.unitree.com/collections/humanoid-robot/products/unitree-h2
    date: 2026
    quote: "31 degrees of freedom, 360N.m joint torque, and precise dynamic movement replication."
  - claim: Apptronik and Jabil are manufacturing and validating Apollo.
    url: https://www.jabil.com/news/apptronik-jabil-collaborate.html
    date: 2025-02-25
    quote: "Newly manufactured Apollo units will leverage Jabil’s factory environment for real-world validation testing."
  - claim: Tesla started Optimus production in Fremont.
    url: https://assets-ir.tesla.com/tesla-contents/IR/TSLA-Q3-2026-Update.pdf
    date: 2026-10-21
    quote: "Optimus production began in Fremont on our high-volume lines."
logos:
  - Figure: figure.ai
  - Boston Dynamics: bostondynamics.com
  - 1X: 1x.tech
  - UBTECH Robotics: ubtrobot.com
  - Agility Robotics: agilityrobotics.com
  - Unitree Robotics: unitree.com
  - Apptronik: apptronik.com
  - Tesla: tesla.com
```

### iv_pipeline
```yaml
status: ok
section: Tech and infra
title: Where are humanoid robots actually at work today?
note: We list eight representative customer-site deployments or paid pilots with reported on-site work; stages reflect disclosed commercial status rather than technical maturity.
t:
  38: FLEET
  34: Tote handling at GXO Flowery Branch warehouse
  37: AGILITY · DIGIT
  27: PILOT
  26: FIGURE · FIGURE 03
  24: Parts sequencing at BMW Spartanburg
  23: PILOT
  22: AGILE · AEON
  20: Battery assembly and component work at BMW Leipzig
  19: PILOT
  18: BOSTON DYNAMICS · ATLAS
  16: Automotive parts sequencing training at Hyundai RMAC
  15: PILOT
  12: Material handling at Schaeffler factories
  14: AGILITY · DIGIT
  11: PILOT
  10: APPTRONIK · APOLLO
  8: Repetitive manufacturing validation inside Jabil factories
  7: PILOT
  6: APPTRONIK · APOLLO
  4: Warehouse proof-of-concept work at GXO distribution operations
  3: PILOT
  2: APPTRONIK · APOLLO
  0: Low-skill physical manufacturing tasks at Mercedes-Benz plants
sources:
  - claim: Digit is in a formal commercial deployment at GXO moving totes to conveyors.
    url: https://www.agilityrobotics.com/content/gxo-and-agility-robotics-expand-partnership-to-accelerate-deployment-of-humanoids-in-u-s-operations
    date: 2026-10-26
    quote: "Digit has worked alongside existing automation to move totes and place them onto conveyors."
  - claim: Figure 03 is at BMW Spartanburg for a sequencing workflow.
    url: https://www.figure.ai/news/f-03-at-bmw
    date: 2026-06-30
    quote: "Figure 03 arrived in Hall 52, one of the assembly and logistics halls at BMW Group Plant Spartanburg."
  - claim: AEON is used at BMW Leipzig for battery assembly and component manufacturing.
    url: https://newsroom.bmwgroup.com/global/bmw-group-to-deploy-humanoid-robots-in-production-in-germany-for-the-first-time/
    date: 2026-02-27
    quote: "The robot will be used in the assembly of high-voltage batteries and in component manufacturing."
  - claim: Atlas is training at Hyundai RMAC on automotive parts sequencing.
    url: https://bostondynamics.com/news/boston-dynamics-opens-robotics-metaplant-application-center-to-train-humanoid-robots-for-manufacturing-tasks/
    date: 2026-09-21
    quote: "The robots are being trained in real-world environments, such as preparing the logistics and sequencing of automotive parts."
  - claim: Digit has been deployed at Schaeffler facilities for material handling and logistics.
    url: https://www.sec.gov/Archives/edgar/data/2074973/000121390026118037/ea0311221-s1_agility.htm
    date: 2026-11-10
    quote: "At Schaeffler, Digit v4 has been deployed across multiple facilities supporting material handling and logistics workflows."
  - claim: Apollo units are being validated inside Jabil factories on repetitive manufacturing tasks.
    url: https://www.jabil.com/news/apptronik-jabil-collaborate.html
    date: 2025-02-25
    quote: "Newly manufactured Apollo units will leverage Jabil’s factory environment for real-world validation testing."
  - claim: GXO conducted an Apollo warehouse proof of concept.
    url: https://investors.gxo.com/news-releases/news-release-details/gxo-advances-humanoid-strategy-announces-multi-phase-rd/
    date: 2024-06-20
    quote: "GXO announced it is conducting an early-stage proof-of-concept program in partnership with robot manufacturer Apptronik."
  - claim: Mercedes-Benz entered a commercial agreement to pilot Apollo in manufacturing facilities.
    url: https://apptronik.com/news-collection/apptronik-and-mercedes-benz-enter-commercial-agreement
    date: 2024-03-15
    quote: "The partnership represents Apptronik’s first publicly announced commercial deployment of Apollo."
logos:
  - Agility Robotics: agilityrobotics.com
  - Figure: figure.ai
  - Agile Robots: agile-robots.com
  - Boston Dynamics: bostondynamics.com
  - Apptronik: apptronik.com
```
