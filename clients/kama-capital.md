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
last_catchup: 2026-11-12T08:16:18Z
status: active
---

## Now
Live Compass-managed A Book on XAUUSD (plus HFT and Kama Securities flow); pilot ended 5 Nov and Nicole's draft contract (3-month rolling, volume tiers, futures/CFDs at no extra cost) awaits Will and Kate. On 5 Nov Kama parked SI to get CFDs and futures live first; the futures went into the client DB on 6 Nov and go live at the weekend restart (verification due 10 Nov). On 9 Nov Velocity passed test trades (FX, XAG) and went into the hedger; CFD book and hedger base setup staged. On 6 Nov Moe had all markups removed. On 11 Nov Kama sent LP quantity limits for CFDs/futures; NZ support is out Fri 13 Nov (email/phone only). Open: FX Edge fill delays, GBPCAD/EURGBP rejects, NOP null-check fix deploy, PXM timeout handling.

## Streams

### futures-cfd-onboarding — Futures and CFDs added to Kama's Compass
status: open · since: 2026-10-29 · last: 2026-11-11
State: Kama want futures and CFDs live (added to the contract at no extra cost, see pilot-commercials). Kate set up indices on the pricing model; Ali listed the Z26/F27 contracts and enabled them on Mahi's connection, and on 5 Nov Kate updated subscription mappings, custom instruments and the instrument list mapping (DAX30, GC, SI, US100, US30, US500, USOIL, UKOIL). On 6 Nov Inald put the new futures (8 families, 52 contracts) into the client DB under CHG-2611-X9VR (ZD #23780, approved by Liam); live only at the kama-ln-trading-1 restart, marked implemented 7 Nov, verification due 10 Nov (3 of 4 checks pending, no result seen). William staged CHG-2611-G9MP (CFD book, hedger and channel base setup, no client routing, live at restart) on 9 Nov and CHG-2611-0KWV (futures P/W books, hedgers and channels, approved 10 Nov 15:06Z); Kate and William kept editing CFD pool, instrumentListMapping and FIX subscriptionMappings on 9-10 Nov, with pool restarts pending. Main LP for CFDs except oil is Velocity. Kama will not use new instruments for XAUUSD until indices, oil and futures are live. On 11 Nov Kate asked for LP min/step/max quantities for CFDs and futures; Ali posted the MT5 connector table (e.g. DAX30 0.1/100/0.1, DAX30 future 0.25/250/0.25, GC 1/1000/1, SI 50/50000/50, USOIL and UKOIL 10/20000/10, XNGUSD 100/50000/100; .YYYY marks the futures contract) and Kate thanked him.
Next: Inald to finish verification (CHG-2611-X9VR); Kate/William to finish CFD and futures books and hedgers (CHG-2611-G9MP, CHG-2611-0KWV), apply Kama's quantity limits, then enable client routing.
Refs: https://mahifx.slack.com/archives/C0B7T6S6D0C/p1793283834284999 https://mahifx.slack.com/archives/C0B6FMU96G2/p1794226387016589 https://mahifx.slack.com/archives/C0B7T6S6D0C/p1794413105717269

### xau-execution-style — Broker vs Broker First, HFT book and markup
status: open · since: 2026-09-21 · last: 2026-11-10
State: A 21 Sep cancel burst (FOK/IOC MinQty handling) led to Kama moving all A_CLIENTS to Broker First (29 Sep). HFT flow got its own book and hedgers (30 Sep) with internalisation on the toxic HFT pool; $20/M markup on HFT and $10/M on A Book internalised flow was agreed on 1 Oct and set up via MultiChannelConfig on 2 Oct. On 30 Sep Kate asked Kama to turn off PXM sweep/boost so each A-book order arrives whole; Ali was confirming with PXM and no outcome is visible. On 15 Oct Kama asked for Broker (not Broker First) over high-impact news; Moe set twilight and roll flow to Broker. Execution rules cannot be day-specific; a bare '*' in counterparty criteria matches none. On 21 Oct FOK orders (21:00-23:00 UTC) expired as no HFT-channel LP accepted FOK; Kate set reference.marketSupport.FOK across the board. Kama staff edited distribution.executionRules repeatedly (22, 26, 27 Oct, 4 and 6 Nov, and four times on 10 Nov by Ali and a colleague; content not visible). The agreed $20/M and $10/M markups were removed on 6 Nov (see markup-removal).
Next: Mahi to confirm whether news criteria can be added to execution rules.
Refs: https://mahifx.slack.com/archives/C0B7T6S6D0C/p1790009143944299 https://mahifx.slack.com/archives/C0C1L6G37HN/p1793098819391439 https://mahifx.slack.com/archives/C0C1L6G37HN/p1794321220997669

