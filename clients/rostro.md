---
slug: rostro
aliases: []
refs:
  vibepulse: ../VibePulse/.claude/clients/rostro.yaml
  billing: ../MahiProduct/data/billing/clients.json     # entry: rostro
  hosts: ../MahiProduct/data/client-hosts.json          # entry: rostro (also: easton for contracting entity)
  wiki: ../MahiProduct/wiki/clients/rostro.md
channels:
  internal-rostro: C08ALS66EDC
  mahi-rostro: C08AQKRU953
contacts:
  - {name: "Oliver Ryan", role: "Rostro trading ops (main day-to-day): routing/classification, hedger and book setup"}
  - {name: "Alexandre Goudergues", role: "ScopeMarkets (CY) trading ops: pricing config, hedging, positions"}
  - {name: "Riz Dusoye", role: "Rostro trading ops: pricing models, PSM, Pulse, CMC/XAUFUT questions"}
  - {name: "Rahul Sanap", role: "ScopeMarkets ops: fill/slippage queries", confidence: low}
  - {name: "Andreas Christofi", role: "ScopeMarkets ops: FIX sessions, new books", confidence: low}
  - {name: "Abdullah Almasharfa", role: "ScopeMarkets ops: PXM connections, IC feeds", confidence: low}
  - {name: "Chrysovalantis Karageorgiou", role: "ScopeMarkets ops: PXM connector/account setup", confidence: low}
  - {name: "Manuel de Cara", role: "Rostro: Pulse/Athena data access", confidence: low}
  - {name: "Sam Steele", role: "Group Chief Strategy Officer at Rostro; commercial counterpart (described internally as basically co-founder)"}
  - {name: "Michael Ayres", role: "senior Rostro contact meeting David Cooney 16 Oct; named replacement after Lochlan left", confidence: low}
last_catchup: 2026-11-19T08:16:35Z
status: active
---

## Now
Relationship under strain: the 14 Oct CMC futures freeze cost ~178k; Andrew accepted five pricing-integrity outcomes onto the roadmap (no owners or dates yet). New commercials signed 11 Nov (Mahi fees discounted by a $150K repayment settlement over 15 months); Sam Steele meeting (crypto and equities tools) postponed to the week of 16 Nov. Rostro keeps adding IC sub-account books and now sends all futures to IC.
Recent: 17-18 Nov quote withdrawals on NDXFUT-Z, a latency-edge client on gold, Invast hedge-limit cancels, XAGUSD.v stale IC prices, and Kate's sim showing classified flow loses money in the SI book.

## Streams

### xagusd-v-ic-stale — XAGUSD.v latency complaint traced to stale IC feed (18 Nov)
status: open · since: 2026-11-18 · last: 2026-11-18
State: Alexandre sent a file for a client complaint of XAGUSD latency. Kate found XAGUSD.v in it matches the IC Markets feed tick for tick, not Mahi prices; IC went stale several times, worst 11:41:44-11:42:19 UTC (sat at about 45.656/45.664 while the market fell to about 45.62, then jumped to 45.628), while Gravity and Mahi streams followed the market. She confirmed no Mahi pricing feed (model or continuity pool) includes IC in XAGUSD price formation, with a Price Forensics view as proof. Alexandre is checking which source XAGUSD.v maps to in the bridge (retail vs SI feed) and said the IC connection runs over the internet; his team looks into it 19 Nov.
Next: Alexandre to confirm the XAGUSD.v bridge mapping and raise the stale IC pricing with IC Markets.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1795018184572319 https://mahifx.slack.com/archives/C08AQKRU953/p1795022132865489 https://mahifx.slack.com/archives/C08AQKRU953/p1795024174062499

