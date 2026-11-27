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
  - {name: "Oliver Ryan", role: "Rostro trading ops (day-to-day): routing, hedger, books"}
  - {name: "Alexandre Goudergues", role: "ScopeMarkets (CY) trading ops: pricing, hedging, positions"}
  - {name: "Riz Dusoye", role: "Rostro trading ops: pricing models, PSM, Pulse, CMC/XAUFUT"}
  - {name: "Rahul Sanap", role: "ScopeMarkets ops: fill/slippage queries", confidence: low}
  - {name: "Andreas Christofi", role: "ScopeMarkets ops: FIX sessions, new books", confidence: low}
  - {name: "Abdullah Almasharfa", role: "ScopeMarkets ops: PXM connections, IC feeds", confidence: low}
  - {name: "Chrysovalantis Karageorgiou", role: "ScopeMarkets ops: PXM connector/account setup", confidence: low}
  - {name: "Manuel de Cara", role: "Rostro: Pulse/Athena data access", confidence: low}
  - {name: "Sam Steele", role: "Group Chief Strategy Officer at Rostro; commercial counterpart"}
  - {name: "Michael Ayres", role: "senior Rostro contact; named replacement after Lochlan left", confidence: low}
last_catchup: 2026-11-27T08:14:57Z
status: active
---

## Now
Relationship under strain: the 14 Oct CMC futures freeze cost ~178k; five pricing-integrity roadmap outcomes still lack owners and dates. New commercials signed 11 Nov (Mahi fees discounted by a $150K repayment settlement over 15 months); Sam Steele meeting (crypto and equities tools) postponed to the week of 16 Nov. Rostro keeps adding IC sub-account books and now sends all futures to IC.
Recent: 26 Nov C-book fill vs streamed price gap traced to a separate execution channel (Mahi investigating); SI hedger trialling 100 oz gold clips on IC; 23 Nov NDX widening-with-CMC rules; tag 150_0_1102181_100076 gold-futures latency arb.

## Streams

### si-hedger-clips — SI hedger XAUUSD: trial of 100 oz clips on IC (26 Nov)
status: open · since: 2026-11-26 · last: 2026-11-26
State: Kate's analysis: over 4 weeks SI hedger gold trades of 100 oz or less cost about $15/M on IC vs about $73/M above 100 oz (IC shows ~100 oz at top of book). From 26 Nov hybridHedgerSI1 (XAUUSD only) sends waves of up to 100 oz 100ms apart when VaR is below ~30k; above that a new high VaR rule clears as before (up to 1,000 oz, 500ms). Expected cost ~$37/M down to ~$33-34/M, about 1s slower clearing, lower fill rate on small clips. SI1 bounced 10:52 UTC; judged on the next full days (US Thanksgiving 26 Nov). More LPs would let big clips split across top of books.
Next: Kate to review cost and clearance speed, then try 50ms and a ~50k VaR switch; revert if clearance slows too much.
Refs: https://mahifx.slack.com/archives/C08ALS66EDC/p1795689120574719 https://mahifx.slack.com/archives/C08ALS66EDC/p1795690375425759

### c-book-lr-price — C book slippage: execution channel price differs from streamed price
status: open · since: 2026-10-16 · last: 2026-11-26
State: C book client complained of slippage on 15 Oct gold. Isaac: on the multi-channel SCOPE_X_FA session, XAUUSD orders from 122_0_* and 117_27* execute on C_CLIENTS and take its LR, but the streamed price carries only SCOPE_X_FA's LR. Options: XAUUSD.c instrument with extra bridge routing, or a global per-process LR. Isaac disabled LR on C_CLIENTS meanwhile (3 Nov: open to global LR capped at $5/M).
26 Nov: Alexandre asked why a 122_0_3518 XAUUSD market order filled at 3534.22 when PXM showed an ask of 3534.04 (published 316ms, 3534.22 at 318ms). Rory first said the fill was the published offer, then corrected: the order executes on a separate channel from the one prices stream on, and that channel's offer was already 3534.22 on arrival; price improvement is off on the SI_REV_SHARE Catch-All profile, so the fill is the worse of that price and the post-hold 3534.13. Mahi is looking into why the two channels differed. Alexandre: LR was disabled to avoid exactly this and wants to know what else affects the price.
Next: Rory/Mahi to explain the channel price gap and come back to Alexandre; Rostro to decide between XAUUSD.c routing and global LR.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1792138607035239 https://mahifx.slack.com/archives/C08AQKRU953/p1795697422179069 https://mahifx.slack.com/archives/C08AQKRU953/p1795708841519419

