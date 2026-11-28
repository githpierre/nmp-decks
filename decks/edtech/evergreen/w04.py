import yaml
out=["# EdTech, chapter 04 Pain points (evergreen, written by Claude, 28 Nov 2026)\n"]
def add(i,d):
    out.append(f"### {i}\n```yaml\n"+yaml.safe_dump(d,allow_unicode=True,sort_keys=False,width=1000)+"```\n")

add("ed054",{"status":"ok","title":"What are the pain points of yesterday vs. today?",
 "note":"We grouped the market into phases: early online courses, pandemic remote learning, the slump after it and today's push for proof. We used studies, filings and budget reporting.",
 "t":{6:"2012 - 2019\nOnline courses and learning apps spread, but most stayed free, and few schools or employers paid for them at scale",
 7:"2020 - 2021\nSchool closures pushed every class online overnight, with poor devices, weak links and teachers who had no training",
 8:"2022 - 2024\nClasses reopened, usage fell and funding dried up, while districts piled up dozens of apps that few students used",
 9:"TODAY\nRelief money has ended, budgets are tight, and buyers want proof that AI tools improve learning before they renew",
 10:"?\nBuyers will need tools that prove learning gains, protect student data and fit into the systems they already use"}})
add("ed055",{"status":"ok","title":"Which old problems are now behind us?",
 "note":"We treat these as problems that new products have removed for many buyers. They do not mean that every school or learner has adopted these tools yet.",
 "t":{5:"Teachers had to write every quiz, worksheet and rubric by hand",7:"MagicSchool and Brisk now draft quizzes, rubrics and feedback with AI, and teachers review them first",
 8:"Language learners had little open speaking practice at home",10:"Speak and Duolingo now offer live AI voice and video calls that give feedback during the talk",
 11:"Independent tutors needed a full school license to run a course",13:"Instructure's Canvas Lite now lets any educator create a course and invite students for free",
 14:"Students had to write their own practice exams from their notes",16:"Quizlet now turns notes into full practice exams with chosen question types and difficulty",
 17:"Employees had to leave their work tools to find any course",19:"Coursera's learning agent now brings its courses inside Microsoft 365 Copilot at work",
 20:"Learners got little feedback after a live online lesson",22:"Preply's Lesson Insights now sum up each lesson, and three in four of its English learners use them"}})
add("ed056",{"status":"ok","title":"What problems do all players face?","page":"1/2",
 "note":"We kept the problems that come back in OECD and UNESCO reviews, procurement guides and classroom studies. We skipped generic startup issues and focused on building learning tools.",
 "t":{25:"AI tutors can give\nwrong answers",23:"You need checked\nanswers",8:"Schools use many\nsystems",6:"You need data\nlinks",
 29:"Each district has\nits own plan",27:"You need local\ncurriculum fit",12:"Student data is\nsensitive",10:"You need privacy\nby design",
 33:"Students stop\nusing the app",31:"You need daily\nhabits",16:"Teachers have\nlittle time",14:"You need simple\ntools",
 37:"Help can replace\nreal learning",35:"You need guided\nhints",20:"Content goes\nout of date",18:"You need fresh\ncontent"}})
add("ed057",{"status":"ok","title":"What problems do all players face?","page":"2/2",
 "note":"We separated the problems of building tools from those of selling them. The second set matters once a tool works, because budgets, buyers, proof and rivals still decide who wins.",
 "t":{25:"Relief money\nhas run out",23:"You need cheaper\noffers",8:"Pilots take a\nfull semester",6:"You need patient\ncash",
 29:"Many teams must\nsay yes",27:"You need a clear\nbuying path",12:"Buyers want proof\nof gains",10:"You need real\nstudies",
 33:"Free AI tools\ncut prices",31:"You need a clear\nedge",16:"Funding fell to a\ndecade low",14:"You need early\nrevenue",
 37:"Licenses go\nunused",35:"You need active\nusers",20:"Big groups buy\nthe leaders",18:"You need strong\npartners"}})
