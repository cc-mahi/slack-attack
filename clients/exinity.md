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
  - {name: "Daniel Kurra", role: "trading ops — pricing channels / hedger config", confidence: low}
  - {name: "Keshav Woottum", role: "ops — alerts/reporting cadence", confidence: low}
  - {name: "George Moore", role: "ops — UBS / Jane Street test-trade liaison", confidence: low}
last_catchup: 2026-04-30T09:35:00Z
---

## Recent issues

> [resolved] 2026-04-27 — Risk-splitting config not routing 3 counterparties to BIG_CLIENTS_LDN
> Samuel: trades for `FX_MT5_LIVE01_231010816`/`…013379`/`FX_MT4_ECN_118002061` landing in `B_Clients` not `BIG_CLIENTS_LDN`. Kate found two issues: a whitespace before the cpty ID in the riskSplitting config (Daniel had already fixed) and the `EXINITY_ECN_XAUUSD` channel missing from the config. Kate added `EXINITY_ECN_XAUUSD` + EURUSD subchannel; resolved 04-27 10:52 BST. [permalink](https://mahifx.slack.com/archives/C0456LSHQQK/p1777257377985069)

> [resolved] 2026-04-26 — Connect_Wagyu metals: spot XAG not ticking + XAU spreads wide (60c)
> XAG ticking restored within minutes. Daria noted XAU 60c was the configured Twilight base spread (vs 19c during other timezones); offered to add a 19c tier at 100, but Mukhammad opted to wait it out since Twilight was ending — closed without changes to base config. [permalink](https://mahifx.slack.com/archives/C0456LSHQQK/p1777241318800319)

> [open] 2026-04-27 — Wagyu XAU client-perceived spread vs published TOB
> Samuel: TOB shows 30–35c with 20q layer since open, but clients reporting wider spreads. Daria: in line with what we publish on the channel — possible additional markup downstream. Awaiting client investigation. [permalink](https://mahifx.slack.com/archives/C0456LSHQQK/p1777328307964599)

> [open] 2026-04-28 — XRPUSD rejects on EXINITY_PROECN_ARU — visible quantity too low
> Louie: 1 cpty getting continuous ripple rejects; visible quantity on the channel substantially lower than CLIENT_PRICE_RETAIL. Kate temp-increased visible qty; XRPUSD-specific override pending to bring channel in line with model liquidity. [permalink](https://mahifx.slack.com/archives/C0456LSHQQK/p1777398508607609)

> [open] 2026-04-28 — Big Hybrid Hedger LDN: XAUUSD rejects to Invast
> Mukhammad reported rejects on XAUUSD trades sent to Invast under BIG_HOUSE. Sam couldn't see a Mahi-side cause; asked Mukhammad to check Invast for cancels on their end. Awaiting client. [permalink](https://mahifx.slack.com/archives/C0456LSHQQK/p1777338900259439)

> [open] 2026-04-30 — DOWUSD trades filled at LP price not Dist (Dynamic Arbitrageur profile)
> Samuel asked why DOW trades for cpty `ASV_MT5_228023951` executed at LP price. Sam: cpty was assigned the Dynamic Arbitrageur execution profile on 04-27 (day of the trades), so filled on `CONTINUITY_POOL` which publishes VELOCITY for DOWUSD. Samuel asked when client was added — clarified, but assignment context (who/why on 04-27) not surfaced. [permalink](https://mahifx.slack.com/archives/C0456LSHQQK/p1777514645330979)

> [open] 2026-04-27 — "Poor $/M report" alert frequency too high since update
> Keshav: receiving multiple alerts in short windows; asked for one-per-minute throttle. No reply visible — outstanding. [permalink](https://mahifx.slack.com/archives/C0456LSHQQK/p1777290223832409)

> [open] 2026-04-23 — Account ASV_MT5_228000145 missing info + no distribution trace
> Louie flagged the account is missing information in Compass and has no distribution trace for the last 24h window; William Denny to investigate. [permalink](https://mahifx.slack.com/archives/C0456LSHQQK/p1776974117585849)

## Notable topics

- 2026-04-29 — UBS reply turnaround flagged by George Moore — Kate apologised for delay, awaiting Charlie's reply; FRCeCommerce@ubs.com supplied as direct route to UBS FRC team. Internal Daria review (04-30): 3 issues escalated, first two looked into, third (this UBS one) was missed — flagged so client could've followed up sooner. [permalink](https://mahifx.slack.com/archives/C0456LSHQQK/p1777446054108019)
- 2026-04-28 — Exinity / Jane Street test-trade meeting confirmed for 04-29 15:00 UK. [permalink](https://mahifx.slack.com/archives/C0456LSHQQK/p1777378983947659)
- 2026-04-30 — Latency notifications (Samuel) traced to a heartbeat received latent from non-Mahi side; Isaac suspects one-off, will recheck Mahi-side latency around the time. [permalink](https://mahifx.slack.com/archives/C0456LSHQQK/p1777510067154679)
