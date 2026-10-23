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
last_catchup: 2026-10-23T07:20:13Z
status: active
---

## Now
Argamon is the NY retail tenant (Mahi) plus Toa-hosted LDN/CHI/APN1 boxes (insti, hedging, crypto). Weekly calls with Jem/Elan/Daria/Shyam drive the agenda: wanting 500:1 leverage and to hold more risk, so Mahi is running sims and rolling CFDs/indices into Compass with internalisation and skew.
Argamon is moving connectivity from Centroid to PrimeXM. Compass 26.4 is on LDN/CHI/APN1; NY was staged for the 10-10/11 weekend restart (outcome unconfirmed).
On 10-21 the NY retail FX book moved to a 500k G8 inventory cap with Friday flatten (William Denny monitoring).
Open operational threads: CHI hedger breaches/CBOE state mismatches, LDN insti pricer reference-market gap, B2PRIME XAU increment rejects.

## Streams

### pxm-centroid-migration — Argamon moving connectivity from Centroid to PrimeXM
status: open · since: 2026-07-21 · last: 2026-10-22
State: James says Centroid has been poor for Argamon and Elan has spent months negotiating a PrimeXM deal; James pitched the Mahi bridge but Argamon needs margin and reporting, which Mahi lacks (Andrew Morgan asked about the business case). The Argamon NY Centroid bridge was migrated to a new IP over the weekend of 09-26/27 (Zendesk 23532; Beeks confirmed the route covers the range; retail dist sessions reconnected 09-27). Toa's crypto session to PXM LD needed a sequence reset on 09-20. On 10-08 a PXM price-improvement mismatch (client filled at 4107.19, Toa at 4107.18) was traced to PXM's default of keeping price improvement; Levi will configure PXM to pass through all slippage and observe. On 10-21 Tom McLean said the relevant Centroid IP has changed again to 192.229.22.160, outside the 192.229.23.x range the Beeks cross-connect route covers; Shyam raised NOCINT-856420 with Beeks and ZD 23672, and Centroid must advertise the new IP over the cross-connect. Argamon has no date for the Centroid move yet (it was due last month). The Wintermute/Centroid-direct question on 09-09 was an expected decommissioned connection.
Next: Levi to apply the PXM passthrough setting and report; Beeks to confirm cross-connect changes for the new Centroid IP; Tom to supply a Centroid move date.
Refs: https://mahifx.slack.com/archives/C06TW3D8NMV/p1784590345336939 https://mahifx.slack.com/archives/C06TW3D8NMV/p1791464526120859 https://mahifx.slack.com/archives/C06TW3D8NMV/p1792647126311719

### retail-leverage-risk — Argamon wants 500:1 leverage and to hold more risk
status: open · since: 2026-08-31 · last: 2026-10-21
State: Argamon wants to offer higher leverage (500:1 vs 100:1 now) and hold more risk. On 2026-10-21 Shyam, agreed with Jem, switched the NY retail FX book to a "G8-Cap" profile: up to a 500k inventory cap on internalised G8 flow with a Friday-close flatten, chosen from earlier sims. Replay Sep 25 to mid Oct showed +$62k (about $1/M) vs the old rules, average G8 risk up from $0.91m to $1.26m with much smaller peaks and near-flat weekends. Rollback is swapping instrumentToProfileMappings G8-Cap to G8 and restarting hybridHedgerHrp1. Will Carter asked William Denny to monitor. Earlier: sims did not clearly support loosening risk; 09-22 call agreed CFD internalisation and asked for leverage recommendations; Argamon also runs a prop-style challenge business outside Compass.
Next: William Denny to monitor retail PnL on the new G8 cap; Argamon to say how much risk they will open up and get leverage recommendations.
Refs: https://mahifx.slack.com/archives/C06U76A7ZJR/p1788152543060319 https://mahifx.slack.com/archives/C06U76A7ZJR/p1792552125427929