### lp-pool-expansion — LP pool and hedging markets, KL/KS connectors
status: open · since: 2026-09-21 · last: 2026-11-09
State: Pool started as Scope only; FXEdge and Arts joined after test trades (5-6 Oct) and Arts was pulled for latency (6 Oct); MatchPrime was restored on all symbols 7 Oct. On 14-15 Oct Star and Velocity were added and Ali sent a clean-up list, ending with Moe's final list: LIQUIDITY_POOL_HFT_LDN = Edgewater_2_KS, MAS_Toxic_KS, Scope_Toxic_KL; LIQUIDITY_POOL_LDN = Edgewater_2_KS, Scope_KL, MAS_KS, FX_EDGE_KL. Kate suggested spreading load across LLC (KL) and Securities (KS) connectors rather than all on KL. Fusion, Arts and Star are subscribed but not in the pools. Removing a market from a pool is dynamic; adding one needs a restart (EOD, or intraday on request). LIQUIDITY_POOL_HFT still carries XAUUSD only; the other instruments were due at the 20 Oct EOD restart (see hft-fx-pricing). On 21 Oct MAS Markets was removed from all pools and hedging at Moe's request (see mas-xau-removal); Isaac changed pools and overrides and restarted the pools and hedger. On 9 Nov Ali asked to test Velocity (FX only for now; not to be used for XAUUSD until CFDs/futures are live). Kate's test trades: EURUSD filled on VELOCITY_KS and KL; XAGUSD priced only on KS, KL showed no XAGUSD price until Ali fixed something on his side, then XAG matched; Ali confirmed all good. Kate then put Velocity in the hedger for FX and XAG (hedging.executionMarkets and distribution.pools.markets edited 10:33-10:35 UTC, pool restart needed), pool addition taking effect at EOD restarts.
Next: Kate to confirm Velocity is in the LDN pool after the EOD restart; Ali to flag when Star is ready for test trades.
Refs: https://mahifx.slack.com/archives/C0B7T6S6D0C/p1789990153651149 https://mahifx.slack.com/archives/C0B7T6S6D0C/p1794219913020909

### markup-removal — Moe orders all markups removed
status: open · since: 2026-11-06 · last: 2026-11-06
State: On 6 Nov Moe told Kate to remove any markup on the system, saying nothing like this should happen without Kama approving it and that Kama only marks up its own clients; Kate removed all internalise and broker markups (markupProfiles edits 12:45-12:52 UTC). Kate explained the internalisation markup on the defensive channels (agreed 1-2 Oct) was also hitting brokered trades, since brokered fills peg to the channel price. Internally Will tied it to the Sammy (xrigroup) friction. Moe and Ali acknowledged; HFT and A-book internalised flow now carries no markup, which may affect the A/HFT economics in the SI and pilot-commercials discussions.
Next: Kama to confirm any markup they do want, via explicit approval.
Refs: https://mahifx.slack.com/archives/C0B7T6S6D0C/p1793969043880159 https://mahifx.slack.com/archives/C0B7T6S6D0C/p1793970050098779

### gbpcad-quote-block — GBPCAD rejects at market open (quote blocked)
status: open · since: 2026-11-06 · last: 2026-11-06
State: On 6 Nov Ali asked Mahi to check the reject reasons on GBPCAD at the market open the night before: Kama's logs show quote blocked and he thinks Scope was not quoting then (screenshot only). No reply yet.
Next: Mahi to diagnose and reply.
Refs: https://mahifx.slack.com/archives/C0B7T6S6D0C/p1793948581789389

