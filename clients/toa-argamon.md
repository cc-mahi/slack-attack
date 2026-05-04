---
slug: toa-argamon
refs:
  vibepulse: ../VibePulse/.claude/clients/toa-argamon.yaml
  billing: null
  hosts: ../MahiProduct/data/client-hosts.json          # entry: toa-argamon
  wiki: null
channels_override: null
key_people_overrides:
  - {name: "Tom McLean", role: "Argamon-side analyst — primary day-to-day contact in mahi-argamon-operations"}
  - {name: "Levi Ulman", role: "Argamon ops — give-up / rejection queries, Centroid migration lead"}
  - {name: "Joanna Theofanous", role: "Argamon-side ops — recurring contact in mahi-argamon-operations for alerts and client trade queries"}
  - {name: "Jonah Ink", role: "Argamon — escalation contact; involved in currency rec disputes and P&L attribution", confidence: low}
  - {name: "Alexander Karnadi", role: "Argamon — analytics / reconciliation; participates in position rec and currency rec calls", confidence: low}
  - {name: "Elan Bension", role: "Argamon — senior contact / decision-maker; calls on insti model, LP config, retail contract renegotiation"}
  - {name: "Alex", role: "Argamon analytics — assists on Wintermute rec and crypto JPY position work (likely Alexander Karnadi)", confidence: low}
last_catchup: 2026-05-04T07:09:21Z
---

## Status

- **Stage:** live (Argamon is a client of Toa; LDN/APN1/CHI single-box setups). Contract split underway: Mahi retains retail tenant; Toa takes B2B/Crypto/RI — insti contract signed to Toa 2025-07-09.
- **Integration:** NYC retail tenant primary. Centroid migration in flight (from OneZero) before Aug 2025. Reactive Markets production setup in progress. XTX-Algo live from 2025-07-08. Lucera for insti (replacing Centroid path). NY4→TKY dedicated WAN link established 2025-06-16 for Toa connectivity.
- **Relationship:** ops-heavy; multiple daily interactions across pricing, hedging, reconciliation, and new LP onboarding. Currency P&L rec dispute escalated to Elan/Jonah calls in late June–July 2025. Retail contract renegotiation pending (Elan wants tighter spreads; Mahi pushing for fixed-fee conversion first).

## Recent issues

> [open] 2025-07-14 — Reactive Markets slow-consumer / Beeks connectivity recurring
> Argamon raised Reactive connectivity issue with Beeks; hour-long phone call before Beeks escalated to L2, then fixed almost instantly on escalation. Same class of issue had been seen earlier (Reactive slow consumer persisting after Beeks cross-connect applied). Reactive production go-live is in progress (Arun handling; UAT test trades passed 2025-06-30; production test trades underway as of 2025-07-01). GTS Reactive markets added to hybridHedger1 non-LP-reducing rules 2025-07-14. [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1752458081221389)

> [open] 2025-07-09 — Retail contract conversion to fixed fee pending; Elan wants spread tightening
> Daria flagged that Elan wants to significantly tighten spreads, which would eat into retail P&L under current billing; pushing to get contract converted to fixed fee before moving reduced spreads to production. No resolution yet. [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1752015694887489)

> [open] 2025-07-08 — XTX-Algo live; HRP booking duplicate issue
> XTX-Algo (fixOrdersXtxAlgo) went live 2025-07-08 after successful test trades. Daria removed XTXM_RCTV_HRP_1 from hedgers on 2025-07-03 after XTX sent duplicate trade reports causing HRP booking issues. NY4→TKY dedicated WAN link established 2025-06-16 (latency now more consistent; cross-connect intermittently times out requiring manual failover to internet route). HRP party-block mappings require command-line restart. [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1751978544253569)

> [resolved] 2025-07-02 — Currency position reconciliation crisis (JPY/AUD breaks); ~$125k P&L dispute
> Argamon opened a formal rec thread 2025-06-23 flagging multi-week USDJPY and AUD currency breaks across client-vs-LP and internal-vs-external Compass positions. Multiple calls with Elan, Jonah, Alex, Isaac, Daria across 2025-06-24 to 2025-07-02: crypto JPY hedging (XBTJPY/ETHJPY) was implicated; AUD break partially attributed to large EURAUD traders whose P&L was included in Compass client positions but not Argamon platform positions; Argamon misread initial rec report causing unintended open risk from 2025-06-20 adjustment. Final position: currency adjustments applied; Argamon to regularly adjust Compass positions based on rec reports going forward; Toa migration expected to consolidate visibility. Elan asked whether ~$125k was a real loss attributable to retail or crypto — Mahi pushed back that attribution would need senior discussion. [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1751424351939279)