### lucera-fill-delay — Lucera insti fill report delayed 42ms (HARD_TIMEOUT)
status: open · since: 2026-10-18 · last: 2026-10-19
State: Levi (Argamon) saw an EUR/USD Lucera order filled over 120ms after placement and wants the expiry to match Lucera's 90ms. Nathan explained the hard timeout is per FIX session (hardTimeoutLength in fixClientConnection, currently 80ms on this session) and a HARD_TIMEOUT comment means it fired and the order was filled because the pool price still crossed. The fill was at 80ms in Compass (21:39:44.733) but the execution report went out at .775, a 42ms internal delay on Mahi/Toa's side; Levi needs the FIX messages for Lucera, which Nathan supplied.
Next: Nathan to find the cause of the 42ms delay before the execution report was sent.
Refs: https://mahifx.slack.com/archives/C06TW3D8NMV/p1792362870440649 https://mahifx.slack.com/archives/C06TW3D8NMV/p1792375513540999


### insti-ldn-pricing — LDN insti pricing indicative / reference markets
status: open · since: 2026-08-17 · last: 2026-10-15
State: CLIENT_PRICE_INSTI_LDN has repeatedly gone indicative (EBS_IMP_CHI removal in the EBS decommission on 2026-08-17; index pricing during roll). James says it is acceptable for this model to be indicative (it alone has no reference-price fallback, deliberately); CBOE liquidity may be too thin for stable index pricing and Elan was to ask CBOE. On 2026-10-15 a pricer restart alert showed a recent change to LDN pricerInsti reference markets left CME FX/metals futures (6AZ6, GCZ6, MGCZ6, SIZ6 etc.) with no reference markets, though no base spreads exist for them on LDN/CHI insti anyway; Lee says they are not published to clients.
Next: Toa/Nathan to decide whether the alert for unpriced futures needs suppressing or configuring.
Refs: https://mahifx.slack.com/archives/C035H1VNCAD/p1786949906190919 https://mahifx.slack.com/archives/C035H1VNCAD/p1787003951012219 https://mahifx.slack.com/archives/C035H1VNCAD/p1792028629227619


### chi-hedgers — Toa CHI hedger breaches and CBOE state mismatches
status: open · since: 2026-08-03 · last: 2026-10-22
State: hedgerCBOE1 and hedgerHrpCME1 at Toa CHI keep tripping PnL/firewall/order-breach limits (09-17, 09-27/28, 10-14) and are restarted by whoever is on call; Toa says the PnL firewalls see only the hedger side, so restart is fine when net PnL is healthy (Cameron Copland restarted on 09-17 and 10-14 after checking net PnL; James restarted hedgerCBOE1 again on 10-22). ordersCboe1 state mismatches (price 1.32503 vs 1.325) were referred to CBOE via Argamon; Lee had a code fix ready in the week of 09-29. 09-07 hedgerHrpCME1 crashed on "No rule for converting XAU to ZAR" from a profileDefinitions edit and was fixed by reverting (the audit log is only visible on LDN). 09-27 ordersCME1/ordersCOMEX1 stuck in starting and ordersCOMEXMarex1 awaiting a fix.
Next: Lee to confirm the CBOE state-mismatch code fix shipped and ordersCOMEXMarex1 fixed.
Refs: https://mahifx.slack.com/archives/C035H1VNCAD/p1785757251842839 https://mahifx.slack.com/archives/C035H1VNCAD/p1790649346754469 https://mahifx.slack.com/archives/C035H1VNCAD/p1791982032259119 https://mahifx.slack.com/archives/C035H1VNCAD/p1792683541640309


