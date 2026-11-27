import yaml
out=["# quantum sensing, chapter 04 Pain points (evergreen, written by Claude, 27 Nov 2026)\n"]
def add(i,d):
    out.append(f"### {i}\n```yaml\n"+yaml.safe_dump(d,allow_unicode=True,sort_keys=False,width=1000)+"```\n")
add("ed054",{"status":"ok","title":"What are the pain points of yesterday vs. today?",
 "note":"We grouped the market into phases: lab physics, the first field units, the rise of GPS jamming, and today's push to production. We used defense programs, trial reports and filings.",
 "t":{6:"2007 - 2017\nQuantum sensors worked only in labs and filled whole tables, so buyers outside research had nothing they could actually use",
 7:"2018 - 2022\nThe first field gravimeters and brain scanners appeared, but they were heavy, costly and sold one by one to a few pioneers",
 8:"2023 - 2024\nGPS jamming spread over Europe and the Middle East, navies and air forces began trials, while sensors still lost accuracy on the move",
 9:"TODAY\nGPS loss hits about 57 of every 1,000 flights, and first products are on sale, but most units are still trial systems built by hand",
 10:"?\nBuyers will need small, cheap sensors made in volume, with maps and safety approvals, to put a backup on every plane and ship"}})
add("ed055",{"status":"ok","title":"Which old problems are now behind us?",
 "note":"We treat these as problems that new products have removed for many buyers. They do not mean that every sensor is ready for production, or works on every platform.",
 "t":{5:"Atomic clocks needed a full lab bench to run and to stay stable",7:"Infleqtion's Tiqker optical clock now fits in a standard server rack and ships with Safran timing systems",
 8:"Gravity sensors could not be moved from one site to another",10:"Field gravimeters from Exail and Atomionics now run on trucks and ships, logging data for months",
 11:"Brain scans needed huge magnets kept very cold with liquid helium",13:"Cerca Magnetics now sells wearable helmets that scan the brain at room temperature, even in children",
 14:"Quantum sensors failed as soon as a ship or a plane moved",16:"Q-CTRL's software now keeps its sensors working at sea and in flight, without heavy shielding",
 17:"No quantum navigator had ever passed aviation safety tests",19:"Q-CTRL's Ironstone Opal passed the DO-160 flight safety tests in 2026, a first for quantum navigation",
 20:"Startups had no clear path to big defense buyers or budgets",22:"DIU's Farseer program now offers up to $200M for prototypes ready in 3 to 9 months, then a path to use"}})
add("ed056",{"status":"ok","title":"What problems do all players face?","page":"1/2",
 "note":"We kept the problems that come back in DARPA, DIU and QED-C documents and in field trials. We skipped generic startup issues and focused on taking sensors out of the lab.",
 "t":{25:"Motion and noise\nblur the readings",23:"You need rugged\ndesigns",8:"Units are still\ntoo big",6:"You need smaller\nparts",
 29:"Each unit costs\ntoo much",27:"You need volume\nproduction",12:"Lasers come from\nfew suppliers",10:"You need steady\nsupply",
 33:"Navigation needs\ngood maps",31:"You need fresh\nsurveys",16:"Aircraft need\nsafety tests",14:"You need DO-160\nproof",
 37:"Buyers compare with\ncheap classic tools",35:"You need clear\nproof of gain",20:"Export rules cap\nwho can buy",18:"You need export\nlicenses"}})
add("ed057",{"status":"ok","title":"What problems do all players face?","page":"2/2",
 "note":"We separated the problems of building sensors from those of selling them. The second set matters once a sensor works, because budgets, buyers, rules and rivals still decide who wins.",
 "t":{25:"States pay most\nof the bills",23:"You need more\nbuyers",8:"Trials take years\nto become orders",6:"You need patient\ncash",
 29:"Few buyers know\nwhat it can do",27:"You need clear\nuse cases",12:"Investors favor\ncomputing",10:"You need sensing\ninvestors",
 33:"Each platform needs\nits own fit",31:"You need a\nsimple fit",16:"Rules split into\nUS and EU blocs",14:"You need local\nsupply chains",
 37:"Classic sensors\nget better too",35:"You need a clear\nedge",20:"Big groups buy\nthe leaders",18:"You need strong\npartners"}})
