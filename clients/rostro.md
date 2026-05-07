---
slug: rostro
refs:
  vibepulse: ../VibePulse/.claude/clients/rostro.yaml
  billing: ../MahiProduct/data/billing/clients.json     # entry: rostro
  hosts: ../MahiProduct/data/client-hosts.json          # entry: rostro (also: easton for contracting entity)
  wiki: null                                             # ../MahiProduct/wiki/clients/rostro.md (not yet)
channels_override: null
key_people_overrides:
  - {name: "Alexandre Goudergues", role: "trading ops (alexandre.goudergues@scopemarkets.com)"}
  - {name: "Will", role: "scheduling contact", confidence: low}
  - {name: "Oliver Ryan", role: "trading ops — classification/routing, hedger setup"}
  - {name: "Abdullah Almasharfa", role: "ops — PXM/LP connections, subscriptions", confidence: low}
  - {name: "Manglai", role: "FIX/technical ops — XCore config, dropcopy, LP subscriptions"}
  - {name: "Riz Dusoye", role: "trading ops — spreads, Pulse, VIP feed (rizwaan.dusoye@rostro.com)"}
  - {name: "Louiza Ignatiou", role: "ops — FIX sessions, IP whitelisting"}
  - {name: "Daniel Lawrance", role: "CEO (linkedin.com/in/daniel-lawrance-/); B2B bridge discussions", confidence: low}
  - {name: "Sammy", role: "primary client-side relationship manager / decision-maker", confidence: low}
  - {name: "Lochlan", role: "departed — was championing Mahi at Rostro; moved to OZ (OneZero?); Dave Cooney to reach Mike Ayres as replacement contact", confidence: low}
  - {name: "Manu", role: "Rostro-side — SI PnL allocation; sending questions on Pulse parameters", confidence: low}
last_catchup: 2026-05-07T07:39:22Z
---

## Recent issues

