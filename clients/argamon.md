---
slug: argamon
aliases: []
refs:
  vibepulse: ../VibePulse/.claude/clients/argamon.yaml
  billing: ../MahiProduct/data/billing/clients.json     # entry: argamon
  hosts: ../MahiProduct/data/client-hosts.json          # entry: argamon
  wiki: ../MahiProduct/wiki/clients/argamon.md
channels:
  internal-argamon: C06U76A7ZJR
  mahi-argamon-operations: C06TW3D8NMV
contacts:
  - {name: "Elan Bension", role: "Argamon principal / decision-maker", confidence: low}
  - {name: "Jem (Jeremy)", role: "Argamon exec on calls with Elan; drives leverage / B-book strategy, surname unknown", confidence: low}
  - {name: "Levi Ulman", role: "Argamon ops / connectivity (PXM, Jump, Centroid)", confidence: low}
  - {name: "Tom McLean", role: "Argamon ops / daily trading monitoring", confidence: low}
  - {name: "Hafiz Mehmood", role: "Argamon back-office / analytics tables", confidence: low}
  - {name: "Maitrya Anupam", role: "Argamon ops (copied on bridge migration)", confidence: low}
last_catchup: 2026-11-27T08:14:57Z
status: active
---

## Now
Argamon (Afterprime workspace) is growing beyond FX/XAUUSD into CFD indices via Jump (brokered, internalisation and skew now on) and is pushing for 500:1 leverage, which Mahi sims do not clearly support. NY Centroid bridge moved to PXM on the weekend of 2026-09-26; Compass 26.4 went on the weekend of 2026-10-10. Retail NY book is weak: toxic INST-1 flow, XAUUSD news-event hedging cost. On 2026-10-21 the retail FX book moved to a 500k G8 inventory cap (G8-Cap) to support higher leverage; being monitored. On 2026-10-27 Argamon asked for all FX on the new risk model; GTS HRP was pulled from NY pools and hedgers. Toa last-look tolerance 0 (from 2026-10-28) was reset on 2026-11-03 and TOA_CHI is back in gold hedging; on the 2026-11-02 call Argamon asked to extend cap internalisation beyond G8 (250k), explore B-booking soft CPs, and try PSM in beta.

## Streams