add("ed059",{"status":"ok","title":"Which problems are startups going after?",
 "t":{16:"GPS\nloss",11:"Lost\ntime",14:"Hidden\nore",
 21:"Pain points change sharply by buyer.\n\nBroad statements quickly mislead.\nSo we split defense forces, telecom and grid operators, miners, hospitals and labs and chipmakers before scoring.",
 13:"Chip\nfaults",12:"Brain\nscans",15:"Bulky\nunits",18:"Blind\nsubs",19:"Radio\nnoise"}})
add("ed060",{"status":"ok","title":"How will we proceed?",
 "note":"We break the market down before scoring because the same sensor creates very different value and risk for a navy, a telecom operator or a hospital.",
 "t":{9:"😣\nPAIN POINTS\n\nWe list each group's main pains and score them to rank them.",
 6:"🎯\nGOAL\n\nFind the pains that matter most in quantum sensing, and who feels them.",
 7:"🏷️\nCATEGORIES\n\nWe split the market by buyer, because who pays and what they need differ.",
 8:"👥\nSEGMENTS\n\nFor each buyer, we list the people who decide, pay, use and check sensors."}})
SEG=[("DEFENSE FORCES","Defense forces","DEFENSE\nFORCES","Navies, air forces and armies that need navigation and exact time when GPS is jammed","Navies, air forces and armies that need navigation\nand exact time when GPS is jammed"),
("TELECOM AND GRID OPERATORS","Telecom and grid operators","TELECOM AND\nGRID OPERATORS","Phone networks, power grids and data centers that need exact time if satellites fail","Phone networks, power grids and data centers that\nneed exact time if satellites fail"),
("MINING AND ENERGY FIRMS","Mining and energy firms","MINING AND\nENERGY FIRMS","Miners, oil and gas firms and builders that need to see what lies under the ground","Miners, oil and gas firms and builders that need\nto see what lies under the ground"),
("HOSPITALS AND RESEARCH LABS","Hospitals and research labs","HOSPITALS AND\nRESEARCH LABS","Hospitals, brain centers and labs that scan brains and study cells and new materials","Hospitals, brain centers and labs that scan brains\nand study cells and new materials"),
("CHIPMAKERS","Chipmakers","CHIP\nMAKERS","Chip factories and their suppliers that must find hidden faults inside advanced chips","Chip factories and their suppliers that must find\nhidden faults inside advanced chips")]
add("ed061",{"status":"ok","title":"Which categories will we use?",
 "note":"We split the market into five types of buyer. They differ enough in who pays, what proof they need and how they buy to score their pain points separately.",
 "t":{7:SEG[0][2],9:SEG[1][2],11:SEG[2][2],13:SEG[3][2],15:SEG[4][2],6:SEG[0][3],8:SEG[1][3],10:SEG[2][3],12:SEG[3][3],14:SEG[4][3],17:"",16:""},"holes_ok":True})
