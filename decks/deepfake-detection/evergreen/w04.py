import yaml
out=["# deepfake detection, chapter 04 Pain points (evergreen, written by Claude, 27 Nov 2026)\n"]
def add(i,d):
    out.append(f"### {i}\n```yaml\n"+yaml.safe_dump(d,allow_unicode=True,sort_keys=False,width=1000)+"```\n")
add("ed054",{"status":"ok","title":"What are the pain points of yesterday vs. today?",
 "note":"We grouped the market into phases: early face swaps, the first voice scams, cheap generative AI, and today's fraud at scale. We used regulator alerts, fraud reports and studies.",
 "t":{6:"2017 - 2019\nFace swap videos spread online, but they were crude and rare, and detection was mostly a research topic funded by DARPA",
 7:"2019 - 2022\nA cloned CEO voice tricked a UK energy firm into wiring €220,000, but most companies still saw deepfakes as a celebrity issue",
 8:"2023 - 2024\nCheap AI tools made fake faces and voices easy, and a fake video call cost Arup about $25.6M, while few firms had any defense",
 9:"TODAY\nDeepfake attacks hit banks, call centers and hiring every day, yet only a small share of firms use a detection tool built for it",
 10:"?\nReal-time fakes may become impossible to spot by eye, so checks must run inside every call, selfie and upload, at very low cost"}})
add("ed055",{"status":"ok","title":"Which old problems are now behind us?",
 "note":"We treat these as problems that new tools have removed for many buyers. They do not mean that every deepfake is now caught, or that detectors work in every condition.",
 "t":{5:"Checking a suspicious video meant sending it to a lab and waiting days",7:"Forensic tools from Sensity, Reality Defender and GetReal now score a file in minutes, with a report",
 8:"Call centers had no way to tell a cloned voice from a real customer",10:"Pindrop and other voice tools now flag synthetic voices during the call, inside the systems agents use",
 11:"Selfie checks could be fooled by a photo, a mask or a replayed video",13:"Liveness checks from Incode, iProov and others now spot many fake faces in under a second at sign-up",
 14:"Video meetings had no check that each person on screen was real",16:"GetReal, Reality Defender and Resemble AI now run checks inside Zoom, Teams and Webex meetings",
 17:"Platforms had no shared way to show where a photo or a video came from",19:"Content Credentials from the C2PA now attach a signed record of origin to media from many cameras and apps",
 20:"Victims of fake intimate images had no US right to quick removal",22:"The TAKE IT DOWN Act now makes US platforms remove such images within 48 hours of a valid request"}})
add("ed056",{"status":"ok","title":"What problems do all players face?","page":"1/2",
 "note":"We kept the problems that come back in detector tests, fraud reports and buyer surveys. We skipped generic startup issues and focused on spotting AI-made media.",
 "t":{25:"New AI models\nbeat old detectors",23:"You need\nfresh data",8:"Lab scores fall\nin real use",6:"You need real-world\ntests",
 29:"False alarms\nblock real users",27:"You need low\nerror rates",12:"Low quality\nhides clues",10:"You need robust\nmodels",
 33:"Live checks must\nbe very fast",31:"You need low\nlatency",16:"Watermarks only\ncover some tools",14:"You need checks\nwithout marks",
 37:"Verdicts must\nhold up in court",35:"You need clear\nreasons",20:"Attackers test\nevery defense",18:"You need constant\nupdates"}})
add("ed057",{"status":"ok","title":"What problems do all players face?","page":"2/2",
 "note":"We separated the problems of detecting fakes from those of selling detection. The second set matters once a tool works, because budgets, platforms, rules and rivals still decide who wins.",
 "t":{25:"Few firms buy\na dedicated tool",23:"You need a\nclear budget",8:"Big platforms add\ndetection for free",6:"You need a\nclear edge",
 29:"Buyers want it\ninside their tools",27:"You need many\nplug-ins",12:"Rules differ by\ncountry and state",10:"You need legal\nclarity",
 33:"Voice data raises\nprivacy claims",31:"You need clear\nconsent",16:"Losses are hard\nto prove upfront",14:"You need ROI\nproof",
 37:"Hype hurts trust\nin accuracy claims",35:"You need open\ntest results",20:"Big security firms\nbuy the leaders",18:"You need partner\nchannels"}})
