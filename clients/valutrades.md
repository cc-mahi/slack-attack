---
slug: valutrades
refs:
  vibepulse: ../VibePulse/.claude/clients/valutrades.yaml
  billing: ../MahiProduct/data/billing/clients.json     # entry: valutrades
  hosts: ../MahiProduct/data/client-hosts.json          # entry: valutrades
  wiki: null                                             # ../MahiProduct/wiki/clients/valutrades.md (not yet)
channels_override: ["internal-valutrades", "mahi-valutrades", "mahi-valutrades-operations"]   # -operations is a distinct operations channel not in VibePulse yaml
key_people_overrides:
  - {name: "Andri", role: "client trading ops — algo connections, rejects", confidence: low}
  - {name: "Neil Whitehead", role: "client data/tech — backtesting, MySQL/Pulse queries", confidence: low}
last_catchup: 2026-05-11T09:53:48Z
---

## Recent issues

> [open] 2026-05-11 — Compass receiving unsubscribed market data — full market config requested, unanswered
> Daria Horton flagged that Compass is receiving market data it's not subscribing to, and listed the current mapping: MFX-IG_Q→ValuCY_Live_Q with JFX_VALUTRADES-SW-NY4; MFX-FEED4_Q→ValuCY_Live_Q with Valutrades, LMAX-ValutradesNWtk1, Currenex-Valutrades, JUMP-CFD, JumpMakerValutrades, Velocity, JFX_VALUTRADES-SW-NY4, Commerz-Valutrades. Client followed up at 08:25 asking Daria for the full configured market list — unanswered. [daria-flag](https://mahifx.slack.com/archives/C09HN93T0G2/p1778465858044369) [client-followup](https://mahifx.slack.com/archives/C09HN93T0G2/p1778484353813979)

