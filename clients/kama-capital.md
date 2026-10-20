---
slug: kama-capital
aliases: []
refs:
  vibepulse: null   # no ../VibePulse/.claude/clients/kama-capital.yaml yet
  billing: ../MahiProduct/data/billing/clients.json     # entry: kama-capital
  hosts: ../MahiProduct/data/client-hosts.json          # entry: kama-capital
  wiki: ../MahiProduct/wiki/clients/kama-capital.md
channels:
  internal-kama: C0B6FMU96G2
  mahi-kama-capital: C0B7T6S6D0C
  mahi-kama-config-updates: C0C1L6G37HN
contacts:
  - {name: "Mohamad (Moe) Ibrahim", role: "COO, decision-maker; sets execution rules and LP choices"}
  - {name: "Ali Chayto", role: "dealing; day-to-day on routing, LPs, test trades"}
  - {name: "Jad Hayek", role: "ops / access, whitelisting, Compass users"}
  - {name: "Mahmoud Kleit", role: "built Kama's swap sync tool; on holiday as of 2026-10-09", confidence: low}
  - {name: "Sammy (xrigroup)", role: "third-party consultant helping Kama on SI and tags; pushes SI", confidence: low}
last_catchup: 2026-10-20T07:16:51Z
status: active
---

## Now
Live Compass-managed A Book on XAUUSD (plus HFT and Kama Securities flow) with most connectors routed since 2026-09-29; Kama keeps tuning execution style and the LP pool. Kate Stagg is the day-to-day owner; Moe Ibrahim drives changes on the client side. Pilot has about a month left (term counts from the 5 Aug go-live; Will, 12 Oct) with post-pilot terms recorded ready to send. Compass 26.4 released 17 Oct; XAUUSD pulled from MAS on 16 Oct over market-order rejects. On 19 Oct the hedger stopped clearing XAUUSD (NOP limits vs unreconciled positions; about 26,000oz unhedged) and a null-check bug crashed the SOR when a NOP key was deleted; NOP limits are off pending a fix deploy. Open: MAS filled-after-cancel reconciliation and PXM timeout handling; Friday-close risk carry under Broker First.

## Streams

### nop-hedger-outage — 19 Oct unhedged XAUUSD, SOR crash, VaR alerting
status: open · since: 2026-10-19 · last: 2026-10-19
State: From about 06:58 UTC on 19 Oct the hedger stopped clearing XAUUSD, most likely blocked by per-LP NOP limits running against unreconciled positions (Kama had posted positions in a thread, so they were missed); VaR passed 10k at 05:33 and hit about 146k (Ali: 26,000oz unhedged), and Kama raised it at 07:31. At 07:35 Isaac deleted risk.nop.perPB to unblock the hedger; a missing null check crashed liquidityPoolSOR and the hybrid and arb hedgers, ten XAUUSD orders sat open 6-9 min and Kama's 180s timeout disabled Mahi as provider until about 07:51. Processes were back by 07:37. Fix (null guard in MarketGroupTradePositionNOPTracker) is committed to release/26.4 and 26.3 but not yet deployed; until then do not delete NOP keys on Kama (set marketListNOPConfigs to [] or raise watermarks). All NOP limits were removed on Ali's request. Kate set a sustained critical-VaR alert (sustainMs 120,000, clearHoldMs 60,000) after Ali asked for an alert and a noisy 10k threshold; Kate offered to post VaR alerts to Kama's Slack notifications channel too. Liam asked how we know we hedge the right thing with unreconciled positions; Kate: Kama was STP before, so all A Book risk is covered by hedging or STP.
Next: Kama to send positions at EOD roll; Isaac to get the null-check fix deployed and raise whether bad non-trading config should keep the old config instead of killing processes; Kate to tune the VaR alert if noisy.
Refs: https://mahifx.slack.com/archives/C0B7T6S6D0C/p1792395096025849 https://mahifx.slack.com/archives/C0B6FMU96G2/p1792397763936839 https://mahifx.slack.com/archives/C0B6FMU96G2/p1792417025779529

