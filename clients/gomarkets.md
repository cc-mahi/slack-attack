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
last_catchup: 2026-04-27T09:35:00Z
---

## Recent issues

> [open] 2026-04-27 — Centroid bridge: Mahi maker disconnect at 2026-04-25 19:46:53 UTC — 2h FX-pricing gap at GoMarkets day-open
> Regina: Centroid lost FX pricing for the first two hours of the day; logs show Mahi maker initiated logout at the disconnect time, then refused logon attempts until restart. Fixed Centroid-side by restarting the bridge — Centroid then logged in cleanly. Kate ack'd, NZ public holiday so investigation deferred. Pair with the gateway-side fix from earlier weekend incidents. [permalink](https://mahifx.slack.com/archives/C09J1DP2QQH/p1777274504232569)

> [open] 2026-04-23 — XAUUSD DIST_NYC client-position discrepancy (~1.4koz vs actual exposure)
> Erik reports client positions on DIST_NYC are ~1.4k oz less than actual exposure on XAU. Root cause: client trades filled against OZ failover when Mahi execution had issues — Tapaas keeps tracking client-side, Mahi doesn't. LP positions still aligned at Mahi level. Erik has isolated most of the missing trades since April and is proposing a 30-min corrective-import automation. William: "we'll look into that". [permalink](https://mahifx.slack.com/archives/C09J1DP2QQH/p1776964441437749)

## Notable topics

- 2026-04-23 — All Books tenant profile migration: Isaac confirmed All Books and legacy profiles co-exist; execution rules now use All Books exclusively. All Books is a soft reset that will populate further over time. [permalink](https://mahifx.slack.com/archives/C09J1DP2QQH/p1776909525989209)
