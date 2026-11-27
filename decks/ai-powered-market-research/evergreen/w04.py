import yaml
out=["# AI-powered market research, chapter 04 Pain points (evergreen, written by Claude, 27 Nov 2026)\n"]
def add(i,d):
    out.append(f"### {i}\n```yaml\n"+yaml.safe_dump(d,allow_unicode=True,sort_keys=False,width=1000)+"```\n")
add("ed054",{"status":"ok","title":"What are the pain points of yesterday vs. today?",
 "note":"We grouped the market into phases: online surveys, text analytics, the arrival of language models, and today's proof gap. We used industry body reports, company releases and studies.",
 "t":{6:"2000 - 2015\nOnline surveys and panels made research cheaper, but studies still took weeks and depth needed costly human moderators",
 7:"2016 - 2022\nText analytics and dashboards sped up reporting, but open answers were still coded by hand and panels filled with fraud",
 8:"2023 - 2025\nLanguage models made AI interviews and synthetic users possible, but buyers did not know which answers they could trust",
 9:"TODAY\nMost research firms use AI, yet few have scaled it, and buyers ask for proof that AI and synthetic answers match real people",
 10:"?\nSynthetic panels may answer early questions in minutes, but they still need human checks on rare groups and new categories"}})
add("ed055",{"status":"ok","title":"Which old problems are now behind us?",
 "note":"We treat these as problems that new tools have removed for many research teams. They do not mean that every study is now fast, cheap or reliable everywhere.",
 "t":{5:"Each in-depth interview needed a human moderator and a booked time slot",7:"AI moderators from Outset, Strella and Conveo now run hundreds of interviews at once, day and night",
 8:"A qualitative study took six to eight weeks from brief to final report",10:"Listen Labs and Conveo report studies where the first findings arrive in a few days instead of weeks",
 11:"Open answers and transcripts were read and coded line by line by hand",13:"AI coding tools such as NVivo AI Cloud now group answers into themes and link each theme to its source",
 14:"A study in many countries needed a local agency and translators in each",16:"AI interviewers now run the same study in dozens of languages, and Conveo supports more than 50 of them",
 17:"Screening an idea meant paying for a full survey with real respondents",19:"Synthetic panels from Zappi, Evidenza and others now pre-screen many ideas before a real survey runs",
 20:"Past findings sat in old slide decks that no one could find again",22:"Listen Labs and Conveo build searchable archives, so each new interview adds to past customer evidence"}})
add("ed056",{"status":"ok","title":"What problems do all players face?","page":"1/2",
 "note":"We kept the problems that come back in industry body reports, buyer surveys and studies on research quality. We skipped generic startup issues and focused on research with AI.",
 "t":{25:"Bots spoil\nonline panels",23:"You need\nverified people",8:"Synthetic answers\nmiss real views",6:"You need human\nbenchmarks",
 29:"AI output can\nmislead teams",27:"You need source\nlinks",12:"Few firms scale\nAI past pilots",10:"You need daily\nworkflows",
 33:"Proof of value\nis hard to show",31:"You need clear\nROI cases",16:"Rare buyers are\nhard to reach",14:"You need wider\nreach",
 37:"Recordings raise\nprivacy risks",35:"You need clear\nconsent",20:"Studies are often\none-off projects",18:"You need repeat\nprograms"}})
add("ed057",{"status":"ok","title":"What problems do all players face?","page":"2/2",
 "note":"We separated the problems of running AI research from those of selling it. The second set matters once a tool works, because security, budgets, rules and rivals still decide who wins.",
 "t":{25:"Security reviews\ndelay purchases",23:"You need enterprise\nreadiness",8:"AI rules differ by\nregion and use",6:"You need legal\nclarity",
 29:"Research budgets\nface cuts",27:"You need lower\ncost per study",12:"Big platforms add\nsimilar tools",10:"You need a\nclear edge",
 33:"Many rivals sell\nlook-alike tools",31:"You need unique\ndata",16:"Agencies fear\nlosing fieldwork",14:"You need partner\nmodels",
 37:"Codes ask to\ndisclose AI use",35:"You need open\nmethods",20:"Buyers lack time\nto check vendors",18:"You need trusted\nreferences"}})
