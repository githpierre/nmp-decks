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

## State on 13 Nov 2026, 23:30 Bangkok (read this first after a break)
- Pierre validated: 4 pain segments, 6 value segments (the base categories), cover kept as on his slide (AI HEALTHCARE).
- Done: cover (copied, words and line spacing), demo, import.args, db slides (db_text.yaml), twins in live.yaml (S04 S05 S07 S08 S09 from base, S10, S11-01, S12, S03-01 as ed052p), pp_s06 in extras.yaml (link still TO WRITE from ed104), the 12 research files in decks/healthcare-ai/research, first fit rewrites in edits.yaml. Rebuild: 189 slides, 4 build issues (map labels), 2 layout issues.
- Google Trends CSVs received: ai in healthcare, ai doctor, ai scribe (assets/trends/healthcare-ai). The live S02 uses "healthcare ai": CSV not received, so ed039p is not in live.yaml yet. Every term falls after July 2026 (also control terms): Google artefact, the curve stops at its last peak.
- To do, in order:
  1. Fit: slide 12 (ed012 products grid: padded and repeated names, rewrite with real product names or drop), map labels (ed049, ed183), ed200 label GOVERNANCE on 2 lines, ed032 signals list (rewrite from the validated SIGNAL slides), ed201 (research answer vs live twin), ed192 (BenevolentAI three times), iv_deals source of the OpenEvidence item (syndication host, find the primary source or drop).
  2. Extra slides (Step 6) from research file 11. Tempus candidates (11, 13) are out: the live radar puts Tempus outside the market. Market opportunity SIGNAL candidates: 02 OpenEvidence users, 04 Insilico H1 revenue, 07 AMA 81%, 08 valuations, 09 pharma deal wave, plus ed039p trends and one from the base (2026 funding already above 2025). Others: 01 funnel, 03 FDA decisions, 06 Recursion loss per dollar, 10 retention, 12 queries per clinician, 14 multiple (Sacra estimate, weak). One review page for Pierre.
  3. Sources (sources_key.yaml, build_sources.py), full visual pass on sheets of 6, diff_slides --snap, review page of the whole deck, then the PDF.
- Open points told to Pierre: live S09 amounts are older than the base (deck twin recomputed), Generate:Biomedicines is in Diagnostic AI Software in the base, Tempus is outside on the live radar but looks present on the live S10 grid, the $29B market size of the live page against Menlo's $1.4B of generative AI spend in 2025, missing logo Verily.

## Update 13 Nov 2026, 23:50
- Pierre's answers: trends on "ai in healthcare" (done, ed039p in live.yaml), live S09 replaced from the base and Tempus tile removed from live S10 (done: fileUpdate v=1794588069, 20 articles updated by Matrixify job 783187687, manifest and journal of nmp-product-pages), latest rounds of $10M or more (done, in make_db_slides.py).
- Prompts now end with a self-check script (tools/selfcheck_template.txt). Skill update proposed to Pierre (card).
- Still to do: items 1 to 3 of the list above (fit of slide 12, extras review page, sources, full visual pass, review page, PDF).
- Seen on the live page texts (not changed): the S10 and S12 paragraphs name Tempus as a known player, and S06 shows slide 06-02 while the manifest lists 06-01 only.

## Update 14 Nov 2026, 00:15
- Page texts of the live page: Tempus replaced by OpenEvidence in the S10 and S12 paragraphs (Matrixify job 783190635, backup in decks/healthcare-ai-pp-fix/backup_live_2026-11-13).
- Extra slides built (extras.yaml, 9 slides + pp_s06) and ed032 rewritten. Review page sent to Pierre: https://claude.ai/artifact/QR9GNe6mFVGKvwhmF8e93o (slug bda12218-13a8-4eaa-951a-d72d12bc8aba, version 1794590029-c815). Waiting for his Oui / Non.
- Deck: 198 slides, 0 build issue, 1 layout issue (slide 12, ed012 products grid to rewrite).
- Humanoid: slide 51 bars fixed with hbars (delivered deck had the bar sizes of another market), PDF rebuilt and to resend.
- Next: slide 12, sources (sources_key.yaml, build_sources.py), full visual pass on sheets of 6, snapshot, review page of the whole deck, PDF.
