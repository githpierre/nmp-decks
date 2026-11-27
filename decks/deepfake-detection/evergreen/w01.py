import yaml
out=["# deepfake detection, chapter 01 Market definition (evergreen, written by Claude, 27 Nov 2026)\n"]
def add(i,d): out.append(f"### {i}\n```yaml\n"+yaml.safe_dump(d,allow_unicode=True,sort_keys=False,width=1000)+"```\n")
add("ed006",{"status":"ok","title":"What is deepfake detection, in simple terms?",
 "text":"It is the market for software that checks whether a face, a voice, a video or a document was faked with AI, so banks, call centers and platforms can stop fraud in time",
 "note":"We use a plain definition here because it makes the boundary with identity checks and content moderation, which use detection without being built around it, easier to see.","icon_tl":"🔍"})
add("ed008",{"status":"ok","title":"What markets are often confused with deepfake detection?",
 "t":{12:"IDENTITY CHECKS",13:"DEEPFAKE DETECTION",14:"TRUST & SAFETY",
 7:"Deepfake detection differs from both because it asks one question first, whether a face, voice or image was made by AI",
 10:"Identity checks confirm that a person matches a document, and many now buy deepfake detection as one layer inside",
 11:"Trust and safety teams remove harmful posts of any kind, real or fake, while detection proves what is synthetic"}})
add("ed009",{"status":"ok","title":"What markets does deepfake detection sit between?",
 "t":{8:"CYBER\nSECURITY",9:"IDENTITY\nVERIFICATION",10:"FRAUD\nPREVENTION",
 13:"Deepfake detection sits between three markets: it sells to security teams like other cyber tools, it protects the selfie and video checks of identity verification, and it stops payments in fraud prevention."}})
add("ed010",{"status":"ok","title":"And what if we break it down in smaller markets?",
 "t":{21:"DEEPFAKE DETECTION",5:"MEETING\nPROTECTION",8:"VOICE\nDETECTION",11:"IDENTITY\nCHECKS",14:"MEDIA\nFORENSICS",17:"CONTENT\nPROVENANCE",
 7:"It is in the market when a tool checks that people in a video call are real",
 10:"It is in the market when a call center flags a cloned voice during a live call",
 13:"It is in the market when a selfie or video check spots a fake face at sign-up",
 16:"It is in the market when software proves that an image or video was made by AI",
 19:"It is in the market when a signed record shows where a photo or video came from"}})
add("ed011",{"status":"ok","title":"What are some common acronyms I should know?",
 "note":"We prioritized acronyms that appear often in vendor, regulator and investor materials rather than very technical machine learning terms.",
 "t":{6:"KYC",15:"C2PA",23:"SOC",8:"Know Your\nCustomer",16:"Content Provenance\nCoalition",24:"Security Operations\nCenter",
 17:"It is the group behind Content Credentials, a signed record of where media came from",
 13:"It is the detection of a fake face or mask shown to a camera during a selfie check",
 21:"It is the team that watches company systems and stops attacks, often the buyer here",
 11:"PAD",19:"IDV",27:"AUC",12:"Presentation\nAttack Detection",20:"Identity\nVerification",28:"Area Under\nthe Curve",
 9:"It is the identity check a bank must run on each new client before opening an account",
 4:"It is a check that a new user is who they claim to be, often a selfie and an ID",
 25:"It is a score from 0.5 to 1 that shows how well a detector separates real and fake media"}})
add("ed012",{"status":"no_data","reason":"products and their names change too often to group them reliably without fresh research"})
add("ed013",{"status":"no_data","reason":"prices depend on the volume, the channel and the contract and are rarely published"})
add("ed014",{"status":"ok","title":"When and where is value created in the market?","items":[
 {"e":"📞","t":"When a call center flags a cloned voice before an account is taken over"},
 {"e":"🎥","t":"When a finance worker learns the CFO on a video call is a deepfake"},
 {"e":"🏦","t":"When a bank stops a fake face at sign-up before a mule account is opened"},
 {"e":"💼","t":"When a recruiter spots a fake candidate before giving access to company systems"},
 {"e":"📺","t":"When a newsroom proves a viral video is fake before it spreads further"},
 {"e":"🛡️","t":"When a platform removes fake intimate images within the 48 hours the law sets"},
 {"e":"🔒","t":"When a signed record proves that a photo came from a real camera"},
 {"e":"⚖️","t":"When a detection report holds up for a court, a regulator or an insurer"}]})