### cmc-futs-dropouts — CMC as sole futures LP: recurring dropouts and rejects
status: open · since: 2026-08-26 · last: 2026-11-25
State: CMC was the only LP pricing gold futures (and XAUFUT, indices), so each dropout (25 Aug, 5 Oct, 29 Oct) leaves no price or fill. NDXFUT-Z was mapped wrongly in PXM after the roll. 10-11 Nov: Oliver approved moving DOWFUT/SPXFUT/NDXFUT hedging and pricing to IC_MARKETS (brokered rules stay on CMC); after IC cancels and NQ rejects Scope briefly reverted, then Kate switched again on 11 Nov. Oliver: all futures go to IC for now, clients chosen for CMC get brokering execution rules.
13 Nov Riz reported hedging with an incorrect step size (screenshot, instrument unstated); no fix confirmed.
23 Nov: XAUFUT-G now maps to GC.G27 (pricing after EOD restarts, Scope aligned); Abdullah raised the CMC market hedger max size to 200 after SP500 rejections and Kate aligned Mahi's side.
25 Nov 07:33 UTC the step-size problem recurred: Abdullah posted a PXM reject of a GC.Z26 limit sell on MAHI_CMC (size 213.35, step=1.0, rejectCount=3); Isaac Dann said he is checking.
Next: Isaac/Kate to fix the GC.Z26 hedge size rounding to step 1.0 (13 Nov step-size report never confirmed fixed); Kate to apply futures brokering-rule changes after the EOD restart and watch IC rejections; Rostro to confirm IC hedging min quantities and whether to set up futures widening; Rostro to confirm Jump stays off as XAUFUT reference; Alex to fix NDXFUT-Z mapping in PXM.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1787733565831759 https://mahifx.slack.com/archives/C08AQKRU953/p1795442353264769 https://mahifx.slack.com/archives/C08AQKRU953/p1795592107310689

### index-widen-cmc — INV model widens indices when CMC widens (NDX, DOW, SPX, G30)
status: open · since: 2026-11-23 · last: 2026-11-23
State: After NDXUSD stopped across LPs at 14:27 UTC, Alexandre asked for spreads to widen when the input source widens. Kate set BMSL and MWMS rules on NDXUSD (INV model, SI only) and then DOWUSD, SPXUSD, G30EUR: at top of book widen to CMC's spread if CMC is wider by more than 0.2 (DOW, NDX, SPX) or 0.7 (G30); past top of book (21+, SPX 201+) never tighter than CMC at the same size. Live 16:09 UTC after pricer bounce.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1795445592491399 https://mahifx.slack.com/archives/C08AQKRU953/p1795446161959399 https://mahifx.slack.com/archives/C08AQKRU953/p1795450352532299

### tag-brokering-xau — Toxic tags brokered on gold (79_16_1502328, 90_15_praxis; 150_0_1102181_100076 on XAUFUT)
status: open · since: 2026-11-20 · last: 2026-11-23
State: Alexandre asked to broker tags 79_16_1502328 and 90_15_praxis to non rev share, for XAUUSD where they are most toxic; they do not trade FX, so he took the simpler all-instrument option. Kate added both tags to the existing SI BOOK execution rule (15:56 UTC). 23 Nov Alexandre saw XAUFUT drifting lower on 150_0_1102181_100076 (looks like latency arb) and got the green light to give the client real market price and broker it, gold only; Kate: it is classified Broker&Don't B-Book&Signal Follow, she is setting up a rule. All gold futures flow routes to CMC (brokered or hedged), and the liquidity-pool override is CMC, so brokering GC to the IC pool needs an EOD restart.
Next: Kate to set up the 150_0_1102181_100076 brokering rule; Alexandre to say CMC or IC.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1795189621971919 https://mahifx.slack.com/archives/C08AQKRU953/p1795450268571809 https://mahifx.slack.com/archives/C08AQKRU953/p1795450753823659

