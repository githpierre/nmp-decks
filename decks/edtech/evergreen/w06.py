import yaml
out=["# EdTech, chapter 06 Value creation (evergreen, written by Claude, 28 Nov 2026)\n"]
def add(i,d): out.append(f"### {i}\n```yaml\n"+yaml.safe_dump(d,allow_unicode=True,sort_keys=False,width=1000)+"```\n")
L={7:"VIDEO COURSES",9:"FLASH CARDS",11:"SCHOOL LMS",13:"QUIZ TOOLS",15:"GRAMMAR APPS",17:"VIDEO CALLS",19:"E-BOOKS",21:"CHATBOTS"}
add("ed101",{"status":"ok","title":"What's commoditized today in the market?",
 "note":"We identified tools that are now broadly available and offered by many companies. They remain necessary, but value is shifting to proof of learning, guided AI, curriculum fit and daily habits.",
 "t":{**L,6:"Recorded video lessons on any topic, free on YouTube and on many course sites",8:"Digital flashcards and simple drill apps that anyone can make in minutes",
 10:"Basic course platforms for posting homework, files and grades online",12:"Online quiz and poll tools that teachers use for free in class every day",
 14:"Spelling and grammar checkers built into every word processor and browser",16:"Video calls for live lessons, offered free by large tech firms to schools",
 18:"Digital textbooks and worksheets, sold or shared as simple PDF files",20:"General AI chatbots that answer homework questions for free, at any hour"}})
add("ed102",{"status":"ok","title":"Why has it become commoditized?",
 "note":"We see commoditization where tools are easy to copy, given away by big tech firms or built on open content. New value therefore comes from tools that prove learning and fit how schools and firms work.",
 "t":{**L,6:"Because cheap cameras and free video sites let anyone teach on screen",8:"Because the idea is simple, and Quizlet and many apps offer it for free",
 10:"Because Canvas, Moodle and Google Classroom all offer these basic features",12:"Because many free tools do the same thing and copy each other",
 14:"Because Microsoft and Google give these checkers away for free",16:"Because Zoom, Teams and Meet are free for schools and well known",
 18:"Because files are easy to copy and many sites share them for free",20:"Because big AI firms give their chatbots away to win new users"}})
add("ed103",{"status":"ok","title":"Where is value created today?","page":"1/2",
 "note":"We derived these elements from the companies that won renewals, funding and deals, and from recent learning studies. The strongest value today sits in tools that prove students learn.",
 "t":{9:"PROOF OF\nLEARNING",7:"Studies and usage data that show a tool raises scores, which districts now ask for before renewal",
 12:"GUIDED\nAI TUTORS",10:"AI tutors that ask questions and give hints instead of answers, so students still do the work",
 17:"CURRICULUM\nFIT",15:"Content built around the standards and materials that each school district has adopted"}})
add("ed104",{"status":"ok","title":"Where is value created today?","page":"2/2",
 "note":"We derived these elements from recent funding rounds, results and deals. Value is increasingly created by daily habits, tools that fit existing workflows and skills that employers accept.",
 "t":{9:"DAILY\nHABITS",7:"Products that bring learners back every day, then turn free use into paid subscriptions",
 12:"WORKFLOW\nFIT",10:"Tools inside Google Docs, Canvas, Teams or WhatsApp, where teachers and staff already work",
 17:"TRUSTED\nSKILL PROOF",15:"Credentials and skill checks that employers accept, so learning leads to a job or a raise"}})
