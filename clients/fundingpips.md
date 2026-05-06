---
slug: fundingpips
refs:
  vibepulse: ../VibePulse/.claude/clients/fundingpips.yaml
  billing: ../MahiProduct/data/billing/clients.json     # entry: fundingpips
  hosts: ../MahiProduct/data/client-hosts.json          # entry: fundingpips
  wiki: null                                             # ../MahiProduct/wiki/clients/fundingpips.md (not yet)
channels_override: null
key_people_overrides: []
last_catchup: 2026-05-06T07:07:30Z
---

## Recent issues

> [resolved] 2026-04-27 — AWS infra wind-down vs preserve decision
> Following the mid-April flow stop (FundingPips reportedly lost ~10mio USD on their futures biz, per David Cooney 2026-04-16, internal channel pre-window), Bonnie asked whether to decommission. Liam costed it on 2026-04-27: ~$100/mo to keep servers stopped, or delete-and-keep-config-backup at negligible cost. Isaac resolved 2026-05-05: chose option A (keep servers stopped, can delete later). https://mahifx.slack.com/archives/C073X2B83CH/p1777329277763629
>
> Resolution: https://mahifx.slack.com/archives/C073X2B83CH/p1777944196442699
>
> Cross-channel context: 2026-04-29 Hussain imported fundingpips into pulse automation terraform state alongside rostro — consistent with "keep infra, don't delete". https://mahifx.slack.com/archives/C8X18LPH9/p1777502447886849

## Notable topics

- Lifecycle ambiguity: client paused flow mid-April after a reported futures-business loss; internal channel discussing AWS server cost trade-offs while infra automation work continues. Not retired — keep watching for either a client restart signal or an explicit shutdown call.
