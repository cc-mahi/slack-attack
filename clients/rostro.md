---
slug: rostro
name: Rostro
type: broker
status: live
products: [fx]
regions: [LDN]
contract_expires: null
channels:
  internal: internal-rostro
  client: [mahi-rostro]
  other: []
key_people:
  - {name: "Alexandre", role: "trading ops", confidence: low}
  - {name: "Will", role: "scheduling contact", confidence: low}
  - {name: "Oliver Ryan", role: "trading ops — classification/routing, hedger setup"}
  - {name: "Abdullah Almasharfa", role: "ops — PXM/LP connections, subscriptions", confidence: low}
athena_dbs: [rostro_ldn]
aws_profile: null
last_catchup: 2026-04-24T09:00:00Z
---

## Summary

LDN-based broker contracted under Easton Consulting (original agreement 2025-06-01). Volume-tiered fixed fee: $30k up to $20bn → $80k up to $100bn. Rolling 1-month terms for first 6 months (30d notice), then rolling 3-month (90d notice). B-book only (`B_CLIENTS`). Hosting: Beeks Apollo (~GBP404/mo est.) plus AWS pass-through.

## Technical notes

- **LDN infra**: trading `rostro-ln-trading-1.wjze.prod.mahimarkets.com`, admin `rostro-ln-admin-1.wjze.prod.mahimarkets.com`, DC LD4.
- **S3**: `rostro-parquet-store`. Athena DB: `rostro_ldn`.
- **6-party book structure** including SI and CNH. Parties: `CLIENTS_NET`, `CLIENTS_HEDGING`, `B_CLIENTS_NET`, `SI_BOOK_NET`, `OFF_BOOK_NET`, `CNH_CLIENTS_NET`.
- **Trade types**: `CLIENT_TRADE`, `BROKER_CLIENT_TRADE`, `SPLIT_CLIENT_TRADE`, `AGGRESSIVE_HEDGE_TRADE`, `UNKNOWN_TYPE_TRADE`.
- **LP FIX**: `fixMarketData1`, `fixMarketData3`, `fixMarketDataInternal1`.
- **Distribution markets (LDN)**: `CLIENT_PRICE_LDN`, `CLIENT_PRICE_BETA_LDN`, `CLIENT_PRICE_INV_LDN`, `CLIENT_PRICE_RETAIL_LDN`, `CLIENT_PRICE_VIP_LDN`, `DISTRIBUTION_LDN`, `DISTRIBUTION_INSTI_LDN`, `DISTRIBUTION_INTERNAL_LDN`, `DISTRIBUTION_INV_LDN`.

## Recent issues

> [open] 2026-04-23 — XNGUSD retail-feed pricing still being finalised
> Abdullah tried subscribing XNGUSD/NGC1 and got `unknown symbol`; Kate confirmed the correct mapping is `NG1USD` but pricing is still being finalised — don't send flow yet. Jump sub-code `NTGASP` confirmed earlier. [permalink](https://mahifx.slack.com/archives/C08AQKRU953/p1776932072322889)

