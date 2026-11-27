import yaml
out=["# quantum sensing, chapter 06 Value creation (evergreen, written by Claude, 27 Nov 2026)\n"]
def add(i,d): out.append(f"### {i}\n```yaml\n"+yaml.safe_dump(d,allow_unicode=True,sort_keys=False,width=1000)+"```\n")
L={7:"RUBIDIUM CLOCKS",9:"MEMS GYROS",11:"FLUXGATES",13:"SQUID SENSORS",15:"GPS RECEIVERS",17:"LAB LASERS",19:"GRAVITY MAPS",21:"PHOTON COUNTERS"}
add("ed101",{"status":"ok","title":"What's commoditized today in the market?",
 "note":"We identified tools that are now broadly available and offered by many companies. They remain necessary, but value is shifting to rugged sensors, noise software, small units and proof on real platforms.",
 "t":{**L,6:"Small rubidium atomic clocks for telecom, sold by Microchip and others",8:"Chip motion sensors in every phone and car, made by the millions",
 10:"Classic magnetic sensors used in drills and compasses for decades",12:"Helium-cooled magnetic sensors used in labs and hospital scanners for decades",
 14:"Satellite navigation chips that cost a few dollars in every phone and car",16:"Standard lasers and optics sold off the shelf by large photonics firms",
 18:"Broad gravity maps of the Earth from satellites, free for anyone to download",20:"Basic single-photon detectors sold by many firms for labs and lidar"}})
add("ed102",{"status":"ok","title":"Why has it become commoditized?",
 "note":"We see commoditization where tools reuse mature physics, open data and mass-made chips. New value therefore comes from sensors that stay precise on the move, at a size and price buyers accept.",
 "t":{**L,6:"Because Microchip has sold them for years and many rivals now compete",8:"Because chip factories make them in huge volumes at very low cost",
 10:"Because the design is decades old and many makers can now build it",12:"Because the physics is old, and big medical groups make them",
 14:"Because GPS chips are made in billions, with dozens of suppliers",16:"Because big photonics firms sell them from catalogs at scale",
 18:"Because space agencies share satellite gravity data for free",20:"Because lidar and lab demand pushed many makers into the market"}})
add("ed103",{"status":"ok","title":"Where is value created today?","page":"1/2",
 "note":"We derived these elements from the companies that won trials, contracts and funding, and from DARPA and DIU program goals. The strongest value today sits in sensors that work on the move.",
 "t":{9:"RUGGED\nSENSORS",7:"Sensors that keep their accuracy on shaking ships, planes and drones, not only in a quiet lab",
 12:"NOISE\nSOFTWARE",10:"Software that cancels vibration and noise, so a sensor works on the move without shielding",
 17:"SMALL\nUNITS",15:"Units small and frugal enough to fit drones, racks and helmets, at a price buyers accept"}})
add("ed104",{"status":"ok","title":"Where is value created today?","page":"2/2",
 "note":"We derived these elements from recent deals, field trials and factory plans. Value is increasingly created by maps, safety approvals and production at volume.",
 "t":{9:"MAPS AND\nFUSION",7:"Gravity and magnetic maps plus software that blends quantum readings with today's systems",
 12:"SAFETY\nAPPROVALS",10:"Approvals like DO-160 that let a sensor fly on aircraft, and records that win defense orders",
 17:"VOLUME\nPRODUCTION",15:"Factories that make vapor cells, chip clocks and diamonds by the thousand, at lower cost"}})
