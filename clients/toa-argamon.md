---
slug: toa-argamon
aliases: []
refs:
  vibepulse: ../VibePulse/.claude/clients/toa-argamon.yaml
  billing: null                     # no billing entry
  hosts: ../MahiProduct/data/client-hosts.json            # entry: toa-argamon
  wiki: null                        # ../MahiProduct/wiki/clients/argamon.md is referenced in Slack but not checked here
channels:
  internal-argamon: C06U76A7ZJR
  mahi-argamon-operations: C06TW3D8NMV
  mahi-argamon-trading: C083GP5F1CL
  internal-toa-ops: C035H1VNCAD
contacts:
  - {name: "Tom McLean", role: "Argamon analyst; day-to-day contact in mahi-argamon-operations (client queries, crypto outages)"}
  - {name: "Levi Ulman", role: "Argamon ops; FIX connectivity (Centroid, PXM, Jump), give-ups, bridge migration lead"}
  - {name: "Elan Bension", role: "Argamon senior; decision-maker on spreads, LP/pricing config, PXM move"}
  - {name: "Hafiz Mehmood", role: "Argamon analytics; Analytics_Position / TradePosition table requests"}
  - {name: "Maitrya Anupam", role: "Argamon; raises rejects in mahi-argamon-trading, copied on bridge migration"}
  - {name: "Mo Srouji", role: "Argamon; supplies MT5 equity/report exports"}
  - {name: "Jem", role: "Argamon exec (also 'Jeremy'); on weekly strategy calls with Elan, Daria and Shyam; surname unknown", confidence: low}
  - {name: "Joanna Theofanous", role: "Argamon ops; no activity seen in window", confidence: low}
  - {name: "Alexander Karnadi", role: "Argamon analytics/reconciliation; no activity seen in window", confidence: low}
last_catchup: 2026-11-27T08:14:59Z
status: active
---

## Now
Argamon is the NY retail tenant (Mahi) plus Toa-hosted LDN/CHI/APN1 boxes (insti, hedging, crypto). Weekly calls with Jem/Elan/Daria/Shyam drive the agenda: wanting 500:1 leverage and to hold more risk, so Mahi is running sims and rolling CFDs/indices into Compass with internalisation and skew.
Argamon is moving connectivity from Centroid to PrimeXM; Beeks add the NY4 Cboe X-connect over 11-27/29. Compass 26.4 is on LDN/CHI/APN1; NY was staged for the 10-10/11 weekend restart (outcome unconfirmed).
On 10-21 the NY retail FX book moved to a 500k G8 inventory cap with Friday flatten (William Denny monitoring); on 11-09 the cap was extended to CNH/ZAR/SGD/MXN (250k), and on the 11-10 call Argamon asked for more internalisation and a gold internalisation review (losing on reval).
GTS HRP sessions were retired on 10-27 (no GTS via NWM market in Compass yet). Toa reset Mahi's last-look/tolerance, so TOA_CHI went back into XAU hedging on 11-03. On the 11-17 call Argamon agreed to wider gold spreads, harder LR and PSM beta moving to prod likely next week. Open operational threads: CHI hedger breaches/CBOE state mismatches, LDN insti pricer reference-market gap, B2PRIME XAU increment rejects.

## Streams

