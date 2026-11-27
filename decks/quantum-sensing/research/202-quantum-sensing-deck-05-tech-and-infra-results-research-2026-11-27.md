# Quantum sensing, deck 05, Tech and infra (research results, 27 November 2026)

### ed087
```yaml
status: ok
section: Tech and infra
title: What are the tech and infra layers?
page: 1/2
t:
  7: "ATOMS"
  10: "Cooled atoms or atom vapor sealed in small glass cells do the actual measuring"
  9: "DIAMOND"
  11: "Tiny flaws in man-made diamond sense magnetic fields at room temperature"
  21: "LAYERS"
  12: "LASERS"
  14: "Stable lasers cool, trap and read the atoms, and are the most finicky part"
  13: "CONTROL"
  15: "Software and electronics cancel noise so sensors keep working on the move"
sources:
  - claim: Rydberg receivers use lasers, optics and a glass vapor cell of atoms
    url: https://electronics360.globalspec.com/article/23364/receivers-go-quantum-through-the-power-of-rydberg-atoms
    date: "2026-02-14"
    quote: "It requires multiple sets of lasers, precise optical equipment such as mirrors and lenses, a glass vapor cell"
  - claim: NV-diamond magnetometers use defects in synthetic diamond and work at room temperature
    url: https://hiqute-diamond.com/insights/nv-diamond-for-quantum-sensing-and-magnetometry
    date: "2026-05-11"
    quote: "Engineered NV-doped diamond for room-temperature quantum magnetometers."
  - claim: Lasers are the most finicky part of an atomic clock
    url: https://physicsworld.com/?p=114254
    date: "2024"
    quote: "The most finicky parts of any atomic-clock system, Roslund explains, are the lasers"
  - claim: Q-CTRL uses AI-powered control software to shield quantum sensors from interference
    url: https://insidegnss.com/?p=194952
    date: "2025-04"
    quote: "This concept uses proprietary AI-powered quantum control software to shield the delicate quantum sensors against interference encountered"
```

### ed088
```yaml
status: ok
section: Tech and infra
title: What are the tech and infra layers?
page: 2/2
t:
  7: "CHIPS"
  10: "Photonic chips and tiny vapor cells shrink sensors from racks to palm-sized units"
  9: "MAPS"
  11: "Gravity and magnetic maps let a sensor match readings and find its position"
  21: "LAYERS"
  12: "FUSION"
  14: "Software blends quantum readings with today's inertial systems and GPS"
  13: "TESTING"
  15: "Field trials and flight safety tests prove a sensor works outside the lab"
sources:
  - claim: Mesa Quantum builds chip-scale quantum sensors and scaled vapor cell production
    url: https://quantumcomputingreport.com/mesa-quantum-raises-11-8m-to-scale-chip-scale-quantum-sensors-and-alternative-pnt-infrastructure/amp/
    date: "2026-09-24"
    quote: "Scaled vapor cell production infrastructure"
  - claim: Q-CTRL's navigator matches measured gravity against gravity maps to bound its position
    url: https://www.gpsworld.com/q-ctrl-demonstrates-gps-free-quantum-navigation-in-coral-sea-field-trial/
    date: "2026-08"
    quote: "the system cross-references locally measured gravity anomalies against broad satellite-derived gravity maps to continuously bound position error."
  - claim: Q-CTRL's gravity navigation corrects an inertial navigation system
    url: https://thequantuminsider.com/?p=2392470
    date: "2026-08-27"
    quote: "This breakthrough approach provides a correction to improve the performance of an inertial navigation syste"
  - claim: Ironstone Opal passed the RTCA DO-160 safety-of-flight qualification
    url: https://interestingengineering.com/innovation/quantum-navigation-system-gps-backup-for-aircraft
    date: "2026-07"
    quote: "is the first quantum navigation technology to achieve RTCA DO-160 safety-of-flight qualification."
```

### ed089
```yaml
status: ok
section: Tech and infra
title: Does every layer carry the same weight?
note: We ranked these layers directionally from DARPA, DIU and QED-C findings and recent field trials, not from a standardized industry score.
t:
  38: "RANKING"
  6: "CONTROL"
  14: "Decides whether a sensor survives vibration and noise on a ship, plane or vehicle"
  7: "MAPS"
  24: "Without good gravity or magnetic maps, a navigator cannot turn readings into position"
  8: "ATOMS"
  26: "Set the precision limit, but the lab physics behind them is now well understood"
  9: "LASERS"
  28: "Remain the most delicate parts, and their supply chain is still fragmented"
  10: "CHIPS"
  30: "Shrink size, weight and price, which decide whether buyers can order many units"
  11: "FUSION"
  32: "Lets buyers add sensors to existing navigation systems with little rework"
  12: "TESTING"
  34: "Turns a promising prototype into something a pilot or a navy will trust"
  13: "DIAMOND"
  36: "Opens room-temperature uses such as chip inspection, but serves narrower markets"
sources:
  - claim: Vibration and electromagnetic interference limit quantum sensors outside the lab (DARPA RoQS)
    url: https://www.darpa.mil/news/2025/roqs-launches-first-phase
    date: "2025-08-27"
    quote: "Even minor vibrations or electromagnetic interference can degrade performance, limiting their operational use."
  - claim: QED-C has flagged a fragmented manufacturing supply chain as an obstacle
    url: https://www.fiercesensors.com/sensors/global-quantum-sensing-market-could-hit-1b-2028-says-qed-c
    date: "2025"
    quote: "awareness, overall cost, and a fragmented manufacturing supply chain for quantum sensors continue to be obstacles in the way of greater market growth."
  - claim: Gravity navigation suits ships partly because gravity maps at sea are widely available
    url: https://www.defenceconnect.com.au/naval/18808-q-ctrl-completes-milestone-maritime-vessel-navigation-without-gps-using-quantum-gravimeter
    date: "2026-08"
    quote: "Quantum gravimetric navigation is suitable for maritime vessels for technical reasons and due to the broader availability of gravity maps at sea."
  - claim: Cost is a main barrier to broader adoption
    url: https://siliconangle.com/?p=821154
    date: "2026-08-20"
    quote: "That’s critical, because cost has been one of the main barriers that has so far prevented the broader adoption of quantum sensing."
```

