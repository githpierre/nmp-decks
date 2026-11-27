# Deepfake detection: Tech and infra (deck 05)

### ed087
```yaml
status: ok
section: Tech and infra
title: What are the tech and infra layers?
page: 1/2
t:
  7: SIGNALS
  10: Detectors read pixels, sound waves and file data for traces AI tools leave behind
  9: MODELS
  11: AI classifiers trained on real and fake samples score how likely media is fake
  21: LAYERS
  12: LIVENESS
  14: Checks prove a live person is on camera, not a replay or injected video
  13: ORIGIN
  15: Signed content credentials show where a file came from and if it changed
sources:
  - claim: Intel FakeCatcher reads subtle blood-flow signals in video pixels
    url: https://www.intel.com/content/www/us/en/newsroom/news/intel-introduces-real-time-deepfake-detector.html
    date: '2022-11-14'
    quote: "Intel’s deepfake detector analyzes ‘blood flow’ in video pixels to return results in milliseconds with 96% accuracy."
  - claim: Liveness and injection defense checks that a real human is in front of the camera
    url: https://incode.com/blog/incode-launches-deepsight
    date: '2025-12-02'
    quote: "Deepsight’s multi-modal AI analyzes video, motion, and depth data to expose inconsistencies that synthetic media cannot reproduce"
  - claim: C2PA Content Credentials are a signed manifest that records where content came from
    url: https://thehackernews.com/2025/09/google-pixel-10-adds-c2pa-support-to.html?m=1
    date: '2025-09-10'
    quote: "C2PA's Content Credentials are a tamper-evident, cryptographically signed digital manifest providing verifiable provenance for digital content"
```

### ed088
```yaml
status: ok
section: Tech and infra
title: What are the tech and infra layers?
page: 2/2
t:
  7: DATA
  10: Fresh sets of real and fake samples must cover each new AI generator as it appears
  9: PLUG-INS
  11: Connectors put checks inside Zoom, Teams, call centers and ID verification apps
  21: LAYERS
  12: SPEED
  14: Live checks must flag a fake voice or face in seconds, during the call
  13: FORENSICS
  15: Reports show why media was flagged, so analysts and courts can rely on it
sources:
  - claim: Detection tools are often trained on data that lacks real-world synthetic media
    url: https://gov.uk/government/publications/deepfake-detection-technology/deepfake-detection-technology
    date: '2026-03-26'
    quote: "Most detection tools are trained on datasets that often lack real-world synthetic media"
  - claim: Detection runs inside Zoom, Webex and Microsoft Teams
    url: https://www.businesswire.com/news/home/20251119488893/en
    date: '2025-11-19'
    quote: "The solution is now available on Zoom, Webex and Microsoft Teams."
  - claim: Real-time communications require managing latency and call quality
    url: https://gov.uk/government/publications/deepfake-detection-technology/deepfake-detection-technology
    date: '2026-03-26'
    quote: "Managing latency and maintaining the quality of video and audio calls"
  - claim: Detection reports can be exported for regulators and counsel
    url: https://resemble.ai/products/meetings
    date: '2026'
    quote: "Every detection produces a forensic report exportable for regulators and counsel."
```

### ed089
```yaml
status: ok
section: Tech and infra
title: Does every layer carry the same weight?
note: We ranked these layers directionally from recent benchmark studies, a UK government review and vendor disclosures, not from a standardized industry score.
t:
  38: RANKING
  6: TRAINING DATA
  14: Decides whether detectors catch new generators or fail on fakes they never saw
  7: MODELS
  24: Turn signals into a score, yet open models lost about half their skill on 2024 fakes
  8: LIVENESS
  26: Blocks replayed and injected video in ID checks, the top use case in every report
  9: REAL TIME
  28: Lets a bank or meeting tool stop a fake mid-call, before the money moves
  10: PLUG-INS
  30: Puts detection where people already work, but cannot fix a weak model
  11: CONTENT ORIGIN
  32: Proves where honest media came from, but fakes simply carry no label
  12: FORENSICS
  34: Explains each verdict for analysts and courts once detection itself works
  13: BENCHMARK
  36: Shows buyers what really works, but test sets lag the newest generators
sources:
  - claim: Open-source detectors lost about half their AUC on real 2024 deepfakes
    url: https://arxiv.org/html/2503.02857v2
    date: '2025-03-04'
    quote: "with AUC decreasing by 50% for video, 48% for audio, and 45% for image models compared to previous benchmarks"
  - claim: Real-world accuracy typically drops after deployment
    url: https://gov.uk/government/publications/deepfake-detection-technology/deepfake-detection-technology
    date: '2026-03-26'
    quote: "accuracy rates typically drop by 10-20% in real-world redeployment with representative datasets"
  - claim: Identity verification and KYC is the leading application
    url: https://www.astuteanalytica.com/industry-report/deepfake-detection-market
    date: '2026-07-15'
    quote: "identity verification & KYC emerged as the leading segment."
  - claim: Inconsistent test sets and metrics lower confidence in detection tools
    url: https://gov.uk/government/publications/deepfake-detection-technology/deepfake-detection-technology
    date: '2026-03-26'
    quote: "Inconsistencies in testing datasets and evaluation metrics result in low confidence in the efficacy of detection tools"
```

