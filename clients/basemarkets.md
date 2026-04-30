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
last_catchup: 2026-04-30T00:00:00Z
---

## Status

- **Stage:** onboarding — pre-flow, working through Tegis onboarding before flow lands on Compass.
- **Integration:** LDN trading + admin (LD5), Athena `basemarkets_ldn`, distribution via CLIENT_PRICE_LDN / CLIENT_PRICE_BETA_LDN / DISTRIBUTION_LDN / DISTRIBUTION_SYNAPSE_LDN. FIX API available; no margin / credit checking yet.
- **Relationship:** healthy — Alex (client) "super happy" with recent report; Nicola Perikhanyan owns commercial, Rory King / Kate Stagg client-facing.

## Recent issues

> [open] 2026-04-29 — Client asking about direct API piping for rewritten algo
> Alex (Base Markets) is planning to rewrite their algo and asked whether they could pipe trades straight into our server (i.e. off MT4/MT5). Andrew Morgan confirmed FIX API connectivity exists, but margin and credit checking are not implemented — flagged as something he'd want to build. No reply yet to Alex. [permalink](https://mahifx.slack.com/archives/C09D05EPCTV/p1777470115067619) [permalink](https://mahifx.slack.com/archives/C09D05EPCTV/p1777470499867149)

## Notable topics

- 2026-04-29 — Alex happy with report; Tegis onboarding underway, ~2 weeks until flow starts hitting Compass. [permalink](https://mahifx.slack.com/archives/C09D05EPCTV/p1777467956510609)
