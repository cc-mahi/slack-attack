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
last_catchup: 2026-06-10T07:34:15Z
---

## Recent issues

> [open] 2026-06-10 — cpty 89468479 yield profile starts below zero — Rory checking
> Client posted Echo yield-profile link (valutrades.NYC, 2026-06-08→2026-06-09, cpty 89468479) asking "Why does it start below zero?" at 08:06 BST. Rory King replied "Hi overnight, checking" at 08:07. No answer in window — unanswered as of run time. [client-query](https://mahifx.slack.com/archives/CSLM3Q8AD/p1781075168367929) [rory-checking](https://mahifx.slack.com/archives/CSLM3Q8AD/p1781075254808079)

> [open] 2026-06-10 — cpty 85551594 toxic yield profile — B-book classification queried, Nathan flagging to dev
> Client asked team to advise on cpty 85551594 at 06:33 BST. Nathan Burch confirmed B-book at 06:41. Client then sent Echo yield-profile link (valutrades.NYC, 2026-06-08→2026-06-09 window) and asked Nathan to check the graph. Nathan replied at 07:58: "that is quite a toxic yield profile and I'd suggest A-booking that flow. I am not sure why the PnL graph suggests otherwise. I will raise this with dev and get back to you." — classification vs yield-profile mismatch, Nathan actively raising with dev. [client-query](https://mahifx.slack.com/archives/CSLM3Q8AD/p1781069589815059) [nathan-b-book](https://mahifx.slack.com/archives/CSLM3Q8AD/p1781070079269269) [nathan-raise-dev](https://mahifx.slack.com/archives/CSLM3Q8AD/p1781074722756569)

> [resolved] 2026-06-04 — Connection issue reported ~22:35 BST — Sam Hewitt fixed, client confirmed reconnected
> Client posted "Hello MAHI Team" + "Please can you fix this?" with a screenshot (image.png) in #mahi-valutrades at 22:35 BST. Sam Hewitt acknowledged ("checking") at 22:35 and asked client to check at 22:41. Client confirmed "Now connected" at 22:47 and thanked Sam. Resolved within ~12 minutes. [client-report](https://mahifx.slack.com/archives/CSLM3Q8AD/p1780608909361739) [sam-checking](https://mahifx.slack.com/archives/CSLM3Q8AD/p1780608958519529) [client-confirmed](https://mahifx.slack.com/archives/CSLM3Q8AD/p1780609632425939)

> [open] 2026-06-02 — Scale POV Gold GCQ6-AUG26 `TT: Submit forbidden` via UBS Algo connection — TT claimed fix, still failing
> Andri switched Gold Algo to Scale POV and ran a live test trade from ~13:53 BST. During testing at 14:09, GCQ6-AUG26 was rejected with `39=8, 58=TT: Submit forbidden` sent via Surya Strait connection. Rory King (Mahi) asked Andri to clarify what "Strait" is and noted different trading account/counterparty from the filled orders. Kate Stagg shared full FIX logs confirming rejection via `TT_MHNY4_FUND_UBSPB_AMB_FIX_OR → VALU_AMB_TT, 57=AMB_Megatrend_13`; `58=TT: Submit forbidden`. Client stated "Raising to TT". **2026-06-03 update:** TT told client they had fixed the issue; client retested and got the same `TT: Submit forbidden` rejection (GCQ6-AUG26 via ScalePOV, account 28836977). Client asked Mahi for FIX log to escalate back to TT. Kate provided the full FIX pair at 13:03 UTC confirming the same reject persists. Still open — TT's claimed fix ineffective. [client-report](https://mahifx.slack.com/archives/C09HN93T0G2/p1780405747363139) [kate-fix-logs](https://mahifx.slack.com/archives/C09HN93T0G2/p1780407130214949) [raised-to-tt](https://mahifx.slack.com/archives/C09HN93T0G2/p1780408112572009) [tt-claimed-fix-still-failing](https://mahifx.slack.com/archives/C09HN93T0G2/p1780491512727679) [kate-fix-log-2](https://mahifx.slack.com/archives/C09HN93T0G2/p1780491838077409)

> [open] 2026-05-29 — New Prod TT connection email — unanswered
> During the Scale POV live test session, client asked Liam if he had seen an email about a new Prod TT connection; noted it has been open with no response for weeks. Liam did not reply to this specific question. [permalink](https://mahifx.slack.com/archives/C09HN93T0G2/p1779982068137559)

> [resolved] 2026-05-28 — Scale POV live test on Phillip/Gold connection — first test trades confirmed flowing
> Liam announced at 09:44 that Scale POV is now configurable. Graeme asked to scope it to Gold on the Phillip connection only, with parameters: Duration 2hr, min participation 1%, max participation 5%, aggression 5, tracked Trend-Mid. Liam configured settings at 15:35–15:38 BST; initial test failed (Liam found a typo, reverted config). Fixed and re-deployed by 16:17; client ran a second test at 16:24. Client confirmed "That looks good too" and "We will leave this live and test with some real trades before moving to other symbols and connections." [liam-announce](https://mahifx.slack.com/archives/C09HN93T0G2/p1779957866479709) [liam-fix](https://mahifx.slack.com/archives/C09HN93T0G2/p1779981435154379) [client-confirm](https://mahifx.slack.com/archives/C09HN93T0G2/p1779981969299249)

> [open] 2026-05-28 — GCQ6-AUG26 (Gold Aug) UAT TT resting orders — SecurityID fixed manually, TT MD connection broken
> Andri reported GCQ6-AUG26 rejected in UAT TT resting orders with `Instrument not found by instrument_id=14347306835933645772`; FIX reject 39=4, tag 58. Arun updated config and identified root cause: incorrect Security ID was in use. Fixed manually at 09:15 BST (orders should now work). However, Arun flagged a related issue: the UAT TT MD connection (`AMB_MH_UAT_FIX_MD→TT_SD/AMB_Megatrend`, targeting `fixmarketdata-ext-uat-cert.trade.tt:11703`) is being rejected on logon with `Requested resource not found`. Security IDs will need manual updating if/when they change until the MD connection is fixed. [client-report](https://mahifx.slack.com/archives/C09HN93T0G2/p1779943449938839) [arun-fix](https://mahifx.slack.com/archives/C09HN93T0G2/p1779956132465369)

> [resolved] 2026-05-28 — Surya FIX seq mismatch `Surya_Live_T→MahiFX_Live_T` — reset confirmed
> Brandon (client) reported seqnum mismatch on `FIX.4.4:Surya_Live_T->MahiFX_Live_T`: session sent seqnum 11424 but Mahi expected 1. Isaac confirmed at 06:27 that the connection appeared logged in and the reset had already been made earlier. Brandon acknowledged. [client-report](https://mahifx.slack.com/archives/C09HN93T0G2/p1779944517420659) [isaac-confirm](https://mahifx.slack.com/archives/C09HN93T0G2/p1779946053563319)

> [open] 2026-05-22 — JUMP_OZNY4_RETAIL_MARGIN_VT missing from XAUUSD TOB — EOD restart done but no price received
> Andri reported 2026-05-21 that JUMP_OZNY4_RETAIL_MARGIN_VT cannot be seen on the TOB for XAUUSD and is generating a negative yield profile for cpty 89468356. Isaac confirmed 2026-05-22: trades land in drop-copy books, no XAUUSD positions in Compass. Root cause: XAUUSD not in the instrument subscription list for JUMP_OZNY4_RETAIL_MARGIN_VT on `senderCompID=MFX-IG_Q,targetCompID=ValuCY_Live_Q`. Isaac offered to add XAUUSD; EOD restart performed. 2026-05-27 05:42 Andri chased — Isaac confirmed at 05:51 that XAUUSD was subscribed but no price received from JUMP_OZNY4_RETAIL_MARGIN_VT. Current XAUUSD pricing in Echo comes from: LMAX_OZNY4_INSTI_NWPB_VT, JUMP_OZNY4_INSTI_NWPB_VT, EDGE_OZNY4_INSTI_NWPB_VT, COMM_OZNY4_RETAIL_NWPB_VT, CNX_OZNY4_INSTI_NWPB_VT — but not the RETAIL_MARGIN_VT variant. Andri asked if EOD restart was done; Isaac confirmed yes at 06:39. Issue unresolved — JUMP_OZNY4_RETAIL_MARGIN_VT still not feeding XAUUSD. INSTI_MARGIN_VT subscription request still pending clarification from Isaac ("How so?"). [client-report](https://mahifx.slack.com/archives/C09HN93T0G2/p1779363979231249) [isaac-diagnosis](https://mahifx.slack.com/archives/C09HN93T0G2/p1779433269964199) [isaac-instrument-list](https://mahifx.slack.com/archives/C09HN93T0G2/p1779687711496309) [insti-request](https://mahifx.slack.com/archives/C09HN93T0G2/p1779687828660719) [no-price-received](https://mahifx.slack.com/archives/C09HN93T0G2/p1779857474916669) [eod-confirmed](https://mahifx.slack.com/archives/C09HN93T0G2/p1779860348385089)

> [open] 2026-05-21 — TT FIX Production Stunnel certificate expiry — no Mahi reply
> Client asked for update on TT FIX Production Stunnel cert expiry (raised via email); screenshot attached. Shyam Hari said he'd follow up. No further reply visible. [permalink](https://mahifx.slack.com/archives/C09HN93T0G2/p1779343214820379)

> [resolved] 2026-05-20 — TT UAT `Scale POV` instrument rejects — FIX account name fixed, orders flowing
> Client (Garry Bersnov / Andri) testing TT UAT resting orders for Scale POV SOW. GCM6-JUN26 / GoldJun rejected with `Unable to find security definition` / `Unknown instrument` through 2026-05-21; Arun made multiple config fixes. Final blocker: `Account does not exist` (tag 1 missing). 2026-05-25 Andri asked for FIX log to raise to TT; Isaac said Mahi would provide. 2026-05-26 client confirmed TT identified tag 1 should be `AMB`; Arun set FIX account to `AMB` at 09:43. Client tested at 11:00 — still `MessageSendFailed: not logged on`. Arun identified an old retired process was the source, shut it down at 11:32, confirmed test trades flowing on the correct `fixOrdersTT1` process. Client confirmed fills visible at 11:54 (`Sell 700` and `Sell 100` GCM6-JUN26); Arun verified both on Mahi side at 11:57. [parent](https://mahifx.slack.com/archives/C09HN93T0G2/p1779276316989649) [tag1-fix](https://mahifx.slack.com/archives/C09HN93T0G2/p1779784983.956559) [confirmed-filled](https://mahifx.slack.com/archives/C09HN93T0G2/p1779792855.699209)

> [resolved] 2026-05-21 — Both SOWs signed: Scale POV + Quantitative Brokers (QB)
> Client (Graeme Watkins) confirmed both SOWs signed and QB UAT credentials shared 2026-05-21 09:57. Liam Cordelle confirmed QB integration started, Mahi will test TT adapter and get to conformance. Agreed to test Scale POV in PROD (not full UAT end-to-end). [client-confirm](https://mahifx.slack.com/archives/C09HN93T0G2/p1779353830413069) [liam-confirm](https://mahifx.slack.com/archives/C09HN93T0G2/p1779356596592969)

> [resolved] 2026-05-13 — XAUUSD yield profile reference LPs clarified — JUMP_OZNY4_RETAIL_MARGIN_VT added
> Client asked which LP is used for XAUUSD yield profile valuation. Nathan Burch initially listed wrong markets (corrected same night); confirmed correct aggregate: COMM_OZNY4_FUND_NWPB_AMB, DB_OZNY4_FUND_NWPB_AMB, GSPM_OZNY4_FUND_NWPB_AMB, JPM_OZNY4_FUND_NWPB_AMB, SC_OZNY4_FUND_NWPB_AMB, UBS_OZNY4_FUND_NWPB_AMB, plus JUMP_OZNY4_RETAIL_MARGIN_VT added per client request. [query](https://mahifx.slack.com/archives/C09HN93T0G2/p1778656219150419) [correction](https://mahifx.slack.com/archives/C09HN93T0G2/p1778704468117649)

> [open] 2026-05-11 — Compass receiving unsubscribed market data — mapping query unanswered
> Daria (Mahi) posted that Compass is receiving market data it's not subscribing to, listing unrecognised markets under `MFX-IG_Q->ValuCY_Live_Q` (JFX_VALUTRADES-SW-NY4) and `MFX-FEED4_Q->ValuCY_Live_Q` (Valutrades, LMAX-ValutradesNWtk1, Currenex-Valutrades, JUMP-CFD, JumpMakerValutrades, Velocity, JFX_VALUTRADES-SW-NY4, Commerz-Valutrades). Asked team to confirm correct market mappings/setup. No reply in window. [permalink](https://mahifx.slack.com/archives/C09HN93T0G2/p1778465858044369)

> [open] 2026-05-10 — Gateways disconnected — confirmation pending
> Client (Brandon) asked Mahi to check gateways were disconnected. Nathan replied asking Brandon to confirm which connections were disconnected and whether they remain so. No client response in window. [client-request](https://mahifx.slack.com/archives/C09HN93T0G2/p1778390311600029) [nathan-reply](https://mahifx.slack.com/archives/C09HN93T0G2/p1778445298015129)

> [resolved] 2026-05-11 — cpty 69942997 yield trade not visible — Echo link provided
> Client asked team to check cpty 69942997 as yield trade not showing. Rory King provided Echo yield-profile link for valutrades.NYC. Client confirmed resolved. [client-query](https://mahifx.slack.com/archives/CSLM3Q8AD/p1778502440118219) [rory-reply](https://mahifx.slack.com/archives/CSLM3Q8AD/p1778502646503639)

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

- 2026-06-10 — QB integration progress check-in: Graeme asked Liam for an update on the Quantitative Brokers algo integration; Liam confirmed on track for the discussed date, asked Graeme to confirm if there's a QB conformance process and to kick it off. Graeme said "Let me check with them." [graeme-checkin](https://mahifx.slack.com/archives/C09HN93T0G2/p1780999540262169) [liam-reply](https://mahifx.slack.com/archives/C09HN93T0G2/p1780999580634929)

- 2026-06-09 — Surya Strait Tag 1 clarification — Andri asked what Tag 1 is used for Surya Philip (Rory confirmed `1=SYE8000`) then asked about Surya Strait; Cameron Hughes (Analyst) checked accounts under Surya/TT, could not find Strait specifically (possibly renamed), asked for an example trade. Andri confirmed no trades on Strait yet to provide. Related to the ongoing Surya Strait algo connection open issue. [andri-query](https://mahifx.slack.com/archives/C09HN93T0G2/p1780994299110339) [cameron-check](https://mahifx.slack.com/archives/C09HN93T0G2/p1780994683205169) [liam-tag1-passthrough](https://mahifx.slack.com/archives/C09HN93T0G2/p1780998251336349)

- 2026-06-09 — cpty 69565751 A/B classification — Rory King confirmed A book with chart. [client-query](https://mahifx.slack.com/archives/CSLM3Q8AD/p1781004243972759) [rory-reply](https://mahifx.slack.com/archives/CSLM3Q8AD/p1781005145808129)

- 2026-06-03 — cpty 92569728 A/B book classification query — Kate confirmed A Book with chart. [client-query](https://mahifx.slack.com/archives/CSLM3Q8AD/p1780493775611609) [kate-reply](https://mahifx.slack.com/archives/CSLM3Q8AD/p1780494293070929)

- 2026-05-28 — cpty 89468255 yield profile query — Isaac confirmed correct: client filled below mid, profiles evaluated against full market. Client sent Echo yield-profile link (valutrades.NYC, 2026-04-28→2026-05-27 window) asking team to advise. Shyam acknowledged; Isaac confirmed profiles are correct — client is being filled below mid and Mahi evaluates yield against the entire market, not just the execution market. [client-query](https://mahifx.slack.com/archives/CSLM3Q8AD/p1779930298067129) [isaac-reply](https://mahifx.slack.com/archives/CSLM3Q8AD/p1779931645060929)

- 2026-05-05 — UAT Compass availability query: Graeme asked `@here` whether a functioning UAT Compass environment is available. Kate replied she would check; Liam noted a UAT environment exists and "we should be able to spin up whatever you need in fairly short order". No definitive confirmation in window. Bonnie flagged the unanswered question internally. [client-query](https://mahifx.slack.com/archives/C09HN93T0G2/p1777997434492069) [liam-reply](https://mahifx.slack.com/archives/C09HN93T0G2/p1777997877227319)

- 2026-05-05 — TT credentials request for order-cancellation testing: client asked for TT credentials to pass orders to TT for testing order-cancel scenarios; noted this would also support the SOW work on algo parameters. No Mahi reply in window. [permalink](https://mahifx.slack.com/archives/C09HN93T0G2/p1777999511634679)

- 2026-05-05 — cpty 92549025 yield profile follow-up: client sent Echo yield-profile chart link (valutrades.NYC, 2026-04-26→2026-05-04 window) asking "is this graph expected?" and flagging no yield after zeros. Isaac confirmed the fix is deployed and data going forward won't have the same issue; historical zeros in the chart remain. [client-query](https://mahifx.slack.com/archives/CSLM3Q8AD/p1777952984794689) [isaac-reply](https://mahifx.slack.com/archives/CSLM3Q8AD/p1777953182292069)

- 2026-05-05 — cpty 84034427 & 84034562 A/B book classification: client asked Isaac to advise on both. Isaac replied: `84034562` = A book (historic losses, recent improvement and increased volume); `84034427` = B book overall (A on USOUSD, B on NDFUSD — larger volume/PnL in NDFUSD drives B classification). [permalink](https://mahifx.slack.com/archives/CSLM3Q8AD/p1777958393137049)

- 2026-05-04 — cpty 89467069 A-book classification check: client asked team to advise on cpty 89467069; Shyam Hari confirmed A-book for JPXJPY and DOWUSD (with charts), client acknowledged. [permalink](https://mahifx.slack.com/archives/CSLM3Q8AD/p1777870072809899)

- 2026-05-11 — Full configured-markets list provided: client (directed at Daria) asked for complete list of markets configured. Nathan Burch provided the full breakdown by FIX feed session (fixMarketDataTT1/TT2, fixMarketDataSurya1, fixMarketDataCTrader1, fixMarketDataValutradesFEED1–5, fixMarketDataValutrades2). Notably includes Surya_ISPrime and Surya_Straits under fixMarketDataSurya1 — relevant to the ongoing Surya Strait algo connection issue. [client-request](https://mahifx.slack.com/archives/C09HN93T0G2/p1778484353813979) [nathan-list](https://mahifx.slack.com/archives/C09HN93T0G2/p1778539303901029)

- 2026-05-10 — Client requested bounce before market open: client sent a standalone message asking for a process/gateway bounce before market open ("Sorry if not bounced already please bounce before the market open"). No Mahi reply visible. [permalink](https://mahifx.slack.com/archives/C09HN93T0G2/p1778432301421509)

- 2026-05-08–12 — Routine A/B book classification queries: several cpty checks answered by overnight team — cpty 39933574 (Nathan: A book, only 22 trades over 3 days, insufficient data), 92518184 (Nathan: A book), 84517632 (Rory: A book), 89468240 (Nathan: B book), 77537069 (Nathan: A book), 77559135 (Nathan: A book). All acknowledged by client. [sample](https://mahifx.slack.com/archives/CSLM3Q8AD/p1778563239391109)

- 2026-05-03 — Pulse upsell in ops thread: following client confirming the MySQL gap fix ("looks good, appreciate help over weekend"), Justin Young suggested moving off MySQL to Pulse (faster, larger retention periods), linking the knowledge base. [permalink](https://mahifx.slack.com/archives/C09HN93T0G2/p1777821952617999)