S=[("K-12 LEARNING","K-12 learning","Apps, lessons and class tools that help children learn at school",
 [("SCHOOL\nDISTRICTS","They are districts that buy reading and math software for thousands of students and must show results to their boards each year"),
  ("CLASSROOM\nTEACHERS","They are teachers who plan lessons, grade work and help students who fall behind, often with little time to spare"),
  ("STRUGGLING\nREADERS","They are children who read below their grade level and need daily practice with fast and kind feedback"),
  ("MATH\nLEARNERS","They are students who need step-by-step practice and hints in math, at their own pace, in and after class"),
  ("SPECIAL\nNEEDS","They are students who need lessons adapted to how they learn, with texts at the right level and extra support")],
 "A student who fell behind in math practices for twenty minutes a day. The app gives hints instead of answers, the teacher sees who is stuck before the test, and by spring the district can show the board real gains in scores.",
 "The district buys an app that most students never open. Teachers have no time to set it up, nobody can tell whether it helps, and at renewal time the money is spent with no sign of better scores.",
 {9:"🔍\nA district tests an app in a pilot",7:"👩‍🏫\nTeachers use it in their classes",6:"📊\nUsage and scores are tracked",8:"💳\nThe district buys a yearly license",13:"🔁\nMore schools join the next year",11:"🏫\nNearby districts hear of the results",10:"📈\nThe app improves with more use",12:"✅\nStudents catch up in math and reading"}),
("HIGHER EDUCATION","Higher education","Software that runs admissions, courses and student support at colleges",
 [("ONLINE\nPROGRAMS","They are universities that teach full degrees online and need a platform that keeps distant students engaged"),
  ("FACULTY\nMEMBERS","They are professors who post lessons, grade work and must now judge which assignments were written by AI"),
  ("STUDENT\nSUCCESS","They are advising teams that spot students at risk of dropping out and reach them early with help"),
  ("ADMISSION\nTEAMS","They are teams that check transcripts and credentials and must catch fake documents before they admit anyone"),
  ("CAMPUS\nIT TEAMS","They are IT teams that run course platforms and student records and must keep them safe from data breaches")],
 "A student at risk of failing is flagged in the third week. An adviser reaches out, the student joins tutoring sessions inside the course platform, and the university keeps a student who finishes the degree and pays tuition until the end.",
 "The student stops logging in and nobody notices for months. Grades fall, the student drops out after the first year, the university loses the tuition, and the student leaves with debt and no degree.",
 {9:"🔍\nA university picks a platform",7:"🎓\nIt runs courses and student data",6:"📊\nIt flags students who fall behind",8:"💳\nThe university pays a yearly fee",13:"🔁\nMore courses move onto the platform",11:"🏛️\nOther campuses adopt the same tool",10:"📈\nMore students finish their degree",12:"✅\nThe campus keeps more tuition"}),
("ONLINE COURSES","Online courses","Courses, apps and video lessons that adults buy to learn on their own",
 [("LANGUAGE\nLEARNERS","They are adults who want to speak a new language for work, travel or family, and need practice every day"),
  ("CAREER\nCHANGERS","They are people who want a new job in tech, data or business and need courses that employers recognize"),
  ("CURIOUS\nLEARNERS","They are adults who learn for pleasure, from chess to music, with short lessons they fit into their day"),
  ("COURSE\nCREATORS","They are experts and teachers who build courses online and need a platform that brings paying learners"),
  ("COMPANY\nTEAMS","They are employers that buy course libraries for their staff, like the 18,000 business clients of Coursera and Udemy")],
 "A learner opens the app for five minutes on the bus every day. Lessons feel like a game, an AI partner talks back in the new language, and after a year of daily streaks the learner gladly pays for the subscription and invites friends.",
 "A learner buys a long video course full of good intentions. There is no practice and no feedback, motivation fades after the second week, and the course sits unfinished while the learner decides never to pay again.",
 {9:"🔍\nA learner downloads a free app",7:"📱\nShort lessons fit into every day",6:"🔁\nDaily streaks bring the learner back",8:"💳\nThe learner pays for extra features",13:"👥\nFriends join through word of mouth",11:"🌍\nNew courses reach new countries",10:"📈\nTests make lessons better each week",12:"✅\nThe learner speaks a new language"}),
("TUTORING AND TEST PREP","Tutoring and test prep","Live and AI tutors that help students practice and prepare for exams",
 [("EXAM\nCANDIDATES","They are students preparing for high-stakes exams that decide their university or career, like India's JEE and NEET"),
  ("PARENTS AND\nFAMILIES","They are parents who pay for tutors to help a child catch up or get ahead, and want to see clear progress"),
  ("LANGUAGE\nSTUDENTS","They are learners who book live lessons to speak a language with a tutor, like those on Preply"),
  ("PRIVATE\nTUTORS","They are independent tutors who need a steady flow of students and tools to plan and follow each lesson"),
  ("SCHOOL\nPROGRAMS","They are schools that buy tutoring for students who fall behind, if the provider can prove learning gains")],
 "A student preparing for a key exam practices with an AI tutor at night and meets a human tutor each week. The tutor sees exactly which mistakes repeat, sessions target them, and the score rises enough to win a place at the chosen university.",
 "The family pays for weekly lessons that follow no plan. The tutor does not know what the student got wrong last time, homework help gives answers instead of practice, and the exam score barely moves despite months of costly sessions.",
 {9:"🔍\nA family books a first lesson",7:"🧑‍🏫\nThe tutor and the AI plan each step",6:"📝\nPractice targets repeated mistakes",8:"💳\nThe family pays for more lessons",13:"🔁\nThe student keeps the same tutor",11:"👥\nParents tell other families",10:"📊\nThe platform sees what works best",12:"✅\nThe student wins a higher score"}),
("EXAMS AND CREDENTIALS","Exams and credentials","Digital tests, certificates and skill records that prove what people know",
 [("UNIVERSITY\nADMISSIONS","They are admissions teams that need trusted English tests and transcripts from students all over the world"),
  ("JOB\nSEEKERS","They are people who need to prove a skill to an employer, beyond a simple list of the courses they started"),
  ("HIRING\nMANAGERS","They are recruiters and managers who want to check real skills quickly before they hire someone"),
  ("TEST\nTAKERS","They are students who need to take an exam from home, at a fair price, and get results within days"),
  ("LICENSING\nBODIES","They are professional bodies that certify nurses, accountants and engineers and need secure exams")],
 "A student abroad takes an English test at home on a laptop. The exam is watched for cheating, the score arrives within days, and universities accept it, so the student applies to five programs without traveling to a distant test center.",
 "The student must travel to a test center in another city and pay a high fee. Results take weeks, a lost certificate is hard to replace, and some universities doubt documents they cannot verify easily.",
 {9:"🔍\nA candidate books an online exam",7:"💻\nThe test is taken at home",6:"🔐\nAI and people check for cheating",8:"💳\nThe candidate pays the exam fee",13:"🔁\nMore universities accept the score",11:"🎓\nMore candidates choose this test",10:"📈\nThe score becomes a known standard",12:"✅\nThe skill is proven and trusted"}),
("WORKFORCE TRAINING","Workforce training","Platforms that employers buy to train their staff and track new skills",
 [("HR AND\nL&D TEAMS","They are training teams that must close skill gaps fast, as the World Economic Forum says 59 of 100 workers need training by 2030"),
  ("FRONTLINE\nSTAFF","They are shop, factory and hotel workers who need short lessons on their phones, between shifts and tasks"),
  ("SALES\nTEAMS","They are sellers and managers who must practice hard conversations, like those trained on Yoodli's AI role-play"),
  ("NEW\nHIRES","They are new employees who must learn tools, products and rules fast to become useful in their first weeks"),
  ("COMPLIANCE\nTEAMS","They are teams that must prove each employee finished required safety and legal training on time")],
 "A new store worker gets a three-minute lesson on WhatsApp before each shift. Quizzes show what she has learned, her manager sees progress on one screen, and the company can link the training to fewer mistakes and better sales in its stores.",
 "The company buys a large course library that staff never open. Training means long videos on a desktop far from the shop floor, managers cannot see any effect, and the budget is cut at the next review.",
 {9:"🔍\nA company tests a training platform",7:"📱\nStaff learn on their own phones",6:"📝\nQuizzes show what each person knows",8:"💳\nThe company pays per employee",13:"🔁\nMore teams and sites join each year",11:"🏢\nThe platform links to HR systems",10:"📊\nTraining is tied to business results",12:"✅\nStaff gain the skills the job needs"})]
for k,(cap,name,desc,users,good,bad,flow) in enumerate(S,1):
    add(f"ed106-s{k}",{"status":"ok","t":{6:"VALUE CREATION",3:cap,5:desc}})
    t={21:cap}
    for (lab,txt),kl,kt in zip(users,[5,8,11,14,17],[7,10,13,16,19]): t[kl]=lab; t[kt]=txt
    nm=name[0].lower()+name[1:]
    add(f"ed107-s{k}",{"status":"ok","title":"Who needs it the most?","note":f"We focus on five groups where {nm} creates the clearest value today. These are priority use cases, not a full list of clients.","t":t})
    add(f"ed108-s{k}",{"status":"ok","title":"What does \"maximum customer value\" look like in practice?","t":{5:cap,10:"EXCEPTIONAL CUSTOMER EXPERIENCE",7:good,12:"VS",9:"BAD CUSTOMER EXPERIENCE",6:bad}})
    add(f"ed109-s{k}",{"status":"ok","title":"How does the money flow in this case?","t":{14:cap,**flow}})
open("/home/claude/nmp-decks/decks/edtech/research/1-edtech-deck-06-value-creation-results-research-2026-11-28.md","w").write("\n".join(out))
