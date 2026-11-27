import yaml
out=["# AI-powered market research, chapter 06 Value creation (evergreen, written by Claude, 27 Nov 2026)\n"]
def add(i,d): out.append(f"### {i}\n```yaml\n"+yaml.safe_dump(d,allow_unicode=True,sort_keys=False,width=1000)+"```\n")
L={7:"SURVEY BUILDERS",9:"ONLINE PANELS",11:"VOICE TO TEXT",13:"CHARTS",15:"SENTIMENT SCORES",17:"AI SUMMARIES",19:"AUTO TRANSLATE",21:"SOCIAL LISTENING"}
add("ed101",{"status":"ok","title":"What's commoditized today in the market?",
 "note":"We identified tools that are now broadly available and offered by many companies. They remain necessary, but value is shifting to verified people, proof of validity, owned archives and deep interviews.",
 "t":{**L,6:"Tools to write and send a basic online survey, offered by dozens of firms",8:"Access to opt-in online respondents, sold per answer by many panel firms",
 10:"Speech to text for interview recordings, built into most meeting tools",12:"Charts and reports of survey results, standard in every survey product",
 14:"Positive or negative scores for open answers, offered by most text tools",16:"Short summaries of interviews and answers, made by any general AI assistant",
 18:"Machine translation of questions and answers, cheap and good in most major languages",20:"Tracking of brand mentions on social media, sold by many platforms"}})
add("ed102",{"status":"ok","title":"Why has it become commoditized?",
 "note":"We see commoditization where tools reuse cheap software, open panels and general AI models. New value therefore comes from verified people, proven accuracy and evidence that teams can reuse.",
 "t":{**L,6:"Because survey software has been sold online for more than twenty years",8:"Because many firms resell the same pools of opt-in respondents to each other",
 10:"Because speech models now turn audio into text for a tiny cost per minute",12:"Because charting is a standard feature of survey and analysis tools",
 14:"Because language models read the tone of a sentence without any setup",16:"Because general AI assistants summarize any text for a few cents or less",
 18:"Because machine translation models now handle most languages for free",20:"Because the same social media data feeds are sold to many monitoring firms"}})
add("ed103",{"status":"ok","title":"Where is value created today?","page":"1/2",
 "note":"We derived these elements from the companies that grew fastest and those that struggled. The strongest value today sits in reaching real verified people, probing deeply and proving accuracy.",
 "t":{9:"VERIFIED\nPEOPLE",7:"Panels where each respondent is checked as a real person and a real buyer of the product",
 12:"DEEP AI\nPROBING",10:"AI moderators that ask good follow-up questions and keep the depth of a human interview",
 17:"PROVEN\nACCURACY",15:"Tests showing that AI and synthetic answers match what real people say and later do"}})
add("ed104",{"status":"ok","title":"Where is value created today?","page":"2/2",
 "note":"We derived these elements from recent deals, funding rounds and buyer surveys. Value is increasingly created by owning research archives, fitting enterprise rules and plugging into daily tools.",
 "t":{9:"RESEARCH\nARCHIVES",7:"Searchable stores of past interviews and answers that make each new study faster and cheaper",
 12:"TRUSTED\nSECURITY",10:"Security, consent and AI disclosure that pass the reviews of large brands and their lawyers",
 17:"LINKED\nWORKFLOWS",15:"Connections that send findings into the tools where product and brand teams make decisions"}})
