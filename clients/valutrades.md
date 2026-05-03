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
  - {name: "Neil Whitehead", role: "client data/tech — backtesting, MySQL/Pulse queries", confidence: low}
last_catchup: 2026-05-03T07:07:50Z
---

## Recent issues

> [open] 2026-04-30 — `riskPathValutrades` on valutrades-ny-admin-1 throwing 14k+ errors/day — `CLIENT_PRICE_ICDX_MINI_NYC` unavailable
> Justin Young investigating why `CLIENT_PRICE_ICDX_MINI_NYC` is set as `defaultClientPriceMarket` for USOUSD and a large instrument list (NDFUSD, CL1USD, CO1USD, DOWUSD, NDXUSD, JPFUSD, SPFUSD, DJFUSD, HSFUSD, SPXUSD, UKXGBP, HSIHKD, JPXJPY, G30EUR); riskPath throwing `IllegalArgumentException: CLIENT_PRICE_ICDX_MINI_NYC/<sym> unavailable` at 14k+/day. No resolution in window. [permalink](https://mahifx.slack.com/archives/CP7A1F8BT/p1777544417254539)

> [resolved] 2026-04-28 — Yield profiles negative/incorrect for cpty 92549025 — fix deployed 2026-05-02
> Garry flagged incomplete chart data for SPXUSD on VALUTRADES_B_CLIENTS (operations channel); Andri also chasing on yield profiles for cpty 92549025 in the trading channel. Issue re-escalated 2026-04-30 — still appearing on 2026-04-29 data. Justin Young confirmed fix requires a weekend release. Justin posted "Release complete" 2026-05-02 18:30 BST. [ops-link](https://mahifx.slack.com/archives/C09HN93T0G2/p1777373692703529) [trading-link](https://mahifx.slack.com/archives/CSLM3Q8AD/p1777445407538749) [re-escalation](https://mahifx.slack.com/archives/CSLM3Q8AD/p1777530647177429) [fix-ETA](https://mahifx.slack.com/archives/CSLM3Q8AD/p1777623275661629) [release-complete](https://mahifx.slack.com/archives/CSLM3Q8AD/p1777743032175839)

> [resolved] 2026-05-02 — MySQL data gap on 2026-01-30 — 6-hour window backfilled
> Neil Whitehead flagged a 6-hour gap on 2026-01-30 remaining after the earlier backfill (which covered 2026-01-01→2026-01-29). Sam Hewitt confirmed the gap is now corrected. Follow-on to the April archiver retention fix. [client-flag](https://mahifx.slack.com/archives/C09HN93T0G2/p1777750823493739) [fix-confirm](https://mahifx.slack.com/archives/C09HN93T0G2/p1777786213688159)

> [resolved] 2026-04-30 — MySQL data archiving — January ExternalOrder data backfilled, retention bumped to 365 days
> Client (Neil Whitehead) reported January data missing after archiver default changed to 90-day retention. Sam Hewitt backfilled 386,250 rows (2026-01-01→2026-01-29) from Pulse parquet into PROD_LIVE_CLIENTDB on 192.81.111.24, and bumped ORDER_HISTORY daysToRetain 90→365. Client confirmed working. [escalation](https://mahifx.slack.com/archives/C09HN93T0G2/p1777543312438289) [resolution](https://mahifx.slack.com/archives/C09HN93T0G2/p1777602765022229)

> [open] 2026-04-25 — Post-26.3 deploy: `analyticsFixServerValutradesMT4` down on valutrades-ln-trading-1
> Restart fails with `MT4/5 Analytics Order connections must have positionReportMetaTraderServer configured in their connectivity.FixTradeAnalyticsSettings`. Leonardo flagged that the analytics sessions under `connectivity.fix.outbound.session` have `FixTradeAnalyticsSettings` but no `positionReportMetaTraderServer` — asking how this should be set. No reply visible. [permalink](https://mahifx.slack.com/archives/CP7A1F8BT/p1777122260901519)

> [open] 2026-04-25 — Post-26.3 deploy: `signalProxyTx1` crashing on valutrades-ny-trading-1 — duplicate consumer
> `MarketMetaDataSubscriber.SIGNALS_NYC2: Consumer for 393 already registered: AFM-Broker. New consumer AFM-Signal` — caused by a new code default in `signalsToPublish`. Leonardo workaround: global override on `connectivity.marketData.marketMetadata.proxy.coe.signalsToPublish`; process is back up. Asked for confirmation this is the right fix or if there's a better one. [permalink](https://mahifx.slack.com/archives/CP7A1F8BT/p1777123880055949)

> [open] 2026-04-23 — Surya Strait algo connection not live — tag to send unclear
> Andri asked about connection status for the Surya Strait algo and what tag to send; Isaac + Daria investigating, Daria asked Andri to clarify which connection. No resolution visible in the 24h window. [permalink](https://mahifx.slack.com/archives/C09HN93T0G2/p1776918937609649)

> [open] 2026-04-23 — TT reject on UBS Algo Gold order — `Exceeds max product long position`
> Andri reported Gold (GCM6) algo order rejected by TT with `3: TT: Exceeds max product long position`; Kate supplied the raw FIX pair for investigation (TT_POV strategy, 162 contracts, UBS Algo cpty). Needs follow-up on position-limit config. [permalink](https://mahifx.slack.com/archives/C09HN93T0G2/p1776949025272839)

> [resolved] 2026-04-28 — TT POV algo: gold time-window changed to 120 min
> Andri changed POV algo parameters via the trading-tech config UI (Liam confirmed dynamic, no restart needed). [permalink](https://mahifx.slack.com/archives/C09HN93T0G2/p1777352230999959)

## Notable topics