### gts-hrp-nwm — HRP LP sessions wound down in favour of NWM/NWPB
status: open · since: 2026-10-27 · last: 2026-11-27
State: Cleanup continues: on 11-26 Shyam switched the Toa CHI pricing subscription proxied from Args NY4 from XTXM_RCTV_HRP_2 to XTXM_RCTV_NWPB_1 because HRP_2 no longer arrives (CHG-2611-52WA, live at the weekend reboots), and CHG-2611-9CS8 (Fri 11-27 01:30Z to Sun 11-29 21:00Z) renames the GTS markets to NatWest and adds Jane to the wide lists. Earlier, CHG-2611-PA7W (Shyam, 11-12) planned the GTS LP remap to NatWest PB for Sun 15 Nov (ZD 23769 window; outcome never confirmed), and Levi's 11-11 pool change list replaced HRP PB markets with NWPB for HSBC, UBS, NWM (and JLQD on crypto/FX hybrid), excluding Jane St (awaiting NWM sessions), keeping HSBC on HRP for metals and HSBC+UBS on HRP for XPT/XPD, with NWPB minimums dropped (FX 250k to 1k, XAUUSD 50 to 1, XAGUSD 15k to 50); Daria applies via EOD restarts. On 10-27 13 trades went to GTS via NWM after NY Compass kept sending to the retired GTS_HRP; Argamon booked them manually and Compass keeps them under GTSX_RCTV_HRP_1, so per-LP reconciliation needs a mapping. There is no GTS via NWM market in Compass. On 10-28 JPM and HSBC moved to NWPB feeds (Levi to decomm unused _2 and HRP feeds); HSBC market data is to be restarted at EOD.
Next: Mahi to confirm the 11-27 to 11-29 weekend changes took effect and the NY pool changes were applied; Argamon to say whether they want a GTS via NWM market in Compass; Mahi to restart HSBC market data at EOD and confirm prices stream.
Refs: https://mahifx.slack.com/archives/C06TW3D8NMV/p1793062310809789 https://mahifx.slack.com/archives/C083GP5F1CL/p1793166381823569 https://mahifx.slack.com/archives/C083GP5F1CL/p1794365783062669 https://mahifx.slack.com/archives/C06U76A7ZJR/p1795742597884209

### fast-hedge-whitelist — Retail book fast-hedge whitelist pruning
status: open · since: 2026-11-27 · last: 2026-11-27
State: On 11-27 Shyam removed whale counterparty 84000303 from the retail book fast-hedge whitelist: it was whitelisted earlier for toxic flow around news events but recent flow looks soft. INST-1 was added to the same whitelist on 10-05 (see inst-toxic-flow).
Next: Shyam to monitor the counterparty closely next week.
Refs: https://mahifx.slack.com/archives/C06U76A7ZJR/p1795748476687579

### xau-spread-lr-psm — Wider gold spreads via higher LR and PSM beta
status: open · since: 2026-11-17 · last: 2026-11-26
State: On 11-26 Shyam proposed the XAU PSM setup to Jem (pending approval): 3-month sim +$5.4k spread earned (+2.7%, about +$1.05/M), avg published -0.86c, avg charged +0.88c; a safe start with widening to be increased over time. Shyam's 11-26 week-so-far report put gold LR at +$7.9k ($11.05/M vs $4.33/M 3-month avg), credited to the tightening to 150k/150k; retail +$30.9k on $937M (+$32.99/M vs +$13.51/M avg) and CFD +$4.9k on $252M, on 2.2x normal volume (about half from one new gold client since 10 Nov, plus AUDCAD copy trading at 12% of volume) and positive reval +$11.7k. On the 11-17 call Jem and Elan agreed they need wider gold spreads to be profitable on gold. LR on XAU was tightened that evening (Daria, 22:06Z) from 500k surplus / 250k per 500ms to 150k surplus / 75k per 500ms, as Shyam proposed and Jem tightened further. They will go harder on LR for bursty flow (no big-client complaints since Toa LR went to $15/M; retail is $4/M), ramped incrementally. They are happy with the 6-12c spread range on beta XAU with PSM; on 11-16 beta published 7.71c vs 8.05c in prod and charged 8.43c vs 8.18c at client trades. Shyam wants to smooth the spread fluctuations before moving it to prod, probably next week; there is room to widen more or tighten less at the same averages. Aim is LR plus PSM keeping average published spread near current. Absorbs the old xauusd-hedging thread.
Next: Jem to approve the XAU PSM setup; Shyam to ramp LR incrementally and move PSM to prod.
Refs: https://mahifx.slack.com/archives/C06U76A7ZJR/p1794887022544449 https://mahifx.slack.com/archives/C06U76A7ZJR/p1795663433237979 https://mahifx.slack.com/archives/C06U76A7ZJR/p1795661872529529