add("ed059",{"status":"ok","title":"Which problems are startups going after?",
 "t":{16:"Slow\nstudies",11:"High\ncosts",14:"Fake\nanswers",
 21:"Pain points change sharply by buyer.\n\nBroad statements quickly mislead.\nSo we split consumer brands, research agencies, product teams, ad agencies and consulting firms before scoring.",
 13:"Shallow\ninsights",12:"Rare\nbuyers",15:"Weak\nproof",18:"Lost\nfindings",19:"Few\nlanguages"}})
add("ed060",{"status":"ok","title":"How will we proceed?",
 "note":"We break the market down before scoring because the same tool creates very different value and risk for a brand, an agency or a product team.",
 "t":{9:"😣\nPAIN POINTS\n\nWe list each group's main pains and score them to rank them.",
 6:"🎯\nGOAL\n\nFind the pains that matter most in AI market research, and who feels them.",
 7:"🏷️\nCATEGORIES\n\nWe split the market by buyer, because who pays and what they need differ.",
 8:"👥\nSEGMENTS\n\nFor each buyer, we list the people who decide, pay, use and check tools."}})
SEG=[("CONSUMER BRANDS","Consumer brands","CONSUMER\nBRANDS","Food, drink, beauty and retail brands that test products, prices, packs and claims","Food, drink, beauty and retail brands that\ntest products, prices, packs and claims"),
("RESEARCH AGENCIES","Research agencies","RESEARCH\nAGENCIES","Agencies and panel firms that run studies for clients and sell fieldwork and analysis","Agencies and panel firms that run studies for\nclients and sell fieldwork and analysis"),
("PRODUCT TEAMS","Product teams","PRODUCT\nTEAMS","Software and app teams that interview users before and after they build a feature","Software and app teams that interview users\nbefore and after they build a feature"),
("AD AGENCIES","Ad agencies","AD\nAGENCIES","Creative and media agencies that test ads and concepts before a campaign launches","Creative and media agencies that test ads\nand concepts before a campaign launches"),
("CONSULTING FIRMS","Consulting firms","CONSULTING\nFIRMS","Strategy and advisory firms that need fast evidence on markets, buyers and rivals","Strategy and advisory firms that need fast\nevidence on markets, buyers and rivals")]
add("ed061",{"status":"ok","title":"Which categories will we use?",
 "note":"We split the market into five types of buyer. They differ enough in who pays, what proof they need and how they buy to score their pain points separately.",
 "t":{7:SEG[0][2],9:SEG[1][2],11:SEG[2][2],13:SEG[3][2],15:SEG[4][2],6:SEG[0][3],8:SEG[1][3],10:SEG[2][3],12:SEG[3][3],14:SEG[4][3],17:"",16:""},"holes_ok":True})
