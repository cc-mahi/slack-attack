---
slug: basemarkets
refs:
  vibepulse: ../VibePulse/.claude/clients/basemarkets.yaml
  billing: ../MahiProduct/data/billing/clients.json     # entry: basemarkets
  hosts: ../MahiProduct/data/client-hosts.json          # entry: basemarkets
  wiki: null                                             # ../MahiProduct/wiki/clients/basemarkets.md (not yet)
channels_override: null
key_people_overrides:
  - {name: "Alex", role: "Base Markets — primary client contact (algo / flow)", confidence: low}
  - {name: "Kate B", role: "Base Markets — client contact (onboarding / MT4 setup queries)", confidence: low}
  - {name: "Aytugan", role: "Centroid — integration contact; led post-call recap on Centroid/Mahi FIX taker setup 2026-05-12", confidence: low}
last_catchup: 2026-05-15T07:21:27Z
---

## Status

- **Stage:** onboarding — Centroid FIX integration underway; Mahi taker credentials sent to Centroid 2026-05-12, whitelisting confirmation pending before bridge can go live.
- **Integration:** LDN trading + admin (LD5), Athena `basemarkets_ldn`, distribution via CLIENT_PRICE_LDN / CLIENT_PRICE_BETA_LDN / DISTRIBUTION_LDN / DISTRIBUTION_SYNAPSE_LDN. FIX API available; no margin / credit checking yet.
- **Relationship:** healthy — Alex (client) "super happy" with recent report; Nicola Perikhanyan owns commercial, Rory King / Kate Stagg client-facing.

## Recent issues

