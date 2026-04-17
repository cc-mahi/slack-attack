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
athena_dbs: [rostro_ldn]
aws_profile: null
last_catchup: 2026-04-17T11:47:00Z
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

> [open] 2026-04-17 — Missing pricing on new retail-feed API
> Alexandre reports gaps on the newly-created retail feed API. Rory King investigating; Chrysovalantis looped in for reference. [permalink](https://mahifx.slack.com/archives/C08AQKRU953/p1776422678609409)

> [resolved] 2026-04-16 — G30 EUR RETAIL spread misconfig
> Alexandre saw TOB 70cfd@1.46 vs configured 20cfd@0.8 (NYC TZ) on primexm. Cameron Hughes: signal widening was making first+second layer spreads match and stack at distribution. Fixed with signal change + pricer bounce; Alexandre confirmed. [permalink](https://mahifx.slack.com/archives/C08AQKRU953/p1776363572685119)

> [resolved] 2026-04-13 — riskReportingExtended1 OOM cascade (PD Q35MSLWK24J7MJ)
> Signal aggregates (`*.Signals.*.SR.*.*.1.CumSumNoOpinion`) frozen in Graphite since 2026-04-11 07:40 UTC because MahiMain commit 066fb9437 broke snapshot publishing; `keepLastValue` across 4,348 series blew heap. Bumping 2→4→6 GB only delayed it. Resolved by rolling back the webstack change (`512a10b`). [permalink](https://mahifx.slack.com/archives/C8568C6HG/p1776073126336049)

## Notable topics

- **Futures-based index pricing / custom basis** — Rostro asking about status; previously discussed with "Sammy". No clear owner on Mahi side; Andrew suggested discussing in person. [permalink](https://mahifx.slack.com/archives/C08ALS66EDC/p1776353177596759)
- **In-person client meeting** — Kate and Andrew scheduling via Will for next week or week after, LDN.
