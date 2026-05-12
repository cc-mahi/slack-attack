---
slug: atc
refs:
  vibepulse: ../VibePulse/.claude/clients/atc.yaml
  billing: ../MahiProduct/data/billing/clients.json     # entry: atc
  hosts: ../MahiProduct/data/client-hosts.json          # entry: atc
  wiki: ../MahiProduct/wiki/clients/atc-brokers.md
channels_override: null
key_people_overrides: []
last_catchup: 2026-05-12T07:24:37Z
---

## Recent issues

> [open] 2026-05-11 — GBPUSD open loss $1.8k; Finalto TOB quantity mismatch; remediation options pending ATC decision
> At market open 2026-05-11, client 27072237 traded GBPUSD at a tighter-than-market spread: Finalto had dropped published quantity to 100k while the model was publishing 300k at TOB, leaving no LP reference at that size and triggering base spreads. Daria proposed four options: (1) reduce TOB qty to 100k; (2) widen base spreads for the first hour (collateral impact); (3) add BMSL/MAHI_BENCHMARK_LDN as reference market; (4) implement a new benchmark-widening type that references smaller quantities. Malik asked whether the hedger could have exited at a lower level to limit the loss; Daria confirmed the hedger cleared the risk fine but the problem was in pricing at execution time (~3s window). Awaiting ATC's preferred approach. [client permalink](https://mahifx.slack.com/archives/C04AZM0LPMH/p1778473221775049) · [Daria options reply](https://mahifx.slack.com/archives/C04AZM0LPMH/p1778534112919499) · [internal TOB analysis](https://mahifx.slack.com/archives/C046RNF64VD/p1778473279858959)

> [open] 2026-05-08 — David Manoukian unable to access LN Compass admin portal after IP whitelisting
> Despite IP `47.41.47.224` being whitelisted (Notable Topics 2026-05-08), David still couldn't reach `atc-ln-admin-1.96yb.prod.mahimarkets.com:8400`. Inald Gjoni ran diagnostics (Test-NetConnection + tracert to `46.235.34.67:8400`), results sent to Beeks. David suspected his own security configuration. No resolution confirmed in window. [client permalink](https://mahifx.slack.com/archives/C04AZM0LPMH/p1778253602532909)

> [open] 2026-05-07 — SI book losing Feb–now; owner unresolved
> Andrew Morgan reviewed account summary and noted ATC SI book has been losing every month from February to present. He couldn't identify the responsible party ("there's an action there for someone I just dont know who"). Thread handed off to Cameron Hughes (Analyst) to pick up. No root-cause or fix in this window. [permalink](https://mahifx.slack.com/archives/C046RNF64VD/p1778157088950569)