### ed090
```yaml
status: ok
section: Tech and infra
title: Where does 80% of quantum sensing value sit?
note: We treated ruggedization and integration as the main value bottlenecks because DARPA, DIU and recent field trials repeatedly name them as the gap between lab and sale.
t:
  9: "💰 💰 💰 💰 💰 💰 💰 💰 💰\n💰 💰 💰 💰 💰 💰 💰 💰 💰\n💰 💰 💰 💰 💰 💰 💰 💰 💰\n💰 💰 💰 💰 💰 💰 💰 💰 💰\n💰 💰 💰 💰 💰 💰 💰 💰 💰\n💰 💰 💰 💰 💰 💰 💰 💰 💰\n💰 💰 💰 💰 💰 💰 💰 💰 💰\n💰 💰 💰 💰 💰 💰 💰 💰 💰\n\n💰 💰 💰 💰 💰 💰 💰 💰 💰\n💰 💰 💰 💰 💰 💰 💰 💰 💰"
  8: "Most value today sits in control and ruggedization, because a quantum sensor only sells once it keeps working on a moving ship, plane or vehicle.\n\nMaps and system integration come next, since a navigator is useless without good maps and a simple way into existing systems.\n\nWinners will pair rugged sensors with small chips, trusted maps and the safety tests buyers demand."
sources:
  - claim: DARPA RoQS aims to make quantum sensors robust enough to leave the lab
    url: https://www.darpa.mil/news/2025/quantum-sensors-defense-platforms
    date: "2025-02-07"
    quote: "RoQS will seek to develop quantum sensors that are inherently resistant to environmental disruptions"
  - claim: DIU's TQS program exists to prove military utility of quantum sensors in field tests
    url: https://www.diu.mil/latest/dius-transition-of-quantum-sensing-tqs-field-testing-to-begin-across-five
    date: "2025-03-12"
    quote: "the Defense Innovation Unit’s (DIU’s) Transition of Quantum Sensing (TQS) program will demonstrate the military utility of quantum sensors"
```

### ed091
```yaml
status: ok
section: Tech and infra
title: How has tech and infra evolved over the years?
note: We used field and sales milestones rather than lab records because they show when the technology became usable outside the lab.
t:
  6: "2010 - 2018\n\n\nAOSense delivered a compact atom gravimeter to an aerospace customer, and Muquans' transportable gravimeter passed field tests in 2018"
  7: "2019 - 2023\n\n\nCerca began selling wearable brain scanners, and Vector Atomic launched the first commercial optical clock in 2023"
  8: "2024 - 2025\n\n\nInfleqtion flew quantum navigation on a UK jet, DIU and DARPA funded field tests, and Q-CTRL beat GPS backups"
  9: "TODAY\n\n\nQ-CTRL's navigator passed flight safety tests, a diamond magnetometer is in orbit and Cerca has sold 19 brain scanners"
  10: "?\n\n\nNext sensors may shrink to chips, ride on drones and map gravity under cities and seas without any drilling"
sources:
  - claim: AOSense delivered its first commercial compact gravimeter to an aerospace customer in 2010
    url: https://arxiv.org/pdf/2003.12516
    date: "2020-03"
    quote: "delivered its first commercial compact gravimeter to an aerospace customer in 2010"
  - claim: Muquans' transportable gravimeter passed field campaigns in 2018
    url: https://observatoiredeparis.psl.eu/muquans-validates-its-quantum.html
    date: "2018-11-06"
    quote: "The first commercial, compact and transportable quantum gravimeter was used during a series of measurement campaigns lasting many days by a team of geophysicists."
  - claim: Vector Atomic launched the first fully integrated commercial optical clock in 2023
    url: https://businesswire.com/news/home/20231113157771/en
    date: "2023-11-13"
    quote: "Vector Atomic has announced the launch of Evergreen-30, the world’s first fully integrated commercial optical clock."
  - claim: Infleqtion flew quantum navigation technology on a UK test aircraft in 2024
    url: https://www.ukri.org/news/un-jammable-quantum-tech-takes-flight-to-boost-uks-resilience/
    date: "2024-05"
    quote: "In a commercial world-first, quantum navigation technology developed in the UK, supported through UKRI funding, was successfully tested in flight."
  - claim: SBQuantum's diamond magnetometer was launched into orbit in March 2026
    url: https://www.techbriefs.com/component/content/article/55180-sbquantum-launches-quantum-sensor-into-space
    date: "2026"
    quote: "reached its completion with the launch of the SBQDM payload in March 2026."
  - claim: Cerca has sold 19 systems
    url: https://thequantuminsider.com/2026/04/21/cerca-magnetics-secures-38m-series-a-funding-scale-quantum-brain-scanner/
    date: "2026-04-21"
    quote: "The company has sold 19 systems to neuroscience centres in 12 countries"
```

