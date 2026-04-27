---
slug: valutrades
refs:
  vibepulse: ../VibePulse/.claude/clients/valutrades.yaml
  billing: ../MahiProduct/data/billing/clients.json     # entry: valutrades
  hosts: ../MahiProduct/data/client-hosts.json          # entry: valutrades
  wiki: null                                             # ../MahiProduct/wiki/clients/valutrades.md (not yet)
channels_override: ["internal-valutrades", "mahi-valutrades", "mahi-valutrades-operations"]   # -operations is a distinct operations channel not in VibePulse yaml
key_people_overrides:
  - {name: "Andri", role: "client trading ops — algo connections, rejects", confidence: low}
last_catchup: 2026-04-27T09:35:00Z
---

## Recent issues

> [open] 2026-04-25 — Post-26.3 deploy: `analyticsFixServerValutradesMT4` down on valutrades-ln-trading-1
> Restart fails with `MT4/5 Analytics Order connections must have positionReportMetaTraderServer configured in their connectivity.FixTradeAnalyticsSettings`. Leonardo flagged that the analytics sessions under `connectivity.fix.outbound.session` have `FixTradeAnalyticsSettings` but no `positionReportMetaTraderServer` — asking how this should be set. No reply visible. [permalink](https://mahifx.slack.com/archives/CP7A1F8BT/p1777122260901519)

> [open] 2026-04-25 — Post-26.3 deploy: `signalProxyTx1` crashing on valutrades-ny-trading-1 — duplicate consumer
> `MarketMetaDataSubscriber.SIGNALS_NYC2: Consumer for 393 already registered: AFM-Broker. New consumer AFM-Signal` — caused by a new code default in `signalsToPublish`. Leonardo workaround: global override on `connectivity.marketData.marketMetadata.proxy.coe.signalsToPublish`; process is back up. Asked for confirmation this is the right fix or if there's a better one. [permalink](https://mahifx.slack.com/archives/CP7A1F8BT/p1777123880055949)

> [open] 2026-04-23 — Surya Strait algo connection not live — tag to send unclear
> Andri asked about connection status for the Surya Strait algo and what tag to send; Isaac + Daria investigating, Daria asked Andri to clarify which connection. No resolution visible in the 24h window. [permalink](https://mahifx.slack.com/archives/C09HN93T0G2/p1776918937609649)

> [open] 2026-04-23 — TT reject on UBS Algo Gold order — `Exceeds max product long position`
> Andri reported Gold (GCM6) algo order rejected by TT with `3: TT: Exceeds max product long position`; Kate supplied the raw FIX pair for investigation (TT_POV strategy, 162 contracts, UBS Algo cpty). Needs follow-up on position-limit config. [permalink](https://mahifx.slack.com/archives/C09HN93T0G2/p1776949025272839)

## Notable topics
