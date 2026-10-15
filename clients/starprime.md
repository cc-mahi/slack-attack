---
slug: starprime
aliases: []
refs:
  vibepulse: ../VibePulse/.claude/clients/starprime.yaml
  billing: ../MahiProduct/data/billing/clients.json     # entry: starprime
  hosts: ../MahiProduct/data/client-hosts.json          # entry: starprime
  wiki: ../MahiProduct/wiki/clients/starprime.md
channels:
  internal-starprime: C095MJHC68J
  mahi-starprime: C096422RPKK
contacts:
  - {name: "Samin Arefzaher", role: "Head of Trading; primary day-to-day contact (hedger/NOP/pricing requests)"}
  - {name: "Shahid Afrid", role: "client tech/ops; FIX connectivity, PXM and LP integrations", confidence: low}
  - {name: "Jay M", role: "CEO / co-founder (Jay Mawji)", confidence: low}
  - {name: "Alison Koay", role: "StarPrime; Echo/Compass access (2026-06), Slack invite 2026-10-06", confidence: low}
  - {name: "Umar Bin Aziz", role: "client ops; execution/pricing incident reporting, needs execution-rule-editor write access", confidence: low}
  - {name: "Clarice Frost", role: "overnight ops (startrader.com)", confidence: low}
  - {name: "Allan Maira", role: "overnight ops (startrader.com)", confidence: low}
last_catchup: 2026-10-15T13:04:16Z
status: active
---

## Now
Relationship is fragile after four incidents in September (two Beeks/PXM connectivity outages, an NFP over-hedge, and old-price rejections on 18 Sep that made them route flow away for about three days); Andrew Morgan promised an improvement review and said more issues likely lose the client.
Pricing latency is healthy since adaptive was cut on 22 Sep, but the pricer-by-asset-class split and the deeper Aeron/CEP fixes are still outstanding.
Growth: RBF (FINPRIME/Vantage) B-book white-label went live 6 Oct with first flow 9 Oct, and XAG on the SI model goes live Monday 19 Oct.

## Streams

### si-hedging — SI model, hedger NOP restarts and LP position reconciliation
status: open · since: 2026-08-17 · last: 2026-10-14
State: Samin updates NOP limits and execution markets in Compass most days and asks Mahi to restart the SI and arb hedgers, which Mahi does by hand. LP positions are periodically realigned through paired maker/client adjustments after StarPrime sends LP snapshots, and risk-reducing LPR rules were added for Edgewater, Argamon, Invast and B2Prime on 28 Sep. XAG on SI is configured and goes live Monday 19 Oct on KAMA_RETAIL, ARGAMON_INSTI_PXM, ISPRIME_VIP and EDGEWATER_RETAIL; EURUSD with tighter spreads is next, and Samin also floated revenue shares on the SI model.
Next: Samin sets XAG maximumMarketPosition per LP before Monday; Will Carter owes Samin an answer on SI revenue-share mechanics.
Refs: https://mahifx.slack.com/archives/C096422RPKK/p1786973579898989 https://mahifx.slack.com/archives/C096422RPKK/p1791872874279109 https://mahifx.slack.com/archives/C095MJHC68J/p1791971454187659

### pricer-load — Pricer CPU/latency, trading-host balance and rejections
status: open · since: 2026-08-19 · last: 2026-10-14
State: Cancels and rejects on 19 Aug (pricer out of sync after restart, trading-1 memory pressure) and the 18 Sep old-price rejects trace to pricer load: node-1 on trading-2 overloaded, an Aeron image-health bug and CEP hotspotting. Rebalancing to node-0 and removing adaptive on FX (22 Sep) cut pricer CPU and worst cycles sharply, and the weekly latency sweep rates StarPrime OK from 7 Oct. On 13 Oct instruments were trimmed to the 14 actually filled to relieve riskReportingExtended1 and mdAnalyticsProcess (effective at the Saturday reboot). Pricer-by-asset-class split, the Aeron fix and the CEP work are still pending, and Samin asked that the pricing load reduction wait until next week so he can give input.
Next: Mahi dev ships the asset-class split and controlled-release fixes; Samin to give input on load reduction.
Refs: https://mahifx.slack.com/archives/C096422RPKK/p1787131381126679 https://mahifx.slack.com/archives/C095MJHC68J/p1789742576436339 https://mahifx.slack.com/archives/C095MJHC68J/p1791967057451979