### ed092
```yaml
status: ok
section: Tech and infra
title: What were the latest tech and infra developments?
page: 1/2
note: We prioritized milestones with direct field or commercial consequences, using company releases and government announcements.
t:
  13: "2023"
  14: "Vector Atomic launched Evergreen-30, the first fully integrated commercial optical clock, built for a server rack"
  15: "2024"
  16: "Infleqtion flew a compact optical clock and a cold-atom system on a UK test jet, the first such flights made public"
  17: "2024"
  18: "The Pentagon awarded Infleqtion $11 million to speed up the fielding of its Tiqker optical clocks in defense systems"
  19: "2025"
  20: "Q-CTRL's Ironstone Opal navigated aircraft without GPS, with up to 50 times less error than a high-end backup system"
  21: "2025"
  22: "DARPA launched its Robust Quantum Sensors program and gave Q-CTRL $24.4 million to build sensors for military vehicles"
  23: "2025"
  24: "IonQ completed its purchase of Vector Atomic, adding field-tested clocks, gravimeters and motion sensors in October"
sources:
  - claim: Evergreen-30 launched in November 2023 as the first fully integrated commercial optical clock, in a 3U rack package
    url: https://datacenterdynamics.com/en/news/vector-atomic-launches-rack-mounted-atomic-clock
    date: "2023-11"
    quote: "The 3U package fits standard server racks"
  - claim: The May 2024 UK flights were the first such flights worldwide to be publicly acknowledged
    url: https://www.gov.uk/government/news/un-jammable-quantum-tech-takes-flight-to-boost-uks-resilience-against-hostile-actors
    date: "2024-05-13"
    quote: "the first such flights worldwide that have been publicly acknowledged."
  - claim: Infleqtion's $11M APFIT contract speeds fielding of Tiqker clocks
    url: https://spacenews.com/?p=509524
    date: "2024-12-03"
    quote: "The Defense Department awarded an $11 million contract to the quantum technology firm Infleqtion to accelerate development of its atomic timing technology"
  - claim: Ironstone Opal outperformed a high-end GPS alternative by up to 50x
    url: https://q-ctrl.com/blog/q-ctrl-overcomes-gps-denial-with-quantum-sensing-achieves-quantum-advantage
    date: "2025-04-14"
    quote: "outperforming a high-end conventional GPS alternative by up to 50x"
  - claim: DARPA launched RoQS Phase 1 in August 2025 and Q-CTRL won $24.4M for military vehicle sensors
    url: https://www.eejournal.com/industry_news/darpa-selects-q-ctrl-to-develop-next-generation-quantum-sensors-for-navigation-on-advanced-defense-platforms/
    date: "2025-08-27"
    quote: "contracts valued at A$38M (US$24.4M) to augment Q-CTRL’s field-validated quantum sensing technologies for demanding real-world use cases in high-performance military vehicles."
  - claim: IonQ completed the Vector Atomic acquisition in October 2025
    url: https://www.sec.gov/Archives/edgar/data/1824920/000095014225002689/eh250685098_ex9901.htm
    date: "2025-10-07"
    quote: "IonQ Completes Acquisition of Vector Atomic, the Global Leader in Advanced Quantum Sensing"
```