### ndxfut-quote-pulls — NDXFUT-Z/NDXUSD quotes withdrawn ~5s at US data releases (6-12 Nov)
status: open · since: 2026-11-17 · last: 2026-11-23
State: Rahul (Scope) reported a client complaint of NDXFUT-Z rejections; FIX logs show bid and ask withdrawn for about 5s on 6, 10 and 12 Nov (13:30 UTC data releases). Daria showed in Price Forensics that quotes stopped on all LP feeds, so upstream, likely an exchange-level pause. Daria said Scope should confirm with IC Markets directly as its feed forms their price. Recurred 23 Nov 14:27-14:30 UTC (NDXUSD stopped across LPs, Kate saw it elsewhere); see index-widen-cmc. Not clearly closed: the 6 and 10 Nov events coincide with the CMC to IC futures switch in cmc-futs-dropouts.
Next: Scope to take the exchange-pause question to IC Markets; Mahi to say if any quote-pull protection applies.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1794947379209009 https://mahifx.slack.com/archives/C08AQKRU953/p1794951936819419 https://mahifx.slack.com/archives/C08AQKRU953/p1795444054347649

### rostro-tickstore-disk — Tickstore disk nearly full after hung S3 uploader (19-20 Nov)
status: open · since: 2026-11-19 · last: 2026-11-20
State: The S3 tick-data uploader on rostro-ln-trading-1 hung at 11:48 UTC 19 Nov (likely the DNS blip also seen on another client host), leaving 2.5G free after 18h. Daria killed it at 06:14 UTC 20 Nov; the backlog is clearing (~5G/h), no tick data lost, 19 Nov data reaches S3 late. No other hosts affected. 20 Nov Alexandre noticed rostro_ldn.tradepositions last timestamp 19 Nov 19:20; Kate said the table is catching up on the backlog, no data lost, fully current by that evening.
Next: deploy the uploader timeout fix (infra PR 1101).
Refs: https://mahifx.slack.com/archives/C08ALS66EDC/p1795156381462139 https://mahifx.slack.com/archives/C08AQKRU953/p1795185855681029

### tag-254-slippage — 254_* tags complaining of slippage, brokered to non rev share
status: open · since: 2026-11-19 · last: 2026-11-19
State: Alexandre asked Mahi to check 254_* tags (e.g. 254_0_6006) complaining of slippage and appearing brokered to non rev share, and asked to improve their experience. Kate: an INSTI VIP rule on 254_0_* brokers broker, signal-follow and arb classified tags.
Next: Rory/Kate to check the 254_* tags; Alexandre to decide whether to change the rule for them.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1795092988483999 https://mahifx.slack.com/archives/C08AQKRU953/p1795094232163479

### xagusd-v-ic-stale — XAGUSD.v latency complaint traced to stale IC feed (18 Nov)
status: open · since: 2026-11-18 · last: 2026-11-19
State: Alexandre sent a file for a client complaint of XAGUSD latency. Kate: XAGUSD.v matches the IC Markets feed tick for tick, not Mahi prices; IC went stale several times (worst 11:41:44-11:42:19 UTC) while Mahi followed the market, and no Mahi pricing feed includes IC in XAGUSD. Alexandre is checking the XAGUSD.v bridge mapping. 19 Nov (internal): Kate sees occasional IC to Rostro PXM disconnects from quotes backing up over the internet link; as IC sits in NY4, IC will connect to a PXM NY4 server linked to Rostro's PXM LD4 server.
Next: Alexandre to confirm the XAGUSD.v bridge mapping; IC/PXM NY4 link to be set up.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1795018184572319 https://mahifx.slack.com/archives/C08AQKRU953/p1795024174062499 https://mahifx.slack.com/archives/C08ALS66EDC/p1795098207570049

### invast-hedge-cancels — Invast cancelling hedge limit orders and tag 163_0_900235
status: open · since: 2026-11-18 · last: 2026-11-19
State: Scope (Abdullah) saw Mahi hedge limit orders on MAHI_INVAST_RETAIL for XAU and EUR blocked; the LP returns PROVIDER_CANCEL ("Failed to fill any volume") despite showing liquidity, Mahi orders carry 10ms TTL and repeated cancels raise rejectCount and block further attempts. Owen: Invast confirmed tag 163_0_900235 executes against a different defensive feed; Kate blacklisted it from the hedger (18 Nov). 19 Nov: Abdullah said quote blocking at Invast is unchanged; Alexandre asked to blacklist four high-reject tags (163_0_900636, 163_0_900644, 138_1_950003, 68_0_100020) from Invast and Kate did it (12:42 UTC).
Next: Scope to ask Invast why it does not fill against liquidity it shows; Kate to watch whether blocking persists.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1794998625174079 https://mahifx.slack.com/archives/C08AQKRU953/p1795091861719799 https://mahifx.slack.com/archives/C08AQKRU953/p1795092176898129

