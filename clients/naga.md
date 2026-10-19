---
slug: naga
aliases: []
refs:
  vibepulse: null          # no VibePulse yaml (prospect)
  billing: null            # no billing entry (prospect)
  hosts: null              # no client-hosts entry (prospect)
  wiki: ../MahiProduct/wiki/clients/naga.md
channels:
  internal-naga: C0C8WA6FAKA
  mahi-naga: C0C8WBNM464
contacts:
  - {name: Adrian Prodan, role: NAGA Operations, main day-to-day contact; drives scheduling of the sims report calls}
  - {name: Philip Tatarov, role: NAGA (Capex), added 2026-10-13}
  - {name: Thomas Fawcett, role: NAGA (ex-IG), joined the 2026-10-14 call; new in role}
  - {name: Alexandru Malanca, role: NAGA Operations}
  - {name: Paris Stephanou, role: NAGA Operations}
  - {name: Andrei Vieru, role: NAGA Operations}
last_catchup: 2026-10-19T07:07:26Z
status: active
---

## Now
Prospect (wiki says parked to Q3 2026, but channels opened 2026-10-09 and work is live). Mahi is running a XAUUSD B-book value-add sim report (SI, classification, skew pricing) for NAGA. First read-out call held 2026-10-14; next catch-up expected the week of 2026-10-19. NAGA has just raised $8m with Presto as an investor, which Andrew Morgan sees as competitive pressure.

## Streams

### xau-valueadd-sims — XAUUSD B-book value-add sims and report
status: open · since: 2026-10-09 · last: 2026-10-15
State: Quarter (Jul-Sep) of 432k NAGA B-book gold fills run through Python SI model. Headline SI 2h (12.5c hedge) is $1.45m vs $2.66m hold-everything, with much better risk (drawdown -$158k after the risk fix). Counterparty classification run daily (M2M 1212) drops SI to $1.09m with lower risk; 2026-10-15 figures compare full B-book, SI, and SI plus classifications (slightly lower PnL, better risk profile). Andrew Morgan's position: leave classification out of the client analysis until it shows a positive effect. Reconciliation of Java SI vs Python found and fixed an End-mark bug; full-quarter matched comparison still running.
Next: Shyam/Cameron Hughes rerun SI on per-trade classifier tags (class lists differed: broker $523m vs $360m); Compass engine sim 721 (one week) still running; Java #799 vs Python $1.45m not yet a matched comparison.
Refs: https://mahifx.slack.com/archives/C0C8WA6FAKA/p1791550292600169 https://mahifx.slack.com/archives/C0C8WA6FAKA/p1791948615791079 https://mahifx.slack.com/archives/C0C8WA6FAKA/p1792035103557469

### naga-client-report — Client report and read-out calls
status: open · since: 2026-10-12 · last: 2026-10-14
State: Adrian Prodan asked when the next call on the analysis of submitted data would be. Mahi had a first-pass report with issues to correct, so moved the call from Thursday to Wednesday 2026-10-14 (6.30pm EEST) and presented. Andrew Morgan: call seemed ok; NAGA spreads cushion them against bad flow. Core message: NAGA realised half-spread is 34c (about 68c full), above the market p75 and about 2x Mahi's widest client; skew subsidises tightening. Report was iterated on internally (PSM section +$95k, +$8.92/M extra spread revenue; pricing layer adds $17.30/M).
Next: Catch-up call next week (Andrew Morgan); Bonnie Cassidy to arrange. Andrew wanted to push rather than rush the next deliverable.
Refs: https://mahifx.slack.com/archives/C0C8WBNM464/p1791882666358299 https://mahifx.slack.com/archives/C0C8WBNM464/p1791994202426999 https://mahifx.slack.com/archives/C0C8WA6FAKA/p1791994319278929

### yp-sims-central — Prospect yield-profile sims in Mahi Central
status: watching · since: 2026-10-13 · last: 2026-10-14
State: Prospect YP sims now visible in Mahi Central (Athena-backed, faster than Echo RDS). Sub-counterparty classification was missing; Arun fixed it 2026-10-14 and sims started after 5pm on 2026-10-13 carry the fix. Echo RDS to be retired once Athena is trusted.
Refs: https://mahifx.slack.com/archives/C0C8WA6FAKA/p1791897832365549 https://mahifx.slack.com/archives/C0C8WA6FAKA/p1791966489414859

### naga-competitive-context — Presto investment and competitive context
status: watching · since: 2026-10-09 · last: 2026-10-14
State: NAGA secured $8m with Presto (quant firm) and MDream as strategic investors. Andrew Morgan asked NAGA directly on the 2026-10-14 call; they said Presto is just an investor, not doing anything operationally. Internally there is concern Presto's arrival raises the bar for results.
Refs: https://mahifx.slack.com/archives/C0C8WA6FAKA/p1791558758023999 https://mahifx.slack.com/archives/C0C8WA6FAKA/p1791994264035769

## Arc
- 2026-10-09 — #internal-naga and #mahi-naga created; Adrian Prodan (NAGA) added to the shared channel.
- 2026-10-14 — First sims read-out call with NAGA.