### ed090
```yaml
status: ok
section: Tech and infra
title: Where does 80% of deepfake detection value sit?
note: We treated model freshness and live delivery as the main value pools because software and APIs hold the largest share of spending and buyers pay to stop fakes during calls.
t:
  9: '💰 💰 💰 💰 💰 💰 💰 💰 💰

    💰 💰 💰 💰 💰 💰 💰 💰 💰

    💰 💰 💰 💰 💰 💰 💰 💰 💰

    💰 💰 💰 💰 💰 💰 💰 💰 💰

    💰 💰 💰 💰 💰 💰 💰 💰 💰

    💰 💰 💰 💰 💰 💰 💰 💰 💰

    💰 💰 💰 💰 💰 💰 💰 💰 💰

    💰 💰 💰 💰 💰 💰 💰 💰 💰


    💰 💰 💰 💰 💰 💰 💰 💰 💰

    💰 💰 💰 💰 💰 💰 💰 💰 💰'
  8: "Most value today sits in detection models and the training data behind them, because a detector is only as good as the newest fakes it has seen.\n\n\nReal-time delivery comes next, since banks, HR teams and meeting platforms pay to stop a fake during the call, not after the money has moved.\n\n\nWinners will pair fast-updating models with deep plug-ins into calls, meetings and ID checks, and explain every verdict."
sources:
  - claim: Software and APIs hold the largest share of the market
    url: https://www.astuteanalytica.com/industry-report/deepfake-detection-market
    date: '2026-07-15'
    quote: "software/APIs segment accounted for the largest share of the market."
  - claim: Detectors must keep up with new generators, and lagging datasets hold them back
    url: https://gov.uk/government/publications/deepfake-detection-technology/deepfake-detection-technology
    date: '2026-03-26'
    quote: "it prevents deepfake detection tools from training on data generated with the latest creation technologies"
  - claim: HR platforms pay for live deepfake defense in hiring
    url: https://www.biometricupdate.com/202608/deel-acquires-clarity-to-strengthen-identity-verification-in-hiring-pipeline
    date: '2026-08'
    quote: "Deel will integrate Clarity’s identity verification directly into Deel IT"
```

### ed091
```yaml
status: ok
section: Tech and infra
title: How has tech and infra evolved over the years?
note: We used product launches rather than research papers because they show when detection became something buyers could use.
t:
  6: "2017 - 2019\n\n\nDeepfakes appeared online in late 2017, and Facebook and Microsoft funded a $10M challenge in 2019 to build a shared detection benchmark"
  7: "2020 - 2022\n\n\nMicrosoft shipped Video Authenticator, C2PA wrote a content origin standard and Intel launched real-time FakeCatcher"
  8: "2023 - 2025\n\n\nVoice clones hit call centers, so Pindrop launched Pulse, and detection moved into Zoom, Teams and ID onboarding"
  9: "TODAY\n\n\nMultimodal platforms check voice, face and video together, and Microsoft Teams now lets certified detectors flag fakes in meetings"
  10: "?\n\n\nNext tools may check physics instead of known fakes, sign media at capture and verify AI agents as well as humans"
sources:
  - claim: Deepfakes emerged in late 2017
    url: https://axbom.com/content/files/2023/06/deepfake_report.pdf
    date: '2019-09'
    quote: "Since emerging in late 2017 the phenomenon of deepfakes has developed rapidly"
  - claim: Facebook funded a $10M Deepfake Detection Challenge with Microsoft in 2019
    url: https://siliconangle.com/?p=489696
    date: '2019-09-05'
    quote: "Facebook Inc. today announced that it’s teaming up with Microsoft Corp. and a number of universities to launch the Deep Fake Detection Challenge"
  - claim: Microsoft launched Video Authenticator in September 2020
    url: https://businessinsider.in/tech/news/microsoft-has-launched-new-deepfake-detecting-tech-ahead-of-the-2020-election/amp_articleshow/77891511.cms
    date: '2020-09-02'
    quote: "Microsoft on Tuesday announced the launch of Microsoft Video Authenticator, a tool designed to spot when videos have been manipulated"
  - claim: C2PA released the first industry standard for content provenance
    url: https://c2pa.org/?p=65
    date: '2022-01-26'
    quote: "The C2PA was launched in February 2021 with founding members Adobe, Arm, BBC, Intel, Microsoft and Truepic"
  - claim: Pindrop launched Pulse for real-time audio deepfake detection in February 2024
    url: https://www.pindrop.com/?p=43737
    date: '2024-02-20'
    quote: "Pulse introduces cutting-edge audio liveness detection capabilities for real-time identification, monitoring, and analysis of audio deepfakes."
  - claim: Microsoft Teams lets certified third-party providers surface deepfake signals in meetings
    url: https://bleepingcomputer.com/news/security/microsoft-teams-to-add-third-party-deepfake-detection-impersonation-protection
    date: '2026-10-08'
    quote: "Organizations can enhance meeting security with synthetic audio and video detection solutions provided by certified third-party providers"
  - claim: New models check physical reality to catch content from unseen generators
    url: https://www.resemble.ai/deepfake-detection-for-google-meet/
    date: '2026'
    quote: "reviewing both known generation patterns and physical reality, including lighting, motion, and continuity"
```

