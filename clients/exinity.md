---
slug: exinity
aliases: []
refs:
  vibepulse: ../VibePulse/.claude/clients/exinity.yaml
  billing: ../MahiProduct/data/billing/clients.json     # entry: exinity
  hosts: ../MahiProduct/data/client-hosts.json          # entry: exinity
  wiki: ../MahiProduct/wiki/clients/exinity.md
channels:
  internal-exinity: C040V9LNKT5
  mahi-exinity: C0456LSHQQK
contacts:
  - {name: "Marianna Konstantinidi", role: "head of trading / primary technical counterpart (MK)", confidence: low}
  - {name: "Matthew Ayub (Matt A)", role: "trading lead — books, hedging, alerting, A/B-book routing", confidence: low}
  - {name: "Daniel Kurra", role: "trading ops — pricing channels, liquidity pools, hedger/execution config", confidence: low}
  - {name: "Mukhammad Khamidov", role: "trading ops — Wagyu/insti pricing, rejects, position recs", confidence: low}
  - {name: "Louie Davidson", role: "ops — order traces, LP test trades, simulations", confidence: low}
  - {name: "Christian Lee", role: "ops — book/position investigations, risk-splitting moves", confidence: low}
  - {name: "Samuel Ewebiyi", role: "ops — alerts, rebase PnL checks, position recs", confidence: low}
  - {name: "Corey Pritchard", role: "pricing config / backtests (joined channel 2026-09-02)", confidence: low}
  - {name: "Keshav Woottum", role: "ops — yield simulations, reporting", confidence: low}
  - {name: "George Moore", role: "ops — LP/UBS test-trade liaison, sim data", confidence: low}
  - {name: "Justin", role: "Exinity exec — CFD licence / commercial decisions", confidence: low}
last_catchup: 2026-11-24T08:13:57Z
status: active
---

## Now
trading-2 tickstore filled 2026-11-20 (~1h of tick data lost, recovered by 04:34Z, fix PR awaits deploy). SI Insti XAU hedger sat on risk on 2026-11-17 (Matt A urgent; Rory checking, position-transfer period ~2h); futures/wash-book hedges were missing from yield profiles until books were added to analytics config 2026-11-17.
Centroid conformance counterparty-tag fix awaits Exinity retest; trading-1 gateway failed to start after the 2026-11-14 reboot (restarted by hand, may recur). Signal-process errors recurred 2026-11-12 and again 2026-11-13 (processes restored each time, dev fix pending); an institutional client's 500ms order-expiry complaint found no Mahi-side cause; Exinity asked about oil and silver futures (needs new book structure).
Reactive LP feeds went silent 2026-11-09 with no alert (stale-price alerts added 2026-11-10); STRDPARTNER sat disabled 2026-11-07 to 11-09 (RCA follow-up owed). NFP showed no LR on B_CLIENTS.
Exinity is migrating LPs from Hidden Road to Wedbush and chasing pricing-spike, book-break and alerting asks; weekend reliability matters as weekend crypto nears. Open on Mahi: per-book PnL-drop alerts, XAU position realignment, TradersHub A-book move, XCUUSD spread decision, Compass 26.4 signalProcessFI1 overflows, adaptive-skew sim owner.

## Streams

### tickstore-disk-full — trading-2 tickstore filled, tick data lost
status: open · since: 2026-11-20 · last: 2026-11-20
State: Internal only. The S3 tick uploader on trading-2 hung 2026-11-19 12:17Z and the tickstore hit 100% at ~01:15Z on 2026-11-20, so tick data from ~01:15Z to ~02:16Z is lost or truncated (about 18.4k empty files deleted, 11.8k truncated kept) and the cleaner deleted some un-uploaded files from 2026-11-19 afternoon. Lee killed the hung upload, restored space (35G free by 04:28Z) and put the Puppet and cleaner crons back at 04:32Z; ~260k files were still uploading at 04:34Z. Fix (upload timeout, skip vanished files, cleaner lock) is merged in MfxCompassInfrastructure PR 1101 but not yet deployed to trading-2.
Next: Infra-Deploy of PR 1101 to trading-2 with a change record; backlog upload to finish.
Refs: https://mahifx.slack.com/archives/C040V9LNKT5/p1795142350003819 https://mahifx.slack.com/archives/C040V9LNKT5/p1795149262039629