### cboe-maker-session — Argamon requesting Cboe ECN Maker session
status: open · since: 2026-11-05 · last: 2026-11-26
State: On 11-26 Shyam noted Beeks are adding the Cboe X-connect routes to argamon-ny-trading-1 and -2 over MS7125 in the Fri 11-27 22:00Z to Sun 11-29 03:00Z window, before the weekly reboots, with no change to the existing Toa connection (NOCINT-863225); this closes the earlier chase of Beeks sales. On the 11-23/24 call Argamon were happy with the quoted 99 GBP/month for the Cboe hidden peg hedging setup if not already covered by the current Toa Argamon Beeks order; Elan expects it to be quite beneficial. On 11-15 Shyam asked internally whether anyone heard from Beeks sales about an X-connect from Argamon NY4 to Cboe (NOCINT-861001 said sales would reach out the week before; nothing received). Levi emailed support on 11-05 for a Maker session connection to Cboe ECN. Shyam is handling it and asked whether the trading account is the same as with Toa; Levi confirmed both are hedged on Argamon's HRP PB account. On 11-09 Shyam noted ordersCboe1 and marketDataCboe1 are being set up on the Toa side (expect alerts while they come up). Likely linked to the CBOE hidden-peg hedging trial in NY4.
Next: Shyam/Daria to set up the Cboe Maker session once the X-connect is in (after the 11-29 weekend work).
Refs: https://mahifx.slack.com/archives/C083GP5F1CL/p1793840550520559 https://mahifx.slack.com/archives/C06U76A7ZJR/p1795490052540999 https://mahifx.slack.com/archives/C06U76A7ZJR/p1795725745693019

### pxm-hrp-dropcopy — PrimeXM drop copy legs vs ATFX aggregate at HRP
status: open · since: 2026-11-24 · last: 2026-11-26
State: On 11-26 four XAG/USD confirms (1000 and 50 lots) were rejected on hrpFxDropCopy1 with "No forward route"; Tom McLean said they were his test of a drop value on a test account (INST-TST) already cancelled with HRP, so not a fault. Levi (Argamon) found ARGAMAU trades from the PrimeXM drop copy to HRP via Toa LDN are split into legs while the ATFX side is aggregated, though sums match, and could not see the legs in LDN Compass. Nathan explained on 11-24 that PrimeXM sends each attempt with its own suffix (e.g. 73376-1 and -2 rejected, then -3 and -4 filled at one price) and Compass treats each as an independent order and trade; Compass trade ID maps to HRP Execution ID and Compass order ID to HRP client order ID, so the legs match many-to-one to ATFX's single trade. In the trading channel Nathan also said Mahi would look into the thread further.
Next: Levi to continue the investigation with PrimeXM using the mapping.
Refs: https://mahifx.slack.com/archives/C083GP5F1CL/p1795497703909559 https://mahifx.slack.com/archives/C083GP5F1CL/p1795503640247509?thread_ts=1795497703.909559 https://mahifx.slack.com/archives/C06TW3D8NMV/p1795703485804639

### cfd-indices-rollout — CFDs and indices into Compass (NY4)
status: open · since: 2026-08-24 · last: 2026-11-26
State: On 11-26 Shyam raised CFD skew (DOW, NDX, SPX, G30) from 0.35 to 0.45 of the benchmark spread, est. $150/week uplift, to be watched for arbing; the flow-price-thresh signal looks optimal. Indices (NDX, SPX, DOW, G30) were moved from Jump STP to Compass: G30EUR live 09-10 brokering to Jump, other indices 09-11, A_CFD books added to analytics tables at Argamon's request (done 09-24), CFD internalisation on 09-23 with hybridHedgerCfd1, and skew sizing raised from 0.25x to 0.35x of the Jump benchmark spread on 10-08 (beta now 0.45x, review the following week). Larger flow looks toxic, so a "Broker CFDs - Large" rule brokers trades above $500k (09-30). NAS100 rejections on 09-13 were because Jump published about 70 NDX, too little for the second tier; BMSL pass-through enabled. MT5 drop copy live 08-28; MT4 showed about 131m index volume for August.
Next: Shyam to monitor arbing at 0.45x; Daria to see whether PSM suits indices.
Refs: https://mahifx.slack.com/archives/C06U76A7ZJR/p1787541873458239 https://mahifx.slack.com/archives/C06U76A7ZJR/p1789003323456489 https://mahifx.slack.com/archives/C06U76A7ZJR/p1791422519718139 https://mahifx.slack.com/archives/C06U76A7ZJR/p1795727529239549