> [open] 2026-04-22 — G30EUR rejects (cpty 109_1_2656) via arb-classification exec rule
> Limit-order flow getting cancelled because arb classification routes to a neutral-rate + markup exec rule, and the continuity rate breached the limit price. Kate digging into the trades to confirm whether the arb tag is correct. [permalink](https://mahifx.slack.com/archives/C08AQKRU953/p1776871777184599)

> [resolved] 2026-04-23 — HRP_AGG_HEDGE re-added to XAUUSD off-book hedger
> Oli asked for HRP_AGG_HEDGE back in the hedging pool for XAUUSD off-book flow only (not brokered). Initially added more broadly; Isaac corrected the scope on 04-24. [permalink](https://mahifx.slack.com/archives/C08AQKRU953/p1776962468190769)

> [resolved] 2026-04-22 — Invast order-response latency (~2s ack, 3min cancel)
> Nathan flagged Invast taking ~2s to respond to order requests (risk exposure on fills unknown) and a separate 3-minute cancel response. Root cause: OZ-Hub maintenance 17:30–18:30 NY on Invast side — order sat as pending leg in xcore until TTL cancel. Kate asked Abdullah to flag scheduled LP maintenance windows in advance. [permalink](https://mahifx.slack.com/archives/C08AQKRU953/p1776741282590589)

> [resolved] 2026-04-22 — INV/SI routing sweep, overrides removed for 104*/146*
> Oli asked for a classification + execution rule sweep so everyone trades down INV except 104* and 146*. Kate confirmed SI/INV connection setup: arb/signal-follow/broker → brokered, fast-hedge → SI book, remainder → Off Book. [permalink](https://mahifx.slack.com/archives/C08AQKRU953/p1776865644758649)

> [resolved] 2026-04-20 — Cpty 104_7_129656_11_0 off-book PnL drop
> Kate caught -$101k aggregated yield over 4 minutes in the off book driven by 104_7_129656_11_0, classified as signal follow + broker. Removed the `104_7*` off-book whitelist and risk-split their flow to SI book; rule priorities adjusted. [permalink](https://mahifx.slack.com/archives/C08AQKRU953/p1776688746006519)

> [open] 2026-04-17 — Missing pricing on new retail-feed API
> Alexandre reports gaps on the newly-created retail feed API. Rory King investigating; Chrysovalantis looped in for reference. Some symbols (USOIL→CL1USD) corrected; XNGUSD now tracked as separate `[open]`. [permalink](https://mahifx.slack.com/archives/C08AQKRU953/p1776422678609409)

> [resolved] 2026-04-16 — G30 EUR RETAIL spread misconfig
> Alexandre saw TOB 70cfd@1.46 vs configured 20cfd@0.8 (NYC TZ) on primexm. Cameron Hughes: signal widening was making first+second layer spreads match and stack at distribution. Fixed with signal change + pricer bounce; Alexandre confirmed. [permalink](https://mahifx.slack.com/archives/C08AQKRU953/p1776363572685119)

> [resolved] 2026-04-13 — riskReportingExtended1 OOM cascade (PD Q35MSLWK24J7MJ)
> Signal aggregates (`*.Signals.*.SR.*.*.1.CumSumNoOpinion`) frozen in Graphite since 2026-04-11 07:40 UTC because MahiMain commit 066fb9437 broke snapshot publishing; `keepLastValue` across 4,348 series blew heap. Bumping 2→4→6 GB only delayed it. Resolved by rolling back the webstack change (`512a10b`). [permalink](https://mahifx.slack.com/archives/C8568C6HG/p1776073126336049)

## Notable topics

- 2026-04-21 — Client call outcomes: (1) they want LR PnL backtesting under different parameter changes — Andrew notes the existing LR sim supports this and will draft a KB article; (2) exploring SI-PnL attribution per client — Kate to check the Exinity script Will C wrote; (3) want a "Big Boys" book with a lower VAR threshold to route large-clip clients and reduce exposure — achievable in next couple of days. [permalink](https://mahifx.slack.com/archives/C08ALS66EDC/p1776761460382099)
- 2026-04-21 — Will/Andrew internal discussion: Rostro LR tuning highlights the value of inverting the sim — "what params get me X $/M across client, with toxic top-5% at 50 $/M and everyone else ≤ 5 $/M" — vs forward parameter search. Declarative-rule direction flagged for future work. [permalink](https://mahifx.slack.com/archives/C08ALS66EDC/p1776764246169119)
- **Futures-based index pricing / custom basis** — Rostro asking about status; previously discussed with "Sammy". No clear owner on Mahi side; Andrew suggested discussing in person. [permalink](https://mahifx.slack.com/archives/C08ALS66EDC/p1776353177596759)
- **In-person client meeting** — Kate and Andrew scheduling via Will for next week or week after, LDN.