### invast-hedge-cancels — Invast cancelling hedge limit orders and tag 163_0_900235
status: open · since: 2026-11-18 · last: 2026-11-18
State: Scope (Abdullah) saw Mahi hedge limit orders on MAHI_INVAST_RETAIL for XAU and EUR blocked; the LP returns PROVIDER_CANCEL ("Failed to fill any volume") despite showing liquidity, Mahi orders carry 10ms TTL and repeated cancels raise rejectCount and block further attempts. Kate's check: 97% of XAUUSD limits went at Invast top of book with size, in about half the cases Invast still quoted the price, so a tolerance on Mahi's side would not help much. Owen: Invast confirmed tag 163_0_900235 executes against a different defensive feed. Alexandre said yes to blacklisting the tag from the hedger and Kate did it (11:41 UTC).
Next: Scope to ask Invast why it does not fill against liquidity it shows; Kate to watch.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1794998625174079 https://mahifx.slack.com/archives/C08AQKRU953/p1795001756318209 https://mahifx.slack.com/archives/C08AQKRU953/p1795002106067729

### si-xau-sim — Internal sim: XAUUSD SI book loses money on classified flow (18 Nov)
status: open · since: 2026-11-18 · last: 2026-11-18
State: Kate's sim of today's rules over 28 Jul to 16 Nov: the SI book would lose $316k to $522k at every off-book setting; off-book alone makes money at short holds (5m: +$234k to +$352k at $2-5M caps). The problem is classified flow ($54B at $25.8/M spread vs $35.3/M hedge cost), with arb and signal-follow flow negative within seconds. Lever is brokering arb ($10.3B) and signal-follow ($8.1B) flow, mostly internalised today via the Force Internalise: VIP profiles, so check the VIP price-improvement commitment first. Kate walked Alexandre through it that afternoon and is looking at hedging costs further.
Next: Kate to continue the hedging-cost analysis; check the VIP price-improvement commitment before changing the VIP internalise profiles.
Refs: https://mahifx.slack.com/archives/C08ALS66EDC/p1795008610871149 https://mahifx.slack.com/archives/C08ALS66EDC/p1795008638687359

### ndxfut-quote-pulls — NDXFUT-Z/NDXUSD quotes withdrawn ~5s at US data releases (6-12 Nov)
status: open · since: 2026-11-17 · last: 2026-11-17
State: Rahul (Scope) reported a client complaint of NDXFUT-Z rejections; FIX stream logs show bid and ask withdrawn for about 5s on 6 Nov (13:30:01), 10 Nov (13:30:01 and 13:30:06) and 12 Nov (13:07:35 UTC). Daria showed in Compass Price Forensics that quotes stopped on all LP feeds across NDXFUT-Z and NDXUSD, so upstream, likely an exchange-level pause, seen across the network. Rahul asked for a definitive root cause from upstream providers; Daria said Scope should confirm with IC Markets directly as its feed forms their price. Not clearly closed: the 6 and 10 Nov events coincide with the CMC to IC futures switch in cmc-futs-dropouts.
Next: Scope to take the exchange-pause question to IC Markets; Mahi to say if any quote-pull protection applies.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1794947379209009 https://mahifx.slack.com/archives/C08AQKRU953/p1794951936819419

### latency-edge-143 — Client 143_0_9963 latency-edge trades and slower Mahi price update
status: open · since: 2026-11-17 · last: 2026-11-17
State: Alexandre asked Mahi to check two XAUUSD orders from 143_0_9963 on 17 Nov and said the client trades a latency edge and Mahi pricing moves a few ms after other LPs. Kate: the client chased stale prices on fast moves and neither paid off (last look re-priced the sell; the buy filled at the current price), and offered a longer last look on this account. Alexandre is fine for now, told the client no slippage help, but wants pricing updated faster; Kate is looking at the pricing side.
Next: Kate to come back on whether pricing updates can be faster; Rostro to ask if it wants longer last look for 143_0_9963.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1794919372167019 https://mahifx.slack.com/archives/C08AQKRU953/p1794929593046499