S=[("QUANTUM TIMING","Quantum timing","Atomic and optical clocks that keep exact time when GPS goes down",
 [("TELECOM\nNETWORKS","They are phone networks whose towers take their time from GPS and must keep calls and data in sync if that signal is lost"),
  ("POWER\nGRIDS","They are grid operators that use exact time to protect power lines, where a timing error can trip equipment"),
  ("DATA\nCENTERS","They are server farms and trading venues that must keep every machine on the same clock, to the microsecond"),
  ("NAVY\nFLEETS","They are navies that need exact time on ships and drone submarines that stay far from any satellite signal"),
  ("SPACE\nOPERATORS","They are satellite firms that want small atomic clocks on board to offer backup timing from orbit")],
 "GPS time is jammed near a city, and the operator does not notice any change. The rack clock holds exact time for days, every cell tower stays in sync, calls and payments keep flowing, and the security team sees an alert that names the attack.",
 "GPS time is jammed and the backup clock drifts within hours. Cell towers fall out of sync, calls drop and payments stall, and engineers drive from site to site to reset equipment while the outage spreads.",
 {9:"🔍\nAn operator picks a quantum clock",7:"🖥️\nIt fits in a standard server rack",6:"⏱️\nThe clock holds exact time for days",8:"💳\nThe operator buys each clock unit",13:"🔁\nMore sites get the same quantum clock",11:"🏢\nOther networks follow the leader",10:"📊\nNetwork outages fall year after year",12:"✅\nThe network never loses its time"}),
("QUANTUM NAVIGATION","Quantum navigation","Atom sensors of motion and gravity that guide ships and planes",
 [("NAVY\nFLEETS","They are navies whose ships and submarines must know their position for days at sea, with no GPS and no signal to betray them"),
  ("AIR\nFORCES","They are air forces whose aircraft and drones face GPS jamming and spoofing near every conflict zone"),
  ("AIR\nLINES","They are airlines that lose GPS on dozens of flights out of every thousand and want a backup on board"),
  ("DRONE\nMAKERS","They are drone makers whose craft get lost or crash when GPS is jammed, and need small backups"),
  ("SHIPPING\nFIRMS","They are cargo lines whose ships see spoofed positions near ports and narrow straits at sea")],
 "GPS is jammed over the sea, and the ship keeps its course. The quantum gravimeter matches readings to gravity maps, the position stays within one nautical mile for days, and the crew never sends a signal that would reveal where it is.",
 "GPS is jammed and the inertial system drifts a little more each hour. After a day the ship is miles off course, the crew must use radar or radio that give it away, and the mission is cut short.",
 {9:"🔍\nA navy picks a quantum navigator",7:"🧭\nIt is tested on a real navy ship",6:"✅\nIt passes field and safety tests",8:"💳\nThe navy pays for the first units",13:"🔁\nThe fleet orders more and more units",11:"🛡️\nAllied navies buy the same system",10:"📈\nMaps and software improve each year",12:"🚀\nShips stay on course with no GPS"}),
("MAGNETIC SENSING","Magnetic sensing","Atom and diamond sensors that map magnetic fields with precision",
 [("CHIP\nMAKERS","They are chip factories that use diamond microscopes to see current flowing inside chips and find hidden faults"),
  ("MINING\nFIRMS","They are miners that map magnetic rock from the air or the ground to find ore bodies before drilling"),
  ("DEFENSE\nFORCES","They are navies and air forces that detect submarines and navigate by the magnetic field of the Earth"),
  ("MATERIALS\nLABS","They are labs that map magnetism at tiny scales to design new materials, batteries and memory chips"),
  ("SPACE\nAGENCIES","They are space agencies that measure the Earth's field from orbit to keep navigation models current")],
 "The chipmaker scans a stacked chip with a diamond microscope and sees exactly where current leaks. The fault is found in minutes without cutting the chip open, the line is fixed the same day, and the yield of the next wafers goes up.",
 "The chipmaker knows a chip fails but cannot see where. Engineers cut it open layer by layer for days, the fault is destroyed in the process, and bad wafers keep coming off the line in the meantime.",
 {9:"🔍\nA chipmaker tests a diamond tool",7:"🔬\nIt scans the chips that failed",6:"🧲\nIt maps the current inside them",8:"💳\nThe chip factory buys the tool",13:"🔁\nMore factories order the same tool",11:"🏭\nIt moves onto the production line",10:"📊\nYields rise on the newest chips",12:"✅\nHidden faults are found in minutes"}),
("MEDICAL IMAGING","Medical imaging","Wearable scanners that map the brain and the heart without helium",
 [("CHILDREN'S\nHOSPITALS","They are hospitals that must scan babies and children who cannot stay still inside a big fixed scanner"),
  ("EPILEPSY\nCENTERS","They are clinics that map where seizures start in the brain, to plan surgery for patients with epilepsy"),
  ("BRAIN\nLABS","They are research centers that study how the brain works while people move, talk or play a game"),
  ("ARMED\nFORCES","They are military health teams that track the effects of blasts and head injuries on soldiers"),
  ("HEART\nCLINICS","They are cardiology teams that want to map the heart's magnetic field without wires or contact")],
 "A child wears a light helmet of quantum sensors and plays during the scan. The brain map is sharp even when the child moves, the room needs no liquid helium, and the doctor plans surgery from a clear image of where seizures start.",
 "The child must lie still inside a huge machine cooled with liquid helium. The scan fails each time the child moves, the family waits months for a new slot, and the doctor plans surgery with less information.",
 {9:"🔍\nA hospital picks a wearable scanner",7:"🧠\nPatients wear light sensor helmets",6:"🔬\nThe system maps the brain at work",8:"💳\nThe hospital buys the full system",13:"🔁\nMore helmets are added each year",11:"👥\nMore hospital teams use the scanner",10:"📄\nScans guide care and brain surgery",12:"✅\nEven moving children are scanned"}),
("RF SENSING","RF sensing","Receivers that use excited atoms to pick up radio and radar signals",
 [("ARMY\nUNITS","They are armies that must hear enemy radios and radars across the whole spectrum with small, hard-to-spot gear"),
  ("ELECTRONIC\nWARFARE","They are teams that detect and locate jammers, and need receivers that are not blinded by strong signals"),
  ("NAVY\nSHIPS","They are navies that want small receivers that cover many bands, instead of large sets of antennas"),
  ("SPECTRUM\nWATCHDOGS","They are agencies that check radio use and track illegal transmitters in crowded city bands"),
  ("TEST\nLABS","They are labs that calibrate antennas and radio gear and need exact field readings tied to atoms")],
 "The unit sets up one small atom receiver instead of a mast of antennas. It hears signals from very low to very high bands, a jammer is located within minutes, and the gear is hard for the enemy to spot or to blind.",
 "The unit carries large antennas for each band and still misses signals between them. A strong jammer blinds the receivers, the source stays hidden, and the antennas make the position easy to find.",
 {9:"🔍\nAn army tests an atom receiver",7:"📡\nIt listens across many radio bands",6:"🔬\nExcited atoms detect each signal",8:"💳\nThe army funds a full program",13:"🔁\nMore army units get the receivers",11:"🛡️\nAllied armies join the program",10:"📈\nThe design moves into production",12:"✅\nEnemy jammers are found in minutes"}),
("OPTICAL SENSING","Optical sensing","Detectors and cameras that count single particles of light",
 [("SPACE\nAGENCIES","They are space agencies that want cameras that see finer detail from orbit with smaller and lighter lenses"),
  ("DEFENSE\nFORCES","They are forces that need to see and track objects at long range, in low light and through haze"),
  ("QUANTUM\nNETWORKS","They are firms building quantum links that need detectors able to count every single photon"),
  ("LIDAR\nMAKERS","They are makers of laser scanners for cars and drones that need very sensitive light detectors"),
  ("SCIENCE\nLABS","They are labs that study single molecules and cells with very faint light and need low-noise detectors")],
 "The satellite carries a quantum-enhanced camera with a small lens. It sees detail many times finer than normal optics allow, images arrive with little noise, and the operator gets sharper pictures from a smaller and cheaper satellite.",
 "The satellite needs a large and heavy lens to see fine detail. Launch costs rise with each kilogram, the camera still blurs small objects, and the operator pays more for images that show less.",
 {9:"🔍\nA space firm picks a quantum camera",7:"🛰️\nIt flies on board a small satellite",6:"🔬\nIt counts single particles of light",8:"💳\nThe operator buys the camera payload",13:"🔁\nMore satellites carry the camera",11:"🌍\nNew clients buy the sharper images",10:"📈\nImages get sharper year after year",12:"✅\nSmall satellites now see fine detail"})]
for k,(cap,name,desc,users,good,bad,flow) in enumerate(S,1):
    add(f"ed106-s{k}",{"status":"ok","t":{6:"VALUE CREATION",3:cap,5:desc}})
    t={21:cap}
    for (lab,txt),kl,kt in zip(users,[5,8,11,14,17],[7,10,13,16,19]): t[kl]=lab; t[kt]=txt
    nm=name[0].lower()+name[1:]
    add(f"ed107-s{k}",{"status":"ok","title":"Who needs it the most?","note":f"We focus on five groups where {nm} creates the clearest value today. These are priority use cases, not a full list of clients.","t":t})
    add(f"ed108-s{k}",{"status":"ok","title":"What does \"maximum customer value\" look like in practice?","t":{5:cap,10:"EXCEPTIONAL CUSTOMER EXPERIENCE",7:good,12:"VS",9:"BAD CUSTOMER EXPERIENCE",6:bad}})
    add(f"ed109-s{k}",{"status":"ok","title":"How does the money flow in this case?","t":{14:cap,**flow}})
open("/home/claude/nmp-decks/decks/quantum-sensing/research/202-quantum-sensing-deck-06-value-creation-results-research-2026-11-27.md","w").write("\n".join(out))