### chi-hedgers — Toa CHI hedger breaches and CBOE state mismatches
status: open · since: 2026-08-03 · last: 2026-11-25
State: hedgerCBOE1 at Toa CHI keeps going down on PnL firewall breaches and is restarted by whoever is on call: 11-25 18:01Z (hourly PnL firewall; Isaac Dann raised the limit from -2m to -2.5m), 11-25 01:20Z (UnrealisedPnlFirewall, 4.32M in 24h; Shyam), 11-23 (RealisedPnlFirewall, -3.0M in 24h; Maten), 11-12 (24h breach of 4,002,402; Arun), 11-05 (daily realised limit; Shyam raised realisedPnlLimitPerDay to -3M with James's approval), 11-04 (1-hour firewalls as XAUUSD gained about $60 in an hour; Daria raised PnL Limit Per Hour from 1.6m to 2.2m and suggests reviewing the sweep config), 10-30 (six UnrealisedPnlFirewall trips in 3 hours; Lee bumped the unrealised limits). hedgerCBOE1 and hedgerHrpCME1 have tripped PnL/firewall/order-breach limits since 09-17; Toa says the firewalls see only the hedger side, so restart is fine when net PnL is healthy, and James says offsetting positions are just bigger and limits will be raised further if it continues. ordersCboe1 state mismatches (price 1.32503 vs 1.325) were referred to CBOE via Argamon; Lee had a code fix ready in the week of 09-29. 09-07 hedgerHrpCME1 crashed on a profileDefinitions edit (XAU to ZAR conversion), fixed by reverting; 09-27 ordersCME1/ordersCOMEX1 stuck in starting and ordersCOMEXMarex1 awaiting a fix.
Next: Mahi to review the CBOE sweep config and firewall limits; Lee to confirm the CBOE state-mismatch code fix shipped and ordersCOMEXMarex1 fixed.
Refs: https://mahifx.slack.com/archives/C035H1VNCAD/p1785757251842839 https://mahifx.slack.com/archives/C035H1VNCAD/p1791982032259119 https://mahifx.slack.com/archives/C035H1VNCAD/p1793838638143019 https://mahifx.slack.com/archives/C035H1VNCAD/p1795629697839949

### retail-leverage-risk — Argamon wants 500:1 leverage and to hold more risk
status: open · since: 2026-08-31 · last: 2026-11-24
State: On the 11-23/24 call Jem again wanted to try full B-book for some tags Compass classifies as B-book; Shyam will sim whether SI on those tags can be run profitably and look at raising FX internalisation caps from 500k to 1M. On 11-09 Shyam extended the capped internalisation to liquid EMs (CNH, ZAR, SGD, MXN; 250k cap, 500k hard backstop; 6-month replay slightly positive to neutral); on the 11-09/10 call Argamon asked for more internalisation and a review of the gold strategy, which is losing on reval. Earlier calls: Argamon wants 500:1 leverage vs 100:1 now and to hold more risk, with no timeline; they are open to holding past 500k for soft CPs and to PSM in beta provided average spreads hold; dark pool hedging (XTX) was floated for NY4 but Toa dropped XTX on spread cost. On 10-21 Shyam switched the NY retail FX book to a G8-Cap profile (500k inventory cap, Friday flatten; replay +$62k, about $1/M, with much smaller peaks); rollback is swapping instrumentToProfileMappings G8-Cap to G8 and restarting hybridHedgerHrp1. Will Carter asked William Denny to monitor. Argamon also runs a prop-style challenge business outside Compass.
Next: Shyam to sim SI on B-book-classified tags, look at FX caps 500k to 1M, and review gold internalisation strategy and look for more full B-book flow; William Denny to monitor retail PnL on the new G8 cap; Shyam to check configurability of holding past 500k and B-book for soft CPs, put PSM in beta with comparative sims, trial hidden peg hedging in NY4 once Elan sends CBOE credentials, and look into dark pool hedging (Daria on fill rate/time to fill); Argamon to say how much risk they will open up.
Refs: https://mahifx.slack.com/archives/C06U76A7ZJR/p1788152543060319 https://mahifx.slack.com/archives/C06U76A7ZJR/p1794258991256239 https://mahifx.slack.com/archives/C06U76A7ZJR/p1795490052540999

### jane-st-ny4 — Reactive Markets setup of Jane Street on NY4
status: open · since: 2026-11-23 · last: 2026-11-23
State: On 11-23 Levi chased an email request (Reactive Markets<>Argamon, set up Jane Street on NY4) with no update; Rory King said he would check status and revert. Related to the Jane Street exclusion awaiting NWM sessions in the HRP to NWPB pool change.
Next: Rory King to check status and revert to Levi.
Refs: https://mahifx.slack.com/archives/C06TW3D8NMV/p1795423330035409 https://mahifx.slack.com/archives/C06TW3D8NMV/p1795425066327019

### roll-fok-topup — FOK market orders cancelled over roll; Allow Top Up enabled
status: open · since: 2026-11-05 · last: 2026-11-20
State: On 11-20 Tom McLean asked why an LDN order group was rejected ("Internalisation Disabled IoC expired"): Daria explained the client order was FOK and no LP in the pool accepts FOK, suggested client IOC or Allow Top Up on the execution rule, and Elan enabled top up on LDN that morning. Over roll, INST-33 FOK market orders on the rollover profile were brokered to the LDN pool and cancelled; on 11-05 Argamon asked for Allow Top Up on the rollover profile, and Nathan explained it sends IoC to the pool and lets the house top up partial fills (adds book risk vs pure brokering; min top-up PnL of 0 agreed). Related: after a XAUUSD trade group hit the net volume limit at about 600oz (11-04), James advised setting profiles (incl. Catch-All) to Don't Cancel, which extends last-look to reprice on imbalance; Elan agreed.
Next: Argamon to set Catch-All and other profiles to Don't Cancel as agreed; Mahi to watch book risk from top-ups after the next roll.
Refs: https://mahifx.slack.com/archives/C083GP5F1CL/p1793839256914529 https://mahifx.slack.com/archives/C06TW3D8NMV/p1793795725289139 https://mahifx.slack.com/archives/C06TW3D8NMV/p1795159478772559

### platform-ops — Toa box housekeeping, config landmines, capacity
status: open · since: 2026-08-17 · last: 2026-11-20
State: CHG-2611-Z81H (James, self-approved 11-20, Sat 21 Nov 08:00-09:00Z) puts Compass 26.4 with in-band Aeron metadata on every market. CHG-2611-9BCQ (James, Sat 21 - Sun 22 Nov) renames the LDN/CHI client price streams (CLIENT_PRICE_EXCL_STANDARD_LDN, CLIENT_PRICE_AGG_STANDARD_LDN); on 11-20 Daria said receiver-side config is imported and goes live at weekend restarts, and Mahi will check each environment has a live book on Sunday before the 22:00Z open and restart any that have not attached. Recurrent config-driven outages: a bad liquidityRefreshProfiles entry took down LDN/CHI distribution gateways 08-20 to 08-23; Elan's skew edit stopped pricerInstiLight2 (09-01); an expired MGCQ6 contract blocked propTrader1HrpChi1 (08-30). CHI /app/fx/apps/mahifx hit 90% (dead EBS model data); 50GB added 10-11 (about 80%). hazelcastNode OOM on APN1 primary (09-07) tied to the secondary box being decommissioned without unwinding multi-region infra. New LP being set up in TKY (10-14), new gateways on CHI (09-22). marketDataNado1 on APN1 OOMed 10-28 and 11-04; Toa disabled PagerDuty for the APN1 service and Isaac agreed the APN1 box can be stopped. Kraken Futures market data on APN1 went down 10-30 (Shyam: Kraken's side). On 11-02 Daria asked Toa whether to extend or disable not-ticking alerts for ISAM_NW_LDN and KGI_RCTV_NYC around roll (16:20-18:15 NY); no answer yet. On 11-12 traderBinance on APN1 went down on an order-breach limit (max breaches 0); Arun is looking into it.
Next: Mahi to check live books Sunday before open after the price-stream rename; Toa to answer on the roll-time not-ticking alerts; stop the APN1 box; watch for Kraken Futures MD recovery on APN1; confirm the leftover EBS model data is actually deleted; unwind multi-region infra from the decommissioned secondary box.
Refs: https://mahifx.slack.com/archives/C035H1VNCAD/p1791220342201259 https://mahifx.slack.com/archives/C035H1VNCAD/p1793148848983029 https://mahifx.slack.com/archives/C035H1VNCAD/p1793805125223629 https://mahifx.slack.com/archives/C035H1VNCAD/p1795193614817319