### fxedge-delays — FX Edge fill delays and cancels via PXM
status: open · since: 2026-11-05 · last: 2026-11-05
State: On 5 Nov Daria asked Kama to check with PXM why order 012drb34aa (GBPNZD, bound for FXEDGE_KL) was acked at once but took 12s to fill, and offered to pull FX Edge from the pool meanwhile; Ali said Kama has issues with orders going to FX Edge and saw high execution times on the Non skewed A provider (quote blocked and max exposure reached on FX Edge). Daria's read of order 4964712: the SOR split it across FX Edge, Scope and Edgewater; Scope and Edgewater filled quickly while FX Edge delayed and cancelled, the SOR kept retrying FX Edge and held the order until it was cancelled and refilled elsewhere; she sees no Compass-side speed issue. Ali asked how long the SOR keeps retrying one provider and how that process works; Cameron Hughes said he will gather details. No decision yet on removing FX Edge from the pool.
Next: Cameron Hughes to answer Ali on SOR retry behaviour; Kama to check FX Edge/PXM side; decide whether to pull FX Edge from the pool.
Refs: https://mahifx.slack.com/archives/C0B7T6S6D0C/p1793859648388519 https://mahifx.slack.com/archives/C0B7T6S6D0C/p1793864803371289

### si-and-risk-golive — Risk-management go-live and SI
status: open · since: 2026-09-15 · last: 2026-11-05
State: Risk go-live began 2026-09-14 but the first A Book client switched off after a position-rec scare and an SOR restart that tripped PXM's firewall; flow came back 17-23 Sep. Mahi view (Andrew, Will): flow with Kama in aggregation (e.g. Star, tag 42060) is not SI material. Kate's SI sims (22-26 Oct) on Kama's XAUUSD drop copy 15 Jul-14 Oct: Compass-good flow (17 logins, $2.7B) with a 2-3h window and no cap beat A-booking by about $400k; short-horizon and long/toxic flow did not reliably. The gain leaned on four HFT-routed logins and tag 42060, so Mahi proposed letting Compass's classification pick logins. On the 29 Oct call Kama were disappointed; Kate explained hardly any accounts are round-trip, so they likely have Mahi in aggregation. Kama wanted to use their own tags with Mahi picking out bad subtags, plus exclude a few physical gold hedgers (Moe to send list). Kama also wants to add 26degrees and ISAM and asked for anonymised reject-rate data from other clients; Kate recommends giving no figure and offering to measure on Kama's own flow (no sign it was sent). On 5 Nov Kate posted follow-up SI analysis on the 51 logins using sub tags (proposal: standard routing, 2h time box, no cap; brokering/signalFollow/arbitrageurs to STP, fastHedge to an SI book, Compass-good and dontBBook-only to the off book; about +$476k vs A-book, $16M peak; letting the classifier choose accounts would add about $1.9B of good flow). On the 5 Nov call Kama chose to park SI and get CFDs and futures live first, since new clients are arriving and they want to see that flow; they can go live later and review new tags in real time. Kama want FX and XAG flow sent to Velocity (tested 9 Nov, see lp-pool-expansion).
Next: SI parked by Kama; revisit once CFDs/futures are live; Moe to send the physical-hedger exclusion list if SI resumes; Kate to reply on reject rates (recommended: no number).
Refs: https://mahifx.slack.com/archives/C0B6FMU96G2/p1789482321712589 https://mahifx.slack.com/archives/C0B6FMU96G2/p1793275423756799 https://mahifx.slack.com/archives/C0B6FMU96G2/p1793877406602359 https://mahifx.slack.com/archives/C0B6FMU96G2/p1793883514943189

