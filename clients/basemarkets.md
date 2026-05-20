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
  - {name: "Aytugan Khafizov", role: "Centroid Solutions — technical contact (Centroid bridge integration)", confidence: low}
last_catchup: 2026-05-20T07:25:25Z
---

## Status

- **Stage:** onboarding — pre-flow, working through Tegis onboarding before flow lands on Compass.
- **Integration:** LDN trading + admin (LD5), Athena `basemarkets_ldn`, distribution via CLIENT_PRICE_LDN / CLIENT_PRICE_BETA_LDN / DISTRIBUTION_LDN / DISTRIBUTION_SYNAPSE_LDN. FIX API available; no margin / credit checking yet.
- **Relationship:** healthy — Alex (client) "super happy" with recent report; Nicola Perikhanyan owns commercial, Rory King / Kate Stagg client-facing.

## Recent issues

> [open] 2026-05-06 — Tegis MT4/MT5 dual-platform: Centroid integration live, Tegis Book + hedger next
> Originally: EA on MT4 requires zero-spread exact-fill; Scope MT5 handles real execution. Compass had no lever on fill price. [permalink](https://mahifx.slack.com/archives/C09D05EPCTV/p1778162773664489) [permalink](https://mahifx.slack.com/archives/C09D05EPCTV/p1778174905149009)
> **2026-05-11 update:** Kate Stagg proposed Tegis's Centroid as the workaround — Centroid handles MT4 zero-spread / MT5 standard-market-conditions split; Mahi receives market orders via FIX, hedges normally, Centroid translates fills to each platform. Andrew Morgan confirmed valid "Compass broker workflow at structural loss on inbound by design". [permalink](https://mahifx.slack.com/archives/C09D05EPCTV/p1778494642.927869) [permalink](https://mahifx.slack.com/archives/C09D05EPCTV/p1778258653.848549) Distribution FIX creds sent 2026-05-11; infra deployed `clientDistGW1`. [permalink](https://mahifx.slack.com/archives/C09D8V41JAG/p1778499833340869) MT5 drop-copy (MTB-199) on roadmap, no ETA. [permalink](https://mahifx.slack.com/archives/C09D05EPCTV/p1778517045666329)
> **2026-05-12 update:** Aytugan Khafizov (Centroid) call with Kate Stagg — agreed integration steps: Mahi creates taker connection, Centroid creates maker using Distribution FIX creds, bridge restarts, Centroid configures MAHI1 TEM (inherits zero spread from Scope setup), dropcopy on Netting account in Base MT5 (not Tegis MT5); test MT4 account created then switch existing accounts from Scope TEM. [permalink](https://mahifx.slack.com/archives/C09D8V41JAG/p1778587371610629) [permalink](https://mahifx.slack.com/archives/C09D8V41JAG/p1778588623913609)
> **2026-05-18 update:** Centroid IP whitelisting resolved via Beeks; Mahi marker confirmed connected from Centroid side. [permalink](https://mahifx.slack.com/archives/C09D8V41JAG/p1779081321195119) Rory King re-added fixMD3/fixOrders3 infra. [permalink](https://mahifx.slack.com/archives/C09D05EPCTV/p1779120037227099) Kate Stagg call with Kate B confirmed strategy: keep current execute/warehouse/STP flow for existing base flow, set up separate Tegis Book (Compass managed) + hedger, plus hedger on B Book to keep risk below 100k. LMAX Sub1 = Tegis account, Sub2 = base flow; round-robin tag management in orderServiceConfiguration. [permalink](https://mahifx.slack.com/archives/C09D05EPCTV/p1779111232980629) [permalink](https://mahifx.slack.com/archives/C09D05EPCTV/p1779185342020389)
> Longer-term: view to move most Tegis flow into the new Book over time, retaining warehouse risk in current setup.

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

- 2026-05-12 — Client requesting call with FastMT today (12–2pm or after 5pm UK) to discuss Tegis setup; unanswered as of run time. [permalink](https://mahifx.slack.com/archives/C09D8V41JAG/p1778570575730699)
- 2026-04-29 — Alex happy with report; Tegis onboarding underway, ~2 weeks until flow starts hitting Compass. [permalink](https://mahifx.slack.com/archives/C09D05EPCTV/p1777467956510609)