### pxm-centroid-migration — Argamon moving connectivity from Centroid to PrimeXM
status: open · since: 2026-07-21 · last: 2026-11-16
State: On 11-16 Shyam told Argamon the Centroid UAT price session keeps disconnecting, apparently because Centroid's UAT side falls behind on the price stream; live Centroid sessions are fine and Levi is checking with Centroid. Argamon say they have Centroid failover for LP aggregation (to confirm, 10-27 call). James says Centroid has been poor and Elan has spent months negotiating a PrimeXM deal; James pitched the Mahi bridge but Argamon needs margin and reporting, which Mahi lacks. On 10-08 a PXM price-improvement mismatch was traced to PXM's default of keeping price improvement; Levi will set PXM to pass through all slippage. On 10-21 the Centroid IP changed to 192.229.22.160, outside the range the Beeks cross-connect covers; Shyam raised NOCINT-856420 and ZD 23672, and Centroid must advertise the new IP over the cross-connect. No Centroid move date yet.
Next: Levi to apply the PXM passthrough setting and report; Beeks to confirm cross-connect changes for the new Centroid IP; Tom to supply a Centroid move date.
Refs: https://mahifx.slack.com/archives/C06TW3D8NMV/p1784590345336939 https://mahifx.slack.com/archives/C06TW3D8NMV/p1792647126311719 https://mahifx.slack.com/archives/C06U76A7ZJR/p1793206534345309 https://mahifx.slack.com/archives/C06TW3D8NMV/p1794794780957499

