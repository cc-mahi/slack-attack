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
last_catchup: 2026-04-27T09:35:00Z
---

## Recent issues

> [open] 2026-04-26 — Yaron escalation: recurring weekend disconnections + order-book changes
> Yaron asked for root cause + permanent fix on the recurring Saturday-morning price feed disconnects, framing it as no longer acceptable. Also requested order-book adjustments (FX +1pt from 0.05 lots; XAG +1pt per side from 0.05 lots). Kate (04-27): initial checks point at the B2Broker price stream as the trigger this weekend; full analysis to follow, order-book changes being applied. [permalink](https://mahifx.slack.com/archives/C07AQJS4E80/p1777196856253159)

> [open] 2026-04-26 — liquidityPool* down on 5ersCryptoCFDs — failed over 5ers→B2BROKER reference
> Sam Hewitt: liquidityPoolMDAggregator1, liquidityPoolMDAggregator2, liquidityPoolSOR1 down; swapped 5ers for B2BROKER in `5ersCryptoCFDs.reference.referencePriceMarketSelectors` to recover, reverting earlier-week change. Likely the same root cause as the Yaron-facing weekend incident — pair these when investigating. [permalink](https://mahifx.slack.com/archives/C079M09MGGP/p1777235724205449)

> [open] 2026-04-27 — Spreads "fixed" on assets switched yourbourse→Mahi
> Andreas: on assets they've switched from yourbourse to Mahi, spreads look more or less fixed — asking if Mahi sends fixed spreads. Kate explained: a couple of instruments look that way because Mahi base spreads are slightly wider than market, dynamic widening then doesn't kick in; offered to bring base spreads down so dynamic widening drives the price. Awaiting Andreas's call. [permalink](https://mahifx.slack.com/archives/C07AQJS4E80/p1777278243169839)

> [open] 2026-04-23 — Weekend failover dropouts — trade-flow anomaly via YourBourse gateway
> Kate raised that recent weekend restart windows show 0–1 trades vs expected higher volume during failover; heartbeats on the `5ers.COrders`↔`MahiFXMT5Bridge` FIX session look fine, so order connection is up but flow isn't routing. Nothing changed Mahi-side — Kate suspects a change to gateway routing rules on 5ers/YourBourse side and asked them to check before next scheduled weekend restart. Linked to earlier Yaniv call (2026-04-21): config issue this weekend prevented dist process from coming back up; change being put in to prevent recurrence. [permalink](https://mahifx.slack.com/archives/C07AQJS4E80/p1776934039029069)

> [watching] 2026-04-23 — Test trades on XAGUSD / JPN225 / XTIUSD via YourBourse gateway
> Andreas sending test trades through yourbourse→Mahi; Shyam + Isaac monitoring. Isaac's 04-24 update: trades flowing as expected; some cancels from off-market/last-look breaching limit orders but nothing unexpected. [permalink](https://mahifx.slack.com/archives/C07AQJS4E80/p1776981907673599)

## Notable topics
