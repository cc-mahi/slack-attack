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
last_catchup: 2026-04-27T09:35:00Z
---

## Recent issues

> [open] 2026-04-27 — LD4 pricing broken at market open — US Oil + multiple CFDs + all FX wider than TY3
> Adam Foltyn turned off MAHI pricing on US Oil at LD4 open (XCore LD4 connection only); shortly after also pulled GER40, HKD50, US30, US100 to backup pricing. Then reported all FX pairs much wider on LD4 vs TY3 — switched everything to backup providers on Axiory and LFI. Sam Hewitt investigating; thinks the fix is restarting the publishing process and asked Adam to confirm all LDN pricing is now from another source before bouncing it. Internal diagnosis (Daria, 04-27): LDN dist channel had `internalisation market = CLIENT_PRICE_TKY` (last edited 2024); AWS config from a couple of weeks ago had `CPL` — suspects a region-based config override flipped it. Needs further investigation. [permalink](https://mahifx.slack.com/archives/C06KHNQQYMR/p1777254243398619) [internal](https://mahifx.slack.com/archives/C06KQT6EU3W/p1777276704165709)

## Notable topics
