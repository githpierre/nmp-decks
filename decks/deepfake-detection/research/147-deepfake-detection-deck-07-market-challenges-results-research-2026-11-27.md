# Deepfake detection deck, chapter 07: Market challenges

### ed132
```yaml
status: ok
title: What do newcomers often miss here?
note: "We grouped recurring issues from independent benchmarks, buyer surveys and vendor disclosures. The field improves fast, but no detector is reliable on every new generator or channel."
t:
  17: "A detector that scores 99% in the lab can fail on fakes made by the newest AI tools"
  25: "Buyers want detection inside Teams, Zoom or the call center, not as one more app"
  28: "Google and TikTok now offer free checks for content made with their own AI tools"
  21: "Deepfakes are only one layer: most selfie fraud still uses simple, non-AI tricks"
  23: "False alarms cost money: flagging a real customer can block a sale or a call"
sources:
  - claim: Open-source detectors lose about half their accuracy on real 2024 deepfakes
    url: https://arxiv.org/pdf/2503.02857
    date: "2025-05-27"
    quote: "We observe an average drop in AUC of 50% for video, 48% for audio, and 45% for image models"
  - claim: Detection must sit inside existing tools
    url: https://www.realitydefender.com/insights/executing-deepfake-detection-in-real-world-settings
    date: "2026-07-01"
    quote: "Deepfake detection must live inside the contact center, the identity platform, and the communications tools teams already run"
  - claim: Google runs a free SynthID checker
    url: https://thenextweb.com/news/google-synthid-detector-public-ai-content-checker
    date: "2026-10-08"
    quote: "The free website checks whether an image, video or audio file carries Google’s SynthID watermark"
  - claim: TikTok opened a free public checker for its own AI content
    url: https://dataconomy.com/2026/11/23/tiktok-rolls-out-deepfake-likeness-detection-tool-worldwide/
    date: "2026-11-23"
    quote: "lets users determine whether an image or video was created or edited with TikTok’s AI tools"
  - claim: 76.5% of fraudulent selfies did not involve AI
    url: https://withpersona.com/guides/26h1-selfie-fraud-report
    date: "2026-06-01"
    quote: "found that 76.5% of the attempts didn't involve deepfakes, synthetic faces, or other AI-generated selfies"
  - claim: Too many false alarms make a detector impractical
    url: https://thehackernews.com/expert-insights/2025/12/purdue-universitys-real-world-deepfake.html
    date: "2025-12-22"
    quote: "A detector that triggers too many false alarms can be impractical at scale."
```

### ed133
```yaml
status: ok
title: What has held back market growth so far?
note: "We grouped the market into broad phases using research contests, fraud cases, studies and buyer surveys. The phases are our judgment but track the main technical and budget bottlenecks."
t:
  6: "2018 - 2020\n\nDeepfakes were a curiosity and detection stayed in labs. In Facebook's 2020 contest, the best model caught only 65% of unseen fakes."
  7: "2021 - 2023\n\nVoice cloning got cheap, but detectors trained on old research datasets kept breaking on each new AI generator."
  8: "2024 - 2025\n\nFraud surged, like the $25M Arup video call scam, yet a CSIRO study found none of 16 leading detectors reliable on real-world deepfakes."
  10: "2025 - 2026\n\nBudgets lag. In 2026, 74% of US security leaders suspected a deepfake attack but only 10% had dedicated tools."
  9: "TODAY\n\nDetection is moving into Teams and call centers, but false alarms, free checkers and fast-changing generators still slow buying."
sources:
  - claim: Top Facebook challenge model reached about 65% accuracy on unseen videos
    url: https://ai.meta.com/blog/deepfake-detection-challenge-results-an-open-initiative-to-advance-ai/
    date: "2020-06-12"
    quote: "the top model achieved an accuracy of 65.18 percent."
  - claim: Academic benchmarks are out of date for real deepfakes
    url: https://arxiv.org/abs/2503.02857
    date: "2025-03-04"
    quote: "While many deepfake detectors report high accuracy on academic datasets, we show that these academic benchmarks are out of date"
  - claim: Arup lost $25M after a deepfake video call
    url: https://fortune.com/europe/2024/05/17/arup-deepfake-fraud-scam-victim-hong-kong-25-million-cfo/
    date: "2024-05-17"
    quote: "A deepfake ‘CFO’ tricked the British design firm behind the Sydney Opera House in $25 million scam"
  - claim: CSIRO found none of 16 detectors reliable
    url: https://www.csiro.au/en/news/all/news/2025/march/research-reveals-major-vulnerabilities-in-deepfake-detectors
    date: "2025-03-13"
    quote: "assessed 16 leading detectors and found none could reliably identify real-world deepfakes."
  - claim: 74% saw a suspected deepfake, 10% have purpose-built defenses
    url: https://helpnetsecurity.com/2026/09/29/pindrop-enterprise-deepfake-attacks-report
    date: "2026-09-29"
    quote: "Nearly three-quarters of security leaders have encountered or suspect a deepfake attack in the past year"
  - claim: Survey covered over 250 US security leaders, 74% suspected attack
    url: https://infosecurity-magazine.com/news/deepfakes-costly-reality-for
    date: "2026-09-29"
    quote: "Pindrop’s survey of over 250 US security leaders found that 74% said they have encountered a suspected deepfake attack in the last 12 months."
  - claim: Teams opens to certified third-party detectors
    url: https://windowslatest.com/2026/10/25/microsoft-confirms-teams-will-let-third-party-tools-scan-your-meetings-for-deepfakes-from-november
    date: "2026-10-25"
    quote: "Microsoft Teams will let organizations plug in certified third-party tools that scan meeting audio and video for deepfakes"
```

