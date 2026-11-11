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
  - {name: "Rakan Awwad", role: "ScopeMarkets ops: FIX rejection queries", confidence: low}
  - {name: "Manuel de Cara", role: "Rostro: Pulse/Athena data access", confidence: low}
  - {name: "Sam Steele", role: "Group Chief Strategy Officer at Rostro; commercial counterpart (described internally as basically co-founder)"}
  - {name: "Michael Ayres", role: "senior Rostro contact meeting David Cooney 16 Oct; named replacement after Lochlan left", confidence: low}
last_catchup: 2026-11-11T08:13:54Z
status: active
---

## Now
Relationship under strain: on 14 Oct a CMC futures price freeze cost the SI book about 178k and Andrew Morgan called it "relationship losing level"; evidence went to Rostro, CMC gave no rebate, and on 16 Oct Andrew accepted five pricing-integrity outcomes onto the roadmap (incident still open, no owners or dates yet). The C book client also complained of slippage on 16 Oct, traced to an LR mismatch. Commercials: after David Cooney and Michael Ayres met, Rostro accepted the new commercials with Mahi fees discounted by a $150K repayment settlement over 15 months, and is likely to take a crypto licence and wants weekend gold (Andrew, 20 Oct); the contract is being drafted. Rostro keeps adding IC sub-account books (rev-share), PSM went live on the INV model 14 Oct, and Rostro is switching Jump off futures (hedgers updated 15 Oct).  On 10 Nov futures (DOW/SPX/NDX) hedging and pricing were switched to IC then rolled back to CMC the same day after IC config issues; Oliver will flip back once confirmed. Sub 11 went live 2 Nov (XAUUSD, XAGUSD, G7 FX and futures via Mahi; Rostro keeps indices direct to IC), and Scope's VIP end client is on a final trial week with skew switched off on USDJPY/EURUSD (30 Oct).

## Streams

### cpi-skew-drop — 10 Nov CPI drop in FI PL on SI and retail skew
status: open · since: 2026-11-10 · last: 2026-11-10
State: Alexandre reported a drop in FI PL around the CPI print (-11k on SI, -2k on retail). Rory King found it was a benchmarking artefact: for a few seconds after the print most LPs in the skew benchmark stopped quoting and the remaining one was very wide, so skew was measured against an unfit reference; Mahi's price followed the venue it executed and hedged on. Alexandre asked whether the drop is not real and only a reporting issue (19:32 UTC); no answer seen.
Next: Rory/Kate to answer Alexandre's question.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1794329146184069 https://mahifx.slack.com/archives/C08AQKRU953/p1794339139125119

### c-book-slippage-file — C book (122_*) client slippage file, tick throttle suspected
status: open · since: 2026-11-10 · last: 2026-11-10
State: After a call that morning, Alexandre sent Kate the file from the client behind sub tag 122_* (C book) that complained of slippage; he sees little slippage on the book before execution and suspects the client's own tick throttle, since it consumes a lot of liquidity quickly. Daria Horton said Mahi will review with Kate. Earlier C book slippage cause is in c-book-lr-price.
Next: Kate/Daria to analyse the file; Alexandre awaiting the client's throttle level.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1794347283583259 https://mahifx.slack.com/archives/C08AQKRU953/p1794347926666539

### cmc-futs-dropouts — CMC as sole futures LP: recurring dropouts and rejects
status: open · since: 2026-08-26 · last: 2026-11-10
State: CMC is the only LP pricing gold futures (and XAUFUT, indices), so each dropout (25 Aug, 5 Oct, 29 Oct NDXUSD 15s gap that rejected an A_CLIENTS sell) leaves no price or fill; 9 Sep DAXFUT-U showed stale CMC prices and Kate promised a CMC-normalisation backtest. 14 Oct CMC filled 800 of a 1,000-lot XAUFUT-Z sweep then expired the rest (see cmc-spx-freeze for the freeze). 15 Oct Rostro moved most futures volume off Jump; Kate removed Jump from the futures hedgers; NDXFUT-Z was mapped wrongly in PXM after the roll (no NDXFUT flow reached Mahi). Broker-first only helps if Jump joins the XAUFUT reference price (Rostro undecided, Riz not optimistic on CMC). 10 Nov: Oliver approved moving DOWFUT/SPXFUT/NDXFUT hedging and pricing (all models) to IC_MARKETS, with brokered rules left on CMC; Kate switched them (~11:05-11:50 UTC). By 13:38 DOWFUT-Z clears to IC were cancelled and NQ missing-price rejects appeared. Kate set hedging min quantity to 1 as a stopgap, but the cause was IC's own config on the CMC market and Scope's pool change needing an EOD restart; Scope switched back to CMC (14:54) and Kate reverted min quantity (15:11). Oliver will flip back to IC once confirmed. Kate also flagged no futures market widening: Mahi priced inside IC's spread 66% SPX, 47% NDX, 51% DOW and inside CMC's 79% DAX, 57% XAU over a week; Alexandre has not answered. Hedging min qty now NDX 0.2, DOW 0.05, SPX 0.5, DAX 0.25, XAU 0.01.
Next: Oliver to confirm and redo the IC switch after Scope's restart aligns the pool; Rostro to confirm min hedging quantities for IC and CMC and say whether to set up futures widening; Rostro decision on Jump in XAUFUT reference price (Jump is being switched off, check it still stands); Alex to fix NDXFUT-Z mapping in PXM; Kate's CMC-normalisation backtest.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1787733565831759 https://mahifx.slack.com/archives/C08AQKRU953/p1791970984817549 https://mahifx.slack.com/archives/C08ALS66EDC/p1794225217062859 https://mahifx.slack.com/archives/C08AQKRU953/p1794317966817829

