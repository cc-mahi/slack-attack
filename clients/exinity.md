---
slug: exinity
refs:
  vibepulse: ../VibePulse/.claude/clients/exinity.yaml
  billing: ../MahiProduct/data/billing/clients.json     # entry: exinity
  hosts: ../MahiProduct/data/client-hosts.json          # entry: exinity
  wiki: null                                             # ../MahiProduct/wiki/clients/exinity.md (not yet)
channels_override: null
key_people_overrides:
  - {name: "Marianna Konstantinidi", role: "head of trading / primary technical counterpart (MK)"}
  - {name: "Oliver Ryan", role: "trading ops — A-book / brokerage queries (leaving Exinity for Rostro, date TBC)", confidence: low}
  - {name: "Justin", role: "Exinity exec — CFD licence / commercial decisions", confidence: low}
  - {name: "Louie Davidson", role: "ops / order-trace investigations", confidence: low}
  - {name: "Samuel Ewebiyi", role: "ops — distribution / risk-splitting config", confidence: low}
  - {name: "Mukhammad Khamidov", role: "trading ops — Wagyu metals pricing/spreads", confidence: low}
  - {name: "Daniel Kurra", role: "trading ops — pricing channels / hedger config", confidence: low}
  - {name: "Keshav Woottum", role: "ops — alerts/reporting cadence", confidence: low}
  - {name: "George Moore", role: "ops — UBS / Jane Street test-trade liaison", confidence: low}
  - {name: "Christian Lee", role: "ops — house position / book break investigations", confidence: low}
last_catchup: 2026-05-13T07:23:31Z
---

## Recent issues