### ny-link-failover — NY link failover retest and flaky SSH
status: open · since: 2026-11-13 · last: 2026-11-16
State: CHG-2611-DHA8 (NY link failover retest, Tokyo crypto feeds may blip, Fri 13 Nov 22:00-22:20Z) was approved, implemented and verified/closed on 11-14. On 11-16 Daria asked whether the intermittent SSH failures (about 50% of attempts succeed) are related; she has Beeks ticket NOCINT-861819 open.
Next: Beeks to resolve NOCINT-861819; confirm whether SSH flakiness relates to the failover retest.
Refs: https://mahifx.slack.com/archives/C06U76A7ZJR/p1794587467071369 https://mahifx.slack.com/archives/C06U76A7ZJR/p1794793297361489?thread_ts=1794587467.071369

### jump-failover — Jump (via OZ) asking about internet failover route
status: open · since: 2026-11-09 · last: 2026-11-09
State: Levi says Jump (via OZ) are setting up failover protocols; the current Jump connection runs over the cross-connect. Shyam replied that over the internet the sessions would come from the server's public IP, not the cross-connect one, so Jump may need to confirm its whitelist covers it, and asked for an internet endpoint (host, quote/trade ports, plain TCP vs SSL) so it can be added as a backup host on both sessions. Levi will pass the public IP to Jump and come back with the endpoint.
Next: Levi to get Jump/OZ to confirm the whitelist and supply the internet endpoint; Shyam to add the backup host and test the switch with OZ.
Refs: https://mahifx.slack.com/archives/C06TW3D8NMV/p1794189940988869 https://mahifx.slack.com/archives/C06TW3D8NMV/p1794192953592729

### lucera-fill-delay — Lucera insti fill report delayed 42ms (HARD_TIMEOUT)
status: open · since: 2026-10-18 · last: 2026-11-02
State: Levi (Argamon) saw an EUR/USD Lucera order filled over 120ms after placement and wants the expiry to match Lucera's 90ms. Nathan explained the hard timeout is per FIX session (hardTimeoutLength in fixClientConnection, currently 80ms on this session) and a HARD_TIMEOUT comment means it fired and the order was filled because the pool price still crossed. The fill was at 80ms in Compass (21:39:44.733) but the execution report went out at .775, a 42ms internal delay on Mahi/Toa's side; Levi needs the FIX messages for Lucera, which Nathan supplied. On 11-02 Levi asked which FIX tag sets the counterparty ID on LD Compass account CLIENTS_HRP_LUCERA; Daria says it uses tag 109 if present, else falls back to 1+448, and Levi will clean up the tags with Lucera.
Next: Nathan to find the cause of the 42ms delay before the execution report was sent.
Refs: https://mahifx.slack.com/archives/C06TW3D8NMV/p1792362870440649 https://mahifx.slack.com/archives/C06TW3D8NMV/p1792375513540999 https://mahifx.slack.com/archives/C06TW3D8NMV/p1793602642195049