add("ed059",{"status":"ok","title":"Which problems are startups going after?",
 "t":{16:"Weak\nproof",11:"Busy\nteachers",14:"Low\nusage",
 21:"Pain points change sharply by buyer.\n\nBroad statements quickly mislead.\nSo we split schools, campuses, employers, families and adult learners into five buyer groups before scoring.",
 13:"Data\nprivacy",12:"Tight\nbudgets",15:"Skill\ngaps",18:"Exam\nstress",19:"Lost\nlearners"}})
add("ed060",{"status":"ok","title":"How will we proceed?",
 "note":"We break the market down before scoring because the same tool creates very different value and risk for a school, an employer or a parent.",
 "t":{9:"😣\nPAIN POINTS\n\nWe list each group's main pains and score them to rank them.",
 6:"🎯\nGOAL\n\nFind the pains that matter most in EdTech, and who feels them most.",
 7:"🏷️\nCATEGORIES\n\nWe split the market by buyer, because who pays and what they need differ.",
 8:"👥\nSEGMENTS\n\nFor each buyer, we list the people who decide, pay, use and check the tools."}})
SEG=[("SCHOOLS AND DISTRICTS","Schools and districts","SCHOOLS AND\nDISTRICTS","Public and private schools and the districts that buy their software and lessons","Public and private schools and the districts that\nbuy their software, lessons and tests"),
("COLLEGE CAMPUSES","College campuses","COLLEGE\nCAMPUSES","Colleges and universities that run courses, admissions and student support online","Colleges and universities that run courses,\nadmissions and student support online"),
("CORPORATE EMPLOYERS","Corporate employers","CORPORATE\nEMPLOYERS","Companies and their HR teams that train staff and check the skills they need","Companies and their HR teams that train\nstaff and check the skills they need"),
("PARENTS AND FAMILIES","Parents and families","PARENTS AND\nFAMILIES","Parents who pay for tutors, apps and test prep to help their children at school","Parents who pay for tutors, apps and test prep\nto help their children at school"),
("ADULT LEARNERS","Adult learners","ADULT\nLEARNERS","Adults who pay for courses, language apps or certificates to grow at work or for fun","Adults who pay for courses, language apps or\ncertificates to grow at work or for fun")]
add("ed061",{"status":"ok","title":"Which categories will we use?",
 "note":"We split the market into five types of buyer. They differ enough in who pays, what proof they need and how they buy to score their pain points separately.",
 "t":{7:SEG[0][2],9:SEG[1][2],11:SEG[2][2],13:SEG[3][2],15:SEG[4][2],6:SEG[0][3],8:SEG[1][3],10:SEG[2][3],12:SEG[3][3],14:SEG[4][3],17:"",16:""},"holes_ok":True})
