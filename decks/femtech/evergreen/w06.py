import yaml
out=["# femtech, chapter 06 Value creation (evergreen, written by Claude, 26 Nov 2026)\n"]
def add(i,d): out.append(f"### {i}\n```yaml\n"+yaml.safe_dump(d,allow_unicode=True,sort_keys=False,width=1000)+"```\n")
L={7:"PERIOD TRACKING",9:"OVULATION TESTS",11:"Video visits",13:"WEARABLE DATA",15:"PILLS BY MAIL",17:"HEALTH CONTENT",19:"BREAST PUMPS",21:"HORMONE TESTS"}
add("ed101",{"status":"ok","title":"What's commoditized today in the market?",
 "note":"We identified products that are now broadly available and offered by many companies. They remain necessary, but value is shifting to clinical proof, payer contracts, trained clinicians and trusted data.",
 "t":{**L,6:"Basic apps that predict the next period, now offered free by dozens of firms",8:"Home urine tests for ovulation and pregnancy, sold cheaply in every pharmacy",
 10:"Video visits with a doctor or nurse, now offered by most health systems",12:"Temperature and heart rate data from rings and watches many women already own",
 14:"Birth control pills sent by mail after a short online visit, from many services",16:"Articles and chatbot answers about periods, pregnancy and menopause",
 18:"Standard electric breast pumps, paid for by most US health plans since 2012",20:"Basic blood tests for hormones such as estrogen, run by large national labs"}})
add("ed102",{"status":"ok","title":"Why has it become commoditized?",
 "note":"We see commoditization where products reuse cheap phones, standard tests and open medical knowledge. New value therefore comes from proven outcomes, coverage by payers and care women can trust.",
 "t":{**L,6:"Because period prediction is simple math that any phone app can run",8:"Because these paper strip tests have been sold over the counter for decades",
 10:"Because the pandemic made video visits a standard part of US health care",12:"Because Oura, Apple and Samsung put heat sensors in mass devices",
 14:"Because many online clinics compete to prescribe the same generic pills",16:"Because general AI chatbots now answer basic health questions for free",
 18:"Because the Affordable Care Act made US plans pay for breast pumps",20:"Because hormone panels run on the same machines as routine blood tests"}})
add("ed103",{"status":"ok","title":"Where is value created today?","page":"1/2",
 "note":"We derived these elements from the companies that grew fastest and those that failed. The strongest value today sits in proving outcomes, getting payers to cover care and clearing FDA review.",
 "t":{9:"CLINICAL\nPROOF",7:"Trials and real-world data showing a product leads to more births or fewer complications",
 12:"PAYER\nCONTRACTS",10:"Deals with employers and health plans that pay for care, so women do not pay it out of pocket",
 17:"FDA\nCLEARANCES",15:"Clearances and approvals that let a test, device or app make a medical claim to doctors"}})
add("ed104",{"status":"ok","title":"Where is value created today?","page":"2/2",
 "note":"We derived these elements from recent deals, funding rounds and fines. Value is increasingly created by owning large health datasets, running trained care teams and keeping women's data safe.",
 "t":{9:"FEMALE HEALTH\nDATA",7:"Large sets of cycle, pregnancy and menopause data that train better predictions and AI tools",
 12:"TRAINED CARE\nTEAMS",10:"Clinicians trained in menopause, fertility and pelvic care, seen in days by video or in person",
 17:"TRUSTED\nPRIVACY",15:"Strong data protection that keeps cycle and pregnancy data safe from sale, leaks or legal use"}})