> [resolved] 2026-05-06 — LP position adjustment applied in Compass
> Malik (ATC) posted a screenshot requesting an LP action-item adjustment between LPs. Rory confirmed the adjustments were reflected in Compass at 13:52 UTC 2026-05-06; Malik acknowledged. [client thread](https://mahifx.slack.com/archives/C04AZM0LPMH/p1778074242656559)

> [open] 2026-05-05 — G30 hedger / CFD position rec; CFD positions not received weekend 10–11 May; deferred to next weekend
> Daria found G30 hasn't been hedging (causing a small loss) and noticed unexplained position divergences: HOUSE G30 = 3.03, G30EUR = -72.87; CFD_CLIENTS_NET G30EUR = -193.27. No adjustments visible to explain the gap — suspected NY-env trades not reflected in current env. Daria attempted to align currency positions with trade positions to get the hedger firing. ATC (David Manoukian) sent EOD position snapshots (client + Velocity) ~22:10 BST 2026-05-05; Daria confirmed positions are mostly in line at the risk-managed level — divergence is in non-risk-managed books. Biggest diff: DOWUSD $62k USD equivalent; G30EUR out $4.5m in trade positions (not risk managed). Daria requested equivalent snapshots post-market-close Friday/weekend to tidy non-risk-managed positions Sunday before open; full rec planned Monday morning before market open. 2026-05-06 13:51 UTC: Rory turned off hedgers for manual booking — executing the planned rec. **2026-05-11 update**: ATC did not send CFD positions over the weekend 10–11 May so the alignment could not be completed. Daria will prompt ATC again later this week to attempt the rec next weekend. [internal permalink](https://mahifx.slack.com/archives/C046RNF64VD/p1777950282470059) · [client channel](https://mahifx.slack.com/archives/C04AZM0LPMH/p1777950007103569) · [fix attempt](https://mahifx.slack.com/archives/C046RNF64VD/p1777954959642469) · [EOD snapshot review](https://mahifx.slack.com/archives/C04AZM0LPMH/p1778026541590429) · [internal rec plan](https://mahifx.slack.com/archives/C046RNF64VD/p1778026160390939) · [hedgers off for manual booking](https://mahifx.slack.com/archives/C046RNF64VD/p1778075469343699) · [CFD positions not received](https://mahifx.slack.com/archives/C046RNF64VD/p1778472694422579)

> [resolved] 2026-04-23 — Finalto order 022dt22vmy status unknown (session disconnect)
> Daria asked Finalto to confirm the status of XAUUSD order 022dt22vmy (4oz sell, limit 0.0). Session dropped right after the order was sent; Compass got no confirmation/fill/cancel. Malik raised with Finalto; confirmed rejected (Cancel-on-Disconnect — `39=8`, `58=Unknown ClientOrderId`) at 08:04 UTC. Daria acknowledged 2026-04-27. [permalink](https://mahifx.slack.com/archives/C04AZM0LPMH/p1776931341977529) · [resolution](https://mahifx.slack.com/archives/C04AZM0LPMH/p1776958997299589)

> [resolved] 2026-04-30 — EUR reconciliation report action item (transient position mismatch)
> Malik flagged an action item on the reconciliation report showing a EUR position mismatch. Cameron investigated: likely a transient Compass book position caught mid-report. Malik confirmed the report cleared ~2 hours later; no outside-Compass manual trades on ATC's side. [permalink](https://mahifx.slack.com/archives/C04AZM0LPMH/p1777554973786509)

## Notable topics

- 2026-05-11 — EURUSD position action item self-cleared. Malik flagged an action item showing on the reconciliation report since UK open (client position 8,145,494 EURUSD). Kate investigated; Malik followed up ~4.5h later saying it had cleared up and ATC would look into the cause. [permalink](https://mahifx.slack.com/archives/C04AZM0LPMH/p1778516831373549)

- 2026-05-08 — David Manoukian IP change whitelisted. David requested new IP `47.41.47.224` whitelisted for Compass access; Daria confirmed; Sam Hewitt confirmed whitelisting complete and requested David test the connection. [permalink](https://mahifx.slack.com/archives/C04AZM0LPMH/p1778186391756579)

- 2026-05-07 — Echo brokered-flow yield query bug fixed. Andrew flagged `-$4k` brokered P&L for April. Justin Young traced it to incorrect party filter on the external brokering books Echo query (too broad — included all hedging books, not just `A_EXTERNAL_WASH`). Correctly scoped query shows ATC made `+$6k` from brokering in April. Justin committed fix to MahiMain ([3e168531](https://github.com/MahiFX/MahiMain/commit/3e168531459ea980a7d86e017aa7590e1d92f2a4)); deploy pending as of 15:00 UTC 2026-05-07. [permalink](https://mahifx.slack.com/archives/C046RNF64VD/p1778156587156009)

- 2026-05-07 — Jan SI P&L Graphite discrepancy resolved (data artefact). Account summary showed `$337k` Jan SI P&L; Graphite `integral(derivative(...))` link showed `$635k`. Justin Young confirmed `$337k` correct — the Graphite formula is wrong for cumulative ledger metrics. A bad data point on 2026-01-24 (brief dip to $1.79M) caused phantom +$298k inflation. `$337k` is the true January SI book P&L. [permalink](https://mahifx.slack.com/archives/C046RNF64VD/p1778157023465809)

- 2026-04-30 — USDCHF added to hybrid hedger G8 instrument list; was sitting on uncleared CHF risk due to no EUR position to cross via EURCHF. Finalto USDCHF spreads tighter than EURCHF (0.60 vs 0.76 pips). [permalink](https://mahifx.slack.com/archives/C046RNF64VD/p1777555520482219)