### signal-process-alerts — Alerts on signal processes, no execution impact
status: open · since: 2026-11-05 · last: 2026-11-19
State: On 2026-11-19 ~03:39Z Samuel again asked Mahi to check errors (screenshot, not readable; likely the same signal processes, not stated); Nathan restarted the processes and confirmed both back online by 04:03Z. On 2026-11-13 Samuel chased an emergency alert and Nathan confirmed the process was back up. On 2026-11-12 Samuel reported signal errors; Nathan restored both processes by 04:45Z and said Mahi knows the cause and dev is working on a fix. Alerts on 2026-11-05/06 were also screenshots; Daria said no trading impact (signal processes are outside execution), restored within minutes. May relate to the 2026-10-26 signalProcessFI1 overflow.
Next: Mahi dev to deliver the fix for the recurring signal-process errors and tell Samuel the cause.
Refs: https://mahifx.slack.com/archives/C0456LSHQQK/p1793854172360089 https://mahifx.slack.com/archives/C0456LSHQQK/p1794534671593379 https://mahifx.slack.com/archives/C0456LSHQQK/p1795059543591619 https://mahifx.slack.com/archives/C0456LSHQQK/p1795060994231009

### order-reject-queries — Reject and fill investigations
status: open · since: 2026-09-21 · last: 2026-11-18
State: On 2026-11-18 Samuel asked why API_111000021 gets cancels on XAU; Nathan found they are all limit IoC XAUUSD buys of 950oz priced at Mahi's top-of-book offer with only ~100oz available, so they cancel with LIQUIDITY_VIOLATION while the same-size market orders fill (same pattern as the 2026-11-04 800oz cancels). Open: Christian's 2026-10-09 FIX-log help request awaits his reply; Mukhammad's 2026-10-02 XAU rejects had no outcome seen. Earlier rejects were explained; the bridge must retry TPs, as Mahi holds no pending TP/SL. On 2026-11-02 a client TP on DOWUSD was rejected ('Internalisation Quantity greater than Published', published quantity 0 as all LPs had stopped pricing).
Next: Christian to say what he needs from the FIX logs; Exinity to check its bridge retry behaviour.
Refs: https://mahifx.slack.com/archives/C0456LSHQQK/p1790857668546679 https://mahifx.slack.com/archives/C0456LSHQQK/p1793756635298589 https://mahifx.slack.com/archives/C0456LSHQQK/p1794980608405509 https://mahifx.slack.com/archives/C0456LSHQQK/p1794981508143979

### si-insti-hedger-risk — SI Insti XAU hedger sat on risk, position transfer period
status: open · since: 2026-11-17 · last: 2026-11-17
State: On 2026-11-17 ~18:04Z Matt A urgently asked Mahi to check whether the SI Insti FX hedger performed as expected on XAU, as SI_INSTI_NET sat on risk for much of the afternoon (windows 12:30-14:36Z and 16:24-16:52Z). Rory saw the SI book's position transfer period is ~2 hours (risk.positionTransfer.config) and is still confirming; Matt said Exinity may adjust its own settings. Matt also asked, not urgently, for an explanation of the 'auto-position transfer adjustments' in the position history tab, which Rory will write up.
Next: Rory to finish the hedger check and explain the auto-position transfer adjustments; Matt to decide on settings changes.
Refs: https://mahifx.slack.com/archives/C0456LSHQQK/p1794938681074289 https://mahifx.slack.com/archives/C0456LSHQQK/p1794939240360569

### futures-yield-visibility — Futures and wash-book hedges missing from yield profiles
status: open · since: 2026-11-17 · last: 2026-11-17
State: On 2026-11-17 Daniel reported B_EXTERNAL_WASH hedge orders (e.g. XAUFUT-Z, a Velocity fill) not appearing in yield profiles. Internally William added FUTURES_CLIENTS_NET, B_HOUSE, B_EXTERNAL_WASH, B_INSTI_HOUSE and B_INSTI_EXTERNAL_WASH to analytics.parties (analyticsProcess bounce, 17:02Z) and B_EXTERNAL_WASH plus the futures books to riskPath outsiderBooks (bounce, 17:50Z). No confirmation to Daniel seen in the shared channel.
Next: Mahi to tell Daniel the books are added and confirm the trades now show.
Refs: https://mahifx.slack.com/archives/C0456LSHQQK/p1794926506147159 https://mahifx.slack.com/archives/C040V9LNKT5/p1794937853367899

