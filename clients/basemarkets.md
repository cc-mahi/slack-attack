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
last_catchup: 2026-05-11T09:53:48Z
---

## Status

- **Stage:** onboarding — pre-flow, working through Tegis onboarding before flow lands on Compass.
- **Integration:** LDN trading + admin (LD5), Athena `basemarkets_ldn`, distribution via CLIENT_PRICE_LDN / CLIENT_PRICE_BETA_LDN / DISTRIBUTION_LDN / DISTRIBUTION_SYNAPSE_LDN. FIX API available; no margin / credit checking yet.
- **Relationship:** healthy — Alex (client) "super happy" with recent report; Nicola Perikhanyan owns commercial, Rory King / Kate Stagg client-facing.

## Recent issues

> [open] 2026-05-06 — Tegis MT4/MT5 dual-platform setup: give-up feed to MT5 required; blocked on MTB-199
> The Tegis flow architecture has been clarified (2026-05-07) and is more problematic than originally understood. The client's EA runs on MT4 with zero spread / exact-fill-price requirement — purely an echo chamber; the actual execution and P&L tracking is on a Scope MT5 server. Liam Cordelle's diagnosis: Compass could technically sit in between (receive MT4 orders, pass to Scope MT5), but has no ability to influence fill price (Scope sets it) and cannot skew fills back to MT4 (client requires exact requested price). Kate Stagg flagged client withheld this workflow when flow was originally analysed. Andrew Morgan's 2026-05-08 synthesis: this is a Compass-broker workflow at a structural loss on the inbound by design — MT4 accepts whatever limit price the EA sends (zero spread, zero slip), Compass hedges to market, give-up feed into MT5 so the client sees real economics. Andrew's view: Compass value is on the outbound (smart hedging, classifier-aware aggression, LR as circuit breaker, brokering-economics reporting per algo), not on the MT4 inbound (Liam is right). The give-up plumbing is JIRA epic MTB-199 (sitting in To Do since 2023, blocked on a 2023 James architectural call about acceptor vs initiator). Base Markets + ATC prop launch + Exinity all stack on the same primitive — Andrew flagged this is worth settling the 2023 question and decomposing the epic. **Client cannot be configured until MTB-199 lands.** [permalink](https://mahifx.slack.com/archives/C09D05EPCTV/p1778162773664489) [permalink](https://mahifx.slack.com/archives/C09D05EPCTV/p1778170633469599) [permalink](https://mahifx.slack.com/archives/C09D05EPCTV/p1778174905149009) [permalink](https://mahifx.slack.com/archives/C09D05EPCTV/p1778258653848549)

> [open] 2026-05-07 — Client asking for FIX API test/sandbox instance
> Alex (Base Markets), relayed via Nicola Perikhanyan, asked whether Mahi has a test instance or sandbox for testing FIX API connectivity. Liam Cordelle replied he wasn't sure what this was about. No answer provided to client yet; unanswered. Related to the earlier API piping question (2026-04-29). [permalink](https://mahifx.slack.com/archives/C09D05EPCTV/p1778164813309659)

> [open] 2026-05-05 — Pre-flow readiness: cross skew + driver pair hedging workflow
> Will Carter flagged need to be ready for Monday (2026-05-11) — wants workflow testing to confirm skew is running on the crosses Base Markets trades, with hedging in driver pairs. Aligns with the ~2-week Tegis onboarding timeline from 2026-04-29. [permalink](https://mahifx.slack.com/archives/C09D05EPCTV/p1777983387923419)

> [open] 2026-04-29 — Client asking about direct API piping for rewritten algo
> Alex (Base Markets) is planning to rewrite their algo and asked whether they could pipe trades straight into our server (i.e. off MT4/MT5). Andrew Morgan confirmed FIX API connectivity exists, but margin and credit checking are not implemented — flagged as something he'd want to build. No reply yet to Alex. [permalink](https://mahifx.slack.com/archives/C09D05EPCTV/p1777470115067619) [permalink](https://mahifx.slack.com/archives/C09D05EPCTV/p1777470499867149)

## Notable topics

- 2026-05-08 — Andrew Morgan diagnosed the give-up plumbing gap as JIRA epic MTB-199 (blocked since 2023 on acceptor-vs-initiator architectural decision); notes Base Markets, ATC prop launch, and Exinity all share the same dependency, making resolution higher leverage. [permalink](https://mahifx.slack.com/archives/C09D05EPCTV/p1778258653848549)
- 2026-04-29 — Alex happy with report; Tegis onboarding underway, ~2 weeks until flow starts hitting Compass. [permalink](https://mahifx.slack.com/archives/C09D05EPCTV/p1777467956510609)
