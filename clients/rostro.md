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
last_catchup: 2026-11-13T08:15:09Z
status: active
---

## Now
Relationship under strain: on 14 Oct a CMC futures price freeze cost the SI book about 178k and Andrew Morgan called it "relationship losing level"; evidence went to Rostro, CMC gave no rebate, and on 16 Oct Andrew accepted five pricing-integrity outcomes onto the roadmap (incident still open, no owners or dates yet). The C book client also complained of slippage on 16 Oct, traced to an LR mismatch. Commercials: Rostro accepted the new commercials with Mahi fees discounted by a $150K repayment settlement over 15 months (likely crypto licence, wants weekend gold); Bonnie reported the new terms signed on 11 Nov. Rostro keeps adding IC sub-account books (rev-share); PSM live on INV since 14 Oct. 12 Nov: FX book down about 20k (GBPNZD roll fallback; gold off-book long); continuity markup rise proposed. Futures (DOW/SPX/NDX) were switched to IC on 10 Nov, rolled back to CMC, and on 11 Nov flipped to IC again after test trades; Rostro wants all futures on IC for now. Sub 11 live since 2 Nov.

## Streams

### gbpnzd-roll-price — GBPNZD continuity-pool fallback at roll and continuity markup
status: open · since: 2026-11-10 · last: 2026-11-13
State: On 2 Nov GBPNZD fell back to the continuity pool at 22:01 UTC (one LP quoting). On the 11 Nov roll the INV model for GBPNZD dropped out under 0.5s and the continuity pool priced about 42 pips wide vs about 90 for the model; six 127_ accounts bought 1.8M within 30ms, hedged via GBPUSD/NZDUSD at roll spreads, hitting non-rev-share PnL. 127_ did the same in GBPUSD on 22 Oct at smaller size. Kate proposed raising the continuity markup (now $50/M) in roll and twilight windows: roll 21:59-23:00 UTC $1,000/M NZD/CHF crosses, $500/M other crosses, $300/M majors; twilight $150/$100/$50 per M, on A_CLIENTS, SCOPE_X_RETAIL/INSTI/VIP. Alexandre said yes; Riz (13 Nov) asked about blocking trading when there is no price instead, but said to apply the levels today and go indicative if clients complain.
Next: Kate to apply the continuity markups (Riz asked for today, ahead of roll); Rostro to revisit indicative-instead-of-continuity if spreads cause complaints.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1794306214114219 https://mahifx.slack.com/archives/C08AQKRU953/p1794507216428059 https://mahifx.slack.com/archives/C08AQKRU953/p1794545552790469

### fx-pnl-drop — SI/non-rev-share FX PnL drops (10-12 Nov) and exposure query
status: open · since: 2026-11-11 · last: 2026-11-12
State: Alexandre reported FX down about 10k on 10 Nov, 5k on 11 Nov and about 20k on 12 Nov on small volume (about -200 per million). Kate traced 12 Nov's drop partly to the GBPNZD roll fallback (see gbpnzd-roll-price) and the gold part to xau-offbook-148; FX and metals share one book so there is no standalone FX VaR. Alexandre asked if a -43.5M summed USD exposure is expected; Kate confirmed it matches SI_BOOK plus NON_REV_SHARE_CLIENTS pair by pair but is not open exposure (crosses are hedged in the drivers, so it nets by currency). Alexandre then said it may be a reporting issue on his side (end-of-day prices the night before). The 11 Nov ~5k drop was never explained in what was read.
Next: Alexandre to finish his own PnL/exposure reconciliation; Kate to report the cause of the 11 Nov SI FX drop if still wanted.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1794393610189339 https://mahifx.slack.com/archives/C08AQKRU953/p1794507740719929

