# deepfake detection, chapter 06 Value creation (evergreen, written by Claude, 27 Nov 2026)

### ed101
```yaml
status: ok
title: What's commoditized today in the market?
note: We identified tools that are now broadly available and offered by many companies. They remain necessary, but value is shifting to fresh training data, live checks, proof in real use and evidence reports.
t:
  7: FACE MATCHING
  9: PHOTO LIVENESS
  11: METADATA
  13: REVERSE SEARCH
  15: AI WATERMARK
  17: SPAM FILTERS
  19: CALLER ID
  21: BLOCK LISTS
  6: Matching a selfie to the photo on an ID card, offered by dozens of firms
  8: Basic checks that a selfie is not a printed photo, built into most ID tools
  10: Reading the date, camera and edits stored in a file, free in many tools
  12: Finding where an image appeared online before, free with any search engine
  14: Invisible marks that AI firms add to their own images and read for free
  16: Filters that block known scam messages and links, standard in email tools
  18: Showing the number and name of a caller, built into phones and networks
  20: Lists of known fraud numbers, devices and accounts shared across firms
```

### ed102
```yaml
status: ok
title: Why has it become commoditized?
note: We see commoditization where tools reuse cheap software, open data and checks that new AI fakes now beat. New value therefore comes from detecting what is synthetic, live and at scale.
t:
  7: FACE MATCHING
  9: PHOTO LIVENESS
  11: METADATA
  13: REVERSE SEARCH
  15: AI WATERMARK
  17: SPAM FILTERS
  19: CALLER ID
  21: BLOCK LISTS
  6: Because face matching models are mature and cheap to run at scale
  8: Because printed photos and masks are old attacks every vendor blocks
  10: Because metadata is easy to read and just as easy for fraudsters to fake
  12: Because image search engines index billions of photos for anyone
  14: Because Google, OpenAI and TikTok give away checkers for their own marks
  16: Because email providers have filtered spam for over twenty years
  18: Because caller ID is free and can be spoofed by any fraudster
  20: Because fraud teams share these lists through networks and vendors
```

### ed103
```yaml
status: ok
title: Where is value created today?
page: 1/2
note: We derived these elements from the companies that grew fastest and those that struggled. The strongest value today sits in fresh training data, live checks and proof that holds in real use.
t:
  9: 'FRESH

    DATA'
  7: Training data from the newest AI models, so detectors keep up with each new kind of fake
  12: 'LIVE

    CHECKS'
  10: Checks that run during a call, a meeting or a selfie in under a second, before harm is done
  17: 'REAL-WORLD

    PROOF'
  15: Tests on compressed, low-quality media from real attacks, not just on clean lab datasets
```

### ed104
```yaml
status: ok
title: Where is value created today?
page: 2/2
note: We derived these elements from recent deals, funding rounds and buyer surveys. Value is increasingly created by fitting into daily tools, writing reports that hold up and proving where media came from.
t:
  9: 'BUILT-IN

    PLACEMENT'
  7: Checks that run inside Zoom, Teams, call center software and identity flows buyers already use
  12: 'EVIDENCE

    REPORTS'
  10: Reports that explain how a file was faked, so courts, regulators and insurers can rely on them
  17: 'SIGNED

    ORIGIN'
  15: Signed records from cameras and apps that prove where a photo or a video really came from
```

### ed106-s1
```yaml
status: ok
t:
  6: VALUE CREATION
  3: MEDIA FORENSICS
  5: Tools that check images, videos and audio files for signs of AI
```

### ed107-s1
```yaml
status: ok
title: Who needs it the most?
note: We focus on five groups where media forensics creates the clearest value today. These are priority use cases, not a full list of clients.
t:
  21: MEDIA FORENSICS
  5: 'NEWS

    ROOMS'
  7: They are media groups that must prove a viral clip is fake within hours, before they report on it or it spreads
  8: 'POLICE

    UNITS'
  10: They are investigators who need to show a court how a photo or video was faked, with a clear written report
  11: 'INSURANCE

    CLAIMS'
  13: They are claims teams that see AI-made photos of damage and need to check them before they pay a claim
  14: 'LAW

    FIRMS'
  16: They are lawyers who must check evidence in disputes, as fake audio and video now appear in court cases
  17: 'DEFENSE

    AGENCIES'
  19: They are defense and intelligence teams that must judge fake images fast during a crisis or a conflict
```

