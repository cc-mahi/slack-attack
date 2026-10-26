---
slug: finprime
aliases: []
refs:
  vibepulse: null    # no VibePulse yaml; only FINPRIME / FINPRIME_RETAIL in MahiProduct hedging-health raw results
  billing: null      # no billing entry
  hosts: null        # no client-hosts entry
  wiki: null         # no wiki page (see ../MahiProduct/wiki/clients/starprime.md for the related StarPrime thread)
channels:
  internal-finprime: C0C8M89J2JY
  mahi-finprime: C0C8HCFKE9G
contacts: []
last_catchup: 2026-10-26T08:05:16Z
status: active
---

## Now
Pre-contract A-book broker prospect (XAUUSD-heavy retail flow, ~$21bn/month). Channels created 2026-10-12. Fresh Jul-Sep dataset with A/T (A-book/T-book) split arrived 2026-10-21; William Denny is running M2M, skew value-add and classification sims on it (overnight batch started 2026-10-22 ~00:00 BST). Andrew wants a narrative-first pitch: retaining spread revenue FinPrime passes to providers, going in cheap with a risk-only install and bundled free bridge/direct connectivity; SI and hedging are not the value-add. Sims are slowed by pool contention (runs due 23-28 Oct); Will is prepping FinPrime for a presentation early next week and has asked for rough commercials. They want a decision in ~2 weeks; NDA status unconfirmed.

## Streams

