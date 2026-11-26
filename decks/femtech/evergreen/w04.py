import yaml
out=["# FemTech, chapter 04 Pain points (evergreen, written by Claude, 26 Nov 2026)\n"]
def add(i,d):
    out.append(f"### {i}\n```yaml\n"+yaml.safe_dump(d,allow_unicode=True,sort_keys=False,width=1000)+"```\n")
add("ed054",{"status":"ok","title":"What are the pain points of yesterday vs. today?",
 "note":"We grouped the market into phases: the first cycle apps, the rise of fertility benefits, the turn to menopause care, and today's payment gap. We used company filings, FDA decisions and health reports.",
 "t":{6:"2013 - 2019\nPeriod and fertility apps reached millions of women, but women's health got little funding and most care stayed in clinics",
 7:"2020 - 2022\nVirtual care and employer fertility benefits grew fast, but the end of Roe v. Wade made women fear sharing their health data",
 8:"2023 - 2025\nThe FDA approved the first pill sold without a prescription and menopause clinics grew, while many apps struggled to earn money",
 9:"TODAY\nWomen have many more tools, but who pays is still the hard part, as menopause and pelvic care are often left out of health plans",
 10:"?\nAt-home tests and AI may find conditions earlier, but too few studies of women's bodies still slow new drugs, devices and tests"}})
add("ed055",{"status":"ok","title":"Which old problems are now behind us?",
 "note":"We treat these as problems that new products and benefits have removed for many women. They do not mean that care is now easy to reach or paid for everywhere.",
 "t":{5:"Tracking a cycle meant a paper calendar and guesses about fertile days",7:"Apps such as Flo, Clue and Natural Cycles now track cycles and predict fertile days for tens of millions of women",
 8:"Almost every couple paid for fertility treatment out of their own pocket",10:"Many large employers now pay for IVF and egg freezing through benefits from Progyny, Carrot or Maven Clinic",
 11:"In the US, birth control pills always required a visit to a doctor first",13:"Opill became the first US birth control pill sold without a prescription, approved by the FDA in July 2023",
 14:"Breast pumps were loud and wired, so mothers had to sit still to pump",16:"Wearable pumps from Elvie and Willow fit inside a bra, so mothers can pump quietly while they move and work",
 17:"Women had few doctors trained to treat the symptoms of menopause",19:"Virtual clinics such as Midi Health now offer menopause care by video, with visits billed to health insurance",
 20:"Pelvic floor training meant repeated visits to a specialist clinic",22:"FDA-cleared home devices such as Elvie Trainer guide pelvic floor exercises and track each session's progress"}})
add("ed056",{"status":"ok","title":"What problems do all players face?","page":"1/2",
 "note":"We kept the problems that come back in health reports, company filings and studies on women's health. We skipped generic startup issues and focused on care built around women's biology.",
 "t":{25:"Few trials study\nwomen's bodies",23:"You need female\nclinical data",8:"Payers often\nrefuse coverage",6:"You need a\npayer path",
 29:"Symptoms are\noften dismissed",27:"You need doctor\nsupport",12:"Care is split\nacross doctors",10:"You need linked\ncare paths",
 33:"FDA reviews\ncan take years",31:"You need clear\napprovals",16:"Fewer ob-gyns\nwork in rural areas",14:"You need more\nproviders",
 37:"Studies take\nlong to recruit",35:"You need solid\nproof",20:"Women often pay\nout of pocket",18:"Prices must fit\nhousehold budgets"}})
add("ed057",{"status":"ok","title":"What problems do all players face?","page":"2/2",
 "note":"We separated the problems of building care for women from those of selling it. The second set matters once a product works, because trust, data, funding and payers still decide who wins.",
 "t":{25:"Health data raises\nprivacy fears",23:"You must protect\nuser data",8:"Rules differ by\nstate and country",6:"You need legal\nclarity",
 29:"Few deals go to\nwomen's health",27:"You need patient\ninvestors",12:"Users drop free\napps quickly",10:"You need paying\nusers",
 33:"Employers trim\nbenefit budgets",31:"You need proof\nof savings",16:"Big platforms add\nsimilar tools",14:"You need a\nclear edge",
 37:"Ads on women's\nhealth get blocked",35:"You need ways to\nreach women",20:"Few doctors are\ntrained in menopause",18:"You need trained\nclinicians"}})
