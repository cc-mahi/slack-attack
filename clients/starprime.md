---
slug: starprime
refs:
  vibepulse: ../VibePulse/.claude/clients/starprime.yaml
  billing: ../MahiProduct/data/billing/clients.json     # entry: starprime
  hosts: ../MahiProduct/data/client-hosts.json          # entry: starprime
  wiki: ../MahiProduct/wiki/clients/starprime.md
channels_override: null
key_people_overrides:
  - {name: "Shahid Afrid", role: "client ops / data integrations", confidence: low}
last_catchup: 2026-05-15T07:30:03Z
---

## Recent issues

> [resolved] 2026-05-07 — Limit order cancellations due to Arbitrageur misclassification of counterparty RBI_5036_LIVE-97F5F2
> Umar Bin Aziz reported execution errors on limit orders (~11:20 BST). Rory King diagnosed: counterparty RBI_5036_LIVE-97F5F2 had been classified under the `BBOOK//Arbitrageurs` execution rule after a small number of trades; limit orders were being force-internalised on the continuity pool with markup, with fills breaching the limit price and cancelling. Umar requested removal; Rory blacklisted the counterparty from the Arbitrageurs profile at 12:03 BST. [permalink](https://mahifx.slack.com/archives/C096422RPKK/p1778151195430889)

> [resolved] 2026-05-07 — XAUUSD LIMIT order LIQUIDITY_VIOLATION on orders 2409798/2409799 (LP-side incident)
> Umar Bin Aziz posted logs showing orders 2409798 and 2409799 (XAUUSD limit) rejected with `LIQUIDITY_VIOLATION` on connector LIV_NRI_5036. Sam Hewitt investigated and confirmed the LP was returning liquidity violation rejects 06:35–06:40 UTC; 49 and 50 hedge legs retried respectively, all cancelled. LP-side issue self-cleared at 06:40, no recurrence. Umar acknowledged. [permalink](https://mahifx.slack.com/archives/C096422RPKK/p1778140090765839)

> [open] 2026-05-05 — Go-live timeline shifted to July; pre-go-live call notes
> Call with Samin (client ops lead) held 2026-05-05. Key points: go-live delayed due to operational issues on client side; Samin is heading to LDN then Madrid; target is July but wants to pull it sooner if packaging allows. Action items: prep Signals deck for Insti SI; PSM discussed — Dave confirmed feasible but chargeable. Testing underway with fixed spread values on gold to assess flow attracted. [permalink](https://mahifx.slack.com/archives/C095MJHC68J/p1777983798434859)

> [open] 2026-04-23 — REST API request for historical trade data
> Shahid asked about connecting to MFX via REST API for historical trade data; Cameron Hughes suggested Pulse (`houseorder_response`) first — Shahid to check with Sam internally and revert. [permalink](https://mahifx.slack.com/archives/C096422RPKK/p1776941638461559)

## Notable topics

- 2026-05-05 — Inald Gjoni performed rolling restart of pricers to load Timezone Conditions for BenchmarkMinimumSpreadLogic (no-restart component deploy). [permalink](https://mahifx.slack.com/archives/C095MJHC68J/p1777981565638809)
- 2026-05-13 — Andrew Morgan noted StarPrime is owned by Vantage; David Cooney confirmed. Context: VANTAGE is already listed as a benchmark spread market in StarPrime's pricer config. [permalink](https://mahifx.slack.com/archives/C095MJHC68J/p1778669482861249)
- 2026-05-11 — Nathan Burch (Training) changed `price adjustment floor pips` on IFMS from 3 → 0.5 for XAUUSD on CLIENT_PRICE_INSTI; prior to this, price could not form because floor was greater than ceiling. [permalink](https://mahifx.slack.com/archives/C095MJHC68J/p1778463918376889)
- 2026-05-01 — Go-live prep: Cameron Hughes noted a call with Samin arranged for Tuesday to get everything ready pre go-live. [permalink](https://mahifx.slack.com/archives/C095MJHC68J/p1777625477346409)