add("ed015",{"status":"ok","title":"What are some common myths about deepfake detection?","page":"1/2",
 "note":"We focused on myths that come back often in vendor, regulator and investor debates. The counters describe what tests, losses and deals have shown so far.",
 "t":{9:"People can easily spot a deepfake by eye",7:"In an iProov test of 2,000 people, only 0.1% picked out every real and fake image and video, so the human eye is no longer a reliable defense",
 12:"Deepfakes are mostly a problem of politics",10:"Entrust found that financial services took 94% of deepfake attacks in its 2027 fraud report, and that attacks rose 165% worldwide",
 15:"Only small startups bet on deepfake checks",13:"KPMG took a stake in Reality Defender in 2026, Deel bought Clarity for up to $50M and Entrust paid a reported $650M for Onfido",
 0:"A detector that scores 99% works anywhere",16:"Detectors trained on older fakes lost about half their accuracy on new real-world deepfakes in the public Deepfake-Eval-2024 test"}})
add("ed016",{"status":"ok","title":"What are some common myths about deepfake detection?","page":"2/2",
 "note":"We focused on myths that come back often in vendor, regulator and investor debates. The counters describe what tests, losses and deals have shown so far.",
 "t":{9:"Watermarks will solve the deepfake problem",7:"Free checkers from Google, OpenAI and TikTok read only their own watermarks, and Full Fact found SynthID Detector flagging real images",
 12:"Most companies already have a defense",10:"A 2026 survey of businesses found that 74% saw a suspected deepfake, but only 10% had a detection tool built just for the job",
 15:"Deepfake losses stay small and very rare",13:"An Arup employee in Hong Kong sent about $25.6M after a single video call with deepfakes of the CFO and other colleagues in 2024",
 0:"A listed detection firm is a safe bet",16:"Cyabra's shares fell from a high of $6.20 to $0.09 in November 2026, and it announced a 30-for-1 reverse split to stay listed"}})
add("ed017",{"status":"ok","title":"How mature is deepfake detection as a market?","score":40,
 "text":"The market is real because banks, call centers, platforms and the US Department of Defense pay for detection today. The score stays below the middle because only a small share of firms use it, detectors lose accuracy on new fakes, and buyers often get it as a feature of identity or security tools.",
 "note":["We rate market maturity with an internal score of products on sale, paying clients, big buyers and funding.","We set 40/100 because demand is real, but use stays thin and detectors must keep up with new fakes."]})
add("ed018",{"status":"ok","title":"How can we categorize companies of the deepfake detection market?","page":"1/3",
 "note":"We use the solution groups of our company database, merged into six, from media forensics to signed records of where content came from.",
 "t":{25:"Here, we categorize by type of solution"},"categories":[
 {"label":"MEDIA\nFORENSICS","description":"Tools that check images, videos and audio files for signs of AI","e":"🔬"},
 {"label":"VOICE\nDETECTION","description":"Software that flags cloned voices in calls to banks and call centers","e":"📞"},
 {"label":"MEETING\nPROTECTION","description":"Tools that check that people in a video call are real people","e":"🎥"},
 {"label":"IDENTITY\nCHECKS","description":"Selfie and video checks that spot fake faces at sign-up or login","e":"💳"},
 {"label":"PLATFORM\nSCREENING","description":"Tools that scan uploads at scale for fake or harmful AI media","e":"📱"},
 {"label":"CONTENT\nPROVENANCE","description":"Signed records that show where a photo or a video came from","e":"🔒"}]})