### hedge-step-size — Hedging with an incorrect step size (13 Nov)
status: open · since: 2026-11-13 · last: 2026-11-13
State: Riz reported at 13:47 UTC that Rostro seems to be hedging with an incorrect step size (screenshot only, instrument not stated in text); Kate replied she was checking and would update it now. No confirmation of the fix seen. May relate to the hedging min quantity changes in cmc-futs-dropouts.
Next: Kate to confirm the step size is corrected.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1794577645417579 https://mahifx.slack.com/archives/C08AQKRU953/p1794577665079449

### commercials-reneg — Commercial renegotiation, value-add and relationship
status: open · since: 2026-08-19 · last: 2026-11-13
State: New Rostro terms signed (Bonnie, 11 Nov); fees discounted by a $150K repayment settlement over 15 months. Sam Steele wants two sessions, on the crypto tool and the equities portfolio tool (Andrew thinks single stocks are the bulk of Rostro's business, a possible gap); meeting set for 13 Nov was postponed by Oliver (people off sick, email outage). Kate delivered a value-add report 15 Oct. Kilo gold: Mahi can do it, Andrew said charge where possible. 3 Nov call: Rostro open to global LR capped at $5/M; considering pricing into Integral, Kate's early read (-$60/M on inception) is poor, dataset requested. Rostro's group got a BVI crypto registration.
Next: Rostro to send Integral flow dataset; set up global LR (max $5/M); rebook and prepare the Sam Steele meeting for the week of 16 Nov (crypto tool, then equities); consider charging for kilo gold.
Refs: https://mahifx.slack.com/archives/C08ALS66EDC/p1787135711511859 https://mahifx.slack.com/archives/C08ALS66EDC/p1793703042394719 https://mahifx.slack.com/archives/C08ALS66EDC/p1794388096504289 https://mahifx.slack.com/archives/C08ALS66EDC/p1794560201354309

### gbpnzd-roll-price — GBPNZD continuity-pool fallback at roll and continuity markup
status: open · since: 2026-11-10 · last: 2026-11-13
State: GBPNZD fell back to the continuity pool at 22:01 UTC on 2 Nov, and on the 11 Nov roll the INV model dropped out under 0.5s: the pool priced about 42 pips wide vs about 90 for the model, six 127_ accounts bought 1.8M within 30ms and Mahi hedged at roll spreads, hitting non-rev-share PnL (127_ did the same in GBPUSD on 22 Oct, smaller). Kate proposed raising the continuity markup (now $50/M) in roll (21:59-23:00 UTC: $1,000/M NZD/CHF crosses, $500/M other crosses, $300/M majors) and twilight ($150/$100/$50 per M) windows on A_CLIENTS and SCOPE_X_RETAIL/INSTI/VIP. Alexandre agreed; Riz (13 Nov) asked to apply today and go indicative if clients complain.
Next: Kate to apply the continuity markups (Riz asked for today, ahead of roll); Rostro may go indicative if spreads cause complaints.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1794306214114219 https://mahifx.slack.com/archives/C08AQKRU953/p1794507216428059 https://mahifx.slack.com/archives/C08AQKRU953/p1794545552790469

### fx-pnl-drop — SI/non-rev-share FX PnL drops (10-12 Nov) and exposure query
status: open · since: 2026-11-11 · last: 2026-11-12
State: Alexandre reported FX down about 10k on 10 Nov, 5k on 11 Nov and about 20k on 12 Nov on small volume. Kate traced 12 Nov partly to the GBPNZD roll fallback (see gbpnzd-roll-price) and the gold part to xau-offbook-148; FX and metals share one book. Alexandre's -43.5M summed USD exposure query: matches SI_BOOK plus NON_REV_SHARE_CLIENTS pair by pair but is not open exposure (crosses hedged in the drivers); he then thought it may be his own EOD-price reporting. The 11 Nov ~5k drop was never explained.
Next: Alexandre to finish his own PnL/exposure reconciliation; Kate to report the cause of the 11 Nov SI FX drop if still wanted.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1794393610189339 https://mahifx.slack.com/archives/C08AQKRU953/p1794507740719929

### hedger-cp-tag — Hybrid hedger orders to IC lost the HybridHedger counterparty tag
status: open · since: 2026-11-11 · last: 2026-11-11
State: Alexandre saw no HybridHedger-tagged trades since 9 Nov and reads a client tag on IC hedges as brokered hedging. Kate: since the post-maintenance restart the SI-book hybrid hedger sends the counterparty of the most recent client trade (skipping tags the LP disallows) instead of HybridHedger. Mahi can add config to always send HybridHedger; reverting needs a hedger restart. No decision seen.
Next: Alexandre to decide whether he wants the fixed HybridHedger tag restored.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1794393367585939 https://mahifx.slack.com/archives/C08AQKRU953/p1794415781616949

### cpi-skew-drop — 10 Nov CPI drop in FI PL on SI and retail skew
status: open · since: 2026-11-10 · last: 2026-11-11
State: Alexandre reported a drop in FI PL around the CPI print (-11k on SI, -2k on retail). Rory King found it was a benchmarking artefact: for a few seconds after the print most LPs in the skew benchmark stopped quoting and the remaining one was very wide, so skew was measured against an unfit reference; Mahi's price followed the venue it executed and hedged on. Alexandre asked whether the drop is not real and only a reporting issue (19:32 UTC) and repeated the question on 11 Nov (10:39 UTC); no answer seen.
Next: Rory/Kate to answer Alexandre's question.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1794329146184069 https://mahifx.slack.com/archives/C08AQKRU953/p1794393541339619

### cmc-futs-dropouts — CMC as sole futures LP: recurring dropouts and rejects
status: open · since: 2026-08-26 · last: 2026-11-11
State: CMC was the only LP pricing gold futures (and XAUFUT, indices), so each dropout (25 Aug, 5 Oct, 29 Oct) leaves no price or fill. 15 Oct Rostro moved most futures volume off Jump; NDXFUT-Z was mapped wrongly in PXM after the roll. 10-11 Nov: Oliver approved moving DOWFUT/SPXFUT/NDXFUT hedging and pricing to IC_MARKETS (brokered rules stay on CMC); after IC clear cancels and NQ rejects Scope briefly reverted, then Kate switched again on 11 Nov after IC test trades and bounced the SI futures hedgers. Oliver: all futures go to IC for now, clients chosen for CMC get brokering execution rules. Kate sets up a CMC liquidity pool from EOD 11 Nov. Futures widening offered; no answer. Hedging min qty NDX 0.2, DOW 0.05, SPX 0.5, DAX 0.25, XAU 0.01.
Next: Kate to apply the futures brokering-rule changes after the EOD restart and watch for IC rejections (Oliver asked); Rostro to confirm hedging min quantities against IC and say whether to set up futures widening; Rostro decision on Jump in XAUFUT reference price (Jump is being switched off, check it still stands); Alex to fix NDXFUT-Z mapping in PXM; Kate's CMC-normalisation backtest.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1787733565831759 https://mahifx.slack.com/archives/C08AQKRU953/p1791970984817549 https://mahifx.slack.com/archives/C08AQKRU953/p1794317966817829 https://mahifx.slack.com/archives/C08AQKRU953/p1794407794037449

### ic-sub-books — IC sub-account rev-share books (SUB 5/9/10/11, C House, Sub SI House)
status: open · since: 2026-08-24 · last: 2026-11-17
State: Rostro flow from specific counterparty tags is split into separate Compass books, each hedged via a dedicated hybridHedgerSub* to an IC_SUBS_* market through Scope's PXM Mahi_3 connection. Tag 251_* (large Cyprus retail broker, soft flow) has FX, CFD, futures and "Sub SI House" books; rev share signed 13 Oct. IC_SUBS_12 set up 19-20 Oct; sub 8 (XAU book) funded 30 Oct. Sub 11 live 2 Nov (indices direct to IC; XAU, XAG, G7 FX and futures via Mahi, tags 251_0 and 79_30 internalised or SI book, hedged to IC_SUBS_11); 3-4 Nov hedging misbehaved (missing risk splitting rule, fixed by Kate). Sub 11 is going into the 15 min SI cycle (FX and metals done, futures pending). Mahi does not price silver futures for Rostro (9 Nov, on Oliver's side). 16 Nov new SI sub hedgers added to expected-book-status; 17 Nov Kate bounced the non rev share hedger to add SAXO back.
Next: Kate to finish the 15 min SI cycle for sub 11 futures and fix risk splitting so sub 11 XAG hedges to IC_SUBS_11; confirm HRP_Saxo works after the 17 Nov hedger bounce; sub 8 test trades and go-live; confirm MAHI_IC_SUBS_12 funded; internal question on charging multi-region (NY4); send the Sub SI House holding-period page to Rostro.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1787569899244609 https://mahifx.slack.com/archives/C08AQKRU953/p1793366254660579 https://mahifx.slack.com/archives/C08AQKRU953/p1793968140238289 https://mahifx.slack.com/archives/C08ALS66EDC/p1794916235045669