### weekend-ops-reliability — Weekend restarts, FIX session windows, hedger recovery
status: open · since: 2026-08-17 · last: 2026-11-15
State: Sat 2026-11-14 clientDistributionGateway1 on trading-1 failed to start after the weekly reboot (duplicate consumer registration on CLIENT_PRICE_VIP_LDN, no auto-restart); James restarted it by hand, which is what Siddig saw missing at 10:55Z. An OS patch on trading-2 (CHG-2611-DA9T) left two riskPathSI down until 09:59Z, and Beeks pulled a faulty LD4 link (NOCINT-860378). The gateway error may recur at the next reboot. Earlier: the 2026-10-17 reboot left hybrid hedgers down 08:15 to ~10:55Z (duplicate Hazelcast shard ID, trading-2 node out of 2 GB heap, MySQL connection limit; RCA written, P2 open; DB limit raised to 2048 on 2026-10-19). Exinity plans weekend crypto pricing.
Next: Mahi to find why the gateway fails to start after reboot; Mahi to raise the trading-2 hazelcastNode heap above 2 GB and break down MySQL connections on trading-1 (limit raise done 2026-10-19); Daniel/Kate to revisit weekend support when weekend crypto starts.
Refs: https://mahifx.slack.com/archives/C0456LSHQQK/p1786976101361259 https://mahifx.slack.com/archives/C0456LSHQQK/https://mahifx.slack.com/archives/C040V9LNKT5/p1792424073139469 https://mahifx.slack.com/archives/C040V9LNKT5/p1794777515302229 https://mahifx.slack.com/archives/C040V9LNKT5/p1794780190721359

### centroid-fok-conformance — Centroid conformance: FOK brokered orders expire
status: open · since: 2026-10-29 · last: 2026-11-13
State: During Centroid/Mahi conformance testing on 2026-10-28 Matt saw an A-Book XAU/USD FOK market order cancelled (EXPIRED) on the Centroid connection while a PrimeXM FOK filled. Kate explained the liquidity pool has no FOK-capable gold market, so the brokered Centroid order expired before reaching an LP; the PXM order was internalised. On 2026-10-30 Kate explained rules are picked by trading account: Centroid (account 001) hits the Exinity Connect rule and Chuck profile with top-up off, while STP FOKs that fill (account 65280, A-BOOK rule) have Allow Top Up on. Daniel asked whether Centroid can be set up like STP. On 2026-11-13 Matt reported Centroid test trades reach Mahi but the Counterparty column lacks the MT5 login tag (MT5_3056_tem); Rory said it is a tag issue and gave the party-ID block to send (453=1, 448=MT5_3056_tem, 447=D, 452=3); Matt retests Monday 2026-11-16.
Next: Matt to retest the party-ID tags and report back; Mahi (Kate) offered on 2026-10-30 to configure Allow Top Up on the Chuck profile; Exinity (Daniel/Matt) to say yes or change Centroid-side config so FOK is not brokered to WB.
Refs: https://mahifx.slack.com/archives/C0456LSHQQK/p1793264343496069 https://mahifx.slack.com/archives/C0456LSHQQK/p1793365009754819 https://mahifx.slack.com/archives/C0456LSHQQK/p1794594865097469 https://mahifx.slack.com/archives/C0456LSHQQK/p1794596136004249

### futures-oil-silver — Exinity asks about adding oil and silver futures
status: open · since: 2026-11-12 · last: 2026-11-12
State: Corey asked on 2026-11-12 whether oil and silver futures are planned. Rory said Mahi would scope it (futures need a new book structure) and asked how Exinity will risk-manage them; no reply yet.
Next: Corey to say how Exinity plans to risk-manage the futures; Mahi to scope the book structure.
Refs: https://mahifx.slack.com/archives/C0456LSHQQK/p1794492374298919 https://mahifx.slack.com/archives/C0456LSHQQK/p1794492465501279

