---
slug: toa-argamon
refs:
  vibepulse: ../VibePulse/.claude/clients/toa-argamon.yaml
  billing: null
  hosts: ../MahiProduct/data/client-hosts.json          # entry: toa-argamon
  wiki: null
channels_override: null
key_people_overrides:
  - {name: "Tom McLean", role: "Argamon-side analyst — primary day-to-day contact in mahi-argamon-operations", confidence: low}
  - {name: "Levi", role: "Argamon ops — give-up / rejection queries", confidence: low}
  - {name: "Joanna", role: "Argamon-side ops — recurring contact in mahi-argamon-operations for alerts and client trade queries", confidence: low}
last_catchup: 2026-05-01T23:59:59Z
---

## Status

- **Stage:** live (Argamon is a client of Toa; LDN/APN1/CHI single-box setups)
- **Integration:** Mahi infra hosting Toa-Argamon distribution across LDN, APN1, CHI. NY4→CHI brokering went live 2026-04-08.
- **Relationship:** downstream of Toa. Slack: `internal-argamon`, `mahi-argamon-operations`. Tom McLean (Argamon-side) is asking detailed questions across pricing, brokering and rejections — relationship is engaged and ops-heavy.

## Recent issues

> [resolved] 2026-05-01 — XAUUSD retail losses from sharp/sniping flow; DFSN signal added; signal-follow whitelist cleaned
> Isaac identified XAUUSD retail losses from 2026-04-30 caused by signal-follow clients sniping sharp moves in pricing. Affected counterparties moved back to broker-only classification (signal-follow whitelist cleaned). DFSN signal rule added to the pricing model to widen Mahi out of the way during large moves. Separate from but related to the CME hedging brokering test (2026-04-28 open issue). [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1746063187834529)