### ndx-min-qty-reject — NDXUSD 0.01 order rejected by CMC min quantity
status: open · since: 2026-11-09 · last: 2026-11-09
State: Alexandre asked why order 72961136 was rejected on NDXUSD (15:29 UTC 9 Nov). Kate found Compass sets CMC minimum quantity at 0.02 but the order was 0.01. Tag 48_0_950003 has had no flow since October (Alexandre changed its classification); Kate said its yields are offside by 30s and suggested an internalise rule up to a notional to sidestep the minimum and pre-empt bigger volume. Kate then made a change at 15:48 and Alexandre will have the client retry.
Next: Alexandre to confirm the retry works; optional internalise-up-to-notional rule for the tag.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1794238189537329 https://mahifx.slack.com/archives/C08AQKRU953/p1794239314132049

### adaptive-skew-pitch — Move Rostro onto adaptive skew after NFP
status: open · since: 2026-11-06 · last: 2026-11-06
State: Will Carter said Rostro's B_INSTI_VIP book barely moved on the 6 Nov NFP release (13:30-13:33 UTC): skew about $3/M, LR $4/M, versus IC Crypto skew about $430/M and Infinox gold LR $125/M after his 15:48 correction (volume $56M, not the $170M first posted). He proposes replaying the release on a sim with an adaptive skew config, showing the client before/after skew PnL and switching on the measured result. Kate is looking at the skew setup. Skew is currently off on USDJPY/EURUSD for the VIP trial (see vip-trial-skew).
Next: owner needed for the adaptive-skew sim this week; Kate reviewing the skew set-up.
Refs: https://mahifx.slack.com/archives/C08ALS66EDC/p1793975301078089 https://mahifx.slack.com/archives/C08ALS66EDC/p1793980120503819

