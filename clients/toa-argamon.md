---
slug: toa-argamon
refs:
  vibepulse: ../VibePulse/.claude/clients/toa-argamon.yaml
  billing: null
  hosts: ../MahiProduct/data/client-hosts.json          # entry: toa-argamon
  wiki: null
channels_override: null
key_people_overrides:
  - {name: "Tom McLean", role: "Argamon-side analyst — primary day-to-day contact in mahi-argamon-operations", confidence: low}
  - {name: "Levi Ulman", role: "Argamon ops — give-up / rejection queries, EOD position rec, crypto margin management", confidence: low}
  - {name: "Joanna Theofanous", role: "Argamon-side ops — recurring contact in mahi-argamon-operations for alerts and client trade queries"}
  - {name: "Jonah Ink", role: "Argamon management — CCed on currency rec breaks and P&L impact discussions alongside Elan", confidence: low}
  - {name: "Alexander Karnadi", role: "Argamon-side tech/ops — runs EOD rec scripts against compassDB, involved in position reconciliation investigation", confidence: low}
  - {name: "Elan Bension", role: "Argamon principal — strategic decisions on insti connectivity (Centroid, Lucera), NOP limits, client onboarding approvals"}
last_catchup: 2026-07-02T06:22:40Z
---

## Status

- **Stage:** live (Argamon is a client of Toa; LDN/APN1/CHI single-box setups)
- **Integration:** Mahi infra hosting Toa-Argamon distribution across LDN, APN1, CHI. NY4→CHI brokering went live 2026-04-08. OneZero → Centroid migration in flight (deadline pre-2026-08-01). Lucera maker integration being set up for insti flow (hedging via Natwest). Crypto hedging migrating from LMAX/Wintermute to Toa/Binance for XBT/XET/XRP/XLC.
- **Relationship:** downstream of Toa. Slack: `internal-argamon`, `mahi-argamon-operations`. Relationship is heavily ops-intensive: daily position recs, crypto manual hedging, connectivity issues. Large ongoing currency position break (JPY) investigation. ACG newly onboarded as sub-client via Argamon.

## Recent issues