> [open] 2026-05-13 — Wagyu XAU spreads 50-60c wide at SGP open: arb protection config tweak applied
> Mukhammad reported Wagyu XAU spreads running 50–60c after open (twilight target 35c, SGP target 19c). Daria diagnosed: widening driven by arb protection, not MWMS multiplier. Applied a 10c buffer either side of the arb protection reference (UBS|360T|SUCDEN) to allow the model to sit tighter. Spreads reduced to 25–40c. Mukhammad to confirm after twilight whether to revert or keep the buffer permanently. Daria noted the buffer is only active during twilight under current config. [permalink](https://mahifx.slack.com/archives/C0456LSHQQK/p1778624005963899)

> [open] 2026-05-12 — XAU HOUSE positions at Invast/LMAX: Compass exposure not matching LP
> Samuel asked why Compass shows XAU positions going to Invast under HOUSE with no corresponding LP position and no order events. Daria traced: the discrepancy stems from manual adjustments — one on 05-07 and another more recent manual adjustment. Samuel also flagged that LMAX XAU exposure in Compass appears double what the LP shows (expected 2014oz, Compass shows ~2x). Daria suggested it may be part of the same set of adjustments and was looking into it as of end of window — no final confirmation of resolution. [permalink](https://mahifx.slack.com/archives/C0456LSHQQK/p1778553846921779)

> [resolved] 2026-05-11 — Velocity XFM unhandled fill alert: manual position adjustment
> Inald Gjoni alerted on `FAILED TO PROCESS FILL FOR UNKNOWN ORDER - MANUAL BOOKING REQUIRED` for 2 lots XFM/USD @ 4679.7 on VELOCITY (MarketTradeId: VR6A00F287001699E.1). Inald asked Louie to confirm whether Velocity executed it. Louie confirmed: filled on Velocity's side — he had made a manual position adjustment to fix a client/insti→LP discrepancy. No Mahi action needed. [permalink](https://mahifx.slack.com/archives/C0456LSHQQK/p1778502206747279)

> [resolved] 2026-05-11 — B-book Compass homepage: -$250K reval at 21:00 UTC Sunday
> Matthew Ayub flagged the B-book graph showing a ~$250K drop at Sunday 21:00 UTC then recovery on gold/indices open. Nathan explained: weekend price gap at market re-open — GBP balance in B_CLIENTS_NET was £16.77M; GBPUSD dropped 71.8 pips from Friday close to Sunday open (~-$120K contribution), plus adverse AUD/EUR/CO1 weekend moves. Metals then recovered, and CO1 drove the subsequent upswing. Normal reval behaviour, no system issue. [permalink](https://mahifx.slack.com/archives/C0456LSHQQK/p1778457525066839)

> [resolved] 2026-05-10 — Hazelcast cluster stale error alert (admin-1 / trading-1 brief disconnect)
> Samuel flagged a Hazelcast heartbeat error on Compass. Sam Hewitt traced: on the morning of 09-May, admin-1 and trading-1 briefly lost connection, triggering an error alert that Compass had not auto-cleared even after the cluster recovered. Servers reconnected automatically; no operational impact. Alert cleared by Sam Hewitt. [permalink](https://mahifx.slack.com/archives/C0456LSHQQK/p1778447962243699)

> [open] 2026-05-07 — LMAX XAUUSD lot-size mismatch: Compass qty vs LMAX contract size
> Louie flagged urgent: a 30oz close at LMAX appeared as 3 lots (10x under), and a 10-lot client buy was reflected as 20 lots at LMAX (10x over). Kate explained Compass sends raw FX quantity and LMAX multiplies by its 10oz contract size (config shows `contractSize=10`). Compass quantities are in oz. The two examples appear to represent the same misalignment from opposing angles. Kate offered a call to resolve. No confirmation from Louie that the discrepancy was understood/fixed as of end of window. [permalink](https://mahifx.slack.com/archives/C0456LSHQQK/p1778164543303029)

> [resolved] 2026-05-07 — analyticsFixServer1 5001ms latency alerts (FX_MT4_ECN_ZEROTrades, FX_MT4_CENT2Trades)
> Keshav alerted on `analyticsFixServer1 MahiFXMT4Bridge >>> recv FX_MT4_ECN_ZEROTrades: Incoming FIX message 5001ms latent` on 05-07, then raised again on 05-08 for `FX_MT4_CENT2Trades` at the same time of day — concerned about back-to-back alerts on different connections. Daria confirmed same explanation for both: analyticsFixServer1 is the internal trade analytics bridge (dropcopy for reporting, not in the execution path), so latency here affects only yield profile reporting, not trade execution. Cameron Hughes acknowledged and said they'd check. No action needed on either. [permalink](https://mahifx.slack.com/archives/C0456LSHQQK/p1778268117987849)

> [open] 2026-05-06 — A-book client XAGUSD routing: HR LPs today vs Invast yesterday
> Louie asked why A-book client `ASV_MT5_228041520` was executed at HR LPs on 2026-05-06 but Invast the day before. Kate traced: a new execution rule `HRP Abook Counterparties (lime)` was created on 2026-05-05 and routes to `LIQUIDITY_POOL_LDN`, whereas yesterday's trades used `Abook Counterparties (lime)` routed to `HEDGING_POOL_LDN`. Kate confirmed the routing is working as the new rule intends; Louie had not replied confirming acceptance as of end of window. [permalink](https://mahifx.slack.com/archives/C0456LSHQQK/p1778082430.457469)

> [resolved] 2026-05-06 — Big House 20% coefficient — B-book PnL confirmation
> Louie asked whether the 80% remainder of client PnL (from two Big House tags each with 20% coefficient) is correctly reflected in B-book PnL. Rory confirmed yes — the 80% remainder is correctly in B-book. [permalink](https://mahifx.slack.com/archives/C0456LSHQQK/p1778060955.121419)

> [resolved] 2026-05-05 — 360T EURUSD A-book position trace (3 Feb 2026)
> Louie followed up on an outstanding query about a 360T EURUSD position executed on A-book on 3 Feb 2026. Kate traced via Compass: Matthew placed two 500k EUR/USD sells at 07:21:58 and 07:22:05 UTC into `CLIENTS_HEDGING` (360T refs `HL69811F160004737.1` and `HL69811F160004754.1`). Louie acknowledged and closed off. [permalink](https://mahifx.slack.com/archives/C0456LSHQQK/p1777971709952829)

> [resolved] 2026-05-05 — XAU/USD 360T limit order cancels ("expired") — offside limit price
> Louie reported XAU/USD limit orders to 360T returning "expired" with no LP cancel reason in FIX logs. Kate reviewed TOB at trade time: orders were sent at LP's bid price rather than the offer (offside limit). Advised Louie to adjust the limit price and confirm with 360T. Louie confirmed they are adjusting limit order room; confirmed the same issue occurred the previous day. [permalink](https://mahifx.slack.com/archives/C0456LSHQQK/p1777993658873589)

> [resolved] 2026-05-03 — EXINITY_ECN FX minor rejects on Singapore Monday open
> Mukhammad Khamidov reported noticeable rejects on FX minors shortly after market open. Nathan Burch diagnosed: EXINITY_ECN channel has WSS configured to go indicative during Singapore Monday (`SingaporeMonday` timezone); when CLIENT_PRICE crosses the threshold (e.g. 0.00633 for GBPNZD), distribution price goes indicative and trades reject. Client acknowledged and elected to keep the config as-is; will discuss internally if adjustment needed. [permalink](https://mahifx.slack.com/archives/C0456LSHQQK/p1777846525218399)

> [open] 2026-05-01 — BIG_INSTI_HOUSE position break: 20L DOWFUT-M / 20S DOWUSD
> Christian Lee (Exinity ops) reported a DOWFUT-M vs DOWUSD mismatch in BIG_INSTI_HOUSE with no visible root cause on their side. Rory King (Mahi) traced it: counterparty MT5_111000009 executed back-to-back futures+spot trades on 2026-03-17 at 13:42 UTC — bought 20 lots DOWFUT-M (Jun futures) and sold 20 lots DOWUSD (spot CFD) within 16 seconds into BIG_INSTI_CLIENTS book, creating the persistent house position. Subsequent 23–26 March DOWFUT-M activity netted to zero. Louie asked whether zeroing BIG_INSTI_HOUSE positions would impact other books; Rory confirmed BIG_INSTI_HOUSE adjustments are isolated (child books only, no impact to Big House / B Insti House etc). As of end of window Louie had not confirmed the fix was applied. [permalink](https://mahifx.slack.com/archives/C0456LSHQQK/p1777632218017979)

> [open] 2025-07-07 — CFD licence (Addendum 5) under commercial review — client says unviable
> Justin (Exinity exec) messaged Nicola requesting a call "early next week" to discuss Addendum 5: "this addition is currently unviable as an offering (for the last few months we have lost money)". Andrew/Nicola discussed internally: need profitability review (actual vs potential value-add if tuned), roadmap, and risk mgmt assessment. Notice period is 1 month per main agreement. Exinity on a multi-year contract for core services; CFD is Addendum 5 only. Call not yet confirmed as of this window. [permalink](https://mahifx.slack.com/archives/C040V9LNKT5/p1751880944781859)

> [open] 2025-06-09 — AWS→Beeks ip route not persisting post server migration
> Post-migration (17/18 May), the route `10.42.48.0/23 via 172.16.17.1` keeps dropping on reboot. Isaac ran `ip route add` manually on 2025-05-26 and again on 2025-06-09; Liam thought he'd fixed it permanently but hadn't. Liam asked Hussain in #dev-infra to investigate. Recurring outage risk for Exinity→AWS connectivity. [permalink](https://mahifx.slack.com/archives/C040V9LNKT5/p1748217672472889)

> [open] 2025-06-09 — FI PnL reporting inaccuracies — riskReporting1 on admin box (Zendesk 20871)
> MK frustrated for 2+ months re: FI PnL figures (especially XAUUSD, USDJPY, EURUSD spikes not matching backtests). Root cause: `riskReporting1` on admin server introduces latency vs trades/pricing on trading boxes, producing spurious spikes/drops. Liam moved riskReporting1 to trading box on 2025-06-09. Cameron ran backtests showing true FI PnL significantly higher than reported (e.g. full wk 2 Jun: backtest ~$76.8k vs reported lower). MK still not satisfied with revised figures as of 2025-06-17; ongoing. Separately, USDJPY FI PnL artifact explained by Liam: RHS-tracked PnL revalued to USD via live USDJPY rate, causing apparent swings with no trading — fix planned (track in USD from trade time). [permalink](https://mahifx.slack.com/archives/C040V9LNKT5/p1749541669220569)

> [open] 2025-05-25 — Post-server-migration connectivity: Wagyu/Chuck/Fillet FIX sessions down; PXM Insti on failover
> Migration weekend 17/18 May mostly successful (DB, config, infra). Immediately post-migration: proxies from Exinity to Beeks broken (AWS route missing — see ip route entry above), fixDropCopyGateway1 not connected, PXM Insti connections down (Exinity using "not a great" failover feed). Wagyu/Chuck/Fillet FIX sessions also not connecting on 2025-05-25 due to IP changes (same aws route issue). Dists back to echo/compass confirmed restored 2025-05-29. FIX sessions status unclear beyond that window. [permalink](https://mahifx.slack.com/archives/C040V9LNKT5/p1747605219503169)

> [open] 2025-05-07 — hybridHedgerSI1 volume breach → 170k PnL drop; risk-splitting rule fix needed
> hybridHedgerSI1 breached $250m/hr limit (same as prior incident), died at ~16:35 UTC. Kate diagnosed: two ASV counterparties (ASV_MT4_STANDARD1_236001796, ASV_MT4_STANDARD1_144171674) traded AUDCHF — hitting the generic off-book split rule rather than their cpty-specific SI-book rule; risk held in off-book 10 mins, transferred to SI book while offside, hedger then died mid-hedge. Loss ~170k on the drop + lock-in on hedging. Limit bumped 250m→300m immediately; MK later requested 500m (agreed, requires restart), then 600m/hr (agreed 12 May). MK to fix cpty-specific risk-splitting rule order so AUDCHF skips off-book for these cptys. Internal: Andrew flagged volume limits may be counterproductive at default levels; Kate agreed clients should be aware and able to waive. [permalink](https://mahifx.slack.com/archives/C040V9LNKT5/p1746636145861299)

> [resolved] 2025-05-05 — VELOCITY_DEFENSIVE subscription symbol change causing rejects
> MK flagged rejects on `VELOCITY_DEFENSIVE` market after subscription symbol change; asked to prioritise investigation. Kate responded the same morning: "all good to ignore — have fixed, only needed an order process bounce". [permalink](https://mahifx.slack.com/archives/C0456LSHQQK/p1746439309559879)

> [resolved] 2025-05-01 — EXINITYCONNECTCHUCK-MD FIX session disconnect
> Matthew Ayub (Exinity) reported urgent FIX session alert for EXINITYCONNECTCHUCK-MD. Daria checked: connections timed out waiting for heartbeat, logon not re-attempted. PXM confirmed issue on their side; resolved shortly after. [permalink](https://mahifx.slack.com/archives/C0456LSHQQK/p1746079067640769)

> [resolved] 2026-04-30 — CPL pricing outage: Xenfin NOP concentration limit → one-sided MD
> Oliver Ryan reported dashboard not updating and 34 critical errors; Client Price London had no pricing. Mahi diagnosed: all Xenfin inbound MD feeds went one-sided. MK later confirmed: hit AUD concentration limit at Xenfin → feeds went one-sided → CPL lost pricing for multiple assets. Mahi added LMAX temporarily to restore CPL. Kate (internal): Xenfin has a setting where hitting NOP → one-sided, cannot be turned off but they'll alert Exinity if it happens again. Config reverted once PXM stable. Amir flagged LMAX as a permanent backup reference market to mitigate single point of failure. [permalink](https://mahifx.slack.com/archives/C0456LSHQQK/p1746021050790359)

> [resolved] 2026-04-27 — Risk-splitting config not routing 3 counterparties to BIG_CLIENTS_LDN
> Samuel: trades for `FX_MT5_LIVE01_231010816`/`…013379`/`FX_MT4_ECN_118002061` landing in `B_Clients` not `BIG_CLIENTS_LDN`. Kate found two issues: a whitespace before the cpty ID in the riskSplitting config (Daniel had already fixed) and the `EXINITY_ECN_XAUUSD` channel missing from the config. Kate added `EXINITY_ECN_XAUUSD` + EURUSD subchannel; resolved 04-27 10:52 BST. [permalink](https://mahifx.slack.com/archives/C0456LSHQQK/p1777257377985069)

> [resolved] 2026-04-26 — Connect_Wagyu metals: spot XAG not ticking + XAU spreads wide (60c)
> XAG ticking restored within minutes. Daria noted XAU 60c was the configured Twilight base spread (vs 19c during other timezones); offered to add a 19c tier at 100, but Mukhammad opted to wait it out since Twilight was ending — closed without changes to base config. [permalink](https://mahifx.slack.com/archives/C0456LSHQQK/p1777241318800319)

> [open] 2026-04-27 — Wagyu XAU client-perceived spread vs published TOB
> Samuel: TOB shows 30–35c with 20q layer since open, but clients reporting wider spreads. Daria: in line with what we publish on the channel — possible additional markup downstream. Awaiting client investigation. [permalink](https://mahifx.slack.com/archives/C0456LSHQQK/p1777328307964599)

> [open] 2026-04-28 — XRPUSD rejects on EXINITY_PROECN_ARU — visible quantity too low
> Louie: 1 cpty getting continuous ripple rejects; visible quantity on the channel substantially lower than CLIENT_PRICE_RETAIL. Kate temp-increased visible qty; XRPUSD-specific override pending to bring channel in line with model liquidity. [permalink](https://mahifx.slack.com/archives/C0456LSHQQK/p1777398508607609)

> [open] 2026-04-28 — Big Hybrid Hedger LDN: XAUUSD rejects to Invast
> Mukhammad reported rejects on XAUUSD trades sent to Invast under BIG_HOUSE. Sam couldn't see a Mahi-side cause; asked Mukhammad to check Invast for cancels on their end. Awaiting client. [permalink](https://mahifx.slack.com/archives/C0456LSHQQK/p1777338900259439)

> [open] 2026-04-30 — DOWUSD trades filled at LP price not Dist (Dynamic Arbitrageur profile)
> Samuel asked why DOW trades for cpty `ASV_MT5_228023951` executed at LP price. Sam: cpty was assigned the Dynamic Arbitrageur execution profile on 04-27 (day of the trades), so filled on `CONTINUITY_POOL` which publishes VELOCITY for DOWUSD. Samuel asked when client was added — clarified, but assignment context (who/why on 04-27) not surfaced. [permalink](https://mahifx.slack.com/archives/C0456LSHQQK/p1777514645330979)

> [open] 2026-04-27 — "Poor $/M report" alert frequency too high since update
> Keshav: receiving multiple alerts in short windows; asked for one-per-minute throttle. No reply visible — outstanding. [permalink](https://mahifx.slack.com/archives/C0456LSHQQK/p1777290223832409)

> [open] 2026-04-23 — Account ASV_MT5_228000145 missing info + no distribution trace
> Louie flagged the account is missing information in Compass and has no distribution trace for the last 24h window; William Denny to investigate. [permalink](https://mahifx.slack.com/archives/C0456LSHQQK/p1776974117585849)

## Notable topics

- 2025-07-07 — Oliver Ryan confirmed leaving Exinity for Rostro (following Sammy). MK described as "gutted" about it. Impact on ops/brokerage coverage unclear. [permalink](https://mahifx.slack.com/archives/C040V9LNKT5/p1750751779254969)
- 2025-06-24 — Large manual client-side position adjustment overnight: 2.71k lots XAUUSD + other instruments; caused 73k VaR swing and 68k PnL impact. Isaac flagged internally; Will told him to ask Exinity directly in future. [permalink](https://mahifx.slack.com/archives/C040V9LNKT5/p1750724808033969)
- 2025-06-03 — SI_HEDGING_MODEL_ARB and SI_INSTI_HEDGING_MODEL_ARB confirmed inactive — arb config commented out in hiera. Will flagged for check with MK; not rectified in this window. [permalink](https://mahifx.slack.com/archives/C040V9LNKT5/p1748935853984529)
- 2025-05-16 — A-book price improvement misunderstood: Oliver raised that client wasn't getting LP fill price on A-book execution; Cameron clarified price improvement must be explicitly enabled for client to benefit — previously off, so Mahi was capturing the improvement. Oli enabled it. MK reacted "ouf". [permalink](https://mahifx.slack.com/archives/C0456LSHQQK/p1747396450537129)
- 2025-05-13 — New LP connection (Wintermute second connection, Tokyo) being set up; Andrew noted 16.5-second delays on wmtprc feed from Wintermute TKY, flagged as interfering with upsell and causing crossed prices in echo. Liam to get Amazon Fabric quote for TKY→LD5 for better crypto routing. [permalink](https://mahifx.slack.com/archives/C040V9LNKT5/p1747321167620639)
- 2025-05-02 — Signal architecture consolidated: signal processes now have 4 publish lists (price, flow, tightening, widening) via multi-CEP. Signal2 process removed as redundant. [permalink](https://mahifx.slack.com/archives/C0456LSHQQK/p1746175471569169)
- 2025-05-02 — Compass release (w/e 3 May): performance/stability enhancements; key item: crossover precision support to 9dp on orders (for Aeron re-enablement without order rejections). Not yet switched on as of release date. [permalink](https://mahifx.slack.com/archives/C0456LSHQQK/p1746192208793839)
- 2025-05-01 — $23M additional spread revenue at Exinity noted by Andrew (2-year cumulative B_CLIENTS lifetime PnL). SI RoS 171%; SI Insti flagged anomalously high at 6,345% — suspected reporting artefact. [permalink](https://mahifx.slack.com/archives/C040V9LNKT5/p1746116025826429)
- 2026-05-07 — Louie requested client simulations from trading data (Athens UTC+3 timezone). Kate confirmed. [permalink](https://mahifx.slack.com/archives/C0456LSHQQK/p1778141520510569)
- 2026-05-07 — Kate bounced `hybridHedgerBigBook1` (internal note only; no client-facing context surfaced). [permalink](https://mahifx.slack.com/archives/C040V9LNKT5/p1778161010370699)
- 2026-05-07 — Andrew deployed an analytics component referencing Zendesk 22880 (no thread context). [permalink](https://mahifx.slack.com/archives/C040V9LNKT5/p1778177980786529)
- 2026-05-12 — UBS FA session: Maten Rehimi confirmed FIX adapters not yet built; had emailed wrong UBS address (FX-ClientDelivery@ubs.com). George Moore chased; UBS Jan replied directing to FRECommerce@ubs.com for UAT/PROD and supplied a conformance test sheet to fill in before production go-live. George forwarded to UBS/Exinity chain. [permalink](https://mahifx.slack.com/archives/C0456LSHQQK/p1778584018956889)
- 2026-05-12 — Second client simulation request (Keshav, GMT+3 data): Nathan confirmed will run. Follows Louie's 2026-05-07 simulation request. [permalink](https://mahifx.slack.com/archives/C0456LSHQQK/p1778619941428319)
- 2026-05-06 — UBS FA session setup: partial-fill risk + £99 cross-connect confirmed. Kate flagged Compass has no guarantee of full-amount delivery on FA sessions (sweep across multiple venues possible). Nick Serff confirmed £99/mo Beeks shared cross-connect is fine; Kate clarified the sweep caveat; Nick's final confirmation on whether to proceed under those conditions not yet received as of end of window. [permalink](https://mahifx.slack.com/archives/C0456LSHQQK/p1778072525.036309)
- 2026-04-29 — UBS reply turnaround flagged by George Moore — Kate apologised for delay, awaiting Charlie's reply; FRCeCommerce@ubs.com supplied as direct route to UBS FRC team. Internal Daria review (04-30): 3 issues escalated, first two looked into, third (this UBS one) was missed — flagged so client could've followed up sooner. [permalink](https://mahifx.slack.com/archives/C0456LSHQQK/p1777446054108019)
- 2026-04-28 — Exinity / Jane Street test-trade meeting confirmed for 04-29 15:00 UK. [permalink](https://mahifx.slack.com/archives/C0456LSHQQK/p1777378983947659)
- 2026-05-01 — Nick (Nicola) in Singapore 11–15 May for Finance Magnates expo; any calls requiring her will need scheduling around that window. [permalink](https://mahifx.slack.com/archives/C040V9LNKT5/p1777621042911649)
- 2026-04-30 — Latency notifications (Samuel) traced to a heartbeat received latent from non-Mahi side; Isaac suspects one-off, will recheck Mahi-side latency around the time. [permalink](https://mahifx.slack.com/archives/C0456LSHQQK/p1777510067154679)