add("ed019",{"status":"ok","title":"How can we categorize companies of the deepfake detection market?","page":"2/3",
 "note":"We also categorize by buyer because banks, call centers, governments and platforms need very different proof, prices and ways to pay.",
 "t":{25:"Here, we categorize by the type of buyer"},"categories":[
 {"label":"BANKS AND\nFINTECHS","description":"Banks and payment apps that check new clients and big transfers","e":"🏦"},
 {"label":"CONTACT\nCENTERS","description":"Call centers that verify callers before they change an account","e":"📞"},
 {"label":"GOVERNMENT\nAGENCIES","description":"Defense, police and election bodies that check media and identities","e":"🏛️"},
 {"label":"NEWSROOMS AND\nPLATFORMS","description":"Media groups and social apps that check what people upload","e":"📺"},
 {"label":"SECURITY\nTEAMS","description":"Company security teams that guard calls, meetings and hiring","e":"🛡️"},
 {"label":"HR AND\nRECRUITERS","description":"Hiring teams that check that remote candidates are real people","e":"💼"}]})
add("ed020",{"status":"ok","title":"How can we categorize companies of the deepfake detection market?","page":"3/3",
 "note":"A third useful lens is the business model, because an API call, a seat license or a government contract earns money very differently.",
 "t":{25:"Here, we categorize by business model"},"categories":[
 {"label":"API\nCALLS","description":"Charging for each image, video, call or selfie that is checked","e":"🔌"},
 {"label":"ENTERPRISE\nLICENSES","description":"Charging a yearly fee for a platform used across a large firm","e":"📄"},
 {"label":"PER-SEAT\nPLANS","description":"Charging for each employee protected in calls and meetings","e":"👥"},
 {"label":"GOVERNMENT\nCONTRACTS","description":"Winning paid projects with defense, police and public agencies","e":"🏛️"},
 {"label":"MARKETPLACE\nSALES","description":"Selling through the stores of Zoom, FICO or cloud platforms","e":"🛒"},
 {"label":"FORENSIC\nSERVICES","description":"Adding experts who analyze media and write reports for a case","e":"⚖️"}]})
add("ed021",{"status":"ok","title":"What do top companies do in this market?",
 "note":"Other companies could also make the top eight. We chose startups with the most clients, funding, contracts or big partners to show the range of the market.",
 "t":{8:"PINDROP",16:"HIVE",7:"It checks callers' voices for banks and call centers, and runs inside NiCE and Zoom",
 15:"It won a $2.4M contract from the US Department of Defense, chosen among 36 firms",
 10:"RESEMBLE AI",18:"DOPPEL",9:"Microsoft named it a certified partner for deepfake checks in Teams in 2026",
 17:"It tracks impersonation across many channels, and was valued above $600M",
 12:"INCODE",20:"REALITY DEFENDER",11:"Its Deepsight check runs at Scotiabank, Nubank and TikTok in live sessions",
 19:"It detects fake media across voice, video and images, and KPMG took a stake in it in 2026",
 14:"SENSITY",22:"GETREAL",13:"It checks images and videos for signs of AI for police, banks and courts",
 21:"Gartner placed it furthest on market disruption, and it protects Teams calls"}})
add("ed022",{"status":"ok","title":"What is rare and that people happily pay for in this market?",
 "note":"We looked at funding rounds, deals, failures and test results to find the capabilities that look truly scarce and valuable.",
 "t":{6:"🧪\nFresh training data, because detectors fail on fakes from the newest AI models",
 7:"📊\nProof in real conditions, because lab scores fall on compressed real-world media",
 8:"⚡\nLive speed, because a call or a selfie check must decide in under a second",
 9:"🔌\nPlace in daily tools, because buyers want checks inside Zoom, Teams and call centers",
 10:"⚖️\nReports that hold up, because courts and regulators ask how a verdict was reached",
 11:"🏦\nBank contracts, because one large bank can send millions of checks each month",
 12:"🎯\nFew false alarms, because a wrong flag blocks a real client or a real story",
 13:"🏛️\nGovernment trust, because defense and police work needs approved vendors"}})