> [resolved] 2026-05-01 — Wide spread on majors (~15:00 BST); LR kicking in on published rate
> Tom flagged EURUSD at ~20 ticks wide for a couple of hours with no client complaints yet. Will identified LR kicking in on the published rate — removed from published, spread immediately restored. [permalink](https://mahifx.slack.com/archives/C06TW3D8NMV/p1746107990556329)

> [resolved] 2026-05-01 — JPY crypto LMAX position risk at rollover (non-issue)
> Tom wanted LMAX removed from JPY crypto hedging/STP ahead of anticipated large JPY financing charge at rollover. Amir confirmed with Isaac that JPY crypto pairs are weekend-only for hedging and are not STP'd — no position should build regardless. No config change needed. [permalink](https://mahifx.slack.com/archives/C06TW3D8NMV/p1746087135603309)

> [open] 2026-04-28 — XAUUSD brokered counterparties expansion to test CME hedging
> Daria added counterparty 104881 to be brokered to Toa, working through softest first (104881, 105048, 105153, 105681, 105773) to evaluate whether hedging XAUUSD to CME helps. Ongoing. https://mahifx.slack.com/archives/C06U76A7ZJR/p1777335260425589

> [resolved] 2026-04-22 — XAUUSD signal switched synapse → neuron
> Shyam moved XAUUSD from synapse to neuron model to reduce spiky pricing; also cited better skew PnL over the last month. https://mahifx.slack.com/archives/C06U76A7ZJR/p1776832052585769

> [open] 2026-04-20 — USDCAD ask-price spike, over-weighting HSBC mid
> Tom flagged order 012dr52nxnb filled at 1.371 while market was around 1.370; only HSBC was deviating. Daria confirmed other mid-formation LPs (LMAX_DIRECT_NY_RETAIL, XTXM_RCTV_HRP_2, GTSX_RCTV_HRP_1, NWM_RCTV_HRP_1) were unavailable so HSBC was sole source. Tom asked Elan re. adding COMZ and other non-skew-protective LPs into mid; no answer yet. https://mahifx.slack.com/archives/C06TW3D8NMV/p1776694811277649

> [resolved] 2026-04-21 — EURHUF indicative pricing; Commerz added
> Daria flagged EURHUF going indicative on/off (2026-04-17), proposed adding LPs into price formation just for that pair. Tom preferred Jane St + Commerz. Shyam added Commerz on 2026-04-21; backtests showed it stops the indicative pricing. https://mahifx.slack.com/archives/C06TW3D8NMV/p1776394647886729

> [open] 2026-04-15 — DB filtered out for small-ticket FX brokering (NWPB min size)
> Tom queried order 012dr82osqn filling via UBS not DB despite both being highlighted. Isaac explained DB was filtered because client order was 5k vs the 15k min-ticket on Mahi's NWPB FX hedger config. James noted Natwest has min ticket sizes and that work with Reactive on a direct setup will remove the constraint. Tom raised whether a 15k floor is justifiable for small-volume auto-brokered clients. Direct-Reactive setup is the in-flight remediation. https://mahifx.slack.com/archives/C06TW3D8NMV/p1776233897732439

> [resolved] 2026-04-13 — Missed give-up to HRP (3 EURUSD trades, one not given up)
> Levi reported HRP saw only 2 of 3 trades give up; HRP manually booked the missing one. Daria pulled the FIX AE messages — all three appear to have been sent from Mahi side. Tom said he'd check with HRP; no further messages, treating as resolved on Mahi side. https://mahifx.slack.com/archives/C06TW3D8NMV/p1776034785118149

> [resolved] 2026-04-13 — First-5min market-open EXPIRED / REJECTSYSTEMERROR RAT bursts
> Levi flagged a quantity of rejected orders at market open. Daria identified cancels/rejects clustered after the first 5min, particularly AUDCAD CAD crosses; brokering rules cancelled them because market data wasn't being received yet (Jane Street AUDCAD MD started at 21:10). RATE_LIMIT_EXCEEDED was hit due to retries — 150 orders/sec/counterparty cap. https://mahifx.slack.com/archives/C06TW3D8NMV/p1776049759858249

> [watching] 2026-04-13 — Wide pricing persisting > 1h after rollover
> Tom raised wide pricing in the post-rollover hour, asking for any improvements. No response captured in the window. https://mahifx.slack.com/archives/C06TW3D8NMV/p1776042834123209

> [open] 2026-04-13 — Centroid LDN distribution backpressure (~10s delays)
> James dug in: Centroid backpressuring (TCP rx window shrinks, zero-window notifications on port 4047, retransmissions on 4031), causing queue on Mahi side. Centroid consume snapshots not increments which compounds at high msg rates. ECB-speech burst hit ~5,000 FIX msgs/sec across both pricing sessions, more than Centroid's receive buffer could drain. Mahi-side publish latency was fine (~0.065ms mean). New /pcap-analysis VibePulse skill referenced. May affect other local NY clients too. https://mahifx.slack.com/archives/C06U76A7ZJR/p1776116671694999

> [resolved] 2026-04-08 — NY4 → CHI brokering live
> Daria flipped on brokering to CHI from NY4. Watching for orders from the counterparties Elan selected. https://mahifx.slack.com/archives/C06U76A7ZJR/p1775686974874039

> [open] 2026-04-02 — Non-flat LP MXN exposure with no client MXN positions
> Tom noticed non-flat LP exposure in USDMXN/EURMXN despite no client positions; was moving exposure from HRP to NWM for better swap rates. Daria explained: hedgers only trade USDMXN, so a client whose classification changed mid-position would have one leg brokered through EURMXN and one internalised + hedged via USDMXN. Cleared Tom to close out so long as net MXN unchanged, asked he do it through Compass or notify. Tom acknowledged but deferred to "next week" (2026-04-03), no follow-up captured in the window. https://mahifx.slack.com/archives/C06TW3D8NMV/p1775139754817979

## Notable topics

- Mid-formation LP set under review — Tom and Daria are both pushing to broaden the price-formation LP set (COMZ, Jane Street) to reduce dependency on HSBC and to fix per-pair indicatives. Decision still sitting with Elan.
- Reactive direct setup is the strategic remediation for NWPB (Natwest) min-ticket-size filtering of small client orders. Flagged in 2026-04-15 thread; no eta.
- Centroid LDN distribution issues are a CTO-level dig (James Furness) — backpressure root-caused via pcap; further work likely needed and may generalise to other NY-local clients distributing via Centroid.
- XAUUSD sharp-flow / signal-follow risk — signal-follow whitelist cleaned 2026-05-01 and DFSN signal added to retail pricing model. May need monitoring if similar sniping recurs.