### tag-lp-exclusion — Block a counterparty tag from a specific LP
status: open · since: 2026-10-19 · last: 2026-10-19
State: Moe asked on 19 Oct whether a specific counterparty tag can be kept from going to a specific LP on Mahi hedging trades; rory.king confirmed it is doable and offered to set it up from an example tag and LP. Moe is confirming with the LP first.
Next: Moe to supply the tag and LP; rory to configure and share the config.
Refs: https://mahifx.slack.com/archives/C0B7T6S6D0C/p1792407866139499 https://mahifx.slack.com/archives/C0B7T6S6D0C/p1792411908923309

### lp-timeouts-pxm-unsub — LP latency and timeouts triggering PXM unsubscribes
status: open · since: 2026-09-15 · last: 2026-10-19
State: Recurring pattern: an order sitting unanswered trips PXM's firewall timeout and PXM unsubscribes XAUUSD on Kama's price sessions with no automatic resubscribe (15 Sep SOR restart; 2 Oct misconfigured MCC restart; 19 Oct, see nop-hedger-outage). On 19 Oct Kate recommended keeping the 180,000ms timeout (Rostro uses the same) and instead having PXM cancel the leg and reject the client order on a pending-leg timeout while keeping the provider enabled; Moe says PXM disables the provider (or the symbol) completely on timeout, Kate noted other PXM clients just reject the order so it looks configurable, and Moe will ask PXM. Moe also wants restarts coordinated better; Kate will give notice of planned ones. Latency incidents: Arts held limit orders 1.4-3.3s and filled 9 of them worse than limit (about $110/M; Arts later said it would fill in 1000ms and was left out of pools 8 Oct), and MAS held IOCs about 360ms against the 300ms latency guard (5 Oct). Mahi's stance (Kate, 12 Oct): never resend an order that is still open (double-fill risk), re-hedge via other LPs only once it is dead; hardTimeoutLength exists but guesses the outcome and can strand risk (Liam). Ali objects that PXM disables the whole Mahi provider on one timeout (rory to check, 9 Oct) and that brokered orders wait for the LP fill so clients with a 500ms TTL time out (William doubts Compass supports client TTL, 5 Oct).
Next: Moe to ask PXM whether disable-on-timeout can be switched off for Kama; Mahi (rory) to confirm the PXM provider-disable behaviour; decide on hardTimeoutLength or asking LPs to reject after about 100ms.
Refs: https://mahifx.slack.com/archives/C0B6FMU96G2/p1791257314493849 https://mahifx.slack.com/archives/C0B7T6S6D0C/p1792409733558559

### position-rec-nop — LP/client position reconciliation and NOP limits
status: open · since: 2026-10-02 · last: 2026-10-19
State: On 19 Oct unreconciled LP positions against per-LP NOP limits blocked the hedger (see nop-hedger-outage); the limits were removed that day and Kate will ask Kama to send positions at EOD roll, XAUUSD being most of their flow. Only apply NOP limits on reconciled positions. LP positions are visible in Compass under Risk Management Positions (Markets tab per LP); NOP limit changes need hedger and pool restarts (pool at EOD) and LP position adjustments can be made intraday with the hedger off, normally by the NZ team before open. Kate asked on 9 Oct for LP and client positions over the weekend for a rec; Kama replied inside the thread (file 10 Oct; Moe 11 Oct: keep NOP limits, reflect LP positions, sell 280oz) so the NZ team never saw it and nothing was updated. Kate says the 280oz was already cleared at Sunday open and asked for positions to be re-posted at roll in the main channel.
Next: Kama to post LP positions at roll in the main channel; agree when NOP limits are re-applied.
Refs: https://mahifx.slack.com/archives/C0B7T6S6D0C/p1791557796452229 https://mahifx.slack.com/archives/C0B6FMU96G2/p1792404397201249