ROLES=[
 [("NAVY\nNAVIGATORS","🧭","They need to know where a ship or a submarine is for days at sea, with no GPS and no signal to give it away"),
  ("AIR FORCE\nCREWS","🛰️","They need a navigation backup that keeps aircraft and drones on course when GPS is jammed or spoofed"),
  ("PROGRAM\nOFFICES","📋","They need sensors that pass long field tests and fit budgets planned years ahead, before they order"),
  ("TEST\nENGINEERS","🔧","They need units that survive shock, heat and vibration on real platforms, not only in a quiet lab"),
  ("DEFENSE\nPRIMES","🏭","They need suppliers that can build sensors in volume and fit them into their planes, ships and drones")],
 [("NETWORK\nENGINEERS","📡","They need exact time across cell towers and fiber links, so calls and data keep flowing if GPS time fails"),
  ("GRID\nOPERATORS","⚡","They need precise time to protect power lines and sync the grid, since a time error can trip equipment"),
  ("DATA CENTER\nTEAMS","🖥️","They need clocks that keep servers and trades in sync for days after satellite time signals are lost"),
  ("SECURITY\nTEAMS","🛡️","They need to protect timing from jamming and spoofing, which can be used to attack critical networks"),
  ("BUYING\nMANAGERS","💰","They need clocks that fit standard racks and cost less than the outages they help the network avoid")],
 [("EXPLORING\nGEOLOGISTS","🔍","They need to map ore bodies and rock layers from the surface before they pay for costly drilling"),
  ("MINE\nMANAGERS","🏭","They need to cut the number of dry holes and find deposits faster, since each drill hole costs a lot"),
  ("SURVEY\nCREWS","🚗","They need sensors that run on trucks, drones and ships in rough terrain and in bad weather all day"),
  ("CIVIL\nENGINEERS","🏗️","They need to find voids, old mines and pipes under streets before they dig, to avoid collapses"),
  ("ENERGY\nTEAMS","🔋","They need to watch reservoirs and stored carbon underground over years, with no new drilling")],
 [("NEURO\nSCIENTISTS","🧠","They need to see brain activity in people who move, such as children and patients with epilepsy"),
  ("HOSPITAL\nBUYERS","🏥","They need scanners that cost less to run than helium-cooled systems and fit in a normal room"),
  ("CLINICAL\nTEAMS","🩺","They need clear brain maps to plan epilepsy surgery and to follow head injuries over time"),
  ("LAB\nRESEARCHERS","🔬","They need tools that map magnetism and currents at tiny scales in cells and new materials"),
  ("GRANT\nMANAGERS","📋","They need proof that a costly new instrument will serve many teams before funding it")],
 [("FAILURE\nANALYSTS","🔍","They need to find the exact spot where a fault hides inside a stacked chip, without cutting it open"),
  ("YIELD\nENGINEERS","📈","They need to catch faults early on the line, since each bad wafer wastes costly machine time"),
  ("PACKAGING\nTEAMS","📦","They need to check the hidden links inside chips stacked in 3D, which old tools cannot see well"),
  ("FAB\nMANAGERS","🏭","They need inspection tools that keep up with the speed of the line and fit into the clean room"),
  ("TOOL\nBUYERS","💰","They need proof that a new tool finds more faults than current ones, before they pay for a fleet")]]
PAINS=[
 ["They see GPS jammed and spoofed near every conflict","They lose position at sea and under water for days","They wait years for trials to turn into orders","They find units too big for small drones and craft","They see sensors lose accuracy on moving platforms","They lack maps of gravity and magnetism in places","They must keep suppliers that meet export rules"],
 ["They depend on GPS time for every single cell tower","They face outages when satellite time is jammed","They need clocks that hold time for many days","They pay a lot for today's best atomic clocks","They must fit new clocks into standard racks","They see timing attacks on their critical networks","They must meet strict rules on network timing"],
 ["They pay for many drill holes that find nothing","They cannot see deep ore bodies from the surface","They need sensors that run in very rough terrain","They face slow survey work over large areas","They find hidden voids only after a collapse","They must watch stored carbon over many years","They see new tools priced far above old ones"],
 ["They pay for helium to cool today's brain scanners","They cannot scan children who move during tests","They need room for big and costly shielded rooms","They wait a long time for scarce brain scans","They lack tools to map currents in tiny samples","They must prove a new tool works for clinicians","They face long approval paths for new scanners"],
 ["They cannot see faults hidden in stacked chips","They lose wafers when faults are caught too late","They must cut chips open to find some faults","They need tools fast enough for the factory line","They see old tools fail on new 3D packages","They pay a lot for each new inspection tool bought","They need proof that a new tool beats old ones"]]