### tag-blacklist-ux — Counterparty tag blacklist scale and wildcard matching
status: open · since: 2026-07-31 · last: 2026-10-14
State: The reference.marketSupport.tagList grows without bound, is slow to load and edit, and Samin asked Dev for a more efficient mechanism. On 14 Oct a Kama counterparty (SXR_5038_n/a) was still receiving flow despite a blacklist attempt; Samin wants one market with a pasted list of tags, and wildcards such as SXR_5038* so new account suffixes are covered. Justin Young is looking at a paste-a-list workflow.
Next: Nathan Burch passed the load concern to Dev; Justin Young on the paste/wildcard UI.
Refs: https://mahifx.slack.com/archives/C096422RPKK/p1785477517683469 https://mahifx.slack.com/archives/C096422RPKK/p1791956484365609 https://mahifx.slack.com/archives/C096422RPKK/p1791978715992619

### access-data-requests — Access provisioning and ad-hoc data/report requests
status: open · since: 2026-08-18 · last: 2026-10-14
State: Recurring asks for orders VWAP proofs for client queries (18 and 20 Aug), hedger fills/rejects reports, FIX logs, and last month's SI breakdown and three months of SI trade data for revenue shares (forwarded 1 Oct, delivery not seen). Samin said Pulse access is needed and wants to chat with Shahid; Edwin Jarilla's access was added then removed (18 Sep), Alison Koay was added to Slack (6 Oct), and on 14 Oct Samin asked for Umar to be allowed to edit the execution-rule-editor, which Nathan Burch is investigating.
Next: Mahi to confirm Umar's execution-rule-editor access; confirm whether the SI data and rev-share file went out.
Refs: https://mahifx.slack.com/archives/C096422RPKK/p1787033520203829 https://mahifx.slack.com/archives/C096422RPKK/p1787233885680149 https://mahifx.slack.com/archives/C096422RPKK/p1791955277857929

### rbf-finprime — RBF (FINPRIME/Vantage) B-book white-label via PrimeXM
status: open · since: 2026-08-25 · last: 2026-10-13
State: RBF clients come into StarPrime's PXM, are sent to Mahi via three maker connections (MFX-RBF-RETAIL1-3) and Mahi brokers 1:1 to FINPRIME (OneZero) through MFX-RBF-T1; FX, metals and indices tested, CFD books and RBF_CFD_TIER1-3 channels added 16 Sep, and go-live 6 Oct with first flow 9 Oct. Running in broker mode (BROKER_FIRST, FINPRIME pool, passthrough fills, no price improvement). Phase 2 timed 1-1 hedging with holding periods needs dev (the hedger can't hedge order by order, brokered orders can't be held, last look doesn't apply), and on 13 Oct Samin said he would try to run it like SI instead. Samin also wants CLIENT_PRICE_FINPRIME_LDN (an unskewed FINPRIME price); Will Carter wants a name avoiding other broker names. Per Samin, FINPRIME is Vantage.
Next: Samin to confirm whether a 1-1 hedger is still needed; Mahi to create the FINPRIME price channel under a neutral name; call Samin/Cameron Hughes/Liam Cordelle on the 1-1 design.
Refs: https://mahifx.slack.com/archives/C096422RPKK/p1787639946529319 https://mahifx.slack.com/archives/C096422RPKK/p1787821229088939 https://mahifx.slack.com/archives/C095MJHC68J/p1791533957409969 https://mahifx.slack.com/archives/C095MJHC68J/p1791896187205599