### mas-xau-removal — XAUUSD pulled from MAS Markets
status: open · since: 2026-10-16 · last: 2026-10-16
State: On 16 Oct Moe asked Kate to stop sending XAUUSD to MAS Markets (standard feed only, not toxic); Kate removed it from the hedging markets straight away but the liquidity-pool (STP) side cannot drop one symbol, so she offered to set everything to internalise while the SOR is bounced. Moe chose to disable gold on Kama's side (switched off the price) and said it is easier if one symbol can be disabled per LP; Kate will look at restructuring the pool setup to allow that. Reason given: MAS rejecting market orders, causing losses in the Compass book. Kate asked for more detail on why.
Next: Moe to give detail on MAS market-order rejects; Kate to see whether pools can disable one symbol per LP.
Refs: https://mahifx.slack.com/archives/C0B7T6S6D0C/p1792154269472349 https://mahifx.slack.com/archives/C0B7T6S6D0C/p1792160709717089

### brokered-flow-review — Brokered vs internalised flow review (internal)
status: open · since: 2026-10-16 · last: 2026-10-16
State: Kate's 9-16 Oct execution-quality review (internal) found most internalisable brokered flow is roll, twilight and Sunday/Monday open. Open brokered $145M and kept $26k ($182/M), almost all EURJPY with spreads slightly wider than Scope; roll/twilight brokered $783M XAUUSD and kept $14.2/M versus about $1.7/M if internalised, so brokering is right there. CP 100079_n/a was tagged arbitrageur then brokering 7-9 Oct and untagged before 12 Oct; it is now internalised on Catch-All at about -$71/M at 1m on $99M XAUUSD, no manual change, watching for re-tag. 40874_30033000 is the only steady internalise candidate (about $1k/week), to watch a couple more weeks. Andrew queried why Broker First internalises some flow at lower yield; Kate: internalised pays Mahi spreads, brokered pays LP spreads, and all rules use passthrough fill price. Andrew fed the lesson into the routine checks (PR 153 merged) so positive markouts need session/regime review before rehabilitation advice.
Next: Kate to finish instrument/timezone/CP breakdown; watch 100079_n/a re-tagging and 40874_30033000.
Refs: https://mahifx.slack.com/archives/C0B6FMU96G2/p1792160321472259 https://mahifx.slack.com/archives/C0B6FMU96G2/p1792165670366029

### lp-pool-expansion — LP pool and hedging markets, KL/KS connectors
status: open · since: 2026-09-21 · last: 2026-10-15
State: Pool started as Scope only. Moe asked 2026-10-01 for Scope, MAS, Edgewater, MatchPrime-FXedge and Arts with NOP limits. FXEdge and Arts went in after test trades (5-6 Oct), then Arts was pulled from the pool and hedging for latency (6 Oct) and left out at the 8 Oct call (NOP limits per LP: Scope 150M, MAS/Edgewater 20M, FXEdge 10M, Arts 5M). MatchPrime was restricted to gold on 7 Oct and restored on all symbols the same day after they fixed swap rates. On 14-15 Oct Star and Velocity were added and Ali sent a clean-up list, ending with Moe's final list: LIQUIDITY_POOL_HFT_LDN = Edgewater_2_KS, MAS_Toxic_KS, Scope_Toxic_KL; LIQUIDITY_POOL_LDN = Edgewater_2_KS, Scope_KL, MAS_KS, FX_EDGE_KL. Kate suggested spreading load across LLC (KL) and Securities (KS) connectors rather than all on KL. Moe's 15 Oct connector subscription list also carries Fusion, Arts, Star and Velocity, which are not in the pools yet. Pool changes need EOD restarts; hedger changes can be bounced intraday. Kate (15 Oct): removing a market from a pool is dynamic, adding one needs a restart; intraday options exist if Kama wants a change before EOD.
Next: Kate to make the 15 Oct pool changes and remove listed LPs ahead of weekend restarts; Ali to flag when Star and Velocity are ready for test trades before they join the pool.
Refs: https://mahifx.slack.com/archives/C0B7T6S6D0C/p1789990153651149 https://mahifx.slack.com/archives/C0B7T6S6D0C/p1792062491797469

