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
last_catchup: 2026-10-29T07:19:16Z
status: active
---

## Now
Argamon (Afterprime workspace) is growing beyond FX/XAUUSD into CFD indices via Jump (brokered, internalisation and skew now on) and is pushing for 500:1 leverage, which Mahi sims do not clearly support. NY Centroid bridge moved to PXM on the weekend of 2026-09-26; Compass 26.4 went on the weekend of 2026-10-10. Retail NY book is weak: toxic INST-1 flow, XAUUSD news-event hedging cost. On 2026-10-21 the retail FX book moved to a 500k G8 inventory cap (G8-Cap) to support higher leverage; being monitored. On 2026-10-27 Argamon asked for all FX on the new risk model; GTS HRP was pulled from NY pools and hedgers.

## Streams

### hsbc-hrp-pricing — HSBC market data via Reactive not streaming
status: open · since: 2026-10-27 · last: 2026-10-27
State: After HRP asked for an HSBC test trade, Tom enabled pricing through Reactive but Compass showed no HSBC prices (EURUSD included). Tom's settings are now reverted and he sees HSBC EURUSD in Reactive on ARGAMON_SW_HRP and ARGAMON_SW_HRP_2, confirmed as the accounts behind both market data and order sessions. Both HSBC sessions are still logged on in Compass, but the market data stream does not resume until reconnect, so the market data processes need an EOD restart.
Next: Mahi (Cameron Hughes) to restart market data processes at EOD 2026-10-27 and confirm HSBC streams in Compass.
Refs: https://mahifx.slack.com/archives/C06TW3D8NMV/p1793105972763279 https://mahifx.slack.com/archives/C06TW3D8NMV/p1793114025899389

### gts-hrp-nwm-mapping — GTS HRP removal and NWM mapping
status: open · since: 2026-10-27 · last: 2026-10-27
State: NY Compass was sending orders to GTS_HRP, which is no longer active in HRP (Levi, 2026-10-27). Shyam took GTSX_RCTV_HRP_1/2 out of the NY pools and HRP hedgers. 13 trades (118 oz XAUUSD) were actually executed at GTS via NWM, with drop copies split between HRP and NWM; Argamon will honour and manually book them at NWM, so Compass needed no change (only the LP label differs; per-LP reconciliation vs NWM needs mapping). There is no GTS-via-NWM market in Compass; Mahi offered to set one up if Argamon wants to keep trading GTS through NWM. Separately Levi asked for the NW market data gateway restart to stream GTS_NW_LDN in LD Compass; Daria fixed it and pricing is now visible.
Next: Argamon to say whether it wants a GTS via NWM market in Compass.
Refs: https://mahifx.slack.com/archives/C06TW3D8NMV/p1793062310809789 https://mahifx.slack.com/archives/C06TW3D8NMV/p1793075092211549

### leverage-risk-sims — 500:1 leverage / more risk-holding sims
status: open · since: 2026-08-31 · last: 2026-10-27
State: Jem/Elan say retail growth is blocked without 500:1 leverage (most capped at 100:1); a separate in-house prop-style challenge product was floated earlier. On 2026-10-21 Shyam, agreed with Jem, switched the retail FX book to a G8-Cap hedging profile (up to 500k inventory cap on internalised G8 flow, Friday close flatten); replay vs old rules showed +$62k (about $1/M), average G8 risk $0.91m to $1.26m with much smaller peaks. Rollback is swapping instrumentToProfileMappings G8-Cap to G8 and restarting hybridHedgerHrp1. On the 2026-10-27 call Jem and Elan gave no timeline for higher leverage, want Mahi to lead on internalising more flow profitably (eventually all their clients), and want all FX, not just G8, on the new risk model; Elan suggested dark pool hedging (XTX) for NY4, but Daria noted Mahi dropped it in recent months for paying spread there, suggesting looser VaR clearance/backstop rules and checking fill rate and time to fill (Elan says Toa fills are good, ~5 min to fill). INST-tagged retail flow can go to Chi if too toxic.
Next: Shyam to sim all-FX on the new risk model and look into dark pool hedging for NY4; William Denny to monitor the G8-Cap book; Argamon to confirm Centroid LP failover is still in place.
Refs: https://mahifx.slack.com/archives/C06U76A7ZJR/p1788152543060319 https://mahifx.slack.com/archives/C06U76A7ZJR/p1792552125427929 https://mahifx.slack.com/archives/C06U76A7ZJR/p1793068905149339

