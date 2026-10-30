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
last_catchup: 2026-10-30T07:21:41Z
status: active
---

## Now
Live Compass-managed A Book on XAUUSD (plus HFT and Kama Securities flow), expanding to crosses, futures and CFDs. On the 29 Oct call Kama agreed the post-pilot terms (pilot ends 5 Nov); Nicole's draft contract (3-month rolling, volume tiers, futures/CFDs at no extra cost) awaits Will and Kate. Kama want to go ahead with SI on their own 51 tags and ask Mahi to flag bad subtags (Kate re-running sims); Kate is the day-to-day owner, Moe drives client-side changes. Roll cancels on 29 Oct came from no HFT-pool liquidity (Ali declined indicative pricing). Still open: NOP/hedger null-check fix deploy, EURGBP rejects, PXM timeout handling, Friday-close risk carry.

## Streams

### roll-stp-rejects — Market order cancels over roll (no HFT-pool liquidity)
status: open · since: 2026-10-29 · last: 2026-10-30
State: On 29 Oct 21:33 UTC Ali reported market order rejections. Shyam explained they were cancels over the roll: all flow goes STP under the 'STP: Twighlight and Roll' execution rule and can only fill from the HFT pool (EDGEWATER_2_KS and SCOPE_TOXIC_KL), and neither LP had a price, so orders came back not marketable and expired. Shyam offered to make pricing go indicative when there is no LP liquidity; Ali declined on 30 Oct (not worth the risk) and asked whether twilight/roll STP is also set on the HFT channel (screenshot only, unanswered).
Next: Mahi to answer Ali's HFT twilight/roll STP question.
Refs: https://mahifx.slack.com/archives/C0B7T6S6D0C/p1793309589660289 https://mahifx.slack.com/archives/C0B7T6S6D0C/p1793341714371219

### cross-pricing-spreads — GBPNZD cross wider than provider, timezone spread config
status: open · since: 2026-10-29 · last: 2026-10-29
State: Ali saw GBPNZD about 60s versus about 30s at his provider. Kate found it was the SNGLDN timezone: drivers' base spreads there are wider and crosses are triangulated from them, while Ali was editing the LDN timezone config; once the session moved to LDN the cross returned in line with the LPs at factor 1. Ali asked how to edit factors; Kate explained the widening factor box and switching timezone at the top of the page. On the 29 Oct call Kama also asked to price crosses directly like the drivers, for more spread flexibility; Ali edited pricing.spreadprofile at 07:57 UTC.
Next: Kate to set up direct cross pricing; consider adjusting the SNGLDN factor.
Refs: https://mahifx.slack.com/archives/C0B7T6S6D0C/p1793258682451549 https://mahifx.slack.com/archives/C0B7T6S6D0C/p1793259683402669

### futures-cfd-onboarding — Futures and CFDs added to Kama's Compass
status: open · since: 2026-10-29 · last: 2026-10-29
State: Kama want futures and CFDs live. Kate set up a handful of indices on the pricing model and will set up books and hedgers; on 29 Oct she asked for instrument mappings and Ali listed the Z26/F27 contracts (DAX30, US100, US30, SI, USOIL, UKOIL) and said he will enable them on Mahi's connection so LP market data can be subscribed. Added to the contract at no extra cost (see pilot-commercials).
Next: Kate to subscribe LP market data and set up books and hedgers.
Refs: https://mahifx.slack.com/archives/C0B7T6S6D0C/p1793283834284999 https://mahifx.slack.com/archives/C0B7T6S6D0C/p1793284336627129

