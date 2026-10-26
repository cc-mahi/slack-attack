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
last_catchup: 2026-10-26T08:05:16Z
status: active
---

## Now
A Saturday 2026-10-17 reboot cascade (Hazelcast, MySQL connections) kept the Insti, BigBook and CFD hedgers down ~2.5h, and the Sunday open cancelled 391 orders on a cold order process; both stem from weekend restarts and have an RCA / dev ticket.
Exinity is mid-migration of its LP stack from Hidden Road to Wedbush LPs (top-up/IOC mechanics, Velocity and Nomura going live) and is chasing a run of pricing-spike, book-break and alerting asks.
Open on Mahi: re-setting per-book PnL-drop alerts, XAU position realignment using the CLIENTS book, the TradersHub A-book move, and an XCUUSD spread decision.
Compass 26.4 went on over the 2026-10-24/25 weekend; signalProcessFI1 on trading-1 overflowed and was restarted Monday 2026-10-26; weekend reliability matters more as Exinity plans weekend crypto pricing.

## Streams

### compass-26-4-upgrade — Compass 26.4 upgrade and post-upgrade signal overflow
status: open · since: 2026-10-23 · last: 2026-10-26
State: Leonardo told Exinity on 2026-10-23 that Compass would be upgraded to 26.4 over the weekend, applied at each host's weekly reboot (change CHG-2610-VSHM, Fri 17:00Z to Sun 05:20Z), with monitoring over the open; no Exinity reply seen. On Mon 2026-10-26 07:39 Cameron posted in #internal-exinity that signalProcessFI1 on trading-1 went down on an IFMSslidWndwCbackStream overflow (PagerDuty incident); it stayed up after a manual restart and is being looked into.
Next: Cameron to find the cause of the signalProcessFI1 overflow and whether it relates to the 26.4 upgrade.
Refs: https://mahifx.slack.com/archives/C0456LSHQQK/p1792760362955399 https://mahifx.slack.com/archives/C040V9LNKT5/p1793000364921949


### pnl-drop-alerts — Per-book PnL-drop alerts and alert email restoration
status: open · since: 2026-09-18 · last: 2026-10-22
State: Matt asked for book-level loss alerts; thresholds given 2026-10-06 (A-Book, SI FX, SI FX Insti below $1K/day, Big Boys $2.5K, DK Inventory $5K) plus an alert when LIQUIDITY_POOL_LDN exposure is above zero (top-up used) and restoration of the old email alerts (hedger throttle, VaR, FIX connection, A/B-book rejections). Alerts went live 2026-10-08 but froze systemStateMonitor for ~2 min per firing, so they were reverted (Zendesk 23617); the fix was deployed 2026-10-14. On 2026-10-20 Rory and Matt called and covered all email alerts Exinity wants back; Rory restarted systemStateMonitor (Matt approved, no trading impact) to pick up the new PnL alerting, and the 24h A-Book alerts fired and Matt confirmed receipt. Rory flagged A-Book CLIENTS_NET averaging ~10 alerts a day earlier. On 2026-10-22 Rory asked again to restart systemStateMonitor to pick up new alerting; Mukhammad (overnight) asked whether the restart affects order execution, no answer seen.
Next: Mahi (Rory) to answer Mukhammad's execution-impact question before restarting, and confirm the other books' PnL alerts and the LP-exposure alert are live; email-alert restoration still to be put in place.
Refs: https://mahifx.slack.com/archives/C0456LSHQQK/p1789753758017939 https://mahifx.slack.com/archives/C0456LSHQQK/p1792052573269699 https://mahifx.slack.com/archives/C0456LSHQQK/p1792511678868259 https://mahifx.slack.com/archives/C0456LSHQQK/p1792683656578339