### toa-chi-ioc-timeouts — LP no-ack timeouts on Toa CHI
status: open · since: 2026-10-22 · last: 2026-10-22
State: Between 03:39:48 and 03:40:05 UTC on 2026-10-22, 8 XAUUSD orders from the AXI-OZOrders session, brokered to UBS, JPM and DB, got no ack or execution report and timed out on Mahi's side (clients sent cancels). Nathan asked Argamon to check with the LPs whether any were received or filled; Maitrya replied they cannot see the trades at reactive or Mahi NYC. Cause of the missing acks is not yet identified.
Next: Nathan to find why the LPs sent no acks (not seen posted).
Refs: https://mahifx.slack.com/archives/C06TW3D8NMV/p1792644401138689 https://mahifx.slack.com/archives/C06TW3D8NMV/p1792646373306319

### centroid-ny-to-pxm — Centroid bridge IP change and NY PXM migration
status: open · since: 2026-06-09 · last: 2026-10-28
State: Argamon NY moved its bridge from Centroid to PXM on the 2026-09-26/27 weekend (ZD 23532; retail dist sessions connected 2026-09-27). The Centroid bridge IP has changed again, to 192.229.22.160 (Tom McLean, 2026-10-21): it sits outside the 192.229.23.x range the Beeks cross-connect route covers, so Centroid must advertise it over the cross-connect. Shyam raised NOCINT-856420 with Beeks and ZD 23672. Tom has no firm date for the move to the new IP (it was due last month). Mahi infra change CHG-2610-HSJB (approved 2026-10-28): Tokyo link cutover on Sat 2026-10-31 10:00-11:00Z will drop Centroid FIX sessions for up to 60 min. Earlier: Wintermute queried 2026-09-09 whether altcrypto connectivity via Mahi was down; Kate confirmed the decommission was agreed.
Next: Argamon (Tom) to give the Centroid move date; Shyam/Beeks to confirm the route change for 192.229.22.160; Argamon to be aware of the 2026-10-31 Centroid session drop.
Refs: https://mahifx.slack.com/archives/C06TW3D8NMV/p1781000635571119 https://mahifx.slack.com/archives/C06U76A7ZJR/p1793206534345309

### lucera-hard-timeout — Lucera LD fill latency and hard timeout
status: open · since: 2026-10-18 · last: 2026-10-19
State: Levi questioned an EURUSD buy on the Lucera LD distribution session filled over 120ms after placement; Argamon wants to match Lucera's 90ms expiry. Nathan explained expiry is the per-FIX-session hardTimeoutLength on fixClientConnection (currently 80ms) and a HARD_TIMEOUT comment means the timeout fired: internalised orders cancel, brokered orders fill if the pool price still crosses (it did, 1.11891 vs limit 1.11892). The fill was at 80ms in Compass but the execution report went out 42ms later, so the delay looks internal to Toa; Nathan is investigating and Levi has the FIX messages to take to Lucera.
Next: Nathan to find the cause of the 42ms gap between fill and execution report.
Refs: https://mahifx.slack.com/archives/C06TW3D8NMV/p1792362870440649 https://mahifx.slack.com/archives/C06TW3D8NMV/p1792375513540999