### ed093
```yaml
status: ok
section: Tech and infra
title: What were the latest tech and infra developments?
page: 2/2
note: We used company releases and specialist press to capture the most consequential 2026 technology milestones.
t:
  13: "2026"
  14: "Q-CTRL put Ironstone Opal on sale as the first commercial quantum navigation system, shown at the Singapore Airshow"
  15: "2026"
  16: "SBQuantum launched its diamond magnetometer into orbit on a SpaceX rideshare to map Earth's magnetic field from space"
  17: "2026"
  18: "Infleqtion and Safran released a timing system built on the Tiqker optical clock, for networks that lose satellite time"
  19: "2026"
  20: "Infleqtion unveiled Quantum Spectrum, radio receivers that use excited atoms instead of antennas, for defense buyers"
  21: "2026"
  22: "Q-CTRL's Ironstone Opal became the first quantum navigation system to pass the DO-160 flight safety test standard"
  23: "2026"
  24: "Q-CTRL guided a 29-meter vessel 83 km without GPS using a quantum gravimeter, staying within one nautical mile"
sources:
  - claim: Q-CTRL unveiled Ironstone Opal as the first commercially available quantum navigation system on 2 February 2026, at the Singapore Airshow
    url: https://quantumzeitgeist.com/?p=262768
    date: "2026-02-02"
    quote: "Q-CTRL has today, February 2, 2026, unveiled the first commercially available quantum navigation system"
  - claim: SBQuantum's diamond magnetometer launched to space on 29 March 2026 for the MagQuest challenge
    url: https://www.datamintelligence.com/blogs/why-quantum-magnetometer-sensors-are-moving-from-lab-precision-to-real-world-deployment-in-2026
    date: "2026"
    quote: "On March 29, 2026, SBQuantum’s quantum diamond magnetometer was launched into space as part of the final phase of the MagQuest Challenge"
  - claim: The launch used SpaceX's Transporter rideshare
    url: https://interestingengineering.com/innovation/quantum-sensor-launch-into-space-spacex
    date: "2026-03"
    quote: "The launch is scheduled for Sunday, March 29th, 2026, on board Transporter 16, a rideshare program from SpaceX."
  - claim: Infleqtion and Safran made a Tiqker-based timing solution available on 1 April 2026
    url: https://www.yolegroup.com/industry-news/infleqtion-announces-2026-revenue-guidance-of-40-million/
    date: "2026-04"
    quote: "On April 1, 2026, Infleqtion announced the availability of its first quantum-enabled precision timing solution delivered with Safran Electronics & Defense."
  - claim: Infleqtion launched Quantum Spectrum Rydberg receivers in May 2026
    url: https://thequantuminsider.com/2026/05/13/infleqtion-quantum-spectrum-rf-sensing/
    date: "2026-05-13"
    quote: "Infleqtion’s Quantum Spectrum receivers use Rydberg atoms as the sensing medium, replacing conventional RF front ends with atom-based detection"
  - claim: Ironstone Opal is the first quantum navigation system qualified to RTCA DO-160 (July 2026)
    url: https://q-ctrl.com/blog/q-ctrl-to-showcase-worlds-first-airworthiness-qualified-quantum-navigation-gps-backup-at-the-farnborough-international-airshow
    date: "2026-07-14"
    quote: "is also the first quantum navigation system to achieve safety-of-flight qualification under the stringent RTCA DO-160 airworthiness standard."
  - claim: Q-CTRL navigated a 29-meter vessel 83 km in the Coral Sea within one nautical mile
    url: https://quantumcomputingreport.com/q-ctrl-demonstrates-first-gps-free-quantum-gravimetric-maritime-navigation-in-coral-sea-field-trial/amp/
    date: "2026-08-27"
    quote: "Tested aboard a 29-meter surface vessel in the Coral Sea off Australia’s eastern coast"
  - claim: The vessel kept 1-nautical-mile accuracy over an 83 km route without GPS
    url: https://www.gpsworld.com/q-ctrl-demonstrates-gps-free-quantum-navigation-in-coral-sea-field-trial/
    date: "2026-08"
    quote: "achieved bounded 1-nautical-mile positioning accuracy without satellite signals, outperforming standard navigation-grade inertial backups by more than 10x over an 83-km trajectory."
```

### ed094
```yaml
status: ok
section: Tech and infra
title: What are the solvable bottlenecks?
note: We selected bottlenecks repeatedly named by DARPA, QED-C and recent field trials as technically addressable but not yet broadly solved.
t:
  39: "BOTTLENECK"
  38: "EXPLANATION"
  41: "BOTTLENECK"
  40: "EXPLANATION"
  7: "SIZE AND\nPOWER"
  5: "Leading optical clocks still weigh up to 22 kg and draw up to 85 W, too much for small drones"
  24: "UNIT\nCOST"
  22: "Cost remains one of the main barriers keeping quantum sensors from wide use"
  11: "MOTION\nNOISE"
  9: "Vibration and sudden motion on vehicles blur the delicate atom measurements"
  28: "LASER\nSUPPLY"
  26: "Lasers and other key parts come from a fragmented supply chain"
  15: "PLATFORM\nNOISE"
  13: "Motors, wiring and electronics on board create fields that drown signals"
  32: "MAP\nGAPS"
  30: "Navigation works only where good gravity or magnetic maps exist and stay current"
  19: "AVIATION\nAPPROVAL"
  17: "Aircraft use needs safety qualification, then approval for each type of airplane"
  36: "BUYER\nAWARENESS"
  34: "Many buyers still do not know what quantum sensors can do or how to compare them"
sources:
  - claim: Infleqtion's Tiqker clock weighs less than 22 kg and draws less than 85 W
    url: https://infleqtion.com/tiqker/
    date: "2026"
    quote: "Less than 22 kg and less than 85 W steady-state power."
  - claim: Cost has been one of the main barriers to broader adoption
    url: https://siliconangle.com/?p=821154
    date: "2026-08-20"
    quote: "cost has been one of the main barriers that has so far prevented the broader adoption of quantum sensing."
  - claim: Vibrations and electromagnetic interference degrade quantum sensors
    url: https://www.darpa.mil/news/2025/roqs-launches-first-phase
    date: "2025-08-27"
    quote: "Even minor vibrations or electromagnetic interference can degrade performance, limiting their operational use."
  - claim: Awareness, cost and a fragmented manufacturing supply chain are obstacles
    url: https://www.fiercesensors.com/sensors/global-quantum-sensing-market-could-hit-1b-2028-says-qed-c
    date: "2025"
    quote: "awareness, overall cost, and a fragmented manufacturing supply chain for quantum sensors continue to be obstacles in the way of greater market growth."
  - claim: Motors, electronics and wiring on platforms disrupt quantum sensors
    url: https://www.nextbigfuture.com/2025/10/darpa-developing-quantum-sensors-that-are-durable-for-real-world-use.html
    date: "2025-10"
    quote: "Fields: Electromagnetic interference from motors, electronics, and wiring disrupts qubit energy levels, reducing coherence."
  - claim: Aging magnetic data degrades navigation, which quantum sensors could help fix
    url: https://www.techradar.com/pro/the-navigation-systems-on-board-aircraft-and-drones-will-be-off-significantly-why-aging-magnetic-data-poses-a-growing-risk-and-how-quantum-sensors-could-help-fix-it
    date: "2026"
    quote: "Our spring 2026 space-launch came after years of testing and retesting with NASA and other organizations."
  - claim: DO-160 checks environmental qualification and is not product certification
    url: https://xenospectrum.com/en/q-ctrl-ironstone-opal-do160/
    date: "2026-07"
    quote: "RTCA itself states that it does not certify products, and what DO-160 verifies is environmental qualification."
```