### position-breaks — Position breaks and position recs
status: open · since: 2026-09-04 · last: 2026-11-05
State: Breaks booked manually 8 Sep, 17 Sep and 2 Oct; 28 Oct Kate booked rev share book positions to fix long-term breaks from the earlier Centroid issue. 5 Nov Alexandre flagged a new 2k GBPJPY break on the SI book vs Scope's coverage account (4 Nov 18:20-22:20 UTC); Rory King: Mahi hedges in drivers, and two cancelled and re-sent trades filled just after 22:00 UTC; he asked for the coverage account position; no answer seen.
Next: Alexandre to share the coverage account position for GBPJPY; Cameron to roll out the VaR alerting now the booking is done.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1788504725919689 https://mahifx.slack.com/archives/C08ALS66EDC/p1793199991187849 https://mahifx.slack.com/archives/C08AQKRU953/p1793892499283759

### exec-rule-requests — Execution rule and routing requests (brokered vs internalised)
status: open · since: 2026-08-18 · last: 2026-11-04
State: Rostro keeps asking for per-tag rule changes (internalise XAGUSD from 122_*, toxic tags to the LDN pool, blacklist 163_0_88068 from brokering, broker tags on gold and index futures). Kate suggested force-internalising the two arb non rev share broker rules; no answer seen. 20 Oct Oliver wanted a rule for one client in the non rev share book; 2 Nov Alexandre asked for price improvement for a VIP end client with multiple APIs, Kate published a new INSTI VIP execution rule (copy of Force Internalise: VIP plus a counterparty criteria). 4 Nov Kate published an NDX FUT brokering rule for tag 165_0_n/a and internalised sub 11 XAG tags caught by an SI brokering rule (see ic-sub-books).
Next: Alexandre to confirm the new INSTI VIP rule gives the intended price improvement.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1787068816321309 https://mahifx.slack.com/archives/C08AQKRU953/p1792510778793009 https://mahifx.slack.com/archives/C08AQKRU953/p1793640528566759 https://mahifx.slack.com/archives/C08AQKRU953/p1793806802597919

