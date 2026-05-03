---
slug: 5ers
refs:
  vibepulse: ../VibePulse/.claude/clients/5ers.yaml
  billing: ../MahiProduct/data/billing/clients.json     # entry: 5ers
  hosts: ../MahiProduct/data/client-hosts.json          # entry: 5ers
  wiki: null
channels_override: null
key_people_overrides:
  - {name: "Yaniv", role: "client stakeholder — weekend/failover escalations", confidence: low}
  - {name: "Yaron", role: "client stakeholder — feed reliability + spread escalations", confidence: low}
  - {name: "Andreas", role: "client trading ops — YourBourse gateway, spread/order-book settings", confidence: low}
last_catchup: 2026-05-03T07:12:27Z
---

## Recent issues

> [open] 2026-04-26 — Recurring weekend disconnections — B2Broker session break / CLIENT_PRICE_LDN going indicative
> Internal (Kate, 04-28): only crypto LP is B2Broker; their session break Saturday morning stopped pricing → drop-out 5ers saw. B2Broker confirmed they can't customise session times. 2026-04-30: Kate deployed crypto feed enrichment — additional market data sourced to supplement B2BROKER, XBTEUR base spreads tightened. 2026-05-01: Kate confirmed to client that additional crypto feeds are normalised into price formation alongside B2Broker; feeds remained stable through the Saturday B2Broker downtime window. CFD side: same pattern applied, additional CFD feeds layered in. **2026-05-02 recurrence:** Yaniv reported crypto trading down on both MT5 and cTrader from ~08:00 UTC. Justin found `CLIENT_PRICE_LDN` was 98–100% indicative during 08:00–10:00 UTC (1,491 rows at 08:00, 5,389 at 09:00 vs ~165k/hr normal); all Synapse + cTrader channels share this market, so the whole crypto/FX/CFD stack was effectively non-tradeable. LMAX also unavailable 08:00–10:00 UTC Saturday. Justin noted B2Broker sessions also down in that window and flagged for analytics follow-up. Yaniv disabled real-account routing on MT5 to restore MT5 crypto; cTrader routing uncontrollable client-side. Analytics investigation still open as of end of window. [yaron-escalation](https://mahifx.slack.com/archives/C07AQJS4E80/p1777196856253159) [internal-rca](https://mahifx.slack.com/archives/C079M09MGGP/p1777394276388709) [feed-fix-update](https://mahifx.slack.com/archives/C07AQJS4E80/p1777572138698369) [resolved-update-05-01](https://mahifx.slack.com/archives/C07AQJS4E80/p1777652354910519) [05-02-client-report](https://mahifx.slack.com/archives/C07AQJS4E80/p1777713097183339) [05-02-justin-analysis](https://mahifx.slack.com/archives/C079M09MGGP/p1777731760352189)

> [resolved] 2026-04-26 — liquidityPool* down on 5ersCryptoCFDs — failed over 5ers→B2BROKER reference
> Sam Hewitt: liquidityPoolMDAggregator1/2 + liquidityPoolSOR1 down; swapped 5ers→B2BROKER in `5ersCryptoCFDs.reference.referencePriceMarketSelectors` to recover. Same root cause as the weekend disconnect (B2Broker session break). 2026-04-30: crypto feed enrichment deployed. 2026-05-01: CFD enrichment also deployed — additional CFD feeds layered in alongside B2Broker; both crypto and CFD sides now multi-source. [permalink](https://mahifx.slack.com/archives/C079M09MGGP/p1777235724205449) [resolved-update](https://mahifx.slack.com/archives/C07AQJS4E80/p1777652354910519)

> [resolved] 2026-04-27 — Spreads "fixed" on assets switched yourbourse→Mahi
> Andreas accepted Kate's proposal to bring base spreads down so dynamic widening drives the price; applied across all symbols 04-27 14:39 BST. Andreas asked 04-28 whether it also applied to FX + XAUUSD — no reply yet, but change was applied across the board. [permalink](https://mahifx.slack.com/archives/C07AQJS4E80/p1777278243169839)

> [open] 2026-04-23 — Weekend failover dropouts — trade-flow anomaly via YourBourse gateway
> Kate raised that recent weekend restart windows show 0–1 trades vs expected higher volume during failover; heartbeats on the `5ers.COrders`↔`MahiFXMT5Bridge` FIX session look fine, so order connection is up but flow isn't routing. Nothing changed Mahi-side — Kate suspects a change to gateway routing rules on 5ers/YourBourse side and asked them to check before next scheduled weekend restart. Linked to earlier Yaniv call (2026-04-21): config issue this weekend prevented dist process from coming back up; change being put in to prevent recurrence. [permalink](https://mahifx.slack.com/archives/C07AQJS4E80/p1776934039029069)

> [resolved] 2026-04-29 — Pending-order rejections via bridge: "liquidity violation"
> Constantinos flagged high pending-order rejections, some duplicated. Kate explained: triggered by Mid Distance Check (price crossed minimum-distance-from-mid by end of last-look window), passed to bridge as `liquidity violation`; designed to stop off-market fills. <1% rate today; yields where present weren't profitable, so rejections look justified. Duplicates are bridge resubmits hitting the same threshold. Constantinos satisfied. [permalink](https://mahifx.slack.com/archives/C07AQJS4E80/p1777447120492979)

> [watching] 2026-04-23 — Test trades on XAGUSD / JPN225 / XTIUSD via YourBourse gateway
> Andreas sending test trades through yourbourse→Mahi; Shyam + Isaac monitoring. Isaac's 04-24 update: trades flowing as expected; some cancels from off-market/last-look breaching limit orders but nothing unexpected. 04-28: client switched XAUUSD flow to YB+Mahi too. [permalink](https://mahifx.slack.com/archives/C07AQJS4E80/p1776981907673599)

## Notable topics

- 2026-04-28 — Yaniv weekly call recap: T4B→YB demo flow migration complete; FX order-book tier change applied (100k/200k/300k/500k…, was 100k/400k/500k…); Yaniv keen on further education for Yaron given he's been trialling YB's order book on demo; client now using Claude to surface toxic counterparties from MT trade logs. [permalink](https://mahifx.slack.com/archives/C079M09MGGP/p1777391713854269)
- 2026-04-30 — Constantinos requested USDSGD pricing — not previously in environment; Kate confirmed will set up. [permalink](https://mahifx.slack.com/archives/C07AQJS4E80/p1777554437360859)