> [open] 2026-07-02 — Crypto hedging migrating to Toa; LMAX/Wintermute crypto positions consolidation ongoing
> Isaac reconfigured hedging to route XBT and XET to Toa/Binance; LPR rules added for XBT, XRP, XLC, XET to close LMAX and Wintermute positions over time (only NOP-reducing trades sent there). Argamon adding collateral to Binance as prerequisite. Daily manual requests to move LMAX crypto positions to Wintermute/Toa before rollover to avoid financing charges, with Mahi executing manually. XRP and XLC previously moved back to Wintermute/LMAX after TOA feed was stopped in 2026-05-15. [permalink](https://mahifx.slack.com/archives/C06TW3D8NMV/p1751413243.433589)

> [open] 2026-06-23 — Major currency pair rec breaks; JPY position drift under investigation
> Levi opened a detailed thread: ongoing breaks in currency pair rec with USDJPY most significant (~380M JPY of adjustments needed). Three distinct breaks: client positions vs Mahi client positions; total client vs LP; LP total vs Mahi LP total. Plan: hedge client-vs-LP diff, adjust client drift, adjust LP drift. Daria performed full Compass redeploy (clients failed over to OZ). Isaac adjusted Compass to match Argamon's positions 2026-06-25; P&L impact of JPY adjustments flagged as separate discussion with Elan/Jonah. Underlying currency drift query also slow on compassDB (net_read_timeout bumped to 240s by Justin 2026-06-27). Still active as of 2026-07-02. [permalink](https://mahifx.slack.com/archives/C06TW3D8NMV/p1750664050.949069)

> [open] 2026-06-27 — Lucera maker integration for insti flow; Natwest hedging setup pending
> Elan asked about Lucera integration for majority of insti client flow. Liam confirmed Mahi only has a taker integration; Lucera agreed to write to Mahi spec (2026-06-02). Lucera conformance confirmed complete 2026-06-27; Elan asked for maker session setup hedging via Natwest. Isaac confirmed and asked whether same insti Natwest book structure applies. As of 2026-07-04 thread ongoing. [permalink](https://mahifx.slack.com/archives/C06TW3D8NMV/p1748324721.924009)

> [open] 2026-06-17 — Large historical AUD/FX position break investigation (~15M AUD around early April)
> Tom investigating a ~15M AUD break in client vs LP rec visible in EOD position history (break appeared 2026-04-04, persisted until ~2026-04-10). Cannot find corresponding trades in Compass. Cameron provided EOD Wintermute position history for investigation. Root cause not yet identified. Mahi team continuing joint investigation. [permalink](https://mahifx.slack.com/archives/C06TW3D8NMV/p1750166592.040329)

> [open] 2026-05-22 — ACG (Alpha Capital Group) onboarding via Argamon; routing issue to be fixed
> ACG tested trades via Argamon (2026-05-22); confirmed filled. INST-26 tag routing down A_CLIENTS channel on retail model — should be insti connection. Amir requested OZ route INST-26 down insti connection. NOP limit hit at 10k; raised to 10M for testing. INST-26 classified as Sub3, not Sub1. As of 2026-05-30 Amir confirmed workflow looks good on Mahi side, no ACG live trades yet; Joanna to follow up with ACG. [permalink](https://mahifx.slack.com/archives/C06TW3D8NMV/p1747929736.657979)

> [open] 2026-05-19 — OneZero → Centroid migration; retail and crypto sessions being stood up (pre-Aug deadline)
> Levi announced migration from OneZero to Centroid before 2026-08-01. New retail and crypto Centroid sessions requested in addition to existing insti session (all via HRP for simplicity). Isaac setting up channels using existing process. Drop copy for failover/bypass trades required (STP sufficient). Centroid test trades 2026-05-28 had FIX tag ordering issue — resolved via tag 109 for client ID (confirmed 2026-06-05). HRP mapping for Reactive streams (MAHI_1/MAHI_2 = HSBC_RCTV_HRP_1/2) clarified 2026-06-09. Lucera being set up separately (see 2026-06-27 entry). [permalink](https://mahifx.slack.com/archives/C06TW3D8NMV/p1747624459.706309)

> [resolved] 2026-06-15 — Compass 25.2 upgrade rollback; pricing outage
> Compass upgraded to 25.2 on 2026-06-13 weekend. Upgrade caused liquidity pool data not reaching distribution process → brokered orders rejected. Argamon failed over to OZ. Lee rolled back to previous version; sessions restored within ~2h. Argamon reported no FX pricing at 22:09 BST; Daria resolved at 22:20 BST (pricing issue separate from rollback, root cause: liquidity pool data). Lee: issue not reproduced in regression tests; to be fixed before next attempt. [permalink](https://mahifx.slack.com/archives/C06TW3D8NMV/p1750034584.742009)

> [resolved] 2026-06-04 — ETHUSD position rec mess; opposing LMAX/Wintermute positions while client net flat
> Large ETHUSD positions built in opposite directions at LMAX (-22.91) and Wintermute while client position netted. Multiple rounds of confusion and manual hedging. Mio/Cameron eventually got LP net = client net (-5.03) via Wintermute adjustment. Will noted hedgers should have been off during LP netting. Flagged need for ops training so Argamon can manage position transfers independently. Root cause: hedgers firing without coordination during manual position movements. [permalink](https://mahifx.slack.com/archives/C06TW3D8NMV/p1749022791.181669)

> [resolved] 2026-06-01 — XRPJPY fractional rejections at Wintermute
> Tom reported orders rejected at Wintermute due to fractional lot sizes on XRPJPY. Asked to limit to 0 dp. Liam fixed on 2026-06-01. [permalink](https://mahifx.slack.com/archives/C06TW3D8NMV/p1748783970.270239)

> [resolved] 2026-06-06 — XPTUSD pricing drop; rejections on XPT
> Tom reported client unable to close XPT position, getting "Failed to find matching volume at liquidity sources for either Hedge execution or warehouse VWAP determination". Amir added UBS for XPT pricing; resolved 2026-06-06. [permalink](https://mahifx.slack.com/archives/C06TW3D8NMV/p1749218740.013189)

> [resolved] 2026-05-25 — Beeks connectivity outage: DNS/public internet broken on trading-1 and trading-2
> Daria reported DNS/public internet broken on trading-1 and trading-2 overnight 2026-05-25/26. Cross-connect still working. Wintermute, LMAX direct, and HRP drop copy went down. Crypto failed over within OZ. Beeks fix took ~2h (ticket NOCINT-710359: "change over the weekend affected outbound public connectivity"). Isaac restarted HRP drop copy and all connections restored. [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1748217445.854529)

> [resolved] 2026-05-23 — Crypto over-hedging: hedged volume ~2x client volume on XBTUSD
> Andrew/Cameron identified external hedging to Wintermute running at ~7.8M vs 3.9M internalised client XBTUSD flow — approx 2x ratio. Root cause: over-active Broker-Wintermute-FASTERx500% rule in LMAX execution rules, combined with delayed dynamic broker hedging rules double-firing. Over-active rule and delayed rule removed 2026-05-23. Execution rule renamed from "Internalise all flow" to "broker" (Spotex flow already brokered per prior Elan config change). [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1748012505.591119)

> [resolved] 2026-05-15 — TOA feed causing 2-min ArgamonPrices FIX session delays; feed stopped
> Andrew noticed 2-min delays on ArgamonPrices FIX session tracing to TOA feed. Decision to stop TOA feed and delete signalProcess1 from hiera. XRP and XLC hedging moved back from Toa to standard Wintermute/LMAX rules (Isaac, 2026-05-15). Toa has open Binance positions (XBT/XLC) requiring unwind before full removal — Argamon asked to close out Toa-side positions. Now being reintroduced as primary crypto hedge venue (see 2026-07-02 entry). [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1747319708.454189)

> [resolved] 2026-05-14 — Retail distribution process outage; ILS rates missing; PnL frozen
> Isaac flagged retail distribution process issues ~22:30 BST (hazelcast error on trading-1 after restarts). Resolved ~22:42. Separately, Andrew noticed Retail Time PnL frozen since 10am: ILS rates missing caused PTR_BYPASS_HOUSE NaN PnL; restored at ~21:25 BST by Andrew. Could not price XAGAUD or USDHUF until EOD next day — flagged for failover by Isaac. riskReportingExtended1 needed defaultClientPriceMarket set to CLIENT_PRICE_RETAIL_NYC. Also: Finalto internal latencies to pricer1 were 5+ seconds that day (Finalto-specific, not Argamon). [permalink](https://mahifx.slack.com/archives/C06TW3D8NMV/p1747258475.449559)

> [resolved] 2026-05-01 — XAUUSD retail losses from sharp/sniping flow; DFSN signal added; signal-follow whitelist cleaned
> Isaac identified XAUUSD retail losses from 2026-04-30 caused by signal-follow clients sniping sharp moves in pricing. Affected counterparties moved back to broker-only classification (signal-follow whitelist cleaned). DFSN signal rule added to the pricing model to widen Mahi out of the way during large moves. Separate from but related to the CME hedging brokering test (2026-04-28 open issue). [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1746063187834529)

> [resolved] 2026-05-01 — Wide spread on majors (~15:00 BST); LR kicking in on published rate
> Tom flagged EURUSD at ~20 ticks wide for a couple of hours with no client complaints yet. Will identified LR kicking in on the published rate — removed from published, spread immediately restored. [permalink](https://mahifx.slack.com/archives/C06TW3D8NMV/p1746107990556329)

> [resolved] 2026-05-01 — JPY crypto LMAX position risk at rollover (non-issue)
> Tom wanted LMAX removed from JPY crypto hedging/STP ahead of anticipated large JPY financing charge at rollover. Amir confirmed with Isaac that JPY crypto pairs are weekend-only for hedging and are not STP'd — no position should build regardless. No config change needed. [permalink](https://mahifx.slack.com/archives/C06TW3D8NMV/p1746087135603309)

> [watching] 2026-04-28 — XAUUSD brokered counterparties expansion to test CME hedging
> Daria added counterparty 104881 to be brokered to Toa, working through softest first (104881, 105048, 105153, 105681, 105773) to evaluate whether hedging XAUUSD to CME helps. No further updates captured in this window. https://mahifx.slack.com/archives/C06U76A7ZJR/p1777335260425589

> [resolved] 2026-04-22 — XAUUSD signal switched synapse → neuron
> Shyam moved XAUUSD from synapse to neuron model to reduce spiky pricing; also cited better skew PnL over the last month. https://mahifx.slack.com/archives/C06U76A7ZJR/p1776832052585769

> [watching] 2026-04-20 — USDCAD ask-price spike, over-weighting HSBC mid
> Tom flagged order 012dr52nxnb filled at 1.371 while market was around 1.370; only HSBC was deviating. Daria confirmed other mid-formation LPs were unavailable so HSBC was sole source. Tom asked Elan re. adding COMZ and other LPs into mid. Separately, COMMERZ_FSS and UBS_2 markets were removed from config in 2026-06-30 to reduce feed latency — mid-formation LP set question remains unresolved for USDCAD specifically. https://mahifx.slack.com/archives/C06TW3D8NMV/p1776694811277649

> [resolved] 2026-04-21 — EURHUF indicative pricing; Commerz added
> Daria flagged EURHUF going indicative on/off (2026-04-17), proposed adding LPs into price formation just for that pair. Tom preferred Jane St + Commerz. Shyam added Commerz on 2026-04-21; backtests showed it stops the indicative pricing. https://mahifx.slack.com/archives/C06TW3D8NMV/p1776394647886729

> [open] 2026-04-15 — DB filtered out for small-ticket FX brokering (NWPB min size)
> Tom queried order 012dr82osqn filling via UBS not DB despite both being highlighted. Isaac explained DB was filtered because client order was 5k vs the 15k min-ticket on Mahi's NWPB FX hedger config. James noted Natwest has min ticket sizes and that work with Reactive on a direct setup will remove the constraint. Tom raised whether a 15k floor is justifiable for small-volume auto-brokered clients. Reactive direct setup advancing: as of 2026-05-07 Amir bounced arb/hybridHedger1 to remove 26DEGREES from insti hedging, FSS markets added to pricing (2026-05-06). HRP mapping for Reactive streams being worked through with Isaac (2026-06-09). https://mahifx.slack.com/archives/C06TW3D8NMV/p1776233897732439

> [resolved] 2026-04-13 — Missed give-up to HRP (3 EURUSD trades, one not given up)
> Levi reported HRP saw only 2 of 3 trades give up; HRP manually booked the missing one. Daria pulled the FIX AE messages — all three appear to have been sent from Mahi side. Tom said he'd check with HRP; no further messages, treating as resolved on Mahi side. https://mahifx.slack.com/archives/C06TW3D8NMV/p1776034785118149

> [resolved] 2026-04-13 — First-5min market-open EXPIRED / REJECTSYSTEMERROR RAT bursts
> Levi flagged a quantity of rejected orders at market open. Daria identified cancels/rejects clustered after the first 5min, particularly AUDCAD CAD crosses; brokering rules cancelled them because market data wasn't being received yet (Jane Street AUDCAD MD started at 21:10). RATE_LIMIT_EXCEEDED was hit due to retries — 150 orders/sec/counterparty cap. https://mahifx.slack.com/archives/C06TW3D8NMV/p1776049759858249

> [watching] 2026-04-13 — Wide pricing persisting > 1h after rollover
> Tom raised wide pricing in the post-rollover hour, asking for any improvements. No response captured in the window. https://mahifx.slack.com/archives/C06TW3D8NMV/p1776042834123209

> [open] 2026-04-13 — Centroid LDN distribution backpressure (~10s delays)
> James dug in: Centroid backpressuring (TCP rx window shrinks, zero-window notifications on port 4047, retransmissions on 4031), causing queue on Mahi side. Centroid consume snapshots not increments which compounds at high msg rates. ECB-speech burst hit ~5,000 FIX msgs/sec across both pricing sessions, more than Centroid's receive buffer could drain. Mahi-side publish latency was fine (~0.065ms mean). Now additionally: Argamon migrating from OneZero to Centroid (pre-Aug 2026-08-01) — new retail and crypto Centroid sessions being set up. Centroid test trades on 2026-05-28 hit REJECT_SYSTEM_ERROR due to FIX tag ordering issue (447/448/452 vs 453); Centroid said tags cannot be configured server-side. Resolved via tag 109 for client ID (confirmed working 2026-06-05). https://mahifx.slack.com/archives/C06U76A7ZJR/p1776116671694999

> [resolved] 2026-04-08 — NY4 → CHI brokering live
> Daria flipped on brokering to CHI from NY4. Watching for orders from the counterparties Elan selected. https://mahifx.slack.com/archives/C06U76A7ZJR/p1775686974874039


## Notable topics

- OneZero → Centroid migration underway (pre-2026-08-01 deadline). Retail and crypto Centroid channels being set up by Isaac. Centroid FIX tag ordering issue resolved (tag 109). Insti NOT going via Centroid — Elan decided against due to Natwest drop copy delays (5 months); moving to Lucera instead.
- Lucera maker integration: Lucera conformance complete as of 2026-06-27. Maker session to hedge via Natwest being set up. This is the strategic insti connectivity path replacing Centroid for insti flow.
- Crypto hedge venue migration: XBT/XET/XRP/XLC moving to Toa/Binance as primary hedge venue. LMAX and Wintermute being wound down for crypto via LPR rules. Requires Argamon to add Binance collateral. TOA feed was stopped 2026-05-15 due to 2-min FIX delays; being reintroduced now as deliberate migration.
- Currency pair rec breaks (JPY, AUD) are a major active issue. Significant position drift between Argamon and Mahi systems. Joint investigation ongoing. P&L impact of adjustments to be discussed with Elan/Jonah.
- LP feed trimming: COMMERZ_FSS and UBS_2 markets removed 2026-06-30 to reduce latency. JPM_INST removed from EURUSD/USDJPY mid formation 2026-05-07. _2 duplicate feeds being pruned. FSS markets added to pricing.
- Mid-formation LP set: COMMERZ_FSS removed; USDCAD mid-formation LP gap (HSBC sole source issue) unresolved for that specific pair.
- ACG onboarded as Argamon sub-client (INST-26). Routing fix needed (A_CLIENTS → insti connection). Sub3 not Sub1.
- Reactive direct setup still in-flight for NWPB (Natwest) min-ticket-size remediation. HRP mapping for Reactive streams being worked through.
- Crypto over-hedging resolved (2026-05-23) — over-active delayed dynamic broker hedging rules removed. Position recs now routine but require frequent manual intervention.
- Counterparty 84004149 (crypto, large): discussed for potential SI — Andrew flagged as up ~$200k, consistently profitable on long holds. Isaac noted flow switches between B-book-friendly and sharp week-to-week. Still on brokered LR on retail book per Amir (2026-05-15).
- Brokered LR added to clientDist1 and EURUSD retail signal response reduced (Amir, 2026-05-15).
- XTX cross-connect being set up at Beeks (2026-06-27), brief outage expected.
- compassDB slow queries: Argamon's daily EOD rec query was hitting 30s timeout. Justin bumped to 240s (2026-06-27). Larger question of whether to grant HouseOrder/ExternalOrder table access (Pulse contract implication) raised by Liam — no resolution captured.
