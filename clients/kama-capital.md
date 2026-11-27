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
last_catchup: 2026-11-27T08:13:31Z
status: active
---

## Now
Live Compass-managed A Book on XAUUSD (plus HFT and Kama Securities flow); pilot ended 5 Nov and Kama signed the new terms (3-month rolling, volume tiers, futures/CFDs at no extra cost) on 20 Nov. SI parked by Kama (5 Nov) to get CFDs and futures live first: futures in the client DB since 6 Nov (verification due 10 Nov, no result seen), Velocity live in the hedger for FX/XAG/oil, Kama quantity limits applied and test trades passed 12 Nov; on 18 Nov CFD test trades on the skewed, non-skewed and HFT feeds routed correctly and futures tests are next. All markups removed 6 Nov. Open: FX Edge fill delays, GBPCAD/EURGBP rejects, NOP null-check fix deploy, PXM timeout handling.

## Streams

### futures-cfd-onboarding — Futures and CFDs added to Kama's Compass
status: open · since: 2026-10-29 · last: 2026-11-25
State: Kama want futures and CFDs live (added to the contract at no extra cost, see pilot-commercials). Kate set up indices on the pricing model and subscription mappings (5 Nov). On 6 Nov Inald put the new futures (8 families, 52 contracts) into the client DB under CHG-2611-X9VR (approved by Liam), implemented 7 Nov, verification due 10 Nov (no result seen). William staged CHG-2611-G9MP (CFD book, hedger, channel setup, no client routing) on 9 Nov and CHG-2611-0KWV (futures books, hedgers, channels; approved 10 Nov). Main LP for CFDs except oil is Velocity. Kama will not use new instruments for XAUUSD until indices, oil and futures are live. On 12 Nov Kate applied Kama's quantity limits and sent test trades (8 futures families on Scope KL, spot index CFDs, VELOCITY_KL oil CFDs); Ali said all fine. Open: Kate asked what decimal places Kama prices futures/CFDs to (unanswered); Ali will give a day's notice of new futures expiries; the UKOFUT-F dash test trade errored 'Cannot convert from CO1 to USD' (needs adding to a pricer process, internal). On 16 Nov Kate asked whether HFT CFD flow should hedge to SCOPE or SCOPE_TOXIC: Ali said US/UK oil hedges with Velocity, futures and spot indices to Scope, and HFT FX used to go to Scope too (small volume). On 17 Nov Ali asked whether to start pricing CFDs; Kate asked him not to switch to Mahi pricing yet (final items on Mahi's side), then said one more distribution process restart is needed before tests. Contract sizes: Mahi's unit is 1 barrel (UKOIL/USOIL), 1 oz (GC/SI), 1 index unit (US30/US500/UT100/DAX30); Ali confirmed Kama's oil lot is 1,000 barrels and index CFDs are 1, min 10 barrels = 0.01 lots, so quantities reach Mahi in barrels/index units and Kate's min/step config matches; Kate will check fill sizes on the test trades. Ali was getting CFD quotes and will confirm the full symbol list on 18 Nov. On 17 Nov Kate removed the MCC rules routing toxic A-book flow to a default channel and added an MCC for CFDs/futures. On 18 Nov Ali confirmed Kama were receiving CFD prices; Kate asked for CFD and futures test trades, changed execution rules for testing (12:08 UTC) and asked for more on the skewed, non-skewed and HFT feeds; Ali sent them (12:06 and 12:44 UTC, one batch to the non-skewed provider like normal FX/gold) and Kate confirmed at 13:43 UTC that the CFD trades on all three feeds came through on the correct channels. She asked Ali for feedback on CFD spreads/instruments and for futures test trades on each feed; Ali will check the futures and revert. Kate made many CFD hedger profile edits 15:13-16:45 UTC; hybridHedgerCFD1 alerted on a duplicate hedging rule (CL1USD, Friday close time guard) at 16:10 UTC (no resolution visible). Internally (18 Nov) Will asked whether the HFT flow hedges to Edgewater; Kate said yes, and that Moe wants no back-and-forth of flow with Velocity (Kama send Velocity FX and XAG and receive its XAU), Will noting IB relationships often set up maker plus taker directions; Kate will check. On 19 Nov 11:26 UTC Kate asked whether Kama are happy to start routing CFD flow to Mahi that day; Ali said he will get back soon (no answer yet). On 23 Nov 01:17 UTC Daria updated hedging.expectedBookStatusOnTimeZones on Kama so the expected status matches actual for hybridHedgerCFD1 and asked Kate to check it. On 23 Nov 09:11 UTC Kate asked Kama to say when they are ready to route CFD flow to Mahi; Moe replied at 10:10 UTC that Kama are discussing internally. Kama's execution rules (distribution.executionRules) were edited via the admin server at 16:23 UTC (config-updates bot). On 24 Nov 11:37 UTC Ali edited pricing.spreadprofile via the admin server (content not visible). On 25 Nov 06:56 UTC Ali said Kama might add FX Edge for the spot indices alongside Scope and asked whether test trades were done on that connection; Shyam said Kate would be online shortly (no answer yet).
Next: Kate to answer Ali on FX Edge test trades for spot indices; Moe/Ali to say when CFD flow routing starts (Kama discussing internally), send futures test trades on each feed and give CFD spread feedback; Kate to check the Velocity two-way flow question, resolve the CL1USD duplicate-rule alert, fix the CO1 to USD pricer-process error and get the dp answer; Inald to finish verification (CHG-2611-X9VR); Kate/William to finish CFD and futures books and hedgers (CHG-2611-G9MP, CHG-2611-0KWV), apply Kama's quantity limits, then enable client routing.
Refs: https://mahifx.slack.com/archives/C0B7T6S6D0C/p1793283834284999 https://mahifx.slack.com/archives/C0B7T6S6D0C/p1794484184431989 https://mahifx.slack.com/archives/C0B7T6S6D0C/p1795087595740039 https://mahifx.slack.com/archives/C0B7T6S6D0C/p1795589782952099

### slippage-gold-drop — Kama query on gold sell slippage in a sharp drop
status: open · since: 2026-11-25 · last: 2026-11-25
State: On 25 Nov Ali asked Mahi to check slippage on a set of XAUUSD sells (screenshot only). Kate found all were during a ~$23 drop in 30s at 11:58:47-11:59:16 UTC. MT5 market orders fill at the better of start or end of a short last-look window; most filled at or near arrival bid, the two at 11:58:48 filled $1.30-1.50 lower. The requested prices were Mahi's bid 120-180ms before arrival while the Kama-bridge round trip is a few ms, so she suspects a delay between Mahi price reaching MT5 and the order reaching the bridge and is checking Mahi's side too. A-book orders went straight to FX Edge, held 670-800ms and filled $1.40-1.90 below arrival; a further $0.50-0.90 was liquidity reduction, applied to orders passed to the market since 19 Nov.
Next: Ali to send MT5 order times and bridge quote-receipt times; Ali to say whether LR should be on for A-book flow; Kama to raise the FX Edge hold; Kate to check Mahi's side.
Refs: https://mahifx.slack.com/archives/C0B7T6S6D0C/p1795611790972399 https://mahifx.slack.com/archives/C0B7T6S6D0C/p1795627379373449

### fxedge-delays — FX Edge fill delays and cancels via PXM
status: open · since: 2026-11-05 · last: 2026-11-25
State: On 5 Nov Daria asked Kama to check with PXM why order 012drb34aa (GBPNZD, bound for FXEDGE_KL) was acked at once but took 12s to fill, and offered to pull FX Edge from the pool meanwhile; Ali said Kama has issues with orders going to FX Edge and saw high execution times on the Non skewed A provider (quote blocked and max exposure reached on FX Edge). Daria's read of order 4964712: the SOR split it across FX Edge, Scope and Edgewater; FX Edge delayed and cancelled while the SOR kept retrying it until the order was refilled elsewhere; no Compass-side speed issue seen. Ali asked how long the SOR keeps retrying one provider and how that process works; Cameron Hughes said he will gather details. On 25 Nov Kate found A-book orders passed straight to FX Edge were held 670-800ms (usually about 10ms) before filling, and said to raise it with FX Edge (see slippage-gold-drop). No decision yet on removing FX Edge from the pool.
Next: Kama to raise the 670-800ms hold with FX Edge; Cameron Hughes to answer Ali on SOR retry behaviour; Kama to check FX Edge/PXM side; decide whether to pull FX Edge from the pool.
Refs: https://mahifx.slack.com/archives/C0B7T6S6D0C/p1793859648388519 https://mahifx.slack.com/archives/C0B7T6S6D0C/p1795627379373449

### rate-limit-rejects — RATE_LIMIT_EXCEEDED rejects on a rapid-fire A-book client
status: open · since: 2026-10-30 · last: 2026-11-25
State: On 30 Oct Ali showed a client's market orders rejected with REJECT_SYSTEM_ERROR RATE_LIMIT_EXCEEDED (counterparty sending consecutive trades, XAUUSD, via the Mahi_Nonskewed_A provider). Isaac explained these come from a per-counterparty throttle of 150 trades per second, set Compass-side and adjustable per counterparty on request. Internally Isaac noted the same counterparty is machine-gunning market orders that are brokered with no LR collected, and suggested turning on brokered liquidity reduction (distribution.liquidityThrottle.brokeredLiquidityReduction). No Kama reply on raising the threshold, and On 19 Nov 09:50 UTC Kate edited distribution.liquidityThrottle.brokeredLiquidityReduction on Kama (content not visible; possibly acting on Isaac's suggestion), and edited liquidityRefreshProfiles.perchannel at 10:30 and 11:35 UTC.
On 25 Nov 17:12 UTC Kate edited distribution.liquidityThrottle.brokeredLiquidityReduction again (content not visible).
Next: Kama to say whether they want a higher per-counterparty throttle; Kate/Isaac to decide on brokered LR.
Refs: https://mahifx.slack.com/archives/C0B7T6S6D0C/p1793354921588429 https://mahifx.slack.com/archives/C0C1L6G37HN/p1795626757877579

