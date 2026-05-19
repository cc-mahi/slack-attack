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
  - {name: "Aytugan Khafizov", role: "Centroid — technical integration contact (FIX bridge / TEM setup)", confidence: low}
last_catchup: 2026-05-19T07:25:39Z
---

## Status

- **Stage:** onboarding — pre-flow, working through Tegis onboarding before flow lands on Compass.
- **Integration:** LDN trading + admin (LD5), Athena `basemarkets_ldn`, distribution via CLIENT_PRICE_LDN / CLIENT_PRICE_BETA_LDN / DISTRIBUTION_LDN / DISTRIBUTION_SYNAPSE_LDN. FIX API available; no margin / credit checking yet.
- **Relationship:** healthy — Alex (client) "super happy" with recent report; Nicola Perikhanyan owns commercial, Rory King / Kate Stagg client-facing.

## Recent issues

> [open] 2026-05-06 — Tegis MT4/MT5 dual-platform: Centroid integration in progress, Mahi maker now connected
> Originally: EA on MT4 requires zero-spread exact-fill; Scope MT5 handles real execution. Compass had no lever on fill price. [permalink](https://mahifx.slack.com/archives/C09D05EPCTV/p1778162773664489) [permalink](https://mahifx.slack.com/archives/C09D05EPCTV/p1778174905149009)
> **2026-05-11 update:** Kate Stagg proposed Tegis's Centroid as the workaround — Centroid handles MT4 zero-spread / MT5 standard-market-conditions split; Mahi receives market orders via FIX, hedges normally, Centroid translates fills to each platform. Distribution FIX creds sent to client 2026-05-11. [permalink](https://mahifx.slack.com/archives/C09D8V41JAG/p1778499833340869)
> **2026-05-12 update:** Aytugan Khafizov (Centroid) recapped the integration plan in `#mahi-base-markets` (create taker connection, Centroid creates maker, restart bridge, MAHI1 TEM configured to inherit zero spreads from Scope TEM, drop-copy on Base MT5 netting account, end-to-end test on MT4 test account, then switch or create new MT4 accounts). Kate Stagg forwarded maker creds to Centroid. [permalink](https://mahifx.slack.com/archives/C09D8V41JAG/p1778587371610629) [permalink](https://mahifx.slack.com/archives/C09D8V41JAG/p1778588623913609)
> **2026-05-15 update:** Centroid restarted; Mahi maker was offline — Centroid asked Kate Stagg to confirm whitelisting of IPs (Primary: 192.109.17.181, Backup: 185.125.204.132, DNS: tzouk.centroidsol.com). [permalink](https://mahifx.slack.com/archives/C09D8V41JAG/p1778914623299679)
> **2026-05-18 update:** Aytugan confirmed "Mahi maker now connected from Centroid side — will proceed with configuration". Daria Horton confirmed sessions are connected. [permalink](https://mahifx.slack.com/archives/C09D8V41JAG/p1779081321195119) [permalink](https://mahifx.slack.com/archives/C09D8V41JAG/p1779081863737599)
> Longer-term: Kate B (client) asked whether Centroid can be removed eventually — MT5 drop-copy (MTB-199, blocked since 2023 on acceptor/initiator architecture call) on roadmap, no delivery commitment. [permalink](https://mahifx.slack.com/archives/C09D05EPCTV/p1778517045666329)

> [resolved] 2026-05-07 — Client asking for FIX API test/sandbox instance
> Alex (Base Markets), relayed via Nicola Perikhanyan, asked whether Mahi has a test instance or sandbox for testing FIX API connectivity. Superseded by 2026-05-11 Centroid FIX credential setup — live Distribution FIX creds sent directly to client on 2026-05-11 as part of Tegis/Centroid onboarding. [permalink](https://mahifx.slack.com/archives/C09D05EPCTV/p1778164813309659)

> [watching] 2026-05-05 — Pre-flow readiness: cross skew + driver pair hedging workflow
> Will Carter flagged need to be ready for Monday (2026-05-11) — wants workflow testing to confirm skew is running on the crosses Base Markets trades, with hedging in driver pairs. Aligns with the ~2-week Tegis onboarding timeline from 2026-04-29. [permalink](https://mahifx.slack.com/archives/C09D05EPCTV/p1777983387923419)
> No further discussion in this window; Centroid maker now connected (2026-05-18) so flow is not yet live.

> [open] 2026-04-29 — Client asking about direct API piping for rewritten algo
> Alex (Base Markets) is planning to rewrite their algo and asked whether they could pipe trades straight into our server (i.e. off MT4/MT5). Andrew Morgan confirmed FIX API connectivity exists, but margin and credit checking are not implemented — flagged as something he'd want to build. No reply yet to Alex. [permalink](https://mahifx.slack.com/archives/C09D05EPCTV/p1777470115067619) [permalink](https://mahifx.slack.com/archives/C09D05EPCTV/p1777470499867149)

> [resolved] 2026-05-12 — Rev share account 110291: partial close internalised instead of brokered to SCOPE_B
> Account 110291 opened 5 lots short, partially closed in ≤50oz increments — these hit the "internalise 50oz" execution rule rather than the REV_SHARE broker rule (which routes to SCOPE_B). Client closed remainder manually on SCOPE_B. Daria Horton confirmed cause (execution rule ordering), shifted Compass positions to rev share book to net out. Client chose to keep rule order as-is and reconsider separately. [permalink](https://mahifx.slack.com/archives/C09D8V41JAG/p1778564784545149) [permalink](https://mahifx.slack.com/archives/C09D8V41JAG/p1778567380357959)

> [resolved] 2026-05-12 — MATUSD showing as indicative / no market data
> Nathan Burch queried whether MATUSD should be pricing. Kate confirmed it is not on the platform. [permalink](https://mahifx.slack.com/archives/C09D8V41JAG/p1778547211274859)

> [resolved] 2026-05-15 — LMAX FIX connection spamming incorrect password / account locked
> Kate (client) reported LMAX FIX connection spamming incorrect password and locking the account; asked team to turn it off while LMAX sends a new password. Rory King confirmed the NZ team turned off the FIX connection. Kate replied 2026-05-18 with new password via email; Rory looking at it. [permalink](https://mahifx.slack.com/archives/C09D8V41JAG/p1778848988422949) [permalink](https://mahifx.slack.com/archives/C09D8V41JAG/p1779117308881069)

> [open] 2026-05-18 — Tegis book + hedger setup: planning agreed, implementation pending
> Kate Stagg caught up with Kate (client) on Tegis flow plan: current flow is warehoused/STP'd with no hedging. Client wants to keep existing setup and run a separate Tegis book, with view to move most flow into it over time (except warehoused risk). Also agreed to set up a hedger on B-book to keep risk below 100k. Next steps: set up Tegis book and hedger (Compass-managed), set up hedger on B-book. [permalink](https://mahifx.slack.com/archives/C09D05EPCTV/p1779111232980629)

> [open] 2026-05-18 — fixMD3 / fixOrders3 re-added to infra
> Rory King noted infra deploy to re-add fixMD3, fixOrders3. [permalink](https://mahifx.slack.com/archives/C09D05EPCTV/p1779120037227099)

## Notable topics

- 2026-05-12 — Client requesting call with FastMT today (12–2pm or after 5pm UK) to discuss Tegis setup; unanswered as of run time. [permalink](https://mahifx.slack.com/archives/C09D8V41JAG/p1778570575730699)
- 2026-04-29 — Alex happy with report; Tegis onboarding underway, ~2 weeks until flow starts hitting Compass. [permalink](https://mahifx.slack.com/archives/C09D05EPCTV/p1777467956510609)
