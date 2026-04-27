---
slug: rostro
refs:
  vibepulse: ../VibePulse/.claude/clients/rostro.yaml
  billing: ../MahiProduct/data/billing/clients.json     # entry: rostro
  hosts: ../MahiProduct/data/client-hosts.json          # entry: rostro (also: easton for contracting entity)
  wiki: null                                             # ../MahiProduct/wiki/clients/rostro.md (not yet)
channels_override: null
key_people_overrides:
  - {name: "Alexandre", role: "trading ops", confidence: low}
  - {name: "Will", role: "scheduling contact", confidence: low}
  - {name: "Oliver Ryan", role: "trading ops — classification/routing, hedger setup"}
  - {name: "Abdullah Almasharfa", role: "ops — PXM/LP connections, subscriptions", confidence: low}
last_catchup: 2026-04-27T09:35:00Z
---

## Recent issues

> [open] 2026-04-27 — YM.M26 invalid-size alerts on MAHI_CMC — step size mismatch (Mahi 0.05)
> Andreas: receiving multiple alerts on YM.M26 on MAHI_CMC due to invalid size; their step is 0.05 and asked Mahi to adjust to match. Rory King acknowledged and will adjust. [permalink](https://mahifx.slack.com/archives/C08AQKRU953/p1777282393851299)

> [open] 2026-04-24 — UBS direct feed — connect into Mahi rather than PXM
> Owen: Rostro receiving a direct feed from UBS and want to connect directly into Mahi rather than via PXM; asked for the technical point of contact for UBS's tech team. Kate routed via support@mahifx.com. Awaiting UBS engagement. [permalink](https://mahifx.slack.com/archives/C08AQKRU953/p1777044459539369)

> [open] 2026-04-23 — XNGUSD retail-feed pricing still being finalised
> Abdullah tried subscribing XNGUSD/NGC1 and got `unknown symbol`; Kate confirmed the correct mapping is `NG1USD` but pricing is still being finalised — don't send flow yet. Jump sub-code `NTGASP` confirmed earlier. [permalink](https://mahifx.slack.com/archives/C08AQKRU953/p1776932072322889)

> [open] 2026-04-22 — G30EUR rejects (cpty 109_1_2656) via arb-classification exec rule
> Limit-order flow getting cancelled because arb classification routes to a neutral-rate + markup exec rule, and the continuity rate breached the limit price. Kate digging into the trades to confirm whether the arb tag is correct. [permalink](https://mahifx.slack.com/archives/C08AQKRU953/p1776871777184599)

> [open] 2026-04-17 — Missing pricing on new retail-feed API
> Alexandre reports gaps on the newly-created retail feed API. Rory King investigating; Chrysovalantis looped in for reference. Some symbols (USOIL→CL1USD) corrected; XNGUSD now tracked as separate `[open]`. [permalink](https://mahifx.slack.com/archives/C08AQKRU953/p1776422678609409)

> [resolved] 2026-04-23 — HRP_AGG_HEDGE re-added to XAUUSD off-book hedger
> Oli asked for HRP_AGG_HEDGE back in the hedging pool for XAUUSD off-book flow only (not brokered). Initially added more broadly; Isaac corrected the scope on 04-24. [permalink](https://mahifx.slack.com/archives/C08AQKRU953/p1776962468190769)

> [resolved] 2026-04-22 — Invast order-response latency (~2s ack, 3min cancel)
> Nathan flagged Invast taking ~2s to respond to order requests (risk exposure on fills unknown) and a separate 3-minute cancel response. Root cause: OZ-Hub maintenance 17:30–18:30 NY on Invast side — order sat as pending leg in xcore until TTL cancel. Kate asked Abdullah to flag scheduled LP maintenance windows in advance. [permalink](https://mahifx.slack.com/archives/C08AQKRU953/p1776741282590589)

> [resolved] 2026-04-22 — INV/SI routing sweep, overrides removed for 104*/146*
> Oli asked for a classification + execution rule sweep so everyone trades down INV except 104* and 146*. Kate confirmed SI/INV connection setup: arb/signal-follow/broker → brokered, fast-hedge → SI book, remainder → Off Book. [permalink](https://mahifx.slack.com/archives/C08AQKRU953/p1776865644758649)

> [resolved] 2026-04-20 — Cpty 104_7_129656_11_0 off-book PnL drop
> Kate caught -$101k aggregated yield over 4 minutes in the off book driven by 104_7_129656_11_0, classified as signal follow + broker. Removed the `104_7*` off-book whitelist and risk-split their flow to SI book; rule priorities adjusted. [permalink](https://mahifx.slack.com/archives/C08AQKRU953/p1776688746006519)

> [resolved] 2026-04-16 — G30 EUR RETAIL spread misconfig
> Alexandre saw TOB 70cfd@1.46 vs configured 20cfd@0.8 (NYC TZ) on primexm. Cameron Hughes: signal widening was making first+second layer spreads match and stack at distribution. Fixed with signal change + pricer bounce; Alexandre confirmed. [permalink](https://mahifx.slack.com/archives/C08AQKRU953/p1776363572685119)

> [resolved] 2026-04-13 — riskReportingExtended1 OOM cascade (PD Q35MSLWK24J7MJ)
> Signal aggregates (`*.Signals.*.SR.*.*.1.CumSumNoOpinion`) frozen in Graphite since 2026-04-11 07:40 UTC because MahiMain commit 066fb9437 broke snapshot publishing; `keepLastValue` across 4,348 series blew heap. Bumping 2→4→6 GB only delayed it. Resolved by rolling back the webstack change (`512a10b`). [permalink](https://mahifx.slack.com/archives/C8568C6HG/p1776073126336049)

## Notable topics

- 2026-04-21 — Client call outcomes: (1) they want LR PnL backtesting under different parameter changes — Andrew notes the existing LR sim supports this and will draft a KB article; (2) exploring SI-PnL attribution per client — Kate to check the Exinity script Will C wrote; (3) want a "Big Boys" book with a lower VAR threshold to route large-clip clients and reduce exposure — achievable in next couple of days. [permalink](https://mahifx.slack.com/archives/C08ALS66EDC/p1776761460382099)
- 2026-04-21 — Will/Andrew internal discussion: Rostro LR tuning highlights the value of inverting the sim — "what params get me X $/M across client, with toxic top-5% at 50 $/M and everyone else ≤ 5 $/M" — vs forward parameter search. Declarative-rule direction flagged for future work. [permalink](https://mahifx.slack.com/archives/C08ALS66EDC/p1776764246169119)
- **Futures-based index pricing / custom basis** — Rostro asking about status; previously discussed with "Sammy". No clear owner on Mahi side; Andrew suggested discussing in person. [permalink](https://mahifx.slack.com/archives/C08ALS66EDC/p1776353177596759)
- **In-person client meeting** — Kate and Andrew scheduling via Will for next week or week after, LDN.
