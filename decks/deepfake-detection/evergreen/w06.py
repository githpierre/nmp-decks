import yaml
out=["# deepfake detection, chapter 06 Value creation (evergreen, written by Claude, 27 Nov 2026)\n"]
def add(i,d): out.append(f"### {i}\n```yaml\n"+yaml.safe_dump(d,allow_unicode=True,sort_keys=False,width=1000)+"```\n")
L={7:"FACE MATCHING",9:"PHOTO LIVENESS",11:"METADATA",13:"REVERSE SEARCH",15:"AI WATERMARK",17:"SPAM FILTERS",19:"CALLER ID",21:"BLOCK LISTS"}
add("ed101",{"status":"ok","title":"What's commoditized today in the market?",
 "note":"We identified tools that are now broadly available and offered by many companies. They remain necessary, but value is shifting to fresh training data, live checks, proof in real use and evidence reports.",
 "t":{**L,6:"Matching a selfie to the photo on an ID card, offered by dozens of firms",8:"Basic checks that a selfie is not a printed photo, built into most ID tools",
 10:"Reading the date, camera and edits stored in a file, free in many tools",12:"Finding where an image appeared online before, free with any search engine",
 14:"Invisible marks that AI firms add to their own images and read for free",16:"Filters that block known scam messages and links, standard in email tools",
 18:"Showing the number and name of a caller, built into phones and networks",20:"Lists of known fraud numbers, devices and accounts shared across firms"}})
add("ed102",{"status":"ok","title":"Why has it become commoditized?",
 "note":"We see commoditization where tools reuse cheap software, open data and checks that new AI fakes now beat. New value therefore comes from detecting what is synthetic, live and at scale.",
 "t":{**L,6:"Because face matching models are mature and cheap to run at scale",8:"Because printed photos and masks are old attacks every vendor blocks",
 10:"Because metadata is easy to read and just as easy for fraudsters to fake",12:"Because image search engines index billions of photos for anyone",
 14:"Because Google, OpenAI and TikTok give away checkers for their own marks",16:"Because email providers have filtered spam for over twenty years",
 18:"Because caller ID is free and can be spoofed by any fraudster",20:"Because fraud teams share these lists through networks and vendors"}})
add("ed103",{"status":"ok","title":"Where is value created today?","page":"1/2",
 "note":"We derived these elements from the companies that grew fastest and those that struggled. The strongest value today sits in fresh training data, live checks and proof that holds in real use.",
 "t":{9:"FRESH\nDATA",7:"Training data from the newest AI models, so detectors keep up with each new kind of fake",
 12:"LIVE\nCHECKS",10:"Checks that run during a call, a meeting or a selfie in under a second, before harm is done",
 17:"REAL-WORLD\nPROOF",15:"Tests on compressed, low-quality media from real attacks, not just on clean lab datasets"}})
add("ed104",{"status":"ok","title":"Where is value created today?","page":"2/2",
 "note":"We derived these elements from recent deals, funding rounds and buyer surveys. Value is increasingly created by fitting into daily tools, writing reports that hold up and proving where media came from.",
 "t":{9:"BUILT-IN\nPLACEMENT",7:"Checks that run inside Zoom, Teams, call center software and identity flows buyers already use",
 12:"EVIDENCE\nREPORTS",10:"Reports that explain how a file was faked, so courts, regulators and insurers can rely on them",
 17:"SIGNED\nORIGIN",15:"Signed records from cameras and apps that prove where a photo or a video really came from"}})