### si-and-risk-golive — Risk-management go-live and SI
status: open · since: 2026-09-15 · last: 2026-10-15
State: Risk go-live began 2026-09-14 but the first A Book client switched off after a position-rec scare and an SOR restart that tripped PXM's firewall; flow came back 17-23 Sep. Kate pushed Kama to run the Compass book for a few weeks before SI, and ran SI sims on Moe's tag cohort (results weak; Sammy argued SI may not suit Kama). Mahi view (Andrew, Will): flow with Kama in aggregation (e.g. Star, tag 42060) is not SI material. On the 8 Oct call Kama wanted SI soon and supplied a list of tags; Kate is running sims on those tags and the full portfolio and will review with them. Kama also wants to add 26degrees and ISAM and asked for anonymised reject-rate data from other clients; Kate's 8 Oct Pulse analysis (6 clients, 30d) found gold reject rates of about 5-89% depending on setup and clip size, so she recommends giving no figure and offering to measure on Kama's own flow (no sign it was sent).
Next: Kate to finish the SI sims and walk Kama through them; reply to Kama on reject rates (recommended: no number).
Refs: https://mahifx.slack.com/archives/C0B6FMU96G2/p1789482321712589 https://mahifx.slack.com/archives/C0B6FMU96G2/p1792064464469069

### xau-execution-style — Broker vs Broker First, HFT book and markup
status: open · since: 2026-09-21 · last: 2026-10-15
State: A 21 Sep cancel burst came from FOK/IOC MinQty handling (fixed with reference.marketSupport.FOK) and led to Kama moving all A_CLIENTS to Broker First (29 Sep). HFT flow got its own book and hedgers (30 Sep) with internalisation on the toxic HFT pool; $20/M markup on HFT and $10/M on A Book internalised flow was agreed on the 1 Oct call and set up via MultiChannelConfig on 2 Oct (a type=list vs ArrayList misconfig caused stuck orders that day). On 30 Sep Kate asked Kama to turn off PXM sweep/boost so each A-book order arrives whole and Ali asked to switch to single IOC (Kate: IOC or FOK is fine); Ali was confirming with PXM and no outcome is visible. The automated classifier moves clients between broker/signal-follow and catch-all, so catch-all history on a tag is expected (William, 21 Sep). On 15 Oct Kama asked for Broker (not Broker First) over high-impact news and said they are happy to switch manually; Moe set twilight and roll flow to Broker. Kate flagged that execution rules cannot be day-specific. Kate answered that a bare '*' in counterparty criteria matches none (rule will not fire); to apply to every counterparty, remove the criteria altogether.
Next: Mahi to confirm whether news criteria can be added to execution rules.
Refs: https://mahifx.slack.com/archives/C0B7T6S6D0C/p1790009143944299 https://mahifx.slack.com/archives/C0B6FMU96G2/p1792064464469069

### xauusd-skew-signals — B Book XAUUSD skew tuning
status: open · since: 2026-10-08 · last: 2026-10-14
State: B Book XAUUSD skew was about -$0.35/M for 1-8 Oct because FI optimisation parties included CLIENTS_LDN (INSTI-priced, never skewed). Kate switched the skew signal to IFM, then limited optimisation parties to B_CLIENTS_LDN (8 Oct). Skew since was +$1.61/M over 9, 12 and 13 Oct (+$528 on $329M; early). On 14 Oct she moved the signal from IFM to flow-price-thresh (57.7% volume correct, $675 potential vs IFM 51.0%, $424).
Next: Kate to keep reviewing; a before/after backtest was planned.
Refs: https://mahifx.slack.com/archives/C0B6FMU96G2/p1791471223806789 https://mahifx.slack.com/archives/C0B6FMU96G2/p1791965822602239