### ed092
```yaml
status: ok
section: Tech and infra
title: What were the latest tech and infra developments?
page: 1/2
note: We prioritized launches with direct product consequences, using company releases and trade press where available.
t:
  13: '2024'
  14: Pindrop launched Pulse to spot AI voices in real time in call centers, with First National Bank of Omaha among early users
  15: '2024'
  16: Pindrop added Pulse Inspect, letting newsrooms and nonprofits upload audio files to check them for synthetic speech
  17: '2025'
  18: Pindrop put Pulse for Meetings in beta on Zoom, Teams and Webex, checking participants' audio and video in real time
  19: '2025'
  20: Google's Pixel 10 became the first phone to attach C2PA Content Credentials to every photo taken with its camera app
  21: '2025'
  22: Incode launched Deepsight, which blocks deepfakes and injected virtual cameras in under 100 milliseconds during ID checks
  23: '2025'
  24: Resemble AI released DETECT-3B Omni, a model that checks voice, image and video for fakes in more than 38 languages
sources:
  - claim: Pindrop launched Pulse in February 2024, and First National Bank of Omaha used it since beta
    url: https://voicebot.ai/2024/02/21/pindrop-launches-real-time-audio-deepfake-detection-tool-pindrop-pulse/
    date: '2024-02-21'
    quote: "Some Pindrop clients have already been using Pulse since its beta, such as First National Bank of Omaha"
  - claim: Pindrop launched Pulse Inspect for uploaded audio files in August 2024
    url: https://pindrop.com/?p=39341
    date: '2024-08-15'
    quote: "users can upload audio files into the Pindrop platform to quickly and accurately determine if the files contain synthetic speech"
  - claim: Pindrop announced Pulse for Meetings in beta in April 2025
    url: https://www.pindrop.com/article/announcement-pulse-for-meetings/
    date: '2025-04-28'
    quote: "analyzing audio and video content in real time to detect AI-generated manipulation"
  - claim: Pixel 10 is the first lineup with Content Credentials built into every photo from Pixel Camera
    url: https://blog.google/security/pixel-android-trusted-images-c2pa-content-credentials/
    date: '2025-09-10'
    quote: "The Pixel 10 lineup is the first to have Content Credentials built in across every photo created by Pixel Camera."
  - claim: Incode launched Deepsight in December 2025, working in under 100 milliseconds
    url: https://idtechwire.com/incode-launches-deepsight-deepfake-defense-validated-by-purdue-study/
    date: '2025-12-02'
    quote: "a real-time AI system designed to detect and block deepfakes, injected virtual cameras, and synthetic identity attacks in under 100 milliseconds"
  - claim: Resemble AI released DETECT-3B Omni with 98% accuracy across more than 38 languages
    url: https://www.artificialintelligence-news.com/news/google-sony-and-okta-back-resemble-ai-push-into-deepfake-detection/
    date: '2025-12-08'
    quote: "DETECT-3B Omni, a deepfake detection model designed for enterprise environments. The company reports 98% detection accuracy in more than 38 languages."
```

