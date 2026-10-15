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
  - {name: "Rahul Sanap", role: "ScopeMarkets ops: slippage/fill/latency queries on client orders", confidence: low}
  - {name: "Andreas Christofi", role: "ScopeMarkets ops: FIX sessions, subscriptions, new books", confidence: low}
  - {name: "Abdullah Almasharfa", role: "ScopeMarkets ops: PXM connections, IC feeds, session config", confidence: low}
  - {name: "Chrysovalantis Karageorgiou", role: "ScopeMarkets ops: PXM connector/account setup (CK)", confidence: low}
  - {name: "Rakan Awwad", role: "ScopeMarkets ops: FIX rejection queries", confidence: low}
  - {name: "Manuel de Cara", role: "Rostro: Pulse/Athena data access", confidence: low}
  - {name: "Sam Steele", role: "Group Chief Strategy Officer at Rostro; commercial counterpart (described internally as basically co-founder)"}
  - {name: "Michael Ayres", role: "senior Rostro contact meeting David Cooney 15-16 Oct; was named as replacement after Lochlan left", confidence: low}
last_catchup: 2026-10-15T13:04:16Z
status: active
---

## Now
Relationship under strain: on 14 Oct a CMC futures price freeze cost the SI book about 178k and Andrew Morgan called it "relationship losing level"; evidence pack went to Rostro, David Cooney meets Michael Ayres this week (Thursday per 14 Oct note, "tomorrow" per Bonnie on 15 Oct). Commercials are being renegotiated at Rostro's request and the 2026-09-14 draft got "a no from the board". Rostro keeps adding IC sub-account books (rev-share), PSM went live on the INV model 14 Oct, and the 26.4 Compass upgrade landed the weekend of 10-11 Oct.

## Streams

### ic-sub-books — IC sub-account rev-share books (SUB 5/9/10/11, C House, Sub SI House)
status: open · since: 2026-08-24 · last: 2026-10-15
State: Rostro flow from specific counterparty tags is split into separate Compass books, each with its own hybridHedgerSub* hedging to a dedicated IC_SUBS_* market (SUB1/2 live 7 Oct on tags 76_0*/117_70* and 84_0*/117_75*, C House live 30 Sep, SUB 11 test trades 14-15 Oct; routing via MultiChannelConfig or risk splitting for multi-model tags). On 9 Oct Rostro said tag 251_* (large Cyprus retail broker, soft flow) will be warehoused 50% in PXM and 50% sent to Compass, with separate FX, CFD and futures books and a "Sub SI House" book; Kate's sim says transfer every 15 min ($328k vs $280k at 5m). The client signed the rev share 13 Oct; SUB 11 tests showed ~500ms on half of trades on 14 Oct, ~70ms on 15 Oct, and Oliver said "looks good". They are also considering a NY4 server.
Next: Kate to confirm SUB 11 go-live; internal question on how multi-region (NY4) is charged; send the Sub SI House holding-period page to Rostro.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1787569899244609 https://mahifx.slack.com/archives/C08ALS66EDC/p1791540027260459 https://mahifx.slack.com/archives/C08AQKRU953/p1792054971300949

### commercials-reneg — Commercial renegotiation, value-add and relationship
status: open · since: 2026-08-19 · last: 2026-10-15
State: Rostro asked to renegotiate; Sam Steele challenged whether STP flow should count toward fees and tried for discounts by flow type (Andrew Morgan, 1 Sep), while saying he wants to send all flow and discussing fees above 100bn. Options on the table were $0.45/M, or $0.40/M with a 24-month term. Joint PR and a party were in flight in late Aug and a joint press release topic was TBD. A new-commercials draft had the wrong entity and a marginal fee schedule (14 Sep); on 15 Sep Andrew replied "It's a no from the board" to whether Rostro signed; later outcome not seen. On 15 Oct David Cooney asked for a month-by-month value-add report for the last 3 months plus monthly volumes since they started.
Next: Kate or analytics to produce the value-add and monthly volumes report for David; David meets Michael Ayres this week.
Refs: https://mahifx.slack.com/archives/C08ALS66EDC/p1787135711511859 https://mahifx.slack.com/archives/C08ALS66EDC/p1789402809750969 https://mahifx.slack.com/archives/C08ALS66EDC/p1792035521266049