### ic-sub-books — IC sub-account rev-share books (SUB 5/9/10/11, C House, Sub SI House)
status: open · since: 2026-08-24 · last: 2026-11-09
State: Rostro flow from specific counterparty tags is split into separate Compass books, each hedged via a dedicated hybridHedgerSub* to an IC_SUBS_* market through Scope's PXM Mahi_3 connection (shared MAHI_IC_SUBS stream; Mahi sends tag 1 = MAHI_IC_SUBS_n). Tag 251_* (large Cyprus retail broker, soft flow) has FX, CFD, futures and "Sub SI House" books; its rev share was signed 13 Oct. IC_SUBS_12 set up 19-20 Oct; sub 8 (XAU book) funded 30 Oct. 22 Oct IC market data dropped (net 20oz unhedged until Scope refreshed the connection). Sub 11 went live 2 Nov: Rostro keeps indices direct to IC; XAUUSD, XAGUSD, G7 FX and futures (DAX, NDX, SPX, DOW, XAU) go via Mahi, with tags 251_0 and 79_30 (VIP Vol, always internalised) split to the off book or SI book and hedged to IC_SUBS_11. 3-4 Nov hedging misbehaved (XAG, USDJPY, DAX fut): Kate fixed a missing risk splitting rule, moved sub 11 back to the SI book and set an interim execution rule internalising the XAG tags caught by an SI book brokering rule (risk to normal IC feed, Rostro flat). Abdullah asked Mahi to stop hedging an account rejecting "account not found" (HRP_Saxo, MAHI_2); Kate removed it pending Scope's EOD restart. 6 Nov one futures trade hit the SI book broker rule and went to CMC; Kate added a higher-priority internalise futures rule. Sub 11 is going into the 15 min SI cycle (FX and metals done, futures being looked at). 9 Nov Oliver planned to send 50% of sub 11 trades to Mahi (Mahi accepts min 0.01oz), then reported silver futures still going to CMC; Kate said Mahi does not price silver futures for Rostro and Oliver said it was on his side.
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
State: Oliver flagged 622k of EUR SI net unhedged (4 Sep); Rostro pulls positions from Pulse to check; breaks booked manually on 8 Sep (151 XAUUSD) and 2 Oct (G30EUR, SPX, DOW, NDX), and a 200oz break on 17 Sep. On 28 Oct Kate booked positions in the rev share book (hedger off while booking, done by 15:48 UTC) to fix long-term breaks left by the earlier Centroid issue. On 5 Nov Alexandre flagged a new 2k GBPJPY break on the SI book vs Scope's coverage account, begun between 18:20 and 22:20 UTC on 4 Nov; Rory King said Mahi hedges in drivers (GBPUSD, USDJPY), and that two trades cancelled and re-sent were filled just after 22:00 UTC (72725714-2 and 72725715-2 replaced -1); he asked for the coverage account position; no answer seen.
Next: Alexandre to share the coverage account position for GBPJPY; Cameron to roll out the VaR alerting now the booking is done.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1788504725919689 https://mahifx.slack.com/archives/C08ALS66EDC/p1793199991187849 https://mahifx.slack.com/archives/C08AQKRU953/p1793892499283759