### xau-execution-style — Broker vs Broker First, HFT book and markup
status: open · since: 2026-09-21 · last: 2026-11-13
State: A 21 Sep cancel burst led to Kama moving all A_CLIENTS to Broker First (29 Sep). HFT flow got its own book and hedgers (30 Sep); markups of $20/M HFT and $10/M A Book internalised flow were agreed 1 Oct and set via MultiChannelConfig 2 Oct. On 17 Nov Kate removed the MCC rules routing toxic A-book flow to a default channel (Broker First no longer set). On 30 Sep Kate asked Kama to turn off PXM sweep/boost so each A-book order arrives whole; Ali was confirming with PXM and no outcome is visible. On 15 Oct Kama asked for Broker (not Broker First) over high-impact news; Moe set twilight and roll flow to Broker. Execution rules cannot be day-specific; a bare '*' in counterparty criteria matches none. On 21 Oct FOK orders (21:00-23:00 UTC) expired as no HFT-channel LP accepted FOK; Kate set reference.marketSupport.FOK across the board. Kama staff edited distribution.executionRules repeatedly (22 Oct to 13 Nov; content not visible). The agreed $20/M and $10/M markups were removed on 6 Nov (see markup-removal).
Next: Mahi to confirm whether news criteria can be added to execution rules.
Refs: https://mahifx.slack.com/archives/C0B7T6S6D0C/p1790009143944299 https://mahifx.slack.com/archives/C0C1L6G37HN/p1793098819391439 https://mahifx.slack.com/archives/C0C1L6G37HN/p1794578047239229