> [open] 2026-05-13 — Group codes requested for Centroid/MT4 setup
> Unattributed message (likely Aytugan / Centroid) requested addition of three group codes: `real\USD-MU-SD-KAJ-X`, `real\USD-MU-SD-KAJ-R`, `real\USD-MU-SD-KAJ-S`. Kate Stagg replied "sure thing" — no confirmation of completion yet. [permalink](https://mahifx.slack.com/archives/C09D8V41JAG/p1778666314632929) [permalink](https://mahifx.slack.com/archives/C09D8V41JAG/p1778666813240759)

> [open] 2026-05-06 — Tegis MT4/MT5 dual-platform: Centroid workaround adopted, MT5 drop-copy on roadmap with no ETA
> Originally: EA on MT4 requires zero-spread exact-fill; Scope MT5 handles real execution. Compass had no lever on fill price. [permalink](https://mahifx.slack.com/archives/C09D05EPCTV/p1778162773664489) [permalink](https://mahifx.slack.com/archives/C09D05EPCTV/p1778174905149009)
> **2026-05-11 update:** Kate Stagg proposed Tegis's Centroid as the workaround — Centroid handles MT4 zero-spread / MT5 standard-market-conditions split; Mahi receives market orders via FIX, hedges normally, Centroid translates fills to each platform. Andrew Morgan confirmed this is a valid "Compass broker workflow at a structural loss on the inbound by design" — MT4 accepts whatever limit price, Compass hedges to market, give-up feed into MT5 for real economics. [permalink](https://mahifx.slack.com/archives/C09D05EPCTV/p1778494642.927869) [permalink](https://mahifx.slack.com/archives/C09D05EPCTV/p1778258653.848549)
> Distribution FIX creds sent to client on 2026-05-11; infra deploying `clientDistGW1`. [permalink](https://mahifx.slack.com/archives/C09D8V41JAG/p1778499833340869)
> Longer-term: Kate B (client) asked whether Centroid can be removed eventually — MT5 drop-copy (MTB-199, blocked since 2023 on acceptor/initiator architecture call) added to roadmap, no delivery commitment. [permalink](https://mahifx.slack.com/archives/C09D05EPCTV/p1778517045666329) [permalink](https://mahifx.slack.com/archives/C09D05EPCTV/p1778517127566459)
> Call with FastMT requested by client 2026-05-12 (12–2pm or after 5pm UK) to discuss Tegis setup — no reply in thread. [permalink](https://mahifx.slack.com/archives/C09D8V41JAG/p1778570575730699)
> **2026-05-12 update:** Post-call recap from Aytugan (Centroid) confirmed integration steps: (1) Mahi creates taker FIX connection (IPs: 192.109.17.181 primary, 185.125.204.132 backup); (2) Mahi passes FIX creds to Centroid to create a maker; (3) bridge restart; (4) Centroid prepares MAHI1 TEM inheriting zero-spread setup from Scope TEM; (5) dropcopy on Base MT5 netting account; (6) end-to-end test on a new MT4 account; (7) switch existing MT4 accounts from Scope TEM to MAHI1 TEM after Alex + Anatoly sign-off. [permalink](https://mahifx.slack.com/archives/C09D8V41JAG/p1778587371610629)
> Kate Stagg confirmed maker creds sent to Aytugan 2026-05-12 13:23, asked for whitelisting confirmation. [permalink](https://mahifx.slack.com/archives/C09D8V41JAG/p1778588623913609)
> 2026-05-15: follow-up message "Send credentials to Centroid to create a maker" — suggests creds may not have been actioned yet or is an internal reminder. [permalink](https://mahifx.slack.com/archives/C09D8V41JAG/p1778827116883419)

> [resolved] 2026-05-07 — Client asking for FIX API test/sandbox instance
> Alex (Base Markets), relayed via Nicola Perikhanyan, asked whether Mahi has a test instance or sandbox for testing FIX API connectivity. Superseded by 2026-05-11 Centroid FIX credential setup — live Distribution FIX creds sent directly to client on 2026-05-11 as part of Tegis/Centroid onboarding. [permalink](https://mahifx.slack.com/archives/C09D05EPCTV/p1778164813309659)

> [open] 2026-05-05 — Pre-flow readiness: cross skew + driver pair hedging workflow
> Will Carter flagged need to be ready for Monday (2026-05-11) — wants workflow testing to confirm skew is running on the crosses Base Markets trades, with hedging in driver pairs. Aligns with the ~2-week Tegis onboarding timeline from 2026-04-29. [permalink](https://mahifx.slack.com/archives/C09D05EPCTV/p1777983387923419)

> [open] 2026-04-29 — Client asking about direct API piping for rewritten algo
> Alex (Base Markets) is planning to rewrite their algo and asked whether they could pipe trades straight into our server (i.e. off MT4/MT5). Andrew Morgan confirmed FIX API connectivity exists, but margin and credit checking are not implemented — flagged as something he'd want to build. No reply yet to Alex. [permalink](https://mahifx.slack.com/archives/C09D05EPCTV/p1777470115067619) [permalink](https://mahifx.slack.com/archives/C09D05EPCTV/p1777470499867149)

> [resolved] 2026-05-12 — Rev share account 110291: partial close internalised instead of brokered to SCOPE_B
> Account 110291 opened 5 lots short, partially closed in ≤50oz increments — these hit the "internalise 50oz" execution rule rather than the REV_SHARE broker rule (which routes to SCOPE_B). Client closed remainder manually on SCOPE_B. Daria Horton confirmed cause (execution rule ordering), shifted Compass positions to rev share book to net out. Client chose to keep rule order as-is and reconsider separately. [permalink](https://mahifx.slack.com/archives/C09D8V41JAG/p1778564784545149) [permalink](https://mahifx.slack.com/archives/C09D8V41JAG/p1778567380357959)

> [resolved] 2026-05-12 — MATUSD showing as indicative / no market data
> Nathan Burch queried whether MATUSD should be pricing. Kate confirmed it is not on the platform. [permalink](https://mahifx.slack.com/archives/C09D8V41JAG/p1778547211274859)

## Notable topics

- 2026-05-15 — Internal reminder to send credentials to Centroid to create a maker; status unclear. [permalink](https://mahifx.slack.com/archives/C09D8V41JAG/p1778827116883419)
- 2026-05-13 — Group codes `real\USD-MU-SD-KAJ-{X,R,S}` requested by Centroid; Kate Stagg acknowledged. [permalink](https://mahifx.slack.com/archives/C09D8V41JAG/p1778666314632929)
- 2026-05-12 — Centroid integration call held; Aytugan posted full 7-step recap; maker creds sent by Kate Stagg. [permalink](https://mahifx.slack.com/archives/C09D8V41JAG/p1778587371610629)
- 2026-05-12 — Client requesting call with FastMT today (12–2pm or after 5pm UK) to discuss Tegis setup; no reply in thread. [permalink](https://mahifx.slack.com/archives/C09D8V41JAG/p1778570575730699)
- 2026-04-29 — Alex happy with report; Tegis onboarding underway, ~2 weeks until flow starts hitting Compass. [permalink](https://mahifx.slack.com/archives/C09D05EPCTV/p1777467956510609)