### ed093
```yaml
status: ok
section: Tech and infra
title: What were the latest tech and infra developments?
page: 2/2
note: We used company releases and trade press to capture the most consequential 2026 product and platform milestones.
t:
  13: '2026'
  14: OmniSpeech put AI Detect on the Zoom App Marketplace, flagging AI-generated voices in live meetings with color codes
  15: '2026'
  16: ID-Pal added injection attack detection, catching fake or prerecorded video fed straight into a selfie check
  17: '2026'
  18: GetReal made continuous identity checks generally available, pairing deepfake detection with proof of who is speaking
  19: '2026'
  20: Resemble AI unveiled DETECT-World, which checks lighting, motion and physics so it can catch fakes from unseen generators
  21: '2026'
  22: Cyberette launched a forensics platform that shows where an image, video or voice file was manipulated, not just a verdict
  23: '2026'
  24: Microsoft Teams opened meetings to certified third-party deepfake detectors, with Resemble AI live from November 3
sources:
  - claim: OmniSpeech AI Detect launched on the Zoom App Marketplace with color-coded voice indicators
    url: https://www.securityinfowatch.com/ai/news/55341632/omnispeech-omnispeech-brings-real-time-deepfake-audio-detection-to-zoom-marketplace
    date: '2026-01-06'
    quote: "Real-time analysis of audio streams during Zoom meetings with color-coded indicators for AI-generated, synthetic, or human voices."
  - claim: ID-Pal enhanced injection attack detection against camera feed manipulation
    url: https://www.id-pal.com/injection-attack-detection-launch/
    date: '2026-03-24'
    quote: "designed to catch and prevent camera feed manipulation and deepfake injection during remote onboarding"
  - claim: GetReal announced general availability of continuous identity verification
    url: https://www.tmcnet.com/usubmit/2026/05/18/10384211.htm
    date: '2026-05-18'
    quote: "today announced the general availability of continuous identity verification"
  - claim: Resemble AI introduced DETECT-World on August 12, 2026
    url: https://www.resemble.ai/resources?3244b5b1_page=22
    date: '2026-08-12'
    quote: "catching unseen generators by checking physics, not memorizing signatures."
  - claim: Cyberette launched a deepfake forensics platform on September 30, 2026
    url: https://www.biometricupdate.com/202610/cyberette-launches-deepfake-forensics-platform-to-show-where-media-was-manipulated
    date: '2026-10'
    quote: "for fraud, identity and investigative teams that need more than a verdict on whether an image, video or voice recording is fake"
  - claim: Resemble AI's native Microsoft Teams integration went live on November 3
    url: https://www.resemble.ai/resources/microsoft-teams-certified-deepfake-detection-partner
    date: '2026-11'
    quote: "following the launch of our native Microsoft Teams integration on November 3, which is already live in production environments"
```

### ed094
```yaml
status: ok
section: Tech and infra
title: What are the solvable bottlenecks?
note: We selected bottlenecks named in a 2026 UK government review, recent benchmark studies and vendor threat reports as fixable but not yet broadly solved.
t:
  39: BOTTLENECK
  38: EXPLANATION
  41: BOTTLENECK
  40: EXPLANATION
  7: "NEW\n\nMODELS"
  5: Detectors trained on older fakes often miss media made with the newest AI generators
  24: "LAB\n\nGAP"
  22: Open detectors lost about half their skill on real 2024 fakes versus lab tests
  11: "INJECTED\n\nVIDEO"
  9: Fraudsters feed fake video straight into apps, skipping the camera liveness checks watch
  28: "FALSE\n\nALARMS"
  26: Flagging real customers as fake blocks sales and wears out staff at bank call volumes
  15: "POOR\n\nAUDIO"
  13: Phone compression, blur and noise hide many of the clues detectors look for
  32: "LIVE\n\nSPEED"
  30: Live calls give detectors seconds to decide without hurting call quality
  19: "MISSING\n\nLABELS"
  17: Content credentials prove real media is genuine, but most fakes simply carry no label
  36: "NO\n\nSTANDARD"
  34: Vendors test on their own data, so buyers cannot compare accuracy claims fairly
sources:
  - claim: Detection tools struggle to train on media from the latest generators
    url: https://gov.uk/government/publications/deepfake-detection-technology/deepfake-detection-technology
    date: '2026-03-26'
    quote: "it prevents deepfake detection tools from training on data generated with the latest creation technologies"
  - claim: Open-source detectors lost about half their AUC on real 2024 deepfakes
    url: https://arxiv.org/html/2503.02857v2
    date: '2025-03-04'
    quote: "the performance of open-source state-of-the-art deepfake detection models drops precipitously when evaluated on Deepfake-Eval-2024"
  - claim: Injection attacks feed false material directly into systems instead of a live person on camera
    url: https://securitybrief.co.uk/story/iproov-report-warns-of-soaring-ios-injection-attacks
    date: '2026-04-09'
    quote: "Injection attacks involve feeding false or manipulated material directly into systems instead of presenting a live person to a camera or sensor."
  - claim: Pindrop markets a false positive rate under 1%, a key buyer requirement
    url: https://www.pindrop.com/?p=43732
    date: '2024-05-22'
    quote: "Pindrop’s deepfake detection technology has demonstrated a 99% detection rate with a false positive rate of less than 1%."
  - claim: Compression, blur and poor audio can hide detection clues
    url: https://digitaltrends.com/phones/microsoft-teams-is-adding-a-safeguard-against-deepfake-imposters-in-meetings/
    date: '2026-10'
    quote: "Compression, lighting changes, blur, background movement, and poor audio can hide some of the clues detection systems normally look for."
  - claim: Real-time calls require managing latency and quality
    url: https://gov.uk/government/publications/deepfake-detection-technology/deepfake-detection-technology
    date: '2026-03-26'
    quote: "Managing latency and maintaining the quality of video and audio calls"
  - claim: Content Credentials distinguish media with proof of creation from media without it
    url: https://securityaffairs.com/?p=182068
    date: '2025-09-10'
    quote: "Google’s Pixel 10 applies Content Credentials to distinguish between content with verifiable proof of creation and media without such provenance."
  - claim: Providers often claim high accuracy without independent validation
    url: https://gov.uk/government/publications/deepfake-detection-technology/deepfake-detection-technology
    date: '2026-03-26'
    quote: "providers often claim high accuracy without independent validation"
```