### ed134
```yaml
status: ok
title: And more recently?
t:
  12: 2026 (JAN)
  13: "Ofcom opened a formal probe into X after Grok was used to make sexualized deepfakes {1|Ofcom}"
  14: 2026 (MAY)
  15: "NewsGuard found three of five popular image detectors labeled some real news photos as fake {1|NewsGuard}"
  16: 2026 (MAY)
  17: "The FTC began enforcing the TAKE IT DOWN Act, which gives platforms 48 hours to remove reported deepfake nudes {1|FTC}"
  18: 2026 (AUG)
  19: "EU AI Act rules took effect requiring deepfake labels, with a grace period to December for older AI tools {1|EU}"
  20: 2026 (SEP)
  21: "Pindrop surveyed 250+ US security leaders: 74% faced a suspected deepfake, only 10% had dedicated tools {1|Pindrop}"
  22: 2026 (OCT)
  23: "Full Fact showed Google's free SynthID Detector flagged real-looking photos as AI, and Google updated it {1|Full Fact}"
sources:
  - claim: Ofcom opened a formal investigation into X over Grok imagery on 12 January 2026
    url: https://www.ofcom.org.uk/online-safety/illegal-and-harmful-content/ofcom-launches-investigation-into-x-over-grok-sexualised-imagery?language=en
    date: "2026-01-12"
    quote: "Ofcom has decided to open a formal investigation to establish whether X has failed to comply with its legal obligations"
  - claim: NewsGuard audit of AI image detectors on real photos
    url: https://www.newsguardtech.com/?p=33448
    date: "2026-05-08"
    quote: "Leading AI Image Detection Tools Mislead Online Users, Often Declaring Authentic Content Fake"
  - claim: Three of five detectors wrongly flagged real news photos
    url: https://www.photoworkout.com/?p=222434
    date: "2026-05-15"
    quote: "A NewsGuard audit (May 2026) found three of five leading detectors wrongly flagged real news photos as AI"
  - claim: FTC began enforcing TAKE IT DOWN on 19 May 2026
    url: https://www.orrick.com/fr-FR/Insights/2026/06/Nonconsensual-Intimate-Images-Online-Take-It-Down-Act-Enforcement-In-Full-Swing
    date: "2026-06-17"
    quote: "On May 19, 2026, the FTC began enforcement of the Take It Down Act"
  - claim: 48-hour removal window including deepfakes
    url: https://www.reedsmith.com/our-insights/blogs/viewpoints/102ms5e/covered-platforms-are-you-ready-to-take-it-down/
    date: "2026-05-06"
    quote: "every covered platform must have a functioning system in place to receive and act within 48 hours on requests to remove nonconsensual intimate images"
  - claim: Article 50 applies from 2 August 2026, older systems get until 2 December 2026
    url: https://lewissilkin.com/insights/2026/07/09/council-of-the-eu-gives-ai-omnibus-final-green-light-102nbb1
    date: "2026-07-09"
    quote: "Systems placed on the market before 2 August 2026 have until 2 December 2026, but newer systems must comply from 2 August 2026."
  - claim: Pindrop readiness survey figures
    url: https://infosecurity-magazine.com/news/deepfakes-costly-reality-for
    date: "2026-09-29"
    quote: "Pindrop’s survey of over 250 US security leaders found that 74% said they have encountered a suspected deepfake attack in the last 12 months."
  - claim: Only 10% have purpose-built defenses
    url: https://helpnetsecurity.com/2026/09/29/pindrop-enterprise-deepfake-attacks-report
    date: "2026-09-29"
    quote: "while just 10% say their organizations have purpose-built defenses"
  - claim: Full Fact found SynthID Detector flagging apparently real images, Google updated it
    url: https://fullfact.org/toolkit/google-synthid-detector-flagging-apparently-real-images/
    date: "2026-10-21"
    quote: "Google updates AI detector after Full Fact investigation finds it flagging apparently real images"
```

