---
slug: example
aliases: []                                                # other slugs (billing/VibePulse) that map to this dossier; e.g. [example-crypto]
refs:
  vibepulse: ../VibePulse/.claude/clients/example.yaml   # hosts, slack channels, party names, distribution markets, LR rules
  billing: ../MahiProduct/data/billing/clients.json       # entry: example
  hosts: ../MahiProduct/data/client-hosts.json            # entry: example
  wiki: null                                               # ../MahiProduct/wiki/clients/example.md when it exists
channels_override: null                                    # only if VibePulse is wrong for this client
key_people_overrides: []                                   # external contacts not yet in ../MahiProduct/wiki/people/; [{name, role, confidence: low}]
last_catchup: null                                         # ISO8601; updated by /catchup
status: active                                             # active (default — omit) | retired
retired_at: null                                           # YYYY-MM-DD when status: retired
retired_reason: null                                       # short prose + permalink(s) when status: retired
---

## Status

Populate **only when `wiki: null`** — i.e. MahiProduct doesn't yet have a `wiki/clients/<slug>.md`. Three lines, no more. Delete this whole section when a wiki page lands and update the `wiki:` ref.

- **Stage:** live / onboarding / pre-launch / paused / churned
- **Integration:** one line — what they're using us for (platforms, products, scope)
- **Relationship:** one line — health / cadence / primary contact

## History

Long-horizon relationship arc — major status changes, integrations, commercial milestones, stakeholder evolution. Populated by `/backfill`, not `/catchup`. Optional — only present when `/backfill` has been run. Lives between `## Status` (if present) and `## Recent issues`. Refused if `wiki:` is set (the wiki page is canonical for relationship history).

## Recent issues

Reverse chronological. Trim entries >90d. Each entry:

```
> [open|resolved|watching] YYYY-MM-DD — short title
> 1–3 lines. [permalink](https://mahifx.slack.com/archives/<CID>/p<TS>)
```

Permalink required. `/catchup` promotes `[open]` → `[resolved]` when the thread closes.

## Notable topics

Ongoing themes, decisions-in-flight, cross-cutting milestones. Shorter-lived than anything in VibePulse / MahiProduct. Same permalink requirement, no status markers.