### vip-trial-skew — VIP end-client final trial: skew off on USDJPY/EURUSD
status: open · since: 2026-10-30 · last: 2026-11-19
State: Alexandre said the end client behind tag ending 100029 (most VIP USDJPY/EURUSD flow) is on its last trial week with Scope and asked for skew to be disabled. Skew is per price stream, not per tag, so Kate turned skew off on USDJPY and EURUSD on the VIP feed for the trial; the alternative is skew on with this tag's trades excluded from the signals, as its own trades drive most of the skew it sees. 19 Nov Alexandre asked to check skew on EURUSD in the VIP feed, needs it off; Kate said it was turned off, will double check config and asked for a sample or timestamp.
Next: Kate to double check EURUSD VIP skew is off; Alexandre to supply the client's sample/timestamp; Kate to review skew after the trial and decide between skew on with the tag excluded from signals or staying off.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1793361779461789 https://mahifx.slack.com/archives/C08AQKRU953/p1795094040215509 https://mahifx.slack.com/archives/C08AQKRU953/p1795094125777979

### si-xau-sim — Internal sim: XAUUSD SI book loses money on classified flow (18 Nov)
status: open · since: 2026-11-18 · last: 2026-11-18
State: Kate's sim of today's rules over 28 Jul to 16 Nov: the SI book would lose $316k to $522k at every off-book setting; off-book alone makes money at short holds (5m: +$234k to +$352k at $2-5M caps). The problem is classified flow ($25.8/M spread vs $35.3/M hedge cost), arb and signal-follow negative within seconds. Lever: broker arb ($10.3B) and signal-follow ($8.1B) flow, mostly internalised today via the Force Internalise: VIP profiles.
Next: Kate to continue the hedging-cost analysis; check the VIP price-improvement commitment before changing the VIP internalise profiles.
Refs: https://mahifx.slack.com/archives/C08ALS66EDC/p1795008610871149 https://mahifx.slack.com/archives/C08ALS66EDC/p1795008638687359

### latency-edge-143 — Client 143_0_9963 latency-edge trades and slower Mahi price update
status: open · since: 2026-11-17 · last: 2026-11-17
State: Alexandre asked Mahi to check two XAUUSD orders from 143_0_9963 on 17 Nov and said the client trades a latency edge and Mahi pricing moves a few ms after other LPs. Kate: the client chased stale prices on fast moves and neither paid off (last look re-priced the sell; the buy filled at the current price), and offered a longer last look on this account. Alexandre wants pricing updated faster.
Next: Kate to come back on whether pricing updates can be faster; Rostro to ask if it wants longer last look for 143_0_9963.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1794919372167019 https://mahifx.slack.com/archives/C08AQKRU953/p1794929593046499

### ic-sub-books — IC sub-account rev-share books (SUB 5/9/10/11, C House, Sub SI House)
status: open · since: 2026-08-24 · last: 2026-11-17
State: Rostro flow from specific counterparty tags is split into separate Compass books, each hedged via a dedicated hybridHedgerSub* to an IC_SUBS_* market through Scope's PXM Mahi_3 connection. Tag 251_* has FX, CFD, futures and "Sub SI House" books (rev share signed 13 Oct); sub 8 (XAU) funded 30 Oct. Sub 11 live 2 Nov (indices direct to IC; XAU, XAG, G7 FX and futures via Mahi, hedged to IC_SUBS_11); Sub 11 is going into the 15 min SI cycle (FX and metals done, futures pending). 17 Nov Kate bounced the non rev share hedger to add SAXO back.
Next: Kate: sub 11 futures 15 min SI cycle, sub 11 XAG risk splitting to IC_SUBS_11, confirm HRP_Saxo after the 17 Nov bounce, sub 8 go-live, MAHI_IC_SUBS_12 funded, send Sub SI House holding-period page.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1787569899244609 https://mahifx.slack.com/archives/C08AQKRU953/p1793968140238289 https://mahifx.slack.com/archives/C08ALS66EDC/p1794916235045669

