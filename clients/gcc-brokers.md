---
slug: gcc-brokers
refs:
  vibepulse: ../VibePulse/.claude/clients/gcc-brokers.yaml
  billing: ../MahiProduct/data/billing/clients.json     # entry: gcc-brokers
  hosts: ../MahiProduct/data/client-hosts.json          # entry: gcc-brokers
  wiki: null                                             # ../MahiProduct/wiki/clients/gcc-brokers.md (not yet)
channels_override: null
key_people_overrides:
  - {name: "Carl", role: "client ops / LMAX + Finalto mappings", confidence: low}
  - {name: "Nael", role: "client trading ops", confidence: low}
  - {name: "Youssef Bouz", role: "client — CFD internalisation rollout; swap-free account queries", confidence: low}
  - {name: "Layan", role: "client ops — reports Finalto gold fills for Compass adjustment", confidence: low}
last_catchup: 2026-05-14T07:27:02Z
---

## Recent issues

> [open] 2026-05-13 — XAGUSD internalisation proposed; maximumMarketPosition override added
> Daria flagged XAGUSD as a candidate for internalisation (performance screenshot shared in client channel). Nathan added a `maximumMarketPosition` override (20k) on Finalto only for XAGUSD and XAUUSD — intentionally excludes LMAX and LMAX_DEFENSIVE to avoid double-counting combined LMAX exposure. Daria asked internally whether the trial has been extended; no response in window. [Daria XAGUSD proposal](https://mahifx.slack.com/archives/C09QS1NUA80/p1778732190932909) [Nathan override](https://mahifx.slack.com/archives/C09QS1NUA80/p1778712459189179)

> [resolved] 2026-05-13 — XAUUSD/XAGUSD position divergence; LP position limit raised; positions reconciled
> Client reported volume stuck from close-by process at ~21:25 BST. Daria investigated and identified a 15k XAUUSD LP position limit was hit; client (Nael) consented to raising the limit. Carl reported positions: XAUUSD Finalto 65oz / LMAX 0 / Client 65oz; XAGUSD Finalto 111,049 / LMAX 124,900 / Client 235,949. Daria requested EOD position snapshots going forward to catch divergence early. Nathan confirmed positions reconciled by 23:33 BST. [client report](https://mahifx.slack.com/archives/C09PNC1MFAA/p1778703945959439) [Daria limit raise](https://mahifx.slack.com/archives/C09PNC1MFAA/p1778705603277839) [Nathan reconciled](https://mahifx.slack.com/archives/C09PNC1MFAA/p1778711637266609)

> [resolved] 2026-05-14 — Hedger performance report: XAUUSD ~$13k ($71/M), XAGUSD ~$920 ($59/M)
> Daria posted rollover hedger performance summary in client channel. Estimated savings vs previously-paid spreads: XAUUSD ~$13k ($71/M), XAGUSD ~$920 ($59/M). [permalink](https://mahifx.slack.com/archives/C09PNC1MFAA/p1778731913293849)

> [resolved] 2026-05-07 — CO1USD, CL1USD and CFD Indices switched to live internalisation
> William proposed the go-live switch at 13:37 BST; client confirmed at 14:22 BST; William confirmed "all done" at 14:27 BST. Covers CO1USD, CL1USD, and all previously-tested indices (ASXAUD, G30EUR, F40EUR, JPXJPY, UKXGBP, NDXUSD, DOWUSD, SPXUSD). Pricers bounced at 11:22 BST to pick up XAU signals change ahead of the switch. William noted futures fast-hedge setup is still in progress (separate entry). [permalink](https://mahifx.slack.com/archives/C09PNC1MFAA/p1778157450972219) [pricers bounce](https://mahifx.slack.com/archives/C09QS1NUA80/p1778149361517089)

> [resolved] 2026-05-07 — 6718oz XAUUSD long filled on Finalto, Compass adjustment done
> Layan reported 6718oz gold long filled on Finalto at 16:39 BST; William confirmed adjustment done at 16:58 BST. [permalink](https://mahifx.slack.com/archives/C09PNC1MFAA/p1778168396858199)

> [resolved] 2026-05-06 — 116oz XAUUSD long filled on Finalto, Compass adjustment done
> Client reported 116oz gold long filled on Finalto at 15:05 BST; William confirmed booked at 16:26 BST. [permalink](https://mahifx.slack.com/archives/C09PNC1MFAA/p1778076310926249)

> [open] 2026-05-06 — Fast-hedge for futures: metals + indices live 2026-05-13; spot commodities pending
> Client asked for fast-hedge setup on futures ASAP — specifically tags 4004072 and 4004241 slipping on gold futures. 2026-05-07: William confirmed "Futures setup still in progress". 2026-05-12: William told Nael the workflow is being restructured for fast hedging, needs a couple more restarts. 2026-05-13: full test session with client (tag 4036) — XAU, XAG, NDX, SPX, DOW, DAX futures all tested and confirmed hedging to Finalto; William switched metals + indices futures to internalise. Internal: `riskQuantisationOverride` bounced for futures indices (small positions not triggering hedger); dashboard gateway bounced for futures tenant profiles. Client asked about USOIL/UKOIL/NGAS — William confirmed hedger setup "nearly complete" for spot commodities, will advise when ready to test. [original](https://mahifx.slack.com/archives/C09PNC1MFAA/p1778060389989769) [2026-05-13 go-live](https://mahifx.slack.com/archives/C09PNC1MFAA/p1778695014614019) [commodities update](https://mahifx.slack.com/archives/C09PNC1MFAA/p1778695413586369) [internal bounce](https://mahifx.slack.com/archives/C09QS1NUA80/p1778693579315139)

> [resolved] 2026-05-06 — XAGUSD false FI PnL drop on A_CLIENTS (Nathan investigation)
> Nathan flagged a Graphite signal showing a FI PnL drop on XAGUSD for A_CLIENTS on 2026-05-05. Investigated and confirmed false alarm — XAGUSD is not skewed for A_CLIENTS; only XAUUSD is. Nathan noted that only XAUUSD skew on A_CLIENTS should be reported/billed. [permalink](https://mahifx.slack.com/archives/C09QS1NUA80/p1778107331037799)

> [resolved] 2026-05-05 — 1251oz XAUUSD long filled on Finalto, Compass adjustment done
> Nael reported 1251oz gold long filled on Finalto at 15:04 BST; William confirmed adjustment complete at 15:39 BST. [permalink](https://mahifx.slack.com/archives/C09PNC1MFAA/p1777989872967679)

> [resolved] 2026-05-05 — UKXGBP riskQuantisationOverride fix; hybridHedgerCFD1 bounced
> William identified that small UKXGBP test positions were not fulfilling the `minRisk` quantity needed to activate VaR triggers. Applied a change to `hedging.risk.riskQuantisationOverride` for UKX in Compass config, then bounced `hybridHedgerCFD1` to pick it up. Related to ongoing CFD internalisation testing. [internal-config](https://mahifx.slack.com/archives/C09QS1NUA80/p1777995611679109) [bounce](https://mahifx.slack.com/archives/C09QS1NUA80/p1777995516640649)

> [open] 2026-05-04 — Counterparty 4004089 reclassified to Dynamic Signal Follow after ABook PnL drop
> A-book XAUUSD PnL dropped ~$2,700 at 10:20 UTC as counterparty 4004089 traded ahead of a large price move (internalised; market moved against). After a second similar event, 4004089 was reclassified to Dynamic Signal Follow (now brokered). Counterparty 700154 then placed a similarly-sized internalised XAUUSD trade; market moved in Mahi's favour and ~$2,500 was recovered. Reclassification appears actioned; no follow-up confirmation of stability. [internal](https://mahifx.slack.com/archives/C09QS1NUA80/p1777949002875889)

> [open] 2026-05-04 — Fast-hedge strategy proposed for counterparty 700154; swap-free viability questioned
> Cameron Hughes shared yield profile for counterparty tag 700154 (Echo access issue resolved after permissions fix): stays onside for 16 mins in aggregate, making it suitable for fast-hedge (hold risk up to 5 min, let arb hedger chip away, clear via hybrid). Youssef raised concern that this client's high volume is tied to a swap-free offer, which may erode the edge — estimated XAUUSD spread margin ~$20/M and FX ~$11/M. Daria noted analysis needed on whether positions are held overnight vs closed intraday, plus swap charge quantum, before concluding viability. No resolution yet. [permalink](https://mahifx.slack.com/archives/C09PNC1MFAA/p1777908996386319) [Daria analysis](https://mahifx.slack.com/archives/C09PNC1MFAA/p1777931713192039)

> [resolved] 2026-05-01 — CFD internalisation live testing: all instruments confirmed and switched live 2026-05-07
> Client confirmed routing split: Futures + Spot Commodities (USOIL/UKOIL/NGAS) → Finalto only; Spot Indices + CFD Crypto → LMAX only (Finalto has no CFD Indices; crypto offer on Finalto deemed poor). Shyam set up MAHI_LP_CFD proxy (VELOCITY_EXINITY + LMAX) for CFD pricing. William bounced hybridHedgerCFD1 to pick up CO1USD and CL1USD additions; initial CL1USD test hedged to LMAX (wrong), fixed mapping, re-tested to Finalto. CO1USD also confirmed Finalto. DOWUSD, NDXUSD, SPXUSD tested to LMAX — all confirmed. JPXJPY, UKXGBP also confirmed during testing session. ASXAUD test position opened and subsequently closed (confirmed "done" by client 2026-05-01 ~17:13 BST). G30EUR and F40EUR deferred to next week — markets closed over bank holiday weekend. NG1USD flagged internally as third Finalto commodity — mapping not yet complete. 2026-05-05: UKXGBP riskQuantisationOverride fix applied (small positions were not satisfying minRisk to activate VaR triggers); hybridHedgerCFD1 bounced again. 2026-05-06: G30EUR and F40EUR test trades completed by client (14:46 BST); F40EUR hedged by William, client closed position; G30EUR position also closed. Pricers and hybridHedgerCFD1 bounced for CFD benchmark normalisation change at 10:54 BST. William stated "ready to go live with the Indices" pending these tests — indices go-live appears imminent. Remaining open: NG1USD Finalto mapping and fast-hedge setup for futures (separate entry). [permalink](https://mahifx.slack.com/archives/C09PNC1MFAA/p1777636046504329) [internal](https://mahifx.slack.com/archives/C09QS1NUA80/p1777635124504809) [ASXAUD close](https://mahifx.slack.com/archives/C09PNC1MFAA/p1777653635607519) [G30EUR/F40EUR tests done](https://mahifx.slack.com/archives/C09PNC1MFAA/p1778061056321559)

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