### ed095
```yaml
status: ok
section: Tech and infra
title: Why can’t we solve them yet?
note: We tied each reason to how detection actually works rather than assuming one engineering change can solve the full problem.
t:
  39: BOTTLENECK
  38: REASON WHY
  41: BOTTLENECK
  40: REASON WHY
  7: "NEW\n\nMODELS"
  5: Each new generator leaves different traces, so a detector must relearn with fresh fake samples
  24: "LAB\n\nGAP"
  22: Lab datasets use old fakes and staged actors, unlike what spreads on social media
  11: "INJECTED\n\nVIDEO"
  9: Virtual camera apps sold online make an injected feed look like a real camera to the app
  28: "FALSE\n\nALARMS"
  26: Real customers on bad phones or webcams can look odd, so every threshold trades risk
  15: "POOR\n\nAUDIO"
  13: Compression throws away the fine detail where AI traces hide in sound or image
  32: "LIVE\n\nSPEED"
  30: Bigger, more accurate models need more computing, which adds delay to a call
  19: "MISSING\n\nLABELS"
  17: Labels only work when cameras and apps adopt them, and fraudsters never opt in
  36: "NO\n\nSTANDARD"
  34: There is no shared test set or accuracy rule, and few vendors publish outside tests
sources:
  - claim: Fraud tactics evolve and require constant detector updates
    url: https://gov.uk/government/publications/deepfake-detection-technology/deepfake-detection-technology
    date: '2026-03-26'
    quote: "Evolving fraud tactics that require constant updates to detection tools"
  - claim: Academic benchmarks use outdated techniques and staged paid actors
    url: https://pdf.arxiv.org/pdf/2503.02857
    date: '2025-03-04'
    quote: "these datasets are not representative of deepfakes circulating on social media, because many use outdated manipulation techniques"
  - claim: Native virtual camera attacks rose 2665%, partly through app store infiltration
    url: https://www.businesswire.com/news/home/20250226745447/en
    date: '2025-02-26'
    quote: "Native Virtual Camera attacks have become the primary threat vector, increasing by 2665% due partly to mainstream app store infiltration."
  - claim: Real-time calls must balance latency and quality
    url: https://gov.uk/government/publications/deepfake-detection-technology/deepfake-detection-technology
    date: '2026-03-26'
    quote: "Managing latency and maintaining the quality of video and audio calls"
  - claim: Inconsistent test datasets and metrics lower confidence in detection tools
    url: https://gov.uk/government/publications/deepfake-detection-technology/deepfake-detection-technology
    date: '2026-03-26'
    quote: "Inconsistencies in testing datasets and evaluation metrics result in low confidence in the efficacy of detection tools"
```