ROLES=[
 [("SCHOOL\nLEADERS","🏫","They need tools that raise test scores and fit tight budgets, and they must defend each purchase"),
  ("CLASSROOM\nTEACHERS","👩‍🏫","They need tools that save time on planning and grading and fit the lessons they already teach"),
  ("IT AND DATA\nTEAMS","🔐","They need apps that link to school systems and protect student data under privacy laws"),
  ("CURRICULUM\nLEADS","📚","They need content that matches state standards and the lessons the district has already adopted"),
  ("BUYING\nTEAMS","💰","They need clear prices, contracts and proof of use before they renew any license each year")],
 [("ACADEMIC\nLEADERS","🎓","They need to keep students enrolled and on track to graduate while costs and debt keep rising"),
  ("FACULTY\nMEMBERS","👩‍🏫","They need course tools that are simple to use and that help them spot work written by AI"),
  ("CAMPUS IT\nTEAMS","🖥️","They need platforms that link to student records and protect data from breaches"),
  ("STUDENT\nSERVICES","🧑","They need to reach struggling students early with tutoring, advice and other kinds of help"),
  ("ADMISSIONS\nTEAMS","📋","They need to verify transcripts and credentials quickly and catch fake documents early")],
 [("HR AND\nL&D LEADS","💼","They need training that closes skill gaps fast and shows a clear return to company leaders"),
  ("TEAM\nMANAGERS","👥","They need staff trained on new tools quickly, without long hours away from their work"),
  ("FRONTLINE\nSTAFF","📱","They need short lessons on the phones they already use, between shifts and tasks"),
  ("COMPLIANCE\nTEAMS","⚖️","They need proof that every employee finished required safety and legal training on time"),
  ("IT AND\nSECURITY","🔐","They need learning platforms that connect to company systems and keep employee data safe")],
 [("WORKING\nPARENTS","🏠","They need help for children who fall behind, at a price they can afford, after school hours"),
  ("YOUNG\nSTUDENTS","🎒","They need lessons and practice that feel like a game, so they keep coming back every day"),
  ("TEENS AND\nTEST TAKERS","📝","They need targeted prep for key exams, with feedback on the exact mistakes they make"),
  ("PRIVATE\nTUTORS","🧑‍🏫","They need a steady flow of students and tools to plan lessons and track each child's progress"),
  ("SCHOOL\nTEACHERS","🏫","They need to know which apps children use at home, so that home and class practice match")],
 [("CAREER\nCHANGERS","🚀","They need courses and credentials that employers trust, so that a new skill leads to a job"),
  ("LANGUAGE\nLEARNERS","🗣️","They need regular speaking practice and feedback without the cost of a tutor at each lesson"),
  ("WORKING\nADULTS","⏱️","They need short lessons they can fit around work and family, on the phone they carry"),
  ("JOB\nSEEKERS","🔍","They need proof of skills that recruiters can check, beyond a list of finished courses"),
  ("COURSE\nCREATORS","🎥","They need a platform that brings them paying learners and pays them fairly for courses")]]
PAINS=[
 ["They see relief money end as costs keep rising","They pay for licenses that students never open","They need proof that a tool raises test scores","They run privacy reviews for every single app","They find apps that do not link to their systems","They see teachers with no time to learn new tools","They wait a full semester to judge each pilot"],
 ["They see too many students drop out before a degree","They find that work written by AI is hard to spot","They face breaches of student data and records","They pay for many tools that do not link together","They must check transcripts for credential fraud","They need online courses that keep students engaged","They face tight budgets and falling enrollment"],
 ["They need staff to learn new AI tools very quickly","They pay for online courses that staff never finish","They cannot prove training changes performance","They lose staff time to long sessions away from work","They must track required training for audits","They find frontline staff hard to reach on apps","They see course catalogs that miss real job tasks"],
 ["They pay a lot for private tutors every single month","They see their children fall behind in math and reading","They cannot tell which learning apps really work","They worry about screen time and phones at home","They find exam prep stressful and very costly","They need tutors who fit around school and family hours","They worry about how apps use their children's data"],
 ["They pay for courses and then never finish them","They doubt that employers trust online certificates","They lack time to study after work and family","They need speaking practice without a tutor's price","They find it hard to know which skills to learn","They lose motivation when they study all alone","They see AI change the skills their jobs need"]]