### ed108-s1
```yaml
status: ok
title: What does "maximum customer value" look like in practice?
t:
  5: MEDIA FORENSICS
  10: EXCEPTIONAL CUSTOMER EXPERIENCE
  7: The team uploads a viral video, and the tool flags it as AI-made in minutes. It shows which frames were changed and why, an expert checks the result, and a report goes to editors or a court with each finding explained.
  12: VS
  9: BAD CUSTOMER EXPERIENCE
  6: The team sends the video to an outside lab and waits days for a verdict. By then the fake has spread, the tool gives a score with no reason, and a lawyer argues the result in court because no one can explain it.
```

### ed109-s1
```yaml
status: ok
title: How does the money flow in this case?
t:
  14: MEDIA FORENSICS
  9: '🔍

    A newsroom picks a forensic tool'
  7: '📤

    Its staff upload suspect files'
  6: '🔬

    The tool flags signs of AI'
  8: '💳

    The newsroom pays a yearly license'
  13: '🔁

    The contract adds more users'
  11: '👥

    More teams check their files'
  10: '📄

    Reports explain each verdict'
  12: '✅

    The fake is exposed in time'
```

### ed106-s2
```yaml
status: ok
t:
  6: VALUE CREATION
  3: VOICE DETECTION
  5: Software that flags cloned voices in calls to banks and call centers
```

### ed107-s2
```yaml
status: ok
title: Who needs it the most?
note: We focus on five groups where voice detection creates the clearest value today. These are priority use cases, not a full list of clients.
t:
  21: VOICE DETECTION
  5: 'RETAIL

    BANKS'
  7: They are banks whose call centers get cloned voices of clients asking to move money or change account details
  8: 'INSURANCE

    FIRMS'
  10: They are insurers whose phone lines receive fake claims and requests to change who receives a payout
  11: 'HEALTH

    PLANS'
  13: They are health plans and benefit firms whose members' accounts are targeted by callers using cloned voices
  14: 'ONLINE

    RETAILERS'
  16: They are retailers whose service lines face account takeovers and refund fraud by callers with fake voices
  17: 'TELECOM

    FIRMS'
  19: They are phone networks that want to stop scam calls with cloned voices before they reach their customers
```

### ed108-s2
```yaml
status: ok
title: What does "maximum customer value" look like in practice?
t:
  5: VOICE DETECTION
  10: EXCEPTIONAL CUSTOMER EXPERIENCE
  7: The caller asks to change an account, and the tool flags a synthetic voice within seconds. The agent gets a clear alert, the caller is sent to a stronger check, and the fraud ring is blocked across all the bank's lines.
  12: VS
  9: BAD CUSTOMER EXPERIENCE
  6: The caller sounds exactly like the client and answers every security question. The agent changes the account, money leaves the next day, and the bank only learns of the fraud when the real client calls in weeks later.
```

### ed109-s2
```yaml
status: ok
title: How does the money flow in this case?
t:
  14: VOICE DETECTION
  9: '🔍

    A bank adds voice detection'
  7: '📞

    Calls run through the tool'
  6: '⚠️

    It flags synthetic voices'
  8: '💳

    The bank pays per call checked'
  13: '🔁

    More call centers are added'
  11: '🏢

    Other lines of business join'
  10: '📊

    Fraud losses fall over time'
  12: '✅

    Accounts stay with real clients'
```

### ed106-s3
```yaml
status: ok
t:
  6: VALUE CREATION
  3: MEETING PROTECTION
  5: Tools that check that people in a video call are real people
```