S=[("AI INTERVIEWS","AI interviews","create","AI moderators that interview real buyers by voice, video or text at scale",
 [("INSIGHTS\nTEAMS","They are brand research teams that need dozens of in-depth interviews in days to shape a launch before the date is set"),
  ("UX\nRESEARCHERS","They are product researchers who want many more user interviews with the same team, while keeping depth and quotes"),
  ("GLOBAL\nBRANDS","They are brands that want the same interview run in many countries and languages without a local agency in each"),
  ("RESEARCH\nAGENCIES","They are agencies that want to run more interviews per project and spend their time on analysis and the story"),
  ("CONSULTING\nFIRMS","They are strategy teams that need to hear from many buyers and experts within the tight deadline of a project")],
 "The team writes a short guide, and the AI moderator interviews 100 verified buyers by video in three days. It asks follow-up questions, flags key quotes and clips, and a researcher checks the themes before sharing a clear report with leaders.",
 "The team waits weeks to book a moderator and recruit people, then gets twelve interviews that say little. Notes take days to write up, half the panel turns out to be fake, and the findings arrive after the launch decision was made.",
 {9:"🔍\nA brand team picks an AI interview tool",7:"🎙️\nThe AI runs interviews with real buyers",6:"📝\nThe tool codes answers into themes",8:"💳\nThe brand pays a yearly license",13:"🔁\nThe contract grows to new teams",11:"👥\nMore teams run their own studies",10:"🗂️\nThe archive of interviews grows",12:"✅\nThe launch decision uses the evidence"}),
("AI SURVEYS","AI surveys","create","Survey tools where AI writes, adapts and analyzes questions sent to real people",
 [("BRAND\nMANAGERS","They are brand managers who want to test packs, claims and prices with real buyers every week, not once a quarter"),
  ("PRODUCT\nTEAMS","They are software teams that want quick surveys inside their product, with open answers sorted without manual work"),
  ("RESEARCH\nAGENCIES","They are agencies that want to build and clean surveys faster, so each study costs less and leaves more margin"),
  ("SMALL\nFIRMS","They are smaller firms that cannot hire researchers and want AI to write good questions and explain the results"),
  ("CX\nTEAMS","They are customer experience teams that want to know why scores drop, not only that they dropped last month")],
 "The manager describes the question, and the AI drafts a survey that avoids leading questions. It adapts follow-ups to each answer, removes bots and fake respondents, and explains the results in plain words with charts ready for the team.",
 "The manager writes a long survey with confusing questions and sends it to a cheap panel. Bots and speeders fill a third of the answers, open text goes unread, and the team argues about results no one fully trusts.",
 {9:"🔍\nA team writes its question in plain words",7:"📋\nAI drafts and checks the survey",6:"👥\nReal people answer on a verified panel",8:"💳\nThe team pays per study or a license",13:"🔁\nThe team repeats the survey each month",11:"🏢\nMore teams adopt the tool",10:"📈\nTrends build up across waves",12:"✅\nThe team acts on clear answers"}),
("SYNTHETIC RESPONDENTS","Synthetic respondents","create","AI personas and simulations that answer in place of real buyers and voters",
 [("INNOVATION\nTEAMS","They are teams that screen dozens of ideas and want to drop the weak ones before paying for a full real-world study"),
  ("B2B\nMARKETERS","They are business marketers whose buyers are rare and busy, so a synthetic panel lets them test messages early"),
  ("PRICING\nTEAMS","They are teams that want to try many price and offer options quickly before a real test confirms the best ones"),
  ("AD\nAGENCIES","They are agencies that want fast reactions to many ad ideas, so only the strongest reach a real pretest"),
  ("POLICY\nTEAMS","They are public and campaign teams that want to model how different groups may react to a plan or a message")],
 "The team tests twenty ideas on a synthetic panel built from real survey data in one afternoon. Five ideas stand out, a real study with verified buyers confirms two of them, and the vendor shows how well its answers matched past human results.",
 "The team trusts a synthetic panel with no human benchmark and bets a launch on its answers. The panel misses the views of a small but key group, real buyers react very differently, and the launch fails at a high cost.",
 {9:"🔍\nA team chooses a synthetic panel",7:"🧠\nAI personas answer the questions",6:"📊\nResults are checked against real data",8:"💳\nThe team pays in usage credits",13:"🔁\nMore ideas are screened each month",11:"👥\nMore teams use it early in projects",10:"📈\nThe vendor proves its accuracy",12:"✅\nOnly strong ideas reach real tests"}),
("INSIGHT SYNTHESIS","Insight synthesis","creates","Software that codes interviews and open answers and writes the research report",
 [("RESEARCH\nAGENCIES","They are agencies whose staff spend long hours coding open answers and transcripts by hand for every project"),
  ("UX\nRESEARCHERS","They are product researchers who want to turn hours of recordings into themes, clips and quotes the same day"),
  ("INSIGHTS\nTEAMS","They are brand teams that want to search all past studies at once and stop paying again for answers they own"),
  ("ACADEMIC\nTEAMS","They are university teams that code interviews for studies and need each theme traced back to its source"),
  ("CONSULTING\nFIRMS","They are strategy teams that must check every summary before it reaches a client report and need clear sources")],
 "The researcher uploads fifty transcripts, and the AI groups them into themes in minutes. Each theme links back to the exact quotes, the researcher edits and approves the codes, and the findings join a searchable archive that later teams reuse.",
 "The researcher spends a week coding transcripts by hand, line by line. The summary from a general AI tool invents a quote, no one can trace a theme to its source, and the report is filed in a deck that nobody ever opens again.",
 {9:"🔍\nA team uploads its interviews",7:"📝\nAI codes answers into themes",6:"🔗\nEach theme links to its source",8:"💳\nThe team pays per seat each year",13:"🔁\nNew projects add to the archive",11:"👥\nMore researchers join the workspace",10:"🗂️\nPast studies become searchable",12:"✅\nReports ship faster with sources"}),
("MARKET INTELLIGENCE","Market intelligence","creates","Platforms that track consumer, category and brand trends from many data sources",
 [("CATEGORY\nMANAGERS","They are retail and brand managers who want to see which flavors, claims or formats are rising before rivals do"),
  ("INNOVATION\nTEAMS","They are teams that want early signals of new needs so they can build products before demand peaks"),
  ("BRAND\nSTRATEGISTS","They are strategists who want to track how a brand is seen against rivals, week by week, in each market"),
  ("INVESTORS","They are investors who want early signs that a category or a brand is growing before it shows in sales data"),
  ("RETAILERS","They are retailers that want to know which products to stock next season based on real demand signals")],
 "The manager sees that a new flavor is rising in social posts, searches and sales data across three markets. The platform predicts it will keep growing, a quick study with real buyers confirms it, and the product reaches shelves ahead of rivals.",
 "The manager reads a trend report that is months old and already known to rivals. Signals from social media, search and sales sit in separate tools, the team argues about what they mean, and the product arrives after demand has peaked.",
 {9:"🔍\nA brand subscribes to trend data",7:"🌍\nThe platform tracks many sources",6:"📈\nAI predicts which trends will grow",8:"💳\nThe brand pays a monthly fee",13:"🔁\nNew markets are added",11:"👥\nMore teams use the alerts",10:"📊\nPredictions are checked against sales",12:"✅\nProducts launch ahead of demand"}),
("AD PRETESTING","Ad pretesting","creates","Tools that predict how buyers will react to an ad or a concept before launch",
 [("BRAND\nMARKETERS","They are marketers who spend millions on media and want to know which ad will work before the money goes out"),
  ("CREATIVE\nAGENCIES","They are agencies that want to test more ideas for each brief and show the client why one idea won"),
  ("MEDIA\nPLANNERS","They are planners who want to predict how an ad will perform on each channel before splitting the budget"),
  ("PRODUCT\nTEAMS","They are teams that test product concepts and packs with buyers before they commit to production"),
  ("SOCIAL VIDEO\nTEAMS","They are teams that make many short videos each week and need fast tests that fit their publishing pace")],
 "The team uploads five video ideas, and AI predicts attention and appeal for each in minutes. The two best go to a quick test with real viewers, the winner is tuned before launch, and its sales lift is tracked to improve the next prediction.",
 "The team picks an ad based on the boss's taste and spends the full media budget on it. A slow pretest arrives after launch, the ad fails to hold attention, and no one can say which part went wrong or what to change next time.",
 {9:"🔍\nA brand uploads ad ideas",7:"🎨\nAI predicts attention and appeal",6:"👥\nReal viewers test the best ideas",8:"💳\nThe brand pays per test or a license",13:"🔁\nMore campaigns are tested each year",11:"🏢\nAgencies join the platform",10:"📈\nSales results improve the model",12:"✅\nThe best ad gets the media budget"})]
for k,(cap,name,v,desc,users,good,bad,flow) in enumerate(S,1):
    add(f"ed106-s{k}",{"status":"ok","t":{6:"VALUE CREATION",3:cap,5:desc}})
    t={21:cap}
    for (lab,txt),kl,kt in zip(users,[5,8,11,14,17],[7,10,13,16,19]): t[kl]=lab; t[kt]=txt
    add(f"ed107-s{k}",{"status":"ok","title":"Who needs it the most?","note":f"We focus on five groups where {name[0]+name[1:]} {v} the clearest value today. These are priority use cases, not a full list of clients.","t":t})
    add(f"ed108-s{k}",{"status":"ok","title":"What does \"maximum customer value\" look like in practice?","t":{5:cap,10:"EXCEPTIONAL CUSTOMER EXPERIENCE",7:good,12:"VS",9:"BAD CUSTOMER EXPERIENCE",6:bad}})
    add(f"ed109-s{k}",{"status":"ok","title":"How does the money flow in this case?","t":{14:cap,**flow}})
open("/home/claude/nmp-decks/decks/ai-powered-market-research/research/121-ai-powered-market-research-deck-06-value-creation-results-research-2026-11-27.md","w").write("\n".join(out))
