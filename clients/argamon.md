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
last_catchup: 2026-10-15T12:57:40Z
status: active
---

## Now
Argamon (Afterprime workspace) is growing beyond FX/XAUUSD into CFD indices via Jump (brokered, internalisation and skew now on) and is pushing for 500:1 leverage, which Mahi sims do not clearly support. NY Centroid bridge moved to PXM on the weekend of 2026-09-26; Compass 26.4 went on the weekend of 2026-10-10. Retail NY book is weak: toxic INST-1 flow, XAUUSD news-event hedging cost.

## Streams

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

### leverage-risk-sims — 500:1 leverage / more risk-holding sims
status: open · since: 2026-08-31 · last: 2026-09-22
State: Jem/Elan say retail growth is blocked without 500:1 leverage (most capped at 100:1) and are exploring options up to B-booking, plus a separate in-house prop-style challenge product. Daria's sims (Compass, SI, inventory, B book) do not clearly support changing risk management; 2026-09-22 call showed FX-only internalisation as the best option so far, Argamon to review and say how much risk they will open up, and they want Mahi advice on leverage levels and instruments. Logged in the MahiProduct wiki client requests.
Next: Argamon to come back on risk appetite; Mahi to run further instrument-group and smaller-account sims.
Refs: https://mahifx.slack.com/archives/C06U76A7ZJR/p1788152543060319 https://mahifx.slack.com/archives/C06U76A7ZJR/p1788499126033959 https://mahifx.slack.com/archives/C06U76A7ZJR/p1790047491374069

### toa-crypto-stability — Crypto pricing outages and sizing on Toa
status: open · since: 2026-08-19 · last: 2026-09-21
State: Crypto min-quantity rejects (XBTUSD 0.03, BCHJPY, ETHJPY/XETUSD defaults of 1.0) were fixed via overrides and EOD restarts on 2026-08-19 (Rakuten micro sizes). Major crypto pricing stopped from Toa on 2026-09-13 after a server reboot left processes down, and again on 2026-09-21 ("similar to last Sunday"); William Denny said it was being resolved but no root cause was posted for the second occurrence.
Next: Root cause and prevention for the Sunday crypto pauses owed to Argamon.
Refs: https://mahifx.slack.com/archives/C06TW3D8NMV/p1787099040590799 https://mahifx.slack.com/archives/C06TW3D8NMV/p1789287085078259 https://mahifx.slack.com/archives/C06TW3D8NMV/p1789997451357139

### xauusd-hedging-risk — XAUUSD hedging, news events, VaR
status: open · since: 2026-05-18 · last: 2026-09-17
State: Hybrid hedger plus arb (arb doing >70% of XAUUSD hedge volume as of 2026-08-20), max VaR raised to 8k on 2026-08-19 with Argamon fine up to $20k; a VaRClearance-EOD rule at 10% of max VaR was added 2026-08-17. The NFP drop on 2026-09-04 (30k VaR, small loss) was RCA'd as client volume decaying faster than hedging; after calls with Jem the post-news widening on 100-weighted events was extended 90s -> 180s, news-based MWMS widens toward hedging cost, and fill-at-WSS was turned off on 2026-09-17, with Jem having suggested brokering over news instead. Toa CHI was pulled from the hedger (2026-08-19) over ~10ms latency to CHI.
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

### centroid-ny-to-pxm — NY bridge migration Centroid to PXM
status: watching · since: 2026-06-09 · last: 2026-09-29
State: Argamon NY moved its bridge from Centroid to PXM (Centroid UAT FIX work since 2026-06 was the lead-in); IP whitelisting via Beeks sorted 2026-09-24 and Daria confirmed retail dist sessions connected on 2026-09-27 after the weekend migration (ZD 23532). Internally James says Centroid has been poor for them and Elan negotiated PXM terms for months; Mahi's own bridge was pitched but lacks margin/reporting. Wintermute queried on 2026-09-09 whether altcrypto connectivity via Mahi was down; Kate confirmed the decommission was agreed earlier.
Next: nothing outstanding seen; downgraded to watching, no post-migration issues in the window.
Refs: https://mahifx.slack.com/archives/C06TW3D8NMV/p1781000635571119 https://mahifx.slack.com/archives/C06U76A7ZJR/p1790353314143069 https://mahifx.slack.com/archives/C06U76A7ZJR/p1790673025680519

### fx-pricing-tuning — LP sets, signals and direct pricing
status: watching · since: 2026-05-04 · last: 2026-09-01
State: AUDCAD priced directly from 2026-08-25 (5th most traded in Compass); XAUUSD arb min inception raised to -$5/M (2026-08-31); NZDUSD reference, signal, BMSL and MWMS markets got UBS and COMZ added after an AUDNZD FI loss (2026-09-01), to cut erratic mids over roll. Earlier LP-set and mid work (EURUSD mid, XAU/EUR/GBP reference selectors) is background.
Refs: https://mahifx.slack.com/archives/C06U76A7ZJR/p1777855717442529 https://mahifx.slack.com/archives/C06U76A7ZJR/p1787623926715189 https://mahifx.slack.com/archives/C06U76A7ZJR/p1788229484766809

## Arc
- 2026-06-26 — TraderEvolution discontinued; Argamon retail clients moved to MT5
- 2026-08-24 — Argamon asks for weekly calls again; plan to bring indices into Compass
- 2026-08-28 — MT5 drop copy live for Argamon
- 2026-08-31 — Argamon exploring 500:1 leverage and B-booking; Mahi starts risk sims
- 2026-09-10 — G30EUR live, brokered to Jump; other indices follow 2026-09-11
- 2026-09-23 — CFD internalisation switched on
- 2026-09-27 — NY bridge moved from Centroid to PXM
- 2026-10-11 — Compass 26.4 live at weekend restart