ROWS=[
 [("Federal relief money has ended while school costs keep rising",[3,1,1,1,3],"CRITICAL"),("Districts pay for licenses that students never even open",[3,1,2,1,3],"MAJOR"),("Buyers need proof that a tool really raises test scores",[3,2,1,3,3],"CRITICAL"),("Every new app must pass a privacy and security review",[1,1,3,1,2],"HIGH"),("Many apps do not link to the systems schools already use",[1,2,3,1,1],"MAJOR"),("Teachers have little time to learn and set up new tools",[2,3,1,2,1],"CRITICAL"),("Each pilot takes a full semester before any decision is made",[2,1,1,2,3],"HIGH")],
 [("Too many students drop out before they finish a degree",[3,1,1,3,2],"CRITICAL"),("Work written by AI is hard for teachers to spot and to grade",[2,3,1,1,1],"MAJOR"),("Breaches can expose student records and personal data",[2,1,3,1,2],"MAJOR"),("Campuses pay for many tools that do not link together",[2,2,3,1,1],"HIGH"),("Fake transcripts and credentials are getting harder to catch",[1,1,1,1,3],"HIGH"),("Online courses struggle to keep students engaged to the end",[3,3,1,3,1],"CRITICAL"),("Budgets are tight as enrollment falls at many campuses",[3,1,2,2,3],"MAJOR")],
 [("Staff must learn new AI tools faster than training can follow",[3,3,2,1,1],"CRITICAL"),("Companies pay for online courses that staff never finish",[3,2,1,1,1],"MAJOR"),("Training rarely shows a clear effect on staff performance",[3,3,1,1,1],"CRITICAL"),("Long training sessions take staff away from their daily work",[1,3,3,1,1],"MAJOR"),("Required training must be tracked and proven for audits",[2,1,1,3,1],"HIGH"),("Frontline staff are hard to reach through desktop apps",[2,2,3,1,1],"HIGH"),("Course catalogs often miss the real tasks of each job",[3,3,2,1,1],"MAJOR")],
 [("Private tutors cost families a lot of money every month",[3,1,2,1,1],"CRITICAL"),("Children fall behind in math and reading and lose confidence",[3,3,2,2,3],"CRITICAL"),("Parents cannot tell which learning apps really work",[3,1,1,1,2],"MAJOR"),("Screen time and phone use worry parents and teachers",[3,1,1,1,3],"MAJOR"),("Exam preparation is stressful and costly for many families",[3,1,3,1,1],"HIGH"),("Tutors must fit around school hours and family schedules",[2,1,2,3,1],"HIGH"),("Apps may collect and use children's data without clear limits",[3,1,1,1,2],"MAJOR")],
 [("Many learners pay for courses and then never finish them",[2,2,3,2,3],"CRITICAL"),("Employers do not always trust certificates earned online",[3,1,1,3,2],"CRITICAL"),("Adults lack time to study after work and family duties",[2,2,3,1,1],"MAJOR"),("Speaking practice with a tutor costs a lot for each lesson",[1,3,1,1,1],"MAJOR"),("It is hard to know which skills are worth learning next",[3,1,2,3,1],"HIGH"),("Learners lose motivation when they study all alone",[2,3,3,1,2],"MAJOR"),("AI keeps changing the skills that many jobs require",[3,1,2,3,2],"HIGH")]]
for k,(cap,name,_,_,intro) in enumerate(SEG,1):
    add(f"ed062-s{k}",{"status":"ok","t":{6:"PAIN POINTS",3:cap,5:intro}})
    R=ROLES[k-1]; t={27:cap}
    for (lab,ic,txt),kl,ki,kt in zip(R,[5,8,11,14,17],[20,21,22,23,24],[7,10,13,16,19]): t[kl]=lab; t[ki]=ic; t[kt]=txt
    add(f"ed063-s{k}",{"status":"ok","title":"Who needs EdTech?","note":"We focus on the five groups inside these buyers that choose, pay for, use and check learning tools.","t":t})
    t={13:cap}; t.update({14+i:p for i,p in enumerate(PAINS[k-1])})
    add(f"ed064-s{k}",{"status":"ok","title":"What are these customers' strongest pain points?","note":"We prioritized problems that recur in studies, buyer surveys, company results and procurement guides on learning tools.","t":t})
    add(f"ed065-s{k}",{"status":"ok","title":"Which pains deserve attention first?","subtitle":name,"icons":[r[1] for r in R],
      "rows":[{"pain":p,"s":s,"p":pr} for p,s,pr in ROWS[k-1]],
      "note":["Every stakeholder is different, and this table is a simplified view based on reports and studies","It gives a starting point, not a checklist, so priorities should be checked with real buyers"]})
open("/home/claude/nmp-decks/decks/edtech/research/1-edtech-deck-04-pain-points-results-research-2026-11-28.md","w").write("\n".join(out))