### cross-pricing-spreads — Direct cross pricing and spread control
status: open · since: 2026-10-29 · last: 2026-11-02
State: GBPNZD looked wider than Ali's provider (29 Oct) because crosses were triangulated from the wider SNGLDN driver spreads; on 29 Oct Kama asked to price crosses directly with Kama setting the level. On 2 Nov Kate went live with 19 directly priced crosses (JPY, AUD, NZD, CAD, CHF and EURSGD crosses; 19 total), uploaded to pricing.spreadprofile (12:11-15:24 UTC). Each cross has its own base spread per size tier and timezone, seeded from the last week of LP quotes; the widening factor applies only to triangulated crosses. Two non-dynamic floors (Benchmark Minimum Spread and Market Width Minimum Spread, factor 1) stop the price being tighter than the LPs; cutting base spreads below them shows no change. Hedging is unchanged and still goes through the drivers.
Next: Kama to tune base spreads and report crosses or sessions still flagged by clients; Kate to review the market-widening config if Kama wants tighter than the LP floor.
Refs: https://mahifx.slack.com/archives/C0B7T6S6D0C/p1793258682451549 https://mahifx.slack.com/archives/C0B7T6S6D0C/p1793640066486849

### roll-stp-rejects — Market order cancels over roll (no HFT-pool liquidity)
status: open · since: 2026-10-29 · last: 2026-10-30
State: On 29 Oct 21:33 UTC Ali reported market order rejections. Shyam explained they were cancels over the roll: all flow goes STP under the 'STP: Twighlight and Roll' execution rule and can only fill from the HFT pool (EDGEWATER_2_KS and SCOPE_TOXIC_KL), and neither LP had a price, so orders came back not marketable and expired. Shyam offered to make pricing go indicative when there is no LP liquidity; Ali declined on 30 Oct (not worth the risk) and asked whether twilight/roll STP is also set on the HFT channel (screenshot only, unanswered).
Next: Mahi to answer Ali's HFT twilight/roll STP question.
Refs: https://mahifx.slack.com/archives/C0B7T6S6D0C/p1793309589660289 https://mahifx.slack.com/archives/C0B7T6S6D0C/p1793341714371219

### rate-limit-rejects — RATE_LIMIT_EXCEEDED rejects on a rapid-fire A-book client
status: open · since: 2026-10-30 · last: 2026-10-30
State: On 30 Oct Ali showed a client's market orders rejected with REJECT_SYSTEM_ERROR RATE_LIMIT_EXCEEDED (counterparty sending consecutive trades, XAUUSD, via the Mahi_Nonskewed_A provider). Isaac explained these come from a per-counterparty throttle of 150 trades per second, set Compass-side and adjustable per counterparty on request. Internally Isaac noted the same counterparty is machine-gunning market orders that are brokered with no LR collected, and suggested turning on brokered liquidity reduction (distribution.liquidityThrottle.brokeredLiquidityReduction). No Kama reply on raising the threshold, and no decision on brokered LR is visible.
Next: Kama to say whether they want a higher per-counterparty throttle; Kate/Isaac to decide on brokered LR.
Refs: https://mahifx.slack.com/archives/C0B7T6S6D0C/p1793354921588429 https://mahifx.slack.com/archives/C0B6FMU96G2/p1793355181129629