### ed096
```yaml
status: ok
section: Tech and infra
title: When can we realistically expect to solve them?
note: We base these estimates on current product launches, benchmark studies and public guidance. They are directional rather than consensus forecasts.
t:
  39: BOTTLENECK
  38: WHY THIS TIMELINE
  41: BOTTLENECK
  40: WHY THIS TIMELINE
  7: "NEW\n\nMODELS"
  5: Models that check physics may catch unseen fakes, but proof on live traffic needs a few years
  24: "LAB\n\nGAP"
  22: Shared real-world datasets like Deepfake-Eval-2024 help, but they need refreshing every year
  42: '2030'
  46: '2027'
  11: "INJECTED\n\nVIDEO"
  9: Injection checks already ship, but attackers keep moving to new phone platforms like iOS
  28: "FALSE\n\nALARMS"
  26: Layering voice, device and behavior signals cuts errors, but tuning needs real customer data
  43: '2027'
  47: '2028'
  15: "POOR\n\nAUDIO"
  13: Phone-grade models already exist, but very low-quality audio will stay hard
  32: "LIVE\n\nSPEED"
  30: Smaller models cut delay, and Microsoft Teams now gives detectors a native hook
  44: '2028'
  48: '2027'
  19: "MISSING\n\nLABELS"
  17: Phones like the Pixel 10 sign photos at capture, but most devices and apps do not yet
  36: "NO\n\nSTANDARD"
  34: The UK government calls for a standard accuracy test, but no shared scheme exists yet
  45: '2030'
  49: '2028'
sources:
  - claim: DETECT-World checks physical consistency to flag content from untrained generators
    url: https://www.resemble.ai/deepfake-detection-for-google-meet/
    date: '2026'
    quote: "so it can flag content from generators it hasn't been trained on"
  - claim: Deepfake-Eval-2024 is a public in-the-wild benchmark built from 2024 deepfakes
    url: https://arxiv.org/abs/2503.02857v1
    date: '2025-03-04'
    quote: "Deepfake-Eval-2024 consists of 44 hours of videos, 56.5 hours of audio, and 1,975 images"
  - claim: Injection attacks on iOS rose 741% in 2025
    url: https://www.businesswire.com/news/home/20260408812610/en
    date: '2026-04-08'
    quote: "Injection attacks targeting iOS devices surged by 1,151% in the second half of 2025, contributing to a 741% annual increase."
  - claim: Microsoft Teams provides integration for certified detection providers
    url: https://bleepingcomputer.com/news/security/microsoft-teams-to-add-third-party-deepfake-detection-impersonation-protection
    date: '2026-10-08'
    quote: "Microsoft says it will provide Teams integration and experiences to surface and act on deepfake detection signals triggered by supported providers."
  - claim: Pixel 10 attaches Content Credentials to every photo, and Google plans to extend it to other Android devices
    url: https://www.redhotcyber.com/en/post/google-fights-misinformation-c2pa-arrives-on-pixel-and-photos-for-ai-image-recognition
    date: '2025-09'
    quote: "For now, the Content Credentials system will only be available on Pixel 10 devices"
  - claim: The UK government review recommends a standard approach to accuracy evaluation
    url: https://gov.uk/government/publications/deepfake-detection-technology/deepfake-detection-technology
    date: '2026-03-26'
    quote: "A standardised approach and guidance on accuracy evaluation would benefit both consumers and providers"
```

### ed097
```yaml
status: ok
section: Tech and infra
title: Which bold bets could reshape deepfake detection?
note: We grounded the bets in current product directions such as signing at capture, platform hooks, AI agent detection, loss warranties and physics-based models.
t:
  9: PROOF AT CAPTURE
  12: DETECTION IN EVERY CALL
  15: AGENT VERIFICATION
  18: LOSS GUARANTEE
  33: "NEAR-TERM HORIZON\n\n(0-5 YEARS)"
  7: It is every phone and camera signing photos and video when they are taken, like the Pixel 10
  10: It is deepfake checks built into every meeting and phone platform, as Teams now allows
  13: It is checking whether a caller or a chat is a real person or an AI agent acting for someone
  16: It is vendors paying back losses when their tool misses a fake, as Pindrop's warranty began
  21: WORLD MODELS
  24: VERIFIED HUMAN ID
  27: COURT-READY FORENSICS
  30: ON-DEVICE CHECKS
  34: "LONG-TERM HORIZON\n\n(5-10 YEARS)"
  19: It is detectors that check light, motion and physics, so they catch fakes they never saw
  22: It is a reusable proof that a real person stands behind an account, the goal of Moir
  25: It is detection reports that judges and insurers accept as evidence of manipulation
  28: It is phones that warn users about fake voices and video locally, without the cloud
sources:
  - claim: Pixel 10 attaches Content Credentials to every photo at capture
    url: https://blog.google/security/pixel-android-trusted-images-c2pa-content-credentials/
    date: '2025-09-10'
    quote: "The Pixel 10 lineup is the first to have Content Credentials built in across every photo created by Pixel Camera."
  - claim: Teams opens meetings to certified third-party deepfake detection
    url: https://bleepingcomputer.com/news/security/microsoft-teams-to-add-third-party-deepfake-detection-impersonation-protection
    date: '2026-10-08'
    quote: "Organizations can enhance meeting security with synthetic audio and video detection solutions provided by certified third-party providers"
  - claim: Vendors now sell AI agent detection
    url: https://www.resemble.ai/integrations-and-partners/linkedin
    date: '2026'
    quote: "The first System One model for AI agent detection"
  - claim: Pindrop's Pulse Deepfake Warranty compensates eligible customers when a deepfake is missed
    url: https://siliconangle.com/?p=663034
    date: '2024-07-17'
    quote: "its Pulse Deepfake Warranty offering, which compensates eligible customers if its tools are unable to detect a deepfake"
  - claim: Physics-based detection catches generators the model was not trained on
    url: https://www.resemble.ai/deepfake-detection-for-google-meet/
    date: '2026'
    quote: "reviewing both known generation patterns and physical reality, including lighting, motion, and continuity"
  - claim: Moir is raising about $50M to help people prove their identity online
    url: https://www.bloomberg.com/news/articles/2026-09-21/former-xai-staffer-eyes-50-million-for-firm-to-fight-deepfakes
    date: '2026-09-21'
    quote: "Tina Oberoi is forming a new startup called Moir that aims to develop new technology to help individuals prove their identities online"
  - claim: Detection reports exported for regulators and counsel
    url: https://resemble.ai/products/meetings
    date: '2026'
    quote: "Every detection produces a forensic report exportable for regulators and counsel."
comment: On-device checks is a forward-looking bet with no single product cited.
```

