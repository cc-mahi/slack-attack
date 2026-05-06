---
slug: axiory
refs:
  vibepulse: ../VibePulse/.claude/clients/axiory.yaml
  billing: ../MahiProduct/data/billing/clients.json     # entry: axiory
  hosts: ../MahiProduct/data/client-hosts.json          # entry: axiory
  wiki: null                                             # ../MahiProduct/wiki/clients/axiory.md (not yet)
channels_override: null
key_people_overrides:
  - {name: "Adam Foltyn", role: "client trading ops — LP/pricing escalations", confidence: low}
last_catchup: 2026-05-06T07:07:30Z
---

## Recent issues

> [resolved] 2026-04-27 — LD4 pricing broken at market open — US Oil + multiple CFDs + all FX wider than TY3
> Adam Foltyn pulled MAHI pricing on US Oil → GER40/HKD50/US30/US100 → all FX to backup at LD4 open. Restored 04-27 after Sam Hewitt restarted the publishing process; Adam confirmed pricing recovered and switched back. Root cause (Daria, 04-28): a hazelcast WAN replication `Update overrides[distribution.distributionChannels]` at 2026-04-20 00:48:48 UTC set the LDN dist channel's internalisation market to `CLIENT_PRICE_TKY` (override last edited 2024) — surprise it didn't trigger sooner; Kate to watch LDN for similar oddities. Adam pinged 04-29 asking for RCA update — no reply yet, RCA write-up still owed. 2026-05-02: Adam confirmed `_z` suffix symbols switched back to MAHI pricing and included in give-ups as agreed — full pricing restoration complete. [permalink](https://mahifx.slack.com/archives/C06KHNQQYMR/p1777254243398619) [internal-rca](https://mahifx.slack.com/archives/C06KQT6EU3W/p1777276704165709) [resolution](https://mahifx.slack.com/archives/C06KHNQQYMR/p1777738779200109)

## Notable topics