### ed107-s3
```yaml
status: ok
title: Who needs it the most?
note: We focus on five groups where meeting protection creates the clearest value today. These are priority use cases, not a full list of clients.
t:
  21: MEETING PROTECTION
  5: 'FINANCE

    TEAMS'
  7: They are finance staff who receive payment orders on video calls and must know the CFO on screen is real
  8: 'TOP

    EXECUTIVES'
  10: They are leaders whose face and voice are cloned to trick staff, partners and investors on video calls
  11: 'HR AND

    RECRUITERS'
  13: They are hiring teams that interview candidates by video and must check that each one is a real person
  14: 'IT HELP

    DESKS'
  16: They are help desks that verify employees by video before they reset a password or give system access
  17: 'LAW

    FIRMS'
  19: They are lawyers who hold sensitive calls with clients and must be sure no one on the call is a fake
```

### ed108-s3
```yaml
status: ok
title: What does "maximum customer value" look like in practice?
t:
  5: MEETING PROTECTION
  10: EXCEPTIONAL CUSTOMER EXPERIENCE
  7: The CFO joins a video call to approve a payment, and the tool checks each face and voice in real time. A fake attendee is flagged before anyone acts, the payment is stopped, and security gets a record of the attempt.
  12: VS
  9: BAD CUSTOMER EXPERIENCE
  6: A finance worker joins a call where every face looks like a colleague. The CFO asks for urgent transfers, the worker sends them, and the company learns days later that every person on the call was a deepfake.
```

### ed109-s3
```yaml
status: ok
title: How does the money flow in this case?
t:
  14: MEETING PROTECTION
  9: '🔍

    A company adds meeting checks'
  7: '🎥

    The tool joins each video call'
  6: '🔬

    It checks faces and voices live'
  8: '💳

    The company pays per seat'
  13: '🔁

    More staff are covered'
  11: '🏢

    More teams turn it on'
  10: '📊

    Blocked attempts prove value'
  12: '✅

    Payments go only to real orders'
```

### ed106-s4
```yaml
status: ok
t:
  6: VALUE CREATION
  3: IDENTITY CHECKS
  5: Selfie and video checks that spot fake faces at sign-up or login
```

### ed107-s4
```yaml
status: ok
title: Who needs it the most?
note: We focus on five groups where identity checks creates the clearest value today. These are priority use cases, not a full list of clients.
t:
  21: IDENTITY CHECKS
  5: 'DIGITAL

    BANKS'
  7: They are online banks that open accounts by selfie and must stop fake faces used to open mule accounts
  8: 'FINTECH

    APPS'
  10: They are payment and lending apps that check millions of new users and cannot slow down each sign-up
  11: 'CRYPTO

    EXCHANGES'
  13: They are crypto platforms that must check new users by law and face many attacks with fake faces
  14: 'GIG

    PLATFORMS'
  16: They are ride and delivery apps that check workers' faces and see accounts rented or faked with AI
  17: 'PUBLIC

    AGENCIES'
  19: They are public agencies that check citizens online for benefits, taxes and digital identity cards
```

### ed108-s4
```yaml
status: ok
title: What does "maximum customer value" look like in practice?
t:
  5: IDENTITY CHECKS
  10: EXCEPTIONAL CUSTOMER EXPERIENCE
  7: The new user takes a selfie, and the check spots an AI-made face in under a second. Real users pass without friction, fraud teams see each blocked attempt, and the bank can show regulators how every check worked.
  12: VS
  9: BAD CUSTOMER EXPERIENCE
  6: The fraudster shows an AI-made face to the camera and passes a basic photo check. The account opens, it is used to move stolen money, and the bank only finds out when a regulator asks why it missed the fraud.
```

### ed109-s4
```yaml
status: ok
title: How does the money flow in this case?
t:
  14: IDENTITY CHECKS
  9: '🔍

    A bank picks an identity check'
  7: '📱

    New users take a selfie'
  6: '🔬

    The check spots fake faces'
  8: '💳

    The bank pays per check'
  13: '🔁

    Logins are checked as well'
  11: '👥

    Volumes grow with new clients'
  10: '📊

    Fraud rates fall at sign-up'
  12: '✅

    Only real people open accounts'
```

### ed106-s5
```yaml
status: ok
t:
  6: VALUE CREATION
  3: PLATFORM SCREENING
  5: Tools that scan uploads at scale for fake or harmful AI media
```

