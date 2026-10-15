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
last_catchup: 2026-10-15T13:45:51Z
status: active
---

## Now
Pre-contract A-book broker prospect (XAUUSD-heavy retail flow, ~$21bn/month). Channels created 2026-10-12; value-add sims on their Jul-Sep flow are finished and recorded internally. They want a decision in ~2 weeks. Nothing has gone to FinPrime yet: NDA not signed, report not presented.

## Streams

### valueadd-sims — XAUUSD value-add sims on FinPrime flow
status: open · since: 2026-10-14 · last: 2026-10-15
State: Rory ran M2M, SVA, SI and Compass sims on FinPrime's Jul-Sep XAUUSD fills (681k fills, $62.6bn, `prospects` tenant, `exinity.LDN`, comparable to NAGA). Findings: SVA skew plus size control is +$69.6/M at 8c (size control +$45.7/M still needs fill-rate cost shown); SI only adds value with classification (+$1.3-2.1M/quarter, internalising everything loses); Compass netting 34-42% on the busiest week. Internal record exists in MahiProduct docs/valueadd-sims. Sim limits: no LP fills, no weekend gold, 29-30 Sep missing to the known sim shutdown defect.
Next: Rory/Will: client-facing proposition summary after review; show fill-rate cost alongside size control before any client page.
Refs: https://mahifx.slack.com/archives/C0C8M89J2JY/p1791968009205219 https://mahifx.slack.com/archives/C0C8M89J2JY/p1792055440799729

### data-asks — Data gaps to raise with FinPrime (Derick)
status: open · since: 2026-10-14 · last: 2026-10-15
State: Four asks change sim results: their LP hedge fills, A/B or LP-routed flag per fill, weekend gold (absent from export), and whether logins 7610696 (12.2% of notional) and 7125182 are omnibus/API accounts. Will owns taking these to Derick. Also open internally: StarPrime both-sides decision (no StarPrime flow is in the export).
Next: Will to raise with Derick; Mahi to decide StarPrime both-sides position.
Refs: https://mahifx.slack.com/archives/C0C8M89J2JY/p1791969668222939 https://mahifx.slack.com/archives/C0C8M89J2JY/p1792055440799729

### commercial-timeline — NDA, presentation and decision timing
status: open · since: 2026-10-15 · last: 2026-10-15
State: FinPrime want to decide in ~2 weeks. Bonnie asked when the report is ready to present; Will said early next week, plans to book them Monday morning (a Q&A the following afternoon floated, likely Tuesday). No NDA yet; Bonnie will send one, and Will asked whether one is needed before sharing commercials.
Next: Bonnie: send NDA. Will: finish report, book Monday session.
Refs: https://mahifx.slack.com/archives/C0C8M89J2JY/p1792067299721989 https://mahifx.slack.com/archives/C0C8M89J2JY/p1792067828307029

## Arc
- 2026-10-12 — #mahi-finprime and #internal-finprime created by Bonnie Cassidy; FinPrime liquidity app added to the shared channel
- 2026-10-14 — FinPrime XAUUSD trade file received and sims started