### cmc-spx-freeze — 14 Oct CMC SPX/NDX freeze, RCA and evidence pack
status: open · since: 2026-10-14 · last: 2026-10-14
State: CMC's SPX price (futures and cash) froze 12:18:36-12:34:15 UTC while IC and Jump fell about 38 points after the 12:30 print; CMC kept changing quoted size on each hedge order so the 10-minute stuck-price filter never fired, and filled no SPX futures hedges until 12:34. Loss on affected instruments is about 178k (SPX fut -145k, SPX cash -23k, NDX cash -10k), roughly 114k of it client trades at the frozen price. Kate sent Rostro a summary PDF and two spreadsheets (repriced vs Jump, CMC quote updates); Rostro is chasing CMC and PXM FIX logs were not recorded. Internally Liam says the size changes make the quotes look real and PrimeXM must explain; open issues are rebate vs direct loss with CMC, engineering fixes (ignored quote-condition tags, stalePriceFeed alerts off for futures, alert on primary vs secondary divergence), and Amana also affected.
Next: Mahi to get PXM to explain; Liam asked Rostro for PXM FIX logs; Andrew to probe discreetly how Rostro handles CMC; Will's pricing backtest; briefing for David before the Michael Ayres meeting.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1791981542846109 https://mahifx.slack.com/archives/C08ALS66EDC/p1791992168810219 https://mahifx.slack.com/archives/C08AQKRU953/p1791993119452699

### cmc-futs-dropouts — CMC as sole futures LP: recurring dropouts and rejects
status: open · since: 2026-08-26 · last: 2026-10-14
State: CMC is the only LP in the pool pricing gold futures (and prices XAUFUT, indices), so each CMC dropout (23 single-tick XAUFUT-Z withdrawals on 25 Aug, DAXFUT-U gaps on 9 Sep, NDXFUT-U unfilled on 18 Sep, 11 of 233 rejects on tag 148 on 5 Oct) leaves no price or no fill. Kate offered adding Jump to the pool and the reference price (caveat: Jump reprices ahead of CMC in fast markets); Rostro has not decided and Riz is "not optimistic on CMC". On 14 Oct CMC filled 800 of a 1,000-lot XAUFUT-Z sweep then expired the remaining 200 and all retries despite showing size; Rostro said they would raise it with CMC.
Next: Rostro decision on adding Jump to XAUFUT reference price and pool.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1787733565831759 https://mahifx.slack.com/archives/C08AQKRU953/p1791202740464639 https://mahifx.slack.com/archives/C08AQKRU953/p1791970984817549

### pxm-connections — PrimeXM connections, LP list and feeds
status: open · since: 2026-09-04 · last: 2026-10-14
State: Rostro and Mahi cleaned up the PXM taker connections (LPs removed 7 Sep) and added feeds (MAHI_HRP_MFP, MAHI_STP, HRP_UBS_DIRECT, IC_MARKETS_2, IC_SUBS_*). Kate pushed for a third connection (MAHI_3, done 30 Sep) because MAHI_2 is close to MAHI in throughput. On 14 Oct, Mahi found the VIP price session in PXM never requests XAGUSD, so Alex sees the INV book on VIP silver.
Next: Alexandre to add XAG/USD to the VIP price session in PXM.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1788508022729149 https://mahifx.slack.com/archives/C08AQKRU953/p1790608061088529 https://mahifx.slack.com/archives/C08AQKRU953/p1791995219776019

### pxm-order-handling — PXM order splitting, boost, latency and tick throttle
status: open · since: 2026-09-30 · last: 2026-10-13
State: PXM splits large FA/VIP orders into tier-sized clips so fills land near TOB (30 Sep, 6 Oct); Kate's reading is that boost should be on with limit price passed through, which contradicts earlier guidance, and was checking other PXM clients. Client-reported latency was traced to a 1-per-10ms tick throttle both in Mahi's VIP distribution and in PXM: Mahi moved the VIP channel to 2 per 10ms on 7 Oct, Rostro raised PXM to 1 per ms, and about 99% of ticks now go out; Rostro found a PXM throttle of 1 tick per 10ms per market they can change, and is changing the Mahi quote throttle for INVAST, EDGEWATER and IC_MARKETS from 10ms to 5ms (needs a bounce, EOD restarts). FA pricer BMSL window was changed 10ms to 50ms on 1 Oct.
Next: Kate awaiting post-change market data from Rostro; Kate to check protective throttling on Mahi side before Rostro changes the PXM throttle.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1790776376391349 https://mahifx.slack.com/archives/C08ALS66EDC/p1791298744478709 https://mahifx.slack.com/archives/C08ALS66EDC/p1791884626485049