S=[("MEDIA FORENSICS","Media forensics","create","Tools that check images, videos and audio files for signs of AI",
 [("NEWS\nROOMS","They are media groups that must prove a viral clip is fake within hours, before they report on it or it spreads"),
  ("POLICE\nUNITS","They are investigators who need to show a court how a photo or video was faked, with a clear written report"),
  ("INSURANCE\nCLAIMS","They are claims teams that see AI-made photos of damage and need to check them before they pay a claim"),
  ("LAW\nFIRMS","They are lawyers who must check evidence in disputes, as fake audio and video now appear in court cases"),
  ("DEFENSE\nAGENCIES","They are defense and intelligence teams that must judge fake images fast during a crisis or a conflict")],
 "The team uploads a viral video, and the tool flags it as AI-made in minutes. It shows which frames were changed and why, an expert checks the result, and a report goes to editors or a court with each finding explained.",
 "The team sends the video to an outside lab and waits days for a verdict. By then the fake has spread, the tool gives a score with no reason, and a lawyer argues the result in court because no one can explain it.",
 {9:"🔍\nA newsroom picks a forensic tool",7:"📤\nIts staff upload suspect files",6:"🔬\nThe tool flags signs of AI",8:"💳\nThe newsroom pays a yearly license",13:"🔁\nThe contract adds more users",11:"👥\nMore teams check their files",10:"📄\nReports explain each verdict",12:"✅\nThe fake is exposed in time"}),
("VOICE DETECTION","Voice detection","create","Software that flags cloned voices in calls to banks and call centers",
 [("RETAIL\nBANKS","They are banks whose call centers get cloned voices of clients asking to move money or change account details"),
  ("INSURANCE\nFIRMS","They are insurers whose phone lines receive fake claims and requests to change who receives a payout"),
  ("HEALTH\nPLANS","They are health plans and benefit firms whose members' accounts are targeted by callers using cloned voices"),
  ("ONLINE\nRETAILERS","They are retailers whose service lines face account takeovers and refund fraud by callers with fake voices"),
  ("TELECOM\nFIRMS","They are phone networks that want to stop scam calls with cloned voices before they reach their customers")],
 "The caller asks to change an account, and the tool flags a synthetic voice within seconds. The agent gets a clear alert, the caller is sent to a stronger check, and the fraud ring is blocked across all the bank's lines.",
 "The caller sounds exactly like the client and answers every security question. The agent changes the account, money leaves the next day, and the bank only learns of the fraud when the real client calls in weeks later.",
 {9:"🔍\nA bank adds voice detection",7:"📞\nCalls run through the tool",6:"⚠️\nIt flags synthetic voices",8:"💳\nThe bank pays per call checked",13:"🔁\nMore call centers are added",11:"🏢\nOther lines of business join",10:"📊\nFraud losses fall over time",12:"✅\nAccounts stay with real clients"}),
("MEETING PROTECTION","Meeting protection","create","Tools that check that people in a video call are real people",
 [("FINANCE\nTEAMS","They are finance staff who receive payment orders on video calls and must know the CFO on screen is real"),
  ("TOP\nEXECUTIVES","They are leaders whose face and voice are cloned to trick staff, partners and investors on video calls"),
  ("HR AND\nRECRUITERS","They are hiring teams that interview candidates by video and must check that each one is a real person"),
  ("IT HELP\nDESKS","They are help desks that verify employees by video before they reset a password or give system access"),
  ("LAW\nFIRMS","They are lawyers who hold sensitive calls with clients and must be sure no one on the call is a fake")],
 "The CFO joins a video call to approve a payment, and the tool checks each face and voice in real time. A fake attendee is flagged before anyone acts, the payment is stopped, and security gets a record of the attempt.",
 "A finance worker joins a call where every face looks like a colleague. The CFO asks for urgent transfers, the worker sends them, and the company learns days later that every person on the call was a deepfake.",
 {9:"🔍\nA company adds meeting checks",7:"🎥\nThe tool joins each video call",6:"🔬\nIt checks faces and voices live",8:"💳\nThe company pays per seat",13:"🔁\nMore staff are covered",11:"🏢\nMore teams turn it on",10:"📊\nBlocked attempts prove value",12:"✅\nPayments go only to real orders"}),
("IDENTITY CHECKS","Identity checks","create","Selfie and video checks that spot fake faces at sign-up or login",
 [("DIGITAL\nBANKS","They are online banks that open accounts by selfie and must stop fake faces used to open mule accounts"),
  ("FINTECH\nAPPS","They are payment and lending apps that check millions of new users and cannot slow down each sign-up"),
  ("CRYPTO\nEXCHANGES","They are crypto platforms that must check new users by law and face many attacks with fake faces"),
  ("GIG\nPLATFORMS","They are ride and delivery apps that check workers' faces and see accounts rented or faked with AI"),
  ("PUBLIC\nAGENCIES","They are public agencies that check citizens online for benefits, taxes and digital identity cards")],
 "The new user takes a selfie, and the check spots an AI-made face in under a second. Real users pass without friction, fraud teams see each blocked attempt, and the bank can show regulators how every check worked.",
 "The fraudster shows an AI-made face to the camera and passes a basic photo check. The account opens, it is used to move stolen money, and the bank only finds out when a regulator asks why it missed the fraud.",
 {9:"🔍\nA bank picks an identity check",7:"📱\nNew users take a selfie",6:"🔬\nThe check spots fake faces",8:"💳\nThe bank pays per check",13:"🔁\nLogins are checked as well",11:"👥\nVolumes grow with new clients",10:"📊\nFraud rates fall at sign-up",12:"✅\nOnly real people open accounts"}),
("PLATFORM SCREENING","Platform screening","create","Tools that scan uploads at scale for fake or harmful AI media",
 [("SOCIAL\nPLATFORMS","They are social apps that receive millions of uploads a day and must find fake and harmful AI media"),
  ("DATING\nAPPS","They are dating apps where fake profiles with AI photos are used for scams and must be removed fast"),
  ("MARKET\nPLACES","They are online stores where AI photos make fake listings and fake reviews look real to buyers"),
  ("ADULT\nSITES","They are sites that must remove fake intimate images within 48 hours under the TAKE IT DOWN Act"),
  ("CHILD SAFETY\nGROUPS","They are groups that sort real abuse images from AI-made ones, as reports of AI images rise fast")],
 "Each upload is scanned in milliseconds, and AI-made media is flagged before it is shown to anyone. The few doubtful items go to a human reviewer, takedown requests are met within the legal limit, and the cost per item stays low.",
 "Fake media goes live and spreads for days before anyone reports it. Moderators review items by hand, the platform misses the legal deadline for removal, and regulators and the press ask why it did nothing.",
 {9:"🔍\nA platform adds AI screening",7:"📤\nUploads pass through the tool",6:"⚠️\nIt flags AI-made media",8:"💳\nThe platform pays per item",13:"🔁\nNew types of media are added",11:"📈\nVolumes grow with each launch",10:"🛡️\nTakedowns meet legal limits",12:"✅\nHarmful fakes never go live"}),
("CONTENT PROVENANCE","Content provenance","create","Signed records that show where a photo or a video came from",
 [("CAMERA\nMAKERS","They are camera and phone makers that add signed records of origin to each photo their devices take"),
  ("NEWS\nAGENCIES","They are news agencies that want readers to see that a photo came from their own photographer"),
  ("INSURANCE\nFIRMS","They are insurers that ask clients to take claim photos in apps that sign each image at capture"),
  ("CONSUMER\nBRANDS","They are companies that sign their own ads and videos so fakes of their brand are easy to spot"),
  ("SOCIAL\nPLATFORMS","They are social and search platforms that read signed records and show labels to their users")],
 "The photographer takes a photo with a camera that signs it at capture. Each edit is recorded, the newsroom publishes it with a visible label, and readers can check its origin while fakes without a record stand out.",
 "A real photo is shared without any record and called a fake by people who dislike it. At the same time, an AI image looks just as real, and readers have no way to tell which one to trust.",
 {9:"🔍\nA camera maker joins the C2PA",7:"📷\nIts devices sign each photo",6:"🔒\nEdits are added to the record",8:"💳\nThe tool vendor is paid per device",13:"🔁\nMore apps read the records",11:"📰\nNews groups require signed photos",10:"🏷️\nPlatforms show origin labels",12:"✅\nReaders trust real photos"})]
for k,(cap,name,v,desc,users,good,bad,flow) in enumerate(S,1):
    add(f"ed106-s{k}",{"status":"ok","t":{6:"VALUE CREATION",3:cap,5:desc}})
    t={21:cap}
    for (lab,txt),kl,kt in zip(users,[5,8,11,14,17],[7,10,13,16,19]): t[kl]=lab; t[kt]=txt
    nm=name[0].lower()+name[1:]
    add(f"ed107-s{k}",{"status":"ok","title":"Who needs it the most?","note":f"We focus on five groups where {nm} creates the clearest value today. These are priority use cases, not a full list of clients.","t":t})
    add(f"ed108-s{k}",{"status":"ok","title":"What does \"maximum customer value\" look like in practice?","t":{5:cap,10:"EXCEPTIONAL CUSTOMER EXPERIENCE",7:good,12:"VS",9:"BAD CUSTOMER EXPERIENCE",6:bad}})
    add(f"ed109-s{k}",{"status":"ok","title":"How does the money flow in this case?","t":{14:cap,**flow}})
open("/home/claude/nmp-decks/decks/deepfake-detection/research/147-deepfake-detection-deck-06-value-creation-results-research-2026-11-27.md","w").write("\n".join(out))