### beeks-pxm-connectivity — Beeks/PrimeXM connectivity outages and cross-connect
status: open · since: 2026-09-03 · last: 2026-10-05
State: Distribution sessions dropped for about 4h16m from 2 Sep 21:31 UTC when Beeks removed the only firewall permit, undetected by Mahi because session monitoring was not on. A Beeks change on 9 Sep caused a second outage, and weekend changes broke the outbound PXM target again on 13 Sep (fixed 14 Sep with a new target IP). Session monitoring is now on by default, RBF stream sessions excepted until live. The cross-connect path is asymmetric (outbound to PXM over LINX), and a written post-mortem to Samin was still pending on 8 Sep; Beeks sent an RFO on 1 Oct that Mahi may need to forward. Shahid proposed hosting Mahi on PXM infrastructure; Liam Cordelle offered a direct call between Mahi and PXM.
Next: Mahi to forward the Beeks RFO and written post-mortem to Samin; PXM and Mahi hosting call; fix the cross-connect asymmetry.
Refs: https://mahifx.slack.com/archives/C096422RPKK/p1788398257009819 https://mahifx.slack.com/archives/C095MJHC68J/p1788407799564089 https://mahifx.slack.com/archives/C096422RPKK/p1789042170691379 https://mahifx.slack.com/archives/C095MJHC68J/p1791200108861299

### stability-reviews — Client confidence, incident follow-up and improvement review
status: open · since: 2026-09-18 · last: 2026-10-02
State: Jay and Samin felt let down after four incidents in a month; at the 21 Sep Dubai meeting no reparations were sought, they want better service and reliability with auto-routing around Mahi outages, and Andrew Morgan promised a review of improvements. A review was booked for Wednesday 7 Oct; no record of it happening is in these channels. Mahi added a policy that restoring service is pre-approved (PR 76) and tuned a weekly latency review routine; Andrew also planned an RFP note on PrimeXM/Beeks.
Next: Andrew Morgan to present the operational changes; confirm the 7 Oct review took place and its outcome.
Refs: https://mahifx.slack.com/archives/C095MJHC68J/p1789745037600429 https://mahifx.slack.com/archives/C095MJHC68J/p1789906351811219 https://mahifx.slack.com/archives/C095MJHC68J/p1790930290687889 https://mahifx.slack.com/archives/C096422RPKK/p1790932610630419

### lr-slippage-yield — LR tuning, slippage automation and yield classification
status: open · since: 2026-08-20 · last: 2026-09-27
State: An LR health check on 20 Aug found StarPrime's LR healthy ($5.62/M, rank 5 of 17) but the B_CLIENTS profile mis-tuned (burst 5,000,000, cap 25) and B_CLIENTS_TIER2 a stub; recommendation was burst 500,000 and cap 60, and it is not visible whether it was applied. Classification-based brokering is working well. Dave Cooney wants slippage applied to every classifier-matched counterparty, with StarPrime as pilot (Zendesk 23424); first-trade coverage needs a small MahiMain change. BIGG LR went live for the first time on 20 Sep after a reorder fix, and on 27 Sep David asked what the STARPRIME_MT5_LN1 parties in the Echo yield profile represent.
Next: confirm whether the B_CLIENTS LR change was applied; MahiMain first-trade slippage change; answer David Cooney's party question.
Refs: https://mahifx.slack.com/archives/C095MJHC68J/p1787222052913939 https://mahifx.slack.com/archives/C095MJHC68J/p1788454059838229 https://mahifx.slack.com/archives/C095MJHC68J/p1790478344455159

### weekend-gold-247 — 24/7 gold launch and weekend support scope
status: open · since: 2026-08-21 · last: 2026-09-20
State: StarTrader launched 24/7 XAUUSD in August; Mahi learned from the news. Samin said on 16 Sep he could launch it with Mahi and asked for a price, spreads and margin, but by 18 Sep it was PR'd and not live. After the incident Jay questioned Mahi's ability to support it, and Andrew told Jay on 20 Sep that the current agreement is market-hours support only, to be scoped alongside weekend trading.
Next: scope weekend support coverage with StarPrime if 24/7 gold goes ahead.
Refs: https://mahifx.slack.com/archives/C095MJHC68J/p1787313823826079 https://mahifx.slack.com/archives/C095MJHC68J/p1789548218691959 https://mahifx.slack.com/archives/C096422RPKK/p1789906497829189