### leverage-risk-sims — 500:1 leverage / more risk-holding sims
status: open · since: 2026-08-31 · last: 2026-11-27
State: Jem/Elan say retail growth is blocked without 500:1 leverage (most capped at 100:1). Retail FX book has been on a G8-Cap profile (500k inventory cap on internalised G8 flow, Friday close flatten) since 2026-10-21; rollback is swapping instrumentToProfileMappings G8-Cap to G8 and restarting hybridHedgerHrp1. After the 2026-10-27 call Argamon wants all FX on the new risk model and dark pool hedging explored. On the 2026-11-02 call Jem and Elan asked to extend cap internalisation beyond G8 with a 250k cap on other currencies (Shyam's sims show roughly PnL-neutral, closer to supporting higher leverage), to hold past 500k for soft-looking CPs, and to try full B-book for some soft-flow CPs (Shyam says little such flow exists; Argamon sounded interested in an A-book/B-book model). They are very open to PSM: Shyam to run it in beta with comparative sims, go-ahead if average spread and related metrics hold; Elan may want it at Toa too. Elan is sending CBOE session credentials for hidden peg hedging, to be trialled in NY4; on 2026-11-09 Shyam flagged that ordersCboe1 and marketDataCboe1 were being set up, so expect related alerts. On 2026-11-09 Shyam extended cap internalisation to the liquid EMs (CNH, ZAR, SGD, MXN) with a 250k cap and 500k hard backstop, same setup as G8; a 6-month replay is slightly positive to neutral on PnL, and the remaining FX was left out as it gets under $0.1M combined. On the 2026-11-10 call Jem and Elan were happy with last week's performance and the direction of more internalisation, want more internalisation opportunities explored (including fully B-bookable flow), and want the gold internalisation strategy reviewed as it is losing on reval. On 2026-11-15 Shyam said Beeks support had told him sales would contact Mahi about an NY4 cross-connect to Cboe (NOCINT-861001) but nothing has arrived, and asked whether anyone else heard. On the 2026-11-16/17 call Jem and Elan agreed they need wider gold spreads to be profitable on gold (gold hedging/news-event risk is tracked here now, max VaR 8k, post-news widening 180s, fill-at-WSS off since 2026-09-17), are happy to push LR harder for bursty flow (no big-client complaints since LR went to $15/M at Toa; retail is $4/M), to be ramped incrementally, and are happy with the 6-12c beta XAU PSM spread range (16 Nov: published 7.71c vs 8.05c in prod, charged 8.43c vs 8.18c); Shyam wants to smooth the spread fluctuations first and move it to prod probably the week of 2026-11-23, aiming for a similar average published spread from LR plus PSM. On 2026-11-17 the Channel LR on XAU was tightened from 500k surplus, 250k/500ms to 150k surplus, 75k/500ms (Shyam proposed, Jem agreed and tightened further). On the 2026-11-24 call Jem wanted to try full B-book on some tags Compass has classified as B-book; Cboe hidden peg hedging was quoted at 99 GBP/month if not already covered by the current Toa Argamon Beeks SO (Elan thinks it will be quite beneficial); and FX internalisation caps may rise from 500k to 1M. On 2026-11-26 Shyam proposed the XAU PSM setup to Jem (pending approval): 3-month sim shows about +$5.4k spread earned (+2.7%, roughly +$1.05/M), average published spread 8.25c vs 9.11c and average charged 9.77c vs 8.89c, a safe start with widening to be increased over time. Same day he reported a strong week: retail +$30.9k on $937M (+$32.99/M) vs a 3-month weekly average of +$13.51/M, CFD +$4.9k on $252M (+$19.23/M), volume 2.2x usual (about half from one new gold client that started 2026-11-10, plus AUDCAD copy trading at 12% of retail volume), gold LR +$11.05/M vs +$4.33/M average after the 150k tightening, and positive reval +$11.7k vs a -$1.7k average. On 2026-11-26 Shyam noted Beeks are adding the Cboe cross-connect routes to argamon-ny-trading-1 and -2 over the weekend of 2026-11-27/29, before the weekly reboots, with no change to the Toa connection (NOCINT-863225, replacing the earlier unanswered NOCINT-861001 query). On 2026-11-27 Shyam removed whale counterparty 84000303 from the retail book fast-hedge whitelist as its flow looks soft again, to be monitored next week.
Next: Jem to approve the XAU PSM setup; Shyam to sim whether SI on B-book-classified tags is profitable, move some quotes and orders sessions from HRP to NWPB once Reactive confirms a window, and look into raising FX internalisation caps from 500k to 1M; Shyam to smooth beta XAU PSM spreads and move to prod, ramping LR incrementally; Beeks to complete the Cboe cross-connect this weekend (NOCINT-863225); Shyam to monitor the retail book after the whale whitelist removal; Shyam to look for further internalisation and full B-book flow, review the gold internalisation strategy, check configurability of holding past 500k, put PSM in beta with sims, and trial hidden peg hedging in NY4 once credentials arrive; Argamon to confirm Centroid LP failover is in place.
Refs: https://mahifx.slack.com/archives/C06U76A7ZJR/p1788152543060319 https://mahifx.slack.com/archives/C06U76A7ZJR/p1794193748388459 https://mahifx.slack.com/archives/C06U76A7ZJR/p1794778517811549 https://mahifx.slack.com/archives/C06U76A7ZJR/p1795748476687579

### gts-hrp-nwm-mapping — GTS HRP removal and NWM mapping
status: open · since: 2026-10-27 · last: 2026-11-27
State: NY Compass was sending orders to GTS_HRP, which is no longer active in HRP (Levi, 2026-10-27). Shyam took GTSX_RCTV_HRP_1/2 out of the NY pools and HRP hedgers. 13 trades (118 oz XAUUSD) were actually executed at GTS via NWM, with drop copies split between HRP and NWM; Argamon will honour and manually book them at NWM, so Compass needed no change (only the LP label differs; per-LP reconciliation vs NWM needs mapping). There is no GTS-via-NWM market in Compass; Mahi offered to set one up if Argamon wants to keep trading GTS through NWM. Separately Levi asked for the NW market data gateway restart to stream GTS_NW_LDN in LD Compass; Daria fixed it and pricing is now visible. GTS has been dark in Argamon NY pricing references and XAUUSD arb protection since 2026-10-27; change CHG-2611-PA7W (Shyam, awaiting approval, weekend window pending in ZD 23769) remaps the Reactive sessions so the GTS LP moves to NatWest PB, to be applied Sun 2026-11-15 05:00-17:00Z during Sunday checks, after which GTS returns to those references once it ticks on sessions 2 and 4. A further change, CHG-2611-9CS8 (Shyam, 2026-11-27, window Fri 27 Nov 01:30Z to Sun 29 Nov 21:00Z), renames the GTS markets to NatWest and adds Jane to the wide lists.
Next: Approvers to approve CHG-2611-PA7W and agree the weekend window; Shyam to apply it and confirm GTS ticks on sessions 2 and 4; Argamon to say whether it wants a GTS via NWM market in Compass.
Refs: https://mahifx.slack.com/archives/C06TW3D8NMV/p1793062310809789 https://mahifx.slack.com/archives/C06TW3D8NMV/p1793075092211549 https://mahifx.slack.com/archives/C06U76A7ZJR/p1795742597884209

### client-exec-queries — Execution and pricing questions from ops
status: open · since: 2026-08-17 · last: 2026-11-26
State: Recurring one-off ops questions. Tom's slippage query (2026-08-17) was last look and AUDUSD signals were smoothed; Sep 3 liquidity reduction on order 042dr11e8ch was picked up by Rory (outcome not seen); the 624ms order book age (2026-09-10) was a timestamp artefact, not stale price. 2026-09-01 pricerInstiLight2 went down after Elan removed skew delegates (Nathan restored it); 2026-10-09 Shyam asked Argamon to raise B2PRIME 3dp XAU invalid-increment rejects with the LP (Argamon said they would). 2026-11-04 Tom asked where the net volume limit config lives after a 600oz XAUUSD trade group was throttled well below the 100,000 base units/ms setting; James pointed to the Execution Rule and distribution.liquidityThrottle.netVolumeLimitingProfile, explaining it is a small amount and most rules use Don't Cancel, which only extends to the max last-look delay on a buy/sell imbalance so trades can be repriced. The Catch-All profile (not Scope) triggered; James advised setting all profiles to Don't Cancel unless flow is very toxic, and Elan agreed. On 2026-11-20 Tom asked why a Toa LDN client buy (order group 042dr11mg3n) was rejected "Internalisation Disabled IoC expired" when external liquidity looked available; Daria found the client order was FOK and no LP in the pool accepts FOKs, and suggested the client send IOCs or enabling top-up on the execution rule so partial fills can be topped up to a full FOK fill. Elan enabled top-up. On 2026-11-26 James forwarded an HRP booking issue (two XAGUSD confirms rejected "No forward route"); Tom said it was his test account for seeing drop values and had already asked HRP to cancel the drops.
Next: Tom to monitor FOK handling after top-up; Tom to set Catch-All to Don't Cancel; Argamon to raise B2PRIME increments; Rory outcome on the 2026-09-03 liquidity reduction.
Refs: https://mahifx.slack.com/archives/C06TW3D8NMV/p1786964549641859 https://mahifx.slack.com/archives/C06TW3D8NMV/p1789022941524499 https://mahifx.slack.com/archives/C06TW3D8NMV/p1793795725289139 https://mahifx.slack.com/archives/C06TW3D8NMV/p1795704982274269

### cfd-indices-rollout — CFD / indices via Jump into Compass
status: open · since: 2026-08-24 · last: 2026-11-26
State: Indices (G30EUR, then NDX/DOW/SPX) went live 2026-09-10/11 brokered to Jump after the Jump OZ connection was re-established and MT5 drop copy went live (2026-08-28); internalisation on from 2026-09-23, and Argamon analytics tables now include the A_CFD books. Shyam raised CFD skew sizing in prod to 0.35x of benchmark spread on 2026-10-08 (beta at 0.45x, review next week; raised to 0.45x in prod on 2026-11-26 for DOW, NDX, SPX and G30, est. +$150/week, watching for arbing), added a Broker CFDs - Large rule for >$500k notional (2026-09-30) and added INST-1 to the Retail Book fast-hedge whitelist (2026-10-05).
On 2026-11-09 Jump (via OZ) asked, through Levi, how Mahi would connect if the cross-connect fails and the Jump sessions must fail over via the internet. Shyam said the internet path would come from a different source IP than the cross-connect, asked for an internet endpoint for the Jump hub (host, ports, whether plain TCP is possible) to add as a backup host on both sessions, and suggested a short failover test with OZ; Levi will pass Mahi's public IP to Jump for whitelist confirmation.
Next: Levi to get Jump to confirm the whitelist and supply the internet failover endpoint, then Shyam to add the backup host and test; Shyam to watch the 0.45x CFD skew for arbing; Argamon wanted internal reconciliations to account for Mahi internalisation (status not seen).
Refs: https://mahifx.slack.com/archives/C06U76A7ZJR/p1787541873458239 https://mahifx.slack.com/archives/C06U76A7ZJR/p1791422519718139 https://mahifx.slack.com/archives/C06TW3D8NMV/p1794189940988869 https://mahifx.slack.com/archives/C06U76A7ZJR/p1795727529239549

### jane-street-ny4 — Jane Street setup on NY4 via Reactive
status: open · since: 2026-11-23 · last: 2026-11-23
State: Levi chased Mahi on 2026-11-23 for an update on the Reactive Markets request to set up Jane Street on NY4 (handled by email, request already raised). Rory replied that he will check the status and revert.
Next: Rory to check the status and revert to Levi.
Refs: https://mahifx.slack.com/archives/C06TW3D8NMV/p1795423330035409 https://mahifx.slack.com/archives/C06TW3D8NMV/p1795425066327019

### centroid-ny-to-pxm — Centroid bridge IP change and NY PXM migration
status: open · since: 2026-06-09 · last: 2026-11-16
State: Argamon NY moved its bridge from Centroid to PXM on the 2026-09-26/27 weekend (ZD 23532; retail dist sessions connected 2026-09-27). The Centroid bridge IP has changed again, to 192.229.22.160 (Tom McLean, 2026-10-21): it sits outside the 192.229.23.x range the Beeks cross-connect route covers, so Centroid must advertise it over the cross-connect. Shyam raised NOCINT-856420 with Beeks and ZD 23672. Tom has no firm date for the move to the new IP (it was due last month). Mahi infra change CHG-2610-HSJB (approved 2026-10-28): Tokyo link cutover on Sat 2026-10-31 10:00-11:00Z will drop Centroid FIX sessions for up to 60 min. Earlier: Wintermute queried 2026-09-09 whether altcrypto connectivity via Mahi was down; Kate confirmed the decommission was agreed. On 2026-11-13 Afterprime reported retail MT4/MT5 down for about ten minutes; Rory showed the Centroid bridge retail price connection went quiet at 16:01:02 UTC, Mahi's test request and then the session failed at 16:01:51 for lack of acks, and Centroid did not log back in until 16:11:02 UTC (prices resumed immediately; the retail order session stayed up and nothing restarted on Mahi's side). Nevio will ask Centroid why it stalled and took nine minutes to reconnect. On 2026-11-16 Shyam flagged the Centroid UAT price session (Argamon-Centroid-UAT-Prices) dropping and reconnecting frequently, apparently Centroid UAT falling behind on the stream; live Centroid sessions are fine and Levi is checking with Centroid.
Next: Nevio and Levi to get Centroid's explanation for the 2026-11-13 stall and the UAT drops; Argamon (Tom) to give the Centroid move date; Shyam/Beeks to confirm the route change for 192.229.22.160; Argamon to be aware of the 2026-10-31 Centroid session drop.
Refs: https://mahifx.slack.com/archives/C06TW3D8NMV/p1781000635571119 https://mahifx.slack.com/archives/C06U76A7ZJR/p1793206534345309 https://mahifx.slack.com/archives/C06TW3D8NMV/p1794589247435179 https://mahifx.slack.com/archives/C06TW3D8NMV/p1794794780957499