ROLES=[
 [("INSIGHTS\nLEADERS","🔍","They need evidence that leaders trust, fast enough to shape a launch before the budget is locked"),
  ("BRAND\nMANAGERS","🏷️","They need to test packs, claims and prices with real buyers in days, not wait weeks for each wave"),
  ("INNOVATION\nTEAMS","💡","They need to screen many ideas cheaply and keep only the few worth a full study with real people"),
  ("PROCUREMENT\nTEAMS","📋","They need vendors with clear prices, security proof and contracts they can compare and renew each year"),
  ("FINANCE\nTEAMS","💰","They need proof that faster research cuts failed launches and lowers the total cost of each study")],
 [("AGENCY\nLEADERS","💼","They need new AI services that keep margins up as clients cut fieldwork budgets and run studies alone"),
  ("PROJECT\nRESEARCHERS","🔬","They need tools that run interviews and code answers fast, so they spend their time on the story"),
  ("PANEL\nMANAGERS","👥","They need to keep bots and fake respondents out of studies, with checks that clients can audit"),
  ("CLIENT\nSERVICE TEAMS","💬","They need to show clients how AI was used and why the findings can be trusted, as codes require"),
  ("DATA\nTEAMS","📊","They need synthetic and real answers that fit their dashboards, trackers and data rules without rework")],
 [("PRODUCT\nMANAGERS","💻","They need to hear from many users before a feature is built, without waiting for a research slot"),
  ("UX\nRESEARCHERS","🎙️","They need to run more interviews with the same team, while keeping depth, follow-ups and quotes"),
  ("PRODUCT\nDESIGNERS","🎨","They need quick reactions to screens and flows, so each design round gets real feedback in days"),
  ("ENGINEERING\nLEADS","🛠️","They need clear user evidence before they commit engineers to building a feature for many months"),
  ("SECURITY\nTEAMS","🔒","They need research tools that pass security reviews and keep user recordings safe and private")],
 [("STRATEGY\nPLANNERS","🎯","They need fast reads on what buyers feel, so a creative brief starts from evidence and not guesses"),
  ("CREATIVE\nDIRECTORS","🎨","They need to know which ad idea works best before money is spent on production and media buying"),
  ("MEDIA\nPLANNERS","📺","They need to predict how ads will perform on each channel before the budget is split across them"),
  ("ACCOUNT\nLEADS","💼","They need proof for the client that a chosen idea will work, to win approval and keep the account"),
  ("BRAND\nCLIENTS","🏷️","They need pretest results they trust, at a price that lets them test more ideas for each campaign")],
 [("FIRM\nPARTNERS","💼","They need fast evidence for a client question, so a proposal or a due diligence starts with facts"),
  ("CASE\nTEAMS","👥","They need to interview many buyers and experts in days, within the tight timeline of each project"),
  ("KNOWLEDGE\nTEAMS","🗂️","They need to store past interviews and findings so later projects can reuse them across clients"),
  ("EXPERT\nNETWORKS","🗣️","They need ways to reach rare experts and decision makers, who are slow and costly to recruit"),
  ("CLIENT\nEXECUTIVES","🏢","They need answers they can act on, with a clear method behind each number shown in the report")]]
PAINS=[
 ["They wait weeks for results while launch dates are fixed","They pay high fees for each study and each wave","They screen too few ideas before choosing one","They find fake answers and bots in online panels","They lose findings in old decks no one can find","They struggle to reach rare or niche buyers fast","They doubt synthetic answers for big decisions"],
 ["They see clients cut fieldwork budgets each year","They lose margin when clients run studies alone","They fight fraud and bots in their own panels","They must disclose AI use and check its output","They spend long hours coding open answers by hand","They compete with cheaper software-only rivals","They face clients who doubt synthetic answers"],
 ["They wait for a research slot before each feature","They run too few interviews to see clear patterns","They lose days recruiting the right users each time","They spend days turning recordings into notes","They fail security reviews with new AI tools","They lose past findings across teams and tools","They struggle to prove research changed a product"],
 ["They spend on ads before they know if they work","They pay for slow pretests that delay campaigns","They test too few ideas for each campaign brief","They find that panels miss younger audiences","They struggle to compare results across markets","They see scores that do not predict real sales","They must convince clients that AI tests are valid"],
 ["They have days, not weeks, to answer each client","They pay high fees to recruit experts and buyers","They reach too few decision makers per project","They lose interviews and notes when projects end","They must check AI summaries before each report","They see clients use AI tools to do it themselves","They struggle to show a clear method for each figure"]]
