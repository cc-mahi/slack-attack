---
slug: exinity
refs:
  vibepulse: ../VibePulse/.claude/clients/exinity.yaml
  billing: ../MahiProduct/data/billing/clients.json     # entry: exinity
  hosts: ../MahiProduct/data/client-hosts.json          # entry: exinity
  wiki: null                                             # ../MahiProduct/wiki/clients/exinity.md (not yet)
channels_override: null
key_people_overrides:
  - {name: "Louie Davidson", role: "ops / order-trace investigations", confidence: low}
  - {name: "Samuel Ewebiyi", role: "ops — distribution / risk-splitting config", confidence: low}
  - {name: "Mukhammad Khamidov", role: "trading ops — Wagyu metals pricing/spreads", confidence: low}
last_catchup: 2026-04-27T09:35:00Z
---

## Recent issues

> [open] 2026-04-27 — Risk-splitting config not routing 3 counterparties to BIG_CLIENTS_LDN
> Samuel: counterparties `FX_MT5_LIVE01_231010816`, `FX_MT5_LIVE01_231013379`, `FX_MT4_ECN_118002061` were added to `distribution.riskSplitting` but their trades are still landing in `B_Clients` instead of `BIG_CLIENTS_LDN`. Asked for investigation. [permalink](https://mahifx.slack.com/archives/C0456LSHQQK/p1777257377985069)

> [open] 2026-04-26 — Connect_Wagyu metals: spot XAG not ticking + XAU spreads wide (60c)
> Mukhammad: XAG spot not ticking; XAU spread ~60c, asking Sam Hewitt to reduce MWMS multiplier temporarily to bring spreads in line. Pre-warned via email ~30min before metals open. Thread has 11 replies through 26-04 23:59 BST. [permalink](https://mahifx.slack.com/archives/C0456LSHQQK/p1777241318800319)

> [open] 2026-04-23 — Account ASV_MT5_228000145 missing info + no distribution trace
> Louie flagged the account is missing information in Compass and has no distribution trace for the last 24h window; William Denny to investigate. [permalink](https://mahifx.slack.com/archives/C0456LSHQQK/p1776974117585849)

## Notable topics