> [open] 2026-05-10 — Client requested gateway disconnect check — clarification pending
> Client (Brandon) asked Mahi to confirm gateways were disconnected. Nathan Burch replied at 21:34 asking Brandon to confirm which connections he saw as disconnected and whether they remain disconnected. No client reply in window. Earlier (17:58) client also sent an unthreaded message: "Sorry if not bounced already please bounce before the market open" — no Mahi reply visible. [gateway-request](https://mahifx.slack.com/archives/C09HN93T0G2/p1778390311600029) [bounce-request](https://mahifx.slack.com/archives/C09HN93T0G2/p1778432301421509)

> [resolved] 2026-05-11 — cpty 89468240 A/B book classification query (mahi-valutrades)
> Client asked overnight for book classification on cpty 89468240. Nathan Burch checked and confirmed B-book (with chart). Client thanked. [client-query](https://mahifx.slack.com/archives/CSLM3Q8AD/p1778478084784169) [nathan-reply](https://mahifx.slack.com/archives/CSLM3Q8AD/p1778478527256749)

> [resolved] 2026-05-08 — cpty 77008554 A/B book classification query (mahi-valutrades)
> Client asked team to advise on cpty 77008554; Daria replied "Hey overnight, A book" with two charts. Client acknowledged ("thanks"). [client-query](https://mahifx.slack.com/archives/CSLM3Q8AD/p1778219665733729) [daria-reply](https://mahifx.slack.com/archives/CSLM3Q8AD/p1778220819121709)

> [open] 2026-05-07 — `valu.user` DB access denied on 43.218.202.79 — unanswered
> Client reported `Error: 1044 (42000): Access denied for user 'valu.user'@'43.218.202.79' to database 'PROD_LIVE_CLIENTDB'`. Note: this IP was whitelisted for `airflow` in the 2026-05-06 DB whitelist run (see below); `valu.user` may require separate whitelisting. No Mahi reply in window. [permalink](https://mahifx.slack.com/archives/C09HN93T0G2/p1778151018652949)

> [open] 2026-05-07 — USD volume on TT algo trades incorrect in Echo — fix in progress
> Graeme (client) chasing fix for USD volume displayed on TT algo trades in Echo. Inald replied: "we are currently working on a fix for this and should hopefully get this out soon." No ETA given. [client-chase](https://mahifx.slack.com/archives/C09HN93T0G2/p1778153944809909)

> [resolved] 2026-05-06 — Echo chart data incomplete for VALUTRADES_B_CLIENTS (ops channel) — fixed by Liam same day
> Garry Bersnov (client) had raised incomplete Echo yield-profile chart data for SPXUSD and other instruments on VALUTRADES_B_CLIENTS on 2026-04-28 (ops thread). Issue persisted after the trading-channel yield-profiles fix (2026-05-02 release); Andri chased again 2026-05-06 10:52 ("Have this been fixed?") and 11:08 ("please give a priority"). Liam replied 10:52 ("tricky to investigate"), identified the bug at 11:09 ("I think I've managed to identify the bug, just working on a fix"), deployed fix and confirmed at 14:41, corrected historic data at 20:59. Client confirmed "Looks good now" 2026-05-07 06:08. [client-chase](https://mahifx.slack.com/archives/C09HN93T0G2/p1778061150922779) [liam-fix](https://mahifx.slack.com/archives/C09HN93T0G2/p1778074877176869) [historic-fixed](https://mahifx.slack.com/archives/C09HN93T0G2/p1778097584848219) [client-confirm](https://mahifx.slack.com/archives/C09HN93T0G2/p1778130513793059)

> [resolved] 2026-05-05 — MySQL DB whitelist: new users `bpambudi` + `airflow` whitelisted 2026-05-06
> Brandon (client) requested whitelisting of `108.136.197.46` for DB access; Maten found prior whitelist but asked Brandon to clarify credentials. Brandon requested `bpambudi` (IP `108.136.197.46`) and `airflow` (private IP `10.200.1.216`); Maten suggested shared creds for bpambudi and asked for a public IP for airflow. Brandon supplied public IP `43.218.202.79` for airflow on 2026-05-06. Inald confirmed both whitelistings complete at 16:44 on 2026-05-06. [initial-request](https://mahifx.slack.com/archives/C09HN93T0G2/p1777966759391499) [resolution](https://mahifx.slack.com/archives/C09HN93T0G2/p1778082282395519)

> [open] 2026-04-30 — `riskPathValutrades` on valutrades-ny-admin-1 throwing 14k+ errors/day — `CLIENT_PRICE_ICDX_MINI_NYC` unavailable
> Justin Young investigating why `CLIENT_PRICE_ICDX_MINI_NYC` is set as `defaultClientPriceMarket` for USOUSD and a large instrument list (NDFUSD, CL1USD, CO1USD, DOWUSD, NDXUSD, JPFUSD, SPFUSD, DJFUSD, HSFUSD, SPXUSD, UKXGBP, HSIHKD, JPXJPY, G30EUR); riskPath throwing `IllegalArgumentException: CLIENT_PRICE_ICDX_MINI_NYC/<sym> unavailable` at 14k+/day. No resolution in window. [permalink](https://mahifx.slack.com/archives/CP7A1F8BT/p1777544417254539)

> [resolved] 2026-04-28 — Yield profiles negative/incorrect for cpty 92549025 — fix deployed 2026-05-02
> Garry flagged incomplete chart data for SPXUSD on VALUTRADES_B_CLIENTS (operations channel); Andri also chasing on yield profiles for cpty 92549025 in the trading channel. Issue re-escalated 2026-04-30 — still appearing on 2026-04-29 data. Justin Young confirmed fix requires a weekend release. Justin posted "Release complete" 2026-05-02 18:30 BST. [ops-link](https://mahifx.slack.com/archives/C09HN93T0G2/p1777373692703529) [trading-link](https://mahifx.slack.com/archives/CSLM3Q8AD/p1777445407538749) [re-escalation](https://mahifx.slack.com/archives/CSLM3Q8AD/p1777530647177429) [fix-ETA](https://mahifx.slack.com/archives/CSLM3Q8AD/p1777623275661629) [release-complete](https://mahifx.slack.com/archives/CSLM3Q8AD/p1777743032175839)

> [resolved] 2026-05-02 — MySQL data gap on 2026-01-30 — 6-hour window backfilled
> Neil Whitehead flagged a 6-hour gap on 2026-01-30 remaining after the earlier backfill (which covered 2026-01-01→2026-01-29). Sam Hewitt confirmed the gap is now corrected. Follow-on to the April archiver retention fix. [client-flag](https://mahifx.slack.com/archives/C09HN93T0G2/p1777750823493739) [fix-confirm](https://mahifx.slack.com/archives/C09HN93T0G2/p1777786213688159)

> [resolved] 2026-04-30 — MySQL data archiving — January ExternalOrder data backfilled, retention bumped to 365 days
> Client (Neil Whitehead) reported January data missing after archiver default changed to 90-day retention. Sam Hewitt backfilled 386,250 rows (2026-01-01→2026-01-29) from Pulse parquet into PROD_LIVE_CLIENTDB on 192.81.111.24, and bumped ORDER_HISTORY daysToRetain 90→365. Client confirmed working. [escalation](https://mahifx.slack.com/archives/C09HN93T0G2/p1777543312438289) [resolution](https://mahifx.slack.com/archives/C09HN93T0G2/p1777602765022229)

> [open] 2026-04-25 — Post-26.3 deploy: `analyticsFixServerValutradesMT4` down on valutrades-ln-trading-1
> Restart fails with `MT4/5 Analytics Order connections must have positionReportMetaTraderServer configured in their connectivity.FixTradeAnalyticsSettings`. Leonardo flagged that the analytics sessions under `connectivity.fix.outbound.session` have `FixTradeAnalyticsSettings` but no `positionReportMetaTraderServer` — asking how this should be set. No reply visible. [permalink](https://mahifx.slack.com/archives/CP7A1F8BT/p1777122260901519)

> [open] 2026-04-25 — Post-26.3 deploy: `signalProxyTx1` crashing on valutrades-ny-trading-1 — duplicate consumer
> `MarketMetaDataSubscriber.SIGNALS_NYC2: Consumer for 393 already registered: AFM-Broker. New consumer AFM-Signal` — caused by a new code default in `signalsToPublish`. Leonardo workaround: global override on `connectivity.marketData.marketMetadata.proxy.coe.signalsToPublish`; process is back up. Asked for confirmation this is the right fix or if there's a better one. [permalink](https://mahifx.slack.com/archives/CP7A1F8BT/p1777123880055949)

> [open] 2026-04-23 — Surya Strait algo connection not live — tag to send unclear
> Andri asked about connection status for the Surya Strait algo and what tag to send; Isaac + Daria investigating, Daria asked Andri to clarify which connection. No resolution visible in the 24h window. [permalink](https://mahifx.slack.com/archives/C09HN93T0G2/p1776918937609649)

> [open] 2026-04-23 — TT reject on UBS Algo Gold order — `Exceeds max product long position`
> Andri reported Gold (GCM6) algo order rejected by TT with `3: TT: Exceeds max product long position`; Kate supplied the raw FIX pair for investigation (TT_POV strategy, 162 contracts, UBS Algo cpty). Needs follow-up on position-limit config. [permalink](https://mahifx.slack.com/archives/C09HN93T0G2/p1776949025272839)

> [resolved] 2026-04-28 — TT POV algo: gold time-window changed to 120 min
> Andri changed POV algo parameters via the trading-tech config UI (Liam confirmed dynamic, no restart needed). [permalink](https://mahifx.slack.com/archives/C09HN93T0G2/p1777352230999959)

## Notable topics

- 2026-05-05 — UAT Compass availability query: Graeme asked `@here` whether a functioning UAT Compass environment is available. Kate replied she would check; Liam noted a UAT environment exists and "we should be able to spin up whatever you need in fairly short order". No definitive confirmation in window. Bonnie flagged the unanswered question internally. [client-query](https://mahifx.slack.com/archives/C09HN93T0G2/p1777997434492069) [liam-reply](https://mahifx.slack.com/archives/C09HN93T0G2/p1777997877227319)

- 2026-05-05 — TT credentials request for order-cancellation testing: client asked for TT credentials to pass orders to TT for testing order-cancel scenarios; noted this would also support the SOW work on algo parameters. No Mahi reply in window. [permalink](https://mahifx.slack.com/archives/C09HN93T0G2/p1777999511634679)

- 2026-05-05 — cpty 92549025 yield profile follow-up: client sent Echo yield-profile chart link (valutrades.NYC, 2026-04-26→2026-05-04 window) asking "is this graph expected?" and flagging no yield after zeros. Isaac confirmed the fix is deployed and data going forward won't have the same issue; historical zeros in the chart remain. [client-query](https://mahifx.slack.com/archives/CSLM3Q8AD/p1777952984794689) [isaac-reply](https://mahifx.slack.com/archives/CSLM3Q8AD/p1777953182292069)

- 2026-05-05 — cpty 84034427 & 84034562 A/B book classification: client asked Isaac to advise on both. Isaac replied: `84034562` = A book (historic losses, recent improvement and increased volume); `84034427` = B book overall (A on USOUSD, B on NDFUSD — larger volume/PnL in NDFUSD drives B classification). [permalink](https://mahifx.slack.com/archives/CSLM3Q8AD/p1777958393137049)

- 2026-05-04 — cpty 89467069 A-book classification check: client asked team to advise on cpty 89467069; Shyam Hari confirmed A-book for JPXJPY and DOWUSD (with charts), client acknowledged. [permalink](https://mahifx.slack.com/archives/CSLM3Q8AD/p1777870072809899)

- 2026-05-03 — Pulse upsell in ops thread: following client confirming the MySQL gap fix ("looks good, appreciate help over weekend"), Justin Young suggested moving off MySQL to Pulse (faster, larger retention periods), linking the knowledge base. [permalink](https://mahifx.slack.com/archives/C09HN93T0G2/p1777821952617999)