### exec-rule-requests — Execution rule and routing requests (brokered vs internalised)
status: open · since: 2026-08-18 · last: 2026-11-04
State: Rostro keeps asking for per-tag rule changes (internalise XAGUSD from 122_*, toxic tags to the LDN liquidity pool, blacklist 163_0_88068 from brokering, broker tags on gold and index futures). Kate suggested force-internalising the two arb non rev share broker rules (about $170M executed in 28 days, yields $58/M at 5s and $130/M at 30s); Rostro's answer not seen. Mahi cannot set percentage splits on hedge flow (25 Aug). On 20 Oct Oliver wanted an execution rule for one client in the non rev share book (SI book, VIP Vol model, "insti vip"); Kate offered help setting it up and Oliver said he will let her know. On 2 Nov Alexandre asked for price improvement for a VIP end client with multiple APIs (150_, 146_, 148_, 105_, 41_, later also 160_); Kate copied the Force Internalise: VIP rule, added a counterparty criteria and published it as a new INSTI VIP execution rule. On 4 Nov Alexandre asked to start brokering tag 165_0_n/a in NDX FUT and Kate published a rule for it (thanks, 16:25 UTC); the same day an SI book brokering rule was found catching sub 11 XAG tags, so Kate internalised that flow (see ic-sub-books).
Next: Alexandre to confirm the new INSTI VIP rule gives the intended price improvement.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1787068816321309 https://mahifx.slack.com/archives/C08AQKRU953/p1792510778793009 https://mahifx.slack.com/archives/C08AQKRU953/p1793640528566759 https://mahifx.slack.com/archives/C08AQKRU953/p1793806802597919