### ed107-s5
```yaml
status: ok
title: Who needs it the most?
note: We focus on five groups where platform screening creates the clearest value today. These are priority use cases, not a full list of clients.
t:
  21: PLATFORM SCREENING
  5: 'SOCIAL

    PLATFORMS'
  7: They are social apps that receive millions of uploads a day and must find fake and harmful AI media
  8: 'DATING

    APPS'
  10: They are dating apps where fake profiles with AI photos are used for scams and must be removed fast
  11: 'MARKET

    PLACES'
  13: They are online stores where AI photos make fake listings and fake reviews look real to buyers
  14: 'ADULT

    SITES'
  16: They are sites that must remove fake intimate images within 48 hours under the TAKE IT DOWN Act
  17: 'CHILD SAFETY

    GROUPS'
  19: They are groups that sort real abuse images from AI-made ones, as reports of AI images rise fast
```

### ed108-s5
```yaml
status: ok
title: What does "maximum customer value" look like in practice?
t:
  5: PLATFORM SCREENING
  10: EXCEPTIONAL CUSTOMER EXPERIENCE
  7: Each upload is scanned in milliseconds, and AI-made media is flagged before it is shown to anyone. The few doubtful items go to a human reviewer, takedown requests are met within the legal limit, and the cost per item stays low.
  12: VS
  9: BAD CUSTOMER EXPERIENCE
  6: Fake media goes live and spreads for days before anyone reports it. Moderators review items by hand, the platform misses the legal deadline for removal, and regulators and the press ask why it did nothing.
```

### ed109-s5
```yaml
status: ok
title: How does the money flow in this case?
t:
  14: PLATFORM SCREENING
  9: '🔍

    A platform adds AI screening'
  7: '📤

    Uploads pass through the tool'
  6: '⚠️

    It flags AI-made media'
  8: '💳

    The platform pays per item'
  13: '🔁

    New types of media are added'
  11: '📈

    Volumes grow with each launch'
  10: '🛡️

    Takedowns meet legal limits'
  12: '✅

    Harmful fakes never go live'
```

### ed106-s6
```yaml
status: ok
t:
  6: VALUE CREATION
  3: CONTENT PROVENANCE
  5: Signed records that show where a photo or a video came from
```

### ed107-s6
```yaml
status: ok
title: Who needs it the most?
note: We focus on five groups where content provenance creates the clearest value today. These are priority use cases, not a full list of clients.
t:
  21: CONTENT PROVENANCE
  5: 'CAMERA

    MAKERS'
  7: They are camera and phone makers that add signed records of origin to each photo their devices take
  8: 'NEWS

    AGENCIES'
  10: They are news agencies that want readers to see that a photo came from their own photographer
  11: 'INSURANCE

    FIRMS'
  13: They are insurers that ask clients to take claim photos in apps that sign each image at capture
  14: 'CONSUMER

    BRANDS'
  16: They are companies that sign their own ads and videos so fakes of their brand are easy to spot
  17: 'SOCIAL

    PLATFORMS'
  19: They are social and search platforms that read signed records and show labels to their users
```

### ed108-s6
```yaml
status: ok
title: What does "maximum customer value" look like in practice?
t:
  5: CONTENT PROVENANCE
  10: EXCEPTIONAL CUSTOMER EXPERIENCE
  7: The photographer takes a photo with a camera that signs it at capture. Each edit is recorded, the newsroom publishes it with a visible label, and readers can check its origin while fakes without a record stand out.
  12: VS
  9: BAD CUSTOMER EXPERIENCE
  6: A real photo is shared without any record and called a fake by people who dislike it. At the same time, an AI image looks just as real, and readers have no way to tell which one to trust.
```

### ed109-s6
```yaml
status: ok
title: How does the money flow in this case?
t:
  14: CONTENT PROVENANCE
  9: '🔍

    A camera maker joins the C2PA'
  7: '📷

    Its devices sign each photo'
  6: '🔒

    Edits are added to the record'
  8: '💳

    The tool vendor is paid per device'
  13: '🔁

    More apps read the records'
  11: '📰

    News groups require signed photos'
  10: '🏷️

    Platforms show origin labels'
  12: '✅

    Readers trust real photos'
```