### ed095
```yaml
status: ok
section: Tech and infra
title: Why can’t we solve them yet?
note: We tied each reason to known sensor physics and market facts rather than assuming a single engineering change can solve the full problem.
t:
  39: "BOTTLENECK"
  38: "REASON WHY"
  41: "BOTTLENECK"
  40: "REASON WHY"
  7: "SIZE AND\nPOWER"
  5: "Atoms need vacuum, lasers and control electronics, and every part must shrink at once"
  24: "UNIT\nCOST"
  22: "Output is still small-batch, and the first sensor factories are only being built"
  11: "MOTION\nNOISE"
  9: "Platform motion limits how long atoms can be measured, and short reads lose precision"
  28: "LASER\nSUPPLY"
  26: "Each atom type needs lasers tuned to exact colors, a niche with few volume buyers"
  15: "PLATFORM\nNOISE"
  13: "Shielding adds bulk, so designs must reject noise by physics or by software"
  32: "MAP\nGAPS"
  30: "Fine maps need costly surveys, and magnetic maps age as the Earth's field moves"
  19: "AVIATION\nAPPROVAL"
  17: "Beyond DO-160, aviation rules also demand software assurance and fitting approval"
  36: "BUYER\nAWARENESS"
  34: "The field is young, and many results are still shown in trials, not in sales"
sources:
  - claim: Platform motion limits sampling rates and the long integration times quantum sensors rely on
    url: https://www.nextbigfuture.com/2025/10/darpa-developing-quantum-sensors-that-are-durable-for-real-world-use.html
    date: "2025-10"
    quote: "Platform motion limits sampling rates and coherence times, preventing long integration periods that quantum sensors rely on for sensitivity."
  - claim: QuantumDiamonds is building the world's first production facility for quantum-based chip inspection
    url: https://www.hpcwire.com/off-the-wire/quantumdiamonds-raises-e91m-to-set-global-standard-for-next-gen-chip-inspection/
    date: "2026-07"
    quote: "The company is investing €152 million to build the world’s first production facility for quantum-based semiconductor inspection in Munich"
  - claim: DARPA RoQS rejects shielding and isolation as temporary fixes and redesigns sensors instead
    url: https://www.darpa.mil/news/2025/roqs-launches-first-phase
    date: "2025-08-27"
    quote: "not by applying temporary fixes like shielding or isolation, but by rethinking sensor design from the ground up."
  - claim: Certification needs software and hardware assurance and installation approval per airframe beyond DO-160
    url: https://xenospectrum.com/en/q-ctrl-ironstone-opal-do160/
    date: "2026-07"
    quote: "RTCA itself states that it does not certify products, and what DO-160 verifies is environmental qualification."
  - claim: Only nearly a third of companies had their main technology commercially available in 2025
    url: https://quantumconsortium.org/publication/2026-market-forecast-quantum-sensing/
    date: "2026-04"
    quote: "Nearly a third of respondents report their primary technology as commercially available in 2025, rising to 58% by 2028."
  - claim: Magnetic reference data ages and needs refreshing (MagQuest and the World Magnetic Model)
    url: https://interestingengineering.com/innovation/quantum-sensor-launch-into-space-spacex
    date: "2026-03"
    quote: "The World Magnetic Model (WMM) is a large-scale spatial representation of the Earth’s magnetic field."
```

