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
last_catchup: 2026-11-12T08:14:50Z
status: active
---

## Now
Newest: signal-process errors recurred 2026-11-12 (processes restored, dev fix pending), and an institutional client's 500ms order-expiry complaint found no Mahi-side cause. Reactive price feeds (BAML, DB, Jane Street, Jump, Nomura) went silent 2026-11-09 15:53-17:05Z with sessions still logged on; Mahi added stale-price alerts for several LPs 2026-11-10. Newest: the STRDPARTNER order session sat disabled from the Saturday 2026-11-07 open until Nathan re-enabled it Monday 2026-11-09 (sequence-reset logon race, no alert fired); RCA follow-up owed. Internally, NFP showed no LR and weak skew on B_CLIENTS, and an adaptive-skew sim needs an owner.
Weekend restarts caused the 2026-10-17 hedger outage (~2.5h) and 391 cancelled orders at the Sunday open; RCA / dev ticket exist.
Exinity is mid-migration of its LP stack from Hidden Road to Wedbush LPs (top-up/IOC mechanics, Velocity and Nomura going live) and is chasing a run of pricing-spike, book-break and alerting asks.
Open on Mahi: per-book PnL-drop alerts, XAU position realignment using the CLIENTS book, the TradersHub A-book move and an XCUUSD spread decision; Compass 26.4 (2026-10-24/25) caused signalProcessFI1 overflows, and weekend reliability matters as Exinity plans weekend crypto pricing.

## Streams

### signal-process-alerts — Alerts on signal processes, no execution impact
status: open · since: 2026-11-05 · last: 2026-11-12
State: On 2026-11-12 ~04:34Z Samuel reported signal errors again (screenshot); Nathan brought both processes back up by 04:45Z and said at 04:51Z that Mahi knows the cause and dev is working on a fix. On 2026-11-05 ~04:49Z Mukhammad asked Mahi to check a set of alerts (screenshot, not readable). Daria said they should be fixed shortly and, asked about execution impact, said there was no noticeable trading impact because these processes produce signals and are not in the execution pipeline. Which processes alerted is not stated; may relate to the 2026-10-26 signalProcessFI1 overflow. On 2026-11-06 ~01:30Z Mukhammad reported another error (screenshot, not readable); Nathan restored the process within minutes.
Next: Mahi dev to deliver the fix for the recurring signal-process errors and tell Samuel the cause.
Refs: https://mahifx.slack.com/archives/C0456LSHQQK/p1793854172360089 https://mahifx.slack.com/archives/C0456LSHQQK/p1793928885999739 https://mahifx.slack.com/archives/C0456LSHQQK/p1794458029345139 https://mahifx.slack.com/archives/C0456LSHQQK/p1794459060239709


### insti-500ms-expiry — Institutional client sees ~500ms before orders expire
status: open · since: 2026-11-11 · last: 2026-11-11
State: Louie relayed an institutional client's complaint of a 500ms delay on almost all orders (XAUUSD limit orders via FIX, three examples 2026-11-11 14:37-15:08Z). Rory found nothing on Mahi's side adding 500ms: the first order arrived 14:37:26.633 and was cancelled at .635 (limit through price, 20ms last look), so the 'expired' the client saw came ~500ms later; the other two never appear in Mahi logs. Louie will check them on Exinity's side.
Next: Louie to check the 14:40 and 15:08 orders on Exinity's side.
Refs: https://mahifx.slack.com/archives/C0456LSHQQK/p1794419081666329 https://mahifx.slack.com/archives/C0456LSHQQK/p1794422570877219