### pilot-commercials — Pilot end and post-pilot terms
status: open · since: 2026-09-10 · last: 2026-10-29
State: Pilot ends 5 Nov (Will, 22 Oct). On the 29 Oct call Kama said they are happy to move ahead with the proposed terms (12-month volume-banded ladder from Moe's 2 Jun acceptance), either as an addendum or a new contract, and Mahi agreed to add futures and CFDs at no extra cost (billing is on volume, so this should raise volume). Nicole circulated a draft Compass Services Agreement at 22:22 UTC on 29 Oct: 3-month rolling term, CFDs and futures added to the pilot offerings, volume tiers in the fees section; she asked Will and Kate to check it matches their discussions (the 3-month term differs from the 12-month ladder discussed earlier). Open point: which flow counts toward the bands, since billing today counts CLIENTS and B_CLIENTS only, not Kama Securities MT5 flow or the new A/HFT books.
Next: Will and Kate to review Nicole's draft (term length, volume tiers) and then send to Moe; settle which flow counts toward bands; sign before 5 Nov.
Refs: https://mahifx.slack.com/archives/C0B6FMU96G2/p1789029069493129 https://mahifx.slack.com/archives/C0B6FMU96G2/p1793312572894189

### si-and-risk-golive — Risk-management go-live and SI
status: open · since: 2026-09-15 · last: 2026-10-29
State: Risk go-live began 2026-09-14 but the first A Book client switched off after a position-rec scare and an SOR restart that tripped PXM's firewall; flow came back 17-23 Sep. Early SI sims on Moe's tag cohort were weak. Mahi view (Andrew, Will): flow with Kama in aggregation (e.g. Star, tag 42060) is not SI material. On the 8 Oct call Kama wanted SI soon and supplied a list of tags; Kate ran sims on those tags and the full portfolio; on 22 Oct she walked Kama through the results on the weekly call, and on 26 Oct posted the written SI sim write-up and proposal in the client channel. Sims ran on Kama's XAUUSD drop copy 15 Jul-14 Oct (A and HFT flow only): Compass-good flow (17 logins, $2.7B) with a 2-3h window and no cap beat A-booking by about $400k and was ahead every month, while short-horizon and long/toxic flow did not beat it reliably. Of Kama's own 51-login list, 34 ($23.0B) were in scope and the gain leaned on four HFT-routed logins and tag 42060, so Mahi proposes letting Compass's classification pick the logins rather than a fixed list. Proposal: (1) go live with an SI book on the Compass-good flow, everything else stays A-book/STP; (2) next, a separate execution channel with a markup, filling currently brokered flow at the pool price and hedging within seconds. Moe asked on 26 Oct whether the 1h window was tried; Kate added those results to the doc. On the 29 Oct call Kama were disappointed the sims suggested something different from what they expected (they wanted to know which subtags of their tag list to exclude); Kate explained the sims use round-trip info and the classifier and hardly any of their accounts are round-trip, so they likely have Mahi in aggregation. Kama want to go ahead with their own tags and have Mahi pick out the bad subtags, plus exclude a few physical gold hedgers (Moe to send the list); Kate will re-run the sims on the 51 tags with that in mind. Kama also wants to add 26degrees and ISAM and asked for anonymised reject-rate data from other clients; Kate recommends giving no figure and offering to measure on Kama's own flow (no sign it was sent).
Next: Kate to re-run sims on the 51 tags to flag bad subtags; Moe to send the physical-hedger exclusion list; Kate to reply on reject rates (recommended: no number).
Refs: https://mahifx.slack.com/archives/C0B6FMU96G2/p1789482321712589 https://mahifx.slack.com/archives/C0B6FMU96G2/p1793275423756799

### compass-login-error — Jad hit a Compass login error
status: open · since: 2026-10-26 · last: 2026-10-28
State: At 00:57 UTC on 26 Oct Jad posted a screenshot of an error when logging in (page not visible); Shyam replied at 00:59 that he is checking. On 28 Oct 06:30 UTC Justin told Jad he is pushing a fix soon, with the dashboard down for a couple of minutes and no client or trading impact (presumably this issue; not stated). No confirmation from Jad yet.
Next: Confirm Jad can log in after Justin's fix.
Refs: https://mahifx.slack.com/archives/C0B7T6S6D0C/p1792976237806039 https://mahifx.slack.com/archives/C0B7T6S6D0C/p1793169011218019

### hft-fx-pricing — HFT channel FX spreads and pool coverage
status: open · since: 2026-10-20 · last: 2026-10-28
State: On 20 Oct Ali saw FX spreads on the .HFT symbols far wider than the LP feeds (about 12 cents on EURUSD) because LIQUIDITY_POOL_HFT carried only XAUUSD, so other instruments fell back to the continuity pool at $50/M markup; markup was cut to $10/M then $0 at Moe's request. On 21 Oct Ali reported FX HFT spreads at zero versus a spread on the normal feed and asked to construct the HFT price like the normal ones. Resolved by design on 28 Oct: Kate set up a dedicated pricing model CLIENT_PRICE_HFT_LDN (same as the standard non-skewed insti model, but benchmarking spreads on SCOPE_TOXIC_KL instead of SCOPE_KL) with base spreads editable in Compass spread-config; Ali confirmed they can now construct the price from it. After the 28 Oct EOD restarts the HFT connections publish this pricing model instead of the liquidity pool (distribution channels edited 14:17-14:20 and 21:02-21:04 UTC; the restart detector flagged CorePrice LIQUIDITY_POOL_HFT_LDN != CLIENT_PRICE_HFT_LDN as expected). Ali edited pricing.spreadprofile seven times on 29 Oct about 07:14-07:16 UTC (content not visible). Ali's markup versus price-model spread-config question was not explicitly answered but the new model covers spread control.
Next: Watch HFT FX spreads after the switch to CLIENT_PRICE_HFT_LDN; add remaining instruments to the HFT pool if still needed.
Refs: https://mahifx.slack.com/archives/C0B7T6S6D0C/p1792484649892479 https://mahifx.slack.com/archives/C0B7T6S6D0C/p1793196612192619

### xau-execution-style — Broker vs Broker First, HFT book and markup
status: open · since: 2026-09-21 · last: 2026-10-27
State: A 21 Sep cancel burst came from FOK/IOC MinQty handling (fixed with reference.marketSupport.FOK) and led to Kama moving all A_CLIENTS to Broker First (29 Sep). HFT flow got its own book and hedgers (30 Sep) with internalisation on the toxic HFT pool; $20/M markup on HFT and $10/M on A Book internalised flow was agreed on the 1 Oct call and set up via MultiChannelConfig on 2 Oct (a type=list vs ArrayList misconfig caused stuck orders that day). On 30 Sep Kate asked Kama to turn off PXM sweep/boost so each A-book order arrives whole and Ali asked to switch to single IOC (Kate: IOC or FOK is fine); Ali was confirming with PXM and no outcome is visible. On 15 Oct Kama asked for Broker (not Broker First) over high-impact news and said they are happy to switch manually; Moe set twilight and roll flow to Broker. Execution rules cannot be day-specific; a bare '*' in counterparty criteria matches none (remove the criteria to match all). On 21 Oct Kate explained FOK orders arriving 21:00-23:00 UTC expired because the HFT channel brokers everything to the HFT pool and none of its LPs were configured to accept FOK; Moe said all LPs accept FOK except Fusion (a crypto LP), so Kate set reference.marketSupport.FOK across the board. Kama staff edited distribution.executionRules repeatedly on 22, 26 and 27 Oct (content not visible).
Next: Mahi to confirm whether news criteria can be added to execution rules.
Refs: https://mahifx.slack.com/archives/C0B7T6S6D0C/p1790009143944299 https://mahifx.slack.com/archives/C0C1L6G37HN/p1793098819391439

### position-rec-nop — LP/client position reconciliation and NOP limits
status: open · since: 2026-10-02 · last: 2026-10-27
State: On 26 Oct Kate asked Kama for an LP position snapshot over roll; Jad posted a spreadsheet that evening and Shyam asked for a split by entity (KL/KS), Edgewater 1/2 and Scope/Scope Toxic. On 27 Oct Kate asked again for an EOD snapshot; Jad said Kama's set-up cannot split positions into the Compass format, Kate said per-LP is enough since markets are grouped for NOP limits, and Jad sent the 27 Oct EOD file in yesterday's format. Nathan compared it with Compass' roll snapshot: instruments missing from the file are flat at that LP (Jad confirmed; e.g. Compass had 29k long EURGBP across Edgewater, so a -29k adjustment), plus XPTUSD 86 at Scope; Nathan is applying the adjustments in Compass. On 19 Oct unreconciled LP positions against per-LP NOP limits blocked the hedger (see nop-hedger-outage); the limits were removed that day and Kate will ask Kama to send positions at EOD roll, XAUUSD being most of their flow. Only apply NOP limits on reconciled positions. LP positions are visible in Compass under Risk Management Positions (Markets tab per LP); NOP limit changes need hedger and pool restarts (pool at EOD) and LP position adjustments can be made intraday with the hedger off, normally by the NZ team before open.
Next: Nathan to finish the Compass position adjustments; Kama to keep sending per-LP snapshots at EOD; agree when NOP limits are re-applied.
Refs: https://mahifx.slack.com/archives/C0B7T6S6D0C/p1791557796452229 https://mahifx.slack.com/archives/C0B7T6S6D0C/p1793145150334519

### xau-open-rejects — XAUUSD market-open rejects on B book
status: open · since: 2026-10-23 · last: 2026-10-23
State: On 23 Oct Ali posted a screenshot of rejected XAUUSD orders at the market open on Kama's B book. Isaac first read it as an A-book order (Scope cancelled, client price off the limit so cancelled rather than internalised); Ali corrected that the B book is not routed to the LP, and Isaac saw no B-book cancels in Compass at that time and asked for the 012* order ID. Ali said he will share logs; none seen yet.
Next: Ali to send logs / order IDs; Isaac to diagnose.
Refs: https://mahifx.slack.com/archives/C0B7T6S6D0C/p1792735564284869 https://mahifx.slack.com/archives/C0B7T6S6D0C/p1792743155724969

### eurgbp-rejects — Market rejections on EURGBP
status: open · since: 2026-10-21 · last: 2026-10-21
State: On 21 Oct Ali asked the team to look at market rejections on EURGBP (screenshot only; no reply yet).
Next: Mahi to diagnose and reply.
Refs: https://mahifx.slack.com/archives/C0B7T6S6D0C/p1792566675726999

### lp-pool-expansion — LP pool and hedging markets, KL/KS connectors
status: open · since: 2026-09-21 · last: 2026-10-21
State: Pool started as Scope only. Moe asked 2026-10-01 for Scope, MAS, Edgewater, MatchPrime-FXedge and Arts with NOP limits. FXEdge and Arts went in after test trades (5-6 Oct), then Arts was pulled from the pool and hedging for latency (6 Oct) and left out at the 8 Oct call (NOP limits per LP: Scope 150M, MAS/Edgewater 20M, FXEdge 10M, Arts 5M). MatchPrime was restricted to gold on 7 Oct and restored on all symbols the same day after they fixed swap rates. On 14-15 Oct Star and Velocity were added and Ali sent a clean-up list, ending with Moe's final list: LIQUIDITY_POOL_HFT_LDN = Edgewater_2_KS, MAS_Toxic_KS, Scope_Toxic_KL; LIQUIDITY_POOL_LDN = Edgewater_2_KS, Scope_KL, MAS_KS, FX_EDGE_KL. Kate suggested spreading load across LLC (KL) and Securities (KS) connectors rather than all on KL. Fusion, Arts, Star and Velocity are subscribed but not in the pools. Removing a market from a pool is dynamic; adding one needs a restart (EOD, or intraday on request). LIQUIDITY_POOL_HFT still carries XAUUSD only; the other instruments were due at the 20 Oct EOD restart (see hft-fx-pricing). On 21 Oct MAS Markets was removed from all pools and hedging at Moe's request (see mas-xau-removal); Isaac changed pool markets and instrument overrides and restarted the HFT and LDN pools and hedger around 12:45 UTC.
Next: Ali to flag when Star and Velocity are ready for test trades before they join the pool; confirm the current pool list after the MAS removal.
Refs: https://mahifx.slack.com/archives/C0B7T6S6D0C/p1789990153651149 https://mahifx.slack.com/archives/C0B7T6S6D0C/p1792586254793539

### nop-hedger-outage — 19 Oct unhedged XAUUSD, SOR crash, VaR alerting
status: open · since: 2026-10-19 · last: 2026-10-21
State: From about 06:58 UTC on 19 Oct the hedger stopped clearing XAUUSD, most likely blocked by per-LP NOP limits running against unreconciled positions (Kama had posted positions in a thread, so they were missed); VaR passed 10k at 05:33 and hit about 146k (Ali: 26,000oz unhedged), and Kama raised it at 07:31. At 07:35 Isaac deleted risk.nop.perPB to unblock the hedger; a missing null check crashed liquidityPoolSOR and the hybrid and arb hedgers, ten XAUUSD orders sat open 6-9 min and Kama's 180s timeout disabled Mahi as provider until about 07:51. Processes were back by 07:37. Fix (null guard in MarketGroupTradePositionNOPTracker) is committed to release/26.4 and 26.3 but not yet deployed; until then do not delete NOP keys on Kama (set marketListNOPConfigs to [] or raise watermarks). All NOP limits were removed on Ali's request. Kate set a sustained critical-VaR alert (sustainMs 120,000, clearHoldMs 60,000) after Ali asked for an alert and a noisy 10k threshold; On 21 Oct Kate set up a new Kama notifications channel (high VaR, PnL drops, LP and client rejects, indicative pricing) alongside the config-change channel. Liam asked how we know we hedge the right thing with unreconciled positions; Kate: Kama was STP before, so all A Book risk is covered by hedging or STP.
Next: Kama to send positions at EOD roll; Isaac to get the null-check fix deployed and raise whether bad non-trading config should keep the old config instead of killing processes; Kate to tune the VaR alert if noisy.
Refs: https://mahifx.slack.com/archives/C0B7T6S6D0C/p1792395096025849 https://mahifx.slack.com/archives/C0B6FMU96G2/p1792397763936839 https://mahifx.slack.com/archives/C0B7T6S6D0C/p1792572412812379

### mas-xau-removal — MAS Markets pulled (XAUUSD 16 Oct, whole LP 21 Oct)
status: open · since: 2026-10-16 · last: 2026-10-21
State: On 16 Oct Moe asked Kate to stop sending XAUUSD to MAS Markets (standard feed only, not toxic); Kate removed it from the hedging markets straight away but the liquidity-pool (STP) side cannot drop one symbol, so she offered to set everything to internalise while the SOR is bounced. Moe chose to disable gold on Kama's side (switched off the price) and said it is easier if one symbol can be disabled per LP; Kate will look at restructuring the pool setup to allow that. Reason given: MAS rejecting market orders, causing losses in the Compass book. Kate asked for more detail on why. On 21 Oct Moe escalated: Kama is closing the MAS account, so Kate was asked to disable MAS Markets from all pools, with no pricing and no execution, from everywhere (including pricing models); only the connectors stay in case MAS fix things. Isaac made the config changes and restarted processes about 12:48 UTC (hedging markets, pool markets, HFT and LDN pool restarts); Moe worried about a reconnect as before, Isaac saw trades flowing and no disconnects.
Next: Kate to see whether pools can disable one symbol per LP (less pressing now); confirm MAS is fully out of pricing models.
Refs: https://mahifx.slack.com/archives/C0B7T6S6D0C/p1792154269472349 https://mahifx.slack.com/archives/C0B7T6S6D0C/p1792586254793539

### lp-timeouts-pxm-unsub — LP latency and timeouts triggering PXM unsubscribes
status: open · since: 2026-09-15 · last: 2026-10-19
State: Recurring pattern: an order sitting unanswered trips PXM's firewall timeout and PXM unsubscribes XAUUSD on Kama's price sessions with no automatic resubscribe (15 Sep SOR restart; 2 Oct misconfigured MCC restart; 19 Oct, see nop-hedger-outage). On 19 Oct Kate recommended keeping the 180,000ms timeout (Rostro uses the same) and instead having PXM cancel the leg and reject the client order on a pending-leg timeout while keeping the provider enabled; Moe says PXM disables the provider (or the symbol) completely on timeout, Kate noted other PXM clients just reject the order so it looks configurable, and Moe will ask PXM. Moe also wants restarts coordinated better; Kate will give notice of planned ones. Earlier latency incidents (Arts 1.4-3.3s holds, MAS 360ms IOCs) led to Arts being left out of the pools. Mahi's stance (Kate, 12 Oct): never resend an order that is still open (double-fill risk), re-hedge via other LPs only once it is dead; hardTimeoutLength exists but guesses the outcome and can strand risk (Liam). Ali objects that PXM disables the whole Mahi provider on one timeout (rory to check, 9 Oct) and that brokered orders wait for the LP fill so clients with a 500ms TTL time out (William doubts Compass supports client TTL, 5 Oct).
Next: Moe to ask PXM whether disable-on-timeout can be switched off for Kama; Mahi (rory) to confirm the PXM provider-disable behaviour; decide on hardTimeoutLength or asking LPs to reject after about 100ms.
Refs: https://mahifx.slack.com/archives/C0B6FMU96G2/p1791257314493849 https://mahifx.slack.com/archives/C0B7T6S6D0C/p1792409733558559

### brokered-flow-review — Brokered vs internalised flow review (internal)
status: open · since: 2026-10-16 · last: 2026-10-16
State: Kate's 9-16 Oct execution-quality review (internal) found most internalisable brokered flow is roll, twilight and Sunday/Monday open. Open brokered $145M and kept $26k ($182/M), almost all EURJPY with spreads slightly wider than Scope; roll/twilight brokered $783M XAUUSD and kept $14.2/M versus about $1.7/M if internalised, so brokering is right there. CP 100079_n/a was tagged arbitrageur then brokering 7-9 Oct and untagged before 12 Oct; it is now internalised on Catch-All at about -$71/M at 1m on $99M XAUUSD, no manual change, watching for re-tag. 40874_30033000 is the only steady internalise candidate (about $1k/week), to watch a couple more weeks. Andrew queried why Broker First internalises some flow at lower yield; Kate: internalised pays Mahi spreads, brokered pays LP spreads, and all rules use passthrough fill price. Andrew fed the lesson into the routine checks (PR 153 merged) so positive markouts need session/regime review before rehabilitation advice.
Next: Kate to finish instrument/timezone/CP breakdown; watch 100079_n/a re-tagging and 40874_30033000.
Refs: https://mahifx.slack.com/archives/C0B6FMU96G2/p1792160321472259 https://mahifx.slack.com/archives/C0B6FMU96G2/p1792165670366029

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

### tag-lp-exclusion — Block a counterparty tag from a specific LP
status: closed · since: 2026-10-19 · last: 2026-10-20 · closed: 2026-10-21
State: Done 20 Oct: Kate set a blacklist entry in the reference.marketSupport.tagList config on the FXEDGE_KL market (trading account A_INST_CLIENTS plus the counterparty tag Moe named, all instruments, which Moe confirmed was what he wanted); the tag can still go to other LPs.
Refs: https://mahifx.slack.com/archives/C0B7T6S6D0C/p1792407866139499 https://mahifx.slack.com/archives/C0B7T6S6D0C/p1792489839786759

### mas-fill-after-cancel — MAS 2-minute timeout, 75oz filled after cancel
status: closed · since: 2026-10-09 · last: 2026-10-12 · closed: 2026-10-22
State: Moot: Kama closed its MAS account (21 Oct, see mas-xau-removal). A 9 Oct MAS timeout crashed the hedger and MAS filled a cancelled 75oz order, leaving Compass over-hedged until Kama closed it manually.
Refs: https://mahifx.slack.com/archives/C0B7T6S6D0C/p1791566302175459 https://mahifx.slack.com/archives/C0B7T6S6D0C/p1791800955956099

## Arc
- 2026-06-02 — Deal accepted; pilot agreement signed 2026-06-08
- 2026-08-05 — B Book flow live on Compass (pricing and execution)
- 2026-09-14 — Risk-management go-live (A Book), interrupted and restored 17-23 Sep
- 2026-09-23 — Kama Securities MT5 A/B flow routed to Compass
- 2026-09-29 — Almost all Kama connectors routed to Compass; HFT clients added; VaR raised to 2,000