### ed096
```yaml
status: ok
section: Tech and infra
title: When can we realistically expect to solve them?
note: We base these estimates on current field trials, DARPA and DIU program timelines and the UK goal of quantum navigation on aircraft by 2030. They are directional rather than consensus forecasts.
t:
  39: "BOTTLENECK"
  38: "WHY THIS TIMELINE"
  41: "BOTTLENECK"
  40: "WHY THIS TIMELINE"
  7: "SIZE AND\nPOWER"
  5: "Chip-scale parts and vapor cells are now in production, but whole systems need more design cycles"
  24: "UNIT\nCOST"
  22: "New factories such as QuantumDiamonds' Munich site cut costs, but volume buyers must come first"
  42: "2030"
  46: "2030"
  11: "MOTION\nNOISE"
  9: "Software already lets Q-CTRL sensors work at sea and in flight, and DARPA's RoQS adds new designs"
  28: "LASER\nSUPPLY"
  26: "New startups now make vapor cells and lasers, but supply chains take years to mature"
  43: "2028"
  47: "2029"
  15: "PLATFORM\nNOISE"
  13: "DARPA's RoQS second phase will put sensors on real defense platforms"
  32: "MAP\nGAPS"
  30: "Gravity maps at sea are already broad, but fine land and magnetic maps need new surveys"
  44: "2028"
  48: "2031"
  19: "AVIATION\nAPPROVAL"
  17: "Q-CTRL passed DO-160 in 2026, and the UK aims for quantum navigation on aircraft by 2030"
  36: "BUYER\nAWARENESS"
  34: "Each public field trial and contract makes the case easier for the next buyer"
  45: "2030"
  49: "2029"
sources:
  - claim: Mesa Quantum scaled vapor cell production and builds chip-scale sensors for integration at scale
    url: https://www.hpcwire.com/off-the-wire/mesa-quantum-raises-oversubscribed-11-8m-round-to-end-dependence-on-fragile-gps/
    date: "2026-09-28"
    quote: "Mesa Quantum is developing the next generation of chip-scale quantum sensing technology for integration at scale."
  - claim: QuantumDiamonds is building a €152M production facility in Munich
    url: https://www.hpcwire.com/off-the-wire/quantumdiamonds-raises-e91m-to-set-global-standard-for-next-gen-chip-inspection/
    date: "2026-07"
    quote: "The company is investing €152 million to build the world’s first production facility for quantum-based semiconductor inspection in Munich"
  - claim: Q-CTRL software lets its gravimeter work in heavy seas without special countermeasures
    url: https://ifsma.org/?p=1102
    date: "2026-08-27"
    quote: "Q-CTRL’s AI-powered software stabilizes the quantum sensor, enabling it to work under heavy seas with no special counterme"
  - claim: RoQS phase 2 will integrate quantum sensors onto actual DoD platforms
    url: https://intelligencecommunitynews.com/?p=42553
    date: "2025-08-27"
    quote: "its real impact will be realized in the program’s second phase, during which quantum sensors will be integrated onto actual DOD platforms"
  - claim: Gravity maps are more widely available at sea
    url: https://www.defenceconnect.com.au/naval/18808-q-ctrl-completes-milestone-maritime-vessel-navigation-without-gps-using-quantum-gravimeter
    date: "2026-08"
    quote: "due to the broader availability of gravity maps at sea."
  - claim: UK Mission 4 targets quantum navigation systems on aircraft by 2030
    url: https://www.gov.uk/government/publications/national-quantum-strategy/national-quantum-strategy-missions
    date: "2023"
    quote: "By 2030, quantum navigation systems, including clocks, will be deployed on aircraft"
```

### ed097
```yaml
status: ok
section: Tech and infra
title: Which bold bets could reshape quantum sensing?
note: We grounded the bets in current directions such as quantum navigation trials, wearable brain scanners, atom radio receivers, chip-scale clocks and NASA's quantum gravity mission.
t:
  9: "GPS-FREE FLIGHT"
  12: "WEARABLE BRAIN SCANS"
  15: "ATOM RADIO RECEIVERS"
  18: "GRAVITY MINING SURVEYS"
  33: "NEAR-TERM HORIZON\n\n(0-5 YEARS)"
  7: "It is a quantum navigator that keeps planes on course when GPS is jammed or spoofed"
  10: "It is a helmet that maps brain activity in children and adults without liquid helium cooling"
  13: "It is a radio receiver that uses excited atoms to hear signals across the whole spectrum"
  16: "It is a gravity sensor on a truck or drone that finds ore bodies without drilling holes"
  21: "CHIP-SCALE CLOCKS"
  24: "CITY GRAVITY MAPS"
  27: "SUBMARINE NAVIGATION"
  30: "SPACE GRAVITY WATCH"
  34: "LONG-TERM HORIZON\n\n(5-10 YEARS)"
  19: "It is an optical clock on a chip that brings timing to cars, phones and cell towers"
  22: "It is a sensor that images pipes, voids and tunnels under streets before anyone digs"
  25: "It is a sealed motion sensor that steers submarines through long missions with no signal"
  28: "It is a quantum gravity sensor in orbit, like the one NASA JPL plans to test from space"
sources:
  - claim: Ironstone Opal operates independently of satellite signals when GPS is jammed or spoofed
    url: https://interestingengineering.com/innovation/quantum-navigation-system-gps-backup-for-aircraft
    date: "2026-07"
    quote: "allowing it to continue providing navigation data even when GPS is unavailable or affected by jamming or spoofing."
  - claim: Cerca's wearable scanner lets patients move and suits babies and children
    url: https://radiologybusiness.com/topics/artificial-intelligence/worlds-most-advanced-functional-brain-scanner-cerca
    date: "2020"
    quote: "There are many advantages to our system but for me, the biggest is the ability to scan babies and children."
  - claim: Rydberg receivers tune from hertz to terahertz in a single aperture
    url: https://thequantuminsider.com/2026/05/13/infleqtion-quantum-spectrum-rf-sensing/
    date: "2026-05-13"
    quote: "atom-based detection that tunes continuously from hertz to terahertz across the full RF spectrum in a single aperture."
  - claim: Atomionics is developing vehicle and drone gravimeter surveys
    url: https://www.mining-technology.com/?p=718766
    date: "2026-10"
    quote: "The company is also developing drone-based gravimeter surveys"
  - claim: Infleqtion's roadmap points Tiqker toward chip scale
    url: https://infleqtion.com/tiqker/
    date: "2026"
    quote: "Toward chip-scale"
  - claim: Delta.g's gravity gradiometers detect voids, cavities and buried structures
    url: https://www.techuk.org/what-we-deliver/london-tech-week-2026/delta-g.html
    date: "2026"
    quote: "designed to support non-intrusive detection of voids, cavities, buried structures, ground instability"
  - claim: Atom inertial sensors target submarine navigation
    url: https://thequantuminsider.com/?p=8982
    date: "2026-04"
    quote: "leverages atom-based quantum sensing to develop precision inertial sensors for submarine navigation, aerospace, and geophysics."
  - claim: Infleqtion collaborates on NASA JPL's Quantum Gravity Gradiometer Pathfinder mission
    url: https://www.barchart.com/story/news/1941548/infleqtion-reports-record-q1-revenue-as-customer-demand-accelerates
    date: "2026-05-14"
    quote: "Announced Infleqtion’s role as a collaborator on NASA JPL’s Quantum Gravity Gradiometer Pathfinder mission, supported by $20 million in contracts to date"
```