### xau-offbook-148 — 12 Nov XAUUSD off-book long and risk splitting for the 148_ tag set
status: open · since: 2026-11-12 · last: 2026-11-12
State: About 20k was lost around 15:00 UTC on 12 Nov: the off book built a long of about 3koz between 14:55 and 14:57 as clients (mainly 152_1_300402 and a handful incl. 148_0_43886_n/a, 1,120oz over 132 fills) sold into a roughly $10 drop. Kate says the counterparty flagged earlier was hedged within seconds, so not the cause. 148_0_43886_n/a is classified signal follow and broker (about $330/M at 4 min over the month) but the 148_* risk splitting rule, set at Rostro's request, sends all 148_ flow to the off book regardless of classification. Kate proposed splitting 148_ by classification so signal follow, broker and fast hedge flow goes to the SI book (execution unaffected); no answer seen.
Next: Alexandre/Oliver to approve or decline splitting 148_ risk by classification.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1794502387640839 https://mahifx.slack.com/archives/C08AQKRU953/p1794503863384269

### hedger-cp-tag — Hybrid hedger orders to IC lost the HybridHedger counterparty tag
status: open · since: 2026-11-11 · last: 2026-11-11
State: Alexandre saw no HybridHedger-tagged trades since Monday 9 Nov and reads a client tag on IC hedges as brokered/fast hedge, not risk-cycle hedging. Kate: hedging is unchanged, but since the restart after the weekend server maintenance the SI-book hybrid hedger sends the counterparty of the most recent client trade in the instrument (skipping tags not allowed on the LP) instead of replacing it with HybridHedger. Mahi can add config to always send HybridHedger; reverting needs a hedger restart (intraday possible, brief downtime). Alexandre asked if it can be reverted on the fly; no decision seen.
Next: Alexandre to decide whether he wants the fixed HybridHedger tag restored.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1794393367585939 https://mahifx.slack.com/archives/C08AQKRU953/p1794415781616949

### cpi-skew-drop — 10 Nov CPI drop in FI PL on SI and retail skew
status: open · since: 2026-11-10 · last: 2026-11-11
State: Alexandre reported a drop in FI PL around the CPI print (-11k on SI, -2k on retail). Rory King found it was a benchmarking artefact: for a few seconds after the print most LPs in the skew benchmark stopped quoting and the remaining one was very wide, so skew was measured against an unfit reference; Mahi's price followed the venue it executed and hedged on. Alexandre asked whether the drop is not real and only a reporting issue (19:32 UTC) and repeated the question on 11 Nov (10:39 UTC); no answer seen.
Next: Rory/Kate to answer Alexandre's question.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1794329146184069 https://mahifx.slack.com/archives/C08AQKRU953/p1794393541339619

### c-book-slippage-file — C book (122_*) client slippage file, tick throttle suspected
status: open · since: 2026-11-10 · last: 2026-11-10
State: After a call that morning, Alexandre sent Kate the file from the client behind sub tag 122_* (C book) that complained of slippage; he sees little slippage on the book before execution and suspects the client's own tick throttle, since it consumes a lot of liquidity quickly. Daria Horton said Mahi will review with Kate. Earlier C book slippage cause is in c-book-lr-price.
Next: Kate/Daria to analyse the file; Alexandre awaiting the client's throttle level.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1794347283583259 https://mahifx.slack.com/archives/C08AQKRU953/p1794347926666539