### yield-sims-giraffe — Yield simulations on Exinity trade datasets
status: open · since: 2026-10-05 · last: 2026-10-20
State: On 2026-10-20 Matt sent another UTC+3 sim request (TRAD-2510 attachments); Rory will confirm when run and said the benchmark is the aggregate of the LP feeds in referencePriceMarketSelectors. On 2026-10-19 Matt sent a new October test-data workbook for a quick-turnaround yield sim, asking for a UTC+3 run as well because of a 'DST correction' in its UTC+2 timestamps; Rory confirmed the data aligned and posted the sim Echo link the same afternoon (done unless Matt has questions). Earlier, Keshav asked for simulations on three GMT+3 datasets. Rory found about half the trades are 20 to 40 pips or $19-30 off the Mahi retail mid, in blocks; Louie says they traded on a different LP, and George confirmed TradePrice is fill price and TransactTime is GMT+3 execution time. George suggested excluding outliers; Rory shows a non-trivial share is off market, so the sims have not run.
Next: Rory to run and report the 2026-10-20 sim; Matt to review the 2026-10-19 sim; Exinity (George/Keshav) to decide on excluding or correcting off-market trades in the earlier datasets.
Refs: https://mahifx.slack.com/archives/C0456LSHQQK/p1791216865711639 https://mahifx.slack.com/archives/C0456LSHQQK/p1791893099757919 https://mahifx.slack.com/archives/C0456LSHQQK/p1792509715236449