### ed098
```yaml
status: ok
section: Tech and infra
title: Which companies are working on groundbreaking tech today?
t:
  8: "INFLEQTION"
  6: "They use neutral atoms for clocks, radio receivers and motion sensors sold to defense"
  24: "VECTOR ATOMIC"
  22: "They built the first rackmount optical clock and sea-tested atom gravimeters, now inside IonQ"
  11: "SANDBOXAQ"
  9: "They pair quantum magnetometers with AI to navigate aircraft by Earth's magnetic field"
  27: "SBQUANTUM"
  25: "They make diamond magnetometers proven in geology surveys and qualified for space"
  14: "Q-CTRL"
  12: "They use control software to keep quantum navigation sensors stable on planes and ships"
  30: "DELTA.G"
  28: "They build quantum gravity gradiometers that spot voids and buried structures"
  17: "CERCA MAGNETICS"
  15: "They build wearable brain scanners from atomic magnetometers, with 19 systems sold"
  33: "MESA QUANTUM"
  31: "They build chip-scale quantum timing sensors and vapor cells for timing without GPS"
sources:
  - claim: Infleqtion sells Tiqker clocks and Exaqt sensors for timing and navigation
    url: https://www.fool.com/quote/NYSE/INFQ
    date: "2026"
    quote: "Devices like Tiqker clocks and Exaqt sensors for precise timing and navigation"
  - claim: Vector Atomic systems include sea-proven gravimetry and airborne clocks
    url: https://www.sec.gov/Archives/edgar/data/1824920/000095014225002689/eh250685098_ex9901.htm
    date: "2025-10-07"
    quote: "Vector Atomic systems are deployable and field-validated from sea-proven gravimetry to, airborne clocks, to space-ready gyros"
  - claim: AQNav uses quantum sensors and AI to navigate by Earth's geomagnetic variations
    url: https://quantumcomputingreport.com/sandboxaq-partners-with-dows-defense-innovation-unit-to-advance-quantum-enabled-magnetic-navigation/amp/
    date: "2025-11-18"
    quote: "SandboxAQ will deploy its proven, dual-use AQNav software, which utilizes quantum sensors and AI to navigate using Earth’s natural geomagnetic variations."
  - claim: SBQuantum's NV magnetometer was demonstrated in geological surveys and designed for space
    url: https://quantumzeitgeist.com/?p=238217
    date: "2025"
    quote: "The sensor is designed for space deployment, with a launch planned for early 2025, and has been demonstrated in terrestrial surveys for geological mapping."
  - claim: Q-CTRL's software-ruggedized sensors navigate ships and aircraft
    url: https://q-ctrl.com/case-study/q-ctrl-delivering-quantum-advantage-to-airborne-systems
    date: "2025"
    quote: "Q-CTRL provided a new solution from top to bottom, built around the concept of “software ruggedized hardware.”"
  - claim: Delta.g builds quantum gravity gradiometers for voids and buried structures
    url: https://www.techuk.org/what-we-deliver/london-tech-week-2026/delta-g.html
    date: "2026"
    quote: "Our quantum gravity gradiometers detect minute variations in the gravitational field exposing what no camera, radar, or traditional sensor can."
  - claim: Cerca uses optically pumped magnetometers and has sold 19 systems
    url: https://thequantuminsider.com/2026/04/21/cerca-magnetics-secures-38m-series-a-funding-scale-quantum-brain-scanner/
    date: "2026-04-21"
    quote: "The company has sold 19 systems to neuroscience centres in 12 countries"
  - claim: Mesa Quantum delivers accurate time independent of GPS with chip-scale sensors
    url: https://www.hpcwire.com/off-the-wire/mesa-quantum-raises-oversubscribed-11-8m-round-to-end-dependence-on-fragile-gps/
    date: "2026-09-28"
    quote: "Mesa Quantum’s ability to deliver exquisitely accurate time, independent of GPS, is the first of many breakthroughs in quantum sensing"
```