add("ed059",{"status":"ok","title":"Which problems are startups going after?",
 "t":{16:"Voice\nclones",11:"Fake\nselfies",14:"CEO\nfraud",
 21:"Pain points change sharply by buyer.\n\nBroad statements quickly mislead.\nSo we split banks and fintechs, contact centers, agencies, newsrooms and platforms and security teams before scoring.",
 13:"Fake\nhires",12:"False\nnews",15:"Slow\nchecks",18:"Fake\nnudes",19:"False\nalarms"}})
add("ed060",{"status":"ok","title":"How will we proceed?",
 "note":"We break the market down before scoring because the same tool creates very different value and risk for a bank, a call center or a newsroom.",
 "t":{9:"😣\nPAIN POINTS\n\nWe list each group's main pains and score them to rank them.",
 6:"🎯\nGOAL\n\nFind the pains that matter most in deepfake detection, and who feels them.",
 7:"🏷️\nCATEGORIES\n\nWe split the market by buyer, because who pays and what they need differ.",
 8:"👥\nSEGMENTS\n\nFor each buyer, we list the people who decide, pay, use and check tools."}})
SEG=[("BANKS AND FINTECHS","Banks and fintechs","BANKS AND\nFINTECHS","Banks, payment apps and lenders that check new clients, logins and large transfers","Banks, payment apps and lenders that check\nnew clients, logins and large transfers"),
("CONTACT CENTERS","Contact centers","CONTACT\nCENTERS","Call centers of banks, insurers and retailers that verify callers before account changes","Call centers of banks, insurers and retailers that\nverify callers before account changes"),
("GOVERNMENT AGENCIES","Government agencies","GOVERNMENT\nAGENCIES","Defense, police, election and public agencies that check media, evidence and identities","Defense, police, election and public agencies that\ncheck media, evidence and identities"),
("NEWSROOMS AND PLATFORMS","Newsrooms and platforms","NEWSROOMS AND\nPLATFORMS","Media groups and social apps that check what people upload and share every day","Media groups and social apps that check\nwhat people upload and share every day"),
("SECURITY TEAMS","Corporate security teams","SECURITY\nTEAMS","Company security teams that protect calls, meetings, payments and hiring from fakes","Company security teams that protect calls,\nmeetings, payments and hiring from fakes")]
add("ed061",{"status":"ok","title":"Which categories will we use?",
 "note":"We split the market into five types of buyer. They differ enough in who pays, what proof they need and how they buy to score their pain points separately.",
 "t":{7:SEG[0][2],9:SEG[1][2],11:SEG[2][2],13:SEG[3][2],15:SEG[4][2],6:SEG[0][3],8:SEG[1][3],10:SEG[2][3],12:SEG[3][3],14:SEG[4][3],17:"",16:""},"holes_ok":True})