### lp-pool-expansion — LP pool and hedging markets, KL/KS connectors
status: open · since: 2026-09-21 · last: 2026-11-09
State: Pool started as Scope only; FXEdge and Arts joined after test trades (5-6 Oct), Arts was pulled for latency. On 14-15 Oct Star and Velocity were added; Moe's final list: LIQUIDITY_POOL_HFT_LDN = Edgewater_2_KS, MAS_Toxic_KS, Scope_Toxic_KL; LIQUIDITY_POOL_LDN = Edgewater_2_KS, Scope_KL, MAS_KS, FX_EDGE_KL. Kate suggested spreading load across KL and KS connectors. Fusion, Arts and Star are subscribed but not in the pools. Removing a market from a pool is dynamic; adding one needs a restart (EOD, or intraday on request).  MAS Markets was removed from all pools on 21 Oct (see mas-xau-removal). On 9 Nov Ali asked to test Velocity (FX only for now; not to be used for XAUUSD until CFDs/futures are live). Kate's EURUSD and XAGUSD test trades filled on Velocity (XAG KL price fixed on Ali's side); Kate then put Velocity in the hedger for FX and XAG, pool addition taking effect at EOD restarts.
Next: Kate to confirm Velocity is in the LDN pool after the EOD restart; Ali to flag when Star is ready for test trades.
Refs: https://mahifx.slack.com/archives/C0B7T6S6D0C/p1789990153651149 https://mahifx.slack.com/archives/C0B7T6S6D0C/p1794219913020909

### markup-removal — Moe orders all markups removed
status: open · since: 2026-11-06 · last: 2026-11-06
State: On 6 Nov Moe told Kate to remove any markup on the system, saying nothing like this should happen without Kama approving it and that Kama only marks up its own clients; Kate removed all internalise and broker markups (markupProfiles edits 12:45-12:52 UTC). Kate explained the internalisation markup (agreed 1-2 Oct) also hit brokered trades, since brokered fills peg to the channel price. Moe and Ali acknowledged; HFT and A-book internalised flow now carries no markup, which may affect the A/HFT economics in the SI and pilot-commercials discussions.
Next: Kama to confirm any markup they do want, via explicit approval.
Refs: https://mahifx.slack.com/archives/C0B7T6S6D0C/p1793969043880159 https://mahifx.slack.com/archives/C0B7T6S6D0C/p1793970050098779

### gbpcad-quote-block — GBPCAD rejects at market open (quote blocked)
status: open · since: 2026-11-06 · last: 2026-11-06
State: On 6 Nov Ali asked Mahi to check the reject reasons on GBPCAD at the market open the night before: Kama's logs show quote blocked and he thinks Scope was not quoting then (screenshot only). No reply yet.
Next: Mahi to diagnose and reply.
Refs: https://mahifx.slack.com/archives/C0B7T6S6D0C/p1793948581789389

### si-and-risk-golive — Risk-management go-live and SI
status: open · since: 2026-09-15 · last: 2026-11-05
State: Risk go-live began 2026-09-14 but the first A Book client switched off after a position-rec scare and an SOR restart that tripped PXM's firewall; flow came back 17-23 Sep. Mahi view (Andrew, Will): flow with Kama in aggregation (e.g. Star, tag 42060) is not SI material. Kate's SI sims (22-26 Oct) on Kama's XAUUSD drop copy: Compass-good flow beat A-booking by about $400k but other flow did not reliably, and the gain leaned on four HFT-routed logins and tag 42060. On the 29 Oct call Kama were disappointed; Kate said hardly any accounts are round-trip, so Mahi is likely in aggregation. Kama wanted their own tags and to exclude a few physical gold hedgers (Moe to send list). Kama also wants to add 26degrees and ISAM and asked for anonymised reject-rate data from other clients; Kate recommends giving no figure and offering to measure on Kama's own flow (no sign it was sent). On 5 Nov Kate posted follow-up SI analysis on the 51 logins using sub tags (proposal: 2h time box, no cap; about +$476k vs A-book, $16M peak). On the 5 Nov call Kama chose to park SI and get CFDs and futures live first, since new clients are arriving and they want to see that flow; they can go live later and review new tags in real time. Kama want FX and XAG flow sent to Velocity (tested 9 Nov, see lp-pool-expansion).
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

### position-rec-nop — LP/client position reconciliation and NOP limits
status: open · since: 2026-10-02 · last: 2026-10-27
State: On 26-27 Oct Kate asked Kama for LP position snapshots over roll and at EOD; Jad said Kama's set-up cannot split positions into the Compass format, Kate said per-LP is enough since markets are grouped for NOP limits, and Jad sent the 27 Oct EOD file. Nathan compared it with Compass' roll snapshot: instruments missing from the file are flat at that LP (Jad confirmed; e.g. a -29k EURGBP adjustment), plus XPTUSD 86 at Scope; Nathan is applying the adjustments in Compass. Unreconciled positions earlier blocked the hedger (see nop-hedger-outage), so NOP limits were removed. Only apply NOP limits on reconciled positions.
Next: Nathan to finish the Compass position adjustments; Kama to keep sending per-LP snapshots at EOD; agree when NOP limits are re-applied.
Refs: https://mahifx.slack.com/archives/C0B7T6S6D0C/p1791557796452229 https://mahifx.slack.com/archives/C0B7T6S6D0C/p1793145150334519

### nop-hedger-outage — 19 Oct unhedged XAUUSD, SOR crash, VaR alerting
status: watching · since: 2026-10-19 · last: 2026-10-21
State: From about 06:58 UTC on 19 Oct the hedger stopped clearing XAUUSD, most likely blocked by per-LP NOP limits running against unreconciled positions (Kama had posted positions in a thread, so they were missed); VaR hit about 146k (26,000oz unhedged) and Kama raised it at 07:31. At 07:35 Isaac deleted risk.nop.perPB to unblock the hedger; a missing null check crashed liquidityPoolSOR and the hybrid and arb hedgers, ten XAUUSD orders sat open 6-9 min and Kama's 180s timeout disabled Mahi as provider until about 07:51. Fix (null guard in MarketGroupTradePositionNOPTracker) is on release/26.4 and 26.3, not yet deployed; until then do not delete NOP keys on Kama (set marketListNOPConfigs to [] or raise watermarks). All NOP limits were removed on Ali's request. Kate set a sustained critical-VaR alert and, on 21 Oct, a Kama notifications channel.
Next: Downgraded to watching (no activity since 21 Oct). Kama to send positions at EOD roll; Isaac to get the null-check fix deployed and raise whether bad non-trading config should keep the old config instead of killing processes; Kate to tune the VaR alert if noisy.
Refs: https://mahifx.slack.com/archives/C0B7T6S6D0C/p1792395096025849 https://mahifx.slack.com/archives/C0B6FMU96G2/p1792397763936839 https://mahifx.slack.com/archives/C0B7T6S6D0C/p1792572412812379

### lp-timeouts-pxm-unsub — LP latency and timeouts triggering PXM unsubscribes
status: watching · since: 2026-09-15 · last: 2026-10-19
State: Recurring pattern: an order sitting unanswered trips PXM's firewall timeout and PXM unsubscribes XAUUSD on Kama's price sessions with no automatic resubscribe (15 Sep SOR restart; 2 Oct misconfigured MCC restart; 19 Oct, see nop-hedger-outage). On 19 Oct Kate recommended keeping the 180,000ms timeout and having PXM reject the client order on a pending-leg timeout while keeping the provider enabled; Moe says PXM disables the provider on timeout, Moe will ask PXM. Kate will give notice of planned restarts. Mahi: never resend an open order (double-fill risk); hardTimeoutLength can strand risk.
Next: Downgraded to watching (no activity since 19 Oct). Moe to ask PXM whether disable-on-timeout can be switched off for Kama; Mahi (rory) to confirm the PXM provider-disable behaviour; decide on hardTimeoutLength or asking LPs to reject after about 100ms.
Refs: https://mahifx.slack.com/archives/C0B6FMU96G2/p1791257314493849 https://mahifx.slack.com/archives/C0B7T6S6D0C/p1792409733558559

### brokered-flow-review — Brokered vs internalised flow review (internal)
status: watching · since: 2026-10-16 · last: 2026-10-16
State: Kate's 9-16 Oct review found internalisable brokered flow is mostly roll, twilight and weekend open; roll/twilight brokered XAUUSD kept $14.2/M versus about $1.7/M if internalised, so brokering is right there. CP 100079_n/a was tagged arbitrageur then brokering 7-9 Oct, untagged before 12 Oct; now internalised on Catch-All at about -$71/M at 1m on $99M XAUUSD, watching for re-tag. 40874_30033000 is the only steady internalise candidate (about $1k/week), to watch a couple more weeks.
Next: Downgraded to watching (no activity since 16 Oct). Kate to finish instrument/timezone/CP breakdown; watch 100079_n/a re-tagging and 40874_30033000.
Refs: https://mahifx.slack.com/archives/C0B6FMU96G2/p1792160321472259 https://mahifx.slack.com/archives/C0B6FMU96G2/p1792165670366029

### xauusd-skew-signals — B Book XAUUSD skew tuning
status: watching · since: 2026-10-08 · last: 2026-10-14
State: B Book XAUUSD skew was about -$0.35/M for 1-8 Oct because FI optimisation parties included CLIENTS_LDN (INSTI-priced, never skewed). Kate switched the skew signal to IFM, then limited optimisation parties to B_CLIENTS_LDN (8 Oct). Skew since was +$1.61/M over 9, 12 and 13 Oct (+$528 on $329M; early). On 14 Oct she moved the signal from IFM to flow-price-thresh (57.7% volume correct, $675 potential vs IFM 51.0%, $424).
Next: Downgraded to watching (no activity since 14 Oct). Kate to keep reviewing; a before/after backtest was planned.
Refs: https://mahifx.slack.com/archives/C0B6FMU96G2/p1791471223806789 https://mahifx.slack.com/archives/C0B6FMU96G2/p1791965822602239

### weekend-risk-carry — Friday close hedging did not clear risk
status: watching · since: 2026-10-12 · last: 2026-10-13
State: Compass book carried risk over the 9-10 Oct weekend (about $23k PnL bump on open). Cause: a Broker First top-up just before close (the unfilled 280oz of client 43795's 1,000oz sell at 20:56 UTC) could not be hedged because LP liquidity had dried up; Friday_Close tried and got no fill, and the hedger sold the 280oz at Sunday's open (22:01-22:02 UTC). The weekly hybrid-diagnostic missed dormant rules. Kama prefer Broker First to avoid cancels and client rebate claims (Moe does not want to pass cancels to LPs). On 15 Oct Moe set twilight and roll flow to Broker.
Next: Downgraded to watching (no activity since 13 Oct). Shyam's PR (MahiProduct #126) adding dormant-rule and weekend-carry checks awaits Will's approval; Kate to find a way to avoid carry without day-specific execution rules; check the 16 Oct Friday close to see whether twilight Broker removes the carry.
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

### pilot-commercials — Pilot end and post-pilot terms
status: closed · since: 2026-09-10 · last: 2026-11-20 · closed: 2026-11-23
State: Kama signed the new post-pilot terms on 20 Nov, 11 minutes after receipt (Bonnie, internal). Terms were the draft Compass Services Agreement (3-month rolling, volume tiers, futures and CFDs at no extra cost). Whether Kama Securities MT5 and the new A/HFT books count toward the bands was not visible in Slack.
Refs: https://mahifx.slack.com/archives/C0B6FMU96G2/p1789029069493129 https://mahifx.slack.com/archives/C0B6FMU96G2/p1795166660229179

## Arc
- 2026-06-02 — Deal accepted; pilot agreement signed 2026-06-08
- 2026-08-05 — B Book flow live on Compass (pricing and execution)
- 2026-09-14 — Risk-management go-live (A Book), interrupted and restored 17-23 Sep
- 2026-09-23 — Kama Securities MT5 A/B flow routed to Compass
- 2026-09-29 — Almost all Kama connectors routed to Compass; HFT clients added; VaR raised to 2,000
- 2026-11-20 — Kama signed post-pilot terms
