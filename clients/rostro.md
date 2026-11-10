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
last_catchup: 2026-11-10T08:18:25Z
status: active
---

## Now
Relationship under strain: on 14 Oct a CMC futures price freeze cost the SI book about 178k and Andrew Morgan called it "relationship losing level"; evidence went to Rostro, CMC gave no rebate, and on 16 Oct Andrew accepted five pricing-integrity outcomes onto the roadmap (incident still open, no owners or dates yet). The C book client also complained of slippage on 16 Oct, traced to an LR mismatch. Commercials: after David Cooney and Michael Ayres met, Rostro accepted the new commercials with Mahi fees discounted by a $150K repayment settlement over 15 months, and is likely to take a crypto licence and wants weekend gold (Andrew, 20 Oct); the contract is being drafted. Rostro keeps adding IC sub-account books (rev-share), PSM went live on the INV model 14 Oct, and Rostro is switching Jump off futures (hedgers updated 15 Oct).  Sub 11 went live 2 Nov (XAUUSD, XAGUSD, G7 FX and futures via Mahi; Rostro keeps indices direct to IC), and Scope's VIP end client is on a final trial week with skew switched off on USDJPY/EURUSD (30 Oct).

## Streams

### ic-sub-books — IC sub-account rev-share books (SUB 5/9/10/11, C House, Sub SI House)
status: open · since: 2026-08-24 · last: 2026-11-09
State: Rostro flow from specific counterparty tags is split into separate Compass books, each with its own hybridHedgerSub* hedging to a dedicated IC_SUBS_* market via Scope's PXM Mahi_3 connection (one shared MAHI_IC_SUBS price stream; Mahi sends tag 1 = MAHI_IC_SUBS_n per book). Tag 251_* (large Cyprus retail broker, soft flow) has FX, CFD and futures books plus a "Sub SI House" book; its rev share was signed 13 Oct. IC_SUBS_12 was set up 19-20 Oct and sub 8 (MAHI_IC_SUBS_8, XAU book) was funded 30 Oct. 22 Oct IC market data dropped (net 20oz unhedged until Scope refreshed the connection; hedger worked as designed). Sub 11 went live 2 Nov with a changed scope: Rostro goes direct to IC for indices, and XAUUSD, XAGUSD, G7 FX and the futures (DAX, NDX, SPX, DOW, XAU) go via Mahi; for tags 251_0 and 79_30 (FA model, XAUUSD on VIP Vol, always internalised) risk is split to the FX/futures off book or the SI book and hedged to IC_SUBS_11. 3-4 Nov: sub 11 hedging misbehaved (XAG, USDJPY, DAX futures); Kate fixed a missing risk splitting rule, moved sub 11 back to the SI book at Oliver's request, and set an interim execution rule internalising the XAG tags caught by an SI book brokering rule (risk goes to the normal IC feed, Rostro flat). Abdullah asked Mahi to stop hedging an account rejecting "account not found" (HRP_Saxo, MAHI_2); Kate removed it from the hedger pending Scope's EOD restart. 6 Nov: one futures trade was caught by the SI book broker rule and went to CMC; Kate added a higher-priority internalise futures rule and Oliver moved risk off CMC. Oliver asked for sub 11 in the 15 min SI cycle; Kate set it up for FX and metals and is looking into futures. 9 Nov: Oliver said he would send 50% of sub 11 trades to Mahi that day, asked whether Mahi accepts under 1oz (Kate: yes, minimum configured at 0.01oz), then at 13:28 reported silver futures still going to CMC for sub 11; Kate said Mahi does not price silver futures for Rostro, and Oliver replied it was on his side.
Next: Kate to finish the 15 min SI cycle for sub 11 futures; Kate to fix the risk splitting config so sub 11 XAG tags hedge to IC_SUBS_11 rather than the normal IC feed (replace the interim internalise-all rule); re-add the removed HRP_Saxo account to the hedger after Scope's EOD restart; sub 8 book test trades and go-live; confirm MAHI_IC_SUBS_12 funded and retested; internal question on how multi-region (NY4) is charged; send the Sub SI House holding-period page to Rostro.
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

