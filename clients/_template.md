---
slug: example
aliases: []                       # other slugs (billing etc.) that map to this dossier
refs:                             # sources only — never copy their contents into the body
  vibepulse: ../VibePulse/.claude/clients/example.yaml   # hosts, slack names, party names, distribution
  billing: ../MahiProduct/data/billing/clients.json       # entry: example
  hosts: ../MahiProduct/data/client-hosts.json            # entry: example
  wiki: null                                               # ../MahiProduct/wiki/clients/example.md if it exists
channels:                         # Slack channel name: ID — catchup's read list
  internal-example: C0000000000
  mahi-example: C0000000001
contacts: []                      # external people NOT in ../MahiProduct/wiki/people/: {name, role[, confidence: low]}
last_catchup: null                # ISO8601 UTC; updated by /catchup
status: active                    # active | retired (+ retired_at: YYYY-MM-DD, retired_reason: text)
---

## Now
Up to 4 lines: what matters with this client right now, for the next agent.

## Streams

### example-topic — Example stream title
status: open · since: 2026-10-01 · last: 2026-10-01
State: Current truth in 1–4 sentences, rewritten in place each time the stream moves.
Next: What we're waiting on / who owes what (omit if nothing).
Refs: https://mahifx.slack.com/archives/C0000000000/p1790856000000100

## Arc
- 2026-10-01 — One line per relationship-level milestone