### reactive-feed-gap — Reactive LP price feeds stopped, no alerting
status: open · since: 2026-11-10 · last: 2026-11-10
State: Matt A asked 2026-11-10 whether Reactive's 2026-11-09 API incident (15:43-18:03 UTC) affected Exinity's connections. Nathan found the Reactive-routed feeds (BAML, Deutsche Bank, Jane Street, Jump, Nomura) stopped pricing 15:53:21Z and resumed 17:05:53Z while sessions stayed logged on; no orders were attempted at those venues and hedging continued through other LPs. Matt then asked whether any alert covers a sustained feed stop on this connection, which matters because the sessions never dropped. At 11:23Z Rory bounced systemStateMonitor with stale-pricing alerts added for several LPs (staleMarketDataFeed.alertThreshold) per Matt's request (internal note); no confirmation to Exinity seen in the shared channel.
Next: Mahi to tell Exinity the stale-price alerts are live and which LPs they cover.
Refs: https://mahifx.slack.com/archives/C0456LSHQQK/p1794292235121349 https://mahifx.slack.com/archives/C040V9LNKT5/p1794309815194049


### xau-cpi-slippage — XAUUSD 900oz fill slippage at CPI
status: open · since: 2026-11-10 · last: 2026-11-10
State: Louie flagged a 900oz XAUUSD fill (API_111000021, DISTRIBUTION_INSTI_LDN, ~13:30Z) that passed on $60 of spread. Rory found execution as expected: the pricing model widened its deeper size levels sharply just after the CPI release (100oz at 4066.22, 400 at 4055.99, 400 at 4011.94, average 4037.55), CLIENT_PRICE_LDN stayed two-sided with no drop-out, and depth across several LPs was sufficient. Louie accepted.
Refs: https://mahifx.slack.com/archives/C0456LSHQQK/p1794324361585969 https://mahifx.slack.com/archives/C0456LSHQQK/p1794330199036949


### strd-partner-logon-gap — STRDPARTNER session disabled after sequence reset
status: open · since: 2026-11-09 · last: 2026-11-09
State: Samuel reported 2026-11-09 ~02:17Z that orders were not going through on ExinitySTRDPARTNER. Nathan re-enabled the session (~03:01Z) and explained at 06:20Z: the session's sequence numbers reset to 1 at the weekly start (Saturday 10:00 UTC); Exinity's side rejected the reply as MsgSeqNum too low and dropped within 4ms; Mahi's gateway treated the half-open logon as faulty and disabled the session, which nothing re-enables automatically. Exinity retried every ~2s and got "session is disabled" from the Saturday 2026-11-07 open until Monday, so orders were down roughly two days. Mahi is reviewing the mechanism and why no alert fired.
Next: Nathan to report back on the review and the missing alert; fix so a fast disconnect cannot leave the session disabled.
Refs: https://mahifx.slack.com/archives/C0456LSHQQK/p1794190632412229 https://mahifx.slack.com/archives/C0456LSHQQK/p1794205214970219


### nfp-lr-skew-review — NFP skew and missing LR on B_CLIENTS (internal)
status: open · since: 2026-11-06 · last: 2026-11-06
State: Internal only. Will Carter found that over 13:30-13:33 UTC on NFP (2026-11-06) B_CLIENTS booked about $2.1k skew (~$10/M on $203M, corrected from an initial $609M figure) and no LR, well below comparators, and asked whether LR is off by design or a gap and for an owner for an adaptive-skew sim replay of the release to take to the client. He also messaged Exinity's lead (Nick) about skew underperformance; Kate says he replies poorly on Slack, so the catch-up is deferred to next week. No owner named for the sim yet.
Next: Someone to confirm LR config on B_CLIENTS and own the adaptive-skew sim; Will to catch up with Exinity next week.
Refs: https://mahifx.slack.com/archives/C040V9LNKT5/p1793975304979759 https://mahifx.slack.com/archives/C040V9LNKT5/p1793980122754249