### ed136
```yaml
status: ok
title: What slows deepfake detection adoption down?
note: "We summarized adoption constraints that recur in buyer surveys, platform admin notices, audits and vendor case studies. The burden is shifting from building detectors to fitting them into daily workflows."
t:
  6: "🎯\n\nNew AI generators keep appearing, so detectors need constant retraining"
  7: "⚠️\n\nFalse alarms on real customers or real photos erode trust"
  8: "💼\n\nBoards often act only after an executive gets fooled"
  9: "🔐\n\nScanning calls and meetings triggers privacy and data reviews"
  10: "🔌\n\nIt must plug into Teams, Zoom or call center systems to be useful"
  11: "🆓\n\nFree checkers from Google and TikTok cover their own AI content"
  12: "🧩\n\nDeepfakes are one fraud layer, so buyers want it inside ID tools"
  13: "⏳\n\nDetectors give a risk score, not a final verdict"
sources:
  - claim: Detection tools go obsolete within months
    url: https://qz.com/ai-artificial-intelligence-bank-fraud-theft-deloitte-1851488289
    date: "2024-05-30"
    quote: "even tools that might have detected this three, four months ago, tend to be obsolete right now"
  - claim: Detectors wrongly flag authentic images
    url: https://www.newsguardtech.com/?p=33448
    date: "2026-05-08"
    quote: "Leading AI Image Detection Tools Mislead Online Users, Often Declaring Authentic Content Fake"
  - claim: Boards act after a leader is fooled
    url: https://www.helpnetsecurity.com/?p=386107
    date: "2026-09-29"
    quote: "Three-quarters of respondents said deepfakes would become a boardroom priority only after a leader at their organization was personally fooled or impersonated."
  - claim: Teams admins must review provider data handling
    url: https://mc.merill.net/message/MC1509787
    date: "2026-10-22"
    quote: "Review provider terms, data handling, and compliance documentation before enabling."
  - claim: Detection must live inside existing tools
    url: https://www.realitydefender.com/insights/executing-deepfake-detection-in-real-world-settings
    date: "2026-07-01"
    quote: "Deepfake detection must live inside the contact center, the identity platform, and the communications tools teams already run"
  - claim: SynthID Detector only finds Google's watermark
    url: https://thenextweb.com/news/google-synthid-detector-public-ai-content-checker
    date: "2026-10-08"
    quote: "The detector only finds the SynthID watermark."
  - claim: TikTok checker covers TikTok AI tools
    url: https://dataconomy.com/2026/11/23/tiktok-rolls-out-deepfake-likeness-detection-tool-worldwide/
    date: "2026-11-23"
    quote: "lets users determine whether an image or video was created or edited with TikTok’s AI tools"
  - claim: Detection is expected to be embedded in identity and fraud platforms
    url: https://varindia.com/news/gartner-maps-emerging-deepfake-detection-market-names-startups-driving-enterprise-adoption
    date: "2026-07-17"
    quote: "deepfake detection capabilities are expected to be embedded into identity verification, fraud prevention and cybersecurity platforms rather than remaining standalone products."
  - claim: Detectors return probability scores
    url: https://cdn.featuredcustomers.com/CustomerCaseStudy.document/reality-defender_global-bank-ol_953891.pdf
    date: "2025-01-01"
    quote: "Our platform returned probability-based risk scores for each"
```