### platform-ops — Toa box housekeeping, config landmines, capacity
status: open · since: 2026-08-17 · last: 2026-10-11
State: Recurrent config-driven outages: bad liquidityRefreshProfiles entry (GBPUSD typed as Currency) took down distribution gateways and systemStateMonitor on LDN/CHI from 08-20 until removed 08-23; Elan's skew edit removed delegates and pricerInstiLight2 would not start (09-01); an expired MGCQ6 contract in instrumentToProfileMappings blocked propTrader1HrpChi1 (08-30). CHI /app/fx/apps/mahifx hit 90% (mostly model weights incl. dead EBS series); James said delete the EBS data and Nathan added 50GB on 10-11 (about 80%). hazelcastNode OOM on APN1 primary (09-07) tied to the secondary box being decommissioned without unwinding multi-region infra. New LP being set up in TKY (10-14) and new gateways on CHI (09-22). PD licence renewed 08-17.
Next: confirm the leftover EBS model data is actually deleted; unwind multi-region infra from the decommissioned secondary box.
Refs: https://mahifx.slack.com/archives/C035H1VNCAD/p1787462723096659 https://mahifx.slack.com/archives/C035H1VNCAD/p1791220342201259 https://mahifx.slack.com/archives/C035H1VNCAD/p1791711442423979


### xau-invalid-increment — XAU price increment rejects (TOA_CHI, B2PRIME)
status: open · since: 2026-09-09 · last: 2026-10-09
State: On 09-09 TOA_CHI/A_EXTERNAL_WASH rejected 410 XAU orders with INVALID_INCREMENT; Mahi pulled TOA_CHI from the market, changed the increment and re-added it at EOD. On 2026-10-09 B2PRIME XAU orders after the 10-08 rollover were all priced to 3dp and rejected on increment; Shyam asked Argamon to raise it with B2PRIME and Maitrya agreed. A PD incident was also raised in internal-toa-ops.
Next: Argamon to get B2PRIME to price XAU to the right increment; Mahi to confirm rejects stopped.
Refs: https://mahifx.slack.com/archives/C083GP5F1CL/p1788912414279449 https://mahifx.slack.com/archives/C06TW3D8NMV/p1791507691705119


### cfd-indices-rollout — CFDs and indices into Compass (NY4)
status: open · since: 2026-08-24 · last: 2026-10-08
State: Indices (NDX, SPX, DOW, G30) were moved from Jump STP to Compass: G30EUR live 09-10 brokering to Jump, other indices 09-11, A_CFD books added to analytics tables at Argamon's request (done 09-24), CFD internalisation on 09-23 with hybridHedgerCfd1, and skew sizing raised from 0.25x to 0.35x of the Jump benchmark spread on 10-08 (beta now 0.45x, review the following week). Larger flow looks toxic, so a "Broker CFDs - Large" rule brokers trades above $500k (09-30). NAS100 rejections on 09-13 were because Jump published about 70 NDX, too little for the second tier; BMSL pass-through enabled. MT5 drop copy live 08-28; MT4 showed about 131m index volume for August.
Next: Shyam to review 0.45x beta skew; Daria to see whether PSM suits indices.
Refs: https://mahifx.slack.com/archives/C06U76A7ZJR/p1787541873458239 https://mahifx.slack.com/archives/C06U76A7ZJR/p1789003323456489 https://mahifx.slack.com/archives/C06U76A7ZJR/p1791422519718139


### inst-toxic-flow — INST-1 large toxic flow in retail book
status: open · since: 2026-10-05 · last: 2026-10-05
State: INST-1 began trading the NY retail book with large, highly toxic volumes that are internalised under the "Internalise <500k - INST" rule, causing most of the recent PnL drops. Shyam added INST-1 to the Retail Book fast-hedge whitelist on 10-05; no follow-up on whether it worked.
Next: Shyam to review the effect on retail PnL.
Refs: https://mahifx.slack.com/archives/C06U76A7ZJR/p1791171597533909


### ioc-timeouts-chi — XAUUSD IoC orders timed out with no LP response (CHI)
status: watching · since: 2026-10-22 · last: 2026-10-22
State: Between 03:39 and 03:40 UTC on 10-22, 8 XAUUSD orders from the AXI-OZOrders session were brokered to UBS, JPM and DB at Toa CHI and got no ack or execution report, so they timed out and clients were sent cancels. Nathan asked Argamon to check with the LPs whether any were received or filled; Maitrya replied they cannot see the trades on either reactive or Mahi NYC, and Nathan acknowledged. Cause of the missing LP responses is not stated.
Refs: https://mahifx.slack.com/archives/C06TW3D8NMV/p1792644401138689 https://mahifx.slack.com/archives/C06TW3D8NMV/p1792646965509099