### adausd-insti-rounding — Stale ADAUSD/DOGUSD on insti feeds
status: open · since: 2026-11-06 · last: 2026-11-06
State: On 2026-11-06 ~03:14Z Mukhammad reported ADAUSD insti pricing stale on the Wagyu, Chuck and Fillet channels (retail fine). Nathan found the insti channels price from the liquidity pool, which rounded ADAUSD to 3 decimals so the price rarely moved and often showed bid equal to offer; DOGUSD was affected the same way. Config now sets 5 decimals but needs a process restart, so it takes effect after the weekend reboot. Mukhammad acknowledged.
Next: Mahi to confirm the 5dp pool rounding is live after the weekend reboot.
Refs: https://mahifx.slack.com/archives/C0456LSHQQK/p1793934874890119 https://mahifx.slack.com/archives/C0456LSHQQK/p1793937644348509


### strd-feed-drops — STRD connector and pricing drop-outs
status: open · since: 2026-10-28 · last: 2026-11-06
State: On 2026-11-06 Louie reported offline XAUUSD orders at 14:09Z on ExinitySTRD-Orders; Rory found they reached Mahi's gateway 3.2-4.0s after their SendingTime, then acked and filled within ~40ms with other sessions normal, so the delay arose before the gateway and Mahi is still looking into the cause (Louie accepted). On 2026-11-06 Mahi added USDTHB to the reference-price override after it stopped ticking for ~10 min (see pricing-spikes-widening). Matt's 2026-10-28 USDJPY no-pricing report was withdrawn within a minute. At 02:05Z on 2026-10-29 Samuel reported errors (screenshot, not readable); Nathan said all was good and Mahi's team was already bringing processes up, but the cause is still under investigation.
Next: Mahi (Nathan) to report the cause of the 2026-10-29 errors to Samuel; Mahi (Rory) to report why the 2026-11-06 XAU orders arrived 3-4s late.
Refs: https://mahifx.slack.com/archives/C0456LSHQQK/p1793222374723979 https://mahifx.slack.com/archives/C0456LSHQQK/p1793239541468319 https://mahifx.slack.com/archives/C0456LSHQQK/p1793977409207179