### pxm-order-handling — PXM order splitting, boost, latency and tick throttle
status: open · since: 2026-09-30 · last: 2026-10-30
State: PXM splits large FA/VIP orders into tier-sized clips so fills land near TOB not VWAP. PXM boost off suits limit orders but market orders then sweep too; LR is the only in-product fix and the no-slippage agreement rules it out; Kate proposes asking PXM for per-order-type boost. Client latency traced to tick throttles (Mahi VIP 2 per 10ms, PXM 1 per ms). 30 Oct the VIP end client still saw 12ms tick latency; Alexandre will lower the PXM sampling interval (5 to 3) and Mahi ticks per 10ms at 7; Kate wants a fresh dataset (none available).
Next: PXM/Alex on pass-through or per-order-type boost; Kate to review tick publishing next week after the PXM sampling change (no dataset from the end client); Kate to check protective throttling on Mahi side before Rostro changes the PXM throttle.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1790776376391349 https://mahifx.slack.com/archives/C08ALS66EDC/p1791298744478709 https://mahifx.slack.com/archives/C08ALS66EDC/p1791883456395629 https://mahifx.slack.com/archives/C08AQKRU953/p1793361779461789

### vip-trial-skew — VIP end-client final trial: skew off on USDJPY/EURUSD
status: open · since: 2026-10-30 · last: 2026-10-30
State: Alexandre said the end client behind tag ending 100029 (most VIP USDJPY/EURUSD flow) is on its last trial week with Scope and asked for skew to be disabled. Skew is per price stream, not per tag, so Kate turned skew off on USDJPY and EURUSD on the VIP feed for the trial (price-based signals still apply to others), to be reviewed afterwards; the alternative is skew on with this tag's trades excluded from the signals, as its own trades drive most of the skew it sees. Tick latency side is in pxm-order-handling.
Next: Kate to review skew after the trial and decide between skew on with the tag excluded from signals or staying off.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1793361779461789 https://mahifx.slack.com/archives/C08AQKRU953/p1793372430907599

### pxm-connections — PrimeXM connections, LP list and feeds
status: open · since: 2026-09-04 · last: 2026-10-27
State: PXM taker connections cleaned up (7 Sep); MAHI_3 added 30 Sep for IC_SUBS. On 14 Oct Mahi found the VIP price session in PXM never requests XAGUSD, so Alex sees the INV book on VIP silver.
On 26 Oct Alexandre added the missing XAGUSD spread config on the FA stream; on 27 Oct Kate confirmed risk splitting for XAGUSD on FA was fine, Scope's test trade was routed to the off book and Kate said it looked good. Alexandre is still tweaking XAGUSD spreads (no BMSL on silver); Kate offered to check them.
Next: Alexandre to add XAG/USD to the VIP price session in PXM; Alexandre to share target XAGUSD spreads/widening if he wants Kate to check the setup.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1788508022729149 https://mahifx.slack.com/archives/C08AQKRU953/p1790608061088529 https://mahifx.slack.com/archives/C08AQKRU953/p1793051109437589 https://mahifx.slack.com/archives/C08AQKRU953/p1793109730716639