### news-brokering — Client switching to broker mode around news
status: watching · since: 2026-09-04 · last: 2026-10-02
State: On 4 Sep (NFP) Samin switched all execution rules to broker with top-ups on, shifting about 92k VaR into the SI book and an over-hedge swing of about -23k that finished positive after risk was cleared; Isaac Dann's RCA notes Samin knows to turn top-ups off. He switched to broker again on 11 Sep (about $6k, without top-ups) and on 2 Oct (about +$1k), against Mahi's advice, because the exposure is outside his risk appetite. A news-specific broker rule is not currently possible.
Next: reopen if another unannounced switch or top-up incident occurs.
Refs: https://mahifx.slack.com/archives/C095MJHC68J/p1788535241170629 https://mahifx.slack.com/archives/C095MJHC68J/p1789129730968719 https://mahifx.slack.com/archives/C095MJHC68J/p1790944325652239

### lp-connections-ttl — LP connectors, TTLs and order linking
status: watching · since: 2026-08-19 · last: 2026-09-15
State: Shahid asked for FIX tag 527 on hedges so PXM orders link to final LP fills (19 Aug, outcome not visible). New or renamed LP connections landed: Argamon on MFX-T5, EDGEWATER_RETAIL rename, Invast and B2Prime in the hedgers. On 15 Sep hedger TTLs for B2PRIME_RETAIL and ARGAMON_* were raised from 10 ms to 30 ms (config added, EOD restart needed), after Shahid explained PXM honours the TTL and that Mahi-to-PXM latency fluctuates 6-9 ms. TTL lives in reference.marketSupport.marketThrottle.
Next: confirm tag 527 outcome; reopen if TTL or rejection issues recur.
Refs: https://mahifx.slack.com/archives/C096422RPKK/p1787149002785969 https://mahifx.slack.com/archives/C096422RPKK/p1787744436191109 https://mahifx.slack.com/archives/C096422RPKK/p1788161355501189 https://mahifx.slack.com/archives/C096422RPKK/p1789468762100799

### ui-feedback — Compass UI feedback and dashboard releases
status: watching · since: 2026-08-20 · last: 2026-09-02
State: Samin's reference call credits the platform highly but names GUI polish and Mahi-internal wording in the config editor as weak, plus a learning curve for new staff. Price Forensics flat-lining was a cancel-price bug fixed 20 Aug, and a large dashboard release went to PROD on 2 Sep. Suggested follow-ups: refresh timeline, a walkthrough for new staff, KB articles.
Next: Mahi to share the dashboard refresh timeline and offer a walkthrough session.
Refs: https://mahifx.slack.com/archives/C096422RPKK/p1787207208884779 https://mahifx.slack.com/archives/C095MJHC68J/p1788275053949079 https://mahifx.slack.com/archives/C095MJHC68J/p1788337882063819

### xau-pricing-config — XAUUSD reference pricing and config-change process
status: watching · since: 2026-08-19 · last: 2026-08-20
State: A pricing config change on 19 Aug made pricing spike (merged liquidity tiers) and was reverted; Samin asked that future changes go to BETA first, then PROD, and agreed. On 20 Aug a $10 XAUUSD spread at market close on CLIENT_PRICE_INSTI led to a timezone-scoped sanity-check config with MAHI_LP_11 still sole reference elsewhere; Samin asked for a backtest of the setting during the roll and referencing ISPRIME_VIP/KAMA_RETAIL/EDGEWATER. No result is visible in the channels.
Next: Daria Horton to report the roll backtest; no activity since 2026-08-20.
Refs: https://mahifx.slack.com/archives/C096422RPKK/p1787126774501579 https://mahifx.slack.com/archives/C096422RPKK/p1787206299160379

## Arc
- 2026-05-13 — Internal: StarPrime is owned by Vantage (David Cooney confirmed).
- 2026-07-14 — Contract signed; onboarding underway.
- 2026-09-01 — GreySpark (Project Redwood) reference call with Samin, top marks across features, technology and QoS; GUI polish, coverage depth and learning curve raised.
- 2026-09-03 — 4h16m distribution outage from Beeks firewall change; session alerting enabled for all connections.
- 2026-09-09 — Second Beeks-caused outage; on 10 Sep Shahid asks about hosting Mahi in PXM infrastructure.
- 2026-09-18 — Old-price rejects; StarPrime routes flow away and switches the SI model off, "fourth incident in a month".
- 2026-09-21 — Dubai meeting with Jay and Samin; Samin turns SI maker back on after the Sunday open telemetry looks good.
- 2026-10-06 — RBF (FINPRIME) go-live; first flow 2026-10-09.