### pilot-commercials — Pilot end and post-pilot terms
status: open · since: 2026-09-10 · last: 2026-10-29
State: Pilot ends 5 Nov (Will, 22 Oct). On the 29 Oct call Kama said they are happy to move ahead with the proposed terms (12-month volume-banded ladder from Moe's 2 Jun acceptance), either as an addendum or a new contract, and Mahi agreed to add futures and CFDs at no extra cost (billing is on volume, so this should raise volume). Nicole circulated a draft Compass Services Agreement at 22:22 UTC on 29 Oct: 3-month rolling term, CFDs and futures added to the pilot offerings, volume tiers in the fees section; she asked Will and Kate to check it matches their discussions (the 3-month term differs from the 12-month ladder discussed earlier). Open point: which flow counts toward the bands, since billing today counts CLIENTS and B_CLIENTS only, not Kama Securities MT5 flow or the new A/HFT books.
Next: Will and Kate to review Nicole's draft (term length, volume tiers) and then send to Moe; settle which flow counts toward bands; sign before 5 Nov.
Refs: https://mahifx.slack.com/archives/C0B6FMU96G2/p1789029069493129 https://mahifx.slack.com/archives/C0B6FMU96G2/p1793312572894189

### position-rec-nop — LP/client position reconciliation and NOP limits
status: open · since: 2026-10-02 · last: 2026-10-27
State: On 26-27 Oct Kate asked Kama for LP position snapshots over roll and at EOD; Jad said Kama's set-up cannot split positions into the Compass format, Kate said per-LP is enough since markets are grouped for NOP limits, and Jad sent the 27 Oct EOD file. Nathan compared it with Compass' roll snapshot: instruments missing from the file are flat at that LP (Jad confirmed; e.g. a -29k EURGBP adjustment), plus XPTUSD 86 at Scope; Nathan is applying the adjustments in Compass. Earlier unreconciled positions blocked the hedger (see nop-hedger-outage), so NOP limits were removed. Only apply NOP limits on reconciled positions.
Next: Nathan to finish the Compass position adjustments; Kama to keep sending per-LP snapshots at EOD; agree when NOP limits are re-applied.
Refs: https://mahifx.slack.com/archives/C0B7T6S6D0C/p1791557796452229 https://mahifx.slack.com/archives/C0B7T6S6D0C/p1793145150334519

### nop-hedger-outage — 19 Oct unhedged XAUUSD, SOR crash, VaR alerting
status: open · since: 2026-10-19 · last: 2026-10-21
State: From about 06:58 UTC on 19 Oct the hedger stopped clearing XAUUSD, most likely blocked by per-LP NOP limits running against unreconciled positions (Kama had posted positions in a thread, so they were missed); VaR hit about 146k (26,000oz unhedged) and Kama raised it at 07:31. At 07:35 Isaac deleted risk.nop.perPB to unblock the hedger; a missing null check crashed liquidityPoolSOR and the hybrid and arb hedgers, ten XAUUSD orders sat open 6-9 min and Kama's 180s timeout disabled Mahi as provider until about 07:51. Fix (null guard in MarketGroupTradePositionNOPTracker) is committed to release/26.4 and 26.3 but not yet deployed; until then do not delete NOP keys on Kama (set marketListNOPConfigs to [] or raise watermarks). All NOP limits were removed on Ali's request. Kate set a sustained critical-VaR alert and, on 21 Oct, a Kama notifications channel.
Next: Kama to send positions at EOD roll; Isaac to get the null-check fix deployed and raise whether bad non-trading config should keep the old config instead of killing processes; Kate to tune the VaR alert if noisy.
Refs: https://mahifx.slack.com/archives/C0B7T6S6D0C/p1792395096025849 https://mahifx.slack.com/archives/C0B6FMU96G2/p1792397763936839 https://mahifx.slack.com/archives/C0B7T6S6D0C/p1792572412812379

### lp-timeouts-pxm-unsub — LP latency and timeouts triggering PXM unsubscribes
status: open · since: 2026-09-15 · last: 2026-10-19
State: Recurring pattern: an order sitting unanswered trips PXM's firewall timeout and PXM unsubscribes XAUUSD on Kama's price sessions with no automatic resubscribe (15 Sep SOR restart; 2 Oct misconfigured MCC restart; 19 Oct, see nop-hedger-outage). On 19 Oct Kate recommended keeping the 180,000ms timeout and having PXM reject the client order on a pending-leg timeout while keeping the provider enabled; Moe says PXM disables the provider on timeout, Moe will ask PXM. Kate will give notice of planned restarts. Mahi: never resend an open order (double-fill risk); hardTimeoutLength can strand risk.
Next: Moe to ask PXM whether disable-on-timeout can be switched off for Kama; Mahi (rory) to confirm the PXM provider-disable behaviour; decide on hardTimeoutLength or asking LPs to reject after about 100ms.
Refs: https://mahifx.slack.com/archives/C0B6FMU96G2/p1791257314493849 https://mahifx.slack.com/archives/C0B7T6S6D0C/p1792409733558559

### brokered-flow-review — Brokered vs internalised flow review (internal)
status: open · since: 2026-10-16 · last: 2026-10-16
State: Kate's 9-16 Oct execution-quality review found most internalisable brokered flow is roll, twilight and Sunday/Monday open; roll/twilight brokered XAUUSD kept $14.2/M versus about $1.7/M if internalised, so brokering is right there. CP 100079_n/a was tagged arbitrageur then brokering 7-9 Oct, untagged before 12 Oct; now internalised on Catch-All at about -$71/M at 1m on $99M XAUUSD, watching for re-tag. 40874_30033000 is the only steady internalise candidate (about $1k/week), to watch a couple more weeks.
Next: Kate to finish instrument/timezone/CP breakdown; watch 100079_n/a re-tagging and 40874_30033000.
Refs: https://mahifx.slack.com/archives/C0B6FMU96G2/p1792160321472259 https://mahifx.slack.com/archives/C0B6FMU96G2/p1792165670366029

### xauusd-skew-signals — B Book XAUUSD skew tuning
status: open · since: 2026-10-08 · last: 2026-10-14
State: B Book XAUUSD skew was about -$0.35/M for 1-8 Oct because FI optimisation parties included CLIENTS_LDN (INSTI-priced, never skewed). Kate switched the skew signal to IFM, then limited optimisation parties to B_CLIENTS_LDN (8 Oct). Skew since was +$1.61/M over 9, 12 and 13 Oct (+$528 on $329M; early). On 14 Oct she moved the signal from IFM to flow-price-thresh (57.7% volume correct, $675 potential vs IFM 51.0%, $424).
Next: Kate to keep reviewing; a before/after backtest was planned.
Refs: https://mahifx.slack.com/archives/C0B6FMU96G2/p1791471223806789 https://mahifx.slack.com/archives/C0B6FMU96G2/p1791965822602239

### weekend-risk-carry — Friday close hedging did not clear risk
status: open · since: 2026-10-12 · last: 2026-10-13
State: Compass book carried risk over the 9-10 Oct weekend (about $23k PnL bump on open). Cause: a Broker First top-up just before close (the unfilled 280oz of client 43795's 1,000oz sell at 20:56 UTC) could not be hedged because LP liquidity had dried up; Friday_Close tried and got no fill, and the hedger sold the 280oz at Sunday's open (22:01-22:02 UTC). The weekly hybrid-diagnostic missed dormant rules. Kama prefer Broker First to avoid cancels and client rebate claims (Moe does not want to pass cancels to LPs). On 15 Oct Moe set twilight and roll flow to Broker.
Next: Shyam's PR (MahiProduct #126) adding dormant-rule and weekend-carry checks awaits Will's approval; Kate to find a way to avoid carry without day-specific execution rules; check the 16 Oct Friday close to see whether twilight Broker removes the carry.
Refs: https://mahifx.slack.com/archives/C0B6FMU96G2/p1791798684555499

### fx-hedge-swaps — Hedging crosses in drivers vs swap cost
status: watching · since: 2026-10-09 · last: 2026-10-09
State: Moe says Kama loses on swaps because Compass hedges crosses in the drivers (EURJPY example) and wants hedging in the same currency as the client trade. Kate pushed back (drivers avoid the cross spread; only a loss if risk is held several nights). Peer data: Kama's FX major and JPY swap points are about half the network median, while gold swap is second widest. Moe agreed to inventory-skewed swaps (feasible: the analytics bridge saves swap points daily); Mahmoud (swap sync tool) is on holiday and will do it on return.
Next: Parked while Mahmoud is away (no activity since 9 Oct). Kate to raise swap skewing with Moe; follow up when Mahmoud is back.
Refs: https://mahifx.slack.com/archives/C0B6FMU96G2/p1791544461594299

### xpd-pricing — XPDUSD price jumps between LP levels
status: watching · since: 2026-10-09 · last: 2026-10-09
State: XPDUSD published mid jumped between two LP price levels 10-40bp apart (worst 8 Oct). Kate changed reference.referencePriceMarketSelectors so XPD prices off SCOPE_KL only, applied at weekend restarts. No PnL impact so far (140 XPD fills, about $28M since 8 Sep).
Next: Check XPD price variation after the weekend restart.
Refs: https://mahifx.slack.com/archives/C0B6FMU96G2/p1791557308635619

### beeks-multicast — Beeks multicast/IGMP issue and false PnL alerts
status: watching · since: 2026-09-28 · last: 2026-10-07
State: Outdated reference mid prices caused false PnL-drop pager alerts on Kama; tied to a Beeks multicast issue (Zendesk 23343, Beeks NOCINT-839427). On 30 Sep Beeks said enabling IGMP snooping mitigated storm control, that it is still investigating blackholing on an LD5 distribution switch (servers cannot see the querier), and that Mahi should take no action and leave its test scripts in place. Liam sent a chaser on 7 Oct asking for an ETA; no Beeks answer is visible since; no Kama-side impact seen since, so downgraded to watching.
Next: Liam/Inald to chase Beeks for a fix ETA.
Refs: https://mahifx.slack.com/archives/C0B6FMU96G2/p1790597791892939 https://mahifx.slack.com/archives/C0B6FMU96G2/p1791364219575089

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

### compass-login-error — Jad hit a Compass login error
status: closed · since: 2026-10-26 · last: 2026-10-28 · closed: 2026-11-11
State: Jad's 26 Oct login error; Justin pushed a fix on 28 Oct. No further reports; assumed resolved.
Next: Confirm Jad can log in after Justin's fix.
Refs: https://mahifx.slack.com/archives/C0B7T6S6D0C/p1792976237806039 https://mahifx.slack.com/archives/C0B7T6S6D0C/p1793169011218019

### hft-fx-pricing — HFT channel FX spreads and pool coverage
status: closed · since: 2026-10-20 · last: 2026-10-28 · closed: 2026-11-11
State: Wide HFT FX spreads (20-21 Oct) fixed by design: dedicated pricing model CLIENT_PRICE_HFT_LDN with editable base spreads, published by the HFT connections after the 28 Oct EOD restarts; Ali confirmed. No complaints since.
Next: Watch HFT FX spreads after the switch to CLIENT_PRICE_HFT_LDN; add remaining instruments to the HFT pool if still needed.
Refs: https://mahifx.slack.com/archives/C0B7T6S6D0C/p1792484649892479 https://mahifx.slack.com/archives/C0B7T6S6D0C/p1793196612192619

### xau-open-rejects — XAUUSD market-open rejects on B book
status: closed · since: 2026-10-23 · last: 2026-10-23 · closed: 2026-11-11
State: Ali's 23 Oct screenshot of rejected XAUUSD orders at the open on the B book; Isaac saw no B-book cancels and asked for the 012* order ID. No logs since; no activity since 23 Oct, assumed resolved.
Next: Ali to send logs / order IDs; Isaac to diagnose.
Refs: https://mahifx.slack.com/archives/C0B7T6S6D0C/p1792735564284869 https://mahifx.slack.com/archives/C0B7T6S6D0C/p1792743155724969

### eurgbp-rejects — Market rejections on EURGBP
status: closed · since: 2026-10-21 · last: 2026-10-21 · closed: 2026-11-11
State: Ali's 21 Oct screenshot of EURGBP market rejections; no reply or follow-up since; assumed resolved.
Next: Mahi to diagnose and reply.
Refs: https://mahifx.slack.com/archives/C0B7T6S6D0C/p1792566675726999

### mas-xau-removal — MAS Markets pulled (XAUUSD 16 Oct, whole LP 21 Oct)
status: closed · since: 2026-10-16 · last: 2026-10-21 · closed: 2026-11-06
State: MAS removed from XAUUSD hedging 16 Oct (rejecting market orders); Kama closed the account 21 Oct and Isaac disabled MAS from all pools and hedging. No activity since.
Refs: https://mahifx.slack.com/archives/C0B7T6S6D0C/p1792154269472349 https://mahifx.slack.com/archives/C0B7T6S6D0C/p1792586254793539
## Arc
- 2026-06-02 — Deal accepted; pilot agreement signed 2026-06-08
- 2026-08-05 — B Book flow live on Compass (pricing and execution)
- 2026-09-14 — Risk-management go-live (A Book), interrupted and restored 17-23 Sep
- 2026-09-23 — Kama Securities MT5 A/B flow routed to Compass
- 2026-09-29 — Almost all Kama connectors routed to Compass; HFT clients added; VaR raised to 2,000