### weekend-ops-reliability — Weekend restarts, FIX session windows, hedger recovery
status: open · since: 2026-08-17 · last: 2026-10-19
State: Mon 2026-10-19 Liam raised the DB connection limit to 2048 and restarted replica DBs (change CHG-2610-VP5A, 15:40-16:30Z, self-approved), and moved NSCA to daemon mode to stop Nagios alert storms. Weekend reboots repeatedly leave things down. After the 2026-08-22 reboot ~25 processes were missed; components failed again 2026-09-12; STRD_PARTNER crypto pricing did not publish at weekends (fixed 2026-09-23). On Sat 2026-10-17 the trading-1 reboot (07:36Z) left clientDistributionGateway1 dead (duplicate Hazelcast shard ID 1533 after trading-2's node ran out of 2 GB heap; trading-2 missed its 07:50Z slot and rebooted 08:16Z for the kernel patch, admin-1 rebooted twice) and trading-1 MySQL hit 1512/1536 connections, so the Insti, BigBook and CFD hybrid hedgers were down 08:15 to ~10:55Z. James restarted all Hazelcast nodes and raised max_connections to 2048; Justin restarted the hedgers; a rebase bug (not hedger-related) showed a -42k PnL, fixed by a MahiWebstack commit (about -3k after). RCA written (P2, status open). The Friday 21:00Z to Sunday 21:00Z FIX logout of the ECN/ECNARU/PROECNARU/STRD/TE sessions (earlier flagged by Nathan) is Exinity's normal weekly cycle, seen the same the prior weekend, and the bare TCP connects every 10s from Exinity IPs are a health probe. Exinity mirrors Mahi's nightly offline window (07:00 to 09:00 UTC). Daniel says Exinity is comfortable self-monitoring but plans weekend crypto pricing.
Next: Mahi to raise the trading-2 hazelcastNode heap above 2 GB and break down MySQL connections on trading-1 (limit raise done 2026-10-19); Daniel/Kate to revisit weekend support when weekend crypto starts.
Refs: https://mahifx.slack.com/archives/C0456LSHQQK/p1786976101361259 https://mahifx.slack.com/archives/C0456LSHQQK/p1791752884902819 https://mahifx.slack.com/archives/C040V9LNKT5/p1792233233302349 https://mahifx.slack.com/archives/C040V9LNKT5/p1792424073139469


### sunday-open-cancels — Last-look latency cancels at Sunday FX open
status: open · since: 2026-10-18 · last: 2026-10-18
State: Samuel reported cancels on several instruments with "Forcibly cancelled order due to excessive internal latency" (last-look delay overran by ~1257ms). Nathan explained 391 orders received 21:15:00 to 21:15:03 UTC on Sunday 2026-10-18 were cancelled by the internal latency safeguard because the order-handling process, restarted over the weekend, had not warmed up and queued orders; speed was normal from 21:15:04 (about four seconds affected, no further cancels). Tied to the weekend restarts above.
Next: Mahi dev to review process warm-up after restart (ticket raised by Nathan).
Refs: https://mahifx.slack.com/archives/C0456LSHQQK/p1792359440287539


### ld-network-route28 — Beeks LD network incident and unconfirmed Route28 AVAX order
status: open · since: 2026-10-16 · last: 2026-10-16
State: On 2026-10-16 Liam posted a networking incident in the LD environment (10:33 BST, recovery 11:47, resolved 12:30). hybridHedgerCFD1 went down on an order breach after a Route28 AVAX/USD order (99 AVAX, 012e1d2mn2, sent 10:01Z) got no confirmation; Kate asked Exinity to check with Route28 whether it filled, with the FIX log, and brought the hedger back up accepting a small risk if the fill must be booked and hedged. No Exinity answer seen.
Next: Exinity to confirm whether Route28 filled order 012e1d2mn2.
Refs: https://mahifx.slack.com/archives/C0456LSHQQK/p1792143223051249 https://mahifx.slack.com/archives/C0456LSHQQK/p1792148922388959


### insti-exotics-pricing — Exotic pairs unpriced on Distribution_Insti_LDN
status: open · since: 2026-10-15 · last: 2026-10-16
State: Mukhammad asked why exotics (AUDNOK, AUDSEK etc.) are not priced on the Insti streams. Shyam traced it to the Hidden Road to Wedbush LPs SW switch (live 21 Aug): AUDNOK/CHFNOK only have Jane Street, blank 21:00-00:00 UTC daily; AUDSEK and CHFSGD have no Wedbush LP and are unpriced since 21 Aug; TRYJPY, AUDSGD, ZARJPY go blank after the 21:00 rollover for up to an hour or more. Mahi offered adding UBS (and LMAX for EURMXN); Mukhammad will confirm with his team. Shyam also reported the hedger back up and is looking into pricing (overnight 2026-10-15/16, cause not stated).
Next: Exinity to confirm whether to add UBS/LMAX for the exotics.
Refs: https://mahifx.slack.com/archives/C0456LSHQQK/p1792107598604319 https://mahifx.slack.com/archives/C0456LSHQQK/p1792111952713259


### order-reject-queries — Reject and fill investigations
status: open · since: 2026-09-21 · last: 2026-10-15
State: On 2026-10-01 Louie reported an urgent quote disconnect; Kate showed all Mahi sessions stayed up 00:06:52 to 00:35:33 UTC and the logged TARGET_QUOTE_Mahi_ECN session (FXTM) is not Mahi's, so it is downstream in Exinity's bridge. On 2026-10-06 Christian asked why a CL1USD take-profit rejected three times NO_PRICE/EXPIRED after a WTI spike; Rory explained pricing stayed indicative until 13:01:43 UTC after the LP stopped quoting and that Mahi does not hold pending TP/SL orders (immediate market orders), so the bridge must retry. On 2026-10-09 Christian asked for help reading FIX logs and Rory asked what he needs. Mukhammad's 2026-10-02 XAU rejects on API_111000023 had a Shyam acknowledgement but no outcome seen. On 2026-10-15 Matt asked about slippage on a 3oz XAUUSD market buy; Nathan showed the offer ticked up $0.04 during the 20ms last-look hold on the Top Four execution profile (price improvement off, so fill at the worse-for-client end-of-window price), $0.12 total.
Next: Christian to say what he needs from the FIX logs; Exinity to check its bridge retry behaviour.
Refs: https://mahifx.slack.com/archives/C0456LSHQQK/p1790857668546679 https://mahifx.slack.com/archives/C0456LSHQQK/p1791304956108509 https://mahifx.slack.com/archives/C0456LSHQQK/p1791563954367589 https://mahifx.slack.com/archives/C0456LSHQQK/p1792095434905469


### xau-book-realignment — XAU position breaks across A House, Big House and Clients Net
status: open · since: 2026-09-25 · last: 2026-10-14
State: The Big House vs Big Clients Net XAU break (an Invast to LMAX move on 2026-05-07 booked to the wrong book) was fixed on 2026-09-28 by Rory with a six-row import into BIG_HEDGING_WASHBOOK_LDN and BIG_HOUSE, with the Big hedger off, plus a 14oz follow-up; Daniel confirmed it looked right. Separately, Mukhammad raised a 1.13k oz visual break between A House and Clients Net (not real risk, per Nathan, who supplied a realignment CSV based on A_HOUSE). On 2026-10-01 Daniel asked for the adjustment to use the CLIENTS book as source of truth instead; Rory said Mahi would look, and Daniel chased on 2026-10-14 with no reply seen.
Next: Mahi (Rory/Nathan) to produce adjustments using CLIENTS as the reference and reply to Daniel's 2026-10-14 chase.
Refs: https://mahifx.slack.com/archives/C0456LSHQQK/p1790329597165279 https://mahifx.slack.com/archives/C0456LSHQQK/p1790613838734949 https://mahifx.slack.com/archives/C0456LSHQQK/p1790555345540849 https://mahifx.slack.com/archives/C0456LSHQQK/p1791976466451139


### insti-book-moves — Insti routing, tag forwarding and position moves
status: open · since: 2026-08-31 · last: 2026-10-12
State: PrimeXM tag forwarding on the CONNECT_FILLET stream (2026-08-31) was confirmed by Daria to keep landing in BIG_INSTI_CLIENTS_1 as long as new tags avoid the wildcard risk-splitting counterparties. Matt moved an 11.35k oz CL1 position into A Insti Hedging Manual in September (Rory: PnL cannot be backdated, historic trade price can be used). On 2026-10-02 William closed an LMAX XAU position in 100oz clips due to a $2M LMAX volume cap. On 2026-10-12 Christian asked to move TradersHub (111000023) to A-book and open exposure at Wedbush; Nathan promised confirmation and help with the adjustment before EOD, no outcome seen.
Next: Nathan to confirm the steps/books and help with the TradersHub adjustment.
Refs: https://mahifx.slack.com/archives/C0456LSHQQK/p1788203770663179 https://mahifx.slack.com/archives/C0456LSHQQK/p1789471167917609 https://mahifx.slack.com/archives/C0456LSHQQK/p1791828427289149


### pricing-spikes-widening — Spiky and wide pricing complaints
status: open · since: 2026-09-01 · last: 2026-10-09
State: Sep 1 Wagyu spikes at the open traced to Nomura via the Market Width Minimum Spread (MWMS) references; Exinity is backtesting adding Wedbush LPs to MWMS (Kate to check the sims ran). US30 widening on 2026-09-23 was MWMS tracking Velocity (Cameron Hughes set it to 100, Corey confirmed better). NZD/CHF/NOK cross spikes were treated with order-book rounding and lower skew ceilings (0.3 to 0.05 pips, 2026-09-25). EURUSD spikes on 2026-10-07 were skew plus Invast's bid crossing the Wedbush offers in the mid; skew was cut (ceiling 0.6 to 0.4, SNG 1.3 to 0.5, SNGMON 2.7 to 0.5) and Mahi proposed dropping Invast from the EURUSD mid, which Daniel declined on 2026-10-09. A 2026-09-29 LP feed stoppage (ticks stopped at Wedbush and Invast ~14:52) resumed after about three hours.
Next: Exinity to say whether spikiness persists; Wedbush-in-MWMS backtest result unconfirmed.
Refs: https://mahifx.slack.com/archives/C0456LSHQQK/p1788299416706969 https://mahifx.slack.com/archives/C0456LSHQQK/p1790270255985109 https://mahifx.slack.com/archives/C0456LSHQQK/p1791468162700719 https://mahifx.slack.com/archives/C0456LSHQQK/p1791555149344069


### velocity-nomura-onboard — Velocity (VTI C2C) and Nomura Elysium onboarding
status: open · since: 2026-08-21 · last: 2026-10-08
State: William set up the Velocity VTI C2C connection with Elysium reporting (config added 2026-09-02, FIX passwords awaited), tested Nomura's Elysium reporting leg on 2026-09-22 and made NOMURA_SW_WB a live market on 2026-09-23. On 2026-10-01 William ran in-out XAUUSD/EURUSD test trades on VELOCITY_WB and sent the FIX messages to Wedbush by email; on 2026-10-08 Louie asked if Velocity_WB was subscribed for his own test trade and Rory confirmed pricing is flowing. Wedbush sign-off not seen.
Next: Louie's test trade result; Wedbush conformance sign-off.
Refs: https://mahifx.slack.com/archives/C0456LSHQQK/p1787314659822969 https://mahifx.slack.com/archives/C0456LSHQQK/p1789999351066319 https://mahifx.slack.com/archives/C0456LSHQQK/p1790864738809539 https://mahifx.slack.com/archives/C0456LSHQQK/p1791462553978629


### wedbush-lp-migration — Hidden Road to Wedbush LPs, IOC/top-up mechanics
status: open · since: 2026-08-05 · last: 2026-10-01
State: Wedbush LPs do not take FOK/market orders, so on 2026-08-19 Daniel chose top-up enabled with IOC Limits at very high slippage for STP clients on the 'Wedbush LPs SW' list; Nathan applied it at EOD 2026-08-20 and the first FoK AUDUSD order brokered cleanly. Reference Price Market Selectors all moved to Wedbush on 2026-09-15 and CLIENT_PRICE_LDN pricers were restarted EOD 2026-10-01 for the Hidden Road to Wedbush switch. On 2026-09-17 a top-up left 200oz residual (Jane Street cancelled three 200oz attempts, Compass topped up at 4287.45, booked on LIQUIDITY_POOL_LDN); Louie said Exinity cannot carry that risk for 111000021/22/26, so Rory set Allow Top-Up to No on the EXINITY_CONNECT_CHUCK rule. How to book the residual 200oz was still being worked out in thread.
Next: Exinity to book/move the 200oz residual; confirm where top-up should be on versus off.
Refs: https://mahifx.slack.com/archives/C0456LSHQQK/p1787146976800389 https://mahifx.slack.com/archives/C0456LSHQQK/p1789637820930659 https://mahifx.slack.com/archives/C0456LSHQQK/p1790858852806429


### compass-config-questions — Config and UI how-it-works questions
status: watching · since: 2026-09-09 · last: 2026-10-14
State: Shyam explained Signal Return Benchmark (skew PnL midpoint, normalisation) versus Reference Price Mid (model mid from reference markets, yield markouts) on 2026-09-22, after Daniel found T50USD/SPMUSD/GDIUSD have no benchmark. Rory confirmed on 2026-10-13 that execution rule changes are dynamic and on 2026-10-14 Shyam explained SI Insti XAUUSD hedging (client-trade rules 5/10/30s; risk rules at 48s/60s/200s with 10oz/40oz thresholds). Dashboard glitches (GBPSEK shown unpriced 2026-10-04, Trading Overview stats 2026-10-12) were UI-only and fixed; Louie's manual-order error on 2026-09-21 was a 37s browser clock skew. Daniel asked on 2026-10-06 for AEXEUR/HISKHKD/S30SGD to be checked as enabled; no reply seen.
Next: Mahi to confirm AEXEUR/HISKHKD/S30SGD enablement.
Refs: https://mahifx.slack.com/archives/C0456LSHQQK/p1790076650019729 https://mahifx.slack.com/archives/C0456LSHQQK/p1791263973364079 https://mahifx.slack.com/archives/C0456LSHQQK/p1792005318722349


### copper-xcu-pricing — Copper (XCUUSD) stack and execution routing
status: watching · since: 2026-08-21 · last: 2026-10-05
State: Invast copper orders arrived at 5dp instead of 4dp (2026-08-21) causing rejects; Isaac set a temporary internalise rule. On 2026-09-21 XCUUSD's stack was one 50-unit layer at a $1 spread, so a 300-unit order cancelled; Nathan deepened the stack to ~15k and left TOB spread at $1. The 2026-09-25 fill at 7.1247 was expected from config (pool price published, internalised against the wider RETAIL market). Exinity wants XCU priced and executed on the pool, so on 2026-10-05 Rory copied the BACKUP rule into the multiChannelConfig and added the _CFD channel to the CFD Internalise rule; both are in place.
Next: Exinity to decide the XCUUSD TOB spread on CLIENT_PRICE_RETAIL_LDN.
Refs: https://mahifx.slack.com/archives/C0456LSHQQK/p1787324960613979 https://mahifx.slack.com/archives/C0456LSHQQK/p1789964680045919 https://mahifx.slack.com/archives/C0456LSHQQK/p1791218263170469

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
