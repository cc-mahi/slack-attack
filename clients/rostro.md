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
last_catchup: 2026-10-20T07:16:51Z
status: active
---

## Now
Relationship under strain: on 14 Oct a CMC futures price freeze cost the SI book about 178k and Andrew Morgan called it "relationship losing level"; evidence went to Rostro, David Cooney was to meet Michael Ayres 16 Oct (outcome not seen), and on 16 Oct Andrew accepted five pricing-integrity outcomes onto the roadmap (incident still open, no owners or dates yet). The C book client also complained of slippage on 16 Oct, traced to an LR mismatch. Commercials were renegotiated at Rostro's request but Rostro did not sign the 2026-09-14 draft ("a no from the board", 15 Sep); no later outcome seen. Rostro keeps adding IC sub-account books (rev-share), PSM went live on the INV model 14 Oct, the 26.4 Compass upgrade landed the weekend of 10-11 Oct, and Rostro is switching Jump off futures (hedgers updated 15 Oct). A value-add and volumes pack went to David 15 Oct.

## Streams

### ic-sub-books — IC sub-account rev-share books (SUB 5/9/10/11, C House, Sub SI House)
status: open · since: 2026-08-24 · last: 2026-10-19
State: Rostro flow from specific counterparty tags is split into separate Compass books, each with its own hybridHedgerSub* hedging to a dedicated IC_SUBS_* market (SUB1/2 live 7 Oct on tags 76_0*/117_70* and 84_0*/117_75*, C House live 30 Sep, SUB 11 test trades 14-15 Oct; routing via MultiChannelConfig or risk splitting for multi-model tags). Scope's CK settled the PXM wiring on 5 Oct: Mahi_3 carries one shared MAHI_IC_SUBS price stream and Mahi sends tag 1 = MAHI_IC_SUBS_9 or _10 per book when hedging. The IC price in PXM carried a markup (min 7 vs 5 cents); Oliver will change the profile. Tag 251_* (large Cyprus retail broker, soft flow) gets separate FX, CFD and futures books and a "Sub SI House" book; on 9 Oct Rostro said 50% would be warehoused in PXM and 50% sent to Compass; Kate's sim says transfer every 15 min ($328k vs $280k at 5m). Oliver said 8 Oct warehousing 50% is hard because of drop copy on their side, and by 13 Oct all 251* flow was to be risk-split into the new books (FX, futures, indices to IC_SUBS_11), so the 50/50 plan may be dropped (8 Oct reply thread not read). Rostro's end client (251*) signed its rev share 13 Oct; SUB 11 tests showed ~500ms on half of trades on 14 Oct, ~70ms on 15 Oct, and Oliver said "looks good". Rostro is considering a NY4 server. On 19 Oct ScopeMarkets created a new execution account MAHI_IC_SUBS_12 (tags 114_0, 117_153) on the third connection (Mahi_3) and asked Mahi for a matching account and a new book routed by client identifier; Oliver said the client will trade on FA.
Next: Mahi to create the MAHI_IC_SUBS_12 account and book (Kate asked, Rakan confirmed Mahi_3); Kate to confirm SUB 11 go-live; internal question on how multi-region (NY4) is charged; send the Sub SI House holding-period page to Rostro.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1787569899244609 https://mahifx.slack.com/archives/C08ALS66EDC/p1791540027260459 https://mahifx.slack.com/archives/C08AQKRU953/p1792054971300949 https://mahifx.slack.com/archives/C08AQKRU953/p1792415070077209

### c-book-lr-price — C book slippage: LR applied at fill but not in quoted price
status: open · since: 2026-10-16 · last: 2026-10-16
State: Alexandre said the C book client complained of slippage on 15 Oct gold (order 71563075 filled 4151.71 vs PXM quote 4151.52/4151.64 with no market move). Isaac found the cause: on the multi-channel SCOPE_X_FA session, XAUUSD orders from 122_0_* and 117_27* execute on C_CLIENTS and take its liquidity reduction, but the streamed price is built from SCOPE_X_FA and carries only that channel's LR. Fix offered: a suffixed XAUUSD.c instrument streaming the C_CLIENTS price, with extra bridge routing on Rostro's side. Isaac disabled LR on C_CLIENTS meanwhile (Alexandre agreed, will review). Riz asked for an alternative without a new instrument; Isaac said only a global per-process LR (with per-channel caps) can span channels, not LR grouped over selected channels.
Next: Rostro (Alexandre/Riz) to decide between XAUUSD.c routing and global LR; LR stays off on C_CLIENTS until then.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1792138607035239 https://mahifx.slack.com/archives/C08AQKRU953/p1792140741428669 https://mahifx.slack.com/archives/C08AQKRU953/p1792141257894219