ROWS=[
 [("Results arrive weeks after the launch date was already set",[3,3,3,1,2],"CRITICAL"),("Each study and each new wave costs high fees",[2,2,2,3,3],"MAJOR"),("Too few ideas are screened before one is chosen",[2,2,3,1,2],"HIGH"),("Fake answers and bots slip into online panels and studies",[3,2,2,2,2],"CRITICAL"),("Past findings sit in old decks that no one can find",[3,2,2,1,1],"HIGH"),("Rare or niche buyers are hard and costly to reach",[3,3,2,1,1],"MAJOR"),("Synthetic answers are not yet trusted for big bets",[3,2,2,2,3],"MAJOR")],
 [("Clients cut fieldwork budgets as they run studies alone",[3,2,2,3,1],"CRITICAL"),("Margins fall as software rivals sell cheaper studies",[3,2,1,2,1],"CRITICAL"),("Bots and fake respondents spoil their own panels",[2,2,3,3,2],"MAJOR"),("AI use must be disclosed and checked for each client",[2,3,1,3,2],"HIGH"),("Coding open answers by hand takes long hours",[1,3,1,2,3],"MAJOR"),("Clients doubt synthetic data and ask for human proof",[3,2,1,3,3],"MAJOR"),("Old panels lose value as AI interviews spread fast",[3,1,3,1,2],"HIGH")],
 [("Features wait for a research slot before work can start",[3,3,2,3,1],"CRITICAL"),("Too few interviews leave user patterns unclear",[3,3,2,2,1],"MAJOR"),("Recruiting the right users takes days for each study",[2,3,2,1,1],"HIGH"),("Turning recordings into notes takes days of work",[2,3,3,1,1],"MAJOR"),("New research tools fail strict enterprise security reviews",[2,2,1,2,3],"HIGH"),("Findings are lost across teams, tools and years",[3,3,3,2,1],"HIGH"),("It is hard to prove research changed the product",[3,2,2,3,1],"HIGH")],
 [("Money goes to ads before anyone knows if they work",[3,3,3,3,3],"CRITICAL"),("Slow pretests delay the start of each campaign",[3,3,3,2,2],"MAJOR"),("Too few ideas get tested for each campaign brief",[3,3,2,2,2],"HIGH"),("Panels miss younger and harder-to-reach audiences",[3,2,3,1,2],"HIGH"),("Results are hard to compare from one market to another",[2,1,3,2,3],"HIGH"),("Test scores do not always predict real sales results",[3,2,3,3,3],"CRITICAL"),("Clients need to be convinced that AI tests are valid",[2,2,1,3,3],"MAJOR")],
 [("Client answers are due in a few days, not in weeks",[3,3,1,1,3],"CRITICAL"),("Recruiting rare experts and buyers costs high fees",[3,2,1,3,2],"MAJOR"),("Too few decision makers are reached per project",[3,3,1,3,3],"MAJOR"),("Interviews and notes are lost when projects end",[2,2,3,1,1],"HIGH"),("AI summaries must be checked before each report",[3,3,2,1,3],"HIGH"),("Clients use AI tools to do the work themselves",[3,1,2,2,1],"CRITICAL"),("Each figure needs a clear method for the client",[3,3,1,1,3],"HIGH")]]
for k,(cap,name,_,_,intro) in enumerate(SEG,1):
    add(f"ed062-s{k}",{"status":"ok","t":{6:"PAIN POINTS",3:cap,5:intro}})
    R=ROLES[k-1]; t={27:cap}
    for (lab,ic,txt),kl,ki,kt in zip(R,[5,8,11,14,17],[20,21,22,23,24],[7,10,13,16,19]): t[kl]=lab; t[ki]=ic; t[kt]=txt
    add(f"ed063-s{k}",{"status":"ok","title":"Who needs AI market research?","note":"We focus on the five groups inside these buyers that choose, pay for, use and check research tools.","t":t})
    t={13:cap}; t.update({14+i:p for i,p in enumerate(PAINS[k-1])})
    add(f"ed064-s{k}",{"status":"ok","title":"What are these customers' strongest pain points?","note":"We prioritized problems that recur in industry body reports, buyer surveys, studies and company releases on research.","t":t})
    add(f"ed065-s{k}",{"status":"ok","title":"Which pains deserve attention first?","subtitle":name,"icons":[r[1] for r in R],
      "rows":[{"pain":p,"s":s,"p":pr} for p,s,pr in ROWS[k-1]],
      "note":["Every stakeholder is different, and this table is a simplified view based on reports and studies","It gives a starting point, not a checklist, so priorities should be checked with real buyers"]})
open("/home/claude/nmp-decks/decks/ai-powered-market-research/research/121-ai-powered-market-research-deck-04-pain-points-results-research-2026-11-27.md","w").write("\n".join(out))
