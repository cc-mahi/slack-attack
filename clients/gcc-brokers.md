---
slug: gcc-brokers
refs:
  vibepulse: ../VibePulse/.claude/clients/gcc-brokers.yaml
  billing: ../MahiProduct/data/billing/clients.json     # entry: gcc-brokers
  hosts: ../MahiProduct/data/client-hosts.json          # entry: gcc-brokers
  wiki: null                                             # ../MahiProduct/wiki/clients/gcc-brokers.md (not yet)
channels_override: null
key_people_overrides:
  - {name: "Daria Horton", role: "Mahi trading ops liaison"}
  - {name: "Carl", role: "client ops / LMAX + Finalto mappings", confidence: low}
  - {name: "Nael", role: "client trading ops", confidence: low}
  - {name: "Youssef", role: "client — CFD internalisation rollout", confidence: low}
last_catchup: 2026-04-30T11:10:00Z
---

## Recent issues

> [open] 2026-04-24 — 1599oz XAUUSD long filled on Finalto, Compass adjustment needed
> Nael reported 1599oz gold long filled on Finalto; William to adjust Compass position. [permalink](https://mahifx.slack.com/archives/C09PNC1MFAA/p1777020863581119)

> [open] 2026-04-23 — LMAX XAUUSD feed still throttled to ~10/sec after requested 100/sec uplift
> Daria asked for LMAX feed throttle uplift from 10/sec (1 per 100ms) to 100/sec to improve hedging in fast markets. Client applied 100/sec ~04:59 BST, but Mahi still seeing <10/sec as of 11:43 BST — William suspects EOD restart needed on Mahi side; asked Carl to also recheck throttle on LP side. [permalink](https://mahifx.slack.com/archives/C09PNC1MFAA/p1776908972956929)

> [open] 2026-04-23 — CFD internalisation go-live instrument list proposed
> Will proposed initial indices for CFD hedging go-live: ASXAUD, G30EUR (DE40), STXEUR, F40EUR, JPXJPY, IBXEUR, UKXGBP, NDXUSD, DOWUSD, SPXUSD, E50EUR. Awaiting Youssef confirmation. [permalink](https://mahifx.slack.com/archives/C09PNC1MFAA/p1776957653145169)

> [resolved] 2026-04-23 — NG futures orders rejected (distribution quantity set to 500)
> Carl's 1k-quantity NG futures orders rejected; Shyam identified the distribution qty was capped at 500 vs Finalto min 10k. Normal-quantity bumped to 10k; distribution gateway restart scheduled for EOD. NGASM6→NGM6 mapping confirmed active. [permalink](https://mahifx.slack.com/archives/C09PNC1MFAA/p1776900791650569)

## Notable topics

- 2026-04-23 — "Crypto later?" — William agreed to follow-up session with client on crypto setup after CFD list sign-off.