### ed138
```yaml
status: ok
title: How is regulation evolving?
note: "We mapped the main rule changes that affect deepfake detection in the US, UK, EU and India. Most new laws target platforms and creators, which pulls detection in indirectly rather than by direct mandate."
t:
  7: "2024\n\nFinCEN warned US banks about deepfake ID fraud and asked them to flag it in suspicious activity reports."
  8: "2025\n\nThe US signed the TAKE IT DOWN Act, and the UK made creating nonconsensual intimate deepfakes a crime."
  9: "2026\n\nNew rules took effect in India, the UK, the US and the EU, from AI labels to fast takedowns."
  10: "TODAY\n\nUS platforms must remove reported deepfake nudes within 48 hours, and EU deployers must label deepfakes."
  11: "?\n\nMost rules target platforms. A duty for banks or meeting apps to screen deepfakes would reshape demand."
sources:
  - claim: FinCEN alert on deepfake media fraud, 13 November 2024
    url: https://fincen.gov/news/news-releases/fincen-issues-alert-fraud-schemes-involving-deepfake-media-targeting-financial
    date: "2024-11-13"
    quote: "reminds financial institutions of their reporting requirements under the Bank Secrecy Act"
  - claim: TAKE IT DOWN Act signed 19 May 2025
    url: https://iapp.org/news/a/take-it-down-act-how-to-comply-as-the-ftc-begins-enforcement
    date: "2026-05-19"
    quote: "The TAKE IT DOWN Act was  signed into law 19 May 2025."
  - claim: UK creation offence under the Data (Use and Access) Act 2025, in force 6 February 2026
    url: https://www.dlapiper.com/en/insights/topics/algorithm-to-advantage/how-the-law-is-catching-up-with-ai-deepfakes
    date: "2026-04-08"
    quote: "Creating or requesting AI-generated intimate images without consent is now illegal under Section 138 of the Data (Use and Access) Act 2025"
  - claim: India's synthetic content rules in force 20 February 2026
    url: https://www.nishithdesai.com/research-and-articles/hotline/technology-law-analysis/ai-generated-content-and-combating-deepfakes-what-indias-new-rules-mean-for-global-platforms-15532
    date: "2026-02-12"
    quote: "notified the Information Technology (Intermediary Guidelines and Digital Media Ethics Code) Amendment Rules, 2026"
  - claim: US platforms have 48 hours to act on removal requests including deepfakes
    url: https://www.reedsmith.com/our-insights/blogs/viewpoints/102ms5e/covered-platforms-are-you-ready-to-take-it-down/
    date: "2026-05-06"
    quote: "act within 48 hours on requests to remove nonconsensual intimate images (NCII), including AI-generated digital forgeries"
  - claim: EU Article 50 applies from 2 August 2026, including deepfake labelling
    url: https://cdp.cooley.com/digital-ai-omnibus-delays-key-deadlines-introduces-new-rules/
    date: "2026-07-27"
    quote: "Article 50 transparency obligations (including chatbot disclosure and deepfake labelling obligations for systems launched from 2 August 2026)"
```

### iv_fda
```yaml
status: ok
title: What does it take to win a big security buyer?
note: "We built these steps from vendor case studies, government contract records and platform admin notices. Durations and costs vary widely with the buyer's size and channel."
t:
  7: "INDEPENDENT TESTS\n\nBuyers compare tools on outside tests, like Purdue's 2025 study of 24 detectors on real fakes."
  8: "SECURITY REVIEW\n\nThe buyer's security team checks audits such as SOC 2 and how call or meeting data is handled."
  9: "LIVE PILOT\n\nA bank first reviews recorded calls, then goes live. One top bank scanned 1.7 million calls this way."
  11: "INTEGRATION\n\nThe tool must plug into existing systems. Since November 2026, Teams lets admins add certified ones."
  10: "MULTIYEAR DEAL\n\nContracts run for years: the Pentagon gave Hive a two-year, $2.4M deepfake detection deal."
sources:
  - claim: Purdue evaluated detectors on real political deepfakes
    url: https://www.pymnts.com/newswire-announcements/incode-launches-deepsight-an-effective-deepfake-defense/
    date: "2025-12-02"
    quote: "which evaluated 24 detection systems across commercial, government, and academic providers."
  - claim: Vendors present SOC 2 Type 2 for security reviews
    url: https://realitydefender.com/faq
    date: "2026-01-01"
    quote: "The platform has a range of US, UK, and EU certifications including SOC2 Type 2 and GDPR."
  - claim: Teams admins must review provider data handling
    url: https://mc.merill.net/message/MC1509787
    date: "2026-10-22"
    quote: "Review provider terms, data handling, and compliance documentation before enabling."
  - claim: Tier-one bank pilot then live deployment on 1.7 million calls
    url: https://realitydefender.com/insights/real-time-deepfake-detection-in-call-centers
    date: "2026-01-01"
    quote: "The deployment analyzed more than 1.7 million customer calls and identified about 960 synthetic voice calls"
  - claim: The bank started with recorded calls
    url: https://realitydefender.com/insights/real-time-deepfake-detection-in-call-centers
    date: "2026-01-01"
    quote: "The bank started with a review of recorded calls to set a baseline."
  - claim: Teams support for certified third-party detectors from mid-November 2026
    url: https://windowslatest.com/2026/10/25/microsoft-confirms-teams-will-let-third-party-tools-scan-your-meetings-for-deepfakes-from-november
    date: "2026-10-25"
    quote: "with the rollout starting in mid-November 2026 on Teams for desktop, Mac and web"
  - claim: Hive won a two-year $2.4M DoD deepfake detection contract
    url: https://www.biometricupdate.com/202412/dod-awards-contract-for-deepfake-detection-to-hive
    date: "2024-12-06"
    quote: "The two-year deal will reinforce the country’s national security"
  - claim: Contract amount $2.4M
    url: https://meritalk.com/articles/pentagon-to-prototype-deepfake-detection-tech/
    date: "2024-12-05"
    quote: "The Department of Defense (DoD) is investing $2.4 million over two years to prototype a deepfake detection capability"
```