### cfd-indices-rollout — CFD / indices via Jump into Compass
status: open · since: 2026-08-24 · last: 2026-10-08
State: Indices (G30EUR, then NDX/DOW/SPX) went live 2026-09-10/11 brokered to Jump after the Jump OZ connection was re-established and MT5 drop copy went live (2026-08-28); internalisation on from 2026-09-23, and Argamon analytics tables now include the A_CFD books. Shyam raised CFD skew sizing in prod to 0.35x of benchmark spread on 2026-10-08 (beta at 0.45x, review next week), added a Broker CFDs - Large rule for >$500k notional (2026-09-30) and added INST-1 to the Retail Book fast-hedge whitelist (2026-10-05).
Next: Shyam reviews 0.45x beta skew next week; Argamon wanted internal reconciliations to account for Mahi internalisation (status not seen).
Refs: https://mahifx.slack.com/archives/C06U76A7ZJR/p1787541873458239 https://mahifx.slack.com/archives/C06TW3D8NMV/p1787702895306119 https://mahifx.slack.com/archives/C06U76A7ZJR/p1791422519718139

### pxm-ldn-toa — Toa LDN and PXM connectivity
status: open · since: 2026-07-21 · last: 2026-10-08
State: Toa LDN sessions to Argamon's PXM: ClientID via tag 448/452=3 was configured 2026-07-21; the Toa crypto session to PXM LD lost sequence numbers on 2026-09-20 (reset requested; running over internet pending xconnect). On 2026-10-08 two simultaneous XAUUSD orders showed different fills; Levi found PXM keeps price improvement by default and will configure it to pass all slippage through to the client, then re-enable on 2026-10-09; James agreed PXM should pass orders through unmodified.
Next: Levi to confirm the PXM config change worked; xconnect for the crypto session.
Refs: https://mahifx.slack.com/archives/C06TW3D8NMV/p1784590345336939 https://mahifx.slack.com/archives/C06TW3D8NMV/p1789872139334399 https://mahifx.slack.com/archives/C06TW3D8NMV/p1791464526120859

### retail-toxic-flow — Retail NY book PnL and toxic flow
status: open · since: 2026-07-24 · last: 2026-10-05
State: Retail NY volume is down roughly 50% month on month (2026-07) and the book has been weak; INST-1 started trading with large, highly toxic volumes and the Internalise <500k - INST rule means Mahi took the hit. Shyam added INST-1 to the Retail Book fast-hedge whitelist on 2026-10-05; weekly PnL was $18k in the week to 2026-08-20 but noted as lucky on XAUUSD moves.
Next: Watch whether the whitelist reduces the PnL drops.
Refs: https://mahifx.slack.com/archives/C06U76A7ZJR/p1784863388281539 https://mahifx.slack.com/archives/C06U76A7ZJR/p1791171597533909

### toa-crypto-stability — Crypto pricing outages and sizing on Toa
status: watching · since: 2026-08-19 · last: 2026-09-21
State: Downgraded to watching, no activity since 2026-09-21. Crypto min-quantity rejects (XBTUSD 0.03, BCHJPY, ETHJPY/XETUSD defaults of 1.0) were fixed via overrides and EOD restarts on 2026-08-19 (Rakuten micro sizes). Major crypto pricing stopped from Toa on 2026-09-13 after a server reboot left processes down, and again on 2026-09-21 ("similar to last Sunday"); William Denny said it was being resolved but no root cause was posted for the second occurrence.
Next: Root cause and prevention for the Sunday crypto pauses owed to Argamon.
Refs: https://mahifx.slack.com/archives/C06TW3D8NMV/p1787099040590799 https://mahifx.slack.com/archives/C06TW3D8NMV/p1789287085078259 https://mahifx.slack.com/archives/C06TW3D8NMV/p1789997451357139

