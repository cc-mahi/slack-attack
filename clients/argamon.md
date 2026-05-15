---
slug: argamon
refs:
  vibepulse: ../VibePulse/.claude/clients/argamon.yaml
  billing: ../MahiProduct/data/billing/clients.json     # entry: argamon
  hosts: ../MahiProduct/data/client-hosts.json          # entry: argamon
  wiki: null                                             # ../MahiProduct/wiki/clients/argamon.md (not yet)
channels_override: null
key_people_overrides:
  - {name: "Elan (Argamon CEO/principal)", role: "Principal contact / decision-maker", confidence: low}
  - {name: "Levi Ulman", role: "Argamon ops / connectivity", confidence: low}
  - {name: "Tom (Argamon)", role: "Argamon ops / daily trading", confidence: low}
  - {name: "Jonah Ink", role: "Argamon reconciliation / back-office", confidence: low}
  - {name: "Alex (Karnadi)", role: "Argamon back-office / rec", confidence: low}
  - {name: "Joanna Theofanous", role: "Argamon ops (client-side contact in mahi-argamon-operations)", confidence: low}
last_catchup: 2026-05-15T07:09:01Z
---

## Status

- Stage: live, actively growing (new LPs, platform migration in progress)
- Integration: retail + insti + crypto, NYC only; OneZero→Centroid migration underway (target before Aug 1)
- Relationship: active, operationally intensive; ongoing rec disputes and infra expansion; contract being restructured (Mahi=retail, Toa=crypto/B2B/RI)

## Recent issues