### valueadd-sims — XAUUSD value-add sims on FinPrime flow
status: open · since: 2026-10-14 · last: 2026-10-23
State: Rory's earlier internal results on Jul-Sep fills were provisional (skew ~$5m/yr, LR ~$11m/yr, classification adding ~$0.9-2.1m/quarter). William Denny has since rerun on the fresh A/T data (A 445,764 trades, T 235,344; UTC timestamps verified). M2M canaries and July runs done with continuous per-day classification (212 of 744 A-book logins change class within a week); full 1 Jul-1 Oct M2M runs in progress. SVA canaries (1 Jul, 09:00-13:00 UTC) show signal ranking IFMS > SKEW_1 > SKEW_0 on both books; at benchmark skew (median $0.15) PnL scales ~7-8x versus fixed 2c. Known drops: SVA hardcodes a 1% yield outlier filter, and replay end truncates late trades. Overnight batch: SVA on A/T x Jul/Aug/Sep at fixed $0.05 skew, M2M with classifier, and soft-flow variants (brokers, signal followers, arbitrageurs removed) to show uplift without toxic accounts. Andrew also wants internalisation rates and holding-period analysis; Will Carter asked about adaptive skew (Andrew: realistic skews first, adaptive is its own research track). As of 2026-10-23 William reports all T-book and all-counterparty runs done and (14:57 BST) all SVA sims done; only A-book soft Jul/Aug (continuous and non-continuous classification) were still running. Best results: SI PnL (30s window) A $3.44M ($85/M), T $2.16M ($97/M); skew PnL best signal IFMS everywhere at ~$11.3/M (A $454k, T $251k). A new classification run completed in 58 min at warp x2295 once pool contention eased. Andrew's regime sim (run #19, house perspective, hedge at wholesale +15%) shows A-book hold-everything only came good on the 28 Sep gold fall (final +$6.1M, max drawdown $19.2M, -$3.5M without its 3 largest days) while classifier-live earned steadily (final +$4.7M, drawdown $1.9M); counterfactual, as FinPrime pass A through at zero DPM today and the T-book lacks their manual hedge trades. Andrew also notes FinPrime's holding period is far longer than the wider network, so yield profiles should be extended past the longest revaluation (as for Bluecrest, 24-48h), with an AI routine for holding-period assessment, timezone analysis, sim first and UI second; per-counterparty skew PnL versus book skew to decide when tailoring skew is worthwhile. Andrew is moving yield profiles in-memory alongside holding period and skew stats, adding rules to record sim failure reasons, and floated a swap-inventory skew idea (clients sit on losing positions; skew at rollover) as a possible prototype and GTM study.
Next: William Denny: finish A-book soft Jul/Aug runs, then per-classification yields on full Jul-Sep, Python SI sims and an internal summary with links; progress tracked in his Claude artifact tracker.
Refs: https://mahifx.slack.com/archives/C0C8M89J2JY/p1791968009205219 https://mahifx.slack.com/archives/C0C8M89J2JY/p1792590134007479 https://mahifx.slack.com/archives/C0C8M89J2JY/p1792742226807169 https://mahifx.slack.com/archives/C0C8M89J2JY/p1792780135778559

### openclose-info — Open/close information needed on new orders
status: open · since: 2026-10-23 · last: 2026-10-23
State: Andrew, working the FinPrime data, sees growing evidence that reclassification needs open/close information on new orders: when flow is reclassified only new positions should route to the new classification, which is impossible without it. Vantage classification is quite active, largely routing the close to the open book, which Andrew calls reckless as a dominating consideration. A product-level gap rather than FinPrime-specific.
Refs: https://mahifx.slack.com/archives/C0C8M89J2JY/p1792749044344509 https://mahifx.slack.com/archives/C0C8M89J2JY/p1792749578890209

### data-asks — Data gaps to raise with FinPrime (Derick)
status: open · since: 2026-10-14 · last: 2026-10-21
State: Fresh Jul-Sep XAUUSD dataset with the A/T identifier arrived via Zendesk #23665 and was prepped on 2026-10-21 (589 logins trade both books; only 70 T-only). Still open: their LP hedge fills, per-fill LP-routed flag, and whether logins 7610696 (12.2% of notional) and 7125182 are omnibus/API accounts. Will owns taking these to Derick. Weekend gold is dropped as a lead ask (traced to Mahi's own prep, not the 9 Oct call); a separate `XAUUSD247` symbol is possible but not a priority. Also open internally: StarPrime both-sides decision (no StarPrime flow in the export).
Next: Will to raise remaining asks with Derick; Mahi to decide StarPrime both-sides position.
Refs: https://mahifx.slack.com/archives/C0C8M89J2JY/p1791969668222939 https://mahifx.slack.com/archives/C0C8M89J2JY/p1792495003035739 https://mahifx.slack.com/archives/C0C8M89J2JY/p1792571655168959

### commercial-timeline — NDA, presentation and decision timing
status: open · since: 2026-10-15 · last: 2026-10-23
State: FinPrime want to decide in ~2 weeks. Bonnie asked when the report is ready to present; Will said early next week, plans to book them Monday morning (a Q&A the following afternoon floated, likely Tuesday). No NDA confirmed in channel; Bonnie was to send one. On 2026-10-20 Will, with Isaac, reworked the microsites to do what the earlier Gamma reports did (numbers don't all align, value is there) and planned to wing the meeting, presenting by speaking rather than slides, then fix the numbers and send afterwards. Andrew's line if FinPrime are A-book: Mahi moved GCC and ATC from STP brokers (RoS at most 40% of the book) to far higher; Will agrees A-book optimisation will come through in comms.
Andrew (2026-10-21): start with the narrative and use the analysis to support it; SI and intelligent hedging are not value-adds, the value-add is what changes in FinPrime's economics. For the A-book, the story is retaining more of the spread revenue passed to providers; he is tempted to go in low with a risk-only install (feature-led as much as P&L-led) and close on the wider pricing opportunity later. Andrew (2026-10-22): go in cheap enough to win and respect feature breadth; they may not participate in execution or pricing at all (in-house bridge); bundle free bridge and direct connectivity to undermine in-house tech. On 2026-10-23 Will told FinPrime they are being prepped for early next week and asked William and Bonnie for rough commercials on current data.
Next: William/Bonnie: rough commercials. Will: fix microsite numbers post-meeting and send. Bonnie: NDA (unconfirmed).
Refs: https://mahifx.slack.com/archives/C0C8M89J2JY/p1792067299721989 https://mahifx.slack.com/archives/C0C8M89J2JY/p1792567913393749 https://mahifx.slack.com/archives/C0C8M89J2JY/p1792739183473799

## Arc
- 2026-10-12 — #mahi-finprime and #internal-finprime created by Bonnie Cassidy; FinPrime liquidity app added to the shared channel
- 2026-10-14 — FinPrime XAUUSD trade file received and sims started
