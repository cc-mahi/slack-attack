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
  - {name: "Aytugan Khafizov", role: "Centroid — technical integration contact (FIX / TEM setup)", confidence: low}
  - {name: "Anatoly", role: "Base Markets — internal sign-off contact (referenced alongside Alex for MT4 account switch confirmation)", confidence: low}
last_catchup: 2026-05-18T07:25:34Z
---

## Status

- **Stage:** onboarding — pre-flow, working through Tegis onboarding before flow lands on Compass.
- **Integration:** LDN trading + admin (LD5), Athena `basemarkets_ldn`, distribution via CLIENT_PRICE_LDN / CLIENT_PRICE_BETA_LDN / DISTRIBUTION_LDN / DISTRIBUTION_SYNAPSE_LDN. FIX API available; no margin / credit checking yet.
- **Relationship:** healthy — Alex (client) "super happy" with recent report; Nicola Perikhanyan owns commercial, Rory King / Kate Stagg client-facing.

## Recent issues

> [open] 2026-05-06 — Tegis MT4/MT5 dual-platform: Centroid workaround adopted, MT5 drop-copy on roadmap with no ETA
> Originally: EA on MT4 requires zero-spread exact-fill; Scope MT5 handles real execution. Compass had no lever on fill price. [permalink](https://mahifx.slack.com/archives/C09D05EPCTV/p1778162773664489) [permalink](https://mahifx.slack.com/archives/C09D05EPCTV/p1778174905149009)
> **2026-05-11 update:** Kate Stagg proposed Tegis's Centroid as the workaround — Centroid handles MT4 zero-spread / MT5 standard-market-conditions split; Mahi receives market orders via FIX, hedges normally, Centroid translates fills to each platform. Andrew Morgan confirmed this is a valid "Compass broker workflow at a structural loss on the inbound by design" — MT4 accepts whatever limit price, Compass hedges to market, give-up feed into MT5 for real economics. [permalink](https://mahifx.slack.com/archives/C09D05EPCTV/p1778494642.927869) [permalink](https://mahifx.slack.com/archives/C09D05EPCTV/p1778258653.848549)
> Distribution FIX creds sent to client on 2026-05-11; infra deploying `clientDistGW1`. [permalink](https://mahifx.slack.com/archives/C09D8V41JAG/p1778499833340869)
> Longer-term: Kate B (client) asked whether Centroid can be removed eventually — MT5 drop-copy (MTB-199, blocked since 2023 on acceptor/initiator architecture call) added to roadmap, no delivery commitment. [permalink](https://mahifx.slack.com/archives/C09D05EPCTV/p1778517045666329) [permalink](https://mahifx.slack.com/archives/C09D05EPCTV/p1778517127566459)
> Call with FastMT requested by client 2026-05-12 (12–2pm or after 5pm UK) to discuss Tegis setup — unanswered as of run time. [permalink](https://mahifx.slack.com/archives/C09D8V41JAG/p1778570575730699)
> **2026-05-12 update:** Post-call recap from Aytugan Khafizov (Centroid technical contact) confirmed 7-step integration plan: (1) Mahi creates taker FIX connection with Centroid IPs whitelisted, (2) Centroid creates a maker from Mahi creds, (3) bridge restart, (4) Centroid builds MAHI1 TEM (inheriting MT4 zero-spread config from current Scope TEM), (5) drop-copy on netting account in Base MT5, (6) end-to-end test on MT4 test account, (7) Alex and Anatoly confirm before switching existing MT4 accounts. Kate Stagg sent maker creds to Centroid. [permalink](https://mahifx.slack.com/archives/C09D8V41JAG/p1778587371610629)
> **2026-05-16:** Centroid restarted; Mahi maker went offline. Client reported IPs not whitelisted (Primary: 192.109.17.181, Backup: 185.125.204.132, DNS: tzouk.centroidsol.com). [permalink](https://mahifx.slack.com/archives/C09D8V41JAG/p1778914623299679)
> **2026-05-18:** Daria Horton confirmed Beeks whitelisting; Aytugan confirmed Mahi maker now connected from Centroid side — proceeding with configuration. [permalink](https://mahifx.slack.com/archives/C09D8V41JAG/p1779081321195119)

> [resolved] 2026-05-15 — LMAX FIX connection spamming incorrect password / locking account
> Client (Kate B) flagged that LMAX FIX session was spamming incorrect password and locking the account. Asked Mahi to turn it off so LMAX could send a new password. Rory King confirmed the NZ team had already disabled it early morning UK time. [permalink](https://mahifx.slack.com/archives/C09D8V41JAG/p1778848988422949) [permalink](https://mahifx.slack.com/archives/C09D8V41JAG/p1778849696126849)

> [resolved] 2026-05-13 — Client requesting three new group codes
> Kate B requested addition of: `real\USD-MU-SD-KAJ-X`, `real\USD-MU-SD-KAJ-R`, `real\USD-MU-SD-KAJ-S`. Kate Stagg acknowledged. [permalink](https://mahifx.slack.com/archives/C09D8V41JAG/p1778666314632929)

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

- 2026-05-18 — Centroid FIX maker session confirmed connected from Centroid side (Aytugan); Daria Horton confirmed Beeks whitelisting complete. Integration proceeding to TEM configuration phase. [permalink](https://mahifx.slack.com/archives/C09D8V41JAG/p1779081321195119)
- 2026-05-12 — Post-call: Aytugan Khafizov (Centroid) posted 7-step integration plan covering Mahi taker FIX setup, MAHI1 TEM build, MT4 test account end-to-end, and final Alex/Anatoly sign-off before account switch. [permalink](https://mahifx.slack.com/archives/C09D8V41JAG/p1778587371610629)
- 2026-05-12 — Client requesting call with FastMT today (12–2pm or after 5pm UK) to discuss Tegis setup; unanswered as of run time. [permalink](https://mahifx.slack.com/archives/C09D8V41JAG/p1778570575730699)
- 2026-04-29 — Alex happy with report; Tegis onboarding underway, ~2 weeks until flow starts hitting Compass. [permalink](https://mahifx.slack.com/archives/C09D05EPCTV/p1777467956510609)
