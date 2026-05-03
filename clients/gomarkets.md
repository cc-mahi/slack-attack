---
slug: gomarkets
refs:
  vibepulse: ../VibePulse/.claude/clients/gomarkets.yaml
  billing: ../MahiProduct/data/billing/clients.json     # entry: gomarkets
  hosts: ../MahiProduct/data/client-hosts.json          # entry: gomarkets
  wiki: null                                             # ../MahiProduct/wiki/clients/gomarkets.md (not yet)
channels_override: null
key_people_overrides:
  - {name: "Erik", role: "client ops — reconciliation / position discrepancies", confidence: low}
  - {name: "Mac", role: "client ops — tenant profile / All Books migration", confidence: low}
  - {name: "Regina", role: "client ops — Centroid bridge / FIX session incidents", confidence: low}
  - {name: "David", role: "client ops — execution-rule / pricing-model questions", confidence: low}
last_catchup: 2026-05-03T07:17:21Z
---

## Recent issues

> [open] 2026-04-29 — Radex AUDCAD/AUDNZD/NZDCAD slippage complaint — LR + LL PnL pattern on FX crosses
> Erik (GoMarkets) reports Radex accounts seeing "slippage" on AUD/CAD, AUD/NZD, NZD/CAD. His own analysis: LR active (expected — they trade simultaneously) plus LL PnL we recapture since PI is off on FX-crosses execution rules; LL amount at 150ms appears to grow on AUDNZD when orders execute via Dynamic Signal Follow, and the cross prices look reactive/zig-zag versus smoother LP feeds. Asking whether we can smooth the price or add liquidity to reduce LR effect. Nathan replied: LR is applied directly into published price (not represented as slippage; LL is) via the liquidity throttle toggle on B_CLIENTS_RA; PI is intentionally off on Radex so client always fills at worst price during last-look window. Drilled into a -$42 LL counterparty 63193567/AUDNZD, showed the -$18 trade was actually +PnL for us via internalisation. Backtest: our mid follows triangulated LP mids; we price tighter than all LPs; offer skews slightly from the no-arb protection node. Erik thanked, asked William to revert with findings — William: "we'll review and revert". [permalink](https://mahifx.slack.com/archives/C09J1DP2QQH/p1777474386410269)

> [resolved] 2026-04-29 — XAGUSD offer spike at 23:44:35 UTC dragged by MAHI_CONTINUITY_NYC
> William flagged a large XAGUSD spike caused by MAHI_CONTINUITY_NYC offer spiking and pulling our offer up. Isaac diagnosed: legacy no-arb pricing config for XAGUSD was using MAHI_CONTINUITY_NYC mid as a safety net; current mid-formation config makes that redundant. Isaac removed the no-arb config; William confirmed "should be good now". [permalink](https://mahifx.slack.com/archives/C09J1DP2QQH/p1777422105899199)

> [watching] 2026-04-28 — David (client) asking about "internalise on indicative mid + continuity-pool failover" toggle
> Client (David) opened a discussion on the execution-rule flag that allows internalisation when the pricing model is indicative and pricing has failed over to the continuity pool. He noted the docs strongly recommend leaving it off, while Mahi has it enabled across most profiles. Daria explained: the flag was previously off but had to be turned on to get orders filled; the pricing-model-indicative condition is what gates the continuity pool publishing, the rule then decides whether fills are allowed against it. Daria flagged you could disable it on more toxic counterparties (so they'd fail to fill if they failed over to continuity, even when exiting). No action yet — educational; client may follow up with profile-specific tuning request. [permalink](https://mahifx.slack.com/archives/C09J1DP2QQH/p1777340162333429)

> [resolved] 2026-04-27 — Centroid bridge: Mahi maker disconnect at 2026-04-25 19:46:53 UTC — 2h FX-pricing gap at GoMarkets day-open
> Regina: Centroid lost FX pricing for the first two hours of the day; logs show Mahi maker initiated logout at the disconnect time, then refused logon attempts until restart. Fixed Centroid-side by restarting the bridge — Centroid then logged in cleanly. Kate Stagg (Centroid, 2026-04-27 18:10 UTC) confirmed that the GoMarkets-B-Prices-Centroid session received no logon request within session timings; the other three sessions (A-Prices, A-Orders, B-Orders) all logged on cleanly at 21:00:00 UTC on 2026-04-26. Last logon attempt seen on B-Prices was 2026-04-25 19:46:58 UTC; nothing further until the bridge restart at 2026-04-26 22:53:59 UTC. Kate suggested Centroid look at why the bridge stopped retrying that one session while the other three kept going. Pair with the gateway-side fix from earlier weekend incidents. [permalink](https://mahifx.slack.com/archives/C09J1DP2QQH/p1777313446640279)

> [open] 2026-04-23 — XAUUSD DIST_NYC client-position discrepancy (~1.4koz vs actual exposure)
> Erik reports client positions on DIST_NYC are ~1.4k oz less than actual exposure on XAU. Root cause: client trades filled against OZ failover when Mahi execution had issues — Tapaas keeps tracking client-side, Mahi doesn't. LP positions still aligned at Mahi level. Erik has isolated most of the missing trades since April and is proposing a 30-min corrective-import automation. William: "we'll look into that". [permalink](https://mahifx.slack.com/archives/C09J1DP2QQH/p1776964441437749)

## Notable topics

- 2026-04-23 — All Books tenant profile migration: Isaac confirmed All Books and legacy profiles co-exist; execution rules now use All Books exclusively. All Books is a soft reset that will populate further over time. [permalink](https://mahifx.slack.com/archives/C09J1DP2QQH/p1776909525989209)