ROLES=[
 [("FRAUD\nTEAMS","🛡️","They need to stop fake faces and voices before money moves, without blocking real clients at each step"),
  ("ONBOARDING\nTEAMS","💳","They need selfie and ID checks that catch deepfakes in seconds, so new clients do not give up at sign-up"),
  ("COMPLIANCE\nOFFICERS","📋","They need records that show regulators how each check worked, and reports of fraud filed on time"),
  ("PAYMENT\nTEAMS","💰","They need to confirm that a request for a large transfer really comes from the client or the CFO"),
  ("RISK\nLEADERS","📊","They need proof that a tool cuts fraud losses by more than it costs, before it gets a yearly budget")],
 [("CALL CENTER\nAGENTS","📞","They need a clear alert when a caller's voice is synthetic, so they do not change an account for a fraudster"),
  ("CENTER\nMANAGERS","🏢","They need checks that do not slow each call, since each extra second costs money across millions of calls"),
  ("FRAUD\nANALYSTS","🔍","They need to see which calls were flagged and why, to find fraud rings that call again and again"),
  ("IT\nTEAMS","🔌","They need tools that plug into their phone systems and call platforms without a long and costly project"),
  ("PRIVACY\nTEAMS","🔒","They need consent and data rules for recorded voices, since voice analysis has led to lawsuits")],
 [("DEFENSE\nANALYSTS","🛰️","They need to check fake images and videos fast in a crisis, when a false clip can shape public reactions"),
  ("POLICE\nDETECTIVES","🔍","They need reports that show how a file was faked, written so that a court can accept the evidence"),
  ("ELECTION\nOFFICIALS","🏛️","They need to spot fake videos of candidates before a vote and to warn the public in a clear way"),
  ("PROCUREMENT\nOFFICERS","📋","They need approved vendors with security clearances, sold through contracts their agency can use"),
  ("CHILD SAFETY\nUNITS","🛡️","They need to sort real abuse images from AI-made ones, since reports of AI images are rising fast")],
 [("FACT\nCHECKERS","📰","They need to prove a viral video is fake within hours, before it spreads further than any correction"),
  ("TRUST AND\nSAFETY TEAMS","🛡️","They need to scan millions of uploads a day for fake media, at a cost that fits their budget"),
  ("EDITORS","✍️","They need to know a photo or a clip is real before they publish it, since one mistake hurts trust"),
  ("LEGAL\nTEAMS","⚖️","They need to meet takedown rules, like the 48-hour limit for fake intimate images in the US"),
  ("PRODUCT\nTEAMS","📱","They need to label AI media and show where content came from, without slowing down users' posts")],
 [("SECURITY\nLEADERS","🛡️","They need to protect executives, meetings and payments from impersonation without adding friction"),
  ("FINANCE\nTEAMS","💰","They need to confirm that a payment request on a call or a video really comes from their CFO"),
  ("HR AND\nRECRUITERS","💼","They need to check that remote job candidates are real people and not deepfakes before hiring"),
  ("IT AND HELP\nDESKS","💻","They need to confirm that a caller asking for a password reset is really the employee they claim"),
  ("EXECUTIVES","👔","They need to stop fake copies of their face and voice from being used to trick staff and partners")]]
PAINS=[
 ["They see deepfake attempts rise at account sign-up","They lose new clients when checks feel too slow","They face fake selfies that pass basic checks","They see fraud losses rise with each new AI tool","They must report deepfake fraud to regulators","They find it hard to prove that a tool pays back","They struggle to keep up with new attack methods"],
 ["They hear cloned voices that sound like real clients","They cannot slow down millions of calls with checks","They miss fraud rings that call again and again","They face lawsuits over recording and voice data","They find it hard to connect old phone systems","They see agents fooled by calm and urgent fakes","They lack proof of losses avoided each year"],
 ["They must judge viral fakes fast during a crisis","They need evidence that a judge and court accept","They face fake videos of candidates before votes","They buy slowly through long public contracts","They see AI images flood child safety reports","They need vendors with a federal security approval","They struggle to train their staff on new fakes"],
 ["They have only hours to stop a fake from spreading","They scan many millions of new uploads every day","They face strict legal limits on takedown times","They see watermarks missing on most AI content","They risk publishing a fake clip by mistake","They pay a lot for each item that gets checked","They face false alarms on real photos and clips"],
 ["They see fake CFOs order urgent large payments","They face fake candidates in remote job interviews","They see help desks tricked into password resets","They lack a budget line for deepfake defense","They need checks inside Zoom, Teams and Webex","They see their executives cloned for phone scams","They find it hard to train every single employee"]]