### insti-ldn-pricing — LDN insti pricing indicative / reference markets
status: open · since: 2026-08-17 · last: 2026-11-01
State: CLIENT_PRICE_INSTI_LDN has repeatedly gone indicative (EBS_IMP_CHI removal in the EBS decommission on 2026-08-17; index pricing during roll). James says it is acceptable for this model to be indicative (it alone has no reference-price fallback, deliberately); CBOE liquidity may be too thin for stable index pricing and Elan was to ask CBOE. On 10-15 a change to LDN pricerInsti reference markets left CME FX/metals futures (6AZ6, GCZ6 etc.) with none; Lee says they are not published to clients. On 11-01 Daria restarted the Argamon LDN prices and pricerInsti1 again alarmed (unable to create 12 of 35 pricing models, all no-reference-price markets); she asked whether those instruments should be removed.
Next: Toa/Nathan to decide whether to remove the unpriced instruments or suppress the alert.
Refs: https://mahifx.slack.com/archives/C035H1VNCAD/p1786949906190919 https://mahifx.slack.com/archives/C035H1VNCAD/p1787003951012219 https://mahifx.slack.com/archives/C035H1VNCAD/p1792028629227619 https://mahifx.slack.com/archives/C035H1VNCAD/p1793571986506049

### inst-toxic-flow — INST-1 large toxic flow in retail book
status: watching · since: 2026-10-05 · last: 2026-10-27
State: Downgraded to watching: no INST-1 discussion since 10-27 (31d). On 11-27 Shyam separately removed whale counterparty 84000303 from the retail fast-hedge whitelist (see fast-hedge-whitelist). INST-1 began trading the NY retail book with large, highly toxic volumes that are internalised under the "Internalise <500k - INST" rule, causing most of the recent PnL drops. Shyam added INST-1 to the Retail Book fast-hedge whitelist on 10-05; no follow-up on whether it worked. On the 10-27 call Elan agreed that INST-tagged retail flow can be sent to Chi if it gets too toxic.
Next: Shyam to review the effect on retail PnL and decide whether to route INST flow to Chi.
Refs: https://mahifx.slack.com/archives/C06U76A7ZJR/p1791171597533909 https://mahifx.slack.com/archives/C06U76A7ZJR/p1793068905149339

### ioc-timeouts-chi — XAUUSD IoC orders timed out with no LP response (CHI)
status: watching · since: 2026-10-22 · last: 2026-10-22
State: Between 03:39 and 03:40 UTC on 10-22, 8 XAUUSD orders from the AXI-OZOrders session were brokered to UBS, JPM and DB at Toa CHI and got no ack or execution report, so they timed out and clients were sent cancels. Nathan asked Argamon to check with the LPs whether any were received or filled; Maitrya replied they cannot see the trades on either reactive or Mahi NYC, and Nathan acknowledged. Cause of the missing LP responses is not stated.
Refs: https://mahifx.slack.com/archives/C06TW3D8NMV/p1792644401138689 https://mahifx.slack.com/archives/C06TW3D8NMV/p1792646965509099

### xau-invalid-increment — XAU price increment rejects (TOA_CHI, B2PRIME)
status: watching · since: 2026-09-09 · last: 2026-10-09
State: No activity since 2026-10-09; downgraded to watching, no confirmation that B2PRIME fixed the increment. On 09-09 TOA_CHI/A_EXTERNAL_WASH rejected 410 XAU orders with INVALID_INCREMENT; Mahi pulled TOA_CHI from the market, changed the increment and re-added it at EOD. On 2026-10-09 B2PRIME XAU orders after the 10-08 rollover were all priced to 3dp and rejected on increment; Shyam asked Argamon to raise it with B2PRIME and Maitrya agreed. A PD incident was also raised in internal-toa-ops.
Next: Argamon to get B2PRIME to price XAU to the right increment; Mahi to confirm rejects stopped.
Refs: https://mahifx.slack.com/archives/C083GP5F1CL/p1788912414279449 https://mahifx.slack.com/archives/C06TW3D8NMV/p1791507691705119