add("ed023",{"status":"ok","title":"Which deepfake detection truths have flipped?",
 "note":"These are market shifts we see in recent deals, failures and company releases. They are not formal industry rules, but they come back across the evidence.",
 "t":{6:"Deepfakes used to be mostly a political and celebrity issue",8:"Now financial services take 94% of the deepfake attacks Entrust sees",
 10:"A cloned voice used to be a rare, one-off scam",12:"Now Pindrop and banks see deepfake calls every day at scale",
 14:"Seeing a person on video used to prove who they were",16:"Now a full video call of fake colleagues cost Arup about $25.6M",
 18:"Detection used to be a research project funded by DARPA",20:"Now Gartner rates deepfake detection startups for large buyers",
 22:"Fake intimate images used to have no clear federal rule",24:"Now the TAKE IT DOWN Act makes platforms remove them within 48 hours",
 26:"Detection used to be sold as a standalone product",28:"Now Deel, Entrust and LexisNexis buy it to put inside their own"}})
add("ed024",{"status":"ok","title":"What has changed (very) recently?","page":"1/2","items":[
 {"d":"SINCE 2024","t":"An Arup employee in Hong Kong sent about $25.6M in early 2024 after a video call with deepfakes of the CFO and colleagues, a warning heard by every corporate finance team."},
 {"d":"SINCE 2024","t":"Entrust completed its purchase of Onfido in April 2024 for a reported $650M, bringing deepfake defense for selfie and document checks into a large security group."},
 {"d":"SINCE 2024","t":"FinCEN issued an alert on deepfake fraud schemes on November 13, 2024, reminding US banks to report suspicious activity that involves fake media and identities."},
 {"d":"SINCE 2025","t":"GetReal Security raised a $17.5M Series A in March 2025, co-founded by Hany Farid, to sell deepfake forensics and live checks to companies and governments."},
 {"d":"SINCE 2025","t":"The TAKE IT DOWN Act became US law in May 2025, requiring platforms to remove fake intimate images within 48 hours, with FTC enforcement from May 2026."},
 {"d":"SINCE 2025","t":"Doppel raised a $70M Series C in November 2025 at a valuation above $600M, three times its value six months earlier, to track impersonation across channels."}],
 "note":["We kept the milestones that most changed the products, the money and the big players of the market","There is no official timeline, and another analyst could reasonably pick a few different milestones here"]})
add("ed025",{"status":"ok","title":"What has changed (very) recently?","page":"2/2","items":[
 {"d":"SINCE 2026","t":"GetReal made continuous identity checks in video meetings generally available in May 2026, a sign that detection is moving into live calls on Teams and Webex."},
 {"d":"SINCE 2026","t":"Gartner published its first Emerging Market Quadrant for deepfake detection in June 2026, giving large buyers a framework to compare startups in the market."},
 {"d":"SINCE 2026","t":"Deel bought Clarity in August 2026 in a deal estimated at $40M to $50M, to check that remote job candidates are real people and not deepfakes."},
 {"d":"SINCE 2026","t":"The transparency duties of Article 50 of the EU AI Act began to apply on August 2, 2026, including labels for deepfakes and marks on AI outputs."},
 {"d":"SINCE 2026","t":"KPMG took a minority stake in Reality Defender in 2026, a sign that large advisory firms want to sell deepfake defense to their own clients."},
 {"d":"SINCE 2026","t":"Entrust's identity fraud report of November 2026 found that deepfake attacks rose 165% in a year, with financial services taking 94% of them."}],
 "note":["We kept the milestones that most changed the products, the money and the big players of the market","There is no official timeline, and another analyst could reasonably pick a few different milestones here"]})
open("/home/claude/nmp-decks/decks/deepfake-detection/research/147-deepfake-detection-deck-01-market-definition-results-research-2026-11-27.md","w").write("\n".join(out))