### fill-queries — Client execution, slippage and rejection queries
status: open · since: 2026-08-27 · last: 2026-10-13
State: Recurring queries from ScopeMarkets ops about fills: NQ.U26 118-point gap (27 Aug), XAUUSD Invast slippage on brokered tag (27 Aug), fill validity during sharp move (28 Sep), 3-leg XAUUSD slippage (2 Oct), slow fills on 12 Oct (13 Oct; delay was LP last look: Edgewater_2 146ms, HRP_MFP 200ms then INVAST 11ms). Pattern is usually LP-side behaviour on brokered flow rather than Mahi pricing.
Next: Rory King owns the 28 Sep validity query; no reply seen.
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
State: 26.3 to 26.4 staged Friday 9 Oct, live at the weekend restart; infra main moved to LDN before 26.4 staging. Dashboard-only deploys continued through August and September, plus a classifier bug on tags containing "/" tracked as ZD-23407.
Refs: https://mahifx.slack.com/archives/C08ALS66EDC/p1791483337578909 https://mahifx.slack.com/archives/C08AQKRU953/p1791543772435149

### position-breaks — Position breaks and position recs
status: watching · since: 2026-09-04 · last: 2026-10-02
State: Oliver flagged 622k of EUR SI net unhedged (4 Sep); Mahi did a weekend position rec and Rostro pulls positions from Pulse to check; breaks booked manually on 8 Sep (151 XAUUSD) and 2 Oct (G30EUR, SPX, DOW, NDX), and a 200oz break on 17 Sep.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1788504725919689 https://mahifx.slack.com/archives/C08ALS66EDC/p1790942297984149

### news-hedging — News-event hedging, single-LP risk (NFP 4 Sep)
status: watching · since: 2026-09-04 · last: 2026-09-17
State: On 4 Sep NFP wiped about $90k of SI P&L because both hedgers hedge only to IC Markets (rev-share) and hit cancels/rejects; RCA written. Outcome: high-weight news rules on SI and off-book hedgers (16 Sep, 1 min before and after, multiple LPs for metals and G7), slippage tolerance first 150 pips, then reduced and execution markets reverted to IC-only on 17 Sep at Rostro's request. MWMS news widening proposed for XAUUSD (INV, VIP, VIP_VOL).
Next: Rostro said they want to hold off on a news rule for the off-book hedger and to trial a deviation over PPI; no decision on MWMS news widening seen.
Refs: https://mahifx.slack.com/archives/C08AQKRU953/p1788526116336149 https://mahifx.slack.com/archives/C08ALS66EDC/p1788530463357869 https://mahifx.slack.com/archives/C08ALS66EDC/p1789657801727309

### brokered-lr-review — Brokered last-look yield decline
status: watching · since: 2026-08-25 · last: 2026-09-01
State: Brokered LR fell to $1.47/M on $4.6B in August vs $7.60-8.88/M last Nov-Dec; coverage dropped 30.9% to 5.4% (Dec to Feb), partly due to median brokered ticket falling $118k to about $6k. Standing agreements: no price-moving fill-time mechanisms, config changes discussed with Rostro. Kate to draft a message to ramp LR up; Andrew prefers a PSM-style widening approach.
Next: Kate's message to Rostro on ramping LR.
Refs: https://mahifx.slack.com/archives/C08ALS66EDC/p1787649194353099 https://mahifx.slack.com/archives/C08ALS66EDC/p1788280858317659

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

## Arc
- 2025 — Rostro live on Compass (per Kate, 2026-09-14, sanity check disabled before go-live)
- 2026-05 — Lochlan, key contact championing Mahi, left Rostro for OZ; Saul Knapp left for MAS Markets
- 2026-07-14 — oil reference-feed incident (~$350k client loss) raised by Rostro; Mahi offers no goodwill
- 2026-07-30 — Sam Steele intro meeting; asks for documented safeguards, not reimbursement
- 2026-08-25 — commercial renegotiation and joint PR started at Rostro's request
- 2026-09-15 — draft new commercials "a no from the board"
- 2026-10-14 — PSM live on INV; CMC SPX freeze costs ~178k, treated as relationship-level risk