> [open] 2026-05-06 — NAS100 XCore order 61437785: brokering rejected 3× by CMC
> Abdullah queried rejection on XCore order 61437785 (SUBID3 2895, NAS100, ordered 14:12:09 UTC 2026-05-06). Kate confirmed three rejects from CMC when trying to broker the trade. No resolution or further Rostro response in window. [permalink](https://mahifx.slack.com/archives/C08AQKRU953/p1778078860807189) [Kate confirms CMC rejects](https://mahifx.slack.com/archives/C08AQKRU953/p1778079332175879)

> [open] 2026-05-06 — New LP proposal: route SI VIP hedging with no aggregation; Kate flagged risks
> Alex (Rostro) emailed Kate proposing to go live with a new LP offering tighter spreads in Gold and FX majors, initially routing SI VIP soft flow with no aggregation (full lifecycle to the LP), then phasing in more SI hedging flow later. Kate flagged internally: single-LP risk (no fallback if they widen/reject, citing Kama as precedent), book restructure required (VIP flow to separate book to ensure fully hedged), and reduced SI offsetting (more hedge volume = more spread paid). No Mahi response to Alex yet in window. [permalink](https://mahifx.slack.com/archives/C08ALS66EDC/p1778060197092949) [Kate's risks](https://mahifx.slack.com/archives/C08ALS66EDC/p1778060619854249)

> [open] 2026-05-06 — riskreportingmetrics in Pulse stale since 2026-05-05 18:29 UTC
> Riz flagged that riskreportingmetrics has not updated since 2026-05-05 18:29:58. Daria acknowledged and said "we'll have a look". No resolution confirmed yet. Separate from the 2025-09-17 missing-instruments entry (that was about specific new instruments not appearing; this is a full metrics refresh stall). [permalink](https://mahifx.slack.com/archives/C08AQKRU953/p1778050841008309) [Daria ack](https://mahifx.slack.com/archives/C08AQKRU953/p1778051309275809)

> [open] 2026-05-05 — Key contact Lochlan departed to OZ (OneZero?)
> Will flagged Lochlan has moved to OZ. Andrew asked who remains as a good point of contact given Lochlan was championing Mahi at Rostro, and whether the departure was acrimonious (potential first attempted customer for Lochlan at OZ). Mahi currently only has Oli (ex-Exinity, LDN-based) as a strong contact. Dave Cooney to try to reach Mike Ayres (described as "the main boss") to rebuild the senior relationship. [permalink](https://mahifx.slack.com/archives/C08ALS66EDC/p1777970074025209) [Andrew's question](https://mahifx.slack.com/archives/C08ALS66EDC/p1777971293751749)

> [open] 2025-10-03 — NAS100/SPX/DOW/CL1 futures pricing spikes at open
> Oli reported urgent SPX pricing spikes on 2025-10-03 (second consecutive day). Kate changed harmonics signals for DOW and SPX; pricing improved but CL1 still spiky later that day. Louiza submitted full futures min/step/max size spreadsheet; Kate applied changes pending weekend restarts. Rostro asked to give advance notice before rolling new instruments. Kate also noted DAXFUT-Z subscription failing via PXM with "invalid symbol" — symbol mapping in progress. [permalink](https://mahifx.slack.com/archives/C08AQKRU953/p1759483209208009) [futures sizes](https://mahifx.slack.com/archives/C08AQKRU953/p1759483009859979)

> [open] 2025-09-26 — VIP XAUUSD slippage: client seeing retail price, filled on VIP model
> Alex flagged 10ct slippage on Scope-X-VIP XAUUSD (sample orders 44752358, 44752372). Kate's internal note: clients see retail price in MT5, trade gets sent down VIP connection, executed on VIP model — perceived as slippage. Kate reverted signals from synapse-insti back to harmonics-insti + IFMS-INSTI; kicked off backtests. Andrew flagged that if clients are being shown one model and filled on another, this will build mistrust. Rostro working with TS to fix the MT5 routing issue on their side. [permalink](https://mahifx.slack.com/archives/C08AQKRU953/p1758888142404869) [internal](https://mahifx.slack.com/archives/C08ALS66EDC/p1759139558735169)

> [open] 2025-09-17 — FI/LR P&L missing in Pulse for newly-added instruments
> Sammy flagged on 2025-09-12 that live instruments added recently are not appearing in Pulse for FI P&L in riskreportingmetrics (visible in Compass but not Pulse). Bonnie checked; Pulse access confirmed but data gap persists. Still outstanding as of 2025-09-18 with Sammy chasing. [permalink](https://mahifx.slack.com/archives/C08AQKRU953/p1757665068899269)

> [open] 2025-09-04 — Jump direct connection conformance testing stalled
> Kate stopped fixMarketData2 and fixOrders2 on 2025-08-05 whilst awaiting Jump conformance. As of 2025-09-08 Mahi had messaged Jump twice with no reply; Kate asked Sammy to nudge Jump on the "MahiMarkets <> Jump FX - UAT" email thread. Jump feed currently consumed via PXM as JUMP_2. Futures FIX session (Scope-X-Fut) credentials sent 2025-08-07; conformance still in progress. [permalink](https://mahifx.slack.com/archives/C08AQKRU953/p1757325715665229) [internal](https://mahifx.slack.com/archives/C08ALS66EDC/p1754388667282279)

> [open] 2025-07-21 — Compass failover: Sammy blocking on XCore failover plan
> Sammy struggling to configure automatic failover from A-booking to Mahi to B-booking in PXM if Compass goes down. Proposed B-booking all via PXM with skewed Compass price — Mahi pushing back. Alternatives discussed: One Zero bridge failover, London COE as failover source. As of 2025-07-16 Kate reported Sammy "back on board with One Zero failover" and testing internally. Plan was to have failover agreed before go-live. [permalink](https://mahifx.slack.com/archives/C08ALS66EDC/p1752590947240169) [update](https://mahifx.slack.com/archives/C08ALS66EDC/p1752670637687949)

> [resolved] 2025-07-21 — XAUUSD retail go-live: counterparty tag (tag 1) missing
> Sammy announced going live with retail XAUUSD flow on 2025-07-21. Kate immediately asked Sammy to revert — FIX messages from Scope-X-Retail-Orders were missing tag 1 (trading account remap). Isaac and Kate worked through the mapping (tag 1=ROSTRO, tag 448 for cpty). Manglai fixed and sent a test trade EOD 2025-07-18 (pre-announcement). As of 2025-07-24 Kate confirmed receiving counterparty tags correctly. [permalink](https://mahifx.slack.com/archives/C08AQKRU953/p1753085649110309) [resolved](https://mahifx.slack.com/archives/C08AQKRU953/p1753343821482759)

> [resolved] 2025-06-13 — Test trades: JUMP_2 field validation error; ROSTROOrders channel possibly redundant
> Test trades on 2025-06-13: client orders via Scope-X-Retail-Orders hitting correct book; external orders filled at EDGEWATER, EDGEWATER_2, INVAST. JUMP_2 (XAUUSD only) hit a field validation error in the UI. Amir following up internally. ROSTROOrders (B_CLIENTS channel) — Rostro don't have config for it, possibly redundant. Resolved by 2025-06-16: Justin longed and shorted 1oz at JUMP_2 successfully. [permalink](https://mahifx.slack.com/archives/C08ALS66EDC/p1749824834932309) [resolved](https://mahifx.slack.com/archives/C08ALS66EDC/p1750074876417109)

> [resolved] 2025-05-20 — Dropcopy FIX session setup (Manglai)
> Manglai provided dropcopy FIX config and worked through IP whitelisting across multiple rounds: Beeks whitelist via Maten, additional IPs 69.6.29.122/32 and 46.28.177.153/32 added. Multiple dropcopy config versions exchanged. As of 2025-05-22 further connectivity issues (nc timeout) resolved; dropcopy established in time for test trades. [permalink](https://mahifx.slack.com/archives/C08AQKRU953/p1747812582784569) [connectivity resolved](https://mahifx.slack.com/archives/C08AQKRU953/p1747930393940489)

> [resolved] 2026-05-04 — Edgewater 4-second fill on XCore order 61206552
> Client (Abdullah, cc Oli) queried a ~4-second fill time on XCore order 61206552 (SUBID3 5d87b54a). Cameron Hughes investigated: flow was STP-classified (signal-follow) and routed externally; Edgewater returned `expired` (DONE_CANCELLED) on the first two hedge attempts after ~2.0s each, with the third attempt filling at 16:25:31.226 UTC (~24ms). Client received fill at 4639.7. Client confirmed understanding and closed. No config change; pattern consistent with prior Edgewater last-look behaviour (see 2026-04-22 Invast latency entry for parallel). [permalink](https://mahifx.slack.com/archives/C08AQKRU953/p1777889706290469) [Cameron Hughes timeline](https://mahifx.slack.com/archives/C08AQKRU953/p1777898412438959)

> [resolved] 2026-05-04 — DAX40 Scope-X-SI-Prices: no pricing received
> Louiza (Rostro) flagged DAX40 not receiving prices on the SI feed. Isaac confirmed checking as of market open, then posted a live G30EUR FIX snapshot from Scope-X-SI-Prices at 08:32 UTC confirming Mahi is publishing quotes. Client asked "So from your side you are sending prices?" — Isaac confirmed "Yes". Client acknowledged. [permalink](https://mahifx.slack.com/archives/C08AQKRU953/p1777879262200339) [Isaac confirms](https://mahifx.slack.com/archives/C08AQKRU953/p1777879927998989)

> [open] 2026-04-30 — USDJPY cpty 95_0_652431 arb-classification slippage complaint
> Alex flagged consistent slippage on USDJPY from cpty 95_0_652431. Kate confirmed: classifier tagged them as arb after 29 sells / $15.05M in ~6 min 10:27–10:33, aggregated 4-min yield -$17k → trades brokered. Kate proposed internalising to SI book for fast-hedge instead; client acknowledged short-term markout vol. No config change confirmed yet. [permalink](https://mahifx.slack.com/archives/C08AQKRU953/p1777562968245279) [Kate's analysis](https://mahifx.slack.com/archives/C08AQKRU953/p1777567089259889)

> [open] 2026-04-30 — G30EUR client_price_vip_ldn TOB ~1.35 vs configured 0.6
> Alex flagged the VIP-LDN G30EUR spread is ~1.35 against 0.6 config. Kate confirmed signals look responsible and was deploying a change at 12:09 BST. Awaiting confirmation post-fix. [permalink](https://mahifx.slack.com/archives/C08AQKRU953/p1777547078939949)

> [resolved] 2026-04-29 — Centroid-Retail-Orders FIX: XAGUSD/XAUUSD min-quantity rejection
> Chrysovalantis hit `FIELD_VALIDATION_ERROR {DISTRIBUTION_LDN-maximumShowQuantity=TOO_SMALL, DISTRIBUTION_LDN-quantity=TOO_SMALL}` on XAGUSD via session 49=MahiFX-Orders / 56=Centroid-Retail-Orders (Mahi config 50 from prior request). Asked for connection-specific min 0.5 XAGUSD / 0.01 XAUUSD. Kate making the config change; needs EOD restart to pick up. Centroid-Retail connection rebuilt with new FIX creds in Sep 2025 (see Sep entry); min sizes confirmed 0.01oz XAUUSD / 1k FX. [permalink](https://mahifx.slack.com/archives/C08AQKRU953/p1777466777885749)

> [open] 2026-04-29 — China FIX session removal: please disconnect Scope-X-China-2
> Kate (Mahi) requested Rostro disconnect the Scope-X-China-2 Orders/Prices sessions ahead of removing the unused China FIX config; Scope-X-China-1 already idle 7d, China-2 still showing live heartbeats. Awaiting Rostro disconnect. [permalink](https://mahifx.slack.com/archives/C08AQKRU953/p1777465172441569)

> [resolved] 2026-04-27 — YM.M26 invalid-size alerts on MAHI_CMC — step size mismatch (Mahi 0.05)
> Andreas: receiving multiple alerts on YM.M26 on MAHI_CMC due to invalid size; their step is 0.05 and asked Mahi to adjust to match. Rory King made the hedger config changes to trade in 0.05 minimum increments for Dow futures, live same morning. [permalink](https://mahifx.slack.com/archives/C08AQKRU953/p1777283400358769)

> [resolved] 2026-04-29 — XAUUSD HRP_AGG_HEDGE risk-reducing-only mode + position alignment
> 04-28: Oli asked to flip HRP_AGG_HEDGE to risk-reducing only; Kate stripped the prior hedging rule, imported a -10,009oz position to align with Rostro's -9,334oz, hedger chipped flat through 04-29. 04-29 14:00 BST cycle: -6,918oz residual surfaced (HRP_AGG aggregate had still routed flow there before removal); Kate re-imported and the hedger cleared it again to flat. Returned to standard hedging rules at 17:30 BST with a tighter risk-reducing rule retained alongside, so position-reducing trades still take priority but at a tighter spread. Alex confirmed; will revisit if positions grow again (Centroid don't do giveups, so risk-reducing mode is their main lever). [permalink](https://mahifx.slack.com/archives/C08AQKRU953/p1777372407923539)

> [open] 2026-04-24 — UBS direct feed — connect into Mahi rather than PXM
> Owen: Rostro receiving a direct feed from UBS and want to connect directly into Mahi rather than via PXM; asked for the technical point of contact for UBS's tech team. Kate routed via support@mahifx.com. Awaiting UBS engagement. [permalink](https://mahifx.slack.com/archives/C08AQKRU953/p1777044459539369)

> [open] 2026-04-23 — XNGUSD retail-feed pricing still being finalised
> Abdullah tried subscribing XNGUSD/NGC1 and got `unknown symbol`; Kate confirmed the correct mapping is `NG1USD` but pricing is still being finalised — don't send flow yet. Jump sub-code `NTGASP` confirmed earlier. [permalink](https://mahifx.slack.com/archives/C08AQKRU953/p1776932072322889)

> [open] 2026-04-22 — G30EUR rejects (cpty 109_1_2656) via arb-classification exec rule
> Limit-order flow getting cancelled because arb classification routes to a neutral-rate + markup exec rule, and the continuity rate breached the limit price. Kate digging into the trades to confirm whether the arb tag is correct. [permalink](https://mahifx.slack.com/archives/C08AQKRU953/p1776871777184599)

> [resolved] 2026-04-17 — Missing pricing on new retail-feed API
> Alexandre reports gaps on the newly-created retail feed API. Rory King investigating; Chrysovalantis looped in for reference. Some symbols (USOIL→CL1USD) corrected; XNGUSD now tracked as separate `[open]`. Superseded by full onboarding through May–Sep 2025: Compass logins issued, FIX sessions (Retail, Insti, Futures, VIP, Centroid) all stood up, and XAUUSD retail went live 2025-07-21. [permalink](https://mahifx.slack.com/archives/C08AQKRU953/p1776422678609409)

> [resolved] 2026-04-23 — HRP_AGG_HEDGE re-added to XAUUSD off-book hedger
> Oli asked for HRP_AGG_HEDGE back in the hedging pool for XAUUSD off-book flow only (not brokered). Initially added more broadly; Isaac corrected the scope on 04-24. [permalink](https://mahifx.slack.com/archives/C08AQKRU953/p1776962468190769)

> [resolved] 2026-04-22 — Invast order-response latency (~2s ack, 3min cancel)
> Nathan flagged Invast taking ~2s to respond to order requests (risk exposure on fills unknown) and a separate 3-minute cancel response. Root cause: OZ-Hub maintenance 17:30–18:30 NY on Invast side — order sat as pending leg in xcore until TTL cancel. Kate asked Abdullah to flag scheduled LP maintenance windows in advance. [permalink](https://mahifx.slack.com/archives/C08AQKRU953/p1776741282590589)

> [resolved] 2026-04-22 — INV/SI routing sweep, overrides removed for 104*/146*
> Oli asked for a classification + execution rule sweep so everyone trades down INV except 104* and 146*. Kate confirmed SI/INV connection setup: arb/signal-follow/broker → brokered, fast-hedge → SI book, remainder → Off Book. [permalink](https://mahifx.slack.com/archives/C08AQKRU953/p1776865644758649)

> [resolved] 2026-04-20 — Cpty 104_7_129656_11_0 off-book PnL drop
> Kate caught -$101k aggregated yield over 4 minutes in the off book driven by 104_7_129656_11_0, classified as signal follow + broker. Removed the `104_7*` off-book whitelist and risk-split their flow to SI book; rule priorities adjusted. [permalink](https://mahifx.slack.com/archives/C08AQKRU953/p1776688746006519)

> [resolved] 2026-04-16 — G30 EUR RETAIL spread misconfig
> Alexandre saw TOB 70cfd@1.46 vs configured 20cfd@0.8 (NYC TZ) on primexm. Cameron Hughes: signal widening was making first+second layer spreads match and stack at distribution. Fixed with signal change + pricer bounce; Alexandre confirmed. [permalink](https://mahifx.slack.com/archives/C08AQKRU953/p1776363572685119)

> [resolved] 2026-04-13 — riskReportingExtended1 OOM cascade (PD Q35MSLWK24J7MJ)
> Signal aggregates (`*.Signals.*.SR.*.*.1.CumSumNoOpinion`) frozen in Graphite since 2026-04-11 07:40 UTC because MahiMain commit 066fb9437 broke snapshot publishing; `keepLastValue` across 4,348 series blew heap. Bumping 2→4→6 GB only delayed it. Resolved by rolling back the webstack change (`512a10b`). [permalink](https://mahifx.slack.com/archives/C8568C6HG/p1776073126336049)

## Notable topics

- 2026-05-06 — Saul Knapp (Rostro exec) hired as CRO at MAS Markets. Will flagged the article internally with "What is going on at Rostro". No discussion yet. Adds to the senior relationship risk alongside Lochlan's departure (see 2026-05-05 entry). [permalink](https://mahifx.slack.com/archives/C08ALS66EDC/p1778069286617949) [source](https://fxnewsgroup.com/forex-news/executives/mas-markets-hires-rostro-exec-saul-knapp-as-cro/)
- 2026-04-21 — Client call outcomes: (1) they want LR PnL backtesting under different parameter changes — Andrew notes the existing LR sim supports this and will draft a KB article; (2) exploring SI-PnL attribution per client — Kate to check the Exinity script Will C wrote; (3) want a "Big Boys" book with a lower VAR threshold to route large-clip clients and reduce exposure — achievable in next couple of days. [permalink](https://mahifx.slack.com/archives/C08ALS66EDC/p1776761460382099)
- 2026-04-21 — Will/Andrew internal discussion: Rostro LR tuning highlights the value of inverting the sim — "what params get me X $/M across client, with toxic top-5% at 50 $/M and everyone else ≤ 5 $/M" — vs forward parameter search. Declarative-rule direction flagged for future work. [permalink](https://mahifx.slack.com/archives/C08ALS66EDC/p1776764246169119)
- **Futures-based index pricing / custom basis** — Rostro asking about status; previously discussed with "Sammy". No clear owner on Mahi side; Andrew suggested discussing in person. [permalink](https://mahifx.slack.com/archives/C08ALS66EDC/p1776353177596759)
- **In-person client meeting** — Kate and Andrew scheduling via Will for next week or week after, LDN.
- 2025-06-18 — Cyprus in-person meeting. Andrew met Sammy + ops team + CEO Daniel Lawrance (linkedin.com/in/daniel-lawrance-/). Context framed around bridge eval: Rostro in early vendor selection for a B2B bridge, not planning to move until 2026. Andrew proposed bridge white-label deal (Rostro as bridge white-labeller, flow from ~5 broker clients). Daniel Lawrance very interested in client-stickiness angle. Actions: Sammy to write B2B bridge requirements doc; Mahi to propose commercials + pilot plan. [permalink](https://mahifx.slack.com/archives/C08ALS66EDC/p1750232392028879)
- 2025-08-11 — Sammy sent RFP heads-up to Andrew. Rostro sending RFPs to vendors in coming weeks for bridge selection. Mahi will be receiving one. [permalink](https://mahifx.slack.com/archives/C08ALS66EDC/p1754905124966239)
- 2025-05-27 — Andrew update: Rostro fairly early in bridge evaluation; not planning to move until 2026. Cyprus meeting framing: vendor selection assessment. Sammy has been asking OneZero if they can do SI out of the box for single stocks. [permalink](https://mahifx.slack.com/archives/C08ALS66EDC/p1748345316279539)
- 2025-06-10 — Internal discussion: Sammy wants another "MK-style" relationship (deep operator access). Will/Kate pushing back — they will manage signals and outcomes, not give full config access. Decision to hide `pricing.adjustmentSignalRegistry` keys from non-Mahi users. Weekly calls established on Tuesdays. [permalink](https://mahifx.slack.com/archives/C08ALS66EDC/p1749551514053999)
- 2025-06-25 — Kate flagged Jump gold futures SI integration (priced by and hedged to Jump); low priority, could take feed through PXM initially. Kate/Justin back and forth on prioritisation through July. [permalink](https://mahifx.slack.com/archives/C08ALS66EDC/p1750860061915179)
- 2025-09-12 — Sammy requested Centroid-Retail connection (separate pricing API for retail Centroid flow, same model/channel as Scope-X-Retail). New FIX creds issued. Min deal sizes: XAUUSD 0.01oz, FX 1k (base). [permalink](https://mahifx.slack.com/archives/C08AQKRU953/p1757660365030579) [creds](https://mahifx.slack.com/archives/C08AQKRU953/p1757684113491319)
- 2025-08-29 — Sammy exploring DPSM (Dynamic Predictive Spread Modulation), volatility widening, and zero-spread econ news widening. Will explained econ news base spread override config for 0-spread instruments. Sammy also asked about roll-period spread management (marketWidthMinimumSpreadParameters with timezone overrides). [permalink](https://mahifx.slack.com/archives/C08AQKRU953/p1756459549972139)
- 2025-10-06 — Liam working on solution to let Rostro query Mahi classifications from database. IPs needed: 161.12.67.66 and 10.101.10.9. [permalink](https://mahifx.slack.com/archives/C08AQKRU953/p1759745772797999)