### insti-500ms-expiry — Institutional client sees ~500ms before orders expire
status: open · since: 2026-11-11 · last: 2026-11-11
State: Louie relayed an institutional client's complaint of a 500ms delay on almost all orders (XAUUSD limit orders via FIX, three examples 2026-11-11 14:37-15:08Z). Rory found nothing on Mahi's side adding 500ms: the first order arrived 14:37:26.633 and was cancelled at .635 (limit through price, 20ms last look), so the 'expired' the client saw came ~500ms later; the other two never appear in Mahi logs. Louie will check them on Exinity's side.
Next: Louie to check the 14:40 and 15:08 orders on Exinity's side.
Refs: https://mahifx.slack.com/archives/C0456LSHQQK/p1794419081666329 https://mahifx.slack.com/archives/C0456LSHQQK/p1794422570877219

### reactive-feed-gap — Reactive LP price feeds stopped, no alerting
status: open · since: 2026-11-10 · last: 2026-11-10
State: Matt A asked 2026-11-10 whether Reactive's 2026-11-09 API incident (15:43-18:03 UTC) affected Exinity's connections. Nathan found the Reactive-routed feeds (BAML, Deutsche Bank, Jane Street, Jump, Nomura) stopped pricing 15:53:21Z and resumed 17:05:53Z while sessions stayed logged on; no orders were attempted at those venues and hedging continued through other LPs. Matt asked whether any alert covers a sustained feed stop. At 11:23Z Rory bounced systemStateMonitor with stale-pricing alerts added for several LPs (staleMarketDataFeed.alertThreshold) per Matt's request (internal note); no confirmation to Exinity seen in the shared channel.
Next: Mahi to tell Exinity the stale-price alerts are live and which LPs they cover.
Refs: https://mahifx.slack.com/archives/C0456LSHQQK/p1794292235121349 https://mahifx.slack.com/archives/C040V9LNKT5/p1794309815194049

### strd-partner-logon-gap — STRDPARTNER session disabled after sequence reset
status: open · since: 2026-11-09 · last: 2026-11-09
State: Samuel reported 2026-11-09 ~02:17Z that orders were not going through on ExinitySTRDPARTNER. Nathan re-enabled the session (~03:01Z) and explained at 06:20Z: the session's sequence numbers reset to 1 at the weekly start (Saturday 10:00 UTC); Exinity's side rejected the reply as MsgSeqNum too low and dropped within 4ms; Mahi's gateway treated the half-open logon as faulty and disabled the session, which nothing re-enables automatically. Exinity got "session is disabled" from the 2026-11-07 open until Monday, so orders were down ~two days. Mahi is reviewing why no alert fired.
Next: Nathan to report back on the review and the missing alert; fix so a fast disconnect cannot leave the session disabled.
Refs: https://mahifx.slack.com/archives/C0456LSHQQK/p1794190632412229 https://mahifx.slack.com/archives/C0456LSHQQK/p1794205214970219

### nfp-lr-skew-review — NFP skew and missing LR on B_CLIENTS (internal)
status: open · since: 2026-11-06 · last: 2026-11-06
State: Internal only. Will Carter found that over 13:30-13:33 UTC on NFP (2026-11-06) B_CLIENTS booked about $2.1k skew (~$10/M on $203M, corrected from an initial $609M figure) and no LR, well below comparators, and asked whether LR is off by design or a gap and for an owner for an adaptive-skew sim replay of the release to take to the client. Will is catching up with Exinity's lead (Nick) separately. No owner named for the sim yet.
Next: Someone to confirm LR config on B_CLIENTS and own the adaptive-skew sim; Will to catch up with Exinity next week.
Refs: https://mahifx.slack.com/archives/C040V9LNKT5/p1793975304979759 https://mahifx.slack.com/archives/C040V9LNKT5/p1793980122754249

### adausd-insti-rounding — Stale ADAUSD/DOGUSD on insti feeds
status: open · since: 2026-11-06 · last: 2026-11-06
State: On 2026-11-06 ~03:14Z Mukhammad reported ADAUSD insti pricing stale on the Wagyu, Chuck and Fillet channels (retail fine). Nathan found the insti channels price from the liquidity pool, which rounded ADAUSD to 3 decimals so the price rarely moved and often showed bid equal to offer; DOGUSD was affected the same way. Config now sets 5 decimals but needs a process restart, so it takes effect after the weekend reboot. Mukhammad acknowledged.
Next: Mahi to confirm the 5dp pool rounding is live after the weekend reboot.
Refs: https://mahifx.slack.com/archives/C0456LSHQQK/p1793934874890119 https://mahifx.slack.com/archives/C0456LSHQQK/p1793937644348509