### fok-partial-fill — 26 Oct SI XAUUSD position break from partial-fill FOK brokering
status: open · since: 2026-10-26 · last: 2026-10-26
State: Scope flagged a -1.2M average SI short held since Friday; Kate traced it to partial fills on FOK orders attempted to broker (400oz got 350oz; one topped up 50oz, the other client trade cancelled, leaving the house short 300oz at the LPs). Oliver later said the position looked right. Kate turned off hedger-to-book position adjustment, set a high-VAR alert on Retail A Book and asked Oliver to rec CLIENTS_NET; Riz's rule had top-up allowed.
Next: Riz to confirm whether top-up allowed was intended on the rule; Kate to answer Scope's partial-fill detection question; Oliver to rec CLIENTS_NET positions.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1793005750513019 https://mahifx.slack.com/archives/C08AQKRU953/p1793006840087599 https://mahifx.slack.com/archives/C08ALS66EDC/p1793015998283009

### fill-queries — Client execution, slippage and rejection queries
status: open · since: 2026-08-27 · last: 2026-10-23
State: 23 Oct Rahul reported 57 of 86 orders negative slippage on a sub-account; Kate: brokered to IC after classification briefly flagged the account, internal fills got the shown price. 22 Oct a USDJPY Limit IOC to IC sat 3 min (IC reset), tripping an order-breach limit; no open risk.
Next: Rostro to say whether to change the LP, internalise, or relax the anti-spoof node; no reply seen.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1787835257505189 https://mahifx.slack.com/archives/C08AQKRU953/p1792665379140899 https://mahifx.slack.com/archives/C08AQKRU953/p1792781435455779 https://mahifx.slack.com/archives/C08AQKRU953/p1792782045722059