### weekend-risk-carry — Friday close hedging did not clear risk
status: open · since: 2026-10-12 · last: 2026-10-13
State: Compass book carried risk over the 9-10 Oct weekend (about $23k PnL bump on open). Cause: a Broker First top-up just before close (the unfilled 280oz of client 43795's 1,000oz sell at 20:56 UTC) could not be hedged because LP liquidity had dried up; Friday_Close tried and got no fill, and the hedger sold the 280oz at Sunday's open (22:01-22:02 UTC). Friday_Close had only 4 fills since 14 Sep (all XAUUSD, 9 Oct) and Metals.WEEKDAY-CLOSE none; the weekly hybrid-diagnostic missed dormant rules. Kama prefer Broker First to avoid cancels and client rebate claims (Moe does not want to pass cancels to LPs). On 15 Oct Moe set twilight and roll flow to Broker.
Next: Shyam's PR (MahiProduct #126) adding dormant-rule and weekend-carry checks awaits Will's approval; Kate to find a way to avoid carry without day-specific execution rules; check the 16 Oct Friday close to see whether twilight Broker removes the carry.
Refs: https://mahifx.slack.com/archives/C0B6FMU96G2/p1791798684555499

### mas-fill-after-cancel — MAS 2-minute timeout, 75oz filled after cancel
status: open · since: 2026-10-09 · last: 2026-10-12
State: On 9 Oct a 75oz XAUUSD buy sent to MAS Markets got no response for about 2 minutes and crashed the hedger; MAS then sent a cancel and PXM disabled MAS (hedger restarted, Moe took it to MAS). Kate worked out on 12 Oct that two 75oz buys went to MAS at 16:59:57 UTC, one on KS (filled) and one on KL (order 4570942, cancelled after 3 minutes), and that MAS actually filled the cancelled one, leaving Compass over-hedged 75oz until Kama closed it manually in the MAS account. Ali had not yet confirmed whether he saw one fill or two; Kate says it is not sorted and wants a call.
Next: Ali to confirm one fill vs two; Kate to get Kama and MAS on a call.
Refs: https://mahifx.slack.com/archives/C0B7T6S6D0C/p1791566302175459 https://mahifx.slack.com/archives/C0B7T6S6D0C/p1791800955956099

### fx-hedge-swaps — Hedging crosses in drivers vs swap cost
status: open · since: 2026-10-09 · last: 2026-10-09
State: Moe says Kama loses on swaps because Compass hedges crosses in the drivers (EURJPY example) and wants hedging in the same currency as the client trade. Kate pushed back (drivers avoid the cross spread; only a loss if risk is held several nights). Peer data: Kama's FX major and JPY swap points are about half the network median, while gold swap is second widest. Moe agreed to inventory-skewed swaps (feasible: the analytics bridge saves swap points daily); Mahmoud (swap sync tool) is on holiday and will do it on return.
Next: Kate to raise swap skewing with Moe; follow up when Mahmoud is back.
Refs: https://mahifx.slack.com/archives/C0B6FMU96G2/p1791544461594299

### beeks-multicast — Beeks multicast/IGMP issue and false PnL alerts
status: open · since: 2026-09-28 · last: 2026-10-07
State: Outdated reference mid prices caused false PnL-drop pager alerts on Kama; tied to a Beeks multicast issue (Zendesk 23343, Beeks NOCINT-839427). On 30 Sep Beeks said enabling IGMP snooping mitigated storm control, that it is still investigating blackholing on an LD5 distribution switch (servers cannot see the querier), and that Mahi should take no action and leave its test scripts in place. Liam sent a chaser on 7 Oct asking for an ETA; no Beeks answer is visible since.
Next: Liam/Inald to chase Beeks for a fix ETA.
Refs: https://mahifx.slack.com/archives/C0B6FMU96G2/p1790597791892939 https://mahifx.slack.com/archives/C0B6FMU96G2/p1791364219575089

### pilot-commercials — Pilot term and post-pilot terms
status: watching · since: 2026-09-10 · last: 2026-10-12
State: Pilot term runs from the 5 Aug go-live with a free integration period, not from signing; Bonnie's "expired" figures count from 9 Sep. On 12 Oct Bonnie (from Nic's handover doc) said the pilot was 33 days expired; Will answered "same story" (linking the 10 Sep note) and "month left on the pilot", and Bonnie accepted ("Ah sorry"). So the pilot has about a month left (ends around early Nov, inferred as 3 months from 5 Aug) and the post-pilot terms are recorded ready to send. The wiki table still says the pilot expired 9 Sep.
Next: Will to send the post-pilot terms before the pilot period ends; no evidence in Slack they have gone to Kama.
Refs: https://mahifx.slack.com/archives/C0B6FMU96G2/p1789029069493129 https://mahifx.slack.com/archives/C0B6FMU96G2/p1791824613643489