> [open] 2026-04-30 — Retail pricing degradation: wide spreads on majors / LR on retail published rate
> 2025-05-01: client (Tom) flagged majors 20-tick wide for ~2 hours. Will Carter identified LR was kicking in on the published rate and removed it from published. Separately Amir bounced retail pricers to include FSS markets and replace MWMS/BMSL. [permalink](https://mahifx.slack.com/archives/C06TW3D8NMV/p1746108590467959)

> [open] 2025-05-01 — LMAX crypto JPY NOP pressure / hedging adjustment
> Client requested no JPY crypto positions at LMAX ahead of rollover financing. Amir identified LMAX_CFD_DIRECT had -19.21 BTC position. NOP-reducing rules loosened and prioritised; LMAX removed from JPY crypto hedging/STP for the day. [permalink](https://mahifx.slack.com/archives/C06TW3D8NMV/p1746087268008479)

> [resolved] 2025-05-01 — DFSN signal misconfigured as flow signal on insti EURUSD model
> Isaac found DFSN was publishing as a flow signal (not working with specified hold times) on the insti EURUSD model. Fixed; now working as expected. [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1746079638467609)

> [open] 2025-05-06–14 — XAUUSD retail losses from signal-following snipers + model gaps
> Sharp signal-following clients (whitelist; previously broker-only) sniping big XAUUSD moves. Isaac: signal-follow whitelist cleaned up, rule reverted to broker; DFSN signal added to model to step out of way of large moves faster. Retail Time PnL also froze 10am–~8pm 2025-05-14 (ILS rates missing for mark-to-market; PTR_BYPASS_HOUSE NaN position pnl). [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1746063187834529) [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1747250040002329)

> [open] 2025-05-07–16 — LP feed overload / CPU saturation / signal process consolidation
> CPU saturated under latency spike. Exercise to prune LP feeds: cutting duplicate FSS/OZ _2 feeds, removing 26DEGREES from insti hedging, removing JPM_INST from EURUSD/USDJPY mid formation. Andrew consolidated signal processes (signalProcessFI1 taking on what 4 processes did; 9 hybrid hedgers noted as record). Liam: not yet in a position needing emergency action but improvement underway. [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1747151157445879)

> [resolved] 2025-05-14 — Finalto 5+ second latencies to pricer1
> Andrew flagged Finalto-specific latency (5s+) internal to Compass pricer1. Appeared to resolve same day. [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1747246578430539)

> [open] 2025-05-14–16 — Toa feed 2-minute delays (internet buffering) + Toa feed stopped
> ArgamonPrices FIX session backed up to 2 minutes at 2pm 2025-05-14. Root cause: data buffering across internet (not conflating at publisher). Toa feed based on Binance perps at different contract than LMAX/WM. James Furness: dedicated Equinix Fabric NY4-APN1 or Beeks WAN would fix it; Starfish with ACKs as alternative. Decision 2025-05-15: MD feed stopped temporarily and "delete evidence of it" until issues fixed. XRP/XLC hedging moved back to standard Wintermute/LMAX rules; open Binance positions unwound. NY4→TKY dedicated WAN link connected 2025-06-16, latency more consistent. [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1747249556851979) [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1747319952039229) [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1750085749166509)

> [open] 2025-05-14 — Retail distribution process down + XAGAUD/USDHUF pricing gap
> Isaac: retail distribution issue resolved same evening. Residual: XAGAUD/USDHUF couldn't be priced (failover requested). Also hazelcast error on trading-1 restart (2025-05-18); signalAnalysisRx1 down but not in use. [permalink](https://mahifx.slack.com/archives/C06TW3D8NMV/p1747258475449559) [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1747544931545879)

> [open] 2025-05-15–16 — Toxic flow review: counterparties 84004149 and 84004395
> 84004149: big crypto trader, $200k lifetime PnL, up on long-horizon bets; blacklisted from broker automation but flow recently went sharp. Isaac: XBT SI attempted multiple times, never on winning side. Flow moved to broker-only after review. 84004395: identified as toxic (negative yield profile), Andrew flagged "should feel more" at ~$3.5k/M shortfall. Brokered LR added to clientDist1, reduced signal response on retail + EURUSD. [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1747325006356819) [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1747346604273939)

> [open] 2025-05-19 — OneZero→Centroid migration (target before Aug 1)
> Argamon (Levi) confirmed migration plan: current IP 192.81.110.72 is insti; requesting additional retail + crypto sessions. Centroid to clear exclusively via HRP for now. Drop-copy (STP) required for failover/bypass. Centroid FIX tag ordering issue found during test trades (447/448/452 dependent on 453 — Centroid can't configure order); workaround via tag 109 tested successfully 2025-06-05. Retail + crypto Centroid channels set up 2025-05-27. [permalink](https://mahifx.slack.com/archives/C06TW3D8NMV/p1747624459706309) [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1748473150880459)

> [open] 2025-05-19–27 — OneZero→Centroid migration to Lucera (insti) — NatWest drop-copy delay killed Centroid insti plan
> Elan call 2025-05-20 (Daria): not doing insti via Centroid — NatWest drop-copy integration takes 5 months; moving to Lucera instead. Liam noted Mahi bridge as alternative. Lucera FIX spec shared 2025-05-27; Elan asked about HRP mapping. Isaac: using HSBC_RCTV_HRP_1/2 in Compass, not MAHI_1/2 as HRP uses. Reactive UAT test trades passed by 2025-06-30; production test trades 2025-07-01. [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1747698414197519) [permalink](https://mahifx.slack.com/archives/C06TW3D8NMV/p1748324721924009)

> [open] 2025-05-20 — FXSpotStream NOP issues at HSBC (10.13k long position)
> Argamon flagged rejected trades on A Arb NYC 1 / A Hybrid NYC 1 sessions. Cameron confirmed no compass risk, being filled elsewhere; HSBC had 10.13k long position. Offered to configure NOP-reducing trades only to HSBC or remove from markets. HSBC advised resolved same day. [permalink](https://mahifx.slack.com/archives/C06TW3D8NMV/p1747761226613649)

> [open] 2025-05-22 — ACG (new client via Argamon) going live — routing and NOP issues
> ACG (Alpha Capital Group, INST-26) routed via A_CLIENTS/retail model instead of insti. Amir flagged; needs OZ to route down insti connection. NOP limit was 10k (blocking $200k+ trades); raised to 10m. Test trades confirmed 2025-05-22; ACG planned go-live Monday 2025-05-26 but no live trades seen by 2025-05-30. Amir confirmed workflow sound. [permalink](https://mahifx.slack.com/archives/C06TW3D8NMV/p1747923659467649) [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1747929238687569)

> [open] 2025-05-23 — Crypto over-hedging: hedged volume ~2x client volume
> Andrew/Cameron identified hedge volume (7.84M XBTUSD out) roughly double internalised client flow (3.9M) for the week. Root cause: overactive broker-Wintermute delayed dynamic hedging rule interacting with brokered execution rule (broker-first). Rule removed. Possible XBTJPY cross double-counting also flagged. Issue of brokering then hedging simultaneously suspected. [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1748012505591119)

> [open] 2025-05-25 — Beeks connectivity outage (DNS/public internet broken on trading-1/2)
> Beeks change over weekend broke outbound public connectivity on trading-1 and 2; cross-connect unaffected. Retail FX unaffected. Wintermute, LMAX direct, HRP drop copy went down; crypto failed over within OZ. Spotex risk control profile temporarily disabled. Beeks fixed ~2h after request. [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1748217445854529)

> [open] 2025-05-27–ongoing — Compass/Wintermute BTC/ETH position rec divergence
> Ongoing reconciliation work between Argamon and Compass on BTC/ETH positions at Wintermute. First break identified EOD 3 March (BTC). Alex/Jonah/Levi working through trade-by-trade rec; Cameron providing EOD position data. Hedger overactivity (hedgers running during LP-to-LP position netting) identified as a root cause of further drift on 2025-06-04 ETH rec. Will: ops training planned so Argamon can manage this independently. XRPJPY fractional request rejection at Wintermute also fixed 2025-06-01. [permalink](https://mahifx.slack.com/archives/C06TW3D8NMV/p1747206016694509) [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1748964893500969)

> [open] 2025-06-09 — XPTUSD retail loss: -$13.3k from hybrid over-hedging
> Retail lost $13.3k from $51.2m volume. Hybrid hedger did 10M XPTUSD vs 1.1M client flow; XPT was manually hedged. VaR peaked at $23.9k briefly. Will: risk not cleared quickly enough; VaR alert threshold was 80k (too high for the book), proposed drop to 20k. Isaac changed mid used by hybrid hedger to allow it to fire in future. Will: "on track for consecutive months of minimal PnL billing" and a compass backtest over the period recommended to show Elan the fix will work. [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1749459127167139)

> [open] 2025-06-15 — Compass 25.2 release outage (distribution processes down, rollback)
> Release broke all clientDist processes (enableFileBasedMessagePersistence not set). OZ lost pricing, forced failover. Release rolled back; Justin re-enabled setting and processes came up. Second release attempt 2025-06-22 succeeded. [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1749967652935749)

> [open] 2025-06-16–ongoing — Full position rec: AUD/currency drift (~$125k unresolved)
> Position break from 2025-06-16 connectivity issues (dropped trades on reconnect). Ongoing rec of currency positions; AUD drift traced to April (large EURAUD traders) with 15M AUD break between 3–10 April. Jonah/Alex/Levi working through it; Will got rec script into analytics-python-tools. Elan acknowledged noticing AUD position in April. Daria pushed back on P&L attribution ($125k) being a real Compass loss — may be currency conversion not being recced. Elan also asked if loss attributed to retail or crypto; Daria deferred to management. Call planned to continue. Will noted migration to Toa will give much better visibility. [permalink](https://mahifx.slack.com/archives/C06TW3D8NMV/p1750055113472619) [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1751324709151589)

> [open] 2025-07-01 — Contract restructure: Mahi=retail, Toa=crypto/B2B/RI
> Andrew: contract being split — Mahi manages retail tenant, Toa takes crypto/B2B/RI and connectivity pipeline. Meeting requested to discuss new operational setup and resource shuffle. Toa becoming main crypto LP is expected to resolve many rec complexities. [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1751381584552799)

> [open] 2026-04-28 — XAUUSD brokerage to Toa expansion
> Daria added party 104881 to brokered-to-Toa for XAUUSD on argamon.NYC; plan is to migrate the softest of 104881/105048/105153/105681/105773 progressively to see if hedging to CME helps yield. Starting with softest first. [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1777335260425589)

> [open] 2026-05-04 — TOA_CHI/A_EXTERNAL_WASH XAUUSD reject spike (quantity too large) — analytics support question unanswered
> Alert at 11:59–12:00Z: 98% reject ratio (93/95 orders) on TOA_CHI/A_EXTERNAL_WASH for XAUUSD from 1 counterparty (90000580), error `FIELD_VALIDATION_ERROR: quantity=TOO_LARGE, maximumShowQuantity=TOO_LARGE`. Justin Young forwarded the ZD ticket to internal-argamon asking who's on analytics support today; two +1 reactions but no reply in thread. As of 2026-05-08 still no thread reply — unresolved. Zendesk ticket: https://mahifx.zendesk.com/agent/tickets/22907. [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1777898434100499)

> [watching] 2026-05-08 — XAUUSD signal switched to synapse
> Shyam changed XAUUSD signal from current to synapse, motivated by simple skew analysis. Will monitor pricing impact next week; watching for CPs picking off the model post-change. [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1778211684932129)

> [watching] 2026-05-08 — Weekly P&L: $7.5k from 402m (week to date)
> Daria's mid-week update: 222m internalised, 180m brokered. Brokered flow decays quickly but stays onside (3x spread of internalised: $14/M brokered vs $47/M internalised). Two counterparties (928986, 928994) blacklisted from broker for now — bad couple of weeks but aggregate yield acceptable for internalisation. Net brokered spread $3.4k; internalisation P&L $4.1k (RoS 130%); LR P&L $1.4k mostly on brokered. Skew P&L had initial EURUSD open loss from arb but has fully recovered. Focus on skew and mid improvements (Shyam reviewing). [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1778199139811789)

> [resolved] 2026-05-13 — XAUAUD retail scalping loss $5.9k (UBS arb-protection misconfiguration)
> Two new retail accounts (CPs 105988 and 105990, ~6 days old) scalped XAUAUD during FX twilight (22:26–22:42 UTC 2026-05-12): 106 round-trips, 1–30 oz each. Root cause: UBS is sole firm XAUAUD LP; `pricing.arbProtectionParameters` had UBS in reference markets but not referencePriceMarketSelectors, clamping published quote into UBS's wide twilight spread instead of the clean triangulated XAUUSD×AUDUSD price. Fix: removed XAUAUD from arbProtectionParameter rules; pricing now uses pure triangulated price. Shyam monitoring CPs 105988/105990 for activity on other crosses. [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1778648027949039)

> [resolved] 2026-05-13 — toa_argamon.LDN XAUUSD signal data missing on TOB (signal persistence gap post-reboot)
> Elan flagged missing signal data on toa_argamon.LDN XAUUSD in Echo TOB. Daria diagnosed: signal persistence broke after last system reboot. Restart fixed it; signals persisting again from ~02:30 BST. Historical signal data cannot be backfilled for the gap. Elan satisfied with resolution. [permalink](https://mahifx.slack.com/archives/C06TW3D8NMV/p1778634120272459)

## Notable topics

- 2025-05-14 — Spotex FIX orders missing limit price (tag 44) causing rejects; Daria identified in FIX logs, issue patched by Spotex 2025-05-06. [permalink](https://mahifx.slack.com/archives/C06TW3D8NMV/p1746144575233089)
- 2025-05-14 — Compass DB access limitations: Argamon cannot do trade-by-trade rec via compassDB (no HouseOrder/ExternalOrder tables). Cameron/Maten discussing Pulse or expanded permissions. Liam: Pulse contract normally required for that level of access. [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1747653704595619)
- 2025-05-14 — XPD position management: 3 XPD open without client orders; multiple manual HRP GUI trades required to flatten. Trade reconciliation between Compass/OZ explained (trade batching means last trade ID only recorded as adjustment reference). [permalink](https://mahifx.slack.com/archives/C06TW3D8NMV/p1747202086516749)
- 2025-05-16 — Spotex flow changed by Elan to brokered (previously internalise-all); Amir renamed execution rule accordingly. [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1747390292424499)
- 2025-05-19 — Tick frequency query: Liam confirmed most channels throttled to 1 tick/10ms or 3 ticks/10ms. [permalink](https://mahifx.slack.com/archives/C06TW3D8NMV/p1747662637772189)
- 2025-05-20 — Insti discussion: pre-trade credit check / margin component repeatedly requested (by Argamon, Rostro, Alpha, others); Liam confirmed client-side pre-trade check exists; Andrew proposing v1 margin component for alpha platform. [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1747730071488359)
- 2025-05-20 — Crypto JPY trader NOP: 4m limit (other European clients have 8m); requesting 30m–50m. Isaac noted. [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1747698414197519)
- 2025-05-22 — INST-18 vs INST-26 (ACG) channel routing confusion: INST-26 missing ARGM-Bespin1 counterparty; INST-18 should be Sub3 not Sub1. [permalink](https://mahifx.slack.com/archives/C06TW3D8NMV/p1747932640870629)
- 2025-06-03 — Jump (Mando4_T) FIX session connection timeout flagged. [permalink](https://mahifx.slack.com/archives/C06TW3D8NMV/p1748906841745799)
- 2025-06-03 — OZ ACL removal for Mando1/Mando4: Beeks confirming IP address for ACL restoration. [permalink](https://mahifx.slack.com/archives/C06TW3D8NMV/p1748936756234279)
- 2025-06-06 — UBS added for XPT pricing (retail pricers bounced). [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1749219464281909)
- 2025-06-11 — XTX cross-connect NY4 being set up for Argamon via Beeks (shared XC with Integral, £96/m). XTX conformance complete 2025-06-23. [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1749643162624409)
- 2025-06-16 — ILS pairs: Isaac asked Argamon to confirm client/LP positions for ILS ahead of removing from Compass. [permalink](https://mahifx.slack.com/archives/C06TW3D8NMV/p1747344140363979)
- 2025-06-25 — Retail roadmap call requested: Will asked to schedule call with Jeremy and Elan (Argamon doing interesting things on client acquisition). [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1750845735746069)
- 2025-06-26 — XRP and LTC hedging back on Toa. [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1750927626443199)
- 2025-06-30 — Reactive UAT test trades passed; production test trades 2025-07-01 with party mapping config updates. [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1750269992249569)
- 2026-05-03 — XAUUSD retail NY4→CHI hedging disabled: retail achieving positive spreads; CHI giving negative spreads so hedging there turned off. [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1777845150173619)
- 2026-05-04 — EURUSD mid formation: Elan approved adding all LPs back into mid (NY now retail-only). Shyam added DB_RCTV_NWPB_1, EDGW_RCTV_NWPB_1, GTSX_RCTV_HRP_2 as supplementary LPs; backtests show reduced spiky pricing and arb opportunities. Adaptive mid logic also added to betaRetailPricer1 for EURUSD; FI/skew PnL review ongoing. [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1777855717442529) [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1777869938380839)