S=[("FERTILITY CARE","Benefits, clinics and tests that help people have a baby",
 [("COUPLES TRYING\nTO CONCEIVE","They are couples who have tried for a year or more without success and want a clear plan, a known price and real odds of a baby"),
  ("WOMEN FREEZING\nTHEIR EGGS","They are women in their thirties who want to keep the option of a child later and need clear prices and success data"),
  ("LGBTQ+\nFAMILIES","They are same-sex couples and single parents who need donor eggs or sperm, IVF or surrogacy, often across borders"),
  ("LARGE\nEMPLOYERS","They are companies that pay for fertility benefits to hire and keep staff, and want fewer twins and lower costs"),
  ("IVF\nCLINICS","They are fertility clinics that want tools to raise birth rates per cycle and to treat more patients with the same labs")],
 "The couple gets tests within days, a care plan from a specialist and a single price covered by an employer benefit. A care guide answers questions by message, the clinic transfers one embryo at a time, and a healthy baby arrives after one or two cycles.",
 "The couple waits months for a first visit, pays tens of thousands of dollars out of pocket and gets little explanation of each step. Cycles fail with no clear reason, twins add risk and cost, and the couple stops treatment when the money runs out.",
 {9:"🔍\nAn employer chooses a fertility benefit",7:"🩺\nA patient gets tests and a care plan",6:"🧪\nThe clinic runs IVF or egg freezing",8:"💳\nThe benefit pays the clinic per cycle",13:"🔁\nThe employer renews the contract",11:"👥\nMore employees join the benefit",10:"📈\nBirth data show lower total costs",12:"🍼\nA healthy single baby is born"}),
("PREGNANCY CARE","Apps, monitors and virtual care from pregnancy to the postpartum year",
 [("EXPECTANT\nMOTHERS","They are pregnant women who want answers between visits and quick access to a nurse when something feels wrong"),
  ("NEW\nMOTHERS","They are women in the year after birth who need help with feeding, sleep, mood and recovery once visits stop"),
  ("HEALTH\nPLANS","They are insurers and Medicaid plans that pay for births and want fewer preterm babies and NICU stays"),
  ("HOSPITAL\nSYSTEMS","They are hospital systems that want to follow high-risk mothers at home and cut readmissions after birth"),
  ("RURAL\nCLINICS","They are clinics far from a delivery hospital that need remote monitoring and specialist advice for their patients")],
 "The mother logs her blood pressure at home and a nurse calls the same day when it rises. Questions get answers by message, mental health checks continue after birth, and the health plan pays because the program cuts emergency visits.",
 "The mother waits weeks between visits with questions no one answers. High blood pressure after birth goes unnoticed until an emergency, support stops at six weeks, and a large bill arrives even though she has health insurance.",
 {9:"🔍\nA health plan selects a maternity program",7:"📱\nThe mother joins early in pregnancy",6:"🩺\nNurses follow her data at home",8:"💳\nThe plan pays per member each month",13:"🔁\nThe plan extends to new regions",11:"👥\nMore mothers enroll each year",10:"📈\nFewer emergencies prove the savings",12:"🍼\nMother and baby leave care healthy"}),
("HORMONAL HEALTH","Tests, apps and care for cycles, contraception and conditions like PCOS",
 [("YOUNG\nWOMEN","They are women in their teens and twenties who want to understand their cycle and choose a birth control that suits them"),
  ("WOMEN WITH\nPCOS","They are women with irregular cycles, acne or weight changes who want a diagnosis and a plan that treats the cause"),
  ("COUPLES\nPLANNING","They are couples who want to know the fertile days to plan or avoid a pregnancy without taking hormones"),
  ("PRIMARY\nCARE","They are general doctors who want simple tests and guidance to treat cycle problems without a specialist referral"),
  ("RETAIL\nPHARMACIES","They are drugstores and online pharmacies that want to sell birth control and hormone tests without a prescription")],
 "The woman takes a home hormone test, gets results in days and talks to a clinician who explains them. Her app learns her real cycle, her birth control fits her body, and a condition like PCOS is found early and treated by one care team.",
 "The woman tracks her cycle in a free app that gives the same advice to everyone. Her symptoms are dismissed for years, she tries several pills without follow-up, and her data is shared with advertisers she never chose.",
 {9:"🔍\nA woman downloads a cycle app",7:"🧪\nShe orders a home hormone test",6:"🩺\nA clinician reviews the results",8:"💳\nShe pays for a yearly plan",13:"🔁\nNew tests and services are added",11:"👥\nFriends join through referrals",10:"📈\nMore data improve each prediction",12:"💊\nShe gets the right treatment"}),
("PELVIC HEALTH","Devices and care for the pelvic floor, endometriosis and sexual health",
 [("NEW\nMOTHERS","They are women who leak urine or feel pelvic pain after birth and want help at home before it becomes long-term"),
  ("WOMEN WITH\nPELVIC PAIN","They are women with painful periods or endometriosis who wait years for a diagnosis and want care that takes pain seriously"),
  ("OLDER\nWOMEN","They are women over 50 with bladder leaks or pelvic organ problems who want to avoid surgery if they can"),
  ("PT\nCLINICS","They are physical therapy clinics that want home devices that guide exercises and show patients' progress between visits"),
  ("HEALTH\nPLANS","They are insurers that want home therapy that costs less than surgery and keeps women out of the hospital")],
 "The woman uses a cleared device at home that guides each exercise and shows her progress on her phone. Her therapist follows the data and adjusts the plan, the health plan covers the device, and symptoms improve within weeks without surgery.",
 "The woman is told that leaks or pain are normal after birth or with age. She waits months for a specialist, pays for a device herself, stops using it without guidance, and ends up needing surgery that earlier care might have avoided.",
 {9:"🔍\nA doctor prescribes home therapy",7:"📦\nThe device ships to the patient",6:"📱\nShe follows exercises on her phone",8:"💳\nThe health plan pays for the device",13:"🔁\nNew conditions are added",11:"👥\nMore doctors prescribe it",10:"📈\nOutcome data support coverage",12:"✅\nSymptoms improve without surgery"}),
("MIDLIFE CARE","Virtual clinics, drugs and tools for perimenopause and menopause",
 [("WOMEN IN\nMIDLIFE","They are women of about 40 to 60 with hot flashes, poor sleep or mood changes who want a doctor who knows menopause"),
  ("WORKING\nWOMEN","They are women at the top of their careers who want quick care so symptoms do not force them to cut hours or quit"),
  ("PRIMARY\nCARE","They are general doctors who want clear guidance on hormone therapy and new drugs for midlife patients"),
  ("LARGE\nEMPLOYERS","They are companies that want to keep experienced women and add menopause support to their benefits"),
  ("HEALTH\nPLANS","They are insurers that want menopause care that lowers later costs in heart, bone and mental health")],
 "The woman books a video visit within days with a clinician trained in menopause. She leaves with a plan, the visit is billed to her insurance, her treatment is adjusted after a few weeks, and her sleep and focus at work come back.",
 "The woman sees several doctors who tell her that her symptoms are just stress or age. She pays out of pocket for supplements that do not work, gets mixed advice on hormone therapy and cuts her hours at work as symptoms get worse.",
 {9:"🔍\nA woman searches for menopause care",7:"🩺\nShe books a video visit with a clinician",6:"📋\nShe gets a treatment plan",8:"💳\nThe visit is billed to her insurer",13:"🔁\nThe clinic adds new conditions",11:"👥\nEmployers add it to benefits",10:"📈\nFollow-ups keep her in care",12:"💊\nHer symptoms are under control"}),
("WOMEN'S CANCER TESTS","Tests and imaging that find breast and gynecological cancers early",
 [("WOMEN OVER\n40","They are women who need regular breast cancer screening and want accurate results without long waits or false alarms"),
  ("WOMEN WITH\nDENSE BREASTS","They are women whose breast tissue hides tumors on standard mammograms and who need an extra exam to be sure"),
  ("IMAGING\nCENTERS","They are radiology groups that read more mammograms with fewer radiologists and want AI to flag what matters"),
  ("OB-GYN\nPRACTICES","They are gynecology practices that want simple tests for cervical, ovarian and uterine cancers in routine visits"),
  ("HEALTH\nPLANS","They are insurers that want tests which find cancer early, when treatment costs far less than at a late stage")],
 "The woman gets her mammogram read with the help of AI that flags a small tumor early. Results arrive in a day, an extra exam is covered for dense breasts, and treatment starts while the cancer is small and easy to treat.",
 "The woman waits weeks for results, gets a false alarm that leads to a painful biopsy, or has a tumor missed in dense tissue. The cancer is found a year later at a later stage, when treatment is harder and far more costly.",
 {9:"🔍\nAn imaging center tests an AI tool",7:"🩻\nThe tool reads each mammogram",6:"🔬\nIt flags images for the radiologist",8:"💳\nThe center pays per scan read",13:"🔁\nNew cancers and tests are added",11:"🏥\nMore centers adopt the tool",10:"📈\nStudies prove earlier detection",12:"✅\nCancers are found at an early stage"})]
for k,(cap,desc,users,good,bad,flow) in enumerate(S,1):
    add(f"ed106-s{k}",{"status":"ok","t":{6:"VALUE CREATION",3:cap,5:desc}})
    t={21:cap}
    for (lab,txt),kl,kt in zip(users,[5,8,11,14,17],[7,10,13,16,19]): t[kl]=lab; t[kt]=txt
    v="create" if cap.endswith("S") else "creates"
    add(f"ed107-s{k}",{"status":"ok","title":"Who needs it the most?","note":f"We focus on five groups where {cap.lower().replace('women','women')} {v} the clearest value today. These are priority use cases, not a full list of clients.","t":t})
    add(f"ed108-s{k}",{"status":"ok","title":"What does \"maximum customer value\" look like in practice?","t":{5:cap,10:"EXCEPTIONAL CUSTOMER EXPERIENCE",7:good,12:"VS",9:"BAD CUSTOMER EXPERIENCE",6:bad}})
    add(f"ed109-s{k}",{"status":"ok","title":"How does the money flow in this case?","t":{14:cap,**flow}})
open("/home/claude/nmp-decks/decks/femtech/research/17-femtech-deck-06-value-creation-results-research-2026-11-26.md","w").write("\n".join(out))