### commercials-reneg — Commercial renegotiation, value-add and relationship
status: open · since: 2026-08-19 · last: 2026-11-03
State: Rostro asked to renegotiate; Sam Steele challenged whether STP flow counts toward fees but wants to send all flow (1 Sep). A draft went 14 Sep and was declined 15 Sep. After David, Michael Ayres and Andrew spoke the week of 13 Oct, Rostro accepts the new commercials with Mahi fees discounted by a $150K repayment settlement over 15 months (effectively a locked contract); likely to take a crypto licence, interested in weekend gold. Susan asked 20 Oct for a contract; Bonnie asked for details to go to Nicole Vivian to draft. Sam Steele wants two sessions, on the crypto tool and the equities portfolio tool (Andrew thinks single stocks are the bulk of Rostro's business, so Mahi may need to close a gap); his meeting is booked for the 13th (month not stated, presumably Nov). 15 Oct Kate delivered a month-by-month value-add report for David; Rostro is deliberately keeping some spreads tight to win flow back, so tailored models are being built. Alex asked about kilo gold; Kate said Mahi can do it, Andrew said charge where possible. 3 Nov call (Kate): Rostro happy to set up global LR, conservative at $5/M max; considering pricing into Integral, but Kate's early read (-$60/M on inception or worse) is poor and she asked for a dataset. Rostro's group got a crypto registration in the BVI.
Next: Rostro to send Integral flow dataset; set up global LR (max $5/M); settlement details to Nicole Vivian for the contract draft; prepare for the Sam Steele meeting on the 13th (crypto tool, then equities); consider charging for kilo gold.
Refs: https://mahifx.slack.com/archives/C08ALS66EDC/p1787135711511859 https://mahifx.slack.com/archives/C08ALS66EDC/p1789481310304399 https://mahifx.slack.com/archives/C08ALS66EDC/p1792485246173679 https://mahifx.slack.com/archives/C08ALS66EDC/p1793703042394719

### pxm-order-handling — PXM order splitting, boost, latency and tick throttle
status: open · since: 2026-09-30 · last: 2026-10-30
State: PXM splits large FA/VIP orders into tier-sized clips so fills land near TOB not VWAP (30 Sep, 6 Oct). PXM's reply (13 Oct): boost off suits limit orders (it sweeps) but market orders then sweep too and Mahi cannot tell to fill tiers two and three; Liam says LR is the only in-product fix and would add slippage, ruled out by the no-slippage agreement, and calls all-TOB clipping "machine gunning". Kate proposes Alex ask PXM for pass-through or per-order-type boost. Client latency was traced to a 1-per-10ms tick throttle in Mahi's VIP distribution and in PXM: Mahi moved VIP to 2 per 10ms (6-7 Oct), Rostro raised PXM to 1 per ms, over 99% of VIP ticks now go out; Alex (8 Oct) said client latency fell 22ms to 16ms vs peer and asked for 4 per 10ms, Kate (12 Oct) doubts it helps and wants a fresh tick sample. On 30 Oct Alexandre said the VIP end client still sees 12ms tick latency; Scope's PXM sampling interval is 5 and he wants 3 and Mahi ticks per 10ms at 7. Kate wanted a fresh dataset first (every tick was being published after the last change); Alexandre has no dataset, so he will lower the PXM sample interval and Mahi will check next week whether every tick is published.
Next: PXM/Alex on pass-through or per-order-type boost; Kate to review tick publishing next week after the PXM sampling change (no dataset from the end client); Kate to check protective throttling on Mahi side before Rostro changes the PXM throttle.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1790776376391349 https://mahifx.slack.com/archives/C08ALS66EDC/p1791298744478709 https://mahifx.slack.com/archives/C08ALS66EDC/p1791883456395629 https://mahifx.slack.com/archives/C08AQKRU953/p1793361779461789

### vip-trial-skew — VIP end-client final trial: skew off on USDJPY/EURUSD
status: open · since: 2026-10-30 · last: 2026-10-30
State: Alexandre said the end client behind tag ending 100029 (most of VIP flow on USDJPY/EURUSD) is on its last trial week with Scope and will switch Scope off if unhappy, and asked for skew to be disabled. Skew is per price stream, not per tag, so Kate turned skew off on USDJPY and EURUSD on the VIP feed for the trial (price-based signals still apply to others), to be reviewed afterwards; the alternative is skew on with this tag's trades excluded from the signals, as its own trades drive most of the skew it sees. Alexandre called the skew PnL small. Tick latency side is in pxm-order-handling.
Next: Kate to review skew after the trial and decide between skew on with the tag excluded from signals or staying off.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1793361779461789 https://mahifx.slack.com/archives/C08AQKRU953/p1793372430907599

### pxm-connections — PrimeXM connections, LP list and feeds
status: open · since: 2026-09-04 · last: 2026-10-27
State: PXM taker connections were cleaned up (7 Sep) and feeds added (incl. IC_SUBS_*). A third connection (MAHI_3, done 30 Sep) was added because MAHI_2 is close to MAHI in throughput; it carries the IC_SUBS stream. On 14 Oct, Mahi found the VIP price session in PXM never requests XAGUSD, so Alex sees the INV book on VIP silver. On 16 Oct Kate confirmed no DST change is needed on Scope's side (FIX connections run on NY time).
On 26 Oct Alexandre added the missing XAGUSD spread config on the FA stream; on 27 Oct Kate confirmed risk splitting for XAGUSD on FA was fine, Scope's test trade was routed to the off book and Kate said it looked good. Alexandre is still tweaking the XAGUSD spread config (no BMSL set on silver, even on the SI) and Kate offered to check the setup against his target spreads/widening.
Next: Alexandre to add XAG/USD to the VIP price session in PXM; Alexandre to share target XAGUSD spreads/widening if he wants Kate to check the setup.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1788508022729149 https://mahifx.slack.com/archives/C08AQKRU953/p1790608061088529 https://mahifx.slack.com/archives/C08AQKRU953/p1793051109437589 https://mahifx.slack.com/archives/C08AQKRU953/p1793109730716639

### fok-partial-fill — 26 Oct SI XAUUSD position break from partial-fill FOK brokering
status: open · since: 2026-10-26 · last: 2026-10-26
State: Scope (Alexandre) flagged a -1.2M average SI short held since Friday; Oliver put it at -1028 and guessed the outage. Kate traced it to partial fills on FOK orders attempted to broker: 400oz orders got 350oz from the LPs, one was topped up 50oz (long 50oz) and for the other the client trade was cancelled, leaving the house short 300oz at the LPs. Oliver confirmed the SI house needed to be short and, after a call, said the position looked right at 09:38 UTC. Kate turned off the hedger-to-book position adjustment, set a high-VAR alert on the Retail A Book tenant profile and asked Oliver to rec CLIENTS_NET positions; Riz's rule had top-up allowed. Scope asked for a DB query to detect FOK partial fills and alert proactively.
Next: Riz to confirm whether top-up allowed was intended on the rule; Kate to answer Scope's partial-fill detection question; Oliver to rec CLIENTS_NET positions.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1793005750513019 https://mahifx.slack.com/archives/C08AQKRU953/p1793006840087599 https://mahifx.slack.com/archives/C08ALS66EDC/p1793015998283009

### fill-queries — Client execution, slippage and rejection queries
status: open · since: 2026-08-27 · last: 2026-10-23
State: On 23 Oct Scope (Rahul) queried a sub-account's EURUSD sell 72096515-1 (200k filled 1.11996 vs 500k quoted at 1.11999) and reported 57 of 86 orders with negative slippage ($106.53); Kate replied that every negatively slipped order was brokered to IC because automated classification briefly flagged the account, cleared 08:50 UTC, and internally filled orders all got the shown price; Rahul acknowledged. On 22 Oct a 100k USDJPY Limit IOC to IC sat 3 min before cancel (IC connection reset), breaching hybridHedgerOffBook1's order-breach limit and shutting it down; no open risk. Recurring ScopeMarkets fill queries, mostly LP-side behaviour on brokered flow or model behaviour. 
Next: Rostro to say whether to change the LP, internalise, or relax the anti-spoof node; no reply seen.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1787835257505189 https://mahifx.slack.com/archives/C08AQKRU953/p1792665379140899 https://mahifx.slack.com/archives/C08AQKRU953/p1792781435455779 https://mahifx.slack.com/archives/C08AQKRU953/p1792782045722059

### cmc-spx-freeze — 14 Oct CMC SPX/NDX freeze, RCA and evidence pack
status: open · since: 2026-10-14 · last: 2026-10-20
State: CMC's SPX price (futures and cash) froze 12:18:36-12:34:15 UTC while IC and Jump fell about 38 points after the 12:30 print. Loss about 178k (SPX fut -145k, SPX cash -23k, NDX cash -10k); roughly 114k client trades at the frozen price (251* sold about $31.5M into it); Rostro is the only client that dealt at it. Cause: CMC stayed connected, and its displayed-size changes in response to Mahi's unfilled hedge attempts reset the stuck-filter's 10 min clock (reproduced in Will's replays): upstream failure plus a Mahi protection gap. Evidence went to Rostro 14 Oct; PXM FIX logs were not recorded. Andrew told David the clients were remarked to the Jump rate (amendments and remaining loss to be confirmed) and accepted five outcomes onto roadmap 7.2-PI-1 to 5: quantity-only updates must not hide frozen prices, divergence alert vs a normalised reference (first), quote pull at a replay-validated threshold, hedge availability alongside pricing health, and reconciling the Jump repricing with any CMC recovery. 20 Oct: CMC gave no rebate; its incident report said internal config was published with errors halting pricing.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1791981542846109 https://mahifx.slack.com/archives/C08ALS66EDC/p1792137303134229 https://mahifx.slack.com/archives/C08ALS66EDC/p1792139709277749 https://mahifx.slack.com/archives/C08ALS66EDC/p1792490159068509

