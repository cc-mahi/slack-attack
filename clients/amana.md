---
slug: amana
name: Amana
channels:
  internal: internal-amana
  client: [mahi-amana]
  other: []
refs:
  commercial: ../MahiProduct/data/billing/clients.json  # entry: amana
  hosts: ../MahiProduct/data/client-hosts.json  # entry: amana
  wiki: null  # TODO: ../MahiProduct/wiki/clients/amana.md (doesn't exist yet)
key_people_overrides:
  - {name: "Karen Montero", role: "ops / test trading liaison", confidence: low}
  - {name: "Nikos", role: "primary desk contact — skew config, LR tuning, futures onboarding"}
  - {name: "Princess Rosete", role: "test trading / ops liaison", confidence: low}
last_catchup: 2026-04-23T22:00:00Z
---

Commercial terms, hosting, contract dates → see `refs.commercial`.
Graphite host + s3 slug → see `refs.hosts`.
Everything below is Slack-derived or slack-context-only (not yet in MahiProduct).

## Slack-context cheat sheet

- Distribution markets (LDN): `CLIENT_PRICE_LDN`, `CLIENT_PRICE_ABOOK_LDN`, `CLIENT_PRICE_BETA_LDN`, `DISTRIBUTION_LDN`.
- LP FIX connections: `fixMarketData1`, `fixMarketData2`, `fixMarketDataCentroid`.
- Trade types: `CLIENT_TRADE`, `BROKER_CLIENT_TRADE`, `SPLIT_CLIENT_TRADE`, `AGGRESSIVE_HEDGE_TRADE`, `UNKNOWN_TYPE_TRADE`.
- Party names: `CLIENTS_NET` = client net P&L; `CLIENTS_HEDGING` = hedging P&L; `B_CLIENTS_NET` = B-book client net P&L. 3-party setup — no `SI` / `OFF_BOOK`.
- Futures: XAU/XAG internalised since 2026-04-22, routed to CMC_CENTROID under a separate per-instrument book structure. Bridge sends `GC6{M,J}_→XAUFUT-{M,J}` / `SI6{K,N}_→XAGFUT-{K,N}` on tag 55.

## Recent issues

> [open] 2026-04-23 — Gold skew post instant uplift
> Uplift 2x last week on volume, but skew predictiveness slipped since Wed's instant uplift. Isaac proposing: bump base spread proportion 0.5→1.0, double Twilight base/benchmark, new LDN overrides at 1.2, swap IFMS→IFM. [permalink](https://mahifx.slack.com/archives/C08T42TMKU3/p1776976532606559)

> [open] 2026-04-23 — Silver skew pulled pending investigation
> Silver skew dragging FI PnL down; Will removed while investigating. [permalink](https://mahifx.slack.com/archives/C08T42TMKU3/p1776934554832829)

> [open] 2026-04-23 — CMC XAUUSD latency review (Steerco ask)
> Steerco flagged CMC latency on XAUUSD; Mahi to pull stats. Also on the list: indexes next week, new futures books, start with 121 futures + 121 cash before normalisation. Karen still waiting on email re support. [permalink](https://mahifx.slack.com/archives/C08T42TMKU3/p1776943121111249)

> [open] 2026-04-21 — Nikos requesting daily skew files
> Nikos asking for skew files daily (email or Pulse), wants an ETA even if ~2 weeks out. Awaiting Rory/Will reply. [permalink](https://mahifx.slack.com/archives/C08T42TMKU3/p1776765921428599)

> [open] 2026-04-22 — XAU futs hedger timing on large positions
> Cpty 8004007 generated small PnL drop via XAU futs — hedger took ~30s to cover 512oz. Rory digging into decreasing timing for larger incoming positions. Supersedes prior XAG hedger-wait tuning. [permalink](https://mahifx.slack.com/archives/C08T42TMKU3/p1776860083517709)

> [resolved] 2026-04-22 — XAU + XAG futures internalisation live
> XAU futs live 09:17 BST (first trade internalised + hedged), XAG futs live 13:53 BST. FI yield +10x day-on-day post-changes (2026-04-21). LR levers tuned for new arb cpty 8008699: 1.2 multiplier + 1s rate-limit period (max-reduction $200/M lifted earlier). Profile definitions copied from spot XAG/XAU to fix holding risk too long. [permalink](https://mahifx.slack.com/archives/C08T42TMKU3/p1776845875089209)

> [resolved] 2026-04-13 — dashboard snapshot outage
> Post-release regression from MahiMain commit 066fb9437 (addServiceInBackground race in `riskReportSnapshotRequestPublisher`) stopped AggregateReportStream snapshots; Amana couldn't use the Trading Overview. Justin rolled back the webstack change same day (`512a10b`). Followup on moving `brokerDashboard` to core component still open in #dev. [permalink](https://mahifx.slack.com/archives/C8568C6HG/p1776073126336049)

## Notable topics

- 2026-04-21 — P&L Attribution KB article added (`kbPnlAttribution`) to Compass knowledge base, covering risk-path closed-system P&L, 0→120m/0→20m horizons, and reconciliation vs Account Summary. Driven by Nikos asking for per-client trading PnL attribution. [permalink](https://mahifx.slack.com/archives/C08T42TMKU3/p1776760822802469)
- 2026-04-20 — LP price-withdrawal handling: Centroid now passes through 0/empty MD updates when an LP withdraws price; Will confirmed OK to enable on Mahi side (hedger will keep retrying, client experience preserved). [permalink](https://mahifx.slack.com/archives/C08T42TMKU3/p1776681806903129)
