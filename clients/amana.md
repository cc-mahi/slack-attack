---
slug: amana
name: Amana
type: broker
status: live
products: [fx, metals]
regions: [LDN]
contract_expires: null
channels:
  internal: internal-amana
  client: [mahi-amana]
  other: []
key_people:
  - {name: "Karen Montero", role: "ops / test trading liaison", confidence: low}
athena_dbs: [amana_ldn]
aws_profile: null
last_catchup: 2026-04-17T13:36:00Z
---

## Summary

Broker on profit-share commercial terms covering MFX Compass. 25% of Skew PnL + 25% of LR, with a $10k/mo Compass fixed fee that is waived if the variable component exceeds $10k. Single LDN desk, 3-party setup (no SI, no OFF_BOOK). Original agreement (v2) signed 2025-04-01, rolling 1-month renewal for the first 6 months (30d notice), then rolling 3-month (90d notice).

## Technical notes

- Hosts — LDN: `amana-ln-trading-1.x38p.prod.mahimarkets.com`, `amana-ln-admin-1.x38p.prod.mahimarkets.com` (DC LD5).
- Athena DB: `amana_ldn`. S3 bucket: `amana-parquet-store`.
- Distribution markets (LDN): `CLIENT_PRICE_LDN`, `CLIENT_PRICE_ABOOK_LDN`, `CLIENT_PRICE_BETA_LDN`, `DISTRIBUTION_LDN`.
- LP FIX connections: `fixMarketData1`, `fixMarketData2`, `fixMarketDataCentroid`.
- Trade types: `CLIENT_TRADE`, `BROKER_CLIENT_TRADE`, `SPLIT_CLIENT_TRADE`, `AGGRESSIVE_HEDGE_TRADE`, `UNKNOWN_TYPE_TRADE`.
- Party names: `CLIENTS_NET` = client net P&L; `CLIENTS_HEDGING` = hedging P&L; `B_CLIENTS_NET` = B-book client net P&L.
- 3-party setup — no `SI` or `OFF_BOOK` parties.
- Books: `B_CLIENTS`.
- Hosting: Beeks est. 1 Hades + 2 Apollo ~GBP2,655/mo (estimate, 3 servers per Guru env page). AWS pass-through at cost. GBP→USD month-end rate.

## Recent issues

> [open] 2026-04-17 — XAGUSD onboarding + rollout acceleration asks
> 3dp limit on hedger fixed; hedger latency tuned 10s→5s; XAG added to arb hedger instruments and swapfree hedger config copied over. Amana asking to speed up Futures/Indexes rollout and move all flow into Compass; LR Option 1 to be implemented next. [permalink](https://mahifx.slack.com/archives/C08T42TMKU3/p1776424391417259)

> [open] 2026-04-16 — hedger latency investigation
> Hedger took 30–50s to cover XAG risk on some test trades even after 3dp fix. Tuned wait from 10s→5s; further digging flagged. [permalink](https://mahifx.slack.com/archives/C08SYSMP0EB/p1776332567124099)

## Notable topics
