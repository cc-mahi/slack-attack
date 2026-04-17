---
slug: example
name: Example Client
type: broker              # broker | prop-firm | institutional | other
status: live              # live | trial | onboarding | paused | churned
products: []              # asset classes traded: [fx, crypto, cfd, equities, ...]
regions: []               # [LDN, NYC, CHI, ...]
contract_expires: null    # YYYY-MM-DD if known, else null
channels:
  internal: internal-example
  client: []              # shared with client, e.g. [mahi-example]
  other: []               # additional related channels
key_people: []            # [{name, role, org: client|mahi|unknown, confidence: low}] — confidence optional (default high)
athena_dbs: []
aws_profile: null
last_catchup: null        # ISO8601; updated by /catchup
---

## Summary

One-paragraph orientation: who they are, what they do on the platform, anything structurally unusual.

## Technical notes

Durable facts: infra quirks, non-obvious configuration, things I'd forget. Not a changelog.

## Recent issues

Reverse chronological. Trim >90d. Each entry:

```
> [open|resolved|watching] YYYY-MM-DD — short title
> 1–3 lines. [permalink](https://mahifx.slack.com/archives/<CID>/p<TS>)
```

Permalink required. `/catchup` promotes `[open]` → `[resolved]` when thread closes.

## Notable topics

Ongoing themes / projects / decisions-in-flight. Shorter-lived than technical notes.