### cmc-futs-dropouts — CMC as sole futures LP: recurring dropouts and rejects
status: open · since: 2026-08-26 · last: 2026-11-11
State: CMC was the only LP pricing gold futures (and XAUFUT, indices), so each dropout (25 Aug, 5 Oct, 29 Oct NDXUSD 15s gap) leaves no price or fill. 15 Oct Rostro moved most futures volume off Jump; Kate removed Jump from the futures hedgers; NDXFUT-Z was mapped wrongly in PXM after the roll (no NDXFUT flow reached Mahi). Broker-first only helps if Jump joins the XAUFUT reference price (Rostro undecided, Riz not optimistic on CMC). 10 Nov: Oliver approved moving DOWFUT/SPXFUT/NDXFUT hedging and pricing (all models) to IC_MARKETS, with brokered rules left on CMC; Kate switched them (~11:05-11:50 UTC). IC clears were cancelled and NQ rejects appeared (IC config, Scope pool change needing EOD restart), so Scope switched back to CMC. 11 Nov: IC test trades accepted 0.1 for ES/NQ/YM; IC mins are ES 0.5, NQ 0.2, YM 0.1; Oliver asked to flip NAS/SPX/DOW back to IC, Kate switched after test trades and bounced the SI futures hedgers (~14:36 UTC). Oliver: for now all futures go to IC, and clients chosen for CMC get execution rules brokering to CMC. Kate will set up a CMC liquidity pool live from EOD 11 Nov and suggests waiting for the EOD restart to change the brokering rules for SPXFUT/DOWFUT/NDXFUT; Oliver replied ok. Kate also asked whether to set up futures widening (Mahi priced inside IC's spread about half the time over a week); no answer. Hedging min qty now NDX 0.2, DOW 0.05, SPX 0.5, DAX 0.25, XAU 0.01.
Next: Kate to apply the futures brokering-rule changes after the EOD restart and watch for IC rejections (Oliver asked); Rostro to confirm hedging min quantities against IC and say whether to set up futures widening; Rostro decision on Jump in XAUFUT reference price (Jump is being switched off, check it still stands); Alex to fix NDXFUT-Z mapping in PXM; Kate's CMC-normalisation backtest.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1787733565831759 https://mahifx.slack.com/archives/C08AQKRU953/p1791970984817549 https://mahifx.slack.com/archives/C08AQKRU953/p1794317966817829 https://mahifx.slack.com/archives/C08AQKRU953/p1794407794037449

### ic-sub-books — IC sub-account rev-share books (SUB 5/9/10/11, C House, Sub SI House)
status: open · since: 2026-08-24 · last: 2026-11-09
State: Rostro flow from specific counterparty tags is split into separate Compass books, each hedged via a dedicated hybridHedgerSub* to an IC_SUBS_* market through Scope's PXM Mahi_3 connection (shared MAHI_IC_SUBS stream; Mahi sends tag 1 = MAHI_IC_SUBS_n). Tag 251_* (large Cyprus retail broker, soft flow) has FX, CFD, futures and "Sub SI House" books; its rev share was signed 13 Oct. IC_SUBS_12 set up 19-20 Oct; sub 8 (XAU book) funded 30 Oct. Sub 11 went live 2 Nov: Rostro keeps indices direct to IC; XAUUSD, XAGUSD, G7 FX and futures (DAX, NDX, SPX, DOW, XAU) go via Mahi, with tags 251_0 and 79_30 (VIP Vol, always internalised) split to the off book or SI book and hedged to IC_SUBS_11. 3-4 Nov hedging misbehaved (XAG, USDJPY, DAX fut): Kate fixed a missing risk splitting rule, moved sub 11 back to the SI book and set an interim rule internalising the XAG tags.  Kate removed HRP_Saxo (MAHI_2 "account not found") pending Scope's EOD restart. 6 Nov Kate added a higher-priority internalise futures rule after one trade went to CMC. Sub 11 is going into the 15 min SI cycle (FX and metals done, futures being looked at). 9 Nov Oliver planned to send 50% of sub 11 trades to Mahi (Mahi accepts min 0.01oz), then reported silver futures still going to CMC; Kate said Mahi does not price silver futures for Rostro and Oliver said it was on his side.
Next: Kate to finish the 15 min SI cycle for sub 11 futures and fix risk splitting so sub 11 XAG hedges to IC_SUBS_11 (replacing the interim rule); re-add HRP_Saxo after Scope's restart; sub 8 test trades and go-live; confirm MAHI_IC_SUBS_12 funded; internal question on how multi-region (NY4) is charged; send the Sub SI House holding-period page to Rostro.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1787569899244609 https://mahifx.slack.com/archives/C08AQKRU953/p1793366254660579 https://mahifx.slack.com/archives/C08AQKRU953/p1793968140238289 https://mahifx.slack.com/archives/C08AQKRU953/p1794231007095749

### ndx-min-qty-reject — NDXUSD 0.01 order rejected by CMC min quantity
status: open · since: 2026-11-09 · last: 2026-11-09
State: Alexandre asked why order 72961136 was rejected on NDXUSD (15:29 UTC 9 Nov). Kate found Compass sets CMC minimum quantity at 0.02 but the order was 0.01. Alexandre said the tag (48_0_950003) has had no flow since October, so he changed its classification until volume returns; Kate said its yields are offside by 30s and suggested an internalise rule up to a notional to sidestep the minimum and pre-empt bigger volume. Kate then made a change at 15:48 and Alexandre will have the client retry.
Next: Alexandre to confirm the retry works; optional internalise-up-to-notional rule for the tag.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1794238189537329 https://mahifx.slack.com/archives/C08AQKRU953/p1794239314132049

### adaptive-skew-pitch — Move Rostro onto adaptive skew after NFP
status: open · since: 2026-11-06 · last: 2026-11-06
State: Will Carter said Rostro's B_INSTI_VIP book barely moved on the 6 Nov NFP release (13:30-13:33 UTC): skew about $3/M, LR $4/M, versus IC Crypto skew about $430/M and Infinox gold LR $125/M after his 15:48 correction (volume $56M, not the $170M first posted). He proposes replaying the release on a sim with an adaptive skew config, showing the client before/after skew PnL and switching on the measured result. Kate is looking at the skew setup. Skew is currently off on USDJPY/EURUSD for the VIP trial (see vip-trial-skew).
Next: owner needed for the adaptive-skew sim this week; Kate reviewing the skew set-up.
Refs: https://mahifx.slack.com/archives/C08ALS66EDC/p1793975301078089 https://mahifx.slack.com/archives/C08ALS66EDC/p1793980120503819

### position-breaks — Position breaks and position recs
status: open · since: 2026-09-04 · last: 2026-11-05
State: Breaks booked manually 8 Sep, 17 Sep and 2 Oct. On 28 Oct Kate booked positions in the rev share book (hedger off while booking, done by 15:48 UTC) to fix long-term breaks left by the earlier Centroid issue. On 5 Nov Alexandre flagged a new 2k GBPJPY break on the SI book vs Scope's coverage account, begun between 18:20 and 22:20 UTC on 4 Nov; Rory King said Mahi hedges in drivers (GBPUSD, USDJPY), and that two trades cancelled and re-sent were filled just after 22:00 UTC (72725714-2 and 72725715-2 replaced -1); he asked for the coverage account position; no answer seen.
Next: Alexandre to share the coverage account position for GBPJPY; Cameron to roll out the VaR alerting now the booking is done.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1788504725919689 https://mahifx.slack.com/archives/C08ALS66EDC/p1793199991187849 https://mahifx.slack.com/archives/C08AQKRU953/p1793892499283759

### exec-rule-requests — Execution rule and routing requests (brokered vs internalised)
status: open · since: 2026-08-18 · last: 2026-11-04
State: Rostro keeps asking for per-tag rule changes (internalise XAGUSD from 122_*, toxic tags to the LDN liquidity pool, blacklist 163_0_88068 from brokering, broker tags on gold and index futures). Kate suggested force-internalising the two arb non rev share broker rules; no answer seen. On 20 Oct Oliver wanted an execution rule for one client in the non rev share book (SI book, VIP Vol model, "insti vip"); Kate offered help setting it up and Oliver said he will let her know. On 2 Nov Alexandre asked for price improvement for a VIP end client with multiple APIs (150_, 146_, 148_, 105_, 41_, later also 160_); Kate copied the Force Internalise: VIP rule, added a counterparty criteria and published it as a new INSTI VIP execution rule. On 4 Nov Alexandre asked to start brokering tag 165_0_n/a in NDX FUT and Kate published a rule for it (thanks, 16:25 UTC); the same day an SI book brokering rule was found catching sub 11 XAG tags, so Kate internalised that flow (see ic-sub-books).
Next: Alexandre to confirm the new INSTI VIP rule gives the intended price improvement.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1787068816321309 https://mahifx.slack.com/archives/C08AQKRU953/p1792510778793009 https://mahifx.slack.com/archives/C08AQKRU953/p1793640528566759 https://mahifx.slack.com/archives/C08AQKRU953/p1793806802597919

### commercials-reneg — Commercial renegotiation, value-add and relationship
status: open · since: 2026-08-19 · last: 2026-11-11
State: New Rostro terms signed (Bonnie, 11 Nov). Draft declined 15 Sep; after mid-Oct talks Rostro accepted terms with fees discounted by a $150K repayment settlement over 15 months (crypto licence likely, interested in weekend gold). Sam Steele wants two sessions, on the crypto tool and the equities portfolio tool (Andrew thinks single stocks are the bulk of Rostro's business, so Mahi may need to close a gap); his meeting is booked for the 13th (month not stated, presumably Nov). Kate delivered a value-add report 15 Oct; tailored models are being built. Alex asked about kilo gold; Kate said Mahi can do it, Andrew said charge where possible. 3 Nov call (Kate): Rostro happy to set up global LR, conservative at $5/M max; considering pricing into Integral, but Kate's early read (-$60/M on inception or worse) is poor and she asked for a dataset. Rostro's group got a crypto registration in the BVI.
Next: Rostro to send Integral flow dataset; set up global LR (max $5/M); prepare for the Sam Steele meeting on the 13th (crypto tool, then equities); consider charging for kilo gold.
Refs: https://mahifx.slack.com/archives/C08ALS66EDC/p1787135711511859 https://mahifx.slack.com/archives/C08ALS66EDC/p1792485246173679 https://mahifx.slack.com/archives/C08ALS66EDC/p1793703042394719 https://mahifx.slack.com/archives/C08ALS66EDC/p1794388096504289

### pxm-order-handling — PXM order splitting, boost, latency and tick throttle
status: open · since: 2026-09-30 · last: 2026-10-30
State: PXM splits large FA/VIP orders into tier-sized clips so fills land near TOB not VWAP (30 Sep, 6 Oct). PXM boost off suits limit orders but market orders then sweep too; LR is the only in-product fix and the no-slippage agreement rules it out; Kate proposes asking PXM for per-order-type boost. Client latency traced to tick throttles in Mahi's VIP distribution and PXM (Mahi VIP 2 per 10ms, PXM 1 per ms). On 30 Oct Alexandre said the VIP end client still sees 12ms tick latency; Scope's PXM sampling interval is 5 and he wants 3 and Mahi ticks per 10ms at 7. Kate wanted a fresh dataset first (every tick was being published after the last change); Alexandre has no dataset, so he will lower the PXM sample interval and Mahi will check next week whether every tick is published.
Next: PXM/Alex on pass-through or per-order-type boost; Kate to review tick publishing next week after the PXM sampling change (no dataset from the end client); Kate to check protective throttling on Mahi side before Rostro changes the PXM throttle.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1790776376391349 https://mahifx.slack.com/archives/C08ALS66EDC/p1791298744478709 https://mahifx.slack.com/archives/C08ALS66EDC/p1791883456395629 https://mahifx.slack.com/archives/C08AQKRU953/p1793361779461789

### vip-trial-skew — VIP end-client final trial: skew off on USDJPY/EURUSD
status: open · since: 2026-10-30 · last: 2026-10-30
State: Alexandre said the end client behind tag ending 100029 (most of VIP flow on USDJPY/EURUSD) is on its last trial week with Scope and will switch Scope off if unhappy, and asked for skew to be disabled. Skew is per price stream, not per tag, so Kate turned skew off on USDJPY and EURUSD on the VIP feed for the trial (price-based signals still apply to others), to be reviewed afterwards; the alternative is skew on with this tag's trades excluded from the signals, as its own trades drive most of the skew it sees. Tick latency side is in pxm-order-handling.
Next: Kate to review skew after the trial and decide between skew on with the tag excluded from signals or staying off.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1793361779461789 https://mahifx.slack.com/archives/C08AQKRU953/p1793372430907599

### pxm-connections — PrimeXM connections, LP list and feeds
status: open · since: 2026-09-04 · last: 2026-10-27
State: PXM taker connections cleaned up (7 Sep); MAHI_3 added 30 Sep for the IC_SUBS stream. On 14 Oct, Mahi found the VIP price session in PXM never requests XAGUSD, so Alex sees the INV book on VIP silver.
On 26 Oct Alexandre added the missing XAGUSD spread config on the FA stream; on 27 Oct Kate confirmed risk splitting for XAGUSD on FA was fine, Scope's test trade was routed to the off book and Kate said it looked good. Alexandre is still tweaking the XAGUSD spread config (no BMSL set on silver, even on the SI) and Kate offered to check the setup against his target spreads/widening.
Next: Alexandre to add XAG/USD to the VIP price session in PXM; Alexandre to share target XAGUSD spreads/widening if he wants Kate to check the setup.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1788508022729149 https://mahifx.slack.com/archives/C08AQKRU953/p1790608061088529 https://mahifx.slack.com/archives/C08AQKRU953/p1793051109437589 https://mahifx.slack.com/archives/C08AQKRU953/p1793109730716639

### fok-partial-fill — 26 Oct SI XAUUSD position break from partial-fill FOK brokering
status: open · since: 2026-10-26 · last: 2026-10-26
State: Scope (Alexandre) flagged a -1.2M average SI short held since Friday; Kate traced it to partial fills on FOK orders attempted to broker: 400oz orders got 350oz from the LPs, one was topped up 50oz (long 50oz) and for the other the client trade was cancelled, leaving the house short 300oz at the LPs. Oliver later said the position looked right. Kate turned off the hedger-to-book position adjustment, set a high-VAR alert on the Retail A Book tenant profile and asked Oliver to rec CLIENTS_NET positions; Riz's rule had top-up allowed.
Next: Riz to confirm whether top-up allowed was intended on the rule; Kate to answer Scope's partial-fill detection question; Oliver to rec CLIENTS_NET positions.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1793005750513019 https://mahifx.slack.com/archives/C08AQKRU953/p1793006840087599 https://mahifx.slack.com/archives/C08ALS66EDC/p1793015998283009

### fill-queries — Client execution, slippage and rejection queries
status: open · since: 2026-08-27 · last: 2026-10-23
State: 23 Oct Rahul reported 57 of 86 orders negative slippage on a sub-account; Kate: brokered to IC after classification briefly flagged the account, internal fills got the shown price. 22 Oct a USDJPY Limit IOC to IC sat 3 min (IC connection reset), tripping an order-breach limit; no open risk.
Next: Rostro to say whether to change the LP, internalise, or relax the anti-spoof node; no reply seen.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1787835257505189 https://mahifx.slack.com/archives/C08AQKRU953/p1792665379140899 https://mahifx.slack.com/archives/C08AQKRU953/p1792781435455779 https://mahifx.slack.com/archives/C08AQKRU953/p1792782045722059

### cmc-spx-freeze — 14 Oct CMC SPX/NDX freeze, RCA and evidence pack
status: open · since: 2026-10-14 · last: 2026-10-20
State: CMC's SPX price (futures and cash) froze 12:18:36-12:34:15 UTC while IC and Jump fell about 38 points after the 12:30 print. Loss about 178k (SPX fut -145k, SPX cash -23k, NDX cash -10k); roughly 114k client trades at the frozen price Cause: CMC stayed connected and its size changes reset the stuck-filter's 10 min clock (reproduced in Will's replays): upstream failure plus a Mahi protection gap. Evidence went to Rostro 14 Oct. Andrew accepted five outcomes onto roadmap 7.2-PI-1 to 5: quantity-only updates must not hide frozen prices, divergence alert vs a normalised reference (first), quote pull at a replay-validated threshold, hedge availability alongside pricing health, and reconciling the Jump repricing with any CMC recovery. 20 Oct: CMC gave no rebate; its incident report said internal config was published with errors halting pricing.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1791981542846109 https://mahifx.slack.com/archives/C08ALS66EDC/p1792137303134229 https://mahifx.slack.com/archives/C08ALS66EDC/p1792139709277749 https://mahifx.slack.com/archives/C08ALS66EDC/p1792490159068509

### c-book-lr-price — C book slippage: LR applied at fill but not in quoted price
status: open · since: 2026-10-16 · last: 2026-10-16
State: Alexandre said the C book client complained of slippage on 15 Oct gold (filled 4151.71 vs quote 4151.52/4151.64, no market move). Isaac found the cause: on the multi-channel SCOPE_X_FA session, XAUUSD orders from 122_0_* and 117_27* execute on C_CLIENTS and take its liquidity reduction, but the streamed price is built from SCOPE_X_FA and carries only that channel's LR. Options: a suffixed XAUUSD.c instrument with extra bridge routing on Rostro's side, or a global per-process LR (per-channel caps). Isaac disabled LR on C_CLIENTS meanwhile.
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

### xau-bad-print — 11 Sep Jane Street XAUUSD bad print (CPI) and missing price guard
status: watching · since: 2026-09-11 · last: 2026-09-15
State: At the 12:30 UTC CPI release the XAUUSD reference panel collapsed to Jane Street alone while its bid went erratic, so published variants on this book hit a $319.84 spread at 12:30:03 for about 2s. No filter engaged: the outlier filters only run on a crossed book, and the sanity check was off since go-live at Rostro's request. Riz pulled Jane Street from the XAU reference selectors; XAUUSD sanity check enabled 15 Sep.
Next: Kate to decide whether to adjust bad-tick fills.
Refs: https://mahifx.slack.com/archives/C08ALS66EDC/p1789131695104789 https://mahifx.slack.com/archives/C08ALS66EDC/p1789373254421619 https://mahifx.slack.com/archives/C08AQKRU953/p1789463134083049

### centroid-b2c-prices — B2C Centroid connection showed no GBPNZD prices
status: closed · since: 2026-10-28 · last: 2026-10-28 · closed: 2026-11-02
State: GBPNZD missing on B2C Centroid; traced to an MT5 filter on Scope's side.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1793187010016709 https://mahifx.slack.com/archives/C08AQKRU953/p1793189507174379

### c-book-clearance — C book risk clearance speed (15 Oct gold)
status: closed · since: 2026-10-15 · last: 2026-10-15 · closed: 2026-11-11
State: 15 Oct 30M C book clearance took ~5 min; Kate turned off fill-ratio adjustment on the hedgers; assumed resolved.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1792078136400489 https://mahifx.slack.com/archives/C08ALS66EDC/p1792081751691529

### pulse-athena-access — Rostro cannot read Pulse/Athena from new IP
status: closed · since: 2026-08-27 · last: 2026-09-09 · closed: 2026-11-05
State: assumed resolved.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1787822793611979 https://mahifx.slack.com/archives/C08AQKRU953/p1788950130321199

### brokered-lr-review — Brokered last-look yield decline
status: closed · since: 2026-08-25 · last: 2026-09-01 · closed: 2026-11-02
State: assumed resolved or superseded (PSM live on INV).
Refs: https://mahifx.slack.com/archives/C08ALS66EDC/p1787649194353099 https://mahifx.slack.com/archives/C08ALS66EDC/p1787740328562409 https://mahifx.slack.com/archives/C08ALS66EDC/p1788280858317659

### oil-incident-rca — July oil reference-feed incident RCA
status: closed · since: 2026-08-17 · last: 2026-09-01 · closed: 2026-11-02
State: assumed resolved (RCA sent Aug).
Refs: https://mahifx.slack.com/archives/C08ALS66EDC/p1786988498348909 https://mahifx.slack.com/archives/C08ALS66EDC/p1788273338625779

## Arc
- 2025 — Rostro live on Compass (per Kate, 2026-09-14, sanity check disabled before go-live)
- 2026-05 — Lochlan, key contact championing Mahi, left Rostro for OZ; Saul Knapp left for MAS Markets
- 2026-07-14 — oil reference-feed incident (~$350k client loss) raised by Rostro; Mahi offers no goodwill
- 2026-07-30 — Sam Steele intro meeting; asks for documented safeguards, not reimbursement
- 2026-08-25 — commercial renegotiation and joint PR started at Rostro's request
- 2026-09-15 — Rostro did not sign the new commercials draft ("a no from the board")
- 2026-10-14 — PSM live on INV; CMC SPX freeze costs ~178k, treated as relationship-level risk
- 2026-10-16 — Andrew accepts five pricing-integrity outcomes from the CMC freeze RCA onto the roadmap
- 2026-10-20 — Rostro accepts new commercials with a $150K repayment settlement over 15 months
- 2026-11-11 — new Rostro terms signed