### cmc-spx-freeze — 14 Oct CMC SPX/NDX freeze, RCA and evidence pack
status: open · since: 2026-10-14 · last: 2026-10-20
State: CMC's SPX price (futures and cash) froze 12:18:36-12:34:15 UTC while IC and Jump fell about 38 points; loss about 178k (about 114k client trades at the frozen price). Cause: CMC stayed connected and its size changes reset the stuck-filter's 10 min clock (Will's replays): upstream failure plus a Mahi protection gap. Evidence went to Rostro 14 Oct. Andrew accepted five outcomes onto roadmap 7.2-PI-1 to 5: quantity-only updates must not hide frozen prices, divergence alert vs a normalised reference (first), quote pull at a replay-validated threshold, hedge availability alongside pricing health, reconciling Jump repricing with CMC recovery. 20 Oct: CMC gave no rebate; its report said internal config published with errors halted pricing.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1791981542846109 https://mahifx.slack.com/archives/C08ALS66EDC/p1792137303134229 https://mahifx.slack.com/archives/C08ALS66EDC/p1792139709277749 https://mahifx.slack.com/archives/C08ALS66EDC/p1792490159068509

### c-book-lr-price — C book slippage: LR applied at fill but not in quoted price
status: watching · since: 2026-10-16 · last: 2026-10-16
State: C book client complained of slippage on 15 Oct gold (filled 4151.71 vs quote 4151.52/4151.64). Isaac: on the multi-channel SCOPE_X_FA session, XAUUSD orders from 122_0_* and 117_27* execute on C_CLIENTS and take its LR, but the streamed price carries only SCOPE_X_FA's LR. Options: XAUUSD.c instrument with extra bridge routing, or a global per-process LR. Isaac disabled LR on C_CLIENTS meanwhile. Watching: no decision in 31 days (3 Nov call: open to global LR capped at $5/M, see commercials-reneg).
Next: Rostro (Alexandre/Riz) to decide between XAUUSD.c routing and global LR; LR stays off on C_CLIENTS until then.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1792138607035239 https://mahifx.slack.com/archives/C08AQKRU953/p1792140741428669 https://mahifx.slack.com/archives/C08AQKRU953/p1792141257894219

### psm-inv-rollout — Predictive spread modulation on the INV model
status: watching · since: 2026-09-01 · last: 2026-10-14
State: PSM live on INV 13-14 Oct after a month-long beta (+$0.83/M).
Next: watch volumes and spreads after go-live.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1788280838936589 https://mahifx.slack.com/archives/C08AQKRU953/p1791971029551609

### compass-26-4 — Compass 26.4 upgrade and dashboard deploys
status: watching · since: 2026-10-08 · last: 2026-10-09
State: 26.4 live at the 10-11 Oct restart; Rostro opted out of PSM overlays. Classifier bug on tags containing "/" is ZD-23407.
Refs: https://mahifx.slack.com/archives/C08ALS66EDC/p1791483337578909 https://mahifx.slack.com/archives/C08AQKRU953/p1791543772435149

### xau-offbook-148 — 12 Nov XAUUSD off-book long and risk splitting for the 148_ tag set
status: closed · since: 2026-11-12 · last: 2026-11-16 · closed: 2026-11-17
State: ~19k off-book gold loss 16 Nov; Oliver approved splitting 148_ risk by classification, Kate did it same day.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1794502387640839 https://mahifx.slack.com/archives/C08AQKRU953/p1794824898300319

### c-book-slippage-file — C book (122_*) client slippage file, tick throttle suspected
status: closed · since: 2026-11-10 · last: 2026-11-16 · closed: 2026-11-17
State: Kate: no throttling; the client fires about 10 orders within ms against one quote, so each fills behind pending quantity. Alexandre accepted on 16 Nov.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1794347283583259 https://mahifx.slack.com/archives/C08AQKRU953/p1794847070992339

### xau-bad-print — 11 Sep Jane Street XAUUSD bad print (CPI) and missing price guard
status: closed · since: 2026-09-11 · last: 2026-09-15 · closed: 2026-11-16
State: At the CPI release the XAUUSD reference panel collapsed to Jane Street alone, giving a $319.84 spread for ~2s; sanity check had been off since go-live. Riz pulled Jane Street from the XAU selectors and the check was enabled 15 Sep. Assumed resolved.
Refs: https://mahifx.slack.com/archives/C08ALS66EDC/p1789131695104789 https://mahifx.slack.com/archives/C08AQKRU953/p1789463134083049

### c-book-clearance — C book risk clearance speed (15 Oct gold)
status: closed · since: 2026-10-15 · last: 2026-10-15 · closed: 2026-11-11
State: 15 Oct 30M C book clearance took ~5 min; Kate turned off fill-ratio adjustment on the hedgers; assumed resolved.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1792078136400489 https://mahifx.slack.com/archives/C08ALS66EDC/p1792081751691529

### pulse-athena-access — Rostro cannot read Pulse/Athena from new IP
status: closed · since: 2026-08-27 · last: 2026-09-09 · closed: 2026-11-05
State: assumed resolved.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1787822793611979 https://mahifx.slack.com/archives/C08AQKRU953/p1788950130321199

## Arc
- 2025 — Rostro live on Compass (per Kate, 2026-09-14, sanity check disabled before go-live)
- 2026-05 — Lochlan, key contact championing Mahi, left Rostro for OZ; Saul Knapp left for MAS Markets
- 2026-07-14 — oil reference-feed incident (~$350k client loss) raised by Rostro; Mahi offers no goodwill
- 2026-07-30 — Sam Steele intro meeting; wants documented safeguards, not reimbursement
- 2026-08-25 — commercial renegotiation and joint PR started at Rostro's request
- 2026-09-15 — Rostro did not sign the new commercials draft ("a no from the board")
- 2026-10-14 — PSM live on INV; CMC SPX freeze costs ~178k, treated as relationship-level risk
- 2026-10-16 — Andrew accepts five pricing-integrity outcomes from the CMC freeze RCA onto the roadmap
- 2026-10-20 — Rostro accepts new commercials with a $150K repayment settlement over 15 months
- 2026-11-11 — new Rostro terms signed