add("ed059",{"status":"ok","title":"Which problems are startups going after?",
 "t":{16:"Late\ndiagnosis",11:"High\ncosts",14:"No\ncoverage",
 21:"Pain points change sharply by buyer.\n\nBroad statements quickly mislead.\nSo we split large employers, women in midlife, IVF clinics, expectant mothers and ob-gyn practices before scoring.",
 13:"Data\nprivacy",12:"Long\nwaits",15:"Few\nexperts",18:"Scarce\nresearch",19:"Split\ncare"}})
add("ed060",{"status":"ok","title":"How will we proceed?",
 "note":"We break the market down before scoring because the same product creates very different value and risk for an employer, a clinic or a woman who pays herself.",
 "t":{9:"😣\nPAIN POINTS\n\nWe list each group's main pains and score them to rank them.",
 6:"🎯\nGOAL\n\nFind the pains that matter most in FemTech, and who feels them.",
 7:"🏷️\nCATEGORIES\n\nWe split the market by buyer, because who pays and what they need differ.",
 8:"🧑‍🤝‍🧑\nSEGMENTS\n\nFor each buyer, we list the people who decide, pay, use and check products."}})
SEG=[("LARGE EMPLOYERS","Large employers","LARGE\nEMPLOYERS","Companies that pay for fertility, maternity and menopause benefits for their staff","Companies that pay for fertility, maternity\nand menopause benefits for their staff"),
("WOMEN IN MIDLIFE","Women in midlife","WOMEN IN\nMIDLIFE","Women of about 40 to 60 facing perimenopause, menopause and midlife health risks","Women of about 40 to 60 facing perimenopause,\nmenopause and midlife health risks"),
("IVF CLINICS","IVF clinics","IVF\nCLINICS","Fertility clinics and lab networks that run IVF, egg freezing and embryo tests","Fertility clinics and lab networks that run IVF,\negg freezing and embryo tests"),
("EXPECTANT MOTHERS","Expectant mothers","EXPECTANT\nMOTHERS","Women who are pregnant or just gave birth, from the first test to the postpartum year","Women who are pregnant or just gave birth, from\nthe first test to the postpartum year"),
("OB-GYN PRACTICES","Ob-gyn practices","OB-GYN\nPRACTICES","Obstetrics and gynecology practices and hospital units that care for women","Obstetrics and gynecology practices and\nhospital units that care for women")]
add("ed061",{"status":"ok","title":"Which categories will we use?",
 "note":"We split the market into five types of buyer. They differ enough in who pays, what proof they need and how they buy to score their pain points separately.",
 "t":{7:SEG[0][2],9:SEG[1][2],11:SEG[2][2],13:SEG[3][2],15:SEG[4][2],6:SEG[0][3],8:SEG[1][3],10:SEG[2][3],12:SEG[3][3],14:SEG[4][3],17:"",16:""},"holes_ok":True})