### c-book-lr-price — C book slippage: LR applied at fill but not in quoted price
status: open · since: 2026-10-16 · last: 2026-10-16
State: Alexandre said the C book client complained of slippage on 15 Oct gold (filled 4151.71 vs quote 4151.52/4151.64, no market move). Isaac found the cause: on the multi-channel SCOPE_X_FA session, XAUUSD orders from 122_0_* and 117_27* execute on C_CLIENTS and take its liquidity reduction, but the streamed price is built from SCOPE_X_FA and carries only that channel's LR. Fix offered: a suffixed XAUUSD.c instrument streaming the C_CLIENTS price, with extra bridge routing on Rostro's side. Isaac disabled LR on C_CLIENTS meanwhile (Alexandre agreed, will review). Riz asked for an alternative without a new instrument; Isaac said only a global per-process LR (with per-channel caps) can span channels, not LR grouped over selected channels.
Next: Rostro (Alexandre/Riz) to decide between XAUUSD.c routing and global LR; LR stays off on C_CLIENTS until then.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1792138607035239 https://mahifx.slack.com/archives/C08AQKRU953/p1792140741428669 https://mahifx.slack.com/archives/C08AQKRU953/p1792141257894219

### gbpnzd-roll-price — GBPNZD price source around the 2 Nov roll
status: watching · since: 2026-11-10 · last: 2026-11-10
State: Riz asked what sourced the INSTI distribution price for GBPNZD before CLIENT_PRICE_LDN started pricing at 22:01:20 UTC on 2 Nov. Kate: the channel fell back to its continuity pool, where only one LP quoted GBPNZD from 22:01:00, so it published around that LP's mid at the roll max spread, then switched back. Riz suspects the triangulated legs were missing and asked whether spread is capped; Kate offered to review the pool's LPs.
Next: Riz to say whether he wants the pool LPs reviewed; answer on the spread cap.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1794306214114219 https://mahifx.slack.com/archives/C08AQKRU953/p1794309708989839

