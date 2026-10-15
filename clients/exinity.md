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
last_catchup: 2026-10-15T13:00:34Z
status: active
---

## Now
Exinity is mid-migration of its LP stack from Hidden Road to Wedbush LPs (top-up/IOC mechanics, Velocity and Nomura going live) and is chasing a run of pricing-spike, book-break and alerting asks.
Open on Mahi: re-setting per-book PnL-drop alerts, XAU position realignment using the CLIENTS book, the TradersHub A-book move, and an XCUUSD spread decision.
Weekend reliability matters more as Exinity plans weekend crypto pricing.

## Streams

### pnl-drop-alerts — Per-book PnL-drop alerts and alert email restoration
status: open · since: 2026-09-18 · last: 2026-10-15
State: Matt asked for book-level loss alerts; thresholds given 2026-10-06 (A-Book, SI FX, SI FX Insti below $1K/day, Big Boys $2.5K, DK Inventory $5K) plus an alert when LIQUIDITY_POOL_LDN exposure is above zero (top-up used) and restoration of the old email alerts (hedger throttle, VaR, FIX connection, A/B-book rejections). Alerts went live 2026-10-08 but froze systemStateMonitor for ~2 min per firing, so they were reverted (heap 2G to 4G, 24h PnL tracking removed, Zendesk 23617). The fix was deployed overnight 2026-10-14 and Rory is re-setting the alerts; he also flagged A-Book CLIENTS_NET averaging ~10 alerts a day.
Next: Mahi (Rory) to re-set PnL alerts and the LP-exposure alert; Matt to supply parameters for the email alerts.
Refs: https://mahifx.slack.com/archives/C0456LSHQQK/p1789753758017939 https://mahifx.slack.com/archives/C0456LSHQQK/p1791471698265769 https://mahifx.slack.com/archives/C0456LSHQQK/p1792052573269699

### xau-book-realignment — XAU position breaks across A House, Big House and Clients Net
status: open · since: 2026-09-25 · last: 2026-10-14
State: The Big House vs Big Clients Net XAU break (an Invast to LMAX move on 2026-05-07 booked to the wrong book) was fixed on 2026-09-28 by Rory with a six-row import into BIG_HEDGING_WASHBOOK_LDN and BIG_HOUSE, with the Big hedger off, plus a 14oz follow-up; Daniel confirmed it looked right. Separately, Mukhammad raised a 1.13k oz visual break between A House and Clients Net (not real risk, per Nathan, who supplied a realignment CSV based on A_HOUSE). On 2026-10-01 Daniel asked for the adjustment to use the CLIENTS book as source of truth instead; Rory said Mahi would look, and Daniel chased on 2026-10-14 with no reply seen.
Next: Mahi (Rory/Nathan) to produce adjustments using CLIENTS as the reference and reply to Daniel's 2026-10-14 chase.
Refs: https://mahifx.slack.com/archives/C0456LSHQQK/p1790329597165279 https://mahifx.slack.com/archives/C0456LSHQQK/p1790613838734949 https://mahifx.slack.com/archives/C0456LSHQQK/p1790555345540849 https://mahifx.slack.com/archives/C0456LSHQQK/p1791976466451139

### yield-sims-giraffe — Yield simulations on Giraffe datasets
status: open · since: 2026-10-05 · last: 2026-10-13
State: Keshav asked for simulations on three GMT+3 datasets. Rory found about half the trades are 20 to 40 pips or $19-30 off the Mahi retail mid, in blocks; Louie says they traded on a different LP, and George confirmed TradePrice is fill price and TransactTime is GMT+3 execution time. George suggested excluding outliers; Rory shows a non-trivial share is off market, so the sims have not run.
Next: Exinity (George/Keshav) to decide on excluding or correcting off-market trades.
Refs: https://mahifx.slack.com/archives/C0456LSHQQK/p1791216865711639 https://mahifx.slack.com/archives/C0456LSHQQK/p1791893099757919

### insti-book-moves — Insti routing, tag forwarding and position moves
status: open · since: 2026-08-31 · last: 2026-10-12
State: PrimeXM tag forwarding on the CONNECT_FILLET stream (2026-08-31) was confirmed by Daria to keep landing in BIG_INSTI_CLIENTS_1 as long as new tags avoid the wildcard risk-splitting counterparties. Matt moved an 11.35k oz CL1 position into A Insti Hedging Manual in September (Rory: PnL cannot be backdated, historic trade price can be used). On 2026-10-02 William closed an LMAX XAU position in 100oz clips due to a $2M LMAX volume cap. On 2026-10-12 Christian asked to move TradersHub (111000023) to A-book and open exposure at Wedbush; Nathan promised confirmation and help with the adjustment before EOD, no outcome seen.
Next: Nathan to confirm the steps/books and help with the TradersHub adjustment.
Refs: https://mahifx.slack.com/archives/C0456LSHQQK/p1788203770663179 https://mahifx.slack.com/archives/C0456LSHQQK/p1789471167917609 https://mahifx.slack.com/archives/C0456LSHQQK/p1791828427289149

