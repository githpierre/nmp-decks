# Healthcare AI deck: plan (13 Nov 2026)

- Model: the In Vivo CAR-T deck (reference). uuid 19, handle healthcare-ai, footer label "H E A L T H C A R E    A I".
- Startups base: rounds searched until 2026-11-04 (9 days before the start). 685 companies, 892 equity rounds since January 2024, $30.8B. Pierre updates it himself in another conversation.
- Definition v2 (5 Nov 2026) and its 6 categories: Clinical AI Tools, Diagnostic AI Software, Care Workflow AI, Revenue Cycle AI, Payer AI Platforms, Life Science AI.
- Pain points chapter (4 segments, proposed, to be validated by Pierre): hospitals and health systems; physician practices and clinics; health insurers; pharma and biotech.
- Value creation chapter (proposed, to be validated): the 6 categories of the base, so the deck has one category set everywhere (Humanoid Robotics kept two sets and that was left open).
- Cover: "nmp - cover deck (1-225)" slide 19 (objectId g3b2eeb73a21_0_168) -> cover_slide.json, cover.yaml, assets/covers/healthcare-ai.jpg. Compared with the slide thumbnail: same crop. The slide title reads "AI HEALTHCARE" (three lines), copied as is.
- Live product page: 13 slides, S01 to S12 one each plus S11-02. No category donut (S03-02): ed047p is asked in the prompts and judged at Step 4.
- Google Trends: the live S02 uses "healthcare ai" (worldwide, 5 years). CSVs to come from Pierre.
- Research prompts (13 Nov): `python3 tools/make_market_prompts.py --spec plans/healthcare-ai.yaml` -> 12 TXT, 118 slides asked. iv_pipeline -> rollouts at named customers, iv_deals -> corporate deals, iv_fda -> path into a hospital, iv_safety -> patient safety risks.