### xauusd-hedging-risk — XAUUSD hedging, news events, VaR
status: watching · since: 2026-05-18 · last: 2026-09-17
State: Downgraded to watching, no activity since 2026-09-17. Hybrid hedger plus arb (arb doing >70% of XAUUSD hedge volume as of 2026-08-20), max VaR raised to 8k on 2026-08-19 with Argamon fine up to $20k; a VaRClearance-EOD rule at 10% of max VaR was added 2026-08-17. The NFP drop on 2026-09-04 (30k VaR, small loss) was RCA'd as client volume decaying faster than hedging; after calls with Jem the post-news widening on 100-weighted events was extended 90s -> 180s, news-based MWMS widens toward hedging cost, and fill-at-WSS was turned off on 2026-09-17, with Jem having suggested brokering over news instead. Toa CHI was pulled from the hedger (2026-08-19) over ~10ms latency to CHI.
Next: Daria owes Argamon a write-up of the NFP loss (as of 2026-09-07; not seen sent).
Refs: https://mahifx.slack.com/archives/C06U76A7ZJR/p1779116545067019 https://mahifx.slack.com/archives/C06U76A7ZJR/p1788530007371599 https://mahifx.slack.com/archives/C06U76A7ZJR/p1789609500783629

### compass-26-4-upgrade — Compass 26.4 upgrade and deploys
status: watching · since: 2026-08-17 · last: 2026-10-13
State: Argamon moved 26.3 to 26.4 at the 2026-10-10/11 weekend restart (approved by James at RC #7224); known pricing change: with no adjustmentSignalParametersForWidening/Tightening set, prices move by one increment on PSM-W/PSM-T signals, Liam decided to let it go on. Infra main to NYC and a dashboard component deploy (2026-10-13) followed. No post-upgrade issues seen in the window.
Next: Watch PSM widening/tightening effect on pricing.
Refs: https://mahifx.slack.com/archives/C06U76A7ZJR/p1786964189701069 https://mahifx.slack.com/archives/C06U76A7ZJR/p1791483328149119 https://mahifx.slack.com/archives/C06U76A7ZJR/p1791866233863029

### client-exec-queries — Execution and pricing questions from ops
status: watching · since: 2026-08-17 · last: 2026-10-09
State: Recurring one-off ops questions. Tom's slippage query (2026-08-17) was last look and AUDUSD signals were smoothed; Sep 3 liquidity reduction on order 042dr11e8ch was picked up by Rory (outcome not seen); the 624ms order book age (2026-09-10) was a timestamp artefact, not stale price. 2026-09-01 pricerInstiLight2 went down after Elan removed skew delegates (Nathan restored it); 2026-10-09 Shyam asked Argamon to raise B2PRIME 3dp XAU invalid-increment rejects with the LP (Argamon said they would).
Next: Argamon to raise B2PRIME increments; Rory outcome on the 2026-09-03 liquidity reduction.
Refs: https://mahifx.slack.com/archives/C06TW3D8NMV/p1786964549641859 https://mahifx.slack.com/archives/C06TW3D8NMV/p1789022941524499 https://mahifx.slack.com/archives/C06TW3D8NMV/p1791507691705119

### fx-pricing-tuning — LP sets, signals and direct pricing
status: watching · since: 2026-05-04 · last: 2026-09-01
State: AUDCAD priced directly from 2026-08-25 (5th most traded in Compass); XAUUSD arb min inception raised to -$5/M (2026-08-31); NZDUSD reference, signal, BMSL and MWMS markets got UBS and COMZ added after an AUDNZD FI loss (2026-09-01), to cut erratic mids over roll. Earlier LP-set and mid work (EURUSD mid, XAU/EUR/GBP reference selectors) is background.
Refs: https://mahifx.slack.com/archives/C06U76A7ZJR/p1777855717442529 https://mahifx.slack.com/archives/C06U76A7ZJR/p1787623926715189 https://mahifx.slack.com/archives/C06U76A7ZJR/p1788229484766809

### roll-broker-profile — Roll-period trades under internalise query
status: closed · since: 2026-10-23 · last: 2026-10-23 · closed: 2026-10-23
State: Elan asked whether daylight saving had flipped ROLL-timezone FX from broker to internalise, having seen clock times rather than session names in the execution rule. Nathan found the USDCHF roll trades hit the INSTI/Broker Rollover profile, and none were filled (all cancelled), so no rule change; Elan acknowledged.
Refs: https://mahifx.slack.com/archives/C06TW3D8NMV/p1792715308732409 https://mahifx.slack.com/archives/C06TW3D8NMV/p1792717939925079

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