### weekend-ops-reliability — Weekend restarts, FIX session windows, crypto publishing
status: open · since: 2026-08-17 · last: 2026-10-11
State: Weekend reboots repeatedly leave things down: ~25 processes missed after the 2026-08-22 reboot (reboot order reversed; internal note flags a Hazelcast shard-id collision as worth a ticket), components failed again on 2026-09-12, and STRD_PARTNER crypto pricing did not publish on weekends (fixed 2026-09-23: prices were published but market data not persisted into Compass). Kate re-offered the weekend-support proposal; Daniel says Exinity is comfortable self-monitoring but plans weekend crypto pricing. Exinity mirrors Mahi's nightly offline window (07:00 to 09:00 UTC, sequence reset 09:00) after the 2026-08-17 MsgSeqNum rejects. On 2026-10-11 all five Exinity FIX session pairs logged out at 21:00:02 UTC Friday and only logged on at 21:00 Sunday; Nathan asked Exinity to confirm their configured session times, no answer yet.
Next: Exinity to confirm FIX session times; Daniel/Kate to revisit weekend support when weekend crypto starts.
Refs: https://mahifx.slack.com/archives/C0456LSHQQK/p1786976101361259 https://mahifx.slack.com/archives/C0456LSHQQK/p1789215530822229 https://mahifx.slack.com/archives/C0456LSHQQK/p1789909690377469 https://mahifx.slack.com/archives/C0456LSHQQK/p1791752884902819

### pricing-spikes-widening — Spiky and wide pricing complaints
status: open · since: 2026-09-01 · last: 2026-10-09
State: Sep 1 Wagyu spikes at the open traced to Nomura via the Market Width Minimum Spread (MWMS) references; Exinity is backtesting adding Wedbush LPs to MWMS (Kate to check the sims ran). US30 widening on 2026-09-23 was MWMS tracking Velocity (Cameron Hughes set it to 100, Corey confirmed better). NZD/CHF/NOK cross spikes were treated with order-book rounding and lower skew ceilings (0.3 to 0.05 pips, 2026-09-25). EURUSD spikes on 2026-10-07 were skew plus Invast's bid crossing the Wedbush offers in the mid; skew was cut (ceiling 0.6 to 0.4, SNG 1.3 to 0.5, SNGMON 2.7 to 0.5) and Mahi proposed dropping Invast from the EURUSD mid, which Daniel declined on 2026-10-09. A 2026-09-29 LP feed stoppage (ticks stopped at Wedbush and Invast ~14:52) resumed after about three hours.
Next: Exinity to say whether spikiness persists; Wedbush-in-MWMS backtest result unconfirmed.
Refs: https://mahifx.slack.com/archives/C0456LSHQQK/p1788299416706969 https://mahifx.slack.com/archives/C0456LSHQQK/p1790270255985109 https://mahifx.slack.com/archives/C0456LSHQQK/p1791468162700719 https://mahifx.slack.com/archives/C0456LSHQQK/p1791555149344069

### order-reject-queries — Reject and fill investigations
status: open · since: 2026-09-21 · last: 2026-10-09
State: On 2026-10-01 Louie reported an urgent quote disconnect; Kate showed all Mahi sessions stayed up 00:06:52 to 00:35:33 UTC and the logged TARGET_QUOTE_Mahi_ECN session (FXTM) is not Mahi's, so it is downstream in Exinity's bridge. On 2026-10-06 Christian asked why a CL1USD take-profit rejected three times NO_PRICE/EXPIRED after a WTI spike; Rory explained pricing stayed indicative until 13:01:43 UTC after the LP stopped quoting and that Mahi does not hold pending TP/SL orders (immediate market orders), so the bridge must retry. On 2026-10-09 Christian asked for help reading FIX logs and Rory asked what he needs. Mukhammad's 2026-10-02 XAU rejects on API_111000023 had a Shyam acknowledgement but no outcome seen.
Next: Christian to say what he needs from the FIX logs; Exinity to check its bridge retry behaviour.
Refs: https://mahifx.slack.com/archives/C0456LSHQQK/p1790857668546679 https://mahifx.slack.com/archives/C0456LSHQQK/p1790909329116969 https://mahifx.slack.com/archives/C0456LSHQQK/p1791304956108509 https://mahifx.slack.com/archives/C0456LSHQQK/p1791563954367589

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