> [resolved] 2025-06-27 — Lucera conformance complete; insti maker session to be set up via Natwest
> Elan confirmed Lucera completed conformance 2025-06-27 and requested a maker session hedging via Natwest. Isaac setting up; Lucera credentials issued 2025-07-09 per Daria. Insti contract formally moved to Toa 2025-07-09 (signed). [permalink](https://mahifx.slack.com/archives/C06TW3D8NMV/p1751005957276989)

> [resolved] 2025-06-22 — Compass 25.2 upgrade; first attempt failed, rollback, successful 2025-06-22
> Compass 25.2 upgrade attempted weekend 2025-06-14/15: distribution processes failed to start (SBE metadata mismatch, missing `enableFileBasedMessagePersistence`); rolled back. Redeploy 2025-06-22 successful. Post-upgrade: Argamon requested full redeploy and failover to OZ for process restart. Aeron issue from 25.2 seen at Amana also cautioned against restarts without prior deploy. [permalink](https://mahifx.slack.com/archives/C06TW3D8NMV/p1749805003282489)

> [open] 2025-06-16 — Position breaks after Beeks outage; ongoing rec with Argamon
> Beeks outage 2025-05-25/26 (DNS/public connectivity broken on trading-1 and -2; fixed ~2h after ticket NOCINT-710359). Trades dropped on reconnection created position break. Daria asked Argamon for position rec 2025-06-16 to realign Compass. Subsequent rec work revealed deeper currency breaks (see 2025-06-23 entry). compassDB query performance also degraded — slow queries against HOUSE1TradePositionHistory taking >30s; Justin bumped `net_read_timeout` to 240s. Argamon also requesting Pulse or broader DB access for trade-by-trade rec. [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1748216407505139)

> [resolved] 2025-06-09 — XPTUSD retail losses ~$13k; hybrid hedger not clearing risk fast enough
> Amir flagged -$13.3k retail P&L from $51.2m volume (−$260/M); VaR above $20k for 1 min. Will identified XPTUSD risk not cleared quickly enough — hybrid did 10M while client flow was only 1.1M. Isaac changed mid used by hybrid hedger to allow it to fire. VaR threshold lowered from $80k to $20k. UBS added for XPT pricing 2025-06-06. [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1749459127167139)

> [open] 2025-05-28 — Centroid migration (from OneZero) in flight; FIX tag-ordering issue blocking counterparty ID
> Argamon notified 2025-05-19 of planned migration from OneZero to Centroid before Aug 1 (currently one Mahi insti session; requesting retail + crypto sessions). Centroid test trades 2025-05-28 rejected due to FIX tag ordering (447/448/452 dependent on 453, but Centroid cannot reorder via maker API). Liam suggested tag 109 as workaround; Lee confirmed tag 109 works (tested 2025-06-05). Isaac setting up retail + crypto Centroid channels. HRP party-block mappings require new LP setup per Guru card process. [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1748473150880459)

> [resolved] 2025-05-23 — Crypto over-hedging bug; hedging ~2x client volumes
> Andrew flagged XBTUSD hedge volume ~7.84M vs internalised client flow ~3.9M for the week. Root cause: over-active "Broker-Wintermute-FASTERx500%" execution rule firing beyond inbound flow; delayed dynamic broker-LMAX hedging rule also implicated. Both rules removed 2025-05-23. Cameron and Andrew investigated whether broker-then-hedge double-counting was occurring; concluded execution-rule ordering was the cause. [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1748012505591119)

> [resolved] 2025-05-22 — ACG (Alpha Capital Group) routing via OZ→Argamon; NOP limit and insti channel issues
> ACG (INST-26) flow coming through A_CLIENTS channel, executed on retail model instead of insti. Amir set up a price-check execution rule ($200/M, −$100/M mid distance). Argamon asked to request OZ route flow down an insti connection. NOP limit raised from 10k → 10M for testing; test trades confirmed booked correctly. ACG delayed go-live to Monday 2025-05-26; Amir confirmed no trades since, workflow was sound. Ongoing: Amir to follow up with ACG for live flow. [permalink](https://mahifx.slack.com/archives/C06TW3D8NMV/p1747918313029609)

> [resolved] 2025-05-15 — TOA feed 2-min delays; signalProcess consolidation; TOA MD stopped
> Andrew identified TOA FIX session causing 2-min delays in ArgamonPrices. TOA market data feed stopped 2025-05-15 (Andrew: "stop and delete evidence"). Positions open at Binance/Toa complicated permanent removal — Amir flagged needing Argamon to close TOA positions before removing feed/orders connection. XRP/XLC hedging temporarily moved back to standard Wintermute/LMAX rules while Toa positions unwound. Separately, signal processes consolidated (all into signalProcessFI1 + SIGNALS_NYC); FSS markets added to price formation; MWMS and BMSL markets replaced. TOA hedging later restored for XRP/LTC by 2025-06-26. [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1747315634169499)

> [resolved] 2025-05-15 — Counterparty 84004149 crypto flow review; brokered LR / EURUSD skew tuning
> Andrew flagged counterparty 84004149 as consistently bad for Mahi crypto book (up $200k lifetime, but consistently costly over recent weeks). Reviewed with Isaac: XBT flow switches between BBook and sharp brokered week-to-week. Amir added brokered LR to clientDist1; EURUSD signal response reduced (skew was 1 pip on 0.1 spread, dialled down to ~0.2). Separately, counterparty 84004395 flagged as toxic (retail, EURUSD-focused). [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1747325182217329)

> [resolved] 2026-05-04 — EURUSD mid-formation LP set broadened; arb opportunities eliminated
> Elan approved adding all LPs back into mid formation for NY (now retail-only). Shyam added DB_RCTV_NWPB_1, EDGW_RCTV_NWPB_1, GTSX_RCTV_HRP_2 as supplementary EURUSD mid-formation LPs — backtests confirm significantly reduced spiky pricing and arb opportunities at open and general periods. Adaptive mid logic also added to betaRetailPricer1 for EURUSD as a further experiment. Shyam continuing review of other instruments and overall FI/skew PnL. [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1777869938380839)

> [resolved] 2026-05-03 — XAUUSD retail NY4→CHI hedging disabled (negative retail spreads in CHI)
> Daria disabled XAUUSD retail hedging via NY4→CHI because retail flow was achieving positive spreads while CHI was delivering negative spreads — the brokering test was working against retail PnL. Closes out the 2026-04-28 CME hedging expansion trial. [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1777845150173619)

> [resolved] 2026-05-01 — XAUUSD retail losses from sharp/sniping flow; DFSN signal added; signal-follow whitelist cleaned
> Isaac identified XAUUSD retail losses from 2026-04-30 caused by signal-follow clients sniping sharp moves in pricing. Affected counterparties moved back to broker-only classification (signal-follow whitelist cleaned). DFSN signal rule added to the pricing model to widen Mahi out of the way during large moves. Separate from but related to the CME hedging brokering test (2026-04-28 open issue). [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1746063187834529)

> [resolved] 2026-05-01 — Wide spread on majors (~15:00 BST); LR kicking in on published rate
> Tom flagged EURUSD at ~20 ticks wide for a couple of hours with no client complaints yet. Will identified LR kicking in on the published rate — removed from published, spread immediately restored. [permalink](https://mahifx.slack.com/archives/C06TW3D8NMV/p1746107990556329)

> [resolved] 2026-05-01 — JPY crypto LMAX position risk at rollover (non-issue)
> Tom wanted LMAX removed from JPY crypto hedging/STP ahead of anticipated large JPY financing charge at rollover. Amir confirmed with Isaac that JPY crypto pairs are weekend-only for hedging and are not STP'd — no position should build regardless. No config change needed. [permalink](https://mahifx.slack.com/archives/C06TW3D8NMV/p1746087135603309)

> [resolved] 2026-04-28 — XAUUSD brokered counterparties expansion to test CME hedging; CHI hedging disabled 2026-05-03
> Daria added counterparty 104881 to be brokered to Toa (working through 104881, 105048, 105153, 105681, 105773) to evaluate whether hedging XAUUSD to CME helps. Result: CHI hedging disabled 2026-05-03 as retail was achieving positive spreads (negative in CHI), meaning the NY4→CHI brokering was not beneficial for retail flow. [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1777845150173619)

> [resolved] 2026-04-22 — XAUUSD signal switched synapse → neuron
> Shyam moved XAUUSD from synapse to neuron model to reduce spiky pricing; also cited better skew PnL over the last month. https://mahifx.slack.com/archives/C06U76A7ZJR/p1776832052585769

> [resolved] 2026-04-20 — USDCAD ask-price spike, over-weighting HSBC mid; LP set broadened 2026-05-04
> Tom flagged order 012dr52nxnb filled at 1.371 while market was around 1.370; only HSBC was deviating (other mid-formation LPs unavailable). Tom asked Elan re. adding COMZ and other non-skew-protective LPs into mid. Resolved 2026-05-04: Elan approved adding all LPs into mid formation now that NY is retail-only; Shyam added DB_RCTV_NWPB_1, EDGW_RCTV_NWPB_1, GTSX_RCTV_HRP_2 for EURUSD, significantly reducing spiky pricing. Further instruments under review. [permalink](https://mahifx.slack.com/archives/C06TW3D8NMV/p1776694811277649)

> [resolved] 2026-04-21 — EURHUF indicative pricing; Commerz added
> Daria flagged EURHUF going indicative on/off (2026-04-17), proposed adding LPs into price formation just for that pair. Tom preferred Jane St + Commerz. Shyam added Commerz on 2026-04-21; backtests showed it stops the indicative pricing. https://mahifx.slack.com/archives/C06TW3D8NMV/p1776394647886729

> [open] 2025-04-15 — DB filtered out for small-ticket FX brokering (NWPB min size)
> Tom queried order 012dr82osqn filling via UBS not DB despite both being highlighted. Isaac explained DB was filtered because client order was 5k vs the 15k min-ticket on Mahi's NWPB FX hedger config. James noted Natwest has min ticket sizes and that work with Reactive on a direct setup will remove the constraint. Tom raised whether a 15k floor is justifiable for small-volume auto-brokered clients. Direct-Reactive setup is the in-flight remediation; as of 2025-07-07 Liam/Isaac are configuring HRP LP mappings for Reactive (HSBC/JPM/UBS/NWM/JLQD/XTXM_RCTV_HRP_1) and test trades are progressing. https://mahifx.slack.com/archives/C06TW3D8NMV/p1776233897732439

> [resolved] 2026-04-13 — Missed give-up to HRP (3 EURUSD trades, one not given up)
> Levi reported HRP saw only 2 of 3 trades give up; HRP manually booked the missing one. Daria pulled the FIX AE messages — all three appear to have been sent from Mahi side. Tom said he'd check with HRP; no further messages, treating as resolved on Mahi side. https://mahifx.slack.com/archives/C06TW3D8NMV/p1776034785118149

> [resolved] 2026-04-13 — First-5min market-open EXPIRED / REJECTSYSTEMERROR RAT bursts
> Levi flagged a quantity of rejected orders at market open. Daria identified cancels/rejects clustered after the first 5min, particularly AUDCAD CAD crosses; brokering rules cancelled them because market data wasn't being received yet (Jane Street AUDCAD MD started at 21:10). RATE_LIMIT_EXCEEDED was hit due to retries — 150 orders/sec/counterparty cap. https://mahifx.slack.com/archives/C06TW3D8NMV/p1776049759858249

> [watching] 2026-04-13 — Wide pricing persisting > 1h after rollover
> Tom raised wide pricing in the post-rollover hour, asking for any improvements. No response captured in the window. https://mahifx.slack.com/archives/C06TW3D8NMV/p1776042834123209

> [watching] 2025-04-13 — Centroid LDN distribution backpressure (~10s delays)
> James dug in: Centroid backpressuring (TCP rx window shrinks, zero-window notifications on port 4047, retransmissions on 4031), causing queue on Mahi side. Centroid consume snapshots not increments which compounds at high msg rates. ECB-speech burst hit ~5,000 FIX msgs/sec across both pricing sessions, more than Centroid's receive buffer could drain. Mahi-side publish latency was fine (~0.065ms mean). New /pcap-analysis VibePulse skill referenced. May affect other local NY clients too. Update: Argamon is migrating from OneZero to Centroid before Aug 2025 — CPU saturation seen again at high load; market pruning (cutting LP feeds) flagged as needed but Elan asked to wait for Reactive first. Will/Liam agreed to action LP feed cuts anyway (2025-06-10). https://mahifx.slack.com/archives/C06U76A7ZJR/p1776116671694999

> [resolved] 2026-04-08 — NY4 → CHI brokering live
> Daria flipped on brokering to CHI from NY4. Watching for orders from the counterparties Elan selected. https://mahifx.slack.com/archives/C06U76A7ZJR/p1775686974874039

> [watching] 2025-04-02 — Non-flat LP MXN exposure with no client MXN positions
> Tom noticed non-flat LP exposure in USDMXN/EURMXN despite no client positions; was moving exposure from HRP to NWM for better swap rates. Daria explained: hedgers only trade USDMXN, so a client whose classification changed mid-position would have one leg brokered through EURMXN and one internalised + hedged via USDMXN. Cleared Tom to close out so long as net MXN unchanged, asked he do it through Compass or notify. Tom acknowledged but deferred to "next week" (2025-04-03), no further follow-up seen across the catchup window. https://mahifx.slack.com/archives/C06TW3D8NMV/p1775139754817979

## Notable topics

- Mid-formation LP set under review — Tom and Daria are both pushing to broaden the price-formation LP set (COMZ, Jane Street) to reduce dependency on HSBC and to fix per-pair indicatives. Decision still sitting with Elan.
- Reactive direct setup is the strategic remediation for NWPB (Natwest) min-ticket-size filtering of small client orders. Flagged in 2025-04-15 thread; HRP LP mappings being configured as of 2025-07-07; production test trades in progress.
- Centroid LDN distribution issues are a CTO-level dig (James Furness) — backpressure root-caused via pcap; further work likely needed and may generalise to other NY-local clients distributing via Centroid. Argamon simultaneously migrating to Centroid from OneZero before Aug 2025, creating CPU-saturation risk; LP feed pruning flagged.
- XAUUSD sharp-flow / signal-follow risk — signal-follow whitelist cleaned 2025-05-01 and DFSN signal added to retail pricing model. May need monitoring if similar sniping recurs.
- Contract restructure: Mahi retains retail tenant; Toa taking B2B/Crypto/RI. Insti contract signed to Toa 2025-07-09. Retail contract conversion to fixed-fee pending before Elan's planned spread tightening.
- Currency position rec with Argamon is now a formal recurring process — Argamon to submit regular rec reports; Mahi adjusts Compass positions to match. Root causes include crypto JPY hedging creating currency exposure Argamon didn't anticipate, and client P&L included in Compass but not client platform positions (large EURAUD traders). Will Carter proposed argamon_rec.ipynb notebook in analytics-python-tools for this.
- Reactive Markets (Argamon via Mahi) — XTX-Algo live 2025-07-08; NY4→TKY dedicated WAN live 2025-06-16; production Reactive test trades in progress. XTXM_RCTV_HRP_1 temporarily pulled due to HRP booking duplicate issue. Slow-consumer issue with Beeks cross-connect is recurring.
- Lucera for insti — conformance completed 2025-06-27; Daria issued credentials 2025-07-09; pricing review needed before going live (new Reactive feeds to be used).
- Insti model change: not doing insti via Centroid — moved toward Lucera instead (Natwest drop copy 5-month delay was blocking factor). Per Daria/Elan call 2025-05-20.
- Compass DB access / Pulse — Argamon requesting broader DB access (HouseOrder/ExternalOrder tables) for trade-by-trade rec. Liam flagged this should require a Pulse contract. Slow HOUSE1TradePositionHistory queries addressed (timeout bumped to 240s).
- Argamon requested shared project tracking system 2025-07-07 — Daria pushed back; not proceeding at this stage.