### compass-26-4 — Compass 26.3 to 26.4 upgrade
status: watching · since: 2026-09-26 · last: 2026-10-09
State: 26.4 deployed to Toa LDN/CHI and APN1 on 09-26 (aeron inband metadata enabled for KRAKEN as a test). The NY retail env was staged on 10-09 with a weekend restart planned (CHG-2610-FX8E, Argamon told in mahi-argamon-operations); Liam flagged that argamon sets neither widening nor tightening adjustment params, so prices will widen/tighten by one increment on PSM signals after the upgrade and decided to let it go on; James approved the RC.
Next: confirm NY upgrade went live and PSM overlays behaved at the open (no post-restart report seen).
Refs: https://mahifx.slack.com/archives/C035H1VNCAD/p1790435088325269 https://mahifx.slack.com/archives/C06U76A7ZJR/p1791483328149119 https://mahifx.slack.com/archives/C06TW3D8NMV/p1791543787933719

### chi-gold-roll — Toa CHI gold hedging still on Dec contracts after roll to Feb
status: closed · since: 2026-11-25 · last: 2026-11-25 · closed: 2026-11-26
State: Shyam flagged on 11-25 (PagerDuty incident) that CHI gold hedging was still on Dec although the market had rolled to Feb; Toa said they were starting the roll that day. James announced the roll underway at 11:22Z: Dec close-only since 11:11Z, new gold hedging into Feb (GCG7/MGCG7), silver moved to Mar.
Refs: https://mahifx.slack.com/archives/C035H1VNCAD/p1795582253672819 https://mahifx.slack.com/archives/C035H1VNCAD/p1795605763725059

### toa-last-look-hedge — Toa last-look tolerance 0 rejecting Mahi gold hedges
status: closed · since: 2026-11-02 · last: 2026-11-03 · closed: 2026-11-26
State: Toa set last-look tolerance to 0 on 10-28 (fill rate fell from about 40% to 7%); Shyam pulled TOA_CHI from gold hedging on 11-02. Toa reset it by 11-03 and Shyam added TOA_CHI back; no further reports, assumed resolved.
Refs: https://mahifx.slack.com/archives/C06U76A7ZJR/p1793588984698429 https://mahifx.slack.com/archives/C06U76A7ZJR/p1793678514931149

### crypto-pricing — Toa crypto pricing outages and sizes
status: closed · since: 2026-08-19 · last: 2026-09-21 · closed: 2026-11-23
State: No activity since 2026-09-21; assumed resolved. Crypto pricing dropped on Sunday 09-13 (APN1 pricers failed to start after a reboot) and again 09-21; root cause never posted.
Refs: https://mahifx.slack.com/archives/C06TW3D8NMV/p1787099040590799 https://mahifx.slack.com/archives/C06TW3D8NMV/p1789286838789979 https://mahifx.slack.com/archives/C06TW3D8NMV/p1789997451357139

### xauusd-hedging — XAUUSD hedging, news widening and NFP loss
status: closed · since: 2026-08-14 · last: 2026-09-17 · closed: 2026-11-17
State: merged into xau-spread-lr-psm (no activity since 2026-09-17).
Refs: https://mahifx.slack.com/archives/C06U76A7ZJR/p1786681733979849 https://mahifx.slack.com/archives/C06U76A7ZJR/p1788530007371599 https://mahifx.slack.com/archives/C06U76A7ZJR/p1789609500783629

## Arc
- 2026-06 — Centroid migration from OneZero completed; Centroid test trades through July.
- 2026-07-01 — Contract split: Mahi keeps the retail tenant, Toa takes B2B/crypto/RI; Toa-hosted LDN/CHI/APN1 boxes carry insti and hedging.
- 2026-07-24 — FSS markets (14) decommissioned from Argamon.
- 2026-08 — Jonah Ink left Argamon; Elan weighing switching off NY insti routing around Mahi.
- 2026-08-17 — EBS feed decommissioned.
- 2026-08-24 — Weekly strategy calls with Jem/Elan restarted.
- 2026-08-31 — Argamon asked to offer 500:1 leverage and hold more risk; sims started.
- 2026-09-04 — NFP XAUUSD loss on retail; RCA completed.
- 2026-09-26 — Compass 26.4 live on LDN/CHI/APN1.
- 2026-09-29 — Argamon confirmed to be moving from Centroid to PrimeXM.
- 2026-10-21 — NY retail FX book moved to G8 500k inventory cap with Friday flatten.