### lucera-hard-timeout — Lucera LD fill latency and hard timeout
status: open · since: 2026-10-18 · last: 2026-11-02
State: Levi questioned an EURUSD buy on the Lucera LD distribution session filled over 120ms after placement; Argamon wants to match Lucera's 90ms expiry. Nathan explained expiry is the per-FIX-session hardTimeoutLength on fixClientConnection (currently 80ms) and a HARD_TIMEOUT comment means the timeout fired: internalised orders cancel, brokered orders fill if the pool price still crosses (it did, 1.11891 vs limit 1.11892). The fill was at 80ms in Compass but the execution report went out 42ms later, so the delay looks internal to Toa; Nathan is investigating and Levi has the FIX messages to take to Lucera.
On 2026-11-02 Levi asked which FIX tag populates the counterparty ID for CLIENTS_HRP_LUCERA on LD Compass; Daria said it uses tag 109 if present, else falls back to tag 1 plus 448, and Levi will clean up the tags with Lucera.
Next: Nathan to find the cause of the 42ms gap between fill and execution report.
Refs: https://mahifx.slack.com/archives/C06TW3D8NMV/p1792362870440649 https://mahifx.slack.com/archives/C06TW3D8NMV/p1793602642195049

### compass-26-4-upgrade — Compass 26.4 upgrade and deploys
status: watching · since: 2026-08-17 · last: 2026-10-13
State: Argamon moved 26.3 to 26.4 at the 2026-10-10/11 weekend restart (approved by James at RC #7224); known pricing change: with no adjustmentSignalParametersForWidening/Tightening set, prices move by one increment on PSM-W/PSM-T signals, Liam decided to let it go on. Infra main to NYC and a dashboard component deploy (2026-10-13) followed. No post-upgrade issues seen in the window.
Next: Watch PSM widening/tightening effect on pricing.
Refs: https://mahifx.slack.com/archives/C06U76A7ZJR/p1786964189701069 https://mahifx.slack.com/archives/C06U76A7ZJR/p1791483328149119 https://mahifx.slack.com/archives/C06U76A7ZJR/p1791866233863029

### pxm-ldn-toa — Toa LDN and PXM connectivity
status: watching · since: 2026-07-21 · last: 2026-10-08
State: Downgraded to watching, no activity since 2026-10-08. Toa LDN sessions to Argamon's PXM: ClientID via tag 448/452=3 was configured 2026-07-21; the Toa crypto session to PXM LD lost sequence numbers on 2026-09-20 (reset requested; running over internet pending xconnect). On 2026-10-08 two simultaneous XAUUSD orders showed different fills; Levi found PXM keeps price improvement by default and will configure it to pass all slippage through to the client, then re-enable on 2026-10-09; James agreed PXM should pass orders through unmodified.
Next: Levi to confirm the PXM config change worked (not seen); xconnect for the crypto session.
Refs: https://mahifx.slack.com/archives/C06TW3D8NMV/p1784590345336939 https://mahifx.slack.com/archives/C06TW3D8NMV/p1789872139334399 https://mahifx.slack.com/archives/C06TW3D8NMV/p1791464526120859

### retail-toxic-flow — Retail NY book PnL and toxic flow
status: watching · since: 2026-07-24 · last: 2026-10-05
State: Downgraded to watching, no activity since 2026-10-05. Retail NY volume is down roughly 50% month on month (2026-07) and the book has been weak; INST-1 started trading with large, highly toxic volumes and the Internalise <500k - INST rule means Mahi took the hit. Shyam added INST-1 to the Retail Book fast-hedge whitelist on 2026-10-05; weekly PnL was $18k in the week to 2026-08-20 but noted as lucky on XAUUSD moves.
Next: Watch whether the whitelist reduces the PnL drops.
Refs: https://mahifx.slack.com/archives/C06U76A7ZJR/p1784863388281539 https://mahifx.slack.com/archives/C06U76A7ZJR/p1791171597533909

### hsbc-hrp-pricing — HSBC market data via Reactive not streaming
status: closed · since: 2026-10-27 · last: 2026-10-27 · closed: 2026-11-27
State: No activity since 2026-10-27; assumed resolved (EOD restart outcome not seen). After HRP asked for an HSBC test trade, Tom enabled pricing through Reactive but Compass showed no HSBC prices (EURUSD included). Tom's settings are now reverted and he sees HSBC EURUSD in Reactive on ARGAMON_SW_HRP and ARGAMON_SW_HRP_2, confirmed as the accounts behind both market data and order sessions. Both HSBC sessions are still logged on in Compass, but the market data stream does not resume until reconnect, so the market data processes need an EOD restart.
Refs: https://mahifx.slack.com/archives/C06TW3D8NMV/p1793105972763279 https://mahifx.slack.com/archives/C06TW3D8NMV/p1793114025899389

### toa-chi-ioc-timeouts — LP no-ack timeouts on Toa CHI
status: closed · since: 2026-10-22 · last: 2026-10-22 · closed: 2026-11-24
State: No activity since 2026-10-22; assumed resolved (cause of the missing acks never posted). Between 03:39:48 and 03:40:05 UTC on 2026-10-22, 8 XAUUSD orders from the AXI-OZOrders session, brokered to UBS, JPM and DB, got no ack or execution report and timed out on Mahi's side (clients sent cancels). Nathan asked Argamon to check with the LPs whether any were received or filled; Maitrya replied they cannot see the trades at reactive or Mahi NYC. Cause of the missing acks is not yet identified.
Refs: https://mahifx.slack.com/archives/C06TW3D8NMV/p1792644401138689 https://mahifx.slack.com/archives/C06TW3D8NMV/p1792646373306319

### toa-crypto-stability — Crypto pricing outages and sizing on Toa
status: closed · since: 2026-08-19 · last: 2026-09-21 · closed: 2026-11-24
State: No activity since 2026-09-21; assumed resolved. Crypto min-quantity rejects (XBTUSD 0.03, BCHJPY, ETHJPY/XETUSD defaults of 1.0) were fixed via overrides and EOD restarts on 2026-08-19 (Rakuten micro sizes). Major crypto pricing stopped from Toa on 2026-09-13 after a server reboot left processes down, and again on 2026-09-21 ("similar to last Sunday"); William Denny said it was being resolved but no root cause was posted for the second occurrence.
Refs: https://mahifx.slack.com/archives/C06TW3D8NMV/p1787099040590799 https://mahifx.slack.com/archives/C06TW3D8NMV/p1789287085078259 https://mahifx.slack.com/archives/C06TW3D8NMV/p1789997451357139

### xauusd-hedging-risk — XAUUSD hedging, news events, VaR
status: closed · since: 2026-05-18 · last: 2026-09-17 · closed: 2026-11-17
State: merged into leverage-risk-sims.
Refs: https://mahifx.slack.com/archives/C06U76A7ZJR/p1779116545067019 https://mahifx.slack.com/archives/C06U76A7ZJR/p1789609500783629

## Arc
- 2026-06-26 — TraderEvolution discontinued; Argamon retail clients moved to MT5
- 2026-08-24 — Argamon asks for weekly calls again; plan to bring indices into Compass
- 2026-08-28 — MT5 drop copy live for Argamon
- 2026-08-31 — Argamon exploring 500:1 leverage and B-booking; Mahi starts risk sims
- 2026-09-10 — G30EUR live, brokered to Jump; other indices follow 2026-09-11
- 2026-09-23 — CFD internalisation switched on
- 2026-09-27 — NY bridge moved from Centroid to PXM
- 2026-10-11 — Compass 26.4 live at weekend restart
- 2026-10-21 — Retail FX book moved to G8-Cap (500k internalised inventory cap) to support higher leverage