### cmc-futs-dropouts — CMC as sole futures LP: recurring dropouts and rejects
status: open · since: 2026-08-26 · last: 2026-11-09
State: CMC is the only LP in the pool pricing gold futures (and XAUFUT, indices), so each dropout (25 Aug, 5 Oct) leaves no price or fill. On 9 Sep DAXFUT-U showed flat CMC prices re-sent every 4-10s; Kate promised a CMC-normalisation backtest; the 14 Oct freeze is the same failure mode at scale. On 5 Oct Kate said broker-first only helps if Jump joins the XAUFUT reference price, then the pool (caveat: Jump reprices ahead of CMC in fast markets); Rostro has not decided, Riz is "not optimistic on CMC". On 14 Oct CMC filled 800 of a 1,000-lot XAUFUT-Z sweep then expired 200 and all retries despite showing size; Scope will raise it with CMC. On 15 Oct Rostro moved most futures volume away from Jump and expected to switch them off, so Kate removed Jump from the futures hedgers' config and bounced them; Alex then saw NQ hedges still going to a backup LP, which was a wrong PXM mapping on the new NDXFUT-Z contract (no NDXFUT flow reached Mahi since the roll; DOW, DAX and SPX futures were fine). On 29 Oct CMC stopped quoting NDXUSD for 15s (20:01:00-20:01:15 UTC), so CLIENT_PRICE_INV_LDN and CONTINUITY_POOL_LDN went indicative and an A_CLIENTS NDX/USD sell was rejected LIQUIDITY_VIOLATION; Nathan Burch explained it to Rahul in thread. 9 Nov call (Oliver): Rostro will start routing NDXFUT, SPXFUT and DOWFUT to IC_MARKETS instead of CMC, but wants the option to broker to CMC; Kate will add futures to LIQUIDITY_POOL_IC_LDN and leave CMC as the futures market in LIQUIDITY_POOL_LDN, with the switch on 10 Nov after EOD restarts.
Next: Kate to add futures to LIQUIDITY_POOL_IC_LDN and switch NDXFUT/SPXFUT/DOWFUT routing to IC after 10 Nov EOD restarts; Rostro decision on adding Jump to XAUFUT reference price and pool (Jump is being switched off on Rostro's side, so check this still stands); Alex to fix the NDXFUT-Z mapping in PXM; Kate's CMC-normalisation backtest.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1787733565831759 https://mahifx.slack.com/archives/C08AQKRU953/p1791970984817549 https://mahifx.slack.com/archives/C08AQKRU953/p1793319660284079 https://mahifx.slack.com/archives/C08ALS66EDC/p1794225217062859

### pxm-order-handling — PXM order splitting, boost, latency and tick throttle
status: open · since: 2026-09-30 · last: 2026-10-30
State: PXM splits large FA/VIP orders into tier-sized clips so fills land near TOB not VWAP (30 Sep, 6 Oct). PXM's reply (13 Oct): boost off suits limit orders (it sweeps) but market orders then sweep too and Mahi cannot tell to fill tiers two and three; Liam says LR is the only in-product fix and would add slippage, ruled out by the no-slippage agreement, and calls all-TOB clipping "machine gunning". Kate proposes Alex ask PXM for pass-through or per-order-type boost. Client latency was traced to a 1-per-10ms tick throttle in Mahi's VIP distribution and in PXM: Mahi moved VIP to 2 per 10ms (6-7 Oct), Rostro raised PXM to 1 per ms, over 99% of VIP ticks now go out; Alex (8 Oct) said client latency fell 22ms to 16ms vs peer and asked for 4 per 10ms, Kate (12 Oct) doubts it helps and wants a fresh tick sample. Rostro is moving the Mahi quote throttle for four feeds from 10ms to 5ms; FA pricer BMSL window went 10ms to 50ms on 1 Oct. On 30 Oct Alexandre said the VIP end client still sees 12ms tick latency; Scope's PXM sampling interval is 5 and he wants 3 and Mahi ticks per 10ms at 7. Kate wanted a fresh dataset first (every tick was being published after the last change); Alexandre has no dataset, so he will lower the PXM sample interval and Mahi will check next week whether every tick is published.
Next: PXM/Alex on pass-through or per-order-type boost; Kate to review tick publishing next week after the PXM sampling change (no dataset from the end client); Kate to check protective throttling on Mahi side before Rostro changes the PXM throttle.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1790776376391349 https://mahifx.slack.com/archives/C08ALS66EDC/p1791298744478709 https://mahifx.slack.com/archives/C08ALS66EDC/p1791883456395629 https://mahifx.slack.com/archives/C08AQKRU953/p1793361779461789

### vip-trial-skew — VIP end-client final trial: skew off on USDJPY/EURUSD
status: open · since: 2026-10-30 · last: 2026-10-30
State: Alexandre said the end client behind tag ending 100029 (most of VIP flow on USDJPY/EURUSD) is on its last trial week with Scope and will switch Scope off if unhappy, and asked for skew to be disabled. Skew is per price stream, not per tag, so Kate turned skew off on USDJPY and EURUSD on the VIP feed for the trial (price-based signals still apply to others), to be reviewed afterwards; the alternative is skew on with this tag's trades excluded from the signals, as its own trades drive most of the skew it sees. Alexandre called the skew PnL small. Tick latency side is in pxm-order-handling.
Next: Kate to review skew after the trial and decide between skew on with the tag excluded from signals or staying off.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1793361779461789 https://mahifx.slack.com/archives/C08AQKRU953/p1793372430907599

### commercials-reneg — Commercial renegotiation, value-add and relationship
status: open · since: 2026-08-19 · last: 2026-11-03
State: Rostro asked to renegotiate; Sam Steele challenged whether STP flow should count toward fees but said he wants to send all flow (Andrew, 1 Sep). A new-commercials draft went to Rostro 14 Sep and was initially declined (15 Sep). After David, Michael Ayres and Andrew spoke the week of 13 Oct, Rostro accepts the new commercials, with Mahi fees discounted by a $150K repayment settlement over 15 months (effectively a locked contract); they will probably take a crypto licence and are interested in weekend gold. Susan asked 20 Oct for this to be written into a contract, so Bonnie asked for details to go to Nicole Vivian to draft. Sam Steele wants two separate sessions, on the crypto tool and the equities portfolio tool; Andrew thinks single stocks are the bulk of Rostro's business, so Mahi may need to close a gap there, and the crypto meeting is to be locked first (offered for next Tuesday, 27 Oct). On 15 Oct David Cooney asked for a month-by-month value-add report for the last 3 months plus monthly volumes since they started; Kate delivered it the same day and noted Rostro is deliberately keeping some spreads tight to win flow back, so tailored models are being built. On 26 Oct Andrew noted nothing from Sam Steele in reply and Bonnie asked if Andrew has another day this week for the session, saying she will nudge it along. On 28 Oct Andrew said the Sam Steele meeting is booked for the 13th (month not stated, presumably Nov) and the team should prepare for it. Alex (Rostro) asked about kilo gold; Kate said Mahi can do it, and Andrew said given the discounting Mahi should charge where possible. 3 Nov call notes (Kate): Rostro is happy to set up global LR, initially conservative with a $5/M max; they are considering pricing into Integral to win flow, but Kate's early read (-$60/M on inception or worse, stays offside) is poor and she asked for a dataset. Bonnie shared news that Rostro's group got a crypto registration in the BVI.
Next: Rostro to send Integral flow dataset; set up global LR (max $5/M) when ready; send settlement details to Nicole Vivian for the contract draft; prepare for the Sam Steele meeting on the 13th (crypto tool, then the equities tool session); consider charging for kilo gold if Rostro proceeds.
Refs: https://mahifx.slack.com/archives/C08ALS66EDC/p1787135711511859 https://mahifx.slack.com/archives/C08ALS66EDC/p1789481310304399 https://mahifx.slack.com/archives/C08ALS66EDC/p1792485246173679 https://mahifx.slack.com/archives/C08ALS66EDC/p1793703042394719

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
State: On 23 Oct Scope (Rahul) queried a sub-account's EURUSD sell 72096515-1 (200k filled 1.11996 vs 500k quoted at 1.11999) and reported 57 of 86 orders with negative slippage ($106.53); Kate replied that every negatively slipped order was brokered to IC because automated classification briefly flagged the account, cleared 08:50 UTC, and internally filled orders all got the shown price; Rahul acknowledged. On 22 Oct a 100k USDJPY Limit IOC to IC sat 3 min before cancel (IC connection reset), breaching hybridHedgerOffBook1's order-breach limit and shutting it down; no open risk. Recurring ScopeMarkets fill queries, mostly LP-side behaviour on brokered flow or model behaviour. Earlier: NQ.U26 gap was the anti-spoof node; XAUUSD Invast slippage was Invast's fill. 
Next: Rostro to say whether to change the LP, internalise, or relax the anti-spoof node; no reply seen.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1787835257505189 https://mahifx.slack.com/archives/C08AQKRU953/p1792665379140899 https://mahifx.slack.com/archives/C08AQKRU953/p1792781435455779 https://mahifx.slack.com/archives/C08AQKRU953/p1792782045722059

### cmc-spx-freeze — 14 Oct CMC SPX/NDX freeze, RCA and evidence pack
status: open · since: 2026-10-14 · last: 2026-10-20
State: CMC's SPX price (futures and cash) froze 12:18:36-12:34:15 UTC while IC and Jump fell about 38 points after the 12:30 print; CMC filled no SPX futures hedges until 12:34. Loss about 178k (SPX fut -145k, SPX cash -23k, NDX cash -10k), roughly 114k client trades at the frozen price (251* sold about $31.5M into it). Root cause per Athena: from 12:22:53 each CMC SPX message came about 10ms after one of Mahi's own hedge orders with a bid-size dip, so it counted as a changed book and reset the stuck filter's 10 min clock, reproduced in Will's Echo replays. Amana had no stale fills, so Rostro is the only client that dealt at the frozen price. Evidence went to Rostro 14 Oct; PXM FIX logs were not recorded. 16 Oct refinement: CMC stayed connected, and its displayed-size changes in response to Mahi's unfilled hedge attempts reset the stuck-filter timer; upstream failure plus a Mahi protection gap. Andrew told David the clients were remarked to the Jump rate (applied amendments and remaining loss still to be confirmed), and accepted five outcomes onto roadmap 7.2-PI-1 to 5: quantity-only updates must not hide frozen prices, divergence alert vs a normalised independent reference (first), quote pull at a higher replay-validated threshold, hedge availability and repeated cancels alongside pricing health, and reconciling the Jump repricing and loss with any CMC recovery recorded separately. 20 Oct: Riz confirmed CMC gave no rebate, and its whole incident report was that internal configuration was published with errors causing pricing to halt, which at least confirms CMC as the cause.
Next: name accountable delivery owners, work items and replay plans for 7.2-PI-1 to 5; Rostro to confirm the Jump repricing and remaining loss; Mahi to get PXM to explain; Andrew to probe how Rostro handles CMC.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1791981542846109 https://mahifx.slack.com/archives/C08ALS66EDC/p1792137303134229 https://mahifx.slack.com/archives/C08ALS66EDC/p1792139709277749 https://mahifx.slack.com/archives/C08ALS66EDC/p1792490159068509

### c-book-lr-price — C book slippage: LR applied at fill but not in quoted price
status: open · since: 2026-10-16 · last: 2026-10-16
State: Alexandre said the C book client complained of slippage on 15 Oct gold (filled 4151.71 vs quote 4151.52/4151.64, no market move). Isaac found the cause: on the multi-channel SCOPE_X_FA session, XAUUSD orders from 122_0_* and 117_27* execute on C_CLIENTS and take its liquidity reduction, but the streamed price is built from SCOPE_X_FA and carries only that channel's LR. Fix offered: a suffixed XAUUSD.c instrument streaming the C_CLIENTS price, with extra bridge routing on Rostro's side. Isaac disabled LR on C_CLIENTS meanwhile (Alexandre agreed, will review). Riz asked for an alternative without a new instrument; Isaac said only a global per-process LR (with per-channel caps) can span channels, not LR grouped over selected channels.
Next: Rostro (Alexandre/Riz) to decide between XAUUSD.c routing and global LR; LR stays off on C_CLIENTS until then.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1792138607035239 https://mahifx.slack.com/archives/C08AQKRU953/p1792140741428669 https://mahifx.slack.com/archives/C08AQKRU953/p1792141257894219

### c-book-clearance — C book risk clearance speed (15 Oct gold)
status: open · since: 2026-10-15 · last: 2026-10-15
State: A 30M exposure on the C book (Rostro's new C House client) took about 5 min to clear on 15 Oct: IC cancelled some hedge trades and the default fill-ratio liquidity adjustment zeroed IC for 30s, then the VAR-CLEARANCE rule spent about half the remaining time paused. Kate turned the fill-ratio adjustment off on hybridHedgerCHouse1 and hybridHedgerSI1 (single LP, nowhere to steer) and set forceShortenExecutionOnSurplus on VAR-CLEARANCE, bounced the hedger, and told Alex IC left about half the orders unfilled.
Next: Kate to watch clearance performance; Alex has not replied.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1792078136400489 https://mahifx.slack.com/archives/C08ALS66EDC/p1792081751691529

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

### pulse-athena-access — Rostro cannot read Pulse/Athena from new IP
status: closed · since: 2026-08-27 · last: 2026-09-09 · closed: 2026-11-05
State: no activity since 2026-09-09; Mahi has no Pulse/Athena whitelisting; assumed resolved.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1787822793611979 https://mahifx.slack.com/archives/C08AQKRU953/p1788950130321199

### centroid-b2c-prices — B2C Centroid connection showed no GBPNZD prices
status: closed · since: 2026-10-28 · last: 2026-10-28 · closed: 2026-11-02
State: GBPNZD missing on B2C Centroid; Mahi streams were live, Abdullah traced it to an MT5 filter on Scope's side.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1793187010016709 https://mahifx.slack.com/archives/C08AQKRU953/p1793189507174379

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