### ed098
```yaml
status: ok
section: Tech and infra
title: Which companies are working on groundbreaking tech today?
t:
  8: RESEMBLE AI
  6: They sell DETECT-World, tested on 250+ AI generators, and bots that watch meetings
  24: REALITY DEFENDER
  22: They score voice, video and images for fakes and offer a free API tier of 50 checks a month
  11: PINDROP
  9: They check calls for cloned voices and extend that defense to Zoom, Teams and Webex
  27: INCODE
  25: Deepsight blocks deepfakes and fake cameras in ID checks for Scotiabank, Nubank and TikTok
  14: MODULATE
  12: They analyze over 10 million hours of audio a month to flag fake voices and scams
  30: IDENTIFAI
  28: They power F-Secure's Deepfake Protection, sold through 200+ telecom partners
  17: GETREAL SECURITY
  15: They pair deepfake detection with continuous checks of who is really speaking in a call
  33: IMPER.AI
  31: They spot impersonators on Zoom, Teams and Slack using device and network signals
sources:
  - claim: DETECT-World is tested against 250+ generative AI models and Resemble Meetings bots join calls
    url: https://www.resemble.ai/our-solution/
    date: '2026'
    quote: "Real-time multimodal detection across audio, video, and images. Battle-tested against 250+ generative AI models"
  - claim: Reality Defender launched a public API with a free tier of 50 detections a month
    url: https://www.securitysystemsnews.com/article/reality-defender-launches-public-api-and-free-tier
    date: '2025'
    quote: "along with a free tier offering 50 detections per month"
  - claim: Pindrop Pulse for Meetings works on Zoom, Webex and Microsoft Teams
    url: https://www.businesswire.com/news/home/20251119488893/en
    date: '2025-11-19'
    quote: "Now available on Zoom®, Webex by Cisco® and Microsoft Teams."
  - claim: Incode Deepsight is deployed at Scotiabank, Nubank and TikTok
    url: https://www.pymnts.com/newswire-announcements/incode-launches-deepsight-an-effective-deepfake-defense/
    date: '2025-12-05'
    quote: "Deepsight is already being deployed at Scotiabank, Nubank, and, TikTok having protected millions of users across more than 6 million live identity sessions"
  - claim: Modulate analyzes more than 10 million hours of audio a month
    url: https://www.securityweek.com/modulate-raises-25-million-to-advance-deepfake-detection/
    date: '2026-09-28'
    quote: "The firm currently analyzes more than 10 million hours of audio each month"
  - claim: IdentifAI powers F-Secure's Deepfake Protection across 200+ service-provider partners
    url: https://www.f-secure.com/en/partners/newsroom/f-secure-and-identifai-launch-deepfake-protection
    date: '2026-06-16'
    quote: "The partnership brings together F‑Secure’s network of more than 200 service-provider partners and IdentifAI’s specialist deepfake detection technology."
  - claim: GetReal combines multimodal deepfake detection with continuous identity verification
    url: https://pr.taosnews.com/article/GetReal-Security-Has-Been-Named-As-a-Market-Shaper-in-the-2026-Gartnerr-Emerging-Market-Quadrant-for-Deepfake-Detection-Startup-Vendors/6a4f838d16e7610b3c53da41
    date: '2026-07-09'
    quote: "The platform combines multimodal deepfake detection, continuous identity verification"
  - claim: imper.ai analyzes device telemetry, network diagnostics and behavior across Zoom, Teams and Slack
    url: https://www.ynetnews.com/tech-and-digital/article/sykm5eym11e
    date: '2025-12-04'
    quote: "analyzing hard-to-fake signals like device telemetry, network diagnostics and behavioral patterns rather than scanning message content"
comment: Incode (founded 2015) and IdentifAI are included as identity and consumer deepfake defense specialists. Clarity is left out because Deel acquired it in August 2026.
```