### pricing-spikes-widening — Spiky and wide pricing complaints
status: open · since: 2026-09-01 · last: 2026-11-06
State: On 2026-11-06 ~20:35Z Christian reported USDTHB not ticking for almost 10 min with poor pricing; Cameron Hughes added USDTHB to the referencePriceMarketSelectors override (internal note 20:51Z) and asked Christian to recheck, no reply seen. Sep 1 Wagyu spikes traced to Nomura via the Market Width Minimum Spread (MWMS) references; Exinity is backtesting adding Wedbush LPs to MWMS. EURUSD spikes on 2026-10-07 were skew plus Invast's bid crossing the Wedbush offers in the mid; skew was cut and Mahi proposed dropping Invast from the EURUSD mid, which Daniel declined on 2026-10-09. On 2026-10-27 Christian reported poor LP pricing 2026-10-26 20:45-22:00; Kate found the market itself was wide over the NY rollover (GBPCHF LPs 25-30 pips 21:00-22:00 UTC, several LPs not quoting, normal by ~22:05); Mahi stayed firm and the mid held.
Next: Christian to confirm USDTHB now ticks; Exinity to say whether spikiness persists and to check rollover width with Wedbush/LPs (and why Barclays, DB, HSBC, Velocity don't stream GBPCHF) or send a timestamp; Wedbush-in-MWMS backtest result unconfirmed.
Refs: https://mahifx.slack.com/archives/C0456LSHQQK/p1788299416706969 https://mahifx.slack.com/archives/C0456LSHQQK/p1793100609912989 https://mahifx.slack.com/archives/C0456LSHQQK/p1793127985564209 https://mahifx.slack.com/archives/C0456LSHQQK/p1793997336044029


### order-reject-queries — Reject and fill investigations
status: open · since: 2026-09-21 · last: 2026-11-04
State: Open: Christian's 2026-10-09 FIX-log help request awaits his reply; Mukhammad's 2026-10-02 XAU rejects had no outcome seen. Resolved: 2026-10-01 quote disconnect was Exinity's bridge; 2026-10-06 CL1USD TP rejects were indicative pricing after the LP stopped quoting (Mahi holds no pending TP/SL, so the bridge must retry); 2026-10-15 3oz XAUUSD slippage was a $0.04 offer tick in the 20ms last-look hold. On 2026-11-02 a client TP on DOWUSD was rejected ('Internalisation Quantity greater than Published', published quantity 0 as all LPs had stopped pricing); on 2026-11-04 API_111000021's cancels on EXINITY_CONNECT_WAGYU were 800oz limit buys against 100oz at top of book.
Next: Christian to say what he needs from the FIX logs; Exinity to check its bridge retry behaviour.
Refs: https://mahifx.slack.com/archives/C0456LSHQQK/p1790857668546679 https://mahifx.slack.com/archives/C0456LSHQQK/p1791304956108509 https://mahifx.slack.com/archives/C0456LSHQQK/p1791563954367589 https://mahifx.slack.com/archives/C0456LSHQQK/p1793756635298589


### echo-tob-crash — Echo TOB errors on historical dates
status: open · since: 2026-11-03 · last: 2026-11-03
State: On 2026-11-03 Daniel reported Echo TOB crashing when EURUSD is selected for 2026-10-21 (recent days work). Daria asked if 2026-10-25 also failed (a weekend, may explain it) and pointed him to Compass price forensics meanwhile; no fix or root cause yet.
Next: Mahi (Daria) to investigate the Echo TOB error; Daniel to say whether 2026-10-25 also fails.
Refs: https://mahifx.slack.com/archives/C0456LSHQQK/p1793686208763259 https://mahifx.slack.com/archives/C0456LSHQQK/p1793686599906029


### admin-feed-multicast — Multicast change undo to restore admin feeds
status: open · since: 2026-11-02 · last: 2026-11-02
State: Saturday 2026-10-31's multicast change broke the admin feeds; Liam posted change CHG-2611-0Z3D (approved) to undo it Mon 2026-11-02 22:00-23:00Z. Internal only, no Exinity thread seen.
Next: Confirm admin feeds restored after the 22:00Z window.
Refs: https://mahifx.slack.com/archives/C040V9LNKT5/p1793646965293749


### bbook-weekend-pnl — False -1.7M B-book PnL at Sunday open
status: open · since: 2026-11-01 · last: 2026-11-01
State: On 2026-11-01 ~22:23Z Mukhammad asked whether the B-book PnL of -1.7M when rebased from Friday close was real, since XAU had not reopened (rebased from Sunday close it was fine). Shyam said it was not an actual loss: it reverted at the metals open once live pricing resumed, and Mahi is looking into the pricing used to mark the book over the weekend. Mukhammad confirmed numbers looked better after the gold open.
Next: Mahi (Shyam) to report what weekend marking price caused the false -1.7M.
Refs: https://mahifx.slack.com/archives/C0456LSHQQK/p1793571776435089 https://mahifx.slack.com/archives/C0456LSHQQK/p1793575936910949


### centroid-fok-conformance — Centroid conformance: FOK brokered orders expire
status: open · since: 2026-10-29 · last: 2026-10-30
State: During Centroid/Mahi conformance testing on 2026-10-28 Matt saw an A-Book XAU/USD FOK market order cancelled (EXPIRED) on the Centroid connection while a PrimeXM FOK filled. Kate explained the Centroid order was set to broker by the channel/execution rule but the liquidity pool has no FOK-capable market for gold, so it expired before reaching an LP; the PXM order was internalised. On 2026-10-30 Kate explained routing: execution rules are picked by trading account, and the Centroid connection (account 001) lands on the Exinity Connect rule and Chuck profile, which has top-up off, whereas the MT4/MT5 A-book STP FOKs that fill (account 65280, A-BOOK rule) have Allow Top Up on. Non-FOK brokering works; the only FOK cancels were the 112 Centroid test orders. Daniel asked whether Centroid can be set up like STP.
Next: Mahi (Kate) offered on 2026-10-30 to configure Allow Top Up on the Chuck profile; Exinity (Daniel/Matt) to say yes or change Centroid-side config so FOK is not brokered to WB.
Refs: https://mahifx.slack.com/archives/C0456LSHQQK/p1793264343496069 https://mahifx.slack.com/archives/C0456LSHQQK/p1793365009754819


### wedbush-lp-migration — Hidden Road to Wedbush LPs, IOC/top-up mechanics
status: open · since: 2026-08-05 · last: 2026-10-30
State: Wedbush LPs do not take FOK/market orders, so top-up with IOC Limits at very high slippage was applied for STP clients on 'Wedbush LPs SW' (EOD 2026-08-20). Reference Price Market Selectors moved to Wedbush 2026-09-15; pricers restarted EOD 2026-10-01. On 2026-09-17 a top-up left a 200oz residual (booked on LIQUIDITY_POOL_LDN); Louie said Exinity cannot carry that risk for 111000021/22/26, so Rory set Allow Top-Up to No on the EXINITY_CONNECT_CHUCK rule. How to book the residual was still being worked out.
Next: Exinity to book/move the 200oz residual; confirm where top-up should be on versus off (Kate offered 2026-10-30 to enable it on Chuck, see centroid-fok-conformance).
Refs: https://mahifx.slack.com/archives/C0456LSHQQK/p1787146976800389 https://mahifx.slack.com/archives/C0456LSHQQK/p1789637820930659 https://mahifx.slack.com/archives/C0456LSHQQK/p1793365009754819


### pnl-drop-alerts — Per-book PnL-drop alerts and alert email restoration
status: open · since: 2026-09-18 · last: 2026-10-29
State: Matt chased on 2026-10-29 for an update on the "emergency alerts" (no reply seen). He asked for per-book loss alerts (thresholds $1K-$5K/day given 2026-10-06), an alert when LIQUIDITY_POOL_LDN exposure is above zero, and restoration of old email alerts (hedger throttle, VaR, FIX connection, A/B-book rejections). Alerts went live 2026-10-08 but froze systemStateMonitor ~2 min per firing and were reverted (Zendesk 23617); fix deployed 2026-10-14; 24h A-Book alerts fired 2026-10-20. On 2026-10-22 Rory asked to restart systemStateMonitor for new alerting; Mukhammad asked if that affects execution, no answer seen.
Next: Mahi to reply to Matt's 2026-10-29 chase on the emergency alerts; Rory to answer Mukhammad's execution-impact question before restarting, and confirm the other books' PnL alerts and the LP-exposure alert are live; email-alert restoration still to be put in place.
Refs: https://mahifx.slack.com/archives/C0456LSHQQK/p1789753758017939 https://mahifx.slack.com/archives/C0456LSHQQK/p1792511678868259 https://mahifx.slack.com/archives/C0456LSHQQK/p1792683656578339 https://mahifx.slack.com/archives/C0456LSHQQK/p1793265485080539


### compass-26-4-upgrade — Compass 26.4 upgrade and post-upgrade signal overflow
status: open · since: 2026-10-23 · last: 2026-10-26
State: Leonardo told Exinity on 2026-10-23 that Compass would be upgraded to 26.4 over the weekend (change CHG-2610-VSHM, Fri 17:00Z to Sun 05:20Z); no Exinity reply seen. On Mon 2026-10-26 signalProcessFI1 on trading-1 went down on an IFMSslidWndwCbackStream overflow at 07:18Z (PagerDuty incident). Matt asked urgently whether skew on XAUUSD was switched off; Kate replied that skew stayed live apart from the brief restart and a fix was in hand. Andrew Morgan pushed a fix seen in TKY CoE; the overflow recurred (Christian's alert 16:18Z, Kate: process restarted and back up, Mahi gets all alerts too), and Cameron bounced signalProcessFI1 and rolled the fix out to Exinity at ~17:23Z.
Next: Confirm the signalProcessFI1 fix holds (no further overflow alerts) and whether it was caused by the 26.4 upgrade.
Refs: https://mahifx.slack.com/archives/C0456LSHQQK/p1792760362955399 https://mahifx.slack.com/archives/C040V9LNKT5/p1793035385218119


### yield-sims-giraffe — Yield simulations on Exinity trade datasets
status: open · since: 2026-10-05 · last: 2026-10-20
State: On 2026-10-20 Matt sent another UTC+3 sim request (TRAD-2510 attachments); Rory will confirm when run and said the benchmark is the aggregate of the LP feeds in referencePriceMarketSelectors. On 2026-10-19 Matt sent a new October test-data workbook for a quick-turnaround yield sim, asking for a UTC+3 run as well because of a 'DST correction' in its UTC+2 timestamps; Rory ran it the same afternoon. Keshav's three GMT+3 datasets had about half the trades 20 to 40 pips ($19-30) off the Mahi retail mid, in blocks (Louie: different LP; George: TradePrice is fill price, TransactTime GMT+3); George suggested excluding outliers, so those sims have not run.
Next: Rory to run and report the 2026-10-20 sim; Matt to review the 2026-10-19 sim; Exinity (George/Keshav) to decide on excluding or correcting off-market trades in the earlier datasets.
Refs: https://mahifx.slack.com/archives/C0456LSHQQK/p1791216865711639 https://mahifx.slack.com/archives/C0456LSHQQK/p1791893099757919 https://mahifx.slack.com/archives/C0456LSHQQK/p1792509715236449


### weekend-ops-reliability — Weekend restarts, FIX session windows, hedger recovery
status: open · since: 2026-08-17 · last: 2026-10-19
State: Mon 2026-10-19 Liam raised the DB connection limit to 2048 and restarted replica DBs (change CHG-2610-VP5A, 15:40-16:30Z, self-approved), and moved NSCA to daemon mode to stop Nagios alert storms. On Sat 2026-10-17 the trading-1 reboot (07:36Z) left clientDistributionGateway1 dead (duplicate Hazelcast shard ID 1533 after trading-2's node ran out of 2 GB heap) and trading-1 MySQL hit 1512/1536 connections, so the Insti, BigBook and CFD hybrid hedgers were down 08:15 to ~10:55Z. James restarted all Hazelcast nodes and raised max_connections to 2048; Justin restarted the hedgers. RCA written (P2, status open). The Friday 21:00Z to Sunday 21:00Z FIX logout of the ECN/ECNARU/PROECNARU/STRD/TE sessions is Exinity's normal weekly cycle,. Exinity self-monitors but plans weekend crypto pricing.
Next: Mahi to raise the trading-2 hazelcastNode heap above 2 GB and break down MySQL connections on trading-1 (limit raise done 2026-10-19); Daniel/Kate to revisit weekend support when weekend crypto starts.
Refs: https://mahifx.slack.com/archives/C0456LSHQQK/p1786976101361259 https://mahifx.slack.com/archives/C0456LSHQQK/p1791752884902819 https://mahifx.slack.com/archives/C040V9LNKT5/p1792233233302349 https://mahifx.slack.com/archives/C040V9LNKT5/p1792424073139469


### insti-exotics-pricing — Exotic pairs unpriced on Distribution_Insti_LDN
status: open · since: 2026-10-15 · last: 2026-10-16
State: Mukhammad asked why exotics (AUDNOK, AUDSEK etc.) are not priced on the Insti streams. Shyam traced it to the Hidden Road to Wedbush LPs SW switch (live 21 Aug): AUDNOK/CHFNOK only have Jane Street, blank 21:00-00:00 UTC daily; AUDSEK and CHFSGD have no Wedbush LP and are unpriced since 21 Aug; TRYJPY, AUDSGD, ZARJPY go blank after the 21:00 rollover for up to an hour or more. Mahi offered adding UBS (and LMAX for EURMXN); Mukhammad will confirm with his team. Shyam also reported the hedger back up and is looking into pricing (overnight 2026-10-15/16, cause not stated).
Next: Exinity to confirm whether to add UBS/LMAX for the exotics.
Refs: https://mahifx.slack.com/archives/C0456LSHQQK/p1792107598604319 https://mahifx.slack.com/archives/C0456LSHQQK/p1792111952713259


### xau-book-realignment — XAU position breaks across A House, Big House and Clients Net
status: open · since: 2026-09-25 · last: 2026-10-14
State: The Big House vs Big Clients Net XAU break (an Invast to LMAX move on 2026-05-07 booked to the wrong book) was fixed on 2026-09-28 by Rory with a six-row import into BIG_HEDGING_WASHBOOK_LDN and BIG_HOUSE, with the Big hedger off, plus a 14oz follow-up; Daniel confirmed it looked right. Separately, Mukhammad raised a 1.13k oz visual break between A House and Clients Net (not real risk, per Nathan, who supplied a realignment CSV based on A_HOUSE). On 2026-10-01 Daniel asked for the adjustment to use the CLIENTS book as source of truth instead; Rory said Mahi would look, and Daniel chased on 2026-10-14 with no reply seen.
Next: Mahi (Rory/Nathan) to produce adjustments using CLIENTS as the reference and reply to Daniel's 2026-10-14 chase.
Refs: https://mahifx.slack.com/archives/C0456LSHQQK/p1790329597165279 https://mahifx.slack.com/archives/C0456LSHQQK/p1790613838734949 https://mahifx.slack.com/archives/C0456LSHQQK/p1790555345540849 https://mahifx.slack.com/archives/C0456LSHQQK/p1791976466451139


### insti-book-moves — Insti routing, tag forwarding and position moves
status: watching · since: 2026-08-31 · last: 2026-10-12
State: PrimeXM tag forwarding on CONNECT_FILLET keeps landing in BIG_INSTI_CLIENTS_1 if new tags avoid the wildcard risk-splitting counterparties (Daria, 2026-08-31). On 2026-10-12 Christian asked to move TradersHub (111000023) to A-book and open exposure at Wedbush; Nathan promised confirmation and help with the adjustment before EOD, no outcome seen.
Next: Nathan to confirm the steps/books and help with the TradersHub adjustment.
Refs: https://mahifx.slack.com/archives/C0456LSHQQK/p1788203770663179 https://mahifx.slack.com/archives/C0456LSHQQK/p1789471167917609 https://mahifx.slack.com/archives/C0456LSHQQK/p1791828427289149


### compass-config-questions — Config and UI how-it-works questions
status: watching · since: 2026-09-09 · last: 2026-11-11
State: On 2026-11-11 Matt asked how to view order books at a timestamp for a pricing stream; Rory pointed to Compass price forensics (better than Echo TOB; full depth needs Pulse), Matt found the trade-detail widget sufficient, and Rory confirmed price-forensics spreads are per unit (e.g. $60.80 x 900oz); Matt's extra Compass IP (102.115.49.162) was whitelisted ~14:12Z. Shyam explained Signal Return Benchmark (skew PnL midpoint, normalisation) versus Reference Price Mid (model mid from reference markets, yield markouts) on 2026-09-22, after Daniel found T50USD/SPMUSD/GDIUSD have no benchmark. Shyam explained SI Insti XAUUSD hedging rules on 2026-10-14. Daniel asked on 2026-10-06 for AEXEUR/HISKHKD/S30SGD to be checked as enabled; no reply seen.
Next: Mahi to confirm AEXEUR/HISKHKD/S30SGD enablement.
Refs: https://mahifx.slack.com/archives/C0456LSHQQK/p1790076650019729 https://mahifx.slack.com/archives/C0456LSHQQK/p1791263973364079 https://mahifx.slack.com/archives/C0456LSHQQK/p1792005318722349 https://mahifx.slack.com/archives/C0456LSHQQK/p1794394501162529


### velocity-nomura-onboard — Velocity (VTI C2C) and Nomura Elysium onboarding
status: watching · since: 2026-08-21 · last: 2026-10-08
State: No activity since 2026-10-08; downgraded to watching, Wedbush sign-off unconfirmed. William set up the Velocity VTI C2C connection with Elysium reporting (config added 2026-09-02, FIX passwords awaited), tested Nomura's Elysium reporting leg on 2026-09-22 and made NOMURA_SW_WB a live market on 2026-09-23. On 2026-10-01 William ran in-out XAUUSD/EURUSD test trades on VELOCITY_WB and emailed the FIX messages to Wedbush; on 2026-10-08 Rory confirmed Velocity_WB pricing is flowing for Louie's test trade. Wedbush sign-off not seen.
Next: Louie's test trade result; Wedbush conformance sign-off.
Refs: https://mahifx.slack.com/archives/C0456LSHQQK/p1787314659822969 https://mahifx.slack.com/archives/C0456LSHQQK/p1789999351066319 https://mahifx.slack.com/archives/C0456LSHQQK/p1790864738809539 https://mahifx.slack.com/archives/C0456LSHQQK/p1791462553978629


### copper-xcu-pricing — Copper (XCUUSD) stack and execution routing
status: watching · since: 2026-08-21 · last: 2026-10-05
State: Invast copper 5dp-vs-4dp rejects (2026-08-21) got a temporary internalise rule. XCUUSD's one-layer 50-unit stack cancelled a 300-unit order (2026-09-21); Nathan deepened it to ~15k, TOB spread left at $1. On 2026-10-05 Rory copied the BACKUP rule into the multiChannelConfig and added the _CFD channel to the CFD Internalise rule; both are in place.
Next: Exinity to decide the XCUUSD TOB spread on CLIENT_PRICE_RETAIL_LDN.
Refs: https://mahifx.slack.com/archives/C0456LSHQQK/p1787324960613979 https://mahifx.slack.com/archives/C0456LSHQQK/p1789964680045919 https://mahifx.slack.com/archives/C0456LSHQQK/p1791218263170469

### gbpaud-roll-cancels — GBPAUD cancels at rollover (wide-spread suppression)
status: closed · since: 2026-11-11 · last: 2026-11-11 · closed: 2026-11-12
State: Samuel asked why ASV_MT4_STANDARD1_5618035 got GBPAUD cancels at the 2026-11-11 rollover. Shyam: spread widened past the wide-spread-suppression threshold, so the distribution price went indicative and orders cancelled; the bridge retried and filled at 22:24Z once spread normalised. Mahi offered to loosen the rollover WSS for GBPAUD; Samuel said keep as is for now.
Refs: https://mahifx.slack.com/archives/C0456LSHQQK/p1794435903177429 https://mahifx.slack.com/archives/C0456LSHQQK/p1794437737729939

### sunday-open-cancels — Last-look latency cancels at Sunday FX open
status: closed · since: 2026-10-18 · last: 2026-10-18 · closed: 2026-11-12
State: 391 orders at 21:15:00-03Z on Sunday 2026-10-18 were cancelled by the internal-latency safeguard because the weekend-restarted order process had not warmed up; normal from 21:15:04. Dev ticket raised for warm-up; no activity since, assumed resolved.
Refs: https://mahifx.slack.com/archives/C0456LSHQQK/p1792359440287539


### ld-network-route28 — Beeks LD network incident and unconfirmed Route28 AVAX order
status: closed · since: 2026-10-16 · last: 2026-10-16 · closed: 2026-11-12
State: Beeks LD network incident 2026-10-16 (10:33-12:30 BST) took hybridHedgerCFD1 down on an unconfirmed Route28 AVAX order (012e1d2mn2); Kate restarted it accepting a small risk and asked Exinity to check with Route28. No answer seen; no activity since, assumed resolved.
Refs: https://mahifx.slack.com/archives/C0456LSHQQK/p1792143223051249 https://mahifx.slack.com/archives/C0456LSHQQK/p1792148922388959


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