### ed140
```yaml
status: ok
title: Where do vendors, buyers and regulators clash?
t:
  7: "US regulators want reported deepfake nudes removed within 48 hours"
  0: "Vendors want detection sold as a paid layer, not as a free feature"
  19: "Banks want fewer false alarms on real customers"
  18: "Investors want fast growth from a few big platform deals"
  10: "Privacy teams limit how calls and meetings are scanned"
  9: "Fraud teams want every call and meeting checked in real time"
  22: "EU rules ask AI makers to mark content, not users to detect it"
  21: "Platforms push their own free checks for their own AI content"
  13: "Researchers keep showing detectors fail on new fakes"
  12: "Vendors market accuracy scores of 98% or more to buyers"
  25: "Courts and newsrooms need explainable, court-ready proof"
  24: "Busy agents want one simple yes or no answer per call"
sources:
  - claim: 48-hour removal duty
    url: https://www.reedsmith.com/our-insights/blogs/viewpoints/102ms5e/covered-platforms-are-you-ready-to-take-it-down/
    date: "2026-05-06"
    quote: "act within 48 hours on requests to remove nonconsensual intimate images (NCII), including AI-generated digital forgeries"
  - claim: Teams admins must review provider data handling before scanning meetings
    url: https://mc.merill.net/message/MC1509787
    date: "2026-10-22"
    quote: "Review provider terms, data handling, and compliance documentation before enabling."
  - claim: EU Article 50(2) requires providers to mark AI outputs
    url: https://chambers.com/articles/eu-ai-act-the-latest-compliance-checkpoint
    date: "2026-08-03"
    quote: "providers of AI systems that generate or manipulate images, videos, audio or text, must ensure that such outputs are marked in a machine-readable format"
  - claim: Google's free SynthID Detector checks Google's own watermark
    url: https://thenextweb.com/news/google-synthid-detector-public-ai-content-checker
    date: "2026-10-08"
    quote: "The detector only finds the SynthID watermark."
  - claim: None of 16 detectors reliable on real-world deepfakes
    url: https://www.csiro.au/en/news/all/news/2025/march/research-reveals-major-vulnerabilities-in-deepfake-detectors
    date: "2025-03-13"
    quote: "assessed 16 leading detectors and found none could reliably identify real-world deepfakes."
  - claim: Vendors market 98% and 98.9% accuracy
    url: https://www.accessnewswire.com/newsroom/en/computers-technology-and-internet/resemble-ai-raises-13m-from-sony-innovation-fund-okta-ventures-an-1115357
    date: "2025-12-08"
    quote: "DETECT-3B Omni, an industry-leading, enterprise-grade deepfake detection model with 98% detection accuracy across more than 38 languages."
  - claim: Forensic tools sell court-ready output
    url: https://shuftipro.com/blog/best-deepfake-detection-tools/
    date: "2026-08-15"
    quote: "Multilayer forensic analysis with explainable, court-ready output"
  - claim: Too many false alarms make a detector impractical
    url: https://thehackernews.com/expert-insights/2025/12/purdue-universitys-real-world-deepfake.html
    date: "2025-12-22"
    quote: "A detector that triggers too many false alarms can be impractical at scale."
```