### commercials-reneg — Commercial renegotiation, value-add and relationship
status: open · since: 2026-08-19 · last: 2026-11-13
State: New Rostro terms signed (Bonnie, 11 Nov); fees discounted by a $150K repayment settlement over 15 months. Sam Steele wants two sessions (crypto tool, equities portfolio tool; Andrew thinks single stocks are the bulk of Rostro's business, a possible gap); the 13 Nov meeting was postponed by Oliver. 3 Nov call: Rostro open to global LR capped at $5/M; considering pricing into Integral, Kate's early read (-$60/M on inception) is poor.
Kilo gold: Mahi can do it, charge where possible.
Next: Rostro to send Integral flow dataset; set up global LR (max $5/M); rebook and prepare the Sam Steele meeting for the week of 16 Nov (crypto tool, then equities).
Refs: https://mahifx.slack.com/archives/C08ALS66EDC/p1787135711511859 https://mahifx.slack.com/archives/C08ALS66EDC/p1794388096504289 https://mahifx.slack.com/archives/C08ALS66EDC/p1794560201354309

### gbpnzd-roll-price — GBPNZD continuity-pool fallback at roll and continuity markup
status: open · since: 2026-11-10 · last: 2026-11-13
State: GBPNZD fell back to the continuity pool at 22:01 UTC on 2 Nov, and on the 11 Nov roll the INV model dropped out under 0.5s: the pool priced about 42 pips wide vs about 90 for the model, six 127_ accounts bought 1.8M within 30ms and Mahi hedged at roll spreads, hitting non-rev-share PnL. Kate proposed raising the continuity markup (now $50/M) in roll (21:59-23:00 UTC: $1,000/M NZD/CHF crosses, $500/M other crosses, $300/M majors) and twilight ($150/$100/$50 per M) windows on A_CLIENTS and SCOPE_X_RETAIL/INSTI/VIP. Alexandre agreed; Riz asked to apply it 13 Nov.
Next: Kate to apply the continuity markups (Riz asked for today, ahead of roll); Rostro may go indicative if spreads cause complaints.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1794306214114219 https://mahifx.slack.com/archives/C08AQKRU953/p1794507216428059 https://mahifx.slack.com/archives/C08AQKRU953/p1794545552790469

### fx-pnl-drop — SI/non-rev-share FX PnL drops (10-12 Nov) and exposure query
status: open · since: 2026-11-11 · last: 2026-11-12
State: Alexandre reported FX down about 10k on 10 Nov, 5k on 11 Nov and about 20k on 12 Nov on small volume. Kate traced 12 Nov partly to the GBPNZD roll fallback (see gbpnzd-roll-price) and the gold part to xau-offbook-148; FX and metals share one book. His -43.5M summed USD exposure query is not open exposure (crosses hedged in the drivers). The 11 Nov ~5k drop was never explained.
10 Nov CPI: FI PL drop (-11k SI, -2k retail) was a skew-benchmark artefact (most LPs stopped quoting for seconds, the remaining one very wide); Alexandre asked twice (last 11 Nov) whether it is only a reporting issue, no answer seen.
Next: Rory/Kate to answer the CPI question; Alexandre to finish his own PnL/exposure reconciliation; Kate to report the cause of the 11 Nov SI FX drop if still wanted.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1794393610189339 https://mahifx.slack.com/archives/C08AQKRU953/p1794507740719929

### hedger-cp-tag — Hybrid hedger orders to IC lost the HybridHedger counterparty tag
status: open · since: 2026-11-11 · last: 2026-11-11
State: Alexandre saw no HybridHedger-tagged trades since 9 Nov and reads a client tag on IC hedges as brokered hedging. Kate: since the post-maintenance restart the SI-book hybrid hedger sends the counterparty of the most recent client trade (skipping tags the LP disallows) instead of HybridHedger. Mahi can add config to always send HybridHedger; reverting needs a hedger restart. No decision seen.
Next: Alexandre to decide whether he wants the fixed HybridHedger tag restored.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1794393367585939 https://mahifx.slack.com/archives/C08AQKRU953/p1794415781616949

### adaptive-skew-pitch — Move Rostro onto adaptive skew after NFP
status: open · since: 2026-11-06 · last: 2026-11-06
State: Will Carter said Rostro's B_INSTI_VIP book barely moved on the 6 Nov NFP release (13:30-13:33 UTC): skew about $3/M, LR $4/M, versus IC Crypto skew about $430/M and Infinox gold LR $125/M after his 15:48 correction (volume $56M, not the $170M first posted). He proposes replaying the release on a sim with an adaptive skew config, showing the client before/after skew PnL and switching on the measured result. Skew is currently off on USDJPY/EURUSD for the VIP trial (see vip-trial-skew).
Next: owner needed for the adaptive-skew sim this week; Kate reviewing the skew set-up.
Refs: https://mahifx.slack.com/archives/C08ALS66EDC/p1793975301078089 https://mahifx.slack.com/archives/C08ALS66EDC/p1793980120503819

### position-breaks — Position breaks and position recs
status: open · since: 2026-09-04 · last: 2026-11-05
State: 28 Oct Kate booked rev share positions to fix long-term Centroid breaks. 5 Nov Alexandre flagged a new 2k GBPJPY break on the SI book vs Scope's coverage account (4 Nov 18:20-22:20 UTC); Rory King: he asked for the coverage account position; no answer seen.
26 Oct SI XAUUSD -1.2M short traced to partial FOK brokering fills; Kate set a high-VAR alert on Retail A Book.
Next: Riz to confirm whether top-up allowed was intended on the rule; Oliver to rec CLIENTS_NET; Alexandre to share the coverage account position for GBPJPY; Cameron to roll out the VaR alerting now the booking is done.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1788504725919689 https://mahifx.slack.com/archives/C08ALS66EDC/p1793199991187849 https://mahifx.slack.com/archives/C08AQKRU953/p1793892499283759

### exec-rule-requests — Execution rule and routing requests (brokered vs internalised)
status: open · since: 2026-08-18 · last: 2026-11-04
State: Rostro keeps asking for per-tag rule changes (internalise XAGUSD from 122_*, toxic tags to the LDN pool, blacklist 163_0_88068 from brokering, broker tags on gold and index futures). 2 Nov Alexandre asked for price improvement for a VIP end client with multiple APIs, Kate published a new INSTI VIP execution rule (copy of Force Internalise: VIP plus a counterparty criteria). 4 Nov Kate published an NDX FUT brokering rule for tag 165_0_n/a and internalised sub 11 XAG tags caught by an SI brokering rule (see ic-sub-books).
9 Nov: NDXUSD 0.01 order rejected (CMC min qty 0.02); Kate changed it.
Next: Alexandre to confirm the new INSTI VIP rule gives the intended price improvement and the NDXUSD retry works.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1787068816321309 https://mahifx.slack.com/archives/C08AQKRU953/p1793640528566759 https://mahifx.slack.com/archives/C08AQKRU953/p1793806802597919

### pxm-order-handling — PXM order splitting, boost, latency and tick throttle
status: open · since: 2026-09-30 · last: 2026-10-30
State: PXM splits large FA/VIP orders into tier-sized clips so fills land near TOB not VWAP. PXM boost off suits limit orders but market orders then sweep; LR is ruled out by the no-slippage agreement; Kate proposes per-order-type boost from PXM. Client latency traced to tick throttles (Mahi VIP 2 per 10ms, PXM 1 per ms). 30 Oct the VIP end client still saw 12ms tick latency; Alexandre will lower the PXM sampling interval (5 to 3) and Mahi ticks per 10ms at 7; Kate wants a fresh dataset (none available).
Next: PXM/Alex on pass-through or per-order-type boost; Kate to review tick publishing next week after the PXM sampling change (no dataset from the end client); Kate to check protective throttling on Mahi side before Rostro changes the PXM throttle.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1790776376391349 https://mahifx.slack.com/archives/C08ALS66EDC/p1791883456395629 https://mahifx.slack.com/archives/C08AQKRU953/p1793361779461789

### pxm-connections — PrimeXM connections, LP list and feeds
status: watching · since: 2026-09-04 · last: 2026-10-27
State: Watching: no Slack activity since 27 Oct. On 14 Oct Mahi found the VIP price session in PXM never requests XAGUSD, so Alex sees the INV book on VIP silver.
26-27 Oct Alexandre added the missing XAGUSD spread config on FA; Kate confirmed risk splitting was fine. Alexandre is still tweaking XAGUSD spreads (no BMSL on silver).
Next: Alexandre to add XAG/USD to the VIP price session in PXM; Alexandre to share target XAGUSD spreads/widening if he wants Kate to check the setup.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1788508022729149 https://mahifx.slack.com/archives/C08AQKRU953/p1793051109437589 https://mahifx.slack.com/archives/C08AQKRU953/p1793109730716639

### cmc-spx-freeze — 14 Oct CMC SPX/NDX freeze, RCA and evidence pack
status: watching · since: 2026-10-14 · last: 2026-10-20
State: CMC's SPX price (futures and cash) froze 12:18:36-12:34:15 UTC while IC and Jump fell about 38 points; loss about 178k. Cause: CMC stayed connected and its size changes reset the stuck-filter's 10 min clock: upstream failure plus a Mahi protection gap. Andrew accepted five outcomes onto roadmap 7.2-PI-1 to 5: frozen-price detection despite quantity updates, a divergence alert (first), replay-validated quote pull, hedge availability, Jump/CMC recovery reconciliation. 20 Oct: CMC gave no rebate; its report said internal config published with errors halted pricing. Watching: no Slack activity since 20 Oct; roadmap outcomes still lack owners or dates.
Next: roadmap owners and dates for 7.2-PI-1 to 5.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1791981542846109 https://mahifx.slack.com/archives/C08ALS66EDC/p1792139709277749 https://mahifx.slack.com/archives/C08ALS66EDC/p1792490159068509

### mfp-xau-reject — HRP_MFP_Trading rejected an XAU order (24 Nov)
status: closed · since: 2026-11-24 · last: 2026-11-24 · closed: 2026-11-27
State: Kate cleared the risk to other venues after the cancel; MFP filled afterwards. Resolved.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1795527839720459 https://mahifx.slack.com/archives/C08AQKRU953/p1795528641864379

### fill-queries — Client execution, slippage and rejection queries
status: closed · since: 2026-08-27 · last: 2026-11-19 · closed: 2026-11-27
State: 19 Nov XAUUSD limit rejected as off market vs the 1ms-old internal book; Alexandre accepted. Resolved.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1795090566237569

### hedger-ew-ic-split — Temporary hedger bias: sell at EW, buy at IC (20 Nov)
status: closed · since: 2026-11-20 · last: 2026-11-20 · closed: 2026-11-23
State: Alexandre asked about biasing the hedger to sell at EW and buy at IC briefly; Kate: needs fake positions plus hedging rules. Dropped.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1795170989628879

### xau-offbook-148 — 12 Nov XAUUSD off-book long, 148_ risk split
status: closed · since: 2026-11-12 · last: 2026-11-16 · closed: 2026-11-17
State: Oliver approved splitting 148_ risk by classification; done 16 Nov.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1794824898300319

### c-book-slippage-file — C book (122_*) slippage file
status: closed · since: 2026-11-10 · last: 2026-11-16 · closed: 2026-11-17
State: No throttling; accepted by Alexandre 16 Nov.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1794847070992339

### hedge-step-size — Hedging with an incorrect step size (13 Nov)
status: closed · since: 2026-11-13 · last: 2026-11-13 · closed: 2026-11-20
State: merged into cmc-futs-dropouts.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1794577665079449

### cpi-skew-drop — 10 Nov CPI drop in FI PL on SI and retail skew
status: closed · since: 2026-11-10 · last: 2026-11-11 · closed: 2026-11-20
State: merged into fx-pnl-drop.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1794393541339619

### ndx-min-qty-reject — NDXUSD 0.01 order rejected by CMC min quantity
status: closed · since: 2026-11-09 · last: 2026-11-09 · closed: 2026-11-20
State: merged into exec-rule-requests.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1794239314132049

### fok-partial-fill — 26 Oct SI XAUUSD partial-fill FOK break
status: closed · since: 2026-10-26 · last: 2026-10-26 · closed: 2026-11-20
State: merged into position-breaks.
Refs: https://mahifx.slack.com/archives/C08ALS66EDC/p1793015998283009

### psm-inv-rollout — Predictive spread modulation on the INV model
status: closed · since: 2026-09-01 · last: 2026-10-14 · closed: 2026-11-23
State: PSM live on INV 13-14 Oct (+$0.83/M in beta); no activity since; assumed resolved.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1791971029551609

### compass-26-4 — Compass 26.4 upgrade and dashboard deploys
status: closed · since: 2026-10-08 · last: 2026-10-09 · closed: 2026-11-23
State: 26.4 live at the 10-11 Oct restart; assumed resolved.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1791543772435149

### xau-bad-print — 11 Sep XAUUSD bad print (CPI)
status: closed · since: 2026-09-11 · last: 2026-09-15 · closed: 2026-11-16
State: Bad print at CPI; sanity check enabled 15 Sep.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1789463134083049

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
