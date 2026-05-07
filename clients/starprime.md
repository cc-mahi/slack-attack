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
last_catchup: 2026-05-07T07:37:21Z
---

## Recent issues

> [open] 2026-05-07 — XAUUSD LIMIT order LIQUIDITY_VIOLATION, rejectCount=35
> Umar Bin Aziz posted logs showing order 2409798-50 (1.0 lot XAUUSD limit @ 4735.94) rejected by connector LIV_NRI_5036 with `LIQUIDITY_VIOLATION`; `maker_trade_setting.rejectCount=35`. Sam Hewitt acknowledged and is investigating. No resolution yet. [permalink](https://mahifx.slack.com/archives/C096422RPKK/p1778138513075849)

> [open] 2026-05-05 — Go-live timeline shifted to July; pre-go-live call notes
> Call with Samin (client ops lead) held 2026-05-05. Key points: go-live delayed due to operational issues on client side; Samin is heading to LDN then Madrid; target is July but wants to pull it sooner if packaging allows. Action items: prep Signals deck for Insti SI; PSM discussed — Dave confirmed feasible but chargeable. Testing underway with fixed spread values on gold to assess flow attracted. [permalink](https://mahifx.slack.com/archives/C095MJHC68J/p1777983798434859)

> [open] 2026-04-23 — REST API request for historical trade data
> Shahid asked about connecting to MFX via REST API for historical trade data; Cameron Hughes suggested Pulse (`houseorder_response`) first — Shahid to check with Sam internally and revert. [permalink](https://mahifx.slack.com/archives/C096422RPKK/p1776941638461559)

## Notable topics

- 2026-05-05 — Inald Gjoni performed rolling restart of pricers to load Timezone Conditions for BenchmarkMinimumSpreadLogic (no-restart component deploy). [permalink](https://mahifx.slack.com/archives/C095MJHC68J/p1777981565638809)
- 2026-05-01 — Go-live prep: Cameron Hughes noted a call with Samin arranged for Tuesday to get everything ready pre go-live. [permalink](https://mahifx.slack.com/archives/C095MJHC68J/p1777625477346409)