### iv_safety
```yaml
status: ok
title: What could go wrong for deepfake detection?
note: "We used peer-reviewed studies, media audits and official rule texts. Each risk has a documented case, but how often each one hurts buyers is not yet measured."
t:
  6: "NEW GENERATORS\n\nOpen-source detectors lost about half their accuracy on real 2024 deepfakes compared with older academic test sets"
  7: "FALSE ALARMS\n\nIn a May 2026 NewsGuard audit, ZeroGPT labeled 20% of real news photos as fake, which can discredit genuine evidence"
  8: "DETECTOR BYPASS\n\nResearchers fooled two commercial detectors more than 95% of the time by subtly changing features such as an open mouth"
  9: "FREE CHECKERS\n\nGoogle made its SynthID Detector free for everyone in October 2026, and OpenAI and TikTok run their own free AI checkers"
  10: "SHIFTING LAWS\n\nIndia's deepfake rules gave platforms just 10 days in February 2026 to add labels and detection tools"
sources:
  - claim: Average AUC drop of about 50% for open-source detectors
    url: https://arxiv.org/pdf/2503.02857
    date: "2025-05-27"
    quote: "We observe an average drop in AUC of 50% for video, 48% for audio, and 45% for image models"
  - claim: ZeroGPT flagged 20% of real images
    url: https://www.newsguardtech.com/?p=33448
    date: "2026-05-08"
    quote: "ZeroGPT classified three of the 15 real images (20 percent) as fake"
  - claim: AVA attack beat two commercial detectors over 95% of the time
    url: https://ar5iv.labs.arxiv.org/html/2312.08675
    date: "2023-12-14"
    quote: "achieves more than a 95% success rate on two commercial DeepFake detectors."
  - claim: Attack changes inconspicuous attributes such as mouth opening
    url: https://deepfake-demo.aisec.fraunhofer.de/related_work/2312.08675
    date: "2023-12-14"
    quote: "manipulates inconspicuous image attributes (e.g., mouth open) to bypass state-of-the-art deepfake detection algorithms"
  - claim: SynthID Detector freely available to everyone
    url: https://petapixel.com/2026/10/08/googles-synthid-ai-detector-is-now-freely-available-to-everyone/
    date: "2026-10-08"
    quote: "Google’s SynthID AI Detector is Now Freely Available to Everyone"
  - claim: OpenAI runs its own verification page
    url: https://thenextweb.com/news/google-synthid-detector-public-ai-content-checker
    date: "2026-10-08"
    quote: "It also runs its own verification page, which checks images and audio for SynthID and C2PA signals."
  - claim: TikTok public checker without account
    url: https://dataconomy.com/2026/11/23/tiktok-rolls-out-deepfake-likeness-detection-tool-worldwide/
    date: "2026-11-23"
    quote: "The checker does not require a TikTok account."
  - claim: India gave intermediaries 10 days
    url: https://www.mondaq.com/india/social-media/1745278/indias-new-deepfake-regulation-meity-notifies-amendments-to-information-technology-rules-2021
    date: "2026-02-16"
    quote: "giving intermediaries barely 10 (ten) days to overhaul their content moderation systems, deploy automated detection tools"
```

### ed141
```yaml
status: ok
title: Which constraints are structural?
t:
  5: "Every new AI generator can break\ndetectors trained on older fakes"
  10: "Detection gives a probability,\nnot proof a court will always accept"
  15: "Attackers can test their fakes against\ndetectors before they strike"
  20: "Most fraud mixes deepfakes with\nsimple tricks and stolen data"
  25: "Real customers and real photos\ncan be flagged by mistake"
sources:
  - claim: Detectors lose accuracy on new real-world deepfakes
    url: https://arxiv.org/pdf/2503.02857
    date: "2025-05-27"
    quote: "All off-the-shelf open-source models perform poorly on Deepfake-Eval-2024."
  - claim: Detectors return probability-based scores
    url: https://cdn.featuredcustomers.com/CustomerCaseStudy.document/reality-defender_global-bank-ol_953891.pdf
    date: "2025-01-01"
    quote: "Our platform returned probability-based risk scores for each"
  - claim: Fraud rings test systems with different manipulations
    url: https://withpersona.com/blog/detect-more-ai-based-face-spoofs-persona
    date: "2025-01-21"
    quote: "we caught a fraud ring testing our systems with different types of image manipulations across subsequent submissions"
  - claim: Most selfie fraud is simple presentation attacks
    url: https://marketing.withpersona.com/guides/26h1-selfie-fraud-report
    date: "2026-06-01"
    quote: "We also found that the vast majority of attempts (86.2%) were relatively simple presentation attacks."
  - claim: Real images flagged as fake
    url: https://www.newsguardtech.com/?p=33448
    date: "2026-05-08"
    quote: "ZeroGPT classified three of the 15 real images (20 percent) as fake"
```