ROLES=[
 [("BENEFITS\nLEADERS","💼","They need benefits that help hire and keep women, at a cost per employee the company can carry each year"),
  ("HR AND\nPEOPLE TEAMS","👥","They need programs staff actually use, with simple sign-up and support across every country they work in"),
  ("FINANCE\nTEAMS","💰","They need proof that fertility and maternity benefits cut costs, such as fewer twins and NICU stays"),
  ("BENEFIT\nBROKERS","🤝","They need vendors with clear prices, outcome data and contracts they can compare and renew each year"),
  ("FEMALE\nEMPLOYEES","👔","They need care for fertility, pregnancy and menopause that is private, quick to reach and fully covered")],
 [("WOMEN IN\nMIDLIFE","🧑","They need clear answers on hot flashes, sleep and mood, and a treatment plan that works for their body"),
  ("PRIMARY CARE\nDOCTORS","🩺","They need simple guidance on hormone therapy and new drugs, since few were trained in menopause care"),
  ("MENOPAUSE\nCLINICIANS","🏥","They need tools to follow many patients at once, track symptoms and adjust doses between video visits"),
  ("HEALTH\nPLANS","🛡️","They need proof that menopause care lowers other costs, such as heart, bone and mental health claims"),
  ("LARGE\nEMPLOYERS","🏢","They need to keep experienced women at work, as many cut hours or quit when symptoms are not treated")],
 [("FERTILITY\nDOCTORS","🩺","They need better odds of a live birth per cycle and tools that help choose the embryo most likely to succeed"),
  ("LAB\nSTAFF","🔬","They need steady lab results with fewer manual steps, as each lab error can cost a patient her embryos"),
  ("CLINIC\nOWNERS","💼","They need to treat more patients with the same staff and labs, at prices payers and patients accept"),
  ("PATIENT\nTEAMS","💬","They need to guide anxious patients through each step, with clear costs, dates and results by message"),
  ("INSURERS AND\nEMPLOYERS","💳","They need proof that their money buys healthy births, with fewer twins and fewer failed cycles over time")],
 [("EXPECTANT\nMOTHERS","🧑","They need to know what is normal week by week and to reach a clinician fast when something feels wrong"),
  ("PARTNERS AND\nFAMILIES","👥","They need simple ways to help with care, feeding and sleep, and to spot warning signs after the birth"),
  ("MIDWIVES AND\nNURSES","🩺","They need to follow blood pressure, sugar and mood at home between visits, without more paperwork"),
  ("HOSPITAL\nTEAMS","🏥","They need to cut the risk of preventable emergencies and readmissions after birth, mostly in the first weeks"),
  ("HEALTH\nPLANS","🛡️","They need fewer preterm births and NICU stays, the costliest part of pregnancy care for the plans")],
 [("OB-GYN\nDOCTORS","🩺","They need to see more patients in less time, with fewer missed problems and less paperwork after each visit"),
  ("PRACTICE\nMANAGERS","💼","They need care that is billed and paid on time, with staff costs kept in check as visits keep growing"),
  ("NURSES AND\nMEDICAL STAFF","👥","They need simple tools for screening, follow-ups and patient messages that fit busy clinic days"),
  ("IMAGING\nDOCTORS","🔬","They need tools that flag breast and pelvic findings early, so each image gets a careful and timely review"),
  ("WOMEN\nPATIENTS","🧑","They need short waits, clear answers and care that takes their symptoms seriously from the first visit")]]
PAINS=[
 ["They see fertility benefit costs rise each year","They cannot easily prove a return on women's benefits","They find employees in some countries left uncovered","They lose experienced women who quit during menopause","They juggle many vendors for each life stage","They worry about the privacy of employee health data","They see low use when staff do not know a benefit exists"],
 ["They wait years for a correct diagnosis of perimenopause","They find few doctors trained in menopause care","They get mixed messages about the safety of hormone therapy","They pay for many visits and treatments themselves","They miss work or cut hours when symptoms are severe","They find many apps that give generic advice only","They struggle to find care for sleep, mood and joint pain"],
 ["They see success rates fall sharply as patients get older","They face a shortage of trained lab embryologists","They run labs with many manual and error-prone steps","They lose patients who cannot pay for another cycle","They face rules that differ from one state to the next","They wait months for new tools to prove better births","They compete with large networks backed by private equity"],
 ["They wait weeks between visits with questions unanswered","They miss warning signs of high blood pressure at home","They lose support at the end of the first weeks after birth","They pay large bills even when they have health insurance","They live far from a hospital that delivers babies","They face postpartum depression that often goes untreated","They see risks of severe problems rise with each age band"],
 ["They see more patients with fewer ob-gyns per county","They lose time on notes, coding and insurance forms","They struggle to follow high-risk patients between visits","They face rising malpractice costs in obstetrics","They see payments that do not cover the time of each visit","They miss cancers and conditions that show late symptoms","They see wide gaps in care across rural areas"]]