### strd-feed-drops — STRD connector and pricing drop-outs
status: open · since: 2026-10-28 · last: 2026-11-06
State: 2026-11-06 XAUUSD orders on ExinitySTRD-Orders reached Mahi's gateway 3.2-4.0s after SendingTime then filled in ~40ms, so the delay arose before the gateway; cause still under investigation. Samuel's 2026-10-29 error report was handled by bringing processes up; cause open.
Next: Mahi (Nathan) to report the cause of the 2026-10-29 errors to Samuel; Mahi (Rory) to report why the 2026-11-06 XAU orders arrived 3-4s late.
Refs: https://mahifx.slack.com/archives/C0456LSHQQK/p1793222374723979 https://mahifx.slack.com/archives/C0456LSHQQK/p1793239541468319 https://mahifx.slack.com/archives/C0456LSHQQK/p1793977409207179

### pricing-spikes-widening — Spiky and wide pricing complaints
status: open · since: 2026-09-01 · last: 2026-11-06
State: On 2026-11-06 ~20:35Z Christian reported USDTHB not ticking for almost 10 min with poor pricing; Cameron Hughes added USDTHB to the referencePriceMarketSelectors override and asked Christian to recheck, no reply seen. Sep 1 Wagyu spikes traced to Nomura via MWMS references; Exinity is backtesting Wedbush LPs in MWMS. 2026-10-07 EURUSD spikes were skew plus Invast's bid crossing Wedbush offers (skew cut, Invast kept in the mid). Poor LP pricing 2026-10-26 20:45-22:00 was the market itself wide over NY rollover (GBPCHF 25-30 pips); the mid held.
Next: Christian to confirm USDTHB now ticks; Exinity to say whether spikiness persists and to check rollover width with Wedbush/LPs (and why Barclays, DB, HSBC, Velocity don't stream GBPCHF) or send a timestamp; Wedbush-in-MWMS backtest result unconfirmed.
Refs: https://mahifx.slack.com/archives/C0456LSHQQK/p1788299416706969 https://mahifx.slack.com/archives/C0456LSHQQK/p1793100609912989 https://mahifx.slack.com/archives/C0456LSHQQK/p1793127985564209 https://mahifx.slack.com/archives/C0456LSHQQK/p1793997336044029

### echo-tob-crash — Echo TOB errors on historical dates
status: open · since: 2026-11-03 · last: 2026-11-03
State: On 2026-11-03 Daniel reported Echo TOB crashing when EURUSD is selected for 2026-10-21 (recent days work). Daria pointed him to Compass price forensics; no root cause yet.
Next: Daria to investigate; Daniel to say whether 2026-10-25 also fails.
Refs: https://mahifx.slack.com/archives/C0456LSHQQK/p1793686208763259 https://mahifx.slack.com/archives/C0456LSHQQK/p1793686599906029

### admin-feed-multicast — Multicast change undo to restore admin feeds
status: open · since: 2026-11-02 · last: 2026-11-02
State: Saturday 2026-10-31's multicast change broke the admin feeds; Liam posted change CHG-2611-0Z3D (approved) to undo it Mon 2026-11-02 22:00-23:00Z. Internal only, no Exinity thread seen.
Next: Confirm admin feeds restored after the 22:00Z window.
Refs: https://mahifx.slack.com/archives/C040V9LNKT5/p1793646965293749

### bbook-weekend-pnl — False -1.7M B-book PnL at Sunday open
status: open · since: 2026-11-01 · last: 2026-11-01
State: On 2026-11-01 ~22:23Z Mukhammad asked whether the B-book PnL of -1.7M when rebased from Friday close was real, since XAU had not reopened (rebased from Sunday close it was fine). Shyam said it was not an actual loss: it reverted at the metals open once live pricing resumed, and Mahi is looking into the pricing used to mark the book over the weekend.
Next: Mahi (Shyam) to report what weekend marking price caused the false -1.7M.
Refs: https://mahifx.slack.com/archives/C0456LSHQQK/p1793571776435089 https://mahifx.slack.com/archives/C0456LSHQQK/p1793575936910949

### wedbush-lp-migration — Hidden Road to Wedbush LPs, IOC/top-up mechanics
status: open · since: 2026-08-05 · last: 2026-10-30
State: Wedbush LPs do not take FOK/market orders, so STP clients top up with high-slippage IOC Limits (live 2026-08-20). A 2026-09-17 top-up left a 200oz residual on LIQUIDITY_POOL_LDN; Rory set Allow Top-Up to No on EXINITY_CONNECT_CHUCK; residual booking unresolved.
Next: Exinity to book/move the 200oz residual; confirm where top-up should be on versus off (Kate offered 2026-10-30 to enable it on Chuck, see centroid-fok-conformance).
Refs: https://mahifx.slack.com/archives/C0456LSHQQK/p1787146976800389 https://mahifx.slack.com/archives/C0456LSHQQK/p1789637820930659 https://mahifx.slack.com/archives/C0456LSHQQK/p1793365009754819

### pnl-drop-alerts — Per-book PnL-drop alerts and alert email restoration
status: open · since: 2026-09-18 · last: 2026-10-29
State: Matt chased on 2026-10-29 for an update on the "emergency alerts" (no reply seen). He asked for per-book loss alerts (thresholds $1K-$5K/day given 2026-10-06), an alert when LIQUIDITY_POOL_LDN exposure is above zero, and restoration of old email alerts (hedger throttle, VaR, FIX connection, A/B-book rejections). Alerts froze systemStateMonitor on 2026-10-08 (reverted; fix deployed 2026-10-14); 24h A-Book alerts fired 2026-10-20. Mukhammad's 2026-10-22 question on execution impact of a systemStateMonitor restart is unanswered.
Next: Mahi to reply to Matt's 2026-10-29 chase and Mukhammad's question, and confirm the other books' PnL alerts and the LP-exposure alert are live; email-alert restoration still to be put in place.
Refs: https://mahifx.slack.com/archives/C0456LSHQQK/p1789753758017939 https://mahifx.slack.com/archives/C0456LSHQQK/p1792511678868259 https://mahifx.slack.com/archives/C0456LSHQQK/p1792683656578339 https://mahifx.slack.com/archives/C0456LSHQQK/p1793265485080539

### compass-26-4-upgrade — Compass 26.4 upgrade and post-upgrade signal overflow
status: open · since: 2026-10-23 · last: 2026-10-26
State: Compass 26.4 went live the weekend of 2026-10-24 (CHG-2610-VSHM). On 2026-10-26 signalProcessFI1 on trading-1 went down on an IFMSslidWndwCbackStream overflow (07:18Z); Kate told Matt skew stayed live apart from the restart. The overflow recurred 16:18Z; Cameron bounced it and rolled out the fix ~17:23Z.
Next: Confirm the signalProcessFI1 fix holds (no further overflow alerts) and whether it was caused by the 26.4 upgrade.
Refs: https://mahifx.slack.com/archives/C0456LSHQQK/p1792760362955399 https://mahifx.slack.com/archives/C040V9LNKT5/p1793035385218119

### yield-sims-giraffe — Yield simulations on Exinity trade datasets
status: watching · since: 2026-10-05 · last: 2026-10-20
State: [watching: no activity since 2026-10-20] On 2026-10-20 Matt sent another UTC+3 sim request (TRAD-2510); Rory to confirm when run (benchmark is the LP-feed aggregate in referencePriceMarketSelectors). Rory ran Matt's 2026-10-19 October workbook that day. Keshav's three GMT+3 datasets had ~half the trades 20-40 pips off the retail mid; not run pending outlier handling.
Next: Rory to run and report the 2026-10-20 sim; Matt to review the 2026-10-19 sim; Exinity (George/Keshav) to decide on excluding or correcting off-market trades in the earlier datasets.
Refs: https://mahifx.slack.com/archives/C0456LSHQQK/p1791216865711639 https://mahifx.slack.com/archives/C0456LSHQQK/p1791893099757919 https://mahifx.slack.com/archives/C0456LSHQQK/p1792509715236449

### compass-config-questions — Config and UI how-it-works questions
status: watching · since: 2026-09-09 · last: 2026-11-11
State: On 2026-11-11 Matt asked how to view order books at a timestamp for a pricing stream; Rory pointed to Compass price forensics (better than Echo TOB; full depth needs Pulse), Matt found the trade-detail widget sufficient, and Rory confirmed price-forensics spreads are per unit (e.g. $60.80 x 900oz); Matt's extra Compass IP was whitelisted. Daniel asked on 2026-10-06 for AEXEUR/HISKHKD/S30SGD to be checked as enabled; no reply seen.
Next: Mahi to confirm AEXEUR/HISKHKD/S30SGD enablement.
Refs: https://mahifx.slack.com/archives/C0456LSHQQK/p1790076650019729 https://mahifx.slack.com/archives/C0456LSHQQK/p1791263973364079 https://mahifx.slack.com/archives/C0456LSHQQK/p1792005318722349 https://mahifx.slack.com/archives/C0456LSHQQK/p1794394501162529

### insti-exotics-pricing — Exotic pairs unpriced on Distribution_Insti_LDN
status: watching · since: 2026-10-15 · last: 2026-10-16
State: [watching: no Exinity reply since 2026-10-16] Mukhammad asked why exotics (AUDNOK, AUDSEK etc.) are not priced on the Insti streams. Shyam traced it to the Hidden Road to Wedbush LPs SW switch (live 21 Aug): AUDNOK/CHFNOK only have Jane Street, blank 21:00-00:00 UTC daily; AUDSEK and CHFSGD have no Wedbush LP and are unpriced since 21 Aug; TRYJPY, AUDSGD, ZARJPY go blank after the 21:00 rollover. Mahi offered UBS (and LMAX for EURMXN); Mukhammad to confirm.
Next: Exinity to confirm whether to add UBS/LMAX for the exotics.
Refs: https://mahifx.slack.com/archives/C0456LSHQQK/p1792107598604319 https://mahifx.slack.com/archives/C0456LSHQQK/p1792111952713259

### xau-book-realignment — XAU position breaks across A House, Big House and Clients Net
status: watching · since: 2026-09-25 · last: 2026-10-14
State: [watching: awaiting Mahi reply to 2026-10-14 chase] The Big House vs Big Clients Net XAU break (a 2026-05-07 Invast to LMAX move booked to the wrong book) was fixed on 2026-09-28 by Rory with a six-row import into BIG_HEDGING_WASHBOOK_LDN and BIG_HOUSE, with the Big hedger off, plus a 14oz follow-up; Daniel confirmed it looked right. Separately, Mukhammad raised a 1.13k oz visual break between A House and Clients Net (not real risk, per Nathan, who supplied a realignment CSV based on A_HOUSE). On 2026-10-01 Daniel asked for the adjustment to use the CLIENTS book as source of truth instead; Rory said Mahi would look, and Daniel chased on 2026-10-14 with no reply seen.
Next: Mahi (Rory/Nathan) to produce adjustments using CLIENTS as the reference and reply to Daniel's 2026-10-14 chase.
Refs: https://mahifx.slack.com/archives/C0456LSHQQK/p1790329597165279 https://mahifx.slack.com/archives/C0456LSHQQK/p1790613838734949 https://mahifx.slack.com/archives/C0456LSHQQK/p1790555345540849 https://mahifx.slack.com/archives/C0456LSHQQK/p1791976466451139

### insti-book-moves — Insti routing, tag forwarding and position moves
status: watching · since: 2026-08-31 · last: 2026-10-12
State: PrimeXM tag forwarding on CONNECT_FILLET keeps landing in BIG_INSTI_CLIENTS_1 if new tags avoid the wildcard risk-splitting counterparties (Daria, 2026-08-31). On 2026-10-12 Christian asked to move TradersHub (111000023) to A-book and open exposure at Wedbush; Nathan promised confirmation and help with the adjustment before EOD, no outcome seen.
Next: Nathan to confirm the steps/books and help with the TradersHub adjustment.
Refs: https://mahifx.slack.com/archives/C0456LSHQQK/p1788203770663179 https://mahifx.slack.com/archives/C0456LSHQQK/p1789471167917609 https://mahifx.slack.com/archives/C0456LSHQQK/p1791828427289149

### velocity-nomura-onboard — Velocity (VTI C2C) and Nomura Elysium onboarding
status: watching · since: 2026-08-21 · last: 2026-10-08
State: No activity since 2026-10-08; downgraded to watching, Wedbush sign-off unconfirmed. William set up the Velocity VTI C2C connection with Elysium reporting (config added 2026-09-02, FIX passwords awaited), tested Nomura's Elysium reporting leg on 2026-09-22 and made NOMURA_SW_WB a live market on 2026-09-23. William ran VELOCITY_WB test trades 2026-10-01 and sent FIX messages to Wedbush; Rory confirmed pricing flowing 2026-10-08. Wedbush sign-off not seen.
Next: Louie's test trade result; Wedbush conformance sign-off.
Refs: https://mahifx.slack.com/archives/C0456LSHQQK/p1787314659822969 https://mahifx.slack.com/archives/C0456LSHQQK/p1789999351066319 https://mahifx.slack.com/archives/C0456LSHQQK/p1790864738809539 https://mahifx.slack.com/archives/C0456LSHQQK/p1791462553978629

### copper-xcu-pricing — Copper (XCUUSD) stack and execution routing
status: watching · since: 2026-08-21 · last: 2026-10-05
State: Invast copper 5dp-vs-4dp rejects (2026-08-21) got a temporary internalise rule. XCUUSD's one-layer 50-unit stack cancelled a 300-unit order (2026-09-21); Nathan deepened it to ~15k, TOB spread left at $1. On 2026-10-05 Rory copied the BACKUP rule into the multiChannelConfig and added the _CFD channel to the CFD Internalise rule; both are in place.
Next: Exinity to decide the XCUUSD TOB spread on CLIENT_PRICE_RETAIL_LDN.
Refs: https://mahifx.slack.com/archives/C0456LSHQQK/p1787324960613979 https://mahifx.slack.com/archives/C0456LSHQQK/p1789964680045919 https://mahifx.slack.com/archives/C0456LSHQQK/p1791218263170469

### gbpaud-roll-cancels — GBPAUD cancels at rollover (wide-spread suppression)
status: closed · since: 2026-11-11 · last: 2026-11-11 · closed: 2026-11-12
State: 2026-11-11 rollover cancels were wide-spread suppression; bridge retried and filled. Samuel declined loosening it.
Refs: https://mahifx.slack.com/archives/C0456LSHQQK/p1794435903177429 https://mahifx.slack.com/archives/C0456LSHQQK/p1794437737729939

### sunday-open-cancels — Last-look latency cancels at Sunday FX open
status: closed · since: 2026-10-18 · last: 2026-10-18 · closed: 2026-11-12
State: 391 orders cancelled by the latency safeguard before the restarted order process warmed up; dev ticket raised, assumed resolved.
Refs: https://mahifx.slack.com/archives/C0456LSHQQK/p1792359440287539

### ld-network-route28 — Beeks LD network incident and unconfirmed Route28 AVAX order
status: closed · since: 2026-10-16 · last: 2026-10-16 · closed: 2026-11-12
State: Beeks LD incident took hybridHedgerCFD1 down on an unconfirmed Route28 AVAX order; Kate restarted it. No answer seen, assumed resolved.
Refs: https://mahifx.slack.com/archives/C0456LSHQQK/p1792143223051249 https://mahifx.slack.com/archives/C0456LSHQQK/p1792148922388959


### xau-cpi-slippage — XAUUSD 900oz fill slippage at CPI
status: closed · since: 2026-11-10 · last: 2026-11-10 · closed: 2026-11-16
State: 900oz fill after CPI (2026-11-10) was as expected; Louie accepted.
Refs: https://mahifx.slack.com/archives/C0456LSHQQK/p1794324361585969 https://mahifx.slack.com/archives/C0456LSHQQK/p1794330199036949

## Arc
- 2026-04-29 — Exinity / Jane Street test-trade meeting
- 2026-05-14 — Jump/Wedbush conformance call held; JUMP_SW_WB EURUSD live
- 2026-06-04 — Centroid migration planned: new FIX connections on Connect channels, gradual move off PXM
- 2026-06-21 — UBS_FA_WB / UBS_SW_WB testing done; Wedbush LP panel live on Insti hedgers
- 2026-07-17 — HYBRID hedger root cause (down ~18 days since 2026-06-12) found and fixed
- 2026-08-08 — XRPUSD went live over the weekend, all weekend flow internalised
- 2026-08-20 — Wedbush top-up / IOC-limit config live
- 2026-09-02 — Corey Pritchard added to the shared channel
- 2026-09-23 — NOMURA_SW_WB live market
- 2026-09-28 — Big book XAU Invast to LMAX realignment booked
- 2026-10-17 — Weekend reboot cascade left hedgers down ~2.5h (P2 RCA)