### ed143
```yaml
status: ok
title: How likely is each deepfake detection risk?
note: "Each probability is our judgment of the chance that the event happens within five years. We anchor it on published studies, audits, deals and platform moves."
t:
  38: ≈7%
  34: "Forensic tools now sell explainable, court-ready reports"
  37: COURT REJECTION
  27: ≈8%
  26: PRIVACY LIMITS
  24: "Teams admins must review vendor data handling before scans"
  23: ≈10%
  22: FUNDING SQUEEZE
  20: "Many rounds are small, from a €1.7M pre-seed to a $28M launch"
  19: ≈12%
  18: PLATFORM BUILDS ITS OWN
  16: "Microsoft now lets outside vendors scan Teams calls"
  15: ≈15%
  12: "Full Fact found Google's detector flagging real photos"
  14: FALSE ALARM SCANDAL
  11: ≈18%
  10: FREE CHECKERS WIN
  8: "Google, OpenAI and TikTok now offer free checks for their own AI"
  7: ≈20%
  6: MAJOR DETECTOR BYPASS
  4: "Studies show detectors still miss many real-world deepfakes"
  3: ≈35%
  2: BIG VENDOR BUYOUTS
  0: "Deel bought Clarity and LexisNexis bought IDVerse in two years"
sources:
  - claim: Court-ready forensic output
    url: https://shuftipro.com/blog/best-deepfake-detection-tools/
    date: "2026-08-15"
    quote: "Multilayer forensic analysis with explainable, court-ready output"
  - claim: Admins must review data handling
    url: https://mc.merill.net/message/MC1509787
    date: "2026-10-22"
    quote: "Review provider terms, data handling, and compliance documentation before enabling."
  - claim: Neuramancer €1.7M pre-seed
    url: https://tech.eu/2026/03/12/neuramancer-lands-eur17m-pre-seed-to-scale-deepfake-detection-tools/
    date: "2026-03-12"
    quote: "Neuramancer lands €1.7M pre-seed to scale deepfake detection tools"
  - claim: imper.ai launched with $28M
    url: https://siliconangle.com/2025/12/04/imper-ai-launches-28m-stop-ai-powered-impersonation-attacks/
    date: "2025-12-04"
    quote: "Cyber impersonation prevention startup Imper.ai Inc. launched today with $28 million in new funding"
  - claim: Microsoft relies on third-party detectors in Teams
    url: https://windowsreport.com/microsoft-teams-will-soon-flag-deepfake-audio-and-video-in-meetings/
    date: "2026-10-09"
    quote: "Microsoft is not developing the underlying deepfake detection technology itself."
  - claim: Full Fact found SynthID Detector flagging real images
    url: https://fullfact.org/toolkit/google-synthid-detector-flagging-apparently-real-images/
    date: "2026-10-21"
    quote: "Google updates AI detector after Full Fact investigation finds it flagging apparently real images"
  - claim: Free checkers from Google, OpenAI, TikTok
    url: https://petapixel.com/2026/10/08/googles-synthid-ai-detector-is-now-freely-available-to-everyone/
    date: "2026-10-08"
    quote: "OpenAI operates its own detector, but it checks for OpenAI watermarks rather than identifying all forms of AI-generated content."
  - claim: Detectors fail on real-world deepfakes
    url: https://www.csiro.au/en/news/all/news/2025/march/research-reveals-major-vulnerabilities-in-deepfake-detectors
    date: "2025-03-13"
    quote: "assessed 16 leading detectors and found none could reliably identify real-world deepfakes."
  - claim: Deel acquired Clarity
    url: https://idtechwire.com/deel-acquires-clarity-to-add-deepfake-detection-across-hiring-and-workforce-identity/
    date: "2026-08-03"
    quote: "Global payroll and HR platform Deel has acquired Israeli deepfake-security startup Clarity"
  - claim: LexisNexis Risk Solutions closed IDVerse acquisition
    url: https://risk.lexisnexis.com/global/en/about-us/press-room/press-release/20250219-idverse-acquisition
    date: "2025-02-19"
    quote: "LexisNexis® Risk Solutions, part of RELX, closed its acquisition of IDVerse™"
```

### ed144
```yaml
status: ok
title: How severe is the impact of each one?
comment: "Severity levels are our judgment of how much each event would slow market growth (no note, as on the template)."
t:
  38: MEDIUM
  37: FUNDING SQUEEZE
  34: "Smaller rounds would slow young vendors, but leaders have strategic backers"
  27: MEDIUM
  24: "A court rejection would hurt forensic use, but fraud checks go on"
  26: COURT REJECTION
  23: MEDIUM
  22: BIG VENDOR BUYOUTS
  20: "Buyouts would cut vendor choice, but put detection into big platforms"
  19: MEDIUM
  18: PRIVACY LIMITS
  16: "Tighter privacy rules would slow call and meeting scans, but are workable"
  15: MEDIUM
  14: FREE CHECKERS WIN
  12: "Free checkers only read their own watermarks, so paid detection stays needed"
  11: HIGH
  8: "A Microsoft-built detector could shut outside vendors out of a key channel"
  10: PLATFORM BUILDS ITS OWN
  7: HIGH
  4: "A public false alarm scandal could make banks pause automated blocking"
  6: FALSE ALARM SCANDAL
  3: HIGH
  2: MAJOR DETECTOR BYPASS
  0: "A widely used bypass would hit trust in every vendor, not just one product"
sources:
  - claim: KPMG and Deel moves show strategic backers
    url: https://www.internationalaccountingbulletin.com/news/kpmg-llp-acquires-stake-in-deepfake-detection-business-reality-defender/
    date: "2026-09-11"
    quote: "US-based audit, tax and advisory company KPMG LLP has acquired a minority stake in Reality Defender"
  - claim: Free checkers read only their own watermark
    url: https://thenextweb.com/news/google-synthid-detector-public-ai-content-checker
    date: "2026-10-08"
    quote: "The detector only finds the SynthID watermark."
  - claim: Microsoft relies on third parties today
    url: https://windowsreport.com/microsoft-teams-will-soon-flag-deepfake-audio-and-video-in-meetings/
    date: "2026-10-09"
    quote: "Microsoft is not developing the underlying deepfake detection technology itself."
  - claim: Detectors fail under real-world conditions
    url: https://deepfake-demo.aisec.fraunhofer.de/related_work/2510.16556
    date: "2025-10-18"
    quote: "most models struggle significantly to generalize effectively to these authentic political deepfakes, and often fail under real-world conditions."
```