### iv_pipeline
```yaml
status: ok
section: Tech and infra
title: Which deepfake detection products launched recently?
note: We list eight representative products launched or expanded in the last 12 months because the slide has eight fixed rows. Other launches exist outside this layout.
t:
  38: LAUNCH
  34: Forensics tool shows where media was altered, beyond a verdict
  37: CYBERETTE · FRAUD TEAMS
  27: SCALE
  26: IDENTIFAI · CONSUMERS
  24: Deepfake Protection checks images, video and voice for F-Secure
  23: LAUNCH
  22: ID-PAL · REMOTE KYC
  20: Injection Attack Detection catches fake video fed into selfie checks
  19: SCALE
  18: INCODE · ID ONBOARDING
  16: Deepsight blocks deepfakes and fake cameras in selfie checks
  15: LAUNCH
  12: Continuous identity checks catch deepfake callers in live calls
  14: GETREAL SECURITY · IDENTITY
  11: LAUNCH
  10: RESEMBLE AI · TEAMS CALLS
  8: Resemble Meetings runs natively in Teams, flagging fake faces and voices
  7: LAUNCH
  6: POLYGRAF AI · MEETINGS
  4: Meeting Guard spots deepfakes and impostors in Zoom, Meet and Teams
  3: LAUNCH
  2: OMNISPEECH · ZOOM CALLS
  0: AI Detect flags cloned voices live in Zoom calls with color codes
sources:
  - claim: Cyberette launched its deepfake forensics platform on September 30, 2026
    url: https://www.biometricupdate.com/202610/cyberette-launches-deepfake-forensics-platform-to-show-where-media-was-manipulated
    date: '2026-10'
    quote: "Amsterdam-based media forensics startup Cyberette launched a deepfake detection platform on September 30"
  - claim: IdentifAI's Deepfake Protection launched with F-Secure, a named large partner, on June 16, 2026
    url: https://www.f-secure.com/en/partners/newsroom/f-secure-and-identifai-launch-deepfake-protection
    date: '2026-06-16'
    quote: "F‑Secure and deepfake-detection experts IdentifAI have joined forces to help digital service providers combat the rapidly rising threat of AI‑generated scams"
  - claim: ID-Pal announced enhanced Injection Attack Detection on March 24, 2026
    url: https://www.id-pal.com/injection-attack-detection-launch/
    date: '2026-03-24'
    quote: "today announced enhancements to their Injection Attack Detection (IAD) capabilities, as part of its Liveness Testing function"
  - claim: Incode Deepsight runs at Scotiabank, Nubank and TikTok across 6 million live sessions
    url: https://www.pymnts.com/newswire-announcements/incode-launches-deepsight-an-effective-deepfake-defense/
    date: '2025-12-05'
    quote: "having protected millions of users across more than 6 million live identity sessions to date"
  - claim: GetReal made continuous identity verification generally available on May 18, 2026
    url: https://www.tmcnet.com/usubmit/2026/05/18/10384211.htm
    date: '2026-05-18'
    quote: "today announced the general availability of continuous identity verification"
  - claim: Resemble Meetings launched as a native Microsoft Teams integration on November 3, 2026
    url: https://www.resemble.ai/resources/microsoft-teams-certified-deepfake-detection-partner
    date: '2026-11'
    quote: "Organizations running Teams can now deploy Resemble Meetings as a native Teams integration from the Teams admin center."
  - claim: Polygraf AI launched Meeting Guard for Zoom, Microsoft Teams and Google Meet in July 2026
    url: https://www.channelinsider.com/security/tools-and-platforms/polygraf-ai-meeting-guard-deepfake-detection/
    date: '2026-07-14'
    quote: "Polygraf AI launches Meeting Guard to detect deepfakes, impersonation, AI-generated responses, and PII exposure during enterprise video meetings."
  - claim: OmniSpeech AI Detect became globally available on the Zoom App Marketplace in January 2026
    url: https://www.securityinfowatch.com/ai/news/55341632/omnispeech-omnispeech-brings-real-time-deepfake-audio-detection-to-zoom-marketplace
    date: '2026-01-06'
    quote: "announced the global availability of OmniSpeech AI Detect™ on the Zoom App Marketplace"
comment: This slide is re-targeted to eight recent products. Stage reads BETA for private or public beta, LAUNCH for general availability in the last 12 months, SCALE for use by a named large client or with a public usage figure. Incode is SCALE (6 million sessions, Scotiabank, Nubank, TikTok) and IdentifAI is SCALE (F-Secure and its 200+ partners).
```
