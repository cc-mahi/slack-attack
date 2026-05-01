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
last_catchup: 2026-05-01T15:35:00Z
---

## Recent issues

> [open] 2026-05-01 — CFD internalisation live testing: LP routing clarified, instrument tests in progress
> Client confirmed routing split: Futures + Spot Commodities (USOIL/UKOIL/NGAS) → Finalto only; Spot Indices + CFD Crypto → LMAX only (Finalto has no CFD Indices; crypto offer on Finalto deemed poor). Shyam set up MAHI_LP_CFD proxy (VELOCITY_EXINITY + LMAX) for CFD pricing. William bounced hybridHedgerCFD1 to pick up CO1USD and CL1USD additions; initial CL1USD test hedged to LMAX (wrong), fixed mapping, re-tested to Finalto. CO1USD also confirmed Finalto. DOWUSD, NDXUSD, SPXUSD tested to LMAX — all confirmed. JPXJPY, UKXGBP, ASXAUD queued next as of window close. NG1USD flagged internally as third Finalto commodity — mapping not yet complete. [permalink](https://mahifx.slack.com/archives/C09PNC1MFAA/p1777636046504329) [internal](https://mahifx.slack.com/archives/C09QS1NUA80/p1777635124504809)

> [resolved] 2026-04-30 — 7230oz XAUUSD long filled on Finalto, Compass adjustment needed
> Carl reported 7230oz gold long filled on Finalto at 21:56 BST; Shyam adjusted Compass positions to match at 01:13 BST 2026-05-01. Carl confirmed "Perfect thanks". [permalink](https://mahifx.slack.com/archives/C09PNC1MFAA/p1777559404368639)

> [resolved] 2026-04-30 — Daria ran manual hedger training call with Carl and Nael
> Daria huddled with Nael/Carl to walk through XAUUSD manual hedging process (hybridHedgerManualFinalto1 + hybridHedgerManualLmax1). Daria confirmed Carl and Nael watched the process, then operated XAGUSD hedger themselves — "should be able to leave it with them from now on". Total XAUUSD spread on the training session was $360 averaging $21/M vs Nathan's estimate of $219/M — saving est. $3.3k vs unhedged. Hedgers left enabled post-session. [permalink](https://mahifx.slack.com/archives/C09PNC1MFAA/p1777581628461159) [internal](https://mahifx.slack.com/archives/C09QS1NUA80/p1777585361762089)

> [resolved] 2026-04-24 — 1599oz XAUUSD long filled on Finalto, Compass adjustment needed
> Nael reported 1599oz gold long filled on Finalto; William to adjust Compass position. [permalink](https://mahifx.slack.com/archives/C09PNC1MFAA/p1777020863581119)

> [open] 2026-04-23 — LMAX XAUUSD feed still throttled to ~10/sec after requested 100/sec uplift
> Daria asked for LMAX feed throttle uplift from 10/sec (1 per 100ms) to 100/sec to improve hedging in fast markets. Client applied 100/sec ~04:59 BST, but Mahi still seeing <10/sec as of 11:43 BST — William suspects EOD restart needed on Mahi side; asked Carl to also recheck throttle on LP side. No further mention in window. [permalink](https://mahifx.slack.com/archives/C09PNC1MFAA/p1776908972956929)

> [resolved] 2026-04-23 — CFD internalisation go-live instrument list proposed
> Will proposed initial indices for CFD hedging go-live: ASXAUD, G30EUR (DE40), STXEUR, F40EUR, JPXJPY, IBXEUR, UKXGBP, NDXUSD, DOWUSD, SPXUSD, E50EUR. Awaiting Youssef confirmation. Now superseded by 2026-05-01 live testing run — routing split confirmed and testing commenced. [permalink](https://mahifx.slack.com/archives/C09PNC1MFAA/p1776957653145169)

> [resolved] 2026-04-23 — NG futures orders rejected (distribution quantity set to 500)
> Carl's 1k-quantity NG futures orders rejected; Shyam identified the distribution qty was capped at 500 vs Finalto min 10k. Normal-quantity bumped to 10k; distribution gateway restart scheduled for EOD. NGASM6→NGM6 mapping confirmed active. [permalink](https://mahifx.slack.com/archives/C09PNC1MFAA/p1776900791650569)

## Notable topics

- 2026-05-01 — Bank holiday notice (Mon 4 May): Nia posted standard Mahi bank holiday advisory — Slack less monitored, emergency support via support@mahimarkets.com or London/NZ phone lines. [permalink](https://mahifx.slack.com/archives/C09PNC1MFAA/p1777622406041909)
- 2026-04-23 — "Crypto later?" — William agreed to follow-up session with client on crypto setup after CFD list sign-off.