### ed145
```yaml
status: ok
title: Which constraints have largely disappeared today?
note: "We kept constraints that have clearly eased thanks to platform, legal or market changes. This is our judgment, not a claim that the issues are fully gone."
t:
  32: CONSTRAINT
  31: WHY IT HAS DISAPPEARED
  5: "Meeting apps had no way to plug in\noutside deepfake detectors"
  7: "Teams now lets admins add certified\ndetectors to live meetings"
  8: "No analyst framework helped buyers\ncompare deepfake vendors"
  10: "Gartner mapped deepfake startups\nfor the first time in 2026"
  11: "Detection ran in the cloud, so the\ndata had to leave the device"
  13: "Samsung and Reality Defender are\nbuilding on-device detection"
  14: "US law had no takedown duty\nfor deepfake nudes"
  16: "The TAKE IT DOWN Act now forces\nremovals in 48 hours"
  17: "Detection lacked big-name buyers\nand strategic owners"
  19: "Deel bought Clarity and KPMG\nbacked Reality Defender"
  20: "Detectors mostly checked files after\nthe fact, not live calls"
  22: "Pindrop and Reality Defender now\nscreen live calls in real time"
sources:
  - claim: Teams supports certified third-party detection
    url: https://mc.merill.net/message/MC1509787
    date: "2026-10-22"
    quote: "Microsoft Teams will support integration with certified third-party synthetic audio and video detection solutions to enhance meeting security."
  - claim: Gartner's first Emerging Market Quadrant for deepfake detection, 25 June 2026
    url: https://www.gartner.com/en/documents/8056333
    date: "2026-06-25"
    quote: "Emerging Market Quadrant for Deepfake Detection"
  - claim: Samsung and Reality Defender on-device detection
    url: https://news.samsung.com/sg/samsung-electronics-singapore-partners-with-reality-defender-to-advance-on-device-deepfake-detection-for-enterprises-in-singapore
    date: "2026-10-14"
    quote: "Samsung Electronics Singapore Partners with Reality Defender to Advance On-Device Deepfake Detection for Enterprises in Singapore"
  - claim: TAKE IT DOWN 48-hour removal
    url: https://www.reedsmith.com/our-insights/blogs/viewpoints/102ms5e/covered-platforms-are-you-ready-to-take-it-down/
    date: "2026-05-06"
    quote: "act within 48 hours on requests to remove nonconsensual intimate images (NCII), including AI-generated digital forgeries"
  - claim: Deel acquired Clarity
    url: https://idtechwire.com/deel-acquires-clarity-to-add-deepfake-detection-across-hiring-and-workforce-identity/
    date: "2026-08-03"
    quote: "Global payroll and HR platform Deel has acquired Israeli deepfake-security startup Clarity"
  - claim: KPMG minority stake in Reality Defender
    url: https://www.internationalaccountingbulletin.com/news/kpmg-llp-acquires-stake-in-deepfake-detection-business-reality-defender/
    date: "2026-09-11"
    quote: "US-based audit, tax and advisory company KPMG LLP has acquired a minority stake in Reality Defender"
  - claim: Pindrop real-time deepfake detection in contact centers
    url: https://www.nasdaq.com/press-release/pindrop-zoom-integration-embeds-real-time-deepfake-detection-and-identity
    date: "2026-03-12"
    quote: "announced an expanded integration with Zoom to bring real-time deepfake detection for Zoom Contact Center."
  - claim: Reality Defender real-time detection on live calls
    url: https://realitydefender.com/insights/real-time-deepfake-detection-in-call-centers
    date: "2026-01-01"
    quote: "Detection works on the audio itself, so it needs the call while it’s live."
```