ROWS=[
 [("Deepfake attempts at account sign-up keep rising each year",[3,3,2,1,3],"CRITICAL"),("Clients give up when identity checks feel too slow",[1,3,1,1,2],"MAJOR"),("Fake selfies get past basic liveness checks today",[3,3,2,1,2],"CRITICAL"),("Fraud losses rise with each new AI generation tool",[3,1,2,3,3],"CRITICAL"),("Deepfake fraud must be reported to regulators",[2,1,3,1,2],"HIGH"),("It is hard to prove a detection tool pays back",[2,1,1,1,3],"HIGH"),("New attack methods appear faster than updates",[3,2,1,2,2],"MAJOR")],
 [("Cloned voices sound just like real clients on calls",[3,2,3,1,1],"CRITICAL"),("Checks cannot slow down millions of calls a year",[2,3,1,3,1],"MAJOR"),("Fraud rings call again and again with new voices",[2,2,3,1,1],"MAJOR"),("Recording and voice analysis can lead to lawsuits",[1,2,1,2,3],"HIGH"),("Old phone systems are hard to connect to new tools",[1,2,1,3,1],"HIGH"),("Calm or urgent fake callers fool trained agents",[3,2,2,1,1],"CRITICAL"),("Losses avoided are hard to prove to the board each year",[1,3,2,1,1],"HIGH")],
 [("Viral fakes must be judged fast during a crisis",[3,1,3,1,2],"CRITICAL"),("Evidence must be accepted by a court or a tribunal",[2,3,1,1,3],"MAJOR"),("Fake videos of candidates appear before votes",[2,1,3,1,1],"CRITICAL"),("Long contracts slow the purchase of new tools",[1,1,1,3,1],"HIGH"),("AI-made images flood child safety reports each year",[1,3,1,1,3],"CRITICAL"),("Vendors need security approval to work with agencies",[2,1,1,3,2],"HIGH"),("Staff struggle to keep up with new kinds of fakes",[2,2,2,1,2],"HIGH")],
 [("A fake must be stopped within hours, before it spreads",[3,3,3,2,2],"CRITICAL"),("Millions of uploads must be scanned every day",[1,3,1,1,3],"MAJOR"),("Laws set short limits on takedown times for platforms",[1,3,1,3,2],"MAJOR"),("Most AI content carries no watermark to read",[3,3,2,1,3],"HIGH"),("A fake can be published by mistake and hurt trust",[3,1,3,2,1],"CRITICAL"),("Each item checked adds to a large yearly bill",[1,3,1,1,2],"HIGH"),("False alarms flag real photos and real clips",[3,2,3,1,2],"MAJOR")],
 [("Fake CFOs on calls order urgent large payments",[3,3,1,1,3],"CRITICAL"),("Fake candidates slip into remote hiring processes",[2,1,3,2,1],"CRITICAL"),("Help desks are tricked into giving password resets",[3,1,1,3,1],"MAJOR"),("No budget line exists yet for deepfake defense",[3,2,1,1,2],"HIGH"),("Checks must run inside Zoom, Teams and Webex",[2,1,2,3,2],"MAJOR"),("Executives are cloned to scam staff and partners",[3,2,1,1,3],"MAJOR"),("Training every employee is slow and very costly",[2,1,2,2,1],"HIGH")]]
for k,(cap,name,_,_,intro) in enumerate(SEG,1):
    add(f"ed062-s{k}",{"status":"ok","t":{6:"PAIN POINTS",3:cap,5:intro}})
    R=ROLES[k-1]; t={27:cap}
    for (lab,ic,txt),kl,ki,kt in zip(R,[5,8,11,14,17],[20,21,22,23,24],[7,10,13,16,19]): t[kl]=lab; t[ki]=ic; t[kt]=txt
    add(f"ed063-s{k}",{"status":"ok","title":"Who needs deepfake detection?","note":"We focus on the five groups inside these buyers that choose, pay for, use and check detection tools.","t":t})
    t={13:cap}; t.update({14+i:p for i,p in enumerate(PAINS[k-1])})
    add(f"ed064-s{k}",{"status":"ok","title":"What are these customers' strongest pain points?","note":"We prioritized problems that recur in fraud reports, regulator alerts, detector tests and company releases on deepfakes.","t":t})
    add(f"ed065-s{k}",{"status":"ok","title":"Which pains deserve attention first?","subtitle":name,"icons":[r[1] for r in R],
      "rows":[{"pain":p,"s":s,"p":pr} for p,s,pr in ROWS[k-1]],
      "note":["Every stakeholder is different, and this table is a simplified view based on reports and studies","It gives a starting point, not a checklist, so priorities should be checked with real buyers"]})
open("/home/claude/nmp-decks/decks/deepfake-detection/research/147-deepfake-detection-deck-04-pain-points-results-research-2026-11-27.md","w").write("\n".join(out))
