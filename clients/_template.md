---
slug: example
name: Example Client
type: broker              # broker | prop-firm | institutional | other
status: live              # live | trial | onboarding | paused | churned
products: []              # [fx, crypto, cfd, equities, ...]
regions: []               # [LDN, NYC, CHI, ...]
channels:
  internal: internal-example
  client: []              # shared with client, e.g. [mahi-example]
  other: []               # additional related channels
key_people: []            # [{name, role, org: client|mahi, notes}]
athena_dbs: []
aws_profile: null
last_catchup: null        # ISO8601; updated by /catchup
---

## Summary

One-paragraph orientation: who they are, what they do on the platform, anything structurally unusual.

## Technical notes

Durable facts: infra quirks, non-obvious configuration, things I'd forget. Not a changelog.

## Recent issues

Reverse chronological. Each entry: `YYYY-MM-DD — short title` + 1–3 lines. Trim >90d.

## Notable topics

Ongoing themes / projects / decisions-in-flight. Shorter-lived than technical notes.