### compass-26-4 — Compass 26.3 to 26.4 upgrade
status: watching · since: 2026-09-26 · last: 2026-10-09
State: 26.4 deployed to Toa LDN/CHI and APN1 on 09-26 (aeron inband metadata enabled for KRAKEN as a test). The NY retail env was staged on 10-09 with a weekend restart planned (CHG-2610-FX8E, Argamon told in mahi-argamon-operations); Liam flagged that argamon sets neither widening nor tightening adjustment params, so prices will widen/tighten by one increment on PSM signals after the upgrade and decided to let it go on; James approved the RC.
Next: confirm NY upgrade went live and PSM overlays behaved at the open (no post-restart report seen).
Refs: https://mahifx.slack.com/archives/C035H1VNCAD/p1790435088325269 https://mahifx.slack.com/archives/C06U76A7ZJR/p1791483328149119 https://mahifx.slack.com/archives/C06TW3D8NMV/p1791543787933719

### crypto-pricing — Toa crypto pricing outages and sizes
status: watching · since: 2026-08-19 · last: 2026-09-21
State: No activity since 2026-09-21; downgraded to watching, root cause of the Sunday pauses never posted. Crypto pricing dropped on Sunday 09-13 from about 02:00 UTC (APN1 pricers failed to start after a server reboot; Daria's JsonMapping exception about DefaultIndex OMX not in the name factory) and again on 2026-09-21 ("similar to last Sunday"; William Denny investigating, resolution not posted). Earlier, XBTUSD/ETHJPY/BCHJPY rejects on small quantities (Rakuten micro sizes) were fixed by adding overrides and EOD dist restarts (08-19). Centroid_NY4 MD sessions flapped for about 2 minutes on 09-16.
Next: Toa/Mahi to confirm root cause of the recurring Sunday crypto pauses.
Refs: https://mahifx.slack.com/archives/C06TW3D8NMV/p1787099040590799 https://mahifx.slack.com/archives/C06TW3D8NMV/p1789286838789979 https://mahifx.slack.com/archives/C06TW3D8NMV/p1789997451357139


### xauusd-hedging — XAUUSD hedging, news widening and NFP loss
status: watching · since: 2026-08-14 · last: 2026-09-17
State: No activity since 2026-09-17; downgraded to watching, Argamon was happy after FOMC. XAUUSD risk is held with an arb plus hybrid backstop (arb did over 70% of hedge volume on 08-20; max VaR for the hybrid raised to 8k, Argamon happy with up to $20k; VaRClearance-EOD rule added 08-17). The 09-04 NFP loss (about 30k VaR) was RCA'd: heavy decay, clients closed positions before hedge (52.5m internalised, 13.59m filled vs 16.55m cancelled). After the loss and Jem's push to broker over news, post-news widening on 100-weighted events went from 90s to 180s, news-based MWMS added, and "fill at WSS" was turned off on 09-17 with Jem's approval; Argamon happy with the FOMC result.
Next: Daria owes Argamon a written review of the NFP loss; watch the next big news events.
Refs: https://mahifx.slack.com/archives/C06U76A7ZJR/p1786681733979849 https://mahifx.slack.com/archives/C06U76A7ZJR/p1788530007371599 https://mahifx.slack.com/archives/C06U76A7ZJR/p1789609500783629


### roll-internalise-query — Roll-period trades under internalise rule (DST check)
status: closed · since: 2026-10-23 · last: 2026-10-23 · closed: 2026-10-23
State: Elan asked whether DST changed the ROLL-timezone broker rule after USDCHF trades at roll ran under internalise. Nathan showed they hit the INSTI//Broker Rollover execution profile and were all cancelled, none filled; Elan accepted.
Refs: https://mahifx.slack.com/archives/C06TW3D8NMV/p1792715308732409 https://mahifx.slack.com/archives/C06TW3D8NMV/p1792717939925079

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