ROWS=[
 [("GPS is jammed and spoofed near every single conflict zone",[3,3,3,2,3],"CRITICAL"),("Ships and subs lose their position for days out at sea",[3,2,2,2,2],"CRITICAL"),("Field trials take years before they turn into real orders",[1,1,3,1,3],"MAJOR"),("Units are still too big and too heavy for small drones",[1,3,2,3,3],"MAJOR"),("Sensors lose accuracy on moving ships, planes and drones",[3,3,3,3,2],"CRITICAL"),("Gravity and magnetic maps are missing in many places",[3,3,1,2,1],"HIGH"),("Suppliers must meet strict export and security rules today",[1,1,3,1,3],"HIGH")],
 [("Every cell tower depends on GPS satellites for its time",[3,1,2,2,2],"CRITICAL"),("Network outages follow when satellite time is jammed",[3,3,3,3,1],"CRITICAL"),("Backup clocks must hold exact time for many days alone",[3,2,3,1,1],"MAJOR"),("Today's best atomic clocks cost a lot for each single unit",[1,1,1,1,3],"HIGH"),("New clocks must fit into the standard server racks in use",[2,1,3,1,2],"MAJOR"),("Timing attacks threaten phone networks and power grids",[2,2,1,3,1],"MAJOR"),("Strict rules apply to the timing used in phone networks",[2,3,1,2,1],"HIGH")],
 [("Many drill holes cost a lot of money and find nothing at all",[3,3,1,1,1],"CRITICAL"),("Deep ore bodies cannot be seen from the surface today",[3,2,1,1,2],"CRITICAL"),("Sensors must keep running in rough terrain and bad weather",[1,1,3,1,1],"MAJOR"),("Survey work over very large areas is slow and costly",[2,3,3,1,1],"MAJOR"),("Hidden voids under the ground are found only after a collapse",[1,1,1,3,1],"HIGH"),("Carbon stored underground must be watched for many years",[1,1,1,1,3],"HIGH"),("New survey tools are priced far above the old ones today",[1,3,1,2,2],"HIGH")],
 [("Today's big brain scanners need costly liquid helium",[1,3,1,1,2],"MAJOR"),("Children who move cannot be scanned well in big scanners",[3,1,3,1,1],"CRITICAL"),("Shielded scan rooms take a lot of space and a lot of money",[1,3,1,1,2],"HIGH"),("Patients wait a long time for scarce brain scan slots",[2,2,3,1,1],"MAJOR"),("Few tools can map currents and fields in tiny samples",[1,1,1,3,2],"HIGH"),("A new scanner must prove its value to busy clinicians",[2,3,3,1,3],"MAJOR"),("New scanners face long approval paths before clinic use",[1,3,3,1,2],"HIGH")],
 [("Faults stay hidden deep inside chips stacked in layers",[3,2,3,1,1],"CRITICAL"),("Costly wafers are lost when faults are caught too late",[2,3,1,3,2],"CRITICAL"),("Some faults are found only by cutting the chips open",[3,2,2,1,1],"MAJOR"),("Inspection tools must keep up with the speed of the line",[1,3,1,3,2],"MAJOR"),("Old tools fail to see inside the new 3D chip packages",[3,2,3,1,1],"CRITICAL"),("Each new inspection tool costs a lot to buy and to run",[1,1,1,2,3],"HIGH"),("A new tool must prove that it beats the old ones on the line",[2,2,2,2,3],"HIGH")]]
for k,(cap,name,_,_,intro) in enumerate(SEG,1):
    add(f"ed062-s{k}",{"status":"ok","t":{6:"PAIN POINTS",3:cap,5:intro}})
    R=ROLES[k-1]; t={27:cap}
    for (lab,ic,txt),kl,ki,kt in zip(R,[5,8,11,14,17],[20,21,22,23,24],[7,10,13,16,19]): t[kl]=lab; t[ki]=ic; t[kt]=txt
    add(f"ed063-s{k}",{"status":"ok","title":"Who needs quantum sensing?","note":"We focus on the five groups inside these buyers that choose, pay for, use and check quantum sensors.","t":t})
    t={13:cap}; t.update({14+i:p for i,p in enumerate(PAINS[k-1])})
    add(f"ed064-s{k}",{"status":"ok","title":"What are these customers' strongest pain points?","note":"We prioritized problems that recur in defense programs, trial reports, company releases and market surveys on quantum sensors.","t":t})
    add(f"ed065-s{k}",{"status":"ok","title":"Which pains deserve attention first?","subtitle":name,"icons":[r[1] for r in R],
      "rows":[{"pain":p,"s":s,"p":pr} for p,s,pr in ROWS[k-1]],
      "note":["Every stakeholder is different, and this table is a simplified view based on reports and studies","It gives a starting point, not a checklist, so priorities should be checked with real buyers"]})
open("/home/claude/nmp-decks/decks/quantum-sensing/research/202-quantum-sensing-deck-04-pain-points-results-research-2026-11-27.md","w").write("\n".join(out))
