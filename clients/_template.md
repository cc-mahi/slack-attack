---
slug: example
refs:
  vibepulse: ../VibePulse/.claude/clients/example.yaml   # hosts, slack channels, party names, distribution markets, LR rules
  billing: ../MahiProduct/data/billing/clients.json       # entry: example
  hosts: ../MahiProduct/data/client-hosts.json            # entry: example
  wiki: null                                               # ../MahiProduct/wiki/clients/example.md when it exists
channels_override: null                                    # only if VibePulse is wrong for this client
key_people_overrides: []                                   # external contacts not yet in ../MahiProduct/wiki/people/; [{name, role, confidence: low}]
last_catchup: null                                         # ISO8601; updated by /catchup
---

## Recent issues

Reverse chronological. Trim entries >90d. Each entry:

```
> [open|resolved|watching] YYYY-MM-DD — short title
> 1–3 lines. [permalink](https://mahifx.slack.com/archives/<CID>/p<TS>)
```

Permalink required. `/catchup` promotes `[open]` → `[resolved]` when the thread closes.

## Notable topics

Ongoing themes, decisions-in-flight, cross-cutting milestones. Shorter-lived than anything in VibePulse / MahiProduct. Same permalink requirement, no status markers.
