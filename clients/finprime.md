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
last_catchup: 2026-10-16T07:05:37Z
status: active
---

## Now
Pre-contract A-book broker prospect (XAUUSD-heavy retail flow, ~$21bn/month). Channels created 2026-10-12; initial value-add sims on their Jul-Sep flow are recorded internally (reruns with daily classification pending); Will frames it as an A-book optimisation story, weekend gold de-emphasised. They want a decision in ~2 weeks. Nothing has gone to FinPrime yet: NDA not signed, report not presented.

## Streams

### valueadd-sims — XAUUSD value-add sims on FinPrime flow
status: open · since: 2026-10-14 · last: 2026-10-15
State: Rory's internal initial results (NAGA as basis) on Jul-Sep XAUUSD fills: pricing layer is skew ~$5m/yr plus size control (LR) ~$11m/yr (84% from tickets of 500 oz+, a third from two logins; LR to be sized with FinPrime, PSM not yet read); classification plus selective internalisation adds ~$0.9m/quarter holding only B-book flow, up to ~$2.1m routing by class with a bigger worst day (provisional, classes from console lists; 37% of flow unclassified due to 28-day classifier lookback; 38% netted in busiest week). Classification stays out of client material until the rerun shows value. Will reframes this as an A-book optimisation story (think GCC and Velocity): show how the classifier picks flow to run in a Compass risk model across SI holding periods, with Jenkins Compass sims for PnL and risk plots and SVA on good cohorts; must answer whether paying Mahi beats A-booking and what aggregation does to their book; PnL in $/M. Sim limits: no LP fills, 29-30 Sep missing to the known sim shutdown defect.
Next: Rory: M2M rerun with daily classification then SI on per-trade tags (~5h) and PSM read from SVA #807 (~15 min). Will/Rory: fill-rate cost alongside size control before any client page.
Refs: https://mahifx.slack.com/archives/C0C8M89J2JY/p1791968009205219 https://mahifx.slack.com/archives/C0C8M89J2JY/p1792072798832239 https://mahifx.slack.com/archives/C0C8M89J2JY/p1792073078399249

### data-asks — Data gaps to raise with FinPrime (Derick)
status: open · since: 2026-10-14 · last: 2026-10-15
State: Asks that change sim results: their LP hedge fills, A/B or LP-routed flag per fill, whether logins 7610696 (12.2% of notional) and 7125182 are omnibus/API accounts. Will owns taking these to Derick. Weekend gold is dropped as a lead ask: Rory traced it to Mahi's own prep (the 30 Sep expo email and pitch), not the 9 Oct call; the export only has `XAUUSD`, so a separate `XAUUSD247` symbol is possible but Will says not to get hooked on it. Also open internally: StarPrime both-sides decision (no StarPrime flow is in the export).
Next: Will to raise with Derick; Mahi to decide StarPrime both-sides position.
Refs: https://mahifx.slack.com/archives/C0C8M89J2JY/p1791969668222939 https://mahifx.slack.com/archives/C0C8M89J2JY/p1792076672117709

### commercial-timeline — NDA, presentation and decision timing
status: open · since: 2026-10-15 · last: 2026-10-15
State: FinPrime want to decide in ~2 weeks. Bonnie asked when the report is ready to present; Will said early next week, plans to book them Monday morning (a Q&A the following afternoon floated, likely Tuesday). No NDA yet; Bonnie will send one, and Will asked whether one is needed before sharing commercials.
Next: Bonnie: send NDA. Will: finish report, book Monday session.
Refs: https://mahifx.slack.com/archives/C0C8M89J2JY/p1792067299721989 https://mahifx.slack.com/archives/C0C8M89J2JY/p1792067828307029

## Arc
- 2026-10-12 — #mahi-finprime and #internal-finprime created by Bonnie Cassidy; FinPrime liquidity app added to the shared channel
- 2026-10-14 — FinPrime XAUUSD trade file received and sims started