ROWS=[
 [("Fertility benefit costs keep rising as more employees use them",[3,1,3,2,1],"CRITICAL"),("A return on women's health benefits is hard to prove with data",[3,2,3,2,1],"CRITICAL"),("Employees in some countries get no coverage for the same care",[2,3,1,2,3],"MAJOR"),("Experienced women quit or cut hours because of menopause symptoms",[3,3,2,1,3],"CRITICAL"),("Each life stage brings another vendor to choose and manage",[2,3,1,2,1],"HIGH"),("Employee health data must stay private and out of HR files",[2,3,1,1,3],"MAJOR"),("Many staff never use a benefit because they do not know it exists",[2,3,2,1,2],"HIGH")],
 [("Perimenopause often takes years to be correctly diagnosed",[3,3,2,1,1],"CRITICAL"),("Few doctors are trained to treat menopause symptoms with confidence",[3,3,2,1,1],"CRITICAL"),("Mixed messages on hormone therapy safety still worry many women",[3,2,2,1,1],"MAJOR"),("Many visits and treatments are paid out of pocket by women",[3,1,1,2,2],"MAJOR"),("Severe symptoms make women miss work or cut their hours",[3,1,1,2,3],"HIGH"),("Most apps give generic advice instead of a treatment plan",[2,1,2,1,1],"HIGH"),("Care for sleep, mood and joint pain is split across doctors",[3,2,3,2,1],"HIGH")],
 [("Success rates per cycle fall sharply as patients get older",[3,2,3,2,3],"CRITICAL"),("Trained embryologists are scarce and hard to keep in labs",[1,3,3,1,1],"MAJOR"),("Many manual lab steps raise the risk of costly human errors",[2,3,3,2,2],"CRITICAL"),("Patients drop out when they cannot pay for another cycle",[3,1,3,3,3],"MAJOR"),("Rules on IVF and embryos differ from one state to the next",[2,2,3,2,2],"HIGH"),("New tools take years to show that they lead to more births",[3,2,2,1,3],"HIGH"),("Large networks backed by private equity squeeze small clinics",[1,1,3,1,1],"HIGH")],
 [("Weeks pass between visits while questions go unanswered",[3,2,2,1,1],"HIGH"),("High blood pressure after birth is often missed at home",[3,2,3,3,3],"CRITICAL"),("Support stops after the first weeks, when many risks remain",[3,3,3,2,2],"MAJOR"),("Large bills arrive even for mothers with health insurance",[3,3,1,1,2],"MAJOR"),("Many women live far from a hospital that delivers babies",[3,2,2,3,2],"CRITICAL"),("Postpartum depression often goes unnoticed and untreated",[3,3,3,2,2],"CRITICAL"),("Risks of severe problems rise with the mother's age",[3,1,2,2,2],"HIGH")],
 [("Fewer ob-gyns must care for more patients in each county",[3,3,2,1,3],"CRITICAL"),("Notes, coding and insurance forms take time from patients",[3,3,3,1,2],"MAJOR"),("High-risk patients are hard to follow between visits",[3,1,3,2,3],"MAJOR"),("Malpractice costs in obstetrics keep rising year after year",[3,3,1,1,1],"HIGH"),("Payments often do not cover the real time of each visit",[3,3,1,1,1],"HIGH"),("Some cancers and conditions are found late, when symptoms show",[3,1,2,3,3],"CRITICAL"),("Rural areas show wide gaps in care for women and mothers",[2,2,2,1,3],"HIGH")]]
for k,(cap,name,_,_,intro) in enumerate(SEG,1):
    add(f"ed062-s{k}",{"status":"ok","t":{6:"PAIN POINTS",3:cap,5:intro}})
    R=ROLES[k-1]; t={27:cap}
    for (lab,ic,txt),kl,ki,kt in zip(R,[5,8,11,14,17],[20,21,22,23,24],[7,10,13,16,19]): t[kl]=lab; t[ki]=ic; t[kt]=txt
    add(f"ed063-s{k}",{"status":"ok","title":"Who needs FemTech?","note":"We focus on the five groups inside these buyers that choose, pay for, use and check women's health products.","t":t})
    t={13:cap}; t.update({14+i:p for i,p in enumerate(PAINS[k-1])})
    add(f"ed064-s{k}",{"status":"ok","title":"What are these customers' strongest pain points?","note":"We prioritized problems that recur in company filings, health surveys, studies and specialist reports on women's health.","t":t})
    add(f"ed065-s{k}",{"status":"ok","title":"Which pains deserve attention first?","subtitle":name,"icons":[r[1] for r in R],
      "rows":[{"pain":p,"s":s,"p":pr} for p,s,pr in ROWS[k-1]],
      "note":["Every stakeholder is different, and this table is a simplified view based on filings and reports","It gives a starting point, not a checklist, so priorities should be checked with real buyers"]})
open("/home/claude/nmp-decks/decks/femtech/research/17-femtech-deck-04-pain-points-results-research-2026-11-26.md","w").write("\n".join(out))