### c-book-clearance — C book risk clearance speed (15 Oct gold)
status: open · since: 2026-10-15 · last: 2026-10-15
State: A 30M exposure on the C book (Rostro's new C House client) took about 5 min to clear on 15 Oct: IC cancelled some hedge trades and the default fill-ratio liquidity adjustment zeroed IC for 30s, then the VAR-CLEARANCE rule spent about half the remaining time paused. Kate turned the fill-ratio adjustment off on hybridHedgerCHouse1 and hybridHedgerSI1 (single LP, nowhere to steer) and set forceShortenExecutionOnSurplus on VAR-CLEARANCE, bounced the hedger, and told Alex IC left about half the orders unfilled.
Next: Kate to watch clearance performance; Alex has not replied.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1792078136400489 https://mahifx.slack.com/archives/C08ALS66EDC/p1792081751691529

### commercials-reneg — Commercial renegotiation, value-add and relationship
status: open · since: 2026-08-19 · last: 2026-10-15
State: Rostro asked to renegotiate; Sam Steele challenged whether STP flow should count toward fees but said he wants to send all flow (Andrew, 1 Sep). Options were $0.45/M, or $0.40/M with a 24-month term. A joint PR and party were in flight in late Aug (topic TBD). A new-commercials draft had the wrong entity (incorporation wording BVI vs Antigua & Barbuda) and a marginal fee schedule; the corrected version went to Rostro for signature 14 Sep. Rostro did not sign: asked "Did Rostro sign the new commercials?", Andrew answered 15 Sep "It's a no from the board". No later outcome seen. On 15 Oct David Cooney asked for a month-by-month value-add report for the last 3 months plus monthly volumes since they started; Kate delivered it the same day in thread (skew and LR $/M by month with verify links, monthly volumes since Jul 2025, book P&L, a Rostro Value Add microsite) and noted Rostro is deliberately keeping some spreads tight to win flow back, so tailored models are being built with them. On the SI book Rostro whitelists chosen tags into the off book to take risk; Kate says execution quality can stay good with the classifier routing.
Next: David meets Michael Ayres 16 Oct; Rostro's current position on terms is unknown.
Refs: https://mahifx.slack.com/archives/C08ALS66EDC/p1787135711511859 https://mahifx.slack.com/archives/C08ALS66EDC/p1789481310304399 https://mahifx.slack.com/archives/C08ALS66EDC/p1792035521266049 https://mahifx.slack.com/archives/C08ALS66EDC/p1792078095470549

### cmc-futs-dropouts — CMC as sole futures LP: recurring dropouts and rejects
status: open · since: 2026-08-26 · last: 2026-10-15
State: CMC is the only LP in the pool pricing gold futures (and XAUFUT, indices), so each dropout (23 single-tick XAUFUT-Z withdrawals on 25 Aug, 11 of 233 rejects on tag 148 on 5 Oct) leaves no price or fill. On 9 Sep DAXFUT-U showed flat CMC prices with quotes re-sent every 4-10s, which PXM and Scope could not see as gaps; Kate attributed it to CMC and promised a CMC-normalisation backtest (none seen); the 14 Oct freeze is the same failure mode at scale. The 18 Sep NDXFUT-U non-fill was contract expiry, not a dropout (Kate flattened the position in Compass at Alex's request). On 5 Oct Kate said broker-first only helps if Jump joins the XAUFUT reference price, then the pool (caveat: Jump reprices ahead of CMC in fast markets); Rostro has not decided, Riz is "not optimistic on CMC". On 14 Oct CMC filled 800 of a 1,000-lot XAUFUT-Z sweep then expired 200 and all retries despite showing size; Scope will raise it with CMC. On 15 Oct Rostro moved most futures volume away from Jump and expected to switch them off, so Kate removed Jump from the futures hedgers' config and bounced them; Alex then saw NQ hedges still going to a backup LP, which was a wrong PXM mapping on the new NDXFUT-Z contract (no NDXFUT flow reached Mahi since the roll; DOW, DAX and SPX futures were fine).
Next: Rostro decision on adding Jump to XAUFUT reference price and pool (Jump is being switched off on Rostro's side, so check this still stands); Alex to fix the NDXFUT-Z mapping in PXM; Kate's CMC-normalisation backtest.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1787733565831759 https://mahifx.slack.com/archives/C08AQKRU953/p1791970984817549 https://mahifx.slack.com/archives/C08AQKRU953/p1792078098426429 https://mahifx.slack.com/archives/C08AQKRU953/p1792080246319599

### cmc-spx-freeze — 14 Oct CMC SPX/NDX freeze, RCA and evidence pack
status: open · since: 2026-10-14 · last: 2026-10-16
State: CMC's SPX price (futures and cash) froze 12:18:36-12:34:15 UTC while IC and Jump fell about 38 points after the 12:30 print; CMC filled no SPX futures hedges until 12:34. Loss about 178k (SPX fut -145k, SPX cash -23k, NDX cash -10k), roughly 114k client trades at the frozen price (251* sold about $31.5M into it). Root cause per Athena: from 12:22:53 each CMC SPX message came about 10ms after one of Mahi's own hedge orders with a bid-size dip, so it counted as a changed book and reset the stuck filter's 10 min clock (it would have pulled CMC at 12:28:36); Will's Echo replays reproduce it, with CMC the only SPX source. Amana had no stale fills, so Rostro is the only client that dealt at the frozen price. Kate sent Rostro the evidence 14 Oct; PXM FIX logs were not recorded (PXM says CMC prices looked normal) and Rostro will ask CMC. Mahi ignores quote-condition tags on CMC mass quotes (PXM's spec does not use them, per Liam). Candidate fixes: price-level stuck clock, divergence alert/firewall vs the normalised reference index, sanity-check benchmark other than PrimaryMarket. Rebate vs direct loss with CMC is open (Andrew). 16 Oct refinement: CMC stayed connected and heartbeating, and its displayed-size changes in response to Mahi's unfilled hedge attempts reset the stuck-filter timer (heartbeats alone did not); CMC was the only source for the affected rules, so this is an upstream failure plus a Mahi protection gap. Andrew told David the clients were remarked to the Jump rate (applied amendments and remaining loss still to be confirmed), and accepted five outcomes onto roadmap 7.2-PI-1 to 5: quantity-only updates must not hide frozen prices, divergence alert vs a normalised independent reference (first), quote pull at a higher replay-validated threshold, hedge availability and repeated cancels alongside pricing health, and reconciling the Jump repricing and loss with any CMC recovery recorded separately. Acceptance does not mean fixes are live.
Next: name accountable delivery owners, work items and replay plans for 7.2-PI-1 to 5; Rostro to confirm the Jump repricing and remaining loss; Mahi to get PXM to explain; Andrew to probe how Rostro handles CMC.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1791981542846109 https://mahifx.slack.com/archives/C08ALS66EDC/p1791986751396079 https://mahifx.slack.com/archives/C08ALS66EDC/p1792137303134229 https://mahifx.slack.com/archives/C08ALS66EDC/p1792139709277749

### pxm-connections — PrimeXM connections, LP list and feeds
status: open · since: 2026-09-04 · last: 2026-10-16
State: Rostro and Mahi cleaned up the PXM taker connections (LPs removed 7 Sep) and added feeds (MAHI_HRP_MFP, MAHI_STP, HRP_UBS_DIRECT, IC_MARKETS_2, IC_SUBS_*). Kate pushed for a third connection (MAHI_3, done 30 Sep) because MAHI_2 is close to MAHI in throughput (Scope first asked for a ticket; Oliver backed a third connection); MAHI_3 carries the IC_SUBS stream. On 14 Oct, Mahi found the VIP price session in PXM never requests XAGUSD, so Alex sees the INV book on VIP silver. On 16 Oct Kate confirmed to Abdullah that no DST change is needed on Scope's side (distribution and market data/order FIX connections run on NY time, instrument hours on local market time), and Liam noted networking issues that day with Rostro's environment mostly unaffected after Alexandre saw S3 config channel errors.
Next: Alexandre to add XAG/USD to the VIP price session in PXM.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1788508022729149 https://mahifx.slack.com/archives/C08AQKRU953/p1790608061088529 https://mahifx.slack.com/archives/C08AQKRU953/p1792160152347079

### pxm-order-handling — PXM order splitting, boost, latency and tick throttle
status: open · since: 2026-09-30 · last: 2026-10-13
State: PXM splits large FA/VIP orders into tier-sized clips so fills land near TOB not VWAP (30 Sep, 6 Oct). PXM's reply (13 Oct): boost off suits limit orders (it sweeps) but market orders then sweep too and Mahi cannot tell to fill tiers two and three; Liam says LR is the only in-product fix and would add slippage, ruled out by the no-slippage agreement, and calls all-TOB clipping "machine gunning". Kate proposes Alex ask PXM for pass-through or per-order-type boost. Client latency was traced to a 1-per-10ms tick throttle in Mahi's VIP distribution and in PXM: Mahi moved VIP to 2 per 10ms (6-7 Oct), Rostro raised PXM to 1 per ms, over 99% of VIP ticks now go out; Alex (8 Oct) said client latency fell 22ms to 16ms vs peer and asked for 4 per 10ms, Kate (12 Oct) doubts it helps and wants a fresh tick sample. Rostro is changing the Mahi quote throttle for INVAST, INVAST_2, EDGEWATER and IC_MARKETS from 10ms to 5ms (EOD restarts). FA pricer BMSL window changed 10ms to 50ms on 1 Oct.
Next: PXM/Alex on pass-through or per-order-type boost; Kate awaiting a fresh tick sample from Rostro; Kate to check protective throttling on Mahi side before Rostro changes the PXM throttle.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1790776376391349 https://mahifx.slack.com/archives/C08ALS66EDC/p1791298744478709 https://mahifx.slack.com/archives/C08ALS66EDC/p1791883456395629 https://mahifx.slack.com/archives/C08ALS66EDC/p1791884626485049

### fill-queries — Client execution, slippage and rejection queries
status: open · since: 2026-08-27 · last: 2026-10-13
State: Recurring ScopeMarkets fill queries, mostly LP-side behaviour on brokered flow or model behaviour. NQ.U26 118-point gap (27 Aug) was the anti-spoof node holding the bid low after the daily close; Sam Hewitt offered to disable it or speed up tightening, Scope said it would review. XAUUSD Invast slippage (27 Aug) was Invast's fill; Cameron Hughes offered to change the brokered LP or internalise the tag and Rahul asked Oliver to choose. The 28 Sep validity query was answered the same day by Rory (valid executable price). On 27 Sep an order stuck 3 min at the LP with no response and shut hybridHedgerNonRevShare1 as a precaution; Scope will raise it with the LP. Also 3-leg XAUUSD slippage (2 Oct) and slow fills 12 Oct (13 Oct; LP last look: Edgewater_2 146ms, HRP_MFP 200ms then INVAST 11ms).
Next: Rostro to say whether to change the LP, internalise, or relax the anti-spoof node; no reply seen.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1787835257505189 https://mahifx.slack.com/archives/C08AQKRU953/p1790583002096399 https://mahifx.slack.com/archives/C08AQKRU953/p1791898254846899

### exec-rule-requests — Execution rule and routing requests (brokered vs internalised)
status: open · since: 2026-08-18 · last: 2026-09-30
State: Rostro keeps asking for per-tag rule changes (internalise XAGUSD from 122_*, toxic tags to Edgewater pool then moved to LIQUIDITY_POOL_LDN, blacklist 163_0_88068 from brokering, broker tags 148_0_n/a_44641/45753 on gold and index futures). Kate suggested force-internalising the two arb non rev share broker rules (about $170M executed in 28 days, yields $58/M at 5s and $130/M at 30s); Rostro's answer not seen. Mahi cannot set percentage splits on hedge flow (25 Aug).
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1787068816321309 https://mahifx.slack.com/archives/C08AQKRU953/p1790789855177739

### psm-inv-rollout — Predictive spread modulation on the INV model
status: watching · since: 2026-09-01 · last: 2026-10-14
State: Kate proposed PSM on CLIENT_PRICE_INV_LDN on 1 Sep (average spread no wider than today). A Beta model ran for about a month; volume-weighted it was +$0.83/M round trip wider than INV. Rostro agreed and PSM went live 13-14 Oct. XAUUSD sanity check was also enabled on all models on 15 Sep after the off-market Jane Street tick.
Next: watch volumes, distributed spreads and trade spread distribution after go-live.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1788280838936589 https://mahifx.slack.com/archives/C08AQKRU953/p1791971029551609

### compass-26-4 — Compass 26.4 upgrade and dashboard deploys
status: watching · since: 2026-10-08 · last: 2026-10-09
State: 26.3 to 26.4 staged Friday 9 Oct, live at the weekend restart; the RC (approved 9 Oct, then re-cut for an arb hedger startup fix) restores PSM overlays but Rostro has opted out (null on both keys), so no pricing change from it; infra main moved to LDN before 26.4 staging. Dashboard-only deploys continued through August and September, plus a classifier bug on tags containing "/" tracked as ZD-23407.
Refs: https://mahifx.slack.com/archives/C08ALS66EDC/p1791483337578909 https://mahifx.slack.com/archives/C08AQKRU953/p1791543772435149

### position-breaks — Position breaks and position recs
status: watching · since: 2026-09-04 · last: 2026-10-02
State: Oliver flagged 622k of EUR SI net unhedged (4 Sep); Mahi did a weekend position rec and Rostro pulls positions from Pulse to check; breaks booked manually on 8 Sep (151 XAUUSD) and 2 Oct (G30EUR, SPX, DOW, NDX), and a 200oz break on 17 Sep.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1788504725919689 https://mahifx.slack.com/archives/C08ALS66EDC/p1790942297984149

### xau-bad-print — 11 Sep Jane Street XAUUSD bad print (CPI) and missing price guard
status: watching · since: 2026-09-11 · last: 2026-09-15
State: At the 12:30 UTC CPI release the XAUUSD reference panel collapsed to Jane Street alone (EDGEWATER withdrew, others silent) while its bid went erratic, so all published variants on this book (not MAHI_2) hit a $319.84 spread at 12:30:03 for about 2s. No filter engaged: the uncrossing/outlier filters only run on a crossed book and SignalPricingNode passes a too-wide source through unchanged; the sanity check was off since go-live at Rostro's request and its benchmark shares the panel. Riz pulled Jane Street/HRP from the XAU reference selectors that day; XAUUSD sanity check enabled on all models 15 Sep. Fills on the bad tick were to be checked against the no-slippage agreement; no outcome seen.
Next: Kate to pull order IDs and decide whether to adjust bad-tick fills; MahiMain defect candidates (SignalPricingNode pass-through, crossed-only consensus filter, low-source floor) not seen raised.
Refs: https://mahifx.slack.com/archives/C08ALS66EDC/p1789131695104789 https://mahifx.slack.com/archives/C08ALS66EDC/p1789373254421619 https://mahifx.slack.com/archives/C08AQKRU953/p1789463134083049

### brokered-lr-review — Brokered last-look yield decline
status: watching · since: 2026-08-25 · last: 2026-09-01
State: Brokered LR fell to $1.47/M on $4.6B in August vs $7.60-8.88/M last Nov-Dec; coverage dropped 30.9% to 5.4% (Dec to Feb), partly due to median brokered ticket falling $118k to about $6k. Standing agreements: no price-moving fill-time mechanisms, config changes discussed with Rostro (Andrew wants these codified as categories Mahi may change freely within guard rails such as average spread no wider). Config explains only the 26 Jun leg (~$0.85/M); counterparty-layer LR, the bigger lever, needs a config field not yet built; PSM widening cannot be scoped to the brokered leg. Kate agreed to draft a message to Rostro on ramping LR up and agreeing parameters; the PSM request went out 1 Sep (psm-inv-rollout) but the LR message has not been seen. Alex (1 Oct) said LR looked unset for the new C-book client on FA gold.
Next: Kate's message to Rostro on ramping LR.
Refs: https://mahifx.slack.com/archives/C08ALS66EDC/p1787649194353099 https://mahifx.slack.com/archives/C08ALS66EDC/p1787740328562409 https://mahifx.slack.com/archives/C08ALS66EDC/p1788280858317659

### oil-incident-rca — July oil reference-feed incident RCA
status: watching · since: 2026-08-17 · last: 2026-09-01
State: ~$350k client-side loss from an oil reference source change applied beyond intended scope; Mahi's stated position is no goodwill. RCA was prepared 17-24 Aug as a separate email from commercials; Sam Steele "wasn't super happy with our accountability" on it but did not press (1 Sep). Delivery confirmation not seen in channel. The 14 Oct CMC freeze is being treated against this precedent.
Refs: https://mahifx.slack.com/archives/C08ALS66EDC/p1786988498348909 https://mahifx.slack.com/archives/C08ALS66EDC/p1788273338625779

### pulse-athena-access — Rostro cannot read Pulse/Athena from new IP
status: watching · since: 2026-08-27 · last: 2026-09-09
State: Manuel de Cara could not retrieve metrics from Pulse from a given IP; Isaac said it is not a whitelisting issue, Liam said there is no whitelisting for Pulse/Athena and asked for error details. No reply with details seen since 9 Sep; downgraded as stale.
Next: Rostro to send specifics.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1787822793611979 https://mahifx.slack.com/archives/C08AQKRU953/p1788950130321199

### vip-book-shape — VIP order-book tier merging (EURUSD/USDJPY/XAGUSD)
status: closed · since: 2026-08-17 · last: 2026-08-21 · closed: 2026-10-15
State: Tiers merged around the roll when BMSL and wide-spread suppression caps collapsed layers; Mahi changed BMSL multipliers and VWAP spreads (19-20 Aug). Alex reported it still happening 21 Aug; no activity since; assumed resolved.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1787136862033619 https://mahifx.slack.com/archives/C08AQKRU953/p1787309561700819

### news-hedging — News-event hedging, single-LP risk (NFP 4 Sep)
status: closed · since: 2026-09-04 · last: 2026-09-17 · closed: 2026-10-15
State: 4 Sep NFP wiped about $90k of SI P&L because both hedgers hedge only to IC Markets (rev-share) and hit cancels/rejects. After calls on 8 and 16 Sep, high-weight news rules were set on both SI and off-book hedgers (1 min before/after, 150 pips slippage, multiple LPs for metals and G7, PPI max-slippage trial from $1); on 17 Sep, at Rostro's request, execution markets reverted to IC-only and slippage was reduced. Riz approved MWMS news widening for XAUUSD (INV, VIP, VIP_VOL) on 9 Sep and Kate set it up. No open items seen.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1788526116336149 https://mahifx.slack.com/archives/C08AQKRU953/p1788946405404699 https://mahifx.slack.com/archives/C08ALS66EDC/p1789657801727309

## Arc
- 2025 — Rostro live on Compass (per Kate, 2026-09-14, sanity check disabled before go-live)
- 2026-05 — Lochlan, key contact championing Mahi, left Rostro for OZ; Saul Knapp left for MAS Markets
- 2026-07-14 — oil reference-feed incident (~$350k client loss) raised by Rostro; Mahi offers no goodwill
- 2026-07-30 — Sam Steele intro meeting; asks for documented safeguards, not reimbursement
- 2026-08-25 — commercial renegotiation and joint PR started at Rostro's request
- 2026-09-15 — Rostro did not sign the new commercials draft ("a no from the board")
- 2026-10-14 — PSM live on INV; CMC SPX freeze costs ~178k, treated as relationship-level risk
- 2026-10-16 — Andrew accepts five pricing-integrity outcomes from the CMC freeze RCA onto the roadmap