### psm-inv-rollout — Predictive spread modulation on the INV model
status: watching · since: 2026-09-01 · last: 2026-10-14
State: Kate proposed PSM on CLIENT_PRICE_INV_LDN on 1 Sep. A Beta model ran for about a month at +$0.83/M round trip wider than INV. Rostro agreed and PSM went live 13-14 Oct.
Next: watch volumes, distributed spreads and trade spread distribution after go-live.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1788280838936589 https://mahifx.slack.com/archives/C08AQKRU953/p1791971029551609

### compass-26-4 — Compass 26.4 upgrade and dashboard deploys
status: watching · since: 2026-10-08 · last: 2026-10-09
State: 26.3 to 26.4 staged Friday 9 Oct, live at the weekend restart; the RC (approved 9 Oct, then re-cut for an arb hedger startup fix) restores PSM overlays but Rostro has opted out (null on both keys), so no pricing change from it. A classifier bug on tags containing "/" is tracked as ZD-23407.
Refs: https://mahifx.slack.com/archives/C08ALS66EDC/p1791483337578909 https://mahifx.slack.com/archives/C08AQKRU953/p1791543772435149

### xau-bad-print — 11 Sep Jane Street XAUUSD bad print (CPI) and missing price guard
status: watching · since: 2026-09-11 · last: 2026-09-15
State: At the 12:30 UTC CPI release the XAUUSD reference panel collapsed to Jane Street alone while its bid went erratic, so published variants on this book hit a $319.84 spread at 12:30:03 for about 2s. No filter engaged: the outlier filters only run on a crossed book, and the sanity check was off since go-live at Rostro's request. Riz pulled Jane Street/HRP from the XAU reference selectors that day; XAUUSD sanity check enabled on all models 15 Sep.
Next: Kate to pull order IDs and decide whether to adjust bad-tick fills; MahiMain defect candidates (SignalPricingNode pass-through, crossed-only consensus filter, low-source floor) not seen raised.
Refs: https://mahifx.slack.com/archives/C08ALS66EDC/p1789131695104789 https://mahifx.slack.com/archives/C08ALS66EDC/p1789373254421619 https://mahifx.slack.com/archives/C08AQKRU953/p1789463134083049

### centroid-b2c-prices — B2C Centroid connection showed no GBPNZD prices
status: closed · since: 2026-10-28 · last: 2026-10-28 · closed: 2026-11-02
State: GBPNZD missing on B2C Centroid; Mahi streams were live, Abdullah traced it to an MT5 filter on Scope's side.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1793187010016709 https://mahifx.slack.com/archives/C08AQKRU953/p1793189507174379

### c-book-clearance — C book risk clearance speed (15 Oct gold)
status: closed · since: 2026-10-15 · last: 2026-10-15 · closed: 2026-11-11
State: 30M C book exposure took about 5 min to clear on 15 Oct (IC cancels, fill-ratio adjustment zeroing IC, VAR-CLEARANCE paused). Kate turned the fill-ratio adjustment off on the C House and SI hedgers and set forceShortenExecutionOnSurplus; no activity since, assumed resolved.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1792078136400489 https://mahifx.slack.com/archives/C08ALS66EDC/p1792081751691529

### pulse-athena-access — Rostro cannot read Pulse/Athena from new IP
status: closed · since: 2026-08-27 · last: 2026-09-09 · closed: 2026-11-05
State: no activity since 2026-09-09; Mahi has no Pulse/Athena whitelisting; assumed resolved.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1787822793611979 https://mahifx.slack.com/archives/C08AQKRU953/p1788950130321199

### brokered-lr-review — Brokered last-look yield decline
status: closed · since: 2026-08-25 · last: 2026-09-01 · closed: 2026-11-02
State: no activity since 2026-09-01; assumed resolved or superseded (PSM live on INV 13-14 Oct).
Refs: https://mahifx.slack.com/archives/C08ALS66EDC/p1787649194353099 https://mahifx.slack.com/archives/C08ALS66EDC/p1787740328562409 https://mahifx.slack.com/archives/C08ALS66EDC/p1788280858317659

### oil-incident-rca — July oil reference-feed incident RCA
status: closed · since: 2026-08-17 · last: 2026-09-01 · closed: 2026-11-02
State: no activity since 2026-09-01; assumed resolved (RCA sent Aug; see Arc).
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
- 2026-10-20 — Rostro accepts new commercials with a $150K repayment settlement over 15 months; contract being drafted