### iv_pipeline
```yaml
status: ok
section: Tech and infra
title: Which quantum sensing products launched recently?
note: We list eight representative quantum sensing products launched, delivered or expanded in the past year, each named in a company release or specialist press.
comment: "Stages: BETA means field trial or prototype delivered, LAUNCH means on sale in the last 12 months, SCALE means a named large buyer or volume orders. Quantum Diamonds is written with a space so the name fits the slide."
t:
  38: "SCALE"
  34: "Tiqker optical clock, in a timing system built with Safran"
  37: "INFLEQTION · TIMING"
  27: "LAUNCH"
  26: "ATOMIONICS · MINING"
  24: "GRAVIO gravimeter on an SUV, mapped an iron ore deposit in India"
  23: "LAUNCH"
  22: "Q-CTRL · AIR NAVIGATION"
  20: "Ironstone Opal GPS backup, first quantum navigator to pass DO-160"
  19: "SCALE"
  18: "CERCA MAGNETICS · BRAIN SCANS"
  16: "Wearable OPM-MEG brain scanner, 19 systems in 12 countries"
  15: "BETA"
  12: "Diamond magnetometer launched into orbit for MagQuest"
  14: "SBQUANTUM · SPACE MAPS"
  11: "BETA"
  10: "INFLEQTION · RF SENSING"
  8: "Quantum Spectrum receiver that uses excited atoms in place of antennas"
  7: "BETA"
  6: "PIXEL PHOTONICS · PHOTONS"
  4: "Chip-integrated superconducting single-photon detectors"
  3: "LAUNCH"
  2: "QUANTUM DIAMONDS · CHIP TESTS"
  0: "QDm.1 chip microscope, engaged by 9 of the 10 largest chipmakers"
sources:
  - claim: Infleqtion's Tiqker-based timing solution with Safran became available in April 2026, after an $11M Pentagon APFIT contract to field Tiqker clocks
    url: https://www.yolegroup.com/industry-news/infleqtion-announces-2026-revenue-guidance-of-40-million/
    date: "2026-04"
    quote: "On April 1, 2026, Infleqtion announced the availability of its first quantum-enabled precision timing solution delivered with Safran Electronics & Defense."
  - claim: The Pentagon funded Tiqker fielding through APFIT
    url: https://spacenews.com/?p=509524
    date: "2024-12-03"
    quote: "The funding awarded to Infleqtion will accelerate the deployment and fielding of these clocks, ensuring they are integrated into defense systems faster"
  - claim: Atomionics' SUV-mounted GRAVIO matched a drilled resource at an active iron ore mine in India
    url: https://www.mining-technology.com/?p=718766
    date: "2026-10"
    quote: "The company used a sports utility vehicle (SUV)-mounted quantum gravimeter coupled with a machine learning (ML) inversion tool to collect data over three weeks."
  - claim: Ironstone Opal is commercially available and the first quantum navigation system qualified to DO-160
    url: https://q-ctrl.com/blog/q-ctrl-to-showcase-worlds-first-airworthiness-qualified-quantum-navigation-gps-backup-at-the-farnborough-international-airshow
    date: "2026-07-14"
    quote: "is also the first quantum navigation system to achieve safety-of-flight qualification under the stringent RTCA DO-160 airworthiness standard."
  - claim: Navigation already generates revenue for Q-CTRL
    url: https://www.eweek.com/news/q-ctrl-290m-series-c-quantum-software-apac/
    date: "2026-11-19"
    quote: "Salesforce Ventures says navigation already generates revenue for Q-CTRL."
  - claim: Cerca has sold 19 systems in 12 countries and won a £2.8M UK Ministry of Defence project
    url: https://thequantuminsider.com/2026/04/21/cerca-magnetics-secures-38m-series-a-funding-scale-quantum-brain-scanner/
    date: "2026-04-21"
    quote: "a £2.8 million UK Ministry of Defence project to develop a mobile platform for assessing the effects of blast exposure on military personnel."
  - claim: SBQuantum's diamond magnetometer launched to space in March 2026 for MagQuest
    url: https://www.datamintelligence.com/blogs/why-quantum-magnetometer-sensors-are-moving-from-lab-precision-to-real-world-deployment-in-2026
    date: "2026"
    quote: "On March 29, 2026, SBQuantum’s quantum diamond magnetometer was launched into space as part of the final phase of the MagQuest Challenge"
  - claim: Infleqtion's Quantum Spectrum is moving from prototypes to field trials under contracted defense programs
    url: https://thequantuminsider.com/2026/05/13/infleqtion-quantum-spectrum-rf-sensing/
    date: "2026-05-13"
    quote: "Infleqtion is the first company with contracted defense programs in three allied nations developing atom-based RF sensing for operational deployment"
  - claim: Pixel Photonics raised €13.5M in 2026 to turn its waveguide-integrated SNSPDs into industrial products
    url: https://sprind.org/en/words/magazine/pixel-photonics
    date: "2026-04-08"
    quote: "Pixel Photonics secures 13.5 million euros in funding"
  - claim: Nine of the ten largest chipmakers engage with QuantumDiamonds, with systems deployed in Europe, the US and Asia
    url: https://www.hpcwire.com/off-the-wire/quantumdiamonds-raises-e91m-to-set-global-standard-for-next-gen-chip-inspection/
    date: "2026-07"
    quote: "Nine of the world’s ten largest semiconductor manufacturers are engaged with QuantumDiamonds, with systems deployed across Europe, the United States, and Asia."
```