### xpd-pricing — XPDUSD price jumps between LP levels
status: watching · since: 2026-10-09 · last: 2026-10-09
State: XPDUSD published mid jumped between two LP price levels 10-40bp apart (worst 8 Oct). Kate changed reference.referencePriceMarketSelectors so XPD prices off SCOPE_KL only, applied at weekend restarts. No PnL impact so far (140 XPD fills, about $28M since 8 Sep).
Next: Check XPD price variation after the weekend restart.
Refs: https://mahifx.slack.com/archives/C0B6FMU96G2/p1791557308635619

### kama-securities-oz — Kama Securities entity and OZ hub connections
status: watching · since: 2026-09-23 · last: 2026-10-05
State: Kama Securities MT5 A and B clients were routed to Compass on 23 Sep (Cameron Hughes saw no rejects). On 2 Oct infra added clientDistributionGatewayOZ3 and InstOZ4 for 10 extra distribution connections for Kama's OZ hub, copying the PXM setup. On 5 Oct Arun saw all ten OZ FIX sessions unconnected; Kate confirmed they are not live yet (OZ is new to Kama, credentials issued) and turned monitoring off until they connect.
Next: Re-enable OZ session monitoring when Kama connects.
Refs: https://mahifx.slack.com/archives/C0B7T6S6D0C/p1790147027559829 https://mahifx.slack.com/archives/C0B6FMU96G2/p1791200801834109

### scope-price-latency — Hedge-fund client blames Scope price latency for win-rate drop
status: watching · since: 2026-10-01 · last: 2026-10-01
State: From Kate's 1 Oct call notes: one of Kama's clients, an aggregating hedge fund that sends weekly stats, saw Kama's win rate fall from 27% to 17% in a week and attributes it to latency in Scope's price. At the time Kama passed Scope's price straight through (Scope was the only market in price formation and the hedging pool). Kate flagged it as "one to look into at rostro"; no follow-up seen in Slack since. Price formation and the pool have since widened beyond Scope (see lp-pool-expansion), which may dilute the effect.
Next: Kate/Will to check Scope's price latency on the Rostro side, or confirm it was dropped.
Refs: https://mahifx.slack.com/archives/C0B6FMU96G2/p1790858811618719

### limit-order-deviation — Limit order deviation (tag 10001)
status: watching · since: 2026-09-25 · last: 2026-09-28
State: Kama pass limit-order deviation in tag 10001, which is not in Mahi's FIX spec; Mahi expects it baked into price (tag 44). Moe explained on 25 Sep that PXM sets the limit price from Kama's TOB (not the client's limit) and sends a deviation, so Compass should respect limit plus/minus deviation and allow worse fills up to it; this also explains Scope limit rejects. William noted price improvement is off on all A_CLIENTS rules and has a cap setting. Mahi still does not accept the tag and no decision on honouring it is visible.
Next: Kate to decide whether Compass can honour limit plus/minus deviation (tag 10001).
Refs: https://mahifx.slack.com/archives/C0B7T6S6D0C/p1790332508870719 https://mahifx.slack.com/archives/C0B6FMU96G2/p1790598299904109

### settldate-tag64 — Bad SettlDate (tag 64) from LPs
status: closed · since: 2026-10-02 · last: 2026-10-06 · closed: 2026-10-15
State: FXEdge sent a timestamp instead of a yyyyMMdd SettlDate (2 Oct); ignoreSettlDate was switched on for fixOrders1 (5 Oct, Moe approved). The 6 Oct PXM drop-copy failures were the same FXEdge date carried through the Xcore execution report, not a PXM change, and Arun added ignoreSettlDate to analyticsFixServerPXM1 (Kate agreed); no later failures seen, assumed fixed.
Refs: https://mahifx.slack.com/archives/C0B7T6S6D0C/p1790929869661149 https://mahifx.slack.com/archives/C0B6FMU96G2/p1791289838943309

## Arc
- 2026-06-02 — Deal accepted; pilot agreement signed 2026-06-08
- 2026-08-05 — B Book flow live on Compass (pricing and execution)
- 2026-09-14 — Risk-management go-live (A Book), interrupted and restored 17-23 Sep
- 2026-09-23 — Kama Securities MT5 A/B flow routed to Compass
- 2026-09-29 — Almost all Kama connectors routed to Compass; HFT clients added; VaR raised to 2,000
